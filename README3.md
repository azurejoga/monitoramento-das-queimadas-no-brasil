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
| 65bd7ab6-16a0-3d61-a61f-2b2f6fb783f2 | -5.7945 | -45.0586 | 2026-06-17 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 85193a62-4081-3ae8-ac18-75c42542c38a | -9.3234 | -45.4787 | 2026-06-17 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 65fd4c95-b98a-3304-a9d3-8e86f9daf9a7 | -9.3045 | -45.4809 | 2026-06-17 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 92f50705-d851-37d1-bbfa-37c8b57c62d5 | -12.0756 | -54.6131 | 2026-06-17 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 4d642551-ff5e-349f-a2fb-e2da3ef31100 | -5.7943 | -45.0813 | 2026-06-17 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 1a90d576-d4e3-3256-882f-6909162651f3 | -9.3237 | -45.4559 | 2026-06-17 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fcb901b9-e600-335d-8210-fffd79bfd865 | -12.8548 | -44.3625 | 2026-06-17 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| be356b7f-7684-3c32-a739-d70ae64d2679 | -4.3588 | -47.7636 | 2026-06-17 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 36485142-e1d0-3e2c-be0f-4710d8692ffb | -10.5637 | -46.2135 | 2026-06-17 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0f5c5737-086e-3a26-8967-551a584fdf49 | -12.8543 | -44.386 | 2026-06-17 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a9e211b3-156c-3195-9ce6-387a6013c144 | -9.3048 | -45.4581 | 2026-06-17 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 839c21b8-c8ab-3e7b-98e9-f161654d1ec1 | -9.3048 | -45.4581 | 2026-06-17 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a99eadef-2e91-3ee8-8563-c478caa5d5bc | -12.8548 | -44.3625 | 2026-06-17 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 1fbf3ebc-45ef-376d-9abf-da0283b202c7 | -12.0945 | -54.6113 | 2026-06-17 00:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 4ae297a4-4aa5-312a-869d-77beb23ef7b5 | -9.42 | -40.3198 | 2026-06-17 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 00443ed5-b99f-3b10-9d71-e2f17d0202b1 | -9.3234 | -45.4787 | 2026-06-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2554caaf-47ff-3f16-9d39-6e2ea2b68f72 | -9.4391 | -40.3171 | 2026-06-17 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| e1eda764-359b-39ae-b7e6-38947fe40b77 | -10.5637 | -46.2135 | 2026-06-17 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 2f6425ed-2d4d-3723-9a4f-c95a2b9177bd | -9.3045 | -45.4809 | 2026-06-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c50b83fe-3b66-3aa9-afaa-c9da10845691 | -12.0756 | -54.6131 | 2026-06-17 00:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| c73e01ae-7fd0-3a1c-9ea5-8323436ef042 | -5.7943 | -45.0813 | 2026-06-17 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 0c5e5d34-6ebf-340f-b8cc-8bedf8efa20d | -12.8354 | -44.3657 | 2026-06-17 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2472851f-4988-3d1d-a447-14ce19905a3e | -9.3237 | -45.4559 | 2026-06-17 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c53a3d92-3d8f-3321-ba52-25e6c5d17cc3 | -5.7943 | -45.0813 | 2026-06-17 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a9a02155-9efd-314f-967e-ee2109b31618 | -9.4196 | -40.3447 | 2026-06-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.2 |
| a4ad86f1-2569-36db-8bb3-592b36bd2d4e | -9.4387 | -40.3419 | 2026-06-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 3547e194-6ada-373e-bb0d-7682537d0ef0 | -12.8354 | -44.3657 | 2026-06-17 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c73702dd-7a44-3f06-b039-5ae0f47b7fb2 | -12.0756 | -54.6131 | 2026-06-17 00:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| de19c99d-3d05-32f9-b25c-5c65ac47635b | -12.2327 | -52.8199 | 2026-06-17 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 4f14c525-eefe-344a-8ac2-cb7b1616fb17 | -9.3048 | -45.4581 | 2026-06-17 00:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 15ccccb4-a3ec-3f05-b528-1283077ba8c3 | -12.252 | -52.7969 | 2026-06-17 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 3368e00e-6c71-3fef-8e82-4a4bb0f94e3a | -12.8548 | -44.3625 | 2026-06-17 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0dc6d167-f4b8-3d00-a11e-99c52e853af6 | -9.3237 | -45.4559 | 2026-06-17 00:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4264d5fc-1bad-39c7-a1c0-d200fefccd7f | -12.0945 | -54.6113 | 2026-06-17 00:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5d1b934e-784f-3749-9de3-6df50bb32346 | -9.3045 | -45.4809 | 2026-06-17 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 340081ba-b57a-38d8-a212-7e4dab9ea016 | -9.4391 | -40.3171 | 2026-06-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 802201a0-714e-3411-82a3-48a657740f81 | -9.42 | -40.3198 | 2026-06-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 3e8c5ee4-3d82-3785-b5ac-1a91c4709733 | -9.3234 | -45.4787 | 2026-06-17 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 3c884ca3-5833-3688-92d2-778f6243ebb5 | -12.233 | -52.799 | 2026-06-17 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9aaae80b-38bb-3bf0-bf06-6977c9213256 | -9.4391 | -40.3171 | 2026-06-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 654.9 |
| 892fff8c-684b-3ae2-b482-9a16413c708a | -9.4196 | -40.3447 | 2026-06-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 252.8 |
| 976f6d08-d992-3237-b91a-7bf60f6b4802 | -9.3048 | -45.4581 | 2026-06-17 00:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c357689a-d599-3802-a425-56a77a2121ba | -9.3045 | -45.4809 | 2026-06-17 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d080f72d-89d6-3193-acc1-31fb7384c15b | -9.42 | -40.3198 | 2026-06-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 553.9 |
| e525010b-fab0-3817-8e1b-a3b5dc1ab37a | -12.0756 | -54.6131 | 2026-06-17 00:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 6165994d-eecc-3e6d-b055-c96292650640 | -9.4008 | -40.3225 | 2026-06-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 7c24d2cd-b8d5-336a-8a36-13147999ac4c | -12.0945 | -54.6113 | 2026-06-17 00:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 055f4c37-d68b-3ffc-86ab-c52d59554512 | -9.3234 | -45.4787 | 2026-06-17 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 292fbc84-7c19-3a1a-b904-f39b04a8cb59 | -4.3588 | -47.7636 | 2026-06-17 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 84d34004-619a-37d7-9bba-44152a9cf81a | -12.8354 | -44.3657 | 2026-06-17 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 5544dd98-3c34-377c-9a9d-47857448701a | -9.3237 | -45.4559 | 2026-06-17 00:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 211d033b-a504-39da-8235-4130f18dff1c | -9.4387 | -40.3419 | 2026-06-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 294.3 |
| 0bcdc648-51e0-314d-8389-fe66b1baac05 | -5.7943 | -45.0813 | 2026-06-17 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2090c590-0c40-381a-99da-19da8689a3c3 | -9.4395 | -40.2922 | 2026-06-17 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| a3679950-c37f-3a4c-9980-3b72bc0bec1b | -12.8548 | -44.3625 | 2026-06-17 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d85232ef-cdb9-38ce-a50e-802d14fd4668 | -10.2773 | -60.5383 | 2026-06-17 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4bdee8-a41d-3793-821c-84f203003ea9 | -12.0819 | -54.607899 | 2026-06-17 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc570472-bea5-3dad-9863-559a64e67ccc | -12.764 | -58.997501 | 2026-06-17 00:59:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e20e237a-94fd-31b9-a63d-35609340f45e | -9.2106 | -58.054798 | 2026-06-17 00:59:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d234da3-7b90-3d72-80d6-5c7eb74afed7 | -10.1137 | -52.1576 | 2026-06-17 00:59:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67cdfc41-5047-370f-b4b8-0b39b6cb3495 | -14.0937 | -59.4464 | 2026-06-17 00:59:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e579b0a-7fb4-38df-922b-1481e6ffc8d9 | -12.0789 | -54.595699 | 2026-06-17 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 324df5bc-b845-3da8-91f0-7fcfcf161500 | -12.4311 | -58.403198 | 2026-06-17 00:59:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f53e188-88b4-3ad4-9d7c-e778cd68a193 | -14.0953 | -59.453499 | 2026-06-17 00:59:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41a3c34b-893e-380f-b9ba-5540c08454d1 | -12.9141 | -54.210201 | 2026-06-17 00:59:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec2c6476-d694-39a6-b1b5-82b6e50d8727 | -10.1483 | -56.604698 | 2026-06-17 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3509bd7-a66f-32dc-b686-4da8f56ba9ef | -10.146 | -56.595001 | 2026-06-17 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0059fe58-1468-3e06-862c-a5f834417e0d | -11.5886 | -55.3363 | 2026-06-17 00:59:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5c7df8e-c6ac-3792-bc7e-8d60963b02f3 | -12.1542 | -63.0331 | 2026-06-17 00:59:00 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a872710b-951d-330a-b985-c2ff8171efc7 | -10.2757 | -60.5313 | 2026-06-17 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2b9461d-63a8-38dd-96a7-2db7536f24b0 | -12.0691 | -54.598099 | 2026-06-17 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acee062b-48d5-389c-995a-f38b50dd4ea9 | -10.711 | -56.236801 | 2026-06-17 00:59:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df53399c-b4c2-3e88-81cb-d263bd8bd66c | -12.0721 | -54.610298 | 2026-06-17 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f928bbd-f89b-361e-919c-7503099a057d | -11.5858 | -55.325199 | 2026-06-17 00:59:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab7934ba-033f-34d6-b61c-cf6fd29e67dd | -10.1558 | -56.592602 | 2026-06-17 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb81871a-36f3-3de4-81c0-6db4514429fe | -9.1871 | -58.042801 | 2026-06-17 00:59:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e20f7946-14b8-3a3b-8a0b-602a78b901b7 | -12.2278 | -57.268101 | 2026-06-17 00:59:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9693374d-2295-3775-809d-057f882b41fd | -12.4294 | -58.395599 | 2026-06-17 00:59:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3d73fb-7acc-3751-bcd1-7b3523077278 | -12.0759 | -54.5835 | 2026-06-17 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 036b8da4-c5b3-3de6-bfbe-7687536a7ba2 | -10.1185 | -52.176601 | 2026-06-17 00:59:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d58bad1-c265-3b9b-ab0a-212147dd7708 | -12.4276 | -58.387901 | 2026-06-17 00:59:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7bd4c31-fc5c-3b6b-9ba4-5f67c1ecbbff | -9.3237 | -45.4559 | 2026-06-17 01:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| df85a423-6330-3c86-9e24-41ae811f3f16 | -9.4196 | -40.3447 | 2026-06-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 223.1 |
| ea46dd61-c72c-3e1e-b02b-b93394c2412c | -5.7943 | -45.0813 | 2026-06-17 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 506de32d-19b9-35f4-9b22-3b8f1d5eb01c | -12.8543 | -44.386 | 2026-06-17 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 17828d10-21f5-3da6-90d7-a9b7bab9295d | -12.0756 | -54.6131 | 2026-06-17 01:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c0ec3c2f-e80e-3166-947b-7ebb5f83b9f6 | -9.4391 | -40.3171 | 2026-06-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 270.5 |
| 5a779695-3d33-371c-8890-114d61590dc1 | -12.8548 | -44.3625 | 2026-06-17 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| f45290d8-33f6-32c4-bdaa-27cb59de7a4d | -9.4204 | -40.2949 | 2026-06-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 9c12415b-25c0-35d6-b41e-579e7345d161 | -9.4387 | -40.3419 | 2026-06-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.0 |
| ddfad6f4-c3ff-3b44-9664-7009b823d036 | -12.8354 | -44.3657 | 2026-06-17 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 15e9d94c-fd21-38a0-8423-c9eb0ea21f5f | -9.3048 | -45.4581 | 2026-06-17 01:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 766b65f8-a479-3927-9d14-261bd39369e2 | -12.0945 | -54.6113 | 2026-06-17 01:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8f3d6e6a-bbef-3213-9e60-ee1aa77c9069 | -9.3234 | -45.4787 | 2026-06-17 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 41cc46c4-f14c-3de3-8882-655502b5f0ec | -9.3045 | -45.4809 | 2026-06-17 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 1849c4dc-3917-306c-a18b-257899e44636 | -9.42 | -40.3198 | 2026-06-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 545.3 |
| 588b4045-6b77-32db-bf8a-83fdf213926d | -9.3237 | -45.4559 | 2026-06-17 01:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 987dd8d4-f6df-31f3-82b2-ef3b58e8ceaf | -9.42 | -40.3198 | 2026-06-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.3 |
| e301bbe3-00fd-3fef-bd58-9cfe9c87846b | -9.3045 | -45.4809 | 2026-06-17 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ed10a5f0-63ac-3f19-9ad3-e5b17ee83c6c | -12.8354 | -44.3657 | 2026-06-17 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |


[Clique aqui para ver as próximas entradas](README4.md)
