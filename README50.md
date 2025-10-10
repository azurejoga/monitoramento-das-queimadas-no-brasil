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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bd9b8af-7020-378d-a630-40c0e964c727 | -7.39838 | -45.91031 | 2025-10-10 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0431d668-6df8-3c0a-b6e9-aadaadcee93d | -14.87742 | -48.23283 | 2025-10-10 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f025943c-d369-3dc6-8da5-aa7f8706e200 | -14.92477 | -46.76756 | 2025-10-10 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3bf74d3d-45d2-3057-bbf1-04074ed46a56 | -15.08594 | -46.60751 | 2025-10-10 06:12:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c8265e4-7379-3caa-aa87-53b5b5317bab | -14.92295 | -46.78107 | 2025-10-10 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 419dd721-0986-3825-9959-f4f3963d7712 | -15.08778 | -46.59335 | 2025-10-10 06:12:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bc631256-2b4f-3a30-98f1-fdad982309de | -15.42413 | -47.98045 | 2025-10-10 06:12:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 54b93574-add0-3c05-a955-26629c251957 | -17.92404 | -44.99903 | 2025-10-10 06:12:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 77a109c1-4859-3f50-af4a-e58fa3a9c54b | -15.74874 | -48.97771 | 2025-10-10 06:12:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9982a08b-1143-34e1-bf25-eaaa5cfcc48d | -17.92167 | -45.01978 | 2025-10-10 06:12:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a3fd2ffa-c7ea-3e42-9b94-1e09239e0bbe | -17.93454 | -45.02107 | 2025-10-10 06:12:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b673dd9c-3eed-32b3-bf5e-07f5b22ef2da | -14.86495 | -48.46152 | 2025-10-10 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49eda759-4ef8-37b2-b2f4-fb92c32071e9 | -17.89495 | -57.5023 | 2025-10-10 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 951aa09e-2e44-3b69-b438-01185eaf63c2 | -15.74733 | -48.9879 | 2025-10-10 06:12:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 79f763ba-716e-3b85-817b-4149e614bc08 | -15.42261 | -47.99177 | 2025-10-10 06:12:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c7356b97-d45e-3cc7-8c83-9817a369859b | -14.88062 | -47.23258 | 2025-10-10 06:12:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 130c92a0-acf0-3c4b-bc65-d157b4340514 | -17.88827 | -57.49609 | 2025-10-10 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| d71f2173-44e1-3dfb-a557-2aeee4619e2b | -14.879 | -48.2215 | 2025-10-10 06:12:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c03e3af7-0f18-3374-87c7-f897a771a62f | -14.92945 | -46.77411 | 2025-10-10 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b5671f03-c59f-340e-99e7-ab01f3860448 | -14.93119 | -46.76053 | 2025-10-10 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| bf5cf113-6cc9-3259-b548-80fbae95f55f | -14.88228 | -47.21994 | 2025-10-10 06:12:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4413ae17-bc0d-3647-bf5b-384d9f766bd2 | -17.81241 | -57.64465 | 2025-10-10 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 3a97fa34-0d60-33dd-8efa-3f6387cf7314 | -14.9266 | -46.754 | 2025-10-10 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ba55438d-76ed-3ef0-b1c0-fa984f32a5e6 | -14.83656 | -48.45662 | 2025-10-10 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcaa3b3c-3675-3de0-8798-3e274cda1318 | -15.29523 | -46.14079 | 2025-10-10 06:12:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9b4b5adc-4ae3-33d1-9062-2ee0803cd3d2 | -14.68784 | -48.05775 | 2025-10-10 06:12:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0cdce6f7-b24d-32fd-83a6-763f4f168686 | -14.9417 | -46.76328 | 2025-10-10 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 3f8aa804-89a6-3e1f-8067-6ba52d7acc5d | -10.7996 | -69.30861 | 2025-10-10 06:33:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 775c2644-14b4-331f-8a9b-49cace6a4224 | -9.68716 | -67.44935 | 2025-10-10 06:33:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e11da689-8c96-3e5a-b230-981f628c19cd | -10.7941 | -69.30784 | 2025-10-10 06:33:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed7033fd-d2c3-3356-b0c3-89fbc0ecd49e | -10.08241 | -67.53466 | 2025-10-10 06:33:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9661f8e1-f140-3510-b89c-af97f9440c99 | -9.68662 | -67.45066 | 2025-10-10 06:33:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e7af4f1-3db2-3432-a184-112d353e614b | -8.25827 | -71.11903 | 2025-10-10 06:33:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e20ce73b-ce7e-3206-9080-afdcfb2f18b4 | -10.08273 | -67.53551 | 2025-10-10 06:33:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c371cbba-646b-3401-a353-b4e512fcd31c | -9.69213 | -67.45965 | 2025-10-10 06:33:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30115e2-d5f6-365e-ae91-8ffd23066f2a | -10.82206 | -68.22948 | 2025-10-10 06:33:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6dc64ea-b749-3c55-abc9-d01c5b1be937 | -7.68142 | -72.33041 | 2025-10-10 06:33:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79a5e78a-7698-3243-a2b2-e214018a7887 | -9.68659 | -67.45406 | 2025-10-10 06:33:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb8c4b73-e7e7-3910-aff2-3581e48355ec | -13.8491 | -45.8454 | 2025-10-10 10:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 93c33175-c3e6-33c8-b7e2-5c05a317a731 | -13.8491 | -45.8454 | 2025-10-10 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 42895784-b639-38dd-956c-34c5f5ff0900 | -13.8491 | -45.8454 | 2025-10-10 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 15e10494-c844-3008-906c-4339240233e6 | -11.7589 | -43.3136 | 2025-10-10 10:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| bf4eb008-f6a3-34a1-917a-3624fed84eb6 | -11.7589 | -43.3136 | 2025-10-10 10:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 60ef7b32-97a7-305c-9c48-a95f1da2050d | -13.8491 | -45.8454 | 2025-10-10 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 3660cce8-6f9e-3ec5-b419-1d243f119663 | -13.8491 | -45.8454 | 2025-10-10 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 85b35bf8-3125-3efc-8520-5268148f35f6 | -13.8496 | -45.8223 | 2025-10-10 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 002ab5f2-263d-345d-9e9c-d142a7b02888 | -15.4375 | -47.9871 | 2025-10-10 11:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 73b64e9d-1e22-3813-8d64-5f3cdb96383b | -5.56624 | -38.39429 | 2025-10-10 11:19:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 9f4585f5-c421-385e-b077-951ef6e61e31 | -6.65802 | -36.17565 | 2025-10-10 11:19:00 | TERRA_M-M | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 00d621fc-d721-3b4e-850e-817ddea2a354 | -12.68169 | -43.08518 | 2025-10-10 11:19:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 68e6efad-f066-35ff-92fe-8244235f63e7 | -11.75544 | -43.31145 | 2025-10-10 11:19:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 57fcaa4f-4959-3ebc-b1b2-3005f8af2330 | -8.20858 | -43.38933 | 2025-10-10 11:19:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| e0e2766a-f8d6-354e-a72f-546e690be9d3 | -8.19789 | -43.33984 | 2025-10-10 11:19:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 4fec725a-dd54-39b5-be26-000c3c233e5d | -11.77179 | -43.31443 | 2025-10-10 11:19:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| e636f56e-fd93-3b7b-8618-64b4257a730b | -11.76188 | -43.27564 | 2025-10-10 11:19:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 4a59bd3c-1f47-3412-8bb9-6b983c1e9e7b | -6.42729 | -38.42634 | 2025-10-10 11:19:00 | TERRA_M-M | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 27.6 |
| a51f32b3-c9b4-3294-b15e-7d1d8d78ea54 | -8.20844 | -43.3837 | 2025-10-10 11:19:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| 7e5a5762-96b5-37fa-9f98-de8a4be40efc | -17.9357 | -45.02952 | 2025-10-10 11:21:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1e05480e-184a-3d2d-996d-e05d51b8d55a | -12.3592 | -47.2335 | 2025-10-10 11:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 9a01dfe5-0348-386f-a844-368cd933948d | -13.8491 | -45.8454 | 2025-10-10 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| b96a6757-7228-32c2-b0f0-c1c85b2473bf | -13.8496 | -45.8223 | 2025-10-10 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 230dd55d-1504-3abf-823a-7dc5f30c2db3 | -15.4375 | -47.9871 | 2025-10-10 11:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c148208e-0bc3-37ce-94c6-cf5d390288d1 | -13.8302 | -45.8255 | 2025-10-10 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3c404a68-fcaa-38ec-8328-336a89e7f4ed | -10.1517 | -44.5984 | 2025-10-10 11:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d017527d-3f1b-398c-a972-06be09a2806d | -12.3592 | -47.2335 | 2025-10-10 11:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 2bad8c84-7a03-365d-bcc1-7dc1e953f29f | -13.8496 | -45.8223 | 2025-10-10 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 45d2794d-c550-3ef3-9edc-cc30e883a47a | -13.8491 | -45.8454 | 2025-10-10 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 2c8a06fe-6c72-3797-9242-49063cd1566f | -15.4375 | -47.9871 | 2025-10-10 11:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 2439066d-d2cb-3884-8e22-5a78a3f14d10 | -13.8491 | -45.8454 | 2025-10-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ba083f44-4aeb-3c5d-9d0c-c699d8458851 | -13.8496 | -45.8223 | 2025-10-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 0c6166c7-87cc-39a1-a71f-06c1ab8d551f | -13.8311 | -45.7793 | 2025-10-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 281.2 |
| f146bcaf-9aef-385c-8a5b-67b01611deda | -12.3592 | -47.2335 | 2025-10-10 11:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 03759e3c-8b1c-3678-b987-769adf588d3d | -13.8307 | -45.8024 | 2025-10-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 46d6a429-63a5-39f2-a319-c1a6d46a3c1d | -13.8117 | -45.7826 | 2025-10-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 703befb4-287c-3d63-81e3-edb2315a2c5c | -12.3592 | -47.2335 | 2025-10-10 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 189a64ba-25b3-300b-b832-390f039870c0 | -13.8307 | -45.8024 | 2025-10-10 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4582e531-65eb-3fb3-8767-27445b287d2e | -13.8491 | -45.8454 | 2025-10-10 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 6fb8771c-b0da-33e1-99c8-3c14f9bb6486 | -13.8496 | -45.8223 | 2025-10-10 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 9f8f4645-611d-3ffc-97fe-51a752611d3e | -12.3592 | -47.2335 | 2025-10-10 12:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 14f1f0a8-4eb5-3900-96fc-a5113637c3fe | -13.8496 | -45.8223 | 2025-10-10 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 87d1b8db-0ac0-3c94-9ba0-b99a242e375f | -13.8491 | -45.8454 | 2025-10-10 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8e7cc597-794d-30a3-884e-f1b0344a9e60 | -15.0962 | -46.6167 | 2025-10-10 12:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| c9744fe1-4bfd-37b0-b68c-a10dd2636f67 | -13.8491 | -45.8454 | 2025-10-10 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 33e67c5c-8468-343b-82ec-cb13804b57ed | -13.8496 | -45.8223 | 2025-10-10 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 43c86ff4-a629-3079-a4bb-bf1df8eda40c | -12.3592 | -47.2335 | 2025-10-10 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 82f4e97c-97cf-3a8f-8085-13bbf0838c79 | -15.0962 | -46.6167 | 2025-10-10 12:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a6c9ab0b-8d0f-3b1b-8fd7-e187995c24f1 | -13.8496 | -45.8223 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| bd518e75-84ab-353e-ba91-6a0427ccaac2 | -15.0962 | -46.6167 | 2025-10-10 12:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 131.8 |
| ff8de02a-bd30-3f5d-90da-e19c2e5a7ccf | -14.2744 | -45.911 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 751ff629-3ece-3560-af88-4b66564fba28 | -13.8311 | -45.7793 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 7e78d8aa-d01e-32b3-b596-97f77bff38b7 | -13.8307 | -45.8024 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| cfcf754c-7d88-31fb-bed3-5abf0cd7fe33 | -15.0967 | -46.5937 | 2025-10-10 12:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f3786267-6612-32ef-9130-5ad73ba4e5d4 | -13.8491 | -45.8454 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 16cf4b23-a510-3267-95d5-533b2f0148de | -15.4375 | -47.9871 | 2025-10-10 12:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d8ba5779-16a5-3c52-961e-3a47abdff8fa | -14.2749 | -45.8879 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 7c85b8ea-9866-301c-9d29-f906e3b2e72b | -13.8487 | -45.8685 | 2025-10-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c7c53266-39e9-3fb2-8e52-a86af9c6301a | -12.3592 | -47.2335 | 2025-10-10 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| b339ea2e-8cde-3186-90f3-13dac78e75c9 | -12.3592 | -47.2335 | 2025-10-10 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 15752135-86a7-3f96-949b-a31eb425684b | -10.1517 | -44.5984 | 2025-10-10 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 84f98625-81b0-3f3e-a062-ac0c1104b871 | -10.1707 | -44.5959 | 2025-10-10 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |


[Clique aqui para ver as próximas entradas](README51.md)
