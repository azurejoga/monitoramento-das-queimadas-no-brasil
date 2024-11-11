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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22ce26c2-26ad-3fec-bf34-8fe41fc4971a | -2.28896 | -46.77142 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8fc622f-5605-3fdc-8280-7b7dc1037c85 | -2.40234 | -46.50751 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a29c46d-a840-302b-b7a5-a7bbb3d2baab | -3.18589 | -46.52574 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 225b949c-935f-329c-b3a8-1b976b75b0db | -3.47558 | -46.02024 | 2024-11-11 04:18:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa316e3b-f2bb-3e84-8bf5-43088f1d525f | -2.19035 | -48.3795 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| f169ab50-1dab-32a1-9787-051c60462a11 | -2.78424 | -45.96899 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90391093-1add-338a-b9c2-8e7bd6b8ff87 | -1.55323 | -51.85722 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3c2de5a-faba-3775-8c18-6aa0799d5fce | -3.47352 | -53.49062 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffe42f9b-af50-397a-92fd-37dbcb2084da | -2.36811 | -48.51498 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa02a5d8-939b-39f9-ac96-6c7eff141020 | -2.06792 | -53.30572 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 392b2f4f-c586-32d9-9544-d19685803704 | -2.38439 | -49.39535 | 2024-11-11 04:18:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dfe0a40-5653-39e7-a9a5-1ad7cb4d250f | -2.83866 | -46.64685 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fe9c9f5-5055-3f87-9956-4a3c60e2163b | -2.39059 | -46.79041 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef66753-2fa8-30ac-8848-66968570e91e | -2.52258 | -45.44393 | 2024-11-11 04:18:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da73f790-8332-3f36-9881-e3fdfd840d29 | -2.57436 | -48.13547 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 865ba792-4c95-3bfc-842f-01352d5a28e8 | -2.37053 | -46.79998 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97f73b54-1857-389f-8a53-8edd1178b706 | -1.40272 | -54.49784 | 2024-11-11 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6340be2-1c67-3dc0-81b9-733bab743077 | -1.99479 | -47.92964 | 2024-11-11 04:18:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4644380-bd29-3e41-b1fc-5597b41c4eba | -2.99399 | -46.93738 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bd401c9a-2175-36e8-829e-b767ed32bf21 | -0.88452 | -52.9316 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6b36d2-7e3b-3bcc-8dee-c5b446374c70 | -2.24431 | -46.50921 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9da9dbaf-dfd3-318c-b588-3ba8543fc22b | -0.04234 | -50.77733 | 2024-11-11 04:18:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 144b70dc-6932-3e3f-a2a4-c4ce5899b5e1 | -2.63091 | -46.16119 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3992b76c-a70e-312b-a063-2bcd8859d77f | -2.31842 | -53.88077 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 116d5086-1498-3347-982b-6ec0dc0c5714 | -3.24602 | -46.30978 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceda5ed2-433a-3ac5-96f0-353e7918517f | -3.73477 | -44.534 | 2024-11-11 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8225705e-98ef-3c0e-8f7a-3894ab546af1 | -2.26302 | -46.58618 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43c01caf-7ce2-331f-a3f9-974bdc3e4033 | -3.5292 | -45.70445 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2212ee1c-6d38-3125-9269-79cc3ab49cd8 | -2.59436 | -54.24969 | 2024-11-11 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17a1cffb-58be-31cc-901d-3f17ebf532b2 | -1.65309 | -51.90167 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dea371e-cd3d-35c3-83c6-57bd5b8d1e75 | -0.87924 | -52.93443 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df9be953-9ec8-342c-9311-9f5ab463c3c1 | -3.54233 | -43.1712 | 2024-11-11 04:18:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02f54f87-1039-35ac-9968-e0112cacd8f6 | -5.3146 | -43.73589 | 2024-11-11 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cc6c281-93a3-37ee-a2c7-2216d3a2817d | -2.66132 | -46.77879 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba216ac6-aece-3818-9a0d-2f09e8c98057 | -4.69172 | -46.42813 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b819d41d-10bb-3621-815f-eedcd0cc9815 | -3.30178 | -42.38009 | 2024-11-11 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c88b2198-3084-3942-a2e0-b42d47c052ab | -3.14176 | -45.96532 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04c1543f-40f0-3c1a-9662-f1d9534026f9 | -3.23503 | -45.37891 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c2c557e-350a-3284-80c1-5d968c6d21be | -2.73428 | -45.20884 | 2024-11-11 04:18:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd715197-da85-35de-8313-d5facea9e6dd | -2.98298 | -46.98307 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cebc138-7387-3074-a8d2-9ec077297355 | -1.63441 | -52.5473 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fdee543-4427-3e6f-a376-e1a9ae5e379b | -2.19894 | -46.40311 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f57694f6-e223-369a-8225-2037268c093b | -2.60411 | -51.71661 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d6a840a-3e6b-3834-ad04-60db5fcd85f6 | -3.11919 | -45.97334 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de47312b-4931-3382-8c9b-9b3df3c61d9f | -2.26829 | -53.74718 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79624e38-7297-3208-b8af-3360aca1aef8 | -4.08911 | -43.93827 | 2024-11-11 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aabf1523-25db-31a5-9366-60ea65f5c72e | -4.70948 | -46.38393 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb5e60c1-bea5-3ea3-9903-9534c5fa2af0 | -0.39667 | -49.96663 | 2024-11-11 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ed24310-494d-3257-9d1c-0e47cf581f83 | -3.06164 | -48.03984 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fe129fe-1aef-3e5b-ac8a-d7ef939981a4 | -2.22773 | -53.67219 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 4bcc4478-1010-3df3-803f-a0076edbab61 | -1.6104 | -52.39569 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0467709-dbc1-3ef1-8d68-60fb647d9b4a | -4.07644 | -43.95398 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f94c19d-1ee2-33ad-accc-8f32841cb00a | -3.1204 | -45.96581 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6958df5-0769-36ca-8b6c-dd6c195fc3b0 | -1.02553 | -48.8549 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10cce859-0427-34f5-a160-b8f7bd13c6d2 | -1.02492 | -48.85868 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a2c3eb3-e91b-3a23-9e91-2468bb78ef48 | -2.17329 | -46.70321 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5afa4a4-58bf-3938-89ac-20a948b24073 | -3.56706 | -52.30063 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfdc4b61-388f-398c-9bb3-bf25bdf4a768 | -2.73275 | -54.14069 | 2024-11-11 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2cf4684-d6cd-3bd8-a99d-58f7a1fcf51b | -3.92727 | -45.00507 | 2024-11-11 04:18:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89a09fb6-283d-361b-9c75-0b8b62309a2b | -2.99791 | -49.5248 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76bfeeaa-36bd-30a4-bb2e-372759edfdc4 | -2.04454 | -46.31149 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23616cb6-6d7e-3357-a236-0aa0d9ecb3ab | -3.30574 | -42.37699 | 2024-11-11 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0de40c3f-8d63-3dc7-9a05-83477af041bd | -2.06307 | -46.28593 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66e232c5-ea2c-3daa-9837-020b63ac0602 | -3.02998 | -50.98182 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e48d303b-741a-32c6-852b-087ecb99b067 | -3.53203 | -45.70868 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a9c79c47-4728-3cba-8132-b7f3594f72cf | -0.39684 | -49.96508 | 2024-11-11 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ad4b1a1-03fa-3d86-b9b2-799e66915df3 | -2.63796 | -46.8089 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1849fed-8b33-39cb-9ce0-1fa8c5a71c09 | -3.24636 | -46.48616 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 462af53d-d056-3ddb-976b-aafb2ae1e320 | -2.25179 | -53.74028 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1d12e592-a3cf-3549-a51a-4ed0715fd64b | -2.67289 | -48.65975 | 2024-11-11 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a68c0af3-fcc5-3ae9-8247-fb1de83ca3c9 | -3.20444 | -46.50018 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3705645-52da-3e1d-8a64-8d8d645a571d | -3.68326 | -45.24249 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b174eb1e-ca20-32ad-b934-abc378f4300e | -1.61126 | -54.40755 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 642a0523-956e-36d2-891f-0592ac23e2f8 | -2.40584 | -46.30379 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc3d8014-49c7-343d-8ca2-1e27d10dd8a1 | -4.90982 | -44.65835 | 2024-11-11 04:18:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637473df-999c-3aeb-80b9-8eea102ed92c | -4.02522 | -46.95832 | 2024-11-11 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2af7649-7d89-3331-8aee-aced60c52d2b | -2.41582 | -48.8596 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b1d8871-ac4b-367a-b537-55796b19783e | -0.14479 | -51.55196 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c862f703-13d6-3f35-a87a-548168e48909 | -2.17165 | -46.69024 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db2368d9-a864-3003-9142-fe115530d1c4 | -2.23013 | -48.38583 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f39ddc1-b2ef-3dff-9fce-bca1ea709aef | -2.37861 | -50.33705 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38b3a6a3-1e8d-3d83-9995-c1cfa93b5b11 | -4.6911 | -46.43197 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e474ce55-c4f8-3529-82d4-7b94182825cf | -2.17705 | -48.85136 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c039227-794d-348c-bc5a-f84e59a82b20 | -2.31386 | -50.67822 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec566852-b1ed-30c9-89ea-a648673cc737 | -2.35539 | -46.80184 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf11384a-5875-3034-9699-2c193196930d | -4.61537 | -45.9892 | 2024-11-11 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b362dd94-b0dd-3fa8-b126-016b8d9eca47 | -1.61133 | -52.3956 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98bdbfd8-f79e-30d2-9936-e2da5617f89b | -2.23461 | -53.77383 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13132dd3-c3ab-315f-8e79-c5f176c6797a | -1.87227 | -48.54928 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c09bb14-c0f1-3841-8cf2-b2da46caacce | -4.57036 | -49.59994 | 2024-11-11 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 745b2222-2d13-381f-b069-64e39ee8f530 | -0.28705 | -51.73007 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9202aaef-71b1-3074-baa5-1514d77709fe | -3.23935 | -46.52965 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66688677-b978-3095-b4de-f99417112916 | -1.98616 | -46.45016 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c89bd38-bfe6-314d-a462-4a042988f451 | -2.46237 | -53.68766 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89cc2da2-dda5-3556-b67c-838dac234499 | -2.55975 | -45.97357 | 2024-11-11 04:18:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47d6b636-6ddc-3e93-b29b-e54408b55c32 | -2.97439 | -46.99027 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19b76973-43df-3810-ba7d-3cd312d287af | -2.54014 | -47.30918 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f044e77a-b791-3ae3-8994-7e26f1204452 | -2.87209 | -46.64395 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4fa4968-2d8e-3b08-8e4c-42d2d9b3d2fb | -3.95652 | -46.71349 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adb766cb-2f1b-3543-a635-907692c00227 | -1.63495 | -52.544 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README35.md)
