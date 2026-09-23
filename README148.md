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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d525352f-2954-363e-9a21-6325ffe159be | 1.5284 | -55.9439 | 2026-09-23 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 830f529b-78a1-3911-9477-7a4004d62695 | 1.4085 | -50.7451 | 2026-09-23 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a0d5bd0a-6302-3e30-b4e2-eda56b798b9e | -6.5449 | -44.8871 | 2026-09-23 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b957f018-53e8-3883-b001-51f6dc71f7b6 | -1.3933 | -48.9534 | 2026-09-23 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1f396929-9d5f-3a11-8f77-b38debdcb587 | 1.5102 | -55.885 | 2026-09-23 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fae819a2-cf32-3e36-911a-8f4793322aea | -6.5763 | -45.4968 | 2026-09-23 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e8778fa0-2a7b-31d4-83ce-765bd83ea7d8 | -1.4487 | -48.9526 | 2026-09-23 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c14a600c-4c25-3ef1-81de-63c6c135a92f | -6.5451 | -44.8643 | 2026-09-23 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 250f459b-2358-31b7-bc9c-0965400a6011 | 1.5468 | -55.8649 | 2026-09-23 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2c83d84a-44e0-318f-a11a-8ce9f811a8bf | -1.5858 | -54.4353 | 2026-09-23 16:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| abbe3228-f4f4-31cd-b89e-dbb008997584 | -6.5953 | -45.4727 | 2026-09-23 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 0d1ee1ba-c415-3787-8adc-0394d445e778 | -3.3367 | -57.8673 | 2026-09-23 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6d197f75-0aa6-3da1-9d89-4dae78b4f088 | 1.4453 | -50.7655 | 2026-09-23 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8adf8937-8465-3e27-bc4c-96a33130d782 | -2.7713 | -57.0229 | 2026-09-23 16:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cb6f98ff-67d2-3005-a610-3e2eb4f009aa | -1.4302 | -48.9529 | 2026-09-23 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ae17899c-fdfc-3802-9e05-1ecc9a307df1 | 1.4919 | -55.8852 | 2026-09-23 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| fe073eff-207e-30d2-9d2f-47fea2d64f63 | -1.0244 | -48.8087 | 2026-09-23 16:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 84228425-54d5-3628-9aff-abf32bbc7154 | -13.5 | -40.74 | 2026-09-23 16:15:00 | MSG-03 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 648d2e5c-1d0a-3f4a-a0e8-2c1323f79e81 | -11.65 | -43.49 | 2026-09-23 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb7712e-3677-35f4-b2ba-7c8ee27dd39d | -6.23 | -41.68 | 2026-09-23 16:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c111623-2417-3caf-a7f6-cbadccd279b3 | -6.23 | -41.72 | 2026-09-23 16:15:00 | MSG-03 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76e32765-c8c8-3373-b59e-f5f18ac8d0e3 | -10.02 | -50.19 | 2026-09-23 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec61f843-4468-315e-8d2a-4813a7a31071 | -6.23 | -41.63 | 2026-09-23 16:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e57071c-667c-35e5-8708-81098279d2cd | -1.0244 | -48.8087 | 2026-09-23 16:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1fa8f3a0-be01-3a7b-8764-bacafd064703 | -6.5442 | -44.9555 | 2026-09-23 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f38f5053-9cb2-36b2-99f7-c6a113bbdc46 | -1.2082 | -49.2539 | 2026-09-23 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 20d7dbc4-cda3-376a-98fc-9cbdaf0fabd2 | -1.4487 | -48.9526 | 2026-09-23 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a88c7dbf-df87-3462-ac95-8c672a352f8e | -1.4302 | -48.9529 | 2026-09-23 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a21e85e9-e7e9-3f45-baab-1699366ef30c | -1.0243 | -48.83 | 2026-09-23 16:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c0c6fb29-1a26-394a-968a-619d1b31cbf2 | -6.5763 | -45.4968 | 2026-09-23 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 7aa74d93-6822-362e-ad0a-4d1a3a7830a3 | -9.5542 | -47.9549 | 2026-09-23 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3ea3fa3a-d529-352b-a602-873c40ca497a | 1.5651 | -55.8844 | 2026-09-23 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 2c24b3e1-4a07-332a-b32c-eb4d045d8997 | -1.3373 | -49.2947 | 2026-09-23 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 916615ff-7085-3682-8e86-a992c71c1ffd | -6.5451 | -44.8643 | 2026-09-23 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4308f8ce-0e2c-3a8a-94ce-cd330275936f | -1.4302 | -48.9529 | 2026-09-23 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 61f57ac6-f0eb-3947-981a-1fa7d4bee1eb | -9.5542 | -47.9549 | 2026-09-23 16:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 1172d3d3-f5e7-3df4-a490-90a7edb22e7c | -1.4487 | -48.9526 | 2026-09-23 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 44363cf0-b45e-3d9a-8453-c523fde17199 | -1.0244 | -48.8087 | 2026-09-23 16:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d08e2b39-d9f2-32e0-bd25-0a8d77b66999 | 1.5469 | -55.8058 | 2026-09-23 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f4a9a1dc-5219-3813-b505-9a80be27dddd | 1.5651 | -55.9041 | 2026-09-23 16:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 198.1 |
| 33d15b2d-4d79-3522-98cf-14b6a55a0dd5 | -1.4487 | -48.9526 | 2026-09-23 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8c4cfd52-be44-32c8-913c-1f232f0d1959 | -1.0244 | -48.8087 | 2026-09-23 16:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 37e0b189-1a95-38d7-a41f-8e8289e71ce2 | -6.5763 | -45.4968 | 2026-09-23 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1b8a7578-4d98-32ee-947d-20d223e5a389 | -1.4302 | -48.9529 | 2026-09-23 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5a8bcba8-bb8b-3aea-8ba1-bbada1121115 | 1.5651 | -55.8844 | 2026-09-23 16:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 066e08ce-142e-3f44-a137-b35dd4b0cfab | -1.0243 | -48.83 | 2026-09-23 16:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9f4fe509-b0e3-393e-877d-1c779d41f478 | -1.4487 | -48.9526 | 2026-09-23 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6e123f9d-5bc7-3f43-ae58-a31e94dc7c51 | 1.5468 | -55.8846 | 2026-09-23 16:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0bbcfcb9-c1af-39eb-a007-37b01efe481c | -1.0244 | -48.8087 | 2026-09-23 16:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d340242e-f577-313d-933d-5248b2807e28 | -6.5442 | -44.9555 | 2026-09-23 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| aeb9fabd-d5f1-347c-b117-634a9f49c00e | -5.5648 | -60.2121 | 2026-09-23 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 44a8ef97-d959-34b4-8a54-8d07338d4d7e | -1.4302 | -48.9529 | 2026-09-23 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 63afe313-98a7-3667-96b2-73ce37c13af0 | -1.0244 | -48.8087 | 2026-09-23 17:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 01a43419-3698-3f6a-b971-19b9d9853e3a | 1.5468 | -55.8846 | 2026-09-23 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2f6a5693-ba6b-3a2e-9db6-0c5e173d245e | -9.8404 | -46.3911 | 2026-09-23 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8e9ffed0-5119-3673-91fb-30fdccc6cb98 | -1.3932 | -49.0387 | 2026-09-23 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8d23f56c-8ee4-37b5-bab1-9b8c0131dc07 | -1.4855 | -48.9947 | 2026-09-23 17:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 15ffccc6-7950-37bb-b0a2-b709792c4d6a | -0.803 | -48.6611 | 2026-09-23 17:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 26758d4d-e877-33f9-9f77-b94e5de6c573 | -2.5689 | -57.4163 | 2026-09-23 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| adfd180a-fd5c-3a3c-b5f3-a348e28f78aa | -5.5648 | -60.2121 | 2026-09-23 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 3306d42c-30cd-306d-aa2a-b8bc18f2f541 | -1.4671 | -48.995 | 2026-09-23 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f9da9fa7-43ab-3bda-92a1-4e64c348ca5b | 1.5651 | -55.9041 | 2026-09-23 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 094f063e-12a2-36ca-b57c-d2202c1db021 | -1.3747 | -49.039 | 2026-09-23 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a00902c9-c517-381a-9cc1-70dd070d6ec9 | -6.8784 | -58.9343 | 2026-09-23 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7b53b614-208d-3cad-b643-9fe97c179585 | 1.5468 | -55.8846 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ecd4030c-9579-39d8-8cc9-b22c0db26be3 | 1.5469 | -55.8452 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b7887f98-398e-39a9-8d44-bdb01c75f9fb | 1.5651 | -55.8844 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 0a4f0d12-aa0e-397c-95d5-d5fd07132326 | 1.51 | -56.0229 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b1009da7-bd99-3a31-98e2-94f433ea2d86 | 1.5652 | -55.845 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 3ebab25e-6339-344a-ace7-2a3bfdf678d0 | 1.5283 | -56.0227 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1546e92c-4e75-3ce0-98a0-cbd511f6d8e0 | -2.5872 | -57.416 | 2026-09-23 17:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 62796188-1b61-339f-af1f-5cdf1beb918d | -2.6235 | -57.532 | 2026-09-23 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 613b4b53-d0cb-37dd-b0c8-5cfce4ab25e8 | 1.5651 | -55.9041 | 2026-09-23 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| d96cd2a7-d63b-3bcb-a8b6-ebbd78bc9abe | 2.4397 | -50.9344 | 2026-09-23 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 90024d76-00ad-3f5d-8def-585c7170bd4c | -1.4302 | -48.9529 | 2026-09-23 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ce341a03-ac71-33bb-820d-a653429ae846 | 1.9791 | -50.9441 | 2026-09-23 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e0eead82-fb3f-36b5-883c-d4dd826e7c25 | -5.3157 | -49.051 | 2026-09-23 17:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6435e2ea-ff39-3a6a-a899-db00f0538dcb | -1.4487 | -48.9526 | 2026-09-23 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |


