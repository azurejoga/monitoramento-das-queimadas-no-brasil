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
| 8d9cd0b2-1721-355a-8a49-66411c97b595 | -7.42337 | -42.76282 | 2025-11-16 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f1241899-8756-35e5-95c9-3ea450f4c3cf | -9.01575 | -44.82915 | 2025-11-16 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 385eca60-5ec5-334b-998e-15043d3d9c7c | -3.85505 | -44.02859 | 2025-11-16 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 960fbefd-37a7-3c4f-ab04-19bed49e81f9 | -5.68571 | -45.99467 | 2025-11-16 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5232ea65-f2ed-3818-b4b0-12608f25fa13 | -4.13508 | -45.37438 | 2025-11-16 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 331f8d9e-71fe-31b8-85b2-23685be563e6 | -5.74315 | -49.47304 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bf859e0a-d591-30c7-9904-6d7ef9c181b7 | -3.99577 | -45.56837 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a57641a4-399b-3d80-ba42-c2d642123987 | -8.09365 | -46.03099 | 2025-11-16 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f8a74ac4-7f4e-398d-a614-6bc66c0652fa | -3.67061 | -44.81654 | 2025-11-16 00:13:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 051e7fcc-6d82-3826-b6ee-8af5152d2ce4 | -6.70655 | -42.1338 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9dad7d5d-2304-3de1-b41b-62fc38827922 | -6.69338 | -40.79458 | 2025-11-16 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| ec3a085d-ed58-3b67-87ad-d8f434d7ef8c | -7.04933 | -42.24645 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 44982900-9912-3be9-b32b-649039e9681d | -4.18064 | -45.63791 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12b8225e-8594-3284-be15-4d7fae2ebf2b | -5.47825 | -40.97248 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 7340f3f1-9dd9-3770-a766-0c278b5e88ea | -3.5774 | -44.08696 | 2025-11-16 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 18e19a41-2c0b-367f-9d23-287f093c5aa9 | -4.45738 | -41.79086 | 2025-11-16 00:13:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 2bafa675-8bb8-3cfd-a910-c99b2aaba52b | -4.93899 | -44.53203 | 2025-11-16 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 07db1a96-a94a-36b6-8ef2-ec865a9e4516 | -5.46608 | -40.97967 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| c0930661-b37a-3d03-8904-89d6bb503e47 | -8.57549 | -46.05464 | 2025-11-16 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed2939fb-64a0-3258-baca-96fb7dd380b5 | -7.26745 | -48.02117 | 2025-11-16 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| b418826e-9227-3c8c-bdfe-bd8028a129e4 | -7.72125 | -47.29083 | 2025-11-16 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 55d9d335-3e2c-3b3e-a034-b9930ca054d9 | -3.63659 | -45.16708 | 2025-11-16 00:13:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55fe09cf-4ba9-34d3-b63c-6323a5095972 | -5.99053 | -41.91988 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 3306d7a1-e06d-35f6-b927-5aac7ce55079 | -3.86998 | -46.05594 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a8863760-bc16-3da8-80a1-126181589ccf | -6.27941 | -47.44246 | 2025-11-16 00:13:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17c89cc3-8ccf-32c1-a306-3e10ad537a4a | -7.41336 | -40.07459 | 2025-11-16 00:13:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 9fbe2266-6d22-3683-a30b-067db443e3e2 | -7.0509 | -42.2575 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 682a9246-309f-39db-96d1-593ca823621b | -6.36061 | -46.14875 | 2025-11-16 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c8664616-0a3c-34f8-a17c-8e13e0d30216 | -3.84833 | -40.76136 | 2025-11-16 00:13:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 2ca23d78-152e-36e9-b29d-5699f6639478 | -9.85727 | -47.60801 | 2025-11-16 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2f048d81-ac7a-34c8-bb8f-dffc773fb858 | -9.74536 | -43.98505 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| adc3a5fa-0dc4-3869-b50c-efcd54b10fe2 | -6.40183 | -42.29444 | 2025-11-16 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 5f895198-9f36-3874-9322-a289d6e25c33 | -7.46012 | -42.5452 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 7d4271f8-8550-3ef4-9bf3-465880cae8e5 | -6.67161 | -42.03418 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 5becfb04-1376-3b88-ae7e-8757a70bf94a | -4.94026 | -44.5411 | 2025-11-16 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 744256c4-69c7-348f-ac03-4fa9087b5b40 | -6.38719 | -46.00188 | 2025-11-16 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 17ec4d00-e2b0-32e9-8801-04dae6480e43 | -5.53863 | -41.77594 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7ad55107-ce1f-3e77-81e5-81073c1b7d77 | -9.85499 | -44.70813 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 40428e0c-04df-3605-816a-edef4c7155a7 | -7.04774 | -42.23528 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| cd6f11d1-6be5-391f-b4d0-3d9b5ecd4ad4 | -6.92819 | -39.62609 | 2025-11-16 00:13:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 8cc058a6-bda2-3cb7-94d1-951f610965f7 | -8.99706 | -44.30457 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 96dd8e12-b143-35cb-8559-8faafc8bbe5c | -10.03256 | -44.0626 | 2025-11-16 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2202fb00-fcac-3862-8f2c-db656f7620c3 | -6.72086 | -42.93609 | 2025-11-16 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| fab0b73d-498a-3c18-ae57-b9684836b1ad | -9.85356 | -44.16501 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff7d43f7-ba07-3f92-9a9b-f58a31bb1879 | -9.57317 | -44.60356 | 2025-11-16 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e86ab887-cd27-3b8d-86a5-b06b514341e3 | -8.32116 | -45.40969 | 2025-11-16 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5843d50d-6e1a-3623-b8df-07c4a1e7e895 | -5.47713 | -40.97834 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 9ca433d0-e39a-333d-a4e6-cbee184fa9ae | -6.62779 | -43.70269 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9e530956-bbda-3048-bd97-815f3272c36f | -4.58753 | -45.9154 | 2025-11-16 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ed4d2dcc-056d-3973-82cb-a25068afde7a | -4.68265 | -46.73844 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1684d216-aa49-3a34-a91b-54dce20dca3c | -3.5958 | -43.28747 | 2025-11-16 00:13:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 989a1b41-46ef-3c4c-8109-3280595393ab | -4.31773 | -44.63514 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00c5cee8-2304-33cd-ac23-48c0a1ef9024 | -5.69335 | -45.98453 | 2025-11-16 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 865e2e73-c1a5-348f-8f1f-93e3ec3f5294 | -4.30601 | -46.2702 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2bfaffe-ae53-3d51-b173-e0dfa734878e | -6.30797 | -43.7838 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a486eec-fe01-3836-9361-478ac9e87ea8 | -7.71591 | -42.93865 | 2025-11-16 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 22251949-1144-305f-a674-800493867d60 | -9.05768 | -44.74151 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6086b627-12d0-3c2a-9dac-08c1bb3a213a | -4.33992 | -46.31973 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b265077c-9330-3b94-b361-650a78e294fa | -3.8712 | -46.06475 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 56c1c168-fc13-3122-bc0d-cc217800867e | -6.35918 | -39.63229 | 2025-11-16 00:13:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| f8216248-4464-3562-aa06-4b6ec81e544b | -6.92969 | -46.00484 | 2025-11-16 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0bda0a05-6b94-3441-8396-0f6749332da2 | -8.41363 | -40.45368 | 2025-11-16 00:13:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| a5586ad7-3f6e-3496-bb0b-461ac71809ec | -7.05032 | -45.93892 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c2581aa6-d8c7-3566-bdde-ad7f98c88002 | -6.44839 | -43.92894 | 2025-11-16 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8c6a7ed1-7149-3a60-b858-ae590232badc | -4.70019 | -46.3265 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02ee5a7f-d172-3a8f-9ca9-8310db98e30e | -9.64763 | -46.02147 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd341257-f02e-3386-8c57-28625e0148d0 | -8.10262 | -46.02976 | 2025-11-16 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a28bee5f-dfca-3d98-8e1e-87a885958de0 | -4.49475 | -47.66271 | 2025-11-16 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa6ab8d3-f90d-3353-b94c-c7f0e38bda48 | -3.85166 | -46.18437 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c48ab17c-1338-3d53-afec-53cb9222af8c | -6.71647 | -42.13231 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 4f542245-2a2e-3cbb-9bfd-eabc6bc7ab76 | -6.03221 | -48.18587 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 2247508f-4a23-3354-978e-5712152798ba | -4.80208 | -41.7029 | 2025-11-16 00:13:00 | TERRA_M-M | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| a84c106c-c9bc-3c07-8dff-ec870f7bc756 | -9.84742 | -47.60941 | 2025-11-16 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5a1353f5-35b3-3efc-bcc8-90551a152f77 | -3.72414 | -45.9926 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1125fc30-de82-3522-a3f1-0e1be3e503de | -4.36079 | -44.35068 | 2025-11-16 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2bc4d355-57f8-3998-a810-c1b88f3e2675 | -5.77513 | -44.38504 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 29aa52fb-c894-3c71-8ca7-3d5ca269e012 | -3.82977 | -46.02569 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| df36f94a-747e-39e4-b79b-8bbb893f2c68 | -6.59572 | -44.25894 | 2025-11-16 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa6010bd-2bd3-33f2-8435-b936eb3b7a48 | -10.54027 | -47.92197 | 2025-11-16 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 230db028-303d-318b-8796-e9e23f7e48e4 | -4.64745 | -44.61943 | 2025-11-16 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e9382341-a2c6-3f2d-8a41-2f9859f0e4c1 | -4.6901 | -46.31888 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 15d79889-8a2d-34af-a225-191997ffd233 | -9.0191 | -46.00043 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4bd67874-3ca1-31bc-ad06-5e6bfe6956ff | -3.86316 | -40.6389 | 2025-11-16 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 17.2 |
| c264c41a-f7df-3992-af0e-81505abe8d05 | -5.48947 | -46.9151 | 2025-11-16 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| b78ef2f0-9ff6-3a1c-a627-781f8f88d1cb | -3.88736 | -47.18415 | 2025-11-16 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 763c721e-5abb-3b89-bb46-d1b6a5bb6ba5 | -10.0109 | -44.76468 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dc193ce5-1062-314b-838e-72cd231ba889 | -6.67496 | -42.05695 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| f25f1506-7242-34f0-8c97-cdc36745f2e3 | -8.05254 | -43.09272 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4552f4b6-c85b-3e51-b060-da23e51daa64 | -3.66354 | -45.76523 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 814f3293-2771-3c97-98c7-6a8be61e3543 | -4.0719 | -44.58903 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 66b25ec0-943f-3919-ad7c-3c86fa34982f | -4.7431 | -46.37511 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fc26ee4b-91bf-368e-800b-7ef39ace2edf | -8.05394 | -43.10255 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.6 |
| 5ff46572-bb73-3ff6-ae4f-040e116fda84 | -9.58324 | -44.61119 | 2025-11-16 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 24f7864b-bc94-340f-aef3-e1d0705dd790 | -4.44687 | -41.79245 | 2025-11-16 00:13:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| edfacda9-2ff9-3456-8e37-e38f3978d869 | -3.58915 | -41.66524 | 2025-11-16 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 81fdfa2f-1a2e-3c5f-a833-42500fc329d7 | -7.26891 | -48.03207 | 2025-11-16 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 67d97d93-1bc7-3326-8a2f-5a48cde97e00 | -7.62935 | -38.9166 | 2025-11-16 00:13:00 | TERRA_M-M | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 68.6 |
| ab26f8ff-946f-3be0-a9ca-759affa8a2c9 | -4.00012 | -44.27401 | 2025-11-16 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 22b2e023-f38b-3fb7-8fcd-dd7c9bf71778 | -8.06179 | -43.09141 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 14beb6b2-1857-3d3a-aecd-202fde9189de | -6.33037 | -46.33438 | 2025-11-16 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README7.md)
