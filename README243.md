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

## Dados Diários - Página 243

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2fef50c-4c89-3b08-ad18-cf14f361bfe8 | -6.92464 | -45.26322 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 33b2d718-7f52-3913-a459-8f24fac06471 | -6.59336 | -41.54676 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 37d84eff-a776-37c5-8842-a24d37563af8 | -9.97692 | -43.50467 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 687962b4-9dc1-3096-b66d-1a0e6524b523 | -6.57613 | -41.60874 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 09506f02-70b5-3cf3-b783-53cbd098069a | -5.38114 | -44.18362 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 28b2928b-a3b8-3a86-9981-4baa29ae2594 | -5.71991 | -41.73523 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| adf48298-cc58-3574-95b7-40b1a36b2b00 | -5.91275 | -35.37751 | 2026-10-08 15:41:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 049c0c08-deb2-3e28-8dcf-9b620222f329 | -6.89105 | -45.90711 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a49e3173-3cc0-3c88-ae74-bc879256596e | -7.48281 | -42.8274 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0bb58253-ebf2-385d-b5e9-dd0909f69435 | -7.4884 | -42.82683 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 078a6577-7a6a-3993-a70a-051ec1503ecf | -10.61016 | -46.27192 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 808e88c0-5ac6-38a7-a23d-7f21aee8d2e0 | -7.08832 | -41.50523 | 2026-10-08 15:41:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1c21e1c6-47f6-379a-b3d2-cfed577d72bd | -11.27467 | -45.20042 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 11e8e568-fea2-3416-8a2f-a17756ef72dc | -5.76294 | -42.06947 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 71a48445-0927-3bf2-afcc-f13803699c2f | -4.74962 | -40.92666 | 2026-10-08 15:41:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 68338fd5-bc87-362c-836b-7e09195a3ddd | -8.95134 | -45.16323 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0d265d73-5fb6-379e-8bac-ee2fb176bf93 | -5.10212 | -38.10052 | 2026-10-08 15:41:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2317c64b-edd9-3c9c-a648-34b4b884597d | -8.67516 | -41.18783 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a5bcfd96-c005-3d8b-af28-3317d513e6a6 | -11.21915 | -44.86053 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bb833810-c801-3a8c-abb6-5112aabb148b | -5.7522 | -41.6395 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 50e3de21-b700-3a85-97d7-aa9b3517792e | -6.93214 | -45.26123 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f51f51ad-1c34-3dcb-bbee-34f0defbc273 | -6.77723 | -38.26927 | 2026-10-08 15:41:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 2d2a1df2-000e-30a9-a55b-e3a6fab99114 | -5.77459 | -42.06266 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 59ece1e1-4215-342b-a769-3bc42f547a7d | -6.93763 | -44.56776 | 2026-10-08 15:41:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| eb1815bc-7459-37c3-9bbf-a66921445d30 | -7.59819 | -42.39167 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 9eb5b6e8-e510-38b7-871b-e4a6cffe1429 | -11.13358 | -46.13116 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 84ab0f81-7d33-381e-b40a-035e6223ff99 | -6.82268 | -39.55005 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 07d43177-899e-3959-96da-1f1c3d2d7007 | -6.03134 | -42.71604 | 2026-10-08 15:41:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7bb46fb4-c296-33f4-891a-aad869791b38 | -6.40685 | -44.95244 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e3d6b801-4e8c-3985-acbc-15795b5b45f7 | -5.37924 | -45.94107 | 2026-10-08 15:41:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76f9eaee-0da5-3105-b730-29c5a1284443 | -5.71636 | -41.63845 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e2b807e2-d0e0-3f01-9fb9-fbd1f52fa78e | -9.91669 | -44.79337 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 71ea0737-0a5a-3080-ad03-a3c2c2dba000 | -5.71279 | -41.7571 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9d50025c-b9e1-3e11-8f8d-dbff8f1ef64e | -8.94636 | -45.13223 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 96cedd7a-48f7-3971-81d9-0b7550893caa | -6.79725 | -45.05548 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 28921822-cd37-3167-8b66-3f721c0dc6e6 | -6.67353 | -45.36545 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| a0eeaa87-404a-3616-a9e5-271a95eb0ee5 | -6.36733 | -42.90435 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9fd166d1-d55f-3905-ac80-024a71db2509 | -9.51163 | -45.62231 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93bb704c-c530-310c-a3bf-ad3048536e7f | -8.88622 | -45.3964 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| c349d37f-f3c6-3482-a659-756f26a896b9 | -6.53856 | -45.39441 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| ccdbd7ce-eeb4-334f-9018-173556b9fd0f | -9.88549 | -44.8643 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 996bec5a-1fa1-39e2-b0ff-a20bf0a5adeb | -10.36443 | -42.48499 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 37afa67b-4c12-36f2-bec7-612f38f7ec86 | -5.33074 | -35.56302 | 2026-10-08 15:41:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 670ec978-8484-3794-9762-96273a4bd5ea | -6.23769 | -43.86129 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 18cd44e1-d8aa-3ea0-90a5-d95b4333ca4d | -9.13664 | -45.84169 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c00d16a0-d4a4-3aee-84b4-b7cfe4be2144 | -6.53824 | -45.39837 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 4a1a2860-082b-38e5-95ce-f53a603a237a | -6.5714 | -41.60578 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9cce3921-58ac-3a25-a38e-0953a5d9ab35 | -5.36993 | -45.72696 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0e4cae63-0296-32fd-86e5-f381c3c15ff0 | -7.03602 | -45.45182 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1f42db03-12af-3a5f-8427-4acd8fda8118 | -5.45357 | -42.90292 | 2026-10-08 15:41:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 4a93bd73-1996-3496-99ac-a34396e19003 | -6.83858 | -39.56583 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1e98c2d2-d6d9-330b-ab43-dfde8dc4a245 | -8.93677 | -45.15363 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 37db04e5-51ff-3bef-a1fe-76c87480d269 | -9.90061 | -45.20019 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 253d58fe-d564-3bb2-8c5e-4527ef457c45 | -11.01188 | -45.42727 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d8dc6d92-fdd3-3173-8ca5-6b9604ab9767 | -8.96675 | -45.13557 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| eb7b7ead-19d7-3b31-ac9a-280f99d668d7 | -9.42097 | -45.81611 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8da62dd0-11aa-3278-bfcd-997ee94cac37 | -6.12256 | -44.14679 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0b38a4d-734a-3fcf-8b05-3a2f3efebe43 | -7.08183 | -35.03964 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c651513d-b76d-30e2-883a-905d3f024278 | -8.94477 | -45.16404 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fb133f13-5ab8-3cda-a7c5-d740579744aa | -6.32215 | -35.13816 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| d44f5af6-e433-3f6e-b302-de45245595fe | -6.31583 | -43.34948 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9d0bdd22-e043-3f24-adc0-c217226aa746 | -8.94702 | -45.13768 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ab534e59-c5c4-3687-8983-10ce7a3a4bc4 | -6.95287 | -45.27779 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6ad185bf-3022-363f-9e99-58396b03ffe5 | -11.09348 | -44.01512 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f127b299-3f15-3fac-a8fa-bd7c90e53ed5 | -8.94991 | -45.152 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f5688bea-1fc5-3eda-ac94-2545219e7bef | -6.0159 | -42.26015 | 2026-10-08 15:41:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8f0115bd-b37c-3e2e-bcce-96606af20cb4 | -5.70479 | -41.73717 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 5338da3d-da7f-3e18-8f23-7099962cb930 | -8.36654 | -44.76764 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 200baa38-34c8-3539-b942-aedf46be141d | -5.75823 | -42.0733 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 49fcec69-b9a7-3cc6-a9ef-79216a884865 | -6.64531 | -43.76522 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a261188-af81-3b3c-8bed-4e5023ded433 | -10.34169 | -46.23653 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 0dabf54f-9a27-3444-8795-02407381d1e5 | -5.7821 | -45.38571 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d1951fce-05ad-31ef-97b1-cb4bd7edfce6 | -11.27532 | -45.20628 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4c053352-788b-3c3d-919a-291cdcb36779 | -6.86021 | -39.15631 | 2026-10-08 15:41:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 25.8 |
| afaf3d71-e6c6-31a5-adac-6ae642f0cb08 | -8.19896 | -46.39079 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 23ffcd4d-3ba9-3425-a9c6-0e337f4b4adb | -5.94865 | -45.69197 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| df059517-52e4-3851-b1a6-a9625e73c59b | -7.25021 | -43.5051 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c859b34b-7928-3e64-a258-435171ef2258 | -4.74821 | -40.50451 | 2026-10-08 15:41:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| fd84051a-b3d6-3dbb-9e6b-162bc0f8d393 | -6.32821 | -43.35565 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8124946a-6b30-37b0-95b4-9ad3e28aeb4e | -6.97777 | -43.29161 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a97ed748-08bd-3290-9d25-17fdba8d2583 | -6.81508 | -38.53603 | 2026-10-08 15:41:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0abd8a80-c641-3a6e-b571-be1a36e5a4c2 | -6.60018 | -37.8984 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 216.4 |
| 686b018a-5235-312e-a45a-2da211db1621 | -10.25257 | -37.85849 | 2026-10-08 15:41:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b21dc7fa-6f71-3abd-9bec-796154659bdf | -5.37581 | -44.18848 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ab78749f-757c-3767-ac1b-fe1cba1a3e92 | -9.36607 | -45.94361 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| ea208da2-cc3e-3666-a65b-009cbfd22b8a | -9.89716 | -44.79565 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| b9684bfe-67a8-30da-9ac5-37f5b47b8bea | -11.11175 | -45.69575 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b0647384-4fd2-3a5c-8a8e-54e1b6cbe59e | -8.96543 | -45.12466 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cac859f9-13ac-3f68-b02a-7857b8c73719 | -6.15672 | -39.42855 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ac9df543-1388-3544-a4d2-18757ae09fb4 | -8.94405 | -45.1584 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b0405bd0-8111-38a7-ac09-2f9d61596a08 | -5.71444 | -41.73292 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| cca652d4-b7a3-3222-9a23-4e68fc8b4a6a | -5.46916 | -41.22652 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| bf2abede-c1b8-3d11-8e36-c31c179430db | -6.67216 | -45.35499 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| c72b72d5-5c2e-3c9a-b2ba-6f0ec305e5be | -7.31156 | -44.00134 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ea484666-66da-3f6b-b6d4-c4c7e760c9f5 | -6.84553 | -41.74496 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| f186df3a-9a97-3331-96e0-60b59bec9ce1 | -5.48285 | -44.60169 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b2ff6339-b2a4-3b99-a6cc-e61575a9a203 | -6.33335 | -43.35099 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f74b12c-9303-38ac-a0e9-f362a754598e | -5.76855 | -42.07191 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1aefeef4-cfbe-31f1-bf3b-f3e4eccc7015 | -6.37019 | -42.52843 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 824c777f-8583-3eaf-afaf-f499571f9d09 | -10.98781 | -45.39795 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README244.md)
