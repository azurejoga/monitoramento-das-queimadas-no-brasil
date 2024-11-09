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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8f46f0e-b018-3a82-8896-67672e3d9bcd | -4.71406 | -49.60561 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bd6a4cb-f4b5-3ad6-91bc-04ed61203bcb | -3.47772 | -52.62496 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fdb0878-c9c8-3e60-a56b-ccab3527d7db | -10.51059 | -42.39353 | 2024-11-09 04:33:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81774428-0145-39f6-95d0-a9e073ed3aa8 | -3.33831 | -50.07684 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e08fa2b-a772-3e5b-9664-c39632075d9e | -5.13791 | -48.24715 | 2024-11-09 04:33:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a16da1a-0dbf-3e25-860f-ec87455272af | -4.82371 | -47.31859 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1816a4f4-aa5a-351b-9556-ebe98335f32e | -2.45588 | -53.68796 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 670e7636-738b-3718-b48a-9ea6e3b4c544 | -4.24358 | -46.0132 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a671acd-2065-3a86-a772-ee6ba9271c08 | -3.66799 | -50.26061 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7075c015-99ff-3948-81b5-a783160045c6 | -2.84474 | -49.43718 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17ec5c3-e7bb-3ebc-ab32-833bcb1bc17e | -3.92071 | -52.20852 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 880d4eb5-9d3f-3f83-8776-e5f360b1d150 | -4.73507 | -48.98914 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77697e5d-3a10-34fe-94c2-f6ecb8b0479e | -2.92451 | -49.35303 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e65821a-0a87-3528-bfdb-811234043ad5 | -3.96954 | -48.12647 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac113cd0-8354-3388-aeac-b354eaf7cb31 | -5.6633 | -49.99461 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c3f3c6-7843-341d-9985-08613ae019ff | -3.02573 | -48.09224 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5894ecf2-e08a-3d12-90db-3c731451d278 | -3.51161 | -51.67022 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 910444f8-6480-37d2-96ae-bf2557ea8bec | -3.856 | -46.62944 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab6811a5-bbf6-3da8-b3d7-536949ac9ec0 | -5.17371 | -44.00246 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a434ba71-9b03-32a2-9f96-ecb077154bc7 | -4.21354 | -45.86109 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1d5bd3f-3983-3030-873a-fcc2fc25f1fd | -4.62205 | -46.5364 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24b4863e-442f-306b-a494-94ae188fd3b2 | -4.13512 | -46.82555 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 936d7a0e-1e7e-33da-a0f7-82a287842d53 | -3.05356 | -47.69572 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99146eee-c1b6-3b87-b52f-a332a2613574 | -3.14149 | -48.57188 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8b3bdde-f015-3bac-a905-aeb6a01a5a51 | -5.50273 | -47.17334 | 2024-11-09 04:33:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9db8ab9-f014-3b40-9c0c-6ba76127e88b | -3.533 | -50.86903 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| efedbae7-2de6-32a2-9059-029b21bc4cef | -4.25037 | -47.5705 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0484744c-d596-38eb-9d94-9e0d0c2aa8b1 | -4.49465 | -48.48764 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad151506-36d5-31df-bfdf-fbc2487d4f33 | -3.23179 | -50.26648 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 016a81f1-9bd2-3e06-9152-61dd676b828a | -2.23525 | -53.7683 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| ebca2d77-6f29-3b39-9d2c-9ad9c05b6fcb | -2.77306 | -51.61018 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 509b1663-3a3f-3280-805f-0517ff4e6d22 | -4.92078 | -48.52592 | 2024-11-09 04:33:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88941d95-c5d4-3a85-bff3-8597d2c6da35 | -2.43602 | -51.5798 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 884e0c28-506e-3456-9ea2-0abbc50cb88b | -2.21149 | -53.67284 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c81d275d-fe4c-3589-be4a-ac35bd4d65c5 | -3.70029 | -54.62051 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 663c877d-88cd-3929-9acd-bf4c8314fe9e | -2.67432 | -50.95739 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b2a782d-5528-3ea3-8230-5b5828bfe2d0 | -3.33 | -50.08366 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 077a9fe5-0eb9-3138-a140-37582317190e | -3.59055 | -53.09163 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efdade38-66b2-3581-97ae-8e32087217a9 | -2.82089 | -50.43936 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d129108d-590f-36f9-a4d6-420bfebc305a | -3.61628 | -51.20947 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c06c9e0-a15e-34f8-8bc9-f3868c1ae6ad | -3.58872 | -47.34349 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 2da0f83c-957a-3039-a413-eaecba469237 | -3.57281 | -50.5449 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e746604-328a-34d4-8151-3841359a18e7 | -2.80697 | -51.80433 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 484119fd-27bc-32df-a323-8f3361188d96 | -3.95844 | -48.99277 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1fb98e5-8c1e-377e-9650-e27e204022cd | -3.04506 | -50.37338 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b512c2f7-d6e5-3e6c-9a18-8f0485dd43e2 | -2.6035 | -51.30407 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec4b386-cdd6-3e0a-b1da-d347f87c3105 | -5.55505 | -45.83295 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc4b8510-0c8d-3366-9d97-2ebd1cbbccc1 | -3.95303 | -48.14522 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28e9f6e8-3114-30ca-81d0-82b28713c49b | -2.83994 | -51.79922 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdf1e67b-f2b6-37c1-b234-07b8d3591281 | -2.88079 | -49.23096 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 319d49d3-63a4-38f8-93dd-2e62082adde2 | -4.39485 | -45.66729 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fe8b2d1-da83-3059-b655-fd2f8c9abe0f | -2.99105 | -49.51449 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b3f3e6-80ef-3dc6-852f-7a5fe6c19339 | -2.81416 | -52.95603 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ee28fc5-fe52-3555-8566-13676c41249e | -3.09256 | -53.32732 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72bbcbe5-d9be-336b-80eb-c862acc9dc22 | -3.24186 | -50.27224 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08ddecfc-8f25-3c5d-924c-0754d450f342 | -11.1031 | -43.34043 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ad23793e-35f3-3693-97ae-5e851bc0b70e | -2.87841 | -50.41246 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e539a44d-4202-3e46-b7d9-b5db00be65ff | -4.50129 | -46.39184 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9649917b-addb-30e0-bb0b-f522bae7f7aa | -6.30035 | -41.56271 | 2024-11-09 04:33:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17481cf0-7b67-3323-8568-551bdd12b3a7 | -3.96473 | -48.17902 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 43779afa-be1b-3f30-9432-516d3ee74630 | -3.07223 | -50.98712 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6221094a-0705-3ec4-8ec0-18c62063200f | -3.11441 | -50.14152 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3218911-2b7a-30df-b28c-ac8b6ed58ca3 | -3.37141 | -51.6456 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0f51d7a-52c2-3b11-aadf-29b5dc602fa2 | -2.85231 | -51.77379 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60cfeb3a-9f30-300d-bb11-ce8ad550f06d | -9.23269 | -44.3195 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 224ce146-824f-3583-89f4-28269e2bd406 | -3.0481 | -53.27446 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e517ed9a-203b-33da-b869-09c21dbb1242 | -10.86069 | -44.9705 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2685a228-ce36-3fcc-82ef-4073181bb117 | -2.68409 | -51.8188 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 183b7ac5-14a7-380b-9612-a5ff9f3fa1d8 | -4.54535 | -48.64297 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dee8fba1-81ba-35ba-9204-cd502cda11b1 | -4.73467 | -43.24916 | 2024-11-09 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74caea07-7a23-3279-8f0a-4bb3ccaec336 | -8.85532 | -47.67814 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6da72de2-4c6c-3b28-b975-fa26f720a65b | -2.67227 | -51.81704 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a69fa72a-c9b8-3dbb-9865-a09f536c40a1 | -2.61846 | -51.75013 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb458d56-17e0-3ba9-9746-5b692244e91e | -4.17127 | -46.59254 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99309731-1635-39f7-9e1b-24bfbe6461ad | -3.22061 | -50.38224 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b321cd6d-b398-35fa-9d05-efcb3eea54a1 | -4.19684 | -48.39067 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b5ffd5-de88-3a19-bb94-6a0e8a2d4331 | -4.22484 | -50.64118 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b195e95-e350-37ef-8d1b-a4b66afb9b02 | -4.20395 | -45.85589 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0fa13713-e482-3f8b-935a-fbb0206bc664 | -3.19086 | -54.31866 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0951c35f-df79-357c-b489-6ee437d6f79e | -3.53871 | -51.25418 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63e747f3-93ee-31ff-88f4-17d8de81ce44 | -2.72418 | -49.28764 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a25d942d-a5a0-3acf-90bd-8febf4d12d8f | -4.18565 | -46.58761 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a311ae-f472-3e8b-8236-5ca62253800d | -3.22949 | -50.30371 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 23c6bd91-0043-3776-9a51-cf80763b72d7 | -2.9213 | -51.66862 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db340ea9-17bc-3b82-a58d-720f60d3a3e9 | -3.9669 | -48.16515 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a13013b-1d7a-39a0-8535-21c8ae5ccac3 | -4.24876 | -47.58081 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0fb1352f-789c-3d5a-a7be-bfb1ffbc9a52 | -4.74774 | -48.58842 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb437060-0830-33cd-b9cc-a43202606800 | -2.65592 | -49.89719 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 811c6930-5902-3aac-a21a-416ac92f69b6 | -3.34674 | -46.64642 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 867dbcde-0042-3825-afe3-b416cc333869 | -2.83925 | -52.90787 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4714e226-f5d2-3fdb-8f71-dbe7f55e0b7c | -2.94226 | -52.70392 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8136d35-bef3-35af-8202-026a298c631b | -3.09524 | -50.21751 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c3a6905-97fa-34df-95c7-5f73c938150b | -3.16108 | -50.5911 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e9bf798-e84c-3c00-acba-35deb495f3a7 | -4.21369 | -48.54409 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83070a9d-93f5-3614-b5d5-8f612a504f94 | -5.14107 | -47.70734 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724cd683-3e60-3e3f-bf29-64f0d25e6ef9 | -3.76895 | -51.34278 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97566ee5-bbd4-36da-9f9e-b20aa0254ad2 | -4.18223 | -50.42461 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e837a89-6beb-3d58-a14a-e3f9b07e6b0d | -3.89672 | -50.07922 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee74eedb-f901-3dd3-803d-f7849fe790e0 | -3.31129 | -51.66364 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b53b535-68ae-34d6-8ba4-abdb25ffc0e2 | -3.092 | -51.11237 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README44.md)
