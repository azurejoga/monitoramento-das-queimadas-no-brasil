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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bbe9d43-82ec-344f-b90e-9a1017705f8c | -6.65154 | -58.8229 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5abebae1-e23c-3e9d-9a52-e98c25036826 | -6.55433 | -56.20273 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff5aeab1-1042-3f64-90f0-9f59b585a7ad | -6.38098 | -53.32753 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d10ec36c-91ac-3824-bf2f-dce762b2724e | -6.56113 | -56.1835 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1076e1b5-add4-3fd6-9546-62d7008d37fd | -6.4578 | -53.36461 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d21a3ff-d8d2-394a-b469-612f29a0a15e | -6.65901 | -56.39067 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f42fe464-737d-31e4-b88f-781625dbf3b2 | -6.52752 | -56.19209 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 113d2881-cf39-3490-a4b3-6ac25407a48a | -6.54722 | -56.19674 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4ec69b5-1855-389d-bb79-d6a0a21a7a10 | -10.15394 | -67.23073 | 2025-07-31 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60609723-cf05-3241-b69f-cb2fab8f022b | -6.52307 | -56.19815 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce8bd8da-243a-38f0-ab45-077fb0618005 | -6.50503 | -56.20895 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6db3a9b5-ec57-3cc9-b188-203e73cbbad0 | -6.37413 | -53.33096 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db439308-56ee-3d3b-aefb-300a0fd801fe | -6.90161 | -52.86253 | 2025-07-31 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a25b95b7-8feb-3ebc-882f-da9a6538b2c6 | -6.66749 | -56.38679 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 561bba44-662f-338f-8607-586ab4672456 | -6.20212 | -57.5832 | 2025-07-31 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b7e11e1-df92-330c-a3e3-00ee2389b4b8 | -6.45852 | -53.35957 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a13e794-13e6-3295-b4d2-7a7bec2e3b41 | -6.5458 | -56.20654 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5288c47-93c0-37c6-b995-b3bf92204102 | -6.52362 | -56.19147 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a004aff4-edf3-3624-84e0-f0eed131598b | -6.51597 | -56.19196 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35b57cef-19b0-3cee-a4ba-21bb22ffea45 | -6.56431 | -56.18907 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e5ed98d-80f6-36a4-ac23-0d26fb88342f | -6.64812 | -58.82238 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceb63963-72db-3eed-8b4b-9c4ce178779a | -6.52235 | -56.20312 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 37857500-6cae-34f8-9e47-3e099c9457a0 | -6.53088 | -56.19934 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a36033c-e0d0-3e28-9481-0187ea415c77 | -6.9581 | -56.37664 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8f16b84-866b-31e8-832e-170ed06c0fc6 | -6.52164 | -56.20808 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fa97ad4c-ea1c-34f4-b9fc-ea81582cd350 | -6.90349 | -52.86449 | 2025-07-31 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f9f6cbf-bd9e-3f7d-a3d4-3de656947540 | -6.56359 | -56.19403 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31e44736-13b7-36ef-a610-8421caf39921 | -6.50355 | -56.21883 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2d45117-090b-3609-9632-ee5049cd9fba | -16.36803 | -52.6615 | 2025-07-31 05:25:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29f64761-50c0-32dc-9e37-a0b2d4748570 | -10.09962 | -63.19292 | 2025-07-31 05:25:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 975df523-c72f-329f-922a-b02dd115fa08 | -6.5082 | -56.21446 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b580bb3-874d-3539-8590-27237bb6124e | -6.51581 | -56.19027 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e44a7e1-95e8-3be0-936d-48a5a516637a | -6.49259 | -56.21214 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd16955f-a0f9-3f49-a9c5-26981a357ba2 | -6.53016 | -56.2043 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fda8e42a-baba-3654-98cc-75fa8f621553 | -6.52603 | -56.20199 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94088af9-1e49-3d2b-99d2-7e57e397b4a4 | -6.56504 | -56.18409 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 147e60de-7785-3084-bda2-819379c70e67 | -6.51989 | -56.21624 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62efa10c-61ec-32cb-bd92-69c5f1410e9f | -6.50334 | -56.19355 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b77b060-207a-3370-9aca-94b3d981db03 | -6.54189 | -56.20596 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f357470-1911-32cd-9a7f-a6d45d7e091b | -6.90273 | -52.87011 | 2025-07-31 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a6143ef-654d-3e10-af36-d9ab92fd9341 | -6.9008 | -52.86815 | 2025-07-31 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb5904e4-3fde-3f7a-96f0-3a9521fa456b | -6.66463 | -56.40612 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbe4bf0d-ca19-39ba-ac04-cfe9a796b8df | -6.5323 | -56.18944 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f39ba625-48d5-36fb-9802-5eaee6cdd870 | -6.65372 | -56.39977 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c6eb382-05f6-30d1-9fa5-766026b2d659 | -6.67304 | -56.40266 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f5713b56-7bca-3439-b902-25e5e32e3660 | -6.64755 | -58.8261 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ede08fd-170a-3f86-a14a-27384ecc1359 | -6.50994 | -56.20626 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a206756f-03ec-36c2-81ee-e2539bd84102 | -6.66077 | -56.40555 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63e2eb34-bd72-317c-9571-5c6947c53df7 | -6.52138 | -56.20635 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35a369bd-df84-3385-9f3d-b60150babcd1 | -6.55361 | -56.20769 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b218d4a5-ef83-34f2-b545-6218e5ce054a | -6.52768 | -56.19379 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cabcce98-459a-3f72-9cee-86eddebd9d0f | -6.6629 | -56.39112 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eba1902b-93b3-343d-8174-d87deb2c7702 | -6.52626 | -56.20371 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d075068-14d2-332b-9049-b334de50c13b | -6.51845 | -56.20251 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 91dc955d-ae5b-36a5-8633-c1e53e12fa0e | -6.65832 | -56.39541 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d93e8bdf-94cb-3ef5-a0e6-cec8cb82beb6 | -6.51206 | -56.19137 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f82669ef-d283-3c46-83a4-9873814b8fc9 | -6.51988 | -56.19256 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e332b658-4bfd-3ed1-bbb1-cbf7211b0456 | -6.51116 | -56.19465 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42efaf3e-e272-3083-9524-a4e6e12e7357 | -12.62774 | -48.09508 | 2025-07-31 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b29befe-f72d-3650-89c2-d36501f1084e | -6.66992 | -56.39706 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 86b744fd-7590-3ef3-89c5-a3ee7384c40f | -6.67377 | -56.39774 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3214400f-1965-37fc-bd4d-e9df83930266 | -6.49944 | -56.19297 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aea55611-a58f-3d8e-802f-f8d275578c07 | -11.74237 | -58.34367 | 2025-07-31 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3818aee-d721-38a2-a2cb-994b3c60f5b6 | -6.40848 | -53.37275 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e33289-0e99-3e44-84f5-a64621c97f4a | -6.96198 | -56.3773 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ea7d986-ea08-3335-93e4-6cb7d4a99ca3 | -6.67233 | -56.4075 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 31e9749b-47c8-33a5-90c6-1a8fef5799be | -7.74381 | -51.08757 | 2025-07-31 05:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9961174e-bd3c-3e1f-970c-a53a4a810b50 | -6.51774 | -56.20747 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e8d4b7b7-c962-32ea-8ae1-5641fa414099 | -6.40779 | -53.37773 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0569a8ec-fbbf-3d82-a089-5752d3b38ca8 | -6.51507 | -56.19523 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6dc524fa-2827-3a78-adaf-f3a7045b509d | -6.51065 | -56.2013 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12d77f1e-0fff-30f2-8fc3-585dfafcc956 | -7.74888 | -51.09241 | 2025-07-31 05:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d37d2929-8ff1-3350-9bfe-ae4f60a8428e | -6.51823 | -56.20079 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d4bf30d8-5cb7-3450-8ece-4de80c7b93f2 | -17.15248 | -49.99076 | 2025-07-31 05:25:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15a12d9d-3fb7-3967-8b07-327f64a770d0 | -6.51916 | -56.19754 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7c4c0647-de6d-3d20-9171-e6ec2286d2c9 | -16.36844 | -52.65766 | 2025-07-31 05:25:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 153f594a-133e-3e38-8fdd-cc1cdb523ed5 | -6.66392 | -56.41095 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6f58c654-95c4-39c6-9fd3-4fcccc764938 | -6.41861 | -53.36918 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ad95fa3-f576-374b-af01-72b787d83026 | -7.05364 | -55.43015 | 2025-07-31 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb0c2ce7-ef53-37dc-855a-fcb87650334c | -6.6622 | -56.39588 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 51347d0e-195c-34d1-9ab1-3e476b1f2202 | -6.50187 | -56.20342 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c41b948-17a6-3293-8088-fd49b09c11c4 | -6.52378 | -56.19318 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1a1da08-9eff-38d6-8b21-dbc0b5a961c7 | -12.25513 | -63.81202 | 2025-07-31 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 702d1b8a-b05f-375f-8621-3d1df713d03e | -6.55649 | -56.1879 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 844d5130-9836-3351-b874-4fcf5a33b833 | -6.39182 | -53.31887 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0874b4ce-b866-33d1-8051-900cd1029433 | -6.51674 | -56.21069 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 637fd28a-8e03-3efc-96fc-c93f5cb4a0ac | -6.67065 | -56.39217 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd30cc80-c5b2-3601-8213-f0852e88028e | -6.67762 | -56.39844 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ee9ce4c5-4161-3e6f-ba45-8b8fe786b447 | -6.5497 | -56.20711 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a604b9-0217-3fa6-9c63-003c6242c846 | -6.54118 | -56.2109 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a6ab9b4-e9aa-3cb5-adbc-ab4ef9ef535e | -6.52449 | -56.1882 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a414136-0ab7-3525-8db8-6e1697b131b4 | -6.5026 | -56.1985 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e62aaa8-a516-3d14-ab00-9a3c593c46ff | -6.65689 | -56.40509 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1845a8b2-bc1f-3a8f-8a3f-223b68e91774 | -12.63426 | -48.10201 | 2025-07-31 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3ec8580d-5048-35ce-a842-467b8439733e | -7.74945 | -51.0882 | 2025-07-31 05:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e3399c2-4bab-34ca-9398-d9af52922805 | -6.67689 | -56.40339 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 63ae79bd-8a5b-3e7e-a83f-5f41da242a36 | -6.21142 | -55.63988 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92af89f3-5192-3cf9-8678-d3b93c91d4a9 | -6.68429 | -58.86208 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4366ad1-6be0-34ad-9415-2f2d152184fe | -6.51703 | -56.21242 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c5c7a35-e4aa-3db0-9f2e-4e1d01b0657d | -6.52528 | -56.20693 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README16.md)
