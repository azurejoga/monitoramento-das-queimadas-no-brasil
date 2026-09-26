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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f40e33a-05ac-303d-85f0-d81196a4a8a1 | -12.1366 | -50.3112 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 0e3c58d6-f189-3253-acd3-6e3c035b9ea4 | -12.1952 | -52.7821 | 2026-09-26 15:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6921c892-e6bd-3fe3-8413-1a9e2d48cb4d | -11.6514 | -50.9449 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| a8e889a2-b791-36a3-b452-c858885d1096 | -1.2085 | -49.0838 | 2026-09-26 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| d9a48012-ae59-3e6e-9468-4525424de06d | -11.657 | -50.5603 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| cea14a7d-a18c-3387-9ef1-f2b1533c4c12 | -12.3679 | -50.1539 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| e7cbaffa-a9c1-32fe-8210-8fdf4bf781fe | -12.0803 | -50.2535 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 4d3b9bad-0135-3a94-a8bf-a63da7412688 | 1.6566 | -55.9424 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d0985b50-65da-3b67-9a09-cfe73c06daa4 | -11.6377 | -50.5839 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 640ab3bd-702c-3c6b-8c31-52570a728794 | -12.1557 | -50.3089 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 2e569e4e-12b6-36bf-b183-9143ebdb8069 | -12.0277 | -49.9583 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| de942d9f-9385-353d-a101-2fb1dada00a9 | -11.118 | -54.0268 | 2026-09-26 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 46f197c3-193a-391a-b0d9-7583a19d4532 | -12.7674 | -54.0502 | 2026-09-26 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7499d2b8-2419-3c47-8d47-77177a0f723a | -0.8215 | -48.6609 | 2026-09-26 15:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5a759967-eba2-3fd1-8d5b-e7a8891382c5 | -12.6608 | -50.9549 | 2026-09-26 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 19a6e6a2-675c-39c8-a63d-01183073ed9a | -12.1747 | -50.3066 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 096bbbe9-ed5f-337b-9b6e-2eb2d56649f6 | 1.1316 | -51.185 | 2026-09-26 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a7e2dee5-c25a-3802-8f78-53e9da7a19ac | 1.6199 | -56.002 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 203e67ec-026b-3c4e-abd2-bb5bc49dc268 | -11.784 | -50.9725 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 4fff0a9a-7104-3c8e-bee7-17f78a6000f0 | -13.3824 | -51.3138 | 2026-09-26 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 32251893-d46c-340d-bd5c-59e1284f8e32 | -12.1369 | -50.2897 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| c66e6c72-8dbd-3837-a91e-28ba62d5761c | -11.6508 | -50.9875 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 96cf5d93-5f1d-3e2e-a986-cc871e8d5067 | -11.8472 | -50.5598 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 35df5dea-5cc8-3419-a1a5-90f11c10bcf2 | -11.7903 | -50.545 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 84d98870-8cf8-37bc-b0c2-f802c4f44956 | -12.2254 | -50.7294 | 2026-09-26 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f0b0b7d7-5b9d-3c9c-aee5-89dac336c602 | -11.9205 | -50.7437 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| e424de8d-e8d3-3f90-b547-0b98d93c9a1f | 0.7082 | -51.437 | 2026-09-26 16:00:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ae668aa8-94c6-37f9-ab79-3adaaf8f7858 | -1.3008 | -49.0613 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| baef2943-3988-3295-ab22-18fafa92f782 | -12.0339 | -50.7946 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 5130c7b5-0b52-32f2-97ce-91950535ee17 | -11.7138 | -50.5752 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| ac400789-45ae-3579-9594-0999cc5ecfb2 | -13.2186 | -54.5182 | 2026-09-26 16:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 88d79a5d-6b3d-3f3b-add3-d5764b522b34 | -1.3008 | -49.0826 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 3d6aa38c-4802-30ca-ad83-e3ff7b1d3511 | -11.8024 | -51.013 | 2026-09-26 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 8c99bb70-d6df-3f2f-9b6c-daffe6f57ace | -1.19 | -49.1266 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e3dc27f8-c724-3e31-92e2-9db72af371cd | -11.7325 | -50.5944 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 42737821-a320-3dde-b872-4c2d4c78e69f | -11.7834 | -51.0152 | 2026-09-26 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 6d46bf83-ce63-3a03-ad67-581cb194b956 | 1.62 | -55.9232 | 2026-09-26 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f9acfbef-f192-3e79-8f94-4dff228d043a | -12.0994 | -50.2512 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| dd380dcd-42dc-333b-bd45-7d456895fe23 | -12.2445 | -50.7271 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c7ceb9c7-8918-3032-a1f1-7838ff42cccf | -12.3679 | -50.1539 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 692664c1-db80-3b43-8cb7-df0baf3b29d1 | -1.2085 | -49.0838 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 20eeb410-0173-3680-8f40-98c26b65108d | -10.7115 | -60.7312 | 2026-09-26 16:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 391906ff-ab16-397c-91d3-8079c87a3701 | -11.6199 | -50.5004 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| b5921fa1-8ffa-3dc1-ac4c-e22892838c30 | -12.3478 | -50.221 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| c1324e36-3e2e-331d-a64b-f6b009967ccc | 1.6018 | -55.8446 | 2026-09-26 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4e5372d9-e8cc-34e6-a92c-72fc92440451 | -1.3193 | -49.061 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7d31553a-e1bd-3911-96bd-b41d15f35c65 | -11.118 | -54.0268 | 2026-09-26 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 02e960ba-0688-3d02-b07e-abff89b986fd | -11.9199 | -50.7865 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| f3182843-bcb9-3e88-a725-406530992be2 | -12.2911 | -50.1849 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2331a3de-8959-3fff-9277-2ab6c50f1d7a | -11.9011 | -50.7673 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 3f998780-10b0-34d7-9196-11d3224005d5 | -11.8472 | -50.5598 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| efd60e4e-c9d7-319a-adc1-d0007be16d3c | -1.1715 | -49.1268 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 84ab4853-a1b7-3bb7-a533-76ffbd353025 | -12.1366 | -50.3112 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| ffc587c7-2aea-3967-82da-99715efc0d98 | 1.6382 | -55.982 | 2026-09-26 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6e0c47d2-0d58-35dc-8fa1-4475f5584cd0 | 1.6198 | -56.0216 | 2026-09-26 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6e262743-27d4-33c3-b29b-e9a4c0fba88a | -11.7843 | -50.9512 | 2026-09-26 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.4 |
| b5a80f95-8b99-3104-87a9-4b0fe428e6cc | -1.0792 | -49.213 | 2026-09-26 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5a2db782-93c1-345c-850f-1e7ee774bf36 | -14.3693 | -52.1026 | 2026-09-26 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0890860d-532b-3b3e-b6d6-56459388ff68 | -12.522 | -50.07 | 2026-09-26 16:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| dfa859f0-4f90-34ed-9486-0ec49f1003ab | -11.8475 | -50.5384 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| d678494c-ec96-3b9b-a808-8a91fbf72067 | -11.8094 | -50.5428 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 28891470-6253-3704-8dc7-a69b08f282a9 | -12.8059 | -54.0255 | 2026-09-26 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 5f5ef49f-e77a-3ca8-96c4-4f20b5bde02e | -11.7903 | -50.545 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 22e956dd-950d-3f4b-9758-7f08b0cdeefa | -12.2636 | -50.7248 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| aea546ed-c708-3966-8f2b-165701de214d | 1.6198 | -56.0413 | 2026-09-26 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8f25b513-1a40-360b-a376-d1c778521cb1 | -12.329 | -50.2018 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 364cb811-5ac3-3681-a163-ae740c8b7977 | -10.7114 | -60.7505 | 2026-09-26 16:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c269cfcf-5d5b-395a-af69-02427a175e59 | 1.2794 | -50.851 | 2026-09-26 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 207ff9c9-1d4a-3e1a-97ea-2b543def7738 | -11.8078 | -50.6499 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 7a82af0d-0c69-3d9c-8437-c4b9637a4356 | -12.0612 | -50.2558 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| a55080ba-1c00-3e10-81a3-ed3724df543d | -12.7226 | -50.669 | 2026-09-26 16:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| baea33a4-c5f5-3229-b309-a71d28de709c | -11.8821 | -50.7695 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| d883d5ae-c0df-354f-ad09-a1bb689673e7 | -1.3193 | -49.0823 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e726638c-5b65-35ac-84f6-fd9973049d4c | -12.2827 | -50.7226 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 5158c95d-8d6b-34f8-9222-7ea2006c08ce | -11.9015 | -50.7459 | 2026-09-26 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 39d76188-faf4-33a2-8ee9-d877ccd19709 | 1.6199 | -55.9823 | 2026-09-26 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| dcdf344c-9486-3e43-bb50-54ca4c279a3a | -12.3286 | -50.2234 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 242998ba-41d2-365a-b287-23a4d5f31d30 | 1.1316 | -51.185 | 2026-09-26 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b90c8e63-6cdd-38ee-b043-124ca4934ccb | -11.803 | -50.9704 | 2026-09-26 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ff5fe5b2-b862-3094-addb-475867d7d1ba | -11.7094 | -50.8745 | 2026-09-26 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 8192063c-a960-36e7-b741-4639ffd30a79 | -12.1557 | -50.3089 | 2026-09-26 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 69f45482-addb-3112-8be8-f1a6b5a8f792 | -14.3499 | -52.1051 | 2026-09-26 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 33dbf643-e114-3082-9b33-a7e63531204f | -1.2086 | -49.0625 | 2026-09-26 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 154e3ef2-1dc8-350c-ba63-69e65bc6708b | 1.4452 | -50.8071 | 2026-09-26 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6906bc61-ee46-3333-ba75-2102900f955c | -12.0339 | -50.7946 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a299d4a7-b885-32d9-8e87-02ad79a007d2 | 1.5652 | -55.8253 | 2026-09-26 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a040578f-7f17-37d5-8600-6844f95a555c | -12.0803 | -50.2535 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 6b8ff5e0-fd4e-32fa-aef1-97bcb34dae4e | -14.3693 | -52.1026 | 2026-09-26 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 09b613e3-a073-3d3a-aec9-ab2f95463eab | -11.6701 | -50.9641 | 2026-09-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 8078213b-af22-3198-9048-a5dc994adbfe | -11.9205 | -50.7437 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 151.6 |
| deb8e5eb-647f-3467-a26a-84c11df6fa07 | -10.7115 | -60.7312 | 2026-09-26 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 473c8125-1c53-32df-b117-81f863887d08 | -12.7767 | -50.8766 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e6fb352e-8d77-36f5-a22e-935469aa0155 | -12.2911 | -50.1849 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 052e9220-2d1d-3681-93d3-a3805dfed985 | 1.5652 | -55.845 | 2026-09-26 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7b1a41b3-b91e-3851-ab3b-66855db9c428 | 1.6198 | -56.0216 | 2026-09-26 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ef17df39-6d2d-3085-b721-8a4614e0f268 | -12.0612 | -50.2558 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 9147a5ea-07fd-3a16-a782-e7ff3bbaa5d3 | -12.3478 | -50.221 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 186e6096-6b74-365f-9c8f-741e92ce63dd | -12.3105 | -50.161 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 1d9749d8-daa7-3109-9644-1f6fd551136c | -12.0408 | -50.3442 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| d47d4edd-46ae-3863-87ab-c75098235ad2 | -11.8281 | -50.562 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |


[Clique aqui para ver as próximas entradas](README40.md)
