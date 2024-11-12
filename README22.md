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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e42a0a44-f9c7-38a1-b9a6-7a76ed95348a | -17.28743 | -57.31092 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 20376374-5f89-3643-800d-7d1db82dd6f0 | -20.1132 | -49.18731 | 2024-11-12 05:22:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e702907f-11c8-34e4-81e7-0d1e336d355d | -17.58456 | -57.51495 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8cc0a088-617c-34c1-93de-f936fdc34c3d | -15.96158 | -59.29185 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 785a85de-2f9a-354d-8b1a-d07639803fe0 | -15.95992 | -59.3275 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 645c045c-c218-31e9-9394-1234918bd962 | -21.32084 | -53.9257 | 2024-11-12 05:22:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 006af31d-73af-3103-bcf5-97a8a4b9bb44 | -17.58393 | -57.51978 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 2fa0f67f-fee6-31df-8b84-b55bb1b76462 | -17.25104 | -57.47262 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 26db8539-af24-3131-800b-3ebb012a4e96 | -20.32333 | -48.82563 | 2024-11-12 05:22:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03fae124-b8b9-38d9-8d0e-46014456d62c | -15.93659 | -59.34331 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2ba46a-fbc7-3726-b8e7-c940accafbe1 | -15.96045 | -59.29966 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d44bc7d8-aacc-3387-acaa-0fc16a944b95 | -20.32285 | -48.83192 | 2024-11-12 05:22:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b487daa2-a0f1-3ea5-b2e8-742a8915e4b2 | -15.96845 | -59.29292 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98dadbd3-9bb8-3119-86c5-b9e730884966 | -15.95189 | -59.31034 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 302fcac8-13f5-3941-938f-ef50cfda357e | -17.3056 | -57.49702 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1068fd2-0275-3b1e-8123-c1cccde871cc | -19.62628 | -54.15492 | 2024-11-12 05:22:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50cb909a-269d-3fd8-8307-7af320efbe9f | -15.92544 | -59.82063 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a2baf0e-c159-3d6c-8512-ac96d3fea7ef | -17.25038 | -57.47743 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fbf69863-7a08-35a3-9bce-a2f58e3d5855 | -17.26393 | -57.49081 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c2f713c2-cecf-3998-8657-99b72c3d2fcc | -17.25286 | -57.4876 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ccee14b0-95b9-31ba-b3aa-50cd0b9a3b18 | -20.32809 | -48.82534 | 2024-11-12 05:22:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2698c73-bcc8-3a9e-8985-058f89d26ac3 | -17.28857 | -57.47977 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5eddea74-41bf-34a7-b99f-47156fe66a67 | -17.293 | -57.47552 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f8c8f9b0-592f-3265-901a-e36b87723f1b | -15.99479 | -59.37631 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a0d0cb6-44bf-3cfb-a440-c37b7baaf179 | -17.27719 | -57.47808 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 05004ac7-3ed5-3f78-8caf-89b657086ce5 | -16.00906 | -59.37454 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 199c2327-9aa2-342c-adf4-f3efcd84b689 | -17.29364 | -57.4707 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1d42e6a1-fa68-36b8-bc50-5f43ca0057e0 | -17.58899 | -57.51067 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| da38c006-754f-35eb-9752-56ad9e087955 | -15.42118 | -60.28291 | 2024-11-12 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad9ee457-d276-3ed9-901e-ead5bf799866 | -15.95646 | -59.30299 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 87500c3f-dd1e-3a16-92b1-320c79f8c0cf | -17.24084 | -57.49071 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e2576977-a4a5-3468-b4f4-b3d6c2c5ff9a | -17.27656 | -57.48289 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0d382360-f65c-3e93-b2c7-0c6377e1dc6c | -17.60037 | -57.54195 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 0725fdd1-98c1-3e3c-a9cc-513025444fde | -15.95706 | -59.32305 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d408ab0-3536-3240-bc21-866e006b0609 | -16.0922 | -60.1119 | 2024-11-12 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff4f3b4b-0768-3a08-9219-6775c4c9f4f7 | -15.96501 | -59.2924 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4b3a3c7-2cb8-3eda-ac47-2bbba33f16e0 | -15.93317 | -59.34272 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c69075-b935-3507-b1c7-40b5bb73b597 | -16.00164 | -59.37737 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 789ed0cd-377b-3f78-9d5b-23ba64c109c3 | -23.95509 | -54.03991 | 2024-11-12 05:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e6d2aca2-fb95-3476-987c-e27c120eac3b | -23.95477 | -54.04321 | 2024-11-12 05:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d2630bc5-a21d-38fa-b8c9-b6bff8381291 | -2.1271 | -50.7121 | 2024-11-12 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4469547b-b6a8-3ef9-b7e3-f7791b741cb0 | -2.1086 | -50.7124 | 2024-11-12 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a605aae4-4812-3b3c-ad48-a51734dbb081 | -3.9483 | -48.1724 | 2024-11-12 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 87dea089-fcb7-3ae2-ab92-adbaf217c896 | -2.1272 | -50.6703 | 2024-11-12 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ca2ac31b-ea98-326a-8041-db85b9730619 | -3.9482 | -48.194 | 2024-11-12 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0fce7130-4c55-3d04-9241-b11d239a6f5f | -3.1097 | -54.2865 | 2024-11-12 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 714cdd49-3ad8-343b-8f9c-1228e48edb81 | -3.1096 | -54.3066 | 2024-11-12 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b83830fa-6330-3a11-a246-2887a1039d1f | -3.0913 | -54.307 | 2024-11-12 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 106f40af-afec-37f9-9043-7a5f7dcdd4ba | -2.1455 | -50.6908 | 2024-11-12 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8ba2dbbe-e5a6-36bc-ad47-98840f551125 | -2.1087 | -50.6916 | 2024-11-12 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0ed139db-234f-3efa-90aa-8dfb5cdc1c51 | -2.1271 | -50.6912 | 2024-11-12 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 31df99b8-c1ef-36d1-b499-00358b8859ef | 3.05664 | -60.52338 | 2024-11-12 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b5896da-0eb9-3e82-83e1-6d73686a9dde | -3.9482 | -48.194 | 2024-11-12 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 81bfdc2e-bce2-324f-b4ba-1e0862b3d20c | -2.1271 | -50.7121 | 2024-11-12 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ff409f7a-df84-3851-b332-b4c3bf338491 | -3.9668 | -48.1932 | 2024-11-12 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d5205e04-08e8-3c48-bd32-727f9fa48994 | -2.1455 | -50.6908 | 2024-11-12 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 12100ee2-f7dc-3207-b4e6-58046dc40c80 | -3.0689 | -50.3326 | 2024-11-12 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f0127b43-ccef-36d7-86de-561d49d66d53 | -2.1087 | -50.6916 | 2024-11-12 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e40fe387-e6fe-3600-a476-cc3d0bcf5ffe | -3.9669 | -48.1716 | 2024-11-12 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8ccf4123-375a-3264-8c3b-f229509edaf9 | -3.9483 | -48.1724 | 2024-11-12 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 067ca2b9-592d-3409-b36c-5c630fa1dec3 | -2.1271 | -50.6912 | 2024-11-12 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| d9594b41-b046-363b-9625-aca56ce87ebe | -3.0504 | -50.3332 | 2024-11-12 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 36397263-c8cd-3f3c-a81b-9c6de8d1125e | -2.62504 | -54.28964 | 2024-11-12 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38b84f0a-6578-36d1-8470-f835b52952a3 | 1.08389 | -60.59534 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24e07817-da32-3280-aba4-b5f95b8a84d3 | 1.06115 | -60.59062 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d517d0-47c2-3872-b1af-ce66524abef6 | 1.52921 | -60.674 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d12b51da-4ec8-3184-ad87-23945ad419f8 | -3.33753 | -54.18498 | 2024-11-12 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 885aed7b-ef82-3ba6-97cb-fcc4de3264ac | 0.62378 | -60.08695 | 2024-11-12 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bc8abff-c4cb-31c0-a5be-123696c61b73 | -2.12658 | -50.68804 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9fb1c361-b807-3921-9ee4-a53c4b89c398 | -2.6256 | -54.28577 | 2024-11-12 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69246869-c007-3af0-8efb-c928b2ecb0b8 | -3.53423 | -54.09057 | 2024-11-12 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29b616d0-e771-3dd6-b375-67d6ef59c1ae | 1.1394 | -60.59904 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f14347-80cd-3418-8676-052caf53becf | -3.34386 | -53.20983 | 2024-11-12 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd61d902-ee66-350e-8ccd-56c48edfb136 | -2.6239 | -54.28487 | 2024-11-12 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8bc8ab4-7266-3b67-ae5e-4b555cb41939 | 1.05529 | -60.59982 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b37fd2c7-ca54-38e7-9890-d7cbc866731d | 0.62269 | -60.08824 | 2024-11-12 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b787c6f5-bacd-371e-aa57-b8cbf0bc35c0 | -2.12557 | -50.69484 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c47355e8-992c-3e3e-90fb-49c57ca59551 | -2.78967 | -51.75242 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90ceed1b-b1a3-3188-92fa-dfd5349cb8c4 | -2.78611 | -51.7518 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c209421a-d340-3839-be0b-18e9c6973c18 | 1.054 | -60.59173 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0d0ba2f-55c1-33c4-9fa2-754ed2317a9f | 1.06015 | -60.60733 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4af6ab9-447f-3fdf-922e-f05cc28a0803 | -2.72986 | -54.13627 | 2024-11-12 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18cd8aaa-ecb7-3458-a730-9aadfc5efcf3 | -2.1195 | -50.68696 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 933fc4a7-5eb9-305a-8b88-ef4b9d472e44 | -3.18727 | -54.31998 | 2024-11-12 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aef77551-5f5d-357b-a7f7-c16e7b36d805 | -3.10167 | -54.30045 | 2024-11-12 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69c2879e-4aa6-364c-adca-9488d6312d0c | -2.72925 | -54.1403 | 2024-11-12 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43e4947-d874-3c4b-a587-078c81206c2d | -2.78298 | -51.75135 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe1f944f-8d52-346f-8234-bd33a955e13e | -2.62449 | -54.28101 | 2024-11-12 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22a692f3-3133-34aa-9a9c-ea7dcd0b785c | 1.06373 | -60.60678 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2a91590-f5e7-3c8e-8554-6b0ea1a9fb34 | -2.31888 | -50.68444 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0f3e46-85e1-3bdb-96fe-c93b9e56a850 | -3.33692 | -53.21394 | 2024-11-12 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8403263-6c7f-36fc-ae94-67bcd7c5a355 | 1.05951 | -60.60331 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c7897b7-b3d7-3307-bfde-9a4fb901a656 | -3.34205 | -54.1946 | 2024-11-12 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07d4119f-18de-3b48-923d-138774e2e60c | 1.13813 | -60.59982 | 2024-11-12 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc2afbc-29df-39b8-886a-333950f76f6e | -3.34268 | -54.19031 | 2024-11-12 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59f23b3d-1fe7-3b43-9885-2bbd7adbcddc | -2.78696 | -51.74591 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7e814000-9dcd-33e1-b315-3e6ae4c10513 | -2.62616 | -54.2819 | 2024-11-12 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a707aa5-c824-3712-813b-3153fd10568c | -2.13365 | -50.6891 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f24321a-7b96-3350-8ed7-fdcfc8621821 | -2.3199 | -50.67778 | 2024-11-12 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e6ae05-bfc2-3d79-a6fb-c735b205960a | 0.89074 | -60.43118 | 2024-11-12 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
