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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9de5ca09-71d0-3b34-b5e9-0ec9e5d64afe | -11.46135 | -44.5673 | 2026-08-07 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe62943-c8df-3507-b130-b95c01e0e263 | -11.19478 | -54.84945 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9a51fbe-1da5-330a-b368-8fc3383f9433 | -11.14211 | -44.47688 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 933a1cbf-bb76-3b05-99c6-04dc809ad025 | -13.96229 | -47.36712 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea5f274c-ad9e-3111-9249-adb1656c68a5 | -13.93515 | -47.35604 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83e486fc-f978-3aaf-bde5-45e0129e8f64 | -11.1478 | -54.91055 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af6889ac-6f00-35ad-a2ca-3652a9993e39 | -6.55364 | -56.24956 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32ed0f0c-be30-3773-bc37-1634399a3536 | -6.10047 | -55.81838 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e56e8104-693e-336d-b34a-98897db9d6dc | -12.55704 | -46.93864 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44b2c6b4-7fed-34f5-b7e9-00af47734982 | -11.14519 | -44.47843 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 31dc65d0-d559-32a6-991f-22ce27729ae8 | -6.72229 | -58.92872 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21d92938-0648-3313-b422-a1ec223a7166 | -6.62176 | -56.37066 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21953177-996d-316a-8b5d-1fa1b3e34bb0 | -10.935 | -50.28435 | 2026-08-07 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0444a9-2421-35ad-a2c8-19a9bd2ca6a2 | -7.75241 | -45.02725 | 2026-08-07 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1db7ff8-abbe-346a-b900-52364fb9601d | -12.00566 | -49.28064 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc9c176f-c667-3831-aa3f-42302842249d | -6.72148 | -58.93365 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aee44243-a19f-3893-8ac3-e3e79b9d246c | -6.71759 | -58.93299 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1285c475-309c-390a-99ca-4af0697766bd | -6.53722 | -55.14964 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804271d7-0777-3891-bbcb-b94a127d1478 | -12.55569 | -46.94962 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2476fb7-8bff-3670-adcc-5b9d420344da | -6.86236 | -58.9369 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c8175758-7c13-3eb8-9892-104507de4694 | -6.54357 | -56.55051 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 620c6f48-3155-322b-b8a1-2f68711a22c6 | -13.77058 | -47.18393 | 2026-08-07 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1e21f59-bcce-31a4-81cc-97c9583748a4 | -6.64467 | -56.4241 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a41ebaa-3e39-39c3-8f74-2ed3c1ca06f5 | -14.4274 | -45.66053 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 702520bb-4485-3be4-a9fd-700d2493cd26 | -6.5411 | -55.14668 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24bc38e8-f761-3f19-b84f-7ce8b82b3ac7 | -11.15939 | -54.85824 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae01967a-2430-3ddb-8602-b5f883a220d9 | -6.63424 | -56.38024 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 491c65e0-c56d-3be0-9e95-aa9b99d3a1f8 | -6.64428 | -56.40486 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3619969-e816-3dbf-afdf-4618a3ac3c1d | -6.23097 | -55.6182 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ba5ab4a-6fd4-3cc6-9c38-2071b631def5 | -6.10106 | -55.81475 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7ce533e-9a61-39ab-be1b-9505ae7f3f69 | -12.33022 | -53.1689 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 870ac25d-33dd-3f72-9c6e-e4b12ec74acc | -12.14016 | -48.26346 | 2026-08-07 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8deddede-1867-397d-ad01-0c004cce8e8f | -6.5379 | -56.54185 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79f9d2f8-8b47-3d8e-ade7-8d8b6e0b5922 | -11.13453 | -54.90844 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73967911-e414-38d8-bd86-29f54c922ccf | -11.18372 | -54.85491 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e237b0d-8313-360d-b3b5-7bb352d812dc | -11.1279 | -54.90739 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5dd47f-093a-371c-ba72-aa5450a23175 | -6.60711 | -56.35296 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ab0e69-bfa1-3577-8dd6-03e1bd444257 | -8.08125 | -45.58248 | 2026-08-07 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fbb9ba2-7917-3969-9bd6-875773829561 | -6.6475 | -56.42837 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8788e328-19de-3b9c-b11d-33a4a2a54b08 | -11.08122 | -47.79723 | 2026-08-07 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c0f46be-fe84-3d5f-b03d-9e939f34fe38 | -12.33431 | -53.16545 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8af453-b15d-36ab-b862-4ceaf8698fb3 | -13.94026 | -47.35698 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 955893f0-1170-372e-a53e-82d172214053 | -7.09292 | -46.55156 | 2026-08-07 05:04:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36b25acb-dc7b-3c71-927d-68c9b282e867 | -13.77137 | -47.17723 | 2026-08-07 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a035d76f-b9c9-3f0e-a46b-d1d1a03a613b | -12.57672 | -46.90782 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 140569af-2962-388f-a592-f4eb0cf853ce | -7.08878 | -46.5453 | 2026-08-07 05:04:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cef96023-deb3-38ea-98b6-8d4aa9e329d9 | -6.10443 | -55.8153 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35a9bf2d-7d2a-3b74-b064-4fd6454ebcf8 | -12.34795 | -48.20629 | 2026-08-07 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aee5716-8647-3a1b-8d74-c12b9b8a2323 | -6.64527 | -56.4204 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6af121db-f7ec-3bcf-8e00-c29ccba60089 | -11.18815 | -54.84838 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c111e8f-1a3b-375b-8fc4-5438db21d3fd | -11.14448 | -54.91002 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc93ef1c-b751-3b4a-9d42-d0edf37ce884 | -6.15711 | -56.14127 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93bc7370-d3cf-3cd7-aff5-c0bc045429b3 | -6.6477 | -56.40543 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a50ec12b-3cc3-365c-b21d-06a6b0de2c5d | -6.54963 | -56.25269 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c2d7de1-365e-33bb-81f7-eecafe50b0c4 | -14.42598 | -45.67308 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5570abee-d38f-3fa7-b1a5-7c7bf26d18fb | -12.33373 | -53.16943 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfd0366d-3b99-3ca4-bb16-b84c44458ceb | -11.13785 | -54.90897 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce3a78a8-b806-394f-b89a-c3716de9f8d2 | -6.62519 | -56.37116 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b38b38ee-b7e8-3b43-8edb-e7e2131a81e4 | -5.98715 | -52.15516 | 2026-08-07 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 345dbd8f-7b90-39e6-aad0-806b2449efea | -6.63966 | -56.41165 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e88062da-e260-30a3-896a-7b7ea838e8d5 | -10.12387 | -48.91399 | 2026-08-07 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a757992-f50d-3a58-8ee5-698c87435811 | -6.62458 | -56.37488 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbe1896f-1221-3bee-ad7a-2c7b714652b4 | -6.86624 | -58.93756 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d8ce034-ddf1-37e7-8488-269ed4658e71 | -6.65113 | -56.40599 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0dd2767-373b-3aab-97eb-3593f6d3f68b | -12.57712 | -46.90456 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04dfaafe-931a-3622-a524-aeadfc105591 | -11.18151 | -54.84732 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dfa344d-242f-32fe-8705-7aa55aad2f4d | -6.8598 | -46.00215 | 2026-08-07 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5413fed5-0577-339b-89cb-47782dcc1dfa | -13.69045 | -51.97299 | 2026-08-07 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d873cd27-7ba5-39f7-894f-f625c383e9f0 | -13.42134 | -57.04186 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f77681a5-4231-3577-a191-b90ad2cefd10 | -19.71005 | -48.13421 | 2026-08-07 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a8afd6d-42c2-3271-b906-6ee7186fbbc6 | -13.057 | -60.65948 | 2026-08-07 05:06:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d350bbb4-0765-3e06-9370-c4b5f8bd577c | -14.33726 | -54.93196 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ffca68e-1b8b-3188-9fd6-f425cae31c50 | -15.0774 | -53.58838 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f5fdd67-3058-302f-b86c-8f42968a2903 | -13.6272 | -54.67445 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2937e1fb-7fa3-31d2-a4e9-b5470e77975a | -15.10511 | -53.59586 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 497a123a-6934-3961-bbab-6a9f3a487113 | -14.3278 | -54.97165 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| beef100c-b1dd-37ff-baab-084770630804 | -13.42976 | -57.03219 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f23a07b8-8b9c-341b-9d69-51b4fbde285e | -15.10924 | -53.59231 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80e42ce5-96d8-321b-af1d-5c723970e262 | -13.62384 | -54.67391 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 50d50c26-0b65-3813-9b37-bb11e549da42 | -14.34173 | -54.92517 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86a404fd-692d-391c-b8ff-1d44520569c9 | -17.47455 | -53.32269 | 2026-08-07 05:06:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 528c273a-06ed-31e5-a455-6d8693f9061c | -13.43093 | -57.025 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a21e7f25-d48a-3a45-a69c-3b2231ff3b42 | -15.07326 | -53.59101 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a58fd1e4-a937-32d0-8181-31d9013c4e8a | -17.85288 | -49.61344 | 2026-08-07 05:06:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b68892c5-5787-3c0f-9ef7-51a6108058a2 | -15.08446 | -53.58853 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 15c907c9-1ff1-37c4-9d0f-b49cd2cf8da3 | -16.49019 | -52.72237 | 2026-08-07 05:06:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d49a123-87c9-380f-a01c-98ec7a767b6a | -13.41975 | -57.03048 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 174fe611-c1f3-3f9e-9980-f6f2a074e780 | -19.70969 | -48.13757 | 2026-08-07 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba5b5cc3-5846-3ac5-9481-2c1c5875dc2b | -16.74953 | -47.58456 | 2026-08-07 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 440bd9b6-a6e1-32f3-a728-f794ce3f3c4e | -14.35348 | -54.91577 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48cf101a-4020-3498-8fff-7cc69819fc79 | -13.83782 | -53.7157 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d8f9a1d-85db-3dd5-af8c-591b3f71fc87 | -15.09646 | -52.76483 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73f5c94e-e7c5-356b-b420-1e7ce17586e6 | -15.10983 | -53.5882 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7f8dad-2635-3c78-9943-39f75c9e9ed5 | -13.05764 | -60.65805 | 2026-08-07 05:06:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea30da5e-00f9-304e-82bf-ca031717c438 | -15.07325 | -53.59193 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef4ebd47-4abc-3ae4-bd03-6cec36bcfc17 | -17.47824 | -53.32319 | 2026-08-07 05:06:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b41502-f22b-3692-8f40-14a62475c9cd | -13.42091 | -57.0233 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b97a7159-81b9-31f5-903a-f679ca52eb34 | -14.33781 | -54.92829 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35fd625b-078f-38c3-be7c-96ad59d281b5 | -13.42526 | -57.03881 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2de70b43-9841-3be1-9812-2bf5cd5fd29e | -19.99674 | -43.97704 | 2026-08-07 05:06:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |


[Clique aqui para ver as próximas entradas](README24.md)
