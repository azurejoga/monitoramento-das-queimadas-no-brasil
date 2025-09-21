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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87eae947-8804-3d12-b0a3-81c367552dab | -10.09521 | -68.8378 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b7571b-e7c0-317b-b09b-b82350fb32fa | -7.98977 | -70.92957 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a134773f-d758-3854-a58c-a5d519162805 | -8.76427 | -69.12306 | 2025-09-21 06:18:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b906221-5e18-39c7-9da5-44e85d008e85 | -8.22305 | -71.02738 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb162f9f-e6e0-35d1-86b3-9ebd8302c42c | -15.9783 | -59.4069 | 2025-09-21 06:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5e777d33-a64e-370e-a445-116e45798fcb | -15.978 | -59.4269 | 2025-09-21 06:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 8bf0e707-2634-3d15-acae-6e6b319af7f2 | -15.9586 | -59.4288 | 2025-09-21 06:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0620d67d-b76a-35dd-a802-a00cb9d9fc24 | -15.9783 | -59.4069 | 2025-09-21 06:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 97d0292b-4f37-3e19-9200-1424c6f2ff1c | -15.978 | -59.4269 | 2025-09-21 06:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 54cf4f7f-8b2a-3dd6-854e-b037e035aae6 | -15.9586 | -59.4288 | 2025-09-21 06:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d66e2c41-8de1-3b7f-9cb1-8f3856b146e4 | -15.978 | -59.4269 | 2025-09-21 06:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 66a44b04-a6f3-31a5-90cc-722aacabdabc | -15.9783 | -59.4069 | 2025-09-21 06:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c3ca23d1-a3aa-38b9-98d8-1a098767aafa | -15.8218 | -59.5217 | 2025-09-21 06:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1cfd9845-ba70-3517-94d3-a8b5c8e2927b | -15.9586 | -59.4288 | 2025-09-21 06:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 1fc7142f-f743-32bb-870d-9739187bc470 | -15.8218 | -59.5217 | 2025-09-21 06:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7cbdd369-8572-3ee7-bf53-f17cbc44fb94 | -15.9783 | -59.4069 | 2025-09-21 06:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| d9795d68-8dd4-3708-8712-d904e3ef201b | -15.9586 | -59.4288 | 2025-09-21 06:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e37c8d56-4c76-3807-941b-fb860a6125fa | -15.978 | -59.4269 | 2025-09-21 06:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 3e8dbbf8-0e80-3e11-8c74-3fdad027599b | -15.9589 | -59.4087 | 2025-09-21 06:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f26584c7-1649-34a6-98de-829dadcc254e | 4.33156 | -60.74378 | 2025-09-21 06:57:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 713459e2-c5a0-33e7-86d4-cdf1ea29706e | -3.75277 | -54.80185 | 2025-09-21 06:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| eab4b65d-1e97-3424-9929-f80edf4bf2a1 | -15.9586 | -59.4288 | 2025-09-21 07:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5f738e1f-14a8-3fcb-8413-73f0ac3829a0 | -15.8218 | -59.5217 | 2025-09-21 07:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5b9f3459-e536-3007-991e-4822f53b486f | -15.9783 | -59.4069 | 2025-09-21 07:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0151e142-cb78-374d-a098-93f6f6b55cf5 | -15.978 | -59.4269 | 2025-09-21 07:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 8a923f0a-ad8e-31ba-a8ac-bf7965f57022 | -9.41096 | -63.70126 | 2025-09-21 07:01:00 | AQUA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49ce86de-b1b6-3dad-b878-4b2c5d617334 | -15.27626 | -56.84263 | 2025-09-21 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3ef947a7-742b-3e6e-bd5f-3508ddeee82b | -9.4035 | -63.69107 | 2025-09-21 07:01:00 | AQUA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92e5f63c-0b7f-3abb-9eb8-a32b98dbf3a2 | -9.4123 | -63.69239 | 2025-09-21 07:01:00 | AQUA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4510cf0c-06d6-3406-a33e-8d46855f24e2 | -8.98585 | -65.45157 | 2025-09-21 07:01:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e99e9e3e-adda-32de-ac39-715b697d8e72 | -15.97478 | -59.4144 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b20c0c17-55f8-398c-8636-94cf18ef526b | -15.96127 | -59.42813 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 514bbdaf-efea-34f5-809f-53631c63f289 | -15.8249 | -59.50241 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6066e90c-8c23-335c-b708-b001d76be015 | -15.96523 | -59.39587 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a77b2e86-073e-38e6-a1e1-f30f6d205cf0 | -15.82309 | -59.51735 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| af09f6b0-5478-398b-8bf8-34b7ea501917 | -15.81709 | -59.49355 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7092fe8d-3806-3366-ab5c-f60fdf1965a9 | -15.82651 | -59.51156 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 1006e981-1b8d-31f2-a75e-8df6407db375 | -15.97694 | -59.39695 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cff5e102-5d1c-3e35-98d9-d07e4a5062b9 | -15.97283 | -59.43018 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 2c17c81b-4a3e-39f8-98cf-d2a4f89a7421 | -15.96322 | -59.41222 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 37cfb3a6-9a90-3a6a-8eb9-06bcdf9e422d | -15.8151 | -59.5092 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4f07f713-b832-3637-9174-b01a39628439 | -15.94966 | -59.42649 | 2025-09-21 07:03:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ddb1f896-fb53-3a25-a4a7-f3d98cf2c746 | -15.9783 | -59.4069 | 2025-09-21 07:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 9c8188a8-501b-3420-a82d-232d3539952a | -15.978 | -59.4269 | 2025-09-21 07:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| be64825c-1e05-3f43-8b40-d82a4e832c89 | -15.8218 | -59.5217 | 2025-09-21 07:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 87b6f8ee-33e5-3b5b-b534-7a70a16fd706 | -15.9589 | -59.4087 | 2025-09-21 07:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d6e5b025-c299-33e4-a004-b52ef802f4e1 | -15.9586 | -59.4288 | 2025-09-21 07:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c368de9e-80ce-3aef-ad19-ab3f96778c4c | -24.7621 | -48.8093 | 2025-09-21 07:20:00 | GOES-19 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 9ce61c4d-c320-3a42-a6e2-4b966d30ba44 | -15.978 | -59.4269 | 2025-09-21 07:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 761748cf-141c-3932-83b9-e83135ce9301 | -15.9783 | -59.4069 | 2025-09-21 07:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| bed88a9e-4903-341f-b8f5-07e97415ab55 | -15.9783 | -59.4069 | 2025-09-21 07:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 8f81cb0c-e742-3131-b851-51633bda8677 | -15.8218 | -59.5217 | 2025-09-21 07:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b88ace33-0a0a-36dc-ab57-4729e0ed8474 | -15.9974 | -59.4251 | 2025-09-21 07:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e648422e-9d3e-3fa6-b7da-ba0339168844 | -15.978 | -59.4269 | 2025-09-21 07:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| d834191e-6d19-3e6c-a23f-8d96d6d7f292 | -15.9783 | -59.4069 | 2025-09-21 07:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 62fdfe7b-5086-33e9-8e5b-7c7aa18397a6 | -15.8218 | -59.5217 | 2025-09-21 07:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cb5fa92c-eff2-3652-89e2-5b96869ccdc7 | -23.3989 | -49.1191 | 2025-09-21 07:40:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d89317d6-e7b7-3067-a0f3-93eda139f3b2 | -15.978 | -59.4269 | 2025-09-21 07:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 133.9 |
| b8335cbc-1ec7-3406-8dfa-159d577e9d87 | -23.3981 | -49.1427 | 2025-09-21 07:40:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1d88e310-84e4-35aa-abe7-18566fcf68e9 | -15.9778 | -59.4469 | 2025-09-21 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 01887244-007d-343a-93e1-eddbf520b2b8 | -15.9977 | -59.405 | 2025-09-21 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 548db17a-1e5d-3775-ab64-972ded2f7adf | -15.978 | -59.4269 | 2025-09-21 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 246.9 |
| 4ade112b-df30-335e-9c34-fee2241ae00c | -15.9974 | -59.4251 | 2025-09-21 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 2966be28-3066-38d3-bf0d-f7d422884ddd | -12.7114 | -46.8454 | 2025-09-21 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9f2fb9a5-26c1-3bd3-b062-09c5d4226b01 | -12.6921 | -46.8482 | 2025-09-21 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 7065710d-dc67-3fb3-b396-86a57a0a2007 | -15.9783 | -59.4069 | 2025-09-21 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 010cef2e-33a9-3b20-856a-860a5f918d21 | -15.9977 | -59.405 | 2025-09-21 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 64956748-e1d7-3b08-bf06-c22b95fe8d2c | -15.9783 | -59.4069 | 2025-09-21 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 381183b2-71c4-371a-a48b-3f01aa8a683d | -15.978 | -59.4269 | 2025-09-21 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 5757ce64-54a2-335a-a22a-caef9c188b6c | -15.9974 | -59.4251 | 2025-09-21 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 466a930b-57a4-3b69-bb21-d35195c72154 | -12.6921 | -46.8482 | 2025-09-21 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e30ca522-5a66-37e1-b515-5aa1ba2c4e7c | -12.7114 | -46.8454 | 2025-09-21 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 52f74410-83d2-360c-a2dd-100c6f25aff6 | -15.978 | -59.4269 | 2025-09-21 08:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d8739cc1-dbb3-3c18-85a1-2937be4506bc | -15.9783 | -59.4069 | 2025-09-21 08:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 62a47a7a-a0bf-3a77-b395-85fc43720405 | -22.4874 | -48.1992 | 2025-09-21 08:20:00 | GOES-19 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 21e8958a-6038-3ea5-ad6f-1abb45a41252 | -15.978 | -59.4269 | 2025-09-21 08:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 284d752b-25dd-315c-9d84-7a05a0c4b2e9 | -12.7114 | -46.8454 | 2025-09-21 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 74ccdddd-00f1-36c7-95b4-a01eb174f335 | -15.9783 | -59.4069 | 2025-09-21 08:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 70f0db17-826e-39f1-a559-79253c920717 | -22.4866 | -48.2229 | 2025-09-21 08:20:00 | GOES-19 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4dbcaa18-7596-3f7c-880c-63ee85840131 | -15.9583 | -59.4488 | 2025-09-21 08:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 718f5d5b-cdfd-30f1-8e91-2f4cded67cf6 | -15.978 | -59.4269 | 2025-09-21 08:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5fb979b8-d3f1-3b45-a219-a28d6f6b8f80 | -15.9783 | -59.4069 | 2025-09-21 08:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 560c457e-dece-3d50-aab3-05362ee6f3f5 | -15.9778 | -59.4469 | 2025-09-21 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5596d35b-341a-3f04-b474-16058e3eb2c9 | -15.9974 | -59.4251 | 2025-09-21 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a5814c39-f4ab-33fa-b40c-72b8bcfec02c | -15.978 | -59.4269 | 2025-09-21 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 92a2ff55-63cf-33ec-9efc-f75026bd1e67 | -15.9783 | -59.4069 | 2025-09-21 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 570b67b6-70b0-355e-ae16-bb6f8b56c9c1 | -15.9583 | -59.4488 | 2025-09-21 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9c4dbd9f-01fe-33e7-9c65-1d9c1ea1338e | -15.9977 | -59.405 | 2025-09-21 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| df33b006-3eda-3374-8e59-98a672916311 | -15.9783 | -59.4069 | 2025-09-21 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 765b0f4c-1515-3f3b-95d2-878aeb328aaf | -15.978 | -59.4269 | 2025-09-21 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a2494782-0baa-321d-8bb3-31848357dc36 | -15.9974 | -59.4251 | 2025-09-21 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5f1c5f3d-0bc0-358e-8f13-7437fc241680 | -15.978 | -59.4269 | 2025-09-21 09:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4836939d-e20c-32e8-9640-b0471514f19c | -15.9783 | -59.4069 | 2025-09-21 09:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6f42f9ed-da30-3210-af44-822fe4cdf695 | -15.978 | -59.4269 | 2025-09-21 09:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| be902185-854e-392f-be66-dd630ce6647a | -15.978 | -59.4269 | 2025-09-21 11:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 389b7b6d-4971-31d8-aaf7-a74ac2ac316c | -15.9583 | -59.4488 | 2025-09-21 11:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 84124f18-c4bc-3ca1-b41a-b0358f776d02 | -15.9583 | -59.4488 | 2025-09-21 11:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 41ced9c9-0e82-30dd-98be-a55c505dd6ea | -23.1523 | -47.6245 | 2025-09-21 11:10:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.5 |
| 8ed39787-1de8-3c7e-87ad-7d8eb4eb4a81 | -15.978 | -59.4269 | 2025-09-21 11:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 198.1 |
| a271cee1-6a91-3d2a-b636-f23c3a82de47 | -12.4361 | -45.1052 | 2025-09-21 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README47.md)
