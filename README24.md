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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e1008e6-bf21-343f-8319-50f6664e4eed | -7.08718 | -59.19049 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4250cf04-d5d9-32cd-8ae8-d952a237e79b | -11.78489 | -49.56881 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1dda4eb-5ce2-3784-b989-ae4945c3908e | -11.71905 | -50.10634 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e06f0de-991d-318a-854a-12d2246afd79 | -11.7854 | -49.56463 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2287e6ee-c75a-37f4-8a3a-7d0edc783970 | -7.06687 | -59.21211 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b020fa72-4db9-34a9-b6d6-3e7fb87270af | -10.37432 | -50.80983 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b2fb7dcf-f494-3858-bc12-951229b7cde5 | -9.82964 | -63.01458 | 2025-08-11 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ccd91bc-590b-30e8-b200-ce8781c8797a | -7.40609 | -59.9984 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d0c95fe-0b02-30bd-a7e1-1e04ebaa5892 | -7.25688 | -59.99577 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b06e64d1-b2ae-38a8-9e5c-6230de8d7988 | -9.38393 | -61.52557 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcc409a7-ce6a-32f6-a55c-df95ff97988c | -7.08057 | -59.18946 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61b563ce-0821-36c8-ba34-80f8c13ca951 | -8.93738 | -60.7458 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7efaa7e-f1ea-392a-8467-ecd51a6c2915 | -9.37475 | -61.53922 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368f3d62-437b-385b-b0f7-9d271958ab33 | -7.06512 | -59.17995 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a38ce14-cb27-33dd-abbf-f2d43af6b70f | -7.06849 | -59.20174 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa5339f2-2798-351a-99b3-8a3dd0f63711 | -7.07179 | -59.20226 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e2d79559-a7cd-3b0e-9559-9663b5203403 | -10.04587 | -64.89843 | 2025-08-11 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8718ba9e-2c5e-34a8-bb98-8fe2105c934c | -9.37714 | -61.52447 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1fec45d9-34ed-3505-88d9-a0a49038780b | -7.06734 | -59.18739 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd179dbe-923d-36be-8d6a-8164492adf15 | -11.12055 | -54.65264 | 2025-08-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fed72b3-63c5-3580-b0f9-ee1b7a8584dc | -8.92865 | -60.74072 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f3e9561-7e10-39ed-a385-ae16e4b1673b | -8.93574 | -60.73462 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b878246d-f288-3b49-aa0a-b1fdbedd9423 | -7.08772 | -59.18703 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04624c85-f83f-346c-85e4-9803290b9437 | -10.36642 | -50.82965 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85a9b325-b3e7-3524-b000-4fd0f8e0605c | -8.90503 | -60.54474 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 249a1276-4100-3dc6-b4eb-f77cc0ee7b28 | -7.06133 | -59.20417 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3e2be8e-a0bd-3d5a-a162-e126f9de3e41 | -8.93794 | -60.74224 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4734af6-ea75-3cf1-9932-9a0d0f2bfde6 | -10.3722 | -50.8269 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66ecd534-df75-340e-9c86-7ce9a645494e | -9.37255 | -61.5313 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50a3950d-0bea-345f-960b-77f3f756818f | -8.93461 | -60.74171 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cdaf8c8-d91f-3bae-86a5-107da383057e | -7.0805 | -59.16819 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62a70095-260f-32e9-a638-d50aac0c1d36 | -10.37305 | -50.82007 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ca79254-8ec1-3ee8-8a0e-921e4cc8bb59 | -8.92978 | -60.73362 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02da00dd-b275-3803-a900-3e8f6480f1a2 | -12.54654 | -47.06704 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c54c8e59-b216-34bc-b027-2c56844e9739 | -7.0552 | -59.17841 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb56fd40-cdaa-3793-9e01-d600206602ff | -7.05412 | -59.18533 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3f5f5a5-db43-30f0-aad5-2a4f323ab61e | -7.06451 | -59.16215 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edbac126-3191-3de7-b0ac-acbd95cdcbd9 | -9.74041 | -63.19407 | 2025-08-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93723adc-2a10-3697-81fe-5534b386658c | -7.0799 | -59.1964 | 2025-08-11 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| de7d095b-1b5e-3add-abfa-230e88a761da | -9.3806 | -61.5315 | 2025-08-11 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d2c8a7e7-8cab-3e2e-981d-dde306c829a2 | -6.5856 | -44.564 | 2025-08-11 05:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 269703ac-ff9d-3578-b2cb-3e16f35bf174 | -7.0614 | -59.1972 | 2025-08-11 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 227d67d7-2dc8-3c79-b2a9-316f4ee1b7a2 | -15.4407 | -53.9258 | 2025-08-11 05:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b50c2fc6-4406-3276-8cde-839b98c86c4d | -15.44122 | -53.93574 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efdf3168-3a53-376e-bd5f-fc014ea51806 | -16.04826 | -48.48589 | 2025-08-11 05:21:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25ba4787-984a-3ff0-9782-34cef78314d2 | -15.4285 | -53.92377 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4432b46-854e-390f-8824-9a86a6cbc0e5 | -15.41981 | -53.91744 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 827f2705-4916-311e-a1e7-da49bd2dcc45 | -15.43856 | -53.92813 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c99cd76-6ea1-3785-aa9a-30668b582308 | -16.30699 | -52.92647 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c59304ff-f85a-33bf-abb7-36417bceb8bf | -15.42386 | -53.9231 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d1fbf04-1cc4-32ee-b622-7c66e43343e7 | -14.3045 | -51.99653 | 2025-08-11 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d00ee45-78a5-30c3-a75c-562f41422214 | -16.29757 | -52.9195 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 64d86684-95f2-329a-a20e-eacb102ff615 | -19.28078 | -49.77018 | 2025-08-11 05:21:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 79405eaa-aa9b-328e-8b67-620b1e6aac34 | -16.3073 | -52.92376 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 208193d7-5f7f-301f-ba60-d4578b2cfe76 | -15.43718 | -53.93007 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| fd912ffd-537b-3bfb-be9b-b44706cd8bd1 | -15.43793 | -53.93311 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de7054ce-e994-3da1-a447-332a729920b5 | -15.44242 | -53.92576 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b1db7d14-5f00-3e7d-8a46-a6242878ac88 | -15.54513 | -49.99043 | 2025-08-11 05:21:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9135dcdc-1c70-351c-b8b2-2d4dab0fd27d | -14.60059 | -49.61034 | 2025-08-11 05:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2136591f-19f9-343b-8ea0-da71fe462a76 | -15.45109 | -53.93209 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 28cb5383-9cc4-3e56-958e-11dd5fde5906 | -15.42445 | -53.91811 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b80047e-d15e-3f9b-bc0a-264f64b3f58d | -15.43919 | -53.92316 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd6ef31c-59bf-3eb5-a41b-fe7ce7bf90d2 | -15.4499 | -53.94203 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61f0880b-683f-3320-a5a0-ba5c686f896f | -16.30228 | -52.92297 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd49e8df-c2b9-3368-9df8-f2f943122b38 | -15.43455 | -53.92251 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17d545ec-3f55-3e5f-b077-095915930ed9 | -15.41922 | -53.92243 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9c3655b-06c3-32be-b017-894e5d9cba19 | -15.43659 | -53.93506 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35eb79d7-1930-370f-b413-220b3049b1f8 | -13.06226 | -56.84722 | 2025-08-11 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe18ff80-a5cc-32a1-8a4b-78fab1805619 | -14.83501 | -51.22928 | 2025-08-11 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 398615fc-ec3e-3f52-aef4-137350cc32ae | -15.43778 | -53.92509 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 7383f443-c019-37b6-8ae7-d2458e348139 | -15.41261 | -53.90924 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 655218ed-ac01-3d57-8de4-738c3b37f305 | -19.28123 | -49.76482 | 2025-08-11 05:21:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 210593da-edab-3dd2-be90-6d7cfbe90e4b | -13.066 | -56.84775 | 2025-08-11 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 188281f1-aaa8-330d-9a27-cbe8987f6049 | -15.45513 | -53.93772 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4914e763-396f-3be3-bd36-9b41357895bf | -15.43329 | -53.93245 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4202b75e-e315-37ca-9295-793f5f90a9c2 | -15.42591 | -53.91621 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da8b22fc-5acc-3bee-8641-b6fe56ac93d7 | -19.27874 | -49.76515 | 2025-08-11 05:21:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e330c8be-3bc8-320a-b7d4-50d065a56493 | -15.42791 | -53.92875 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a64129e5-9d3d-3187-af07-d32eb7b74857 | -16.2909 | -52.93637 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44dfe2c8-b6b3-3cd2-b333-ea948a43f134 | -16.30259 | -52.92024 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 195f6194-3bfb-3120-bbfa-30660a02bfc7 | -15.54467 | -49.99504 | 2025-08-11 05:21:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d25ac504-8649-3cb0-9648-64ba9e22dffa | -14.71791 | -59.62221 | 2025-08-11 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe16b6b-76ae-33e1-863e-773dadef2b30 | -19.28506 | -49.7663 | 2025-08-11 05:21:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f8fa598-4cd2-3389-8b1b-99d8d12231e5 | -15.43255 | -53.92941 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d35137d-47f2-39f7-9305-91ba7171817d | -15.43314 | -53.92443 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f39ce3a8-0925-32d5-b1e9-8bb7e1609c01 | -15.42064 | -53.92054 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56231640-c418-32ba-a5c4-071de01edde8 | -16.29061 | -52.93625 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 512582a8-ea06-36ca-8c97-93ff330af720 | -15.42528 | -53.9212 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2793d972-5e6a-3d03-840f-60475cd2eadf | -16.30268 | -52.9231 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 417c843a-eddd-3f62-8279-8fe81a23bead | -15.54294 | -49.99178 | 2025-08-11 05:21:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 38918c72-56aa-3218-a3d9-6c5b4089223c | -15.44646 | -53.93142 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fa8a1f8d-398b-3c64-a548-0da3e1d314ab | -14.8295 | -51.22855 | 2025-08-11 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1a54f4d-f8fa-3e4f-9971-3d83999a089e | -16.29799 | -52.91964 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d0bc372-3c17-303c-a3f9-008f92382c8b | -14.30305 | -51.9635 | 2025-08-11 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 68fb731a-edee-31e9-9515-aa5064eab75e | -16.30289 | -52.91756 | 2025-08-11 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 916f5f37-29db-3e72-a6a8-a469e6ec0253 | -19.28459 | -49.7714 | 2025-08-11 05:21:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e1b014e-ed01-3ac1-a41c-8d324e49d518 | -14.31006 | -51.99417 | 2025-08-11 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3f8d1e5-ecaa-3c0c-9432-9a890ad14a5c | -14.60007 | -49.61518 | 2025-08-11 05:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9df12e26-70aa-3e88-b46c-6a2e86959a71 | -15.42127 | -53.91556 | 2025-08-11 05:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94f171e0-d70b-3ed2-ac28-f16b69568b39 | -14.30487 | -51.99333 | 2025-08-11 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
