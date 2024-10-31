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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 813c8d63-b28e-3bec-af3a-c0ef7b8bbc8b | -29.81398 | -51.17722 | 2024-10-31 04:55:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| ad3cc696-f223-3eda-a26e-d89b3841f807 | -24.23216 | -52.86744 | 2024-10-31 04:55:00 | NOAA-20 | JANIÓPOLIS | PARANÁ | Brasil | 4112207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fdb6cf4e-da45-3f29-a440-16e034f1c986 | -26.56377 | -53.56775 | 2024-10-31 04:55:00 | NOAA-20 | GUARACIABA | SANTA CATARINA | Brasil | 4206405 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e7bdb129-d266-33d9-9118-babeb7c0d7be | -23.99633 | -54.10215 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a26b43b-5280-318e-80ec-fb532b559170 | -23.99282 | -54.10157 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6824b726-91c3-3869-975a-a4d163cdcd37 | -23.98931 | -54.101 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 0d6e0e03-5478-3fd0-9073-99f312e3f8c1 | -23.9858 | -54.10042 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 7b0b7b28-9f49-3c8a-86c0-21dc6d073443 | -23.9823 | -54.09985 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| f8ad739b-dbf0-3223-91f5-1686b499d2f6 | -23.9817 | -54.10408 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 38dc56f7-bd90-3598-a980-a2ea34c00548 | -23.9782 | -54.10351 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4f07650e-0e9b-3d0e-a8e5-31e3447980c1 | -23.9776 | -54.10775 | 2024-10-31 04:55:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 7d300d23-4eb1-332e-9c8e-bb98ed197f71 | -4.2749 | -43.4357 | 2024-10-31 04:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 21983620-9b90-31de-b0ee-dd9b8ea0bdf7 | -4.8178 | -45.8429 | 2024-10-31 04:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 95229158-4ddd-30ca-b459-a0d30beb56d0 | -6.1416 | -43.9563 | 2024-10-31 04:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8bc73755-58c6-3e72-83c1-2b18292d4fa4 | -9.7419 | -36.0772 | 2024-10-31 04:56:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| cf0c5d31-7bda-3b6b-8fc4-f1e2298a9c8f | -10.1628 | -36.2185 | 2024-10-31 04:56:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| 23dee83e-cba0-38dc-8f23-6c3f620b670f | -10.1623 | -36.2456 | 2024-10-31 04:56:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 139.3 |
| 75a5c6f1-2bfa-3025-a1a8-d95b2c44d349 | -10.1816 | -36.2421 | 2024-10-31 04:56:03 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 164.9 |
| baa82d51-69ab-338f-85d9-e16447beb383 | -10.1821 | -36.215 | 2024-10-31 04:56:03 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 114.9 |
| d72c067e-cc87-357f-89bb-4ca9e97566a8 | -12.4206 | -63.2682 | 2024-10-31 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4eebe3cc-4f73-3ef6-885f-cb63c71c6726 | -12.4393 | -63.2864 | 2024-10-31 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| eadbbfe0-a257-39f2-818a-5bc986701193 | -12.4395 | -63.2672 | 2024-10-31 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f75abbf1-e6c3-3caf-a367-95723949cc5b | -19.5087 | -56.5779 | 2024-10-31 04:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 741e1813-3bfb-36b0-8f54-58d2e5be0477 | -3.0152 | -45.5026 | 2024-10-31 05:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| cafced64-32ca-3376-a5c6-3c3c9dc7a988 | -3.0153 | -45.4802 | 2024-10-31 05:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| eb20d1f0-30bf-3723-80fc-849fd7313830 | -4.2749 | -43.4357 | 2024-10-31 05:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e390e5c7-51d8-3d48-abef-08d7783d3f20 | -4.8178 | -45.8429 | 2024-10-31 05:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d8a6cbc0-a091-3b69-8b4c-82ac10b74e43 | -5.0466 | -45.1542 | 2024-10-31 05:05:35 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 3cca4505-0e77-3954-a23d-84768fc688d3 | -6.1416 | -43.9563 | 2024-10-31 05:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4c682771-62ec-3abc-a17c-0a8f43a4f69c | -9.7419 | -36.0772 | 2024-10-31 05:06:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.2 |
| 0df9ba05-8d3f-33bd-89c1-fe1d5380fd75 | -12.4204 | -63.2874 | 2024-10-31 05:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 39e3b118-b164-3fe4-b10f-9b791961a2f2 | -12.4206 | -63.2682 | 2024-10-31 05:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9ec19a7a-b226-36b5-a737-f694c0dd4920 | -12.4393 | -63.2864 | 2024-10-31 05:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 55bb60d6-fbff-3c83-be96-bd79197bb0c8 | -12.4395 | -63.2672 | 2024-10-31 05:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| da8b9b58-eb83-34f7-8e7a-0675ed09edea | -2.5216 | -48.4591 | 2024-10-31 05:15:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d9361a05-de97-3729-b229-c63635cd0d87 | -2.8431 | -46.6871 | 2024-10-31 05:15:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 14f1f0b4-7b4a-3f1b-ab38-f3256942619f | -3.4568 | -50.2992 | 2024-10-31 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 588ccaf2-f6de-3154-981e-253c18696c7e | -4.454 | -44.5534 | 2024-10-31 05:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b68f077e-df40-32f9-a117-78d2d5aa2ae8 | -4.4726 | -44.5524 | 2024-10-31 05:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 9bc4ffcb-8e29-3fec-a6a8-09e5a8b35a07 | -4.8178 | -45.8429 | 2024-10-31 05:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b0b243fe-04f6-3306-850c-905126489560 | -4.8364 | -45.8418 | 2024-10-31 05:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ce54e035-0f90-35f5-ab6d-4179c70f580d | -6.1416 | -43.9563 | 2024-10-31 05:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4ff03ce0-6bcd-3a80-8df9-aadd70636353 | -2.5216 | -48.4591 | 2024-10-31 05:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f4cb3ac5-0763-3811-8e11-1b18d24cd8c8 | -2.5225 | -54.0791 | 2024-10-31 05:25:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2309640c-0f4c-32b3-aad2-d2aa1f55f45f | -2.8431 | -46.6871 | 2024-10-31 05:25:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b3788c41-e708-3fd6-8669-063e808974ab | -4.454 | -44.5534 | 2024-10-31 05:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2fe4583f-32e4-3870-b83f-c4af3292a3b2 | -4.8178 | -45.8429 | 2024-10-31 05:25:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 6651a00a-db66-3b8b-8dd8-edc2a7a0e192 | -5.0466 | -45.1542 | 2024-10-31 05:25:35 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b52986f1-6bdc-3de1-a57a-0c113ad030d8 | -6.1416 | -43.9563 | 2024-10-31 05:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c89db3c4-b49f-332c-bede-5f094ec465c8 | -3.2209 | -45.2475 | 2024-10-31 05:35:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 313a4dc4-cb41-3a37-811f-1a888e7d8755 | -3.2535 | -50.3479 | 2024-10-31 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f6817935-7ac7-3b5e-8488-d2bc5c8ff055 | -3.2719 | -50.3473 | 2024-10-31 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5cfb244b-0b03-31f8-97f8-b362eb5f3158 | -4.454 | -44.5534 | 2024-10-31 05:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| da568aa8-7030-3f92-adaa-3d240ac30515 | -4.8178 | -45.8429 | 2024-10-31 05:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e373732b-7a73-3978-a27e-924d9b931656 | -4.8364 | -45.8418 | 2024-10-31 05:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| deeec126-a915-359d-b174-ab1a3e3a5289 | 3.18245 | -64.20384 | 2024-10-31 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acc7509d-fba7-3926-a391-1a4018379512 | 1.13435 | -50.94034 | 2024-10-31 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01eaacf9-74e2-30ff-9cab-871659eaa6f3 | 1.13343 | -50.9345 | 2024-10-31 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60578898-0772-3f02-b4d5-058fce61cfb0 | 1.13164 | -50.94126 | 2024-10-31 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45d6db88-c9a2-3e7e-92fc-e1d24e0b6250 | 1.13067 | -50.93542 | 2024-10-31 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a36cec9-dc24-3c05-86e6-11b872969061 | 3.43784 | -51.24604 | 2024-10-31 05:40:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52dca9bf-09d3-35c0-8aff-bb3c12db3c8d | 3.43154 | -51.24719 | 2024-10-31 05:40:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a568d6d-850e-3a6a-9c4b-45eebc4ece49 | 3.35358 | -51.36033 | 2024-10-31 05:40:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71209eee-b304-32e7-a940-0d45aa17221c | -0.69339 | -51.68238 | 2024-10-31 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f902a6b5-9edf-381d-961f-9b0f16523d3b | -0.16068 | -51.55796 | 2024-10-31 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88fd2f10-1aed-309d-b3fd-084fdda9734e | -0.15979 | -51.56351 | 2024-10-31 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be280361-5984-31c0-8a91-febd70895203 | -0.15958 | -51.56253 | 2024-10-31 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b2e747e-20b9-3b95-b6a1-463edd7e8465 | 1.68901 | -55.88827 | 2024-10-31 05:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 976e0239-9b1c-3fc3-84e1-cac129f87e61 | 3.94792 | -59.80958 | 2024-10-31 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 458c274e-a373-31be-a88f-902c929ad891 | 1.12652 | -59.4448 | 2024-10-31 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c6335ba-83e3-356f-bf0e-1054eed4d7f6 | 1.12579 | -59.44019 | 2024-10-31 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5866c7f-30ea-3163-a245-3c9900b97b2b | 0.97629 | -59.60065 | 2024-10-31 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba9c5c67-7d11-3d1e-8720-852082595897 | 0.97558 | -59.59613 | 2024-10-31 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d461fe6-81bf-36b3-bcd9-9082ec18542b | 0.92306 | -59.55721 | 2024-10-31 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d55639ab-de15-31eb-99ee-fa1621525c20 | 4.96627 | -60.30228 | 2024-10-31 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9fbd819-43e7-3513-9d91-a02944307648 | 1.72316 | -60.67508 | 2024-10-31 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 408e1d2c-a560-338f-bac1-16794ca7c1d7 | 3.55924 | -61.84191 | 2024-10-31 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 873b2bbd-cb5a-32a1-abc4-167d53b46f69 | -1.89318 | -52.06279 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d912ef5-d30d-3c5d-91e6-ca7838660fea | -1.89311 | -52.06324 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9871d5df-f911-38bb-b33e-ce58db7d64dd | -1.88671 | -52.06166 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 403e8468-18b3-3b27-8cb5-60470b48908d | -1.88664 | -52.06215 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a785e2d-2953-397f-926a-eaa2c710bb85 | -1.85675 | -52.04034 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40546147-970f-30ec-8b5c-4cd52104b4d3 | -1.64826 | -52.58468 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28396cce-5dc1-39de-b14d-7ed40b0b5cc2 | -1.64275 | -52.57872 | 2024-10-31 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f4b4e24-b6b3-3d91-bfa5-0f56241558b1 | -1.44157 | -52.26811 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e856edba-1f24-35b8-be78-c6d08218b9b1 | -1.44076 | -52.27329 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2e07eeb-2239-3e23-9169-aa27aed94a5c | -1.43702 | -52.27005 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b97b1c7-3040-35cc-ba99-4583e9b433b3 | -1.43625 | -52.27524 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7ad0b79b-53df-34a9-a468-b3f7334fe5b2 | -1.4344 | -52.2723 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 282fdf88-27ce-31cf-bea6-6bce003d6ad7 | -1.4336 | -52.27748 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c46639f-ee21-3df1-9bcc-abbfa93ce978 | -2.20104 | -53.72521 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| beb7b359-3f9f-3c10-b72f-ec6da14c9967 | -2.19582 | -53.71984 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5647785f-9369-3c76-9220-41083c3e3fbf | -2.19519 | -53.72414 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aea4edae-49a6-37e7-b6a9-9ad53c408e7f | -2.19106 | -53.58733 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692266a0-569d-3a36-b978-34196c076016 | -2.19047 | -53.59139 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 505149e7-7c4d-3d2a-b5af-44f2e4d31b52 | -1.46886 | -54.21317 | 2024-10-31 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93dc9860-c418-3157-a27f-52e5d0b2b565 | -1.4683 | -54.21692 | 2024-10-31 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a94a00-953d-3460-81ee-117a15f466c3 | -1.20633 | -53.77869 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00a6ed72-6f07-33ce-8087-f532fb9e1701 | -1.20055 | -53.77789 | 2024-10-31 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e251e340-d8bf-3c96-bfa1-25133d6cb38e | -1.15417 | -53.3823 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README46.md)
