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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 539ff4e4-42a5-3745-8ef6-7635402fc89e | -3.5575 | -41.6118 | 2025-12-24 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 442edc68-2d7d-3356-9619-d5283bd25ad0 | -3.5573 | -41.6357 | 2025-12-24 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 226735a7-e09c-3dfc-ba08-7946d00dde2b | -3.5409 | -41.622299 | 2025-12-24 00:12:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ec129bb-a4ae-309c-8f91-2abca8896425 | -20.985901 | -48.743301 | 2025-12-24 00:12:00 | METOP-C | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87a20d37-76d3-3afd-940f-3cca01b35d41 | -17.5688 | -46.643299 | 2025-12-24 00:12:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 087f0b7e-7f27-33c4-9a1d-3c2f4515e80f | -4.577 | -38.109402 | 2025-12-24 00:12:00 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7f5b91d3-bcf1-3476-9a99-9b8e41fcc2b8 | -20.044701 | -43.237499 | 2025-12-24 00:12:00 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec3307b3-8889-3e87-ac32-d990b820e216 | -8.0551 | -36.139999 | 2025-12-24 00:12:00 | METOP-C | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 382929b5-22e8-3e1f-92ea-ccc96351a1be | -2.9612 | -39.950401 | 2025-12-24 00:12:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2038ab24-5110-31c6-90e9-b8c7c29ff91e | -4.5789 | -38.117401 | 2025-12-24 00:12:00 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9eaa0564-ba61-3df6-8eb4-c111f0a6821d | -7.2287 | -43.085098 | 2025-12-24 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e64f6f8e-0a3e-302b-b312-c905e1dce488 | -17.572201 | -46.661701 | 2025-12-24 00:12:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| de18987e-90d4-3b1f-a01b-ba959dfcca80 | -12.2746 | -43.509102 | 2025-12-24 00:12:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f83000c5-7752-3de1-bbfe-69b993d0b09e | -20.900801 | -48.641701 | 2025-12-24 00:12:00 | METOP-C | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39e233c0-08dc-3251-8ff1-d6112da68cc4 | -5.7034 | -35.5397 | 2025-12-24 00:12:00 | METOP-C | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 10eadcca-b7df-3205-897d-68b066520ecc | -2.9628 | -39.9575 | 2025-12-24 00:12:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1147b4a1-d401-33b0-923f-709763356b41 | -7.2269 | -43.077202 | 2025-12-24 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d94f72e-bb00-3684-a56d-713dfef96f4e | -12.2786 | -43.528301 | 2025-12-24 00:12:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f20bb290-a9e7-39da-b14a-86a15811e2d6 | -12.2806 | -43.5378 | 2025-12-24 00:12:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e58a32e1-1007-3235-9895-8d2ada517a1a | -12.2766 | -43.5187 | 2025-12-24 00:12:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f455cf51-9ab7-3f42-8345-e17bdfc6c414 | -8.8107 | -40.5438 | 2025-12-24 00:12:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| fd927516-1864-331a-8b40-20a69145c493 | -20.9816 | -48.714901 | 2025-12-24 00:12:00 | METOP-C | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f8fb299-5da0-3dce-a6c1-2a511061bcb8 | -3.5507 | -41.620098 | 2025-12-24 00:12:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2307ea9e-6dd4-38a7-8138-9bcc6ccf26ff | -5.7059 | -35.5504 | 2025-12-24 00:12:00 | METOP-C | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f23451a7-3a23-36d1-8a3a-60aab6c0d2a9 | -5.7008 | -35.5289 | 2025-12-24 00:12:00 | METOP-C | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| ffe902df-6c25-3b0c-ae2f-407624387b23 | -22.48771 | -49.91124 | 2025-12-24 00:26:00 | TERRA_M-M | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5e079b43-c89f-3704-bc65-0456d097dac2 | -22.48635 | -49.89991 | 2025-12-24 00:26:00 | TERRA_M-M | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c57c925d-5e94-3a97-8008-28e9b2c2e29a | -22.3846 | -49.89785 | 2025-12-24 00:26:00 | TERRA_M-M | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8dd51704-06ea-3d3c-b8a1-c589f85fd937 | -22.39417 | -49.89629 | 2025-12-24 00:26:00 | TERRA_M-M | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| a9e2a2e7-e321-3c72-bf13-3a669ca580af | -16.58575 | -45.8836 | 2025-12-24 00:28:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71aeeeda-7187-3eea-9c44-00aeb184c1c2 | -20.99514 | -48.7632 | 2025-12-24 00:28:00 | TERRA_M-M | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.6 |
| eb714871-c1d7-380c-bf24-bf1a84ef65a6 | -19.91321 | -50.86439 | 2025-12-24 00:28:00 | TERRA_M-M | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a64fa4d3-dc60-3101-99fe-b333b7af4d91 | -16.52012 | -43.5394 | 2025-12-24 00:28:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b1b3638c-6c3b-32bf-bcd2-8d1b8d24994b | -16.58409 | -45.87278 | 2025-12-24 00:28:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7121b117-ed71-30ae-96f5-866f4c532abc | -20.91867 | -48.67105 | 2025-12-24 00:28:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 915c115c-fa78-3355-9479-139292e55157 | -20.05358 | -43.24927 | 2025-12-24 00:28:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 1065d93e-56c8-30e3-a2e6-3409ef6525a3 | -20.05115 | -43.23478 | 2025-12-24 00:28:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| de7f0af1-22c7-3156-95fe-5dce66a535f4 | -20.91738 | -48.66128 | 2025-12-24 00:28:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| abbeceb7-7031-3d24-abc9-c0b50546956a | -20.99929 | -49.28748 | 2025-12-24 00:28:00 | TERRA_M-M | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| f3c552da-8420-35e3-a087-0b2ec577a6c6 | -20.3106 | -49.57264 | 2025-12-24 00:28:00 | TERRA_M-M | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c79a0308-49d6-3d27-ab19-3619b9ae7216 | -17.9186 | -54.12555 | 2025-12-24 00:28:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a299c75f-ed1f-35aa-b119-42cc58ea9181 | -21.05239 | -48.43075 | 2025-12-24 00:28:00 | TERRA_M-M | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9c6e9042-303b-33aa-97d1-d090267bb217 | -20.05043 | -43.25644 | 2025-12-24 00:28:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| cd762197-9b58-306b-bed4-f75029759ec5 | -20.95569 | -47.18249 | 2025-12-24 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 706042d9-55d2-3c89-a718-8e61f4475a08 | -17.92064 | -54.14373 | 2025-12-24 00:28:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4833587b-479a-3765-84c2-0385e8256f4e | -20.04812 | -43.24212 | 2025-12-24 00:28:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 32c4a718-202d-359d-ba71-7b0300e18806 | -20.99386 | -48.75341 | 2025-12-24 00:28:00 | TERRA_M-M | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| e05775a6-4f65-30f3-ab40-1e7807172d1a | -17.58062 | -46.6621 | 2025-12-24 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bf518449-444c-3d3f-bb55-d96c2b0a6e9d | -17.58206 | -46.6719 | 2025-12-24 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8edfd1de-68d1-3962-b057-d004e1b529bb | -14.03752 | -50.53107 | 2025-12-24 00:30:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bec844ee-362a-3d45-a439-bec8f9703d41 | -14.03878 | -50.54064 | 2025-12-24 00:30:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4aea0d04-cd66-3733-9f33-049782da439b | -11.8424 | -43.78523 | 2025-12-24 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 026c2246-9c72-3246-9492-d8a461538fd9 | -11.83731 | -43.79235 | 2025-12-24 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 08b9571d-a134-3a6e-a59e-eba4cc176660 | -13.29284 | -49.23817 | 2025-12-24 00:30:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b0f25864-8ec2-3d8e-95d9-b2bd3dc4da20 | -7.23326 | -43.08845 | 2025-12-24 00:32:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 8721d418-e44c-38cf-bd01-f8d3f66d941e | -7.22772 | -43.09504 | 2025-12-24 00:32:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 2986da05-772a-36cc-8ebf-3556d3c7b516 | -12.2929 | -43.5359 | 2025-12-24 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6d7961b2-d980-3603-97ca-7175f251bdfe | 4.3653 | -60.3521 | 2025-12-24 01:09:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 38de6b44-0b2f-3d43-9941-eff26564284c | 3.6369 | -60.2659 | 2025-12-24 01:09:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f85cccf1-c6b3-3790-96bb-5ad962956c8b | 3.6513 | -60.293201 | 2025-12-24 01:09:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a2d20d5d-9a5b-3c00-a6c4-062540662314 | 3.6415 | -60.2911 | 2025-12-24 01:09:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 38c6ac52-899d-334c-8a2c-e3e99ee9e7d2 | -17.9146 | -54.148201 | 2025-12-24 01:09:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7a9f91ac-a4ee-37de-9f3b-879c044d1d8a | -3.5573 | -41.6357 | 2025-12-24 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 880f6d7b-5174-3102-ad7b-80f1bd489584 | -3.5575 | -41.6118 | 2025-12-24 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| d917b5f4-ceb7-3b6f-991b-81a5815fd87f | -3.5573 | -41.6357 | 2025-12-24 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 8a3c8e92-9e0b-35f2-8333-7bfd98ac23ee | -3.5386 | -41.6367 | 2025-12-24 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 777a9a5a-6e86-375e-9718-6739ed767114 | -3.5575 | -41.6118 | 2025-12-24 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 7f5eeb25-85c2-3400-afe9-2992dfc89d05 | -3.5573 | -41.6357 | 2025-12-24 02:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| a726c14b-6610-316e-9740-d7ba472f94d1 | -3.5386 | -41.6367 | 2025-12-24 02:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 2dc7eb4a-e096-3fd8-b5cf-2c9e70e54098 | -3.5386 | -41.6367 | 2025-12-24 02:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| ab59311c-65c2-3c7a-94e2-e7fbcfb45163 | -3.5575 | -41.6118 | 2025-12-24 02:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 56f8688f-cfa0-3610-b435-1b4c3cec7ff9 | -3.5573 | -41.6357 | 2025-12-24 02:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| a74b7adc-ce15-3f4e-83a9-281e7ea3d808 | -3.5388 | -41.6127 | 2025-12-24 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 03d9b491-8149-3073-9dcf-20a4dc12c946 | -3.5573 | -41.6357 | 2025-12-24 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 8a310c28-185a-3462-8e5a-2dd4a1147299 | -3.5386 | -41.6367 | 2025-12-24 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 72b41c6f-0a72-32be-960d-631b290ff9cf | -3.5575 | -41.6118 | 2025-12-24 02:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 365a2273-5135-37a2-895e-920bef7789ca | -3.5573 | -41.6357 | 2025-12-24 02:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| a91daca6-dceb-3e90-8b60-0bf4957fc99f | -7.00079 | -35.23897 | 2025-12-24 03:04:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cf70d30f-5303-3258-b8f6-bbc115e5bb2e | -7.00617 | -35.23986 | 2025-12-24 03:04:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 11f89491-88fd-31b0-a1b0-beb056185c2f | -8.35497 | -37.02158 | 2025-12-24 03:06:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7c90407-43e6-3048-8ce6-7b990276392d | -8.74683 | -37.17821 | 2025-12-24 03:06:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 278eb372-5cc7-30ad-8bee-43ff9a0b70ee | -8.74407 | -37.18082 | 2025-12-24 03:06:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b1cdf850-a2dd-3782-946c-ef081122009b | -18.82153 | -43.16768 | 2025-12-24 03:08:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 90c30d25-4566-384e-b55d-a20134fcba16 | -18.82043 | -43.16399 | 2025-12-24 03:08:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3ede9899-4daa-3c66-8ce1-65408b39f679 | -18.81899 | -43.16986 | 2025-12-24 03:08:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f699776b-d18a-3b64-9787-deb46a4a4b30 | -3.55573 | -41.62705 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4d2084fa-e193-3e7d-8075-276960d50eec | -3.54428 | -41.6251 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| dfa44b65-556b-3416-a428-84ea9fe37477 | -5.42762 | -36.70525 | 2025-12-24 03:34:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf573181-21bd-31ca-b632-fa84fc6bb4d3 | -3.55001 | -41.62606 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5449f5d4-a919-357c-8747-5913f66315b6 | -3.54362 | -41.62902 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 6db74a41-847d-31ff-9c0f-1f829605857d | -5.23263 | -37.68866 | 2025-12-24 03:34:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d94d0f3-8024-3065-9969-08346b626553 | -3.54495 | -41.6212 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0a5d948d-34fc-32bf-8272-4a32bbb326a3 | -3.54935 | -41.62997 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 0ab6953f-dced-314e-a7b5-d1d86003f147 | -8.05693 | -36.15118 | 2025-12-24 03:34:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 753223ee-80c0-3da6-980e-a6056c8c3515 | -3.55068 | -41.62215 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 00e4e333-76d7-34fb-b716-7ee7f53f31f2 | -3.5564 | -41.62315 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 279f6b60-dc9e-37cd-a8bf-db4fff52dd2b | -3.55507 | -41.63093 | 2025-12-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| dd824e65-41b2-37e6-bb45-34d421e24727 | -4.57699 | -38.11987 | 2025-12-24 03:34:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7faf0973-9de4-392b-a609-384f2afec5de | -3.20372 | -41.84879 | 2025-12-24 03:34:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c3032bc-6548-3aa4-848a-ae73a02b1e57 | -8.74651 | -37.17937 | 2025-12-24 03:34:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
