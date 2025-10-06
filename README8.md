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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c172b9e8-f5fc-3685-886d-39e6a9d85446 | -14.3163 | -47.6561 | 2025-10-06 02:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 0e0457aa-daed-35b4-9dd0-15ae30fac7f3 | -5.3224 | -43.392 | 2025-10-06 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4d8abd64-c8b3-300e-a57b-d6230fedc7e5 | -14.9014 | -51.518 | 2025-10-06 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f51351ec-fa11-3919-b6d7-cb31aa6cb5f3 | -17.981 | -57.5468 | 2025-10-06 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 8da77026-75d9-3656-adbb-779519016023 | -14.6893 | -48.4021 | 2025-10-06 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 32d0eaee-30af-3af0-a4b8-bcf6cd3da62a | -14.6897 | -48.3797 | 2025-10-06 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| d37abafb-7f13-3a95-a77c-0d78656c2b56 | -13.6007 | -48.7013 | 2025-10-06 02:00:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 1f94b0a7-d00e-3b56-b4e3-b0677c4ca62d | -8.4353 | -70.13 | 2025-10-06 02:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5c522491-dec3-3cc9-98ed-b8113dc3a131 | -5.3601 | -43.366 | 2025-10-06 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 8eb088ee-7a38-3c97-be9a-af3097fc9030 | -5.3416 | -43.3441 | 2025-10-06 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4eff0571-d022-3596-bc21-036091c21cf6 | -18.1167 | -53.3977 | 2025-10-06 02:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f4d0df1b-ea6a-3ce4-a572-88abb3f16ebe | -14.6703 | -48.3828 | 2025-10-06 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 47fd9578-124c-39db-b701-fc9e1121649f | -12.3793 | -63.7294 | 2025-10-06 02:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4edba6c4-69bb-300d-b95f-e5b3c99c9c47 | -14.855 | -54.2287 | 2025-10-06 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 227.1 |
| cfc0095d-7179-369b-a787-53301e823739 | -13.2699 | -47.8398 | 2025-10-06 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5d03513a-72f4-3cda-a572-27ae55cc5261 | -14.8828 | -51.4777 | 2025-10-06 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 148.6 |
| f2a9c774-f3c2-3b4b-97c4-a7625674d67f | -14.8357 | -54.231 | 2025-10-06 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 1507eb3b-b800-320e-930a-ca92e36dbb19 | -14.9018 | -51.4965 | 2025-10-06 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 25181736-94dc-3f24-b34c-5d553a7a4319 | -14.9022 | -51.4749 | 2025-10-06 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 87025172-a928-3d69-8ed6-5f655fa8313d | -14.8828 | -51.4777 | 2025-10-06 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a8792ab6-3700-33d8-8790-e152a0b25f06 | -18.1167 | -53.3977 | 2025-10-06 02:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9f188776-3138-3810-853d-e3ab47ab10e3 | -5.703 | -44.838 | 2025-10-06 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9966384c-3625-3186-a7df-a5ffa60d46cc | -18.1366 | -53.3946 | 2025-10-06 02:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a52ef5be-ba5f-3454-8ef2-f059716172e9 | -5.3287 | -47.2744 | 2025-10-06 02:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 19e8fdda-585c-3468-a279-596723d34a50 | -5.7028 | -44.8607 | 2025-10-06 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c699c01c-da4e-30f9-9daa-1e77e4fde95b | -13.2699 | -47.8398 | 2025-10-06 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9981989e-fe28-396a-b2e8-6cb956e74571 | -15.6007 | -52.5529 | 2025-10-06 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 78713134-7c7f-35fc-8628-38336117491d | -14.8824 | -51.4992 | 2025-10-06 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2b478527-91b4-31f0-96ff-2db567b53ce9 | -14.9022 | -51.4749 | 2025-10-06 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3cd6f868-80a9-3995-af03-f5f94148cf17 | -14.8554 | -54.2078 | 2025-10-06 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 357.5 |
| 06eb4c2a-7aef-3dbd-9aa4-1639a9342e10 | -14.8357 | -54.231 | 2025-10-06 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| c3015da4-902e-3b0d-b8a7-fe6d42912924 | -18.0008 | -57.5444 | 2025-10-06 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| df8075c0-b358-3bc9-8861-8fd4e540a1e9 | -14.9018 | -51.4965 | 2025-10-06 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| f9395d00-212f-3b25-ade6-0bd5fad741ae | -14.6897 | -48.3797 | 2025-10-06 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 501c4a39-1fbf-323a-98a4-6b9a25bbfed3 | -14.855 | -54.2287 | 2025-10-06 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 4b1ca872-5eef-3f45-8130-7fe1c3c55958 | -13.6007 | -48.7013 | 2025-10-06 02:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 11f9db5a-ecae-3867-bbf7-f6ae489488cf | -14.3357 | -47.653 | 2025-10-06 02:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8f171dde-d085-38ef-882a-bab9b0fae068 | -14.836 | -54.2102 | 2025-10-06 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 7f709dbf-94e5-36c5-ad3f-c436ad5423f7 | -13.62 | -48.6985 | 2025-10-06 02:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 377bd46d-0aed-3295-aeac-ac50c5dd8906 | -13.6011 | -48.6792 | 2025-10-06 02:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bc70ffcb-4a52-33fe-b9cc-0f12ad8a5ec7 | -5.7028 | -44.8607 | 2025-10-06 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4b87b57c-a282-392d-8941-59d6f757cba6 | -13.2699 | -47.8398 | 2025-10-06 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6e857e1e-78e1-3b37-936a-1a225213992c | -18.1366 | -53.3946 | 2025-10-06 02:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 85a37d09-070f-3e0b-b149-7e62d82a10b4 | -5.703 | -44.838 | 2025-10-06 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 0ca0a419-03ed-3d3f-9e6b-46225b264865 | -5.7215 | -44.8594 | 2025-10-06 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| bcdbe8c2-46e1-3e13-a6e2-5e03677e9e77 | -14.855 | -54.2287 | 2025-10-06 02:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| ada387cd-7409-3663-821a-d4336e600d58 | -18.0008 | -57.5444 | 2025-10-06 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 2b182783-481a-3b75-9a57-28e6251a3317 | -15.6007 | -52.5529 | 2025-10-06 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8a722d6b-b976-3fed-9247-bfc211e26feb | -13.6007 | -48.7013 | 2025-10-06 02:20:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 3f4abb9c-8a72-3021-ae4b-e5e836d91b30 | -14.5438 | -46.9633 | 2025-10-06 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| fc1ae335-65e3-3ea3-9c25-69938de56e21 | -14.9018 | -51.4965 | 2025-10-06 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d087018a-3237-354c-afa8-45a61de9ebe2 | -14.8554 | -54.2078 | 2025-10-06 02:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 91f07f24-d267-3ebd-b4ae-7eed2637d66d | -8.6327 | -46.3208 | 2025-10-06 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 05245070-5d53-35c0-824a-8d83b3df1fe3 | -8.6144 | -46.2778 | 2025-10-06 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 75db9fc8-93bc-3313-85cc-9f4f88fc6967 | -14.6897 | -48.3797 | 2025-10-06 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| da9f00e8-d552-3266-943c-5eea5d8ca02a | -13.62 | -48.6985 | 2025-10-06 02:20:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 71a3c744-6d8e-3ec1-8cef-96d5dd9de12a | -18.1167 | -53.3977 | 2025-10-06 02:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7ceefb5f-59ee-3184-adcd-7d38ac8c6b6e | -11.0151 | -46.5393 | 2025-10-06 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e45a7509-ec28-3a56-87e8-781a2ed19259 | -14.6897 | -48.3797 | 2025-10-06 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 74718246-db78-39e7-bf06-616d3d9558b2 | -18.0008 | -57.5444 | 2025-10-06 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 5d23f2be-640c-368a-95e3-287c7fbf1478 | -2.5968 | -48.1124 | 2025-10-06 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| dd442009-8825-375c-b14b-8d55c51196ca | -10.3162 | -50.278 | 2025-10-06 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 77eeffb8-38b7-3228-a56e-148ca3848b3c | -8.6144 | -46.2778 | 2025-10-06 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ab4a4c9d-630a-3f62-842c-93d6acb34bc0 | -13.2699 | -47.8398 | 2025-10-06 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1db2bd38-4b42-342f-adbe-b58593d3a1fd | -8.6327 | -46.3208 | 2025-10-06 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0cf4174d-ef4a-3954-b8c5-cd8355bb5a75 | -18.1366 | -53.3946 | 2025-10-06 02:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a16a3f0b-3c87-3c06-b481-20b4e5902f68 | -11.0342 | -46.5369 | 2025-10-06 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d4c9219a-8a7d-3368-b6ab-378cd81e7ae6 | -18.1167 | -53.3977 | 2025-10-06 02:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6e1b5bef-8ef0-3c80-8758-1813506236fb | -10.4285 | -50.3518 | 2025-10-06 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 61584c98-4db9-36a9-b61c-80524587a397 | -8.6327 | -46.3208 | 2025-10-06 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| fc23c715-1f13-38aa-8f40-26dbf1041349 | -18.1167 | -53.3977 | 2025-10-06 02:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8888ebdf-d39b-321a-8f7e-41cf3bee70a2 | -11.0037 | -51.1635 | 2025-10-06 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 18a4d3d5-beec-3467-8b04-e5e75e7a3b6d | -14.5438 | -46.9633 | 2025-10-06 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 232f3867-62c1-3182-9cc5-3f70ff67f8cc | -14.6897 | -48.3797 | 2025-10-06 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| be121745-b11c-3a78-be49-729ac1c01a54 | -17.981 | -57.5468 | 2025-10-06 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 30f782a6-49b0-39c5-b759-a2116240cbaa | -10.9848 | -51.1655 | 2025-10-06 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 5c8a4a65-71d5-371a-bde5-851f73c85bbf | -18.1366 | -53.3946 | 2025-10-06 02:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 814b2e54-ab9a-3ce6-8bb2-2cfb45a84f0a | -5.4742 | -43.1711 | 2025-10-06 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c54d4fe6-479a-3754-9346-ecf498e70019 | -5.6653 | -42.7578 | 2025-10-06 02:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| a0560a2d-2b1a-310e-b04b-e29bd74d18fb | -8.6141 | -46.3003 | 2025-10-06 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d3b1543d-97b8-37ed-9fec-3dfc9fd29844 | -14.6135 | -52.495 | 2025-10-06 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 8684f0a2-2074-3237-abac-9d8c11c95a52 | -8.6327 | -46.3208 | 2025-10-06 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1f179c6c-30af-3f35-b30c-c6629e1b8b51 | -11.0037 | -51.1635 | 2025-10-06 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| cc50b6c6-af14-380a-a381-f3ebdadc12dd | -18.1167 | -53.3977 | 2025-10-06 02:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 74b2a2b7-1eb9-339e-9dff-4885ce014418 | -18.1366 | -53.3946 | 2025-10-06 02:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 43f48b0a-4146-3b6f-ae40-b8a2d2dc89c4 | -10.9848 | -51.1655 | 2025-10-06 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 41d07ca8-ed10-3fc9-97a3-a25ee81834e7 | -10.4096 | -50.3538 | 2025-10-06 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 24ad180a-9cca-39b6-8597-373814d1075d | -10.4285 | -50.3518 | 2025-10-06 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 04cba7bf-4801-3c2d-b4ec-2eb5ff5a68ef | -11.004 | -51.1423 | 2025-10-06 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a11831ea-328a-3f94-9c56-dd3c9ee9ac65 | -14.6897 | -48.3797 | 2025-10-06 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| cbec25e9-f6a4-3c64-938b-230dfd2e87dd | -14.6131 | -52.5163 | 2025-10-06 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 7471313c-0665-3e82-827f-23f36c78072e | -8.6144 | -46.2778 | 2025-10-06 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2dba03e3-f540-33ae-bb26-400e54c1e758 | -10.4099 | -50.3324 | 2025-10-06 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b9f8d9c9-5e70-3c79-802c-4b9ed0afb5b9 | -17.8818 | -57.5794 | 2025-10-06 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 1bf23e8b-8444-3580-8e6a-81ffee27b45f | -14.6135 | -52.495 | 2025-10-06 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 2839d3ee-0ede-34f4-b5f2-7c2f3d90d0ad | -8.6144 | -46.2778 | 2025-10-06 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 195eb717-22f2-300e-b8d1-acf06569f579 | -18.1167 | -53.3977 | 2025-10-06 03:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 157e0884-8848-32fa-aad9-e22ef4ff821c | -8.633 | -46.2984 | 2025-10-06 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e7c42cd3-1689-3bda-847c-b3ba89ffa8c9 | -5.6653 | -42.7578 | 2025-10-06 03:00:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 2b4d5cc7-1637-3cbb-a9a2-530cb66ac9a9 | -8.6141 | -46.3003 | 2025-10-06 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |


[Clique aqui para ver as próximas entradas](README9.md)
