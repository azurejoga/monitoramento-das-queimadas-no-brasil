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

## Dados Diários - Página 238

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e03419a-4650-3b5a-9c92-be19a9ee40a2 | -6.88527 | -43.70204 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 639d3c49-e1b2-3cce-9cfe-56d5205404d3 | -8.74124 | -38.28555 | 2026-10-08 15:41:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 93f6c869-b200-3221-ac31-29d8001c430d | -5.99206 | -42.71085 | 2026-10-08 15:41:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 082b0abc-9c79-37e6-81ec-66628c6482fe | -5.77501 | -42.06576 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e5056e26-8eb1-335d-b57e-96c08915572d | -5.73131 | -41.77841 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f157f5cd-45c5-3bdc-8823-6d5ea7faeb32 | -5.77754 | -42.06138 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 169ccea0-a42b-3309-b4f5-92c4354c330a | -8.07549 | -45.62134 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 03d51913-4ef5-32b5-97bd-2b2514c5a59f | -7.53508 | -42.08577 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 76cd25ca-f9ef-317d-a14a-fa819ce8c614 | -9.89172 | -44.85926 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 275.5 |
| c512410b-5a59-3bae-a538-b59483354a34 | -6.59642 | -44.85955 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9c0c0b20-23f0-39ed-913d-2e3956a614f6 | -6.84512 | -41.74193 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e3757b98-4df7-3c14-8559-348deec1959b | -5.51314 | -37.49109 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 173bddf8-0d7b-3db4-a237-ab09a59273d0 | -7.21954 | -44.15419 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90bb5bdc-9278-3a86-9719-1846b4864252 | -7.47233 | -42.83823 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 76af0ea9-0f82-35bc-9428-1844d1d17614 | -6.67235 | -45.36155 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 4ede0189-1ddc-35d4-a970-6aa549e5a673 | -6.37236 | -42.90022 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d5b76742-f242-32c5-8fcc-97fd1b603fa9 | -5.96474 | -43.90422 | 2026-10-08 15:41:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| edc4c169-4749-3a21-923a-80fef413ecbc | -11.22281 | -45.24649 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 45ddb847-98a8-3b1a-ba4f-e0891a75a661 | -6.69599 | -45.28705 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5ce0f3a8-4874-3b2f-bb5a-6262adba725f | -5.4362 | -45.68056 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| db6f975a-495b-305a-b80e-290a88accd6f | -9.91017 | -44.79406 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0dcb31a2-aaef-31cd-a59a-2f87a0f807e1 | -5.28992 | -42.73957 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| a6df8a67-26ad-3d7b-87fc-1d742893c3b4 | -10.37604 | -46.31447 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1b1e133a-117d-3400-8abb-5846f54a894e | -7.14495 | -45.01338 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bcfa61cb-53be-320b-8df9-38a1dd6d4904 | -6.9925 | -40.03503 | 2026-10-08 15:41:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 25f69a1c-130f-3a79-8a62-868327cbe850 | -5.53309 | -44.29128 | 2026-10-08 15:41:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4637e9d9-08ae-30d2-a8bf-a98b1aad3d96 | -5.10724 | -43.15924 | 2026-10-08 15:41:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1b4a5635-0af1-39b8-b84d-d2fa78d14fab | -5.33362 | -35.5588 | 2026-10-08 15:41:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 8644418d-7835-3102-94f0-1128a7bcbcc5 | -6.22369 | -44.98003 | 2026-10-08 15:41:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c5bf39c5-bdd5-321f-9bfd-be160a8c8ce0 | -10.03525 | -45.59856 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e00f30c7-86d7-38bb-af56-8029d905827c | -6.45585 | -46.02247 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| be65dcdb-d165-3e1b-8cae-f7ab8f52a67c | -11.08028 | -44.01142 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 267d92ae-aee1-3cb5-8078-1f18bb9d1d41 | -7.30868 | -43.98013 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6becf9a-359d-317a-b0b0-26719e3a33c6 | -5.30352 | -45.728 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 91329b38-0549-3ff9-9d0d-b637a24adb04 | -9.76393 | -44.78874 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 53d21021-05eb-3a31-9988-ac20bf16e74e | -6.36587 | -42.57526 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8d1898ca-40df-3f94-9d43-3edbb2b46ed7 | -5.74792 | -42.07475 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| d5c0688d-8e10-368d-95a9-907623a5df50 | -5.48631 | -43.96125 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ff1207bc-6f86-3b85-9fbc-907cfb286769 | -10.89873 | -45.54387 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 43f6a8c3-e87f-3263-b688-a3609c3d8f0f | -4.27408 | -38.68996 | 2026-10-08 15:41:00 | NOAA-21 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7737be0-9977-39cc-9ebb-be9a6d06ae51 | -5.72332 | -41.65196 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| c946c74a-4bc9-391e-9764-2c587734715b | -9.43232 | -41.742 | 2026-10-08 15:41:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 879ecabe-ae91-3cd1-a3fd-8e7cbd9abb07 | -5.99568 | -43.61885 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8c26925-880d-30da-8929-926b06d893ab | -5.74841 | -41.64883 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e7a691b9-1685-3499-809f-98a90ebe8644 | -6.36181 | -42.90501 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c8a77c2b-79f1-3cb8-ba75-6c5e22a0f1c6 | -9.67295 | -42.73478 | 2026-10-08 15:41:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5aff5d19-679f-345a-8e80-0d1b2671ed12 | -6.53751 | -45.39304 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| caab45b2-d06f-3771-93ae-0bfe31c84dc9 | -5.71318 | -41.72419 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a737a885-697b-3d7e-96b1-45ed1a3194ed | -11.08206 | -44.02655 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 5b190f56-7ece-3485-9788-49dbc38b3092 | -6.15588 | -39.43795 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 56c741de-5bf0-34aa-b39b-97a80e1e99e8 | -9.44475 | -44.60726 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d7b0f99a-52ac-341e-99aa-32728fdb0b37 | -6.05896 | -42.91417 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b1b745f2-e14b-32f2-8e96-a9b027ef0449 | -7.69593 | -45.44484 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f469acb1-6884-3bf4-a597-0e839164e4ae | -7.16384 | -41.99283 | 2026-10-08 15:41:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 21f4c2f1-42e1-3849-9cd3-69a867f53f20 | -5.70312 | -41.72557 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| bd96691e-83b0-3deb-abce-3116905b2995 | -6.80984 | -44.18427 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95309acc-b5c3-3928-bdb8-a7b9879928c4 | -8.94125 | -45.13636 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 308d60b4-8391-3565-82b6-a10047863ad1 | -5.88596 | -43.45721 | 2026-10-08 15:41:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 36ac3e0c-83af-35c8-9f74-5e83c099fe51 | -5.95771 | -40.94409 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 97b94cb2-be77-37a3-acb2-c41bf7257955 | -6.89807 | -44.92128 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e433f75a-66b7-3d3e-96e8-84c8e843e287 | -5.96032 | -40.92785 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.2 |
| abc84f29-ef7c-33b2-93db-0d097a9ec5aa | -8.55238 | -35.10426 | 2026-10-08 15:41:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5fc9f7d1-2828-3519-8861-11947040455d | -7.74284 | -45.44527 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 02d4d27d-edfe-33a5-b2f9-552a8157165c | -11.25911 | -45.18364 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4e64f04a-c52e-38e1-b800-f3c8997d5e06 | -5.36208 | -42.84148 | 2026-10-08 15:41:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b54ee286-efd0-3e9f-9352-f9b96f0ec2c0 | -6.97474 | -45.13568 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 32d4e1c5-0d28-3f94-acf0-28215761be3e | -7.18595 | -44.3189 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fcb1cb9-aab1-393a-aa3d-134f76a37adf | -8.59549 | -44.86744 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 00b4490f-ead9-3b64-b115-9579acb2f7f6 | -10.03435 | -45.60147 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 14d7819b-942c-3778-aa3d-e02d1153cb14 | -8.58978 | -44.87385 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6d78519e-8191-3c5c-bbb0-289753701a32 | -5.37713 | -44.65254 | 2026-10-08 15:41:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d2a13f6-ffbc-3edb-b40f-b4570e58d4a7 | -5.71111 | -41.67458 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ca24c839-5f77-3aee-8334-d16d2a026af4 | -8.20935 | -46.41711 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8b761031-1cf1-38b4-b652-1e29235bb6be | -7.00182 | -44.05253 | 2026-10-08 15:41:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 27187451-3be0-35a5-b930-1b63db46555e | -8.63649 | -41.04879 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9dd0f3cd-f902-3f0b-893a-c37113e2bb04 | -8.94264 | -45.14728 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 1b136712-4828-3170-9643-e643116995f1 | -9.50935 | -45.62006 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5556b605-09c1-3c54-92aa-75913d9b6912 | -5.48477 | -44.60663 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 628f6b4a-67ff-3eca-89ce-b0edc94e56d3 | -8.889 | -45.6138 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8d625bc0-6b5f-3980-aef8-eb72b8c85736 | -5.74056 | -42.05994 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 7d285631-2998-31cd-91c3-f36ce2fd069a | -9.89852 | -44.80704 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| f227a4be-e27e-3e8e-b8ca-01d483a0b712 | -8.95229 | -45.1262 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 5826ea71-85bc-37a2-aa58-856ca151b248 | -6.35949 | -42.56893 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 6671bcf5-d53a-34a5-82fa-a2ea7bda96fc | -7.10222 | -41.74634 | 2026-10-08 15:41:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d2cee31c-1071-340b-8c1d-03591190b318 | -5.52219 | -45.57693 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe82217f-f3d3-3950-86a9-64da34980730 | -9.89239 | -44.86464 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 1c564a16-c94a-3300-b68a-9f8ab5ebb50b | -6.97269 | -45.12008 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f53628ce-745f-307d-9b26-ddf5727bbba3 | -7.73877 | -40.56701 | 2026-10-08 15:41:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 9b59aabf-c9e5-33dc-983f-48c7b3fbede2 | -7.31437 | -44.00145 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dea73817-b237-30cf-857b-0d9adb1b1e3f | -9.10533 | -45.1302 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| e2cc58e1-a5e9-3971-b39f-a94bada342d5 | -10.37527 | -46.30767 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 40ac97c7-cb96-3615-bd61-87418fc14acd | -6.6657 | -45.35583 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 615961e3-bc85-3fec-876a-6335412cdd67 | -5.87764 | -45.95994 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a5f28f53-44aa-335c-bcbf-603d0b91968a | -7.851 | -45.15048 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fcba6c78-fffe-3ede-93e3-4a87bcfb2681 | -6.84194 | -39.55762 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 11e36cd3-7fe3-3846-ba45-c1e1b46142c4 | -10.2513 | -37.85894 | 2026-10-08 15:41:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 44e9e5c9-5699-309f-adc8-1311c3e85690 | -5.87282 | -45.95754 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 61cb8a98-66a7-35bf-a78d-18d28ab3a402 | -5.7651 | -42.07011 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f08901a6-38f2-37c6-926f-22683708498f | -5.98665 | -42.71151 | 2026-10-08 15:41:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| c4d8d7db-2ec3-3fa9-a58a-f0199d196cd8 | -7.75204 | -43.81222 | 2026-10-08 15:41:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |


[Clique aqui para ver as próximas entradas](README239.md)
