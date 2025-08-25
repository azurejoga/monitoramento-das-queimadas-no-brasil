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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd89797-9a01-398f-bb4b-aae12df0cbc8 | -8.9689 | -65.4198 | 2025-08-25 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ce7021c9-f709-3904-b229-84debcb6d0c4 | -8.9874 | -65.4192 | 2025-08-25 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2dde6a4d-4cef-3b31-abf5-50e715635a7c | -10.7206 | -47.1365 | 2025-08-25 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d81207d8-31ee-3b85-b8df-77292be268d7 | -10.7015 | -47.1388 | 2025-08-25 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 008263d7-6cb8-3a1f-a564-5b01a637578e | -11.6089 | -46.3699 | 2025-08-25 11:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 30a9d6f9-475a-3666-a787-94552d2f78d3 | -10.7209 | -47.1142 | 2025-08-25 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ebc0569b-6979-3a28-a2fe-f56f202b6934 | -12.3078 | -49.1421 | 2025-08-25 11:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| c706da2c-da71-3016-b892-4e0bf4d11ea1 | -11.6089 | -46.3699 | 2025-08-25 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 42b8f467-c05c-3faf-bb63-cfe8b01e627f | -12.3078 | -49.1421 | 2025-08-25 11:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 417185b1-ea4e-3668-9f6a-a8ac9f375c96 | -3.4542 | -43.3386 | 2025-08-25 11:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4269fe32-18ac-387e-ab8e-8eec6f42dabb | -10.7015 | -47.1388 | 2025-08-25 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8ffc330a-59fd-3ec8-ab36-ae5efdf9bfba | -11.6089 | -46.3699 | 2025-08-25 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| de5c1de4-eb06-3304-8ff3-1fae28a3b687 | -8.3202 | -47.2635 | 2025-08-25 11:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0fac33d0-9f90-3ee5-a7a2-bd6e3b3e436c | -12.3078 | -49.1421 | 2025-08-25 11:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3d0849fa-5fd0-3571-bb1b-68f7e75b1ca8 | -11.6089 | -46.3699 | 2025-08-25 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e2c4ad6e-f2b9-37da-980b-58af8d5958f1 | -12.3078 | -49.1421 | 2025-08-25 12:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2cf233ac-c93f-3794-802d-b010e54dec44 | -12.6937 | -47.8339 | 2025-08-25 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7bf9e2bc-348f-3349-b6e7-869c4de29ec3 | -13.3936 | -51.802 | 2025-08-25 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3cf7ab99-17c8-3f3a-ba9e-e122e1d92d94 | -12.3078 | -49.1421 | 2025-08-25 12:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ebd5c1d8-fc62-3bdc-8b5a-d0a37ad58ef2 | -5.6254 | -45.1612 | 2025-08-25 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f02f283c-5898-3f7f-a63e-6f93420ab33c | -11.6089 | -46.3699 | 2025-08-25 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 9f54d2e2-caaf-383b-8bf5-09685b869496 | -5.69071 | -45.13374 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 581fa18c-71f7-3ed9-8958-977e35cf658f | -6.90655 | -47.92505 | 2025-08-25 12:14:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3d6d0edb-85a8-345d-9d61-6fbdf74a4610 | -10.49251 | -46.87714 | 2025-08-25 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d7d6b8f9-d523-3a04-b08c-31c894cfa43c | -10.74899 | -47.01628 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 16836d6b-4709-341b-8e80-7844a8857f85 | -6.89712 | -47.92357 | 2025-08-25 12:14:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e8c8a95c-6fba-3027-9e1a-cb2099f10d80 | -6.41746 | -44.69054 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 386e0a22-86f8-37ff-b63d-c7425d3683eb | -5.10663 | -43.20657 | 2025-08-25 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 5f7e1581-eac5-30ff-9979-75fe48a4db7c | -7.33372 | -44.53133 | 2025-08-25 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d299b204-867c-390e-aa66-2d0b766cca7a | -6.03529 | -44.00193 | 2025-08-25 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a145df4-ff12-3aee-ad36-53fb5149800e | -8.24017 | -45.0961 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 307e6b63-c344-33c7-ba4a-055e4b78c14a | -10.04065 | -45.59234 | 2025-08-25 12:14:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f261d458-c830-3300-a617-a961a82bae38 | -5.94168 | -44.14303 | 2025-08-25 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54bb7fff-77e1-3c37-b842-c153a4dc33d0 | -10.81443 | -46.37664 | 2025-08-25 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64b7e198-3ce6-3ef9-8289-a27e94cd31b1 | -8.4143 | -47.39728 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 74fa3017-0a8a-3918-8383-80ce27638be4 | -5.12243 | -37.82611 | 2025-08-25 12:14:00 | TERRA_M-T | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 6ee796e1-48bd-37a9-964b-6878b5433950 | -8.28063 | -47.24099 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9d66f4c2-51bd-3692-9a11-e23354efef13 | -6.24653 | -43.74931 | 2025-08-25 12:14:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 962dfcdc-191c-30de-a654-776797628974 | -10.71147 | -47.14928 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c8764663-5ef3-3665-9ba4-f388db5a52b8 | -5.89252 | -43.38013 | 2025-08-25 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8868c8d1-f430-30d4-b9f7-e41779fc8f67 | -8.32174 | -47.27559 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6a08ef07-482b-3f1a-a63c-e8fb34817909 | -7.58746 | -46.24133 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e30c9287-11a0-3c1d-a200-227865e3dcc4 | -10.59279 | -47.14391 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 75a98b11-2f74-39c9-834c-7ac0117d5f63 | -10.81315 | -46.38556 | 2025-08-25 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97966f76-26eb-34c6-ad5c-1498109e78bf | -8.87256 | -45.45414 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 999c5f29-548f-3f47-b2d1-09c0557ddb3f | -5.52683 | -41.29364 | 2025-08-25 12:14:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 35.8 |
| f394a214-7927-30cb-a335-777782e70fd3 | -6.65289 | -44.39393 | 2025-08-25 12:14:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1d8807d5-921b-35e4-91c2-ad0fa36931c1 | -10.28237 | -46.74257 | 2025-08-25 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9e22c01a-e7eb-3db1-b518-7352320067b5 | -6.71701 | -43.06386 | 2025-08-25 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fd83e634-21d3-30a6-9fef-aaf8cb6d1f59 | -8.06536 | -49.68423 | 2025-08-25 12:14:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b1f51a99-3f22-3d95-abe0-1134776e5a8c | -6.68066 | -45.43105 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2c72c68e-9787-3b89-abd3-995e703bac3d | -5.63258 | -45.14657 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 9a7447df-2862-3c23-9a3c-d2a8b81fa9b3 | -6.03661 | -43.99245 | 2025-08-25 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f3998425-1a1f-3d8a-91e0-6ca417f9a839 | -9.84318 | -46.46584 | 2025-08-25 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| bd67f69f-51c6-3f4f-8266-42a0ee687899 | -8.04323 | -47.34723 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b38d0744-a1ef-327a-83ee-c3128d94c313 | -6.06379 | -43.99617 | 2025-08-25 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e601b427-b839-33e5-98d5-7824d3be0675 | -10.71676 | -47.11301 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ddd42c74-3635-3800-ba17-5709590bb577 | -8.23761 | -45.11409 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5934dc85-d1de-3a3f-890e-b44198ba49a3 | -7.59632 | -46.24256 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6a1bcb09-a2b3-3032-a2ef-a2e204ff39a5 | -7.08412 | -44.08061 | 2025-08-25 12:14:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e8d3e3c3-8a53-338b-a8f5-9c3c8cb6f459 | -3.4549 | -43.34326 | 2025-08-25 12:14:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e902a091-7ecf-3135-b1a4-354f759cb9ae | -8.8979 | -48.11958 | 2025-08-25 12:14:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5ea5e36f-1e32-337d-8c36-ad5a4142071a | -3.70367 | -42.19226 | 2025-08-25 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 44bce581-af72-34f2-8a6b-c2afc65a9e05 | -9.88793 | -40.62847 | 2025-08-25 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 1392256e-7067-31b4-b74d-350206db2745 | -8.46319 | -48.23601 | 2025-08-25 12:14:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 827e08a8-cd01-3eeb-807d-fe13327e3387 | -10.82397 | -48.32604 | 2025-08-25 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 120fd2da-d23e-3a82-aa9d-3d1807198e6a | -8.88142 | -45.45538 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dc8fa8a5-a86c-3324-8294-6060a4619032 | -5.81174 | -44.99516 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 51430356-ef0f-3c97-b83e-08549dc4d824 | -5.63384 | -45.13777 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dc1a60a4-2be8-3229-8f66-9a2fa1c99110 | -7.73324 | -47.45144 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 626878c1-58bf-3ac1-b084-4057d5e51bba | -2.95606 | -42.95728 | 2025-08-25 12:14:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 02a50552-f0be-3cf6-8473-77f10665d108 | -3.70622 | -42.19856 | 2025-08-25 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| fb9c7402-0af4-33fc-88aa-707860ed19b4 | -7.14762 | -44.15307 | 2025-08-25 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 75e20bdc-c657-340a-bd68-bbffd5d96e20 | -8.80472 | -47.31667 | 2025-08-25 12:14:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 97090466-41c8-3dbe-8edc-ac1d4dc904ca | -6.36044 | -43.65041 | 2025-08-25 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a5fd2f69-9ee0-3117-b69f-7ee6b78da244 | -10.72565 | -47.11432 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| c640e69e-d0d1-3981-8993-7c9f1811443b | -10.53816 | -46.76202 | 2025-08-25 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 440d93b7-219c-3109-8ba6-1df5cda8b0d4 | -5.81048 | -45.00399 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b034efaf-267f-3990-8a13-0ea0760eb971 | -6.19172 | -44.13372 | 2025-08-25 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4c00a731-bd26-302c-a72d-ced0c1575d27 | -7.59245 | -47.46373 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3bca3255-a678-31bd-bb47-d82c29344c4c | -9.8944 | -40.62284 | 2025-08-25 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 486c5ce3-8094-3e8c-876a-bda46729085d | -8.31128 | -47.65787 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a0f51742-3d8b-3f2b-a3fb-4b63b8fa1d3c | -8.40521 | -47.39597 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8b6ec6e5-6087-3def-a7b6-0129401ecf48 | -7.91622 | -45.88167 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d4a2f6d5-4890-378f-95d1-48381d5d3c66 | -6.37175 | -45.20081 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2e954f08-50c0-3d2d-b40b-67c9c6305ffa | -8.4038 | -47.40541 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 09698d0d-8de3-3b55-a0dd-505c9bed285b | -8.75565 | -49.95171 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f3495b00-4fd9-3762-996b-1a09f8a60e39 | -7.2889 | -44.45956 | 2025-08-25 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bfb72bbe-b40b-3c26-a9a5-241d74667f05 | -6.36503 | -44.47438 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 868e1be3-e73c-32a0-80cb-1ac0ae78e10e | -6.35248 | -43.65266 | 2025-08-25 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3c7c668e-f48c-352d-a892-ddb11aeef3d9 | -10.37753 | -47.9113 | 2025-08-25 12:14:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8f5a1d4a-5886-37b0-8b5a-2d90e0e273fc | -5.86659 | -43.89023 | 2025-08-25 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d0f0beb-1099-326b-aa45-a3c82387af3f | -7.62168 | -45.23686 | 2025-08-25 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2dc32bd9-eaeb-33ec-8658-3e1d1bd54c01 | -6.50617 | -42.94274 | 2025-08-25 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e3971bcf-2d70-3f0b-8f53-3fd6ff27347b | -7.59292 | -45.23548 | 2025-08-25 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 438ef8f4-76de-357d-987c-4065408db5fd | -7.50645 | -45.83744 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 093fa493-58c3-3e0a-bb0f-979936348ace | -9.84448 | -46.45692 | 2025-08-25 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 24f2065b-2d53-395d-b796-e1948190905b | -9.38923 | -40.61422 | 2025-08-25 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 49cdd7ad-229f-3d30-9e7b-3dda86e7725c | -7.62294 | -45.22796 | 2025-08-25 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c064d715-b049-3d20-8a8f-b6a57b10f382 | -8.07469 | -47.32291 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README93.md)
