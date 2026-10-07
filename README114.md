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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df8d6438-17fc-3455-b76c-7d1ecf37b6c0 | -9.4457 | -68.40147 | 2026-10-07 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6df22dbb-b7b1-31f7-b9ed-d62365f2387a | -9.13855 | -68.27664 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e6cb835-1a2d-3542-9d73-fce3521f66ae | -9.1732 | -67.32236 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e37ae0-6ed8-3656-96e3-da64207fda4e | -9.44501 | -68.40534 | 2026-10-07 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fe4754cb-5952-34ab-96e4-ca3d9b560bf3 | -9.95766 | -67.19447 | 2026-10-07 05:44:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 247717a2-6cd2-3422-9940-55dae96ee428 | -8.27209 | -70.89587 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b7e24b7-66a3-39dd-ac5d-d20ee1ef384a | -9.22664 | -67.89529 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3dde6efb-4c9d-36eb-94f7-ede5b65302ef | -8.69166 | -68.71227 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3128a9e1-e6ae-368a-a0f4-4ef8083b93e2 | -9.33539 | -65.4588 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6f587e8-19da-347f-8cf0-6b2cf557a270 | -9.59633 | -64.29533 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c538755b-033c-321f-ba5b-f546e9803840 | -9.15284 | -65.94815 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c951a342-20c6-3435-a3c0-f66135c3ca0e | -9.11247 | -67.83459 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55b3d834-ca3a-3132-87c5-69f728438483 | -9.33894 | -65.45941 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69b72618-4ec6-3575-86e0-318b42f46c55 | -8.33563 | -70.80296 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 688c01ff-2076-369c-904b-f998e1b6dd36 | -9.67496 | -66.82292 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7567363-ce49-352f-92c2-0696450a02b2 | -9.10627 | -67.72658 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3ce78e-3b9c-3042-a57e-de0e2ceb351f | -9.34635 | -64.71264 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7e9969c-1d7b-3ee9-b3a9-259316a049b6 | -9.16784 | -65.76897 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 231fdb38-dbc2-3bcc-862f-892b5e5e347e | -9.20889 | -67.82879 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4790632b-e5ec-3fe2-bf9e-df22838c8de1 | -8.45492 | -70.21105 | 2026-10-07 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6edebe1-5847-3185-b736-10c47b61340f | -9.23857 | -67.87495 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 178ae08c-507d-3bde-8451-e820daee79b0 | -9.2279 | -67.88802 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc7c6a57-9091-31cb-b77b-fbae2d8d163b | -9.50538 | -67.1645 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19c08588-4851-3c51-9666-2e368966c3f2 | -11.01717 | -68.56543 | 2026-10-07 05:44:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 852f6c72-d482-3d21-b493-6bfaefcbcb0b | -9.46105 | -64.33315 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 359e97d9-5cd3-3aab-9ca8-a0f2508a2b11 | -9.46385 | -64.3374 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c965bf13-fbc5-3486-9f51-3b8ed0b35e94 | -9.44178 | -67.09329 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 952e2edb-7f62-3b24-a675-612a56e227b2 | -8.26702 | -70.89497 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0002b489-1338-3af0-98da-f046961d41c8 | -10.01257 | -67.56976 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195cc592-6c1a-3156-9f50-459996f95ee1 | -9.38436 | -68.33028 | 2026-10-07 05:44:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27fe97f8-e1ba-3cff-a235-62969f399fb1 | -9.10638 | -67.72634 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3390da21-3e63-34e1-871d-47aab1822544 | -8.97726 | -67.51045 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445dc20d-1de3-3555-beaf-ea5aaab96ce5 | -8.71577 | -69.46375 | 2026-10-07 05:44:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2958e902-c8ab-3017-8d5d-9c5293c4cc75 | -9.08929 | -67.67962 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c5c8a3-750f-3a34-b751-ebb4fb54bc9a | -9.9527 | -67.19672 | 2026-10-07 05:44:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41d5e972-ee0b-3dab-9208-6c481dda8cb7 | -11.01789 | -68.56852 | 2026-10-07 05:44:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8600d2af-897b-352c-b556-1c59782fd552 | -9.54897 | -64.81963 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b49408b-2487-36fc-9d1c-51e5ffb0894a | -9.23197 | -67.88876 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b54764e9-c978-313c-b480-ccbe6e684da6 | -9.07089 | -67.73868 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2112b5d9-3593-35af-9dd2-2158bbc69146 | -9.44922 | -68.40604 | 2026-10-07 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7b8fda9b-9e54-3762-b80b-c9b0ef54a17a | -9.61127 | -67.48072 | 2026-10-07 05:44:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e415898-1a81-373c-82e5-e6b911012fb2 | -9.60732 | -67.48003 | 2026-10-07 05:44:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 880ed7df-ed22-3dba-8b6e-12d76f159dca | -12.47494 | -51.2878 | 2026-10-07 05:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a90ae42b-2300-322f-8eb5-c03fce5504de | -8.7301 | -69.98486 | 2026-10-07 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 457d9b4b-ee92-3559-a0a3-4597f6583b2e | -8.24688 | -70.83339 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcc229f6-ff2e-355b-b7cb-6cd7b350c3d2 | -9.47626 | -64.34703 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 436b49b0-f075-36d8-a9b5-98cca0ca218b | -9.28764 | -67.90218 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9e3d3e4-82f3-3b9f-be8a-f74c54894ce6 | -10.45306 | -69.2991 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4cadb80-039a-39a5-b272-94171d08787e | -9.42233 | -67.752 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 979e48cb-fa94-387c-98b4-fe9ed2c3228b | -9.46536 | -66.78207 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 388c4178-5f63-3835-b54f-e26b48edfc3a | -9.23605 | -67.8895 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 165e2e48-3d37-3db8-811f-aefd19f634e9 | -8.97416 | -67.50455 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a353a7f2-51e0-312e-9858-785b0241fdb4 | -9.81776 | -65.03147 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aa66119-1e79-348d-a302-762a52553b64 | -9.09735 | -67.68105 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f995e51-a7c6-3156-ace1-6e0e9dd412d1 | -9.49944 | -66.73766 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6a3dad8-d50d-39f6-8689-3e6d00262dba | -9.54207 | -64.81844 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e35c8a7-0e11-33ee-b990-6d1d98fe911a | -9.75724 | -65.06564 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23d30d48-4005-3edd-92a0-7f86bd05774e | -9.54615 | -64.81519 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08cb12c7-5d00-362c-a527-a36071f01337 | -9.42216 | -67.75245 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc2d4f63-a94a-3b22-ad33-93e0d80a9fe3 | -10.73222 | -68.86223 | 2026-10-07 05:44:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53e5d25a-b2b0-34cd-ac17-38dc9ecaaed7 | -9.23668 | -67.88587 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 805ffdc2-9199-389b-b4d2-37c8c2101d7b | -9.75376 | -65.06505 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca20bfbd-3dde-3b6e-8d98-39e7eb47fb83 | -10.2828 | -60.54587 | 2026-10-07 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97d070ba-bcf1-364f-8fd3-f07289328cec | -9.17459 | -67.32071 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c5b86c-e0cf-3fe2-9916-1a43ce316229 | -9.46278 | -67.08698 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c877999-9e27-3f84-a8f2-133a18099e2c | -8.86655 | -69.1744 | 2026-10-07 05:44:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75f4f08f-aae2-3214-9285-502a015fbd16 | -10.24687 | -68.29743 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abf37f30-6e39-336d-94fa-e26f122aec97 | -9.10701 | -67.72278 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2a728fb-7a90-3dde-be69-537e5d4a183d | -9.51831 | -67.11156 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da576066-70ec-3698-8d73-6dd4d2650b8c | -9.5496 | -64.81582 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ecc46b9-574a-340a-9638-c412c6367436 | -8.6294 | -69.50297 | 2026-10-07 05:44:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 015dee81-b600-3528-a3d3-af1443fd9d38 | -9.95656 | -67.19741 | 2026-10-07 05:44:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1d3cd78-530e-3a90-80be-8ed68c58ea0b | -9.13787 | -68.28049 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cfb5a655-5f2f-37d6-ba2b-09c8030046c5 | -8.96581 | -68.59324 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63bccd87-e900-3838-a4e9-68a1785f7b8d | -8.33665 | -70.79721 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1907bb9b-3d41-31e0-b750-0d4306c682f0 | -9.46725 | -64.33797 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34e834f6-fffd-36e3-9a88-b0b61fb5ef7e | -9.28433 | -67.90187 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 739eaa3d-96bc-3ea9-83d9-ff7c3d5ebf7c | -9.59482 | -65.24348 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54336191-62d7-3843-ade4-e465814e7096 | -9.11105 | -67.72348 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77caa178-4235-30a9-bcea-c34891d3baa6 | -9.47005 | -64.34221 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3a27d2c-5d8a-3593-b152-4f31cad3b705 | -10.58933 | -69.24187 | 2026-10-07 05:44:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 962e22b5-61a1-3017-a1f4-286363c995d9 | -9.23008 | -67.89966 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7180738-d7ec-3b1c-aafe-485e8cb40514 | -12.46829 | -51.28697 | 2026-10-07 05:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b029239-7e02-3589-b1d3-e3c272721248 | -9.44094 | -67.09811 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe7d06f8-dd2b-37fc-916c-6ab9f60febc4 | -9.15649 | -65.94877 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b0c461d2-9204-339f-98d2-611bcb51bd86 | -9.15356 | -65.94389 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 59a40327-f52f-3131-b952-6b8827f841e4 | -8.97815 | -67.50525 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed52634-9991-3c72-9992-7bcc81972e59 | -9.9538 | -67.19378 | 2026-10-07 05:44:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b22ed364-d002-31fe-83af-50205ccffddc | -9.41122 | -68.22508 | 2026-10-07 05:44:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1b1df88-081b-31b1-93af-5595e6ebeb61 | -9.11619 | -67.86143 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ed9f484-875e-324f-87b6-9aea5286328b | -9.46916 | -67.07307 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e4b05cb-ab00-3f00-8da4-ba7f668911c1 | -10.0383 | -62.45294 | 2026-10-07 05:44:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7864868-e4a3-30d7-8369-826a3d78e862 | -9.66878 | -68.53585 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b19bade-0511-3989-a498-b402b26bf796 | -9.71604 | -65.09852 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 842aecd9-6dea-338e-b405-4c61cd51dbe9 | -9.2884 | -67.9026 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab8f8ccc-1a51-36ff-b096-3b91a3499768 | -10.08738 | -68.46846 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74b922c1-e9c6-3a44-a3cd-597e69169e9e | -9.45506 | -67.08559 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b8f81c9-e4d8-3a1f-8ddc-1336224be0ee | -8.91493 | -68.87865 | 2026-10-07 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79432dd5-9e56-39ad-ad70-ddede78ad799 | -8.91255 | -68.79147 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ce4cbb5-7c2f-3578-a4f7-db8ae001cd98 | -9.11682 | -67.8578 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README115.md)
