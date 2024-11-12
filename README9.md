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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25462654-7520-3677-b067-c39fdc4be504 | -20.22078 | -47.0906 | 2024-11-12 03:42:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5530d76e-d9c9-3756-9b6e-e0f34b5a89ad | -20.11222 | -49.19046 | 2024-11-12 03:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c2c19b3b-a7a7-33c8-ab35-48bcc1c772ff | -21.18097 | -43.98106 | 2024-11-12 03:42:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1ec43afd-a5b1-3634-9d7a-36744612fc19 | -22.54013 | -48.81321 | 2024-11-12 03:42:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abe864af-0bc0-372e-94da-6bfd2d8e6a7a | -20.32214 | -48.83327 | 2024-11-12 03:42:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 83285f71-5962-3e8a-899e-1666aae095f0 | -20.10725 | -49.18411 | 2024-11-12 03:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a1f34e16-8095-3c15-acd1-871e13899918 | -21.20855 | -42.83731 | 2024-11-12 03:42:00 | NOAA-21 | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f152847e-89a3-3499-919b-a376bd3f72a5 | -22.54142 | -48.8121 | 2024-11-12 03:42:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcc63e35-5633-3d9f-844c-f9caf5ed44d9 | -20.32429 | -48.82378 | 2024-11-12 03:42:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b58ff7af-7cfb-3b92-82bf-7f4b905d0de5 | -25.19197 | -49.32626 | 2024-11-12 03:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e07634e-037a-31ce-b26e-1c4a27562ffc | -25.19845 | -49.32377 | 2024-11-12 03:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1ce720df-ca68-30e9-b9de-030c3bbfc445 | -2.1455 | -50.6908 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7645f266-c6b1-3fa1-9105-881e515d5e00 | -2.1272 | -50.6703 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2d6b3aab-b0f6-3faf-aef9-33d3321c1707 | -2.1271 | -50.6912 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 3c623875-1317-3285-95ab-533fcd3cffa8 | -2.1087 | -50.6916 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1bbccaee-cfcf-32d6-8002-30ccce09a148 | -3.0504 | -50.3332 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| e93b7c0b-9602-3ef3-be55-8a344e15a6b9 | -3.0689 | -50.3326 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 75ffe7ad-05ee-371a-8e5d-4badb9aaa3b2 | -3.1096 | -54.3066 | 2024-11-12 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 92885451-b70f-31b9-a877-d16653c1ac2a | -2.1271 | -50.7121 | 2024-11-12 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 70571066-0977-3e7b-b654-997119b5ccc8 | -3.22181 | -39.76614 | 2024-11-12 03:57:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ec55343d-2e4c-306b-8db0-dd8a6b45e338 | -2.77941 | -50.30089 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e3b3af9-af5d-3e26-9d75-1a26472c70a4 | -3.43008 | -50.30758 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd93a368-25d7-3603-8226-288335cd53e1 | -2.78345 | -50.30856 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9b0f47b-b9c0-3847-90ff-b433d66b3c48 | -3.2256 | -50.29231 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86644ffc-4741-35cd-aadd-d66753933d33 | -3.2248 | -50.29697 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5bdbec9-844e-35c6-ad7b-f1de03c1de20 | -3.40735 | -50.36844 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd8fe792-f779-3b45-9b97-9a4103606015 | -3.04923 | -50.33543 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cdbdbdd5-b78f-3f86-950e-ec478671227b | -3.10079 | -49.42476 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c08b723-3057-3fa3-91a5-fc31b6d3c64f | -2.70742 | -49.18423 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51193b84-8aca-3367-b4ca-c1c7a1dd8121 | -3.06231 | -50.3329 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9dd97445-e0ec-3a67-ba4d-0341384bc2ca | -6.97733 | -40.0276 | 2024-11-12 03:59:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d9956957-e141-3d08-a628-937c3f90ce59 | -3.20238 | -50.28153 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 576f3303-38c2-3401-9872-01b19ad7f28c | -3.66076 | -50.20787 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 842190bb-8ecd-31ed-ae1f-9d20f1d9c72b | -5.93443 | -39.47648 | 2024-11-12 03:59:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a5ac20a1-95d6-3759-813f-1d43ea5fc220 | -3.1958 | -50.28246 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6feabacb-0e4f-3af6-b5e0-5ae892e3d86c | -3.9983 | -49.27823 | 2024-11-12 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e59cbf2-d83b-3506-8792-3ab72f5a52db | -3.07966 | -49.19867 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93683576-e04a-3a6f-bbc5-4c78625e025b | -5.51646 | -39.09811 | 2024-11-12 03:59:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 742376a9-777e-3b5b-85d0-9eebaf4ae609 | -6.74311 | -35.10266 | 2024-11-12 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 356a7fad-9d5d-33a9-ad4a-80babd3aa9ad | -2.7256 | -51.82811 | 2024-11-12 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b9a7537-5333-3e26-bc25-f74e2c6578fd | -3.40655 | -50.37322 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3682e959-3a4a-3e38-8c46-57e0bc454eef | -2.77891 | -50.29803 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7311e76-85e1-3758-88f2-31690445b36a | -3.74462 | -50.1902 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac4230a9-16aa-3c58-ad67-3e9749e8bf77 | -3.54112 | -40.37418 | 2024-11-12 03:59:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce4d3b9a-8c44-3e6e-b72d-9df53405e445 | -6.74236 | -35.10783 | 2024-11-12 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1383fa41-b813-3aa0-99e2-ff4984125398 | -3.19548 | -50.28515 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42c2d53e-5aec-3f52-88cc-84b83a8b763c | -3.75217 | -50.18215 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 622ec485-be9b-3b72-a58d-fc4d369dc564 | -3.67135 | -50.21866 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b15be10b-3401-38ae-a4ad-a621420c0e71 | -3.79157 | -50.1035 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c3caea7-2e9a-363a-98c9-4826e89be112 | -6.85574 | -38.8826 | 2024-11-12 03:59:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 968f290c-2b4b-3335-b563-a04086e51918 | -7.42671 | -35.23556 | 2024-11-12 03:59:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 3d74786a-153a-3868-8399-9c2f9a36dbbf | -5.49312 | -37.24397 | 2024-11-12 03:59:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dfcd170e-0339-39ab-b84a-9423b60de627 | -3.99264 | -49.27723 | 2024-11-12 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79ede864-7a11-3e81-9860-c4629a221807 | -3.19703 | -50.27586 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f257c9b8-50e6-3515-9262-92671fe59caa | -3.75361 | -50.1793 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4603c8f9-4e55-36a8-b51b-2a35e1b8a168 | -3.60828 | -48.91443 | 2024-11-12 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2712fe94-1bbc-32da-8521-dd952426885f | -3.07259 | -49.20557 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ce6aa0c-da92-330e-9f13-da474bbefcc9 | -6.85799 | -38.89022 | 2024-11-12 03:59:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4431618b-c52a-37dd-86a6-61458b5e8e5a | -3.65226 | -43.26116 | 2024-11-12 03:59:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6850532-e193-3023-b8fe-ac10b7ce182b | -6.81729 | -35.09699 | 2024-11-12 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a4b4f74-15a3-3884-9d65-b7652c3e05a6 | -3.05537 | -50.33652 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f330d148-713c-3716-a30e-36771313e242 | -4.13299 | -38.7044 | 2024-11-12 03:59:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2dc7a001-3c8f-37da-9e2e-e0e55b2aa113 | -3.19499 | -50.28712 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4dd63d5-26e4-3229-be7f-b01a96f98208 | -3.8451 | -52.3898 | 2024-11-12 03:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9441df5-6918-3855-8372-e2537cc3b3ac | -3.19661 | -50.27781 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 434dda7c-766f-3998-8959-068fe1e5959e | -5.04179 | -37.77323 | 2024-11-12 03:59:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3d90a60-b90c-318b-b6dc-19feb3af6ca5 | -3.16039 | -44.06319 | 2024-11-12 03:59:00 | NPP-375D | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb27f00-a47c-3686-a970-47996e619ed4 | -3.07164 | -49.20729 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 935cf605-b7ce-33b5-8904-cab601547804 | -3.24769 | -50.31054 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f710dea-ea9e-37e7-bd2b-1ae4d9f4511e | -3.8463 | -50.21805 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e11cf38-ec89-3c77-b6e2-a1e77e9e649d | -3.07899 | -49.20258 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acd96e7d-8806-345a-92a0-faf8c9102fa4 | -4.24859 | -50.25322 | 2024-11-12 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f62aec5-d234-38e2-a446-45deaedee9d2 | -3.05615 | -50.33187 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 2aa6efa3-7366-33f7-96f9-5745737826ce | -3.19471 | -50.28982 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ed9ede1-0fb1-3165-b054-7ed3f0abe2f1 | -3.73938 | -50.18439 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef1063a-eafb-327e-83be-e0762da12e47 | -4.15554 | -50.7963 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 61ffe0fd-c444-3730-af70-de781dcad21f | -3.07737 | -49.20826 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdf49403-26b6-3357-aa5b-7041b7c665fc | -2.77784 | -50.31042 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d45f706e-93be-37cc-b003-cfd74c91ffdf | -3.42988 | -43.03666 | 2024-11-12 03:59:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f069c6a-86b8-3f72-ab54-7089432c3fb0 | -5.51314 | -39.0976 | 2024-11-12 03:59:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff6b5f3e-a31b-3266-bfa1-a4c065789614 | -6.97678 | -40.03106 | 2024-11-12 03:59:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab447ed4-ea3d-31f5-971c-ef07e164ad42 | -2.70808 | -49.18026 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82981b71-36d7-3c1b-ad54-6cc1d38c2550 | -2.78557 | -50.302 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbbc810e-3b5d-334f-a8a0-5b9d02119d56 | -3.75962 | -50.18044 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd07916c-b6ed-3559-b0c0-0baa19c693d8 | -3.24691 | -50.31516 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ebd2747c-ecb7-3b8b-8a2d-3c70f8d28779 | -3.7528 | -50.18393 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d3602b4-dea2-30d2-8a4f-53cb9b9cd8f4 | -5.12637 | -37.85706 | 2024-11-12 03:59:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6b6ee0f2-58cc-3b81-b751-3d5a5e6e38e2 | -3.09501 | -49.42365 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99624140-4ed4-36d2-a99c-deac085381fc | -2.78634 | -50.29725 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f75b6a5b-2d77-3bce-9ae5-c85b246175d0 | -3.43698 | -50.30404 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b0e41ad-5446-3429-a166-8d9ae59a3168 | -3.29492 | -43.53942 | 2024-11-12 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edac30c6-6243-3e0f-b202-39bd2e223e2e | -2.77863 | -50.30565 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5b9b6e74-0c3f-30a7-aab8-6aa2e071d621 | -3.67212 | -50.21424 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0494e32b-7bf9-3f24-be26-2cfefc5b3461 | -4.42341 | -49.71756 | 2024-11-12 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d426e6be-0932-30ce-9d04-d6228dbfd9e9 | -3.07765 | -49.21046 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ca65a89-6f2d-36b4-8d4c-c4e30b4fda70 | -3.78634 | -50.09803 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 069deb6c-7c98-39c1-b6ea-8191a7c896db | -3.07866 | -49.20037 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81c90327-fd12-30f9-87a4-0aa5bbf23b05 | -3.75819 | -50.18329 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 565980d3-8389-382f-bef5-5caf40128283 | -5.93111 | -39.47596 | 2024-11-12 03:59:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a739de69-542c-31f3-b4f9-17393248e551 | -4.5606 | -37.97539 | 2024-11-12 03:59:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
