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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b36078d9-f5d5-3d96-85f0-a0382b833316 | -3.70507 | -47.14888 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fb3264e-355e-3379-9df8-85b4b1ed6ce5 | -4.87289 | -41.2993 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1fbc678b-8c05-305c-9a8a-e5591066910e | -7.13443 | -46.4209 | 2024-11-30 03:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a0585d9-c694-3b4f-942b-ec54f17b5fbc | -9.10078 | -43.19489 | 2024-11-30 03:46:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d1efbbc3-12d0-369e-a275-fbb8985e863e | -4.06986 | -46.82273 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d5e2385-d4b9-33c7-b426-96ab9ceee54b | -5.52853 | -45.41021 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3c7b71d-c28e-37bb-bcc4-24cfcb1a340c | -14.33125 | -43.52674 | 2024-11-30 03:46:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 835b1c86-d170-376b-9a8e-54115704727c | -6.06495 | -44.44021 | 2024-11-30 03:46:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fe3ad06-34f0-3252-8a32-40677a63f0b3 | -5.07881 | -44.98974 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c5c4e9f-11c3-357e-ad79-4e0a33b5b750 | -3.80776 | -38.68176 | 2024-11-30 03:46:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 186acb3b-314f-3b89-8bb5-724e4980618b | -4.86782 | -41.30503 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4df442f2-e9aa-38dd-9c1d-1975060fd661 | -4.44744 | -48.57644 | 2024-11-30 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cdea361-34ca-328f-bd0c-ca0333a7058e | -1.77367 | -46.12978 | 2024-11-30 03:46:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20dbbbe9-2307-3793-99f0-5e4fdf0047b4 | -2.71487 | -46.12937 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73aed139-2708-39cf-a5a5-912f9e5b0fca | -2.63083 | -46.20633 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c9564f-705c-3d45-bd51-7e80ad336a85 | -3.99055 | -41.51602 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 48524591-24dd-3aff-a510-184cd15de4e0 | -4.8599 | -41.3031 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 569f0077-ead4-3f35-b896-dacb54b301bb | -3.97053 | -41.50899 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f9ffe897-f00f-3753-bd10-3ae30868f99e | -3.84127 | -46.52187 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74ae2c5a-cf97-3cc0-b134-7e383fca60a3 | -1.67768 | -47.85309 | 2024-11-30 03:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd3f92dc-fa98-3d06-9489-70fc63386116 | -6.81675 | -46.77719 | 2024-11-30 03:46:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22b36ab9-0318-3b71-ae08-70d5b10a50e4 | -2.5834 | -48.20929 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 351038fc-8fba-3886-94f5-23a66cee5f10 | -3.98521 | -41.52282 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8d7a86b1-d68d-389f-a647-998e0c3d4099 | -4.88372 | -41.30858 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ed4c0b8d-98a7-3a74-a948-86c70d392ba0 | -3.99116 | -41.51231 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f03819c4-4008-39c1-a9ad-68cf21290273 | -2.85439 | -46.69433 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93f49268-3e29-3d0b-aab6-83b4666b9551 | -3.0095 | -45.10728 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b1beb69f-4a58-34e6-84fc-0cd36707fad1 | -4.86895 | -41.2734 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 405ba798-2f48-3061-b412-d2e78226d5a6 | -4.43983 | -46.01657 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d33870ec-9484-3a82-8e89-35736ef16429 | -4.03906 | -41.90823 | 2024-11-30 03:46:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| aa758669-db56-3747-a8b0-64316dd4970a | -6.9031 | -43.54171 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3cc1bcac-3bf3-31af-adee-814e957840f1 | -4.64958 | -43.92634 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65976d7f-eda0-30e1-9618-091a320b609a | -6.58974 | -35.25035 | 2024-11-30 03:46:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1965df6-26de-3553-a955-b058d4bb6f9e | -1.68266 | -46.78325 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b6441406-a64d-34c7-b199-18ffb078332d | -4.0913 | -44.8601 | 2024-11-30 03:46:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dd21981-d2e0-3d30-9292-775a99077014 | -3.79905 | -45.85689 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66a8f6f3-f7b9-3023-bda7-965ef6847614 | -4.58847 | -44.70461 | 2024-11-30 03:46:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a7cb5eab-6773-3458-989d-9506fd490df6 | -1.68349 | -46.7803 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1d24e106-5a4b-3603-addd-60dd2501a0df | -2.65962 | -48.78466 | 2024-11-30 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2154f35-5c06-3a69-9175-56f0cc489d01 | -6.91274 | -43.56699 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1480b916-6609-3823-b01c-60b8edf464fb | -2.40081 | -48.2386 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e819616f-2958-3246-8368-ea4c284c83fd | -8.49893 | -40.74022 | 2024-11-30 03:46:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c219749a-276d-31e0-b1c7-8339285d219c | -1.68801 | -46.79078 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ea07e1a9-60a6-376c-aeb2-e4f043e76cca | -3.27586 | -45.57117 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1b6ddf29-3799-3762-bb6a-3836cd99ee48 | -2.42324 | -48.17538 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 353243f5-5ec1-3b53-8c46-86770567156a | -4.8736 | -41.31991 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 675df3e4-65b1-3345-9cd0-645c4b69ebf0 | -4.86219 | -41.28927 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9fc8b42b-284e-30dc-80ce-64d2ef4e44ca | -3.46371 | -48.92831 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a69530c0-11c7-3e03-8ff4-76ce441150a9 | -6.91726 | -43.56777 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3170d81-c15e-3715-9814-be89531663fa | -3.92002 | -38.65859 | 2024-11-30 03:46:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1e1136a-fb67-34f1-a1eb-e43933b10e51 | -6.90232 | -43.54629 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b382a3ac-f898-3487-bfe7-c9e34d53975d | -4.13739 | -48.94075 | 2024-11-30 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 885260dd-05f7-3783-a529-b7aef6cb526a | -6.81443 | -46.77583 | 2024-11-30 03:46:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eafaee5-dc6b-33e2-a373-f554c0b5579f | -3.71116 | -47.14965 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcc43f77-b6d9-3afb-a3b5-e638a2dcda6e | -8.71587 | -44.01505 | 2024-11-30 03:46:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfecf303-fc43-32b8-92d7-b39d239b785b | -5.91385 | -43.84079 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 95270afc-217c-30e4-972c-9f4074c7f3bd | -4.07488 | -43.23249 | 2024-11-30 03:46:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 419089ef-7d49-3d0a-82b4-99069a2674df | -1.83468 | -46.30892 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0127a46e-718e-3fcd-9f5e-1701d8203635 | -1.88823 | -48.65503 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4df7b974-b22f-3eeb-976b-d6298572dfe2 | -4.67101 | -40.69282 | 2024-11-30 03:46:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d501921-0166-33f8-a2d4-a749cb578397 | -4.87632 | -41.27858 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d067ae6b-6a83-325e-8925-8cbbb9ed3947 | -4.07269 | -50.04043 | 2024-11-30 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64576bb9-11f3-3f61-a8d3-f8aa1113cdce | -4.84045 | -41.29612 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4eb19af8-b371-3d5d-8614-1a70e1c8e6af | -3.98046 | -41.52592 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fad466ec-53f6-387a-8161-d201fe95018c | -3.95786 | -48.09476 | 2024-11-30 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aca09c24-db83-3422-a695-45e26f58ed19 | -3.01544 | -45.10477 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c186baa-d444-3412-aabc-5f852df333b2 | -5.34885 | -44.77008 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bc5012a-324f-3507-ba74-71aae5542c4f | -4.87016 | -41.31577 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9d23e5f4-2512-3aee-a15b-4a65309a37b6 | -4.41701 | -46.15087 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5711aa60-a2b3-37f2-aae0-e7419feaff6b | -8.3805 | -44.47501 | 2024-11-30 03:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7625d61-9349-3f60-80e6-ca218bb97fe3 | -4.4327 | -46.58529 | 2024-11-30 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab33bbe-8051-33b7-92ec-94d3aaaf68cd | -4.58396 | -43.25808 | 2024-11-30 03:46:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a4744e-c0b5-3bc0-b90f-624432aa188e | -2.26653 | -46.43575 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daaa5a3d-95d5-3d79-9339-10a1251beb78 | -4.60497 | -47.00745 | 2024-11-30 03:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bc0885-2897-3d4f-b09f-3bb150d833da | -3.81742 | -46.55721 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d80f0ed2-82e4-3b5e-a899-799353b61d16 | -7.9871 | -37.6304 | 2024-11-30 03:46:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8d45c212-10d8-3760-9cec-c09b05bba547 | -2.52093 | -48.18736 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9958913a-7025-3d78-9382-187e19e5487e | -4.87233 | -41.30269 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bb65dc5b-43b8-31a3-ba60-b5c404270a73 | -6.28742 | -39.59387 | 2024-11-30 03:46:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 80a03b95-84cc-3ad6-9578-a265c2f8962f | -3.69845 | -45.68288 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc368aa5-3bbe-36f0-bf94-f05e62c668e5 | -4.86608 | -41.26589 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b9d93cd-d8f9-3915-9174-82cb0c4ed824 | -5.03361 | -45.24626 | 2024-11-30 03:46:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5cad717-f9b5-38cf-88cd-e5410dea8260 | -6.81744 | -46.77326 | 2024-11-30 03:46:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 593d9cda-86bf-364e-af45-06c19f3911dd | -5.73293 | -46.62516 | 2024-11-30 03:46:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b69ea36e-3509-31a3-ba90-cc2124c9a537 | -3.9693 | -41.51646 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 62c7b2c9-7f94-37a3-8da8-fcb720af4790 | -5.34834 | -44.77302 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a612f9b-2a7b-365b-8138-4a4549777316 | -1.68104 | -45.78675 | 2024-11-30 03:46:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f688e28-dc2d-3417-8cbe-6529f1108afc | -4.88085 | -41.30101 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 984b2a15-b1ca-3861-ad8c-b4a41726bbc8 | -4.82954 | -41.25273 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4a52f67-c317-3d45-8c4b-668d56ba663a | -5.03943 | -43.62501 | 2024-11-30 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8fe0ce2-474b-3125-8894-1050dcd1cbb0 | -5.74678 | -46.18737 | 2024-11-30 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1166b647-a37b-3b4f-8ae9-371535bd405e | -2.65856 | -48.7909 | 2024-11-30 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a16ac288-b0c4-3070-85ef-d7b40afe240b | -4.86673 | -41.31157 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fd81152-d228-3937-a429-c5a9663a9efb | -2.63152 | -46.20223 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24376e89-1a7b-348a-bf09-82d683ce7625 | -6.78844 | -39.45161 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 300152e2-76d4-3d9a-baf1-65344f42aa59 | -3.08324 | -49.21089 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 958d3cdd-2f8f-3a78-947d-2a8dc688217f | -6.69942 | -47.27479 | 2024-11-30 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f310c63f-12ec-3ad0-a99e-f556d92601cc | -5.12072 | -43.64217 | 2024-11-30 03:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ee7d9d2-71a3-3ded-aa7e-64684abd113b | -5.02043 | -42.74334 | 2024-11-30 03:46:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fbd09a8-8d96-3a67-9729-67c2ac108546 | -4.24845 | -45.51585 | 2024-11-30 03:46:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
