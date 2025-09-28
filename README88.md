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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1effe744-84c0-3f8c-85cc-8ce2c614beab | -12.99392 | -49.44286 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cadd2413-8931-3051-b252-41cd1f48d305 | -9.91238 | -65.00518 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc767b64-90e0-3441-a1f1-bdf3ea71545f | -13.7921 | -48.32771 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b376f21d-2e0c-3a55-aa22-6e51a45d5d96 | -13.58682 | -47.3079 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c874a886-d0c4-333b-9ecb-f97c137f6c18 | -11.62622 | -52.85736 | 2025-09-28 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45322d6c-5764-31bd-9096-1864e7f4c3ef | -10.97094 | -49.5735 | 2025-09-28 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79e27ce4-e3aa-32a0-b580-49a649e1df6d | -10.18673 | -62.22492 | 2025-09-28 05:18:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e214106-73d3-3068-8ee6-a4de135b708d | -13.0049 | -49.45319 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 24a5468a-2912-3ee3-845f-ea54707fab61 | -9.98646 | -57.81767 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23df00bb-cf82-36c5-878f-f67c9d7d395d | -9.80652 | -61.4928 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77fea749-3e20-3011-9335-052e39669caa | -12.65531 | -51.66637 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e0137a2-ce12-3534-ba44-09e0f95b7073 | -9.41437 | -54.69669 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db1db8ec-fd71-3462-9244-77fa5f0a3b77 | -9.87459 | -64.76218 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86c8560d-e9cf-3cdb-8667-be86609e4cb5 | -10.96514 | -49.57275 | 2025-09-28 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 486cdd45-a72c-34cb-bc8f-25e3e48af03b | -13.32038 | -47.31252 | 2025-09-28 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ae14ee05-a702-3ec9-a2dd-0cc9f3ae5e77 | -9.73832 | -62.36491 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dec64301-d697-335e-9b64-9f66bdf7b3ad | -9.76381 | -65.03812 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9a1326f-4864-3c7e-b602-7f06dfef7bf6 | -12.68636 | -46.87778 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e6337f80-1141-385c-af31-dffe0e6914f5 | -11.9789 | -47.07145 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 13431edf-bf0d-33b2-aaba-e02837d5870c | -13.6059 | -48.10163 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d81d2f45-d42d-313f-90e7-f4fc753d8f6e | -13.62811 | -47.31723 | 2025-09-28 05:18:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05f605e9-b639-3e2e-8865-1d44d5e4a43a | -12.99502 | -49.43319 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d3d8edf-d1ca-3687-86bc-46cbedffbd65 | -9.91112 | -65.01236 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 052f7682-bffa-3899-8611-c2d0d0ab3c9e | -13.00791 | -49.45056 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5fc49af0-7a4a-3fe4-8e15-2de7c48661e6 | -12.6308 | -48.15335 | 2025-09-28 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e907c1f0-3ce8-3619-8d2e-4ecefb366ef6 | -10.00297 | -64.24604 | 2025-09-28 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 388c027d-a0c1-3e37-8c06-50137e0c7f03 | -12.99347 | -49.44677 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5b3537ad-2819-3f85-9e6d-f7d1ccb60139 | -9.56425 | -63.20722 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bbb53fe-c06b-37f2-b220-a43ad7cf8142 | -12.6535 | -51.66643 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9165d7e8-f01e-3c85-b0cb-c6174aa5ce85 | -13.40801 | -48.16163 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 815fbb41-3e5f-3bb7-87ae-6b666eb4a9d9 | -13.01044 | -49.45787 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| df3dd31a-e476-305f-b901-b37a2edf27ec | -9.73327 | -62.35202 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 206f4373-ebb5-367e-b3d2-943fd8677003 | -12.65013 | -51.66578 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e27cd21-2f0b-3611-8b63-9207b64bcb56 | -9.773 | -62.50481 | 2025-09-28 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42f8b732-c066-39b7-bc45-26b7cc28f7d8 | -9.10596 | -45.87509 | 2025-09-28 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d21ef894-39de-3c3f-98ea-b03828cd520e | -8.85856 | -46.60011 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b36ffa35-d80f-3379-bd5f-590868d5c4a1 | -9.96416 | -64.75642 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef44b518-c1c6-3f43-914a-0a59e6e8f871 | -9.17711 | -61.80001 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7090f3fc-b117-3f9b-8503-db2d9783090f | -11.98502 | -47.07882 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c4a5b62-6362-3cf2-911b-278ba396a397 | -10.16492 | -64.73839 | 2025-09-28 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3db52e4-2f7a-3c25-8b07-19c9c90f799d | -10.1902 | -62.22548 | 2025-09-28 05:18:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4884d459-949c-3c52-9010-e6041547b8e0 | -13.60604 | -48.09239 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5edff87e-6c0f-3ea9-8fbf-0aec46f717f5 | -12.42018 | -57.80097 | 2025-09-28 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d13e48-dae1-3a23-ad69-5be00eb9bb60 | -12.2443 | -60.67894 | 2025-09-28 05:18:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 853aaede-c458-3686-a07a-f9396e915501 | -12.9821 | -49.43971 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1eadbfd-e41a-3ea8-877a-1259db521ee2 | -9.82614 | -58.06457 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 502ff358-e086-3f8a-94a9-36cd71c9436c | -13.29624 | -50.69308 | 2025-09-28 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6550e4d5-215b-31b9-8759-44c7dbbe8440 | -11.52072 | -54.30963 | 2025-09-28 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4984a9e3-5e51-3472-a6ee-acfe787b6d5f | -13.60607 | -47.32859 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e37425d2-432d-3aa8-9bde-2cd5ef61a653 | -9.5685 | -63.20637 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa3f7f24-04d6-3ba5-b879-c76791849ea9 | -14.53435 | -48.41655 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f768f76a-412a-30fa-b9b2-276e7d2665c8 | -20.70041 | -50.70537 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 435c657e-b06f-306e-9ee4-dd0acb6549f4 | -18.18346 | -53.3308 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b01a4fb0-6b39-3eb5-bb6a-274bf3c6f09c | -20.9936 | -50.01144 | 2025-09-28 05:21:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4626f030-3a29-36b0-a3c2-69cf3ab09163 | -18.18902 | -53.32629 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eadf8233-c46b-34cb-8f24-13f2fa9ead68 | -15.60151 | -53.16195 | 2025-09-28 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc42346d-f3aa-3455-9805-59a0c3565f79 | -18.17904 | -53.32521 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b69b95a7-0c16-33ee-8e0f-f0a3288abfb4 | -15.92337 | -59.48353 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9923dc0-1f24-3382-b3e0-8ea52c4888cb | -15.93465 | -59.50755 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 524f352b-6a9a-31f6-9f30-d661dc80655e | -14.78525 | -60.17592 | 2025-09-28 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40b40b9a-848b-3c49-98bc-7ec978c77cc2 | -12.86887 | -62.09802 | 2025-09-28 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d05c86f0-0444-31c1-9381-c257aeb75052 | -16.97026 | -53.69172 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 579f157d-ab4e-3fba-a484-a57f86ec5cde | -18.1796 | -53.32023 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f6ab160-6d34-3f23-883e-295b5a4e8b62 | -15.84288 | -59.60498 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 822937b5-1c1b-3c41-81da-5861b2de4647 | -14.3863 | -54.94123 | 2025-09-28 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8506ec3b-628b-3be0-a6af-24c22058fed8 | -15.54397 | -47.91341 | 2025-09-28 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0bbcbf96-d010-3091-b918-97e9ee9b2e47 | -15.95629 | -50.42155 | 2025-09-28 05:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abced89a-a46b-3922-830d-97398781d9e4 | -14.32506 | -52.92316 | 2025-09-28 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cdb139b-21f4-3f22-bd0c-37e2fa68970c | -14.32021 | -52.92242 | 2025-09-28 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63c8a843-169b-3481-b290-19ba0230433a | -16.96192 | -53.68001 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a2561632-3ca3-3b88-bb31-382052990838 | -20.99994 | -50.01212 | 2025-09-28 05:21:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a4a7231f-bca9-36ee-a6cb-3128b4a4605a | -15.93804 | -59.50807 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c646954-2cbd-35ef-8774-f2191be3ea9d | -18.20407 | -53.32714 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ff79c2ce-d06f-385e-bf1c-120558a2da5d | -20.69999 | -50.71009 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 201da8e4-13a2-33bb-af06-d5290510ecdb | -15.27762 | -56.80239 | 2025-09-28 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a189b054-67b9-3a7d-8c9d-6159909578db | -15.44133 | -59.72916 | 2025-09-28 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4914181-68fd-34b2-8dc0-e3193882e99d | -15.94851 | -57.4855 | 2025-09-28 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff2ee5fd-65ab-3ab9-a004-68e381b81958 | -16.9588 | -53.70665 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0023335c-77f4-3184-afdf-18c796394308 | -14.58476 | -48.24625 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18630ea0-4815-3b64-93a0-bf8b65940f41 | -15.92383 | -59.48671 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed162248-5504-3840-b874-89e6ae716a60 | -14.32101 | -52.92654 | 2025-09-28 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a30a53a6-2ea1-33a0-81d4-21e1efe25f6a | -15.28848 | -49.48804 | 2025-09-28 05:21:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 033c84cc-425c-376c-b8c5-3ce3eef8d580 | -14.57747 | -48.25246 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a6d6df6-cd67-3e34-9b7c-d869bb737a19 | -15.94427 | -59.51284 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a857314b-306e-34aa-8c48-789ab0205c5a | -14.58349 | -48.25867 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b941e96-3afb-3dca-b3c3-9ef5d79c425c | -15.29526 | -49.48275 | 2025-09-28 05:21:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30982774-8174-3c2f-b891-02cfed034ab6 | -15.96748 | -50.87457 | 2025-09-28 05:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 655199de-0c1d-3d0a-b459-e6b8f093083d | -20.69433 | -50.70494 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| d23b30d4-9bc5-3db9-80be-486c9645622b | -15.92281 | -59.48727 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b46e077b-a5ca-3375-854d-5419de7f8d27 | -17.20216 | -56.35426 | 2025-09-28 05:21:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2c7efc1b-983f-36b9-8007-259818f81330 | -15.33574 | -47.89363 | 2025-09-28 05:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33dc1e20-9cdb-30a2-b881-dce816ea4b98 | -14.47908 | -48.57574 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10f7fbcb-c5a2-385d-aa79-0b2f8400e24b | -15.2738 | -56.8019 | 2025-09-28 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d3925be4-39c7-3251-8f6b-57662985dfa1 | -16.59063 | -50.6622 | 2025-09-28 05:21:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f52fcb7-d2b7-3763-9a27-f033e076b643 | -16.01365 | -59.48983 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aad8cef-04cd-3365-b45e-fae52b51128b | -15.92611 | -59.49482 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b5d64e0-0cc2-340e-b656-026731829209 | -18.20467 | -53.32188 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2aa40e44-8244-33b0-9829-c4fd45cc24db | -12.40654 | -63.89542 | 2025-09-28 05:21:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bfcb7dd-e781-313e-9a53-738745be1356 | -15.61059 | -53.16875 | 2025-09-28 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee08ade5-5345-3f6e-ab96-cd17ae38b2f0 | -15.92997 | -59.46857 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README89.md)
