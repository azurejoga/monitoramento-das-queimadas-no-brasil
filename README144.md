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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d74ade9-95cd-3d8d-b1fb-83dc489aace8 | -12.69407 | -54.11097 | 2024-10-09 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a457cca-9a60-3d4a-9612-854fc6b89e1a | -12.69142 | -62.96238 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b524ca05-b22a-381f-ad5c-b44e6de14708 | -12.69073 | -62.96191 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 071b5a41-fb36-384c-b23e-b96a3883bf60 | -12.69032 | -62.96766 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 51296334-29cb-33e0-b41b-6a23d6f13129 | -12.68967 | -62.96721 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2eab1f87-8263-392d-b0b7-e3435216c552 | -12.68948 | -62.93991 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fdf00471-2d00-3ef8-9242-6f2151fb3521 | -12.68865 | -62.93937 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11525caa-f5e9-3791-b616-e76f90e45417 | -12.68838 | -62.94518 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6fa26de-7b0d-3a55-9944-71ddebac3327 | -12.68759 | -62.94464 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac89ae75-e9cf-3fc8-abe2-f4006525f7b2 | -12.68728 | -62.95043 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe5914ae-ee93-3919-938f-8fa9e1aa5a04 | -12.68653 | -62.94991 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8939c26a-4f1b-3104-a869-0c7c3e52dc89 | -12.68619 | -62.95568 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b51bb38-4f73-3348-aef7-265513b5572d | -12.68508 | -62.96096 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed7a02fe-d0f0-35cf-b60b-975fbb3af586 | -12.6844 | -62.96045 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98b6ee72-4dfb-3ff7-a23f-a840d6f48853 | -12.68398 | -62.96624 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a03cdc90-19cd-3dd2-8c07-46060c3e70ad | -12.68205 | -62.94373 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 617fde3c-4075-35ba-8932-d4943e5cf5b5 | -12.68126 | -62.94317 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f44ac8c-b612-3645-aecc-48af95e66121 | -12.67258 | -54.71983 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00f76a9b-587e-3a0e-8d51-d4e5d24d7be1 | -12.67233 | -63.08591 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8346ae2c-c112-3667-b9fe-b17f13a1ca7d | -12.67178 | -54.72453 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc760784-33f8-3a58-8a83-f3b7978a4879 | -12.67098 | -53.18907 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b349da77-1105-34ef-bc19-984355a030de | -12.66881 | -54.71915 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81b82815-ae27-3c0b-902f-73edf1065358 | -12.668 | -54.72386 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce423512-fb46-3817-9214-639e31a54ce4 | -12.66603 | -63.08439 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a4f2afd-0ee8-3b96-9d5a-a94fe1db5849 | -12.66594 | -63.0845 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 96a4fc6a-4ddb-37bc-a61e-1723654970e2 | -12.66503 | -54.7185 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e678e6de-e218-36f3-af78-5f184faa66a0 | -12.66423 | -54.7232 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbaccbd3-75a4-3487-ae40-8074b21ab0fc | -12.66126 | -54.71784 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c5a0660-b9c0-3e68-aa4b-a0d28d0feb5c | -12.65745 | -63.09379 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cb2565bc-0cea-3295-947e-7e88fd9f1a3c | -12.65735 | -47.03603 | 2024-10-09 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 179f4924-b41d-399b-be00-0878f82d8c53 | -12.65729 | -63.09388 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1fad1ae0-1601-3685-a22b-50b73eb20ea6 | -12.65692 | -54.69794 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c2c26a9-4083-3725-ab2a-f73d9a6fd411 | -12.65363 | -47.03546 | 2024-10-09 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12f9fd61-6842-3274-bb49-6bd0bccf8133 | -12.65315 | -54.69728 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1736586e-44cf-35e9-99f8-baee5c61afd2 | -12.65106 | -63.09236 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8fe0798-56f8-3e8f-9efd-abdb8f060011 | -12.65089 | -63.09246 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47026c37-558b-3e16-91d7-9606159054df | -12.6343 | -54.69395 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83fe3109-0608-3f45-858d-5d81c0ab2372 | -12.6331 | -53.1104 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de012c73-b129-3580-b971-f9cb844f1174 | -12.63245 | -53.11434 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0cbfa0a-3fd5-3b95-ae76-c176d9e9cdc0 | -12.63179 | -53.11827 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6d9fe1-d7ab-3a26-b7ec-551dbdf2f44b | -12.62953 | -53.4999 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b790a4f-680b-33bb-bdb5-f85b69d90356 | -12.62895 | -53.11374 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c410c76-df05-3124-a9b6-ac496cf2b879 | -12.62884 | -53.504 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d30d542f-704c-35e0-b4fd-b36e0269421a | -12.6283 | -53.11768 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90d3f712-ddbc-3141-a6f5-ab7e1169a813 | -12.62765 | -53.12161 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee2bf955-0562-3acc-b71b-1ab879cb393e | -12.627 | -53.12553 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c683ad7-7323-34b8-9531-bdae22eb4ef0 | -12.62481 | -53.11707 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1965a51-c72d-3953-8a24-bb57ac3edf2f | -12.62416 | -53.12101 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c360eb-9b58-3832-aea9-4ed35e1b6ffc | -12.62066 | -53.1204 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 660a736b-0fc5-3a0b-8409-65f7cfccbc1c | -12.61471 | -53.02658 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9c1879b-7ac0-3551-a7d9-508aab69f0e9 | -12.61468 | -56.51473 | 2024-10-09 04:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61e2df94-2daf-328b-b3a2-d0d79f305a36 | -12.61399 | -56.51865 | 2024-10-09 04:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 568e9d75-d7c5-34e1-a099-bee8facd74ae | -12.61399 | -56.51412 | 2024-10-09 04:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9d92131-cc5b-3065-98de-e17d9d914d7a | -12.61328 | -56.51803 | 2024-10-09 04:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51fb3b59-f738-34ad-a550-589b8f5159a8 | -12.61123 | -53.02599 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a310cdf-aaf3-31f6-8665-1b4333b1689e | -12.61058 | -53.0299 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a709f9-89cb-3ed2-9688-c41d9de2b347 | -12.61046 | -56.51393 | 2024-10-09 04:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 978dbdb0-151d-3382-a792-82df8baf95d0 | -12.60978 | -56.51334 | 2024-10-09 04:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f5b697f-21f9-3f37-8ec0-3a4976dceb14 | -12.60645 | -53.0332 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e1ebbea-8f3d-3974-a855-106ddca7d37f | -12.6058 | -53.0371 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd97f3c0-501c-3717-a574-e3e119d14ba0 | -12.60232 | -53.03651 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2217ae2c-732b-3623-a1c8-b36443868129 | -12.60189 | -53.12526 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a798bc1c-a00c-3e01-8db9-436ac15aeb27 | -12.60123 | -53.1292 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 542f6b49-99cb-323d-a2fc-dd77226980e1 | -12.60057 | -53.13313 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a8b172-d6e8-3668-9977-b042982492bd | -12.59839 | -53.12466 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2e654b7-f975-343d-aa23-27ee1cdc57df | -12.59708 | -53.13254 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb7ffa3e-6b4b-397c-b6a6-3f5475a41659 | -12.59409 | -55.22145 | 2024-10-09 04:40:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6608f1c2-ba8f-36e6-a047-aef1d79485a5 | -12.58381 | -53.06144 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 296145da-808f-306b-b1f2-cd16bd80b968 | -12.58315 | -53.06538 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c0e80fb-324f-34f6-a839-91c8bdd2231e | -12.5825 | -53.0693 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e9b07b1-16a1-36ee-af9d-ae52a380b49f | -12.57967 | -53.06478 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca1b6013-0373-3c5e-a919-fb34b6733b72 | -12.57901 | -53.0687 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45b4c4d3-48dd-38a1-ac00-5de1f53c8b5a | -12.57835 | -53.07262 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ad2d721-8939-3e71-9926-491001cd2955 | -12.57618 | -53.06419 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 538fc230-88de-37a2-accf-bdd0c939447e | -12.57552 | -53.0681 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4b7ded0-ffb8-381e-8583-e41df1001cb2 | -12.57487 | -53.07201 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91e3a149-a503-3661-aa5a-a75e9d7ed73f | -12.57466 | -53.05185 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03c50e47-409e-356b-bea3-1dceda5c6baf | -12.57269 | -53.06361 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d140bfe5-dd5b-368c-9e63-d46581353496 | -12.57203 | -53.0675 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aebf4693-b6f3-3dd3-a699-5c351aad576b | -12.5692 | -53.06302 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fd2435c-b535-3cca-8264-4af48ae67b68 | -12.56855 | -53.06691 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0cd8434-15e2-34f7-8029-75eaa941a9d8 | -12.56506 | -53.06631 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac92546c-07da-374e-964f-c091db25ff6f | -12.52787 | -47.65167 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b09c564e-e5da-3252-9b64-05797dea9f32 | -12.51932 | -53.25479 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebefdb7d-18a5-305a-af33-4796987096d0 | -12.51866 | -53.25878 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 050619bd-0fba-37f1-869a-4d059fe0a3fb | -12.48535 | -53.15485 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99c45eee-f353-3223-b944-bba0025ade66 | -12.48251 | -53.1503 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1294bfc3-7c24-389e-b22a-70838140ec5e | -12.47967 | -53.14574 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53de75bb-c62d-38cb-a4d7-42918ee60062 | -12.47616 | -53.14514 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbc55c70-e07a-302c-8882-05f456994d92 | -12.47266 | -53.14454 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fecca70-5b8c-30e9-90d8-7739d13928a6 | -12.47228 | -47.50103 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70529f11-9c55-3fbc-a7ce-e107d3c5cddf | -12.472 | -53.14847 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d41e5311-3aa5-3d9c-8ffb-c9762baecaa7 | -12.45859 | -47.31237 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91c7e611-175b-3725-8173-9bcfb59a9730 | -12.45796 | -47.3167 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63e26252-c4d9-319c-b393-67df279f5c24 | -12.4543 | -47.31614 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 169f6fac-ea1a-3f2b-9c78-ba5446d7ad47 | -12.45277 | -63.01345 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 958f4a0a-f06b-3a85-9916-723fd5517cd0 | -12.45253 | -63.0134 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d37dffe4-31f7-37ef-b337-4cdd52df0e49 | -12.44638 | -63.01206 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27fd2ccd-1661-310c-b108-23cd92e22d07 | -12.44614 | -63.01199 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba6c5bd4-484e-3e40-ac2a-84c25d22e78f | -12.41743 | -63.0225 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README145.md)
