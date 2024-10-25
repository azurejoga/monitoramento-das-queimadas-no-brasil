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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e8803b4-62eb-38d4-8e80-bcaf47fba553 | -6.96157 | -41.3208 | 2024-10-25 04:14:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64b54a1c-47f6-3782-9f54-f7792e5dbbf3 | -6.47075 | -41.77795 | 2024-10-25 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60820811-8f27-3597-9b9c-9198fea321b6 | -6.46795 | -41.77383 | 2024-10-25 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e3aa02a-7b33-348d-a3e6-0385b234d4ac | -6.4646 | -41.77329 | 2024-10-25 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43551de0-b2e8-3f4c-9a93-0f27a1cbc5c9 | -6.46125 | -41.77276 | 2024-10-25 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7a9984cb-bcc4-37c2-8590-2e765217881b | -9.12029 | -41.18932 | 2024-10-25 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 037407e4-830c-39fd-b59a-d68ec0a5e771 | -8.669 | -40.96766 | 2024-10-25 04:14:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b0d2445a-6f2f-34e9-bdc8-c6865e7b6e05 | -8.66549 | -40.96714 | 2024-10-25 04:14:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7631ebe7-6e36-3b8e-b362-dacb0ad3060f | -8.3885 | -42.26344 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09a3b534-807a-307a-94d3-0af0aa0aee0b | -2.97367 | -42.71384 | 2024-10-25 04:14:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64e2bd17-9ea2-3ec0-a5fb-e7a772a2154a | -2.95163 | -42.70337 | 2024-10-25 04:14:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ec206a8-bb4f-3944-a9a1-3c5b7a8b49fa | -4.02873 | -41.80128 | 2024-10-25 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d04a84ad-d87e-356e-9c9c-cdb251fe8fe3 | -3.85981 | -42.51221 | 2024-10-25 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a9007000-6423-3e46-b298-ab51812cd97b | -4.0722 | -42.89088 | 2024-10-25 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f4a4005-2474-3426-bf95-d61a10caebc3 | -3.79532 | -42.85757 | 2024-10-25 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 257557f9-6db1-3507-8d19-83164f41de76 | -4.92057 | -41.97282 | 2024-10-25 04:14:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5618266-338e-3504-bdd9-e2646c7c2f7c | -4.92003 | -41.9763 | 2024-10-25 04:14:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d691e7d0-730d-36d4-a5f6-1fc0a1e44976 | -5.70673 | -43.14679 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f7eb0e8f-510c-398f-9167-94f89bd7afc7 | -5.70343 | -43.14628 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| be3cdf93-7e1b-3964-b698-a567fc1dec3c | -5.70289 | -43.14972 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6c0016a7-a0ba-3e9f-8a25-abfd52798b3b | -5.69959 | -43.1492 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2468f66d-74ad-3879-8510-a8b280c31a0f | -5.6346 | -42.77929 | 2024-10-25 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be7f0e9f-7bc3-384e-bb31-fc11ff12bf4b | -5.63022 | -42.78565 | 2024-10-25 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1ccd9e95-a0b6-39a5-abcc-134eacdcce4a | -5.53722 | -42.94741 | 2024-10-25 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a28e173a-a82a-324c-8cfd-976e48efc94a | -5.52505 | -42.24191 | 2024-10-25 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 13ba410f-bcff-34f8-9a11-48766331b429 | -5.39434 | -42.6423 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d328e0be-c76d-38ea-bcfd-7ba38cf00c0f | -5.69475 | -42.48515 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 45be8283-85d9-3de6-84cc-3a8a64601a67 | -5.62524 | -42.7743 | 2024-10-25 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d0034903-e2fa-3809-a87a-bdd215ae7a5f | -5.61588 | -42.76932 | 2024-10-25 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 84be0495-a942-39d2-9576-ead49066fc34 | -5.52613 | -42.235 | 2024-10-25 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 31d52d0d-f347-340b-bf40-643c729bc0d6 | -5.62254 | -42.79151 | 2024-10-25 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 105f2243-8b0c-369f-be6f-ae39170118f5 | -5.61924 | -42.79099 | 2024-10-25 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 84af7957-d9f5-35e9-9907-28792533b65c | -5.97425 | -43.21774 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2e74f4c-5a62-3cda-9945-d9b74ed754b3 | -5.52944 | -42.23552 | 2024-10-25 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e269728f-2cd1-3b1c-b071-0f2922cdea6c | -5.5289 | -42.23897 | 2024-10-25 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 174d9c8e-daf1-3162-83f6-4685bcf64aed | -6.32795 | -43.39429 | 2024-10-25 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63988274-ec9f-3b41-8294-4c50f57972fa | -7.80689 | -43.8122 | 2024-10-25 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de7be77a-d74b-3a57-a250-c2b2b4a29a0f | -7.79962 | -43.16571 | 2024-10-25 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 69f1c6ca-dfee-3eed-ba75-7e9f8ae7964b | -7.79632 | -43.16519 | 2024-10-25 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d9149bb7-c861-33a3-869a-2d847a8fbd11 | -7.49808 | -42.91914 | 2024-10-25 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 898489fc-d663-35d3-b1f6-3554f590a45c | -7.49478 | -42.91862 | 2024-10-25 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9dfac6c-9ad7-3709-b2be-a15180c401cc | -7.2735 | -43.63419 | 2024-10-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82bbbd08-02ac-382d-9d3a-77f05730212c | -7.27295 | -43.63765 | 2024-10-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e10e39f6-46ea-3b9a-8543-8919ee4334c3 | -6.97869 | -42.43092 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b4fdcd9-bc7e-34b7-a237-5ed15e94b010 | -6.95396 | -42.48064 | 2024-10-25 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1847cc93-8918-313f-956f-978740342355 | -6.8541 | -42.81706 | 2024-10-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 93f6e9fd-f7eb-3cdf-9e26-d26d7cf831c8 | -7.57194 | -43.44453 | 2024-10-25 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb9eafc8-ccba-390b-b69b-4c71b76dc12d | -6.64091 | -42.52418 | 2024-10-25 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 198b3515-5de0-33a3-8730-61991afd673b | -6.5925 | -42.24558 | 2024-10-25 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 58d0d2dc-b141-3973-8e95-c5a4462eeada | -6.58936 | -42.24451 | 2024-10-25 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e1d6b35f-4c32-3058-ba87-1f074c3cd8ea | -8.3315 | -42.80812 | 2024-10-25 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b77fb2e9-3663-3204-8a7a-0013b2a1ec14 | -8.33095 | -42.81162 | 2024-10-25 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04591431-3ab4-3143-b9b3-c790f5d03080 | -8.30185 | -42.86781 | 2024-10-25 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52dc79fb-7e37-38a0-bef9-3677f033b7f9 | -3.42299 | -43.16692 | 2024-10-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67dc0411-7bf4-32ab-8a14-0db1c30f721e | -3.31032 | -43.5146 | 2024-10-25 04:14:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04ab4742-d68b-38bf-aa9f-a84d03e76cf8 | -4.18238 | -43.33714 | 2024-10-25 04:14:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d383e62-f37b-3894-87ad-4e9edbb68f1c | -3.97967 | -43.15564 | 2024-10-25 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c144645-2c0a-3349-9101-e89a541a682d | -3.97912 | -43.1591 | 2024-10-25 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a9bce91-ad87-3c90-b838-7e69885b255e | -3.80326 | -43.25883 | 2024-10-25 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4d9f969-34ec-3eb7-8521-24c6e381e8b3 | -3.80271 | -43.26231 | 2024-10-25 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dfcf84be-07af-390d-a4e2-0cc4c7265aa4 | -3.79994 | -43.25832 | 2024-10-25 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 010c635e-a237-3d2b-89dd-525d691faea6 | -4.1549 | -44.34934 | 2024-10-25 04:14:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d7ce09f-1f10-305c-be00-f831aa29ce82 | -5.07815 | -43.82681 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 79090560-359b-3737-bc34-566a1be43c85 | -5.0776 | -43.83033 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 81331d77-a911-3ede-9b0b-35dc749d3eab | -5.07426 | -43.8298 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba8d18a5-239c-3ce1-9b7d-93ef4b18f28e | -5.73749 | -44.43074 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6be7782-20c5-336f-adaa-cb2aebd5366c | -5.70871 | -44.65335 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57f98c90-5de3-3613-b94c-e919a5d35ae3 | -5.62342 | -44.83269 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 403c405c-48ae-3bdd-97f7-d3512ccdcf1d | -5.62283 | -44.3797 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d5702b0-b994-33ce-a053-ee196f76603f | -5.62118 | -44.82475 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8653b33-802d-376e-b564-93a735a24540 | -5.62059 | -44.82847 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 471729e5-a892-3765-836e-67cc68a8a2e9 | -5.58901 | -44.42923 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6113dcad-9e01-3536-a992-f92d9d28cfe0 | -5.58564 | -44.42871 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6378216-050d-32e3-a61a-b6b90bf09c51 | -5.58032 | -44.30987 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5cb8382-0748-362e-8e9c-682afeaabafa | -5.5729 | -44.88557 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9f18d3ff-3ae0-3dc9-96f9-7d1aedbece68 | -5.56948 | -44.88504 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 212b092c-e767-3cb8-b03b-b7f2d2bb9f45 | -5.51216 | -44.82609 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bde0ddc8-9bcd-36c1-a02c-88ef858f213e | -5.50874 | -44.82555 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 647743b4-8a5f-3f58-8c89-189797de5ddb | -5.50591 | -44.82129 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e39ff676-11dd-3eb8-bb5b-d2f24a94506c | -5.50532 | -44.82502 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 163f9789-6bce-39a6-874a-629e63c8620c | -5.4297 | -44.79409 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49706a80-908e-3335-9607-f21193f942c1 | -5.34447 | -44.38003 | 2024-10-25 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4cb3dd0-3cdc-3537-bc22-06d599240e1e | -5.28741 | -44.73806 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d733bef-594a-3002-bbcb-8d367dc802f5 | -5.28341 | -44.74121 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ed603e2-6ba9-3582-9f01-63ad8872d2ff | -5.21703 | -44.45241 | 2024-10-25 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 364bf31f-8412-332f-acf1-2fe220c5327d | -5.21645 | -44.45606 | 2024-10-25 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9f4323f-e58f-341b-87b7-3b8693d4df3b | -5.05861 | -44.76285 | 2024-10-25 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eedd46a-ae7c-36c9-9804-7f115ed92fb7 | -5.05801 | -44.76659 | 2024-10-25 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f09d2749-4221-39dd-8928-651de46d33b2 | -6.33516 | -44.80099 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f393ef0-423f-34d8-b12a-4c139bfe3b67 | -6.3201 | -44.76494 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50e5d70e-316a-3548-af7b-f87cb0533234 | -6.29058 | -44.76796 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| debc8be8-bc21-3fbd-9887-4b4924926d45 | -6.29001 | -44.77159 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54bbfd80-f87c-3741-b222-1d6a8fe95ab2 | -6.20217 | -44.86321 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67cdd02e-91da-3c42-91b9-2ec10fccc9bf | -5.82159 | -44.89009 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4492f8a4-6626-31cb-a28d-c7b64b91ec4d | -5.62743 | -44.8295 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 301b5275-eff3-32e2-9a91-e7ccceadd908 | -5.62401 | -44.82899 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 04dbb207-3455-35bb-9979-c0759026a7ac | -5.57633 | -44.88612 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cc6fd93-85e5-34a8-8f48-30f84501f433 | -5.57573 | -44.88987 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68cab006-efb0-3c21-a25b-e05cd4880dfe | -5.50933 | -44.82182 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94c91c17-206a-307c-bf27-80749b813710 | -5.50814 | -44.82928 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
