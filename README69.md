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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ec30c2b-ff53-35c0-ba21-3b3e84c15d5b | -8.17057 | -46.42516 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a78f15a-b13a-3873-a67a-1250bb424c8e | -12.01649 | -47.08293 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c81ce17-6603-3ed2-bd8c-328b25400ddf | -11.98943 | -47.03863 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b020247a-c8ad-3496-abd8-ffdcb2be55d8 | -6.53279 | -43.825 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| def71de0-835a-3fc3-97d3-ba6463585449 | -6.33091 | -43.54059 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1a1df19-3c59-395c-9715-c8ff3e761686 | -7.14994 | -45.5078 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90152438-5546-3f0d-9a44-4269ff15f6c9 | -11.51077 | -46.95113 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c42a2ba7-2ca8-3dfc-a3d8-c37e2be3290d | -7.80835 | -47.0191 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 445698ca-8c3d-32dc-98fb-931dfe6360c4 | -7.18179 | -41.70511 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 102bf418-ca70-3bfa-bfa5-29532072a4a9 | -7.81057 | -47.00514 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f03e8f2-9c01-3a52-839e-c2b2ac5fd2bc | -10.58462 | -46.27264 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a375ff63-91b2-37ba-9bf6-aec8cce3ac15 | -6.48107 | -44.24723 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 123de2d6-4dae-3c53-a8a3-b0c72fcf6211 | -8.62929 | -44.84996 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ed341a0-c3cb-307e-8f4d-010ee57e269f | -8.57981 | -46.99625 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7aa5075-ea4f-3dda-92f6-8d510eaaff54 | -6.4988 | -43.72067 | 2025-09-28 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4003a34-77ca-328d-9991-a8e0ce47698e | -6.09529 | -49.39254 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de311f91-d941-3c8a-9f8c-be7c4e2640d8 | -6.32066 | -43.46601 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec6c2cce-f31c-3404-be25-de64b7c8589e | -10.11571 | -45.66085 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f78c299-9843-331e-98a3-79dc54f1e0d6 | -7.80005 | -47.0285 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 25d3718b-fdff-3d11-b3d1-234d9d576e79 | -6.05494 | -44.86769 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32fc0c3a-21c8-3b31-bb78-5c50138a934b | -7.75104 | -46.97426 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1be355af-3c0d-32da-8589-fd29d1a65eab | -11.62239 | -52.84415 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 920957e1-06a8-3a3d-947e-73540946a7f7 | -8.27941 | -45.44336 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab8d3e0b-3ade-34ae-ae42-70ae329b2159 | -9.09044 | -45.86079 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a90783a-d46e-3bf4-99c4-4acc6968dbae | -8.17053 | -46.40383 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8a213bda-8908-3e67-a1b1-0cda2fd437ae | -12.73328 | -46.8161 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bac9308-48ce-3939-9b41-038b0a5848dc | -7.3726 | -47.02456 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 48e3a7d1-c953-3826-909a-b6babfefa85e | -12.10041 | -44.31298 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 675e3988-be12-3f3d-a151-2e29ee1e2939 | -8.62471 | -49.06648 | 2025-09-28 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb04d68f-01fb-3ebb-95b3-bb43314fe7bd | -12.73438 | -46.80896 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f7ffa9-8160-30da-b65f-e750deed0581 | -7.87647 | -44.5544 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9600d11e-1361-3284-bd37-7e1cdedee626 | -10.75235 | -45.3903 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b50d6c6a-fe03-3713-a440-787505ed18d4 | -5.51026 | -44.91433 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e0aea23-5f25-3e02-834b-dcf22b2eb6a1 | -10.81655 | -45.38086 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d7b041d2-b816-3444-9651-d790ba122aa0 | -6.15188 | -42.80467 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 450b742f-6136-3524-9fe3-921c8818765d | -8.49295 | -47.81874 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 974d519a-f3d8-374c-afa9-677f9b846477 | -10.04323 | -49.20228 | 2025-09-28 04:25:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1716d0ba-6c58-3423-937e-c2bbe52209d3 | -11.98722 | -47.89336 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 354a7063-b140-3a65-a323-7518aef7bfa8 | -10.17825 | -52.57337 | 2025-09-28 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b80a365-4eea-37d4-8e98-95affeaa751a | -8.14021 | -42.37163 | 2025-09-28 04:25:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7946cd6-6d08-3295-b0d5-5c118f0f1be8 | -12.95175 | -45.142 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aad7e3e-05fb-39d4-a67f-da059410095c | -7.62553 | -43.79888 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a20f1994-eeb1-36d1-a480-32174f836618 | -7.44894 | -43.17276 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 79375d34-b0c4-30ad-8dcb-f6f52b60ee96 | -6.43609 | -43.51434 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35f2fc09-1560-30a5-9b6c-f02a2b7c9c20 | -7.4358 | -43.03592 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40d08a57-9ab3-3da0-99c5-7b36d73d3407 | -11.98944 | -47.06031 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc2ba4f8-8acb-3b67-abea-59bb28791d37 | -11.3556 | -45.04959 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75227028-b0d7-3b86-bbd5-524a33faa8c8 | -6.78117 | -44.04885 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67db2d40-40eb-3bb7-94c2-8ecbbd61e82b | -5.89958 | -43.28716 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1d10efd-2e80-31ea-b926-84861b9dbaa6 | -12.06187 | -44.86227 | 2025-09-28 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ad2f90a-f3e4-3c8c-9fc9-02e2ad559c19 | -12.68329 | -46.87763 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b48273f-ce23-3e82-ab17-102ba62995ec | -6.42965 | -43.50925 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82b2fe9d-016d-3530-87ad-ec33394d9008 | -9.75092 | -46.13387 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 061336ad-ee40-3d3e-a021-9013279baaef | -11.09721 | -54.28347 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a6c775d-e312-32b1-8054-bf7404e5cad3 | -6.09319 | -49.4024 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 89697461-1518-34e3-8222-90f4898466f6 | -12.0016 | -47.09118 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6c2a8fa-dd07-3db7-8248-2abbf2d1807c | -10.14256 | -46.47406 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42cd72ad-0ac4-399b-85b9-12cf292b5da9 | -11.37924 | -44.93781 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85391a99-031d-3d3a-9e6a-32339b3bf52d | -6.05815 | -44.86101 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db7754ad-fe5c-3c0c-b23a-0bb6025407d7 | -5.39336 | -45.85824 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24081229-1fb3-328e-8532-94be493b8a48 | -11.4321 | -44.91778 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d79efc0-c480-3a5a-a383-041e2c1649b7 | -12.00843 | -47.95098 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86e3d3ae-de96-3f2a-aa0a-5734d00c2cb8 | -5.64208 | -44.91994 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 328c08ab-47cc-3caa-8ac7-5168d1a89e1e | -6.69809 | -44.61187 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d42e8fc-f6ad-3f88-b721-8e4e2e4be91e | -10.41138 | -46.14351 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f92e014d-ba57-31df-9051-64c1f10e582f | -6.62591 | -45.90371 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e86ecf05-cd88-3813-884f-e59dabb124a4 | -11.85705 | -48.23879 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6685f5b6-f70d-3d3d-97b1-fe6ad5bcd579 | -5.90192 | -43.29565 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41823d08-0390-38bb-9d5f-1e610ea6204d | -8.52155 | -44.61589 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da2bd7dc-617d-3025-acd1-ada1726ee7c1 | -11.60343 | -45.42964 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a1669f0-00a0-3f03-9d42-17c0bf32ebea | -5.56853 | -45.11065 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cec2df44-e2d0-3c6f-abc3-c4462f70cfa7 | -10.60074 | -46.2788 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25331d4c-de6d-317f-8727-8590dbcd71dd | -7.75601 | -47.00719 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67002e88-e0f3-3910-baf9-d04c35e6956f | -7.34996 | -46.56859 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9732417f-1486-3708-aacf-d366f8d5af98 | -7.93688 | -45.68437 | 2025-09-28 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50e59c30-237f-3a2e-8671-d67d24b0d142 | -6.70992 | -44.58032 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14808747-23e5-3320-b4f5-4c6ce5cc093c | -6.15457 | -42.78445 | 2025-09-28 04:25:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07db33df-5f0a-3d35-9935-5bf4bf8a18da | -11.42491 | -45.03667 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| db8adf6c-7a56-33c4-8935-1579ebffeb05 | -6.54941 | -43.81885 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7841d670-46c3-3c0a-be6d-8129041ae2b9 | -11.60285 | -45.43344 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 425318c1-3813-393b-acce-b9024c1ebc7a | -7.104 | -44.22849 | 2025-09-28 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 388dc6e5-fa03-3eee-a088-6268d07e85d4 | -10.45433 | -50.85556 | 2025-09-28 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6154ba99-a62a-31c8-9eea-f4afa846edd7 | -6.7783 | -41.75239 | 2025-09-28 04:25:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9dabb82e-488b-319c-b97f-2af308703b92 | -11.5174 | -46.95219 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76f1deb4-b1f8-3e35-8ebb-6fae48d7b432 | -12.00637 | -47.89993 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54666f6c-055c-3a5c-b15e-dc78f897db64 | -7.59674 | -43.05812 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 88931247-d1d9-3871-9ed1-c321b6f49722 | -7.8622 | -45.28793 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1187334b-22a3-3ebb-ad37-3780e7932bb3 | -8.48854 | -47.80338 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6ae0f98-37c2-3f44-a5c1-2202db022c09 | -8.49699 | -44.73143 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 095b06ed-eb42-3604-8827-4ab074ee3cca | -12.0073 | -47.95803 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6218c68a-61f8-3494-9dec-27c661ad8b05 | -5.94623 | -42.90509 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d36335e0-329e-355a-b85b-c0d19bdc8f79 | -10.965 | -49.56942 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dc12864-4616-33e5-8869-ea15af205598 | -8.48797 | -47.80694 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0c42b25-14b7-3aaa-a69a-e546b6ece11c | -12.82414 | -44.68414 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0331d20e-3047-3e69-b7ef-ee0fd6e92f26 | -11.60203 | -44.33168 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c62945-bba2-3b3c-85a8-efa878065d44 | -5.64543 | -44.92046 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6d6a4f8-ee9e-32ef-8f57-5e1d84df2668 | -6.40278 | -41.7425 | 2025-09-28 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cb88890-6b94-3438-b02c-0f5ad12ab2e5 | -6.76467 | -44.5918 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab811a57-3218-30a9-91f2-48dc9210df8b | -7.75104 | -47.01712 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8e0eeed-4280-3f96-bd52-9915c0dbcaa7 | -11.26028 | -48.38257 | 2025-09-28 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README70.md)
