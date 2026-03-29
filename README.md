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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e69ee14d-0d13-35af-979f-3b7125405e69 | -12.3388 | -48.189499 | 2026-03-29 00:10:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffdf3e49-b9dd-301f-9a97-a40928665ad0 | -21.1772 | -48.5331 | 2026-03-29 00:10:00 | METOP-B | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54b5ad8f-edc8-3f95-bff3-67ebcca016a8 | -12.3404 | -48.196602 | 2026-03-29 00:10:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 644effcf-f77c-3e6f-a4b5-a04edcdc9d86 | -15.0763 | -43.865002 | 2026-03-29 00:10:00 | METOP-B | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc3d0861-27b5-3a15-843d-0c9b8e49462b | -15.0783 | -43.873199 | 2026-03-29 00:10:00 | METOP-B | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3523e8d-fa5d-3df7-a96c-f5653e7c0050 | -21.175501 | -48.524399 | 2026-03-29 00:10:00 | METOP-B | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42ba7034-d23c-3c5c-9e12-1eb3bf7dacca | -23.221701 | -49.966 | 2026-03-29 00:10:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f92ca744-609d-31ed-a491-eb17b91dd5cc | -23.2237 | -49.977001 | 2026-03-29 00:10:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7af4cd0e-920b-3aa6-957d-c324f0540df1 | -23.22291 | -49.99535 | 2026-03-29 00:18:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 2d81d1b1-47da-3d94-ad2c-009a4697c975 | -23.22433 | -50.00766 | 2026-03-29 00:18:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 41.1 |
| c7587ec3-6818-33f8-9bfa-a0a69363a804 | -12.79344 | -45.85819 | 2026-03-29 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf0b2912-36e9-38c6-ad3b-83b283846396 | -15.08906 | -43.89882 | 2026-03-29 00:20:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f277f1b8-f1e3-3e14-9309-a2ec80440823 | -15.08561 | -43.89093 | 2026-03-29 00:20:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e39926b3-851a-348c-86ec-226f89b04887 | -12.34196 | -48.21649 | 2026-03-29 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 895204f0-6b3b-3a06-886a-ee2b77b0d3d6 | -21.22461 | -49.44711 | 2026-03-29 00:20:00 | TERRA_M-M | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 872ac0e6-16cc-3ec0-a0a0-becb382d263c | -10.93678 | -49.43095 | 2026-03-29 00:20:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53d4a0ee-ee62-348f-ad51-106661ba876c | -21.17699 | -48.55534 | 2026-03-29 00:20:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| dbdef419-f4fb-3c79-8d71-a1f4153852ef | -23.2257 | -49.9992 | 2026-03-29 00:30:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 136.0 |
| 2c2aa4dd-6114-3edc-a858-e044c2a6dc21 | -23.2251 | -49.9935 | 2026-03-29 00:44:00 | METOP-C | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| abab75de-02f5-32d7-be0d-863d56508a54 | -12.3416 | -48.210098 | 2026-03-29 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae70d73-3f3b-370c-80d2-a1f4c52b020b | -21.178301 | -48.553902 | 2026-03-29 00:44:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 281a204f-4d94-3597-a778-e6aeb8824126 | -23.215401 | -49.995602 | 2026-03-29 00:44:00 | METOP-C | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 59a0f4cf-8c66-3755-a121-6e59e37b67b8 | -10.74578 | -36.92546 | 2026-03-29 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f544435a-b85d-3289-a4e1-d673c59a387d | -15.08174 | -43.88643 | 2026-03-29 03:25:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f43c241-4e69-3b56-9a27-e74683b4f3ce | -15.08674 | -43.8924 | 2026-03-29 03:25:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21648810-83ed-38d4-b582-fb86da3472a4 | -15.08772 | -43.88776 | 2026-03-29 03:25:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a3f38b4-dada-35fe-9f96-8aae1126571c | -15.08577 | -43.89702 | 2026-03-29 03:25:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2ab7560-c34c-3808-9061-97525c1718c3 | -22.94654 | -43.71315 | 2026-03-29 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b7024d99-db51-3fc8-be24-88412670db5f | -22.91014 | -42.9467 | 2026-03-29 03:28:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f748aa93-be5e-3a51-a0b2-22ce4fcd5e9c | -22.94582 | -43.7164 | 2026-03-29 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19353221-fd86-321b-b48c-3acc211d5973 | -29.9352 | -51.08733 | 2026-03-29 03:32:00 | NOAA-21 | CACHOEIRINHA | RIO GRANDE DO SUL | Brasil | 4303103 | 43 | 33 | nan | nan | nan | Pampa | 4.4 |
| 3c576464-d535-3f8d-bb63-c065c51e87b5 | -10.74492 | -36.92556 | 2026-03-29 03:55:00 | NPP-375D | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 24c2f975-c170-3535-b309-b76e31dbb3df | -12.43882 | -44.75171 | 2026-03-29 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a032f5e6-34a2-344f-b230-6110f06b90c1 | -15.0846 | -43.89036 | 2026-03-29 03:57:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebd5735d-a72a-3417-9328-befc8b9b4c70 | -17.87143 | -45.54789 | 2026-03-29 03:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0d75067-a8bd-33fe-b238-f372da21f99c | -19.22833 | -44.7534 | 2026-03-29 03:57:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a958c20-fb35-3e55-8f2d-e985ef48ef26 | -15.08394 | -43.89397 | 2026-03-29 03:57:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 796c9ac3-3c62-3b06-b03d-1f293d954f17 | -18.1749 | -44.97704 | 2026-03-29 03:57:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d954031-698e-35ed-833f-6a682ca7b770 | -15.08525 | -43.88676 | 2026-03-29 03:57:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3b48796-21c5-3385-9bee-2add005045aa | -19.59932 | -40.07524 | 2026-03-29 03:57:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8d31d59-aa8c-397d-bb17-2c85e9e98449 | -21.17366 | -48.56046 | 2026-03-29 04:00:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 30958b60-05b9-3489-ab11-f473f069617b | -20.05516 | -51.10975 | 2026-03-29 04:00:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3825be1-1b97-3b26-bb8b-54749d122552 | -23.54155 | -46.62267 | 2026-03-29 04:00:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e24cce2a-ee44-340d-a04b-9647f7e2dfde | -23.19665 | -46.89637 | 2026-03-29 04:00:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 73ea630f-e619-3f14-8f0c-8797040a7204 | -22.90794 | -42.94776 | 2026-03-29 04:00:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e0058eae-292c-3248-9ce3-867852bfc869 | -22.90933 | -42.94666 | 2026-03-29 04:00:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 339b9fb5-4a6b-3322-adfb-56cf5af42bde | -22.94473 | -43.71408 | 2026-03-29 04:00:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 93e7d941-139d-36d7-89cd-acdf9b821dee | -23.53959 | -46.62075 | 2026-03-29 04:00:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a346deef-4d28-3995-8d31-65d4e0f2e814 | -22.77938 | -43.04203 | 2026-03-29 04:00:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b73ca4a-04aa-35e2-9c7e-07b94d694481 | -20.80591 | -49.81282 | 2026-03-29 04:00:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da2cf363-ed38-38dc-b110-d5e50b116efb | -21.17485 | -48.5547 | 2026-03-29 04:00:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e0d82eee-ecd0-3a85-b99c-3d453ca906fc | -27.27983 | -49.8236 | 2026-03-29 04:02:00 | NPP-375D | TROMBUDO CENTRAL | SANTA CATARINA | Brasil | 4218608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e3506dd6-c7f0-3939-8002-8dee574a965a | -26.89957 | -49.76143 | 2026-03-29 04:02:00 | NPP-375D | JOSÉ BOITEUX | SANTA CATARINA | Brasil | 4209151 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d070787e-8fd9-3e4e-92d2-d631d797e42c | -27.28443 | -49.8248 | 2026-03-29 04:02:00 | NPP-375D | TROMBUDO CENTRAL | SANTA CATARINA | Brasil | 4218608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6656587d-bf46-3e8b-9ff0-73f640afeeac | -15.96072 | -52.20868 | 2026-03-29 04:17:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cbd0038-9c63-3f69-bb69-00be6dcd5048 | -15.08722 | -43.89582 | 2026-03-29 04:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 215de8e7-2c34-3a1a-8861-9dc77dc12508 | -6.6052 | -47.62237 | 2026-03-29 04:17:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b2bba8-1bdf-3378-825e-f5e317231151 | -13.15295 | -53.25753 | 2026-03-29 04:17:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c42b0d8b-028f-3289-bd49-be50d3aa2350 | -13.15238 | -53.26047 | 2026-03-29 04:17:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab94a8a9-c6fa-3665-84d4-ccd88ee420a2 | -15.08554 | -43.88425 | 2026-03-29 04:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e4e65fe-88d4-3472-98cf-f654878dca90 | -15.08442 | -43.89161 | 2026-03-29 04:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d2f2640-2965-3605-94f0-52abf9db46d8 | -13.15351 | -53.25459 | 2026-03-29 04:17:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b21c9855-af46-360d-b5aa-14c3b90d0034 | -15.08386 | -43.89528 | 2026-03-29 04:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 104a5381-59dc-3adb-ae6a-92c74e9212b7 | -15.08498 | -43.88793 | 2026-03-29 04:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a05e58c4-4d35-3907-aa94-a076351d2ef4 | -15.08162 | -43.88739 | 2026-03-29 04:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 045812d5-09a5-3b32-a3ed-359fba52f200 | -19.22717 | -44.75212 | 2026-03-29 04:19:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2be6b37b-9014-3a0b-9306-5e3fff5cf947 | -13.21505 | -43.69052 | 2026-03-29 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42da488b-b9c8-363c-b047-237dd66cd708 | -19.77871 | -49.77129 | 2026-03-29 04:19:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c10e3cc6-9e0a-354f-b38a-d1a0dca71967 | -22.9438 | -43.7142 | 2026-03-29 04:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| e1c65ae6-8d5a-38c6-91b7-1cf6b6f63fea | -23.541 | -46.61814 | 2026-03-29 04:19:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 71b949db-7951-3227-9b2d-6f66fa0d3d5a | -20.05428 | -51.10802 | 2026-03-29 04:19:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d60d753-82a2-36d4-a78e-f302e09b9779 | -21.17418 | -48.55637 | 2026-03-29 04:19:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 68e791bc-edba-3c13-a69a-4db6fd220848 | -19.92218 | -43.97458 | 2026-03-29 04:19:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f481aed6-65eb-3377-bb19-5920780eb665 | -13.54131 | -43.68601 | 2026-03-29 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 798f243b-0b57-33fa-8497-c53f38190215 | -21.22447 | -49.44567 | 2026-03-29 04:19:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 21b4b565-9e4d-3396-b2f7-66eee4e84787 | -17.86983 | -45.54508 | 2026-03-29 04:19:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b56e12dd-9942-3564-a5e2-699895f4abc6 | -22.70103 | -43.36267 | 2026-03-29 04:19:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f5519b02-1332-3ce2-bae7-6d41326f8c11 | -21.61593 | -46.92286 | 2026-03-29 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8dd0d956-8f67-32be-afc2-d40c166a3e1a | -18.17194 | -44.97445 | 2026-03-29 04:19:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c51cce01-9c0e-3f82-bf6e-5b55cbddf1d3 | -22.90538 | -42.94984 | 2026-03-29 04:19:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e322471-50af-335a-918a-dcf7f419080c | -19.92322 | -44.09024 | 2026-03-29 04:19:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27ff1301-6d8e-3401-aca6-10d9259400da | -12.44146 | -44.7537 | 2026-03-29 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c91e9f5-193e-382c-9a2d-d36bb9dc60b0 | -23.54042 | -46.62192 | 2026-03-29 04:19:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5863b2b-5d9d-34ab-9bd3-9227d288e9ff | -22.78145 | -43.0418 | 2026-03-29 04:19:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec80a626-08e2-33be-824a-bb31a562321e | -21.17759 | -48.557 | 2026-03-29 04:19:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b4b89162-e323-3cde-88da-efdee4323ad5 | -13.54465 | -43.68655 | 2026-03-29 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 324bf7a4-bd1b-3064-a2a5-9458b8fc4e1a | -21.12955 | -46.54153 | 2026-03-29 04:19:00 | NOAA-20 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a983398-6a70-31e5-b659-7e2e38f552ae | -26.89655 | -49.75994 | 2026-03-29 04:21:00 | NOAA-20 | JOSÉ BOITEUX | SANTA CATARINA | Brasil | 4209151 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a72812f2-9fbd-3717-ad11-14bfa562d182 | -25.64043 | -53.2005 | 2026-03-29 04:21:00 | NOAA-20 | BOA ESPERANÇA DO IGUAÇU | PARANÁ | Brasil | 4103024 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 984e8dac-3aee-3af8-ae37-2e2bbe9c49ba | -27.28371 | -49.82166 | 2026-03-29 04:21:00 | NOAA-20 | TROMBUDO CENTRAL | SANTA CATARINA | Brasil | 4218608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20cdd4f2-5c53-3f09-9f7b-b40cb73ade8b | -27.28034 | -49.82094 | 2026-03-29 04:21:00 | NOAA-20 | TROMBUDO CENTRAL | SANTA CATARINA | Brasil | 4218608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 09d913cf-e5d1-33e0-910f-63755bccc4a6 | -25.64276 | -53.20094 | 2026-03-29 04:21:00 | NOAA-20 | BOA ESPERANÇA DO IGUAÇU | PARANÁ | Brasil | 4103024 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b4019f3-7197-3f82-b473-62cc37fef9d3 | -25.26938 | -50.69484 | 2026-03-29 04:21:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8127e521-6ddd-3a63-a533-198f1f082464 | 3.40331 | -59.96492 | 2026-03-29 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb4b1b85-c966-3ad9-a3e6-1e2fabe80e9c | 3.43674 | -59.94661 | 2026-03-29 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21e6db58-7989-32b4-8923-cedbc40e58e4 | 3.44182 | -59.95034 | 2026-03-29 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaaf0b1c-8ef8-30c7-aad5-06d503903701 | 3.43232 | -59.94725 | 2026-03-29 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba8cbd24-703f-32e9-a9c5-e255c2714aa5 | 3.4008 | -59.97858 | 2026-03-29 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b224c9c2-f751-39f5-83da-b1de10990812 | -15.0874 | -43.89535 | 2026-03-29 05:08:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 317b2113-6467-3db0-aa1f-53e006f1070e | -13.15331 | -53.25636 | 2026-03-29 05:08:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README2.md)
