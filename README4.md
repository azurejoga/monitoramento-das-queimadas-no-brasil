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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3590f345-623f-3317-9096-9e5f4920f287 | -19.6715 | -56.93306 | 2026-01-18 05:22:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 78f33154-6a2c-3046-a0e1-5d4090587012 | -20.42987 | -57.87916 | 2026-01-18 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1bd99de7-3234-324d-9328-e5362a760b8c | -20.42537 | -57.88365 | 2026-01-18 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 06158e1f-8d66-3fd8-8b8c-f0a3aafb40a4 | -18.81599 | -51.60344 | 2026-01-18 05:22:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49fe69a5-15bd-3773-948c-9a4ba890cf0a | -20.84493 | -51.73946 | 2026-01-18 05:22:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c3db67fc-c5d7-3e59-a54a-15a10b9222eb | 3.48042 | -60.28917 | 2026-01-18 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea47562-61fc-359e-8546-4b767bce3837 | 3.48108 | -60.29324 | 2026-01-18 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d97b7f39-f500-339f-a107-911aad9e7bf4 | 2.55132 | -60.56778 | 2026-01-18 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 456eaacd-676a-3204-a4a1-163001a49c6b | 2.56837 | -60.65137 | 2026-01-18 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb21871d-8c7f-3074-ad5b-70ad6fd3eca6 | 2.10156 | -60.62193 | 2026-01-18 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 59d5e961-30e1-3590-abe2-55934da18c17 | 2.55489 | -60.56721 | 2026-01-18 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7663a87-f0b8-32f0-a43c-ce0ea32c87d1 | -8.2317 | -35.29007 | 2026-01-18 11:14:00 | TERRA_M-M | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 88434b4b-8dff-3c87-8e06-bdaf37b3a16a | -8.40875 | -38.04067 | 2026-01-18 11:14:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2d609651-3253-3977-87c3-ff94ef5dabe5 | -8.24051 | -35.2973 | 2026-01-18 11:14:00 | TERRA_M-M | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9fe5569d-4d8e-31d8-972a-bab3cd29f77f | -8.24186 | -35.28818 | 2026-01-18 11:14:00 | TERRA_M-M | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ab132d7d-cd30-3e1d-94c8-a9180f9f1f56 | -8.04514 | -36.24349 | 2026-01-18 11:14:00 | TERRA_M-M | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0d4981e4-e886-30f4-a91d-918c35dd80a0 | -7.57016 | -38.02612 | 2026-01-18 11:14:00 | TERRA_M-M | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d79c200e-3119-3a34-8a27-ac3a5cb10315 | -11.59391 | -38.77657 | 2026-01-18 11:17:00 | TERRA_M-M | BIRITINGA | BAHIA | Brasil | 2903607 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0d2edea5-7b36-3182-aa9c-5274ca1861f8 | -9.29869 | -37.78629 | 2026-01-18 11:17:00 | TERRA_M-M | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 19.5 |
| ac84e154-dc7d-3ae7-8aef-2b565580c775 | -9.36693 | -36.91947 | 2026-01-18 11:17:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a493a60a-6ef2-3b07-8e8d-ace6ce69f137 | -20.41 | -57.8323 | 2026-01-18 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| b2407bdc-019e-3043-b6f8-20a83d7526f1 | -20.4294 | -57.8713 | 2026-01-18 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| e572d2d4-e98b-315a-89a8-59d28cfec7cc | -20.41 | -57.8323 | 2026-01-18 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| a4586553-f729-3b51-b8ee-5c8c27c427f8 | -20.41 | -57.8323 | 2026-01-18 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| cac03c4f-7972-39cf-89f0-90af31e2e241 | -19.6623 | -56.9331 | 2026-01-18 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 198f25f7-0dd2-3979-b03e-28f716111f79 | -20.41 | -57.8323 | 2026-01-18 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 7b22cf39-99dc-38e5-bd9b-8324d2aca376 | -19.6623 | -56.9331 | 2026-01-18 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 44e06fa0-2e7d-3770-9402-f7abbb5284bf | -19.6623 | -56.9331 | 2026-01-18 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |


