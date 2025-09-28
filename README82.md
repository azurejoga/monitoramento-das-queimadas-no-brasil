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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72b377e9-58bc-38d8-b461-74f3a82b023a | -20.69593 | -50.71724 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 4a148a3a-e75e-38cd-b1de-3c303bc8e3a5 | -22.73375 | -46.13208 | 2025-09-28 04:29:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 171bf704-8548-3e8b-b4e3-2e6ed05a6cc8 | -20.72631 | -49.38868 | 2025-09-28 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 792fb858-bc6e-3f56-8cc0-556bfaf286e2 | -22.60884 | -49.03811 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68c73dbe-3edf-3ab1-b6b6-7acba67dc5d3 | -23.55466 | -52.22783 | 2025-09-28 04:29:00 | NOAA-20 | DOUTOR CAMARGO | PARANÁ | Brasil | 4107306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61447c95-67c6-3b3d-a66b-535e7c51104c | -22.05876 | -43.01902 | 2025-09-28 04:29:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 18a9ffb8-173f-386c-8eb3-859a6811f356 | -20.99922 | -50.00474 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 763c80a4-1346-3a1d-9a46-b71de2489250 | -21.01235 | -50.02568 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb9d3125-471e-359e-a32b-fdd158fcf8f8 | -21.06857 | -48.6669 | 2025-09-28 04:29:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38dcf614-18f9-3b32-966d-778f776e1c3c | -20.99804 | -50.01214 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7df81c99-0411-30a8-a2c6-6d6390a34127 | -22.34462 | -47.33376 | 2025-09-28 04:29:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 626c8715-764f-37f4-a468-9d27b2b2b021 | -21.58728 | -48.84641 | 2025-09-28 04:29:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 559307d6-cb59-3c8f-833a-5badec4ee00e | -21.00076 | -50.01645 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71667d32-98ed-37d2-9ef0-8f47152b0338 | -21.44318 | -44.90308 | 2025-09-28 04:29:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9f3d9f81-1d7f-3b4a-810c-834fb1706a26 | -20.99472 | -50.01154 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1e0db334-2603-3cb3-98f4-3b0e458b0241 | -22.35719 | -49.96367 | 2025-09-28 04:29:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 842b6298-d2b5-345c-b88a-655d1012114b | -20.30829 | -54.64793 | 2025-09-28 04:29:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b7bdaf0-fecb-3d40-9337-8a5214eaf6f4 | -20.69321 | -50.71285 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 6182b8df-cfb1-33bd-9467-4487f74faf88 | -21.02102 | -46.90496 | 2025-09-28 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae9ffeda-b822-304e-aefa-dd3b9cbf7682 | -22.26377 | -49.5646 | 2025-09-28 04:29:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fbcb8ceb-bd25-3c21-9801-9d5ef3513319 | -20.69446 | -50.7053 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 4ba6525e-20a1-3e97-a1d0-cbfba30ca9e6 | -21.58337 | -48.8496 | 2025-09-28 04:29:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 12769264-0126-37f0-8d1d-430a4a8b40e6 | -23.44218 | -46.7008 | 2025-09-28 04:29:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e1fa663c-7192-35cd-b4d8-ff5da49e7774 | -21.58394 | -48.84584 | 2025-09-28 04:29:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 201758f5-cf0e-34d2-8a9b-44c910090322 | -22.94096 | -49.87945 | 2025-09-28 04:29:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| aa844c4d-6c5a-3fea-ac09-f80bba9172b4 | -21.00453 | -50.03188 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2232749a-8546-308d-9612-c0d6614a5011 | -21.85045 | -53.95421 | 2025-09-28 04:29:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1b3b05e5-a1b9-30fc-816e-5b9e2b70fb9c | -20.77813 | -50.48888 | 2025-09-28 04:29:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45dd0225-e6d8-3d07-ac07-b6c0c868a21d | -22.94154 | -49.87571 | 2025-09-28 04:29:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| c21d1f4c-5430-3782-8253-03a21263f9dd | -21.16504 | -45.73746 | 2025-09-28 04:29:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0211f2a4-45e2-34cb-96f6-ef52b010e3a3 | -21.85067 | -53.95552 | 2025-09-28 04:29:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 86b57c02-c156-3cd1-a56d-20758afa4aae | -23.44259 | -46.69774 | 2025-09-28 04:29:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8a3e8f6-6117-395e-af9c-19d0cb6e379f | -24.43399 | -53.95721 | 2025-09-28 04:29:00 | NOAA-20 | NOVA SANTA ROSA | PARANÁ | Brasil | 4117222 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 69f370e0-0ee2-3384-8fea-d79299b0a175 | -21.09856 | -46.35667 | 2025-09-28 04:29:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 64974cc2-3ca4-3d27-85b9-9b06a400c496 | -21.85101 | -50.5592 | 2025-09-28 04:29:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f0ebe413-a3a7-352a-981f-995b39db56b8 | -22.61723 | -49.02794 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 500e54b0-7996-3ba8-8b1a-2598f6876d27 | -23.43892 | -46.69741 | 2025-09-28 04:29:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 18e9e450-ffaf-3ebc-86cc-ce885fde38a4 | -23.1502 | -47.06405 | 2025-09-28 04:29:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 33971f60-9efb-3531-a3ed-d8ba484961ef | -21.01295 | -50.02198 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 80e618f6-22f4-3f0d-a1a5-466a0f108c63 | -24.43317 | -53.96176 | 2025-09-28 04:29:00 | NOAA-20 | NOVA SANTA ROSA | PARANÁ | Brasil | 4117222 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f6e273a-ea90-3955-b798-85bc90b8f085 | -20.6978 | -50.70592 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| dfb75297-cf3b-3723-a4d2-606e4f255491 | -23.06298 | -49.01745 | 2025-09-28 04:29:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0086b9d3-bab6-3690-985c-15cf7d5323ad | -22.62057 | -49.02853 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa76ad1f-0a42-3db8-b451-567af0455bc7 | -20.99531 | -50.00784 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 05b2294d-4fb7-3c4b-ac51-1542174ac6a6 | -21.00135 | -50.01274 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e35ecc92-8b89-3447-b0e5-abd99c5575df | -22.94427 | -49.88005 | 2025-09-28 04:29:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a4c0d313-2a47-3510-b062-48bfc2acce42 | -22.82108 | -47.33092 | 2025-09-28 04:29:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e17cb66-0416-361e-b8ab-1ad1e330619f | -20.72688 | -49.38499 | 2025-09-28 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d5a55c3-a8fe-3cce-bea4-cfe848c62b9c | -23.28039 | -46.60299 | 2025-09-28 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6a30f253-9f72-3d69-8c9b-28b394adf565 | -9.6511 | -62.8526 | 2025-09-28 04:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 35b24d33-c88b-38a8-b0a2-8630f3603b92 | -9.6512 | -62.8336 | 2025-09-28 04:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e6ec5886-1e3b-3c7c-bc16-a7613fc0ef6a | -32.04376 | -52.09292 | 2025-09-28 04:32:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 8b6bfaa3-c703-3e55-9369-aab687dcb850 | -9.6512 | -62.8336 | 2025-09-28 04:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ce72d84c-a25c-32b1-bd35-3562e7e1b8d4 | -9.6511 | -62.8526 | 2025-09-28 04:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2bdd85c5-5865-33ca-b808-cafb429db013 | -15.0575 | -42.32624 | 2025-09-28 04:59:00 | AQUA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 9796ccd4-7383-3d10-bc52-98f284a12fbc | -19.49486 | -41.103 | 2025-09-28 05:01:00 | AQUA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 172.3 |
| 5d23dc4c-71a8-3544-aa82-4b0b1e5de90b | -19.49376 | -41.09562 | 2025-09-28 05:01:00 | AQUA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 328.3 |
| 4d15e8e1-ae32-3ab1-b340-aefefe7d4377 | -19.49846 | -41.08415 | 2025-09-28 05:01:00 | AQUA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 3a5fa0e4-0c05-3969-9765-1d03c6409790 | 0.27081 | -51.38003 | 2025-09-28 05:14:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5260181d-3efe-3463-a70c-11c5903b4b83 | 2.08372 | -50.91132 | 2025-09-28 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0fad026-1982-304e-a4be-0f381386d5c7 | 0.27407 | -51.40079 | 2025-09-28 05:14:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3165a6c-4b78-3059-a4f9-8b260a4c7db8 | 0.69086 | -51.46205 | 2025-09-28 05:14:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aa190b7-7911-3471-85c0-0e97cf811afd | 0.2784 | -51.40013 | 2025-09-28 05:14:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00392a27-f962-39da-a539-ce82359e1d17 | -7.74363 | -47.00981 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92af6c02-56a8-3790-895a-ef2a2c757b97 | 0.76037 | -59.88079 | 2025-09-28 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0f2682d-c706-3791-8ac4-0b0e3e3c4059 | -7.76836 | -47.02426 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86cb2499-ad3d-32e9-80a6-b75a4b1e4d11 | -7.75016 | -47.01072 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ed7693e-787e-36ce-86e7-7358b39266d6 | -7.78329 | -47.00847 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67686b8e-4a0a-3acd-b9ce-52885d4fd607 | -4.81261 | -48.24226 | 2025-09-28 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57638356-8400-3f39-8071-ea79e1767699 | -7.79049 | -47.00406 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b525542-ff44-3e3d-9545-3b71c9311e59 | -7.80379 | -47.00745 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c5e516e-7945-37d3-92af-525b0df6d254 | -7.54168 | -46.10143 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8761204e-f192-3f4c-82d0-163bc4649454 | -7.81104 | -47.00296 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02a2152d-32ed-3897-95c5-0d9e63c9ce46 | -7.756 | -47.01698 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52420ffa-c81f-378f-a1e9-951e5c6dee0c | -7.79657 | -47.0118 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c50612ee-fc0c-3993-aca0-2ef2a71e476c | -7.74293 | -47.01527 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7658b89-f55e-3896-bb01-ca1ab9492d9b | -8.17182 | -46.40283 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cc0f4128-0e3b-3f70-8c34-a4b9f782e37a | -2.19529 | -54.46539 | 2025-09-28 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f824a78d-13c9-3224-b091-17e5f978b614 | -8.17063 | -46.42595 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f20b96a9-55d3-38fd-a79e-01b58409295c | -7.3772 | -47.02951 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67172e5b-35cb-3414-b84a-ccd1b77b2377 | -2.62216 | -54.73516 | 2025-09-28 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e5dd26e-e0c6-3cf4-9a07-a6a888d5502d | -3.80677 | -47.58868 | 2025-09-28 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f7211a-0b7b-39ba-b6aa-67b244116e15 | -2.75185 | -54.5937 | 2025-09-28 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 799771d5-ec27-345d-a81c-67c945321b3a | -2.58091 | -48.40882 | 2025-09-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 09ece23b-0f58-3d83-8913-94d12d6337ed | -7.80664 | -47.03468 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4d569bd0-601f-3d63-b522-57c700044bcc | -7.53562 | -46.09401 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0eff45b9-e779-36e3-9e31-4c498924f9ab | -8.17276 | -46.40816 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9a0774eb-4009-3cda-a309-43fcbe1f9d32 | -3.03182 | -50.4443 | 2025-09-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee308aed-b94c-309c-a8cf-9dbcc900a015 | -7.80084 | -47.02788 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1c81b2ce-7f1b-3c66-b94b-f94095c2e67a | -4.2927 | -48.26581 | 2025-09-28 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26c70e69-dd06-38a9-9eb7-e56c6c9de99b | -7.80014 | -47.03354 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8451bd48-7bef-3763-b826-6f44d0723c60 | -7.80353 | -47.00619 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 186dba70-6fd0-3c82-982c-f9d111f088f0 | -3.2107 | -51.27845 | 2025-09-28 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7df57b7e-c1fe-3f7b-bdb1-e40b66769c83 | -4.26291 | -48.55339 | 2025-09-28 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 380d86aa-d300-36de-af18-142b95e414e7 | -3.7887 | -48.86597 | 2025-09-28 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ffbb9aa-55bb-33d4-8536-e3585948b414 | -7.79799 | -47.00094 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5db4451-65f0-31ad-9714-b707db9f8ad7 | -2.58202 | -48.40148 | 2025-09-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2b66ce85-43ff-39f1-9519-34c6ef024fb4 | -7.79727 | -47.00641 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a35045e-ec25-3c7d-89c2-29ebfb16da20 | -7.80939 | -47.01255 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 30e0861d-846c-3020-8c7e-54935e5b9ccb | -8.17106 | -46.40885 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README83.md)
