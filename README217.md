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

## Dados Diários - Página 217

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cda340ba-71a5-3bdd-a110-bd9354c70d2e | -8.6292 | -67.0111 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 129c280a-e9aa-3a48-92dd-427b0c07e761 | -8.6107 | -67.0116 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| bdde5aa2-8e41-350b-a174-138f882b66f7 | -8.1878 | -45.7584 | 2026-10-08 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 56017a58-4882-3500-aa78-2812ee6383ba | -1.3277 | -55.4327 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 09d09571-2118-3398-ba35-c7fabb959862 | -15.5216 | -42.6588 | 2026-10-08 14:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.5 |
| d6c98a33-6d83-38d2-b79c-888986a51faa | -11.6369 | -43.6876 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 407.7 |
| a17a4062-b423-34a4-8d47-a4365c044d4e | -5.7315 | -41.7069 | 2026-10-08 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 499226c5-3420-3899-a8c5-1a4c88249e34 | -5.372 | -44.1751 | 2026-10-08 14:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 6f4f9656-3e23-30ad-b634-57da6f5fd226 | -5.7319 | -41.6589 | 2026-10-08 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 303.8 |
| dc3e21d1-dc8e-3f07-a390-87f25a183d6c | -1.4756 | -54.5565 | 2026-10-08 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b6ad775b-5aaf-3a8b-8554-5e07819598fc | -12.0448 | -43.434 | 2026-10-08 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 4c2d19cb-fc00-3cd4-916c-199c782c3474 | -9.4751 | -64.3336 | 2026-10-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a42417de-0ffd-361e-bfd5-2ccf316accde | -11.6374 | -43.664 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7bb852bf-84da-3ff7-ad57-34fc6db369dd | -11.0953 | -44.0037 | 2026-10-08 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 405.7 |
| fa0f29bf-d366-314a-b083-698c574a4d7e | -1.4569 | -54.7562 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| af2e8334-5e3e-321f-a597-aab27a2781bd | -7.1825 | -52.6283 | 2026-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 52099f0d-7476-3906-8894-6e12feda5736 | -8.9501 | -45.1334 | 2026-10-08 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 368.7 |
| 03ceaa1c-9512-3d39-8717-0164a625f1b6 | -9.1543 | -49.8142 | 2026-10-08 14:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 3820e0c9-677d-3c82-b1c7-0d102499cf90 | 1.6385 | -55.785 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 5861325c-2046-335b-b0e7-10cda2f57f95 | -8.6106 | -67.0486 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 259.6 |
| dda51c86-4c48-39fb-85a0-fcf4aa49cbd1 | -11.6186 | -43.6433 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 370.3 |
| a88fb155-7c92-34ed-b01f-7d20846851ac | -11.6562 | -43.6846 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 23eedb70-bffc-336e-8b84-885b464abaa3 | -9.9014 | -44.8147 | 2026-10-08 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| c288c2ce-449f-3655-baf1-dd38ba016322 | 1.1507 | -50.7483 | 2026-10-08 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2f5245fc-8bd4-364c-95ee-6846d6f0a5cd | -10.6912 | -47.8278 | 2026-10-08 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7ccd492d-a501-3589-a51d-255c03b23636 | -10.5287 | -47.2711 | 2026-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 5df8d20b-7947-36c9-9865-b62690c92a8f | -5.7312 | -41.7309 | 2026-10-08 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 91ffb653-3fc7-3cc3-bad6-541c5f47dd64 | -8.5922 | -67.0306 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7f1607a4-cbc1-3f7d-b15b-6fb3c4feee36 | -11.4503 | -43.4091 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 35f19335-6243-317c-983e-415a9a8a84fc | -1.4569 | -54.7761 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2932de16-fa0c-3573-ab34-027c5b12c7ee | -8.1115 | -50.9206 | 2026-10-08 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 02def4ee-d5c7-37de-b1bc-9eaa35290821 | -11.3937 | -46.6922 | 2026-10-08 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d23aa0e8-e98d-31a7-af98-757948e2f565 | 1.6568 | -55.8045 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d235034d-8325-3d79-9c86-7a720a9efdb3 | -8.1996 | -46.3415 | 2026-10-08 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| e6e4ad22-267a-3f35-a41f-7eb3af875995 | -7.3547 | -50.0272 | 2026-10-08 14:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 868e0079-d3a8-3968-9640-45e1b4381eaa | -7.4697 | -42.8315 | 2026-10-08 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 64b52967-a39c-3233-ba50-d27c47caaeb7 | 3.1463 | -60.5937 | 2026-10-08 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a4365551-8851-34fb-97f4-bafe9bf3988e | -10.4724 | -47.2333 | 2026-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 0ed0666f-0a08-3a02-b38b-74ce50a5713e | -3.195 | -42.9772 | 2026-10-08 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1b0a5586-86fb-3c2a-8563-227f353bca9f | -6.988 | -59.123 | 2026-10-08 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b116b86a-d9f0-30e2-abe9-70e04d14cda8 | -9.9018 | -44.7917 | 2026-10-08 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| fd7267bf-7b6b-3b08-994f-3f1e4c7cfc24 | -11.4507 | -43.3854 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.9 |
| ccc34a66-ff1b-3ba8-b06b-90ea92e04298 | -7.3286 | -50.8314 | 2026-10-08 14:40:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 25cc55db-7bb5-326b-8684-e0947ebba58f | 1.6568 | -55.7847 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 119e631f-a1e8-3247-9b4c-082e9fe26fd3 | -7.2369 | -55.1206 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 233.6 |
| 69ab0d0b-675a-32ab-bc24-a12241d97e75 | -6.4392 | -52.7138 | 2026-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5109d975-2ebd-3fc9-b162-35f4f07ab693 | -4.1457 | -43.2103 | 2026-10-08 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0bff2a1c-96b9-319c-90a1-7acbe93e317c | 3.1098 | -60.5943 | 2026-10-08 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a3017446-639f-3eef-8ffb-df3751b72351 | -8.6107 | -67.0301 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 403.8 |
| a15ffdd7-dc6b-3184-9b1e-31044a37de73 | -6.4394 | -52.6933 | 2026-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9d2f26e4-dad7-377c-b1b7-5f2c3b7d228e | -9.8821 | -44.8402 | 2026-10-08 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8d1ded91-0002-331e-bfac-575862638242 | -10.4337 | -47.2824 | 2026-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| a9f69b52-00ce-360c-b01b-5cb325b38680 | -3.86 | -44.1274 | 2026-10-08 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 675a1f9b-23bc-3a5d-8741-89a2595b21c8 | -6.6628 | -55.0912 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d9782c22-2835-36b4-9f0d-49d046081819 | -6.6716 | -45.3308 | 2026-10-08 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 76800e1a-4500-38ec-915b-97650971d2dc | -11.2482 | -46.2604 | 2026-10-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 45e51ac4-a54b-36c7-b6b3-d575abe102b7 | -10.4527 | -47.2801 | 2026-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 461cb247-eea9-3c06-97d1-d1b3448c1580 | -9.7691 | -44.7851 | 2026-10-08 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0e78b458-1653-3b3c-a4c2-c038f4eece6f | -8.2826 | -45.7038 | 2026-10-08 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 64cdc496-58a6-3ea4-bdcf-e9289c6f7698 | -11.619 | -43.6196 | 2026-10-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 691218d6-7f88-3a47-b72a-b8bbef34f0db | -11.8404 | -47.372 | 2026-10-08 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 591dc94f-50fa-3f66-98bc-ae890ab4e8d6 | -9.7689 | -64.9992 | 2026-10-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 115251a4-645f-384f-b193-375f742e221a | -9.5004 | -66.7831 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e1c1ed52-71e6-32e8-9250-c308619abf4b | -1.5306 | -54.5359 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9bd952bd-9d79-38b0-8849-6eeaf21b63c6 | -10.4147 | -47.2846 | 2026-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c50bcea4-ebc4-3c49-aff5-6efc3a4ef2a7 | -13.1833 | -54.3158 | 2026-10-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 413.5 |
| 1548795a-cd37-3de2-9f7d-b353da7ec535 | -7.218 | -55.1617 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6a01cdfb-0ad1-3e69-b063-047dc2691085 | -7.2184 | -55.1216 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 897d4a1e-5e14-3b6c-934e-08cfed270e1c | -8.5921 | -67.0491 | 2026-10-08 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5023a6b2-2a7e-37db-8aeb-6e607adef74f | -6.9881 | -59.1037 | 2026-10-08 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 15ea1f88-9dc5-3f7f-a78d-c306ef4daa46 | -1.6213 | -55.1321 | 2026-10-08 14:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f92e62ca-7ca0-3ffc-a283-2de022ed779e | -1.5118 | -54.8153 | 2026-10-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 9d280055-bf99-31bf-b911-881d0c99b117 | -9.9398 | -43.5542 | 2026-10-08 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 270.6 |
| 49abc1cf-1859-3505-a143-fa84e8e821af | -6.7368 | -55.1074 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5b7b009e-b09b-3642-8cc8-7f82a74be720 | -11.2486 | -46.2377 | 2026-10-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 381aa3a2-5809-36cf-bed0-5fd9faa7e026 | 1.6937 | -55.6263 | 2026-10-08 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 990cd0a4-0609-36f3-a74d-f1cafa9dde4c | -6.3283 | -55.3276 | 2026-10-08 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f956821a-4855-3f5b-b8a0-e90e7515f51e | -9.4749 | -64.3713 | 2026-10-08 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bfd78d48-1c30-3f7e-9f09-69c6169db127 | -7.2187 | -55.0815 | 2026-10-08 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e64154c2-11b3-3fa0-be6f-ee693c1b44ea | -11.3103 | -44.8337 | 2026-10-08 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 95e6d56c-c96e-3c4d-b07f-659bb013d385 | -8.9054 | -63.3378 | 2026-10-08 14:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 341b6439-5dae-366e-ac77-eaf7af663e2b | -11.7771 | -47.7365 | 2026-10-08 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5338db1c-6304-321e-bde8-3629cb0bc441 | -8.2181 | -46.362 | 2026-10-08 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| bca73979-eb32-35ec-be43-aeb447905c2a | -4.3471 | -43.8021 | 2026-10-08 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 3531ebde-83bf-3281-a296-5f6f8f7b6ca9 | -11.8595 | -47.3694 | 2026-10-08 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d3a455f3-4c95-350b-9814-8f5eee59d0c6 | -11.2083 | -45.217 | 2026-10-08 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 7390cb82-be9d-3f2d-89c9-4c366a3bf6e2 | -6.5129 | -55.3784 | 2026-10-08 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9f59d951-563b-3bf3-9042-a801c17611b0 | -5.7321 | -41.6349 | 2026-10-08 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 216.6 |
| 756333b6-5448-3004-8dc7-d2587d4ae2df | -12.1964 | -57.1303 | 2026-10-08 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 957deb5c-21aa-3915-bdcf-d4e5ada09ad4 | -8.5922 | -67.0306 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| f18f3c3f-3e0c-3cb7-b408-1ddfa95ba3e3 | -6.2162 | -52.7876 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 96f7d008-c748-36fe-865d-6e5f55806f77 | -2.7797 | -54.0736 | 2026-10-08 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| a12230c4-598f-34ee-9e62-eca288a6e228 | -6.9737 | -45.124 | 2026-10-08 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4e684e08-6ee0-359f-9d5b-66a9b3f65624 | -12.1922 | -44.7953 | 2026-10-08 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| d75d2ade-cd26-3f11-a392-8ffb817baf2a | -3.195 | -42.9772 | 2026-10-08 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| fe974d6a-f16b-3094-b7f0-42122811fe19 | -1.3277 | -55.4525 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b47a5fb0-f38e-35f2-acdf-3e3882286e13 | -9.5004 | -66.7831 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| dd37c000-a25b-3d29-81f4-bb3da989e420 | -6.3217 | -53.5772 | 2026-10-08 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 08c3df81-a344-3b37-ae3a-1a702631c238 | -9.4749 | -64.3713 | 2026-10-08 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| be04d2c2-c768-32fd-add6-89d844dc113d | -5.7317 | -41.6829 | 2026-10-08 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |


[Clique aqui para ver as próximas entradas](README218.md)
