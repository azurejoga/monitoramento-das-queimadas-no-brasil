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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 021e9187-9af1-3f25-8534-4ca5670ac879 | -17.23326 | -46.79808 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 065726b2-dd7a-30fb-9a4c-44197277d0e2 | -12.52284 | -47.57005 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fcc7b001-27d7-3f60-b030-24c2c2de1291 | -15.15026 | -47.94075 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 829ee28f-3c6e-3da2-ac15-2e1ee3c5ae0d | -14.22795 | -44.38004 | 2025-10-27 03:45:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77f56b5d-1414-3164-a660-e8fa2b43b973 | -11.04311 | -49.89817 | 2025-10-27 03:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4fdc5f3-7bd2-3d15-a682-facf61be0663 | -13.55248 | -49.55449 | 2025-10-27 03:45:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 524ba9b6-245b-3f84-9067-5ba5c93232f8 | -17.23969 | -46.79632 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3c1de65-9d7f-3d7a-8696-d7bbb724ffc2 | -17.31531 | -43.65604 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee3100e-ddf6-3e95-86bc-cdbf3d7642c0 | -14.5375 | -47.99273 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcbfa664-e191-3865-b88f-f12c834783ea | -12.50721 | -44.33804 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87f6f9b2-e710-36e8-8329-e44738404d33 | -17.3238 | -43.65747 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 64eb7a30-75d4-396f-b778-2e8215636a7e | -12.50439 | -44.32626 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10dde242-51f0-31a3-b5ce-593c960e1c58 | -12.27855 | -43.75518 | 2025-10-27 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 406e0111-2871-3645-a3ec-0227533ada1e | -17.50766 | -44.3303 | 2025-10-27 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94d201aa-3882-3c47-b4a7-375b5bfaa53a | -13.55172 | -44.2672 | 2025-10-27 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da265804-c64e-33a6-b9dd-6f958e897dc4 | -18.34748 | -43.96482 | 2025-10-27 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef808fbc-c8e8-3649-a42b-ae19b2e1ce79 | -17.99301 | -48.18541 | 2025-10-27 03:45:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b03f6afd-62c7-3e25-b6b6-2c6762834006 | -15.30383 | -42.87764 | 2025-10-27 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f492e04e-e56d-3073-b4e7-dcb5913e5149 | -17.32111 | -43.64865 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a1acc221-febd-3982-bd82-3416318614ed | -19.69309 | -42.26587 | 2025-10-27 03:45:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e4c3502c-d935-3bea-9774-0b41444166eb | -17.32061 | -43.65349 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9d8735a-11a9-39a0-8c12-a757df371a83 | -14.48709 | -47.88939 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82141001-68d8-3dac-a369-195dcd005690 | -13.59821 | -43.11715 | 2025-10-27 03:45:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d5d685d8-909f-3b8c-acb2-0cf8a419579e | -13.43515 | -47.38755 | 2025-10-27 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac4682d2-d9c0-3ad6-908d-5b662c323df0 | -14.63256 | -48.42257 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc7be34-6808-3011-bb3b-25d32b6a8412 | -15.11353 | -43.26482 | 2025-10-27 03:45:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04a7a9fc-715b-302b-bd4e-c993715a4f44 | -15.29282 | -42.9368 | 2025-10-27 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 558b8b99-8ec4-36d8-9915-0e3e8726f97b | -17.31561 | -43.65686 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ec775a4a-7ca8-3383-8a3e-afcf6c85aaad | -19.66129 | -44.65978 | 2025-10-27 03:45:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a9d33757-420f-3b68-8756-03c2080e37b8 | -14.62351 | -48.40618 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f7b2411-12e5-3325-be44-30aa30b6d223 | -18.62837 | -43.06451 | 2025-10-27 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a45db4ed-ac03-30d9-b403-eb0dba8aae10 | -14.62068 | -48.38092 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26eb9225-7bd2-3f99-a566-35a88166ff2f | -14.62947 | -48.37828 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d060025-337a-39f8-a2b5-71448bfe2c3a | -17.31986 | -43.65756 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93c03b0f-9b0b-39f9-a842-55252053f968 | -19.77036 | -44.25749 | 2025-10-27 03:45:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c44434c2-9ac6-3ff5-b70a-39a4ca060d4f | -15.14448 | -47.93949 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f120c8f8-1314-3cdb-9b48-6e566e66a98f | -17.31141 | -43.60865 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 329492c0-624c-3281-b515-11b55c9f0115 | -11.04865 | -49.90643 | 2025-10-27 03:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eaec7b4-1d98-3dbf-ae8e-0194a39e98f7 | -13.07924 | -44.54754 | 2025-10-27 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26e79dc5-c38c-3590-b0e8-261c17f483fa | -12.28566 | -43.75807 | 2025-10-27 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dce3d665-7f44-3645-90a9-b218cb3f46c8 | -15.14351 | -47.94425 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e78981-a2a4-39f3-95ae-6ec652d5d333 | -13.94392 | -43.81533 | 2025-10-27 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d342a23-e049-32e2-8957-475a22c4ae6b | -14.63948 | -48.41952 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7cc874f-a519-30bf-9892-c02350fbd558 | -18.51376 | -45.08759 | 2025-10-27 03:45:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1222c2e-f36b-31f8-aa9d-6d5dda523064 | -12.32889 | -47.47633 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc85fb88-36b9-32a5-8a67-cc92cf4e0aaf | -12.52533 | -47.57287 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 586df40f-4cc0-3ea0-8b44-743195232cb1 | -17.40534 | -46.8883 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c8040d0-7262-3bac-8dae-1e18a1a5a56e | -18.31005 | -42.13921 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 07774501-f021-3692-8d35-4c7f863a122b | -14.62094 | -48.40994 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a82494-04ba-3b40-b896-cad22ff28480 | -12.97882 | -48.39566 | 2025-10-27 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4611e21e-9db2-3de8-b4e4-fbe56d3ba177 | -12.50239 | -44.3371 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 183e99e5-fd17-3d50-956d-0f5c615ed88f | -12.06956 | -47.99811 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bb6e0cde-1c93-3aec-a35c-501979a27707 | -14.62685 | -48.38131 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1d35f97-2c2b-3f31-812e-ec69975bbe17 | -18.15205 | -44.25941 | 2025-10-27 03:45:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d153e3d-8173-3fd6-a7fa-e0efcf1e37d0 | -12.33633 | -47.47 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 623f887b-26aa-3834-ace2-2708744add6e | -12.27764 | -43.76015 | 2025-10-27 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d3b8b23f-a41f-3f31-8422-d9ea0f82075c | -14.63308 | -48.41184 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47949122-9a05-3f00-875d-bc2f223d3c43 | -12.33112 | -47.47913 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cce634ec-35e0-345b-b747-3c2026206dcd | -14.63647 | -48.4042 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c46b84e-5b3f-3b08-bbff-c11983b2df61 | -13.35868 | -47.40937 | 2025-10-27 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8fd449f-4ced-3fb1-8ec5-4d58cfdcb7fb | -12.32587 | -47.49109 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efedde23-f3f3-3fc4-b10f-3e523a9d9652 | -16.33147 | -43.49 | 2025-10-27 03:45:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3f88cdd-5801-3042-aa10-b139553571ef | -12.32232 | -47.49261 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36b21dd4-abdd-3538-b3ac-80845ade5b27 | -12.86817 | -48.64795 | 2025-10-27 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37849048-aee3-3f28-82cf-e0cdd43e4e80 | -13.1899 | -48.44987 | 2025-10-27 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2249c3f2-a3ec-333a-b65a-b05d6ead7787 | -18.26394 | -45.37115 | 2025-10-27 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1c6cf7c-f4b9-3d99-809a-500edd5ffe38 | -13.03189 | -42.32341 | 2025-10-27 03:45:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0435179-f589-3722-b9ea-e31fcd3a9789 | -14.25292 | -48.14065 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd272541-72a1-323d-8b02-d484eb0a8cb0 | -17.31956 | -43.65674 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 16044567-4e29-37f8-b38a-beb4d0209f6f | -12.28229 | -43.76105 | 2025-10-27 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ae77c10b-f287-31d1-81fb-1718dbc2672e | -16.6256 | -44.59098 | 2025-10-27 03:45:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7aec78a2-c3d2-38f8-b346-13348b59c495 | -17.31636 | -43.65278 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5084f85-46a3-33b1-8d49-bc67f7e63ae0 | -15.32469 | -43.80734 | 2025-10-27 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c20c39a5-6553-3ce8-99a9-1a33dbd7cc94 | -17.64398 | -43.05442 | 2025-10-27 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0defae21-effb-3891-a478-052384ed805e | -13.59906 | -43.11545 | 2025-10-27 03:45:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3e8af124-5432-3137-93e5-1e025a564ca1 | -12.12861 | -45.21177 | 2025-10-27 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f878ad7-4434-3c5b-bb9e-8cb03bba1792 | -12.32003 | -47.48951 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48b776d3-9d77-3c69-9d14-de76854b1378 | -13.08028 | -44.54201 | 2025-10-27 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 25601189-a56a-37ce-9dfd-befcaec55eed | -12.33055 | -47.46817 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6251365f-eba1-3543-98cd-4c7fea7a7709 | -18.00183 | -42.90575 | 2025-10-27 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f317001-8989-3d25-996c-34b5d1c82268 | -13.77775 | -44.09394 | 2025-10-27 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b86fbed1-55bf-3c01-ab11-df58edca2293 | -12.28474 | -43.76297 | 2025-10-27 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 170bd730-6dd0-3933-ab2a-9c4f0042271c | -17.32034 | -43.65268 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dd1fc2e7-546a-3478-9cc1-85f581e0dba2 | -12.86456 | -48.65028 | 2025-10-27 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ea3a1e8-cb16-3975-a400-fd183216c374 | -15.29827 | -42.38553 | 2025-10-27 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81b6e106-99ae-3ed2-a921-9af769081503 | -14.44991 | -47.77922 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 005b0e45-3713-3de0-aea2-4cb0ae18a491 | -14.67312 | -46.34963 | 2025-10-27 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8dce533-1519-3832-9b1b-7f41d04061d2 | -14.63807 | -48.41804 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adcc38db-bc63-317d-a250-28b3dfe1b19d | -17.32065 | -43.6055 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de10b515-da00-3d11-8029-0d56608a52ed | -15.29423 | -42.38479 | 2025-10-27 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 39f20ee7-00c3-3165-bbb4-dd1bfba4e762 | -12.33012 | -47.48425 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b06fcd60-4434-31b6-bb23-192c1b25fa6a | -15.5419 | -44.02197 | 2025-10-27 03:45:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0faa2f76-37db-3a0f-b6ae-d7a3f4cf69f5 | -17.07918 | -43.18895 | 2025-10-27 03:45:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4968c48d-86fd-3a61-a634-5414c6d2c7e5 | -16.66762 | -42.11354 | 2025-10-27 03:45:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d052f61-7d78-3fb6-b63c-7c2f0151fc73 | -17.31563 | -43.60945 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd5186e5-5016-3adf-a068-f10264358e85 | -18.34705 | -43.96385 | 2025-10-27 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 262adcf3-8d28-338a-a9e6-3550b740acc2 | -18.30906 | -42.14471 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82ff37ef-5fb1-3640-aa2b-cfb6e65d44c2 | -14.62238 | -48.38217 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 796ccadd-01f6-3fba-9410-89bf46c49f84 | -19.43848 | -43.03735 | 2025-10-27 03:45:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25f9e389-dfb2-3e10-9b02-9cf0a2418337 | -17.64386 | -43.05449 | 2025-10-27 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
