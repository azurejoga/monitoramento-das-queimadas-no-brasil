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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cd36594-6be2-397f-9617-a0b8e07a6c1c | -10.37161 | -45.06591 | 2026-08-26 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| b4ac70b2-de5f-3d9b-8269-c2de912cb0de | -6.26334 | -53.38501 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4db5c1fb-eb52-3c0b-b53c-cfe73dbca71b | -9.71647 | -49.33464 | 2026-08-26 04:08:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc25fc92-a8d6-30ba-a2bb-475536c8dfb6 | -7.12045 | -42.78942 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11137cc3-24cf-3874-ab51-c3426915a663 | -7.30208 | -42.96233 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0162895d-b641-305c-babe-402e6d4a3cd2 | -8.01681 | -51.80942 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9161ed0-dc04-3805-a619-98f43cfed0f2 | -14.03441 | -43.85245 | 2026-08-26 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56117ee6-83c6-38c0-81d5-0f8b1e8cfe12 | -12.76626 | -46.44841 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05210d78-5397-310e-a741-6876fd4b9968 | -7.31572 | -42.98897 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 22bdc3b1-3a02-334e-a981-5e7f80049b0f | -12.637 | -48.40978 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0783730-9ddc-352b-8dfd-943b26a0b0d5 | -8.02812 | -51.81295 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c465ec8-979c-3772-b8cb-be8cd081c745 | -7.28772 | -44.08113 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e19ee8d3-61d1-3231-a198-545211348727 | -11.64106 | -47.15673 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7031688-7702-322b-8328-a776b2157ac9 | -7.12459 | -42.7861 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d038f14-2a88-38b2-a25b-6d955b9c56cc | -9.03368 | -50.80377 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de558e9e-6444-3abd-be5a-f34f8a075e09 | -12.41559 | -42.8952 | 2026-08-26 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d475cb06-375f-3311-90ce-ff505a40dda1 | -7.51594 | -44.95385 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d5a54e4-691a-359c-ad89-f8eff3d7a7b0 | -9.59656 | -45.99574 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae71c4e4-1d56-353f-93df-4a3003f75101 | -7.32122 | -42.97763 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fe86524b-9ccf-3072-8efb-72df4b21d11f | -9.57063 | -49.26125 | 2026-08-26 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe50c0da-892e-3a42-8023-8b6ad71325b9 | -12.75946 | -44.26834 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ca9a788-0788-3794-818e-da3140f631b7 | -10.37538 | -45.0666 | 2026-08-26 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| c525d9be-b961-3c96-b8b1-3403b8aecc55 | -6.16398 | -53.49899 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14001737-1368-3286-8c9d-472b3d30c9e9 | -6.25197 | -53.36945 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68f3d19f-94e4-3358-a1f0-a036ff4b2bab | -11.28227 | -47.07281 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b4c8c95-f2dd-31f0-82c7-352ec3cc1d90 | -7.76185 | -44.76699 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9d0a7df8-3d43-3253-953c-4943c37d7dac | -11.16349 | -54.00622 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48d64635-7d0f-3761-b9f7-034832e8ea57 | -7.86276 | -46.10999 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46a54293-14c6-31c5-936e-50a9f21fb591 | -10.75526 | -54.02413 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 91200f64-bbdf-3980-989d-26047be52c8f | -7.02017 | -45.7272 | 2026-08-26 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b2a0804-9b21-37bc-925f-3d6ed90adff7 | -8.08411 | -47.49471 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb9513bb-7fb2-31e5-9794-c505d059e8f8 | -7.13593 | -43.17997 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c4725da-f8db-3962-a074-235eeb9dc054 | -13.33506 | -48.23117 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ffe74fd-6ee1-30e8-8ad2-77531003a821 | -10.37241 | -45.06129 | 2026-08-26 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| c8df280f-f128-39c2-8c86-b28b6c90c088 | -13.34016 | -48.20298 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df80f3ce-d3be-372e-ab1e-1aacda959a17 | -12.41618 | -42.89161 | 2026-08-26 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 837a5c2b-05c8-3b19-8800-263d739e0c20 | -8.01602 | -51.81353 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a887962-aa52-33b3-8359-e3590dfaffab | -7.4834 | -46.09206 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bb962ae-1d09-3aa1-8c08-bc9bc1594478 | -9.44621 | -51.67033 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd355a12-92dd-3bb3-8916-d7c792a4d7a3 | -13.34387 | -48.23269 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6054ccbe-60a3-30a1-84f1-9fbd26c5700f | -12.66476 | -48.41052 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 77cc1df7-f0af-33aa-a944-d90e8e469708 | -8.09233 | -51.67591 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 963897db-05a3-3ddb-9516-792ae1b7b782 | -12.76138 | -46.45296 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 937657a8-b995-3835-ac07-bafda9e22d66 | -7.30549 | -49.54317 | 2026-08-26 04:08:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82665af5-6c6f-3ef9-bbed-bd20331b6acf | -7.74967 | -44.75722 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02affce1-5adc-32c2-b228-43ba63a6557c | -12.67601 | -48.40878 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 936fa9c1-0da8-3d28-9bdf-aa40c2131037 | -6.30549 | -53.57591 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fc0ff77-fe93-3342-b113-65c6982aa47b | -13.3696 | -48.21462 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 156935f4-628f-3075-9684-3031b5c4e880 | -6.24962 | -53.38235 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e7d0dae-6c1a-3c36-b2ef-6197f39a4d75 | -7.56324 | -44.47711 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b28ab3bc-4be6-3016-902b-c39636da0f0f | -10.03808 | -46.05125 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f79c8ed0-4121-3ae9-a0a2-e28ff634088d | -8.09528 | -47.56532 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fed0fc7c-655b-3422-bff3-6b1341aa520b | -12.69844 | -48.41314 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40fcb0d5-4b57-3592-9580-54ea9be1ff39 | -12.02369 | -46.01848 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e71aaff0-e186-381f-992a-ba798c48e037 | -10.2983 | -49.95865 | 2026-08-26 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a334dc9-b170-32b6-a358-80c6f86ffd34 | -12.71855 | -48.37977 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4caf91b-4d47-3f14-a765-dbb575273899 | -8.08399 | -45.90318 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3025641b-8c98-37c0-9ef6-440b0a530fa9 | -11.42613 | -44.53546 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e54e950a-4338-376f-b832-22d7d34b0707 | -12.63247 | -48.40911 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ff2d48b-01c6-3778-b3c3-702d9b2592cd | -9.65592 | -48.31382 | 2026-08-26 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccd57f68-22df-317a-9673-5afd6c4a7ba2 | -8.16737 | -46.2025 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7d2031d-c3a7-3708-b2c2-88d166d1ac23 | -10.76359 | -53.98322 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d16ea206-5fc8-36d7-b9e8-df5e4e802a8d | -9.56696 | -49.28163 | 2026-08-26 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b31aa63e-3055-39f7-8a4d-17ab7ad2b838 | -11.42106 | -44.54333 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e5559a7e-7bf5-3588-96ce-879a653f2170 | -8.05141 | -42.68013 | 2026-08-26 04:08:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 16b01a8c-d520-3c91-aa18-b6e9899322d7 | -11.16462 | -54.00054 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0648f152-7c4d-34f9-bde1-f5f6c4b587f1 | -9.18926 | -49.99358 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf12a1bb-ed58-3941-8be9-50dab7b3586c | -13.35636 | -48.23682 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b6684e5-29f9-37f5-82c5-39c9309e4d7d | -11.37596 | -45.16479 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 844fb003-f1ee-3eab-bd93-a1fef64ec95d | -13.35857 | -48.20088 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8afdc3bf-bcb4-380d-8153-6ae9b12d9ee2 | -7.71496 | -43.78802 | 2026-08-26 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5929e032-fbed-3446-8ba0-21e2b3dbb4f0 | -7.27895 | -45.35682 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1732397e-52b8-3137-94c7-23035f0d2d00 | -9.60808 | -55.11683 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 250b49a4-fb2a-35fe-b315-6cc0b485b9f6 | -9.03581 | -50.79235 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 44d492f9-ce95-315d-876a-e068b033a89a | -13.33773 | -48.21642 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91c65a3d-e482-320b-8c0b-ec9f20279839 | -12.76502 | -44.25691 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c8f5f4f-9630-3600-aa60-ef9220579f93 | -9.60741 | -55.10972 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 72e8f31e-34ba-3c94-b81d-b9d6815d8c5a | -8.70865 | -49.60873 | 2026-08-26 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 311407e8-e489-3515-b8cf-81a3deb48d70 | -13.34085 | -48.19923 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42170768-adc4-33a0-bf57-b05f372f2a56 | -7.25583 | -45.37105 | 2026-08-26 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0af03172-b83c-3be7-9c6e-2c13c49771c8 | -11.72111 | -47.76898 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fbfbcab-115b-3e7c-bd1c-e4ea47d38124 | -7.76136 | -44.74687 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d2b7301-a353-362a-89ad-8e6b3e1bb705 | -11.79815 | -47.64172 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b559aa-f528-35c7-857a-ce890a8830cf | -9.04138 | -50.79357 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af87ef0d-a36d-37c6-92ef-7f4b36721225 | -13.49416 | -43.66085 | 2026-08-26 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbbb80bd-787b-3183-a5d8-d3d98f6d9638 | -11.00532 | -51.16364 | 2026-08-26 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 430fb958-5e2d-321f-8eab-c0edd0788ff3 | -6.29854 | -53.57468 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5daf3a20-cbd9-356e-a4c4-90ee489b65e4 | -13.34831 | -48.23323 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba574e58-4401-3606-b245-e3972a14abdf | -8.14275 | -47.51001 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e758860c-49c8-301c-9ca4-68a9fc5a3619 | -7.28429 | -43.02584 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 809caea2-bbdb-3d58-8604-d40fa330e0d0 | -12.72306 | -48.38045 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1654c447-60dc-32f3-91f4-ac66c57672d7 | -10.76188 | -54.02549 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cbbe9e45-8020-38eb-9e0e-df067bbeed47 | -9.60246 | -55.10799 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c7781321-151b-330a-ae0c-d21dc4381e5d | -7.29957 | -49.54554 | 2026-08-26 04:08:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bf45ae5-1b0a-3355-b2eb-8ee160a73f90 | -12.76083 | -44.26031 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6371fd22-ad14-3d65-a1fe-eba90611eaa7 | -7.27493 | -45.35612 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d88f48b-b05b-3f09-975e-38821ff39b2b | -12.41955 | -42.89209 | 2026-08-26 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dcc8340e-ee63-39d1-89a0-13a379322513 | -8.01602 | -51.81033 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f73b8535-f02e-39d0-ad65-765afcfdbfb6 | -11.15696 | -53.99374 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71f3bb4e-241d-3a0c-b029-b6a09217ffa4 | -9.6059 | -55.11718 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |


[Clique aqui para ver as próximas entradas](README18.md)
