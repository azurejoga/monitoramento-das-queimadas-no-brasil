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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd68ac1d-71bc-3ef9-930e-1640e6025c62 | -11.7571 | -46.6431 | 2025-09-13 07:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ed816001-db8b-3396-baba-459ed38c7f56 | -9.5326 | -54.6075 | 2025-09-13 07:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d3b667cb-e95e-3405-b3c0-d60fb40f2e54 | -11.1143 | -51.3846 | 2025-09-13 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| f42f591d-d5a1-3501-a512-bbe80b59c208 | -14.1708 | -46.2275 | 2025-09-13 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5aaeb3d9-3b94-3999-99e8-a275de078986 | -14.1893 | -46.2702 | 2025-09-13 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| dc00fc52-9ba7-33c1-9b84-f91b8123b70f | -15.4517 | -47.3291 | 2025-09-13 07:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 187a1317-4748-363b-b0d5-e4c6446767fa | -14.1898 | -46.2472 | 2025-09-13 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 03f78b2d-2a0c-368d-b2a6-df8f3be861f0 | -18.0298 | -50.9606 | 2025-09-13 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 472.2 |
| a000cc1b-e917-37fb-8406-2be9b5928c57 | -9.5324 | -54.6277 | 2025-09-13 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| e80312f3-134f-39e4-935f-e11c34d39d78 | -11.0953 | -51.3866 | 2025-09-13 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ac1a5ac8-cc68-3b11-b879-b828abe48377 | -18.0502 | -50.935 | 2025-09-13 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 247.5 |
| 39798e26-cda7-3f92-b121-8ddad1c4aefd | -11.114 | -51.4057 | 2025-09-13 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 93417b90-b972-365a-bb57-9b16d243d955 | -10.3701 | -50.4857 | 2025-09-13 07:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c6eb3ea4-df39-38e9-a157-754f60a2b212 | -18.0497 | -50.9571 | 2025-09-13 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 3010aca4-43ff-3b1b-a008-e92de93eaf0b | -18.0308 | -50.9164 | 2025-09-13 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5c6ba612-385d-3942-8007-c7af8a4a3578 | -11.7391 | -46.5779 | 2025-09-13 07:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 29cdef01-409d-3d1e-810e-79c1e9ed6078 | -9.2658 | -59.3997 | 2025-09-13 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 8a224e59-940b-35e3-a783-33ea6f39abfc | -9.5326 | -54.6075 | 2025-09-13 07:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1767dc8a-6011-3e84-9aac-9f96d9aa3d25 | -11.7571 | -46.6431 | 2025-09-13 07:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ce8f1476-9954-3a81-bfa4-15e8c2cbaaec | -9.2844 | -59.3986 | 2025-09-13 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0542dd21-4ff9-3a0f-bd74-08864d3354a0 | -10.3699 | -50.507 | 2025-09-13 07:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b60fc948-36f0-3d03-a002-d4934aaa73b4 | -11.095 | -51.4077 | 2025-09-13 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 2cb66dca-622c-39b8-ba31-b0a97f9159cb | -9.5137 | -54.6292 | 2025-09-13 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| a6d61cbf-8d00-3a91-a964-0d2e7d7099dd | -11.1143 | -51.3846 | 2025-09-13 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 261.1 |
| 3866a9ee-1aab-32a6-ab5c-5009203f5945 | -18.0303 | -50.9385 | 2025-09-13 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 835.1 |
| ea764c89-a1ea-3f2f-874f-52cf4f8068c3 | -12.006 | -47.7505 | 2025-09-13 07:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7ee92441-cb0e-3c62-92ba-1db8ad5a54c0 | -9.2656 | -59.4191 | 2025-09-13 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cd0305ff-3ef5-3e7e-89b2-f7d0e9d06a74 | -9.2844 | -59.3986 | 2025-09-13 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4306d72b-ab65-3cdd-bc5d-5735a68810f7 | -9.5324 | -54.6277 | 2025-09-13 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 2e1345a9-5d41-34fd-af4d-d95762c397fe | -11.1143 | -51.3846 | 2025-09-13 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 36c1d313-dfe4-31f7-a40e-1a43085f9de7 | -18.0303 | -50.9385 | 2025-09-13 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 451.3 |
| bdd7a4fa-dd3c-3ddd-8766-a0f80212075c | -18.0497 | -50.9571 | 2025-09-13 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6fcc281f-1f0e-31ea-8ebe-991af83c9b81 | -11.114 | -51.4057 | 2025-09-13 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ab8a9912-09a7-3377-a422-0d9b858b7164 | -11.7204 | -46.5579 | 2025-09-13 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 72e5df03-87a8-32c8-9968-a96cbb6628c3 | -18.0502 | -50.935 | 2025-09-13 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 196.8 |
| ab511596-326c-32f9-904c-289e2f5a3ada | -9.5006 | -55.9588 | 2025-09-13 07:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 69c6c368-d37a-357a-bb4c-e5526fc9437d | -9.5137 | -54.6292 | 2025-09-13 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| fd60f659-7e12-3096-933c-b70ab756d72e | -11.7571 | -46.6431 | 2025-09-13 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c3a978a3-3fb7-381a-aaef-07e3da9e121c | -11.7391 | -46.5779 | 2025-09-13 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 07a76d17-5c5f-378b-a4b0-d76728c36337 | -9.2656 | -59.4191 | 2025-09-13 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3758eca5-4553-30d7-830d-ec82e4146d0e | -9.2658 | -59.3997 | 2025-09-13 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 94600616-488c-352f-8dc6-e79e23892fc2 | -10.9279 | -47.2446 | 2025-09-13 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| de8f7250-72f6-30fd-b33b-92a80e0866e6 | -11.095 | -51.4077 | 2025-09-13 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| a04637d2-75c9-3b3a-9899-cee0801225e6 | -11.7575 | -46.6205 | 2025-09-13 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c5465784-8dbd-3354-9dbd-e80b30ea1bef | -11.0953 | -51.3866 | 2025-09-13 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 56fd2f21-cca3-33aa-968a-dddca49ad939 | -11.72 | -46.5805 | 2025-09-13 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 310cef43-1680-3911-b542-88af709c4ef0 | -18.0298 | -50.9606 | 2025-09-13 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 5d658595-ef27-3829-95e9-6113d1092f17 | -10.9473 | -47.2199 | 2025-09-13 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c2374d47-e999-3de7-8de9-f9a425be59a7 | -10.9286 | -47.2 | 2025-09-13 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 2c7b84c2-c9e9-3b49-b169-f9d238f909b0 | -10.9283 | -47.2223 | 2025-09-13 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 342af361-4ab8-30b7-8918-27ecb0df8a6c | -11.7395 | -46.5553 | 2025-09-13 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 37bc59bf-8bd2-375a-843a-7b12a7d91943 | -18.0308 | -50.9164 | 2025-09-13 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ca60806c-bec7-3b56-8466-01ed57f3bf49 | -18.0497 | -50.9571 | 2025-09-13 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 232d6a57-7428-3420-a5a4-55403c7b6dbe | -9.5326 | -54.6075 | 2025-09-13 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 83e7c2b3-f3e4-37a6-805b-c26841258a18 | -11.1143 | -51.3846 | 2025-09-13 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0ba298fc-d211-3d2e-bac3-41fb3fdd3dae | -9.2658 | -59.3997 | 2025-09-13 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 35798891-92ec-307f-8ba5-a30fef2327e0 | -11.7571 | -46.6431 | 2025-09-13 07:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0f7e0adb-a1f9-343c-8da0-bb2e532ee7c5 | -9.2656 | -59.4191 | 2025-09-13 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 16a3525c-c610-3f0a-a73e-d2bf33bb991e | -11.0953 | -51.3866 | 2025-09-13 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 847870aa-471d-399a-8580-ae5fef5ad1bd | -12.8263 | -47.9263 | 2025-09-13 07:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| fd393b10-22fb-3d56-93b1-b1926cc87ccc | -11.114 | -51.4057 | 2025-09-13 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 42c40279-f448-32b0-84bf-ef9b6fe3f2d8 | -11.095 | -51.4077 | 2025-09-13 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| d1b70cb3-d972-35f8-b796-07646769b33a | -9.5324 | -54.6277 | 2025-09-13 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 09e66b53-ade3-381c-b82e-11a5035be021 | -11.7575 | -46.6205 | 2025-09-13 07:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ab22be06-49a7-3344-85e5-ab96674e9ad2 | -18.0303 | -50.9385 | 2025-09-13 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 3fdec83b-3cb6-3c75-b8c7-2938b1b7e4dd | -18.0298 | -50.9606 | 2025-09-13 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 137.3 |
| ccb130bd-b6b9-3e2d-965f-38adf0071d6a | -9.5137 | -54.6292 | 2025-09-13 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1e6de823-c471-3a7e-bef7-2892ef95331d | -18.0502 | -50.935 | 2025-09-13 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 54d199d4-fffc-331d-a869-b90b1b557e16 | -18.0303 | -50.9385 | 2025-09-13 08:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 189.4 |
| fb9282a5-1abb-3fb5-a21b-7b1f9f74a71b | -11.8284 | -50.5406 | 2025-09-13 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9da025d3-9249-3dad-8d2d-109f79c0daaa | -10.9473 | -47.2199 | 2025-09-13 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 774de006-f7a1-34ae-a5d7-f966e7f38e08 | -9.5324 | -54.6277 | 2025-09-13 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| ab8e2608-1790-30ea-8bb5-3c4459a20624 | -9.5137 | -54.6292 | 2025-09-13 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 0017e615-4e25-37dd-8220-70694d2ae8b4 | -18.0497 | -50.9571 | 2025-09-13 08:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 79c6b774-1ecd-3d4c-b871-9c31dc5f86b4 | -11.7575 | -46.6205 | 2025-09-13 08:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c652d7d8-563b-393b-a4e6-4beb7aec9e3f | -17.292 | -46.0996 | 2025-09-13 08:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4ea219e2-e86d-3f16-a65e-5e033981e481 | -11.7571 | -46.6431 | 2025-09-13 08:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| aed00213-c4db-381a-b09f-d90744c20455 | -18.0298 | -50.9606 | 2025-09-13 08:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 109.2 |
| d80b831c-f13b-3321-9d13-48555c9391c9 | -9.2844 | -59.3986 | 2025-09-13 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 695fd811-7473-31ee-bd12-9f6d31409326 | -11.095 | -51.4077 | 2025-09-13 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0f57d62d-d5bd-3e9f-8d34-0374c52f59aa | -9.2658 | -59.3997 | 2025-09-13 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 662de33c-4298-3687-a007-847232b1caa2 | -9.2656 | -59.4191 | 2025-09-13 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| eb42dff0-0cd2-3814-bcb7-8e92dbfb45b0 | -18.0502 | -50.935 | 2025-09-13 08:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 42b5226e-ecbc-3a88-94bd-dbca4991561d | -11.7391 | -46.5779 | 2025-09-13 08:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e93f9f69-7ba6-3f13-9034-19ca3fdc3fe4 | -10.9283 | -47.2223 | 2025-09-13 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 99ab8f67-21eb-38e9-9f01-6ec27537433c | -9.2656 | -59.4191 | 2025-09-13 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 12951202-8c0f-336c-bc40-262dfdbe5fc7 | -11.095 | -51.4077 | 2025-09-13 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| eef3bb66-2559-3e3a-a130-60115768cfa0 | -18.0502 | -50.935 | 2025-09-13 08:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f53ccbd9-7b1c-3903-b9bb-4a0192b9b5f1 | -18.0303 | -50.9385 | 2025-09-13 08:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b2db3cb0-b0fd-3bf3-a7cc-b465f14dc1be | -10.9283 | -47.2223 | 2025-09-13 08:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e67a15aa-a7a2-322f-b3be-08e6607c174f | -11.35 | -50.7867 | 2025-09-13 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 38b6ce32-3e3a-36ce-9ddc-3b5b83a50b77 | -11.5809 | -50.569 | 2025-09-13 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 40ea3fbe-fe10-3ff1-a74a-522c1fb05146 | -18.0298 | -50.9606 | 2025-09-13 08:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| d865603d-fdee-3f23-b8e2-493b3782f744 | -11.1426 | -50.7028 | 2025-09-13 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e66c121a-cc20-38ab-a6c9-d06e6d37afa4 | -12.8263 | -47.9263 | 2025-09-13 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| df731ff1-e803-3914-868a-7ada2be422d0 | -9.5006 | -55.9588 | 2025-09-13 08:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ce5d7be5-5bae-386b-ac02-572c2537bd6c | -11.1237 | -50.7049 | 2025-09-13 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b62a7b25-a872-3214-9b3f-03549c99b18a | -9.2658 | -59.3997 | 2025-09-13 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| ff9f2974-23e2-3b5c-9273-cf67e1ea4146 | -11.7571 | -46.6431 | 2025-09-13 08:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5f5fc33a-2758-3634-81b8-7e8fb1d3d465 | -11.8284 | -50.5406 | 2025-09-13 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README119.md)
