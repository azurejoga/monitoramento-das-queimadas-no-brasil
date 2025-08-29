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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a4b6c0e-1722-398a-b9b9-2592c01bde0e | -8.17632 | -61.37563 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2639bd3a-79ab-31d6-9a9e-7564cb9992a6 | -7.55895 | -63.84525 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53759c4-c9d8-3e76-b59f-b07ac4578a56 | -9.11228 | -65.74271 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05423e89-7a89-3f8b-8bf8-432d789e5cae | -8.89857 | -60.56523 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86b332cc-1b03-3a22-858f-a43c604953df | -9.20279 | -59.53982 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dceb17e9-619d-395d-aac6-1a30ffb381e4 | -11.37569 | -63.25971 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8452be71-ca73-3fae-94c7-4cb3533c0fdf | -9.77387 | -64.24983 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 076aa2ee-8755-3973-8756-68bad956e862 | -14.50375 | -52.07102 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a40db2f2-17f3-3ca6-b337-1f84413cccd4 | -9.31616 | -57.69632 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09cfe3cd-6dff-3bbb-ba1b-e18313876e56 | -9.04762 | -65.74178 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d002d88-624f-301c-9d2e-b47f536ee031 | -10.36504 | -57.7928 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc5df42-2fdf-31ca-b821-ff7809a65fe4 | -8.7695 | -70.57826 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe01e89-4037-3e62-ba6c-c2befb1154bd | -10.3215 | -62.62012 | 2025-08-29 05:29:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39720f96-155d-35d9-ba0c-e3a176fca390 | -11.32099 | -55.21826 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 326339a1-635c-342d-acf9-689519fc9f65 | -9.54437 | -65.69398 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 187b3142-7168-3266-9dbc-c0eec23425d5 | -8.25293 | -61.44991 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ae24da1-4d39-3727-9c3c-5e7492fb72e2 | -8.44428 | -70.14287 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e89a4da-afba-323b-9728-1c40901b9fd0 | -9.10975 | -65.7802 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c84756b-d269-346b-aa97-a9eaa7e14477 | -10.15184 | -64.24872 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8105e409-2d7d-3e0f-954b-0d3c4aba7c91 | -14.50633 | -52.0728 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b659fa8-4334-362e-b55e-d12d01923318 | -10.46844 | -57.9677 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ecb3872-0694-36d8-a6ae-1c9922a20ecb | -10.54229 | -67.67708 | 2025-08-29 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81a2a11c-b418-3936-8adf-b41174fe840f | -10.36345 | -57.80391 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8c6d41c-8e3a-353c-924e-1db3d199ef16 | -9.114 | -65.7767 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fa8bccc-166e-31aa-a7a8-432669a1d835 | -9.54083 | -65.6934 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 69215284-a5c2-3c99-b230-d9bbda5e660e | -11.2187 | -55.06332 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 336bf568-b432-3ee7-ba60-ee94628630dc | -10.17605 | -68.15945 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbaafa97-3a9c-386e-bbd5-522f012a1cc6 | -7.62694 | -60.84889 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6fdb12c-0326-3428-a681-af81000d566f | -7.5392 | -63.86055 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fed4d6b-2ccf-36f0-8706-23b33691419f | -9.15565 | -65.78244 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7e4804cd-12e0-3314-8a9e-48ce996f5f88 | -9.12269 | -65.79082 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa0248c6-8955-3b29-9588-121f3931d174 | -10.2564 | -64.49893 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a80f190b-a58a-332f-9833-3f14428cab0d | -8.81004 | -69.30273 | 2025-08-29 05:29:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 896b9474-d9d6-36c6-b46d-5983528dccc3 | -11.36631 | -63.27618 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb7aa8b-6c83-33ec-8ee3-01a602899a69 | -9.64845 | -64.95518 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c34a506f-a4ef-390a-9529-939c109ab623 | -9.41246 | -60.5743 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb0a4385-be3d-3a57-bcd1-d5fb95fd1ff7 | -9.18215 | -65.79956 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c729ad62-05af-3e5b-9fc3-af2b6e1109ee | -8.87874 | -60.74438 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 058c4242-823f-3623-abeb-1a6fd2a8f600 | -9.15096 | -62.35527 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82e15634-8063-338d-99e5-febef3f6c08a | -9.15002 | -59.5892 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7af3fc41-3b53-3cae-8bfd-b7f1d850f040 | -10.44811 | -57.96522 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bdc8565-4cf7-35f5-8e0d-5dfcf9791c14 | -9.17212 | -65.79365 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c24d2e37-5da8-31c3-8ce7-a4f14a961dc7 | -10.22592 | -58.22361 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08806307-551b-3faf-866b-fbbabe446de9 | -8.12774 | -61.21095 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c292ff8c-8d63-3e93-baec-be04a0a9dce3 | -8.69182 | -62.46829 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a852d04-934c-3991-9a4d-5f324ec193a3 | -9.67441 | -64.99055 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ebf01d2-d377-3750-8bb7-d06cd122afb7 | -9.11468 | -65.77261 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49a91022-1c67-308a-9ab3-c9badd94c5b4 | -9.73089 | -64.90308 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68daf25c-54e0-3f2d-bc73-3f0dee7a5598 | -8.94609 | -65.95478 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5faae4b9-f2b2-363d-be6e-59b1ef812b4f | -10.85494 | -60.8156 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7487c003-a420-34cb-accd-c12cd3a076e4 | -10.46936 | -57.96447 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c74f92d-20a3-3eef-aebb-b94960c527b0 | -9.15922 | -65.78304 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f801c34e-a86f-3f12-95ad-f80f1ba5309b | -9.31516 | -57.70356 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34b2e59-abf3-3858-aaae-db63be8cbb86 | -10.03282 | -67.8292 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cfc3247-8391-38ac-839f-e1a8c5866eb3 | -12.6654 | -60.26013 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1670f02-e202-3e68-ba4d-9b033a4c6f7c | -9.23457 | -59.78317 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf0c49b-b4e0-3a54-a394-54c43ac99026 | -9.78117 | -64.24734 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 850ae215-dbe5-3679-8d90-23cd31ec4cf9 | -9.12249 | -65.76976 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d141e538-9f4e-3ba5-ba44-cd10b37a588b | -11.92514 | -63.95124 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a9607a9-7bc4-3fe6-b27d-bebd12dccd68 | -8.23064 | -61.46103 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ddb68cc-f375-33d7-8640-80c95d611e8d | -13.01985 | -56.91969 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57f53f70-8db0-327b-ae0d-737fefc7d1f5 | -9.78395 | -64.2515 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 805789f2-ccff-38bc-8b87-f93841bd26e5 | -14.33749 | -53.28463 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 50acea18-d54e-37e9-8272-7ed395d55a29 | -9.54016 | -65.69743 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 652bb3df-10d5-3618-a63f-c8b07ddcc00a | -9.18278 | -60.86315 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f2e5b67-1bbb-3558-8e09-c1a0d373b5ac | -13.37105 | -51.76141 | 2025-08-29 05:29:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f48318e-b5f6-3828-af63-bd860c4ef570 | -9.52455 | -60.52768 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3fafe79-77a8-34fc-ad83-2b3f50216a79 | -9.45786 | -60.56892 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f92e5f0e-f7ce-376f-a0a7-14e7fef30599 | -9.15833 | -59.53432 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 857d791e-2aab-34da-8acd-a000fd25ce47 | -12.99519 | -56.89721 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7398ee42-29d3-362c-b694-5f02f3313726 | -8.17407 | -61.36795 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a356802b-8405-386b-82b3-f11f0cdcb9cf | -7.56673 | -63.86131 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e99654fa-046e-3c9a-bd27-1b87754b6871 | -9.10429 | -61.42686 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b8e1c7-8a04-3b5d-a4ca-761374a1950e | -6.89159 | -64.24242 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6af0873c-b448-340b-9cb0-52e219d58f81 | -9.11178 | -65.76791 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f60707ee-b900-380b-831b-fbadb2488157 | -10.34773 | -59.18895 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90c3785f-2329-3845-a9f1-fbe38ec41fd1 | -9.31142 | -57.69975 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67e889e1-26b5-39e3-8dbf-964482c604ec | -8.17912 | -61.37973 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afaa5246-7394-32df-9af5-d4357241a868 | -10.35603 | -64.47063 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d592b35b-1b71-3baa-93ec-da56731e4f15 | -9.78175 | -64.24372 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6df21106-588d-3058-98e0-6f96797581ad | -8.18583 | -61.38077 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1aaa65c6-b67f-3ce9-b8db-a386553b2176 | -9.41652 | -60.57096 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34f30a64-eef7-39c6-96fc-5385ed0645ff | -9.10821 | -65.76732 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e5804d93-0593-3d2c-abcc-11dac0a79e21 | -10.7154 | -65.03927 | 2025-08-29 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd032b9f-fb5a-3878-b2e5-85c0ca8990da | -8.39407 | -70.76537 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ffb8fc-7896-3c65-94a5-aec018c6d1d3 | -9.15859 | -59.53747 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c926c0db-80fe-3317-b4ac-991cb5ef8851 | -9.30063 | -56.81757 | 2025-08-29 05:29:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b7e0f70-38cb-346d-8974-e2d1ada42394 | -9.0532 | -65.73007 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32a6895e-8197-3ba1-8d7b-ea3d7c7e6e3b | -7.54153 | -63.84613 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c18b19d1-25d8-38a7-9e1d-c1903e5030c4 | -9.91093 | -62.14056 | 2025-08-29 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 480cc618-802b-35cf-90cc-a5213cea18e1 | -7.47359 | -61.33695 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 352ea428-7259-37f4-88f3-f2140600b92c | -10.44862 | -57.96171 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaac488f-94cc-3e59-b81a-9f69b19dbc59 | -7.56232 | -63.84579 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9892d24b-4baa-39ef-a303-7abe80ab033c | -11.37017 | -63.27321 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b659a09d-4bdf-30e7-803e-a44abd542bbf | -10.07242 | -62.88846 | 2025-08-29 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa28b24c-1133-32ce-8b5f-16ed43461f57 | -8.25195 | -61.50073 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd732e18-132e-339f-bd71-bf8849c7fddb | -9.10515 | -65.74154 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 087e09ad-91d1-34fd-99b2-cf9a16bc08d9 | -9.15301 | -59.57581 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e3d2528-2c2d-3b1e-8ed3-8028084a508f | -9.52396 | -60.53154 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ae19329-4db0-321a-a5a9-9b9f9b6f256a | -9.13138 | -65.80497 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README84.md)
