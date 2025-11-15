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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5107c7e2-e7a6-30ac-8887-a8bcf200bb22 | -4.3217 | -47.570702 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc05fd2-92a2-39b4-8d67-028cd90f6be3 | -4.3457 | -46.484402 | 2025-11-15 00:18:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8737aa6-5ea9-38c3-8ce0-c728965cd8d2 | -5.3855 | -44.840199 | 2025-11-15 00:18:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad6620d8-2b72-3c22-9c33-f9fd17c3efb9 | -7.2615 | -48.041199 | 2025-11-15 00:18:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94d72126-7975-3231-ac38-92c8fb3804f0 | -4.0378 | -48.091301 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65838543-dffb-3009-af1a-7d8d4cee3c6a | -3.3325 | -45.2771 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02962e4f-beab-371c-8a68-10aea4a025fe | -10.5499 | -44.919601 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 020336d4-5267-3fbe-8ecd-488104c9a5dd | -7.0775 | -41.582699 | 2025-11-15 00:18:00 | METOP-C | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8cc25670-f320-305b-a807-18e102f83879 | -8.9946 | -44.191002 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99351da7-72f3-35c4-ac58-3622ff1e7265 | -4.3888 | -44.076 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48a02109-6e64-34cd-a358-26d0604d4edf | -4.3904 | -44.083099 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f40cf4de-e073-36d8-a98d-27b5772c2518 | -3.3787 | -46.026699 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15540286-0f03-3ee1-9503-3375dbcf2135 | -8.7363 | -44.231499 | 2025-11-15 00:18:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c982761-4771-39c6-bf97-0f7b5dfaab92 | -5.2264 | -44.362999 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3fa5f2b-87e5-3e43-966c-0937f522bdfd | -10.3225 | -49.6306 | 2025-11-15 00:18:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71b1403b-3cc3-3f42-a886-70c9cdd30fb0 | -5.5057 | -40.540401 | 2025-11-15 00:18:00 | METOP-C | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ccc4e717-6cda-3767-88f4-e8a5a91af4d1 | -8.587 | -46.0793 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 563843cb-4a84-3772-a33c-a82b563d9fe4 | -3.2239 | -45.206799 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1f83d1-b8ef-3753-b7ab-0d308d596836 | -4.4348 | -44.006599 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1a655f-8006-35d1-9259-0735ac4c9fbb | -5.3272 | -43.036598 | 2025-11-15 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04cbe744-c6c4-34ca-99ae-4835f03cf339 | -7.207 | -47.978199 | 2025-11-15 00:18:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee51e084-8880-3ff7-bd34-b88e4c9d55bd | -3.6992 | -47.632401 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b49707ac-440a-3080-8948-f4a9b7aec457 | -9.1477 | -45.1689 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9f44c9-e577-3c9b-9153-104b28653252 | -4.1053 | -45.5989 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d6a758c-a961-32a9-bb77-44ce55bed1d7 | -12.235 | -49.375401 | 2025-11-15 00:18:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1de8d726-6146-3aee-ae2d-0fcb85e18410 | -5.4181 | -43.2547 | 2025-11-15 00:18:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc8910d-8b86-3305-a24b-aa82e0a7fa3f | -7.1059 | -39.087002 | 2025-11-15 00:18:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c361ee5b-45e1-3117-91d8-21c8deb08df9 | -7.6896 | -47.183201 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5e7f979-3e01-3539-a20a-cfcc1e837e18 | -5.5106 | -40.9622 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 32540844-9c32-31c1-b251-6c8cba94d529 | -6.2802 | -41.748901 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9bb9786-6ecf-3cad-8771-59fd7cb46d1f | -12.981 | -49.783901 | 2025-11-15 00:18:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d39af106-c0bd-33d2-8b09-f37b9ef0b5c7 | -4.3639 | -45.467999 | 2025-11-15 00:18:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d68de56-93ec-3db8-ba2c-e483aa38963b | -8.9929 | -44.1833 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b258cfb-1929-3297-8a71-70d17c437787 | -3.9023 | -45.7934 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5678153a-1084-3c7f-b807-8afd2a58bcf5 | -4.8415 | -44.756001 | 2025-11-15 00:18:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74985dc0-db37-3d6a-bb9b-926de4562255 | -5.088 | -47.696602 | 2025-11-15 00:18:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a80affdd-cac4-3d98-9c0d-27e28980bc10 | -13.8896 | -42.900902 | 2025-11-15 00:18:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 55e85c0d-f5f7-3620-b126-06a9e0171891 | -5.7413 | -42.728001 | 2025-11-15 00:18:00 | METOP-C | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11897864-3ac8-3fd0-9957-76f6c2664921 | -4.7881 | -45.4324 | 2025-11-15 00:18:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8313568-08d1-3c98-851c-700e327f12c9 | -3.2838 | -45.470798 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6283b87-4397-3974-9e24-7dbeedcc7abd | -6.1356 | -48.035702 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 961dcda0-ff6c-3ff3-9699-ec239dd6663c | -4.912 | -43.2952 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 154ac7f4-e520-3e3a-bd1e-c887390ed1de | -6.2992 | -41.8316 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb42df45-1ba5-38c0-a781-8e197d93435a | -4.8535 | -43.264999 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2d2f799-4241-31ef-88d9-8e76321c9d10 | -2.5092 | -47.819801 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40888a21-3100-37de-b9ef-dd15f7b2f292 | -2.7127 | -47.401901 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a035a2-e256-3df8-80de-c5b2b321981c | -5.514 | -40.976501 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e9c031cc-4d18-3a29-ad1c-0f936892dfa9 | -3.4665 | -45.6409 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aedcdeaa-b200-32a8-acab-fb6ee3024f8c | -3.9996 | -44.177101 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c111fc47-fcb8-39f3-b12f-00fae86e2d6b | -4.8504 | -43.251202 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5db4f21b-9384-3d88-8a90-8767eccf5c71 | -4.675 | -45.844501 | 2025-11-15 00:18:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45985f1f-fe9e-3c04-8b85-e1bfec503c9a | -10.6945 | -44.4977 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76fe495b-5539-3495-9267-b355713ca42a | -9.204 | -48.590199 | 2025-11-15 00:18:00 | METOP-C | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49d1aa3f-4d5f-3bce-b2f5-f5a8b401e40f | -3.4372 | -45.920898 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d201339f-d111-38bd-bfad-09692f65f24a | -9.8609 | -44.7225 | 2025-11-15 00:18:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c4efc52-2c3c-3eb5-b368-5943bc9b1121 | -4.2152 | -45.4925 | 2025-11-15 00:18:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fed24d31-0772-3364-b420-4af54692ba8c | -4.5889 | -44.322399 | 2025-11-15 00:18:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c703733-04b4-31ad-93b2-c697f1288515 | -12.9907 | -49.782001 | 2025-11-15 00:18:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df6a0c86-fa2c-32fd-b383-773a13fa5000 | -4.9743 | -43.886902 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 436ddc2c-88a8-35f4-8d1d-dbb17fbcaa2d | -6.2833 | -41.762699 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5489add7-73ab-3ff0-84e3-d8f9ff5ef627 | -13.7376 | -43.626598 | 2025-11-15 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccfaacdb-03ab-3396-83cd-a6c870faaf5f | -14.6899 | -46.6133 | 2025-11-15 00:18:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 98f1eb10-dab5-3057-93f6-f9edfb74723b | -5.5156 | -40.9837 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 463fcd1d-0bb1-35e6-83e0-b7d0b2d61364 | -4.4183 | -43.3909 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 434b715c-a6f3-335d-9b9c-e240c5b96739 | -9.1177 | -47.119499 | 2025-11-15 00:18:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 725b2580-e35c-3d60-b86b-3b432c07e660 | -13.8913 | -42.9086 | 2025-11-15 00:18:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 71aec5d6-eeb8-3cc4-bc19-43e310bed087 | -5.4714 | -40.9711 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d809e9fb-e14e-36c5-9786-84d15bd19049 | -9.1514 | -45.186001 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e45c75b6-9a82-305e-8e06-aeb62f858487 | -4.1047 | -50.0508 | 2025-11-15 00:18:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed3ba941-605f-352c-8d40-4e883773a3e1 | -9.1155 | -43.947899 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ebdcfb33-4308-3bdc-a2af-686b8969c7e2 | -4.7863 | -45.4245 | 2025-11-15 00:18:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36b78616-e05c-39e8-9568-6f04fd90b93a | -17.5755 | -46.6936 | 2025-11-15 00:18:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b04f852f-6726-33e2-8d71-30cdb59824f0 | -11.8402 | -49.220501 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7b8c761-a6b5-3630-8d5e-cae0fd256b63 | -3.439 | -45.928902 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 381035c5-7f6d-3778-8b01-c02f5e10b3be | -4.6239 | -43.388401 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30beeb1b-847b-3e59-a063-1e12eaf57b28 | -3.998 | -47.683498 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef8ec38-4ea4-3a97-825a-b3db0d59b602 | -4.2478 | -48.205799 | 2025-11-15 00:18:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1de42df2-3bc0-33f0-afa5-d8bfaeda8287 | -9.1189 | -43.963001 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 05e37204-0c55-3dc8-a5a1-c9edf1559d0f | -7.2563 | -48.017399 | 2025-11-15 00:18:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb950675-dcb0-3ffb-b1f2-3ad96abf2e08 | -3.447 | -45.9188 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c609e70b-d360-37b5-bed5-164805d0fc4c | -14.6306 | -43.827999 | 2025-11-15 00:18:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa5ddb8b-0f5a-33d4-9514-15d48ab53a0f | -8.5751 | -46.071999 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb66f669-a7d9-3b51-ad01-8752698392ab | -16.565599 | -47.6147 | 2025-11-15 00:18:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 11a91210-66e3-3c28-8895-40de41f1be90 | -7.3518 | -47.277599 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69392574-ef61-36b9-a009-5189e93ed75d | -10.1214 | -43.894901 | 2025-11-15 00:18:00 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e756c3f-8aa2-32ad-8533-e013101002e7 | -6.2535 | -47.079399 | 2025-11-15 00:18:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb137a48-be60-35c5-b994-918563d08451 | -15.4554 | -39.2458 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6f48dac-711f-3743-a160-ac07630695c4 | -6.2976 | -41.824699 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ea9a963-be11-3b6a-8169-632ed60e9c36 | -3.274 | -45.473 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cde971ab-499e-31d0-a179-9ad76113b53d | -9.0108 | -44.171299 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee228c3-cce8-338b-9641-4de0de2ed757 | -6.1576 | -48.042999 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1f78203-7f34-3ec0-9411-d91af282691b | -6.4582 | -35.064899 | 2025-11-15 00:18:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38855b33-fad9-3688-affa-f62d40ef489c | -4.5259 | -43.23 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74432421-498b-3198-940b-262fcfc42c8b | -3.3605 | -45.445801 | 2025-11-15 00:18:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e371fe6-847e-34cd-b0fa-3d973a920718 | -4.3737 | -45.465801 | 2025-11-15 00:18:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 121f07f6-805e-3045-b0c9-7243ac318bf7 | -11.1635 | -48.129299 | 2025-11-15 00:18:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7fff304-2e08-3996-bdd3-b571d4118c6e | -3.3345 | -41.858002 | 2025-11-15 00:18:00 | METOP-C | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f0cc7144-0bb5-3410-b226-92d7b62c73e9 | -4.0861 | -42.524601 | 2025-11-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| afb9012e-e688-3027-b980-2dcd91a37c0e | -10.3142 | -44.5891 | 2025-11-15 00:18:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dfcb0cfa-99f6-3faa-b5e6-9505bc76daf8 | -4.8317 | -44.758099 | 2025-11-15 00:18:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
