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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8072fdf6-6763-39da-b242-9a4b51e25526 | -5.3902 | -41.24085 | 2024-10-12 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0670f79-064d-35d8-ae2d-51139286de13 | -5.19247 | -41.28769 | 2024-10-12 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38be5ada-63b3-35da-80ea-5e2180102c74 | -5.12013 | -41.68281 | 2024-10-12 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 241d3b53-8cff-32cd-9b1b-cfabbd5980a0 | -5.11682 | -41.68229 | 2024-10-12 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b5c7fcd-0e90-354f-aa39-011813e1f54e | -5.11627 | -41.68575 | 2024-10-12 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1899f15-b97a-3194-830b-f91c06d44835 | -5.11573 | -41.68921 | 2024-10-12 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 548ea486-2891-3133-bfb8-2ba090355a3a | -5.11518 | -41.69267 | 2024-10-12 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93557a3a-c626-315b-b4b8-fabd9be29cb9 | -7.99322 | -40.96973 | 2024-10-12 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16fd10cf-ab99-30eb-a9be-343ee3ecbbdf | -7.92469 | -40.95221 | 2024-10-12 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cb5c644-5c4a-30e1-84ec-c0b90f6adfa7 | -7.16394 | -41.41102 | 2024-10-12 04:06:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d611cb3a-b710-3d8c-aaf6-d49ea5469878 | -8.87063 | -42.43904 | 2024-10-12 04:06:00 | NOAA-20 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c5269b98-2b72-3b1d-a7af-452cbdc0e80a | -8.3762 | -41.01878 | 2024-10-12 04:06:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e042ea8-f1cc-3fb1-8ac4-6cc5f0ed0f5b | -8.24168 | -41.1202 | 2024-10-12 04:06:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44f6663e-dd3c-3dd1-8d0a-55a018377c40 | -8.08456 | -41.08105 | 2024-10-12 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62cfc4c3-dece-3e95-a387-22d5331eff47 | -8.08124 | -41.08054 | 2024-10-12 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af90fec5-da30-3f29-a34b-8fd4b2039fc3 | -11.2182 | -41.60705 | 2024-10-12 04:06:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5dcf57d-4c52-3421-8e3d-55b2356ba343 | -11.21541 | -41.60297 | 2024-10-12 04:06:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b2b0035-3fca-3760-b690-27af425b8523 | -11.21486 | -41.60653 | 2024-10-12 04:06:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01a6b348-c7dd-3bcf-9510-764511f507ec | -10.84178 | -42.86442 | 2024-10-12 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 015fd9f5-7f52-3821-8c10-e367a743b2cc | -6.58377 | -42.24557 | 2024-10-12 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec549564-2f2e-3483-b77c-00b03e60cb68 | -6.57555 | -42.08381 | 2024-10-12 04:06:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2135093f-9cb0-3283-ab79-ec6298645564 | -6.16273 | -42.69506 | 2024-10-12 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60ed3e6b-e6ec-38e7-8b9b-9d2cb341cdf3 | -6.16217 | -42.69862 | 2024-10-12 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ec38f2a4-8253-3cea-958a-e2f3996b7ebc | -6.15882 | -42.69808 | 2024-10-12 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59c9bd98-56fd-32b9-ab85-a64b765e3e23 | -6.13233 | -42.77806 | 2024-10-12 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac947a41-83e0-3937-b76e-9b573c6fbc1c | -5.95677 | -43.19765 | 2024-10-12 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c479f5e0-d7fc-383b-9cc6-b9effdd158cb | -5.93138 | -42.73926 | 2024-10-12 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34a899b9-da4f-364c-b748-a2eb7efee567 | -5.88059 | -41.94508 | 2024-10-12 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 755d74ae-5b3b-3cb4-b990-51fcc9c8ce18 | -5.80205 | -43.0007 | 2024-10-12 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0fc98b19-1462-3816-a7e3-27e707ad3aea | -5.7929 | -42.51668 | 2024-10-12 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bf3cd042-7cdd-3e40-a90c-d1be2137f4ad | -5.46518 | -42.01483 | 2024-10-12 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e3c8ef7b-d3ba-3833-9531-1e5d60af4bfb | -5.27622 | -41.83494 | 2024-10-12 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a633a402-d8dc-3ea5-b924-1d02913007ae | -5.2729 | -41.83442 | 2024-10-12 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ba36728-4a5a-3d57-be30-d26c5e38acaa | -5.93027 | -43.34141 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9f97267-b9dd-31dd-acd5-0252a101ee76 | -5.92684 | -43.34087 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3814069d-266f-3171-af24-146ccbacdd3d | -6.58708 | -42.2461 | 2024-10-12 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 08826a83-3571-3c12-9ff1-64811e72e7bf | -6.62261 | -43.57188 | 2024-10-12 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb71ff16-15ca-3082-a87a-a20574f868c5 | -7.71484 | -43.16941 | 2024-10-12 04:06:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3550f73-14b5-31cf-bfc2-5634131204d2 | -7.2103 | -42.28127 | 2024-10-12 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d7a2478a-16f2-306b-b4a0-9ed8e57f5800 | -7.05229 | -42.7168 | 2024-10-12 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5c0e5440-9435-3bfa-9791-a03c919cff6d | -9.26326 | -43.17193 | 2024-10-12 04:06:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa4933c6-1f45-3a7a-b049-75eb8f7e9cc9 | -9.26257 | -43.53906 | 2024-10-12 04:06:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 57b8e4d3-7cd1-320a-bedf-0b5a0038c67c | -9.26198 | -43.54272 | 2024-10-12 04:06:00 | NOAA-20 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ec8ace96-dec7-3f17-ab01-f7ce2e1b4493 | -9.26066 | -43.17228 | 2024-10-12 04:06:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 75cffb24-5896-3064-83a9-0860e204b9f3 | -9.2592 | -43.53851 | 2024-10-12 04:06:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10d1be9c-18f8-3dbc-aacc-db1a085959c1 | -9.20314 | -43.2322 | 2024-10-12 04:06:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71da6a62-cfd3-3234-9d16-720d2a95a46b | -9.03121 | -42.69052 | 2024-10-12 04:06:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d4091e1-2927-3fef-ae9c-c196d7dcad9e | -9.01795 | -42.98732 | 2024-10-12 04:06:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68cd477d-f107-3696-aa01-b8df4ced4298 | -8.38784 | -42.44006 | 2024-10-12 04:06:00 | NOAA-20 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 751df322-78d9-3a5a-bf79-23d1d241c6ee | -8.38232 | -42.45348 | 2024-10-12 04:06:00 | NOAA-20 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 502ebd4d-43c4-3802-afb8-15687b867d89 | -8.37846 | -42.45644 | 2024-10-12 04:06:00 | NOAA-20 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bef0a4cf-aa04-31de-8d7a-9c4574b64754 | -8.27449 | -43.1117 | 2024-10-12 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b9edf3f-c284-35cd-a10f-0c81d8882451 | -8.27392 | -43.11528 | 2024-10-12 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a71c977c-9bf8-32de-97d5-a684c616bddf | -10.34293 | -44.36507 | 2024-10-12 04:06:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c89a635-668c-319c-ac43-cf987e70a912 | -10.33951 | -44.36449 | 2024-10-12 04:06:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0675f4a-9ae5-3ec1-b79b-5300de3a5d7e | -10.25927 | -43.97348 | 2024-10-12 04:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf818c84-bc66-32b7-a9b9-7c80720b7fee | -10.25868 | -43.97713 | 2024-10-12 04:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 819ab22e-18a9-3553-b67b-03b7fe8b0b2e | -10.25251 | -43.97237 | 2024-10-12 04:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc6e88c4-ffe4-326b-802d-c7bf1f582313 | -9.67054 | -42.85827 | 2024-10-12 04:06:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f9a17344-5034-3196-8375-b4d33aa0ae2d | -10.83977 | -44.43756 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 868ca151-c44d-31c1-8c24-bae2bb99cfc2 | -10.83915 | -44.44134 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0abd7aa4-6a1e-3bcc-bb97-f29018132128 | -10.83574 | -44.44075 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dc33b9b-ac13-3162-8f6a-f815340abf37 | -10.81535 | -44.30715 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27d5550-4d65-3a0d-ae61-5f68b789590b | -10.81475 | -44.31087 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41e5e994-7753-34e4-8727-3bacda09188f | -4.81876 | -44.35629 | 2024-10-12 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1bf1d2b-b388-35a9-853b-c3eb9e2ceaa0 | -6.52747 | -44.0471 | 2024-10-12 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4404ca4-421e-3bfa-bae7-041f53ca5e94 | -6.49962 | -44.15097 | 2024-10-12 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63f60d90-95b9-387c-a78d-d3cd25199782 | -6.44981 | -44.27903 | 2024-10-12 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a41ff593-dcf3-3557-87ef-6a207fc40e72 | -6.44694 | -44.27425 | 2024-10-12 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ece0302-e66b-37b9-ab41-9f8dddbddf77 | -6.43214 | -44.27591 | 2024-10-12 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da7828c6-686c-31fa-8715-baa3662757f3 | -6.36777 | -44.4025 | 2024-10-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 800b81c9-27f4-3667-ba83-376812fc9778 | -6.3671 | -44.40659 | 2024-10-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1822f3cb-969a-3860-a69c-5bca3e5b8c97 | -6.36345 | -44.09473 | 2024-10-12 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 219bebda-f828-3090-bb3a-b88d1ba5e948 | -6.12102 | -44.94678 | 2024-10-12 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfa9326c-4eb1-3109-89e5-8a1dddc5059e | -6.12032 | -44.95111 | 2024-10-12 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3462f53a-aad0-33c6-9537-f6c734881e90 | -6.08449 | -44.84779 | 2024-10-12 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ef10555-873b-3c5d-a618-8001f130af24 | -6.07334 | -44.63801 | 2024-10-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6b36735-3304-327b-9e7c-00ea8526dc51 | -6.06904 | -44.64164 | 2024-10-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e4eee2a-bc25-31e7-8639-0e04bae9bff3 | -6.06543 | -44.64103 | 2024-10-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 76841c54-caf1-3923-8ba6-da9d94538f68 | -6.06474 | -44.64529 | 2024-10-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c5af5a6-bab6-3d97-8943-c9cc496a56b0 | -5.9071 | -44.6724 | 2024-10-12 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faea3a45-5d89-3b3c-a555-54cf796ae917 | -5.55483 | -44.69452 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7876e16a-417a-3f2e-a84c-fa9b621646d8 | -5.55412 | -44.6988 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62fb0603-9f7a-3650-b5a5-80f28f7f87c5 | -5.55119 | -44.69387 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f37249f-bc10-32ef-bc1b-e5c2876c3aab | -5.55048 | -44.69815 | 2024-10-12 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c5561f3-e2ce-3c3c-80ab-3e8446109369 | -5.44039 | -44.02206 | 2024-10-12 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a2dd853-54ef-3407-8665-edbb9bbe76ec | -5.34248 | -44.52781 | 2024-10-12 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3a8a4c2-4c93-3257-81b0-addb2e9dc409 | -5.34169 | -44.52926 | 2024-10-12 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03ec703e-f717-37a9-a1b6-2539c1776fb0 | -5.33099 | -44.18316 | 2024-10-12 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cff34148-6c80-3c89-ac91-ced0ebdd52ed | -5.32785 | -44.77557 | 2024-10-12 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42962e1d-e7ba-3b79-9497-15379e37f7c6 | -5.23211 | -44.76634 | 2024-10-12 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5318f1aa-638a-3a02-895f-64df4e48e9b8 | -5.12096 | -44.66595 | 2024-10-12 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2f97eda-33ee-3742-8bb6-3484ddec77c9 | -5.09919 | -44.24915 | 2024-10-12 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 876deba6-7b4b-3f79-ad9e-08ff8d45626d | -5.08357 | -44.78606 | 2024-10-12 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 919c89b6-10bc-3ac6-987c-97b280900dcf | -4.97534 | -44.78352 | 2024-10-12 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86cb1235-c31c-3d58-90c4-1a8e4b277a62 | -5.25727 | -43.44883 | 2024-10-12 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd0281e5-edc5-38e1-a9d2-4c4e8513f4c8 | -6.99845 | -45.21428 | 2024-10-12 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98b5cb7f-74dd-3967-aa28-84a92b1958e3 | -6.99477 | -45.21364 | 2024-10-12 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75a23b99-e2cd-3993-a706-552ec08e5c62 | -6.99404 | -45.21803 | 2024-10-12 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d9cbcc3-99ae-39d6-8d7b-07e7721feee2 | -6.72707 | -44.44528 | 2024-10-12 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
