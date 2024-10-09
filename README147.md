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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36bc7c12-8347-315a-a51a-97b175e0b7dd | -11.28412 | -54.58139 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f5caaf31-76bb-32d6-a2de-d3e330908214 | -11.2803 | -54.5807 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e03cac2-c759-3e2b-8c6d-2223e1bdbf17 | -11.27948 | -54.58549 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97554da2-705d-3991-bb60-c561e8c17122 | -11.27184 | -60.3952 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7175b741-00e6-3760-b3c4-00b2b3f64b29 | -11.27109 | -60.39902 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5b97b55-1aa8-3a5b-a7e5-961bd632d7ea | -11.26778 | -60.38633 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f89098d4-41cc-3bff-93e4-806c7c06dc6c | -11.26704 | -60.39015 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2e7dfe5-a949-30a5-910b-1e5681caa139 | -11.26626 | -60.39412 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a87befb7-f490-3394-9f7f-bae2e08b0a6e | -11.26546 | -60.39827 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d64e373-1c60-3082-999e-3a13a849a4ab | -11.2598 | -60.39763 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a32b86f-6fee-3ebd-8c24-a97b5cacfb6a | -11.25896 | -60.4913 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa5eb0c-4349-387d-b429-adfd03a5d3bf | -11.25825 | -60.49495 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e4730b0-2df4-30db-90a1-deec3999dc95 | -11.25033 | -51.28549 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bb9fb4f-d9d9-3087-b4ae-b7e668101a38 | -11.24976 | -51.28906 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a18f62bf-828e-3d2d-8932-6a3abd28453d | -11.24928 | -51.27066 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b96468b-2d82-3ed8-83ca-bdaef38a628d | -11.24871 | -51.27423 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebe86297-75ed-339d-8dd4-9fc8d23521e4 | -11.24698 | -51.28494 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e2e626c-4e7c-30ee-bff1-4e9a005c8b62 | -11.24593 | -51.27011 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb981dc8-2830-3703-9d6e-6947b09118f8 | -11.24363 | -51.28439 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0713e57-fabf-3aff-a40b-178ace42cfe5 | -11.20724 | -51.40332 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12ccdf97-6282-31e4-93e0-1b8f02000158 | -11.20551 | -51.40331 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caf7a4a9-80a0-3774-aab9-424c4e413e23 | -11.20347 | -51.35144 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbe4a3f6-14a2-38ac-9505-6ad49be6929a | -11.2029 | -51.35503 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52a257e6-a557-340b-9b86-7912bc311312 | -11.20012 | -51.35089 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b95a5f9b-422c-347f-9a33-d17fe0b43728 | -11.19954 | -51.35448 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d73d198-a961-3734-a6bd-6cec32ca5d4f | -11.19562 | -51.35751 | 2024-10-09 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80f2451f-c584-325f-9046-f2db85574360 | -11.18904 | -54.87907 | 2024-10-09 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0abb3170-fe6e-36ba-85f7-d81ff98b9874 | -11.18817 | -54.88403 | 2024-10-09 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ca6f07-bfc7-30ac-b2a6-a90354130a2a | -11.18768 | -51.38564 | 2024-10-09 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c3ab74-1005-3c47-869e-291d012fa538 | -11.18396 | -51.696 | 2024-10-09 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4e9c084-c054-3fea-8a5c-0b3658e171ec | -11.18166 | -54.76156 | 2024-10-09 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e6bdb9f-3eea-3c6d-b333-a4d2ff8012f7 | -11.17333 | -54.78334 | 2024-10-09 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a49e4a49-db4c-3195-85f7-e35d0ae180e7 | -11.17029 | -54.77773 | 2024-10-09 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64cefdf9-f6e4-3c7f-b0cb-062b20201eb5 | -11.16642 | -54.77705 | 2024-10-09 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76879bfb-93f6-325a-be73-5ef726b55294 | -11.15026 | -49.73057 | 2024-10-09 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57ab8651-0f4e-3825-bd03-8e042bfbbf94 | -11.13582 | -48.63494 | 2024-10-09 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c04348c-dc63-34fd-baf3-685497e0af30 | -11.13555 | -54.31868 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6c32ffb-f7a1-35d2-90ef-c4a1d8e6b5c3 | -11.13476 | -54.00578 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e8e30ef-d8e6-31c9-94c4-d64203fd49b7 | -11.134 | -54.01025 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1188797-33df-3e75-bb29-b1b01cbe327d | -11.13323 | -54.01473 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fd1b8ec-7374-3f23-a4c5-6b3bb37b03f1 | -11.1324 | -48.63441 | 2024-10-09 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5c0c01c5-d1a5-3afa-b128-afd1cb9314e9 | -11.13178 | -54.318 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b7d45cb-bc4c-31e4-a91d-cabf1c7eeb95 | -11.13106 | -54.00514 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02b39e0e-b907-32ed-a27b-a0f0d87f87f5 | -11.13101 | -54.3226 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d9fb11a-829b-3f55-a0a5-26797ca6b11b | -11.13029 | -54.00961 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72806fa4-9069-34a9-b9e2-f83ef1e4bb00 | -11.12953 | -54.01409 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44e4f8cf-fb6d-3ab1-ac93-0ff1af386086 | -11.12898 | -48.63388 | 2024-10-09 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f770767f-798c-34e5-b02f-13d2f432f705 | -11.12876 | -54.01858 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba2ff694-2e56-30c2-91a1-be099e15b8f5 | -11.12774 | -59.09306 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ba49f1c-6c79-3f07-8496-372107535168 | -11.12735 | -54.00452 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfcfdd03-b97c-36c1-9216-98c9f6d82c2e | -11.12715 | -59.09624 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d2c9eba-3ade-33e5-b400-5c04af615372 | -11.12659 | -54.00898 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58479418-762b-3173-8dee-2e35ef3d4083 | -11.1226 | -59.09215 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16b53aee-93ea-3982-8bf7-0836d3a5718d | -11.11534 | -54.03007 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c3baa43-76b2-3e25-949d-b472f23dffd8 | -11.1124 | -54.02494 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c8a842-0ef5-3545-8591-72ffc31f577c | -11.11162 | -54.02943 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da41a02c-ccda-37e0-83e2-ef04a88945e1 | -11.10869 | -54.02429 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd6147fa-190c-3b55-a93d-40e5dbf42791 | -11.00033 | -54.24997 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bda592a-a384-387e-abae-1d60b0c8b2de | -10.98827 | -54.25254 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 890d1ce8-c482-350f-9e6d-a409755fafa8 | -10.98451 | -54.25187 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6185a6e4-7360-3659-b875-8f6c51326e9d | -10.91126 | -55.79318 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 136e5918-15d5-3c56-a155-e1d530f136df | -10.91047 | -64.1521 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7d0888b-3d7d-3a81-bace-e3e13736a21e | -10.9093 | -64.15782 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42c9fc77-a840-3cdd-b4e6-6e15e3f91ba6 | -10.90764 | -64.15031 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 023e7980-072f-3033-8624-0f02b238eb1e | -10.90662 | -64.15514 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 849e1651-3b45-3610-8ab0-a6a690e716a1 | -10.90352 | -64.15037 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1aaf5eeb-e92f-333e-860a-81f505628736 | -10.90243 | -64.15565 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5094eeb5-ad08-38e5-b7d8-ba26ef755e50 | -10.89941 | -64.15462 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 62114a13-67ad-357e-bc49-db2ae1498b8f | -10.8977 | -49.14222 | 2024-10-09 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b2e0132-8e18-32a3-a478-0a66d9b10f23 | -10.89503 | -64.15615 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2783525-02da-3f1d-a502-2c2aa335a289 | -10.89489 | -49.13809 | 2024-10-09 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba880b54-4ff4-3bb1-93f3-796ad221950f | -10.89433 | -49.14169 | 2024-10-09 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bac67c2d-ec92-3faa-9bcd-b459f4f154c6 | -10.88603 | -63.91806 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a3e80e-b734-34a0-98bb-db7f4c13d391 | -10.88575 | -63.92478 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d05f3db7-ecde-3057-bf4c-fdedd49f85f3 | -10.88462 | -63.92481 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46c96606-eaf7-36a7-bc95-39b21304cd0f | -10.87886 | -63.92318 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 285d1c5d-ff22-3a98-9153-4e93c684e03a | -10.87772 | -63.9233 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6a6424a-2158-34b9-8f1f-716ba0348630 | -10.87455 | -63.9039 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6cd3808-9213-3404-b7c9-acefdd48df3b | -10.87447 | -63.90918 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a78fb531-9786-32a3-8ebd-d2c332ab8e0d | -10.87342 | -63.9093 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7495518-07cb-30a3-9721-6ba2aff41b37 | -10.8685 | -63.90309 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a7a26a5-dfab-3fec-b245-3dd56e02f8c4 | -10.86745 | -63.90333 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04aca5ef-bd70-3925-91f3-d9af6d3e4b93 | -10.86739 | -63.90859 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c2a65c0-b840-385c-a9bb-dd4acddd2db6 | -10.8663 | -63.90886 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecf2d3d9-b76b-3db4-8a0b-fc09e011d613 | -10.86491 | -63.92085 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e638670c-254b-38da-b2e9-b817f01ab6d3 | -10.86374 | -63.92109 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aedc59c4-a490-3b80-adfa-23cde4008b24 | -10.86031 | -63.90795 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a04f510a-a0f1-3985-8ff0-338f136671f5 | -10.85923 | -63.90811 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b4db143-8b24-3191-b8af-767da9c449a0 | -10.85909 | -63.91397 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d4fc857-67b1-3133-93be-e557de879295 | -10.85796 | -63.91421 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d354a5b-cd47-35d9-ba35-2192b7b69271 | -10.85781 | -63.92028 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6f2823f-631b-33b1-bf57-1644ba310575 | -10.85265 | -51.06377 | 2024-10-09 04:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 187fa288-a9ce-3377-86d0-7df193bae2f0 | -10.80162 | -55.84793 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836e6e9a-09f0-35fe-9abe-0afb32d78d65 | -10.70692 | -64.15826 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0908925b-321f-3895-90be-9c16924c58d7 | -10.69358 | -63.64161 | 2024-10-09 04:40:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b16b9bc1-936d-3b35-bd1b-a90969aa7155 | -10.66834 | -51.53384 | 2024-10-09 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8fd374df-a6b8-3669-81cb-d92f2037ceb6 | -10.66458 | -51.81425 | 2024-10-09 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4509a33-b838-3132-b9cf-9bbd1be8dbf9 | -10.66399 | -51.81794 | 2024-10-09 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 200ee417-c429-35b3-a38d-0c79cc647e7d | -10.66306 | -50.91616 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49f94b01-3dcf-3348-a0a1-f9976bc3cb12 | -10.66029 | -50.91208 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README148.md)
