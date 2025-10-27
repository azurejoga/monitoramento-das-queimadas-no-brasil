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
| c36c830f-2751-35de-b8a1-546aaffd0b1a | -4.09959 | -51.04546 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bae071b-ee0f-3981-90f4-33a1ace3625c | -9.56315 | -46.93513 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f7a635-b4f1-38b6-8003-7a6540b18827 | -5.5917 | -41.31863 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e8a91804-6840-35fb-998a-69c7c9d23c04 | -4.24551 | -48.68741 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a4b6070-a26f-3851-bd9d-992c73e3b645 | -8.12265 | -47.02658 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c58138-edb5-3759-be46-27ac81ab41d9 | -2.18865 | -52.494 | 2025-10-27 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a34615f7-2c43-34cb-8d88-8eb34a3089f4 | -9.57483 | -46.90346 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 936a672d-f2e6-36c5-bec8-82cf0fc57051 | -9.58943 | -44.9435 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64ea4e2-45d9-34a6-99f8-d9b130f68e13 | -5.61519 | -51.78931 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa624cb4-a0be-3bf0-8e83-23a3c203e46a | -7.15385 | -45.16849 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffb2486e-3b03-3342-81d3-2486429c8f4c | -5.64708 | -41.09582 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 185da8b7-f992-315b-8294-b489bedbc79e | -7.39974 | -45.12212 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69cb3ea2-596c-376f-ba69-bdfcbca854dd | -7.85543 | -46.44158 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49a31cf0-eea8-3f1a-81b1-2ed0660a59dc | -8.03041 | -46.74176 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 345ef36d-da5f-36dd-a4f8-f2c4a059f8a8 | -7.96719 | -38.28388 | 2025-10-27 04:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 68724de9-42da-39c5-b66f-3729118609ef | -8.865 | -44.98347 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcabd118-22af-3995-a3c8-9e8f2761acc5 | -3.71211 | -50.17658 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc43a81-bc90-3d53-9661-5cfa3f923fcb | -7.34298 | -48.4915 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56683dc6-1985-3036-ae26-d6668c851a6f | -5.54345 | -41.40557 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a9dc453-38aa-3b4f-8147-d814f95546a2 | -6.44648 | -42.34496 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b8f26475-d3c0-3999-8822-3a2a9d30484d | -6.08406 | -42.15059 | 2025-10-27 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e6b2aad9-2f82-3f08-a91b-d648e6164e37 | -9.2285 | -45.84544 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a095434-23fd-3517-9c49-4523b978ad48 | -4.20514 | -48.36081 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 865bff8a-f3be-3dd2-9b67-6aae388e1fa8 | -8.03432 | -46.73866 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5b0968f-c4d0-345e-af1a-d9f859ed1eb7 | -2.79654 | -54.86418 | 2025-10-27 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 60439b78-5f09-3bda-8271-077e1a9a1992 | -8.64982 | -44.77056 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe47aa65-abd6-38d0-b44d-02d3ffb83bbe | -8.49013 | -41.22726 | 2025-10-27 04:32:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f16d53e-42c6-3020-817a-077d94df32e7 | -7.85827 | -46.44567 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f3dde41-f426-33f4-bd4c-6ed073f41f7b | -2.61479 | -51.74738 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ac04aad-d17d-3a59-b6b2-3a8618e50df3 | -3.9887 | -51.03463 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2c85374a-0be9-390c-8451-c9483750d08e | -3.21597 | -50.79611 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb939f6-0603-38f1-ab53-17c08b45fae4 | -3.2418 | -48.7709 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c7b53e9-2aaa-316f-a902-2553bfb10af7 | -3.80178 | -49.29336 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81cf8428-ea01-3ac8-bcd7-116fffbea957 | -3.73246 | -51.35122 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 601200ae-045e-3992-ab3e-6e9c003e5726 | -3.35471 | -49.25471 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b63ee57-483a-3489-bf29-23b910b2b519 | -4.43817 | -45.97889 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34df65b3-7c01-3a01-b4fb-f8e722c51ef7 | -6.96408 | -49.40087 | 2025-10-27 04:32:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36f5511e-879e-3d6f-b52e-dc8acdb98961 | -6.13152 | -42.45361 | 2025-10-27 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2734404d-bc19-31b3-a951-6c1978f1220c | -9.85941 | -45.34646 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90d3e1f5-bc6b-3268-9525-cea67cd022c9 | -7.34892 | -42.43668 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8dd7f79c-ce22-3f20-8e49-5f27d2cadff1 | -9.56148 | -46.9353 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ac690d1-3616-346d-b220-0328cf4c8ded | -9.99219 | -47.15651 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d570052a-ba20-360e-8b1e-49c1d3794b26 | -6.29357 | -43.80959 | 2025-10-27 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 887cf94a-2937-3f62-8a0e-d5e0fd58b20e | -5.28752 | -44.62499 | 2025-10-27 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e939f19c-259e-3fd8-ae8b-cebb03582afe | -6.83423 | -44.0001 | 2025-10-27 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55d7e879-53b1-3182-8e13-87c3b271a76f | -6.82078 | -41.56588 | 2025-10-27 04:32:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eb33aedc-89d4-3661-8ad1-4586b589a2ee | -4.4812 | -43.41471 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7466ea6-bb36-3295-8a12-79fec3598c99 | -5.63108 | -47.62433 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f3093ba-923e-3e14-b58f-70dded678dec | -4.70563 | -47.4961 | 2025-10-27 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2aa110e0-2ca2-3398-a22e-22f8086786bd | -7.83581 | -46.47947 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a82815f3-33d2-3c5a-8be1-366aa034ae66 | -8.09582 | -46.97891 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 387920bb-05b4-3ca8-ba07-e664a44739cf | -7.8115 | -45.39311 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7d4ca8a-9dd3-3482-b6a5-9a0b944899d6 | -7.67833 | -46.3361 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cef14e1-1be9-37bc-ade7-8b17b758ecec | -7.86061 | -46.49807 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c40ed683-5452-35ca-96a3-586732e802cb | -4.45352 | -45.46773 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73e4be79-f930-3064-80af-832c36e98703 | -7.99696 | -46.20321 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bc18ab7-4cbf-3352-8674-4c98836b35ca | -7.83064 | -46.44535 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b65fe28-eb61-3a7b-badf-cd990dc8bf1c | -7.82781 | -46.44121 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dcb67f9b-5e9f-386b-91a9-ab512923fcf4 | -6.16165 | -41.55146 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 11d12c89-0094-30e3-99e8-6b57ccc332d9 | -7.2492 | -44.96349 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82acf4dc-be3a-3b71-acf7-2d4e8d903e85 | -4.15836 | -51.14158 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76489ac7-c1a0-3478-aefd-1c61d0be117e | -9.57537 | -46.89985 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88e49d06-131d-369b-a447-66b566c3730d | -6.13974 | -41.82555 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8f789fc3-11f6-35e2-a1ff-d111da5da1e8 | -4.15461 | -51.14103 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef91e9e4-d843-3821-8bf8-1329929920c6 | -3.71477 | -50.1759 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab84fed4-33fb-3c08-8a48-e03a996edae5 | -2.50532 | -49.05151 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d64d2e3-c80a-3de9-8927-b73f788d7757 | -7.83409 | -46.46811 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7af65eda-db9a-365a-b97d-62dc7330eaed | -5.88843 | -41.32156 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 618ca952-cec6-3dfb-b444-de11b7573385 | -8.36145 | -46.15878 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c7646bb-173e-3075-81dd-3e44184dd76a | -4.43762 | -45.98244 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef5955b7-0b3e-35f0-8878-8e98da748b57 | -8.02986 | -46.74537 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0a5487c7-0342-35de-b841-ec5b9e5609cf | -4.46726 | -43.43103 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c83885-a3eb-3ff9-a37b-ee1d841bb7b5 | -7.96666 | -45.47146 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| eab1b523-c8d6-3ff2-85f9-f3ae68b6e215 | -5.60464 | -42.77345 | 2025-10-27 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1168c06e-7e79-3ab1-940a-a472245326fb | -4.76063 | -46.42197 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad239bcb-bf03-30b8-9ac1-b8cf7c3788a0 | -6.49376 | -44.44859 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72c28215-3c85-37e0-b5b0-f15034a60e7a | -6.03699 | -46.56937 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ece7ac4-7b78-39ed-9253-5b13144cdadf | -4.44838 | -43.42141 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b905892b-3cf0-3e52-8040-bdb98d01d646 | -3.24065 | -48.77818 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c122a4fb-cda0-376c-9d67-32bff22e4c93 | -5.0538 | -44.85123 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e26737e-ca7d-3165-b7cd-9e4445a6a7bc | -9.48317 | -46.8598 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9109a0fb-adec-369e-bd9b-422bdbd131fa | -9.56224 | -44.71308 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bb21456-11e0-30c0-b6a0-20089d572c4b | -4.09371 | -46.92407 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e44dca74-cf5e-36ad-8a7d-cc5d4ae4a42a | -7.33432 | -42.44983 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5251b46-ccb9-325b-929b-84163c5647b9 | -3.25444 | -50.04071 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a0c759f-eff4-396b-af41-ea5958fd2771 | -10.21953 | -44.82175 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e222505f-428e-32ee-bd7f-56f87a48de09 | -4.49143 | -46.53366 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a47230a-adb9-3f7f-993b-84857ba3bed5 | -8.31588 | -46.18202 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a36e30d1-5d28-328c-9281-b03041da5162 | -4.73631 | -41.48269 | 2025-10-27 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ac06cb2-dc84-3627-9f8b-c5764257c5b3 | -7.9718 | -38.28469 | 2025-10-27 04:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| afba8067-e803-3ded-bbc1-0f6304188b35 | -3.5198 | -49.23432 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e01337af-badf-3bb1-a4c6-5ce5926d31ba | -6.41765 | -48.57558 | 2025-10-27 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0604709-4dc3-3926-b5dd-a7087387e813 | -3.25152 | -50.03607 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4e24a39-afa5-343c-8703-beeacd8db2a6 | -3.19553 | -41.42388 | 2025-10-27 04:32:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9193caf-006e-36a5-a2f5-eb4a479765ac | -3.04608 | -53.02069 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea4fcf31-89b2-39cf-85e7-eaa112f73ad2 | -3.14164 | -50.1587 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d05dd2b-d8c8-3855-8bc7-2b326c02e3b7 | -8.54391 | -47.20381 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f6674c-f576-3c06-b562-c20e7c0e409b | -7.33954 | -42.44296 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75c6fc3c-021f-34fe-925b-3e4e0b9f5db5 | -6.96379 | -45.52126 | 2025-10-27 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b9b48d-05a6-310c-a229-af75c16f34b5 | -5.82622 | -50.0306 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README34.md)
