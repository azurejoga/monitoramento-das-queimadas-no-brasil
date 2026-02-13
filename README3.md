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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe6f8834-5d13-35fe-b58b-ee878078cc91 | 3.79665 | -60.94288 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 216f7c56-8c00-3170-905d-af88edcef5ce | 3.35559 | -59.92891 | 2026-02-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a882fc7e-74a0-3937-a503-be49bbd1a07e | 3.33077 | -59.93539 | 2026-02-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d39d9a84-11df-3e5b-8a8f-01c70b75cf0a | 3.78647 | -60.90655 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb2b53f4-c2bf-3304-8ad7-bedfe6b92314 | 3.79292 | -60.89406 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10d54cd5-b8f7-380b-9246-cdf81bc9dfe5 | 3.3593 | -59.92381 | 2026-02-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0364c36-7ee2-3920-beaa-a93e444ad94f | 3.76458 | -60.90252 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e9c35ba-3e67-32ad-959e-b2849a1b704e | 3.79121 | -60.90958 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9adc8505-8cde-35e0-85ea-3b534c690277 | 3.36527 | -59.90487 | 2026-02-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6476465-0a93-3cc8-a944-40ebdcf20f95 | 3.86152 | -60.91409 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60e98baf-479c-3229-ac91-6e1114e48c62 | 3.76105 | -60.90689 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021ccbee-1d32-3c68-a6c0-a9cfe0420f9f | 3.75815 | -60.91496 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e029bba5-a148-31a3-a75f-8d51356eb780 | 3.78282 | -60.88422 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97b5871c-4720-3d34-a822-d7cb9a48b45d | 3.77867 | -60.8849 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0142fff-7c31-3807-a459-abf1f8dd3acd | 3.79423 | -60.92808 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db0e5d2f-22dd-358e-946a-3218bbbbbb8f | 3.75753 | -60.91125 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 164b616b-afe2-3d00-aeb6-f16be1322b52 | 3.76044 | -60.90319 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c39154b-628d-3cf4-9ea1-48e09d775aa5 | 3.32774 | -59.94485 | 2026-02-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1bca6b10-78f6-3331-9db6-f19ac04fd39f | 3.79605 | -60.93918 | 2026-02-13 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8617277-fa1b-3ee3-a5e9-15e332fc920c | 3.7959 | -60.92476 | 2026-02-13 06:18:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dcd55b22-1b37-33c2-aa0d-6b47b5b8ebb9 | 3.79677 | -60.92982 | 2026-02-13 06:18:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da48eb4c-aa08-32c8-89e2-0c25cf3496fc | 3.79764 | -60.93489 | 2026-02-13 06:18:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31487bd9-12ba-32f7-b6e2-ae78c70925d6 | 3.3673 | -59.9239 | 2026-02-13 07:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| dad6c738-1502-324f-9ab5-5cea449850d1 | 3.3673 | -59.9239 | 2026-02-13 08:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d52b12be-a4a9-374b-8206-1004f02b06b1 | -8.12055 | -40.01773 | 2026-02-13 11:51:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 34afd2eb-5aaa-33ea-a7d8-8ac181ecad77 | -8.11882 | -40.03065 | 2026-02-13 11:51:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0e160461-c95b-39f5-af40-deebc341a2c4 | -9.54774 | -37.17702 | 2026-02-13 11:51:00 | TERRA_M-M | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 27.8 |
| e169a8e0-5046-39c0-be50-8148b8d4a9cc | -11.14599 | -45.80081 | 2026-02-13 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5487e41c-0fe3-39f7-ae2b-c4bec22076e8 | -13.21469 | -47.77067 | 2026-02-13 11:53:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba70a979-fd15-3c29-af54-369592e21051 | -14.00319 | -42.85908 | 2026-02-13 11:53:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 31aafe1b-291a-37b4-a5de-af17f32dfca6 | -19.49014 | -42.62479 | 2026-02-13 11:55:00 | TERRA_M-M | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| b9062b79-79b7-3a32-9832-211b152df416 | -20.73418 | -42.0321 | 2026-02-13 11:55:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| ca7ba2b1-e3a1-3bb2-9ed7-e8496f7fc30e | -20.95564 | -43.79872 | 2026-02-13 11:57:00 | TERRA_M-M | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b1da5d4e-29e6-39cf-b694-2dbcf4cf6a0d | -22.54338 | -46.98311 | 2026-02-13 11:57:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ae2455b-ef75-38c0-a7ba-07cf8cd1eaca | -27.32882 | -50.1184 | 2026-02-13 11:57:00 | TERRA_M-M | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


