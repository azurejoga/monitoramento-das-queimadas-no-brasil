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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d732c6f0-8eb8-3846-9249-9ce48387e27f | -11.3963 | -52.9477 | 2025-04-26 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4b6dd5b9-99d3-3f58-aa50-c4e7872f6bd1 | -11.3963 | -52.9477 | 2025-04-26 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 25022cff-1203-3ece-ad0f-ada08d2207c0 | -11.3963 | -52.9477 | 2025-04-26 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 15269527-94a0-3aed-bfae-060054dcd07e | -11.3963 | -52.9477 | 2025-04-26 09:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 89461ba5-a748-3fe9-b058-644c202a8002 | -8.29373 | -46.13193 | 2025-04-26 12:55:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 665bd352-302e-3400-b9a8-24c741cd2433 | -8.28877 | -48.28012 | 2025-04-26 12:55:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| efe5f9cf-0c87-369f-a6a2-2b3fda76db55 | -7.25192 | -45.75706 | 2025-04-26 12:55:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 73ac65bc-fffb-3a8c-afa5-86305db88495 | -9.29329 | -48.30565 | 2025-04-26 12:55:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6d127139-d28e-350f-bcfe-7033aa75927f | -7.25145 | -45.72575 | 2025-04-26 12:55:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 9804899a-7199-3715-95b7-ac3621525496 | -8.27969 | -46.13038 | 2025-04-26 12:55:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e0056717-7db7-338f-a135-17eeaeda83ca | -13.81076 | -57.7825 | 2025-04-26 12:57:00 | TERRA_M-T | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3aa5e09c-381f-33a3-baf9-0be933a9135c | -11.4045 | -52.95496 | 2025-04-26 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 9a35df27-8971-3a1b-b3c4-cca9f1e6ba21 | -11.39676 | -52.94431 | 2025-04-26 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5b95c3bc-b895-3b99-9bef-248f2f8e6f1c | -13.93624 | -57.57144 | 2025-04-26 12:57:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d7a14325-1d85-323c-b506-3e6298c8bfad | -10.64636 | -49.87422 | 2025-04-26 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 51df9958-c6ef-3db6-9002-028bd6d49b4f | -15.72085 | -51.28043 | 2025-04-26 12:57:00 | TERRA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8440980a-2657-3c63-990f-64079c34d8b9 | -11.27868 | -52.46656 | 2025-04-26 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 49a0a3c8-e4c6-3623-ac98-60382fe7019b | -11.18832 | -45.7843 | 2025-04-26 12:57:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| cabdcc8d-f5a5-3eb1-9e1d-1061c762e10f | -12.81797 | -52.32772 | 2025-04-26 12:57:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d642345c-5dfa-36f4-b232-98069b22497a | -13.37642 | -54.26034 | 2025-04-26 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a833439d-4e12-36ff-8eed-482fc3ed789f | -11.39807 | -52.93488 | 2025-04-26 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 2fa815d1-8dad-3656-a422-1c0bd9c30541 | -15.71504 | -51.27384 | 2025-04-26 12:57:00 | TERRA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f804412a-d53a-301b-9611-a33e1f2811a0 | -11.40712 | -52.93612 | 2025-04-26 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 78624fb0-ce89-3f8e-90d6-1db4acf435fe | -11.40581 | -52.94555 | 2025-04-26 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d7809cd5-9bdc-3765-9d7d-5e6a3f7ff862 | -14.87953 | -47.40153 | 2025-04-26 12:57:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ced159f3-c6f8-3a82-92e6-46a065b7cc9b | -16.80739 | -50.8011 | 2025-04-26 12:57:00 | TERRA_M-T | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2d922eef-8a89-35d4-aeb3-ba9e9d6ac212 | -30.13048 | -51.86845 | 2025-04-26 13:01:00 | TERRA_M-T | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 22.1 |
| d1a01ef6-5032-3a28-9888-8ef061c2644d | -29.78892 | -51.50385 | 2025-04-26 13:01:00 | TERRA_M-T | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 26.1 |
| ae948f8b-c37a-306b-9eb9-a10f355638ea | -30.13242 | -51.84765 | 2025-04-26 13:01:00 | TERRA_M-T | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 13.0 |
| 14e1ccbd-2b93-340c-a062-a821cb62e786 | -29.78693 | -51.52561 | 2025-04-26 13:01:00 | TERRA_M-T | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 25.8 |


