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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3191d97-751a-3382-8d3d-325782e38787 | -7.32749 | -44.58967 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d2ba194-d5e7-380f-8a3c-d0f11ccec861 | -8.63202 | -45.73456 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d433cd5-ebf9-3001-8f4a-1b27cdfb2aa9 | -5.67808 | -43.4917 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 112039b7-290b-34f8-8dfb-d26fd86d4951 | -5.63754 | -45.94667 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71b02d06-cc7d-3c0a-8ee4-09fb7e9ae927 | -7.90447 | -46.24257 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b1a4997-c580-3d91-9806-803fa09215de | -8.88312 | -45.43292 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 582f1165-e855-31bb-a590-271acb9b2e34 | -5.86726 | -43.71944 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7d46c0f-2594-3d22-b318-84bc91ce1119 | -6.10531 | -43.72005 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d969e8-3f4e-3995-b557-9e92fe52166b | -7.0509 | -44.13622 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0b0954a-3306-3f08-941d-eb2521865270 | -6.444 | -44.49686 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dcbb5e5-7c2e-3f5a-a25e-a3ce45fa5f8b | -6.43998 | -44.08385 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3acd522e-22b6-3f0f-9e23-03b3b8f961d6 | -7.6376 | -49.73672 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87a3ba4f-0b71-3066-8f41-0c2731224a9d | -5.70052 | -49.19731 | 2025-09-15 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b83b04e2-bab7-30dd-a18f-b23f6c7ccc64 | -6.02187 | -43.66379 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 020c02be-760b-3bb1-898d-bdb5a2d9af85 | -6.93598 | -44.78991 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3839c6f8-87a1-3b87-b2b4-070c6d00e18d | -8.97882 | -45.8223 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4f8394ed-b340-3416-bc47-7fd298fa4918 | -7.80027 | -46.12802 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f39d2d25-7fb9-32e9-b1d4-ed37f42a8f82 | -8.91782 | -45.4959 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f3187fb-ec45-3054-badc-41d2fba5e214 | -5.74291 | -43.20621 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8192f3e2-d1db-3320-ba1a-4bbca35bb5c4 | -7.48748 | -46.12512 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f29e6f3-d35a-33fb-b37c-6da2e5589494 | -6.26469 | -43.47647 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd1ef653-9b4d-3778-91c3-f291a14512f7 | -3.64782 | -54.06059 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3654e7e-c170-338d-b72a-7417d21b520a | -6.41076 | -46.94159 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3984459c-5c79-38cf-8f64-15ed782623fb | -7.68102 | -44.48161 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d630784-9aab-3bb8-b24e-cd367ea82dca | -6.62794 | -51.004 | 2025-09-15 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02c8a919-b1ca-3733-9195-fbfdaf6bb033 | -5.93248 | -43.23162 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87e33f73-fa76-30b5-b7d8-04b600946559 | -9.23065 | -45.67056 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50b473aa-bddd-3b1c-8df8-74847fc85b79 | -8.11336 | -44.8313 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc3b3751-3122-31c7-93e9-0cf08086be0c | -8.78915 | -46.03102 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e50d2ef-5e29-376f-8ec6-fd6b6fa5c8c1 | -7.89358 | -43.582 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d0b431c1-6b7a-3059-b111-1843c3fd9e03 | -6.55679 | -43.98811 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11246bbc-e253-38ea-bb0a-cfcf887ba575 | -6.41482 | -45.85182 | 2025-09-15 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15df985a-d7f9-39ae-8424-646757914d3e | -7.85689 | -46.11533 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d98f58ad-ab12-3654-afd2-ec7bae3cefff | -7.69646 | -48.86255 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da3f2d3-0882-3707-ba28-7428ef153c1b | -4.66448 | -40.5626 | 2025-09-15 04:19:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2d7c551-1e5d-367d-928f-d09c514964bc | -7.06154 | -43.8895 | 2025-09-15 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baeec720-4060-3d80-a003-3f89e4cd14d3 | -8.97607 | -45.81828 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20202c11-25a4-3598-9ac6-b92440147c1c | -7.88903 | -43.56642 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| fe1d7bbf-baa0-3f88-8772-6f9bbd22ceaa | -7.02419 | -44.52754 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dcc6cfc-5722-3c6b-9246-707273f1f182 | -7.8851 | -43.56953 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e632c5ad-46e9-303e-86f7-d351e6faa017 | -5.64314 | -43.89182 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2550f3f-fcbc-366d-b4f0-b67e29353408 | -9.00943 | -47.03949 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eab39fd-b688-3a34-a2a1-5f1de5bcd51f | -8.62 | -45.74332 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 5562d6d5-1c96-3e3c-ab0a-72f5d30abfee | -7.51894 | -44.36368 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81598ed6-16b6-3efa-928e-25c800a076de | -5.96117 | -42.79555 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4745f3a0-6e58-30a3-b5cc-035ed156f883 | -8.9474 | -46.04256 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9ca9892-2cbf-3334-9cb2-10f7e6d4224c | -6.88884 | -45.62949 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61a0a7e9-2aba-3118-8c8c-7653b8bcf1fa | -5.76557 | -43.91486 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21da216d-331d-3230-8875-7a4750e7be32 | -7.63674 | -49.7417 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1270fc6e-30b0-3909-8fa7-c8de7a939bcc | -6.33215 | -43.41729 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdb4d1ac-ba4a-3749-922f-8d51e9466ac9 | -9.19457 | -45.24818 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ca9deda0-f51f-3b31-afa9-85b07a9126f4 | -6.19998 | -46.43426 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dd316cb-acd8-3b01-aa27-993ec15e76e9 | -6.40388 | -46.9405 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b9055c1-cf2b-3da5-9707-c21a2d02034c | -7.05314 | -44.14378 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1892f02-d8db-3dd7-b125-1bccd241490b | -5.88309 | -44.90554 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b491a2db-56ca-3c11-87ac-a5613a53df69 | -7.39266 | -49.99041 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca4884e-cb4e-3baf-a3f3-8fba8f9bc0a5 | -8.95789 | -46.04063 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b8d0231-5f50-3bb3-848c-f5cb1bf250d0 | -5.9336 | -44.86776 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb333bc9-37d5-3c5c-aafc-e938abca60d4 | -5.76705 | -42.43263 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6cdcd47a-13df-3718-a654-a871ff6aa8bf | -7.87388 | -43.57523 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1315ab43-d580-3fa1-9b90-6ecfff08892e | -7.88282 | -43.56174 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b536344d-95f8-3b94-97b0-007be0878978 | -8.9656 | -45.77736 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24f815a3-722f-36dd-a612-bddfd8492735 | -8.77701 | -46.0649 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7d3bfbf-487c-3760-894e-e6aab99ad888 | -8.7875 | -46.04151 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ada01bc-a639-33be-8bd8-5cd644aeed5a | -7.87898 | -43.58716 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6675cb0e-5674-36df-a8db-bc28e2dc6a93 | -8.314 | -44.91599 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2521a9e-2ffa-3309-8901-264cfcda7c38 | -5.9369 | -44.86827 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad1a4e3e-05bf-331f-8277-12cff8ea2dfa | -7.99509 | -44.82288 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9025b08-fa48-39fd-b5c8-93865b8d3b9b | -8.6062 | -46.34805 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f135e79-9c18-3034-9a66-633d54e7faea | -7.50791 | -44.36909 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d71a8824-e0c6-3578-bd5d-f18f7a3b3608 | -7.22751 | -43.85039 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 684a631f-376c-3a42-b6af-98e44eef7393 | -8.20328 | -45.53719 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3598478-3abb-342c-89f6-49d58e24e457 | -7.96955 | -45.63876 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1352d46-4b8f-3d2b-b641-5fc4e9262626 | -8.13449 | -43.65508 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02509324-72f7-3f26-8021-b82af9694265 | -7.39607 | -49.99449 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c190effe-10f6-3fff-b7c9-ea0a40548204 | -9.04588 | -45.71884 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61e7e19d-5347-308e-bec2-d6d90375ad96 | -8.6265 | -45.72658 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5b94de8-edb1-3015-846c-689e801c4974 | -5.95718 | -42.79879 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b2b527a-ac41-375a-8aeb-024fc5ab3740 | -6.43031 | -42.63898 | 2025-09-15 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60f2e327-db72-3973-bf8a-811e28b6d0f6 | -8.97552 | -45.82177 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 056d56d7-84a0-3de0-9790-c47ce5c44af9 | -6.17121 | -41.19715 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b794d903-c1c4-395b-a06e-68f660cd9aa2 | -7.84691 | -46.11371 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6162129-fd1c-35b9-994e-e2be91eccc98 | -8.78695 | -46.045 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c9e8a0c-eed7-3d04-9060-f7237474d462 | -5.39076 | -42.83356 | 2025-09-15 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3d76c461-d64c-34b5-bffd-a0b231884569 | -7.73631 | -45.30657 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6881e4f0-cb0c-34b4-b9c0-8178e7361f66 | -6.4865 | -42.00264 | 2025-09-15 04:19:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb4fd6a1-cba0-3f3e-b13b-53e10401e700 | -8.96505 | -45.78084 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c89c8d2-f9ca-356d-bf20-85fd860e94dc | -7.69571 | -48.86701 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5454a13-63ef-3b19-a5b6-d47dce113e84 | -7.84809 | -43.85847 | 2025-09-15 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5725f6f9-fd68-363a-92e3-4371dd23e6d3 | -5.64713 | -42.60006 | 2025-09-15 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c7c53317-b81c-39c8-93f5-5a3fc83903f2 | -5.9364 | -43.22855 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| adef9b08-f7bf-3e08-aacc-4303053a9df4 | -7.5456 | -44.01568 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9338bd25-01d8-36ff-88f7-1d62ec5f9694 | -9.23558 | -45.66066 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c37a6d5f-cb84-3dcc-a9eb-0bea959e3c74 | -8.95735 | -45.80817 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b2ff9b4-c4ee-3f73-b765-ba0fde19aa38 | -8.99201 | -45.76017 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a2356c2-821a-3624-b2cb-3ae4afc71b70 | -4.2241 | -50.15527 | 2025-09-15 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8192ec9b-cf49-3381-8f13-8f8e62ef236e | -8.20205 | -47.1213 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 586f859d-55c3-3ff2-a3d0-2b06fc05b20a | -7.73246 | -45.30951 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04f4a1b8-a13d-3fb6-9411-0f39d776dad8 | -6.31071 | -44.56732 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40ed00eb-f008-3018-9361-6c73beb8dc42 | -8.90087 | -46.1644 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
