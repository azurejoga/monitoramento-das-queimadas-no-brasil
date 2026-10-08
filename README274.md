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

## Dados Diários - Página 274

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d4d15cf-f488-3d8c-8470-ea985b782126 | -11.00896 | -47.97143 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 44e066a6-f686-3471-a030-5c150c2e37c2 | -11.75595 | -44.93151 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 87174fcd-533b-344e-8517-5455804953f5 | -8.60117 | -45.62791 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4db3ceb8-f22a-3986-a872-c93685f3df18 | -11.63472 | -43.59443 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 9173d76e-c0c8-3215-9614-6c731d437932 | -8.5312 | -46.90805 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67ab5214-997a-360f-ab3d-f6405710cf44 | -10.9103 | -45.53335 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.3 |
| cecca1ed-9799-3443-8420-8711b700cbae | -13.36185 | -43.87631 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| abd262fb-4e15-36c4-9eb7-53a2bffc8874 | -11.58509 | -43.67489 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 516beb1a-3462-315d-835b-1a9d7a48875b | -11.96609 | -47.77056 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d56ce960-ea16-3d39-b2cc-6dd41d34cebc | -12.70912 | -45.82442 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c206aee4-f252-38b2-8e05-2a89d69a2ed1 | -9.75663 | -44.79475 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 17aec0b4-a771-3074-865b-0684c8423538 | -8.94564 | -45.13145 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ab15dff0-56fb-35c3-b57f-9acf13e51129 | -9.35287 | -46.57991 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a9a6040c-dd8c-38c7-9e29-be5556a6bb61 | -11.61586 | -43.62024 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b68121e4-6579-3d76-b59e-688702d50e63 | -12.24731 | -44.74129 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 85ea21ca-ebfc-335a-a00c-5d1296a9a083 | -13.69302 | -48.63874 | 2026-10-08 16:18:00 | NPP-375 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cac2c48d-0e36-3260-9323-bf40add65c4f | -8.29436 | -45.7364 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b0e44d37-a86c-3617-aa26-3781b513877a | -13.35797 | -47.27022 | 2026-10-08 16:18:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 451359a5-67be-3d16-977e-1089fdcbb065 | -9.88359 | -44.86938 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 173.5 |
| c2979a29-7b3a-3466-ae75-0732b342d9ea | -10.44373 | -46.8466 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 623e9447-8c24-318b-954e-81569b52f1a6 | -12.14274 | -43.31402 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 97a66986-cfb3-364d-be73-f689e234abf2 | -8.5588 | -40.28365 | 2026-10-08 16:18:00 | NPP-375 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 25.9 |
| a3c5fdd8-f4a3-3a12-bc6f-f74c14b9a656 | -9.76531 | -44.7901 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cb6900db-075d-3b84-96e4-e3a75c977326 | -10.52039 | -47.31198 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b4bb2f8d-f398-31cc-88ad-c2a15bd00aad | -11.38716 | -47.73546 | 2026-10-08 16:18:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8167c3f9-9931-34af-9abd-a8e602a83728 | -11.764 | -45.48695 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 48d7175a-04c5-36f5-88a9-bb66ce81e65b | -12.02485 | -43.44 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 7d02d961-6c29-3cc5-85d9-486abdfa3bcd | -11.62987 | -43.69141 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8c8b1050-5778-3fbd-a83d-8d004fd8e56d | -13.13136 | -46.3288 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e1ee14d-58a3-3145-8d3d-5e017ab5135f | -12.62123 | -44.54813 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b37b7bf4-294d-39d6-8f75-34b9166bdfea | -11.08868 | -47.6292 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ceac7ff3-0cfe-3357-a1c2-2e8f282419cc | -11.20718 | -49.42076 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6f6b8370-b28a-3cc9-8040-2d2cd1c4ae7f | -14.05995 | -43.82416 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8ceee036-1808-3dc9-88f3-ba26257ebbf1 | -9.93988 | -43.57278 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| b27bc4a8-ff1b-3901-92ac-733fa8f9da6f | -11.63934 | -43.69835 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7fc2e38a-903f-3857-822f-b6fa7fd6696d | -8.8945 | -45.38828 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b9e6ce91-d6c1-3fbc-92d1-314f8802773e | -11.00848 | -47.9676 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85ac608d-9cf7-33c3-9ff6-abc4ac39bd3f | -13.99103 | -46.35864 | 2026-10-08 16:18:00 | NPP-375 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa89c228-697f-38dd-8930-b2f30c0e9e35 | -13.68706 | -48.63969 | 2026-10-08 16:18:00 | NPP-375 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff63fcad-d0ba-370c-b841-f721367673b8 | -13.95587 | -44.85067 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 421e27c6-5529-32ff-8033-ff7939fa5a98 | -11.77315 | -47.74207 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c49eb36-4fbf-3a97-b22c-e9c2e9daa7d7 | -11.38689 | -47.55688 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e350d038-a690-3d86-a461-509c8d8f3665 | -11.35788 | -46.69821 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 649084dc-68fe-3bb0-af86-491b02d85d3f | -10.50133 | -47.28671 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f8180cf3-38b1-36b7-a5ee-b5ada3309afe | -11.63766 | -43.59414 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 86ec48e0-609a-3990-9334-3a57816c40bf | -8.97671 | -47.55784 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7af05ae-9c9d-357d-903a-af17264e180d | -9.94247 | -43.56156 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| c74cc606-4dd9-321d-bc94-5b7f2e1f3324 | -11.62932 | -43.68743 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 54f01ca5-a7f9-361f-85ba-2578141e7518 | -8.96457 | -47.54628 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9330764d-ac77-39a1-9c3e-b25b23e73cca | -10.5112 | -47.32137 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 58cf0e15-71bb-3911-af54-2216c27fafd8 | -11.09783 | -47.51445 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc320544-e4d1-34bf-ab78-6ce9e6324293 | -8.96137 | -45.14682 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 16a1713b-4160-3147-8a5b-9016116c49a0 | -12.13984 | -43.31462 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 167d31b1-df48-3f18-9cf7-67f9a0a8ce6f | -11.74807 | -43.64864 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b1198254-5e51-3e5b-bb86-6f44de89924c | -11.63351 | -43.59468 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e74f5145-14e3-3fc2-a54c-17eb5303d9e3 | -12.18695 | -38.27365 | 2026-10-08 16:18:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fdf3492d-7c7c-367b-9dd0-b8c61c220165 | -12.84545 | -44.62405 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3ada7488-b69b-3f46-a1e8-46354692d3d7 | -10.97434 | -48.00999 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4398a542-ff22-34de-ae4c-2501dc8b2686 | -9.53653 | -45.62366 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 0f628325-6148-3beb-ac69-87551027a62b | -9.36535 | -45.93568 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dd272004-750c-30dc-ba76-a7d7019fee26 | -9.23413 | -45.66565 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0738ff0f-f1e7-3a75-96f8-8e9cd0557d96 | -8.96714 | -47.56255 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 019f9b68-504e-3abc-85eb-6b09fa2940e6 | -13.74377 | -41.10751 | 2026-10-08 16:18:00 | NPP-375 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8a540db9-b41f-37b2-9f42-ecb610040a57 | -12.21921 | -44.74345 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| b9318b5d-1d50-36ca-9407-5059cbcbcaf4 | -10.5208 | -47.31527 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| f48a57e4-d4d5-3c9e-baee-855d0d025ee3 | -11.75407 | -43.42927 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f90d8206-4bd6-3622-ac97-f51bd135118f | -11.35124 | -46.72788 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 90247d08-6908-3a39-93f0-e31ab4b13b24 | -9.81435 | -45.69135 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e0138627-f0f5-3678-b8b3-87af41eb8ca9 | -12.22736 | -43.92853 | 2026-10-08 16:18:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 5c4f2253-6e04-334e-9dd0-e23f315f97c3 | -8.98781 | -45.90908 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 04f902ba-7310-33a3-b394-1f2909642b0d | -8.61581 | -44.87958 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| a94c208d-b94b-30df-bde6-6880ba683e9e | -10.866 | -45.55933 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| b2085b3d-b33f-3a27-9567-f48becb76b7c | -10.52086 | -47.31337 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0e645beb-7ac3-3caf-b9a5-803ce1aed1e6 | -12.15527 | -44.74721 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8e27eb94-a86f-3976-b679-ebff9b8832b2 | -8.29374 | -45.7296 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 46e6fae9-2086-3259-a93e-5118d45ded33 | -12.13574 | -43.31519 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 79928da7-5324-3224-8cfd-1e8757a74a13 | -9.36102 | -46.57951 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 39a9a5f6-d0bc-3154-882d-2d1aa33e9947 | -9.91751 | -44.79542 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 75144ced-e3cf-39c1-9e7b-cce074ad9f7e | -11.58407 | -43.66729 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 465f3e39-ebd2-3e83-99ef-7bfdc64e71e9 | -13.02031 | -47.20479 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37cf858b-07d2-3d97-b462-f65a66b26e18 | -11.35046 | -46.72169 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e0a03671-1d5d-37d8-970a-a4a3876391fc | -12.23825 | -44.7425 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b6dec2f4-5e18-3b49-938d-b0d440849948 | -8.97588 | -47.55141 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63706f56-13aa-3ea0-aca6-cae9f62b1128 | -7.80743 | -40.12646 | 2026-10-08 16:18:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2536262c-b56d-389f-8a74-adc459c59172 | -8.40562 | -46.95411 | 2026-10-08 16:18:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce4c33ae-8eaa-3da1-8334-bf9b0810a9db | -10.44341 | -46.8837 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 49e6a9f6-1e57-35cc-9c98-ab17891b1983 | -10.74603 | -48.54617 | 2026-10-08 16:18:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab1c8200-0511-38cf-911d-f9e711509834 | -11.77403 | -45.56312 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4266c0cf-19c3-3cc2-b907-03a785853c41 | -14.58264 | -47.53484 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0c4f955f-54cf-36e4-b926-0eae5fe431f6 | -9.51803 | -46.84079 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 70557423-3947-3ea0-b796-e9c36784b90c | -11.40653 | -47.56686 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 36686d71-4891-3fd4-ae10-20f6fcaa4ce0 | -11.3867 | -47.73179 | 2026-10-08 16:18:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f83fb0f-e3f9-3ce6-9aa3-a06ade2bfa03 | -11.85451 | -47.39814 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 53534a71-5f4b-3f9b-85c2-9ad747a1b9b1 | -9.90055 | -44.80233 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3c85d6f9-cf74-3008-8572-a1c3d573d542 | -11.85283 | -47.38442 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c8cd3642-9af5-3e07-bed8-b6e4c365cac6 | -11.31013 | -44.82992 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| eed33916-b0ac-3899-90e8-169558a49692 | -9.01232 | -45.12965 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| aba1b7d8-6ee7-3166-80ac-75423e5be0a3 | -14.00366 | -48.75819 | 2026-10-08 16:18:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 440d88c1-f768-3a55-b7a2-5dbdfbf39812 | -11.79594 | -43.58393 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d31cf48-3a38-3046-b1bc-01b961e83001 | -12.22268 | -44.70087 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README275.md)
