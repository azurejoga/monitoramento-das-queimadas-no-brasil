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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acffcf07-8fe7-33c3-bc8c-4325d0146329 | -9.74171 | -50.65229 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98e629b2-6613-3d1d-887c-e9404cd2ea7d | -9.73765 | -50.65154 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc9751f-25f4-3b40-bbc4-eec8d7dbd45c | -9.73295 | -50.65446 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f933e0-ed11-3a12-8656-899aaff8961d | -9.72887 | -50.65376 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a972f9b-c315-3161-a247-ddfa4642d4fb | -10.44598 | -50.7123 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed8c9240-e3d6-310f-8483-cbb54c9d90d2 | -10.44572 | -50.69008 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfc353ef-14ac-355b-a948-1dc713f2ddc0 | -10.44535 | -50.71588 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e0516cee-0093-3882-8bb4-f9a765bad44a | -10.44509 | -50.69368 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4082e1bb-023a-3b3e-a9f3-75bdd8a34de4 | -10.44473 | -50.71947 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cc82ebb6-24c3-3e5e-be52-48116f765781 | -10.44446 | -50.69726 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 693ed5dc-98e8-3653-9077-312c2bb67bf8 | -10.4441 | -50.72305 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15e130e2-f1ef-3e1d-841e-95c54ece2d57 | -10.44383 | -50.70082 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 24b79401-b68b-3ece-ad3f-9966898c40de | -10.44347 | -50.72663 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 847eda2f-8bfb-3961-99ba-480bf7465fe1 | -10.4432 | -50.7044 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 71eb2fee-8a22-3deb-9b0f-aae97227d798 | -10.44284 | -50.73022 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b7abcd6-50a5-3499-80c8-c4c3b6538920 | -10.44257 | -50.70798 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 2fb0dfc5-9aa4-351e-b4d1-1635d277efce | -10.44221 | -50.73381 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2011596a-00c2-3506-b675-6f47d0fe215a | -10.44195 | -50.71156 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 4abf5080-1a72-3d89-91ce-f14f45d51536 | -10.44169 | -50.68934 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 408983e9-7ddf-3fd7-9fbb-4032eb1d2bed | -10.44131 | -50.71515 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3f4f3c36-5b70-38cd-8640-21b49b2dfebc | -10.44105 | -50.69294 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b316ddc2-ad9b-32db-8b4c-47e123ab6181 | -10.44068 | -50.71875 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8fbd5f03-3019-3317-9937-0f0ce740818a | -10.44042 | -50.69654 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 52632e4d-3b1e-34e8-a8ed-62a02c861585 | -10.44005 | -50.72234 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0a0488a2-2f26-3aac-b612-0c9998c2bc20 | -10.43979 | -50.7001 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 41db8147-8e51-3826-8774-def287a61387 | -10.43942 | -50.72594 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e66c4a98-5f0c-326d-95ec-369404e9a225 | -10.43879 | -50.72953 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c1f2ca9-0620-3956-8a36-53344cd46f3a | -10.43854 | -50.70725 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 7cda2685-2497-3d2f-bb22-8d5201b7d317 | -10.43829 | -50.685 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 180c6668-5628-3d61-b830-d51fc655d53a | -10.43816 | -50.73312 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0eb6eafe-67ca-3ff2-812e-5edec71dc8f5 | -10.43791 | -50.71083 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 02ab704a-0b79-3f21-add7-02e6a6fb648c | -10.43766 | -50.6886 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef3ae1e8-e397-37f5-ae8a-1e5c998fbd6b | -10.43752 | -50.73672 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b49d7862-113b-31a2-a2d7-012f449089c4 | -10.43727 | -50.71441 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| f21536c1-d02f-32d8-925a-190942c586b8 | -10.43702 | -50.69221 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7999d668-63e0-362b-b19c-c49a4b4f6905 | -10.43664 | -50.71802 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f5cc40c6-4d11-3540-a4da-eb7971849445 | -10.43639 | -50.6958 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 5a14d649-aeef-331e-95a3-2702c7307d9a | -10.43601 | -50.72162 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 30305b01-8eee-3f49-b8eb-1a8dabb99c07 | -10.43576 | -50.69939 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| b99709d0-ed4c-32a0-9a40-c819d11e81bc | -10.43537 | -50.72522 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b30697ce-d7d1-3531-a6c3-a6b567fd1ca5 | -10.43474 | -50.72882 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa644bd5-152c-3612-872c-131d5aea1096 | -10.4345 | -50.70653 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.0 |
| ff0652c2-4019-38ef-9b6c-30b734717742 | -10.43387 | -50.71011 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 6a5e7f43-9283-3048-8015-ea19a42bba69 | -10.43363 | -50.68784 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f8de4ab-a69e-3ac5-952c-658deb0d725a | -10.43323 | -50.7137 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 436e6d07-f066-3682-89df-59f225f386d2 | -10.43299 | -50.69146 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c968c4ba-8f0c-3000-aa18-f97500af5c80 | -10.4326 | -50.7173 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 66899e20-7370-3388-9358-22c97102db5d | -10.43235 | -50.69508 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 9eca86df-79d0-3a44-b17e-08a082163d93 | -10.43196 | -50.7209 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 250bc94b-17e3-32d5-b7a3-a7f5883b1999 | -10.43172 | -50.69867 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 7458faa0-81a5-306b-b668-6bed81ba7c78 | -10.43133 | -50.7245 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3940d56-6379-34ca-91ea-eacfe5a6753e | -10.43069 | -50.7281 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f74c75d2-07e8-39ad-a9bc-2dcc48a674bc | -10.42982 | -50.7094 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| cd2e0af7-202e-36a9-b7f2-50ff06ccccef | -10.4296 | -50.68706 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7f854ae-4b09-3658-8f07-5d93e5e4f835 | -10.42919 | -50.71298 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 933da3ab-bfca-39d7-bdf1-da73dd9592cb | -10.42896 | -50.6907 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba7271ab-fb49-3ba0-99a5-2ee81cb95f15 | -10.42856 | -50.71658 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 391bfa02-5901-35e9-86b0-604119146883 | -10.42851 | -50.69101 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a804728-dc29-3978-9beb-5ed3bbc6b168 | -10.42832 | -50.69433 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68cd242e-96b3-300a-ba31-2207770e81ef | -10.4279 | -50.69465 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b65ce171-7af8-3ab9-b32d-46d4dde48fce | -10.42768 | -50.69794 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c3c9228-b885-3b7b-aee5-b13324400101 | -10.42729 | -50.69827 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d25133a-5d47-395e-949b-f7e9a8331782 | -10.42705 | -50.70153 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| bdd52d91-98d4-3f66-9493-d8cc5839ffcb | -10.42668 | -50.70186 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 89c5f1de-1721-3ad9-b922-ae3291562765 | -10.42665 | -50.72739 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fb070d3-b8ea-3281-90f6-f499516e0c69 | -10.42641 | -50.70512 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| d76099c6-5100-392f-9b76-a5a6ef0c22a1 | -10.42607 | -50.70546 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 38e56f3c-8a28-33b5-9324-cb1314fa375c | -10.42601 | -50.731 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6044173-ae22-3a16-b85d-2e57413709cc | -10.42546 | -50.70905 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 6dc32414-5615-3eca-aef3-d99fce68abc5 | -10.42515 | -50.71229 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 524eb906-38a2-3cb0-878c-1b6f0e11db18 | -10.42493 | -50.68993 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7210c82-8b33-3c97-9a88-c5ae33cc90b6 | -10.42485 | -50.71265 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| d57a72c1-314b-32dd-85d5-f2abfc78b88a | -10.42429 | -50.69357 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89ad35d2-bf48-36b0-b773-93b947535790 | -10.42387 | -50.69389 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f201a1-7826-3b74-bd9a-28298a153b3f | -10.42365 | -50.6972 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2114122-c54b-3f30-b14f-293212ae5c88 | -10.42325 | -50.69752 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9fa0baf-f623-3731-b6ec-404cf0c34bce | -10.42301 | -50.70081 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 77ffc78f-c533-312d-9a5c-9747c5d9ebf8 | -10.42264 | -50.70114 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2ad0c146-2a50-3064-aedf-6fe071ac0a1b | -10.4224 | -50.7271 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 079ead12-bc98-36ea-8d4f-e5256eae5b08 | -10.42237 | -50.70441 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| ca44125f-9796-3e53-8c5c-2712e81b6d9c | -10.42202 | -50.70475 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bf0dbc74-754c-344d-9c5d-6d7931718613 | -10.42173 | -50.708 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cf2e3dbf-37fe-384b-8bfc-0e2f990bc087 | -10.42141 | -50.70835 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 5d7b0f9f-a1b9-35a8-86f5-8388785142d7 | -10.4211 | -50.71159 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5a919d88-0501-37bd-a83f-14e990e12569 | -10.4208 | -50.71195 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| b9dd57d3-1cf5-3998-b93b-87e0cf845e12 | -10.42019 | -50.71556 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 48d889aa-c2cd-3c51-86b7-adac5e9bc236 | -10.41982 | -50.7188 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a67da4a7-d06d-309f-9a5e-ebe734959cd0 | -10.41958 | -50.71917 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0001d908-2217-3575-be6d-3c6f28534af3 | -10.41921 | -50.69678 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70ac21ec-72a5-3765-adf5-235f47c4530d | -10.41918 | -50.7224 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| eefbf3bc-0987-366d-a577-d6dd338f78ad | -10.41896 | -50.72278 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e8199f28-99a8-30ee-be16-81325a232f54 | -10.4186 | -50.70041 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 647fa498-8e30-39c5-9665-14dbfad69567 | -10.41855 | -50.726 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| dcca313d-7b47-3d20-9b34-2daa56c607a5 | -10.41835 | -50.72639 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 71150193-4309-36ae-8d2a-84ac65069c3f | -10.41798 | -50.70402 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e47648ac-b6b8-3569-95de-e48f89c96f87 | -10.41774 | -50.73001 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee515853-d50f-3d08-94a9-d6bec835197e | -10.41737 | -50.70763 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c5e5bb7-3a89-35ae-9ab9-e588c5f50f5a | -10.41676 | -50.71124 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 012ec3aa-a97f-390a-b13d-1299c3b007bf | -10.41614 | -50.71484 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bda20220-7d52-3b82-a6e7-aa92e7a0047a | -10.41553 | -50.71846 | 2024-10-06 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README80.md)
