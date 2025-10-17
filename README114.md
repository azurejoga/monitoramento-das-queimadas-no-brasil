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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8759cd0c-8e15-34bb-9a3d-db77ddefa78a | -10.11407 | -44.56169 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76d3f733-55c6-31b3-b346-bfab2847c139 | -11.586 | -44.05403 | 2025-10-17 05:44:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6419bc74-4a2a-3073-b843-82a1d25a641c | -4.73828 | -44.94467 | 2025-10-17 05:44:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0dce4577-cee9-352e-bd26-a43d23dfe0c9 | -8.45456 | -41.26219 | 2025-10-17 05:44:00 | AQUA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0ae8ecff-58af-3af9-99c3-e5ab12db2487 | -6.43627 | -44.72605 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 53f22f10-da08-3665-ab99-4a400dca03a6 | -12.17175 | -45.06322 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 494cb6c2-5f75-3c5f-a21c-a1384f48f5f0 | -6.69363 | -40.8758 | 2025-10-17 05:44:00 | AQUA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d5fe00bf-9863-3b46-a8b3-cb4ea48af4cd | -7.18194 | -42.3772 | 2025-10-17 05:44:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5122c632-cece-3cab-ac46-ded502f81c52 | -6.20338 | -41.74915 | 2025-10-17 05:44:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 4f43beb3-a688-3f0b-a6ba-a4f76fff30a1 | -10.50628 | -43.44266 | 2025-10-17 05:44:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a0e50c0-a8f6-3b92-b19a-9376c4238554 | -8.45573 | -44.16795 | 2025-10-17 05:44:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ad0e1904-a4c5-30b5-8c3f-9f2600bc5a00 | -9.98991 | -47.00407 | 2025-10-17 05:44:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 34b0ab2a-2f32-38ec-b071-9e659938f271 | -5.85817 | -42.33899 | 2025-10-17 05:44:00 | AQUA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 48ba3206-d3e6-337a-81c9-e6eb6d01698b | -6.37429 | -43.56673 | 2025-10-17 05:44:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 00604ffe-1233-3831-a37b-a8f6f7681f3c | -6.13497 | -44.2835 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cf98d9b4-94fa-3544-ad94-7558e276c752 | -3.23873 | -45.95539 | 2025-10-17 05:44:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 462a9a19-3531-37fc-9a44-b10c68d86276 | -9.08805 | -48.01405 | 2025-10-17 05:44:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 74999f5f-0769-3708-8b30-680f1816c10c | -10.53277 | -49.55877 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| aa41de85-a8c3-3fc9-b753-a9d8cd6f5148 | -10.29517 | -44.0342 | 2025-10-17 05:44:00 | AQUA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 41dd90e7-15ac-3585-b5c7-c1d80ed5d957 | -3.97874 | -42.48431 | 2025-10-17 05:44:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 1a44048f-0195-3e94-a058-3bc522292d30 | -4.40174 | -43.40946 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8daf7cfa-bcda-36d5-81c1-04c4a6e3da8d | -12.16144 | -45.07093 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 912f26f7-4546-35ab-bd18-9e9a3f82d2bb | -5.88979 | -42.80668 | 2025-10-17 05:44:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 150fdf2a-5059-3e90-b2d3-75b02e769dda | -5.98863 | -44.15322 | 2025-10-17 05:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58e3e895-0fbe-3f22-99ba-34bf6529a617 | -5.3388 | -44.46598 | 2025-10-17 05:44:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f187fb92-da4b-3dcb-aa67-d71ec7cd1f8b | -6.05817 | -44.24631 | 2025-10-17 05:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66e9c709-c8fd-3f39-9791-58d386eb3580 | -10.43295 | -45.01122 | 2025-10-17 05:44:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e3d8863b-fb4f-3245-b65c-1cf8eb3d48e0 | -10.29652 | -44.02531 | 2025-10-17 05:44:00 | AQUA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0f8939ea-3ca1-31b3-a7d3-43398938fccc | -8.39997 | -46.22246 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dd6b756d-d0c5-380a-b0e3-9f8b45033f41 | -10.49882 | -43.43245 | 2025-10-17 05:44:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bdab55df-93bc-3cd9-a9aa-8db5ea088c33 | -10.13577 | -44.54377 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 665fe38a-99de-3e7f-9aae-891e0b42cd69 | -10.50015 | -43.42358 | 2025-10-17 05:44:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b81f60ff-7fdc-373a-b9da-4622c472b81e | -11.59692 | -44.06134 | 2025-10-17 05:44:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 153c15a5-048e-39bb-94a8-5fc6b45c78dd | -5.31428 | -42.9446 | 2025-10-17 05:44:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5b87617-4baf-3625-95de-531ff7cb5702 | -6.74957 | -42.36366 | 2025-10-17 05:44:00 | AQUA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 78f40607-fe1d-3f26-9ce4-a2723a31559b | -7.17577 | -42.35817 | 2025-10-17 05:44:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 07f74262-5641-3696-9e34-c0ff2a168183 | -10.28637 | -44.03286 | 2025-10-17 05:44:00 | AQUA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| b44da2b5-0904-38ae-8921-6784ca4d0890 | -8.29561 | -43.39594 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 790a36bf-78e2-31f6-bab0-003c3cf9416b | -11.48383 | -44.19361 | 2025-10-17 05:44:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8314ce3d-5956-3d5c-bd9d-2ff481a7df9a | -4.81235 | -43.20165 | 2025-10-17 05:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 75f6b1a1-ad53-3fab-9ef2-7dcfd0ff8983 | -7.00304 | -46.99039 | 2025-10-17 05:44:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2817a40e-60fd-3d43-993b-77f24147bfaf | -7.90435 | -44.98104 | 2025-10-17 05:44:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6f478dd4-622e-3830-8180-ce31adc1a00b | -7.35428 | -41.90497 | 2025-10-17 05:44:00 | AQUA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| bf6542e3-abd3-3a1f-bcc3-71886ffc899a | -4.40313 | -43.40041 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e1057802-f4e5-3712-b9f4-01cf80ffeadc | -5.89045 | -43.89521 | 2025-10-17 05:44:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 001d2922-1557-3803-befc-6111ad2d931f | -6.32474 | -40.93605 | 2025-10-17 05:44:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9e0979c2-346d-3e27-b8db-132e59130d76 | -3.23487 | -45.98071 | 2025-10-17 05:44:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ebd1bcad-9d65-343c-ad40-c850513ac66c | -8.38652 | -46.23624 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| eb3e0eb7-ddad-3236-a79a-5b608b247032 | -8.25733 | -44.06411 | 2025-10-17 05:44:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36af249e-babf-3187-a88b-2adbb29331c0 | -10.15635 | -44.52841 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 332bf579-4cd8-3d27-abfc-b56065369f5f | -9.71111 | -44.54032 | 2025-10-17 05:44:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2c08f2c-55aa-3588-88b6-6a595bf66753 | -10.11458 | -44.6181 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea22f8f0-3d13-37d0-92b9-0b2d18c104db | -5.33166 | -44.46821 | 2025-10-17 05:44:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c26bc291-d406-368e-89d2-a34027ad23b4 | -7.35548 | -43.85655 | 2025-10-17 05:44:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ea08dcf3-2384-37f0-8c31-f17dd11e6f2b | -5.51345 | -43.87402 | 2025-10-17 05:44:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| efcf54ba-7452-38da-96e5-5a76e114f515 | -6.38362 | -41.47271 | 2025-10-17 05:44:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9088feaa-403b-30f5-939d-afbdceb414f8 | -6.75839 | -42.36492 | 2025-10-17 05:44:00 | AQUA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 421a83c5-6e11-3a37-b2d0-415e406ee4d4 | -8.46324 | -44.17833 | 2025-10-17 05:44:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 83969af7-7d2d-3a42-8e23-b0e582064567 | -8.09269 | -45.43516 | 2025-10-17 05:44:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b6417b5-5052-3445-a18c-9ca323586889 | -5.98262 | -42.80008 | 2025-10-17 05:44:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 1d0b3e5b-7dd0-3a82-97a4-cbf5859abfa5 | -11.40456 | -44.22955 | 2025-10-17 05:44:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d1b7d7ed-78bd-3b6a-b4fa-0d3235a5a304 | -8.38542 | -46.31283 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 83443d5c-9f6d-3b43-a317-50378c234083 | -10.28501 | -44.04179 | 2025-10-17 05:44:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b0b56c52-b974-3061-bca5-cfab8ed44772 | -6.76837 | -42.84955 | 2025-10-17 05:44:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0620231d-4a12-3dde-8b37-e864a921e96e | -5.694 | -42.67886 | 2025-10-17 05:44:00 | AQUA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d5f05516-db4d-33a3-a295-03a6bbe82d28 | -11.97543 | -46.55019 | 2025-10-17 05:44:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4989e36d-c4d2-397e-834f-c9a9f74553bf | -12.10997 | -45.88339 | 2025-10-17 05:44:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3048b892-5618-3e54-9710-6053973d9974 | -5.99007 | -44.14382 | 2025-10-17 05:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d825a22f-9073-330e-9c87-eac41612b8a9 | -11.40864 | -44.20273 | 2025-10-17 05:44:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e56f10b9-7afd-3fc4-bafb-707717d66f86 | -7.45674 | -42.15357 | 2025-10-17 05:44:00 | AQUA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c6b499b9-6133-32ba-b8d1-b0d520289785 | -4.42234 | -43.39404 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| e4fc5882-2f1c-3439-8bba-605b2b114d4b | -2.87518 | -50.71085 | 2025-10-17 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| b60eda5e-8054-3704-b710-e310e835bae4 | -8.41052 | -46.28232 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 589a5098-bcc3-3b02-8b52-4bf61b589126 | -9.97792 | -47.01423 | 2025-10-17 05:44:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d04d872f-1fca-3507-be1a-2eba576bdc20 | -8.55857 | -44.58049 | 2025-10-17 05:44:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d280c9f3-3ab8-3fb0-96ac-c904d61c9443 | -5.29577 | -43.54932 | 2025-10-17 05:44:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 21351c9d-c434-3d2b-b508-f0a34c37dc5d | -6.8345 | -42.4097 | 2025-10-17 05:44:00 | AQUA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2b396bc5-f431-3689-9e71-608c1bbd680f | -6.69505 | -40.86617 | 2025-10-17 05:44:00 | AQUA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1cdcf392-3ff6-33e4-a8d9-ac102bc8ea6b | -6.42419 | -44.03168 | 2025-10-17 05:44:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c6a4fbff-b0cb-3e13-be31-a916eac61b0f | -3.84851 | -41.56873 | 2025-10-17 05:44:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ec8631ab-4e3e-3b03-b99b-20027f6de486 | -3.50821 | -52.49213 | 2025-10-17 05:44:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b628f4cb-98de-35d7-8cd1-86156ede2910 | -5.79695 | -42.49375 | 2025-10-17 05:44:00 | AQUA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4ab89af8-0359-3b56-a717-252cf2d0538e | -5.87401 | -44.83618 | 2025-10-17 05:44:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b6bcfa6-8ac4-344c-bb28-5efb8338e59a | -7.83163 | -44.1324 | 2025-10-17 05:44:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f54888e4-e0d3-3b2f-9feb-b4b5ab765b9d | -8.25393 | -44.02671 | 2025-10-17 05:44:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e619f6c4-0417-3c82-9195-32bf6967309c | -8.38656 | -46.24325 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 37df14c7-9883-3872-9120-d819950d9933 | -8.21646 | -43.97501 | 2025-10-17 05:44:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bba16108-33a0-338e-a461-adf4fe408136 | -5.84658 | -43.87346 | 2025-10-17 05:44:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f10443f-029b-3cd8-bc65-e5858aa35087 | -5.89417 | -43.19439 | 2025-10-17 05:44:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b3da1265-aa18-3a3b-a83c-3c6a84209a31 | -8.45868 | -46.23245 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dd1880b9-e548-384a-83d1-558826799177 | -8.33728 | -46.22945 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 38846cc0-ff56-3467-91ba-e41900050446 | -6.74825 | -42.37249 | 2025-10-17 05:44:00 | AQUA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1e8da5da-0953-3c84-984b-efec75ec5be4 | -10.2586 | -44.03773 | 2025-10-17 05:44:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 334216d7-b6d0-3076-9a89-936a5cd03c71 | -10.65788 | -45.29014 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 175dbb1f-5286-367d-9564-6e0627d403ab | -7.33125 | -44.1463 | 2025-10-17 05:44:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11c7879b-c32b-351f-b610-11144dd8efdc | -5.61364 | -42.67596 | 2025-10-17 05:44:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7eeaaf4a-6909-373b-bc1e-2f108809e5d9 | -6.20473 | -41.74016 | 2025-10-17 05:44:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6d31764f-b659-3f66-b09b-7066ec2d9ae4 | -6.31417 | -40.94426 | 2025-10-17 05:44:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 83e69c8a-1abc-34fc-a37a-298ff66560ed | -6.75092 | -42.35472 | 2025-10-17 05:44:00 | AQUA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d00d6bdb-83d4-3d0b-ad79-942c91417234 | -7.94653 | -44.10892 | 2025-10-17 05:44:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README115.md)
