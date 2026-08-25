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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c584e91-2325-3ba3-855f-8cb181ac35d1 | -8.0918 | -47.527 | 2026-08-25 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7a1dab70-b5cb-3a9b-8f96-d552cb4167ee | -14.7787 | -48.7882 | 2026-08-25 14:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 508f5a02-06d7-395a-a81c-8a7504a3ecac | -7.2715 | -45.3473 | 2026-08-25 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 7855bec8-4d1a-3234-84a7-7372bb5d2895 | -7.2713 | -45.37 | 2026-08-25 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 9b8df2df-553d-3f60-9d3f-20b7ab72e31a | -12.656 | -47.7947 | 2026-08-25 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bda67aa5-163f-372c-be1b-6eb56060aea3 | -6.3505 | -54.7665 | 2026-08-25 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fbd03c4e-fdce-3f1e-b133-7421319a13f3 | -12.757 | -46.4538 | 2026-08-25 14:00:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 07808cf6-02bb-39a5-a76b-1ce89b2012a9 | -7.2901 | -45.3683 | 2026-08-25 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| f43e7e58-a056-3e90-8fc3-417592fdbfad | -14.316 | -51.8329 | 2026-08-25 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3e140c1b-a5b8-3c5b-9f93-aafca63c32cd | -8.1765 | -46.7007 | 2026-08-25 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| fdac8b8a-f49e-3010-b777-bf439c98dbd1 | -6.1468 | -57.858 | 2026-08-25 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f2f69e89-28b6-3388-9d6a-dd20d35b33f8 | -7.0242 | -59.2374 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4b38bda7-d09e-3b2f-a548-152f509c8487 | -6.6357 | -45.1752 | 2026-08-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 5476d43f-4eca-3628-9943-60eddaf298a5 | -6.1285 | -57.8393 | 2026-08-25 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| bf0441a8-2e1b-3fab-a71f-a359a56ba728 | -14.335 | -51.8517 | 2026-08-25 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5a6932b9-71ff-3511-b8ed-676c6b36667f | -6.3507 | -54.7464 | 2026-08-25 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 90dc2836-be67-3f02-ac9d-cfe72078e403 | -13.8762 | -54.053 | 2026-08-25 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 7f006183-9ddb-38ba-a12d-0611e6c68cbd | -12.7377 | -46.4567 | 2026-08-25 14:00:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 842420b6-9197-3911-95b9-5eb75dcd7ae9 | -6.8192 | -59.5927 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 41d45d36-c140-31ff-bdde-5b9cc0fce3fb | -7.0497 | -50.7667 | 2026-08-25 14:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c10ae156-caf1-314f-b112-bf5105061c64 | -8.6078 | -50.0124 | 2026-08-25 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| c1b9c6f8-b7bb-3e09-81f1-0ecc92cec76f | -7.0241 | -59.2567 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 319e1aab-7022-3afc-a5aa-5cafde4247f8 | -13.3402 | -48.2079 | 2026-08-25 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f4db9d23-d632-3f89-af56-623cf01074d4 | -13.8759 | -54.0737 | 2026-08-25 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 1afc9bd1-e146-35fa-8d65-2974ecf9d8cc | -12.151 | -50.6098 | 2026-08-25 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 939b4d40-8e14-37c2-9685-347cd670fd56 | -13.3398 | -48.2301 | 2026-08-25 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 410e0f0d-afae-31b5-add7-c568df8dce27 | -3.4167 | -43.3867 | 2026-08-25 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6e4b3674-db16-31dd-abda-93178740c4b5 | -10.8416 | -50.5646 | 2026-08-25 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 154e9ba9-3c47-32b1-ac42-d68f385f943e | -8.073 | -47.5287 | 2026-08-25 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| cc194c2f-51db-30fd-9c5f-b98504659cc8 | -9.5753 | -49.2367 | 2026-08-25 14:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 1b86a8fb-fd30-3518-a02d-c0dcd3bca693 | -6.1284 | -57.8588 | 2026-08-25 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 19b667b1-d7ae-36e1-8124-01728f8ab5e4 | -7.0057 | -59.2575 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| f784a063-9c3d-371d-be6e-48c09d2c4fc5 | -14.7592 | -48.7913 | 2026-08-25 14:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 52abde0f-4aa7-39fd-b0c1-94c442230518 | -6.6411 | -58.4793 | 2026-08-25 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9aec9ac2-e2a1-32de-81a5-fb0f329f57e9 | -6.9872 | -59.2582 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 967f73af-8e2f-3e5f-900e-92d5dc387446 | -6.9873 | -59.2389 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e80dce0e-1f79-392c-8360-cd3d430036f1 | -6.3322 | -54.7473 | 2026-08-25 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 692ee6a9-b06c-3189-8d0d-c02c4b883ef3 | -6.6169 | -45.1767 | 2026-08-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e86122e4-13df-304a-9428-de61839e60d6 | -14.3157 | -51.8542 | 2026-08-25 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1f26a1e0-fddd-30c8-b305-fa6c8ed9ad47 | -13.8765 | -54.0322 | 2026-08-25 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 89540384-f5bf-3610-aa76-0387292be9ac | -7.0058 | -59.2382 | 2026-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ebd224e3-c355-3b64-937d-724d4e844689 | -6.6227 | -58.4801 | 2026-08-25 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 90cf4769-f054-3c84-90f1-a1c1600abf5e | -14.335 | -51.8517 | 2026-08-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 6ff87bf0-7e72-34f1-987b-c999af62dc6c | -7.4474 | -43.1163 | 2026-08-25 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 134.0 |
| acca5223-2c71-31df-bdcd-e54eb95b589e | -6.6169 | -45.1767 | 2026-08-25 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| ee56fd33-273f-3098-9bcb-9dcb12ce270b | -6.1285 | -57.8393 | 2026-08-25 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e83a0c49-12bd-3602-8c4a-c73f94794bf0 | -6.9873 | -59.2389 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a34a489c-4663-31b5-b789-5eab42006148 | -9.5753 | -49.2367 | 2026-08-25 14:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 38a061b1-7a34-339c-81d4-b45363478c12 | -6.6411 | -58.4793 | 2026-08-25 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 68af3fea-e673-34a3-9557-3b6c9e0fdec9 | -7.0058 | -59.2382 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 511b0267-6441-3775-b682-e10a9b01f440 | -8.5775 | -54.8575 | 2026-08-25 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| f545c43b-98c0-3700-8eba-3280159e8dd9 | -13.8765 | -54.0322 | 2026-08-25 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 8eee9cad-e716-3519-b4df-babb72c8a722 | -6.1286 | -57.8198 | 2026-08-25 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| aa3cc196-6b03-3805-a25c-57423364b0e2 | -8.6078 | -50.0124 | 2026-08-25 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 9f07de6d-21c6-3732-8f38-6586a90fb580 | -6.6409 | -58.5181 | 2026-08-25 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| c3ba2c88-db5b-34fa-97eb-389805e28772 | -14.7592 | -48.7913 | 2026-08-25 14:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| d70c6b69-bf3b-38b7-9017-95d46cac79d2 | -11.8168 | -47.6424 | 2026-08-25 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a788bfd1-1e40-31e9-8407-829d6a52581c | -6.6357 | -45.1752 | 2026-08-25 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 275.0 |
| 1c466929-3b36-38ca-887e-3e6966c79c35 | -6.332 | -54.7674 | 2026-08-25 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 05559643-3a11-3e7f-941c-f2961cfe59b0 | -7.0057 | -59.2575 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 1c604258-72b0-320a-9da1-10f73b170f64 | -12.151 | -50.6098 | 2026-08-25 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 7e7ab546-fa72-3f17-981c-e40ba29b5b7f | -12.7377 | -46.4567 | 2026-08-25 14:10:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ab341194-1072-35ef-a726-40c9bb0e9697 | -12.656 | -47.7947 | 2026-08-25 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d7c1edc4-bd4e-3902-8a83-339e3109e9a8 | -8.0918 | -47.527 | 2026-08-25 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 5319df0a-0cb3-3b77-a64e-8382aac28665 | -8.1564 | -52.0453 | 2026-08-25 14:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fc9d22a9-927e-36c4-9b71-b798aa4d5047 | -7.2713 | -45.37 | 2026-08-25 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b81644d9-2353-36e9-9fe0-7b6fb1172876 | -6.1284 | -57.8588 | 2026-08-25 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| fd24c1af-52db-3171-8769-f825ca4c0ba0 | -7.0241 | -59.2567 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 84b45e3d-9d58-3847-90fb-ea24a9ee63f0 | -7.2901 | -45.3683 | 2026-08-25 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 22c6630c-2b58-3e0c-b92e-491075ad6064 | -6.7648 | -59.4408 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ce9057a8-7b26-3b6e-a5a5-b201684af933 | -12.757 | -46.4538 | 2026-08-25 14:10:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1817bf3f-ff3a-38a2-9758-10a2317c1015 | -7.0242 | -59.2374 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8bad57d3-59ad-3478-a8b0-8ef4fb067f1c | -6.3507 | -54.7464 | 2026-08-25 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ecf2b2ba-a4c9-399d-be8d-e2c89579c176 | -3.5407 | -48.1673 | 2026-08-25 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5d841ce7-e18a-30d9-a9ea-8aafb565a9a8 | -6.3322 | -54.7473 | 2026-08-25 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 296.3 |
| 5a0b404d-39fb-3859-b481-4881387be753 | -14.3157 | -51.8542 | 2026-08-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 13bade40-f94e-34c7-a3a3-002de1425097 | -8.0921 | -47.5049 | 2026-08-25 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b7b79457-3cef-3f75-a383-a3d183895f48 | -6.3505 | -54.7665 | 2026-08-25 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a8cb5f38-7fd8-3839-ad3d-bb11eb231a6a | -8.073 | -47.5287 | 2026-08-25 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| adabe5ba-ac24-3123-9ad0-5d8647f18b04 | -14.7787 | -48.7882 | 2026-08-25 14:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3cf9a181-fec7-3440-8b5b-9d67c45e7158 | -13.3595 | -48.2051 | 2026-08-25 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| f8cacd1e-bd35-37a4-bad1-236828dff236 | -13.3402 | -48.2079 | 2026-08-25 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 862b3710-2908-32fc-9cb9-1c0dfd89b9a0 | -7.3089 | -45.3666 | 2026-08-25 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 39f0bd70-1fb9-3f43-b8de-3c3223f51fdd | -3.4167 | -43.3867 | 2026-08-25 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 7a02ad5e-1a19-34b2-ba88-4b4999225d76 | -6.6359 | -45.1525 | 2026-08-25 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 95ec9e87-1f96-331f-aaf8-8f6dd66befa8 | -6.8008 | -59.5934 | 2026-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| df89bd2c-88ad-34f4-8cab-650827522c33 | -8.1765 | -46.7007 | 2026-08-25 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c7ff89f4-a235-376a-9627-cd5f43623d15 | -13.8762 | -54.053 | 2026-08-25 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 5b2578ed-8532-37e7-8fcc-bdf5053a94c6 | -7.3849 | -55.1723 | 2026-08-25 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ff857555-b5e8-3578-909b-6b796e41a0a8 | -14.37 | -52.89 | 2026-08-25 14:15:00 | MSG-03 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46e618da-0f8c-3724-9865-c211d1cedd48 | -8.6078 | -50.0124 | 2026-08-25 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9c33bf13-cedd-3667-a359-e25899be379b | -3.4167 | -43.3867 | 2026-08-25 14:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 5704962b-395b-3bfc-be20-a339c6879232 | -6.9873 | -59.2389 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4542af0a-9f34-3ea8-9ca4-51bedafb59e5 | -8.0918 | -47.527 | 2026-08-25 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a0c5dae7-a054-33b7-8e99-194f6a828175 | -13.3398 | -48.2301 | 2026-08-25 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| cfc54410-c705-3862-9dd5-37b988b24d6d | -14.335 | -51.8517 | 2026-08-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 46a95988-a24c-30ab-8996-a4d81eeeb830 | -6.3507 | -54.7464 | 2026-08-25 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| e0d8c0e5-2144-32b2-b22a-5717522ef39c | -7.4474 | -43.1163 | 2026-08-25 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 77509900-659f-38ac-868c-1808779edcfd | -6.6169 | -45.1767 | 2026-08-25 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 358.1 |
| 64c0187f-4c14-3b1c-a461-897b4b299b52 | -12.757 | -46.4538 | 2026-08-25 14:20:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |


[Clique aqui para ver as próximas entradas](README76.md)
