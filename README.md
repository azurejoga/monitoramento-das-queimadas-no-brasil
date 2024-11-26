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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 278cfe3d-2e7c-3b81-94f2-7fd3c6f089c9 | -4.3232 | -47.5039 | 2024-11-26 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ad195eac-75be-3e67-9911-7d3493a1201e | -2.8013 | -53.043 | 2024-11-26 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b4fe91a8-94b5-31d9-a76f-888c9b1a11b4 | -2.8163 | -54.133 | 2024-11-26 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 462fd365-75c6-35e8-92bc-bbb3326e240a | -4.3231 | -47.5258 | 2024-11-26 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3b019633-7dfe-3f3a-91a9-5fa9c8992828 | 2.6718 | -60.4304 | 2024-11-26 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7bc78772-677a-376c-a5c1-2856be55b5e1 | -3.6041 | -50.3991 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 3ac2d9cb-f2fc-3300-bbbe-794e0ab588fc | -3.9265 | -42.4246 | 2024-11-26 00:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 77eb1ee4-85d8-37f6-9d98-937b8361f12d | -2.178 | -45.9758 | 2024-11-26 00:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| bd563447-fe47-3e95-b089-49715282d97d | -3.2907 | -50.2627 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d72c173f-0d04-36d1-bef6-1ec56264a41e | -17.6453 | -57.5874 | 2024-11-26 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 7ab83bcc-761a-3c5e-afce-c75695f26630 | -3.3937 | -44.1951 | 2024-11-26 00:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 10ba2d0c-027a-3b58-b6fb-49fd344c9c3e | -2.4954 | -45.4303 | 2024-11-26 00:00:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 39b7ecee-e3c2-33f1-9e4e-a4fd3a0cd883 | -3.716 | -50.185 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 70a483f2-b6f2-3dc5-afe3-dbdd1a95fc9c | -3.5857 | -50.3787 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 204.6 |
| e0fdbf48-dd02-36dd-ab71-c84992d8bbfd | -3.3752 | -44.173 | 2024-11-26 00:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5939bf96-a6f9-3dd8-900b-4dc3e9daa566 | -4.6547 | -47.9444 | 2024-11-26 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| ff066840-7f04-3747-873a-98fb06755bd9 | -3.2419 | -53.2954 | 2024-11-26 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9f9ee46d-1872-3640-92fc-86db8b7f564f | -3.242 | -53.2751 | 2024-11-26 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2cd48ffa-88b7-307f-ad20-2cf063225421 | -3.6042 | -50.3781 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| ab75f80e-b44a-3b96-908f-95d011718a08 | 2.6901 | -60.4301 | 2024-11-26 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 81eb09cd-ca90-3083-9785-4aefeba1235b | -3.2906 | -50.2837 | 2024-11-26 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d46970f7-9364-3db8-9337-c3d393eec19d | -4.6732 | -47.9651 | 2024-11-26 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2570447a-1f7c-3ba8-a10c-49dea1ffca24 | -3.5858 | -50.3577 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 43955be1-5eb8-3d82-a358-f58a36850391 | -2.8198 | -53.0222 | 2024-11-26 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3671daf0-c492-37bd-ace5-e50acb027f5d | -3.9078 | -42.4256 | 2024-11-26 00:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 250.0 |
| 857c8b10-2d1a-3f9f-a3dc-c4fdb3f9c2ff | -2.8014 | -53.0227 | 2024-11-26 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 7edf5ad9-4c17-3df8-a408-4e4736f6f9eb | -2.8014 | -53.0024 | 2024-11-26 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9b05428a-ebf6-346e-83b3-cb8109b77639 | -3.3938 | -44.1722 | 2024-11-26 00:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 1a6a59d7-40f7-3e33-9b29-9d19792eadf1 | -3.9267 | -42.401 | 2024-11-26 00:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| f2879915-0abf-3ddd-ac22-eacd2b71a015 | -3.3939 | -44.1492 | 2024-11-26 00:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| fe93e917-3c32-3962-b49b-e120782a5b78 | -2.4955 | -45.4079 | 2024-11-26 00:00:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2a88d334-e4fa-3f25-b150-3eb4a5323ed3 | -2.8347 | -54.1125 | 2024-11-26 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 5088a3db-5ce9-3683-99ff-f03696038eac | 3.8257 | -59.5896 | 2024-11-26 00:00:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 1c63569f-33d0-3366-bd91-02af9dd8bf9b | 2.6901 | -60.4111 | 2024-11-26 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 53219ad4-a58b-3ac2-b31e-1fd35170d6be | -3.908 | -42.402 | 2024-11-26 00:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 175.5 |
| c0a49bec-29db-314e-8e3c-a9076e5e782f | -4.6733 | -47.9434 | 2024-11-26 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| c5427e9e-d487-3e80-89cc-150c25a33b16 | -4.9486 | -45.7904 | 2024-11-26 00:00:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 16d7a57b-adf0-3c8d-b66c-d0002db71c0a | -2.1173 | -54.6671 | 2024-11-26 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| caaf78d2-da02-38de-a99f-ca676304dc42 | -2.8163 | -54.1129 | 2024-11-26 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| da24386d-3f19-3d5f-a1e0-8a148f3219d9 | -3.5856 | -50.3997 | 2024-11-26 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 293ff8e4-815c-38ee-8b96-5910daa281ec | -4.6546 | -47.9661 | 2024-11-26 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f714cc51-6cc1-3cff-b0de-cbf87a23026d | -3.16 | -48.42 | 2024-11-26 00:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6de379a-b535-33e0-8265-29e8f92fef5a | -3.19 | -48.42 | 2024-11-26 00:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02968b8d-ab3b-3a27-bfb0-49a2ae0902f5 | 3.8257 | -59.5896 | 2024-11-26 00:10:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 362aa5c9-07a4-3a6b-948b-dfaa67f1611f | -3.3938 | -44.1722 | 2024-11-26 00:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 65c1ad7d-d94d-3443-a96e-4df7ed959ba3 | 2.6901 | -60.4301 | 2024-11-26 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.1 |
| cbdca5e9-d006-354e-8e4f-5d8182ab4682 | -3.9675 | -48.0634 | 2024-11-26 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 90008d3b-508b-3fc4-8069-5da391940b3b | -3.3937 | -44.1951 | 2024-11-26 00:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| dbae615c-93d5-34bc-afd3-fc8cc5cbc1cd | -3.986 | -48.0626 | 2024-11-26 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 23dadb0c-0370-39b8-a771-69f0a5b9bfd2 | -4.6547 | -47.9444 | 2024-11-26 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 2da59a48-7d5e-3685-9fc3-07443bfc1bd4 | -3.242 | -53.2751 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8838cdc2-2bd5-375a-998d-5181148577a8 | -3.3939 | -44.1492 | 2024-11-26 00:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8b1951d6-0a02-3c53-898a-23b248635e44 | -3.2907 | -50.2627 | 2024-11-26 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ca0f40a1-7e70-3a47-96a4-82a31f163ef3 | 2.6901 | -60.4111 | 2024-11-26 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d336ddb2-4e62-3b2b-9c27-3819cc866cc4 | -2.8014 | -53.0227 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 2cc7ad47-76a3-3750-bffd-b5f6bd4c8912 | -4.6733 | -47.9434 | 2024-11-26 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 7988ddfe-c0e0-38cf-91ad-78e11fa2022c | -3.6041 | -50.3991 | 2024-11-26 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| ea656dc4-717a-3cd1-b892-9f2fd15dba75 | -3.5856 | -50.3997 | 2024-11-26 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| c38b6274-d8af-3b31-8766-dc64d1bf5adc | -3.3752 | -44.173 | 2024-11-26 00:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 45a644ef-483e-3d7f-bac2-c77878efea45 | -3.9265 | -42.4246 | 2024-11-26 00:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 268fffdc-0db1-37b5-9750-4d3320ed3d23 | -2.8014 | -53.0024 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 12f09270-fd6d-391a-9480-a7ab3dfb79d4 | -4.9486 | -45.7904 | 2024-11-26 00:10:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| db25d0b4-de9a-3ce6-a5d0-a43533b6679e | -4.6546 | -47.9661 | 2024-11-26 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0100d07f-a137-3d6e-b101-de7820f0cfe7 | -3.9267 | -42.401 | 2024-11-26 00:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| fe610047-7564-334b-98a3-30e82895c962 | -3.5857 | -50.3787 | 2024-11-26 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 199.8 |
| 541c7b10-f381-3e5a-b2ff-7c134f0a3834 | 2.6718 | -60.4304 | 2024-11-26 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 534b6573-3f3a-3b6f-94e4-003cbafdf4a5 | -3.2906 | -50.2837 | 2024-11-26 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a760c3ba-96ca-3bd2-a4a8-1daf4bc481cc | -3.908 | -42.402 | 2024-11-26 00:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| e6e58858-6fb1-33e5-a0b8-6a248125ae9d | -3.2603 | -53.2949 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ddb5b9f7-ab41-3152-aef8-111490178234 | -3.6042 | -50.3781 | 2024-11-26 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| e40faa1a-faac-3238-a7a4-bafafaabd0f0 | -2.4954 | -45.4303 | 2024-11-26 00:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c29b8c28-fafb-3be5-aa67-54485f9fd6b1 | -2.8198 | -53.0222 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 88af6e4b-3e2b-3a45-8a01-59c66a150152 | -3.9078 | -42.4256 | 2024-11-26 00:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 194.8 |
| 2796c04a-6b7e-3eb0-a9f0-d97089bb6bff | -17.6453 | -57.5874 | 2024-11-26 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 78e84579-8132-3f00-9575-27fd120613b0 | -3.2604 | -53.2746 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0ce7ed74-64d8-3e09-ade1-ae213c5c9d23 | -3.2419 | -53.2954 | 2024-11-26 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e3571970-189d-3046-a472-f31a4686f9d4 | -3.8691 | -49.1415 | 2024-11-26 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0076e209-55c6-36cc-b78a-e74babfc44ca | -3.986 | -48.0626 | 2024-11-26 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7638865f-a833-3558-a02d-6e2ee649ba23 | -3.2907 | -50.2627 | 2024-11-26 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6c3813e5-2cbc-3730-aede-056e38bd1607 | -3.287 | -51.1609 | 2024-11-26 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7fc20a9f-7aac-3b47-8efd-ac0ba2395b25 | -1.791 | -52.7376 | 2024-11-26 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d29039d2-19c3-32ba-95f7-c2d1250e6129 | -3.9078 | -42.4256 | 2024-11-26 00:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 176.2 |
| 1ffd3b92-bf43-3de4-bcd4-12719436e4b7 | -3.3938 | -44.1722 | 2024-11-26 00:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 5d5e4887-3117-3135-937b-54ff0f5c6d9b | -3.9675 | -48.0634 | 2024-11-26 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 12c7100e-583c-3262-8379-9408d434b4bd | 2.6901 | -60.4301 | 2024-11-26 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 49c0c0d0-ec48-3f96-819b-3743580ef697 | -3.3937 | -44.1951 | 2024-11-26 00:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 1dfc3dd6-44f4-3bcd-b6da-35ae82875ccd | -3.8506 | -49.1422 | 2024-11-26 00:20:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 836866ae-dd61-3caf-ae5b-906e34a9f258 | -17.6453 | -57.5874 | 2024-11-26 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 8028b192-7a44-3edd-9dcf-e079dba967ea | -3.9265 | -42.4246 | 2024-11-26 00:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 163.9 |
| 3b285dd7-e3d6-394a-b52b-427a87d80d53 | -3.908 | -42.402 | 2024-11-26 00:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 69a311c1-9039-33ac-9542-b70af29fc297 | -2.8014 | -53.0024 | 2024-11-26 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 2a8fbc58-4657-3d23-90c4-dd803b348690 | -3.5857 | -50.3787 | 2024-11-26 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 224.2 |
| 53e17feb-d61d-3e37-9c8d-bf06d04aaa10 | -6.0676 | -48.0352 | 2024-11-26 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9afea850-0192-3cd7-8f4f-b631ef0ad027 | -2.8014 | -53.0227 | 2024-11-26 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 812d27d9-dd60-361f-8e3a-28e7d324c679 | 3.8257 | -59.5896 | 2024-11-26 00:20:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a701c316-262c-344b-8817-843d3c95d936 | -3.3752 | -44.173 | 2024-11-26 00:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| c957afcb-f8ff-377f-8c70-a37495cbd490 | -3.9267 | -42.401 | 2024-11-26 00:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| d9d06aed-41fc-39fb-8cf4-2fd6789ad9e8 | -3.5856 | -50.3997 | 2024-11-26 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| bbcf0aa1-1d95-3552-9935-b6fa15060215 | -3.6042 | -50.3781 | 2024-11-26 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 303.5 |
| 3e0286a1-b5da-3fa9-875f-32218bed370f | -3.6041 | -50.3991 | 2024-11-26 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |


[Clique aqui para ver as próximas entradas](README2.md)
