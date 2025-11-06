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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e312b118-e3ea-3a0d-9259-71a847f7cd43 | -4.22244 | -38.67225 | 2025-11-06 03:55:00 | NOAA-20 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7472191f-b598-347c-b842-5f265b404700 | -3.47327 | -43.67097 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f111501-88ab-31d0-83d3-fbfcca235d76 | -4.8437 | -42.38111 | 2025-11-06 03:55:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6718e15-9e1f-3408-8a99-266f73b0d5a8 | -3.47531 | -43.65865 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 342650bf-7c73-349f-8d6c-2d20223accc8 | -15.291 | -46.89855 | 2025-11-06 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f561909-928c-33a7-b7ff-666dbd6719fd | -4.5776 | -43.33229 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5fb76af-29bf-3c05-837c-d03fc5ab20bd | -4.57579 | -43.34347 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 037fd93f-81ed-3c4f-a4bd-454233f973bd | -5.1545 | -41.266 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35ee26b2-45fb-32d1-91e9-059431a5b349 | -3.47395 | -43.66687 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3e7fcad-f121-3947-ac3c-ff9a3450d7e1 | -9.45212 | -40.65379 | 2025-11-06 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7c5f263-dba5-3b63-998e-e57f34b6a0af | -5.15157 | -41.2612 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f65a1d9a-9424-36d5-9d1f-d314adf5cead | -12.40185 | -39.24525 | 2025-11-06 03:55:00 | NOAA-20 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a086c0c9-1dda-3cf5-bfb9-e31731b31814 | -5.15003 | -41.24802 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b464082e-10c9-3468-8476-06a7f79879e6 | -10.07264 | -42.74203 | 2025-11-06 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 608a7fa4-55d9-3acc-bea2-cc1520a13bdb | -3.2501 | -43.28922 | 2025-11-06 03:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 937ccbd3-90ee-3028-bcbe-db6bd6601f69 | -3.59005 | -46.05449 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4de557-c168-3c86-8394-93aa3926425c | -3.46871 | -43.64517 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8b31193-ef47-3771-a0f8-9b4681678178 | -4.56607 | -37.96068 | 2025-11-06 03:55:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c3794ddc-7dc1-3fa4-a14b-6a3b01011a34 | -4.58174 | -43.33297 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24a3e518-3f5a-3095-94de-b40b3a4675f0 | -3.90106 | -42.54336 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 44bab6db-b6c2-3b36-89d7-9e9664b41308 | -4.10236 | -48.01948 | 2025-11-06 03:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 50ef0aa6-b252-370e-a0da-318f0197958c | -3.43507 | -43.16849 | 2025-11-06 03:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1424fbb-a235-316e-a82f-cb3f651068d2 | -4.15903 | -46.81541 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b25f5197-f8ff-3dcf-aa06-748c9f4b1b05 | -3.33296 | -43.8631 | 2025-11-06 03:55:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9d7b8a8-131e-36fb-9742-7c06196f4aa2 | -3.11847 | -51.21335 | 2025-11-06 03:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15d614cf-5e66-3199-9719-2aa6a95a1a01 | -2.88369 | -42.95429 | 2025-11-06 03:55:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a29f4f3b-e553-3283-b2a5-a2262f370c5a | -4.58416 | -43.33229 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2380b82f-74d1-3597-b61c-49bc1f72792b | -3.48257 | -43.66822 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6404273-74ca-35a1-b5b6-fc49430fc17f | -3.14026 | -40.0558 | 2025-11-06 03:55:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a56d725-79bc-3eb8-8bbf-c9c04ef39038 | -5.1538 | -41.27024 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5969edf7-dfc2-35d6-8eb1-8e2ead3f9fe9 | -3.46602 | -43.66135 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e50e40c-a7bd-3511-865f-35054e317abd | -4.58408 | -43.34482 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10fc409c-d244-32ae-9361-4491475a0b7c | -4.8524 | -40.63274 | 2025-11-06 03:55:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05acada7-30d7-3a96-b2c6-c36ca04a39c4 | -3.93062 | -40.93159 | 2025-11-06 03:55:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29df1423-c52f-3796-8762-a24ba7410ebe | -3.46172 | -43.66063 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f55e8ec8-0d84-3e18-9750-ed80b986504d | -3.58451 | -46.05656 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 729c31e3-2d18-3671-bdb4-3d8e111ece1e | -10.63241 | -40.56154 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d94ba9fb-22bc-349e-a689-b926145a0256 | -4.48802 | -45.93219 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c01277b-2724-342e-b595-d6f431e367cc | -4.58002 | -43.33161 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f5edae82-21e5-34a8-a919-52b7b0a1b849 | -2.96838 | -44.59147 | 2025-11-06 03:55:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a14d409-cc0a-32d5-ba83-c656933bdb9b | -5.1464 | -41.24754 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 084fc059-1a25-3cf7-8204-205cd9e18820 | -4.68054 | -42.09464 | 2025-11-06 03:55:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96a56879-5e6e-305d-a51e-ae02d92a9d41 | -3.47894 | -43.66344 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9b43315-acd4-3cbd-803c-06281752062a | -4.59244 | -43.3336 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d450533b-4077-3508-af96-ad5084ae034a | -3.47463 | -43.66277 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7876a122-25cf-320b-9904-debc46dabb94 | -9.67112 | -43.90077 | 2025-11-06 03:55:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 255f803f-5454-3992-9f07-0b577b1721bc | -5.15589 | -41.25754 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f11915e3-74bb-3e82-a8a6-8cbed5ffede5 | -4.57939 | -43.33535 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a8d9069e-8dc5-3ecc-a2b8-c029343cce8c | -3.4464 | -45.65137 | 2025-11-06 03:55:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4ca6cf6-ca23-3559-8aa2-e46ce7e1ed13 | -3.471 | -43.65796 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f6a4056-0492-32a5-bab8-4b98facc5e0c | -3.74644 | -40.50195 | 2025-11-06 03:55:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9f1817b-6c1c-3b28-a88f-09105b8c7e87 | -10.33442 | -49.64038 | 2025-11-06 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4968206f-2e9c-3c58-8ee9-4289c4704882 | -15.28749 | -46.89311 | 2025-11-06 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ec7f4fd-75ce-3feb-905f-1dc451300b51 | -4.10735 | -48.02485 | 2025-11-06 03:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2718a5b-59c3-3ea2-9d3f-5011ca176396 | -3.11694 | -51.20561 | 2025-11-06 03:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e79ecd4-9948-3697-8c6d-e6887db054bc | -16.30816 | -45.61596 | 2025-11-06 03:57:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4460aa62-b83b-3384-894a-44ea0b2ff1a2 | -16.86148 | -41.94291 | 2025-11-06 03:57:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 56d67813-2ed9-3047-b849-05061412a770 | -17.16666 | -45.37453 | 2025-11-06 03:57:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8e53943-4203-3fc0-b15e-12971ae887c6 | -22.12238 | -44.70613 | 2025-11-06 03:57:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 77c7c4f6-257f-362e-8c78-8b1ec4b26345 | -20.72074 | -47.94476 | 2025-11-06 03:57:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a173d7ac-e70c-393f-81d2-a7c00b397ea9 | -20.7216 | -47.94605 | 2025-11-06 03:57:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b04275cd-fa2f-3102-bb35-a061ce42f1f5 | -17.96537 | -45.38425 | 2025-11-06 03:57:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ba4dc68-b1d6-3174-8003-86072d5dfbae | -25.08811 | -49.80758 | 2025-11-06 03:59:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33dd5e3c-7944-3b36-a257-056f75c6c425 | -26.17782 | -51.21716 | 2025-11-06 03:59:00 | NOAA-20 | PORTO VITÓRIA | PARANÁ | Brasil | 4120309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 94c1a238-96ae-3f08-b715-6256fca1e5c0 | -26.17948 | -51.21832 | 2025-11-06 03:59:00 | NOAA-20 | PORTO VITÓRIA | PARANÁ | Brasil | 4120309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed0e9459-a8a6-3f08-b3e3-cacdf00e1e61 | -27.51943 | -51.38389 | 2025-11-06 03:59:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a79a9ca3-89b0-323a-8280-7131fdfce65b | -28.06203 | -48.67287 | 2025-11-06 03:59:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 030f329a-42e6-3fd6-a467-f31ded61abf1 | -3.621 | -43.5396 | 2025-11-06 04:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a8a2b2de-6618-3f3c-86c1-b2f3812de33d | -3.9324 | -47.6962 | 2025-11-06 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a16ad9d4-a0e2-3064-843d-cd61d36f48ee | -29.77433 | -51.18057 | 2025-11-06 04:01:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| e312aec4-e7d5-34cf-a979-805c78fc9ed0 | -29.72773 | -53.87621 | 2025-11-06 04:01:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| f7abe3a8-00cc-3800-94ee-3e148143d018 | -29.27136 | -52.83289 | 2025-11-06 04:01:00 | NOAA-20 | LAGOÃO | RIO GRANDE DO SUL | Brasil | 4311254 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 232e27e2-ecce-3484-a90b-37e02208d748 | -3.9324 | -47.6962 | 2025-11-06 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 03355c2f-c5cc-32c9-ae5e-96d84291a5d3 | -6.2757 | -43.6675 | 2025-11-06 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ae84a8ce-9339-37c7-a322-573764fec931 | 0.4466 | -60.4873 | 2025-11-06 04:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9f822c00-4535-35b2-be64-ebfea8114eb2 | -2.986 | -52.8146 | 2025-11-06 04:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cfdaa7be-d858-3929-9c2d-c2509da834ed | -3.9324 | -47.6962 | 2025-11-06 04:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 8f9509d6-87cd-355a-b154-15b0ba9d6aa2 | -4.5934 | -43.3239 | 2025-11-06 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 9f6cfe3f-05c1-3946-aa0d-3778e6985f77 | 0.4466 | -60.4873 | 2025-11-06 04:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 94a62cfc-e423-323e-8194-bfd144840e7c | -4.9335 | -42.8813 | 2025-11-06 04:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| e54babf0-d695-3cc3-b9d9-f9870ab67dc6 | -3.9324 | -47.6962 | 2025-11-06 04:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 3862d7c3-1f86-3542-8b04-e05f05e0c8b8 | 2.12857 | -50.85474 | 2025-11-06 04:42:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b1dd1dd-aee9-3568-a4ea-88cd3173e8bc | 2.01086 | -50.89094 | 2025-11-06 04:42:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8c236d2-cd84-3931-a9a2-8b2e8045a013 | 2.61918 | -51.00946 | 2025-11-06 04:42:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46c9d6a7-3a01-3de2-8bcf-d8110ac653e8 | -0.36047 | -51.73147 | 2025-11-06 04:42:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d17ef7-a14e-33db-8ac4-aa1ad8053cfe | 2.01027 | -50.88725 | 2025-11-06 04:42:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9371bff-3919-3ac6-84f9-e6929c8f1567 | 2.25527 | -50.97188 | 2025-11-06 04:42:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7aa5d02-2f30-36b8-9a40-877bf93b136b | 2.07898 | -50.85434 | 2025-11-06 04:42:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be0d2b49-c04f-352b-b07e-8c3d7497a23a | 0.49277 | -50.87661 | 2025-11-06 04:42:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d97ba01d-a4b0-33b2-b93a-a5c61259cd58 | -1.00707 | -46.80086 | 2025-11-06 04:42:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75015f5f-3d24-3f5c-8a71-9ac39ae8605f | 1.83976 | -60.82959 | 2025-11-06 04:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c85ff41-d996-39da-bcf1-e255b644d363 | -0.36393 | -51.732 | 2025-11-06 04:42:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5992f3f-8e80-30cd-bc15-de95662a0a18 | -0.76476 | -48.53364 | 2025-11-06 04:42:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 910499b2-c28b-3286-9f0a-45bef3001ae8 | 3.39524 | -51.29272 | 2025-11-06 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ef0ab81-c7f5-39ce-8346-0b849f050cf1 | 3.39464 | -51.28879 | 2025-11-06 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec6bd0c5-9aa0-3f1e-916d-3100c9f5aa08 | -4.76604 | -42.64201 | 2025-11-06 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8fcedb10-5c42-3a55-a797-b2cd8dd1d0ed | -3.92373 | -47.69626 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26bc1d80-7f45-3979-a928-7d35acc971de | -3.44761 | -50.0249 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f5fa20f-57d4-3ba1-b77a-3d8db46318d9 | -3.70597 | -49.90032 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dc8201e-6f08-3302-aff9-e563234ec69e | -6.74704 | -47.06042 | 2025-11-06 04:44:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README17.md)
