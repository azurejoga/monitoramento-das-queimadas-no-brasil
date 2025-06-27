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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcdd96ca-6ce4-3f8d-b4b7-1d7b784a6e76 | -5.9028 | -43.4418 | 2025-06-27 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ba09ef09-d6c6-3417-a34c-b9f71d76d6f2 | -11.1903 | -55.9101 | 2025-06-27 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 4b0ad835-d8f2-37b8-9637-a3ea1056a0ef | -10.8196 | -53.7459 | 2025-06-27 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 51611384-2bb8-37c4-a176-1556746e856a | -10.3128 | -57.1367 | 2025-06-27 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1f0e5448-a6fd-3ebc-bfeb-c263ececda5f | -10.2653 | -44.6298 | 2025-06-27 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 77ac05fb-2207-3f2f-93dd-91bd6e462ba8 | -10.6129 | -46.725 | 2025-06-27 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e9cb5a6b-49d5-3d71-9d6c-560071235c30 | -10.2941 | -57.138 | 2025-06-27 14:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a16d1812-1e54-3c55-9ba8-cd8ff73a4576 | -5.9216 | -43.4403 | 2025-06-27 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5b761546-e5e9-3352-a59b-6675cbcbee13 | -11.546 | -47.8772 | 2025-06-27 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 196.3 |
| fbb09044-193f-307f-8478-761d0bdb6a61 | -11.5779 | -52.115 | 2025-06-27 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| b9bc7d8d-e50e-36ab-b1bd-33e5ffb269b6 | -10.6319 | -46.7226 | 2025-06-27 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 7e98ae95-f7bd-34b1-ba57-6c391e65e4d0 | -10.8196 | -53.7459 | 2025-06-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 3890b75a-1f2c-36ed-8799-84b84e3f7071 | -10.384 | -46.7977 | 2025-06-27 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 65dab298-d479-3836-bc16-ceb2c82f69bc | -5.9216 | -43.4403 | 2025-06-27 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a23d53e2-36e7-39ae-8ed7-a8cf40e2bb58 | -10.6129 | -46.725 | 2025-06-27 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| fb8b80e3-43d9-3dcc-9094-2e15729d0e10 | -11.19 | -55.9303 | 2025-06-27 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 201.8 |
| d89dc6b7-904d-39d5-9995-85f09b21c1a7 | -5.9213 | -43.4636 | 2025-06-27 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e7bf34d5-aeb0-399a-b729-836f2b75dff3 | -11.4337 | -54.4689 | 2025-06-27 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f1a12a61-b567-3d12-a55e-d97f7d988f2f | -8.5722 | -51.5761 | 2025-06-27 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0d55106a-0749-3f8c-ad9f-0cce55700a3d | -11.1903 | -55.9101 | 2025-06-27 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 48c90407-fc8c-3930-9e4d-b2addb51890a | -11.5779 | -52.115 | 2025-06-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 2146fc50-d06b-3459-b629-0dee7d1ebece | -10.8198 | -53.7253 | 2025-06-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cf40638c-f389-33d3-a886-3086a4a5c605 | -11.546 | -47.8772 | 2025-06-27 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 1414c526-76ba-39a8-a5c9-3467b7fcae96 | -8.8499 | -50.1616 | 2025-06-27 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ece949a6-93fc-34ba-b5fb-cbe1e0f7f23d | -10.2941 | -57.138 | 2025-06-27 14:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f46e80f3-e60e-3acf-a4ff-c2325a4625de | -5.9028 | -43.4418 | 2025-06-27 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 184265ea-94c1-3582-afa4-bc31f68eb461 | -5.9026 | -43.4651 | 2025-06-27 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 98c21b44-f081-3455-a07b-b5485a75edb1 | -10.8385 | -53.7442 | 2025-06-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b8630bd2-0c0b-3f16-826b-48079e151f50 | -10.6323 | -46.7001 | 2025-06-27 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |


