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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70ebc912-2167-3026-aac6-8f5c999816f5 | -7.80569 | -61.35342 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 150cc22e-c079-3610-9ae7-714d040cb39c | -7.56109 | -61.37473 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d58b2ccf-d0e7-38d5-89d1-1bf5afce7efb | -6.9253 | -62.90664 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4d1270e-bd27-3c6c-b767-c87032892ff1 | -15.35226 | -53.92374 | 2025-08-24 05:23:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e735c27e-0ac7-37e2-93bd-046f5d6bbf53 | -23.32232 | -47.84024 | 2025-08-24 05:23:00 | AQUA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| 05498d79-0f79-350b-8764-04bfc18d3c29 | -5.64819 | -51.84378 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03648f53-c359-32da-9801-44fb25b32853 | -3.83911 | -55.96846 | 2025-08-24 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb70d4c-46b4-3e77-afcf-7eb8f22fc0f4 | -3.59995 | -47.52372 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 803c4755-14aa-348f-9b9d-bab22d6acdf1 | -6.92469 | -62.91044 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a9d5e16-a291-3abf-b598-612e317e71a5 | -7.17199 | -60.65503 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd31eccc-d603-318a-99d7-9896aae2e4ff | -3.65964 | -54.75695 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360f1667-c99f-3a38-aece-b78adcdbabf6 | -4.95598 | -55.81865 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 37a68a1f-d3c6-3656-9a06-963b86d3b446 | -14.82032 | -55.97515 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d16b15b0-7f16-3e03-ab35-108f7a92b44b | -13.62238 | -48.17311 | 2025-08-24 05:23:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1bb28ed-1e26-3312-98d4-7c60ed0ed609 | -6.3095 | -59.87561 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3958481a-1c35-3208-9c8c-a3b0a7419872 | -13.18502 | -51.92125 | 2025-08-24 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6225f9c8-dd5a-3e64-ba03-1ee2b39e7923 | -6.31282 | -59.87611 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04a29f07-5d18-3434-97bc-3475e8088354 | -15.33763 | -53.91534 | 2025-08-24 05:23:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 529c71e1-ccae-3019-9a23-0e59f4602247 | -7.57049 | -63.44321 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849b1c3d-8e7d-3de0-b672-27e6f48947b9 | -2.92771 | -53.69658 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d96dfdbc-a335-3fb6-a697-44d8a01d93b7 | -10.95549 | -63.01153 | 2025-08-24 05:23:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a406f24d-1f33-3715-9111-dfb4dcf37063 | -8.11143 | -47.14252 | 2025-08-24 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8e8b0b41-961c-35b1-8c4f-1bf37420294d | -5.74434 | -57.58223 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b7cc2fb-c68c-390d-b2c6-50bff8c46902 | -5.60685 | -60.24135 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c183b9e1-7160-3bf3-b9be-adf71a5195be | -7.50598 | -63.83591 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3e00c64-2e5b-3950-a935-a1edc3ca8d85 | -7.54951 | -63.83895 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5de77adb-e075-3b71-8526-675a0ce00005 | -5.64862 | -51.84073 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02682e4c-f957-3bf0-93b9-e38293f4497e | -8.83999 | -49.90342 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbd7b38a-b2ff-38d5-add1-598a64d11617 | -8.83938 | -49.90809 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9617fc4b-b17e-3c31-9797-6e2baa6c32cd | -5.74131 | -57.60244 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeb3951a-d137-3305-92bb-d0912f21f101 | -5.61288 | -60.22461 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efdf1615-6753-37cd-b5fc-dc605ece0df8 | -3.90163 | -54.68977 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72ce46e9-662f-33a9-bffa-e8af2867ec8c | -5.87574 | -57.76533 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb5c07e-6c51-3c7f-8c9f-04e1cf8e5920 | -9.68107 | -48.34507 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd64d7de-d490-338d-b6d0-94a318d477b1 | -5.42818 | -60.16757 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ecc3b465-b5e9-34df-b7f9-383fa8164590 | -11.7049 | -60.18506 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f23f883-d259-30f8-88f7-60737da4b005 | -9.68055 | -48.34949 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62bf19b6-bfeb-3e60-a2e0-8efea6788796 | -5.80177 | -59.21601 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef227abf-65f5-35fc-bf6b-59711f2f6733 | -6.68426 | -58.86109 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b20266-2be2-3f9e-9d77-b38fe2f3d9f5 | -14.8153 | -55.97895 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b25cbdba-41cd-31b2-8d7b-ca6dba61d361 | -4.31183 | -48.10152 | 2025-08-24 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9827ba4-2ba1-3f02-b4c7-1a00692bce86 | -5.4482 | -60.19198 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9701898f-02f6-3e58-9dde-218129f86079 | -5.42542 | -60.1636 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13b21aa7-819a-341c-b310-9057ffa62669 | -4.04897 | -56.31606 | 2025-08-24 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ffa59bd-edc9-3354-a52d-f9ba4a201b5f | -9.02176 | -47.65305 | 2025-08-24 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f8d93c4-9d75-3c60-9763-cb7034cf02e1 | -5.42433 | -60.17051 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d684917a-6bc0-3ce6-ae79-2ec2ecd3d612 | -11.70208 | -60.18084 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c6e1a93-4804-3210-8b4f-40e149bfce76 | -7.06013 | -59.23948 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f29e2dd-552b-3e20-b555-f14e949bebcf | -6.42938 | -53.38128 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 721191a0-80d5-3895-b4dd-d4bd2c38480f | -7.60903 | -60.83426 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d6d21d8-6644-3c9d-9f23-5060e90ace71 | -2.71355 | -54.95665 | 2025-08-24 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e472aa19-baf7-31dc-9bc9-0aeb208cda02 | -5.75503 | -57.58388 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf4c1577-fe33-3481-bf1c-a104d0cfc901 | -8.83978 | -49.9054 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3089dc91-1841-33d2-9c31-244bca923912 | -8.76021 | -49.98419 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906e42c5-7825-32e4-bee5-bb79b0513dd7 | -5.61233 | -60.22806 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cdc8f2e-6192-3c83-9812-4baef526ef12 | -8.06727 | -49.65215 | 2025-08-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34a8b1f3-cb92-3c88-a3a0-45c77f1d22dc | -8.0605 | -49.65607 | 2025-08-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de83f4da-595c-3f40-af9b-3cac30bad611 | -5.75259 | -57.60004 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff27444-0dea-3ff5-bf87-88c6a5f162db | -3.78656 | -47.57139 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cadebe2e-b5c6-33d8-97dd-544e9eedfe78 | -7.56827 | -63.43477 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4af8167b-3fd3-31af-a0b8-50607e6f5636 | -9.24878 | -48.19794 | 2025-08-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f355bfad-784a-3714-8b56-0dee9f5a7478 | -5.74608 | -57.59494 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ff8d2a-4f96-38b4-80bd-060b3752554d | -7.50733 | -63.82774 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b112adf1-5755-3967-bb52-54647dd3fe09 | -8.84061 | -49.89867 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e8d371a-df80-3511-ba46-47eb69d60310 | -4.94042 | -55.81628 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8e470ea-1b1f-3f09-a874-95333a8c7e1b | -14.28993 | -60.37454 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89d0858d-78c0-3779-be7a-af006184ab97 | -9.02768 | -47.64833 | 2025-08-24 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a724e85-2af6-347a-853b-d83bdb00a228 | -6.94697 | -59.55624 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 208d34e8-f8ac-3dad-aa73-b0ba9aef46ce | -5.75025 | -57.59144 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dd7836f-cb30-3f9c-a088-ad6b59592e09 | -12.59191 | -60.36142 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 373fcc6b-f810-31a9-a1eb-c032aaa37472 | -7.78463 | -61.57167 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfb4d4a7-20d1-392b-aa25-68f263d997c8 | -5.79059 | -59.22155 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2035b7fe-5606-3ba6-97ff-92ebaf52f564 | -14.29675 | -60.37588 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a770239b-417e-3e11-b6be-d0dea7c86f91 | -6.57433 | -59.87365 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39de4177-85d4-3a8a-9dd2-f29834fe28fc | -14.46745 | -52.04477 | 2025-08-24 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21965ebf-5b43-3a2c-90d2-3c09c786f24c | -20.33616 | -51.70197 | 2025-08-24 05:23:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 30cbbf6b-0a45-335a-a1d5-b11bac790308 | -7.54976 | -63.86002 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 151ebefc-3652-3158-94f1-bd7d1dbeaff3 | -6.90893 | -62.98605 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69f70e1-d1f4-3cab-9d63-f989822bdf4c | -8.84095 | -49.8959 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d2fe646-7604-309b-bb5f-70986cf5e480 | -5.74139 | -57.57762 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 952cae7e-8640-31bc-b26b-279611fda1fb | -5.45536 | -60.18957 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e9f2a5c-3e86-3abb-9bb7-7fee4786531b | -9.02262 | -47.64609 | 2025-08-24 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eef60685-e2fa-3a40-8a55-596c79b985c9 | -12.58907 | -60.3572 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67f10f42-a163-3dd8-bd71-3e43e5f9bda7 | -5.42764 | -60.17102 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 671f62b2-50eb-3189-bc4f-23ca3c93c2d6 | -5.74426 | -57.60703 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b544bf82-a0de-3ec1-bc5d-6ad14aacb99d | -2.70957 | -54.95605 | 2025-08-24 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cb1cf99-7925-31f6-a28a-3469b78a7e82 | -13.0221 | -56.82939 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507d3e45-d0b0-3062-9cf2-f541a3015eef | -2.91752 | -48.31208 | 2025-08-24 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c392476-ee91-31ec-90b0-4348368e5d52 | -14.81528 | -55.97277 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 07146742-90ff-32cd-b6af-d959fff22ba8 | -2.92707 | -53.70073 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 00b41114-5f68-307b-acc5-99971cb13d2c | -14.29276 | -60.37908 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 264cfc50-d33c-37be-a56a-c0a6facea3a6 | -6.87216 | -59.81615 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03066f46-c8f3-351b-97a2-d09f8de16541 | -20.34425 | -51.66371 | 2025-08-24 05:23:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f72f767b-8c49-3c3a-8aee-1107e59a6b3b | -14.33431 | -58.595 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9777d00-bb70-3ff2-ad74-aa9f9e9e45d2 | -5.74374 | -57.58627 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf81b1ba-83a1-3e75-ac60-ca25627f53b6 | -10.98464 | -59.16381 | 2025-08-24 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb87ac9a-18c8-3ac8-a5b4-f6b6b4a3430a | -4.95525 | -55.82353 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 433f80cc-afa7-3e00-bd1e-345d3233b31c | -9.55922 | -68.57695 | 2025-08-24 05:23:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d340365-5ee4-3a85-a967-a60ba5fe5a8d | -14.81589 | -55.9745 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fee7e83c-d829-32ce-b0be-7a611ea58302 | -5.80597 | -59.2238 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README76.md)
