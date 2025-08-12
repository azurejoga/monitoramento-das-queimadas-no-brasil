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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e5b4002-91d4-34b6-951c-03bd3f86dcd9 | -3.83587 | -47.74258 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 86e483aa-66ec-31d3-88e9-3deeb3d48287 | -8.21225 | -45.04613 | 2025-08-12 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e581b130-1608-3bff-9d71-e081d079a96a | -7.20857 | -46.21437 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5ac6718-82d2-39de-9ee3-7bf1fd85329a | -5.93903 | -39.47692 | 2025-08-12 03:45:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 676080cd-6590-3b1f-a1a0-bae4312a8011 | -6.21939 | -43.32882 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 68c9058c-01d9-397e-80f3-83fb2830f533 | -4.31064 | -48.10022 | 2025-08-12 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7a9d85d7-14a1-3c1c-8bf0-59f9fc0d4534 | -6.46504 | -44.57487 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8732af6-cc7a-3fb0-b853-6214d7e39ccf | -8.9935 | -47.45595 | 2025-08-12 03:45:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f8a4a52-70ee-3322-8a27-0064002cd5e0 | -6.46441 | -44.5784 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd6c5ff2-e8f9-3540-8cca-d9734753451f | -6.72346 | -43.5811 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10c6856b-2513-33fd-9849-67b54452ca3a | -5.53524 | -42.66345 | 2025-08-12 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7deda996-26f6-3619-8c80-f773bae7893f | -3.97277 | -47.88465 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b6869de-3414-3ec2-b78a-a62917a1e4ee | -7.21094 | -46.22728 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 110b5176-23cf-3d54-a227-efb6c3b08f0a | -8.52247 | -43.30886 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2ae32961-d79b-3f42-b7f3-30f8b45cca89 | -8.51571 | -43.31865 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad9673dd-95e5-320a-b575-5b8935a2aa5e | -6.57377 | -44.56928 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 859f2392-711a-3682-835a-68d791e429fd | -5.83495 | -44.10831 | 2025-08-12 03:45:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0dd7b369-e62c-3761-b71c-c743f113809c | -6.22073 | -43.33146 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 669f28c2-829c-3a31-b02b-47017daa6a66 | -9.6306 | -40.58634 | 2025-08-12 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9050e5c5-c38d-3051-80fa-5ac63b377803 | -7.21197 | -46.22936 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed100dd8-21dd-3729-b51f-bb2f21dca7c1 | -7.23048 | -41.91137 | 2025-08-12 03:45:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c762a6b-d333-3650-b3d7-dfd982df8d69 | -10.15447 | -40.52416 | 2025-08-12 03:45:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f21c4a86-7548-3afb-9e15-3d6280933356 | -6.21888 | -43.3317 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9cd2cbee-5741-398d-829c-0f22b0294d54 | -6.58395 | -44.57522 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cba2f95a-9e5f-3689-a8ed-d9bc434b0af9 | -4.31447 | -48.10262 | 2025-08-12 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ff05bf53-87e9-3c55-a3c6-5ba56984338d | -6.58648 | -44.56103 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f5168619-cf32-3bf3-828b-5207a1fcc430 | -6.72127 | -43.57647 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8bb4133-a012-39c2-b472-5519f97e18b7 | -6.60951 | -43.88432 | 2025-08-12 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 20c96c9d-a15c-3acd-8904-c189f698a6c4 | -6.22122 | -43.32859 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5e07435-0821-3ada-a36f-7e2c3b3b5bab | -9.1999 | -44.53343 | 2025-08-12 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32b75448-4954-3987-aba9-b42c6f0cb65a | -7.21685 | -46.22892 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a183893-ba6f-3a25-870f-ad3a6aebdaeb | -7.21765 | -46.2244 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91c29515-fb19-3a75-a063-3355eb5c9c24 | -7.11731 | -44.62679 | 2025-08-12 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e0f1eef-f474-393f-a316-e949aa6cfc49 | -8.51667 | -43.31331 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 792bcbd8-d2d6-3e23-88ca-80d3bc35c3f0 | -8.66771 | -36.23353 | 2025-08-12 03:45:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b6a7b5e2-9603-3983-aea9-328389d29745 | -6.61471 | -43.88527 | 2025-08-12 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dab0645f-bc6f-324c-a46f-ba91d5211e8f | -8.52055 | -43.31953 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6027525f-fdae-3e3d-87e8-fe33486ddf2b | -6.61359 | -43.89165 | 2025-08-12 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a3dc8ce-51b9-3f6e-a901-bbf13fa90c3c | -7.21871 | -35.7682 | 2025-08-12 03:45:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85f0b6de-dce1-3b1d-b9b7-3945a74d811c | -3.83444 | -47.74597 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7db064b3-3d06-3da3-8e7c-1cff73604860 | -4.60185 | -43.31843 | 2025-08-12 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d43281fb-9f19-3972-a352-c682d21af28c | -6.58713 | -44.55743 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b397610b-9d53-392f-8a21-42f54809767f | -6.57919 | -44.5704 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 880e7ec0-9813-3fbd-80e4-3b252791dfa5 | -6.57565 | -44.55879 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96462fd3-8f28-3757-9841-d0a5db0a6a2d | -8.52151 | -43.31419 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7370e905-bf09-3fcf-84a1-44ba4d04c835 | -8.21159 | -45.04971 | 2025-08-12 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9776fce1-58d5-37b3-8611-81a5f26cc482 | -3.9657 | -47.88403 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 94ee037e-bbae-3319-80fe-f0bffd4361ad | -7.20869 | -35.59525 | 2025-08-12 03:45:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66dfdbe9-ee25-30e5-980a-a5cf0d18495b | -3.83471 | -47.74929 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6df6486c-2a45-36b4-982c-d6b4aebe619e | -4.30946 | -48.10696 | 2025-08-12 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 558d98a1-81e8-3c8d-bbe9-55817be411ef | -6.1516 | -41.38708 | 2025-08-12 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1806477-a915-3e49-b811-383f34443735 | -6.5817 | -44.55636 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 180a0878-8290-3ca8-9798-973a601400d5 | -4.60119 | -43.31618 | 2025-08-12 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b056c372-c128-39c5-a15a-649ba5c40f51 | -6.21621 | -43.32751 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 149920a8-a9d0-3c6a-92d8-93859d503ce5 | -7.20814 | -35.59872 | 2025-08-12 03:45:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbfb5f6f-e9ba-339a-a7c4-7bd0c944a7ed | -7.21173 | -46.22291 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b2081ac-a6c4-3f33-aafd-86b46fb484e0 | -8.21093 | -45.0533 | 2025-08-12 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55c5f89b-f4de-360f-845d-bc1f1a53cb00 | -6.71892 | -43.57715 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3cc5dcbe-6f5c-3a3a-8ee3-896ad3d84c34 | -7.30135 | -39.64494 | 2025-08-12 03:45:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a58fc40f-4547-36b3-b30a-d16d395ad5f9 | -6.59185 | -44.56244 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71194420-8f8d-39de-ad92-583a05e6e04e | -6.60896 | -43.88745 | 2025-08-12 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5d6c92a8-e04c-3ea4-a322-e5f5f109a414 | -7.2133 | -46.21412 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35211aa5-9edd-31b0-9c13-ab334a571c01 | -6.21571 | -43.33044 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f67b16b-fc61-31ca-9501-64644533836d | -7.21872 | -46.22644 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| daba8e55-a6ba-31c2-b2ce-0f0a6e1fd56a | -8.21575 | -45.05788 | 2025-08-12 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b53eafd5-9527-369a-a845-1d6bed8aa1c5 | -3.97398 | -47.87783 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b2260336-8588-34a3-a799-df7a69c6dec2 | -6.72399 | -43.57812 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a3579b6-0b8b-3417-a2ae-3d783f9fa839 | -7.21201 | -35.59578 | 2025-08-12 03:45:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 23e8c1f5-1159-3766-a08f-a98c3be41b74 | -6.58522 | -44.56813 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 953ea57d-133a-309d-8a94-c9400e8b5d3d | -4.30747 | -48.10128 | 2025-08-12 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bec89660-28dc-3dda-b8f9-feb8cf853aa5 | -3.83324 | -47.75266 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 17134c69-2592-39ba-8e7a-1bd95cf82381 | -5.83018 | -44.10403 | 2025-08-12 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89fb6c28-ad93-39d4-b879-fb05b4f840b6 | -4.60068 | -43.31927 | 2025-08-12 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798604ef-1ec2-3461-b39c-2983c254f394 | -6.22442 | -43.32981 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 710676f8-9238-3b3d-8715-ce1002c0d36a | -5.49458 | -43.98942 | 2025-08-12 03:45:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2f0bb72-5f94-3cbf-90e0-0577b0ee1391 | -8.51959 | -43.32486 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ccfed396-e1dd-3542-9206-0dc6e0d0d28a | -7.22203 | -35.76874 | 2025-08-12 03:45:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d8e69ec-59f8-37a7-baed-ab2a393f3382 | -6.84221 | -37.37109 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a60b0b4-dd50-37a7-a36f-112c315f8ffa | -5.49518 | -43.98603 | 2025-08-12 03:45:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f70ee174-c717-34a4-9fc2-9f44fb6f8c8c | -8.21027 | -45.05692 | 2025-08-12 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd3fa56a-9fed-3efe-8c5d-0af35efae2b9 | -4.59601 | -43.31533 | 2025-08-12 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 391a0134-92a6-3a21-a625-ea20a7ffc3ba | -6.21991 | -43.3259 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6abfc4f2-31b7-3f4e-ae8a-84ea0cd787c4 | -8.51763 | -43.30798 | 2025-08-12 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f39bc90-57e7-33c0-b16b-f62fd95ca7fd | -6.58459 | -44.57167 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c319ed88-6b42-3857-8d8e-9b3e25cc77f0 | -7.21361 | -46.22057 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdf41a47-a3bf-399c-93df-1173dce639f3 | -6.57857 | -44.57391 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83e12c5a-66cc-3ba8-92b5-2efce163e0e0 | -9.20511 | -44.53433 | 2025-08-12 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8932afef-1aa3-346b-a5b8-9e836744911b | -6.72077 | -43.57941 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61914a71-b091-3411-bdab-2518d2c7d33e | -7.23128 | -41.90681 | 2025-08-12 03:45:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ec9fb67-8630-359d-a52c-f1b58d938c0d | -6.58108 | -44.55986 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68e6c898-f772-35ad-90f5-a3a4905bf6da | -6.22172 | -43.32566 | 2025-08-12 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43bb9007-38b0-36b3-b4a8-d7042a4fe7c7 | -9.30087 | -40.21954 | 2025-08-12 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aee980b1-6a30-32ce-b036-03d22a041b91 | -5.54012 | -42.66426 | 2025-08-12 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1051c3a4-4c05-3eb7-bb78-931caf673327 | -7.21279 | -46.22499 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fba292e0-0a75-38d9-a9c8-1a4c2e46f704 | -6.58585 | -44.56459 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d94faa14-c566-3381-9514-76a773f216c7 | -6.61415 | -43.88843 | 2025-08-12 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1d40bfb-7f7c-33ab-a7ae-10062998b0ec | -4.60239 | -43.31535 | 2025-08-12 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20daa29b-cfc3-342f-adf0-39900dabea13 | -6.57314 | -44.57279 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bca6f609-c3b4-3c6a-808f-0c4305ef8f42 | -7.21251 | -46.21852 | 2025-08-12 03:45:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4291b586-3b35-36d9-aaf9-6bfb06be3e7d | -7.30218 | -39.64009 | 2025-08-12 03:45:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
