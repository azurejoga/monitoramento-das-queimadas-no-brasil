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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95ae434f-c411-314a-8e4f-7417acdecf48 | -12.7899 | -62.78747 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 099d8268-506d-3836-bd55-c35c287bbb9d | -12.78856 | -62.7781 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 396c72f3-6765-36ed-8d8c-63c3cf2eced1 | -12.78754 | -54.00893 | 2024-09-28 02:04:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 98b0b3ad-f79c-3b8c-8f75-96290427d0eb | -12.78723 | -62.76873 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 93017f5b-9960-3cb3-8999-7786d0a2abf9 | -12.78589 | -62.75936 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| de6323f1-5c5d-31b7-8435-67b1a6da97c6 | -12.78535 | -62.62801 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e06dc6d2-ebb6-34e8-abde-b07b0605f530 | -12.78455 | -62.74997 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6bbeafbe-0ca5-34f6-a8ec-5bb3ac622c18 | -12.78397 | -62.61856 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| eef94c6c-f0b3-3402-b037-f3ac2d7f98fb | -12.78224 | -62.79821 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d95279a9-3134-315a-949c-5a0435b80619 | -12.7809 | -62.78885 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ebe2d1df-9143-3684-ae58-ec4e71396a4d | -12.77956 | -62.77948 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 84d96172-f6a4-3789-9ff5-3fb6f73e509f | -12.77859 | -62.83696 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7670074b-fd58-331d-92ec-fd26fe6c6612 | -12.77822 | -62.77011 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 55f6f292-80c5-35d1-a770-c123a8bd75b5 | -12.77725 | -62.82763 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ba9ce173-06f6-3d7b-9578-7a125496e8b9 | -12.7763 | -62.62941 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 67a36771-5b59-33ba-a433-3d48c98f6a7c | -12.77492 | -62.61995 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1f95a715-c3e1-33b6-97d1-dd6cbad6caaa | -12.77457 | -62.80894 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 20eb783a-fd22-34b6-a99f-a029e9478ddf | -12.77324 | -62.79959 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f8b93727-226b-323e-8431-65776440367f | -12.77227 | -62.857 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 91208160-81bb-379d-b69a-33920c05c40d | -12.77093 | -62.84767 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f276288d-61eb-3a7c-80b3-e274819012d8 | -12.7696 | -62.83834 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 45fd3120-bc2d-3c92-a8d5-fd315aeffe5d | -12.76703 | -62.6275 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b6976f97-1eac-3a98-a3df-6ab9119c1ab3 | -12.76692 | -62.81967 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| deeb9bb8-1d01-3ceb-b1fa-54d35d630e61 | -12.76558 | -62.81032 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cf239ede-c3df-3495-95fd-b0ee85656798 | -12.76328 | -62.85837 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2823b655-deba-3218-aac8-e4a70f0dceaa | -12.76194 | -62.84905 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0f56dd65-d932-3bd3-96c1-6d0eb3e393f7 | -12.70582 | -54.72049 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 11516348-5533-3cef-b003-506ead7bddba | -12.70012 | -54.68765 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b21be0a5-6fc0-36a3-a317-c78474877bc3 | -12.69925 | -54.71658 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 9293ad17-4666-3e93-ad6f-bc15458d8d58 | -12.6933 | -54.68376 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 141fabfa-c9d5-3434-b32f-4e71d5b5078f | -12.69019 | -54.72396 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 163.8 |
| abaa9676-b8c5-3319-9614-ada15818d203 | -12.68443 | -54.69102 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f9dadfad-8e43-3b0f-bb05-f27c56dae8ae | -12.68363 | -54.72002 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 266.5 |
| 2de6c90a-e043-3f39-9234-b979bcd67759 | -12.67451 | -54.72715 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 9028370c-867f-3a8d-a069-022854a7c291 | -12.66874 | -54.69437 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 34da4834-1044-3fa9-a65b-5925e9f6ff89 | -12.65298 | -54.69735 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 783720fd-9b25-3e7d-b625-f958613e4810 | -12.02318 | -61.22905 | 2024-09-28 02:04:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bb220d99-8872-37e5-aa71-264903ae89ab | -12.02149 | -61.21798 | 2024-09-28 02:04:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 36ffac20-5674-3ec0-9edd-595bbd3b488e | -12.01345 | -61.23067 | 2024-09-28 02:04:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| eeb06daa-a813-323f-8f9e-83b25dc4f4c6 | -12.01174 | -61.21952 | 2024-09-28 02:04:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 34.3 |
| c868fe5c-ed0a-3876-876a-4c6399f57a5e | -12.01031 | -61.22606 | 2024-09-28 02:04:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 211e44a1-a112-3e12-afe8-af2624ed0675 | -12.00867 | -61.21489 | 2024-09-28 02:04:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ad455161-ed0c-37b6-9d22-414ce5830317 | -11.74355 | -62.55938 | 2024-09-28 02:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2a593e9-ea17-3cc0-a1d0-6af4dd1e8638 | -11.67553 | -60.21651 | 2024-09-28 02:04:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 216071dc-0f82-31b1-8371-e4b71e573234 | -11.66147 | -63.99487 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6125bfbe-eaac-3fbb-b07e-31ba327652b2 | -11.6117 | -60.35841 | 2024-09-28 02:04:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0439243a-e3e1-3115-847b-3fd4c978a1b6 | -11.60577 | -60.36515 | 2024-09-28 02:04:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 16c2f411-5cf3-3622-99a4-1f8e65b79bdf | -11.60242 | -65.02852 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbbe1a49-c06c-37fe-9ff0-b88712664e80 | -11.60131 | -60.36014 | 2024-09-28 02:04:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ddc2a218-1a73-35ca-ad97-a687cde97cbc | -11.59698 | -63.92172 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3f9e38f-8eeb-3e23-89c0-7f92f7579d6f | -11.58549 | -63.71186 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f3ad33a-64e7-3854-9570-3ccb55dd8569 | -11.56708 | -63.91364 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fdf05244-ff28-34db-833d-8a4b86f6ce17 | -11.55758 | -63.7067 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec4a6ddc-5895-3442-8680-4b4414bcf7b6 | -11.55695 | -63.90595 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a7b361c-6ea5-366f-8476-8e92db364026 | -11.53253 | -60.16584 | 2024-09-28 02:04:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ac7386d3-7244-3aaf-b8c2-e83f6dae693c | -11.51081 | -62.419 | 2024-09-28 02:04:00 | TERRA_M-M | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 598dff1d-4385-3463-8cf3-99fb8911376d | -11.33029 | -60.58232 | 2024-09-28 02:04:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fdcd7c81-72a8-3321-aef4-e0efc1dd4a28 | -11.18005 | -61.21201 | 2024-09-28 02:04:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7d3efb27-e788-3505-95a8-43b70e4a5e0b | -11.17816 | -61.20644 | 2024-09-28 02:04:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ee37280f-ed38-350e-8324-36917960b26c | -10.9124 | -60.8662 | 2024-09-28 02:04:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ddd85ce3-1248-3821-aa7a-7236d38e5967 | -10.90824 | -63.87975 | 2024-09-28 02:04:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 917ae3e4-9cc9-3807-be60-b0a3832bb396 | -10.86262 | -63.87721 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b35a3cd9-9b35-363c-abb0-18776e8197a9 | -10.63619 | -63.9746 | 2024-09-28 02:04:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c5729687-2856-3070-a1a6-175d1104be2c | -10.65 | -45.96 | 2024-09-28 02:04:24 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1387dd5-f14f-3d80-8a4e-3dfa28a89f0b | -10.57 | -46.08 | 2024-09-28 02:04:24 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac3f1d4c-b81a-3cd8-a383-50ba2eb05444 | -10.57 | -46.03 | 2024-09-28 02:04:24 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c531d5f6-655a-3731-922d-df6168720dfd | -10.6 | -46.09 | 2024-09-28 02:04:24 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acb11626-2ff5-3e75-a9d3-e4c3baddde03 | -7.87 | -44.62 | 2024-09-28 02:04:40 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa30e307-8ea0-346a-9688-205cb587475d | -13.25 | -46.34 | 2024-09-28 03:04:07 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e8bf819-003c-3be4-9bdc-4c061c37594d | -7.87 | -44.62 | 2024-09-28 03:04:42 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cbd6e8c1-955e-3b0c-9f5d-775dbe02030d | -7.87 | -44.58 | 2024-09-28 03:04:42 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a67fc6f-0e5a-3e66-ac37-7ecdac62f78b | -3.96792 | -41.51503 | 2024-09-28 03:25:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff0bd0c8-a7ee-3bde-b727-2d997ae570b6 | -5.07926 | -37.98355 | 2024-09-28 03:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e4629840-ca06-3cd8-80a1-32389427d498 | -3.9622 | -41.51407 | 2024-09-28 03:25:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc6bbd72-7ffa-332c-928b-d5b9addbbe6e | -3.29735 | -43.52153 | 2024-09-28 03:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b15b428e-cb95-3797-9dd9-2bf98ae83eaf | -3.29642 | -43.52705 | 2024-09-28 03:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d915ce3-1c74-348e-98cf-8190f0f8c73a | -3.29599 | -43.52224 | 2024-09-28 03:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1897580a-e289-365f-a7d5-70dc7bd1dd01 | -4.02484 | -43.23918 | 2024-09-28 03:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 769adb44-0fd6-389f-a2bf-2f2dd1e1c938 | -4.02398 | -43.2443 | 2024-09-28 03:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 698679fc-27e9-35fe-b8f2-f70eb719daa0 | -5.30203 | -43.07685 | 2024-09-28 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e67be206-19e4-3539-948e-5c1dd76c7c5d | -10.25854 | -43.58297 | 2024-09-28 03:28:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95ed2d0a-5240-3b22-8a59-63e6ed1d40ae | -5.90378 | -35.43883 | 2024-09-28 03:28:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c6bb424-2df6-399a-af76-c97fb5ff94b5 | -7.7825 | -34.91961 | 2024-09-28 03:28:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4beb5016-42d0-371f-9b4f-b33aa647a2b5 | -7.13895 | -38.78001 | 2024-09-28 03:28:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f8fe042b-0f0d-3e7d-88ca-e002ba562eb1 | -7.13628 | -38.7771 | 2024-09-28 03:28:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6431c734-62b2-309b-bca1-8683ce0f66c3 | -7.13547 | -38.78166 | 2024-09-28 03:28:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bfda5d1b-0bfe-37b8-9271-ed8110a539cb | -7.12997 | -38.77822 | 2024-09-28 03:28:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 865fb855-f081-366d-bec7-e5294f4c8366 | -6.93891 | -39.41792 | 2024-09-28 03:28:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3891cef8-71f6-375d-8db8-e7cb2fa7e977 | -6.93798 | -39.42324 | 2024-09-28 03:28:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6cb945f8-b966-3c0d-8e52-2319b803692d | -6.93725 | -39.4206 | 2024-09-28 03:28:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ef8f46ef-2f72-3e1d-b405-f321ddc16c3d | -9.47758 | -40.39197 | 2024-09-28 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4bb826f-773f-3087-9940-23677f8bd4cd | -9.42811 | -40.31488 | 2024-09-28 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| afa63500-2fbf-32e4-85e5-acdfb9374739 | -7.77674 | -44.68199 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| d7c40ae0-a918-37fe-8215-5d7307f4d3d0 | -9.12443 | -43.15325 | 2024-09-28 03:28:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8be21b5-3494-3bb6-9c92-bf61440e9bd7 | -6.86078 | -41.70264 | 2024-09-28 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 2745ce56-621e-3283-9886-f3ba62b20433 | -6.8604 | -41.70179 | 2024-09-28 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 42d858bf-fdfb-3d4b-86cd-4d6a1f9f2330 | -6.86014 | -41.70636 | 2024-09-28 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 11459ebc-dcc3-3f74-9b29-10387c6d6c34 | -6.85973 | -41.70551 | 2024-09-28 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 46.2 |
| c14af881-7eca-3e16-9090-e68a73e736be | -6.85462 | -41.70535 | 2024-09-28 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 17aa0b84-17d0-361d-a21a-7a2b2ee75096 | -8.11033 | -41.14965 | 2024-09-28 03:28:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
