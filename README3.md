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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36ef6118-deae-3b7d-a1ee-ac0ab376ef38 | -1.3006 | -49.1677 | 2025-11-05 00:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 193c6485-0b6e-3244-b514-8dc5c5a4eac7 | -4.426 | -48.9251 | 2025-11-05 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d47b6c85-7ec3-399d-b409-2b027099b7f1 | -6.7399 | -44.1602 | 2025-11-05 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c031c2f9-61fb-33ad-88a9-e0dd6135b28a | -3.4714 | -43.616 | 2025-11-05 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 7d20a8bb-286f-38a4-b3f4-07fc5475967d | -3.4898 | -43.6614 | 2025-11-05 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b4bd1da0-f857-345e-9494-aa2862e6bf50 | -4.4073 | -48.9474 | 2025-11-05 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 893dba56-51f1-30f9-9051-1e237499940c | -3.2503 | -46.8709 | 2025-11-05 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5c60a518-d540-3b12-af33-7edaf1137ce5 | -4.4635 | -43.1919 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c5d27662-0cdc-3db2-8c35-d15f8cf72b60 | -4.4445 | -43.2397 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 88818c88-f76d-3e07-b6f1-cf02f391ed04 | -5.4555 | -45.3763 | 2025-11-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3536ca7d-8438-3b38-93ce-9ac95ba772d9 | -4.4446 | -43.2164 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| cc38b7d7-7f6e-3dee-b13d-c6536b7cf88c | -11.8473 | -43.7256 | 2025-11-05 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0baae126-5a89-3bbc-b7fe-9e3482ce4f01 | -3.5085 | -43.6374 | 2025-11-05 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 6e7db671-1927-3635-87b5-37c03bbd8440 | -3.4712 | -43.6392 | 2025-11-05 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 94897738-9025-36bb-9848-c75d9a209d6c | -3.2316 | -46.8936 | 2025-11-05 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0580f17b-0d7e-3075-85d2-7ddaf7abee84 | -5.4551 | -45.4214 | 2025-11-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 88f7ea60-26d9-31ce-987a-1180ea760753 | -2.7921 | -50.3196 | 2025-11-05 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| be6ada08-222b-360b-92c4-335abf35e23d | -3.7196 | -45.8769 | 2025-11-05 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b3679b54-8684-320a-b61e-221009b8d7e8 | -3.974 | -43.7763 | 2025-11-05 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d9187536-5da8-3f4c-a48a-01e70b1a30f1 | -5.474 | -45.3976 | 2025-11-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8925e222-9c7f-3ce3-a0d7-9ca3c9283347 | -12.2321 | -50.2997 | 2025-11-05 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f87e7ab2-a72e-34c2-b2af-5dfcae1a0a6d | -4.4259 | -48.9465 | 2025-11-05 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| dbd8aa6e-5145-3878-9d03-2dee5eaddabb | -4.4258 | -48.9679 | 2025-11-05 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| f566fd48-69a6-3384-8a77-f104052140d9 | -4.426 | -48.9251 | 2025-11-05 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 9377b0b9-d4b1-3217-8dc1-929d2fb55ccf | -4.4073 | -48.9474 | 2025-11-05 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 38cd17e9-91d0-351f-bc2c-38e28e850104 | -5.4555 | -45.3763 | 2025-11-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| a7ad1c41-eecc-3fd1-b8d2-f5cb5c16def6 | -5.4553 | -45.3988 | 2025-11-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 304.3 |
| 3c81b9a1-1477-3f9a-902b-a8d5dea4573d | -3.2503 | -46.8709 | 2025-11-05 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 166a1c7e-65a7-3c93-805f-77e0477c97a3 | -9.4761 | -40.3862 | 2025-11-05 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 245.9 |
| a3b1c7c8-175b-3881-a09d-7e32a720612b | -3.4714 | -43.616 | 2025-11-05 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| cd577cbb-efec-303c-b2a7-dc91a571030c | -4.4632 | -43.2386 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 321.9 |
| b8a48d52-cba4-367b-b565-57941c314a48 | -1.2822 | -49.168 | 2025-11-05 01:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b8f0dd32-6604-3e7d-9320-c618cec66060 | -4.482 | -43.2141 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 601c0bfa-1d06-31ea-ab31-8f4df85300d1 | -4.4819 | -43.2374 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 529bbc24-b376-3f52-9d59-c75b1ae4d50e | -4.4445 | -43.2397 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 505b1a9c-3cfa-3185-9703-c5510d100db9 | -4.2789 | -45.6709 | 2025-11-05 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 934bc590-faca-3375-ab97-de3e799960a9 | -3.4899 | -43.6383 | 2025-11-05 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 331.5 |
| fc748b16-d1a1-3856-9dee-a7eed2834691 | -9.4765 | -40.3613 | 2025-11-05 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.5 |
| ca1c045f-ffd7-3f83-aebc-b99945b4c7aa | -4.0505 | -43.4945 | 2025-11-05 01:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c3960f90-03ce-3e6b-8007-adf015e7be9f | -3.49 | -43.6152 | 2025-11-05 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 6f394fd9-9e05-3f36-99b4-ff581577d410 | -11.8473 | -43.7256 | 2025-11-05 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 4133a84a-f51e-3fd7-ad1b-44112bfe2382 | -4.4446 | -43.2164 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| ee9c3838-7715-3bb9-9d7a-e4ca64e0e400 | -3.3135 | -53.839 | 2025-11-05 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e0d6f463-6c2f-3393-9e33-7fe22009a153 | -4.4075 | -48.926 | 2025-11-05 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| fcf1c6b7-8b05-3edf-8cae-9f678ba5a3b8 | -2.6509 | -48.4985 | 2025-11-05 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2aebf6ee-be6c-3665-9d02-6e0b48c7c397 | -4.0506 | -43.4713 | 2025-11-05 01:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| dabc4145-3923-3121-81c1-7034d0b85132 | -4.4633 | -43.2152 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 445.8 |
| 595b3bb7-0071-3eeb-893c-5d5e27efbce3 | -4.279 | -45.6485 | 2025-11-05 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 53d0066e-8269-3ca4-ac0e-9e1ce17b3272 | -3.4712 | -43.6392 | 2025-11-05 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 9583b38b-0edd-3f2a-88c4-f81d7c20bad8 | -3.7195 | -45.8992 | 2025-11-05 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2e67b2f1-7abf-3b9c-a30a-a069d758ab0c | -4.2977 | -45.6475 | 2025-11-05 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 38517086-f3b0-349b-98be-1b4147a48f52 | -4.2975 | -45.67 | 2025-11-05 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8a7b4bb7-f21e-39bd-a786-b361b9d848c3 | -3.2317 | -46.8716 | 2025-11-05 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 08633a87-8d2d-3a26-a15e-6c412b800798 | -4.4635 | -43.1919 | 2025-11-05 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8e93ca0c-99bc-3559-9dec-c3133a3bad87 | -1.3006 | -49.1677 | 2025-11-05 01:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9576c1ad-d07d-3131-bbd7-1c4a8d9f26f8 | -31.84535 | -53.05405 | 2025-11-05 01:06:00 | TERRA_M-M | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| 4f3192e8-5d4f-375c-86f0-2c2c60026dcb | -16.18995 | -56.77157 | 2025-11-05 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3d3cd9f-e8e5-3558-b690-031ffaff1d1c | -16.88978 | -52.86247 | 2025-11-05 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6e781026-928d-3886-92ae-7a9cd0d67f85 | -18.12013 | -53.57394 | 2025-11-05 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 47f17b67-5db2-30d6-b854-53866cf645c9 | -16.88989 | -52.85576 | 2025-11-05 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3803a4d5-2570-3e69-99b8-b68c27d9db8d | -18.11642 | -53.56832 | 2025-11-05 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 7aa64b4b-78c9-3f60-8eca-0770b2779945 | -18.11816 | -53.56129 | 2025-11-05 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 90ad99c2-df5c-3535-a627-501e8159d7a9 | -4.482 | -43.2141 | 2025-11-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 89e22b99-d4f9-34b4-be2e-7b639b6d115d | -3.49 | -43.6152 | 2025-11-05 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 57e20565-7f9e-32ba-b325-743cf1d318fd | -4.4073 | -48.9474 | 2025-11-05 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 0d17292c-0a1c-3205-8939-e198bb65fa91 | -4.4632 | -43.2386 | 2025-11-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 299.6 |
| 6d3f04f7-c8f0-3a59-b9e7-9c4ecde43658 | -4.4075 | -48.926 | 2025-11-05 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 7109b0ed-0863-39c4-a0fa-cd94c3954e25 | -3.7195 | -45.8992 | 2025-11-05 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 95b7ae4f-cd92-36e7-821a-a731edd0cbd9 | -4.0506 | -43.4713 | 2025-11-05 01:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| eb7fa284-33f8-3333-a3b0-7058868648b4 | -4.279 | -45.6485 | 2025-11-05 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a5d4bff4-6e8b-3912-a01e-0d8a175d5b62 | -3.2316 | -46.8936 | 2025-11-05 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 84b7bd25-c255-3460-a308-3cca7167ba99 | -3.4899 | -43.6383 | 2025-11-05 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 2b960a0e-1bd7-38ef-99a9-d49ba73f5b83 | -9.4765 | -40.3613 | 2025-11-05 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 391ae46d-b7b0-3c3a-9f20-7ffd560ff1ae | -4.426 | -48.9251 | 2025-11-05 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d08147cf-0b96-394d-9b16-1a62f72e7ce3 | -3.4714 | -43.616 | 2025-11-05 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 359feea0-2105-3c72-b209-4460a2974053 | -4.4259 | -48.9465 | 2025-11-05 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| cbd337ae-1790-36b0-8841-2fa4c6f6a8fb | -5.4553 | -45.3988 | 2025-11-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 322.7 |
| b3d35d9b-8b3b-30a8-befe-ece5ac5a596f | -4.4445 | -43.2397 | 2025-11-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f4fc4d4e-d929-35ca-8038-25a4db08d374 | -5.474 | -45.3976 | 2025-11-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 3c26df2c-9923-33b1-9b40-58459615cbd9 | -3.2317 | -46.8716 | 2025-11-05 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| efaa97c3-994b-34e8-8abe-30852eeab57f | -5.4551 | -45.4214 | 2025-11-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 57689034-9784-35a5-bd76-e44fc364a6a7 | -4.4446 | -43.2164 | 2025-11-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| f51a50b7-7051-362a-8828-4e8fabe2a748 | -2.6509 | -48.4985 | 2025-11-05 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 441bb836-414a-33c5-ad07-bd35c51d865b | -1.3006 | -49.1677 | 2025-11-05 01:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 82372478-d3d8-312e-89e5-484c298ac250 | -11.8473 | -43.7256 | 2025-11-05 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| c667ec37-6eca-37b4-abcd-9bc64e438edf | -3.7196 | -45.8769 | 2025-11-05 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2a81482e-b2d1-3237-ade0-966dfa108bd9 | -2.6508 | -48.52 | 2025-11-05 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e13b5dca-bfe5-3620-af6a-e93ede9cf81a | -4.2789 | -45.6709 | 2025-11-05 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c02b61ce-c534-3a6b-9969-76eb85045107 | -4.4633 | -43.2152 | 2025-11-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 423.6 |
| 348d149f-b605-36dc-b2eb-5730968136ba | -4.4819 | -43.2374 | 2025-11-05 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 285.0 |
| 21fdd819-f068-39e0-a6f1-69ce29ac9cdb | -3.4712 | -43.6392 | 2025-11-05 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 4df87861-7601-34fc-91df-4a51a0e203cf | -2.7921 | -50.3196 | 2025-11-05 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 230f2d07-1953-3a32-9a57-f468efdaa214 | -8.05 | -49.6325 | 2025-11-05 01:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c7e6c91d-b1f8-3f29-8ed9-571a73686fd7 | -11.34894 | -55.06152 | 2025-11-05 01:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f23d30d4-4678-3119-9f18-0b05b248a27b | -12.2478 | -50.2981 | 2025-11-05 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4853fd2c-caed-3fa3-b620-a7f443c08839 | -8.22705 | -49.99041 | 2025-11-05 01:11:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 8ca39ed6-f34e-3b17-888a-5c6287b9ea6a | -8.06345 | -49.65441 | 2025-11-05 01:11:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| b5c7e31b-eabe-33ec-b2d1-fbc09950f05e | -12.24731 | -50.29142 | 2025-11-05 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 116f2b20-f497-3aff-8363-58711d226ba1 | -11.54336 | -50.20266 | 2025-11-05 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| bbc130a8-81f7-39f9-b8c5-dd85a69096a7 | -13.37031 | -61.29636 | 2025-11-05 01:11:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README4.md)
