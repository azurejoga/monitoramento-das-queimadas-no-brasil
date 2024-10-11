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
| 86bdde35-fda0-3c10-9ba5-750b17a86044 | -9.18351 | -51.49337 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c1e4be-3ae5-341d-b411-3400070ec62d | -9.17755 | -51.492 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d72e79f0-5775-364b-ab83-a23f495a3a49 | -9.10515 | -51.29657 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7668a300-9af6-3261-af67-f982a47eac84 | -9.10212 | -51.29284 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51556e35-4957-3d93-84b3-74084e51bbab | -9.10127 | -51.29725 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8526641-2a9a-30c9-94a3-4ac0ae34456e | -9.09923 | -51.29535 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c19d00-c642-3b39-b2ec-d95ef14461c3 | -9.09534 | -51.29605 | 2024-10-11 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dd3c694-000d-3923-8cc2-c9fcea12c277 | -10.85504 | -51.06078 | 2024-10-11 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70c910dc-8197-338d-bdb3-71314a7e84d1 | -10.85384 | -51.06023 | 2024-10-11 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 825c4f9b-08db-31c8-ae90-4311724f6ded | -10.44542 | -51.8834 | 2024-10-11 04:02:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d3c7882-e01b-3841-ac67-192f4591a2fc | -9.62826 | -51.76938 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceebeb93-4e54-34e4-b326-cddfebc9cff3 | -9.62308 | -51.76358 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fac89ad2-5732-3ab9-a640-7fab072d1363 | -9.62221 | -51.76818 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c496263-df66-3c3c-b3e8-eed9878b9b0f | -9.50132 | -50.98647 | 2024-10-11 04:02:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b38636cc-1e4e-3eb7-a4e1-8d4f39338bb2 | -9.49627 | -50.98154 | 2024-10-11 04:02:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e79ea649-1ecf-3df6-a17c-55c60f0f5a09 | -11.28984 | -50.93692 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ff0aed0-4863-3894-8978-496090e06981 | -11.28746 | -51.08226 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 271bb28b-a06d-35a0-99b5-af57ec24ee75 | -11.28527 | -51.08365 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3095381c-2228-300d-990d-24334abac1ca | -11.27981 | -51.30187 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db300e79-b305-382a-a7e6-4307fa37cb47 | -8.86317 | -53.0134 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f46dde47-7b02-340f-bb31-596ceebdc889 | -8.86205 | -53.01925 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1e7691f-8cd3-36d0-9f9d-597d616af20d | -8.86089 | -53.02532 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86ee2bf9-a5ed-38e2-a509-226a954aa570 | -8.86038 | -53.01371 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 024b9704-cc21-3c31-8ec7-2f13aa354a61 | -8.85926 | -53.01937 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6873cac4-a1ef-3169-b1fd-ac7cfa40b27a | -8.85669 | -53.01139 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dae44fdf-def8-3cb0-abcb-b1f338b0f81c | -8.85565 | -53.01684 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74dbe289-5d44-314e-ba27-bb7d7e6dfd47 | -8.8549 | -53.00673 | 2024-10-11 04:02:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4604b7f-2d78-31c2-b9db-b8285ae4ed4e | -9.77642 | -52.04947 | 2024-10-11 04:02:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 473fdaa6-8595-3fcf-868b-3b2aac0e4030 | -9.77028 | -52.04821 | 2024-10-11 04:02:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16c3101e-b4d1-35d9-81cb-3f1661651284 | -10.05343 | -52.08073 | 2024-10-11 04:02:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d8ff8a-063f-30b1-9cb5-8cd98a26fc30 | -10.0525 | -52.0855 | 2024-10-11 04:02:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aec43c71-c82e-362c-927a-fd726ccc954c | -12.85499 | -53.48857 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2952ee98-d325-33ba-a64a-45eb255bc77b | -12.85389 | -53.49383 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7d69f9a5-ef91-30e7-bc3e-7de744ab2150 | -12.85374 | -53.48711 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 714a6032-0e7b-3427-bcdc-2a1acb018395 | -12.85267 | -53.49239 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6f007bf1-dd61-34f9-9eee-2c4a175fded7 | -12.84864 | -53.48721 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9b996696-854f-3abb-8a59-1947dc66b8cb | -12.84754 | -53.49247 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 618ddc2b-33b9-33dd-8719-85d9df91eef3 | -12.84739 | -53.48572 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a6289f65-78b8-37d8-84e2-bcdf5beaa4f3 | -12.84632 | -53.491 | 2024-10-11 04:02:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| aa9e740f-ec4f-3a36-823c-42ad280498ee | -14.81986 | -54.60485 | 2024-10-11 04:02:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6526baa-5ca1-3b30-b82c-450cfb1fff80 | -14.81844 | -54.61143 | 2024-10-11 04:02:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f11465b7-7f0f-3485-b83f-a2e6f1faf69b | -14.81322 | -54.60387 | 2024-10-11 04:02:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c50ae8bb-f033-30a8-aa8f-a430d0d7cff8 | -14.8119 | -54.60996 | 2024-10-11 04:02:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 075bbfc0-4acf-3eb2-8722-17283639862b | -4.11 | -48.25 | 2024-10-11 04:05:04 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab4b13f2-6f23-3d20-af65-4073720238bf | -2.6716 | -53.3502 | 2024-10-11 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a69a14f2-ca6e-3509-9cee-391d46781598 | -2.6533 | -53.3506 | 2024-10-11 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f7d0d2e0-a54f-3585-80b9-1892cfa79449 | -2.9857 | -52.8961 | 2024-10-11 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 35ebea60-883b-391a-a1d5-7ba8cc851318 | -2.9857 | -52.9164 | 2024-10-11 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 26cf4065-0cf0-39eb-ad63-de91692a48fe | -2.9673 | -52.8966 | 2024-10-11 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0b5e2e12-c68b-3c3b-a013-1438b8da9058 | -2.9673 | -52.9169 | 2024-10-11 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 5b961602-fb88-36af-89c0-6193f9ca1c38 | -3.1607 | -50.4556 | 2024-10-11 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7a467b21-cb10-3d4a-a3d2-d751724a0b4f | -3.1422 | -50.4562 | 2024-10-11 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 92c444d2-171e-3c4a-9ad8-f68b6a12dc59 | -3.1608 | -50.4347 | 2024-10-11 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| d9ff59b2-5b8a-3c88-92cf-7c81d1580dfa | -3.1423 | -50.4352 | 2024-10-11 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c44c2855-7f6d-318c-9ea0-eb6e4c20b08c | -4.0961 | -48.2739 | 2024-10-11 04:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 40ba9b9c-4a9c-39ca-87a8-b8ca14242a9e | -4.0962 | -48.2523 | 2024-10-11 04:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 58d60b53-2ae6-3980-b0a4-2b215090abc0 | -4.0963 | -48.2307 | 2024-10-11 04:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7aa606d7-3d48-380f-b0ac-c54308742d94 | -4.1146 | -48.2731 | 2024-10-11 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 0b7f67b7-b19c-3033-b369-34a97806f0ab | -4.1148 | -48.2515 | 2024-10-11 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 457.4 |
| fa6c8c05-e191-3ab7-8afc-af971941cf96 | -4.1149 | -48.2299 | 2024-10-11 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 20a0e303-4d56-392e-a0b1-32a94c131504 | -5.2486 | -48.0424 | 2024-10-11 04:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a0365b03-58cb-3ee6-af97-9f5458af298f | -7.4991 | -34.8741 | 2024-10-11 04:05:48 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 153.5 |
| 17fbafd0-3873-3d2c-bffb-0b609b39084f | -7.4995 | -34.8464 | 2024-10-11 04:05:48 | GOES-16 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 6be51ae1-1050-3fd8-be67-862e68938dc5 | -8.4231 | -55.4704 | 2024-10-11 04:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2b69773a-9355-34f7-bd54-dca48e8e2f57 | -8.4417 | -55.4692 | 2024-10-11 04:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f0a1c0db-e03f-3071-9932-23282a5bd83c | -9.6389 | -64.9664 | 2024-10-11 04:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 06f585b6-4aac-3b36-ba8b-a83db89f874f | -9.6575 | -64.9658 | 2024-10-11 04:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 49e07585-aeb2-335b-b962-38dca1acedf4 | -9.9481 | -58.1092 | 2024-10-11 04:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 8ca63921-d3e2-3e11-9f8c-c1a35db8062b | -10.6962 | -53.0354 | 2024-10-11 04:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 8e7933f8-2d07-3a41-b314-7df2eda2a261 | -10.7059 | -64.1138 | 2024-10-11 04:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6199c033-9b96-3608-8241-6daedf38223d | -11.2597 | -53.272 | 2024-10-11 04:06:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| cd490d85-6639-3a09-aad3-d1d64c08f0cd | -11.2407 | -53.2738 | 2024-10-11 04:06:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 569fa3b5-74ee-368e-a0cf-df1314c9a381 | -11.2763 | -60.4844 | 2024-10-11 04:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7ae0f60a-53a8-3953-ab6a-4f241f7e5d35 | -12.4373 | -53.1523 | 2024-10-11 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2fdeeadc-809d-31a9-82db-25319268a642 | -12.4563 | -53.1503 | 2024-10-11 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b9e19d8c-9e19-3657-a139-1f3622c00002 | -12.4182 | -53.1544 | 2024-10-11 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 305b5ee3-71cc-378a-b953-5e809b613f0e | -12.7871 | -44.8639 | 2024-10-11 04:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1fee2b99-e8db-3e8e-8310-f5caba7fb915 | -12.7678 | -44.8671 | 2024-10-11 04:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| c056a8fc-03c7-3c72-8272-0aca5131ef78 | -12.7673 | -44.8904 | 2024-10-11 04:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 215b8dba-f698-3f66-8e17-ba9eb0057e2f | -13.7346 | -60.6079 | 2024-10-11 04:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6b2f1171-87bc-3b4e-9d45-62b9116575c7 | -18.1975 | -56.4441 | 2024-10-11 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 8596ac5f-82cc-3bc5-8bb7-14d989c8dc76 | -18.1971 | -56.465 | 2024-10-11 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| b8fc1263-e410-34c1-871b-8e0eefee4a81 | -9.35283 | -35.96133 | 2024-10-11 04:14:00 | AQUA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| 3a2cde86-2962-3dc7-ae28-7f2eec59ef89 | -9.34893 | -35.95068 | 2024-10-11 04:14:00 | AQUA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| c6a414a3-3df5-3c0b-8774-7e3341b2adb8 | -9.34612 | -35.96722 | 2024-10-11 04:14:00 | AQUA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 01d6d4e0-45ef-3945-83d6-d0a3b5fe24f6 | -7.50106 | -34.85563 | 2024-10-11 04:14:00 | AQUA_M-M | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| bcb7f778-539b-35ca-ac90-08165a1e29e7 | -7.50027 | -34.86383 | 2024-10-11 04:14:00 | AQUA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| e0d8538d-db5b-3413-a434-ea1f9363bc42 | -7.49861 | -34.87048 | 2024-10-11 04:14:00 | AQUA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| dca7dd1c-fd37-31d1-8601-7eab873a102b | -2.6533 | -53.3506 | 2024-10-11 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 4cd73d6a-4216-361f-befa-2389b6940d16 | -2.6716 | -53.3502 | 2024-10-11 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a338c539-9cd2-3f5d-a591-86ab38fe6ea6 | -2.9673 | -52.9169 | 2024-10-11 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 23a96271-05d4-38fa-86b2-53bf947e56b9 | -2.9673 | -52.8966 | 2024-10-11 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b09c82fd-bc87-3d97-8cc3-df3510f04134 | -2.9857 | -52.9164 | 2024-10-11 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ae58fa5f-eacb-328b-aeda-0b44254c0b17 | -2.9857 | -52.8961 | 2024-10-11 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6263d487-07aa-3f0d-a09e-53887d726534 | -3.1423 | -50.4352 | 2024-10-11 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 46d3e740-5ba3-3cc3-abde-23f611fbb7e4 | -3.1607 | -50.4556 | 2024-10-11 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f6dfbda0-b5f0-35e5-a3c4-2b27101d744f | -3.1608 | -50.4347 | 2024-10-11 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 4a1eda61-b7e8-3459-b16f-bace3a55354a | -4.0962 | -48.2523 | 2024-10-11 04:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 2ede5c71-c0b3-37e0-a98c-3448f754710c | -4.0963 | -48.2307 | 2024-10-11 04:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 913da94e-bd24-3660-acd7-d65bb0dc18f5 | -4.1146 | -48.2731 | 2024-10-11 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |


[Clique aqui para ver as próximas entradas](README46.md)
