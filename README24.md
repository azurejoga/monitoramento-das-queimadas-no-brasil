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
| 82ba8942-c4a9-3fb1-b489-d1f221653b17 | -7.30365 | -45.16006 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb626e77-e7ba-3940-928a-3e79ce69f2eb | -7.57735 | -45.47813 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 107b1e5a-6e7a-3ed1-abcc-9a52c3051de5 | -10.68612 | -46.46867 | 2025-09-19 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c50fc30b-c42a-32ad-9ec1-ea939f7a9957 | -7.51572 | -44.33391 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6d64163-447f-3fbb-a630-f6cc5168d7ea | -6.26298 | -43.91515 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0f3f97da-9079-34b6-813a-65fd63377bc3 | -7.5748 | -45.46554 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0e0551b-7f9b-3b81-93df-9a3523bfcf1d | -5.77251 | -43.71163 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ba18bfb-73a9-3e81-821b-6bd5d95358e8 | -7.5714 | -45.48917 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2797db16-7a16-33ed-b9d5-74f6fe4d787a | -5.71097 | -49.09702 | 2025-09-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2e669d8-e3e9-3a7b-b2c3-7ef1d50d551d | -7.26354 | -46.34577 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69313548-85a3-356f-81c1-ca1c7208d2a4 | -7.49575 | -45.2952 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89b34306-572a-3e85-9166-5006f4857559 | -6.38488 | -43.33466 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91b70333-3ca1-329c-9f88-e95d4e20091f | -7.83288 | -46.21172 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 625f73f3-d130-3c6d-a94a-abae62793965 | -12.0892 | -44.82736 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fe4558ed-0d98-3f30-a7c9-496f449f8e2c | -7.84054 | -45.63153 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 198cc62f-ee7f-33a4-8050-081117742595 | -5.54367 | -51.05599 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59fb4221-9e27-3d85-b246-0dba90d08ce5 | -6.25764 | -43.91929 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 062daf62-578d-3990-9648-4bac8e3119d4 | -6.26367 | -43.91035 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ab451b07-c9b0-3367-9c64-725ac5e3566f | -6.8295 | -41.0418 | 2025-09-19 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de8ff702-cdf9-3593-ae11-2b80b8b8c8a9 | -9.2081 | -40.25307 | 2025-09-19 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15ff41f2-ea7e-396e-889d-ebe4dbd020c1 | -6.20435 | -43.92634 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e8249aab-a057-369b-a5b0-9dedf5b27f3f | -12.03913 | -46.74198 | 2025-09-19 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7081fc40-7f86-30f5-8bba-c9feb8943cf6 | -8.0337 | -45.70152 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd88e18b-e71d-34c8-94ee-2ad0b8994973 | -11.08671 | -41.06963 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 69358c6b-1f25-3956-8c06-53f4dfa88463 | -6.31565 | -42.92623 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcd857fc-10e0-315d-a4e6-7b147f6d45f8 | -8.95379 | -44.20297 | 2025-09-19 04:46:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38f4dc57-a48a-3dbd-a828-1e828aa3e1e3 | -7.55546 | -45.4788 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ad553eb-8f70-376f-916f-f9169a17ac68 | -7.55498 | -44.78635 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 374c3d49-8a30-32a8-a3cd-e450a76ac8f2 | -8.37728 | -44.67434 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4681b1d9-2bbd-3391-8905-98424d604c2b | -9.17121 | -44.89001 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3647a7d9-9076-35fd-8bc3-55d3cda49acb | -8.61582 | -45.32921 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87e37485-a099-340f-9ecb-91574d622fd8 | -5.83288 | -45.91563 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0641c48b-079c-32b9-9d4b-219eee4dc02d | -6.93574 | -44.90357 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 260ca8e8-e3a3-3b33-aff5-e724a702655f | -7.56882 | -45.47683 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e02f3121-5612-34fe-b45b-c85487af133a | -5.80618 | -43.64537 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 050cc002-5b5f-3dd6-acaf-f15566126cd0 | -12.10082 | -44.84964 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 490cc76e-8a53-3b58-b3db-7e376df312ef | -7.56657 | -45.49249 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19e81366-6e9d-378f-b64e-a5b73fa9c862 | -10.92155 | -45.6409 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 178a8586-532b-3bfb-b799-d5eed4b9a972 | -9.16089 | -44.89753 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55248436-dabd-3593-94ef-303fe6cedffc | -12.10557 | -44.85043 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a498f94-aa93-3b78-8f46-f1577682c8ac | -8.98308 | -46.2261 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4f80207-b5c0-367e-86f1-184d97c2e712 | -10.37269 | -42.46245 | 2025-09-19 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| dbeeb11a-151d-3446-b0df-164125a8407b | -5.87046 | -45.88473 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c450834-2ca4-351a-80b2-ff2d9255ed90 | -8.95337 | -44.20061 | 2025-09-19 04:46:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c09e63d6-575e-368c-9931-e4531b225561 | -12.10203 | -44.80366 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0a88d8-0e30-33c2-beac-6a0cbbff08f3 | -11.18428 | -45.37034 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91d49eb6-6d6d-3dc5-9224-66033fd0f11e | -8.03295 | -45.73769 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7eae1b7-1276-3598-a5ba-f2bf0e16f5b1 | -6.49272 | -49.87564 | 2025-09-19 04:46:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c241b1-e372-33b7-893d-0d3395facaa9 | -5.12847 | -47.82783 | 2025-09-19 04:46:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 790151ce-20de-3ff0-9ce0-5952fe0dcc60 | -10.69084 | -46.4654 | 2025-09-19 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55dbe709-9f17-3382-8d2a-2144b9b9feba | -5.79185 | -45.35976 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9269441d-1c88-3e8a-9695-eca4b6be00e4 | -8.1496 | -46.78255 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0db15ed-8c16-3ae8-9173-dde298cb2967 | -11.16766 | -45.36583 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 136f6182-000c-32b3-9d7d-cd13e23b324e | -9.18779 | -45.31907 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 580dd98e-bb6b-3c4b-8532-c6cc14e4f9f0 | -9.17453 | -45.31715 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2fb6a97b-5b26-3bd8-ac66-5aeb8450ecbf | -5.80374 | -45.71508 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7bb713f-a1c9-3c21-bac9-be8a572f99b1 | -7.58219 | -45.47482 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0ba18e6-e126-3def-8b2b-665910ca6fcd | -7.21986 | -44.37148 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 865fba1d-8a4b-31e8-ac19-6d7bfb649fc7 | -7.92584 | -43.88738 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f544b58-f7ca-3a6c-9d0e-e56680654a86 | -7.84901 | -45.63288 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4d0bf98-d077-3779-9629-6576f35e86ac | -8.23807 | -47.83402 | 2025-09-19 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39d0c4ff-29ab-3aef-9889-5c3c4081c87e | -10.29412 | -50.23425 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d663ad66-a501-340d-b1a7-14a9323f274a | -12.10189 | -44.84571 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a58a938b-a344-386c-ba7a-f58867ff438d | -5.63696 | -45.94413 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2092256a-d361-3a9e-9fd0-914fb1555181 | -7.22971 | -46.60016 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| defda15c-7a7f-3b32-91c4-68f91426cbe2 | -9.17072 | -45.31209 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28e13fb0-35aa-3e62-ba15-aba7410ff59d | -5.95897 | -47.09463 | 2025-09-19 04:46:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d68466fc-d148-3bc9-9489-c66fc052372d | -7.85077 | -45.62039 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 207f2d23-703e-3fb8-968e-ec5e3e0a24c3 | -5.13143 | -47.83245 | 2025-09-19 04:46:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7b56db0d-773a-38a3-bf4f-c03b720826a8 | -6.11673 | -46.33648 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b99d5d3-df44-3d09-945c-31db9ccf3c5d | -9.86498 | -51.88219 | 2025-09-19 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ed8a61f-cfa4-3f87-867f-4b80cb86d1a4 | -5.80413 | -43.63726 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c0a7be3-0538-316e-b441-2e960d03dd0d | -5.87875 | -45.85652 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62f6ccfc-ed10-33b8-aa0b-dc6e5059286f | -8.14242 | -46.77645 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76d2bd5d-d55b-3344-b8c0-8a288a59e43d | -11.54699 | -50.55236 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37c5b562-97b1-3a47-9e7a-8fdcbc24ecec | -6.76414 | -46.00736 | 2025-09-19 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 041f1524-6d53-3fc8-a4e5-8f7ccd134381 | -12.03494 | -46.74136 | 2025-09-19 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f2d23aa-5706-3510-bad9-b0bee5354689 | -6.93933 | -44.75487 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06ca470e-e162-392f-bca8-04f12fc705c7 | -9.72978 | -45.92362 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f415cb89-708b-3a65-8ca0-09f47c17b3d1 | -7.56713 | -45.48857 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67f418c7-74b6-3666-afc9-02c5d796da79 | -12.11144 | -44.8469 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ce8156-bb81-319f-95f4-cd101e1e5541 | -8.03772 | -45.73439 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e281e36-6583-3301-93b7-8109983ccec6 | -11.90785 | -46.7876 | 2025-09-19 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8f40c71-969f-3548-9693-5f3c0a9b57f0 | -8.01996 | -45.70708 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08eb1498-8548-3688-9703-3c8db9dafb05 | -5.98147 | -44.1483 | 2025-09-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b383d4-efce-3ca8-8b62-0c188a8fb61a | -12.09662 | -44.80776 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5d1ced3-add9-35fd-bf4c-3bbc62263efd | -6.52022 | -51.20724 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6570617-9787-3e56-981e-02d1f596c9d8 | -8.0425 | -45.73107 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30950bd6-d482-3560-9294-4d5394759a59 | -8.8797 | -46.13423 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83ef72ac-dce4-306b-a393-7e4a1dc691b6 | -6.75899 | -46.01405 | 2025-09-19 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a58c110-e6f5-30af-921e-e922231b9918 | -7.85382 | -45.62951 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f66bdbb9-65f1-3b59-8fc1-2a3196743393 | -7.57102 | -46.73324 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f26aacbb-47e3-32bd-8238-96cb94e2577c | -7.55377 | -45.49068 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af3f16ff-d38f-3be5-95e2-e5e5fb82ba8c | -11.09519 | -41.06483 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bab7ebab-f4b6-338d-913f-11cb62027b78 | -7.00429 | -44.64001 | 2025-09-19 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7247b1d-2a93-3aa7-9ff5-98f27a2f0cdd | -6.90057 | -44.77225 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7272b0a3-dcfd-36bc-9337-e9cad8e7c3c6 | -7.23365 | -46.60077 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4609c896-39c8-3427-a17b-ded034592254 | -6.83338 | -41.04254 | 2025-09-19 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e1103d3-fcac-34ff-b27d-74ef7cd13eeb | -10.29468 | -50.23054 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6fefd331-9548-38eb-8846-f3e479c44c6b | -5.46243 | -46.68317 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README25.md)
