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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cbf0283-8393-39bb-818a-57c075c186a0 | -7.79882 | -46.48611 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66b7447c-4de1-3226-941d-38af309d469c | -6.12983 | -41.83676 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2a8a830a-1ff2-3881-bf93-ca1f386c52a0 | -8.19057 | -46.9477 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e0a0c13-8b0e-39fd-a9bf-c6951c1066c1 | -8.5465 | -45.69284 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b5838b8-f59b-3bd5-ba67-c11f8f2ef0f5 | -2.8111 | -49.14993 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 978c91fe-9219-36b5-9599-ec3b19faa3d3 | -1.50612 | -53.15871 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8f9464f-4be6-3351-b21e-08e433f4a573 | -7.0336 | -47.37017 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b7aa546-a2c8-3efb-9dbf-c1c4ebe428de | -6.59951 | -46.27795 | 2025-10-29 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d66ad84-e928-3de4-b9c5-b9cee20634f4 | -7.07076 | -44.9534 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9cf86fbd-d1bb-33bd-8046-ce35feea545e | -3.37895 | -49.96619 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf9c2395-0085-3e60-9681-6eb14c9ec1fa | -3.04271 | -50.2686 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2045821-7cc0-3328-9743-88ab8f6ee601 | -5.5971 | -45.35817 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bb250dc-8149-39f3-b671-dd158e55d47b | -5.82389 | -53.45218 | 2025-10-29 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2555bc41-efd2-3b57-a958-693d418078bd | -7.79958 | -46.481 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4b77623-a07d-32cd-89f9-c15f305e456b | -2.93409 | -54.167 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c1e07f-6b69-38fc-851b-8e4f7b7825f5 | -3.32377 | -54.08368 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dfcb481-6057-35b5-bf43-d2b49be17a44 | -7.80407 | -46.45079 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1aea13a1-5da0-359c-94f2-0dc67a9172a4 | -6.09012 | -41.78239 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a42684cb-50d6-34a3-a3ee-3a9c7299e966 | -3.5702 | -43.27976 | 2025-10-29 04:44:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89f32092-b3f8-346e-9965-02e08f66a496 | -7.87273 | -48.41603 | 2025-10-29 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| be8a2123-a6c5-312b-9aa5-354e646967f9 | -2.34282 | -51.93554 | 2025-10-29 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b8ec4cd-2547-3f4d-9321-c0b497641db9 | -2.63279 | -47.95949 | 2025-10-29 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dcd4db9-5c95-39d6-b379-cdbcd21e0434 | -7.30702 | -46.31993 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2d5cece-3791-3b68-b7c7-070cb24a9947 | -6.23298 | -42.53494 | 2025-10-29 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6522010-cb22-3003-a6db-ab562994c13f | -7.16142 | -47.34111 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcc5c71d-671d-39bb-8c04-33db62cd2b1b | -3.14854 | -50.45777 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c1531f6-89fa-3094-84eb-7071b5bef0ee | -4.08311 | -46.94296 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71e2678b-2014-322e-9a3e-9a2f3cff0b6d | -6.29567 | -41.88103 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d46b1232-5ca9-3253-a676-b643e07d5b27 | -4.70549 | -46.1042 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bcf610c-0415-3520-9b34-7639a6538505 | -2.42659 | -49.30428 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 078fcd65-bb53-3f92-92f6-38707493ae25 | -4.2298 | -48.37084 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d37cdb3-7ba0-3734-951b-2333a294ed17 | -4.21071 | -50.07899 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| fd0b9dfa-c2e0-323f-9237-6ec9510dc2f7 | -4.21238 | -50.08984 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7e6fb50-3d0d-312e-a22a-ba833e09817b | 0.44942 | -60.48687 | 2025-10-29 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96ba7421-d0ff-35f5-a4b7-d22eb87a917b | -7.79937 | -46.45519 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be5d6a61-f3f7-3279-98a9-ae06413c2919 | -3.42365 | -50.11411 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0461703-d01a-390b-a6b7-f039ba21ff22 | -4.15781 | -51.08046 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd7d628c-2707-3098-b3ce-9171e162b9af | -5.23839 | -45.13431 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55dfbfd4-e7ad-344a-8306-b5ae069e2f55 | -2.85492 | -48.24357 | 2025-10-29 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 753da148-a543-30a4-bf5e-4db4777330a3 | -2.93622 | -51.06983 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d225b21-2135-3283-b135-762b6c76a2f8 | -7.92444 | -49.73951 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8902faf4-a13a-3451-9de3-a8d29df654cd | -3.71939 | -41.57232 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d27a302a-7a0b-3712-b64a-db3150ed201e | -8.18507 | -44.45219 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01343dda-7d50-3c02-82d7-4b762f945111 | -5.75316 | -45.84695 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a829cdbe-a2c4-35b3-9577-286965938c32 | -8.29106 | -49.31128 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa411b9f-9a4a-3a63-9f29-99790f418470 | -3.74945 | -51.75221 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10cfe8ee-9789-370a-84bc-ee5305d4e97e | -2.93452 | -54.16551 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a95d2a59-2364-30e3-9ca7-1c3cb970fa17 | -2.63565 | -47.96378 | 2025-10-29 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b485142a-55c8-381e-aab5-8b6042985aa4 | -6.54322 | -46.76285 | 2025-10-29 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e80d824-72ad-3e8a-aa17-39bb20ef50ef | -7.12383 | -47.01678 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1d5ac7b-d919-3b5b-813f-ad87ea3d451a | -2.9338 | -54.17012 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fcc03ae-6f5b-33bf-9603-f63c1e8335e2 | -5.43293 | -46.12123 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dae24bd2-ec7b-3b3c-8a35-140f20aaea9b | -7.80315 | -46.42964 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fd87cf4c-9557-3c97-aa9f-d8b3376c00d4 | -4.21347 | -50.08295 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7183c7d5-09b2-393f-8571-a6cf9ed26054 | -8.18783 | -46.94936 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aadc8dbf-1e39-3d76-85dd-4db240200f21 | -4.36784 | -48.67889 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce809d42-c08b-3ffc-8d89-70eab1f94af9 | -2.51443 | -51.93579 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14e55d01-f489-398d-9f98-791fdf3da8ef | -2.53736 | -47.80635 | 2025-10-29 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e0ad10-12c2-32e1-8ab8-e465e80c7cf9 | -8.19238 | -46.94521 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d93797c-536d-3568-9970-02015dc4d8ea | -4.07756 | -42.92467 | 2025-10-29 04:44:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16ef3908-2c3c-363f-923c-e412728a71f9 | -6.3005 | -41.88508 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c622a153-0f6f-3865-ba49-896a0b100731 | -3.54118 | -53.3166 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb4f5920-04aa-3d36-823d-4f03a6b475c3 | -7.79616 | -46.44948 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d7b4f1b-29d3-3a07-800f-02526634d08e | -8.20745 | -47.29628 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da827b26-f50d-3169-bf8f-5d8805325197 | -8.50079 | -45.58935 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de364b5e-0bd6-340e-a58d-3e304f68a8ed | -5.41207 | -45.2202 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6372377-d68a-3eea-908d-03370ccd53b2 | -7.32634 | -44.74357 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84d08e7d-1522-3b79-a9f0-9fa8ffaa9ef6 | -7.74142 | -44.72518 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21e71063-c919-361b-9a66-1b03f985103c | -6.109 | -42.43457 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9d91c05-e9b7-39fd-bd39-243a7a40f414 | -3.261 | -49.11895 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dfe7202-f352-34d9-93d4-09af80b5b587 | -6.49174 | -42.24037 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 165efe7d-aa2a-31ba-9553-8a9b34034073 | -6.13802 | -41.71408 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6d068dc8-9cff-3078-ab15-a1e0d51a0dbb | -8.69545 | -47.13667 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6da7d622-4741-38ad-ae90-4202c7ad1041 | -3.52323 | -53.0701 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49cf69e1-edc5-3bc2-89b7-5aeaa262091d | -6.09912 | -42.46717 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 36ff8926-b289-34a7-a008-f91f4a29e551 | -8.1917 | -46.9499 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54537617-1cdb-352e-8513-b92210f1653f | -8.71258 | -47.98984 | 2025-10-29 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 466c4eb0-f05d-3406-a118-286242a7bf75 | -3.04655 | -50.26569 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e1cb027-354b-3526-8698-548b5308c4d9 | -3.75111 | -51.75227 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f59581f-8fcd-3fc0-b37b-06bec98776f1 | -8.54596 | -45.69664 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f0ba5fa-9805-3fa3-8753-8d2c4903c740 | -7.3061 | -45.67788 | 2025-10-29 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e837d6-8c36-34b1-93cf-353853e9175f | -8.30933 | -47.57005 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5779010-37b9-31c6-88cf-eb31c9301bcd | -4.21016 | -50.08244 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 06029e51-9f11-3c47-b39f-26abf41e539e | -7.90007 | -45.68491 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5aed1b02-ae2b-3eb6-ac65-7b7dfbbf321f | -3.86806 | -43.35632 | 2025-10-29 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d1acca4b-f72d-3291-8be8-09ea5839ed4f | -5.19068 | -45.62491 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcdecd82-98a9-3ff3-bebe-6b0d17b31086 | -7.31025 | -45.67838 | 2025-10-29 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 229ee78a-d08a-3c95-adec-c62bef991b96 | -7.18431 | -46.73965 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcbac6d3-25e4-3a54-ad0e-f41f3435bd59 | -4.33085 | -48.62122 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0961e9f5-1ca9-3c45-ba83-0413d336f3d5 | -5.94454 | -49.10756 | 2025-10-29 04:44:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2b6fa4d-a1a8-3814-ba8c-51914c65656e | -8.18963 | -44.45287 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c26a2b16-6a7d-352f-a169-41f49549143d | -4.33118 | -48.09506 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 425d56d6-d037-3d0b-8baf-7b7ca4b3fc01 | -2.60007 | -51.94928 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb1c7960-a2c0-3b3a-a870-d84133c60cfb | -7.79713 | -46.47031 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb16d08-c69c-3c80-8ef4-6a9f8c492300 | -7.61217 | -43.59705 | 2025-10-29 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d30aebf-b63a-396a-8910-9f25e2ef718f | -8.24125 | -46.90821 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd7d6618-aff8-35cc-837d-0545a0e340bb | -4.25304 | -48.58265 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c6300d1-1808-38d0-841e-49ee6d545b22 | -2.80961 | -48.66415 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b81cee3-aebc-3c00-b740-289dc2d6721a | -6.14443 | -41.69156 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 814f1e0a-8143-3743-8501-3804a7683e28 | -5.60963 | -45.19084 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README62.md)
