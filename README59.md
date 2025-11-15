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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2d61c4e-8dee-377e-b222-5d0cde48dc42 | -12.80939 | -43.06228 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4ca630d9-8c66-30d2-877d-faf1b6bb442b | -11.91873 | -46.21537 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b9bff6d9-862e-3a93-ac95-364b883b24dd | -7.56654 | -42.57578 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 1c0b4104-d36b-37eb-a91e-46815f68123c | -7.56527 | -42.58473 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 8be1804d-76f9-3e33-900a-2e8136271b8c | -12.15617 | -46.66578 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a2e5b971-9b24-3add-9702-b184315bf09a | -8.22075 | -40.06671 | 2025-11-15 11:59:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e9014f51-6ac9-3ba7-b642-b05a68c400e2 | -8.0698 | -43.1184 | 2025-11-15 11:59:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b3c47ad2-9f5a-3336-8ee8-0427791e5370 | -12.0057 | -43.2718 | 2025-11-15 11:59:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a335570f-7085-3c9d-84a5-ba047bf45cb0 | -7.49601 | -42.55042 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 4c01d795-3406-3376-ba92-6cd54295591e | -7.89604 | -41.60994 | 2025-11-15 11:59:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 15cc5f3b-b631-37c1-8c57-26608bd183ea | -7.43067 | -45.22446 | 2025-11-15 11:59:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bcf69077-d1f6-3768-a386-61ca26cb7bc0 | -9.05561 | -44.79461 | 2025-11-15 11:59:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 24640878-64b2-3e7b-be81-7c5374a28500 | -11.92801 | -46.21649 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 271802fa-ef9a-3047-85c9-af7f9829e455 | -12.66733 | -43.42438 | 2025-11-15 11:59:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ae88e65f-5ab0-3fd5-ab64-dd8bc80955f7 | -8.4414 | -43.86885 | 2025-11-15 11:59:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| db3d2807-5b82-35e3-ac4f-671d9aa42e69 | -11.92025 | -46.20534 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| fcef2811-b3b9-34e1-8bd6-e93d7cc87380 | -15.17303 | -43.62513 | 2025-11-15 11:59:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5b0d937c-2bb3-35ee-ab7b-6f61a51cadd3 | -8.18777 | -45.04049 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 3ad67e57-2e8b-370d-9d57-4207a5b0f8f9 | -7.44136 | -45.21603 | 2025-11-15 11:59:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fa7534ec-3686-333b-92fd-99884cf1f70f | -7.97744 | -38.64381 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 144.7 |
| b64e9618-bb7e-338e-a795-cd20d2b308a4 | -9.05424 | -44.80381 | 2025-11-15 11:59:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 538f4f88-5ee9-3be7-bb96-d7b45798acd1 | -13.08412 | -43.00721 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| aabe9306-8a67-35b9-915a-072a53d70ff1 | -6.78894 | -46.75416 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d32107cc-d446-34a1-b9a2-cf622a3757b6 | -8.19969 | -45.0228 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e6ac8f68-567a-3a4b-ab06-5942d598728f | -15.35164 | -47.8553 | 2025-11-15 11:59:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e32cbd32-ca29-37a3-8b57-91ebf40ed7f5 | -12.84763 | -46.43127 | 2025-11-15 11:59:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d31d5e05-eff2-3725-a6db-a1733fc0ec32 | -11.92647 | -46.22668 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 330.5 |
| 16e721d5-b1b6-3e56-9a79-f682a29f3b0e | -8.16953 | -45.04168 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 77c11fe9-84c4-3090-b4ca-1c3f5d5ba5cd | -12.03188 | -42.82073 | 2025-11-15 11:59:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6aefda70-71ea-3e2b-9e74-22f0444d70b3 | -8.57306 | -46.06247 | 2025-11-15 11:59:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c55f68f8-bc16-347e-a840-81611d0e63fa | -8.17093 | -45.0321 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 439.0 |
| e8785644-dbb5-3474-a22c-b776bb87ae43 | -7.3871 | -43.37399 | 2025-11-15 11:59:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 133b26d9-3242-33a4-8c5c-500f0e3e1fb4 | -14.28071 | -44.53557 | 2025-11-15 11:59:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 67010efe-22d7-32e7-bdbd-8eac8e516321 | -16.24194 | -44.80725 | 2025-11-15 11:59:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4cc53c35-4001-3902-a1b2-64ae912281a7 | -8.66016 | -44.14597 | 2025-11-15 11:59:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f1ad21b-5fcb-3459-933d-acd9d224a91b | -9.35362 | -42.26317 | 2025-11-15 11:59:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a70a9666-f409-3e37-ae14-86d1b71f6487 | -13.86541 | -46.84085 | 2025-11-15 11:59:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 35e54b94-7fea-3021-9685-3cef0ad75c96 | -17.16103 | -43.07708 | 2025-11-15 11:59:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ba130c68-c61a-3a7e-95ae-616f8f7f1a40 | -9.44177 | -44.86681 | 2025-11-15 11:59:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2255386a-1e80-3c7f-ae2e-16618071a64c | -7.29096 | -45.1122 | 2025-11-15 11:59:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2599ab6c-82ac-3aeb-8027-f6702571aee4 | -7.8947 | -41.61954 | 2025-11-15 11:59:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 83c3bff1-8026-34ae-a99b-3ab89536ef4e | -10.53986 | -42.61283 | 2025-11-15 11:59:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 925b7811-249c-3c79-af72-3c82f61f6d0e | -12.00442 | -43.28095 | 2025-11-15 11:59:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f8d7b689-f498-3a21-b96a-e17cdda14c34 | -7.77362 | -41.23325 | 2025-11-15 11:59:00 | TERRA_M-M | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f49ced7a-9f9d-3404-80e7-043a70bfbe5b | -8.32689 | -45.40751 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c7ea16f6-b86c-3214-b897-8994e2bc0896 | -12.93319 | -42.28581 | 2025-11-15 11:59:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6448d5bd-5b2c-34b7-b151-5c84e29e4428 | -10.11239 | -40.89536 | 2025-11-15 11:59:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 0a3a0574-34c3-30ea-8e7d-f9f9a78176fe | -12.74831 | -42.97041 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ab8ac844-1415-32d5-b848-01c4638a1900 | -11.92177 | -46.19527 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f7053d9c-3aff-38ca-b438-36cf7afed08c | -11.32805 | -48.51376 | 2025-11-15 11:59:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4154a5c4-0d71-3d6a-bc6b-86f68b269476 | -12.01333 | -43.2822 | 2025-11-15 11:59:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 26dde1d6-bc38-37bb-9d40-29ca8ce2050e | -7.97932 | -38.62918 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 80e77b6a-d369-35fc-815d-e32077372e58 | -15.3402 | -47.86485 | 2025-11-15 11:59:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 92421f56-5a86-34cc-b527-bac94b7849cd | -14.65436 | -46.57439 | 2025-11-15 11:59:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d4bf103a-dbb9-353b-a9d7-41d5bb1870da | -12.94306 | -41.04172 | 2025-11-15 11:59:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 99d89a09-eda1-3e05-929e-83fd3ab0789f | -7.43991 | -45.22578 | 2025-11-15 11:59:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 4a2e27e8-de00-3299-b3e9-08411c733f56 | -8.68169 | -45.50509 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a93e2525-a7eb-3bd7-98f4-502b28d406fe | -8.67179 | -45.45758 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6ba230c3-362e-3f2e-ba8d-4d5393f1f491 | -15.45063 | -46.31506 | 2025-11-15 11:59:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e5b540b5-51ad-3de4-8e8b-839542734f7c | -8.02023 | -37.77683 | 2025-11-15 11:59:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 16.8 |
| ddd96f47-723a-36d6-8bb9-d63d358c6a95 | -8.35589 | -41.68444 | 2025-11-15 11:59:00 | TERRA_M-M | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 35dac7c9-832a-3fe9-95e5-6ffb1139d686 | -11.92954 | -46.20639 | 2025-11-15 11:59:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a4488864-58c5-3a8e-890b-6e267fb53fa6 | -13.2694 | -42.66246 | 2025-11-15 11:59:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1e19f67a-b7c5-39dc-910d-8377c15402e3 | -9.15733 | -45.16755 | 2025-11-15 11:59:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| eacec9cc-68ef-3a17-bcb0-4dfa0f43e240 | -7.4292 | -45.23425 | 2025-11-15 11:59:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b1cf4232-54aa-3604-8dd6-336f8a91822c | -13.01558 | -43.03632 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 7b3cc6b3-f278-348c-9eb1-6c1a7d999b23 | -12.1656 | -46.66726 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4e6a4b00-bcb9-30de-a628-c712414c88e5 | -15.55378 | -43.33139 | 2025-11-15 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f11a5b88-000a-3b77-80be-3d2f8985da7a | -8.33625 | -46.6931 | 2025-11-15 11:59:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2a1555bf-30c3-3f60-8437-cc8f16ba5806 | -12.92251 | -42.29468 | 2025-11-15 11:59:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 2925eef8-fad5-38c6-bd30-5c29b2a2043b | -8.061 | -43.11716 | 2025-11-15 11:59:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 7fe05438-e975-3563-b453-19405c69b069 | -12.83836 | -46.43 | 2025-11-15 11:59:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 341c9725-a16d-3fc8-87c1-3fa1ea8e9af1 | -8.21019 | -45.01466 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| b14c38a1-d936-3af5-a7a2-4a42e7b3e08b | -8.20878 | -45.02412 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 65d18fa7-0fdf-366f-92c6-ded9e643bb1f | -8.07106 | -43.10956 | 2025-11-15 11:59:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 50fe2b87-aec6-361b-9284-4c5647836f5c | -14.23535 | -43.54478 | 2025-11-15 11:59:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4aba28e0-d148-3e63-ac16-a585aaaab70b | -9.52746 | -40.38013 | 2025-11-15 11:59:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d4e5f5f0-271b-3968-83e3-00e1610b752c | -8.21787 | -45.02542 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cdd77607-f1a2-33bd-93ef-7084d5291de6 | -9.9752 | -44.94479 | 2025-11-15 11:59:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 40c80a9a-0fc2-3328-836a-101029877aaa | -8.45982 | -39.79935 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 842bbbf2-95fe-3eca-9cfb-89c1efa34218 | -8.18141 | -45.02391 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 816f36ec-cf33-31de-967b-b4a7a31d9d9c | -9.00479 | -44.4404 | 2025-11-15 11:59:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bd6fc81f-0f4b-30dc-8cdf-1792dbd27449 | -14.91811 | -46.78675 | 2025-11-15 11:59:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ceafcfb8-29f6-3b6e-9f82-df8ab75f388d | -8.66144 | -44.13711 | 2025-11-15 11:59:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d935de2c-a601-31ab-9c22-87829792e7f6 | -14.38612 | -43.7215 | 2025-11-15 11:59:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 2d002adc-fbf9-35ee-a7b7-f19fb9e189bf | -13.02462 | -43.03756 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| e5a3fbf9-c5f3-37c5-be4e-814eff07103c | -7.61986 | -46.54792 | 2025-11-15 11:59:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| fb672d70-d484-30ac-8a3f-25def2ee0ab4 | -8.17232 | -45.0226 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d42958c3-8b40-3721-ba38-c8c87d06e334 | -8.98182 | -41.15757 | 2025-11-15 11:59:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 16d17455-361b-30d4-b488-680230ee5682 | -8.74117 | -46.52547 | 2025-11-15 11:59:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 602cf5ec-968f-3c63-82f3-e630d9d167ba | -17.20646 | -40.68598 | 2025-11-15 11:59:00 | TERRA_M-M | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 4311ca45-1694-3c66-8843-b4975a26d047 | -8.73378 | -45.66462 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ab37ff5e-ac15-3f3f-b48a-9a40f108e3f8 | -8.2011 | -45.01335 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1ea23482-ed9b-3184-9746-c44920a2edb4 | -8.33451 | -46.70447 | 2025-11-15 11:59:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 748b339c-b2d2-3835-9ea1-67524f1b6649 | -11.93425 | -46.23783 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 14225197-72fa-3f93-919d-36815a586b27 | -11.32587 | -48.52776 | 2025-11-15 11:59:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fbd15c62-f56f-327e-9c20-3570e2eab5d6 | -8.17863 | -45.04296 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 1e66da5c-f284-33d4-a343-ad3f4f606e44 | -13.41885 | -42.23746 | 2025-11-15 11:59:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| dd819041-2e29-32bc-a536-80988266bf77 | -9.93946 | -44.93305 | 2025-11-15 11:59:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bfe78682-528e-3b1f-9963-6c8623d8fc65 | -12.84912 | -46.42136 | 2025-11-15 11:59:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README60.md)
