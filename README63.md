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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f694e09-327f-329a-97ea-672e2676342f | -2.61748 | -54.38305 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c417b93-c8ba-3757-841f-59532753ae04 | -3.08642 | -53.26339 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e7d6e7b-9a95-35f4-9ff1-4e9f318a4c72 | -4.00419 | -54.33967 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b8fa7b3-8304-3887-9898-33fe078eb4e5 | -3.19002 | -48.5787 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70e65a43-e16f-3984-8bf1-e4867c4066c7 | -3.90817 | -45.08854 | 2024-11-21 04:55:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f300804e-2c2d-3c48-87de-1fc9d8cdee1c | -3.06282 | -53.28435 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b291e735-6a2a-396d-b711-5a3f7b4e34a6 | -6.31811 | -49.68063 | 2024-11-21 04:55:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e05f2ed-25e4-333e-8f9c-27dab2de4830 | -4.18141 | -53.58288 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd58f783-c72e-379d-bdbc-6e2d111dd876 | -4.13746 | -54.33531 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dbabfd1-77b6-3aff-b314-cf8ffbfe6cec | -4.15486 | -42.02596 | 2024-11-21 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7e193a02-1d3c-34af-819a-4cbc1e548ac8 | -2.96788 | -52.37247 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d538ace-96e2-3b45-b282-ce220fcb2e45 | -3.08643 | -54.55729 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75b92124-3a85-3f1c-92cf-c02a6ce625fa | -3.36129 | -51.05169 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21ed7e49-9ea6-327e-9c93-57f1af823a69 | -4.29728 | -54.09856 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8caf501a-9181-3a76-9203-29b21d558ece | -2.71414 | -53.16974 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c398a532-315d-341d-a251-b38d10588566 | -2.85082 | -54.00551 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1231544e-1552-302a-9fa4-df83ab167e48 | -3.09783 | -53.21236 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00477b95-ae96-33f2-9e93-fa476e59d698 | -3.18974 | -54.76622 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec5d3d7-b171-3873-b208-a28c9cd31fc9 | -3.61357 | -54.74862 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaf98769-77b2-3bfa-8410-fdbc0a930a69 | -2.50753 | -54.24343 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e7fa4cd-3063-39f6-b5c7-f844b244eabf | -2.62922 | -54.26993 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af7eeae5-eb99-34cf-b871-ba0c38de0f76 | -3.38242 | -52.45798 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 78257978-4678-33b4-aa5c-b8d3db9e968e | -2.78788 | -54.03827 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b324ee0e-5f3b-3964-9a57-ccb382fa9c06 | -3.71247 | -51.8431 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 168fdf1f-d349-32a6-8f76-e2bd7bda36eb | -3.10903 | -53.09792 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7730d59-776e-39b9-b3d6-f3a93ab43caf | -6.18246 | -43.41512 | 2024-11-21 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ad7864-6f28-319c-a2a2-5bb3d288a70b | -2.90177 | -53.05466 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2831e7dd-c321-357b-b9b4-a53d515accef | -3.25893 | -50.39511 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca31ebe9-ae3e-388c-856f-38780b1d9507 | -2.37083 | -53.83795 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81e47c71-8827-3aa8-bed3-8166b412388a | -3.68595 | -50.21698 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cc51dd0b-79bc-376b-b911-5cc1a9f68137 | -3.71527 | -49.42602 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3ba06db-fb8a-3841-b06b-da4b4fc2adb2 | -2.83582 | -51.82482 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c73abf-5a1b-3224-a794-76a07b9cc2f2 | -3.42922 | -54.60421 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc5d296-e050-3850-9d24-2935b2fc7d01 | -4.17263 | -50.40844 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d350f0e-7e8d-3d75-a302-11414328fcd5 | -3.92747 | -51.17831 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c82acc2-167f-3a20-a08a-7e5302ed5de8 | -2.91061 | -53.06309 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffe58019-28e4-3dd6-9d01-392285f97587 | -3.50891 | -50.22646 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e14b9c8c-f472-30af-b90c-54c4f0e6bb1a | -2.59669 | -54.00091 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0201e7-48bb-346f-9ecf-acc503611341 | -3.10373 | -53.73742 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d51acd-da08-3136-a841-78bdf71a9c75 | -2.36698 | -53.8409 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61bc7998-c52a-31a2-b1c5-1189eec05c9e | -3.45665 | -51.66216 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 231b73df-ad78-3e32-99b1-051255b5c8d8 | -3.66777 | -54.27583 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6550ab5f-c5b8-3e4e-bd0c-4f852e18f30e | -2.53316 | -54.01558 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46be2392-a3f2-3fd8-bc28-adebd2cbef21 | -4.88297 | -50.94131 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 110c02ae-8192-3330-9a4a-240d7276ce68 | -2.77072 | -52.11084 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5425b57-88c4-345b-bb0b-0505af348633 | -2.92547 | -51.45013 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75441e7e-28c6-343b-ac8c-6556b250f53a | -3.48559 | -51.47723 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf1ac454-1608-3ed5-9301-3167066bb652 | -3.19365 | -54.32995 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d28e7d9b-7489-3997-9a39-d715e50b7013 | -2.95014 | -53.72069 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 690ef005-3a20-3fbc-b889-178510d62188 | -4.60968 | -48.80323 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b2806c-4a73-3245-8b23-cb9c3f9a74c4 | -3.75278 | -52.32759 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94c73b9b-60ad-391c-bc8e-77f429489f6f | -2.60174 | -54.05506 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b45852b3-3c7e-3608-9cbf-851da687d7cb | -3.80181 | -51.26554 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73a7f2c8-c065-3c22-933a-36b7a5fbaef1 | -4.40829 | -45.95817 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3e9f972-8e48-379e-9dd4-fa2b206262e1 | -2.59563 | -54.02915 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba5a2ad9-f572-3690-8276-390f8ed37ff2 | -2.95817 | -53.86309 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51229def-7e6a-318b-984c-dcd40ce5448a | -3.24895 | -50.55606 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3718c209-0ac1-3b11-bcc0-dfafbf0b2bce | -2.26902 | -53.75129 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fb05944-c377-3c85-9bfa-be5e863be940 | -2.81053 | -54.02404 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cde2ec47-8315-315f-9ab8-af74ac373ad8 | -2.37254 | -53.65451 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07358a5b-65d6-3172-bcf5-a68871661caf | -8.589 | -50.97988 | 2024-11-21 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae7452e-d745-3731-884d-dfc6f799ca02 | -2.92329 | -53.06857 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4a9375e-c5ff-31c2-b66b-d8cce489c78b | -2.76292 | -52.11689 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1f8f5d9-0a96-3e3d-b625-2764bc68d289 | -3.11191 | -53.70698 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8faede17-1b03-3cc7-9668-3688fa2d5074 | -3.06913 | -49.20168 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a062894d-a865-3e1f-8098-40a5c03e1976 | -3.05197 | -54.40779 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49438ba3-2a12-31b3-bacb-a8ec902cfe77 | -3.28631 | -53.82983 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d3da0aa-d0c5-3f8c-9dc4-e9dca3474fff | -2.33517 | -53.93525 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b672315-db49-345a-9c76-89eef530bd2f | -2.80003 | -54.02596 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47f04ac0-4bcb-3cc8-aeaa-1e1ed0f6ab71 | -3.54767 | -51.43654 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c32142e2-665c-3fb4-a0d4-b3432793fad4 | -3.27807 | -53.83913 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf48d51e-942e-3697-a5b1-072950c26544 | -2.84964 | -53.96988 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37f2c8c2-f604-37cd-bdd2-732e62c32d7e | -4.05291 | -54.37547 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee23ee2-bf85-357b-a3ec-826384f125bb | -2.89496 | -54.00537 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d919f7c8-5bf5-34db-8539-0f8332e76000 | -3.28246 | -53.83276 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1013e6c-48cb-36fa-8b91-737cd68d8baa | -3.00789 | -51.30257 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e541ae8-32b1-31d6-b373-1356bcfeb690 | -4.18195 | -53.57944 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78afac7c-177d-3b7d-b04a-6e203883d972 | -3.4713 | -50.00872 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f5ef76cf-5db3-3867-9e7d-6cd97ef723c3 | -5.95178 | -44.4646 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33b31748-39c2-3709-b8e9-8409cf3db908 | -4.17918 | -53.57549 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99b3d373-a9fa-3c4f-8781-8c13c32f06d1 | -3.06559 | -53.2883 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0d550fe-4184-308c-93db-3216f5e59f11 | -2.96153 | -54.16504 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08d05414-c317-3c84-a536-f5f771b628ec | -3.75985 | -55.57374 | 2024-11-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f245eea5-d08e-3d1e-ac32-778b10b5a73b | -4.38544 | -47.76142 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99d8d6a2-cb35-34b2-ad62-c1f0da23ba2b | -2.58896 | -51.71768 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 082806d4-13c4-3986-b7f6-016560a5851b | -6.81663 | -46.77624 | 2024-11-21 04:55:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f5c0227f-e3d5-39eb-a015-19655748f8d5 | -2.74693 | -54.01735 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b12163b6-db3a-304c-98ba-208b1412b193 | -3.29243 | -53.85548 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a18ef14-9b42-3d20-bd55-0a75071933c8 | -2.45451 | -53.69587 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37c15263-68c4-3b41-b962-7f66cfde4779 | -2.7477 | -51.82677 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a63cc8-1189-3741-9dbc-d6803c79cf51 | -3.21989 | -53.84026 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af766098-1971-3ccb-ad96-12df2d5b0bce | -2.60893 | -54.05261 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d773aaf-ebf6-3778-b1b7-ff3469fc569a | -6.20229 | -46.22264 | 2024-11-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b55f2350-d632-36c4-badb-ebcfacd9e674 | -3.41852 | -53.29075 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b044c47-0383-3512-a88c-a26a5ceca72e | -2.59011 | -54.04257 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 214a4976-8d91-318c-a03b-624bb6c2888c | -4.58038 | -48.01479 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6970bc3-afa9-3d0c-93fb-4e9285fdbc39 | -4.57981 | -48.01871 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513baebe-ed7a-3f36-9674-ff4245f58a25 | -3.28083 | -53.84309 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8df069fa-fff8-3b10-8737-13b7b57a75e2 | -3.33735 | -51.16192 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d08040e-4fc7-34be-ab21-f8d905f94805 | -3.29148 | -49.19098 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |


[Clique aqui para ver as próximas entradas](README64.md)
