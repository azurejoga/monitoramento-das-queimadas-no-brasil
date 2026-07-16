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
| f18d3e55-d15d-3ccf-9415-afc934f2cee3 | -19.82784 | -57.95671 | 2026-07-16 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 9652ec68-7864-33dc-ae39-825eabed7595 | -17.84703 | -52.48795 | 2026-07-16 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| d3ffb72c-566a-3966-a055-d11ae8f3e467 | -17.83924 | -52.49599 | 2026-07-16 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 71eb9950-3f0c-3a95-b788-d71fd964c6cd | -21.66494 | -56.31958 | 2026-07-16 00:54:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a053ddd2-b425-34f8-9cf5-cfc7200b5d65 | -18.62006 | -54.9174 | 2026-07-16 00:54:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee5b58ef-a7c5-3233-a5a2-d670cf08339e | -10.29504 | -59.4623 | 2026-07-16 00:56:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ca6227c0-1d75-3888-beef-139d2b88f1dc | -12.87842 | -58.27687 | 2026-07-16 00:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f0739713-daf0-3728-9360-8f7592c0f10b | -12.88 | -58.2876 | 2026-07-16 00:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 091d4a9b-3e7a-3936-bb36-ec7d269c5570 | -12.8896 | -58.28605 | 2026-07-16 00:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc886b0a-bfd3-317a-a2e0-e2b63940645c | -10.24145 | -58.51864 | 2026-07-16 00:56:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a036ed58-5600-3ace-831f-eabbe743b8fe | -9.45589 | -63.88384 | 2026-07-16 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0a626e52-2d44-32b9-8cd4-f20075df3d9d | -9.45458 | -63.87371 | 2026-07-16 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7692fa27-77f9-3cc6-972d-6ae99481de13 | -1.64155 | -54.45372 | 2026-07-16 01:00:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e66ee9e3-92e0-3086-b4ba-9a6248f34632 | -1.64627 | -54.48498 | 2026-07-16 01:00:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f44d8be2-fd4a-3301-891c-15d76150296a | -9.4547 | -63.8675 | 2026-07-16 01:01:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43ecfae0-d9a8-32a0-b027-129aa654784a | -21.665199 | -56.306099 | 2026-07-16 01:01:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 033492d7-362b-390c-8c7e-7460c779b97c | -12.881 | -58.265701 | 2026-07-16 01:01:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7483390a-54d1-30ac-950a-ca946c30307c | -12.8847 | -58.2817 | 2026-07-16 01:01:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1080d9-7ac2-31ca-9f57-51c9cf44eae9 | -21.667101 | -56.314301 | 2026-07-16 01:01:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c66ddd06-4cfb-3d1d-afbc-6c7547d95fd9 | -19.8304 | -57.948399 | 2026-07-16 01:01:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0a27c30-e096-3324-a055-a6117fdcd3ee | -12.8828 | -58.273701 | 2026-07-16 01:01:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a96f1bc-8fac-36ee-a249-3ccd95052495 | -17.837099 | -52.486599 | 2026-07-16 01:01:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5c2e8f-e60e-3d5d-af33-7d14e34a9a33 | -17.8333 | -52.471901 | 2026-07-16 01:01:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c5b15fc-c70f-3574-a70c-0cc608bfca50 | -9.4564 | -63.875 | 2026-07-16 01:01:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5a51eea4-c0db-3e65-b294-35f03d97a267 | -22.418699 | -54.680099 | 2026-07-16 01:01:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8918af6f-d4a4-3dc1-b682-ad266abf4f12 | -22.421 | -54.689602 | 2026-07-16 01:01:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0aae2fd7-dee8-30cb-be21-0649665ec94f | -1.6336 | -54.470901 | 2026-07-16 01:01:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20649367-2eab-3354-8f3f-8317e11134a1 | -9.4581 | -63.874401 | 2026-07-16 01:27:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7aef896e-d788-370d-86dd-f9778fdcb026 | -21.675301 | -56.314499 | 2026-07-16 01:27:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cd58b6b7-a8c2-3278-913a-2ea2956f1fbc | -1.6513 | -54.4678 | 2026-07-16 01:27:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67b53876-a894-325f-af0c-c43f1e8e365d | -12.8882 | -58.280499 | 2026-07-16 01:27:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a51b635e-aaa0-3cbf-aa5a-c8635c5da05d | -22.420601 | -54.690899 | 2026-07-16 01:27:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f253f9d5-0163-3a38-b677-ffa10ddd0171 | -1.6416 | -54.4701 | 2026-07-16 01:27:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 004554c1-d001-3e0a-a4db-1dd8e1f9e713 | -22.422501 | -54.698898 | 2026-07-16 01:27:00 | METOP-C | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d18f555-00de-39ca-9224-22ba5cf66842 | -19.8333 | -57.956902 | 2026-07-16 01:27:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 39c444c4-37b3-3ce5-9b70-3d0fab6e1f54 | -8.75383 | -43.94432 | 2026-07-16 03:34:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4fadbad8-c7c1-39b5-9af0-7cae16fb1906 | -8.75988 | -43.94546 | 2026-07-16 03:34:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| cb537924-1a61-3fb0-a645-0dc7080a6184 | -5.13158 | -37.8391 | 2026-07-16 03:34:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52ddd385-7040-3915-823b-f2d8297a8912 | -5.13091 | -37.84317 | 2026-07-16 03:34:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0d0b6e7-2510-337f-a576-ddb1a0427d65 | -9.29889 | -40.37075 | 2026-07-16 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9b3ea55-4b8b-3606-94c5-c4e23f56a902 | -11.78983 | -47.09699 | 2026-07-16 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9c1b79e-0ff1-309c-9d82-6c6f474f7d73 | -14.19616 | -42.81064 | 2026-07-16 03:36:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9034725f-f2c4-3854-b505-7a386f932f37 | -13.26985 | -45.15865 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ab55c765-5c3b-32ec-ae26-3d8e054efa6e | -13.43813 | -43.8518 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf7911d4-b3d8-3398-adb0-9def6e05ccd1 | -13.43737 | -43.85561 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5c3fdad-3c58-3333-8850-7e47dd2a9e14 | -13.26379 | -45.15757 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| afa739e4-8ed8-3970-9bce-6299cb1d6647 | -10.88865 | -46.44721 | 2026-07-16 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7813d598-ae9e-30cd-9ebb-3a679ef63805 | -13.44448 | -43.84885 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b05da525-ccc4-3590-8cca-99bd0796c6de | -15.20652 | -44.05183 | 2026-07-16 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2274aac-64e9-3822-b5f1-5b925eefe71e | -13.27079 | -45.15408 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecf18435-e12c-3239-82b0-9b5203dea838 | -10.40113 | -44.98137 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddf93df8-d3c6-39f7-9a4f-350dbcbca002 | -15.1996 | -44.05794 | 2026-07-16 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78308113-0ea8-3aa0-afd5-2e8bbec23ded | -12.0845 | -43.55201 | 2026-07-16 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b3058a3-06a9-309e-9b7a-80fb3b0eb810 | -13.2657 | -45.1483 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5a5d85c5-af40-307f-a8f3-740d295e61ea | -10.88748 | -46.44457 | 2026-07-16 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ce630c01-ebfc-352f-944e-2daae181680a | -13.443 | -43.85633 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cbe721f-12f9-3721-8bda-2d17d0dcad8d | -13.26065 | -45.14231 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d161d17a-300a-3a50-b8e5-588c7352d9ca | -12.08524 | -43.54822 | 2026-07-16 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13e5c7a7-a86a-3322-83f9-6853fa281a28 | -14.19105 | -42.80957 | 2026-07-16 03:36:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 19fd1de7-bff0-341d-902a-628e9067a3f2 | -13.43335 | -43.84687 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c822aa1f-5d26-3aac-bc9f-1c484c91e0f5 | -14.14215 | -46.27891 | 2026-07-16 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 918f0e87-2b7e-3836-9aaa-4ab819cada88 | -13.25869 | -45.15182 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 8423d9a8-45f6-3307-953d-d5bb5191fd00 | -13.26891 | -45.16324 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f7635979-1d0f-379e-9ef5-51ccd4cc7b02 | -13.26668 | -45.14355 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 87a91df5-30da-3a71-960e-0929b4120501 | -11.78438 | -47.08859 | 2026-07-16 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0cd0769b-d12f-37be-b73f-7b97b9898d9e | -13.26473 | -45.15298 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| b8f04cdd-e9a4-3ad2-99f0-37c3b00fa2b7 | -11.79122 | -47.09037 | 2026-07-16 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 996ccdc5-2085-3f9e-bf49-11805e5710e6 | -15.20035 | -44.05428 | 2026-07-16 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17c0fdd4-1a11-3680-86ad-1969e4bd1047 | -11.78297 | -47.09529 | 2026-07-16 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 103beb07-ff07-396f-8aec-9eaa81df4aab | -10.88869 | -46.43862 | 2026-07-16 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8fa8b78c-6130-3625-8a85-5556ae647134 | -13.43258 | -43.8507 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fc470424-c544-312c-ad98-c223467fbfdb | -13.43662 | -43.8594 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acc56aaf-041a-309e-9e15-c5e507379cba | -13.4389 | -43.84796 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e795a41-f512-31bd-a898-55768b909eb4 | -13.26794 | -45.16796 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6b4c874c-263d-3c05-9eeb-956bb73568e1 | -14.14329 | -46.27349 | 2026-07-16 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72c640e7-d401-3e57-9a62-04a472108698 | -10.8899 | -46.44123 | 2026-07-16 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 23f250a6-1c56-3fe9-b565-45ec817d16be | -13.25967 | -45.1471 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 92a6a1db-328f-35af-a64b-4617420d64a9 | -15.20186 | -44.04695 | 2026-07-16 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79d59d5f-42fc-3e9a-be2f-81866d56b82c | -15.2011 | -44.05061 | 2026-07-16 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ebe7010-3d35-32e4-a4f8-073bc6436f6b | -13.26285 | -45.16212 | 2026-07-16 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| c7864aaf-e533-3573-926f-d2d7db058e85 | -13.44373 | -43.85263 | 2026-07-16 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 189939f2-bde2-324d-be14-d2b7b7337714 | -21.40259 | -41.20556 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 913dcae6-fca0-3a74-a9e2-a0bbf613821a | -17.59732 | -44.60251 | 2026-07-16 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f616f3-23ec-339c-a0f2-5145da35a077 | -21.82055 | -41.41102 | 2026-07-16 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60bdb844-3978-3b6a-88a4-484f667b2385 | -20.62534 | -46.28453 | 2026-07-16 03:38:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e362a745-d0b6-3d4c-b151-6b8f1c014561 | -21.39854 | -41.20472 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc78a0fd-23b8-3717-a8d2-fb1bad8648de | -21.40666 | -43.88718 | 2026-07-16 03:38:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec062f85-dd65-3f26-9f1d-6ceb286f03ab | -22.27679 | -42.88804 | 2026-07-16 03:38:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4fe3bb65-7910-3cef-b96e-a9d8a6e1b9ca | -17.70381 | -42.66407 | 2026-07-16 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 84e6c0a0-4e3f-3878-968d-d73fc2093cc6 | -18.67103 | -42.83491 | 2026-07-16 03:38:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5d443836-460f-35ad-9356-8a0fe427a3c3 | -21.40243 | -41.20471 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fa693b31-3bbe-34a2-a66f-0c03dde77ce1 | -20.81159 | -42.65699 | 2026-07-16 03:38:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b44c9bf-9b2b-30f7-bc20-63d717d9f5ef | -22.47215 | -41.91682 | 2026-07-16 03:38:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf888763-99b7-30d3-9dce-f95b94be3eb4 | -21.40169 | -41.20853 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5643e0b9-f0ef-387f-8a72-4dcdde6671b6 | -16.22819 | -40.90419 | 2026-07-16 03:38:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9b57df1b-5633-3e9b-85f7-3a4b224eb4b0 | -17.59141 | -44.60387 | 2026-07-16 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1649d58-173d-3b8c-b881-932dc85babef | -18.53758 | -40.41804 | 2026-07-16 03:38:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9eec045-e948-3021-9bd5-b9d3f9a502ba | -21.46919 | -41.20765 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 46e82525-abee-3b64-b1d0-16bf860a160b | -22.13692 | -43.21701 | 2026-07-16 03:38:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7eb29edf-f19a-364e-bd3b-b0d095009a20 | -21.39781 | -41.20856 | 2026-07-16 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
