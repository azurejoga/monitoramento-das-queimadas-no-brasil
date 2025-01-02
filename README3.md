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
| a9460141-5c8d-32c2-b7f2-de6babd1ec2e | -5.99429 | -43.57801 | 2025-01-02 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f70758fe-7ceb-3207-b7e2-946fb8ff1a6f | -4.92792 | -48.56599 | 2025-01-02 04:46:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0008cd02-7235-3e2b-898a-9a92f283f2fd | -9.50333 | -40.32204 | 2025-01-02 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ca8571b2-e503-304f-8e66-537e8e4650a6 | -9.50573 | -40.32129 | 2025-01-02 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f226fc6-1a3e-3770-ac20-96a02da8ed56 | -5.99298 | -43.57912 | 2025-01-02 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a47772ae-b362-31d5-bf80-713795e687c7 | -5.9937 | -43.57402 | 2025-01-02 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09add22-ef13-3be1-9975-ff3a057b5702 | -9.49947 | -40.32046 | 2025-01-02 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 96bc7f9b-dfce-3b64-961d-7538dff7af98 | -16.29866 | -56.83877 | 2025-01-02 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 760871cc-1182-3f11-b9b8-11589b6e8d2a | -24.24368 | -50.74043 | 2025-01-02 04:50:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1f6fede-d6ae-3e9f-b86f-5e94055c71af | -22.67715 | -42.85642 | 2025-01-02 04:50:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 090dacca-a153-3fd7-a6bc-85fbf08680b2 | -20.99602 | -51.79182 | 2025-01-02 04:50:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa666298-3721-3db6-9e0b-85a8964dfe14 | -19.77631 | -55.42762 | 2025-01-02 04:50:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2ab65cd0-333e-3482-9db0-1a39285977d7 | -22.67562 | -42.85159 | 2025-01-02 04:50:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3e68d1b3-0fa6-3bb0-b7f8-984cb5fbe9cb | -18.14756 | -54.26584 | 2025-01-02 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9126bce-c54a-3e09-bea4-161f89534f6e | -19.02349 | -57.62345 | 2025-01-02 04:50:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cef20b1d-606b-32d5-ab32-aab13d1ea01e | -22.67758 | -42.85126 | 2025-01-02 04:50:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| daa0a248-e619-3b1e-89e3-33cb1b50a7a4 | -19.3392 | -54.16965 | 2025-01-02 04:50:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59e41451-3088-3539-8fbc-35f6e122d18f | -20.47638 | -53.6758 | 2025-01-02 04:50:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91bfa3d6-b7e1-3441-ac66-f74d4b941d58 | 2.84766 | -60.08217 | 2025-01-02 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3d28e81-f416-3c54-b178-fc682d4db9db | -1.7231 | -53.23941 | 2025-01-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d0dfcc3-2cb4-30d1-a218-9c823c847e81 | -3.21298 | -53.01899 | 2025-01-02 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a8341e5-d0f0-3513-9d08-bfb987b9631e | -1.72605 | -53.24405 | 2025-01-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22c4170-6ad6-3dc0-9b48-aa0e3cc65902 | -1.29207 | -52.10289 | 2025-01-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d411b144-8506-376f-918d-d149a704166b | -1.45355 | -52.63945 | 2025-01-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba8aeaa-a82e-3409-a073-b4ec520523d4 | -1.72246 | -53.2435 | 2025-01-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad41cf6d-46b6-35a2-9ae5-1c0931780390 | -2.86213 | -52.56399 | 2025-01-02 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e361b3bd-889e-3c48-9555-3c9a0ea83e2c | -10.0804 | -64.92193 | 2025-01-02 05:10:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68feadf3-879d-3c24-9786-f81726fb6f9c | -12.26144 | -64.35452 | 2025-01-02 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cfcfc02-59fd-3e98-9aee-408eb0fced7b | -12.34024 | -63.69923 | 2025-01-02 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ad11a7d-9593-362c-bab0-f8392c956af6 | -9.23787 | -60.33732 | 2025-01-02 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a5b3d03-7117-3adc-8a57-0e7c15b57169 | -19.02194 | -57.622 | 2025-01-02 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 066dc6d3-580b-3836-b402-cc3ab8df14ab | -19.33828 | -54.16956 | 2025-01-02 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb9bb56-de51-36fc-91a3-1374a43fde6c | -16.29916 | -56.84026 | 2025-01-02 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 72f030f5-f3f4-343f-a6c8-014405e4005a | -18.14496 | -54.26573 | 2025-01-02 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f8417db-aa52-34a6-afca-6bc2a4cff1be | -19.33775 | -54.17374 | 2025-01-02 05:12:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0181397a-3f85-3c50-8e12-22f9b3fa91a1 | -2.94065 | -39.90066 | 2025-01-02 05:14:00 | AQUA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a72588df-b092-34a5-b53c-5b61d8f3c29d | -5.98489 | -43.57372 | 2025-01-02 05:16:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c4b7c1c-e1c5-38a3-93e8-c5c7eb0187b4 | -10.60036 | -44.3253 | 2025-01-02 05:16:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5ea223c3-8e4c-3428-a3b3-09de1b273107 | -10.59903 | -44.3342 | 2025-01-02 05:16:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8d3f9a00-5b64-3256-a9f8-11855c35a6ed | -10.6017 | -44.31639 | 2025-01-02 05:16:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 450f5fce-d463-35e8-9eab-d2fb05e583de | -10.59288 | -44.31507 | 2025-01-02 05:16:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 65dbf6bd-a393-3837-83d1-b84933222cbb | -10.59155 | -44.32397 | 2025-01-02 05:16:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6faa77ac-6425-395c-a9d1-e5ab58d110f6 | -20.22129 | -40.24178 | 2025-01-02 05:20:00 | AQUA_M-M | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |


