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
| dab90a82-e58e-32f2-beb6-d5fa5a1a5140 | -7.23413 | -46.05218 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0415f0d-50ba-35b7-b40d-b426e8b3b7d8 | -7.02959 | -46.20776 | 2024-10-27 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53baaefc-63d5-3424-8dbd-8f8ca1d99514 | -6.88838 | -45.98348 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9efc4244-700f-3e91-ba5d-af976adadb11 | -6.87651 | -45.8857 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 528270b6-20c7-3cbe-acf3-c31db998e9a2 | -6.87266 | -45.88865 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ec59e5-b06e-3484-bd84-25c547b79c7a | -6.86458 | -45.87342 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e814730c-8c4e-391b-9d46-a582b70a60e7 | -6.86226 | -45.91194 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21fc4883-1f2d-3cd8-aca7-ab0394f3e82c | -6.86127 | -45.87291 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f97975bd-c359-3ef4-8de0-3c3d4a4e0278 | -6.86073 | -45.87639 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e15f1905-ef9c-3956-ad6c-3a1d550c8a88 | -6.85741 | -45.87589 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 928915fe-b518-37a7-ba22-1de40d145e77 | -6.8541 | -45.87537 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46d3c0b9-46d1-362f-baac-cfe1c56177f8 | -6.85198 | -45.91058 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 369f167c-7789-31e1-bb47-a91da361d164 | -6.85079 | -45.87486 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e90b8c6-5469-3bcd-b98c-d04a65d2ef85 | -6.85024 | -45.87835 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0807b5d5-cfb4-3253-9373-92de4f691d8c | -6.84803 | -45.87086 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0c4c1a-0343-3092-bc79-031b813a7c83 | -6.84638 | -45.88133 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 670ef27e-7d08-3a03-aa73-fc8ccf71eb6a | -6.84472 | -45.87035 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc11edd3-a748-3c94-8624-fe1a20f1bd92 | -6.81839 | -46.14648 | 2024-10-27 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e635d16-9b00-34b5-ab3d-263ac85cbefe | -6.50415 | -46.20286 | 2024-10-27 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 430ba8f3-d3b1-3e50-a586-ad4bb916039e | -2.05842 | -46.53485 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8f00b1c-ff52-3677-882e-3908a2059847 | -2.00817 | -46.54879 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a53941b-d420-3bec-8f76-b376ce91e12d | -2.00604 | -46.38946 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937c308a-c273-3f0b-973b-7b2986ad86e8 | -2.00214 | -46.39246 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cbe2171-f2eb-3132-9a4b-b4708052a0a4 | -1.97732 | -46.63491 | 2024-10-27 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc084b31-2d4e-3189-9926-04428973cb83 | -1.97396 | -46.63438 | 2024-10-27 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b0f65f-2dc1-3174-b7e4-71840483bd8d | -1.95845 | -46.63179 | 2024-10-27 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6ffa5b2-2e1a-3b6c-948d-9461490a9cff | -1.95509 | -46.63126 | 2024-10-27 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1ad8cc1-60dc-32c4-aa3a-fbd9c432a44a | -1.7948 | -46.39295 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 481d9294-52c0-3e4a-b175-de3b387f0997 | -1.79425 | -46.39647 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ddd7dd-e489-33b9-b8b4-393429af8e38 | -1.79146 | -46.39243 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfb4f631-ceb2-351e-8806-171115c57f81 | -1.66726 | -46.55407 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4015a5d1-0dd2-34cc-980f-b567e31d9768 | -1.11066 | -46.83316 | 2024-10-27 04:23:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a808a2-cf2c-33c2-a1fe-1205dd0fa57b | -2.92459 | -46.78928 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3daf976c-ba3a-3fbb-8f6e-81b556a9f38a | -2.81729 | -46.63515 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f136d5bc-26fc-3de0-9b40-992c6945ac68 | -2.81674 | -46.63869 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 896a6309-bed9-3688-8fca-8066cd926b20 | -2.77783 | -45.97947 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 731f52c8-bb75-3f2b-8c3f-5c014c2f6b98 | -2.77729 | -45.98292 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 075b6768-6e25-3419-8f1a-e3c089d6da5f | -2.77506 | -45.9755 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe8581e9-7799-3db4-9072-3035eccd306a | -2.77452 | -45.97895 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57d1d5b6-c8b3-382a-a422-6ac3db75ffda | -2.75081 | -46.81727 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28de9412-49c8-3fba-a2fa-3f6f7545a28c | -2.75024 | -46.82084 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c34208af-b475-34d3-ab15-59773b2b21e5 | -2.74093 | -45.99844 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 205f45dd-e1fa-3e2e-9600-0f8bb939cde0 | -2.74039 | -46.00189 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b74bdd8-ca7c-3348-8d56-79adcc75dd9b | -2.73708 | -46.00137 | 2024-10-27 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 509a31bc-e7f3-3756-9461-d3d2b060db73 | -2.72302 | -46.6892 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e1afcb0-d76d-396d-907e-af3f0bed20a0 | -2.72246 | -46.69274 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d02535fc-02bb-3317-817d-f5239c372b5a | -2.72189 | -46.69628 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 113cd4db-f208-34f6-906e-af53f86fcad3 | -2.71911 | -46.69221 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91641f40-50cb-3550-816d-9dd8905450e3 | -2.65191 | -46.00183 | 2024-10-27 04:23:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a532206-9a26-3226-8d47-ec115ad436bb | -2.64374 | -46.05362 | 2024-10-27 04:23:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ba1b6c-21d7-3448-8be1-b1ae94c93f22 | -2.62054 | -46.91033 | 2024-10-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22a56f52-0099-3b9d-ae8a-72fa2bd8b68e | -2.61351 | -46.13757 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6ae17b6-b17d-32d4-ba64-879c6a6bcd8d | -2.61238 | -46.12321 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a368c0f8-a794-3040-a53b-9a0212c148b1 | -2.61074 | -46.13359 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1153462-5b90-3f97-9558-a516bb1e6716 | -2.61019 | -46.13705 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e9bcd7-cd4f-385e-8c2f-61ee91fde01d | -2.60964 | -46.14052 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feda370c-82b4-3910-a65c-f6422d0e9241 | -2.59745 | -46.11024 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2815b80-bae3-31a0-bb5a-764943b996ce | -2.59413 | -46.10972 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e751cc-8bdb-317d-9f75-f8f3fa6c04be | -2.58588 | -46.14036 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1635acf-8cb7-3fea-af77-6416f99a114e | -2.56993 | -46.13431 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7732c3e-2cf6-34fe-8cd2-4c9958d107fa | -2.56938 | -46.13778 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9836d7b4-8871-3604-9de2-f574293dd797 | -2.56661 | -46.1338 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 757aa682-849d-3561-8fef-db6bc739df22 | -2.53647 | -45.98029 | 2024-10-27 04:23:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62af22e3-99e3-39c0-b303-d1809f9a5c1c | -2.52633 | -46.17372 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09b49f5f-e418-3d4a-9418-c79970ec501e | -2.47348 | -45.84001 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7180cb8-d5da-327c-92e0-31b7327a42f2 | -2.47294 | -45.84345 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| adba08d7-19b6-335d-9028-54bc346f246b | -2.4724 | -45.84689 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ef29605-8c8f-32c6-a53c-d87236802cd4 | -2.47017 | -45.83949 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1077d2e-dbf4-3cf9-b9e6-0080bd06fa48 | -2.46963 | -45.84293 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b53f653-832d-3e82-bc0a-90afdb49f51e | -2.46909 | -45.84638 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 262b4e48-88f0-3563-8af3-d632a071de88 | -2.46855 | -45.84982 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06bd5105-1d1f-3c01-aeec-f87e2c983a41 | -2.46578 | -45.84587 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae0eb4c1-7fb8-3d57-943b-e66399d931d6 | -2.26756 | -46.13359 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61cb2327-e9f7-32d4-b633-5b847f26716b | -2.26701 | -46.13706 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acab030-8c91-39da-b192-7cc21c3c2ed6 | -2.26424 | -46.13307 | 2024-10-27 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fce3fb19-ce13-3fbf-ada0-89039539b7d9 | -2.26062 | -46.78515 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a8da60-955e-346b-8283-3b5dea2d54f0 | -2.26006 | -46.78873 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf659a0e-3122-309a-a6d4-885554acaca3 | -3.90683 | -46.44749 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1442c295-f31c-3a75-843c-39ab24a55a41 | -2.25276 | -46.79125 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7c50393-996d-3b27-995b-ad178a091220 | -2.23257 | -46.78809 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0699ac3b-5079-30d9-93d5-6f88196575ac | -2.232 | -46.79167 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edff8135-5302-304b-990b-a5673d0be361 | -2.2147 | -46.70483 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40d3e3f9-10cb-328d-8fd3-04dfb24714e0 | -2.20172 | -46.46677 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c1e2a59-3419-3efc-8a2a-75092e500ebb | -2.19838 | -46.46625 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6205a38b-7257-37a6-830f-e29c0ea15049 | -2.19165 | -46.42194 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 394e9173-8932-33aa-8c72-f1bae5cdee77 | -2.18831 | -46.42142 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 438b3967-376c-331b-8bd9-192a2575de9f | -3.19154 | -46.17883 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf42201-201e-3e1b-981d-3e6629089491 | -3.191 | -46.18228 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df181c99-9c9a-3eeb-ad1c-1a77ae5daaf7 | -3.19045 | -46.18574 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c486ac2-d6ce-3972-bb62-3ded548ef162 | -3.18768 | -46.18177 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b587b9c9-58f0-366f-9a43-eec9e3129a33 | -3.18714 | -46.18523 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc3d64d9-b1fd-3b47-88d1-2132cb962053 | -3.186 | -46.17088 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db8432d0-4ee6-31e9-a1ce-3c3647b49727 | -3.18546 | -46.17433 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40b64572-ab13-3d04-9fd1-8a9e412fbdb5 | -3.18437 | -46.18125 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a263ccd-771f-39b0-aa59-b5e818a13a15 | -3.17997 | -46.18764 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9ff3a20-6855-3471-b62c-b399c25cc882 | -3.17665 | -46.18712 | 2024-10-27 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 672ec4ab-c38a-3732-a8d4-8f96cccbde23 | -2.40968 | -46.71651 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7e01e5-24a1-3027-8f36-9a5fa6beb209 | -2.40912 | -46.72007 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70439d59-f5be-33eb-97e1-0964df4382c3 | -2.40802 | -46.70531 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9870626c-03c3-3b8b-bfa1-f453dee43b59 | -2.40746 | -46.70886 | 2024-10-27 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README44.md)
