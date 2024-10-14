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
| 8b10d1ce-b97f-3fb5-82fd-67f93a5e0f27 | -2.77547 | -49.36573 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a734391-9c08-3674-9211-b9947c4ccb60 | -2.79304 | -49.297 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9154181-7c63-3023-bf2e-c89e63cb183d | -2.7925 | -49.3005 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b31aeae3-9904-3b91-b796-c7e3622d2f11 | -2.79025 | -49.29299 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a18539e-0092-336f-93c9-1e83cbbc63a8 | -2.7897 | -49.29648 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 007edd64-4524-3d09-80ff-9c0c27056be9 | -2.78916 | -49.29998 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11382f35-5fa7-3dfc-a746-1da54603c20d | -2.78691 | -49.29247 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b959736a-3658-3742-bf04-c58ffabbd185 | -2.78636 | -49.29596 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 64937365-ae5d-3742-aa3b-27c56f9b6385 | -2.78582 | -49.29946 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d7793b-07cd-3c47-a30f-c894da5b8de3 | -2.73051 | -49.1587 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d87643d0-9f71-31e2-9c04-52aabf8a970d | -2.72996 | -49.1622 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12d1b27d-2cf6-3bf8-9da9-15be86666cda | -2.62726 | -49.08112 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4482b2dd-9203-3977-8373-bbaaefbee3ed | -2.62281 | -49.08763 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7a116e4c-bf40-399e-9ef3-704b0f7ba651 | -2.62226 | -49.09114 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5f14e5cd-d64c-3a62-a501-3f22c08fe933 | -2.62056 | -49.08009 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bbe9074-5ef2-3b9d-bfce-0925bba1aa95 | -2.62001 | -49.0836 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1473ddb-e067-337a-a35b-89c59abdad0e | -2.61946 | -49.08711 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| eb43da3e-c7f2-3024-8cee-6da3fbdd8945 | -2.61891 | -49.09063 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ea081441-5b50-38f4-835c-4e544490a1d9 | -2.61666 | -49.08308 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 02159c78-005f-31f9-8e9b-3146fededd2f | -2.61611 | -49.08659 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9294ef03-c5c1-394d-a14c-523f46abc4af | -2.61557 | -49.09011 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fafe18ac-5de7-3751-990e-b1de4408b473 | -2.61507 | -49.1152 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e138f0f-9878-3d86-9ac3-47238e2d70fe | -2.61276 | -49.08607 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 71e78494-ecfb-33f8-8f6f-37996a8e85bc | -2.61227 | -49.11117 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59450a6c-ce12-3d69-9572-c7e479c8480c | -2.61173 | -49.11468 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6f8943b-2fc4-3b14-955b-98e626a2c226 | -2.60893 | -49.11065 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| add33153-5a09-364c-aa9a-3d274c23d8b9 | -2.60838 | -49.11416 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4713cc26-114d-37d4-84e6-d2131c3c3550 | -2.60613 | -49.10662 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fdb3be4-7b24-3b11-9bc8-b5f160da2463 | -2.60503 | -49.11364 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce38c8f0-f5b7-3d74-9086-21307a3b45e8 | -2.58705 | -49.25067 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37a8e54d-13f1-3fb6-853e-299931c48f28 | -2.53176 | -49.02334 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5c60a47f-8fa6-3f00-aed3-0aa40ac6682c | -2.5284 | -49.02282 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 248a14b7-a61e-34dd-82e8-393b6bd7802e | -2.43191 | -48.94661 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63b7400f-eb2c-3fbc-8c9d-26fb658a4132 | -2.40788 | -48.9465 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea3d52c6-ea70-3964-b3cf-2192a4f8d594 | -2.40507 | -48.94245 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 989c5108-86fc-3f21-a700-24ea67378e6d | -2.39057 | -49.14523 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f7818b2-1107-3468-99ba-a3e65fb94ca9 | -2.35308 | -49.25385 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6147f4a8-04fa-3764-87fc-59ef22ec78c5 | -2.34974 | -49.25333 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd1ff05d-8c1a-3435-bd8c-9f1f5478199a | -2.32128 | -49.09525 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38ad4e76-8bb7-33fe-8a33-d5a11436184d | -4.64534 | -50.62262 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7192b46-859a-3392-8999-ab95303278ad | -4.6448 | -50.62608 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a40b4bd-acfd-3a14-a910-a0a1338c662c | -4.64202 | -50.6221 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e126831-aa18-3680-b19f-a1281b0c9e60 | -4.5776 | -50.60139 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04fa6ca4-73ee-3028-ad1a-800346c69aa1 | -4.4873 | -50.46698 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b082511-7e11-3d0b-b01f-c01345e3a79c | -4.43493 | -50.54023 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb1c6422-1668-377c-b7c5-a02da2043973 | -4.43239 | -49.73386 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c23436e5-b35d-38a8-83a5-ff263ad1e4a0 | -4.43161 | -50.53971 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d615c66c-fe3e-3dfe-bd20-bb0b7b833ae7 | -4.43045 | -49.73311 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb2f8370-0aca-39ad-aa83-edd8c64495d7 | -4.4299 | -49.7366 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cb1a4fc-5b88-3105-bf03-d9b1f7b80229 | -4.42711 | -49.73259 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a59d90e4-c770-30d5-9c4e-18441fa1bcca | -4.40604 | -49.75793 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c2a4010-055e-36ab-98e0-97060ed8a711 | -4.4055 | -49.76143 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6d40d1d-d41c-34b2-bf26-4f4b97e3c27c | -4.40495 | -49.76492 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 531a5aec-e2ed-386a-b9e0-623af88d3633 | -4.40271 | -49.75742 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d10464f3-ed9e-3a63-ab33-ffdfcf1664ec | -4.40216 | -49.76091 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f280b5e3-9645-3299-ab7b-4be766309324 | -4.39992 | -49.75341 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a96e071-a458-304c-ae6e-8d63ec97dc6e | -4.36577 | -50.80934 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b092fd93-232a-33c1-80c0-6bb679e0d12f | -4.36353 | -50.80189 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1fa1b6-dda3-30ff-b8a9-23f5d46948e3 | -4.36299 | -50.80535 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49c96992-2a25-37c6-b0b0-afcfc76a236d | -4.35966 | -50.80483 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e2e3fef-b4bc-38b0-966f-095f06074e2f | -4.34842 | -50.50899 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 228fb405-fc00-3c03-a895-16ee7682c727 | -4.34787 | -50.51244 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb1b4168-dfd7-3d9f-8786-55f16abc9714 | -4.34733 | -50.5159 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a83b97e-e6ed-3aaf-ba74-6a9f79a6a738 | -4.34509 | -50.50847 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ea5ff02-8576-356e-81a8-19d55bab0b5a | -4.34455 | -50.51192 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69dda20b-7dc6-3d02-95a3-075f7701faa3 | -4.34401 | -50.51538 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5417ae8-48df-305b-b520-a63cbf0922f8 | -4.32784 | -50.46683 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63a9a2cc-c1c9-3dfa-acc1-c4f5b00d0206 | -4.32451 | -50.46631 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3037caca-5929-3003-bdc5-7b5e2196c1f0 | -4.32174 | -50.46233 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc4d0d0b-a184-3b61-9c87-817db3dac68e | -4.32119 | -50.46579 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61d5a483-5dc4-3e2a-b98e-90955c0c6ade | -4.26989 | -50.60239 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e7faa56-de1d-3d69-8b20-0f1f8960c4af | -4.26935 | -50.60585 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 374e6fb3-34dc-36ff-bb0e-d912f126792d | -4.26657 | -50.60187 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 815e571a-9c11-3459-aa3f-d8a5d647628c | -4.26602 | -50.60533 | 2024-10-14 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b31bdff-fb3f-39d6-bc33-92a5e80dd4ed | -3.96298 | -49.88841 | 2024-10-14 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 390dabab-2297-320e-ae11-c58bdaf55588 | -3.94711 | -49.4 | 2024-10-14 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cbcbf49-e568-3fbc-80d5-e7c5cf5f6cf5 | -3.94499 | -49.43565 | 2024-10-14 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a339a7c-b7b2-3fa9-9319-dc10480dc606 | -3.94445 | -49.43916 | 2024-10-14 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4a30fd7-d171-30d2-9692-76a2af3c1f21 | -3.64145 | -49.90952 | 2024-10-14 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7881078d-8d42-3791-b69b-3f350fe95d40 | -6.40801 | -50.77557 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 058be839-80ea-369d-9dca-3036755cfddf | -6.21504 | -50.90158 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d75f5d5-55b0-308c-bdcc-99da3f19f034 | -6.21227 | -50.8976 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b08929b5-c20f-39f7-86d6-cf87d2914a24 | -6.21172 | -50.90106 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cb94e68-495c-34ba-b902-f99c263b20ed | -6.20949 | -50.89361 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e69b6a40-a88f-3593-87cd-222d13c257fd | -6.20007 | -50.88857 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53d15c7d-e55e-3d23-a19d-1c6303918545 | -6.19825 | -50.88438 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e39c4f-8c4c-314b-855d-7f0173a91cbf | -6.19771 | -50.88785 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa6c0590-5693-33dd-a5bf-b95456b752e4 | -6.19439 | -50.88733 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e92142b7-ae9f-3626-ab6b-786f54200732 | -6.19384 | -50.89079 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e65b3c6-9422-3a25-ba91-6245413c7150 | -6.19052 | -50.89027 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0453549-22c3-3c84-af83-5608c71cae1b | -6.16181 | -50.92126 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ba8b364-7969-3e11-ac7a-09b17139b9d1 | -5.95535 | -50.16699 | 2024-10-14 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec8c11b-2858-3753-bb77-9493d50e031b | -5.91964 | -50.11136 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55053144-36c2-3b06-aff2-d559ece38f9e | -5.49958 | -50.52616 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3031e13-7463-3a45-93f7-374528af0a65 | -5.46709 | -50.64875 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 523a3d71-e467-3ff3-baf7-c436dd69bf4a | -5.21176 | -49.99037 | 2024-10-14 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b3274ce-933c-3084-aaa1-f6016f51be2f | -5.17162 | -50.11611 | 2024-10-14 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba5377d7-518a-3068-a1fd-6be49f08d16b | -7.76401 | -50.56395 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 464ade18-32b1-306b-ae01-3dda290f62fb | -7.76346 | -50.56745 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3588119-4883-34b0-8ac5-7600651c17b0 | -7.76067 | -50.56343 | 2024-10-14 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README84.md)
