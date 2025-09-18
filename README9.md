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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 777b419b-9772-31d1-8c04-f0a576352018 | -4.38088 | -43.28414 | 2025-09-18 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac2ea717-1c8b-336b-8894-20fc6fef4491 | -7.05842 | -42.00164 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c00675c0-dcc0-3038-a9aa-a528c5d01996 | -5.76758 | -43.70761 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ddc60a7-3ce6-3329-affc-459d00fbc167 | -6.13907 | -44.49362 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f848ab92-d519-3938-ac89-4be38e80b3dd | -6.89748 | -44.7769 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9fc9d115-eed1-3a8d-815f-8dcce804b35e | -5.79023 | -43.93061 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d51eab63-0d71-3af0-bbc3-410ba0cd3494 | -6.48481 | -45.99852 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cb38c91-f0ec-3685-af78-a87d7a595f05 | -3.15802 | -43.26325 | 2025-09-18 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80781869-5acf-35ff-be09-b1ff88cf36d2 | -7.1212 | -38.51535 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e389441-53a8-35d2-9f5e-5b46c37170cf | -5.55781 | -46.28071 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fbeeda35-8c0c-3cab-907b-cbf4eaccc078 | -3.95048 | -49.36065 | 2025-09-18 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 313a6ff3-313c-3ecd-9245-8e9ad2f62128 | -5.62055 | -42.89903 | 2025-09-18 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 428a1c4b-447c-3915-a71e-3cee73ae7c01 | -3.45403 | -44.13984 | 2025-09-18 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fc58b9f-f5f1-3cea-9bcd-8d45bf64cf2f | -5.04656 | -42.74815 | 2025-09-18 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a835b64-eedd-347e-8204-0e5273a9e188 | -5.61946 | -42.90593 | 2025-09-18 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d120742-c2eb-33f7-aa15-f55d9c186a46 | -6.41057 | -42.66945 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 57b38eb1-f0dd-35bc-9b7b-bdfeaf58406a | -5.63365 | -43.88781 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae096155-e6b6-3443-b7a4-77879b1d4731 | -3.73822 | -49.04826 | 2025-09-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37843eea-004b-3871-a54f-a74a0b136b2d | -6.16472 | -44.49403 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 447be92c-8553-3b20-bb1f-b414f1f1f4cc | -5.51521 | -45.47807 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5dd6f5a-86ba-3c7d-ab55-edb7e9b520cb | -2.91563 | -48.67416 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee436e3d-775a-3db6-a9fe-112819914791 | -5.77988 | -42.77239 | 2025-09-18 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5c9800d-feab-32d6-a647-28aec76a1b06 | -5.78753 | -43.75378 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dede1683-b11e-31db-9bbd-55ed519aef32 | -3.51255 | -49.44757 | 2025-09-18 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9cd84fac-0796-3412-a905-8e00395f74af | -4.34487 | -40.73291 | 2025-09-18 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ad2abdea-617e-3af0-aff7-b955e800e019 | -3.79798 | -47.58009 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 301509cd-1b70-3f57-ac3e-bcde74c07c39 | -4.66277 | -46.32199 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c28824f-2275-3fbb-a5a8-25936dde8442 | -5.53643 | -42.17974 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f1c3909-305d-31af-837f-e9b95cd45f41 | -7.05788 | -44.34973 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b9259af-30b3-36f8-b9bc-c300d90e2646 | -6.98776 | -44.45145 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7592e5a7-079f-3939-b9ee-d8ef945d5f56 | -6.6089 | -45.64135 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5325112-4ab2-3088-9e0f-186d6b84da82 | -6.18426 | -41.22493 | 2025-09-18 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9cd96cc-293f-3918-806a-283a93f0700c | -5.91065 | -45.72116 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a61b508e-2a45-3a34-ae63-c7048ba862ac | -6.59535 | -45.65255 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd6a1b36-771d-3811-ac24-44ecbe1c2308 | -5.43672 | -43.18101 | 2025-09-18 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d51b9570-63e0-3f0c-9773-462c26615992 | -3.15062 | -49.48299 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9fcf72f-fb2d-3539-be0f-2a4489b71b26 | -6.42298 | -44.36919 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a094a75-7654-3ec1-8080-d5e8c7f62424 | -5.78355 | -45.9725 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a1ecb70-5a59-3708-be25-b906aefeabae | -4.71632 | -46.13428 | 2025-09-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 918bdf56-219f-3033-8ff6-df7042cbb595 | -6.31672 | -42.40216 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6b66dc0-0e2d-323b-b865-b3ca9242dd55 | -4.96337 | -42.82338 | 2025-09-18 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfc02ea2-9817-3704-b659-356360212284 | -5.76153 | -46.25006 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b719938d-f300-3c03-84eb-08e12b0535d2 | -5.88629 | -45.6478 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e126776-4a54-3c2e-a799-96dabf3707d8 | -5.99665 | -45.81685 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa76e7cf-cec7-3d45-98fe-ddf06cfaa3df | -5.88694 | -45.6438 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7f8d1a0-1066-35b0-9a58-3fca0181a994 | -6.38515 | -42.6584 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cfd83c0b-7834-347c-9ec7-80e907590c93 | -3.79701 | -48.63368 | 2025-09-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77863b68-c003-3544-885f-48b46f35606b | -6.72718 | -44.1484 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8f6abb98-ce73-3b2f-862e-5b25738482b2 | -3.84358 | -40.37576 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c453a73b-c9f6-3fbb-993c-853dd9e69f80 | -5.86964 | -45.88421 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be7d97a3-b00c-3a25-a9b9-641aef26c2de | -6.38939 | -43.34345 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b83efff1-8591-3f64-8547-a0fd174c5aad | -4.61794 | -47.02283 | 2025-09-18 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bbe5908-183f-3dc3-8a4f-4d3e5a2c2b67 | -6.38718 | -43.33601 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e25d9987-1d0d-3507-a4fd-77dd813367a3 | -6.41809 | -43.35508 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 807de11e-2e90-30ff-92b2-9b86411255bd | -6.61253 | -45.63502 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86be1523-e0ca-3a0a-839a-1789487d8a60 | -3.30102 | -40.99767 | 2025-09-18 04:12:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18736078-5bc6-3cbf-9275-e3062fd43cf8 | -4.29935 | -47.57403 | 2025-09-18 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91f5576d-5419-3e3f-8785-d4fbc5781ea2 | -3.04324 | -47.02039 | 2025-09-18 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42667312-c1de-391a-981d-7f282f70b6bf | -4.6993 | -41.97448 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7df8339f-b93b-389b-b69d-75fd8bfbe70b | -5.62975 | -43.89082 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bde1b98-c9ee-303e-a48d-8ba454a11a00 | -5.82079 | -45.91387 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5709f1c6-184f-3aca-8a97-bcb944df1485 | -6.89807 | -44.77324 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 63752b96-2edd-3e70-a1dd-b8d267810934 | -6.20886 | -44.28411 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3256943-8e33-3aa9-ae9e-4a815825841d | -3.84014 | -40.37523 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46c66ad8-e54f-38f1-ab11-cc9918a52882 | -1.7622 | -48.05197 | 2025-09-18 04:12:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16209826-84bd-3477-af42-d5721cc8c867 | -6.25641 | -43.45338 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7996920-464d-3cce-a75d-f47f25ddb4ea | -7.03801 | -44.17939 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1e55884-8a2c-3092-b246-56e7dae88811 | -6.21835 | -44.28934 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13053954-904c-3ecd-b71a-039de40bcac9 | -6.26303 | -43.45443 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8667bf8d-6a28-3eb4-a831-8faae2a09265 | -6.00772 | -44.33279 | 2025-09-18 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80dacbc0-b72d-3738-9707-81ee4a44b471 | -6.55127 | -44.01158 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b85d043-a6da-363d-83cb-ff4ab7d018c6 | -5.80425 | -45.90289 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f95b166-3d82-33a0-8c24-744951f77dc4 | -6.18256 | -41.23593 | 2025-09-18 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7b08e705-eda1-3cc7-9534-95e8ce6ac103 | -7.08465 | -44.16169 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1a64827-67b0-3fd1-9dc0-6498ea3f4cd8 | -5.80648 | -45.91159 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07782720-f74e-36d4-a163-ea43777bd88c | -5.29053 | -44.71598 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0e1f203-6032-3d2e-8dfd-08b0fe6063cf | -3.84425 | -40.34897 | 2025-09-18 04:12:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76f192e5-24f9-38f4-a86f-bd8af5b700d0 | -5.64745 | -42.599 | 2025-09-18 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c7e3047-4083-352f-8b5c-1dfbb61251b0 | -6.17765 | -44.49973 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0754daee-e5d1-37eb-b730-77debe33e784 | -5.78129 | -45.96365 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f54db21-dd57-3883-84d3-c4594c2d262f | -6.61655 | -45.63857 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd4d99a3-cffe-3674-ad52-93c0203468d6 | -2.38203 | -47.7216 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5878a85-2f65-3b6c-941f-881e6d7e7cff | -3.89564 | -40.92077 | 2025-09-18 04:12:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 660dd2c3-2e8c-3d93-ae10-42e4511d1580 | -5.44706 | -44.83206 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 462dc974-bb2c-3fb7-b0aa-4e0b94136a2d | -6.93144 | -44.76011 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb00c151-9af4-3f7e-ab2a-d6b16285164c | -6.48315 | -45.72008 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e710b8f-d1e5-3783-8423-430da312449b | -6.23405 | -49.22614 | 2025-09-18 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0090b185-e6e0-3a59-9a95-e7e9a5c3d2c9 | -5.72276 | -43.17739 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7895fffa-bf18-350b-bee9-82c6dcdd1695 | -6.001 | -44.33169 | 2025-09-18 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2abba2a0-a8e3-3937-90eb-d94ad816e007 | -6.4258 | -43.34922 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d3fa102-55ee-3baa-a068-2cbd391e651e | -5.81654 | -45.91739 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88a3ed45-c7f4-3b88-9f83-51ba2b80dcc1 | -5.48157 | -43.19909 | 2025-09-18 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd6d167e-9253-3c65-b186-b86bf77c6707 | -7.22796 | -40.17384 | 2025-09-18 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d63cd6f-7958-3ce2-90b6-ba847ca4c720 | -3.84366 | -40.35271 | 2025-09-18 04:12:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4eedce24-9844-3bbd-bbf0-f5b4a1296ee3 | -6.40652 | -43.3639 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 626ba752-804a-3c5b-857c-5adf8e8bb94c | -6.59814 | -45.61284 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1816d75-3b7e-30e7-96a0-3e4e563b2fce | -6.33017 | -44.24798 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb1b96b-5c1f-3f4a-8968-449df8c58f9a | -4.51456 | -42.61148 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 920501ff-7c2e-3bbb-9e57-c34a866843d4 | -6.47833 | -45.99339 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ff1f091-d7f4-3800-846b-6edcd34c9c76 | -6.77288 | -43.25866 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
