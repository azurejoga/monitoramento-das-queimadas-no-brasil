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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bedfccca-3782-35ad-adce-f1349e19d4ec | -6.4545 | -44.5519 | 2026-06-11 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1400298c-cd83-33cb-9e09-7722a980281e | -9.3231 | -45.5015 | 2026-06-11 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d554b198-e0d2-387e-bd85-835b7f61274f | -6.4355 | -44.5764 | 2026-06-11 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f0218e44-0f4c-34a5-b7cd-03f97ba5de58 | -12.8548 | -44.3625 | 2026-06-11 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5523287a-734f-3402-be13-12ecec86152a | -6.4545 | -44.5519 | 2026-06-11 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 0992983e-e142-31d4-9d38-8acdb0893577 | -6.4543 | -44.5749 | 2026-06-11 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d749bb19-7e0c-3613-b799-c7370b3581fb | -6.4355 | -44.5764 | 2026-06-11 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| be033309-fa0c-3237-83af-6b42fefd7814 | -6.4357 | -44.5535 | 2026-06-11 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| faf59cd9-fb26-37d4-b0bf-8798295f396f | -9.3237 | -45.4559 | 2026-06-11 01:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ab438689-0a24-3f25-83bc-fd4a2c5268c1 | -9.3045 | -45.4809 | 2026-06-11 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 714337e8-2590-3487-8fdc-ea1f5d600c97 | -9.3234 | -45.4787 | 2026-06-11 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 566dde51-a0dd-33e5-a13b-f61d54d30d56 | -6.4355 | -44.5764 | 2026-06-11 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e769f562-961a-3018-b9e8-08670acdd357 | -6.4543 | -44.5749 | 2026-06-11 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 45417487-c0df-3882-99dc-62c8808f4a9a | -9.3234 | -45.4787 | 2026-06-11 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| f3fbbf4c-816a-3a33-9811-a0f9e8717cad | -6.4545 | -44.5519 | 2026-06-11 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| d1d574ca-1ca6-3692-a792-f27959493a4d | -6.4357 | -44.5535 | 2026-06-11 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 05dff4e3-6b60-3221-884e-3c6161085132 | -6.4355 | -44.5764 | 2026-06-11 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 1ebadc55-61a0-3d19-aab4-a84cdede27c2 | -6.4543 | -44.5749 | 2026-06-11 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3102aac2-80ef-3305-811d-8ec39f1165fa | -9.3234 | -45.4787 | 2026-06-11 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f1d0e52c-794f-349a-b8e3-2fc080daa3f3 | -6.4357 | -44.5535 | 2026-06-11 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6375650e-d6cc-363d-8c74-2258eeaea799 | -6.4545 | -44.5519 | 2026-06-11 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3b38baa6-b5b9-3dfd-9c98-f77037638fd6 | -12.8548 | -44.3625 | 2026-06-11 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| fdc1b6aa-6349-37a6-acc9-f50feb54a1a8 | -6.4545 | -44.5519 | 2026-06-11 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 13d828ef-2203-3201-aedb-e29c6e20407a | -6.4355 | -44.5764 | 2026-06-11 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 1b9692b3-ad37-3a70-ad96-8f4e0353461d | -6.4543 | -44.5749 | 2026-06-11 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a1151592-07be-36e2-9b7f-5bf67580bb20 | -9.3234 | -45.4787 | 2026-06-11 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1ef38bb2-d31e-3156-9b30-71c67627cdce | -9.3237 | -45.4559 | 2026-06-11 01:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| d755e386-21bd-3911-9325-d7fe761f01b0 | -6.4357 | -44.5535 | 2026-06-11 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 2bd55325-202c-30d4-8b3a-9cf91a45e01b | -12.8548 | -44.3625 | 2026-06-11 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 5797fbc1-4b2c-30b7-b464-3a13967bcd3b | -9.3234 | -45.4787 | 2026-06-11 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| fe6a877a-9505-35d5-88e4-935ff389fb67 | -9.3237 | -45.4559 | 2026-06-11 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 9e0beeb7-0854-36f3-97fe-a6539bb458d5 | -9.3237 | -45.4559 | 2026-06-11 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| fcf24b52-e9f1-3987-afe7-33c856a732f6 | -9.3234 | -45.4787 | 2026-06-11 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 9f8a9536-428a-3985-84a7-b52811173718 | -12.8548 | -44.3625 | 2026-06-11 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 87876bd2-8480-3ed0-9427-ea819864cfb4 | -9.3045 | -45.4809 | 2026-06-11 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 47f58086-3acb-30ab-b2ab-0647d250dee4 | -6.4545 | -44.5519 | 2026-06-11 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 378622ff-649c-37c4-b6ce-e5a13ccb9128 | -12.8548 | -44.3625 | 2026-06-11 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| adc7b00c-904f-34bd-a2ee-544d587ce806 | -6.4355 | -44.5764 | 2026-06-11 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5c5cf3a6-4b45-375d-b4de-28bfda045009 | -6.4357 | -44.5535 | 2026-06-11 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| dc6abf29-3111-3f0b-b983-210e1f7b8929 | -9.3045 | -45.4809 | 2026-06-11 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 0bdc9824-ee40-318d-be8b-bd1798c5db51 | -9.3234 | -45.4787 | 2026-06-11 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 11acecd2-0e92-377d-b573-c9d67d7bc5c1 | -9.3237 | -45.4559 | 2026-06-11 02:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ea4cf251-cfc4-3d17-8062-d91389510dcf | -6.4543 | -44.5749 | 2026-06-11 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a2ed23bf-bcdb-3666-aef7-dc5673dfd656 | -6.4357 | -44.5535 | 2026-06-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cd21927f-7156-33b5-8755-6e47af0afda5 | -6.4543 | -44.5749 | 2026-06-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d598fecf-2bbd-33f6-8fd2-b03962ed4ba4 | -12.8548 | -44.3625 | 2026-06-11 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 7ccabdda-351b-339a-a469-77a828bc1d86 | -6.4545 | -44.5519 | 2026-06-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3ff017f1-ffd4-329f-8b60-75cae0da2474 | -6.4355 | -44.5764 | 2026-06-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| db05895e-c249-3cc4-a6df-bf94cd47bd84 | -9.3237 | -45.4559 | 2026-06-11 02:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 75a0ce02-daf5-3bc4-8ab5-6e1515eec623 | -9.3234 | -45.4787 | 2026-06-11 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 160a3d74-7103-3ac9-a784-ee6509d80d10 | -9.3237 | -45.4559 | 2026-06-11 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 068ded23-c288-3e35-8ed3-3769676fa2a5 | -9.3234 | -45.4787 | 2026-06-11 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| e2f16341-5c50-3b77-a7c8-851be84a4712 | -6.4355 | -44.5764 | 2026-06-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 78e17d9a-defc-3018-920a-44434640f165 | -6.4543 | -44.5749 | 2026-06-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e18c1057-619d-3b8a-8c70-cabd1a587914 | -6.4545 | -44.5519 | 2026-06-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ddb40485-5677-341f-808c-40bf28c7d95a | -6.4357 | -44.5535 | 2026-06-11 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ce226db2-fc54-36aa-951e-a322b10f4a92 | -12.8548 | -44.3625 | 2026-06-11 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d360b78f-af97-360a-8958-2597ec459da6 | -6.4545 | -44.5519 | 2026-06-11 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c0479e6b-df18-33c6-9e6d-e053614ca06e | -6.4355 | -44.5764 | 2026-06-11 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 59fd6d07-82fb-3bd0-b1af-f92bc9ef9aeb | -9.3234 | -45.4787 | 2026-06-11 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 6884f1ba-e0c7-36d5-ab46-efe0f7e0e71c | -6.4357 | -44.5535 | 2026-06-11 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d72ed492-678d-37f4-a721-ab555e35a609 | -6.4545 | -44.5519 | 2026-06-11 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 423605ae-3f4b-3b24-8f9e-760876f4db56 | -6.4543 | -44.5749 | 2026-06-11 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 54a982b3-af90-3427-9f3f-7773a3a685e8 | -12.8548 | -44.3625 | 2026-06-11 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 99e7dacd-6adb-31a9-903b-85625bb8fbf4 | -9.3045 | -45.4809 | 2026-06-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| eae9e595-3f58-3f9b-9cef-603846fb059e | -9.3237 | -45.4559 | 2026-06-11 02:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| da01763d-b449-3be3-8c40-807f761af1fb | -9.3423 | -45.4765 | 2026-06-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| a3ecc2d6-78f3-33e4-ab6f-900927e09768 | -6.4355 | -44.5764 | 2026-06-11 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f83d0237-9a5b-3bf3-ba14-640245e5befa | -9.3234 | -45.4787 | 2026-06-11 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| adb2ea0d-b993-3da5-b6b0-dd2aff7681b1 | -9.3237 | -45.4559 | 2026-06-11 03:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 76a6f356-27de-38de-bf27-3bb891ec3887 | -12.8548 | -44.3625 | 2026-06-11 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| e2e97bfb-37f7-3125-95a8-b0c3895966f7 | -9.3234 | -45.4787 | 2026-06-11 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| c972481d-2ee1-30c0-becb-510e4e55b232 | -6.4545 | -44.5519 | 2026-06-11 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| f023d0ad-b590-3277-a9f5-e7ba15d4acf2 | -9.3234 | -45.4787 | 2026-06-11 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 7695ce40-5727-33b1-bd5d-3c3aad0c3bec | -6.4357 | -44.5535 | 2026-06-11 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2a6afd56-80cf-3a63-a59d-a475e92e5447 | -6.4355 | -44.5764 | 2026-06-11 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 93651d88-a7d8-3ff7-83ea-a295b38463ff | -9.3045 | -45.4809 | 2026-06-11 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| f4274df2-b7c7-3c48-8839-1619b053126a | -6.4545 | -44.5519 | 2026-06-11 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f497ce24-4393-3227-9b1b-939d621f355c | -9.3045 | -45.4809 | 2026-06-11 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 363f686d-3b62-3441-b5bc-58e85303b3c7 | -9.3234 | -45.4787 | 2026-06-11 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| c397a55c-6371-3b09-ac16-95b8438b4347 | -9.3423 | -45.4765 | 2026-06-11 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f27afd4f-3759-3949-a749-868ddc8fa116 | -6.4357 | -44.5535 | 2026-06-11 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1d2430da-674a-317b-bb41-edf3bf346cb3 | -6.4355 | -44.5764 | 2026-06-11 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b1e88ae9-fe3d-3f56-924e-b9cf0eeac496 | -6.4543 | -44.5749 | 2026-06-11 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9038c267-d80a-3e8e-8000-c715a208f6f9 | -6.4355 | -44.5764 | 2026-06-11 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 53d031e3-5f55-3d52-9c12-bcd5cb378e97 | -6.4357 | -44.5535 | 2026-06-11 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 396d8925-73eb-344a-9044-e33ac3fa85cc | -9.3234 | -45.4787 | 2026-06-11 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 1d639d5e-da73-36ee-bef1-efe65ffe24ae | -9.3237 | -45.4559 | 2026-06-11 03:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f5b36be3-5805-32b2-916e-e835c011eed6 | -12.8548 | -44.3625 | 2026-06-11 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 932a6dc2-8166-3040-b63d-db18d8ca70ad | -9.3045 | -45.4809 | 2026-06-11 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 47c94192-54e6-367c-9c0c-bf2b5ea210f0 | -6.77609 | -37.51535 | 2026-06-11 03:36:00 | NOAA-21 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0784b5ad-16e2-39e8-b77f-552f488d4c5b | -6.95851 | -44.54738 | 2026-06-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f19958e-dd8f-316b-b694-63a05966dcc7 | -7.47772 | -36.60519 | 2026-06-11 03:36:00 | NOAA-21 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26eadcad-1bde-3b0d-9694-4fc4c228e7fd | -6.19188 | -44.8635 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2518342e-43bc-3d74-8d41-23e884e1d3a1 | -5.52204 | -37.48421 | 2026-06-11 03:36:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| be2b773b-f8ef-3092-b3f2-8a2eaa99a2ca | -6.44022 | -44.57422 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05a66345-5aa3-3fd8-9cab-522f28159c95 | -5.93354 | -43.48405 | 2026-06-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3aa196f-432b-37a8-a0ce-c392d7b35d03 | -6.43943 | -44.5786 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85d90739-6d0e-3f6c-ac95-00d029f0e9a7 | -6.72934 | -39.27197 | 2026-06-11 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 56c37056-06e3-3eed-9481-ab0d5c36ddb8 | -5.51969 | -37.62085 | 2026-06-11 03:36:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
