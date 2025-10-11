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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03507758-cd0b-3d10-b308-233e0ea79e5b | -12.238 | -51.1545 | 2025-10-11 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8fc2541a-5330-3d9d-bdac-db6c93fc49ff | -8.1996 | -43.3189 | 2025-10-11 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 6090011d-2ce9-34ae-95a3-6650e8bdb93b | -8.4838 | -46.1789 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| a8eb19f9-f41d-36ab-aad7-2730263c04b2 | -8.4833 | -46.2239 | 2025-10-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b23f45ca-7be6-398c-8747-2d7165979246 | -17.2722 | -46.8932 | 2025-10-11 02:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 3c88f68d-7b0f-39ef-80e9-c4fbe65a68a6 | -13.2257 | -42.317 | 2025-10-11 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 53b17b92-0488-3cb5-83cb-a42d841efda2 | -13.2057 | -42.345 | 2025-10-11 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 157.1 |
| bee7d296-c83a-30a4-b1ff-85360ab94618 | -7.4616 | -46.8542 | 2025-10-11 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 5d7550e5-1ddd-31e5-aa59-47a877cbafad | -13.2057 | -42.345 | 2025-10-11 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 169.1 |
| 9c549906-47ef-33bf-bd48-68ffae6ce3d3 | -5.852 | -42.8608 | 2025-10-11 02:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 3e4f8e22-62ca-3fa0-94fc-45ab157c898a | -8.1996 | -43.3189 | 2025-10-11 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 251b111c-b78b-35e3-b8fb-5969a508fd2d | -17.2722 | -46.8932 | 2025-10-11 02:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| d605de96-e299-3278-9ee2-3c7efb3b6405 | -8.4838 | -46.1789 | 2025-10-11 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ba37ef52-c138-3a62-9b07-4ece6f7ba6cf | -8.5024 | -46.1995 | 2025-10-11 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ce1b26b1-0d3c-3af6-bbcb-0b20cdb10169 | -5.8522 | -42.8372 | 2025-10-11 02:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 08685b0a-cafd-32d4-98aa-a6504c4fe255 | -8.4835 | -46.2014 | 2025-10-11 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 14318ee5-028c-3bb3-8596-3f3d737a8e80 | -8.5027 | -46.177 | 2025-10-11 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 50ed386c-24fb-3490-a3b2-d46f0e68fd83 | -5.871 | -42.8357 | 2025-10-11 02:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 46a5544a-b3ac-3741-b216-b64aa0c35709 | -5.8708 | -42.8593 | 2025-10-11 02:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 198.0 |
| 0ad7c7b8-5e7b-3b7d-8a77-7087742343fb | -13.2252 | -42.3414 | 2025-10-11 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 180.7 |
| bc639421-edf9-32f7-aedb-909317b61160 | -5.8522 | -42.8372 | 2025-10-11 02:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 221ee088-ade9-3aef-8d8e-5261434af4fc | -5.8708 | -42.8593 | 2025-10-11 02:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 150.5 |
| 5b460c61-b5e5-3bf7-8cba-f0a5db74d12b | -17.2722 | -46.8932 | 2025-10-11 02:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 685548e6-eeca-33e0-8f01-fd4e9ca5d9e1 | -13.2057 | -42.345 | 2025-10-11 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 8a1007b2-7e08-3d25-8854-37af453dfffd | -5.852 | -42.8608 | 2025-10-11 02:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 177.5 |
| 736c272b-46b8-3e2a-89f5-227eb90ad0d3 | -5.871 | -42.8357 | 2025-10-11 02:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 0cf0cda7-d13f-3843-a88c-70076ed08e92 | -8.1996 | -43.3189 | 2025-10-11 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 463fcfda-7baf-31a4-863c-8bff6f7d40fc | -13.2252 | -42.3414 | 2025-10-11 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 149.7 |
| 1e7ba3bf-1ceb-39fc-a02f-3b75dd80f83a | -8.1996 | -43.3189 | 2025-10-11 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 6c88d555-d7c3-36ec-a94e-2d4272684ed2 | -7.8642 | -44.4922 | 2025-10-11 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0e9991c4-344c-3ffb-9115-66e6f69f33ca | -5.8522 | -42.8372 | 2025-10-11 03:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| e4531b0d-b401-363a-b171-16e1ec5724cf | -13.2057 | -42.345 | 2025-10-11 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 130.5 |
| abf14d2d-2a31-3e16-98b4-6919156c9ae5 | -5.871 | -42.8357 | 2025-10-11 03:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 3f3cf5d5-020d-3e8b-a6ed-453980a44399 | -5.852 | -42.8608 | 2025-10-11 03:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| 4991c274-a900-3df5-bff9-a25d6f9f1327 | -5.8708 | -42.8593 | 2025-10-11 03:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 139.4 |
| f1892d42-9f0a-3f3f-b0d8-e53486562ffb | -13.2252 | -42.3414 | 2025-10-11 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 6693ba98-a16a-34e6-a448-3538fb375e27 | -17.2722 | -46.8932 | 2025-10-11 03:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 47725707-7e14-3797-bd38-3bdfcbb798da | -5.852 | -42.8608 | 2025-10-11 03:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 84219ed4-f04d-3165-8c49-f58c56cc9931 | -5.871 | -42.8357 | 2025-10-11 03:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| f9215ff4-b478-3951-ba62-3fec537ced92 | -5.8708 | -42.8593 | 2025-10-11 03:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| d9effd7e-7a97-327e-94f2-af930d1f9cde | -13.2252 | -42.3414 | 2025-10-11 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 5b1890b6-fb49-356b-8da8-3a67b6b42e15 | -13.2057 | -42.345 | 2025-10-11 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 518c3bd8-da98-38ec-b670-e99b5c0483a3 | -5.8522 | -42.8372 | 2025-10-11 03:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 551ed012-ac99-3e8b-9920-bc68296f598b | -17.2722 | -46.8932 | 2025-10-11 03:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 4dc143f5-85a5-3cd8-b370-1c1d96441e25 | -7.41022 | -42.98393 | 2025-10-11 03:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 26c5ef85-02dc-341b-b779-3520caed6e1b | -8.21184 | -43.35426 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 37515100-d5d9-3325-9e6a-7da960bd5995 | -4.53434 | -38.46608 | 2025-10-11 03:19:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ee4ec602-4297-38e4-a2e2-4f90994f66e1 | -8.19234 | -43.33039 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 93ead22b-f062-3833-b25c-0e0193c07f05 | -3.12656 | -40.99493 | 2025-10-11 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fb4a08dc-ba22-3a62-9463-2de1b31cc7a2 | -6.23021 | -37.44424 | 2025-10-11 03:19:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0eb6c0b3-624c-3223-8f0b-31eade9dd081 | -6.0405 | -42.5061 | 2025-10-11 03:19:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 92e9faa8-49f0-3e39-b3b5-6548d7e79a79 | -8.21107 | -43.34875 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7d827aa9-2953-388d-96bd-91195043b25e | -6.18812 | -39.69978 | 2025-10-11 03:19:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c1d4005-37de-3f7d-bd69-32fe9ef2910f | -8.49214 | -40.75509 | 2025-10-11 03:19:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 45536517-ef35-36b6-8305-ba3aa6b796e9 | -5.15378 | -38.05813 | 2025-10-11 03:19:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62dfcbf8-c3ad-31aa-94d6-1b38e1b23374 | -6.22967 | -37.44731 | 2025-10-11 03:19:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 10695d4b-867e-3382-9109-d88611f837ea | -3.13218 | -40.99609 | 2025-10-11 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80aecec2-3289-3ffe-aec4-8f135a87a2f5 | -8.2009 | -43.32461 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 277fe39c-d5e3-3d17-adb8-1320ff65e7c7 | -5.58804 | -41.10777 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 11ea8885-9899-3f61-bbd6-899e3fce7031 | -8.20388 | -43.3475 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cabaf604-6974-3c79-995c-69448aec03be | -5.40813 | -40.9912 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b6d07a5-5aaa-3e99-8990-166ef57d1485 | -5.86726 | -42.85291 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| d3611449-a8b0-3510-975e-a5ed91c23012 | -3.97961 | -40.92105 | 2025-10-11 03:19:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4c1d12c-ccab-3fa6-85ac-c457f90f10b9 | -5.8528 | -42.85027 | 2025-10-11 03:19:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e11c6fa0-5b71-37f5-9e4e-a386bf624d4f | -7.36249 | -38.75858 | 2025-10-11 03:19:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ffad2d1d-a300-35bf-b573-1ee2a5cb1c5a | -4.53209 | -38.46614 | 2025-10-11 03:19:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 58c5e000-2226-3889-9fa1-536223c8cfe7 | -5.85288 | -42.85769 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 77bc102d-11df-3d99-83fb-5746c16dbb70 | -5.58699 | -41.11372 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d0b9c160-3fc0-3efc-bbd7-1c3ce8bc0afe | -7.41159 | -42.97679 | 2025-10-11 03:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1b6ca534-f793-3d1f-af52-c4dfd277458c | -7.65833 | -42.57877 | 2025-10-11 03:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ce4df2af-d925-34d3-8c5e-7e95cce45dbd | -4.75671 | -40.5771 | 2025-10-11 03:19:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c1686e7a-c77b-3797-98cf-e11bb82cca11 | -6.03703 | -42.50732 | 2025-10-11 03:19:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb6ccebb-b892-3ee2-8962-c42208fa270f | -8.20524 | -43.34051 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 585115c0-4a39-34e9-8b8c-015bb33c174f | -7.36737 | -38.76313 | 2025-10-11 03:19:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a510a293-b8e7-3196-a43d-ef79919e3de1 | -5.86012 | -42.85894 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| ff80ffd4-73e2-3e67-b650-7467863b645e | -7.65597 | -42.58621 | 2025-10-11 03:19:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3fc8432b-a029-3521-8069-ad76e5edf1f1 | -4.4965 | -42.62599 | 2025-10-11 03:19:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95a9a2e2-5d2d-31a3-aa85-03a2961abc04 | -7.21384 | -39.90945 | 2025-10-11 03:19:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99211f35-86fa-3bc5-b5e6-811c9ef55ff8 | -6.73574 | -42.85768 | 2025-10-11 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 5fc7787c-5fa5-3cae-b32e-cd0c2dfc7699 | -8.20972 | -43.35569 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f1212014-6fae-3548-88db-2f1aede61ca0 | -8.68018 | -40.41942 | 2025-10-11 03:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e03b5206-a845-37bd-be80-397fcc88f00f | -7.21466 | -39.90502 | 2025-10-11 03:19:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65ec6b4f-f738-3af9-8524-94315dc3f7f5 | -8.2046 | -43.35323 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1c9019ea-c5dc-3a97-a2a7-d3eb5877df95 | -5.8514 | -42.85787 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 15be5a8d-6fd5-3306-9685-44fcb4336420 | -6.18653 | -39.70855 | 2025-10-11 03:19:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0aa5ab6-2ffd-344a-8cac-dfff8fd1147c | -5.59161 | -41.11572 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08fec906-9806-3640-8b64-11e7aa10ae09 | -5.8616 | -42.85122 | 2025-10-11 03:19:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| d29210f6-8701-3c27-bba2-21fcb1e2a8a4 | -3.12438 | -41.00095 | 2025-10-11 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 82c24d27-bcc3-3ca2-b3fe-7a5528e8f24d | -6.04413 | -42.50843 | 2025-10-11 03:19:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0b7289f9-06c9-3efc-a247-d80447572561 | -8.20665 | -43.33323 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7db12ece-e198-3b5f-81ef-21694115313f | -5.86005 | -42.85151 | 2025-10-11 03:19:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| ad328e14-77bc-380b-bba0-cc2396131e1a | -5.58503 | -41.11457 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c6dc618-ea04-30a5-9681-c801a46f3060 | -5.8688 | -42.85267 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 97993192-1fd0-373b-abdc-0263936cddfe | -8.67936 | -40.42381 | 2025-10-11 03:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ba389d6d-016d-3697-8e43-b4e349bb6970 | -6.18885 | -39.6957 | 2025-10-11 03:19:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b5c5b5a-d705-3fcf-940d-9974ab34bf67 | -5.40922 | -40.98523 | 2025-10-11 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d34210d-0b82-33fe-9adc-a4053f7b866a | -5.86586 | -42.86051 | 2025-10-11 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 2be5ef47-ef05-3d66-9c42-b2f46ee7f9d4 | -3.12548 | -41.00104 | 2025-10-11 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| adf45fc8-aa9a-3b80-bd5a-736c025b913f | -8.20742 | -43.33922 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 64b6de47-182b-350a-a293-7510c2c502e2 | -8.19602 | -43.32198 | 2025-10-11 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |


[Clique aqui para ver as próximas entradas](README6.md)
