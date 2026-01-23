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
| 79877b92-af1f-34f6-a12b-5819f804518e | -7.2782 | -43.0862 | 2026-01-23 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 253.7 |
| 1b3ddacb-a86b-33ca-912d-65db8d046a13 | -7.2594 | -43.0881 | 2026-01-23 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 328a1dbe-81ab-379b-b4d2-58afba61206a | -20.389 | -57.8769 | 2026-01-23 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 209f8264-c123-30b7-b5e7-5089dfbdf8a6 | -19.6832 | -56.8884 | 2026-01-23 13:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 469067d0-5313-3b82-a464-53f04bec616b | -19.6836 | -56.8674 | 2026-01-23 13:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 6014314d-b2ea-3abb-84c2-696874e9e87f | -7.2785 | -43.0627 | 2026-01-23 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 248.3 |
| 739f7fd4-60c7-33ed-a459-fa7742f83754 | -7.2782 | -43.0862 | 2026-01-23 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 300.6 |
| 5d5461a8-6c54-342a-b9f5-7e4f228b63b0 | -7.2785 | -43.0627 | 2026-01-23 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 272.3 |
| b45c32bf-0899-30f3-b7b8-5cea48aa7c99 | -7.2594 | -43.0881 | 2026-01-23 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| 15e32dcb-dd35-332e-97c8-6c0f2647b8d4 | -5.4539 | -39.2287 | 2026-01-23 13:20:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 60d65420-e8a8-3de1-b895-f7bfee4db5cf | -22.0275 | -56.3434 | 2026-01-23 13:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d49bbe21-d21f-3dd1-b8ba-2ddf14682577 | -19.6836 | -56.8674 | 2026-01-23 13:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| cf5b0208-442d-3c92-95f2-3bdb2f4dec92 | -5.4351 | -39.2303 | 2026-01-23 13:20:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 75fc66f9-c73d-3550-a92f-1e8f210e5291 | -22.0275 | -56.3434 | 2026-01-23 13:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 375632b7-9d06-3f89-95ea-99f3d9d5a03d | -7.2594 | -43.0881 | 2026-01-23 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 5d1b7b44-7d58-39da-9ceb-1c6151237ede | -5.4351 | -39.2303 | 2026-01-23 13:30:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 05f9385e-7813-3206-a2e3-b8e18bb2223b | -19.6836 | -56.8674 | 2026-01-23 13:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| fb9bc91c-22c1-3294-98de-f82f842c4d44 | -5.4351 | -39.2303 | 2026-01-23 13:40:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 2cfe139e-ac1b-3d0d-9306-e0b830ce7446 | -22.0275 | -56.3434 | 2026-01-23 13:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5a497f4c-283d-3b5b-83ba-1f55b1733b3a | -19.6836 | -56.8674 | 2026-01-23 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| ad8cc0f7-eaa3-35c2-b0c5-5f5f6a0aa526 | -5.4351 | -39.2303 | 2026-01-23 13:50:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 101.9 |
| b48ff955-dbb5-3c2d-b35f-6d0e8abd014a | -19.6832 | -56.8884 | 2026-01-23 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 7095de40-e138-3790-a593-77de6fc834f6 | -5.4539 | -39.2287 | 2026-01-23 13:50:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 352548ba-8f2d-39c8-b905-c71f9cc86953 | -22.0275 | -56.3434 | 2026-01-23 13:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8d88f72b-2458-3ad2-822a-97443eb1d04c | -19.6836 | -56.8674 | 2026-01-23 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 594fd599-674e-3531-94e8-bb3ee6cabd8a | -5.4351 | -39.2303 | 2026-01-23 14:00:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 106.2 |
| d006d656-e419-33e6-955e-d115c5f2426f | -19.6836 | -56.8674 | 2026-01-23 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.0 |
| c8f15058-c62e-356f-8974-bb4cd442932d | -22.0275 | -56.3434 | 2026-01-23 14:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7cd984cd-592d-3d4d-af0e-71492efea173 | -5.5257 | -37.6932 | 2026-01-23 14:10:00 | GOES-19 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 112.1 |
| a0399946-ad54-3c65-a52c-07c68b6993b0 | -19.6635 | -56.8702 | 2026-01-23 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 2b5b7b62-b78a-369a-bdd3-a05f81f3c327 | -5.4351 | -39.2303 | 2026-01-23 14:10:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 5197f70f-b335-35cf-b728-9d72bee86000 | -19.6836 | -56.8674 | 2026-01-23 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| e46e79eb-3fbb-37f3-aa3c-06397f28e4e5 | -22.0275 | -56.3434 | 2026-01-23 14:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a43216bb-af8d-31c9-83e4-48a9a5fa8b52 | -19.6836 | -56.8674 | 2026-01-23 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 122.5 |
| 15f92295-bb6e-3731-b4dd-1e9950e7d3bd | -19.6836 | -56.8674 | 2026-01-23 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 136.0 |
| 80675f39-5457-3b98-ba8f-a469a1b777be | -19.6635 | -56.8702 | 2026-01-23 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 392602aa-286b-3894-b6ec-764224d0feef | -22.0275 | -56.3434 | 2026-01-23 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 16e72053-2ada-3a05-8cf0-0394fe048509 | -19.6832 | -56.8884 | 2026-01-23 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| a4d84482-60bd-3663-aaf4-84b2b7b5918d | -19.6635 | -56.8702 | 2026-01-23 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| f0a9c25e-0a3d-3468-8e33-779493f44f03 | -19.6836 | -56.8674 | 2026-01-23 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 51fe403b-1dba-3e1a-8151-0abbd80f5df3 | -5.4106 | -37.8588 | 2026-01-23 14:40:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 98.0 |


