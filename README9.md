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
| 940fc956-591f-3b35-ba8a-14f8cbd10d29 | -18.672 | -49.0793 | 2025-08-31 01:30:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9e3e6620-fc53-39bc-bee1-186c6222eb8d | -9.2745 | -67.6433 | 2025-08-31 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 1f36f9f6-17eb-3fb5-9b3f-82e3bcddaa54 | -3.5995 | -47.5142 | 2025-08-31 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 07e39ed2-027f-3cfb-9ac5-285a48c5a067 | -18.6715 | -49.102 | 2025-08-31 01:30:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c9d793ac-0500-3f6f-b276-4046dcef106c | -8.744 | -62.379 | 2025-08-31 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 084e8dc8-2f91-3145-a580-43ca22e29817 | -12.3099 | -45.7 | 2025-08-31 01:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3c7cd6e9-1364-373d-b9fa-0f12bb58e882 | -12.3095 | -45.723 | 2025-08-31 01:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0db495b6-8950-385f-bde8-d7dec0c94e13 | -12.3287 | -45.7201 | 2025-08-31 01:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3f461ccd-401b-3543-96ff-89e5f3946688 | -6.7093 | -51.4165 | 2025-08-31 01:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 086404c3-618d-3f34-90d0-13f189257af1 | -9.4495 | -62.3675 | 2025-08-31 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 517f316a-85d5-3115-9a0c-bac4f7df25fd | -9.4309 | -62.3683 | 2025-08-31 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 24ff2b28-7991-35ad-a592-e793dd771828 | -19.0926 | -48.3106 | 2025-08-31 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fb8181a8-bc4e-39fc-8f54-184b9abc312f | -9.4497 | -62.3485 | 2025-08-31 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 723d2e68-b63f-332c-9cd0-2103007a64ae | -12.3291 | -45.6971 | 2025-08-31 01:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3ecbc556-af83-33d2-a3df-0fc2edb66d45 | -11.3504 | -43.637 | 2025-08-31 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5ff30e6e-95d9-3084-a1ba-b049dbb201e8 | -3.581 | -47.5149 | 2025-08-31 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| bf8626e6-1b36-3c92-bed3-d9ef452b31e2 | -6.1665 | -43.3273 | 2025-08-31 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| e05ad672-e007-34e4-9d1b-bf3fbe90ceb8 | -10.3313 | -59.2011 | 2025-08-31 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 74fe0c34-20cc-36b9-b084-264ca59ece36 | -8.7439 | -62.3979 | 2025-08-31 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5e7f26cd-e0ea-382d-b291-3b1707da8b71 | -8.7472 | -61.8465 | 2025-08-31 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 90ddb33d-a432-3fd2-adc1-0fe24d09a4e1 | -9.0614 | -65.4355 | 2025-08-31 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 1962fee6-f5fe-3f49-a902-3874d6107f4a | -11.3509 | -43.6133 | 2025-08-31 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 35752480-0070-315e-bd32-0cd404b5ad8f | -9.4683 | -62.3476 | 2025-08-31 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a0d8cb70-4347-34b6-8c6a-6c73e3f30d6e | -9.0615 | -65.4169 | 2025-08-31 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e0ae178a-3ff4-39ca-a0a6-9666e69cbcbb | -8.7471 | -61.8656 | 2025-08-31 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 4842a9aa-baaa-3ab6-bcd9-3b9a19af2bab | -9.4495 | -62.3675 | 2025-08-31 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 4ff37b81-5070-379a-ab40-16b0784c61e4 | -9.4432 | -60.5692 | 2025-08-31 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b0f02a78-f057-3705-bd23-4c0563fed8a6 | -9.5913 | -40.3448 | 2025-08-31 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.4 |
| 68b62014-0d27-3e36-9663-dc04255a8328 | -19.0932 | -48.2876 | 2025-08-31 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 6a26ec7c-389f-30dc-986b-0a394534979f | -10.6128 | -44.3284 | 2025-08-31 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 65e5601e-9bd2-3c6f-bade-6306a67a076f | -13.3636 | -46.95 | 2025-08-31 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 5f3b4f3f-3e5e-3589-a4e6-4d7ce244c174 | -9.4684 | -62.3286 | 2025-08-31 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a25519f1-2568-378f-88fc-7c09c6c5ab2f | -19.1128 | -48.3063 | 2025-08-31 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9be81d50-a4cc-3084-ba7b-8731a1f47c56 | -10.1359 | -58.0183 | 2025-08-31 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| dc6cb29c-5c02-363f-9388-6a28c2c8c784 | -9.0614 | -65.4355 | 2025-08-31 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 76fcb571-84c6-381f-b36e-d224534b2e45 | -10.7567 | -59.8175 | 2025-08-31 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3285d6a4-f273-32a1-a36e-bf7d16510fd4 | -6.7093 | -51.4165 | 2025-08-31 01:40:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4f30c591-4222-3585-831b-7f458d7d558b | -16.2221 | -52.6778 | 2025-08-31 01:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3c784ccb-39f2-3411-a97c-b44ab634a4aa | -9.0799 | -65.4349 | 2025-08-31 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ff81c2df-79d7-355f-934f-cd36df071fd8 | -9.5908 | -40.3696 | 2025-08-31 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 623fb3b1-5e6f-3656-acd0-e2d9a6d88199 | -11.3509 | -43.6133 | 2025-08-31 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| cd900e70-f2da-3a9f-bbe5-868ae144b421 | -9.4681 | -62.3667 | 2025-08-31 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3fe68647-9183-3bd5-9fd9-ade3738ce9d7 | -3.5994 | -47.5359 | 2025-08-31 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0773a2ee-57b5-3c32-a878-9256849a9f45 | -12.0976 | -44.717 | 2025-08-31 01:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5533160f-7cfa-3aed-999d-9a4a9ec5abde | -8.6538 | -61.9647 | 2025-08-31 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9b2047b8-513c-3f07-98b2-aee2096e658e | -11.3504 | -43.637 | 2025-08-31 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 249b6e8f-1b24-3e80-8e66-22753ae0e56d | -6.1665 | -43.3273 | 2025-08-31 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c02acf88-d625-3421-9d7b-3d0a6c1811f0 | -13.3559 | -51.7642 | 2025-08-31 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| adeb91fe-e02f-3ea0-8155-baf78f16587c | -3.8146 | -48.9515 | 2025-08-31 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ba703651-455c-34d7-b4b4-7dd50ce8382a | -18.6715 | -49.102 | 2025-08-31 01:40:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e708cb53-7b31-360c-9069-cf04716af883 | -3.5995 | -47.5142 | 2025-08-31 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7d01f2a2-11cf-38d5-9ef9-55f052e6dd76 | -8.7439 | -62.3979 | 2025-08-31 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 71b8b026-96f7-31c9-9f00-dc58dab82edb | -8.7471 | -61.8656 | 2025-08-31 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 947babd6-6b46-331c-9a3d-f480046aa9ea | -9.4498 | -62.3294 | 2025-08-31 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 65eb4108-90b7-3085-99ca-c565cf896a44 | -9.4497 | -62.3485 | 2025-08-31 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 222.4 |
| dbdec8f5-0fdd-37df-911f-d21ce1f44414 | -9.0799 | -65.4536 | 2025-08-31 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6ef86066-3240-3a6f-94b2-53210597137f | -9.4683 | -62.3476 | 2025-08-31 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 157.4 |
| ff059f46-b1fc-3688-8552-056ec77f6782 | -8.744 | -62.379 | 2025-08-31 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 02194b41-0ddf-34d1-b0c4-aab270bbb10f | -10.3126 | -59.2023 | 2025-08-31 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 84f8435b-dee4-3407-970d-8a419598fa69 | -19.0926 | -48.3106 | 2025-08-31 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 392cd9b2-7579-314e-9251-0215417c9ff0 | -6.1853 | -43.3257 | 2025-08-31 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| da5b5008-b40b-3644-a850-d2f9c298ff0a | -10.7565 | -59.8369 | 2025-08-31 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2e6940a9-c591-3cee-b454-29754cf860b7 | -13.3562 | -51.743 | 2025-08-31 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e684d714-bf3f-32f4-ae86-7cbafa21d836 | -10.3313 | -59.2011 | 2025-08-31 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 37cc9dc7-c291-3721-9a25-ab9bb5e85bff | -13.3632 | -46.9727 | 2025-08-31 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 2d9fc952-5bc4-385f-a1dc-7b7fa481732b | -18.672 | -49.0793 | 2025-08-31 01:40:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 68f46ba2-52f7-3306-b66e-95af625a64d8 | -13.3443 | -46.953 | 2025-08-31 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0af32448-686c-30cc-9acf-5e7b97625ec9 | -6.7091 | -51.4373 | 2025-08-31 01:50:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d3f7b0e8-5894-300a-b278-f35d676a4a51 | -6.1853 | -43.3257 | 2025-08-31 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1f3da25d-0ea4-3809-adc9-524fa39f4136 | -9.4683 | -62.3476 | 2025-08-31 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 142ab6d8-39b9-34c9-aab1-38dd98ca94a2 | -9.4498 | -62.3294 | 2025-08-31 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 252c9341-483b-3dea-8b88-82b0f1c23332 | -9.4431 | -60.5884 | 2025-08-31 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4e990d80-b50b-3c73-9230-56cde81bb630 | -13.3636 | -46.95 | 2025-08-31 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 9e2fb4bd-a043-3f4c-b4d5-699a4759d0b6 | -10.1359 | -58.0183 | 2025-08-31 01:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ac473930-fa85-3c9f-940c-e0db2144dcc8 | -18.672 | -49.0793 | 2025-08-31 01:50:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 009741c9-07b9-3699-93ab-ce0f2720eddd | -6.1665 | -43.3273 | 2025-08-31 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 08d12f11-0cec-3f8b-8cfc-0a46dbdf81ee | -3.5995 | -47.5142 | 2025-08-31 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 428a6553-9eeb-3823-b4fb-dd92fbf85ba5 | -8.7439 | -62.3979 | 2025-08-31 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 469d41f8-170e-38db-96ba-46aa0ffc71e7 | -11.3504 | -43.637 | 2025-08-31 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| a799fadd-f1e7-3a4e-9d4a-657c5281ee10 | -3.5994 | -47.5359 | 2025-08-31 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b023d43d-b71f-3ae2-9192-0f1a0ba94803 | -9.4432 | -60.5692 | 2025-08-31 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| ebdf913b-5aa1-345d-bfd1-03b649cefe57 | -16.2221 | -52.6778 | 2025-08-31 01:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f94d3ed8-bd3f-3e92-80af-188c4776f2ac | -9.4681 | -62.3667 | 2025-08-31 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9541297c-f457-3e7b-b8b9-42db748b7f60 | -11.3112 | -43.69 | 2025-08-31 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d59531ac-5a5b-3d8e-b1f1-40b9f89d5124 | -14.5452 | -51.9729 | 2025-08-31 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 19ad29f5-56f9-358e-b989-2f3fbeb041e1 | -8.744 | -62.379 | 2025-08-31 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 5d7b491b-a0c1-38d2-8845-7ef3e7dfe962 | -11.3509 | -43.6133 | 2025-08-31 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 5e989cfa-5612-394a-91eb-482a86776484 | -9.4497 | -62.3485 | 2025-08-31 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 266.6 |
| fd15141d-de20-3b32-a2e7-73e38881eb91 | -11.4233 | -63.2444 | 2025-08-31 01:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 07162b76-a64e-3b2e-8a01-811c8ad1144e | -11.3701 | -43.6104 | 2025-08-31 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 56305231-786b-3e44-bc3a-eba2b75d72c9 | -9.4684 | -62.3286 | 2025-08-31 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 34e0eace-7ca9-3623-bb45-811c9bdb6083 | -11.4045 | -63.2453 | 2025-08-31 01:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 125493e9-e83e-341a-9662-6cee4ae6b649 | -6.7093 | -51.4165 | 2025-08-31 01:50:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 39a236ec-bdca-34db-b30c-9e5c486bf188 | -10.3313 | -59.2011 | 2025-08-31 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2a54c1f9-36ad-3a8c-a5e5-c7b048596e08 | -19.0932 | -48.2876 | 2025-08-31 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 492b0385-f989-3025-bcf7-5a80d8727211 | -18.6715 | -49.102 | 2025-08-31 01:50:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f3633832-e101-307d-8a79-417109eb610c | -13.3632 | -46.9727 | 2025-08-31 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 44c749c1-cd2a-3675-9b94-6e0913bb6c52 | -10.7567 | -59.8175 | 2025-08-31 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d564f20e-6312-3149-9fc5-d41e19cc6618 | -12.0976 | -44.717 | 2025-08-31 01:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| af59ce51-830c-3fb5-be3f-ddbe7b825af7 | -10.3126 | -59.2023 | 2025-08-31 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |


[Clique aqui para ver as próximas entradas](README10.md)
