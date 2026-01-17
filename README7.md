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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 781df6fd-7436-3798-ae96-47021d6dd983 | -12.6536 | -46.76262 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e68b7f4-137d-3a5f-9e1b-593638598da4 | -11.79765 | -45.36377 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66bee228-a8da-3db7-91e4-32180a920ab8 | -15.44204 | -56.33383 | 2026-01-17 04:27:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d877e3f9-9885-3c25-9ab8-4b618c403e75 | -12.65948 | -46.75955 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6489992-4567-367e-8f72-c51350921694 | -15.01128 | -48.65832 | 2026-01-17 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b55da74-07ee-313e-90eb-d376bd166488 | -11.30597 | -49.20984 | 2026-01-17 04:27:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19b0dc63-cc7c-3069-8f9c-56248118846d | -13.50477 | -46.70634 | 2026-01-17 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beab26d8-cf33-34f2-a9f3-5b7337e2e50e | -11.88094 | -45.70065 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7496952c-ea50-31a1-a4f0-a308b7506ca9 | -12.91744 | -49.48842 | 2026-01-17 04:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdbdf893-5f8e-3117-bc7e-fe2d1d18735b | -11.53245 | -47.69357 | 2026-01-17 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47e93cd8-9d74-315a-b921-a585670ea702 | -11.8138 | -45.37001 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45ee0d6d-11a3-3e75-9d6f-3ee24707755a | -11.83011 | -46.59471 | 2026-01-17 04:27:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d272bb57-94c7-307c-b4f9-be8136e9396e | -12.09602 | -43.95803 | 2026-01-17 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efbdd698-dd61-362e-851d-f533f1c62f3c | -11.80672 | -45.54728 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f521852f-0322-3c81-b41e-480eb9f7c920 | -11.96598 | -44.51399 | 2026-01-17 04:27:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e3ea79d-e821-39c9-926e-6d09bb38e3b7 | -15.97198 | -56.27724 | 2026-01-17 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b71cec4-9f8b-3fe1-8a8a-fdf01e6d3f0f | -13.52725 | -43.52541 | 2026-01-17 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f314efb7-848b-3d72-9ea9-86ca22fe2869 | -14.70739 | -48.90294 | 2026-01-17 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b56a6e0f-17c6-3536-a019-b6710cb9a060 | -12.19837 | -43.95015 | 2026-01-17 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0e6cc73-17b3-35f5-adad-61968d25bc1d | -15.82326 | -48.12357 | 2026-01-17 04:27:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e8d6188-bf5b-3c78-9807-4b067854bf26 | -12.66168 | -46.76721 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0df3c8d3-1ecd-373a-b7f5-823c38e44cca | -14.74701 | -45.91192 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20aee0dc-79b4-3def-9991-e7cfc8950b9a | -11.8188 | -45.35986 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce6c4536-ae8d-3c13-ba73-8abcfd9f3512 | -16.09562 | -45.17454 | 2026-01-17 04:27:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59f73f6e-1fbb-37a3-8d95-0a85bf5a3b7c | -14.74981 | -45.91609 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93392542-348c-3820-a9da-9e44466d454c | -11.83822 | -49.19965 | 2026-01-17 04:27:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7925f1b-9ac5-3ab9-a32f-b5236292d3e5 | -11.83893 | -49.19546 | 2026-01-17 04:27:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c195ff99-f22d-3a4d-bf55-6748510fbc2c | -13.9521 | -48.5105 | 2026-01-17 04:27:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac945c92-9a6a-3a76-a7ab-a66808006236 | -11.52904 | -47.693 | 2026-01-17 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e5a8b4b-db73-30cd-a1e4-9d6e1a07b3a8 | -11.8375 | -49.20384 | 2026-01-17 04:27:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0578de8a-4b82-30a0-aaa0-e6bc29a05891 | -14.71095 | -53.95957 | 2026-01-17 04:27:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 928ff6fc-4645-3801-a546-19f41fcd8ff0 | -12.65303 | -46.76617 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ad1fdc0-9258-39b6-9a99-24622a41319f | -15.96674 | -56.27617 | 2026-01-17 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 985de416-7526-3f8f-bd12-f56859bd0535 | -13.53084 | -43.52596 | 2026-01-17 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a1593e7-3d91-3514-b71f-4dd753c1b046 | -20.72777 | -55.161 | 2026-01-17 04:29:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d3a25f8-5589-37ec-9552-077102ecd2e1 | -24.95756 | -49.29218 | 2026-01-17 04:29:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82ff1c9f-f079-3e00-a2b7-0b450caaca85 | -23.44841 | -49.65675 | 2026-01-17 04:29:00 | NPP-375D | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7bd7d1ec-ccb9-365c-ac9b-51c20827d763 | -20.45411 | -57.88416 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d5cd6803-ecc3-3592-b5bd-f067d7f73cd9 | -20.44355 | -57.88151 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8e6dc475-4f99-3acf-8e98-ffd8abde5957 | -18.8226 | -51.60616 | 2026-01-17 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47c96c31-fb1c-380a-aab4-ecc1399924a0 | -23.52184 | -46.97334 | 2026-01-17 04:29:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 771b503a-54be-3609-932a-419ad54a2eda | -23.20939 | -49.41241 | 2026-01-17 04:29:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37d52657-0494-32b7-a286-7769655105d5 | -20.43223 | -57.88238 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a1d744a7-413b-333f-9af1-6ca7fb32242e | -22.8276 | -47.1489 | 2026-01-17 04:29:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0188698c-27c3-3958-9a77-f21e0c582b99 | -24.9609 | -49.29282 | 2026-01-17 04:29:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1550401b-6a8b-35bd-baa8-b2fd051ce285 | -20.43299 | -57.87887 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e8c331bc-3b2c-331c-963c-33fcfadee02f | -18.81888 | -51.60542 | 2026-01-17 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 214a22fa-c12e-3c69-bde3-3ea8c0e224d3 | -20.45486 | -57.88066 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d25b30bb-13ea-3e06-b4e8-0ebcf768a7e9 | -20.43827 | -57.88019 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 956935a1-e7e1-38a6-9429-f1cf4ad2ab50 | -20.43752 | -57.88369 | 2026-01-17 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3fd3adac-941a-322d-abab-de739a6060fd | -18.19504 | -54.49448 | 2026-01-17 04:29:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbef2d1a-cd96-3eaf-8fb3-c7eb90832f2c | -22.84321 | -49.57981 | 2026-01-17 04:29:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 890e28d4-cf8c-301d-843e-d0ac24b6c7f2 | -22.84986 | -42.16756 | 2026-01-17 04:29:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ad1d085-482a-3a67-b659-a2eabfa34b8c | -13.6993 | -55.6773 | 2026-01-17 04:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 3376bee7-6c10-3572-8a00-8921d53038a3 | -6.5631 | -51.1126 | 2026-01-17 04:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f6be69ea-58e7-3dc2-8adf-45d7e455655d | -25.72021 | -51.59369 | 2026-01-17 04:31:00 | NPP-375D | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4569cdcb-d81d-3bf1-b508-709437f38065 | -13.6993 | -55.6773 | 2026-01-17 04:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| fd5e98a2-3509-3ef7-b32b-1c7512a287c5 | -1.50549 | -47.33055 | 2026-01-17 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d94c0247-c593-3c08-8f67-55c8ccf7d92f | -0.97382 | -46.79809 | 2026-01-17 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d3cd2f7-2f63-333e-bb61-076d4d3e3c83 | -1.36533 | -46.63898 | 2026-01-17 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a712fc04-c1c9-3415-af6d-ef2adca44fc7 | -1.01493 | -47.9871 | 2026-01-17 04:44:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad18d408-6586-32f4-9e8e-a1293e17f5d6 | -0.08777 | -51.28085 | 2026-01-17 04:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bcd378e-b2eb-3f6f-83ee-423a5b2fc80b | -1.67324 | -46.70414 | 2026-01-17 04:44:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60b5c06-6aad-3b48-9f98-234b53012378 | -0.08834 | -51.27724 | 2026-01-17 04:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b05512e-1913-324d-9be2-1edc51cc3c4d | -1.724 | -54.31209 | 2026-01-17 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f825aeb4-032e-39d0-8c75-d6f8f0a156fd | -2.9281 | -48.23196 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f43b8ea5-d3cd-3d3b-83c1-237bc594f269 | -2.92869 | -48.2282 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4da6b928-7f14-3ca8-8922-2769714a44fc | -2.95945 | -54.3417 | 2026-01-17 04:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6371b70-36aa-3bcd-9428-678e7fcf3f2c | -8.43357 | -44.01332 | 2026-01-17 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11f5c0b4-ea61-36ec-99d7-198371fb2fe9 | -8.98139 | -48.08034 | 2026-01-17 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4495a40-6102-3cd1-a68e-4d3729423188 | -5.31093 | -45.16954 | 2026-01-17 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f2e2665-642a-351e-87a4-fd7334ac1507 | -2.92927 | -48.22443 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25174915-54ef-3bc8-a135-5608b234f9d5 | -2.96847 | -54.3336 | 2026-01-17 04:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f91ac7b4-99fd-3c25-97e5-e57cc856e8b7 | -6.94709 | -45.85065 | 2026-01-17 04:46:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 498e79b3-b1ec-31ee-ba3f-4ff9ae1aae6f | -1.97052 | -54.54731 | 2026-01-17 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 756e24d0-4e3f-3a9b-92d1-7f935067bec2 | -8.26048 | -48.2862 | 2026-01-17 04:46:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df9cf5e8-ef04-3d64-a04e-3702009cab4d | -2.92751 | -48.23573 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65f2671f-2326-3e47-9c59-4a995a2be953 | -2.93214 | -48.22874 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16d296ab-203d-3f47-8c80-03c57f81bd3f | -1.87414 | -54.24708 | 2026-01-17 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7208a146-608b-328b-866b-60f01467b455 | -6.94293 | -45.8501 | 2026-01-17 04:46:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef62ff82-56bb-340b-869a-69201098eb40 | -6.37636 | -43.81799 | 2026-01-17 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4673311b-2c1f-3c6f-b74e-53f89808bb9c | -8.97343 | -48.53961 | 2026-01-17 04:46:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 404e7d10-7940-34a3-9e1f-fdb48f227684 | -8.43282 | -44.01873 | 2026-01-17 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85d86dfa-d3fb-33fe-9413-90e94553d99b | -8.26477 | -48.28249 | 2026-01-17 04:46:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cab7a21-e87c-38b3-b0ca-faf5696f0493 | -8.44625 | -45.12655 | 2026-01-17 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e080777e-789f-32c0-bb3e-8d937a9d5d6e | -8.26113 | -48.28195 | 2026-01-17 04:46:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 026171dc-927c-3e2f-af85-9500cdf23353 | -3.43096 | -49.22785 | 2026-01-17 04:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 093eff79-aa31-3d38-a4ee-7f464351367e | -3.93618 | -47.20811 | 2026-01-17 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58cbb747-f17b-3f06-bb23-ea8442e6a003 | -2.58052 | -54.72753 | 2026-01-17 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0997334f-83d5-3c40-92b8-539baba11530 | -7.23885 | -44.26934 | 2026-01-17 04:46:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30f13519-841b-3961-b62a-9dafd7ec582d | -3.88507 | -47.58985 | 2026-01-17 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 732947c5-6084-3935-8eb5-726685663044 | -2.92406 | -48.23518 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b40a1fe-8600-3097-b776-f59d668aa752 | -4.89627 | -49.92774 | 2026-01-17 04:46:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 912f16e4-1652-3d7e-8df9-b4aba0d2f187 | -5.43296 | -44.03689 | 2026-01-17 04:46:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e240da7-0d20-3398-86c4-2971fb95bfff | -5.47456 | -45.40991 | 2026-01-17 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8699677f-eb0e-35b3-961a-43c0f5ecdb00 | -8.45072 | -45.12703 | 2026-01-17 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f8cbbb8-744d-3496-b0c2-0752bda98f59 | -8.97767 | -48.07983 | 2026-01-17 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcfcf556-9f3b-360d-b8c2-c9c1a3e0e903 | -2.1486 | -54.39497 | 2026-01-17 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 975a4da4-7b80-37f4-9c65-fdbe34c275d8 | -8.2562 | -48.28994 | 2026-01-17 04:46:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 428baf93-58e5-3693-98f2-69aaa5f12056 | -1.60141 | -53.98911 | 2026-01-17 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)
