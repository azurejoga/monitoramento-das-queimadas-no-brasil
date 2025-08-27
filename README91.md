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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3c11e3e-d640-333a-9300-fe096756e44a | -10.97496 | -41.81123 | 2025-08-27 11:57:00 | TERRA_M-M | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 02b54cbf-38be-34f6-8c94-de948d1e0c95 | -13.61628 | -48.21165 | 2025-08-27 11:57:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 8e28f26c-f9ed-31ac-ab36-de07fdd28210 | -16.3119 | -45.12087 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e4723a96-731c-31db-98d0-bc8ca8e54e08 | -13.52649 | -42.4603 | 2025-08-27 11:57:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 67024aa9-cc05-3d1d-a19c-81ebee0ba915 | -9.67511 | -43.72304 | 2025-08-27 11:57:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 471e91b3-8b47-3c77-94a1-6e2f274d6d63 | -15.14543 | -39.96331 | 2025-08-27 11:57:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| db5b9191-cd30-3cf7-8d6b-ec1cd67f8517 | -10.32018 | -46.79788 | 2025-08-27 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9962295a-3e27-3dfd-82cf-82d29fe80671 | -10.66237 | -47.18811 | 2025-08-27 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0f2e8839-a970-31a0-951f-d440022881fa | -11.32771 | -43.48544 | 2025-08-27 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7d3996a9-1012-3961-9540-db567605b50f | -11.51416 | -41.58226 | 2025-08-27 11:57:00 | TERRA_M-M | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7897b609-090c-3f98-80d8-d594258b6f92 | -11.31706 | -43.49378 | 2025-08-27 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e784195f-a833-300d-86dd-1e26fd60a094 | -12.86248 | -44.86444 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1f71e949-53ad-35af-aa54-ff0bbd49860b | -13.07054 | -46.33815 | 2025-08-27 11:57:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 28caf9c7-8f94-3746-99b4-8a51316cbbe2 | -13.52518 | -42.46935 | 2025-08-27 11:57:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 77612c21-5fcf-33c6-88f4-5e8fb744d5b4 | -11.58658 | -46.38128 | 2025-08-27 11:57:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0d1d869a-1b7c-37ec-bfe8-8437aec0dd92 | -13.60706 | -48.19163 | 2025-08-27 11:57:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| dd61b279-ea11-3494-8f13-dbdd054842e6 | -11.92152 | -46.73553 | 2025-08-27 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 613a33ed-0309-3a79-87c7-38e95b309c55 | -17.2417 | -43.23622 | 2025-08-27 11:57:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3a591741-675a-302e-ab12-ff1179f3b39b | -15.46139 | -44.35309 | 2025-08-27 11:57:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4fc86a69-aa0e-3a85-a78e-6f848d5fe14e | -9.96255 | -46.37101 | 2025-08-27 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 127eedef-a505-30d0-a1c4-b4f72e2e4add | -15.12065 | -48.66394 | 2025-08-27 11:57:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cd4376d0-e935-3b8a-b35f-b229a1a18895 | -15.78447 | -48.00922 | 2025-08-27 11:57:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ffee5f39-eb3d-32ff-846f-7c19416652b8 | -16.78345 | -47.55485 | 2025-08-27 11:57:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c8a5d24e-782e-39bc-9629-6d4385afe8be | -12.97966 | -41.06187 | 2025-08-27 11:57:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| fcddb3b7-bd4a-3aa0-b39a-3c6272283052 | -10.69705 | -47.12374 | 2025-08-27 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1730213e-b813-39cd-ad7e-4b400d341b31 | -9.09525 | -49.56243 | 2025-08-27 11:57:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2e432f8f-3252-39aa-b74d-a9b9bc86152a | -11.92931 | -47.11149 | 2025-08-27 11:57:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 421c24bf-e63a-382d-a376-a20b9f42047a | -13.4034 | -46.91909 | 2025-08-27 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 9a9b5409-b7c6-391b-8b5d-9730b43d631a | -14.1297 | -45.4043 | 2025-08-27 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 3725ed22-a6af-302a-8d96-fbb988a8fcdc | -6.4355 | -44.5764 | 2025-08-27 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fe8ff9bf-f391-3bc2-b40a-4015338448f7 | -8.948 | -65.9429 | 2025-08-27 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 6094ab24-bbc9-3fcf-8469-ad84324f9d49 | -9.4064 | -60.5133 | 2025-08-27 12:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 75a48546-be98-3086-8729-7347a468c892 | -8.271 | -45.1149 | 2025-08-27 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| cf780048-e126-30ad-854e-e53c60daef33 | -10.0977 | -62.9085 | 2025-08-27 12:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d0d1af33-ff06-3da8-9d67-c95ae8d35fce | -8.9479 | -65.9616 | 2025-08-27 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 5b2b7da5-56aa-37d4-800f-57263262b721 | -6.1783 | -44.0457 | 2025-08-27 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d8d6fd21-96d3-3b76-bc30-24a94e86fc27 | -9.4062 | -60.5326 | 2025-08-27 12:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d97a5426-305f-334c-be61-8c9a192a81f7 | -20.02901 | -41.3209 | 2025-08-27 12:00:00 | TERRA_M-T | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6243819a-94b6-310c-a9a9-f3f270c207df | -21.23107 | -45.62012 | 2025-08-27 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 5b5ae9c9-f1bd-37e2-81dc-b5d88f4aaad4 | -18.72973 | -44.89032 | 2025-08-27 12:00:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6e843eb5-5c90-387f-8f8e-4b086c6c0e7d | -19.61982 | -44.06326 | 2025-08-27 12:00:00 | TERRA_M-T | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bf07bcaf-2610-3b5a-ab67-4e775c069ec5 | -20.79111 | -44.75012 | 2025-08-27 12:00:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 76bfa9a0-fcd1-3ee9-b3e0-779408c0fb94 | -19.04594 | -40.81654 | 2025-08-27 12:00:00 | TERRA_M-T | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| d5395e43-9a56-33d8-bbba-697315d64c79 | -19.56187 | -45.3107 | 2025-08-27 12:00:00 | TERRA_M-T | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fe868f21-3ce7-35af-bbb7-07cd17d61cf6 | -21.70951 | -43.56976 | 2025-08-27 12:00:00 | TERRA_M-T | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 7b352466-29be-327a-9c2d-cd1ccad22c06 | -20.59855 | -44.86425 | 2025-08-27 12:00:00 | TERRA_M-T | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 16a29aa3-b285-3388-980d-790a2db10b56 | -20.47301 | -46.20756 | 2025-08-27 12:00:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 881e5f34-3422-3e88-8990-6604ca49c331 | -19.28081 | -43.73517 | 2025-08-27 12:00:00 | TERRA_M-T | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3fdb178e-14eb-3dd8-9f14-38506297938e | -18.98618 | -47.08112 | 2025-08-27 12:00:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 04dfe724-7bbc-3e3e-8d35-66c49ec0c004 | -20.9488 | -41.23561 | 2025-08-27 12:00:00 | TERRA_M-T | ATÍLIO VIVACQUA | ESPÍRITO SANTO | Brasil | 3200706 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4b30870e-f8cd-30ee-a655-d866363d1c07 | -20.47127 | -46.21841 | 2025-08-27 12:00:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 07bdd338-77bc-30ae-8c67-1b8583691a15 | -22.75966 | -43.62807 | 2025-08-27 12:00:00 | TERRA_M-T | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c1d367d8-5ba4-3355-8765-187bf9c6455f | -18.51995 | -46.85019 | 2025-08-27 12:00:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 84be133d-24a2-38ce-bc69-a75dae6c2299 | -19.90467 | -44.63017 | 2025-08-27 12:00:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 03298839-999c-3ccc-a81e-99f03027c25a | -18.20636 | -43.94909 | 2025-08-27 12:00:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2464eb60-5b57-3ffb-b808-0a7fee8bf00d | -19.25278 | -40.22779 | 2025-08-27 12:00:00 | TERRA_M-T | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 585693a2-cba4-364b-8fd2-4f06cbf8a776 | -20.75263 | -44.75749 | 2025-08-27 12:00:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| c50029b0-a150-36b0-be5c-43eb41a357a5 | -18.20292 | -45.55503 | 2025-08-27 12:00:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7df8dfca-331f-347e-8ac8-3d89795e39c0 | -20.76561 | -44.30032 | 2025-08-27 12:00:00 | TERRA_M-T | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| c3aaadb6-0126-31b2-bf68-6bd304ec720a | -19.12884 | -46.45684 | 2025-08-27 12:00:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 83a8ef41-2ad3-3550-83bf-5111f96c461d | -18.20127 | -45.56564 | 2025-08-27 12:00:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5ca34fec-6939-36d7-a9f7-7a8fa82ae7a0 | -20.53813 | -43.96496 | 2025-08-27 12:00:00 | TERRA_M-T | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d8445a74-0065-3273-ada7-ddcdc1dd84b3 | -22.31977 | -43.54702 | 2025-08-27 12:00:00 | TERRA_M-T | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a5f32cf4-ab99-3c17-a9ab-a506384fd634 | -21.79289 | -43.29967 | 2025-08-27 12:00:00 | TERRA_M-T | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0f54ade0-3038-370d-8187-a4cfaa0078b6 | -19.1307 | -46.44542 | 2025-08-27 12:00:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| be15eda6-83b7-35fa-96c1-775641677650 | -21.50905 | -45.55271 | 2025-08-27 12:00:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 61e9ac0a-3049-3ed9-81ca-1c9d0fc507ff | -20.79907 | -44.57471 | 2025-08-27 12:00:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 848c82b4-0bc0-3ed7-ba31-6fb838595e74 | -17.98346 | -48.04609 | 2025-08-27 12:00:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ac8c6760-e12a-3d8a-a4af-f1c3419f8760 | -19.99318 | -41.85823 | 2025-08-27 12:00:00 | TERRA_M-T | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b2161bff-b410-3045-bd09-01526ac1c6d4 | -20.11636 | -44.32532 | 2025-08-27 12:00:00 | TERRA_M-T | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 17bba897-a65d-3e88-b3f7-9aa7ceafc4b3 | -20.02809 | -46.79839 | 2025-08-27 12:00:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a5be4336-92ca-3dad-b552-0e7230b2f82a | -18.68796 | -46.57598 | 2025-08-27 12:00:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e89ce5ca-d283-3ddb-986b-88855cf1429f | -20.01411 | -46.43495 | 2025-08-27 12:00:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cf3d26f8-7207-3350-91b6-858f366f019e | -9.1009 | -49.5621 | 2025-08-27 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3ee7f91f-cede-396e-b906-ad377ec0403c | -12.7447 | -48.2041 | 2025-08-27 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4d0403f3-b757-36fd-b51f-a2954f9e5cc5 | -6.4355 | -44.5764 | 2025-08-27 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 99899d65-1135-32e0-b76d-f7c37c99bb15 | -13.3838 | -46.9017 | 2025-08-27 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 375dec68-edac-33f4-9cb6-4aa70ef732ad | -14.1297 | -45.4043 | 2025-08-27 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b493a953-76e0-345a-b18e-a402c13f931a | -11.5694 | -47.6081 | 2025-08-27 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5b3c5c6f-9a7a-3cd7-9516-ea931f1dda0e | -10.0977 | -62.9085 | 2025-08-27 12:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c93b78e4-0aad-3eaf-ad7c-bc6ef612151a | -8.948 | -65.9429 | 2025-08-27 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 0b1c945b-f452-3511-88aa-ba0ed02d98ef | -9.4062 | -60.5326 | 2025-08-27 12:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 0f2f9544-d40d-3574-9a75-1b15165bd177 | -9.4064 | -60.5133 | 2025-08-27 12:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4e28c03c-3e6a-34aa-b20e-3caf7fd9f787 | -8.271 | -45.1149 | 2025-08-27 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ec214108-d736-34e0-a898-640c44ad5b87 | -8.9479 | -65.9616 | 2025-08-27 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.8 |
| ed4d6d9c-970b-3481-a77b-909e6c394e1e | -13.6097 | -48.2126 | 2025-08-27 12:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6ba875a7-a0cc-3fd3-860d-72d77ff47dad | -8.9664 | -65.961 | 2025-08-27 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 82ce75ee-088f-3180-bd38-5833be1f66e6 | -12.784 | -48.1543 | 2025-08-27 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 06a9942a-8df8-34ed-9301-d813a1df9a72 | -6.1783 | -44.0457 | 2025-08-27 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e6ab3daf-5a42-35ba-aff9-c7fe97daeae4 | -8.4593 | -43.6879 | 2025-08-27 12:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 72389611-6af4-3cd5-a73f-1e5e6d3006e6 | -9.4062 | -60.5326 | 2025-08-27 12:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0b58a273-3fad-3d19-87b9-1757cde0a4b6 | -8.4596 | -43.6645 | 2025-08-27 12:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4053069e-8055-3a1b-b71c-d3c8dee0aefd | -12.784 | -48.1543 | 2025-08-27 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b1c2f9ba-78da-31eb-abb3-ae5601a38cea | -9.1009 | -49.5621 | 2025-08-27 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2f60bcb3-7f50-3f4b-9859-4d7f630a20df | -9.4064 | -60.5133 | 2025-08-27 12:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b61c2147-db6d-34c5-b6f5-9f3cea9025f0 | -8.9664 | -65.961 | 2025-08-27 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| dc1ceb8d-18b1-3eb8-8823-da6b8aa15a6d | -8.271 | -45.1149 | 2025-08-27 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| bf79fecd-7fd9-30d0-9455-591a40de72f6 | -6.4355 | -44.5764 | 2025-08-27 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| e881b677-e6e3-36db-bdc1-2182d8522909 | -10.0977 | -62.9085 | 2025-08-27 12:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 37241bd1-a4d4-36ec-9330-ec1d89970b9d | -13.3838 | -46.9017 | 2025-08-27 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |


[Clique aqui para ver as próximas entradas](README92.md)
