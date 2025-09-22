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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4b28dbd-f23e-38d0-a455-004f8d95a946 | -16.01421 | -59.46719 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6820dd76-0909-3bb7-bf4f-559e3e1ebce7 | -11.33176 | -54.35443 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61dc5ce8-8a59-3b3c-acf6-698e948afc06 | -15.83502 | -59.58464 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 153d9e8c-2c69-301e-8bdb-3946e5d7b2be | -9.1906 | -71.83528 | 2025-09-22 05:31:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca224bb9-582f-35bc-87c3-47c99e8bd9ec | -15.83691 | -59.51109 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6cd0ba5-7c28-3874-a6a7-be7c80814e33 | -11.32691 | -54.35061 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24147199-9899-3a0f-bf6f-b4c9ca073148 | -10.17664 | -68.79175 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0946b16-2953-31e9-ac53-5f1483fe74e1 | -16.02288 | -59.46295 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6ae368c9-010f-3f41-9875-325f6f48571c | -10.10786 | -64.88709 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48ab9996-5ce2-341d-a323-c06b3bcf6a56 | -9.24691 | -67.39288 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e526a2-c1d6-3a57-afe9-e2cb8861ada8 | -10.02315 | -68.40723 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60daf6fc-011e-3ee2-9bb5-7c24566b414b | -11.64174 | -52.85488 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e63f189-6a26-35b3-98c9-39e68b0b43de | -15.77497 | -59.41067 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26da6cd6-3aec-3e2c-98e6-0538a0f50036 | -15.96281 | -59.37833 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4aad7475-2526-322b-b267-5dae74481d1c | -15.00514 | -55.31302 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3de1b78-f665-3b26-8a2d-4bb62ba51edf | -11.83051 | -64.93148 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44181230-cb9c-3ca3-addd-86469bdb597e | -11.64122 | -52.85913 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 583566d3-5600-30bb-9c7e-50a0eaf46666 | -9.97455 | -67.09578 | 2025-09-22 05:31:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b97ddc1f-0d8a-3547-8487-9667b63bea99 | -11.79432 | -64.92953 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee9d14cf-a381-3c5e-975d-513a16897c96 | -11.3176 | -54.33966 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73700ff6-2363-302e-b7fa-1646117df121 | -10.10386 | -64.89024 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6a7a43e-b9a3-362e-9b8f-755353f938e4 | -15.30301 | -56.79647 | 2025-09-22 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d003bd24-703a-3c42-9004-99f3d1aaf5cc | -11.31678 | -54.34619 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c14ea80-9cfd-3509-b9fa-75dec811e9ca | -15.96732 | -59.37508 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2ac8a38-8c42-3f5c-aadc-326595c53d66 | -15.95826 | -59.47264 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 333cdad5-df17-3210-a9e8-891dbea63b94 | -16.01888 | -59.46248 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7d964d54-256a-3993-b294-8a9fcdd30594 | -9.28513 | -68.11973 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94efc8c5-4b45-3176-9a32-1d0f120c959d | -15.41592 | -58.78084 | 2025-09-22 05:31:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9648f70a-7285-359b-b699-9b3d020dacbc | -11.87027 | -64.94181 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a2896bb-2194-38e6-af5b-79abddb99e40 | -10.16157 | -68.69734 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1142d47-0aa6-35d1-be36-e17f7cd59f75 | -15.993 | -59.47446 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b70b9e3d-5b16-31a3-88f1-2e5499882818 | -15.76449 | -59.41661 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd7fda42-8e25-33a4-acee-fadf8de5b499 | -15.76293 | -59.46007 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2ed6b33-27fb-34bc-b1bc-f26a11471403 | -11.32246 | -54.34356 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b72913a6-78fb-3282-b22a-3c8e1b0b653e | -9.24776 | -67.38795 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e15fbdc1-546e-3e5b-b6e8-b2a9b3092956 | -10.10726 | -64.89079 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcf93690-3287-3988-af18-2222cbab66ff | -11.83111 | -64.92783 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38338cc3-27d5-3bdb-8bc4-40d9fe0bdec7 | -10.17179 | -68.79485 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41084ac2-63f2-3892-a352-cb802ebd0ce9 | -11.32731 | -54.34743 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1378c858-af28-3bf5-a6ae-0ddc31739798 | -15.3159 | -56.80811 | 2025-09-22 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 022de92f-2fe2-39fd-89b3-a6a9a8738304 | -15.8376 | -59.50603 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2da8d609-6e9c-320d-91fe-13f3ad5122d9 | -10.1133 | -68.19868 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4600e6a4-38c6-3892-8362-9e6f177570d0 | -15.35737 | -59.1845 | 2025-09-22 05:31:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5742e29f-2eb4-3da6-bfcc-48eeff9a6147 | -11.32205 | -54.34678 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d29834ec-bcd5-3735-955a-6aa40df14fa2 | -12.79512 | -60.18693 | 2025-09-22 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59339f0e-107c-3a20-a4b5-c7508928fbc6 | -11.64653 | -52.86406 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54294f7c-88a9-3e2e-9e41-bdaafa962ba1 | -15.8829 | -59.42975 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea519550-427c-3d5e-a45f-296e3d8144a1 | -16.00158 | -59.47082 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00151872-bede-3869-af05-7b94fe90f6b8 | -9.23355 | -68.25018 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 615cbd62-014e-349f-a5fd-bd8060d16c5a | -11.74692 | -54.72311 | 2025-09-22 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5baaa560-eeb2-3b15-bb8a-d65f5006231d | -11.87422 | -64.93872 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4473481c-71ee-3a4e-b28a-84331c65f651 | -11.62958 | -52.85767 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69a8084a-73d2-356b-8271-3efe661644d1 | -9.02564 | -68.51926 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a4df33-842c-35fb-92d2-d036b3f2cd83 | -15.95849 | -59.4106 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bf13346-73d7-3f83-9d3d-84226a5c63ac | -15.96291 | -59.46822 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a4f2e5-d450-34b1-8f1f-6648d6dcb0a8 | -11.64631 | -52.86546 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32a8ea80-96a1-3a0f-9c1c-bf4de2c09091 | -15.88444 | -59.42918 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bf70528-65a3-3fff-984c-7882c4c4e6af | -10.63809 | -69.03672 | 2025-09-22 05:31:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66753ca3-f183-3aca-b732-e60ee4e0e521 | -9.72013 | -69.08294 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe657d5-f930-3de3-9e65-e3aa95b1832f | -9.47204 | -67.8896 | 2025-09-22 05:31:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 094cc2c9-66f8-3a7b-97f0-aa0909b4d0b7 | -16.01952 | -59.45768 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 10639137-f48c-30bc-a7c7-9ff2a308f663 | -10.17247 | -68.79099 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11765f61-16ce-36b7-92d9-f3b95093b955 | -10.27703 | -68.75763 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ac96e4-066f-39a6-9641-10b6d3a9d482 | -10.05461 | -63.32373 | 2025-09-22 05:31:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0089653b-c881-3433-9707-a77d64da0e2b | -11.32164 | -54.34999 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24196d83-4797-3608-bbe7-c4b151701851 | -10.09485 | -63.54514 | 2025-09-22 05:31:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc08a14c-fc7c-3985-8f74-b346b5c738f4 | -16.01023 | -59.46667 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 577361f4-ce51-352d-9f53-119400519780 | -11.64146 | -52.85623 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 619b4395-0e69-3288-a826-2f1f48d77efe | -11.88212 | -64.93254 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dd7344e-e3db-392f-a6f0-c82179356f24 | -15.95933 | -59.37395 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88f8be0f-986b-3e6f-ab9b-2de390eeaef3 | -11.64705 | -52.85981 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 387ac928-8600-336d-8079-a679486b59f3 | -15.97252 | -59.47622 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de8476d5-313c-3d4c-bd49-0afd4d31a7d0 | -10.13502 | -63.00489 | 2025-09-22 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fc17722-f2e4-32e8-abe5-c9f1fc25555a | -11.63643 | -52.84996 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3e554c62-9697-3ac0-ae37-47d8c15e59a0 | -10.19826 | -69.089 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aedc963f-ba8c-3d34-af56-01b145c8687e | -11.63695 | -52.84566 | 2025-09-22 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 309d060a-a8d5-3d91-bc23-2bf946ace5fa | -15.99762 | -59.47012 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5de1d43b-1f7c-399a-ad9f-c9e2a624c286 | -15.03399 | -55.29064 | 2025-09-22 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca299a95-6807-3e38-84e6-e73be197815c | -15.8416 | -59.50624 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a05d64db-2ca0-319a-ac73-730c61608e1f | -11.88095 | -64.93983 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4a32b244-d6ec-368e-bd5c-505182b40825 | -15.81459 | -59.49695 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85ba1aa9-acb5-3f50-a052-2a9da46c5c25 | -15.30279 | -59.25663 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c7b16ec-8b32-3b00-90fe-cb47fc8f2a64 | -15.77022 | -59.41573 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7cdbef7-a47e-3d69-a193-1845c4e0066d | -10.16459 | -64.72983 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd0c85a4-46a0-3cc4-9973-871254a165b1 | -10.67085 | -69.09869 | 2025-09-22 05:31:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 210aecd4-6e20-3b8d-a75e-4fcbb68d1027 | -9.28755 | -68.34801 | 2025-09-22 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 489ae5e2-d958-3b90-a1cd-323415e6e125 | -9.28574 | -68.11611 | 2025-09-22 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b3360f3-7b05-3ab1-928b-5ac514c6d521 | -9.59555 | -68.57654 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3403e7b7-fa2a-3a9b-8513-e9755515499b | -16.00468 | -59.44708 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04b66711-1121-30b9-b8fb-c8871e13b4ca | -11.87817 | -64.93562 | 2025-09-22 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e8828e-ed4f-3162-b8e2-1c7f0f9f83ca | -15.97635 | -59.3988 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69f35b40-fbe2-3eea-8a61-0e3678bc3c53 | -10.43754 | -61.34261 | 2025-09-22 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8685d376-a68a-360d-8e28-97976989b09c | -11.33217 | -54.35122 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4afdb044-ead0-3de6-8113-7a65cef944e1 | -9.36319 | -68.32632 | 2025-09-22 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fa964cb-2bb0-3db1-9d4d-d96a8d10c8e6 | -11.32771 | -54.34422 | 2025-09-22 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34658ea5-68bf-3d0e-951b-17e38c382f0e | -10.9204 | -68.23679 | 2025-09-22 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 943890ee-2ddb-3cbd-851b-d3ffba7ae764 | -16.0182 | -59.46766 | 2025-09-22 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05c9130c-e797-3970-8352-01410866e5b8 | -10.16288 | -68.6897 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1dc99ae-f124-3e0c-8155-8a96ee721b77 | -10.16572 | -68.69804 | 2025-09-22 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18c0985a-66b8-34d0-be46-91daf6c71d30 | -10.16797 | -64.73038 | 2025-09-22 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
