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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bda3ecf-485a-39bd-a42a-1968b49bc5b9 | -8.9677 | -45.2227 | 2026-08-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 2dc05ede-1495-3684-b938-b5475bb8fb71 | -11.1349 | -49.9117 | 2026-08-01 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| da7424c3-e460-31f4-823b-62be10bb9da5 | -11.1539 | -49.9096 | 2026-08-01 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cfc2cb20-5aa3-388e-9329-7111e96b1d10 | -11.2591 | -54.8517 | 2026-08-01 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 221.0 |
| 958de091-d14e-3f43-ac22-68e824ce7170 | -8.1814 | -55.4455 | 2026-08-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 856afde1-b479-3399-ac66-06232dd7c9bd | -8.2002 | -55.4243 | 2026-08-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 186631d4-5be1-3ea4-989c-c6f5e5ce550c | -8.1816 | -55.4255 | 2026-08-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ec68f368-fbe1-3a63-af46-fcefc57fe9c7 | -11.1539 | -49.9096 | 2026-08-01 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 0fcd428d-301a-3e84-bab6-f8bb3e872d95 | -14.0536 | -46.2702 | 2026-08-01 14:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 116.8 |
| bdb840e9-9923-3724-8452-6297ed2857f9 | -8.1814 | -55.4455 | 2026-08-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 0228c8d0-e4b3-33c2-b0d1-0f772c681f42 | -14.0735 | -46.2439 | 2026-08-01 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3817f7d2-7133-307f-901b-53b0f306b887 | -14.0929 | -46.2407 | 2026-08-01 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0023739b-756e-3c8d-ae7f-f3836decabcd | -8.9677 | -45.2227 | 2026-08-01 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 7516d4cf-5f4f-3b97-a09f-f43985d3246b | -11.1349 | -49.9117 | 2026-08-01 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 62da5a9a-8955-3a77-8870-3f498a99be43 | -8.9681 | -45.1999 | 2026-08-01 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c30c659e-f5cd-3568-b3f1-5fbde0ff0dc5 | -14.073 | -46.2669 | 2026-08-01 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b9883362-da7b-32ee-b5ae-085b5b861b56 | -8.9677 | -45.2227 | 2026-08-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 201.5 |
| d73e9c44-f6e1-3cbd-9b46-d4f27f3daa34 | -11.2591 | -54.8517 | 2026-08-01 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 721.2 |
| ca5ac85a-981e-3ffa-b9dd-655adecfa736 | -11.1349 | -49.9117 | 2026-08-01 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 29869eb8-b808-3410-b955-812777346171 | -14.0536 | -46.2702 | 2026-08-01 14:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 129.5 |
| d01b9141-cce9-36e3-88eb-62beb5a361e9 | -11.2588 | -54.8721 | 2026-08-01 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 264.0 |
| 7c1dfa45-a9f8-35f3-9b7d-15e3c27bcac3 | -14.073 | -46.2669 | 2026-08-01 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 26a4f533-ed85-33db-b47b-cc8300e75e5a | -11.2402 | -54.8534 | 2026-08-01 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 334.9 |
| 44e31b51-afef-3139-b997-608ff0eb6a8f | -8.9681 | -45.1999 | 2026-08-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 190.6 |
| c90b5803-10a5-3cbe-9733-94ce8348bd16 | -13.0538 | -52.7287 | 2026-08-01 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 33c78b6a-c2c7-3b5d-9691-010ee4dded5e | -6.0921 | -45.2406 | 2026-08-01 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e22f5e2c-bcde-3565-af97-1560963b922d | -11.2404 | -54.833 | 2026-08-01 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a0d04eec-8313-3f7d-8cbc-bdb0bfcb1ed4 | -14.0725 | -46.2899 | 2026-08-01 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0bbfef4c-1ca2-3193-9da6-7f9831ec52a5 | -14.0735 | -46.2439 | 2026-08-01 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |


