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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbfc59a2-006b-3941-b7b6-25324ab71aea | -4.0871 | -46.6151 | 2024-12-14 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| cf043a11-9e4d-3a65-902f-4d07175fc017 | -11.8295 | -57.8175 | 2024-12-14 00:00:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a0fa4a5e-f65d-3390-a258-c723b2bec026 | -11.8293 | -57.8373 | 2024-12-14 00:00:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c6e84833-f7f8-368e-9f3c-b28d07b0d3d7 | -12.5492 | -57.7594 | 2024-12-14 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0323f4d0-a5e9-3908-aa84-31a2bedc55e2 | 2.745 | -60.3723 | 2024-12-14 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bb542244-8cb5-3d03-93da-1c563564b00d | -12.5499 | -57.6996 | 2024-12-14 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8ece5c42-78dc-3f33-ad5e-6353975d63ba | -4.7252 | -43.1991 | 2024-12-14 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 1d199846-5349-3433-b67c-a412540aed61 | -12.5682 | -57.7579 | 2024-12-14 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8f4b071a-0d64-393b-bcab-64f96be6b489 | -12.5497 | -57.7196 | 2024-12-14 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 515e81a9-172a-36b9-88f1-9b86c75a265d | -2.328 | -45.525 | 2024-12-14 00:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bec74c0b-34d9-379d-a271-a0f385ca8abf | -3.5644 | -43.658 | 2024-12-14 00:00:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 73d3e229-076b-3c74-990b-c3a7f4e090ff | -6.0472 | -44.0331 | 2024-12-14 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a71f921d-d3b6-369b-bf6b-79e369f11597 | -12.5687 | -57.718 | 2024-12-14 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 372a4898-7390-3b4e-947c-16cd3bfa0fbf | -4.1057 | -46.6142 | 2024-12-14 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| d66699d1-eff7-3d12-add7-141ca7acd50e | -5.5331 | -42.862 | 2024-12-14 00:00:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 34551f82-846b-3dec-8841-319fa06bb316 | -1.7178 | -52.5553 | 2024-12-14 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ec64295e-9d26-39af-8f3f-c1185e47050a | -11.8295 | -57.8175 | 2024-12-14 00:10:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 97c4ec76-a635-3dc4-b75d-e7333ff8d853 | -5.5333 | -42.8385 | 2024-12-14 00:10:00 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 47.1 |
| 2a6eddf0-521f-3030-ab25-e3deee46388f | -10.2015 | -36.2115 | 2024-12-14 00:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 03f23567-7486-3dc9-b7ec-70a64605f7d9 | -12.5497 | -57.7196 | 2024-12-14 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4d43af1c-4885-3c78-9a4b-6551905b202a | -5.5331 | -42.862 | 2024-12-14 00:10:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| fb31bb41-1574-31e7-ba7c-01461b98bfcb | -4.1057 | -46.6142 | 2024-12-14 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| cc1ce331-69b9-3b59-a824-41172ee19741 | -1.7178 | -52.5553 | 2024-12-14 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c7a2ef38-e3cd-3b7b-8516-077acce4b7d5 | 2.745 | -60.3723 | 2024-12-14 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1f5673b7-cd02-3597-8f25-ff46bd3cfb69 | -4.0871 | -46.6151 | 2024-12-14 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 107ea5ee-a807-3f9d-b566-b223fa4e35f8 | -12.5682 | -57.7579 | 2024-12-14 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 902cb50d-9ca2-379d-a8ab-91b806a57004 | -4.7252 | -43.1991 | 2024-12-14 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ff897f32-64e2-3066-9fb3-546445eea7f0 | -6.0472 | -44.0331 | 2024-12-14 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 3c712e9f-921c-3b9b-9709-19e05f553ef1 | -12.5499 | -57.6996 | 2024-12-14 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 7d8c79e0-25ad-354d-a67f-bc5f9088a074 | -5.5331 | -42.862 | 2024-12-14 00:20:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 1ea68ddc-06cb-3911-b3eb-f1d864fae808 | -12.5499 | -57.6996 | 2024-12-14 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4736cc22-758c-395b-a01a-e7c34410321d | -12.5497 | -57.7196 | 2024-12-14 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 661d84aa-ada4-3b5a-b447-ba390176bbb4 | -1.7178 | -52.5553 | 2024-12-14 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 522c8164-d966-3afe-b004-c1d2b87fb761 | -6.0472 | -44.0331 | 2024-12-14 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 66720dad-9ee7-346e-a3c4-f12731f07d3c | -12.5682 | -57.7579 | 2024-12-14 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 929febc8-0a32-31e5-84a0-9a504049571b | -4.1057 | -46.6142 | 2024-12-14 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c24aea5b-e8cd-3cb8-bc71-81c31805ef4d | -11.8295 | -57.8175 | 2024-12-14 00:20:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 5dfabcb8-9ba7-3bc8-930b-53b4c729ecd1 | -4.7252 | -43.1991 | 2024-12-14 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8d1e8d67-83c8-3ab8-b6a5-f29db52502d1 | -11.8295 | -57.8175 | 2024-12-14 00:30:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7bf472c9-2da6-33b5-8364-5833e9764158 | -4.4082 | -45.8209 | 2024-12-14 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 49533d16-df8c-33c3-949e-bd3ab82548f3 | -12.5497 | -57.7196 | 2024-12-14 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| dd7b683c-725f-3204-b09c-e8a6e317917c | -4.0871 | -46.6151 | 2024-12-14 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 07758b24-5e5b-3171-9238-358863afb6d0 | -5.5331 | -42.862 | 2024-12-14 00:30:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| f30e7d00-416d-3598-97f1-5ecb45debf6c | -12.5682 | -57.7579 | 2024-12-14 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 71d7eab5-91eb-3e60-802e-f4297e9e3d80 | -4.1057 | -46.6142 | 2024-12-14 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 32887f37-e78f-3e1f-a5cd-ec98c46b162c | -4.4269 | -45.8199 | 2024-12-14 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e36d3889-dbe0-3460-938f-16ac7d962bb0 | -6.0472 | -44.0331 | 2024-12-14 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f34d90ac-d9a7-3fba-a9f9-77e57afe2ec5 | -4.7252 | -43.1991 | 2024-12-14 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 14fc5072-c478-3f7b-8e09-45fa17754ab0 | -12.5499 | -57.6996 | 2024-12-14 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f6e93c68-5f46-392e-aacd-83e6fc96b7d0 | -4.4081 | -45.8433 | 2024-12-14 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d378d35f-46f7-3d69-94de-2fbc06488329 | -11.8295 | -57.8175 | 2024-12-14 00:40:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 49b9eaae-94f0-3608-9806-2dad94812c8b | -9.8136 | -36.3613 | 2024-12-14 00:40:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| d287ef05-9b20-39eb-84ab-72e25a4bffa2 | -4.7252 | -43.1991 | 2024-12-14 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 44cd76ed-8492-311b-b1b3-0ac7262d5fde | -4.4082 | -45.8209 | 2024-12-14 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| d817e71f-b2a0-3f3a-a4d7-abcb9e602cf0 | -12.5497 | -57.7196 | 2024-12-14 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a821c4ef-da5c-31ae-be37-f2d51bd0235b | -12.5499 | -57.6996 | 2024-12-14 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c3d2d87b-513d-3f90-8d05-26b7e1e808d9 | -12.5682 | -57.7579 | 2024-12-14 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 20fbc9a2-51a9-3c9c-bdf4-64982387cc17 | -6.0472 | -44.0331 | 2024-12-14 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5c88982b-4d94-3a8d-a540-a0c996655203 | -4.7252 | -43.1991 | 2024-12-14 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| be5743d8-2b68-3030-9270-107c8d8a88d8 | -4.4081 | -45.8433 | 2024-12-14 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 282fc439-4b31-37de-aa09-f9b98073a703 | -12.5497 | -57.7196 | 2024-12-14 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e9731342-090d-384d-9375-62192e46fb1a | -12.5499 | -57.6996 | 2024-12-14 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ad2fb4d0-3110-3bcc-9537-de147c6c3b74 | -12.5682 | -57.7579 | 2024-12-14 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 53a378f0-2a60-3a35-b4d4-1acfba672dc5 | -4.4082 | -45.8209 | 2024-12-14 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 812b40bc-fb14-38be-95c7-9f67a511a568 | -6.0472 | -44.0331 | 2024-12-14 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ea734c73-deda-36c7-aa09-38d8ea554620 | -11.8295 | -57.8175 | 2024-12-14 00:50:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 051aa2e4-fdd6-37b9-833e-2d773806e05f | -12.92439 | -47.88994 | 2024-12-14 00:56:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 041e447a-66fd-3570-9adc-9c2187ad7d52 | -12.83452 | -48.36363 | 2024-12-14 00:56:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 79b7feab-43fe-32f4-903e-bcbff7627792 | -11.8263 | -57.83919 | 2024-12-14 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 265763ee-14f7-3149-9acd-501f42e110bb | -4.72478 | -43.20757 | 2024-12-14 00:58:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| e068ef4c-dbec-3736-aaa5-fe3595254c5c | -6.03384 | -44.03894 | 2024-12-14 00:58:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b1b4165a-5fb4-348a-8215-dab04525eb7e | -6.0473 | -44.03125 | 2024-12-14 00:58:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 521ccdb4-d780-3e20-a0af-ab70ba9025fc | -4.71854 | -43.21527 | 2024-12-14 00:58:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8864d467-9b1c-370c-b8f6-271e76e7627a | -4.72121 | -43.18468 | 2024-12-14 00:58:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 905384b7-f6d2-3a6c-add9-c58c2f333786 | -5.35683 | -46.2348 | 2024-12-14 00:58:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0d140f74-2e46-3009-a53f-001318b26f8b | -4.7151 | -43.19222 | 2024-12-14 00:58:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5b2a076a-c53f-3831-84b0-1d4e5fd3fa2f | -4.4133 | -45.82287 | 2024-12-14 00:58:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 087ad270-fc7e-301d-9b8c-fe888d5ff8e9 | -4.41551 | -45.83781 | 2024-12-14 00:58:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 220ad2d1-d242-30ff-a239-c0fae5456b95 | -6.04642 | -44.03725 | 2024-12-14 00:58:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 1b66111b-6932-30c9-9ec0-ebfcb1f64414 | -6.04922 | -44.05613 | 2024-12-14 00:58:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f5a3420b-5f48-377f-8aed-37c408ac0972 | -4.40216 | -45.82481 | 2024-12-14 00:58:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 6ddf5215-45f9-3796-b2bd-a5dfa3b56ebe | -5.36085 | -46.2277 | 2024-12-14 00:58:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1670f816-8dd7-30a2-8d78-c971fbc506e9 | -4.40438 | -45.83969 | 2024-12-14 00:58:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 63e24604-2344-3d39-9416-49d2cac7ae70 | -11.82279 | -57.80813 | 2024-12-14 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 7dc4bda3-f57c-3d51-b056-b09b1dbded8e | -5.42431 | -44.17514 | 2024-12-14 00:58:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7770c298-4962-36b4-93ad-202e242fe264 | -5.53795 | -42.85787 | 2024-12-14 00:58:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 45.1 |
| 85d7216b-06af-3e09-9bd9-82872350b025 | -6.05027 | -44.05028 | 2024-12-14 00:58:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 56d825c0-3099-3c4e-bd60-6487869aa92b | -7.88557 | -42.44216 | 2024-12-14 00:58:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| d507f365-c5ee-33a0-99df-174e259006eb | -4.4081 | -45.8433 | 2024-12-14 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 80f2aa26-e4b4-373e-9d60-b524703228b6 | -4.7252 | -43.1991 | 2024-12-14 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 72b385c0-fdc4-3851-a5ba-ab68c1aabd30 | -4.4082 | -45.8209 | 2024-12-14 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 0056c420-fc3c-3801-acea-b4119d97387e | -12.5497 | -57.7196 | 2024-12-14 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1e921212-92a6-37bd-b410-4deee11df763 | -12.5682 | -57.7579 | 2024-12-14 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c2ac733b-db85-3271-a8d7-85c2cd9af13f | -11.8295 | -57.8175 | 2024-12-14 01:00:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fb2ca10a-1ddf-3bab-9ca6-d1a3870fba56 | -6.0472 | -44.0331 | 2024-12-14 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f415df08-ab91-3a45-9bd1-eaf2ef1e9cfe | -3.50815 | -49.95475 | 2024-12-14 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7e50356b-7485-36f8-821f-fb655fa3aa83 | -3.39825 | -49.9002 | 2024-12-14 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ad7f20a-3651-39aa-b9b5-a2c1349b619f | -1.71636 | -52.56971 | 2024-12-14 01:00:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1040dfd6-a409-3326-8e7b-e1b8fd952544 | -2.80741 | -52.81169 | 2024-12-14 01:00:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 28d4f450-6273-30ef-9120-0301f7aee5dd | -3.01692 | -51.39103 | 2024-12-14 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README2.md)
