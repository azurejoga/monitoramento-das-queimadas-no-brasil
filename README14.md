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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53738bac-d60d-383e-935e-87f3b2eec835 | -10.81469 | -56.95568 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f7d2bb-5777-3f2a-94ab-21761fa82a8b | -14.23366 | -45.49097 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 014f8d01-9424-349e-aa56-783695ca7544 | -11.29901 | -53.98655 | 2025-06-06 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5df0030a-995e-33a4-b21e-5751c7ca76d6 | -14.2273 | -45.49019 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3465b136-9e82-308a-a92c-bb08cd2e6a4e | -9.96366 | -64.97021 | 2025-06-06 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e007753-72bd-351d-99b9-61d0e3a2c9f3 | -10.49351 | -53.66306 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 848f24c1-7079-35cd-8399-28072d7a5099 | -10.49255 | -53.65651 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ada6ac2e-7e82-3d67-bdac-94ddf70a5edd | -19.27833 | -55.15516 | 2025-06-06 05:06:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 543f1bb6-fbc5-39e5-bb2c-91bfeb49b6e5 | -19.4252 | -54.77902 | 2025-06-06 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 314f3a04-03c3-3d46-9624-059355c6763f | -19.42584 | -54.77416 | 2025-06-06 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 29dcce89-84e3-3e87-b6bb-a8625479599a | -18.40853 | -54.57342 | 2025-06-06 05:06:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9acb822b-f372-3493-b66b-a3bb9e561719 | -19.05221 | -53.45913 | 2025-06-06 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e171fb6-b8f4-3a57-8f88-3ed6a3e9e1e2 | -19.04818 | -53.45853 | 2025-06-06 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ad7586a-8d4e-36d4-8a27-e37626fa3329 | -21.02821 | -55.64825 | 2025-06-06 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71a1134d-d128-3f19-a0c7-8f609bf367b8 | -19.43711 | -54.77583 | 2025-06-06 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e14617e-c181-3fb1-bab1-935f8912ea30 | -17.91202 | -54.11204 | 2025-06-06 05:06:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407304fe-c1be-37f6-8ccd-4a9e18d4be8a | -19.01561 | -53.48773 | 2025-06-06 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bae8101-0e67-3a92-bf59-2c2c839bf6d6 | -21.02814 | -55.64606 | 2025-06-06 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c89af43-a395-398a-af8f-a795c4d7ad1e | -19.43335 | -54.77529 | 2025-06-06 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c89ccbd9-ee60-3ca0-9a62-7a61d98f095e | -19.42895 | -54.77959 | 2025-06-06 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0414ec6c-fa85-3195-b435-0b5132522ceb | -20.5444 | -54.11774 | 2025-06-06 05:06:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47fe0618-e6d5-30a1-bc7f-62cc11508887 | -19.42959 | -54.77474 | 2025-06-06 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0828844c-6a60-35fc-a2b4-6226553dcd50 | -19.04912 | -53.4576 | 2025-06-06 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab4029c-227c-3728-ae8a-117c28270087 | -15.93149 | -57.67201 | 2025-06-06 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc01a34e-72c6-3778-849b-5e4595252e2a | -16.57269 | -54.5212 | 2025-06-06 05:06:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 713a6c00-dc60-3f8d-8c06-37d621a2a289 | -16.12643 | -59.86098 | 2025-06-06 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddcd918d-7146-3848-a730-73f11042caab | -14.78891 | -59.56543 | 2025-06-06 05:06:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c389b033-ca3a-3c92-a7e8-2c9289d086f3 | -16.56902 | -54.52065 | 2025-06-06 05:06:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c1eda1c-6190-3c5f-b62c-f1249308f459 | -15.58889 | -59.35827 | 2025-06-06 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cd968b9-7117-3fb8-91e0-d87103f1e2c3 | -7.0169 | -44.5954 | 2025-06-06 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 7a9a04a1-8aa8-344b-9d69-d2e79e185075 | -9.79382 | -63.39236 | 2025-06-06 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5336c56e-7f03-3b00-a2cd-e0a590bff3ff | -13.5153 | -56.56736 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35df11cc-a94b-313e-b442-d305d1dfe785 | -11.38805 | -56.548 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff086d14-e43a-3361-93c2-984cab9a57ac | -10.29424 | -57.13777 | 2025-06-06 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076441ce-d959-35f9-bf37-c6781cc6d0d6 | -9.36884 | -63.50232 | 2025-06-06 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94d6b6ae-aa39-3e95-af2d-b5b5d847687e | -9.96416 | -64.97179 | 2025-06-06 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e650a2fa-babf-3b5b-8ff5-0e98e60a5ab9 | -11.52996 | -56.45696 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c92c846a-b453-3a6e-a3d3-3901e971f5e4 | -12.66721 | -58.22182 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acf57fa3-d0b4-395c-888d-f20ab5ea506b | -12.66779 | -58.21676 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7be405b5-27e4-3557-ba5c-839f41e42426 | -13.52295 | -56.57089 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e85fb42-aca9-3971-aa43-a8cf57868ac5 | -13.52224 | -56.56847 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e1f8cad-02be-3fbd-9dbf-88aa166233bd | -10.68961 | -57.65197 | 2025-06-06 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7123beb-1439-353c-a942-ff4f8b610e48 | -9.49206 | -63.23007 | 2025-06-06 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7928287-d01b-3877-9ea4-b9339622ea5a | -10.69596 | -57.65258 | 2025-06-06 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17db0b1d-e9b7-354f-87e2-8095fd93eb81 | -9.24789 | -63.28566 | 2025-06-06 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 849266fe-3b80-3d65-ae45-c972a09d8bae | -12.66507 | -58.22141 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26322270-d104-35cb-a94b-a2312a550c13 | -10.81786 | -56.95803 | 2025-06-06 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be67e314-ea3a-397a-854f-c9a9dcc5226a | -10.81717 | -56.96384 | 2025-06-06 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0ac7f5b-65da-3cc0-8a0c-b14fb0d80271 | -11.53753 | -56.45166 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2929236e-09d2-3654-97a7-65fc9564e9f6 | -13.51598 | -56.5605 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d4129d1-9f79-3310-a7d1-e560512125e0 | -13.52225 | -56.57745 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfa3a9e3-25ef-3f1c-9c09-92acfd781519 | -10.70352 | -57.64297 | 2025-06-06 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d20de97-4a75-3f3f-9445-3a395e58225d | -12.67134 | -58.22208 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84f47c76-8578-3bda-a303-029d380e74f6 | -11.37923 | -56.55169 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efc9b574-4af9-3f30-a5ec-118ea35009c6 | -13.51674 | -56.563 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2412349d-a3c6-3611-9c9e-5ac2c686da52 | -11.38604 | -56.55261 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 49a6dd63-a4c2-330a-b7a1-0dfdfeba5f52 | -10.2936 | -57.14328 | 2025-06-06 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e2bb7c2-e8b4-30e6-8b45-342a66605e4a | -11.38532 | -56.55888 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0e8deab5-524a-3969-bc36-4f2a656167fe | -9.24731 | -63.2897 | 2025-06-06 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcd28181-b9f7-3ef5-a97e-607e70522394 | -9.78992 | -63.39363 | 2025-06-06 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f15a76-e711-3432-bd68-048a40e65a8f | -13.51602 | -56.56983 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72ea9ff9-a063-31a2-bbe4-20073e311e31 | -13.52369 | -56.56402 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ac76dc1-a6d5-3456-983e-35578042e942 | -13.52157 | -56.57515 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50118e57-02bd-3ab5-bbd3-f8b28b925414 | -10.30075 | -58.44167 | 2025-06-06 05:55:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66e735be-5744-3c5c-9c79-df1919b7fbb0 | -13.52294 | -56.56153 | 2025-06-06 05:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f388e9ce-706c-317e-aa33-e7aa8392896a | -12.67349 | -58.2224 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 964b8e0b-f7ad-3ef5-8c42-ae65d2041699 | -11.38739 | -56.55417 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b060774d-1a01-33b0-bb98-363cc7d814a4 | -11.53681 | -56.4579 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e5124f9-8c53-3e30-980d-4443b117f9a0 | -12.66152 | -58.21606 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a0de598-283e-3ce7-9b4a-3adbc4fcd189 | -11.53806 | -56.45614 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc37ed7a-3b25-32d7-a33c-0adb453dbe25 | -10.29378 | -57.14082 | 2025-06-06 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb8854b-451e-3fb2-a888-df713f2c9520 | -12.52665 | -58.35812 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c088cba3-2093-30bf-8ddf-b053c2d200d0 | -11.38058 | -56.5532 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b8e0b48-fd21-32b2-95af-c17bf8a190d8 | -11.53069 | -56.4506 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ee32ce4-58ae-3c59-bcde-fd4cab67488e | -10.30008 | -57.14428 | 2025-06-06 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56613536-8aa7-3ef9-bc7c-42e082b6508d | -9.49262 | -63.22592 | 2025-06-06 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ea5da1e-b479-3ea3-bde5-2ebd27161119 | -12.53282 | -58.35915 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58c1ff94-3306-3e99-99ad-4998b1adfb0a | -11.3867 | -56.56053 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 146b14c0-186e-34c4-bb4c-7eff5b11f896 | -12.53338 | -58.35426 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 241d5fba-f99e-3e6c-b2b6-b9c8303488a2 | -9.49403 | -63.22698 | 2025-06-06 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c89a4c9-4bf6-3815-a3b1-2bde2c550ef2 | -11.53121 | -56.45518 | 2025-06-06 05:55:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19b10c20-42b9-332c-9c63-56b309e114dc | -12.66561 | -58.21633 | 2025-06-06 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7949c503-af5d-3235-b92e-6f5b95198582 | -9.79417 | -63.39432 | 2025-06-06 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55364c2a-5540-30f3-84a3-df568dcac1ba | -10.30073 | -57.13871 | 2025-06-06 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f01764b8-bb39-3d3e-b5dd-ac3e92b083f9 | -10.30724 | -57.13943 | 2025-06-06 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d5351c3-8365-37a8-9a84-8430214366e8 | -7.0169 | -44.5954 | 2025-06-06 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 1ed26f6f-b580-3fb1-a983-8bd05f461685 | -7.0166 | -44.6184 | 2025-06-06 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 33fb9f9f-9563-357b-88ed-fc505874445d | -7.0169 | -44.5954 | 2025-06-06 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| e36d4f4a-adc8-3301-b84c-d4a6f319e9e1 | -7.0166 | -44.6184 | 2025-06-06 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| d8270b46-1eb7-340a-bbe5-cfd0353eebff | -7.0169 | -44.5954 | 2025-06-06 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| b1dabf7d-49ae-3e83-8bd4-ce7f1fd6866c | -9.96327 | -64.97219 | 2025-06-06 06:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47e73588-3a65-3ed1-b27b-0ef4de37f391 | -10.49903 | -53.64675 | 2025-06-06 06:37:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e56eb6a7-c184-3a80-8fb7-d37d0828aa7a | -12.66015 | -58.21428 | 2025-06-06 06:37:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf206e96-77ca-3777-a059-f03d74e364f8 | -10.49698 | -53.65189 | 2025-06-06 06:37:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 0c5e1206-5316-353a-9620-65efd2ed5e13 | -11.38299 | -56.55505 | 2025-06-06 06:37:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 55c700e8-c595-3792-8095-992c4f1e21fd | -12.52897 | -58.35226 | 2025-06-06 06:37:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 230fbc48-556f-3f9a-935a-29f19be5e75a | -11.38793 | -56.55022 | 2025-06-06 06:37:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d4cbeca7-2c00-3b79-92aa-e0ba103f9840 | -10.49622 | -53.66787 | 2025-06-06 06:37:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a33c6bdc-202f-339e-9c00-7508bc4ba3d0 | -10.29345 | -57.1368 | 2025-06-06 06:37:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9370c456-95b9-3dde-b9d8-caf2fdb26064 | -7.0169 | -44.5954 | 2025-06-06 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |


[Clique aqui para ver as próximas entradas](README15.md)
