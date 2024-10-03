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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6a220c0-159b-3d00-931b-6665d49c1750 | -12.65271 | -54.07038 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f293794-7dfa-348c-8649-7bb73132dcc4 | -12.65162 | -54.0557 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c89f0a1-deab-3938-9c43-0e01d8263e1d | -12.65106 | -54.05923 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8d67bec-adaa-362f-a786-eba3ba71072c | -12.6505 | -54.06277 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40f5a278-314d-370c-84aa-894474cc4ee6 | -12.64995 | -54.06631 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 288004c8-fe06-30c5-be89-46007ef41d62 | -12.33707 | -54.09846 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 512989c5-12af-38b7-be14-819f68f87dbe | -12.33542 | -54.08731 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 418c25c8-b8c7-30a2-a683-ba20946cf58a | -12.33486 | -54.09084 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3dfa9fba-e05e-3615-b4d2-54ed1c5f4b0f | -12.3343 | -54.09438 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2e821c7-5b2d-3537-9ee9-496e62fbe111 | -12.33374 | -54.09792 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3fba594-13ba-38df-9f70-e06ed46fa96f | -12.33209 | -54.08677 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7015992a-e764-3dda-8395-d350554c19af | -12.33154 | -54.09031 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0d00ba-d767-3651-bebb-7ff83d78f1a4 | -12.32877 | -54.08622 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 628987d3-355f-315f-a1ec-b80670ea121d | -12.32821 | -54.08976 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebac5a30-a1f8-3495-8255-fd7e609c943c | -12.32765 | -54.09329 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b7f6f4e-09b4-39a5-b8f9-978523c56c69 | -12.32544 | -54.08568 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81b2ea7c-6c0a-3499-a88d-12c951db1ab7 | -12.32488 | -54.08921 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43b1f7cd-54eb-3c86-91c1-005ac88f2eb4 | -12.32432 | -54.09275 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d478ea0-f686-3d10-9bc7-4ccbba933d51 | -12.32212 | -54.08513 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3e9cc4-a1da-37d6-8f5e-6ffcf6300ce1 | -12.27232 | -53.99764 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99f944fb-1c1b-33ad-9c0d-6ba38f8a41ba | -12.26899 | -53.9971 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4634b1f-8b1c-3efd-9289-267c6b89df42 | -12.26843 | -54.00063 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc7d4e3f-d318-3139-b841-e59f0ca49a13 | -12.26567 | -53.99655 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae0dd4b-c653-386c-9268-7f4e4c633ad8 | -14.33104 | -53.15566 | 2024-10-03 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d73a0554-75a1-333c-bf4e-e8d98ca9499f | -14.32767 | -53.15512 | 2024-10-03 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 583bdd2d-9ee6-3489-bde8-c313a88feafa | -8.71344 | -54.82627 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c965ad7f-b573-3fc2-8c2a-67cde94fd4e8 | -9.65224 | -53.58192 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b60844b3-6fc6-3e4f-a10d-13bbfcee05c7 | -9.65168 | -53.58543 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7469dcd-4c8e-391b-baa9-8f2150318c43 | -9.63893 | -53.57978 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40165461-6a9e-3828-b9fd-6ca3f0af0702 | -9.6356 | -53.57925 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c59d0c49-43f1-3eb5-8973-bea97fa41b02 | -9.58576 | -54.63908 | 2024-10-03 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c511935-ec4c-36c6-94fd-bc13d473486d | -9.57196 | -54.04552 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 963c9dee-75f5-3c9a-800c-245990e4d0ea | -9.53847 | -54.80364 | 2024-10-03 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddbf65a2-9c07-3e0f-a786-c851f9ee7e26 | -10.69619 | -54.48706 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6faf1c5a-7a56-3115-b9bf-82e8bf270a56 | -10.69227 | -54.49009 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 764a0715-a8b8-34c9-a637-2b75ff283bd6 | -10.52575 | -54.59491 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b2809d0-53c8-3b52-9546-45301cd800f7 | -10.52239 | -54.59435 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df7b4cb-5d13-388e-b80b-eb3ceac99599 | -10.52181 | -54.59795 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9458c91-d36d-325d-a206-6bb4dfb80a29 | -10.44987 | -54.70089 | 2024-10-03 04:51:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1553d41-50a2-39d4-b31d-62b5f29bbe6c | -10.44903 | -54.70117 | 2024-10-03 04:51:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11a6e694-8195-31ad-922d-6b3e64c4f393 | -12.14823 | -54.26377 | 2024-10-03 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857511fe-d99c-3b88-8ccd-d03e3687f467 | -12.14767 | -54.26731 | 2024-10-03 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d79ebf18-9218-38de-9790-c87ed00cd1d1 | -11.89336 | -54.80325 | 2024-10-03 04:51:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e084c14-962e-3f4a-8217-576d81022aff | -11.54661 | -54.47844 | 2024-10-03 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 016177fe-c9b0-38da-8887-9234da1a7f0d | -11.4374 | -54.31111 | 2024-10-03 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e51691-e796-317c-baa3-444fe9a2c386 | -11.43463 | -54.30702 | 2024-10-03 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f820e2-5fbc-39b8-a134-a3c240c8082f | -11.43406 | -54.31057 | 2024-10-03 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4f71777-c29e-3f0a-9394-f6e87d0be552 | -11.43073 | -54.31002 | 2024-10-03 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 968c22b5-5000-35b5-a80d-a07ffaf4341f | -11.42796 | -54.30593 | 2024-10-03 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dba3377-369f-3a05-9290-806be17deed5 | -12.32153 | -54.11042 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65351c9f-c90e-306b-a1ff-d9309c50087c | -12.3182 | -54.10987 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc59edf1-728c-3c3b-84c1-82d4967cfb22 | -11.03403 | -53.99548 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08b173cc-32d8-3246-9750-2ec117b0ca4b | -11.03126 | -53.99141 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e188f2d6-ed48-32c7-8240-c91779a53710 | -11.0307 | -53.99493 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5bc676a-8b2e-33da-8eb3-6d846f139c26 | -12.4446 | -54.46156 | 2024-10-03 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 141564be-202e-3309-b523-d9c08b3c2b94 | -7.86615 | -55.50213 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 267848bf-139b-3b0b-a6c5-bd116aac6c94 | -7.45136 | -55.41326 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1723762-6be1-3271-8e02-3a6bf2f9cd4b | -7.44782 | -55.41271 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a7b93e3-cb3f-3d5a-b3d8-a25a696628a4 | -7.44224 | -55.46893 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fea9ff7-c29b-33a0-8d79-8624e0955fac | -7.4387 | -55.46833 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b825200a-21d7-3040-982f-084ca90c880e | -7.405 | -55.43012 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e60743c-89bf-3af2-8fd8-331fe67f5c85 | -7.40434 | -55.43409 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4f0dcdc-daa9-3078-968c-638f40579559 | -7.37829 | -55.50892 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d54ccf1a-468d-3f82-8f65-a833ff7d0fa4 | -7.37539 | -55.50436 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14faa98b-6b13-3f35-818e-eabaff94f4a2 | -7.37474 | -55.50837 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d82166f3-879c-38ea-8dd4-9d5d9eef1646 | -7.31009 | -55.30706 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bfe945d-bfeb-3af2-8a3a-3f9212527544 | -7.91337 | -54.74551 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d57d8715-271c-383b-8e53-66d781bc4d69 | -7.91277 | -54.74924 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78b56649-eb56-3c04-a320-f3da29b51b90 | -7.91217 | -54.75296 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b07f289-e79c-3d57-9d3d-a36cc64f3a3a | -7.91157 | -54.75669 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41fc8c05-9e6d-37d9-8de0-6b9c13bc8c12 | -7.90994 | -54.74495 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71228510-9151-3d16-bdfb-c4e510826dea | -7.90934 | -54.74867 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf49ac97-b6d4-3cda-ba54-2782493f26a0 | -7.90874 | -54.75239 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ee176ed-5858-39af-b4df-6f7ef060e195 | -7.90591 | -54.74811 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26926246-485a-3bf0-9397-0b503517e24b | -7.90531 | -54.75183 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0f269f6-8c9a-307b-a8bf-4150e59fd7ba | -7.90471 | -54.75555 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c2367a-c500-31ac-8b72-d16a292525fc | -7.9041 | -54.75927 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f92f14-b66e-339a-99e9-1f2c16b60332 | -7.90188 | -54.75126 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa630fe-2752-3470-ade9-d47a6b9b5c5c | -7.90127 | -54.75499 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a4568e-d908-3c01-9809-a99608690348 | -7.90067 | -54.75871 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 943a2748-3b48-3f5a-9b1c-20f755b37d3c | -7.89784 | -54.75443 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 135ed179-b05c-3cb0-adf1-39a39705acff | -7.89724 | -54.75815 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23f06461-b366-3276-9505-41b79ea30c86 | -7.89441 | -54.75387 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71f71e08-4871-3657-ac04-85b4c3a1ecd8 | -7.89381 | -54.75759 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76c96b90-0551-3844-809c-4148aac598cc | -7.61421 | -55.16566 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25458f3-050d-37c6-b39d-b30eea16e015 | -7.33543 | -55.08252 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca48921b-cbfc-37d7-9b51-be74edfea7c8 | -7.33257 | -55.07803 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cce0b7a-3c63-3ff3-a452-351d870f3539 | -7.33194 | -55.08193 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d943de-7703-3ec5-af0e-95da81576eb8 | -7.32845 | -55.08135 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 187c9c3e-b455-3f04-baa4-a619ca8c797a | -8.60402 | -54.98573 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de6c4122-8b74-3957-a45a-b149ce2bb790 | -8.60341 | -54.98948 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee078aae-00a1-3d63-9de1-72a33bd5e82e | -8.60059 | -54.98513 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e26490b4-4c66-328e-9274-2670b86665d9 | -8.59998 | -54.98887 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c514f5a-2484-3da5-8226-357d57f91ea9 | -8.50253 | -54.89978 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 351fcac3-869f-3518-81e2-e3fe5e66a3e6 | -8.50192 | -54.90351 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 665cce8c-54d5-3c46-a3a4-d57887b34ce1 | -8.48218 | -54.98126 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6315b124-c752-3bf0-b501-50863d9f7baf | -8.30739 | -55.09393 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00661e4e-1990-3440-952b-41b8abc655da | -8.17102 | -55.1586 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b20c155b-b961-304c-9ee8-78c8ddf613bd | -8.1704 | -55.16245 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d35ba65-ffc9-310b-9868-e07b3162fad0 | -8.16693 | -55.16186 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README141.md)
