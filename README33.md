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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 997a8155-33c5-32d9-8bbf-420eedbdded7 | -12.49396 | -45.50204 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81f73862-e808-38ca-80b8-1a6e2ba9e1f2 | -6.99028 | -45.19931 | 2025-10-18 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9f58788-1f4b-3fda-8320-d21c7b85e760 | -7.76595 | -42.49247 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 10b18d03-b3b5-3b82-924c-1d4179f0d154 | -10.13577 | -44.53753 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72302f98-6b2c-30bc-ae0a-23749abf1434 | -13.92104 | -45.60666 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c57f952d-2912-317d-b092-5ba1e6b50a35 | -10.24616 | -44.05327 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a77ea8d9-7819-3d61-807e-c3563fd84463 | -10.23581 | -44.89152 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b1f9c43-bee3-32b8-aa3d-a876e61044bf | -7.29811 | -41.94775 | 2025-10-18 04:02:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b1ebba1b-f31a-3ce2-9d90-423ce986d11a | -12.10676 | -45.87915 | 2025-10-18 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd0f6d41-4e16-36c1-b345-ec440eb3fe32 | -10.99812 | -47.90373 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d30abd1a-bc13-3bd5-866b-50a17a61c68d | -6.88381 | -45.43314 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac686d9a-a759-37f1-bd09-6715e2efbeb2 | -6.94343 | -43.68116 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abfe0710-39c2-33c0-8aa3-38e94ecf6703 | -13.61786 | -43.95885 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ea5bba-34cb-3621-919e-ed94e20bcd3e | -13.37041 | -42.52863 | 2025-10-18 04:02:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65ec4cf9-d55c-3617-9fc2-17fcbc5a4c78 | -13.70532 | -47.71838 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd1ed09f-2871-3946-a380-c0ae3cd8b270 | -8.44991 | -44.17405 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13d22035-9597-3de7-8617-46e4472d87cc | -10.58182 | -43.82014 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39fa1876-e4f3-3d6c-9a84-c07fb256a071 | -8.83267 | -44.39949 | 2025-10-18 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 198e2641-4158-3a79-945d-fe0fe63b0eb5 | -11.49298 | -44.23977 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d23755d4-be34-3238-bba7-822021810d60 | -13.77219 | -48.24727 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5bbc3c05-f181-3896-beca-a8b8796d86b5 | -7.36226 | -44.2393 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95847d65-1b23-3091-946c-119d85d52f33 | -8.1132 | -45.43793 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8c22c72-e7c6-3d7d-b9a2-76ed38f243c1 | -13.42598 | -47.98059 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 115f0a6e-22da-3705-a403-9711f9132024 | -13.20678 | -46.42436 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f646ca06-bc82-3db7-9b06-db397d754aaa | -12.15327 | -44.02746 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a191b49f-0934-3655-9d4e-0ca9cf4fafc6 | -8.35323 | -46.22501 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42b80b91-ae61-330d-9f79-e9d156be9b89 | -12.5733 | -43.77016 | 2025-10-18 04:02:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa107467-7382-3719-811b-2bf99f60ec7e | -8.3146 | -43.44996 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1734529f-bbd6-358e-85f0-ca0094e0974a | -11.50923 | -44.05424 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55edcf79-2002-3f45-949d-f003c5da6329 | -11.38692 | -44.26639 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70f3c9c7-1abe-3e37-9538-79e5dd205273 | -17.19356 | -46.97399 | 2025-10-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad138976-d6e2-35d4-b1a6-30e57a13bc6a | -16.18538 | -46.95856 | 2025-10-18 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0056b0a0-8e7d-345e-8cf1-f0f89363b87f | -15.79398 | -43.64625 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8ee9cf5-1fc1-3b2e-9106-3bc006838a76 | -15.05223 | -46.60509 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c1eafd2-492c-3ac7-89c1-48d18652b9d9 | -15.18244 | -47.09068 | 2025-10-18 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da5aec34-3c5c-34bf-a370-f6b10eb10161 | -17.99791 | -43.41706 | 2025-10-18 04:04:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9a6bd11-7c4b-3c3e-ac53-c9314599d3e5 | -18.38352 | -55.47272 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 0d2b7d84-2785-3c84-a64e-50ef515a35ea | -15.03873 | -46.61329 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3726c29e-0e25-37e4-97d2-efd4c473ce6e | -18.40282 | -41.83041 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 50a76bce-588e-38e8-ae9e-74efda9f1a43 | -18.42133 | -43.70567 | 2025-10-18 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 711705e5-2236-3b87-8749-52d5be4903d1 | -15.05528 | -46.61068 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 808b925e-71bc-356b-bffe-00654a49e09c | -14.90899 | -46.73127 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fc83a42-d61b-3dc7-8345-e83c74b51658 | -18.37848 | -55.43678 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 956c86af-ac32-3f0f-8f95-0bbf58a9100a | -15.78662 | -43.6488 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bd845ee-9f16-3757-bbb0-e0a1ab115786 | -14.44584 | -52.89748 | 2025-10-18 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3dba044-aeee-35bd-a283-9dbb24a30bfe | -18.52402 | -43.99806 | 2025-10-18 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86ecaa5-4345-3e56-8cc2-7aff583b2b15 | -15.04439 | -46.60394 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df250eb0-9649-340a-80f1-17904346bc43 | -14.90202 | -52.40493 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01792b42-a38f-3738-87c7-2103232db78f | -17.09377 | -44.09895 | 2025-10-18 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b65d679d-6aa8-359c-8969-1ba70e34eaad | -14.92447 | -46.71238 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8241c45a-8dbb-3366-8351-a6ecf0825150 | -15.03863 | -46.61553 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 115da855-dc6d-3ae8-94f8-1fcdf8c013c7 | -18.40615 | -41.83096 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 491fca68-1d0a-3ae5-9e8f-027f9f935220 | -14.41012 | -49.40991 | 2025-10-18 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 296efd06-12b4-3ff6-86ae-a3abe1a7a6a7 | -18.38858 | -55.47976 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| a5bb0256-4019-33f6-975e-c3fcc56124ca | -15.08938 | -42.1242 | 2025-10-18 04:04:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3859d8e7-acef-376c-8804-560ba07160d1 | -15.94331 | -45.21419 | 2025-10-18 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c82e086d-1030-34e9-a528-de4eb5853ebe | -16.23891 | -43.50875 | 2025-10-18 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d040f85-b3f0-3f7e-9361-e164467638a5 | -16.01291 | -44.50786 | 2025-10-18 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75ea6ed8-76cd-3e7c-99af-b95c27a35a58 | -14.26664 | -51.86875 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c45174c6-aa4f-3f4d-86d5-cf8dbc2dc752 | -16.1314 | -41.12585 | 2025-10-18 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4888e83-69be-3f2c-b6bc-c7fb3f5bc7bb | -17.07812 | -45.56004 | 2025-10-18 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d24e33ca-dd50-31dd-9d66-7d89ef8425ed | -20.69924 | -42.57192 | 2025-10-18 04:04:00 | NOAA-21 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b341375d-44fe-303d-a5f1-fd10c4241820 | -14.90523 | -52.40055 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db056f02-ad3e-3ef1-b08b-01a13f7a522a | -18.38224 | -55.47823 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 4122ddb2-fac6-3ce1-a521-c8b1d3d37e60 | -14.86469 | -52.44295 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8b813c9-45d3-3a5c-9153-4dec0c8c3cce | -16.42823 | -42.63131 | 2025-10-18 04:04:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10aaf38a-1198-3198-b955-4e6cc862a83a | -19.21334 | -42.9227 | 2025-10-18 04:04:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 84eaef95-5541-3082-a6b1-580fb41f546f | -14.26742 | -51.86495 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 074e817e-7a1a-3416-9c78-5f6ad196b1a5 | -15.94515 | -45.21145 | 2025-10-18 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15bb3997-dcca-3251-8246-87836b113caa | -20.0903 | -43.01363 | 2025-10-18 04:04:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 82dea032-bc24-334c-95b4-7d9fe8ee7a6b | -16.42397 | -43.61347 | 2025-10-18 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb5ed45-b4ef-34f2-b0ff-a76da8d64067 | -14.85989 | -52.43745 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab48ac03-c53d-36fb-8607-0dd731aea9e9 | -20.67627 | -43.18283 | 2025-10-18 04:04:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06c0dbad-f912-3d89-a86a-29b6b09efb04 | -17.49706 | -43.46189 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6759a20-26dc-39e2-b5d6-863aa765880f | -16.18562 | -46.95663 | 2025-10-18 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dc38a15-cbec-34b3-9a99-047ce5c0e93f | -17.49646 | -43.4656 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7886ebc-b039-3505-8cd0-1d3fdb1f1e2d | -17.98368 | -47.88256 | 2025-10-18 04:04:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2177af6a-8c41-30b3-b6ae-e1c94a8b7909 | -18.3772 | -55.44228 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3a34be7a-0a52-3796-aae0-a2c06b184847 | -15.53198 | -45.6963 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c961b5-3797-3238-8db8-7490018d66a6 | -16.53476 | -43.67786 | 2025-10-18 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f8d98ca-db09-35c1-8874-2373b3bca20f | -18.40892 | -41.83513 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60166cd7-ef4d-3c1b-9b24-d7d22b5aba67 | -18.38034 | -55.45014 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 207397ce-1eec-3465-ad9f-115db4ab1be7 | -15.06515 | -42.12748 | 2025-10-18 04:04:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc9623ac-3ef0-3f28-bc53-a0275715b022 | -14.91005 | -52.39445 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20c42671-49df-3e27-ac99-0719147aa47d | -15.5865 | -44.5131 | 2025-10-18 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73cfbc8d-fdf5-3073-ba6c-4f5cc424098d | -16.07329 | -42.55288 | 2025-10-18 04:04:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 22eaa80f-afc9-33f0-9fb2-75df776c1696 | -18.74489 | -43.70585 | 2025-10-18 04:04:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf00d557-d3bc-357c-b030-c662cf94aaf0 | -19.0589 | -48.13852 | 2025-10-18 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dfd6e6e-7d62-3370-bb1c-2e022fca193f | -17.31413 | -42.14491 | 2025-10-18 04:04:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ea32892-0bed-3df7-915f-df2c8ba3b7c1 | -19.04075 | -42.10476 | 2025-10-18 04:04:00 | NOAA-21 | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a32471f9-5275-36d4-91b7-87d2d1633eb7 | -14.428 | -48.05961 | 2025-10-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7640da1-c493-3a32-954e-6c642f428c20 | -14.91005 | -52.40573 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 173d5db4-d35d-3562-bc29-55a46fcf89cc | -15.8211 | -42.51024 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2324a753-7941-37f0-aa38-6948f06519f5 | -18.09345 | -42.44903 | 2025-10-18 04:04:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2264962e-a33c-3b70-a8d4-79bbae7007cb | -15.79061 | -43.64566 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc1803b6-568d-35d7-8349-06d40d54fdee | -15.45636 | -45.93592 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c39668e-004e-3ff3-99cc-85c0566a4a5f | -14.90765 | -52.38901 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fe09804-3643-35ee-9b84-9fc72a38e830 | -14.48069 | -48.60628 | 2025-10-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4687dfa6-0b56-37a2-81c1-dd0831559540 | -16.20294 | -43.68525 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ec6e40d-fddf-3709-acdc-925340552e54 | -14.93645 | -46.71125 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README34.md)
