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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cd69896-c539-3e0b-b2e5-641d1c2c1604 | -11.83305 | -49.50123 | 2025-03-04 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95fd6cbb-9120-312c-8459-e799969ab1dd | -13.99885 | -45.60345 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92a1bc85-1705-3e65-8aef-82c5de30a529 | -14.01739 | -45.62242 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bc7ff67-256a-3ab2-8c28-5c2a78d3c7e6 | -13.98843 | -45.60184 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 854db46e-32a1-3821-8fe9-e08007a2637b | -13.99073 | -45.58609 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dd766db-3ece-3ab7-aa31-a67b037cc5e5 | -13.989 | -45.5979 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90492b14-7a13-3fc0-9b0e-252060d7fedd | -14.02317 | -45.63135 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1151e5f4-2a56-378d-b46f-710be2ee4814 | -14.01044 | -45.62134 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f7c491-1edb-307e-a128-ce141f068d97 | -14.02606 | -45.63581 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05ae7dc2-ef95-3c8e-9034-d4cdad53c567 | -14.01622 | -45.63027 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43e5f06f-8086-35c7-a274-6085dfd10c4a | -14.03301 | -45.63688 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91dc71ab-9d7f-39a0-bff7-a5fca6fa0483 | -13.98783 | -45.5816 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7421268-ec0b-3c34-9d52-f9bfaed2c338 | -13.99711 | -45.5911 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d59fe698-dfd6-398f-840a-dc96c5ac088d | -11.46438 | -48.00924 | 2025-03-04 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96e1156d-2ada-3937-a426-fc7f80d7927a | -14.02431 | -45.64759 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55e09c09-41c7-34db-8718-64a208a63064 | -13.99653 | -45.59505 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb8fd744-3cd6-32bc-8d30-763253647dbd | -13.22667 | -47.34669 | 2025-03-04 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c4fc99-f803-30d6-8060-3480a69a3b4f | -14.49483 | -45.32211 | 2025-03-04 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9ec293fe-40ef-3d87-bc08-f1ee41318098 | -15.56839 | -47.85461 | 2025-03-04 04:25:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 291f34fb-cb74-3c39-9110-c402009a2235 | -12.18931 | -46.70083 | 2025-03-04 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21318b41-6af4-37c3-9663-ee0fa1f7eb24 | -11.46495 | -48.00572 | 2025-03-04 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f58f17e9-8216-33c6-a3cd-faa45b88b729 | -10.53205 | -44.66733 | 2025-03-04 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64dddde8-a7ee-3398-af49-c8b984942ef0 | -14.02201 | -45.6392 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b12cffc-8609-32c2-af33-387250d99db3 | -14.02433 | -45.62349 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ffd7aa8-470b-3a9a-bcc9-3ff675cfb74e | -14.01681 | -45.62634 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d17f3d1-1dab-3faa-aa8b-0f3a0783b5e9 | -14.01797 | -45.61848 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c913ecd-db51-3ba3-8dec-af118bc7670f | -14.00639 | -45.62473 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed08645e-27ba-3e32-96b3-9b7ed8a7f779 | -13.99247 | -45.57423 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d60ff70-3fb3-3779-b8c1-5ae49605b61e | -11.82963 | -49.50065 | 2025-03-04 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d165059-6eff-354b-9485-845d07bc5885 | -10.53555 | -44.66787 | 2025-03-04 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c49829d8-7284-32d6-8d7a-fa07363a17a4 | -13.99421 | -45.58662 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13e3b578-eb2e-31ad-8e6e-3f746a02ab11 | -14.01448 | -45.64204 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24fe9962-30e4-35f7-85cb-b40248b04fcb | -14.0249 | -45.64366 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 579bd45a-ae30-3423-beee-764ee2862d63 | -14.00928 | -45.6292 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 479c905c-c15a-3fd2-9216-3d9d7c141ac2 | -14.02781 | -45.62402 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e46526-9108-3ba3-806a-7d1c5492810e | -14.02259 | -45.63527 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e27a0fb6-a6fb-3378-9c28-a90972e13232 | -15.07702 | -48.94385 | 2025-03-04 04:25:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d42badf8-9ddd-3962-9cc7-4a1e9f102f5d | -14.27873 | -47.41458 | 2025-03-04 04:25:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b9620ee-1226-3455-873a-7e05f689f06a | -14.0197 | -45.63081 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9256d5d-c0df-3aab-85b4-d82a253544bb | -14.03184 | -45.64473 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 574c7a2a-b2b2-3bea-bfeb-26f4c6fcd880 | -14.01854 | -45.63866 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8691f057-44e0-3a6e-aa6a-e4f815cadd78 | -10.53263 | -44.66338 | 2025-03-04 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f53b0f3-a870-3829-a05f-719f67554fb3 | -9.22984 | -45.02422 | 2025-03-04 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc599778-f07e-3de0-9aa5-a6e17f2ed481 | -13.99827 | -45.58321 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4cccc6d-7d2d-3c80-b296-8fb342a7da0c | -13.99538 | -45.60292 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55d0d219-0b15-3475-9e03-2e2c4b03ba16 | -14.01217 | -45.63366 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6602aa4-1f27-3c32-912b-336dff3a7e6a | -13.98725 | -45.58555 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efa4992b-6a09-3e7b-ab8f-65fa7da29302 | -13.99885 | -45.57925 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c045c3d4-73e3-3e1f-bbcb-d3872fcb515d | -14.02723 | -45.62795 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f36cfb4d-8bc0-30e9-85db-91e1ab7c231d | -14.01449 | -45.61795 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c50ec3f-6a54-3002-b67d-011cefe50ac2 | -14.02492 | -45.61955 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6412a5b-9c57-389c-95ec-230bbc494762 | -14.01565 | -45.6342 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c59e89a6-9bd5-3a80-9285-dff6b54ad66a | -13.99306 | -45.59451 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3c92b5e-3b6c-39cd-a982-815d72647b60 | -13.99596 | -45.59898 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d9c328d-0bd8-324e-b647-e0bc0ca011d8 | -14.02143 | -45.64312 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b6a3c34-de5f-38cb-b6cb-67a3c2023398 | -14.01333 | -45.62581 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f24a65e9-a626-328e-bb30-7324a4111b65 | -14.00986 | -45.62527 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86763837-3bc6-3705-a3c1-6d6a91e74741 | -13.9919 | -45.60238 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c386280-3672-3f66-8e75-1ab9c5366540 | -14.01506 | -45.63812 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 168dada4-61fe-37a2-9f6a-b0601c8a3634 | -14.02086 | -45.62295 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2bbb620-55ce-3c8f-b974-a38c81312717 | -14.02895 | -45.64027 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4187e911-c350-33d4-8f7a-b683c4a8788d | -14.02548 | -45.63973 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 862a7488-ce34-3bdb-89dd-6672ccc7e73b | -13.48178 | -44.03896 | 2025-03-04 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8238190-3995-3786-bda5-0e0236e7c98d | -11.46163 | -48.00517 | 2025-03-04 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bed9dbdf-5bac-3b8a-bea3-d0605dfad840 | -14.01912 | -45.63474 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4f77ed9-72a8-33ed-ad04-1269f551f509 | -13.99189 | -45.57819 | 2025-03-04 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dccd9a4-ac79-3c68-8caa-e6445a178c13 | -20.10288 | -43.9922 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 63ac967d-ca68-33d7-abce-c2f73c0087f5 | -21.44747 | -53.85241 | 2025-03-04 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c5d3c0e-7a2c-34dc-a417-06f80bb6d7a8 | -18.96736 | -49.20177 | 2025-03-04 04:27:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f57c85a0-f196-3f91-af16-667cf8c09c50 | -20.09387 | -43.99781 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c0fcacbe-02d8-37a5-b395-048f72fbaecb | -20.09343 | -44.00123 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad6a50d0-c35c-3648-9347-6af62b38b422 | -21.63132 | -48.67732 | 2025-03-04 04:27:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 059070ec-0c9d-3e5c-86cb-eee76fd6e503 | -21.60734 | -48.47046 | 2025-03-04 04:27:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20e11dd3-fe20-309a-8ee4-b3b6da7c2f4e | -18.15559 | -48.01868 | 2025-03-04 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c37e92a5-6976-39bf-9db8-e0b42f0251f9 | -20.09752 | -44.00167 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e26063b3-3d4f-32df-b133-350234bc1386 | -21.63286 | -48.68114 | 2025-03-04 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a0228f8-eb8d-3dd3-bacb-a3b8cd12287e | -23.4032 | -46.55739 | 2025-03-04 04:27:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12e8c8b7-fbb7-3ea1-a25a-fe26da718eac | -20.09518 | -43.98748 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 876b0adf-f208-3216-bd21-229a355ccb17 | -19.25167 | -49.07833 | 2025-03-04 04:27:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2adb6da8-4086-3f14-b321-aa9c5739affa | -20.09796 | -43.99829 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 0a2c9102-8f26-3ae8-a8d9-419fe1abdae2 | -21.6107 | -48.47104 | 2025-03-04 04:27:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e5ad56-dffd-3227-8525-5c40edb88c8c | -17.33439 | -53.73462 | 2025-03-04 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2beaf82-5f45-3f96-9ade-db42053b3be4 | -18.71595 | -56.56993 | 2025-03-04 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bdf71b2f-cae5-3444-b3aa-ce9138256774 | -20.73911 | -48.54153 | 2025-03-04 04:27:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6e8151d-c858-3be8-8c9d-820b4d13d58a | -20.31174 | -45.58377 | 2025-03-04 04:27:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb1b662a-d708-3806-92ee-94d821fa3dd8 | -18.00717 | -48.58921 | 2025-03-04 04:27:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70f4f171-fbad-3cca-b0db-59c888fbac9c | -20.96887 | -46.46348 | 2025-03-04 04:27:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bdc07c89-0e3d-31a4-a236-58ba42242658 | -20.10245 | -43.99556 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| e748775c-8da9-3719-b27c-05fe0ef8c61d | -20.09839 | -43.99491 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 10e66ad5-ffc5-3b25-b9e6-82a4f0802c19 | -20.92019 | -56.54317 | 2025-03-04 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d08e38b-1413-3902-ac1a-bc9fd763426a | -20.08976 | -43.99749 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| fda65d58-b945-33eb-9a52-7a478cb91170 | -21.66391 | -50.10835 | 2025-03-04 04:27:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55625067-51bc-3010-b6ba-1a186281d2da | -17.33739 | -53.74052 | 2025-03-04 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00a6ea99-a4f2-3542-ba41-0a406e32cf82 | -17.01371 | -46.424 | 2025-03-04 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 266e6e0f-e8c7-3f95-819a-ecff8e2ded46 | -22.90304 | -43.75346 | 2025-03-04 04:27:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3e41df77-9660-3cb9-b3d5-7635dab3708d | -20.09474 | -43.99097 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aa74483e-fb3b-39cd-9014-6533bc61df2d | -22.78675 | -43.75764 | 2025-03-04 04:27:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a2a7e955-70cf-333b-97bd-58e57ffced54 | -20.76385 | -45.57409 | 2025-03-04 04:27:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db38c05-475c-333d-ba40-750629675a5d | -20.82439 | -48.91897 | 2025-03-04 04:27:00 | NOAA-20 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9677a8d-bca1-3796-8628-37f84d1d8ee4 | -21.63564 | -48.68554 | 2025-03-04 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
