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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e56bc21-91ec-389f-90e7-10416c6906d2 | -15.1575 | -56.47892 | 2024-12-10 05:42:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2accfd6-3974-31fb-b4f5-4c00e096fcaf | -13.48435 | -60.35147 | 2024-12-10 05:42:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3c400e8-ac1d-38c8-8af8-c019489f5c3a | -12.54815 | -58.36996 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 54b4d621-2545-33c9-9337-f3360226e99f | -12.04097 | -62.78702 | 2024-12-10 05:42:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b24144bd-3dd9-37b1-a33c-309767efaac7 | -12.55955 | -58.35972 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ac999cce-55b5-3075-98c1-9d893198d432 | -12.04467 | -62.78755 | 2024-12-10 05:42:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a72fef2-e066-3b99-873b-ea07e5d0f8af | -12.55958 | -57.76453 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f496c39-4967-3c8c-bce5-2a7df258ba35 | -12.55108 | -58.34688 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fa6aa59a-ed8c-35a1-8ef6-1a2ab92294bb | -15.07884 | -59.63504 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9af4dd8-8554-3dd5-a9ea-0c51932414cb | -15.08763 | -59.64139 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0124d8f7-7640-316d-9572-4e33574bc70d | -12.53966 | -58.35719 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf8e7ad6-95d0-3b33-b527-0f4aac93e6a3 | -14.16243 | -60.20017 | 2024-12-10 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9f8ea9-e4f6-3880-9bb4-430e19aba290 | -12.56992 | -57.76586 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0953a3e3-1613-3a6b-86af-5254f79313ce | -12.5425 | -58.3561 | 2024-12-10 05:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 28a42bdb-ef3d-324f-b4f8-1e74d05c8f41 | -12.5427 | -58.3362 | 2024-12-10 05:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| b05b8af7-0d17-3540-bd5a-2dc262bec404 | -12.5615 | -58.3546 | 2024-12-10 05:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| fc2c3cbd-f2d3-3763-a98f-3e89d843adcf | -12.5617 | -58.3347 | 2024-12-10 05:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 93c2d17f-2f0e-36ff-85f3-5f373e72a2d8 | -4.3959 | -47.7618 | 2024-12-10 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 40b405cc-c10a-3278-8ef9-8d6e1691454c | -2.9859 | -52.8554 | 2024-12-10 06:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f7d02392-3b59-3ec3-b438-62395e8f1a61 | -4.3959 | -47.7618 | 2024-12-10 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 0c74cb31-6356-36d0-b935-6af90679c838 | -4.3959 | -47.7618 | 2024-12-10 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1aefe2ae-8c2d-392e-a792-ecc66f960ab3 | -4.3959 | -47.7618 | 2024-12-10 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 2eef733d-a6a7-3ef3-9cdc-d8d7b136e379 | -4.3774 | -47.7627 | 2024-12-10 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d18efa0a-ca94-3017-9161-268ae11124dd | -6.9346 | -43.5168 | 2024-12-10 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a52e64e7-3c61-36f9-857e-d5a1166eb829 | -6.9344 | -43.5401 | 2024-12-10 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| e8b341fb-d974-36f9-b21c-9a8ea1cdc28c | 3.22807 | -61.19108 | 2024-12-10 06:24:00 | AQUA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a536e782-8592-3997-8956-1c9fa0276232 | -2.99621 | -52.82965 | 2024-12-10 06:26:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 07be5a6f-0426-3a60-8dd4-9152b3106a1b | -2.91772 | -52.95918 | 2024-12-10 06:26:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4d532962-2a8f-3cc7-b38f-1c86c27ed434 | -2.99233 | -52.85721 | 2024-12-10 06:26:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 4fc26696-442b-3ec5-9286-42d1c02ce368 | -2.91683 | -52.95448 | 2024-12-10 06:26:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 961c5fe1-98da-3f37-a556-e864a5990c05 | -2.81027 | -52.95968 | 2024-12-10 06:26:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 47c917b2-0e22-3eb8-ad43-4f21e42dd7e5 | -12.5356 | -58.35191 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| d8427c2c-37a2-32ed-ab6b-1754df09f1cf | -12.5601 | -58.33966 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d9d0bf00-f63e-363f-9da9-f9ebfd82eea7 | -15.08427 | -59.63885 | 2024-12-10 06:29:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9e9a414-dbcc-38ae-b954-a7d8703eb165 | -12.55805 | -58.35481 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 496680f8-1da4-3ca6-8f87-38634d4d9bb0 | -12.55695 | -58.36182 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 440833b3-96f1-3db1-a997-8daa8c63b381 | -12.55888 | -58.34665 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| a26de571-d6c2-3484-a1d0-e06cf3c31fcd | -15.08601 | -59.62553 | 2024-12-10 06:29:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 08552c66-2fa4-32e7-a915-91f30338b0ef | -12.54763 | -58.34533 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| f19c602e-e3c9-3c6a-8816-fa5c0c4ba6fc | -12.54883 | -58.33839 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 38997fe3-04f5-3ad0-8902-c9825a1d2dad | -12.53759 | -58.33697 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| fb4c8f48-fb89-35c0-b097-81452269933c | -12.54681 | -58.35345 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| f53cd141-9a6d-3b37-851e-72aa103c787a | -12.54481 | -58.36838 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5311187c-bfd5-3c23-9fcf-47022e82686a | -12.54572 | -58.36038 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 3a41a082-3d64-3d65-b9f2-095c5733eba3 | -12.54954 | -58.33024 | 2024-12-10 06:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a1defe83-0a21-3ecb-a860-f9ec9adec013 | -6.9346 | -43.5168 | 2024-12-10 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 79764163-29bf-35cd-bb2e-212ae7453343 | -4.3959 | -47.7618 | 2024-12-10 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7fb0fa11-c314-3764-8d67-c65091c2a976 | -6.9344 | -43.5401 | 2024-12-10 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d5404781-85fd-32f4-b922-c24b6c9c2448 | -4.3959 | -47.7618 | 2024-12-10 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f22fe67c-5a1b-3731-a6c8-1f68156416d4 | -4.3774 | -47.7627 | 2024-12-10 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0cba5aec-6afe-3063-a65f-6b5c82ba0dc6 | -6.9344 | -43.5401 | 2024-12-10 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| dcbe5c63-adc1-3c3c-97b9-42948c7c2469 | -6.9346 | -43.5168 | 2024-12-10 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| af5d9122-a636-35db-92c7-33d0b228a063 | -2.9666 | -53.1201 | 2024-12-10 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 24058c79-c623-3b87-ada2-0fe0d0117a52 | -4.3959 | -47.7618 | 2024-12-10 06:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 25c9c9fe-d224-3548-b980-20389633397a | -4.3774 | -47.7627 | 2024-12-10 06:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 84e550ab-3e0c-3eb1-8236-50038284488e | -6.9344 | -43.5401 | 2024-12-10 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 158.2 |
| c7de6674-ad6e-3f83-98ed-8d6277553135 | -6.9346 | -43.5168 | 2024-12-10 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3c5fa87f-af51-3e67-9cca-ecad890e7c8c | -6.9346 | -43.5168 | 2024-12-10 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 50cb7e89-852b-37ae-807a-fd9539c55240 | -2.9666 | -53.1201 | 2024-12-10 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 83847f52-061c-3c85-8f9b-67f174866ad4 | -6.9344 | -43.5401 | 2024-12-10 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 70e6103d-5678-3f90-be16-08dc6a8fd442 | -6.9344 | -43.5401 | 2024-12-10 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 3a1f7038-954f-3265-94a4-97e2ad4f4df6 | -6.9346 | -43.5168 | 2024-12-10 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4ade808a-5b82-3152-8906-e69438a4bbb6 | -6.9344 | -43.5401 | 2024-12-10 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 7138f522-3da8-341d-8523-ef942629bfca | -6.9532 | -43.5384 | 2024-12-10 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 6856e2e7-1eb9-3f62-9841-c55edc360c0c | -6.9346 | -43.5168 | 2024-12-10 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 39821a24-ca73-3c29-b5cd-4b28ad5e4e00 | -6.9344 | -43.5401 | 2024-12-10 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e8c32ed1-2d54-3320-9286-e1667c7341bb | -6.9532 | -43.5384 | 2024-12-10 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d02e044a-703f-3f56-8545-d2f6fa995985 | -6.9346 | -43.5168 | 2024-12-10 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| fd2ae8f6-a2d2-3290-bdf8-1e1426e67a1d | -6.9344 | -43.5401 | 2024-12-10 07:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 33af1c2e-be03-3ea2-9a30-8f1f91a63eb0 | -2.89046 | -41.92432 | 2024-12-10 12:18:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9f831401-17b2-3327-b4df-5c8cdc85391f | -3.23403 | -42.42697 | 2024-12-10 12:18:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 50347a8a-df05-319c-8f0a-7ed5df6e4112 | -4.04066 | -40.2199 | 2024-12-10 12:18:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 8030af55-9651-3e97-aa42-69215d2acf65 | -3.55204 | -40.60295 | 2024-12-10 12:18:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| a94e0946-7358-3a4a-a889-fe8cfee1fe33 | -1.64773 | -45.91486 | 2024-12-10 12:18:00 | TERRA_M-T | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4f1fac46-f5c5-38a9-a6f6-745ebdab431c | -4.03931 | -40.22934 | 2024-12-10 12:18:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| c1d11a8b-7b34-3914-9039-eb814cb842c0 | -2.94143 | -41.19777 | 2024-12-10 12:18:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| c484d178-dc56-3a97-ac1d-91ac1e114a49 | -3.2935 | -41.25369 | 2024-12-10 12:18:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 26.3 |
| f1c23460-5a10-30fd-b671-bbd9dfa98569 | -3.22406 | -41.40802 | 2024-12-10 12:18:00 | TERRA_M-T | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 131b6de5-8577-39b9-84ba-39e58f6adeff | -3.11019 | -41.94667 | 2024-12-10 12:18:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7fbe0402-91f0-3c67-874c-2ec021d3410d | -3.09313 | -41.09883 | 2024-12-10 12:18:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 4052ac6a-b01d-3606-9106-8355f9bd0dbb | -3.1001 | -41.9542 | 2024-12-10 12:18:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| ed2a3396-546f-3bd6-ac7a-f625a4c85137 | -4.18169 | -38.35707 | 2024-12-10 12:18:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 91997ed8-9aa2-3210-baad-87d125a32361 | -3.10892 | -41.95544 | 2024-12-10 12:18:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ffcb2c93-72d3-35cc-94d7-2adedd17d4e4 | -3.85553 | -42.27169 | 2024-12-10 12:18:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 3707cb26-e54a-3a18-b294-96f79faf44d2 | -3.09441 | -41.08999 | 2024-12-10 12:18:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 30d25e7b-48ae-33aa-89c1-60a37e777268 | -3.10137 | -41.94543 | 2024-12-10 12:18:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0bea106b-cfe9-3181-b178-6c450224d246 | -2.94016 | -41.20658 | 2024-12-10 12:18:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 553e2ecf-4391-36ae-9fe8-0a64462acb3d | -2.96877 | -41.95923 | 2024-12-10 12:18:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 10.1 |
| bb9b9bbf-083d-30a8-bf91-aeb14e4b33ba | -2.95026 | -41.199 | 2024-12-10 12:18:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e16316b4-baa9-398a-aca1-9bf15dee1d0b | -3.23532 | -42.41807 | 2024-12-10 12:18:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f72bf19a-45dc-3feb-a62e-6a8d9b6a68f1 | -8.23132 | -36.48 | 2024-12-10 12:21:00 | TERRA_M-T | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 3381ae63-2de8-335b-b5db-be4e954db9a5 | -7.07256 | -39.04241 | 2024-12-10 12:21:00 | TERRA_M-T | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7618cb73-b11d-3891-accb-170f2f88a7a5 | -7.0709 | -39.05436 | 2024-12-10 12:21:00 | TERRA_M-T | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 4326782d-c3dd-3034-9f1a-a461d4730630 | -8.97929 | -41.01583 | 2024-12-10 12:21:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| f4144b66-a31d-3999-ba63-fb5a0483f1ee | -7.87664 | -40.92796 | 2024-12-10 12:21:00 | TERRA_M-T | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1eeb3a93-dd77-3d3e-8e13-4f4eb97af76a | -8.37932 | -36.87762 | 2024-12-10 12:21:00 | TERRA_M-T | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 43.2 |
| 68887c8c-266a-3702-9b4b-f5036e32ccc3 | -8.23368 | -36.46188 | 2024-12-10 12:21:00 | TERRA_M-T | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 77.2 |
| c0e96624-68b2-3783-98ac-2104942dd096 | -5.00608 | -39.98236 | 2024-12-10 12:21:00 | TERRA_M-T | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3ecba526-8ad0-32ba-8bed-c82058ae26c8 | -10.78603 | -42.77844 | 2024-12-10 12:21:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc4a3983-1f53-3142-b6b5-66003f51275d | -7.23203 | -37.28986 | 2024-12-10 12:21:00 | TERRA_M-T | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 19.2 |


[Clique aqui para ver as próximas entradas](README41.md)
