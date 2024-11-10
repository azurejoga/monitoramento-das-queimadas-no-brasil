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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 383f6e88-0889-3a5d-81a5-06ce53b82f14 | -3.23188 | -46.4872 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd5d3201-1b37-36d5-af4a-2a226e01143d | -3.54115 | -46.36947 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3f03e7c-89a4-36a7-bb54-8e44fb9912b5 | -2.62495 | -51.29426 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac051896-3a26-3724-9259-0ea767cf67d0 | -6.73518 | -40.81264 | 2024-11-10 04:38:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4e823d0-9568-3966-91f6-855d9d8dfe4f | -4.6296 | -48.90119 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4998e635-e8af-3904-bfa3-e36b4c89c04c | -4.13051 | -49.55439 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 248d9e5a-2aa6-3b0b-bbb4-2aaf4c4fc685 | -3.13134 | -50.44308 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 98ed006f-4b7b-3101-b882-9d983ccb7f4f | -2.69059 | -49.8681 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 261638a3-fb19-3d7e-a804-7de53c349739 | -6.36846 | -55.36934 | 2024-11-10 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8049b16-2984-3b6f-9143-1159a6b451fc | -3.07301 | -50.56704 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bfc4c31-e06f-3bbc-9dda-b2a2b223c6b2 | -3.9121 | -47.95137 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebcb2379-9978-3717-bded-e6fd63d08af7 | -3.05129 | -49.53234 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb4b8a54-b9ae-3b69-ab7a-110648488e9c | -3.71444 | -40.71025 | 2024-11-10 04:38:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f36f5b61-e0de-3a0a-907e-6b9199422c1f | -2.61986 | -51.74746 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d038bcc1-d40a-3cc7-b593-8f831e1a93ed | -3.04457 | -50.3274 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae57fa79-2bbc-3316-9cc7-e75fceadfb30 | -2.58901 | -48.16864 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6991b0c0-0af2-34e9-b957-a1c9485e32ba | -3.97941 | -48.40675 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7cad89f-791b-30ce-91ef-f47da183dd34 | -4.53659 | -43.56744 | 2024-11-10 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dbfcad4-adc2-32a5-805d-62db97c0b91a | -3.2351 | -50.27086 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7221ee57-92a4-3c6f-9e9e-cb99cd6d8cd1 | -2.41588 | -48.96511 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1edf6531-faa1-3eb4-bf12-4f48d88b537a | -3.52594 | -49.97603 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d563cb17-1a56-3969-b45c-1315e5b11781 | -3.22947 | -50.43902 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609e3173-e77d-3d17-9c24-a09f07d03147 | -3.11216 | -51.2924 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba61e8fc-1b98-33bd-885f-e9dc0a1b115e | -4.16445 | -46.60217 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cf95023-5e2a-3dc7-9b6f-30ce66eb1b97 | -2.92073 | -49.36836 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99571e63-ee85-3932-a6b3-6ff691fef447 | -2.23358 | -50.69097 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6446c5d9-e81d-33f9-bc19-6dbd6b4bdf6b | -2.94352 | -49.35402 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3cfad30-fa13-34df-8ff6-46be26ffa7c2 | -2.59332 | -48.31417 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f2c476c-7f8f-3010-9b66-c51d82873307 | -2.6888 | -51.95101 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 208b2e8f-cd97-3a3c-a554-eab1fe23c425 | -3.78591 | -47.46176 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fad1f4fa-2c31-3132-91b0-41e7d0290418 | -8.90027 | -44.22528 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5268b3bf-b164-3f5d-b3a5-d5eb8ae902cd | -3.21653 | -50.38793 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 686a1fcf-f993-37ae-a072-94c8bf5dbc77 | -3.43281 | -50.30114 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 2907a795-e9b9-3a7b-b2da-d7aaa505f391 | -3.9654 | -48.17015 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e6b18c-34cf-385e-a962-2d70c36ac6f2 | -1.65984 | -55.08738 | 2024-11-10 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1159523-13cb-37cf-b71d-823edcc9899d | -2.88905 | -48.30337 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 827c8a83-0afa-307c-9c3e-f27c5f831046 | -4.01398 | -48.29507 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80bf3624-f249-3c6d-ba1a-bb43a83ab225 | -4.01289 | -48.30201 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5366c784-9a63-3135-81b2-7ecde67bf320 | -2.97802 | -50.30566 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68e10511-06e3-373f-9701-90707be53e9a | -3.30707 | -50.08516 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7086f39-0b90-3dbe-8708-da6f8dd79cdc | -2.95081 | -51.06332 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85d4a5ae-7554-3b3e-9ca2-6a505d8da282 | -3.0907 | -51.29413 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad068a10-effd-3008-a95f-b515a14d064d | -3.03311 | -50.35566 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43d30a22-f5a4-3ec4-894f-42f2a8309ed2 | -2.13171 | -50.6718 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b976369-cb29-35db-b38c-c0739daebe43 | -8.39267 | -44.1112 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83e01e41-5aee-37fc-a2ac-5ed0ba15ba8c | -2.5697 | -48.18332 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d706f9d-96d2-315c-87c0-068ae684f8c1 | -3.01617 | -50.4855 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cd2ee1c-a2df-3718-a327-f46cc08a086d | -4.34183 | -48.1466 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2481062e-8966-301e-a1f5-130d125033ba | -3.59802 | -47.34575 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1d9f7520-97ab-3c84-9d49-d817e8c4ef3f | -3.88759 | -49.94864 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e045c3a3-2db5-3018-af16-673d479fa1c5 | -5.41137 | -46.41653 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44e849aa-1543-37c8-8a27-00564cd100c9 | -5.1267 | -49.33023 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8607c7f6-5cf9-38dc-9f52-77d0230aa2b5 | -2.60446 | -54.19385 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e324853-ccf9-3dda-b39b-22796d570fd3 | -2.40515 | -50.30449 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 255078e6-442b-3484-8d2a-930eadfd3271 | -3.23173 | -50.44695 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 228b336e-c26d-3369-8494-b3729114ecd3 | -2.672 | -49.89825 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d419dbbe-aaab-316e-a948-dc6c54fe4484 | -3.35374 | -54.1246 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92879348-0f3d-3172-9d41-8f14e4a40399 | -4.38966 | -48.57396 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55690c6d-8231-3f4a-92ca-1cffb3c24a0c | -3.87545 | -48.33752 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58f56d1b-3c76-39a8-a7ad-bd59bda33f53 | -3.87168 | -50.26542 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ef67dee-e45b-369f-a091-1655c1011c8b | -3.74909 | -51.10069 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af9bf409-c853-3f59-8e04-e0d869b674b7 | -7.14096 | -41.10785 | 2024-11-10 04:38:00 | NPP-375D | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5bc123d9-e5aa-3c9f-a3eb-f1a2f33073d8 | -2.84449 | -49.23151 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 612b8b8e-42ed-3b84-b0c6-210706500b3b | -2.87613 | -49.22577 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 311e7cc9-5f3b-34ce-8cf9-60d050d61626 | -4.06568 | -48.31026 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8cf4025-8d8f-370f-97c2-3ca5aaf0ec9b | -3.08159 | -49.50426 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c27b5d87-8187-3a57-a9a3-f78177454aeb | -1.87185 | -54.19196 | 2024-11-10 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de8d9487-249f-3681-a96c-e268c6539c2f | -3.97804 | -48.13297 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f194a58-afad-3f94-b4de-794cfcb087b8 | -4.46746 | -45.66252 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cde772d-69a9-342f-9156-36e04d2ad038 | -3.07599 | -49.58258 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6745284a-5f9b-355f-8f9e-dae9577bfad4 | -4.60793 | -47.98374 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b0ea910-982a-36f4-9a1e-5e70577d7572 | -2.10044 | -50.84875 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd3e0f5a-6224-3f12-aa95-6e497c1d41cf | -5.56639 | -47.77406 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36dd6ffa-5519-3da5-98e5-30f36f2db7d2 | -2.98323 | -49.57213 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77a4369c-2c1f-3e66-b480-be4bffdedfe9 | -3.08785 | -51.22058 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69fb874a-a8e5-330e-8733-ec44ebe00e22 | -2.23554 | -50.52005 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45262dea-159a-31fd-ae6d-33627936af82 | -3.48208 | -48.23712 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a30e15e9-a8ec-362e-b9bb-9875a5ad8c4a | -3.74322 | -50.17534 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 873783b2-4438-34a6-a5e4-44c0cb579750 | -4.27978 | -48.1941 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55400e93-5446-3c28-a70e-5abe5615294b | -8.39042 | -44.1268 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b367006d-eca5-352a-9c4d-6cf2d60838d1 | -5.23623 | -44.07576 | 2024-11-10 04:38:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93be720c-3f87-3b6d-bd9f-aa0f60b49e2b | -4.49931 | -45.6975 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7107af82-cc0d-3e56-ba71-0e1d741952a8 | -4.26841 | -46.917 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29f6292c-5c20-345f-a8f9-c8b24fed4ae4 | -4.85289 | -48.40473 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26743d7e-b428-35c0-a9e6-27fabc4f7f00 | -2.89292 | -49.39267 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 274915b7-292d-3480-83de-36b0e6a846c7 | -3.35041 | -50.35971 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d701e171-7afa-3931-a626-f77f678b04e0 | -3.18428 | -54.31483 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29db422-6e13-3429-8803-384757d14ffd | -2.4035 | -51.30231 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ff4939f-28f8-36e9-bb4e-d1900a86d6a5 | -4.06101 | -48.23129 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f50646e7-602b-34a1-9625-81782af36938 | -2.89558 | -49.23238 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba1bc121-ded9-3ca6-bbf5-27c6407cf49d | -3.82704 | -46.50153 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aac6e91b-ecb6-327f-8827-e46cf1ae6aa6 | -3.03791 | -49.53024 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2396b894-f2d8-341c-a3b1-77bddb70f8be | -5.28155 | -45.37584 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d7a22bb-d8e7-394a-8c2e-72baad9b5e96 | -3.9625 | -46.70302 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f932c337-ab91-3417-b35d-9f9e0205f0ad | -2.66354 | -49.90796 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d33c950f-a714-3646-bad6-c2b3f497e3a0 | -3.95711 | -48.17956 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cfb03f39-6605-3f3c-ba1c-0d1c56874831 | -2.96242 | -48.0315 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f71e90bb-8fb2-3a06-a190-eba661a8cd89 | -2.12754 | -50.84021 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 906a9fd3-c36e-390c-88d8-0809ca4b63f1 | -5.36201 | -47.91803 | 2024-11-10 04:38:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d450cb4-27af-3c8c-bc10-104c0e2937ee | -3.11271 | -50.20741 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README78.md)
