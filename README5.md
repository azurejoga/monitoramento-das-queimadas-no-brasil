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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98753f8a-56d6-3b1b-a1dc-78abdd762931 | -5.4794 | -42.666901 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 372c9ff2-1e41-3355-817f-b04ba2c7c3b8 | -7.8349 | -44.800701 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 015cc7c8-67c4-31cd-8e3e-1e9291f646b8 | -8.4459 | -47.318699 | 2025-09-08 00:25:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89f2686e-f5f2-38bb-b828-81f0bd601475 | -9.9739 | -51.6506 | 2025-09-08 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6d14123-5b6e-3f19-9ae0-5fac3c9ee082 | -4.2551 | -48.193802 | 2025-09-08 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c142ba-edbd-31e5-9e1e-0344ce3c4d99 | -7.5423 | -40.107899 | 2025-09-08 00:25:00 | METOP-C | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 278eeeda-216a-3bb1-a353-14ecad6b2fcd | -6.209 | -49.414799 | 2025-09-08 00:25:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88fc474a-97dc-39f5-ba46-7ca5a79c74ea | -5.3403 | -42.645302 | 2025-09-08 00:25:00 | METOP-C | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e82799f-a751-3f96-a92c-133e4aa185fa | -8.7297 | -46.693802 | 2025-09-08 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f143d98-2041-3923-a6f5-931637b46057 | -9.9677 | -51.6702 | 2025-09-08 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6baa2ca-92aa-3f68-84d2-4eaf27fe5879 | -8.019 | -44.066601 | 2025-09-08 00:25:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7429b2b6-4e7a-3929-9eac-39116a10fd6c | -15.1924 | -44.0215 | 2025-09-08 00:25:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7a8faf7f-7eab-31e2-aac1-609653189e8e | -14.4938 | -48.8008 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e1d84e9f-d742-3b02-8bb9-0c8c63ff69bd | -5.8704 | -43.959599 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f84e4db7-fdc6-360e-abfb-5bfd8b33686b | -9.7108 | -43.983299 | 2025-09-08 00:25:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88394696-8d5b-3cb7-9ada-bd26524a0c36 | -6.2078 | -43.318501 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54e98e66-c58c-3410-8a3f-3872d9b69aa4 | -6.5141 | -49.499599 | 2025-09-08 00:25:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0fa8066-2a71-3fd4-a6e4-7343fa93b47d | -6.5324 | -42.936199 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57dc504c-2abe-3f49-9b92-bf1eb0a30d90 | -7.0686 | -45.193501 | 2025-09-08 00:25:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c55e8cf3-3d19-3ef1-88d3-0fde5a468f42 | -6.1645 | -42.639301 | 2025-09-08 00:25:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5cc741e9-92df-3266-b549-6a1b2e4e5359 | -6.1921 | -51.449699 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a890bf0e-6452-37da-bc30-ff5541d5a084 | -13.7114 | -46.900101 | 2025-09-08 00:25:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f9db031e-ee26-369f-b275-9bf35664e54b | -17.137501 | -44.4375 | 2025-09-08 00:25:00 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d58d58a-47e2-36da-adb1-bbe0b6b917da | -11.1752 | -54.9925 | 2025-09-08 00:25:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 733fe72e-aa36-3c80-932b-7d29c9108e75 | -5.5346 | -45.6982 | 2025-09-08 00:25:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 464ad406-e4d5-3560-b326-827d76e30403 | -5.5341 | -43.797501 | 2025-09-08 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54fafe33-fd49-38c7-8aa1-73ca9f11d1fc | -11.4061 | -43.6437 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64bfd49a-8079-3d0d-8596-c5875537b5c6 | -16.8922 | -45.8274 | 2025-09-08 00:25:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 65f46b63-6d67-3a54-88bf-f62709a3f0dd | -19.875401 | -41.439301 | 2025-09-08 00:25:00 | METOP-C | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 331a6669-a1e2-3d3d-8728-34329ba108a5 | -6.3918 | -42.9977 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e65a5a35-8c48-390f-8841-bdf606ee8b7a | -7.5496 | -43.6814 | 2025-09-08 00:25:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 496033d5-0d79-3e60-a676-cc75319d4a5e | -4.4005 | -47.605701 | 2025-09-08 00:25:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5c78ca-d1d6-34bd-8404-24edd01c10ad | -8.2104 | -44.775799 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb55c861-4172-3dae-9fd4-c22335f84bbe | -7.6381 | -47.939098 | 2025-09-08 00:25:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5e952f-3b71-31ae-8a1b-e65d0dacad4a | -11.3775 | -43.561901 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0e1d53a-ae05-396a-8b48-340c275534f4 | -6.8534 | -47.916302 | 2025-09-08 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a05816e-75e9-3964-a26e-7bd17da3f07c | -13.3409 | -44.4366 | 2025-09-08 00:25:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0405e790-3888-373f-af8e-8081b4761c36 | -8.1974 | -44.763901 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 690934ab-e4ef-3ebf-a621-b97231035aba | -8.0746 | -44.813599 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5f8de66-9068-31d4-878c-478a0788b50a | -6.1788 | -40.9776 | 2025-09-08 00:25:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| edab4b82-89d9-3941-b02b-370335e178f8 | -5.4287 | -43.429298 | 2025-09-08 00:25:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c27fe93-75d7-3bc4-bc95-52c8ad649ff0 | -6.1785 | -43.594101 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d3d4c0f-9407-3c67-9d15-cb4c735ad823 | -19.1957 | -43.745899 | 2025-09-08 00:25:00 | METOP-C | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37193e90-ed15-35b4-b5ef-c4f4a1c1155f | -19.3832 | -44.5112 | 2025-09-08 00:25:00 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f086182-080f-3faa-af80-2c9bebc3f435 | -5.9429 | -45.772701 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1cc5c7-c466-3e56-ae7c-4a8373d91c73 | -11.3619 | -50.396999 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f006fa8a-79ae-362e-a79a-a7e545a64f93 | -7.3754 | -44.002201 | 2025-09-08 00:25:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2023599-ba98-34b6-8a76-fa2bf61b3ddf | -5.8562 | -43.4492 | 2025-09-08 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 512dec20-2c7f-3118-91fe-11d9b3edeab1 | -5.9301 | -45.6703 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13381204-1300-3fcc-899f-45183f114002 | -9.1814 | -46.038799 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8807c59-636c-3e7b-9a77-f4f299ea6bc2 | -6.0098 | -45.8867 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0059cafd-6a7a-3051-913b-a5f51635ec1d | -14.508 | -48.770199 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 16318587-fa5c-36bc-a58f-208a0f604c11 | -17.525 | -43.7463 | 2025-09-08 00:25:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 735bdc8c-64cc-3fc5-94ad-e5d525ba9161 | -5.8606 | -43.9618 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9b4dfe0-6bf2-3a40-bcc3-9c7958b8a719 | -16.8941 | -45.837002 | 2025-09-08 00:25:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3a6abee-cb40-3a36-85ee-00f8155d56c2 | -5.6485 | -45.428001 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87ba3950-be64-3460-896d-3cf80326b282 | -6.2527 | -43.6931 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f37c4e06-41b1-3fa3-9347-87c6966ef557 | -6.1994 | -43.371399 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 723fb6e4-0cf3-3304-baf5-ea4a7afb30cf | -15.2787 | -43.377998 | 2025-09-08 00:25:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| eee16e72-94bd-3157-bec5-78da0613ef23 | -6.5166 | -49.510799 | 2025-09-08 00:25:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4bf936-798c-39a5-bbdf-2d2721044c18 | -14.4813 | -48.789398 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b7b962b8-13ff-33e8-a8a0-c95bbe0c1c25 | -5.859 | -43.955002 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2d7f0b-c19e-368b-92dc-415bfb11e8ce | -7.8333 | -44.793701 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d669a191-fb3f-34f0-8030-0016254080d0 | -14.484 | -48.802799 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b02301e1-a1e4-34c4-a0bb-af83d5672910 | -6.2889 | -42.1978 | 2025-09-08 00:25:00 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24c714e7-ae80-3ca3-b4cc-bc965cf17eff | -5.1944 | -45.8335 | 2025-09-08 00:25:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66fc11cb-3554-31d6-88d7-87a2ea3382d4 | -7.0803 | -49.939899 | 2025-09-08 00:25:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933425d1-6ae0-3a3c-9a0d-a49726f52ef7 | -17.629801 | -44.7873 | 2025-09-08 00:25:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4e6136-24dd-3582-8bbd-df7ba62bb358 | -5.8735 | -43.973301 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fd2bf5a-a2e2-3d64-a3f4-e6ef1f9b6963 | -6.821 | -44.8731 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c49b7a9-ff74-331b-9768-e7b045fde263 | -6.6238 | -42.974499 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc32d04e-0285-3831-a83e-b9e8147a89a1 | -14.5008 | -48.7854 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 541ac223-dbd3-3aa0-bc86-4562e5eb1fc4 | -12.151 | -43.936001 | 2025-09-08 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65d5e0b6-b552-386a-9af6-9a5498758835 | -7.0632 | -43.899502 | 2025-09-08 00:25:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7723797-5ae9-31c1-9a46-0e0f303ea84f | -6.2445 | -43.702202 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0757e78-716e-3448-ab1c-833930a9a1ff | -6.1912 | -43.3806 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af5db743-862f-38d4-93dd-9c977f2a614c | -6.2047 | -43.3046 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7a0eb6-6f0a-3f51-b0f6-f51788da38e9 | -11.4046 | -43.6367 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9eca69af-5c24-3a43-9d19-96df2594d7ad | -5.8637 | -43.975498 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f58ecbf-2544-3adc-964b-562ed148bd67 | -6.8242 | -44.887001 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 255fabe6-5aff-3863-9209-84ed12244cba | -3.2924 | -48.711399 | 2025-09-08 00:25:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b27e50-7765-34c2-a83c-5856a7bc6de8 | -13.636 | -43.812302 | 2025-09-08 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4bbe8511-a92e-352f-a8f4-0bd918e356a4 | -5.9296 | -42.9622 | 2025-09-08 00:25:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2189130b-5ebe-3ea5-a601-03c4975867ce | -17.568899 | -44.542099 | 2025-09-08 00:25:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 58769528-6a13-3c31-b130-8213b6654c00 | -20.617001 | -42.5009 | 2025-09-08 00:25:00 | METOP-C | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 01e53609-5b4c-3f71-9269-4b41be099170 | -13.3425 | -44.444099 | 2025-09-08 00:25:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb1963ee-2345-3631-8709-59e8e8da87d7 | -18.344299 | -43.937302 | 2025-09-08 00:25:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 69aa906b-5911-33ca-b09d-ce0e69fed0a7 | -17.147301 | -44.435398 | 2025-09-08 00:25:00 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc671327-1e05-3865-90a0-a6d84e191928 | -8.0131 | -43.8148 | 2025-09-08 00:25:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d677efcb-b277-32ff-be8a-936c27c84505 | -12.5201 | -49.0938 | 2025-09-08 00:25:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b478c71c-91ad-3f9f-a1c4-09c4e82a8fdf | -15.1101 | -48.065399 | 2025-09-08 00:25:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44f9374a-3227-308f-bb60-812a0188a3ef | -8.606 | -40.1954 | 2025-09-08 00:25:00 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f9221039-99cc-3538-9986-ed4f08f1727c | -5.9266 | -45.746201 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3432861-c178-3201-ad49-3e8a881af758 | -9.8309 | -48.855099 | 2025-09-08 00:25:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0325e190-e6bd-3778-9eba-66d6ac21d9d6 | -11.3888 | -43.5667 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff8989e-8e35-375c-9462-81711a979159 | -7.5584 | -44.6717 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e069c6c1-c63f-37a3-ac74-9081f86b27e4 | -13.6544 | -44.225101 | 2025-09-08 00:25:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a330257b-6cda-3bce-aa54-97b48de6bff3 | -5.9298 | -45.760601 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f567995-c2e7-384f-aa8f-6226def8c6c3 | -19.1817 | -42.081299 | 2025-09-08 00:25:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47b3bc39-0ed6-396d-b0c5-5e4804004a0b | -12.9278 | -54.7668 | 2025-09-08 00:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
