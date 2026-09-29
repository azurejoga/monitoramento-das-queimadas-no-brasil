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
| 63af1717-87b2-3786-aa80-949b614b7de0 | -11.1707 | -50.0581 | 2026-09-29 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 77152bbb-3a5c-34e8-9e8e-49a67cd7c120 | -7.83 | -45.793 | 2026-09-29 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2b82facd-4c8b-379c-8eab-7561b439d24f | -11.1894 | -50.0775 | 2026-09-29 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c3be4f7a-eccd-3498-91b2-bfe612137d4e | 1.8403 | -55.6046 | 2026-09-29 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| eeb9bbd9-bd3a-341b-ada5-2f2b0c37dc50 | 1.6567 | -55.8833 | 2026-09-29 00:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| dbd408a4-87ad-3d96-bdf0-48a6c073d367 | -18.5885 | -48.415 | 2026-09-29 00:00:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.5 |
| bf508119-3434-3666-b856-42280b05a96a | -18.5684 | -48.4191 | 2026-09-29 00:00:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.9 |
| ea910cd1-363c-3c14-8edb-cc86e611b879 | -10.8426 | -60.7429 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 154.6 |
| f6801c6e-7e60-3b76-9708-2d01a297174a | -5.7374 | -45.176 | 2026-09-29 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 15377369-d342-37b0-8d99-a0502cb89ae5 | -7.8488 | -45.7912 | 2026-09-29 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9a7ffc83-50cb-3cd9-a49a-eddb5acc3c45 | -11.1897 | -50.056 | 2026-09-29 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 321.3 |
| 858316ef-a6e6-3ca3-ab90-bf9bb99c3470 | 1.8403 | -55.6244 | 2026-09-29 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4cb44608-bf93-3ebe-b8d7-4c55b9b920e9 | -8.5738 | -66.994 | 2026-09-29 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 92da2b0d-1967-30c0-b735-687f4967334e | -6.6812 | -55.1103 | 2026-09-29 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0b8faea8-d728-31d5-a8a5-ac2d67089210 | -7.6158 | -46.4628 | 2026-09-29 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e7883d3d-9f25-34c7-8b60-741c2fcf37c4 | -11.3823 | -54.0434 | 2026-09-29 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 22731f81-eca7-38cb-b845-39af639568fc | -10.3707 | -61.2513 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| cb49cbd2-e443-3ded-b810-403af3b5e139 | -10.3894 | -61.2502 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 211.5 |
| b1d750a0-8d46-35a3-a9e8-6a341fc0a38a | -11.2084 | -50.0754 | 2026-09-29 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7172582d-6d53-3979-9aad-fdae51c80c31 | -18.1042 | -42.6424 | 2026-09-29 00:00:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 175.6 |
| 5dd61835-4a4a-3be7-bc33-be765f2b7069 | -15.0919 | -53.9282 | 2026-09-29 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| dcf212f5-b630-3db6-b825-ca94a667f7c7 | -11.2087 | -50.0539 | 2026-09-29 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| a2559ed5-a9d1-3f45-ab41-cec2c2a1c83f | 1.822 | -55.6247 | 2026-09-29 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e004fe1f-2384-31c9-a8d4-08e01dbb0abf | -6.2949 | -43.6194 | 2026-09-29 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a8a14767-cf3c-3e75-9b46-5cdeabe9a2f4 | -10.3892 | -61.2695 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 76ff2087-63a3-354a-8d87-2aabb5289791 | -18.1244 | -42.6373 | 2026-09-29 00:00:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| 22d0fd62-f3f2-39f0-95c1-98f88af5f2e7 | -7.8483 | -45.8363 | 2026-09-29 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 5955a6f3-6f22-3694-a79f-0739829599e7 | -11.382 | -54.064 | 2026-09-29 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a211b4ea-3753-370a-8ab7-1b71f0fb0e8e | -3.0876 | -50.2691 | 2026-09-29 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f2122026-62ab-301b-a309-876990301b25 | -7.8297 | -45.8156 | 2026-09-29 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 639568f4-b076-32ec-824a-3eb065417d55 | -4.2954 | -49.0807 | 2026-09-29 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| bcbe4f0e-3f3d-3c50-846e-d4b49a712abb | -18.1049 | -42.6174 | 2026-09-29 00:00:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| 25f08b2e-1d84-35fc-8386-3c5e2ddd03aa | -10.4079 | -61.2685 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 63280084-7975-35e6-80e5-55d41a4cc154 | -7.8486 | -45.8138 | 2026-09-29 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 337.0 |
| 901fbeec-b77b-3655-a97d-5ce263aa7fb2 | -7.7025 | -48.8667 | 2026-09-29 00:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 09479099-2652-3083-8f3e-30b18b7bdaef | -15.0926 | -53.8862 | 2026-09-29 00:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d2a81237-8f3e-38d4-abda-06d626af5ce0 | 1.6566 | -55.903 | 2026-09-29 00:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c9fdf73c-fffb-3257-bd74-ead6530526a5 | -9.1256 | -67.8507 | 2026-09-29 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3524d7f9-75a0-3bee-911a-2983424dc186 | -10.3705 | -61.2705 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 0cc3e1cc-b563-338a-956d-ba2a131f6d17 | -8.5738 | -67.0125 | 2026-09-29 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a3f50aa8-63b2-3c98-9f55-233f93fb984d | -11.4009 | -54.0622 | 2026-09-29 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 4dc747db-a102-3467-bb1f-de2c385ec7ab | -11.4012 | -54.0417 | 2026-09-29 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 8a0d81e6-b4fd-318f-b509-18f547ced14f | -5.6081 | -45.0038 | 2026-09-29 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5d8148e1-339a-3f0e-99d9-f10b9cc548d9 | -15.1116 | -53.9048 | 2026-09-29 00:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9c9a0220-55f6-3f71-98de-e10dca3e6506 | -3.0875 | -50.2901 | 2026-09-29 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6e5ee726-27c1-3235-8d04-37666f8d5ee3 | -10.8424 | -60.7622 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 7231709d-8871-3617-af97-3ec1c5840506 | -9.9266 | -60.7171 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0ec50936-3181-3abd-ae37-fdaba0e9efed | -11.3633 | -54.0452 | 2026-09-29 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| b5ff7a82-0994-3fdd-ab97-99e6697ccddb | -9.9595 | -50.1431 | 2026-09-29 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7c72a3ee-a877-3dac-a6d7-f36f07cfd2bb | -5.7384 | -45.0626 | 2026-09-29 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 37ec9aaa-02ea-3ccd-b51d-2d0d37844a58 | -6.2947 | -43.6427 | 2026-09-29 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 1330788c-bcb4-3e03-978c-12be2844bf9f | -15.0923 | -53.9072 | 2026-09-29 00:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| fa4e98d5-864d-3108-9412-37483dd41b27 | -10.4081 | -61.2492 | 2026-09-29 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 2471fa9f-0a30-3f60-ad6e-dffb7773d2ed | -15.1116 | -53.9048 | 2026-09-29 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 14a8ad1a-586c-3bd3-bca0-6bdfd2c7a4b2 | -18.5885 | -48.415 | 2026-09-29 00:10:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| aa77c414-ad5c-334e-a631-20406878ad72 | -11.4012 | -54.0417 | 2026-09-29 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| eb675c4a-4afa-3cf5-bfd8-264a6d837ce2 | -18.1049 | -42.6174 | 2026-09-29 00:10:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 152.9 |
| bf229088-5cce-3b2a-8fb5-504d6e1fd348 | -9.9595 | -50.1431 | 2026-09-29 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 49ffbf7f-b897-3b30-8c5e-44f4200f7161 | -11.1897 | -50.056 | 2026-09-29 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 36896c0d-9168-3004-82fe-b70926520d44 | -8.5738 | -66.994 | 2026-09-29 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 33ecfdea-28f2-353b-a603-d89a126052f0 | -15.0919 | -53.9282 | 2026-09-29 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 1ca1a4fd-200d-3650-95f3-2391b22b80e6 | -11.1894 | -50.0775 | 2026-09-29 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 31d8c839-f248-3241-9896-84dfdc791410 | -6.2947 | -43.6427 | 2026-09-29 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 272767dc-2e1c-3283-9fed-0a1506362abe | -6.6627 | -55.1112 | 2026-09-29 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e5e390ee-c11a-3b1d-915f-13da5d27b880 | -11.3633 | -54.0452 | 2026-09-29 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 2a6d066c-524a-35a5-b46c-fe32950cda33 | -5.7374 | -45.176 | 2026-09-29 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6d1b0f57-fb49-34cc-bb99-229555d2ceeb | -9.9568 | -59.2629 | 2026-09-29 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 98ead30f-cca4-3960-9d55-fe538eaa5a87 | -18.5684 | -48.4191 | 2026-09-29 00:10:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| 36b82e8f-7160-3528-a3ae-d8f0e824cafb | -11.9929 | -50.9913 | 2026-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4f130b95-5e29-3335-a9e2-cb590de60fca | -15.4389 | -46.1404 | 2026-09-29 00:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 012a9e43-0202-3def-aeb2-8842811b308b | -15.0926 | -53.8862 | 2026-09-29 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 4a85c45d-a5aa-33b4-9067-fd00daab3ef4 | -11.1707 | -50.0581 | 2026-09-29 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eeee0808-87ba-30d5-a7f0-e4105098f720 | -9.1256 | -67.8507 | 2026-09-29 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 39314e63-4545-32d8-b5df-66bc1bae30a7 | -7.8488 | -45.7912 | 2026-09-29 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d953a9a0-4af3-3f8f-a5ce-557b2378b97f | -18.1244 | -42.6373 | 2026-09-29 00:10:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| 253a87d1-2529-3cc8-a415-0f17be73b51f | -9.9266 | -60.7171 | 2026-09-29 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a7ab458f-0c35-33bc-863a-f7f9aa9782c2 | -15.4585 | -46.1367 | 2026-09-29 00:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a755d47a-a481-3612-9d33-65384d1195d3 | -11.4009 | -54.0622 | 2026-09-29 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| eb50fba7-b32d-388e-ac73-0384ea1fd079 | -11.1775 | -44.7832 | 2026-09-29 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| eb065268-b669-370d-b3b4-6fc1a74afcb1 | -7.8297 | -45.8156 | 2026-09-29 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 04f49fa9-91ff-3716-807c-ff892aac88c0 | -7.6158 | -46.4628 | 2026-09-29 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b1af8998-2fb6-3ec0-81f5-84224112cf9f | -7.8483 | -45.8363 | 2026-09-29 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ef6279f9-88da-316e-94bd-f5c4de0c327a | -18.1042 | -42.6424 | 2026-09-29 00:10:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 208.0 |
| 652ef50c-6967-3aa9-b406-662d372f8b49 | -8.5738 | -67.0125 | 2026-09-29 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4f5e6087-6394-3da2-81b3-5bec830432f2 | -6.3287 | -52.6174 | 2026-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3e10a7ee-b36c-3653-a0d7-f362fdeefbdc | -6.2759 | -43.6442 | 2026-09-29 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 51f28f3e-8423-39cf-97ee-0c685c370c10 | -6.7055 | -45.6892 | 2026-09-29 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ce8a3735-3e71-3689-a226-1e8afad375a0 | -11.2087 | -50.0539 | 2026-09-29 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| da0fff18-fe99-373e-a7c0-04474c96e8d0 | -6.6812 | -55.1103 | 2026-09-29 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b1f8919c-bdcb-3782-b180-bff6d53c2330 | -6.2949 | -43.6194 | 2026-09-29 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 53d2ba0f-e2e3-3218-8c87-2a8984acd075 | -12.1202 | -57.1767 | 2026-09-29 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 491ae5fd-b58d-3a93-8317-e3dcd8f156cc | -6.3101 | -52.6184 | 2026-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 87426f32-6de5-3f2b-8576-c6a3ceb38670 | -6.31 | -52.6389 | 2026-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c0015704-d0e0-3476-8e25-b32bf0e0cb7f | -15.0923 | -53.9072 | 2026-09-29 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 389.1 |
| 0f79951d-2e76-3284-bd60-c13e3dea1002 | -11.9739 | -50.9935 | 2026-09-29 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a847ef8e-fbdf-3620-8e4d-31fd2641adbe | -5.7384 | -45.0626 | 2026-09-29 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2dd912cf-aa91-36b9-b492-c8807a269d10 | -5.6081 | -45.0038 | 2026-09-29 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4dc7ad8a-cf7b-35ca-9078-a2e0942b4674 | -7.8486 | -45.8138 | 2026-09-29 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 395.9 |
| 666ff8a6-40bc-35cf-ab31-56aaaf63e7f9 | -4.4507 | -47.9112 | 2026-09-29 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ae634590-2f42-3eac-be57-58336ba360fc | 1.6567 | -55.8833 | 2026-09-29 00:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |


[Clique aqui para ver as próximas entradas](README2.md)
