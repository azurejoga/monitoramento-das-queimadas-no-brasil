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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 429811a2-9634-3c44-a6da-2a6d298156f5 | -10.02816 | -53.47055 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| e4485a6d-3b60-3c46-b3fe-6a8bdb89752e | -10.02744 | -53.47476 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 1247c6b8-c158-3987-ba4a-b3208e9f26fb | -10.02602 | -53.48319 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0ded587-3456-3b5e-93c5-efa7c9bda2b2 | -10.02384 | -53.47412 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a26d1f5-d255-3701-a882-15505099b5a5 | -9.73 | -53.19689 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8be6f397-deff-3339-811b-cf51d18e7af3 | -9.72933 | -53.20104 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eddb954-1fdb-3414-8d87-c0dcc5148762 | -9.72643 | -53.1963 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b241d07-fb8a-3349-8d22-95e7585b969a | -9.72575 | -53.20044 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69a310b1-1906-3650-8bd8-a4236cde981b | -9.72218 | -53.19984 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 453a9780-86c0-3c19-b884-3bc3eee1e128 | -9.66213 | -53.18565 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 851c3cc7-af8a-3956-8e12-da9737c47f7a | -9.65429 | -53.18859 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 461b4fbd-7780-32d5-92b4-4b6350cdcc48 | -9.64796 | -53.20448 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b33ef4e-0fd6-351c-8992-b4ea7038fa74 | -9.64727 | -53.20861 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 684c8356-3f3c-3fc0-ba88-69c7b1c5de70 | -9.64576 | -53.19569 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79e3ce75-c940-3084-a21d-301eeac7072b | -9.64507 | -53.19978 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b8ebfc0-a0e3-3766-9929-95b78555f0cd | -9.64438 | -53.2039 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd0d3cdc-1971-30d2-8df2-e3a13b90e648 | -9.63583 | -53.21102 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e28f0e6-bec6-3cce-8904-e813c5757eec | -9.63514 | -53.21515 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3282215-4e91-37f1-80cc-2a98a7c2f9c4 | -9.63156 | -53.21457 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c0dd0f1-163b-3733-a9fa-4f25526be7a9 | -9.62947 | -53.22697 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e589a7a7-b7d9-3f51-bc6d-7cd56f2d9acc | -9.62658 | -53.22225 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 066630e3-8e03-3a2a-b439-85723e3f78be | -9.40328 | -53.19653 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3ca3725-d59e-3421-9504-30e8e5228972 | -11.0771 | -52.49744 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59aa0be1-0b09-3f90-a383-904c3aae0b12 | -11.0743 | -52.49308 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1f7be7d-864e-395a-a9bc-8eaaa746a053 | -11.07368 | -52.49687 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67c0ea06-1fca-337a-a7f9-386f0a27cd48 | -11.07305 | -52.50066 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea8a0488-f1bd-32b6-ba50-3ad39461cb91 | -11.07025 | -52.4963 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07ecce45-194c-3044-9cfa-2c31bcbc1575 | -11.06963 | -52.50008 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a0ab83c-eb77-3422-aceb-a08111f69e89 | -10.82073 | -53.73606 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 972c0fb9-7ab3-3b10-8b14-10844150c8a8 | -10.82003 | -53.74029 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e726de5b-a7ca-3800-9baa-ec2bf1964233 | -10.81711 | -53.73545 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee76e69-5646-3328-b772-0a591f880f21 | -10.8164 | -53.73968 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ff3595-acff-3a8d-8345-f5ff5a11d916 | -10.77617 | -53.53793 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b6f5f83-58ef-39b6-8c53-efc83e5f47af | -10.77258 | -53.53733 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2e8411c-4c40-3eb9-94b7-ca84b6c08c6f | -10.77187 | -53.54151 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bbaa289-c626-3814-83a2-e1e0f3356cff | -10.7705 | -53.53815 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14c28abe-3bc5-3668-b4a9-3d6d98246d82 | -12.26124 | -53.43905 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75c160b2-fb44-33d7-94f9-c97801e58937 | -12.65104 | -53.21111 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 806c8aab-f53e-34f6-a32a-dd5c2c85dacd | -12.63655 | -53.2126 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d493b2c-193a-3d40-b3ed-cc38b6b0f93b | -12.60861 | -53.18775 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2cc63d2-39fb-3a80-aab6-5ff3612d484e | -12.60796 | -53.19165 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b542741-0633-3ab5-9349-8e5c4108803d | -12.60709 | -53.17548 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82ca24be-971e-35f1-9667-237913a33477 | -12.60579 | -53.18326 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91f22260-ec16-31ab-9a2b-4e4ed2057e17 | -12.60558 | -53.16322 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3a2ae69-0cf4-3105-8246-bb9b023c3bce | -12.60493 | -53.16712 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8658bb3e-3fb3-3694-a73c-439a8a7600bb | -12.60428 | -53.17101 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6afa26a-93a3-30c4-a141-e89682656ce5 | -12.60363 | -53.17489 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce423502-4132-35d6-b320-795bcfad0276 | -12.60276 | -53.15875 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c39b077a-7320-370b-94d2-ce824a96a1ba | -12.60211 | -53.16264 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33c8ffbf-5662-336d-b31a-aa406008db7c | -12.60147 | -53.16653 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca32c0c2-9ecf-3e5d-86c1-6ce7765099f3 | -12.60081 | -53.17043 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b964fcd-c259-34a6-a42c-d0ca3f7eaddc | -12.598 | -53.16594 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08dbe816-1925-3e78-99b5-6a858adf70b9 | -12.59454 | -53.16535 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b80a2f45-6a68-39bd-b3f9-3d8c529234ad | -12.59239 | -53.15698 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c626290-14a1-3548-9fec-caf063cfa9af | -12.59174 | -53.16086 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c10c006-b0bf-3ee4-8522-c36d36861626 | -12.58893 | -53.15638 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3ce1451-1e6d-374e-a11f-ee4a03652019 | -12.58828 | -53.16027 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55bce229-837b-36e3-94d6-5e7bea839544 | -12.58762 | -53.16417 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6668779e-8837-3d31-a109-48f4ebde4a8f | -12.58482 | -53.15968 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ff2939b-9d9a-3931-bd7c-126666580fdb | -12.58416 | -53.16357 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c6172c5-5d3a-37ff-bb83-f4c2a9501b0b | -12.58136 | -53.15909 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e2af702-c13f-3574-91fc-bb7540cd488f | -12.5807 | -53.16298 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d27044d7-5f11-3ecf-96cb-ba3b83b90565 | -12.57724 | -53.16239 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 210226e8-9cd9-303d-a5d4-adecf2e9cce8 | -12.57501 | -53.16261 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 855ec6d9-aed2-3030-b22e-092387bead63 | -12.57313 | -53.16569 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c261873-b91f-3f2b-bdc8-017cfd150f24 | -12.57155 | -53.16201 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ae00c88-7f9f-3b37-9f65-9913f4e4b451 | -12.57092 | -53.16591 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a41676f-7bc9-3695-abbb-d8cdc8b9c7ae | -12.5495 | -53.16626 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59f16097-91ee-315a-861f-a6081f672892 | -12.54733 | -53.15789 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37548f07-b420-358a-91cb-ba2ad4aa7232 | -12.54668 | -53.16179 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e7f30b-6dbe-3413-840a-a14e12c6fad2 | -12.54386 | -53.1573 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65897d0-2c51-308e-ae9b-dd5314ecba12 | -12.54322 | -53.1612 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b6667cf-a99f-33e8-9e44-8ec94f147c5f | -12.5404 | -53.15671 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c45e72c-0cf9-3f5c-9ea2-20b8c48482e6 | -12.54001 | -53.18069 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0de0aa9-2f0d-35a4-83a8-f4eaa8c80243 | -12.53976 | -53.16061 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05778954-44b3-3b53-a462-ab271cd94073 | -12.53936 | -53.1846 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee966020-7764-34cc-8891-5f61f295fb87 | -12.53694 | -53.15612 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 353e1d85-2ce8-3450-81cb-49292eedc04f | -12.53654 | -53.1801 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c515ad00-4c51-3dad-b64d-c1c83c869fd2 | -12.5363 | -53.16002 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4233047-39b9-372e-bdaf-feef799b5bee | -12.5359 | -53.18401 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb6e2873-295d-31d3-9d94-229a81511ad4 | -12.53565 | -53.16392 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c812a729-a66f-3b59-97d4-2bb0583760bb | -12.53372 | -53.17561 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00c74be3-5fba-3007-9d03-fb5b6dff23b3 | -12.53308 | -53.17951 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa81c1ed-77aa-3cea-b1dd-d23adfd7c953 | -12.53243 | -53.18341 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a12b8964-2376-38f7-b9ef-0182b9341d03 | -12.53219 | -53.16333 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e063d293-5052-36ee-a4b9-ccdec9d2eb57 | -12.53154 | -53.16723 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dd8991f-263c-30f3-addf-75fc11348282 | -12.5309 | -53.17113 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 026b35de-9a38-3680-b3a4-d9f0b021b13a | -12.53026 | -53.17502 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4943caa6-6d2f-38d0-b681-b373cf8af9c8 | -12.52961 | -53.17892 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e3851f9-c87f-353c-800b-54c6bddc4f34 | -12.52615 | -53.17833 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80f070ca-f9cf-3bff-9c37-aba8df144dda | -12.52268 | -53.17775 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32e7e2d3-ee7c-3376-ac76-6e06ee462c33 | -12.51922 | -53.17716 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aad76718-4565-37f4-918f-d811e806e44b | -12.51792 | -53.18497 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a6cfd03-12c4-3c02-879f-d2eea7ff325b | -12.55639 | -53.5 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c0d746eb-a357-3e8e-8b6e-891615920022 | -12.55572 | -53.50402 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ac67946-9a38-3f1d-a149-8d6f03e5bc36 | -12.55288 | -53.4994 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e74ac6e4-e6c7-3259-bd9b-bc674ff1a5ca | -12.55221 | -53.50342 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63247b99-ba03-310d-af25-9a9feff99d0c | -12.55005 | -53.49477 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7953deb4-3afb-33f5-9c6c-13985d3fa599 | -12.54937 | -53.49879 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64b0074f-d88c-3f78-a2e2-5206e6cc32de | -12.5487 | -53.50282 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README98.md)
