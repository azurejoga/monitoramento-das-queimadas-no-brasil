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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81215ebf-8f1e-3cb2-b9d0-b0107b8ce679 | -3.60851 | -59.02028 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c4537d1-a3df-3fe1-b7de-496042145377 | -12.9332 | -50.93431 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a364b157-0e89-36f0-9d2b-5edbf4320917 | -3.43619 | -58.02782 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ce23354-04ec-3c50-a601-0ef4383b468f | -6.16421 | -57.7275 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ced950-a197-366b-a9a3-c5d405da24c4 | -5.35761 | -56.04584 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e551ecd8-7dc5-3e48-a727-3c66f4f92d94 | -5.98678 | -57.69588 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e90312c-fdee-3701-a099-1acf19c97b03 | -6.44482 | -48.45814 | 2026-09-22 05:23:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4a47ef4-fa64-3892-a485-bbcbc839d3f9 | -6.04663 | -57.82679 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 46efc645-0326-3cd6-bc92-fd8c36eb927a | -6.74253 | -59.07758 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d4c663a-8560-3b7b-9750-1f73cfae64d3 | -3.51745 | -56.90601 | 2026-09-22 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b89da0d0-0024-3e23-b5b3-84bf9726b6d2 | -8.79278 | -44.29388 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 25f490da-5769-3940-ba77-8fdd6e35a04d | -6.77789 | -48.66491 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f9151eb-dbbb-3005-9b2b-8aeac2679293 | -6.01345 | -47.90783 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ac382d-b239-30ce-bea3-4499625469f3 | -3.68741 | -42.96176 | 2026-09-22 05:23:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7929c90d-8b02-3f54-83f0-d4b6edb0b99b | -1.29484 | -54.21898 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56e14af6-972f-3be2-960c-c1bc7a27e0e4 | -6.91858 | -59.6334 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe5163f1-48fb-3c10-ba22-7f7d36b50fd9 | -13.91679 | -48.56626 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71392376-7b8f-30e1-bd66-1df05a37a53e | -7.58977 | -57.67648 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d5dfd47-5492-3270-bdaf-6c9dba6a386a | -12.15364 | -47.38926 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37ca076d-661d-3fc8-94c0-20cdadfd2cc7 | -6.45284 | -59.9696 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aa836c0-4b91-3f4b-8c4b-6c5a3fb8beeb | -4.34683 | -55.65677 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 203d0fdd-a478-37de-982b-cef9b872b2ea | -9.56123 | -66.0174 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b6ca94b-9c6b-37a2-84bd-9af97cbaa68a | -13.51119 | -51.52803 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 464bcf33-8642-3986-a244-08804e342723 | -6.08499 | -57.62939 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 46d54fbb-8e4f-372d-acf0-bb570ec31759 | -12.84468 | -50.98853 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca0839f1-acf1-393d-b323-55bb6d38ae53 | -4.95999 | -55.82052 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 642400b5-46cf-3857-bfc2-b5b69a860422 | -3.62545 | -54.52827 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1b8493e-a121-3342-84b8-7f69ae77a35b | -3.32735 | -59.81169 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4620de6-f739-3bd6-aa94-3cc4486226c7 | -3.44743 | -58.39366 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cf87aa9-f4df-33ac-a818-600d60a0d912 | -3.00714 | -59.36959 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad3c32c6-8104-3568-8900-e2f9aeacdfb8 | -3.39331 | -59.52224 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 117f2bae-1a7d-3c52-a5a5-ae254941f751 | -5.81182 | -57.73557 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c2210e-367d-3032-b71f-8706adf2535e | -3.11511 | -61.2649 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e43775f3-c4a0-3c01-8c84-6182ed9cd8e9 | -12.95009 | -50.9197 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5394b47e-51a9-3715-b9f6-5f913133251b | -3.21274 | -53.95578 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a234cebf-55aa-3a4d-b317-ea42f60d24d1 | -8.08895 | -55.34063 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b60711f-4242-3461-a64f-a0e9fa059ff4 | -14.75696 | -48.44397 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b419c8f2-fd2c-3e99-8529-94ed5bcdf871 | -4.51196 | -54.98138 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33519098-c055-3e43-95c4-e55bdaba5b1a | -14.75254 | -48.42941 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4515274-1e80-3e70-a0df-dfedfd9cd2d3 | -8.79071 | -44.27861 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f06a0bfd-4cad-3990-ab4f-9dce7f37ed0a | -5.75268 | -51.93204 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65f40451-194e-3cd2-9bd2-9fbd23149d84 | -8.18112 | -54.7811 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a57b77c9-5729-3d21-ac29-7648c2f5b8d8 | -6.25191 | -57.7772 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23559245-0475-3ed6-b9c4-65f4f3708366 | -12.56539 | -45.97527 | 2026-09-22 05:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 66b00371-57e1-3502-9dd9-a16074752822 | -7.57924 | -57.67836 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f05eb64f-6dca-3602-876e-eeaee008cd78 | -5.94182 | -57.69945 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66a84c7e-3801-3dd9-89c8-c6c9da3e9a06 | -10.58663 | -57.48323 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2ccc1bf-2398-333b-9de1-750117423dc7 | -3.72175 | -60.58228 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af4edd12-168a-3378-a91d-0c196e76b684 | -7.40375 | -55.22596 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd2fecfc-ab91-34fc-87e0-dbdaef3f8dc8 | -6.28558 | -56.04291 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0d609aa-814e-3794-9cec-2726495cf86e | -3.18613 | -57.88662 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ea9483e-9475-382a-bbf6-6a2e8ca85888 | -9.10277 | -67.82257 | 2026-09-22 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e31ff87e-76fa-3b16-b30b-5438a33e2337 | -5.93449 | -59.98266 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be49567a-2843-38cd-a9a5-bd5e0f7b64b2 | -5.69359 | -50.01087 | 2026-09-22 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16424e40-f438-349f-bb6a-51c133805a5b | -3.04429 | -61.26209 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27d5ac8e-b9dd-3400-a2de-86ab0b2767da | -3.44195 | -50.60398 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b8e3ea2-91d6-3373-94d0-fe2be8568a6f | -14.04496 | -52.05182 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae6a1fc9-107c-34e2-a5e4-07f073f3e19c | -4.07502 | -56.22733 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac1293f-01af-36f6-9e78-bfb707fb939e | -6.19973 | -57.78315 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6db771d9-4a6f-3155-9ca4-0411645a67aa | -1.83042 | -58.47842 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f94e11a2-e198-393f-aaa6-2654bebd838b | -7.59143 | -57.66603 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07d8d5c2-ada9-37d4-ad9d-e765b621fcea | -6.1194 | -57.67049 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62c8d7a8-929e-303a-8357-d2ba3bbb2280 | -2.86075 | -57.80234 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2bf096d7-ff99-3851-a823-778ea155fb52 | -4.77951 | -55.70158 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03ebd2aa-cbb4-39c6-ae5c-16eed2b9ee0e | -4.42907 | -55.4417 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a826dafd-b7dd-3960-aa30-5905400575b0 | -2.94323 | -50.49263 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93cda4bf-d5f8-3fb3-ab79-c7c177a1cfb8 | -2.31361 | -50.45448 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e34b5a49-18db-31b4-8289-888d5f2c7583 | -3.40046 | -59.52338 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea513676-6455-30dc-bd91-4d88211aa3a1 | -6.73092 | -55.62563 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 089b53b3-d5e1-3faa-a326-460bbb987888 | -3.86889 | -51.1863 | 2026-09-22 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c398b68e-5415-31ed-96f6-e42fd8cf9ec4 | -7.6072 | -55.35401 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e867521-70d5-3e0f-87f4-1ee5db4a57f2 | -3.47361 | -59.59326 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f56b36fa-7ddf-3815-a42a-b8abfcfbe44f | -11.32373 | -54.04075 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6486c96d-4a8d-3f02-9c65-79571f602de9 | -5.85959 | -49.77582 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3a8ac16-ed9b-3add-b557-1836542dc206 | -6.39757 | -55.25798 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93d7837f-5b2d-384e-9c03-2bd3bcc694bb | -9.10207 | -67.82626 | 2026-09-22 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b23e796c-ad78-3e82-b860-db4d327c148d | -7.58645 | -57.67594 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59e73533-4720-3894-8808-d07b14bd6b99 | -6.43936 | -55.63824 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5590ef0-6891-37a7-8c82-167d7922bb84 | -6.38368 | -55.27901 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c0636f8-f81b-3fab-98f9-c3ec7ba6f4ac | -2.16587 | -47.88589 | 2026-09-22 05:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 644139bf-2d5b-39f8-a373-d43e954d7961 | -3.00923 | -54.17458 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6da5b684-f2b1-3b09-ba56-7d8b40d5ff26 | -6.86393 | -59.90493 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c4e91ba-aea0-3a83-88ce-8370e0d67d26 | -2.93737 | -57.80695 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f964e20-fa86-3b32-bc2f-5a03f5a6bce9 | -12.89062 | -52.06811 | 2026-09-22 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5761c361-8bfc-30f4-91cd-a8d9055e53f2 | -2.9629 | -57.62565 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f70a25c-9557-3ba8-8c38-d604627c01d2 | -3.6516 | -58.86335 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff8d1a45-ab5d-3540-b2df-263e45cc7fe1 | -5.8548 | -49.77508 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b95e6c7c-45a1-3eff-ad14-e4849898235a | -6.36092 | -58.28021 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c562e8c-181d-3ee7-92cd-d4d34946e60f | -7.39674 | -55.22495 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d65c05a9-6af6-3f74-8c48-6be303a99f46 | -4.05516 | -56.30978 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0912688d-e3dc-34b6-b541-e29cb95743c1 | -12.95906 | -50.98366 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f094237-c372-33e1-aeea-49b4b29c8866 | -7.24739 | -55.59584 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09675963-60ac-36bb-8fd4-11ac7899a45d | -6.48855 | -57.87947 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db043074-6c45-372a-a263-d69b0646fe27 | -12.79556 | -54.04997 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35e52312-d837-35b9-8125-37072b53921b | -9.39818 | -65.92175 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d40f656-e984-3290-aa82-537b383ec4fe | -6.09886 | -57.62802 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1320c98d-4aad-39f6-b4d1-1ee7385346d2 | -3.58649 | -59.06789 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7da476d6-df11-3cbc-991d-39ca52acbca2 | -8.32677 | -50.83778 | 2026-09-22 05:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 365ef638-a11f-3969-b9b1-b2a4dbb6ae2c | -2.95717 | -57.72629 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f35e2a8-1884-34b6-be75-1d7b2fcf445e | -5.984 | -57.77756 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README94.md)
