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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d28f02da-a43e-34eb-9eaf-c0f30c19e12e | -1.97329 | -52.11085 | 2025-11-03 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6edab1b7-30c2-3c2e-b0db-d277e9c174a4 | -2.97101 | -44.59656 | 2025-11-03 04:27:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c42f99f5-9707-3b70-8144-8173ac359a94 | -2.63391 | -47.30025 | 2025-11-03 04:27:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 059434e8-73a0-3002-af6b-52aa670bde5d | -3.01509 | -49.4434 | 2025-11-03 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 027f8c47-6047-3405-baf4-4ea7eb92facc | -5.78323 | -40.80926 | 2025-11-03 04:29:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4814d358-f26a-3201-b500-874ca1b63ea6 | -3.43179 | -51.0243 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 284cf93a-12b4-39fd-9876-716f7911de61 | -9.85547 | -44.14741 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12144efb-e266-31d7-a83c-11d881c1f4dc | -5.43021 | -46.36155 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8074f861-9d04-3a4a-bb02-bb3d7959137f | -4.96466 | -45.51461 | 2025-11-03 04:29:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b3ebb0f-6191-3b0a-90e1-be6ca47e40d7 | -4.51024 | -50.19215 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e25d2695-9470-3fc7-87b5-785c45137c7d | -6.84834 | -46.29489 | 2025-11-03 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 78b1de34-ffe5-31e1-8d7d-7b3368919856 | -3.30172 | -51.92074 | 2025-11-03 04:29:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25bd6b38-10f2-3fc2-956a-ee44cae3bad8 | -3.42764 | -51.02364 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8a03ae4-fe2b-3c37-900c-c99e3b49ba15 | -3.12087 | -51.20925 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a931144c-80c6-31a1-98c1-75ab9c836349 | -8.72666 | -44.47214 | 2025-11-03 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74860ff9-df6c-377f-aa5f-2967ac09eb9a | -5.2214 | -46.14077 | 2025-11-03 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee7c24ce-30fd-3732-bde2-a584f758c77c | -2.66191 | -54.76755 | 2025-11-03 04:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40d0305d-2576-35a7-97ed-1fab8c26df4e | -5.80932 | -42.34996 | 2025-11-03 04:29:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5cddf8c5-bd3a-3320-8901-1adce087a888 | -5.7838 | -40.80535 | 2025-11-03 04:29:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af98f8f5-46c1-3da9-b6e2-235d5703f093 | -5.46378 | -48.91292 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 194ec3da-f9a2-30e6-ab14-1bfe0fb9eb89 | -7.96365 | -39.62755 | 2025-11-03 04:29:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7c2b991-4549-3066-90d5-d652123b9a6e | -3.13705 | -51.58253 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7afd58b4-e646-3a27-85a6-2d175f00c3e0 | -5.68853 | -38.59062 | 2025-11-03 04:29:00 | NPP-375D | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c653780-a54e-37cb-b12b-053ec6afa465 | -9.90788 | -44.82253 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d7379aa-d170-3ef7-86d4-ec5cc68ed163 | -7.85405 | -46.05377 | 2025-11-03 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62fa4cfa-83ef-38a1-bf9a-cc79f072f7e6 | -5.42967 | -46.36501 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8118f130-10c7-3e4b-8c99-811901d385de | -9.18279 | -43.02293 | 2025-11-03 04:29:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d2978f43-65ff-32ce-89ba-fbeb9ce2e9b8 | -9.94185 | -44.84273 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ac7d3f5-9c60-35dc-9be0-dbba3b412781 | -5.0703 | -40.47536 | 2025-11-03 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66db5d1f-34e0-3be5-a2fa-892a6d04ae8b | -8.51297 | -44.1713 | 2025-11-03 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa3073b0-8196-3ee8-bb53-77e3c80554a6 | -5.87674 | -44.45443 | 2025-11-03 04:29:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a306c3e4-9f83-351c-9967-8648bcef4513 | -3.24112 | -50.79337 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 302c6455-4c84-37a3-9582-ebe509ec68d1 | -3.22556 | -50.58613 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f331b629-ae67-36f7-8199-94b749df7196 | -4.57576 | -44.58622 | 2025-11-03 04:29:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 296493d0-47c9-3071-b4ae-f9163f03d3de | -3.29184 | -50.19913 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e769e0fb-8cc1-3a43-aed7-2c17e4e9b378 | -7.57428 | -56.16109 | 2025-11-03 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d20ed7-3f1c-3575-a18d-88d5afd24d7f | -4.7054 | -46.44955 | 2025-11-03 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 497f03f7-cd69-3900-9bd5-fbab5f18306d | -3.12024 | -51.21313 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d9eb101-94fd-3d4b-abd6-6a19b9dae154 | -5.72157 | -42.18977 | 2025-11-03 04:29:00 | NPP-375D | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 09d60525-a3bb-30ec-af78-a3d9debbf40d | -5.65632 | -46.59663 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 388de782-32db-36f2-a572-5b99bf119c1d | -5.72226 | -42.1852 | 2025-11-03 04:29:00 | NPP-375D | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3239319f-831b-3a89-bfbe-e726f3a0d5d4 | -7.57413 | -56.16126 | 2025-11-03 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8d1a09c-9a91-344e-864a-d2028036d56c | -3.43396 | -51.50713 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14f3deee-f70a-33c1-8447-badc7d667abe | -6.68365 | -46.67432 | 2025-11-03 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 639b01dd-7231-3c69-946b-628bfe36ae54 | -5.03167 | -43.61998 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ff615b46-9996-367c-bd1e-5f52ae01f267 | -6.89437 | -40.40171 | 2025-11-03 04:29:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f25745ea-19e8-3734-a373-a3970c0760ce | -5.43299 | -46.36553 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43f68358-edb0-3da5-822c-424c3615339a | -3.43116 | -51.0281 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4184a53-003a-3ffc-a12f-0adaf5570d30 | -4.94802 | -45.51201 | 2025-11-03 04:29:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e700e003-447e-3b99-bcd6-0306d3a474c0 | -6.02728 | -46.02991 | 2025-11-03 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a4344cbd-1e2f-3b29-b0f5-eaa59d8faa56 | -5.26538 | -42.71861 | 2025-11-03 04:29:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5ce5ea54-7160-3720-a09e-74c793414e37 | -7.05734 | -39.47272 | 2025-11-03 04:29:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 862beab1-100a-3875-95a0-5cfcbe200f36 | -3.07588 | -51.24584 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ad152c6-5aa5-3d70-8987-9868877ff5c8 | -4.7923 | -50.71302 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f25e7940-7586-37f2-a593-533d7d73b300 | -5.93327 | -44.72021 | 2025-11-03 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53ca1e86-398f-3074-8053-086250916f53 | -4.96411 | -45.51809 | 2025-11-03 04:29:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a5b5026-5ae2-354e-b20e-512a0539fed5 | -6.02512 | -46.04372 | 2025-11-03 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a229bad-85be-3660-a238-2fc1f8642234 | -3.24171 | -50.78977 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c44cac4-f8d3-31a7-9acb-2a7835b2674d | -5.07086 | -40.47152 | 2025-11-03 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f0bbc7f-42ea-3131-a8a6-d9382038f84d | -3.38952 | -54.27573 | 2025-11-03 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee0ee475-c62c-3e39-b250-3ef84f6e2ade | -9.85905 | -44.14793 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 555cd7ab-3b53-39ec-ab85-d38599a2c595 | -6.10054 | -41.74282 | 2025-11-03 04:29:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 17c5e43b-e4c1-3445-baa9-6f73e9219644 | -3.4393 | -51.47527 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89244eb9-e181-332a-8957-1f8acea4286d | -9.90936 | -44.82187 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f775e70-05ca-3ee0-9583-83e8e1b2cca0 | -5.03575 | -43.61668 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7641d9c6-402e-3dfc-bc01-b8f965057ee3 | -9.09529 | -44.31997 | 2025-11-03 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5a43642-cfb3-3b5f-ab3e-596df9843923 | -5.03225 | -43.61613 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c24509d0-4f52-3c41-9455-4758a405a471 | -6.18981 | -46.39328 | 2025-11-03 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db2123f8-8515-31c0-97d3-0d33d26f957f | -3.24461 | -50.79766 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9fddfc4-2106-3332-ab34-ffe6480c15d9 | -8.19331 | -41.08795 | 2025-11-03 04:29:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95e3696d-06b4-320e-9a0c-0ee6aff23e6a | -9.93837 | -44.84218 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7f80b51-6db6-39f4-8b1a-80d6d08e3d19 | -6.10443 | -41.74359 | 2025-11-03 04:29:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8232cf86-eec7-3ad4-9c5e-15259cc3262d | -6.04192 | -46.49435 | 2025-11-03 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb9e68de-78c9-3724-9379-1f8c1d941960 | -5.77969 | -40.80451 | 2025-11-03 04:29:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3c8996fe-8e18-3ded-b60c-c373c3de4b8a | -4.65462 | -42.52246 | 2025-11-03 04:29:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b7076b0-a50e-30cb-a8d5-4e9256bbcb4e | -9.94127 | -44.8466 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 460daf26-ccc8-3086-9189-af4c1f5335aa | -6.0306 | -46.03043 | 2025-11-03 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a1b751c-b3d5-38d7-bbb9-bc7a296ced1d | -9.86142 | -44.15663 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 369a3b5d-65a8-3965-8bf6-c1ab983b2094 | -4.51619 | -50.79721 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bebfa353-8c82-3f05-ae69-bec5bc46d4f7 | -2.90727 | -53.95718 | 2025-11-03 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff1f0306-9c86-3a11-943f-e4c26039f183 | -3.42702 | -51.02742 | 2025-11-03 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a05bc4f5-4d90-388d-b59d-9a679cff8459 | -2.90676 | -53.96017 | 2025-11-03 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 869f9839-5733-329f-a8b5-760f0d48bf01 | -9.90092 | -44.82142 | 2025-11-03 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6713821-4d58-3528-9fd6-23476b96415d | -3.24521 | -50.79404 | 2025-11-03 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13468f40-34f4-3a14-8295-c2f6f5fc1280 | -4.51742 | -50.79346 | 2025-11-03 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd931a33-1da5-334f-8a29-68cd6bdb91d6 | -2.90475 | -53.95949 | 2025-11-03 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| defa8ceb-8087-3ea0-bdc6-4f9d51e046d5 | -6.68752 | -46.67138 | 2025-11-03 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae5d615f-29f7-36cf-ac91-8ea00e304ef0 | -3.01813 | -51.36668 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eea1edd-1742-393b-9f65-2fce87649274 | -4.42229 | -43.89093 | 2025-11-03 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 505e5e94-0883-33eb-ad22-68da574769bd | -8.19354 | -41.0882 | 2025-11-03 04:29:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 23e921b2-c1ea-3a1c-b3a9-e8d5d74994a9 | -5.6582 | -47.52265 | 2025-11-03 04:29:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9db8b368-775a-391c-af6e-19e021bf622f | -4.70152 | -46.45251 | 2025-11-03 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b242fd42-569f-3c79-8ef2-869681d31e89 | -5.03806 | -43.62494 | 2025-11-03 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 199c84bb-5485-340f-8824-d2ec013dd90d | -5.31769 | -45.33466 | 2025-11-03 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c86392a-b83b-3bd6-a2c6-49ba9fdfbac9 | -4.65829 | -42.52304 | 2025-11-03 04:29:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b693210d-e671-3309-a805-5eea3fdbf3d6 | -5.653 | -46.59611 | 2025-11-03 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d3690199-4505-394e-9618-bed68debf3b2 | -4.65894 | -42.51877 | 2025-11-03 04:29:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a0ec4c00-49f6-3e7f-a51a-bb4a90330e50 | -6.22096 | -42.68206 | 2025-11-03 04:29:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 8348f159-e5c2-3e9c-bdd8-292e4cad563b | -9.85783 | -44.1561 | 2025-11-03 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd7d7cce-6b7b-3a19-834d-ad649e8183fc | -3.43996 | -51.47132 | 2025-11-03 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
