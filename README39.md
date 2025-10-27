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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31189378-e0f3-3948-8803-8babebe990f0 | -4.77192 | -48.67122 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ecfb6e9-5c10-3721-9bdd-69c7402f60a7 | -3.57819 | -49.02194 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a0f59b7-26dc-3645-95cf-90f51ba738cc | -9.12937 | -51.30258 | 2025-10-27 04:32:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1c1d050-489b-3377-9a4a-6828e743cad1 | -9.58512 | -44.94734 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32f12cec-3666-33bb-9410-64b85eeb6ada | -10.02519 | -47.14315 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e3578a9-b795-379c-b4d8-18e0441ec494 | -8.27348 | -46.88169 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4a34fe4-2bed-370f-a8b6-66cc49cd7f66 | -5.81659 | -40.81405 | 2025-10-27 04:32:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4a4908f-9ac0-3323-ac3f-f4ca58df7857 | -8.15229 | -47.0309 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecbdaf00-afa6-3a00-bc3d-3a643e212a15 | -3.76807 | -44.23254 | 2025-10-27 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d072766e-a4c3-3d93-b18e-2a580e0199ef | -8.31931 | -46.18251 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dc44bac-83c8-3199-94ec-1563d5b2156b | -5.64097 | -47.62587 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e023e656-f456-3c72-87a7-938ab0b8adf0 | -4.86566 | -43.2542 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f773e4a8-5737-31dc-aaec-0c9f4bb881d5 | -7.53792 | -46.24746 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 246e598f-6dfd-3514-bc70-2f0812361036 | -5.53597 | -41.39602 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5121eca-39f0-301b-b503-572446fcd5f8 | -6.88737 | -45.15638 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b114b33-763f-348b-9d76-bc58bc9ad88f | -6.14563 | -41.81494 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cf969b65-6041-3c86-9fb0-747120ce774b | -7.83698 | -46.49445 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 42b7316f-aa77-36bd-bcf1-030897cab302 | -3.55875 | -49.49652 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9db8c7ee-bcc6-36a9-a5ef-fce51961dc8e | -3.98486 | -49.29036 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed34d2f7-dc0f-304a-8b3e-2da7a2280ca7 | -5.6534 | -41.10873 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c0c39d6b-4c0b-3ad6-8143-68e579634394 | -3.11103 | -51.20772 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bb00ac2-a42d-31cd-a3a1-5ec954cbf47b | -4.85464 | -46.7366 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a051c8f-a9e9-3b8b-a3d8-e97c7bb29d7d | -7.06706 | -47.36391 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8c7b6c1-cd03-3c19-9cd9-d76e2090553f | -4.81258 | -38.64554 | 2025-10-27 04:32:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0e26fce9-8a09-3124-9e67-f7e0c711722b | -6.20934 | -41.52806 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ea76f55-2b9c-34af-9a7b-46bf56063da5 | -4.22236 | -48.35991 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e259b3-8ba1-3606-b33b-59d7b2266cb1 | -9.30084 | -45.23132 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d13ac04-1b36-397f-af02-f74cb32fa09b | -8.12488 | -47.03423 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d3566f5-7c02-3c62-9e32-a29b0fba8445 | -4.36897 | -47.2524 | 2025-10-27 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88cd152a-9c3d-3aae-b475-0ef32c99e373 | -7.76696 | -45.40235 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64c9c6bc-a5c8-3ee1-b3d8-01b280cc0d9f | -7.84539 | -46.48462 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26cc86d3-2e98-3305-9be4-b6f8eb029dc1 | -8.09716 | -47.05893 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 713c0499-701e-31f1-86ce-2edfc9b32aca | -8.3318 | -46.16941 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8414a87-deba-3aad-8f9a-ddd26b950c59 | -4.18795 | -46.23276 | 2025-10-27 04:32:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23a4f07-702e-332e-a6cf-e0cdfec828df | -3.77958 | -51.81458 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3405fea-8566-3f5b-9085-4ce94e8f2bbf | -7.80563 | -45.3843 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac0384fb-f5a2-3f0d-83b7-4a46bdc5ccbb | -4.21958 | -48.35588 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9538ac0b-d088-3d9a-aeb3-686dedd35aaf | -9.24559 | -45.60855 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8da3a14-aa4c-3e95-a447-d5015117606c | -6.87914 | -45.16316 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee04dfe0-d195-36b5-ad1a-10617d8e8d9e | -6.92865 | -50.72928 | 2025-10-27 04:32:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778cc692-2cf2-395b-8e09-f6414d0b2f87 | -7.81384 | -45.40138 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 07e52833-c98a-3306-9834-e77c8e67329f | -8.07402 | -46.94269 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01a0c793-1bfb-346b-80a0-780314ca4bae | -3.85749 | -52.17374 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63d772b8-05b9-36a8-b902-cbc0a9fa12c2 | -7.9408 | -49.65047 | 2025-10-27 04:32:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 049a1da1-d1fa-3db0-a26d-0e22538d7569 | -6.88033 | -45.15531 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 525ce6c4-6805-3140-bd0a-6e740dc99b5e | -10.29818 | -44.11415 | 2025-10-27 04:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b4ea264-2c26-30a0-84c5-ffba81089839 | -9.62712 | -40.34772 | 2025-10-27 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f4d1b063-7d3c-34e5-80c1-de99b92abe91 | -7.76461 | -45.39404 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3da7aac9-d3c4-3400-bd70-8bc2e3d39cd0 | -8.53136 | -47.19853 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9848064-e9d1-3372-b6d5-3b29e8161986 | -4.44908 | -43.41691 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c3b3d7c-79e9-3467-8027-7d027a50942d | -8.23378 | -46.92347 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65b0094c-7f4a-3ccf-bede-d224f2a8e79c | -7.35506 | -42.45297 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 03b56441-d591-39bc-9ef7-28909eceb1e2 | -4.48665 | -43.42947 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bd23244-7235-3764-ac5e-e401835f05ae | -3.52184 | -52.2063 | 2025-10-27 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 524353f4-8584-3a3c-8be6-61d9b860a5db | -10.02464 | -47.14677 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bd01b6f-9d85-31fc-a8b9-7062109e3097 | -7.93329 | -47.19548 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 342aeff8-9daf-393c-80ea-e40661b83e1b | -2.79742 | -54.85881 | 2025-10-27 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81c1d930-3584-3266-b735-a1b37ffef588 | -3.24683 | -50.65185 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 230e236e-80e4-39e6-869f-cbf2c058f6a7 | -4.00087 | -48.31831 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74db7dcb-a1b0-3d68-adcb-3e6233824853 | -6.58012 | -48.77428 | 2025-10-27 04:32:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aebb1b9-2af9-3b5a-a3f2-9b6e5b7c4646 | -7.99299 | -46.20633 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff786ac5-b5da-36e2-804c-e60679933ba6 | -7.83188 | -46.48258 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 34541b63-8515-3e3c-a822-5467faab7e54 | -2.32263 | -48.58366 | 2025-10-27 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f852b5b-5c07-3acf-8288-eba515ea3168 | -7.10844 | -47.94733 | 2025-10-27 04:32:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffc2995d-5fce-3431-9e8c-ff418a2580a7 | -3.10461 | -50.18265 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41cb4914-687b-345d-90c1-ac337eb15860 | -10.02238 | -47.139 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c625a1ef-419f-3617-aad8-1d447722cf0b | -3.57486 | -49.01791 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 542d9c14-2aab-3d6a-8d62-b59c441d135e | -5.25703 | -42.48508 | 2025-10-27 04:32:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4222f080-3f75-37a8-9c50-690d1a8ec692 | -3.40993 | -52.7233 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc854cd6-a96e-3762-a493-eab3aa969887 | -5.72224 | -49.28276 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95384c8b-5325-321b-bc09-62e4147131bd | -7.76222 | -46.51994 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5008742e-b946-3e8e-b70b-4bfd4777050c | -6.16533 | -43.10545 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5c4279b6-93e9-34b6-b547-3f88a4e23d92 | -7.59421 | -45.68793 | 2025-10-27 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1885a530-f2af-39c8-83e5-d7228b65d1fc | -9.26504 | -45.59922 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d55c9bc-2a52-3ed9-9f93-c9aacdeb7566 | -6.11212 | -41.745 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 283755ad-dd53-318b-a8f3-e454e53b3dce | -5.67573 | -47.01371 | 2025-10-27 04:32:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 942cf5b0-de70-384f-b953-0fe3fe29baa4 | -4.80344 | -43.30663 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da7da499-629b-3250-8cfb-4db9d437f87b | -6.82833 | -41.20348 | 2025-10-27 04:32:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40174e08-a1bf-3eb4-a2af-7211eeb0aee6 | -3.81313 | -51.78133 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f751a52-eaa7-371e-8dec-033c68eb785e | -6.0991 | -41.77531 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 804cd1aa-47ef-3753-a4ca-b0249961e03b | -4.45639 | -45.44927 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f7d489c-f51f-3951-a874-9031ae197b3c | -9.95976 | -47.06287 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fdf877a-43d5-314c-bd5b-57a66282b434 | -8.31134 | -46.18891 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2ed2cdf-a186-34d4-980b-7de5bd75708f | -9.14597 | -45.83776 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93582df3-5434-3d8f-9908-9cce3f971c4b | -3.46829 | -49.97316 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7cdc9d51-48e3-3b24-acd3-473bae42bfc3 | -7.97781 | -45.46891 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a61100ce-887b-30ee-9a88-8c5748451160 | -4.09886 | -51.05006 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18db1c3f-ca16-31ce-8076-a2fd4ce90930 | -7.83919 | -46.47997 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26e3c72c-ebfd-3041-94bb-628fbb1ef4ad | -8.82406 | -49.98666 | 2025-10-27 04:32:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c511791f-d70c-3d8f-a826-6f9d32125fd2 | -8.31246 | -46.1815 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91dbb851-7f20-3013-85d4-f39a231c90d6 | -8.22047 | -46.94318 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 041ba527-9b18-3af3-8384-26d25c4c1dad | -2.90644 | -53.13467 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30ecb9b4-09b8-3b14-b5b2-6a7d07aeb642 | -9.56415 | -46.80499 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58259a8e-b836-3d4c-a290-397376fb31dd | -6.55135 | -41.59906 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 407225b4-de53-3429-9db4-78923f7ae7c8 | -6.25888 | -41.83867 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2ee2ac94-1cb9-3b41-b372-d749efe3b160 | -7.10568 | -47.94337 | 2025-10-27 04:32:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f1c6cc1-2026-3ccb-804d-5aa0dad7ed8c | -6.12745 | -42.45294 | 2025-10-27 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac927d7a-5b09-3e3a-a520-27f8991ed16e | -7.94672 | -47.24068 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39fa7283-80aa-3fa7-8b0a-3f3ebad13b8a | -2.94704 | -51.75896 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deae776a-131a-3179-80a2-925d20c95f0b | -4.23379 | -50.13359 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)
