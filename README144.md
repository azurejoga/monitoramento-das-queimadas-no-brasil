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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdba8796-7fe7-38f3-8995-384c9306a0ee | -6.9223 | -42.9323 | 2026-09-23 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 5f9d85e0-4fd3-3530-960b-1cebc8ce1815 | -9.8307 | -48.451 | 2026-09-23 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 562f7a58-fa15-3e02-a7fd-871845510296 | -7.4286 | -44.7409 | 2026-09-23 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| aaed1c01-db3d-3628-876d-937718f69b4f | -6.5763 | -45.4968 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b0544ec9-8f0d-30c2-b5b8-a4a8ac39c300 | -6.6127 | -43.7549 | 2026-09-23 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1e206d21-aff2-3262-8c4b-f8913c68aa6f | -2.9341 | -57.7786 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 0c2a79c5-3f65-33aa-acc2-ea63092cd4d2 | -3.1541 | -57.6772 | 2026-09-23 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5d9eb451-9359-38b0-8e14-c83a6a874326 | -6.5056 | -45.0723 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 41390625-3acc-3763-94f5-7661165ca7f5 | -6.5963 | -59.9087 | 2026-09-23 14:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ce89c48d-3954-3379-9637-213afeb9df22 | -9.3794 | -48.345 | 2026-09-23 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a8754759-c098-3f26-9313-f192fcffdfec | -7.0352 | -44.6396 | 2026-09-23 14:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 72f3dc01-eba1-3686-b13e-80b2645d5471 | -2.5687 | -57.5135 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 56202524-bd4e-3ecf-95bb-71a3e43cefde | -6.2036 | -45.3227 | 2026-09-23 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 272e1b74-77ab-3f33-b071-9e0b3e4906f6 | -2.9157 | -57.7983 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b65d7856-c9cd-3b4d-90b1-37cd7478e961 | -6.5829 | -58.9851 | 2026-09-23 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d8237072-3db3-3b4f-99a3-00332f4f3271 | -8.9016 | -45.933 | 2026-09-23 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| d1743562-29f5-378b-817b-a1334bb73ec3 | -9.406 | -47.7507 | 2026-09-23 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 246ee253-b3fa-34f2-880b-220aaaf83f62 | -6.1361 | -59.9063 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d207cad5-40c3-394d-b2ad-72977f36c5f4 | -7.4097 | -44.7427 | 2026-09-23 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e37eb890-2276-324d-810c-cbf59a6fc971 | -6.467 | -59.9902 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 25ae04f8-4b05-3292-ba10-8273d67f549d | -2.8974 | -57.7987 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b46dcd18-38d0-3e23-9e34-c133ce3caa96 | -11.3551 | -43.3764 | 2026-09-23 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 463.3 |
| 3cf1611d-2a9c-3636-af7b-790f353de64b | -6.2208 | -41.6651 | 2026-09-23 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| fd3163c2-1d54-3b11-94e0-002042e139bc | -3.4059 | -59.2155 | 2026-09-23 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| fed1746e-4a29-3914-ad03-d79048e82704 | -6.8839 | -46.5694 | 2026-09-23 14:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9a62c767-ab23-3d48-81df-0040587169c8 | -9.925 | -48.4628 | 2026-09-23 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 97f96d0b-6ac7-3bfb-8aa5-d049aa93d832 | -6.1317 | -45.0109 | 2026-09-23 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8cae55b2-31bb-3bcb-98c1-baaab4602673 | -3.4058 | -59.2347 | 2026-09-23 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 63c26252-9121-3ab7-94a8-f314453bb68c | -11.4018 | -47.3628 | 2026-09-23 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| fea0bb01-808c-3aa5-99a1-285520eb23bc | -6.5639 | -44.8628 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f7907b2f-b05e-322b-b584-c18080a3d0af | -3.3321 | -59.4469 | 2026-09-23 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a9420c86-1956-37ea-9e3f-5109749a81b3 | -6.5953 | -45.4727 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 87833924-5de7-3c16-ba40-7085298a85e8 | -6.4485 | -59.9909 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b3fadf36-c9de-3881-9519-07b5113dd5c0 | -9.3797 | -48.3232 | 2026-09-23 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| f160e79a-aa4a-3edb-bc72-5f73e8b1daef | -3.4635 | -58.3096 | 2026-09-23 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f567bdf4-e30c-3568-be8e-f92eabdcbf0a | -9.5463 | -45.7708 | 2026-09-23 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| daa80785-f597-3c01-a05b-08c5f482c8b7 | -11.1204 | -48.327 | 2026-09-23 14:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 281159c5-7e86-3393-b67c-79167aa50d06 | -8.7772 | -49.955 | 2026-09-23 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 82898270-6d7b-3dd1-9076-d85d23842f65 | -8.5992 | -44.5301 | 2026-09-23 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 352796c7-3155-3806-9c5b-7982f9ac497a | -6.3015 | -59.9387 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e9d3018e-e531-355f-8926-079d5901b3d0 | -6.2832 | -59.9202 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ea00640b-d6a8-3555-8ba3-bd9c84d13c5f | -8.4983 | -57.6271 | 2026-09-23 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 1e336b26-bd26-38ee-aa4f-aff44d98c5e2 | -8.3591 | -45.6056 | 2026-09-23 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 409.3 |
| 11bc4505-f3f6-3fc6-b300-37e58841dad2 | -5.9985 | -45.2476 | 2026-09-23 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| eeb235bb-ff20-39a3-9bbe-d9fed449ee0d | -8.7537 | -44.2821 | 2026-09-23 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 52f80a5b-b941-3a9d-9cb3-bcc3f48de425 | -3.2955 | -59.4284 | 2026-09-23 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3ea70dd4-42de-361d-b407-ea039b56b64f | -9.9067 | -48.4211 | 2026-09-23 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 7e23f761-275d-39f1-b5d7-5b699365461f | -6.8841 | -46.5471 | 2026-09-23 14:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 88e02241-997a-38e2-ae56-a96b55c77cd5 | -6.5444 | -44.9327 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 74f1c616-10ce-3473-bb96-0ba7b5e9f683 | -2.8608 | -57.7994 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 9f26311d-660b-3242-a25a-089493a71ea9 | -6.4366 | -48.4653 | 2026-09-23 14:50:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3abc1b75-cd58-387b-8f14-7b1d9a5015f4 | -8.4985 | -57.6075 | 2026-09-23 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 2e11f8cd-4f73-3c52-810b-8acec0d01794 | -3.4599 | -59.5209 | 2026-09-23 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 692e8de6-aea5-3aa3-bb86-fee09dc594f8 | -3.3138 | -59.4472 | 2026-09-23 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| aa1d1713-d687-3d67-8c6d-39f3659347ca | -6.8951 | -59.2235 | 2026-09-23 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9333b525-58de-3249-a8b9-44ae0726f189 | -11.3784 | -44.2195 | 2026-09-23 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 0eaf5500-d805-36c7-9295-85bfb3754c81 | -7.8811 | -61.1779 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5cbc83d9-a113-3e75-b7af-01d8149ccaca | -6.7124 | -58.9219 | 2026-09-23 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 917bcaa9-aa86-3ac3-a4b0-da4c25374f47 | -6.5761 | -45.5194 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 07cdd8c2-23ff-3f72-a4f8-9892d9a8babf | -2.9157 | -57.8177 | 2026-09-23 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9bace5d7-96be-3ff9-bcc8-1a1d356f8abe | -3.7167 | -54.1896 | 2026-09-23 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 73413bdc-9201-31b8-af08-9afbef9c2ad8 | -8.0279 | -61.3626 | 2026-09-23 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cc354bb0-7aa5-3749-8bf3-2abafa9d68b6 | -11.3976 | -44.2167 | 2026-09-23 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 497.1 |
| 2e5b1715-769d-325b-92d1-98902f71e0c2 | -6.922 | -42.9559 | 2026-09-23 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 512dd79b-62cb-39a5-a47c-a834b1818698 | -5.9987 | -45.225 | 2026-09-23 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6bce3bcd-557c-38bb-b560-e912d8ef7cab | -6.1849 | -45.3241 | 2026-09-23 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fad18f24-6aac-39be-9f02-d160ae8cc0d3 | -6.3199 | -59.9381 | 2026-09-23 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 0ecbe048-acc4-332c-a704-612700e8320e | -6.5636 | -44.8856 | 2026-09-23 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 452c978c-c98f-3594-8e26-a5dfd8e436da | -8.7584 | -49.9566 | 2026-09-23 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7d94cdb8-e78b-355a-b360-e7e4fa4fce1a | -6.9228 | -42.8852 | 2026-09-23 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 1fcf8421-21cc-3e40-9d53-9d61742d849a | -5.9987 | -45.225 | 2026-09-23 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b19a2a89-bcb2-3325-b59e-18a85f4103d4 | -8.0093 | -61.3824 | 2026-09-23 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 44384442-bf72-3c8f-b444-f87b94badb27 | -8.3591 | -45.6056 | 2026-09-23 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 7b1e35c5-7ead-3fc0-a2e3-4828a0b43b7a | -6.1849 | -45.3241 | 2026-09-23 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1a083fd6-ae39-3136-9175-85adac16653b | -6.5636 | -44.8856 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8c288a3a-879f-317c-aac7-a3da71ec17b8 | -6.2036 | -45.3227 | 2026-09-23 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6fcb34f5-3a58-3892-b989-2d8e28967c88 | -7.4097 | -44.7427 | 2026-09-23 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 517bb2a1-be9f-3c7d-a4bb-7ca0f3992183 | -2.8609 | -57.78 | 2026-09-23 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6686cb52-5844-38ab-9b40-560511df77dc | -8.8108 | -44.2525 | 2026-09-23 15:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 176d3440-05d6-3799-9a99-35602ee1e42e | -2.7713 | -57.0229 | 2026-09-23 15:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 905275e4-3668-3256-acd8-b12af15c7798 | -8.8735 | -49.7328 | 2026-09-23 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| af3be1f8-bee9-305c-8c29-fa62e7b2ffcc | -7.4092 | -44.7885 | 2026-09-23 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 5968dc15-2192-3e73-a46e-a3d63552e2f6 | -8.449 | -47.4938 | 2026-09-23 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 79d41720-fb24-3205-82d5-1849dc46289f | -6.3015 | -59.9387 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 92659e5f-62e8-3ead-8d9c-0af3d9d311b5 | -6.8951 | -59.2235 | 2026-09-23 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1116bb6b-c577-3043-975f-96012c6d02f3 | -6.9223 | -42.9323 | 2026-09-23 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| c3ce8aea-03c2-328a-8a32-1753e1f09adf | -6.4368 | -48.4436 | 2026-09-23 15:00:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 48740706-e097-3df3-aaa9-c4f7486034b3 | -6.5449 | -44.8871 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5b8a337c-7bd5-3920-8e1c-eef6af593ff6 | -3.4635 | -58.3096 | 2026-09-23 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4d03e6af-828a-38ae-a01c-a7e29c96f6d7 | -9.8118 | -48.453 | 2026-09-23 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3d034a28-d3ea-32d0-81f2-ddaea3c71ee5 | -6.2832 | -59.9202 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 64c34676-eca1-30aa-a004-e4d252ded0ff | -6.5953 | -45.4727 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a1f955ff-7536-3095-959c-445da072fc07 | -6.3199 | -59.9381 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 82853809-2292-3958-8764-6479c4d69494 | -7.1014 | -42.0849 | 2026-09-23 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 48d24b50-b22c-3383-9229-2b3208256fcd | -5.9153 | -59.9139 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| ac6e5ef9-c983-37a3-8ee0-442adc325316 | -7.0352 | -44.6396 | 2026-09-23 15:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 26714262-0731-3fd4-bba7-9da52232c074 | -6.3197 | -59.9764 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 3cacf6e0-c4bd-3c46-b27c-c2bbe75b49c0 | -6.4302 | -59.9724 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 46e91235-3546-3786-8e88-a6a851fac31e | -7.8406 | -61.7887 | 2026-09-23 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 293ab60c-2e04-3d06-9118-7c0b357dd317 | -2.9525 | -57.72 | 2026-09-23 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |


[Clique aqui para ver as próximas entradas](README145.md)
