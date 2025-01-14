# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24e64bf6-9d42-3d8b-b0f0-f3431f713172 | 4.08105 | -59.94351 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 307470da-d5c6-388d-a2cb-905bbdf17b56 | 1.114 | -59.4583 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cee3a600-3b13-3e69-9b12-249ea1057f11 | 1.17317 | -60.50055 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b078c099-9f64-398c-bd8b-d806826c6512 | 1.32488 | -60.03684 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 68451df6-ce1e-3016-b663-ea8169d3825f | 2.42841 | -60.64742 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2e9c3ed2-4e79-3b8b-929e-6e56a1acecb5 | 3.10137 | -60.72845 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6074da82-e713-3d47-822f-224600593bfd | 0.63615 | -59.94588 | 2025-01-14 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd8bcc2-f838-3136-854c-5ab173c762df | 3.5863 | -60.84797 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc138f20-60c1-3d8c-8edb-9f195e4e68e9 | 2.0736 | -61.83861 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5addd983-6e0e-3ae6-86e6-0f6b77fd6fc2 | 4.00679 | -60.85923 | 2025-01-14 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c0ef41-8f1a-38d5-9b50-855486744a61 | 3.10692 | -60.72046 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8902c858-ed6d-30fc-9091-5f47b7ac6802 | 2.95688 | -60.18039 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 855894df-5a45-36ac-a47a-0e98a5b179cd | 1.32371 | -60.02945 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e03e7c-e72d-35e2-b4ff-152a4aea97f9 | 2.94737 | -60.18555 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 07c903a0-d4a4-3dea-bbc1-320f43644ed7 | 1.3283 | -60.03633 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 1552f1ef-33df-3da2-a151-ae6228254303 | 4.08161 | -59.94702 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab269c48-690c-3dd3-9096-3d63e734cea1 | 1.18159 | -60.4882 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0abedb6-0257-3f12-bdd3-79d1ef68c0b2 | 3.69008 | -60.05926 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44756345-4f4b-30a0-b0fc-a2ac67ff71eb | 1.31746 | -60.03418 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cb1a5c2f-3000-3011-9146-3abfc6dffd4c | 0.85137 | -59.54452 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eec649ca-fdf3-35a7-80e8-010a55b17a4f | 2.28343 | -60.21869 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e26fa50a-3230-39af-84aa-b454fdb9a387 | 3.59756 | -60.94176 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5becbede-7413-3e74-bf7b-e1ce979f3e15 | 1.09002 | -59.67961 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87802530-6da8-3ebe-8ed8-90f858a584ad | 2.94139 | -60.1826 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cd0565ee-1bc2-31c9-ba30-4470fcc7acac | 1.32204 | -60.04105 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6be1ba09-ca2a-3772-b62a-ddfb8e30157f | 1.93522 | -60.41184 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a8f984-e50b-3bde-8c07-f7c6458d7bbf | 2.18148 | -61.81071 | 2025-01-14 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e09069-2151-3cc2-9eab-0afffb377301 | 4.08497 | -59.94655 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e61cab10-696c-3dc3-9e63-4d7e70a6213d | 1.93859 | -60.41136 | 2025-01-14 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7306e1eb-9a48-3578-ae37-92af4729bf3d | 0.50417 | -59.34061 | 2025-01-14 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfd3ee0d-5503-3d6b-8d3e-cd38c5648cbb | 1.17597 | -60.49643 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1efed016-766c-3315-b9d3-15ab3339931b | 3.12074 | -60.72189 | 2025-01-14 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b4e84cf-4b5e-3712-9eec-761949141b0c | 3.59595 | -60.93139 | 2025-01-14 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a82a43e5-9085-3fe2-955c-94e65062d04c | 3.68826 | -60.06284 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa2d64f9-09bb-38d6-a0e3-b9641665adfc | 0.93475 | -60.32536 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b68feac4-b9d2-3194-b6a0-f3b639117fd0 | 1.32604 | -60.04423 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d9cfc9d7-18be-3ad0-aded-8d33d5dfa581 | 0.71249 | -60.11815 | 2025-01-14 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 856f4fb4-cc9f-31e3-98af-a768b13d1eb7 | 4.07041 | -59.91958 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ccd4eec-4000-368d-b52e-9cb3ce4bbfa9 | -0.11973 | -60.67648 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff007f65-bd52-3a71-950d-0ff64dac7c99 | 1.31135 | -60.42344 | 2025-01-14 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f0248fe9-fd96-31d4-80a8-1ced264e66a8 | 0.77759 | -60.53519 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be75c7ee-6932-3674-971c-278c68861b9c | 4.04167 | -60.19369 | 2025-01-14 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7abe652a-8a6f-3bb7-8111-316305f57d8a | 2.94624 | -60.17841 | 2025-01-14 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 08b38358-603e-3996-b9cb-c32a3987a81f | -0.11635 | -60.67595 | 2025-01-14 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 344747ae-368f-39a4-8965-70c0bd32c9cc | 1.3221 | -60.0463 | 2025-01-14 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 5f9fc7c1-c42a-37c6-bd67-a1150a44321f | 1.3403 | -60.0271 | 2025-01-14 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 48b0799f-1e5c-3a06-a147-ae73e12d8809 | 1.3403 | -60.0461 | 2025-01-14 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 09ea48bc-e543-3c94-83ff-1299d2565cae | 1.3221 | -60.0272 | 2025-01-14 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9f0ad010-c350-359f-9c5a-12acd0247601 | -28.78375 | -55.6171 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.7 |
| 0d523a49-7f9e-379b-b2ae-b7fd6b3631f6 | -28.77748 | -55.62362 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| 760ec3ea-1847-307f-ab8e-2c430d7e3f57 | -28.77727 | -55.61679 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.7 |
| c9e6787d-7d98-32f2-85b9-099249204d50 | -28.77809 | -55.61186 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 16.8 |
| 104b9a9f-54f2-3850-aa7b-6aa9619e2ba1 | -28.78364 | -55.63002 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| 0a8848a6-62ae-36fd-b168-f4e060a9e494 | -28.78395 | -55.62405 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| a0c0b380-2c22-349e-a7c8-7363c5629112 | -28.77147 | -55.60453 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 98f3b2d9-e392-3850-903b-dc2e0fefb0cd | -28.78427 | -55.61809 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 16.8 |
| 77d9c699-d2b2-3d14-bf63-d812cf28e918 | -28.78341 | -55.62304 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.7 |
| b69c0d68-aac1-326d-9843-5d81df37f839 | -28.77717 | -55.6295 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| ed5e84dd-1f0a-36ef-a007-1786567adf13 | -28.77761 | -55.61088 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 20.9 |
| 1f71160b-5ad2-33e2-8b1c-119b254ab3d2 | -28.77778 | -55.61776 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 16.8 |
| 23e5738e-50b0-346b-8731-b9e62ae42a66 | -28.77192 | -55.60546 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 5e09bd78-1e52-334b-8c94-53884bae6f27 | -28.78306 | -55.62898 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 29.0 |
| 8ea7294d-fc12-3e79-977d-2e2768c70331 | -28.77796 | -55.60486 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 20.9 |
| 4f3cf3fa-0e16-315d-91a7-3c7e5dbc527a | -28.7784 | -55.60583 | 2025-01-14 05:42:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 22.3 |
| 8dbd4e1c-5a8c-3fff-b60e-789ce60cafc3 | 1.3221 | -60.0272 | 2025-01-14 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 470d0337-c832-3f77-ab3a-a363a034ea6a | 1.3221 | -60.0463 | 2025-01-14 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 84611880-1596-35fe-8a73-2910f602aa65 | 1.3403 | -60.0271 | 2025-01-14 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e44e2c45-78da-343b-996b-203327d83fb0 | 1.3403 | -60.0461 | 2025-01-14 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 8839c2fc-ffaa-3edb-86aa-7c227b9ed44e | 2.95407 | -60.18827 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 284b70f6-2cc7-363c-90b8-bcf8d5358730 | 4.04128 | -60.19625 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46b10e4e-1e8f-3d81-a482-5ce5a84809dc | 3.10256 | -60.72749 | 2025-01-14 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| defc99ba-5948-3a30-813d-eae13039fa77 | 3.59583 | -60.93813 | 2025-01-14 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1498282-86c7-31af-8140-a5f1c1945bd4 | 4.08563 | -59.94917 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6919c73-a8de-3461-acb2-9328a9a82931 | 4.00655 | -60.8582 | 2025-01-14 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc29979-dfb9-3dd1-8447-28cad7b6730e | 3.59664 | -60.94315 | 2025-01-14 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac2bcb5d-718b-37d7-8b6a-b6f57dd51328 | 3.12146 | -60.72297 | 2025-01-14 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7d83ebf-4e74-39af-9c7a-ebf215b390ba | 4.00436 | -60.86154 | 2025-01-14 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5818807-fd39-3f80-945f-83cc9023bb3b | 4.04211 | -60.20114 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2028f7eb-618b-3397-86e1-59550c1d13dd | 4.19115 | -60.56348 | 2025-01-14 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d3c6f3a-3f5a-304e-a30c-3c03a86dcd1b | 2.9406 | -60.17607 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1e1d71cb-300c-39e2-9dc4-cf10e8ed2363 | 4.07051 | -59.91859 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d64126-77b0-31ad-a201-f297f778e2e6 | 4.07104 | -59.91789 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3243a09-8916-374f-95a6-d0027f8ec679 | 4.08482 | -59.94419 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b79792bb-018a-37d4-add6-9ac6cc664cb7 | 2.94148 | -60.18162 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e19a9fb-9ece-3831-8150-26f32dc79c44 | 2.94824 | -60.18372 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9c9ad9f7-bee3-3969-9e08-dafd3be9c66a | 3.68975 | -60.05778 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e229db-2bb2-30b3-a4b4-0b2a8d25c3bc | 2.94331 | -60.18459 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| af1dd18f-b9ca-327b-a19e-8b00c4e2c19c | 4.0864 | -59.94843 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc829646-ac53-3d80-abbd-761742031fb5 | 3.12073 | -60.71935 | 2025-01-14 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a35cc8b-3a3e-31a3-b5cc-75f145218bb5 | 3.69068 | -60.06328 | 2025-01-14 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c3ad91-ac9d-32b7-9ec6-a40957ceedc7 | 2.95717 | -60.17645 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 827076fc-3c2b-3520-81e6-8bfb76e43553 | 3.12154 | -60.72439 | 2025-01-14 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df1a10af-523d-351b-850b-600eee1479e1 | 3.5987 | -60.93974 | 2025-01-14 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10664687-8fba-36b9-b259-f0cce3fa7fec | 3.60048 | -60.93742 | 2025-01-14 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a12a2d44-1a25-3182-a1e9-f820f0aac6cc | 2.4299 | -60.64853 | 2025-01-14 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 211d4fbe-8f6e-306a-ad00-ff8d873435ed | 2.94732 | -60.17826 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 02c10f45-16cc-37c1-8c08-7710f31a6fce | 2.28301 | -60.21834 | 2025-01-14 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f9c64b7-6bdc-3dc2-ae30-455a23ec54d4 | 2.94239 | -60.1791 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2dcfb34b-437d-3b61-a28b-f4902b014d38 | 2.95808 | -60.18195 | 2025-01-14 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3607f378-c38d-3e85-8eb6-1d2dcb932d70 | 3.10649 | -60.72166 | 2025-01-14 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
