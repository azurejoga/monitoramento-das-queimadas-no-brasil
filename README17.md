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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24b44df4-6c37-3aee-8851-effff33f42f6 | -11.82502 | -48.76257 | 2024-10-29 01:28:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0841f742-49d3-34c5-992b-1c02be9c7777 | -8.48464 | -49.45213 | 2024-10-29 01:28:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 210fc7ed-6327-3b43-95fb-88ff12a0e27a | -12.35211 | -49.93858 | 2024-10-29 01:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 70f0664d-a477-3765-a591-c191f5d53dd6 | -12.34914 | -49.92084 | 2024-10-29 01:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6c39ca10-51bd-38a4-bfad-cbc4defb70f4 | -12.3475 | -49.94501 | 2024-10-29 01:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 6e44dff9-d18a-39ba-809b-5c200ba9a535 | -12.34467 | -49.92728 | 2024-10-29 01:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| fe2c824b-7741-3074-bc7d-c2a546e23aad | -12.34183 | -49.90956 | 2024-10-29 01:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 94058383-6aa8-3495-8d10-d7e0deb3c9d2 | -12.09711 | -52.49293 | 2024-10-29 01:28:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 2b1409ef-0829-3f59-a3de-df3953f5ce82 | -12.09535 | -52.48121 | 2024-10-29 01:28:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 7838f4d4-76dd-3239-b0ed-b5dcbdf306d1 | -11.22106 | -51.65075 | 2024-10-29 01:28:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9b2fafbb-1b85-3790-b68d-3155fd6719e1 | -11.04932 | -51.73256 | 2024-10-29 01:28:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b4208ab7-f3f6-37e0-92a7-a540fde93f73 | -13.25827 | -53.93021 | 2024-10-29 01:28:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c6b240e8-e572-301e-92c0-bd00da415cdf | -13.25686 | -53.9206 | 2024-10-29 01:28:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc30082e-0b7d-314c-a55c-5e2f8b02c8da | -13.24964 | -53.92798 | 2024-10-29 01:28:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1602e0d0-9ed0-3a6f-ab9d-e0e2cc89da56 | -9.48168 | -54.52818 | 2024-10-29 01:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| be9f0fee-2a01-3ccd-a37b-fd9cba8fc16b | -9.47247 | -54.52951 | 2024-10-29 01:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ed3f4550-437b-38ad-a768-eb2f3d443a60 | -10.41831 | -55.07525 | 2024-10-29 01:28:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4a49e172-eb1c-323a-9f9a-101153b47271 | -10.03404 | -54.32812 | 2024-10-29 01:28:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c790e24-ad90-3833-8f33-d5b1ed0c4262 | -11.89991 | -54.80192 | 2024-10-29 01:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4a9c8c50-4e85-3d43-9bd5-3c9c5a53d2f3 | -11.76425 | -55.4669 | 2024-10-29 01:28:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e54509c3-7c9b-3a46-a315-6e21f0ce5286 | -11.76299 | -55.45789 | 2024-10-29 01:28:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fa91c365-de7f-357d-9540-9f320e8c5db0 | -11.55918 | -54.48034 | 2024-10-29 01:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4688bd9-dade-33eb-8599-d36a7ac50b6f | -11.55783 | -54.47089 | 2024-10-29 01:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4b18cc9b-708f-391b-aaf1-8bc3c0fb4d31 | -11.3478 | -54.48597 | 2024-10-29 01:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18bc73bd-34fb-3aaa-996c-ea41051c6fce | -11.3237 | -55.21521 | 2024-10-29 01:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 291f27a1-1e94-392d-a855-e8c0f93fd5d7 | -12.50182 | -54.43315 | 2024-10-29 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4f360321-7d64-37a0-81a7-1e61104ea811 | -12.09995 | -56.828 | 2024-10-29 01:28:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b9a9c3a-2cdd-3d43-8ff8-3fd9af067f6e | -11.86865 | -56.88843 | 2024-10-29 01:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 552c2174-4295-3926-b0af-4d0c8a1761b4 | -11.86739 | -56.87915 | 2024-10-29 01:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ef6e595-0707-3b45-b8e0-8cfdcb823c96 | -11.17042 | -56.29911 | 2024-10-29 01:28:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24a7003a-9f6d-3ffc-a2cb-dc9d7112b844 | -11.16918 | -56.29013 | 2024-10-29 01:28:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3acff619-9b63-3e56-a756-3f1c9bb0c22c | -11.13956 | -55.5469 | 2024-10-29 01:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 9a3f5183-e5fc-3ed5-bb2f-81ed4183098d | -11.13829 | -55.5379 | 2024-10-29 01:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 03840991-9980-312c-b25b-f35cd786f864 | -11.13702 | -55.5289 | 2024-10-29 01:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 8d5b33ef-cea9-3e72-91f6-d0a38d60a230 | -12.78171 | -57.04143 | 2024-10-29 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 59998edf-dcb2-349c-a5dc-365f67b924bb | -12.3351 | -56.86737 | 2024-10-29 01:28:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b318db8-eebc-3bfa-bb2a-01315e20e432 | -9.36642 | -56.83687 | 2024-10-29 01:28:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 04d6e6fa-4cd7-30b5-833f-905adb92dff1 | -9.7452 | -56.97836 | 2024-10-29 01:28:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 56e582a0-d23c-3a61-a1b1-ba3817915002 | -10.85158 | -56.92295 | 2024-10-29 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9c8d27e7-2ecc-3bc3-a286-e225aadcc684 | -10.85034 | -56.91382 | 2024-10-29 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 596ed48c-7ac7-3c91-b21d-7878e109a838 | -12.3033 | -58.15314 | 2024-10-29 01:28:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c73c24e5-b371-3f3e-af67-463059ccb7c2 | -3.3061 | -47.20069 | 2024-10-29 01:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 3c1461da-f669-38da-9c67-4a6c09ff348c | -3.30588 | -47.20576 | 2024-10-29 01:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 30858031-d045-3e1d-8fed-a3aed8332676 | -2.18124 | -47.9447 | 2024-10-29 01:30:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 269b4314-f1c2-30cb-80fb-b95d449acbc6 | -2.17751 | -47.95033 | 2024-10-29 01:30:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ea616816-9f6c-3143-8d84-b013f69b7169 | -2.43706 | -48.65126 | 2024-10-29 01:30:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| fe00b5fc-b9ee-3343-86a0-78d40f78f835 | -2.42857 | -48.65776 | 2024-10-29 01:30:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 92fcc97f-dc55-3e1c-84a9-12cb0cde6230 | -2.50983 | -47.46212 | 2024-10-29 01:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c2e6b411-5f24-37e1-bcbd-57fccdbc900d | -2.50899 | -47.46914 | 2024-10-29 01:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d0edcbf3-7b6e-39c9-a616-130a1783d0e4 | -3.32529 | -50.31935 | 2024-10-29 01:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 305a4da5-e3a2-328a-9789-696d8c4e2322 | -3.3219 | -50.29598 | 2024-10-29 01:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 20c73994-62c2-3d71-a329-77d4619e9239 | -3.31742 | -50.31382 | 2024-10-29 01:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 70049bbe-4b2b-3129-b211-5b36d80760b3 | -3.31382 | -50.2904 | 2024-10-29 01:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c3cdfca8-52f9-3765-9f3d-76adff79e41d | -3.18855 | -50.39385 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9fae0c05-6104-3605-9612-85a8b3c3e978 | -3.17478 | -50.39591 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 54c639f8-367c-33e4-a50b-cc55d8596eb6 | -3.17126 | -50.3726 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 379c70ec-160e-3064-b566-a4c88af4a349 | -3.05219 | -50.42607 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 234c7d05-66f9-3a0f-b546-d41e36891fe3 | -3.04455 | -50.42154 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6730893f-c8da-3797-bc7f-4cb6fb682b36 | -3.0384 | -50.42806 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 059ef7fe-c0ce-3e23-bceb-8f7774f55b12 | -3.03504 | -50.40514 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| bee6e358-d964-3274-be11-973a91de1b98 | -2.97661 | -50.48471 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| ab056d1c-64eb-3b2e-a729-8e836d0b2e88 | -2.34191 | -48.90862 | 2024-10-29 01:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 41a26ab5-f875-3124-9458-9a2f4b57d144 | -4.10168 | -50.52363 | 2024-10-29 01:30:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| f6228766-bda9-3467-ada7-c4abd0fb2792 | -4.09995 | -50.53986 | 2024-10-29 01:30:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 805b8d88-61c9-3bc8-943c-20743269742c | -4.09657 | -50.51781 | 2024-10-29 01:30:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bbe0ff93-b0b7-3376-8ab9-e36d3b441ef9 | -5.6013 | -50.06812 | 2024-10-29 01:30:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ca9753ee-3f9b-3a64-9af9-8fd9268cab2b | -3.56426 | -51.51325 | 2024-10-29 01:30:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 859d5fd1-84e2-3e71-8d49-5d40e61a91b1 | -3.27588 | -50.70331 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bcb6d3a0-64c0-3ac6-a0ec-8e218481cd4b | -3.27058 | -50.69838 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 3c842fe1-5acb-3572-8407-497b9276afbb | -3.26991 | -51.02912 | 2024-10-29 01:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1ac7a90f-9e38-3024-9069-4f6aa7f842d3 | -3.18499 | -51.15841 | 2024-10-29 01:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9f19840e-a991-39d1-b609-6186dcfb2f81 | -3.15405 | -50.59213 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| fd0ea9ec-5a95-3214-9a53-78095676cf31 | -3.03123 | -51.44958 | 2024-10-29 01:30:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ffb6e710-51fe-3b9f-b9bd-e0990da16d65 | -2.90797 | -51.76696 | 2024-10-29 01:30:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 42515f87-0c29-3988-953d-318db51bdefc | -2.79053 | -51.96109 | 2024-10-29 01:30:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 008deb72-0a85-31de-bb8a-24d84592c1b7 | -2.64519 | -51.76772 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1d2d09a4-2e3b-355d-8d9e-fb805d3ad430 | -2.64246 | -51.74926 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b07d5511-3f49-31b0-8e24-25dfd12924ff | -2.63972 | -51.73074 | 2024-10-29 01:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 20d9dc2e-8df8-3709-8ba6-fde0e372d4d1 | -3.4737 | -53.25 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d6641e9d-eaf1-3047-937f-1d6fe938f33d | -3.47138 | -53.25614 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f33f8821-358a-397f-98c5-ff56914864a6 | -3.43231 | -52.90077 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| cf6f8e8e-60f6-38f1-84b3-8248c76815f7 | -3.43204 | -52.89501 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 280194cf-169b-3186-a6d0-18eca17fabc3 | -3.41208 | -52.8381 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 01c92347-5c62-3e22-a482-8ac0bbb506aa | -3.00437 | -53.43886 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 281faa75-4ce8-31f9-816b-ad83542d0f2c | -2.99358 | -53.4405 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 24aa34e4-349c-34fe-a539-2b8af7f01c08 | -2.86875 | -53.36704 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fefa84ac-3eeb-36c5-87a2-8270935f960e | -2.86671 | -53.35312 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fa8d30fc-6aef-3041-bcdb-793080d721a9 | -2.86474 | -53.33969 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 70f230f5-d2f5-3857-8afc-8d46223ae378 | -2.85582 | -53.35472 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4cea4b22-3e72-307e-b4e9-f68e5e687ea2 | -2.85386 | -53.34138 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c9953eda-c35c-32ef-bb40-010d29943fd7 | -2.85185 | -53.3479 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1cb2a1f3-2d7a-39f8-9585-47c9fef898c3 | -2.84994 | -53.33426 | 2024-10-29 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dfc72153-12a4-38c2-afb0-35aa3e51e11f | -3.88611 | -52.37963 | 2024-10-29 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 515cebcd-1b9c-338d-b474-221a097f1738 | -4.20472 | -53.46564 | 2024-10-29 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 141fb181-14e5-3ddf-a897-1255fcbaee27 | -4.05098 | -53.4153 | 2024-10-29 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 90a1c6cf-5b99-36b6-9311-e6a9e34583fb | -4.04493 | -53.40852 | 2024-10-29 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4d4e2fe4-09ae-372f-b2c9-afa6e7077871 | -3.66981 | -54.08138 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eddeff5f-0a7c-3139-8ba0-fd6d23d93c23 | -3.57033 | -54.67881 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 97551726-e836-3c33-8087-8fd94d99dc52 | -3.56878 | -54.66779 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ccc2cd26-206f-3c35-b92c-950195998a27 | -3.49574 | -54.43888 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README18.md)
