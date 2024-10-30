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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 795c8ddb-1b00-38a9-8df1-3af6a1184b0a | -7.86804 | -46.89994 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 883e1524-855a-32a3-a5b7-700a0662fae7 | -7.86789 | -46.89812 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9edb4092-7d70-3d36-8a6f-49bd8000fec6 | -7.86734 | -46.90482 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ce826cb-7453-318a-9a60-d23dc693028b | -7.86715 | -46.90298 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5edfac9-44dc-3b8c-b306-39175ea114a8 | -7.86642 | -46.90786 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7249dfb-cded-3c6e-b6ec-387fb871689c | -7.86486 | -46.89448 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87f643d3-d06f-3ce3-a27b-ec0e41e932dd | -7.86474 | -46.89267 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a40ac96-c2c6-3b86-a6d5-09ff62d4ad71 | -7.86416 | -46.89936 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48c76a4d-cd7a-3570-918d-6926e3569f77 | -7.86401 | -46.89754 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3513cbc6-29b4-3bbb-8121-2ce53a111ca2 | -7.86346 | -46.90422 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7071c53d-0e44-3671-a7e8-01496be3d8af | -7.86328 | -46.9024 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e1d6c50-84fa-3123-ba8f-6f2acf415593 | -1.84073 | -47.09896 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aa0cb43-1c5e-3857-a836-94408c3c7005 | -1.83717 | -47.09841 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b4cd0d-a7a4-3b1d-b2e8-5e8e8027237d | -1.60024 | -47.13783 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7df3784a-1d64-36aa-892f-9a1592e71633 | -1.59962 | -47.1418 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abb86fb0-aa02-34a1-b2a6-0f33cdbac523 | -1.59608 | -47.14124 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6de98c02-32f9-3ea0-9df5-0f3aec29d1b8 | -2.72181 | -46.70176 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49d0b435-31c2-37c1-b13c-c60674f6f006 | -2.72116 | -46.70604 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 729a3a35-461a-3713-8f29-9ee0e7c4dc6d | -2.72074 | -46.68405 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 822741de-7d56-37df-8df2-f353c4ef218a | -2.71813 | -46.7012 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94cfd62f-38d2-3b77-8f90-4d8eda2af1e5 | -2.71803 | -46.68558 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 690e46f6-1fad-3aca-972d-8c4954c07dad | -2.71576 | -46.69207 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 065786b6-2a0e-3b18-a7fe-76723186ae24 | -2.71511 | -46.69635 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8582f7a9-1c1b-3856-872d-242301014299 | -2.71381 | -46.70492 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b827582-41c6-37f5-ad6b-b7b690e9634d | -2.71166 | -46.70214 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70753b7a-64c0-3c25-b7e4-30b1fc884b5b | -2.68062 | -46.73245 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c1a040b-0f01-3d85-aaec-6e727ac9b072 | -2.86044 | -46.65073 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a4a0c05-ee4e-3740-ac12-15d0348d8b3a | -2.85675 | -46.65017 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c453c0d9-38e5-33d7-902f-9528a98cec6f | -2.41958 | -46.70837 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b238ac3-5b35-3ab8-8859-5ef24169e9cb | -2.33983 | -46.47346 | 2024-10-30 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d171453-8540-35db-8f31-4433cb587aba | -2.3368 | -46.46852 | 2024-10-30 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5cda97-a73f-3f96-9dc1-e3ff83a6984e | -2.33605 | -46.64514 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71d78f36-8260-3bd6-902f-81abb34bf871 | -2.33305 | -46.64032 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20b2c5e1-d5ef-330a-953c-092b06f06408 | -2.31629 | -46.7247 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00216f2b-f67b-3f0d-8130-91774e41cb1b | -2.26607 | -46.09989 | 2024-10-30 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c0aeb08-1272-3701-a14a-cf62c3ca9b75 | -2.26569 | -46.10218 | 2024-10-30 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ed271f-a07f-3b8c-b24f-9e2efaad8275 | -2.26156 | -46.30615 | 2024-10-30 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7e17434-b347-3982-b879-8b7d091c50e9 | -2.22731 | -46.69982 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62c8859b-fb36-31e0-a990-99f962b9f3f3 | -2.19357 | -46.98832 | 2024-10-30 04:44:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699dbe90-51b5-3d26-9036-26ab97ee6ca8 | -2.18998 | -46.98777 | 2024-10-30 04:44:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba815c8e-880f-348f-b524-b2969766204c | -3.30147 | -47.02961 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 235cd169-7d28-324d-9dba-efa2eceb39b9 | -3.29784 | -47.02906 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb16261b-1efe-3ba7-bd01-ec4a6471e0db | -2.71748 | -46.70549 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ceaa75b-a7f8-3478-9b87-391bd28c5fe4 | -2.71706 | -46.68349 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85b3506b-afe7-3f3b-9927-2b9a357d1229 | -2.71668 | -46.69415 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73360deb-44db-3a7a-9094-774ba8a84888 | -2.71641 | -46.68778 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82e74642-ad70-34bf-a0ca-291e167f5812 | -2.71601 | -46.69842 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf0c7681-0202-3f08-bbec-7b3e9c95a8a6 | -2.71533 | -46.70269 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65aa6f45-583d-3680-a3ed-ca843fe06edb | -2.71446 | -46.70064 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f999eb73-c67f-3d46-9543-7f1f2eb1689c | -2.71436 | -46.68502 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48efb229-daee-3c08-8e10-bae07eb1746d | -2.71301 | -46.6936 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e99e10-0308-3a58-ae17-303b5233155f | -2.71233 | -46.69787 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0294cc1e-ebad-3a17-832b-a66425baf8d8 | -2.68129 | -46.72816 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee64c0b3-b6a6-30d4-ae87-7e84bbbf078f | -2.42088 | -46.69989 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce8930c6-1e64-32c3-8c38-5abeb4badba0 | -2.42023 | -46.70413 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b06da724-d3cd-31ad-8036-6e2011c96768 | -2.41893 | -46.71261 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 080cf7c4-eab9-3bf1-a8f0-3ea71b6b237b | -2.41722 | -46.69934 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce9239f4-2563-3e20-85a5-84166cefcf51 | -2.41657 | -46.70358 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 503d23d4-bf9a-309e-ab54-825093641efe | -2.41356 | -46.69878 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35fa7fff-2d60-3a53-8986-5c3b6ec0c7fc | -2.37102 | -47.23677 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07e1d438-e588-393e-b794-1fddf7d68f6c | -2.33972 | -46.64571 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20296512-31d1-39de-88bd-a232d053d13b | -2.33906 | -46.64996 | 2024-10-30 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99dc9245-dee6-3c15-a30d-6cd3d65a5460 | -4.50079 | -46.45681 | 2024-10-30 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07488669-310d-3362-92c6-98a3dad05d26 | -4.49699 | -46.45615 | 2024-10-30 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb451d64-1552-3dd3-a0a7-4a6b729508c7 | -4.44636 | -46.46569 | 2024-10-30 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72559c61-0802-3e31-b414-92914cdcd0ce | -4.42532 | -46.42479 | 2024-10-30 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 829dccb3-0f50-3a5b-88b8-c715aadb98c7 | -4.42081 | -46.42883 | 2024-10-30 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d6dd1c-c03b-3a5e-ad39-90fca495a955 | -4.36521 | -47.478 | 2024-10-30 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f977e4cb-f2e4-364e-bc76-e389a064cfc3 | -4.35006 | -47.30877 | 2024-10-30 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06701037-9643-37af-8fcf-f1d0d137c707 | -4.34551 | -46.36671 | 2024-10-30 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00b73853-a57b-3aeb-81fd-224cdcfdf538 | -4.23458 | -46.86814 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c1322c3-6bb4-303e-bce4-ad6c43d45de0 | -4.20034 | -46.71143 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02c51c3-1ebb-3025-90de-3258393c81db | -4.19964 | -46.71595 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48860a54-a96b-3342-928a-9cd798c99519 | -4.19659 | -46.71095 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6e16fcd-8b6b-390c-b60c-e38358c0f559 | -4.1959 | -46.71542 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ed43063-fc81-3f3c-bd99-3b13e06a891d | -4.19522 | -46.71984 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddc52bff-f559-3733-bc02-8280606300ca | -4.19286 | -46.71034 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa41d485-083d-3abc-882a-ba6378249726 | -4.19218 | -46.71476 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d56d6926-eab6-33b4-9629-7015466851ea | -4.15391 | -46.84004 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6d28f90-ab37-3237-854c-087a8abca681 | -4.15326 | -46.84429 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f345575-07be-35cf-ae36-52758ef668c6 | -4.1502 | -46.83947 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cdabc10-802b-3c9c-b987-fa3a2733d27b | -4.14955 | -46.84372 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8a7803c-a068-35e8-b274-fee79b9d88fa | -4.12865 | -47.12684 | 2024-10-30 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0da9455-ea63-33c8-bc89-54445e8f6b63 | -5.03658 | -46.94006 | 2024-10-30 04:44:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6953cab1-2b12-3d39-970d-815fb9a341a0 | -5.03354 | -46.93507 | 2024-10-30 04:44:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d6a9eb-af10-3dc6-aeb2-5725775811ee | -5.03287 | -46.93944 | 2024-10-30 04:44:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d991b5ea-5a94-3bb2-90a0-9fa9dbdd1071 | -5.0022 | -46.48512 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b205c5-e6fc-37a2-993a-8fe77c7b6517 | -4.8518 | -46.89165 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6315633-c1b8-34ea-9983-8c802d0d4203 | -4.84696 | -46.87281 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f6db687-3151-3858-9260-0980c022989d | -4.84631 | -46.87724 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07bd670a-2307-3e48-8612-f4562859ac0c | -4.84604 | -46.87423 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 599d3adb-f2d5-33ee-b611-0b583c5fad27 | -4.84322 | -46.87232 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bf22836-19ec-37af-bb64-513b4f3adeb0 | -4.73659 | -46.6576 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85d1fa90-d3dd-308d-af2c-c874c7c60c6f | -4.66805 | -46.6541 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e772f01f-5e6a-3023-8149-289fd143d687 | -4.668 | -46.65155 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c88f115-3e66-3d7b-b832-07799186c142 | -4.66732 | -46.65615 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bc5d289-d34e-379f-9cac-a4f4d73c36e3 | -4.59158 | -46.57235 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efce684d-a606-393d-aedc-97d4af74d289 | -4.58779 | -46.57173 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdf02b26-90eb-3043-b979-5999adeda6bc | -3.8595 | -47.54026 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97381b12-e89b-308b-9e97-48260fba1d1a | -3.85107 | -46.44773 | 2024-10-30 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README74.md)
