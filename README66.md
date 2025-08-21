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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30ad24ea-a288-3ff7-b484-50bb4f3d3161 | -8.7567 | -45.4733 | 2025-08-21 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 200.9 |
| b25d71b8-c84b-3e19-81b0-ff116268645e | -13.051 | -45.1693 | 2025-08-21 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 428f16e0-7138-3702-a7ea-65060bf27b49 | -14.7504 | -56.0151 | 2025-08-21 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 7eeecf26-4fbc-3546-ad7f-06ca382eb12a | -8.7759 | -45.4486 | 2025-08-21 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 2691a0cd-d078-3497-9dcd-5773be19a7c0 | -6.1 | -44.397 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f09b80de-7274-3bd6-8e28-b5dbfe9683e0 | -6.4158 | -44.6695 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| aeadb70c-9415-3ef5-822a-fafe51e10e6f | -8.8552 | -62.3933 | 2025-08-21 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e62d8563-08c3-3698-a4b4-c00176c7cfa6 | -6.4857 | -45.1874 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e4e9736c-208a-3990-bb35-f4658c71be5e | -11.2896 | -44.9291 | 2025-08-21 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d1b2a344-ff37-325a-baca-75b91e48ae0a | -12.2191 | -45.4152 | 2025-08-21 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d998237d-b63b-39ca-bd59-e3c1b24e8e90 | -8.8551 | -62.4123 | 2025-08-21 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 60e211a7-d57a-328d-954b-ebbb88b64bfa | -8.7756 | -45.4713 | 2025-08-21 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 4533412b-fc6c-3b97-abeb-11666c2e9946 | -14.5463 | -51.9088 | 2025-08-21 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 71c2d311-db5a-3799-955b-1853529ec698 | -6.0992 | -59.9267 | 2025-08-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 227a1ac5-da57-37f4-8002-eebc75aaea74 | -15.0189 | -54.8528 | 2025-08-21 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 160900d0-af2c-3b84-b900-5e9107285f40 | -15.1628 | -41.2812 | 2025-08-21 14:40:00 | GOES-19 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 45fa5a8e-0678-3224-becf-d6d4db61ee8b | -9.7241 | -47.9588 | 2025-08-21 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 8129a160-52e6-3f5d-8404-e9f7c7aa073d | -8.8922 | -62.4107 | 2025-08-21 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 19edf6ae-c1c3-3b59-be45-6eee9dafdbc0 | -7.5012 | -44.9626 | 2025-08-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d3d2fad7-b496-3b5e-ba24-2400db258360 | -8.8735 | -62.4305 | 2025-08-21 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7fb43dd0-59f6-3a59-b9da-5a4733aee010 | -15.9187 | -52.2089 | 2025-08-21 14:40:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 148.8 |
| d5cc54e6-2293-34a1-bb65-07de4056706a | -6.2924 | -43.8747 | 2025-08-21 14:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 46890314-b1ef-3f66-901b-9e371e01092d | -6.4855 | -45.2101 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 298df9b9-c9f0-32df-b2b6-6e08fa982e05 | -6.5386 | -45.5224 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e67ce26c-cd4b-31b9-be8c-f1f109b280dc | -7.6296 | -45.2464 | 2025-08-21 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 1a0eaaea-f459-365b-86d5-9ffe79cb87e1 | -14.3127 | -52.0249 | 2025-08-21 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 971d154e-c525-3332-937b-056c4279f1c4 | -8.5555 | -66.9574 | 2025-08-21 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3ff1df2e-5daf-30e7-b21a-1a0f586a763d | -13.3157 | -54.4047 | 2025-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 905a0203-36b4-30e5-8500-c9aa12209ff5 | -6.4528 | -53.3872 | 2025-08-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3a3d1fd5-965e-3305-8229-76b01cb0e8bb | -9.7052 | -47.9609 | 2025-08-21 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 271.5 |
| 5c0268f5-19c8-3c27-93f1-30c3d1455b85 | -8.0152 | -47.6656 | 2025-08-21 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 047731a9-d303-39a1-a036-fe86e961b31d | -9.1712 | -59.5987 | 2025-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 59aea877-92ca-3a71-b983-3ec9cd31122e | -6.4529 | -53.3669 | 2025-08-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 03d39bad-b4b0-35bf-adc4-2361e11bd4da | -7.5832 | -44.3819 | 2025-08-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 66080b31-7652-3dbc-9084-f51beb5b4e91 | -7.0166 | -44.6184 | 2025-08-21 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ed810fd4-52c5-35c6-88ec-572641e764cb | -15.0193 | -54.832 | 2025-08-21 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4ca46dff-ddb3-3ce7-a6c9-039a083c2e08 | -14.7501 | -56.0356 | 2025-08-21 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |


