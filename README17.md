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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd1e10c0-9729-317f-8975-07ca399e3bf2 | -11.99767 | -57.20969 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d5d9365-93ba-3319-9590-da98adf62ff8 | -10.86841 | -54.32354 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cf605d6-48f9-3524-9d67-255ff38cd377 | -10.99445 | -50.75675 | 2025-06-12 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a938f18e-089d-39df-923a-48cbc6e0b9bb | -13.28918 | -57.07456 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 47bdb1bd-c622-3f9d-ad60-125dc176766c | -10.86898 | -54.32001 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35685385-9c49-3860-906e-e7fc8604b22d | -9.25322 | -57.53357 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5f566e62-df00-3f6b-b429-99ab226ad355 | -11.76898 | -54.36618 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2530b8ca-f7f0-3d96-81eb-365aef19d086 | -11.13941 | -53.92443 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cd6f86f-8804-347b-87da-793b10972c6c | -11.83972 | -43.79995 | 2025-06-12 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29d3c417-63c4-322a-9d84-2c2b921189f8 | -10.35509 | -51.99025 | 2025-06-12 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8e2515f-fad4-3a34-8f1d-cbff5b26ae2b | -10.7024 | -49.51242 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f88ab070-47e0-3198-adf0-edbd21fb8f3d | -10.8815 | -54.75299 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f432fe93-cd86-31d9-b73e-6d0a47824170 | -11.5769 | -47.44112 | 2025-06-12 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62ad8b11-1148-397f-9967-f1ff7899b883 | -10.62851 | -49.4366 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f17745f-16de-3505-9073-6f7ad794c299 | -13.29418 | -57.08823 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a64a7ec3-a607-3683-9d68-0932b65acbab | -11.78797 | -54.77685 | 2025-06-12 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce9bb9af-f48c-3b58-ae43-37c1af8687ae | -11.85591 | -62.7654 | 2025-06-12 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b63f04f9-da96-30d3-9f59-c0759bc519da | -13.89642 | -48.73472 | 2025-06-12 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 210669d7-4026-3eeb-857d-8e42f531ce5a | -9.87634 | -61.40078 | 2025-06-12 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0adc4c02-e51d-37c8-b537-413e50636dfe | -14.02965 | -55.12296 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9ca6041-bbb8-34e6-9217-6692a32c08b7 | -10.88266 | -54.7458 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bdba32fe-1a53-3700-a8b3-e9a1619e0b25 | -12.43201 | -54.87225 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5428bf0e-39ca-32c4-b1d9-f63a9b19f8d7 | -13.8907 | -54.65402 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81dabbeb-1530-3f3d-a3fd-39f150c4e67f | -11.7706 | -54.3773 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7536544-37b5-3bac-9a57-e72db6568621 | -11.99476 | -57.20477 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fe037bbd-8a4c-34dc-83da-f5c4d55b6507 | -9.46037 | -55.94039 | 2025-06-12 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 403bf64b-c110-34af-a82f-73574675ddda | -16.26645 | -48.80315 | 2025-06-12 04:51:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bc36f15-23f3-34ad-abf3-c00776208ae3 | -11.77004 | -54.38083 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e3a6bf1-3fa6-34b5-b972-a3a2fbde7f75 | -12.38348 | -45.77341 | 2025-06-12 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88fda65b-272f-3054-9d63-f48d816d8d29 | -13.9048 | -48.73538 | 2025-06-12 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 618d084d-097c-33c1-925a-21ddd72bae89 | -12.5229 | -57.2328 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db5e9826-e6ea-3722-9876-828c46beaeca | -13.88908 | -54.64283 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 218d6b5d-a83b-3346-b18a-f89b50561abe | -12.1741 | -54.23365 | 2025-06-12 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fcfd98a-c14d-34a2-96b4-7626b95cff68 | -10.69794 | -49.51651 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9537d920-1980-3cdf-aef9-c4587c73b196 | -13.28702 | -57.06572 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1be16c62-8f2b-3944-aea0-3cf756afd6df | -12.70929 | -58.03222 | 2025-06-12 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b257a5fd-c672-3543-af3e-9a4a7fed4219 | -12.1068 | -48.8762 | 2025-06-12 04:51:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2aad8c2-efc6-3af8-a347-00e9832312ef | -10.5163 | -53.63329 | 2025-06-12 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fefe04b9-18d2-3223-8ec1-e29cff5e78fa | -11.86704 | -52.25076 | 2025-06-12 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 525428c7-7ff6-3895-8236-cd204cbf1c4d | -14.0363 | -55.12408 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6736476b-fec4-3bc7-b139-736c55ec0b40 | -10.87173 | -54.32409 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dac6f2c-1525-3db0-80ac-07c0d0d26581 | -10.88208 | -54.7494 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c4023e1-6b5d-3225-98a6-efa60d5c0ab9 | -10.29907 | -57.13639 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1321ca4a-f566-3d32-b919-ee8f1f893f42 | -10.70483 | -49.5223 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bce3956-a6bb-3f4c-ae7b-16cb1b342f38 | -14.03297 | -55.12352 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 673fa850-aced-37f1-96f7-7e077363402f | -14.04122 | -55.13595 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8690d328-4638-3ddf-a35b-4fc6f021ec34 | -12.70632 | -58.02696 | 2025-06-12 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b78ba73a-1fec-3eee-950f-2a1498a932fe | -11.90981 | -54.82257 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c01d57d9-af35-3c11-aa4e-bf15c398efb0 | -11.56752 | -51.3049 | 2025-06-12 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d2ba0db-fce5-344e-ad7e-8b76918e745d | -13.65033 | -53.93901 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ceef44f-b952-3d03-bfac-d68fd7948261 | -10.65424 | -49.36107 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a82f6fe1-ec8d-3f30-a593-47d37caaf11c | -11.7036 | -54.50064 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a1c896f-a810-341c-9797-e113bb1943c6 | -14.84246 | -52.28411 | 2025-06-12 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d498fcde-2f0d-3ec3-92ca-55c8c549d112 | -11.91315 | -54.82313 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f5784e2-77b9-3119-9120-8b815edfdbfe | -10.2956 | -57.14267 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e9bb474-a098-35ea-aae9-8dfb63780d9d | -13.89014 | -54.65757 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ef6ebb-df23-3d4c-884b-d8d5bac012c7 | -11.37465 | -56.5516 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db19acfe-dc71-32b3-a0e0-974470817ceb | -14.84302 | -48.31266 | 2025-06-12 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc2f017-17f4-3a71-8685-483abe8d2836 | -13.97135 | -54.4238 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03933df9-9af9-31d8-92ad-ede17405ee6b | -9.39279 | -57.52736 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c495c21b-210c-3c76-94d8-daff4a126b5d | -14.04455 | -55.13652 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2dc498e-87a1-30ea-a602-f6aaba2b3fa1 | -15.37719 | -47.87647 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58c9ce28-41fc-395b-997d-d2a7f2bfaad8 | -11.33894 | -45.2173 | 2025-06-12 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17537901-6fec-3a7c-a797-fa3efe00f388 | -9.83641 | -62.88449 | 2025-06-12 04:51:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9cdc359-cfbd-3dff-afe9-54aaa4ee39c5 | -11.38527 | -56.55343 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93faa955-9ab7-3cc7-aed8-6abdb09a6a7b | -10.80552 | -55.87131 | 2025-06-12 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 625e1de6-f85f-34f6-8e90-b4aee1f94f9c | -13.89514 | -54.64748 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ab49f7fc-8752-3787-8f74-f411d9df68c4 | -11.9191 | -57.47396 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ef17742-ef06-308d-9c02-ca5d0843861f | -11.91648 | -54.82368 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7322abb8-48bf-3231-8168-60100946c48d | -10.65762 | -49.41954 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e66a154d-cf63-3030-9554-c155fcaa29ab | -10.95039 | -55.32837 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87227c68-64d9-3a0f-a081-81a263bc9db2 | -11.60916 | -46.98785 | 2025-06-12 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 815c1cae-c60d-3883-a68e-008e0c1aa5dc | -9.17731 | -61.86388 | 2025-06-12 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0074e58-d0c3-35ab-8897-5d92131bb8b8 | -10.69552 | -49.5066 | 2025-06-12 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13143fd2-3d10-3317-a6f1-1f8bb4857d60 | -10.33857 | -57.49256 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bf14101-6f7d-36f6-b69d-11ed3ed8265d | -11.38458 | -56.55749 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63db4c02-829e-3aa3-a0d0-54de9806880c | -11.13777 | -53.91338 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04fbe591-52ac-3f37-ab89-ac6d04b7a1d5 | -11.13609 | -53.94547 | 2025-06-12 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 305fede8-b24e-37b5-ab3f-d26261479601 | -13.49564 | -53.49173 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7b33bea-1a63-3691-873b-d80c7b709ca1 | -13.88739 | -54.65347 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15d90773-368b-356b-895b-0d2c71c1649e | -10.23817 | -52.23532 | 2025-06-12 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b82805ec-0dfa-3c68-909a-b59e3cb7a4e8 | -10.94941 | -55.31304 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b4f667b-4805-31d4-899d-39bf93a32fc5 | -15.3701 | -47.87743 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a271dfff-92e6-3bbb-9f91-6bf6410319ce | -11.7065 | -54.50101 | 2025-06-12 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04264998-2f8e-3027-8b73-d6359fa10ca7 | -14.03182 | -55.13068 | 2025-06-12 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aacfd99-aa1d-3e36-950a-7cf8c4575820 | -9.3936 | -57.52258 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c82f3249-d98f-3f50-897d-ef89f576a9b8 | -10.94663 | -55.30878 | 2025-06-12 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cce3029-c5a2-3442-ba78-a92479556bd9 | -15.36785 | -47.89465 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7801901-e820-3b63-ba57-92188a24409f | -14.53742 | -53.64737 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 612842b8-633c-3fd9-a31d-bc700d540f57 | -13.29488 | -57.08411 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8dd08b3d-b628-39fb-9374-6a7e344098f0 | -10.36386 | -57.50406 | 2025-06-12 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2082136-3983-3835-99d1-0de8394a1f78 | -12.05116 | -48.0774 | 2025-06-12 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9a0e24b-3092-3459-aafc-1d085b1fcf0c | -13.66026 | -53.94063 | 2025-06-12 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bbad6012-4788-30db-b023-5a464741db14 | -11.37888 | -56.54814 | 2025-06-12 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70706f33-0305-32ff-9080-4295171a3d24 | -9.24938 | -57.53292 | 2025-06-12 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 61b46b60-c76e-3805-84e2-36f6f50b4a8b | -15.3806 | -47.88577 | 2025-06-12 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 217ab6e2-2632-37a3-85ef-2dc12118fc86 | -11.99404 | -57.20907 | 2025-06-12 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5761f3a3-6bce-32be-a9cb-3568c14c7fba | -10.65491 | -49.35633 | 2025-06-12 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8a89b0d-bac2-3ad7-977d-e495b748c9ca | -13.89845 | -54.64803 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a2dfbeb8-3f10-3132-b963-861585996e91 | -13.89345 | -54.65811 | 2025-06-12 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
