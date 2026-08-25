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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f857e3ad-4cb0-3280-a302-86277ab59467 | -7.2901 | -45.3683 | 2026-08-25 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 226.4 |
| aaf2d393-9aa2-3322-9c08-6a8bf56738b3 | -7.3849 | -55.1723 | 2026-08-25 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 58e02518-8f59-3a00-975a-37f773370126 | -6.6225 | -58.5189 | 2026-08-25 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 252f4781-f6c2-3020-b344-647ac724544c | -11.8168 | -47.6424 | 2026-08-25 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 5d3c1032-1f47-3949-8758-bc4e7d101b43 | -7.0057 | -59.2575 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.6 |
| b8b37ec0-ec0f-351e-9cfd-af7716d32129 | -6.1468 | -57.858 | 2026-08-25 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c6f9104d-c977-36a7-992b-d475e51b4c3c | -13.3402 | -48.2079 | 2026-08-25 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 13b0126b-d1d6-35e9-b177-af59280f4fc7 | -4.1934 | -54.5755 | 2026-08-25 14:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 1546bdcf-6313-3d6d-9df9-f52be0cc5d19 | -6.1285 | -57.8393 | 2026-08-25 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7c574513-0b9d-3723-9059-0719cc03ed6c | -8.1765 | -46.7007 | 2026-08-25 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6fb800b3-2fc1-37c0-be4d-747a5751694e | -6.8008 | -59.5934 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 5b52c08d-a713-32bd-bc3d-4a15eb6901c2 | -14.3157 | -51.8542 | 2026-08-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 67348213-196d-33be-97df-959f5879f472 | -9.5753 | -49.2367 | 2026-08-25 14:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 252fb71d-fae0-347c-8a7b-ab5a6a83420b | -6.332 | -54.7674 | 2026-08-25 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| fc3c6675-aa0c-3129-bd94-2c64252f9354 | -14.7592 | -48.7913 | 2026-08-25 14:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 4fb58ccf-445d-3db5-8a9f-1e16edacff20 | -6.7648 | -59.4408 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 51646a65-81c3-39f1-9f5a-da7d9b3b17f1 | -13.6333 | -49.0272 | 2026-08-25 14:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a0bf9317-0f03-30e4-8bf1-73e43f432357 | -14.7787 | -48.7882 | 2026-08-25 14:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d2b61a74-93ab-34bc-87f6-142ce88106e3 | -13.3595 | -48.2051 | 2026-08-25 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 168.2 |
| a8a9d2ec-57e4-34f7-a155-108e2ceefae8 | -6.8192 | -59.5927 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1381687c-38d1-3330-b651-0c4362e32541 | -8.073 | -47.5287 | 2026-08-25 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d3d113d1-db49-335b-acc6-1d7bd6a4d6cc | -7.2715 | -45.3473 | 2026-08-25 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 63ec7a0c-b74d-3d2f-a353-589ea054588e | -12.151 | -50.6098 | 2026-08-25 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 448fa45e-ad2a-3691-8065-ade5c9cc57a9 | -6.6357 | -45.1752 | 2026-08-25 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 336.5 |
| 95c8b608-6158-3041-a813-451e9abe8c45 | -6.6409 | -58.5181 | 2026-08-25 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4ee0fa05-8de9-3bd4-8d93-ae4942a39f6b | -6.3322 | -54.7473 | 2026-08-25 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 4f340983-d020-35b4-903c-14bcae6471cc | -7.0242 | -59.2374 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.6 |
| a9016594-4c36-36dd-9cc2-f5bafd92bb7a | -8.5775 | -54.8575 | 2026-08-25 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| bbed3a0f-1e71-3050-a06a-d484455244aa | -6.6359 | -45.1525 | 2026-08-25 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 0e93a04a-eb29-314e-8891-dc59c219c144 | -6.6227 | -58.4801 | 2026-08-25 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b3533784-5ba0-3822-8ec5-0b7dd6186881 | -6.6411 | -58.4793 | 2026-08-25 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c01b4904-ea6e-3a57-a04e-471cde8c8c89 | -7.2713 | -45.37 | 2026-08-25 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| aaa3b22d-e76a-3a18-89b9-d0a719635f12 | -6.1284 | -57.8588 | 2026-08-25 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 8ee84105-b9e7-3d11-8f76-6ae0186671c5 | -6.3505 | -54.7665 | 2026-08-25 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 455d9338-ac73-3c72-b642-e82527fd7037 | -7.0241 | -59.2567 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 2a9cacbb-74b0-35bf-b385-78f7fadf3cf2 | -7.0058 | -59.2382 | 2026-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 735451c4-0894-30b7-992b-852ef5a448a3 | -8.1564 | -52.0453 | 2026-08-25 14:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 5c1ad1a0-a32f-394b-8f1d-68621cd842c0 | -7.0817 | -42.1585 | 2026-08-25 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 4dcd64c5-8ce8-34cf-bd86-5eb4bb6779f4 | -6.1286 | -57.8198 | 2026-08-25 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6db857d2-9927-300f-a8c8-8557e5f96c08 | -14.7787 | -48.7882 | 2026-08-25 14:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 148.7 |
| ae091fca-c0d6-3ed2-9532-12797478b853 | -6.8192 | -59.5927 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ffebd845-50ea-3c88-86d3-a75a07d54227 | -6.6357 | -45.1752 | 2026-08-25 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 017da359-4ee2-379f-bb5a-9649a9727962 | -11.8168 | -47.6424 | 2026-08-25 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| acdee1a7-2a5a-371f-903c-4dad4c8cc1fa | -6.8008 | -59.5934 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 180d42b7-c883-34ba-8b2d-25e1d7b283c9 | -7.3849 | -55.1723 | 2026-08-25 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6493e850-97c4-381c-941c-72bf3a130975 | -7.2901 | -45.3683 | 2026-08-25 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 6ec2bfd9-44ff-3dc3-a26c-e0db66d939b7 | -6.3505 | -54.7665 | 2026-08-25 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| db3fbdb4-5678-30bb-abf0-f212c8219288 | -7.2715 | -45.3473 | 2026-08-25 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d53d533f-1f27-3167-a9ee-0de9f1a7867b | -11.9036 | -44.8393 | 2026-08-25 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3f000ba1-7430-32bf-a201-444cd5302e79 | -13.3402 | -48.2079 | 2026-08-25 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| af73811a-2a9c-35eb-8a82-129da9bba255 | -6.9873 | -59.2389 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 950a83a8-a26d-3904-90d1-9ca4577f3a74 | -14.316 | -51.8329 | 2026-08-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 09e43f25-7d5c-39cc-abe9-8cafdac6cb59 | -6.6169 | -45.1767 | 2026-08-25 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 221.9 |
| d21ea84e-f6af-3522-a0d2-994ef85afc6e | -9.5753 | -49.2367 | 2026-08-25 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 722f32df-614a-359c-9fee-1e4c26ecdb51 | -12.757 | -46.4538 | 2026-08-25 14:30:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 43d65c99-7587-3e3e-a21c-68c9ee4776d8 | -8.6078 | -50.0124 | 2026-08-25 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 9bfd7ba3-b345-32b9-a0b2-618f301a9a34 | -7.0058 | -59.2382 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| ee5c7e5d-3b32-3bb2-b5fc-5bb0810a1b91 | -6.6227 | -58.4801 | 2026-08-25 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0e6935da-3ab5-3ca1-9328-15821bfa68f2 | -12.5964 | -47.9142 | 2026-08-25 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b85d43e4-4f6b-322a-8589-1e9e9ac113bd | -6.7648 | -59.4408 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6645c195-8242-3778-976e-18308f99e13f | -7.2713 | -45.37 | 2026-08-25 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 7a1421b5-1491-37f7-84d2-dad1cd40cd43 | -6.6225 | -58.5189 | 2026-08-25 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ac416909-036c-3c32-b774-82242abb74aa | -7.0057 | -59.2575 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 207ee2c3-c2d0-35f7-a007-e8603c8d78b1 | -14.335 | -51.8517 | 2026-08-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 274.9 |
| 27449333-77de-3313-b75c-75a18bc9ba6b | -6.6409 | -58.5181 | 2026-08-25 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9d5c6bcb-4494-3af3-9bc5-90f72066c762 | -7.0817 | -42.1585 | 2026-08-25 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| 99bb3939-7c68-39a8-8d63-995d78ce923c | -13.3398 | -48.2301 | 2026-08-25 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| cb01dbde-50b0-3dfe-8d83-4430f34d2c4b | -6.4098 | -51.7049 | 2026-08-25 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| cb0fe034-98e1-343d-8c5d-15cd2213b3a3 | -6.6411 | -58.4793 | 2026-08-25 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 065cc992-eae5-3c80-a91d-a3c6066d37f2 | -3.4167 | -43.3867 | 2026-08-25 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 19cc0f3a-3b39-3ccf-b377-9bb5068e3c3c | -6.7832 | -59.4401 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9feb9de6-83cb-3c21-9f99-66a92ab44474 | -14.7592 | -48.7913 | 2026-08-25 14:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 171.9 |
| a5c2baea-35d3-39b6-9fb2-bcf12af77b58 | -14.3346 | -51.873 | 2026-08-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d2581b5b-03ea-3adf-98a9-f5887288c5c5 | -6.1468 | -57.858 | 2026-08-25 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e29c2baf-cd72-3715-8061-eee046b33c72 | -6.332 | -54.7674 | 2026-08-25 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 09962841-639e-368c-b410-da53b875e6b3 | -6.1286 | -57.8198 | 2026-08-25 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f093fa97-8f8b-3e4a-9845-c07e2ac2556a | -13.3595 | -48.2051 | 2026-08-25 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 12cb664d-9487-39f9-a8c4-294551a4fd38 | -14.3157 | -51.8542 | 2026-08-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 214.4 |
| b231cfa7-9bab-3c8a-9996-be8515677de2 | -6.1285 | -57.8393 | 2026-08-25 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 08af5448-71bf-3fc2-a73c-6aa8dfb96fa6 | -7.4474 | -43.1163 | 2026-08-25 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 147.0 |
| 156bde3f-8fbc-3b37-89de-3c130ec540f9 | -8.073 | -47.5287 | 2026-08-25 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 34eeb6f2-8a2d-3d96-a961-ac0c56dc3cde | -6.6359 | -45.1525 | 2026-08-25 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 964987cc-96cb-32f4-9c6d-262d11d25340 | -6.9872 | -59.2582 | 2026-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 330a8204-7f51-39ed-820e-529e65425b69 | -8.5775 | -54.8575 | 2026-08-25 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |


