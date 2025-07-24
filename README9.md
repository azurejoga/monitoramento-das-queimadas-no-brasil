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
| 35d31b0d-985a-3c46-b7b2-00478fd4d533 | -6.74391 | -48.08038 | 2025-07-24 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72c60e63-76ed-37eb-9b6d-016859ae67a8 | -3.58305 | -47.52678 | 2025-07-24 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31983e5a-8661-35c0-a5ab-bb89dfe62d99 | -5.47911 | -42.14804 | 2025-07-24 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ada62ef8-0d5f-3232-ae1f-c520f5d974b2 | -3.17167 | -49.45885 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| c1af3fc3-0689-3747-a03e-09442fadf23d | -7.25066 | -43.06736 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 996b8b81-2f72-3cd2-b358-5797ea7f2ba6 | -7.26335 | -43.07289 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 4d859494-1b74-310a-85d4-2d45571e2596 | -7.46103 | -49.40109 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dea00fb9-7c49-3110-90c3-cf38f0985556 | -6.14141 | -42.96305 | 2025-07-24 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3834e929-dbf7-3b6c-9e09-3b1f238cca41 | -6.97086 | -44.37212 | 2025-07-24 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b915a58-2aa5-3c1b-8d9a-f77f0c461d3a | -6.87625 | -43.11468 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d39d475d-8191-315a-8813-c98c5f963505 | -8.5184 | -44.67756 | 2025-07-24 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65af1c72-9b2e-3ac0-b600-9d8528d54f35 | -8.09431 | -50.08273 | 2025-07-24 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 742f8bce-802a-3ba2-8ed6-a5e760e9fd31 | -7.66347 | -44.48999 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7172c902-345c-39db-9a8d-34108bcd5dba | -7.17155 | -44.37496 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c78ff52-c6cf-3d3c-9431-57f34e237ce6 | -4.05822 | -42.51552 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 81deec26-6eae-352f-88fa-609c3a136cce | -4.05875 | -42.51207 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 3d00c5f6-b5ec-3352-9bf4-b5348348f371 | -6.58899 | -41.7877 | 2025-07-24 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ca91de1-489f-3520-90fb-1fc10dccc58d | -6.89104 | -44.21131 | 2025-07-24 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f86e89a-8c62-37b2-81f5-3c2305b3d36b | -3.17624 | -49.45963 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2a1c9073-cffd-371d-bdf8-72ec95bf983d | -3.35627 | -47.16191 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 175fa08e-1bf9-3838-afb8-24cbf83d86fa | -9.20459 | -41.02604 | 2025-07-24 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| adb00955-8c7f-35ab-bc93-6d61cfb8f3b9 | -6.38459 | -43.30208 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0460fded-d1db-3f4c-8013-5b7a040febea | -3.05143 | -47.37984 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30f20947-eb9d-3088-b18b-c8e1c24484b7 | -7.25566 | -43.0788 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41ace396-41d4-3ad3-a70d-e3791398a817 | -3.04247 | -49.4439 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca4817a1-c60a-3150-8f92-d7ed4b4de044 | -6.71072 | -44.40621 | 2025-07-24 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f98b9524-77bd-324f-bd24-a2693f9bce65 | -5.74281 | -41.01743 | 2025-07-24 04:14:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fcd6d471-8e22-3371-aa70-f43b5191e3a1 | -8.30454 | -44.97122 | 2025-07-24 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 863ba761-b154-3d8c-855b-bd9bc0dd1687 | -6.26084 | -45.27203 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3478335b-d901-31ce-9abd-36ec528a2069 | -3.10896 | -47.49303 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54ef0a7c-89aa-3104-ab1d-dae3e52e4a90 | -8.92579 | -47.34288 | 2025-07-24 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b892b76-6f40-30dc-8296-0b26ba1cec33 | -3.93771 | -41.49527 | 2025-07-24 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6961c85b-a088-3c73-b818-7eeb218fd8c3 | -4.05714 | -42.5224 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c5aa7a9e-c8dc-3113-ad18-0a3aea6c9550 | -8.92873 | -47.34784 | 2025-07-24 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c700761-b6d7-3097-b3a3-139a179469f9 | -6.87456 | -43.10378 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb17a6e3-1260-3489-a2cf-7e328c51b86a | -2.58375 | -51.92453 | 2025-07-24 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca8c748e-3b0c-3df2-878f-13228b902fc9 | -7.84148 | -44.50379 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc756b27-436f-367d-89c5-be32a337c09a | -6.8196 | -43.99621 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d86bb006-635b-34b7-8ae2-bbe540fe5478 | -6.57723 | -41.5024 | 2025-07-24 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e2bab448-7a50-395c-b9dd-d469d2359bd8 | -3.49781 | -43.31359 | 2025-07-24 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 107b0b7d-cd7b-3be4-8e59-83888e29a007 | -9.26625 | -48.55732 | 2025-07-24 04:14:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6e2698b-6093-3db2-a961-b3d4d2e18b67 | -4.5171 | -42.08083 | 2025-07-24 04:14:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b710d1a8-b584-369b-8b7a-8aba9f88f967 | -6.13864 | -42.95909 | 2025-07-24 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae68cc3b-7d33-39b6-9d36-48e3ae28ea32 | -9.58867 | -46.32209 | 2025-07-24 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37038d53-e7da-3f1b-bbb2-2e1bcc669b67 | -6.57551 | -41.49081 | 2025-07-24 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe66e47d-662a-3615-bfde-3a8e6157dedd | -6.91095 | -42.80403 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e1301629-2a8b-3715-b31a-dadfe0726731 | -6.57837 | -49.5051 | 2025-07-24 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1eb233b-2a37-3ad1-8598-f15ffcb91cf2 | -4.57297 | -48.01666 | 2025-07-24 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94dd83f8-e6f7-33a7-aa3c-9748a9ff5a07 | -7.05432 | -45.85667 | 2025-07-24 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff2274f6-bdad-32da-92c7-75cd095da20e | -7.26281 | -43.07636 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| df693db4-a5ea-3a23-997e-980a0c3d6fa9 | -7.25896 | -43.07932 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7ee5701c-44ec-3d5f-bde0-ced346db8f5f | -3.04745 | -47.37918 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 888c19ea-b2ac-3928-8e2a-db2ab5eebded | -4.05545 | -42.51156 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 1b10ebfc-7163-3341-ad69-d5c102d627bb | -7.46172 | -49.39712 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f4557cf2-ada3-3f3a-90d9-5865668ad352 | -3.04234 | -47.38554 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 854b2518-2ff8-3feb-a9fa-b0d64fa6f079 | -4.81039 | -43.20902 | 2025-07-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc4baa07-aec0-39f3-9201-7e141389691b | -8.03902 | -47.64902 | 2025-07-24 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07aff663-a7b7-3614-afc5-6897df617d91 | -8.03826 | -47.65366 | 2025-07-24 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85945e74-36c5-3fbc-9c53-f0c9e0f8cd4e | -6.26486 | -45.26887 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11b2448a-9f25-3a46-8325-6331a6a5f128 | -4.05438 | -42.51845 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 938f7577-5d60-37c0-b76d-b38cb4a3e5cc | -6.87564 | -43.09686 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa5c6fba-2591-39d2-a42b-3cd074c87946 | -4.05 | -42.52481 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b23f1ae-5fa3-35af-adaf-ffbe24ab498f | -6.93824 | -50.31746 | 2025-07-24 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5678a2b-b265-3a28-a44f-8b0fb2650fb6 | -5.47857 | -42.15155 | 2025-07-24 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07d4cad3-7f46-3194-90f1-5dcd56e86018 | -7.55077 | -44.49315 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5315f763-70f0-3f4a-85a6-2d5414649320 | -8.47765 | -49.55737 | 2025-07-24 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13456f70-64eb-3bc3-ae62-58703b558b72 | -6.60624 | -42.42326 | 2025-07-24 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 456a2788-f6d2-326a-b4c8-f332796d0baa | -3.56989 | -49.5005 | 2025-07-24 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcc27544-3d92-38a1-b25e-e9ffda102e09 | -8.83547 | -44.5229 | 2025-07-24 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6baf30b4-1f80-377a-b92a-d5fa0091e448 | -5.83339 | -44.10084 | 2025-07-24 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 062509d5-d4f1-3a80-928e-c97f9061f614 | -7.54578 | -44.48153 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90b02e90-ebf4-3141-a510-3085dc4dab62 | -7.01807 | -43.44854 | 2025-07-24 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e86dc29d-0d73-3ed4-865f-855505905305 | -7.13659 | -44.10028 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52d5219d-e94f-35aa-8a16-02b383d6b4f2 | -5.73123 | -44.51344 | 2025-07-24 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccb77e5c-db15-3cb7-9e61-7bfb0a086239 | -5.97982 | -45.35919 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 678501fe-24df-301a-8ad9-033bb1d421ee | -4.64813 | -37.79963 | 2025-07-24 04:14:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 370e428c-60c3-32d7-9232-990c31dcaf4f | -4.80708 | -43.20851 | 2025-07-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb32f0df-1baf-3733-85ae-e8dba5150e80 | -6.8916 | -44.2078 | 2025-07-24 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 154f11b5-8e06-3d90-83ab-19edf4f68a1b | -6.81905 | -43.99969 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be169628-4923-3c8f-a66b-196239dc4e38 | -5.67731 | -43.66816 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9d87b31-d402-3161-9851-8d423a7c92e4 | -5.89032 | -45.19503 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4af5727e-25ac-3606-8649-215eab04c96e | -4.78278 | -45.33488 | 2025-07-24 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1ea5bc36-7eb6-342b-9fe6-da35ea8fe209 | -3.35626 | -47.15973 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89e4b497-9002-31f3-a309-602755d1f782 | -7.24242 | -43.07673 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 646843dd-11cc-3610-aa18-6e97e29c1637 | -7.14533 | -43.80595 | 2025-07-24 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30ab5f28-895c-3da8-84f7-f6740be69412 | -4.10776 | -48.20531 | 2025-07-24 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1c2d378-32d2-3adf-8404-b951798dcf82 | -6.89382 | -44.15087 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4fde3a38-4772-33e0-a4d8-3dbe8c304ba6 | -4.88533 | -44.95802 | 2025-07-24 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae011f66-6a8c-30fd-aca2-c7bab4d4d1a7 | -7.45609 | -49.40441 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16d27785-33fc-384b-8ee8-4f14828b2ff6 | -3.93551 | -43.16962 | 2025-07-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e0d2520-73c2-3398-9b8a-876cfcd230ef | -7.30906 | -49.57523 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f25e740e-66de-3cab-ac32-209b6376f6b0 | -2.62052 | -46.85445 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a00a0fbe-ed17-314d-878b-3898b07f63a8 | -7.84425 | -44.50784 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2c14b93-a2b0-342e-b43c-180dabe83bb4 | -9.58804 | -46.32592 | 2025-07-24 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19c65b25-697b-3166-9731-1abd149ff66f | -3.22749 | -46.78972 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 396931fa-52b9-3910-8963-d5024740ded1 | -7.46529 | -49.40178 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2cd7ae92-2866-3ed7-8d6d-f7dc2b5cdcd3 | -4.30359 | -48.10399 | 2025-07-24 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fba4fb7d-4fd7-396a-90f7-91278cbc1c41 | -4.68295 | -43.24143 | 2025-07-24 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ffb0ea6-fc4c-37b9-84aa-71bdc34b4baa | -7.84092 | -44.50732 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2a8d8e2-ed69-3f6b-9d55-a32ea5d44fad | -8.12489 | -43.54669 | 2025-07-24 04:14:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README10.md)
