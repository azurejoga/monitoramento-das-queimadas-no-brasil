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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5ed80da-9ede-35da-9b1b-1899ad88132b | -12.2445 | -50.7271 | 2026-09-26 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| bb70b10a-bb7a-34e3-ad06-91ebcfbe3025 | -12.3706 | -62.4459 | 2026-09-26 16:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 675745ff-3baf-3dd1-bc9b-a05ec922a04a | -1.3008 | -49.0826 | 2026-09-26 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| f85d4814-9ef8-367a-834a-46f3c41d9845 | -1.3008 | -49.0613 | 2026-09-26 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0e93500b-31c8-3659-91e4-abf1c15a502d | -11.8559 | -49.979 | 2026-09-26 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c3fdabd4-a708-3cf9-a61e-4e4770d7b97b | -12.8059 | -54.0255 | 2026-09-26 17:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b5951a8d-57ee-3d6d-b8a7-bd9bda38c759 | -12.2445 | -50.7271 | 2026-09-26 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| c3d0b777-3da5-38f1-b56c-4bf00bef7e25 | -1.3008 | -49.0826 | 2026-09-26 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2b30912f-8659-3008-b1c0-247e9d2a6cb9 | -1.2085 | -49.0838 | 2026-09-26 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f6edf808-5286-3829-b2e7-793c4b4e2eef | -1.19 | -49.1266 | 2026-09-26 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3bde9e20-e547-3eb7-b8cc-cfa6d79c350b | -12.1027 | -50.0355 | 2026-09-26 17:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 46b277eb-f8f3-3f74-b8dc-4eae8caba375 | -1.3562 | -49.0392 | 2026-09-26 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 578ed545-cc6b-3004-a061-246d1033ccf2 | -12.2057 | -50.7745 | 2026-09-26 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 9eccc467-4943-3bca-81e8-e50ffaf85742 | -1.3008 | -49.0826 | 2026-09-26 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 48873cf1-fd6b-3dd6-9dc2-5bc77922aadd | -1.1715 | -49.1268 | 2026-09-26 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0c4d47d3-17e4-3d7e-bc2e-ef015588c4ae | -1.2085 | -49.0838 | 2026-09-26 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d3efe4dd-6a27-3288-9b27-785ebe99db19 | 1.6382 | -55.9624 | 2026-09-26 17:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 613b4df6-c736-3863-9938-7ffd828f1adb | -1.19 | -49.1266 | 2026-09-26 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 96346a7d-e795-37ba-9635-e66d43c7661f | 1.5835 | -55.8448 | 2026-09-26 17:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 6988c26c-520f-3061-93f5-819e84bdb4bb | -12.2254 | -50.7294 | 2026-09-26 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| f1155bf2-d11b-3efd-b770-bfc926e6c622 | -14.06 | -46.3 | 2026-09-26 17:15:00 | MSG-03 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 58bab891-ca43-30e7-9008-791c20f370a3 | -5.04 | -37.72 | 2026-09-26 17:15:00 | MSG-03 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dbeb6e1e-33af-3ccb-b6a4-1f84877db2d4 | 1.6382 | -55.9624 | 2026-09-26 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 35a9ea14-69ce-3764-b8cd-0c75b8578bdb | -12.2254 | -50.7294 | 2026-09-26 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 3c40205c-ed84-38ea-b9bf-b1ea2f40c299 | -1.3008 | -49.0613 | 2026-09-26 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 23c2490d-69d6-3bdc-b133-fa1d04ec9726 | -11.6951 | -50.556 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 5f8231c4-f6f3-35f6-a692-f8b461f36b42 | -11.7329 | -50.573 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| e0a5ced0-652b-3ba5-a709-0a83546768a5 | -11.8472 | -50.5598 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| be7bf8fd-f3cd-303f-8e32-d0827f1e1829 | 1.6382 | -55.982 | 2026-09-26 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 58c45d0d-a0fc-3f17-85d7-c49c09cea749 | -12.2248 | -50.7722 | 2026-09-26 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c5e7efb3-86a6-3fb9-bc4f-291dd9555346 | -11.6954 | -50.5345 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| f3020850-b49e-3e50-842d-b09dfc77a430 | -12.2053 | -50.7959 | 2026-09-26 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 5a8c21af-e5d6-3dd7-a93d-46c9f0316f28 | 1.6565 | -55.9621 | 2026-09-26 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 77fa9394-faf7-3209-aaea-117384cbee2e | -12.7767 | -50.8766 | 2026-09-26 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| df07389e-da84-3061-a125-b68aa8078c2a | -12.0599 | -50.3419 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 651637af-910c-314b-a9c1-8483bffa5005 | 1.6199 | -56.002 | 2026-09-26 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 3f2346ac-c599-3aab-9be4-950a316630de | -11.6377 | -50.5839 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| cf361366-688b-36e4-982f-af0bca0b0774 | -1.2085 | -49.0838 | 2026-09-26 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5c04d768-3145-366a-87a7-4b5508668017 | -12.7958 | -50.8742 | 2026-09-26 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| e07a820b-3094-32a9-ac6b-cb13fd50035b | -11.8014 | -49.8129 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 5466fec3-0e75-35cb-8ab5-b9b7b5e17a07 | -1.3008 | -49.0826 | 2026-09-26 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 59970256-081f-3823-b172-d642cf726423 | -11.7138 | -50.5752 | 2026-09-26 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| ca9ccc3b-e6f8-3850-8061-807ea9570cda | -11.8475 | -50.5384 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7d8cd97d-088a-312a-b86b-86134554fc6a | -12.7958 | -50.8742 | 2026-09-26 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e625fb19-d64f-35d6-88d0-b1e2ddc4ede4 | -11.0802 | -54.0302 | 2026-09-26 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e2cd352d-ea2c-3157-a0d7-b62a2ccd58b7 | -12.8059 | -54.0255 | 2026-09-26 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 660be934-ca12-36e6-865a-94865080ef19 | -11.7325 | -50.5944 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 09d91fd3-ca30-3818-ae4e-026a7444f363 | -11.6377 | -50.5839 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 8ec8e1cf-386b-3c54-b7c8-7ccb7868568f | -11.7138 | -50.5752 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 83fb85d3-bac8-3883-89d5-b6692a3692ca | 1.5835 | -55.8448 | 2026-09-26 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2fe95f37-67b3-3122-b6df-c0b4fa6eef51 | -12.022 | -50.3249 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 3a485236-156a-3c19-aeb0-108efbebcb72 | -12.3286 | -50.2234 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 88831038-416f-3b07-a44b-2058bff75845 | -1.3932 | -49.0387 | 2026-09-26 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 3c4ce485-83c1-3d86-86af-df5864b8f72d | -10.7115 | -60.7312 | 2026-09-26 17:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e75a0e10-1be0-3bad-aa16-ced682ddab3f | -10.6928 | -60.7322 | 2026-09-26 17:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 87b88957-1f8e-3f2e-8d43-43b2c5f19eaf | -11.6186 | -50.5861 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5569d75c-d0fc-3cf0-885d-10d95a6ff2fe | 1.6199 | -56.002 | 2026-09-26 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 10516562-9eef-3617-9721-8667ef1d809e | -11.6321 | -50.9683 | 2026-09-26 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 97af38df-5482-3f59-92a7-785d74860ad8 | -11.7522 | -50.5494 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f84c6aea-8409-3379-b1c3-a3dc0458fdb9 | 1.6198 | -56.0216 | 2026-09-26 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3d951f23-824f-3190-99db-1d4bb7c6de93 | -11.3046 | -51.3222 | 2026-09-26 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 26c99441-8e84-39e5-a2ea-d7e6da110abc | -11.8014 | -49.8129 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| e1a0e8bf-9d42-3ab1-8f1e-5f2c18d89b01 | -11.6954 | -50.5345 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 83cc7c6b-c81e-307d-9593-e4966bd8c6bc | -11.7135 | -50.5966 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 888e49b5-a91a-3546-895b-1ae515ac352f | -12.0803 | -50.2535 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 40e3df23-6bc1-3f6a-8a0e-058f6f2d10ef | -12.2445 | -50.7271 | 2026-09-26 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 67589c83-ed1c-3773-8e87-b1a87ed84c90 | 1.6565 | -55.9621 | 2026-09-26 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 53406310-55a2-3077-adae-847bffcf6286 | -11.2465 | -51.413 | 2026-09-26 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 1529d966-f8dd-3e19-a162-838c18f5cee3 | 1.6015 | -56.0219 | 2026-09-26 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| b49e2487-d6ef-3b18-aa13-48cf3911fb73 | -1.4301 | -49.0382 | 2026-09-26 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 6754eb02-60dd-30eb-a0a2-688ad2badf64 | -11.6511 | -50.9662 | 2026-09-26 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 6476be02-c5c0-3732-8a28-4b657c105435 | -1.4116 | -49.0597 | 2026-09-26 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2b9a9cb7-fc6e-3bf7-8084-f7f8b7fc93f8 | -12.2827 | -50.7226 | 2026-09-26 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 58b0f9e1-1d73-38d7-b54f-ec073e00d233 | -12.2636 | -50.7248 | 2026-09-26 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 471f4688-4545-342d-8fb3-04f0eedee437 | 1.1316 | -51.185 | 2026-09-26 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c13343d1-638a-36aa-8ba8-781c644df75e | -11.6567 | -50.5817 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 6e7036b7-09d1-311c-83ce-6aa94d94c33c | -12.2508 | -50.3189 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| c58fe3a8-fdef-33c1-aa81-dded8a1ac042 | -12.0365 | -50.6233 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| cf9b1b68-42b5-3954-b673-092ed5890013 | -1.0976 | -49.2127 | 2026-09-26 17:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c4bafb44-5e3d-34e0-a0ce-363e1da7c6e6 | 1.6018 | -55.8446 | 2026-09-26 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 261d9af7-161d-3f95-9bfb-226bd5fdd10c | -11.2657 | -51.3898 | 2026-09-26 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 417af71e-23e0-3749-895e-b2445143bee0 | -11.7107 | -50.7891 | 2026-09-26 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| aac6e706-63a3-3336-b7f1-3ff39fa0769b | -11.6951 | -50.556 | 2026-09-26 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| ff78e263-8d15-3ef7-9eca-b81a69213703 | -10.6928 | -60.7322 | 2026-09-26 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9508d534-d240-3960-8a6f-9735388c7684 | 1.6381 | -56.0214 | 2026-09-26 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| ba261b63-7eb2-3ccd-8650-15cf650d799a | -11.6183 | -50.6075 | 2026-09-26 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| bdd8555d-add6-3b2a-becb-7bb63671a8b2 | -10.7115 | -60.7312 | 2026-09-26 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 03569f74-73be-3869-9744-af17cf5b0cec | 1.6018 | -55.8446 | 2026-09-26 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 97a704ce-84e0-3f6f-945c-119de579aca3 | -11.8665 | -50.5362 | 2026-09-26 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a8bdf81b-a247-3aec-b9d1-e36a46584ddb | -11.8281 | -50.562 | 2026-09-26 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 9e7f32fe-ad98-389b-9a74-791f63ec0790 | 1.2794 | -50.851 | 2026-09-26 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 2c7e51f8-1b43-3061-ae35-e7dc646c5f67 | -12.0171 | -50.647 | 2026-09-26 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 0fd4b3ae-2069-3da3-920d-6b0e109bd252 | -11.8472 | -50.5598 | 2026-09-26 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| bba722bb-c46f-3afb-9be8-a059c77a8909 | -11.6714 | -50.8788 | 2026-09-26 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 1a6164e9-878e-3652-aed7-8f00b14da8bb | -1.4116 | -49.0384 | 2026-09-26 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c9c08398-a2fb-3aa2-9755-af4d024e5efb | -1.3008 | -49.0826 | 2026-09-26 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2d946fcb-8237-3e67-892c-af5190dfbad5 | -11.5993 | -50.6096 | 2026-09-26 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 021f97a3-1952-334d-adb6-c50cccbf7099 | -12.815 | -50.8718 | 2026-09-26 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 05463599-7a24-3e17-afe3-f7ca8d5a96e5 | 1.5834 | -55.8645 | 2026-09-26 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a66f16ec-b6c0-3a11-b3e6-6296667bb564 | -12.7767 | -50.8766 | 2026-09-26 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |


[Clique aqui para ver as próximas entradas](README42.md)
