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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c92b608-e857-3ed6-90b2-aa93968e6041 | -10.9854 | -63.94612 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea53f691-d1ba-3adc-a12f-bd0c968cfd60 | -10.98472 | -63.95004 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16bbc395-6e0c-35d7-b1a8-01e8655d6319 | -10.98405 | -63.95395 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fc85c7b-3f92-3883-b591-1a95a69772f0 | -10.98338 | -63.95783 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11e64753-598c-3fc1-b3cd-e3688a094302 | -10.89999 | -64.18607 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 354abd6f-7f4b-3a90-a983-fa2547eef450 | -10.89006 | -63.8958 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46bf063b-1c68-3012-9d4e-b58cbe3ebf2d | -10.87461 | -63.88593 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b634307-754a-3347-adc5-f06248b2f257 | -10.87393 | -63.88988 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4a5c9a7-4d4c-37a5-b2bb-a30b7a594d07 | -10.86972 | -63.88936 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2df9f0a0-2b15-3c23-b9d5-239254a6fe11 | -10.99461 | -63.57684 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f4a2ff3-cc37-3da7-87b3-f3befd27af47 | -10.97819 | -63.57475 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d07a50a-39dc-3961-abf2-2f9b52c9422c | -10.97761 | -63.57798 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7f75b20-3d6e-31df-8381-7b0193b438e3 | -10.97701 | -63.58141 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e288d0-4815-322c-9b94-be6b00fd9194 | -10.96688 | -63.59111 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2be1f5cc-9f32-3f40-b3af-3e6e0cb374e4 | -11.61533 | -63.66969 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14518d48-f445-3189-a2fb-41db93d84f51 | -11.61472 | -63.67313 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 440d5ff8-842f-3aeb-8cc9-3e75722055a4 | -11.57774 | -63.76849 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15c476a3-4f0f-3e22-9fe2-8b5cc7424325 | -11.57707 | -63.77239 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1d8a652-9b08-3581-b72c-62cff91cdf6e | -11.5768 | -63.76794 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69851dd6-d479-3ae0-b45c-661f3bd650c2 | -11.5761 | -63.77185 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed773de2-3c1a-30e7-9190-69933fce9507 | -11.57363 | -63.76788 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02abb168-39ff-3c9a-a056-1448295b92b0 | -11.57297 | -63.7717 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ceae5b2-d5f0-355f-a710-e4489dd5d663 | -11.57201 | -63.77116 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a096a418-c11a-3791-81a4-447e2e2f47a2 | -11.56888 | -63.771 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71374f02-0a4a-316a-831b-2b538acdc133 | -11.56824 | -63.77471 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9faf0683-33d9-34bb-9582-67c2198db1c0 | -11.56351 | -63.7777 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9af7e8b3-6c74-3ee3-889e-0668813514dc | -11.56223 | -63.78511 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddc52e8a-0ef0-3233-a10a-11cc935d76bc | -11.56159 | -63.78881 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 402e2c47-e02d-3e8a-9f50-a7b6ed4a8057 | -11.55814 | -63.78438 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cfbacee2-5cd7-3fa4-a8f6-c668cf02fe39 | -11.5575 | -63.78807 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc2d1f6a-00eb-3ff0-8004-f202883e28b3 | -11.55692 | -63.7185 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17aa91f-7121-3327-9026-f03580db0d75 | -11.55686 | -63.79178 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a9f29bd-acb7-3ed5-94b8-e4bc25c9ea38 | -11.55623 | -63.7225 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 351bbf5c-294e-31d0-a306-49fd6be94c95 | -11.55622 | -63.7955 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f96722fe-1d3c-3609-a3df-78b67951bc2e | -11.55143 | -63.72594 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fbd4a705-9c16-37af-887b-8797c3d8ab6f | -11.54735 | -63.72528 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d93ead94-878d-3bfc-9b2a-62a9ff8c00d5 | -11.54569 | -63.83187 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63f2826b-8aeb-38f6-8f57-b6791b033701 | -11.54505 | -63.83559 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beb2ee8d-3417-3365-b7c1-f4875bdc2f4a | -11.5444 | -63.83931 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99e14527-0cc0-3ec1-b432-c67d68e4a65c | -11.54418 | -63.81621 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaae4dd6-4aca-307f-a551-6c0472304bb3 | -11.54391 | -63.72089 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2060caf-a782-3db8-88ed-c03d033f3603 | -11.54353 | -63.81992 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84511619-f277-31ab-8c16-6da68a55e659 | -11.54326 | -63.72457 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64067739-3146-361c-9606-f887e7c87338 | -11.54289 | -63.82364 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 244defa6-59ef-3d62-8c34-62ab24bfb2a7 | -11.5403 | -63.83853 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c78dfcf-1ec0-361d-94d9-0fc07336ec98 | -11.53641 | -63.71569 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0454e92-0c96-3411-8518-439baaf1242e | -11.53234 | -63.71492 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0edeacf-6876-34b0-86f8-8e1f31bcb5e9 | -11.52827 | -63.71416 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6da79da2-3cab-3a45-b7a6-bb5dc1c82738 | -10.99918 | -63.57475 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5c702124-f6eb-3042-9e42-22a4f49898a2 | -10.99865 | -63.57777 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 41a4eab4-b4dd-3568-9287-24ab645a13f6 | -10.99051 | -63.57629 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5047704f-2fa9-3d86-9af9-c6bd114027ad | -10.98693 | -63.57277 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a84a882-714e-305d-9c1f-21c7c67643ad | -10.9823 | -63.57522 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f283cba-92c7-3a37-bd7f-745a4ebdecc3 | -10.97874 | -63.5716 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6814566-4c3b-3dbb-b30d-ed4ec6f10c82 | -10.95768 | -63.60091 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4202e050-66d7-3311-9b55-2a7185807605 | -10.95683 | -63.60033 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26509778-f7d2-3577-b919-235215c861fd | -10.95359 | -63.60022 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 882113d4-69f1-382e-90a8-81582fe677b8 | -11.77952 | -64.27973 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f872c4ea-66fc-3911-9a0d-9c869ed117b0 | -11.77602 | -64.27499 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8855142d-57c2-3bd6-95ac-f4320498da39 | -11.77464 | -64.28279 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ba9f43b-bc95-3f1d-945b-02301d71f3a4 | -11.75912 | -64.19918 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcc8ec78-529e-3993-886b-bc66072bc0b4 | -11.73189 | -64.11067 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61599334-f03d-34be-9bf9-ad571b98548b | -11.73093 | -64.1103 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47fe2d2d-4498-3841-b43d-1078cc9dfa05 | -11.72276 | -64.13262 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7c724e6-2377-356f-a9d0-ef21da373062 | -11.71792 | -64.13567 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5539d24-a613-3ce3-9570-85623296e986 | -11.71442 | -64.13109 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6317b4f1-3aaf-305e-a587-bd808d528fc9 | -11.714 | -64.05967 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32acabb2-44aa-301c-ba39-6fe254dc0f36 | -11.71224 | -64.26724 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d41e3fac-a20c-328a-b433-d6245e469930 | -11.70985 | -64.05889 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20194329-8626-3a03-ba7b-f8dd8f9b857d | -11.70918 | -64.0627 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e3da919-45c2-3125-b2b8-373f71392022 | -11.70637 | -64.05428 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0799ea6-6598-3570-90cc-990a3d8aea68 | -11.69809 | -64.05264 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a9f4248-142b-3f8f-9fa5-62ca29797bee | -11.67109 | -63.98783 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7d5e0e3-932e-3642-96b6-d484a5e6d235 | -11.66238 | -64.06063 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84688136-d81b-3354-ac88-c4e33a93754e | -11.65765 | -64.23282 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f8d09d-b374-395d-9b69-37840ef5fafe | -11.65343 | -64.20772 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb4a6490-72d7-3e62-85a0-90afe962f227 | -11.65275 | -64.21159 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61350e3f-757c-3774-a041-7bdc1fc17b96 | -11.65255 | -64.01978 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 324acadd-4dcf-328b-81a7-4f4ccbb36b74 | -11.65134 | -64.21947 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a408824-9561-3d06-b49e-487ba46d03ae | -11.64899 | -64.01575 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b2036f4-80d2-326e-a190-1d43924afd58 | -11.63808 | -64.02287 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 640d384e-bbec-3041-b12f-39a5e1492cde | -11.63327 | -64.02593 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 638ab7a3-096e-385f-a28b-e074c3fe3746 | -11.62912 | -64.0252 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6bc53ad3-3b03-3af8-abf9-f4037d7423ee | -11.62212 | -64.11514 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff03273c-23ae-357d-a88b-8c3b60c6ef83 | -11.62197 | -64.09117 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcdc443e-e646-3407-9895-86ec33a9ac88 | -11.6203 | -63.95323 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70c027e1-256b-3d16-bb2d-819b1834edd9 | -11.61964 | -63.957 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17f56721-302d-3e02-bc6f-d0f0ce3fe9bb | -11.61616 | -63.9525 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f37bb5f0-e3e0-3346-98ad-d8995fcd1f05 | -11.6045 | -64.1907 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9f345c-0ce3-3e56-9143-afffdbaf9398 | -11.00246 | -63.92203 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39ecff28-c2cb-3b03-9620-949877e9b013 | -10.99221 | -63.93164 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9844ad9-9b9e-3af2-bb8e-93247d2c16f4 | -10.99155 | -63.93547 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 530bb374-0414-3572-a5e0-e34edeed5c0c | -10.99088 | -63.9393 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8c0e43a-7fed-3137-b2dd-7272b2d9b03e | -10.99023 | -63.9431 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 108931d4-b654-3097-b492-018a127e4ca1 | -10.98271 | -63.96164 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0e9fe66-81a4-3ea8-9bab-0e1f54649944 | -10.89074 | -63.89191 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a382c7de-8fad-3cb3-884d-1b3c94ceab3d | -10.88589 | -63.89514 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df324bef-0ea8-3255-8067-3cfc891e7780 | -10.88305 | -63.88672 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 411caf24-2192-36d1-b66c-8315ce3751e8 | -10.87883 | -63.88635 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 899f90ad-bc51-3c14-a2e0-aa216a6e6938 | -10.8704 | -63.88547 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README160.md)
