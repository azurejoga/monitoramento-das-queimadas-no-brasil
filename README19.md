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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60c7c1d0-a65f-3a31-88dc-9317fd56dab8 | -9.99993 | -44.77448 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31aee617-94ee-3e5e-9880-8ade74e95719 | -3.32425 | -45.85223 | 2025-11-16 03:46:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43b7986b-213f-39b3-af09-1269b8fa06cf | -9.72969 | -43.9679 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6b0ca678-e183-3b05-bf48-0c1dd774ddb6 | -3.79297 | -43.37545 | 2025-11-16 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed51a461-49cb-3bf1-87c0-d2109db42ee5 | -9.05826 | -44.79338 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06e7db7b-5462-32fd-8e2f-750e1ebfa0a5 | -6.714 | -42.12511 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3407eee9-e65a-3323-86ba-87fe517d2b96 | -10.00014 | -44.76725 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51f9bbfe-94ae-3c18-8b58-44249a00f148 | -8.57654 | -46.06052 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abc0108e-81ad-3b5f-adca-cd73bc6f4b7a | -6.36663 | -39.62799 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a7b838a-5c9f-38b3-9f39-ff9d80ca9fa0 | -3.68254 | -40.8733 | 2025-11-16 03:46:00 | NPP-375D | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 964eec5f-8d83-3fdc-858d-081c58625a0d | -9.34655 | -46.60223 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 673a1f05-3068-3fc5-ad9b-331a2e6b663a | -7.72221 | -47.29874 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9a1a088-d2dd-3ddd-abd3-88af67e03c7b | -5.11025 | -40.72769 | 2025-11-16 03:46:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6653e447-3368-345d-966b-19ffe327e9a5 | -7.36973 | -43.31754 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ad1f23b-1eae-3e9c-b941-37a7c5bff527 | -9.45001 | -44.86364 | 2025-11-16 03:46:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83ff2840-d18b-3715-a241-849d7d63d1cb | -6.77731 | -43.54325 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaf90fbf-4660-3ef2-b899-8d14ad507218 | -6.72761 | -42.94408 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d7c2d6ad-e34b-3e3b-9f89-75490088967c | -5.48988 | -41.38002 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3b432179-c1c1-36d2-8336-b7f072b39878 | -9.74156 | -43.95872 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f946f869-60dc-3d17-a00e-cb8de42f7c02 | -7.05613 | -39.62858 | 2025-11-16 03:46:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 62507e3f-4fdf-329b-a909-ad7f9a4f731a | -4.84664 | -45.42734 | 2025-11-16 03:46:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d159da9-6b47-3cb8-a6a8-9132bd591f60 | -5.23249 | -44.35238 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35f86ace-225e-318f-8c63-b0ffa94afd28 | -7.01618 | -45.16219 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e84fd39-9cd5-33b3-a1c0-6cf5043ee758 | -6.67282 | -42.03947 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 392b1c7a-de05-3eba-b11f-4167b718f1ea | -9.06142 | -44.74711 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ad9f54d-e19a-350d-97d1-8915715bef4b | -4.36834 | -45.51178 | 2025-11-16 03:46:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff6e887-912d-33ae-8ebe-1d61356edbed | -6.8109 | -48.79381 | 2025-11-16 03:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 130acf09-618a-317f-9e98-d2276751925f | -7.36202 | -43.33303 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4276d4d-0f2b-3979-9666-a51669c4eee5 | -4.46428 | -46.30396 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d4a3511-fc4b-3fc9-aabd-d707d080e7fa | -5.47801 | -40.96413 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1f0c14e0-c730-389e-89c3-60975d870f61 | -5.68737 | -45.9929 | 2025-11-16 03:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2a1fe6c-5f6c-3b21-aed3-a23d11d3bc24 | -6.36347 | -39.62463 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e256d9a0-a0d4-3cd3-81d5-20ae478cc26d | -8.32121 | -45.40867 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4669e0e4-82cc-311f-974b-b9b32be6d9b6 | -5.85511 | -39.42599 | 2025-11-16 03:46:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4953824d-fd9b-30ba-9874-901df54b5df3 | -4.95293 | -37.39142 | 2025-11-16 03:46:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7687f98c-771e-333c-9c1a-8626ab5dbffc | -6.6986 | -40.79332 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e77203e4-6c6d-3e05-a68f-9c319b494d7f | -4.73224 | -46.37822 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 67b03314-b1a3-33d4-97a7-d567ff600aae | -9.35327 | -46.59882 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea154e78-ee97-3fe6-a456-48b26793394e | -7.19201 | -39.20975 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9b677fa5-49cb-3c95-a7fb-1450f8e46694 | -5.59308 | -38.32547 | 2025-11-16 03:46:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d3d50b0-ae69-38c3-ac9a-a28669f0d113 | -6.69667 | -40.80491 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ad29f5f-d280-3f0a-87ab-68b4c8e8370f | -7.05227 | -39.62791 | 2025-11-16 03:46:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 33ed7aa0-0be7-37b4-96ac-48029536ed85 | -8.67308 | -41.03395 | 2025-11-16 03:46:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 228bee9e-871c-35d4-8c52-93b4f3a63e69 | -6.86467 | -38.35655 | 2025-11-16 03:46:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83f2a6d4-66af-35b2-bb6b-2574aa47fe6e | -6.25983 | -47.08341 | 2025-11-16 03:46:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3da0a54-097e-3e74-b736-c35351d2ec72 | -7.19877 | -39.21569 | 2025-11-16 03:46:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 7a09af8e-d894-37a2-b849-9df39d7d7a2f | -8.41035 | -40.45827 | 2025-11-16 03:46:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7180a52e-5fdd-3405-bf3d-897bff36df63 | -9.15834 | -37.91158 | 2025-11-16 03:46:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b057924-146d-3a1f-9379-37522b6a3f14 | -6.97067 | -41.53246 | 2025-11-16 03:46:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e719f381-2207-3000-8fa3-e1ad6c4a0406 | -5.24743 | -43.91238 | 2025-11-16 03:46:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a06b5025-af96-30e0-9954-de972ea33e0e | -8.46191 | -45.13807 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd600f7f-4423-36a1-9b87-b40ced00d4e7 | -7.2479 | -42.57033 | 2025-11-16 03:46:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ac279e74-055e-370a-886b-c75063bec678 | -5.73525 | -42.72958 | 2025-11-16 03:46:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 78f63db3-21b2-3a13-9d56-b42a28a25c1a | -7.46284 | -42.54681 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 71b6bcd0-f8c4-3b18-971e-4718cd5c432c | -6.35541 | -46.15681 | 2025-11-16 03:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eecf2ba-cd32-3105-b9f7-df4cd919d78f | -6.67576 | -40.80138 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 913ec7ea-8330-3e42-9a1a-abdd09b0abc1 | -4.23068 | -44.64215 | 2025-11-16 03:46:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdd2379b-b76c-33ee-911e-f0870be2a7ab | -5.20452 | -43.47797 | 2025-11-16 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87b8a58d-3f61-3be4-92ce-f27a26ddcd6a | -7.41445 | -40.07052 | 2025-11-16 03:46:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 06a82c6e-382b-38dd-9cac-481fecd14963 | -5.51878 | -40.99586 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f59dc7b-d68b-3bff-9967-70a399cac9fb | -4.07209 | -46.34715 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 677b6bff-13e0-3c8b-b807-8245e1ea841b | -5.46884 | -40.99273 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ac2d837-0309-3e8c-8db3-fe3a16e5f793 | -2.5268 | -47.82001 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fa01ef01-9613-31dd-989b-eb61ffeb586b | -5.52308 | -40.99669 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| edbeebcb-b40c-3da7-ab8b-bc59f6edaeeb | -6.88157 | -39.66408 | 2025-11-16 03:46:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ce75b24-bddf-34a0-80ac-1261517df1c0 | -8.63481 | -39.94245 | 2025-11-16 03:46:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4676f641-9e43-3112-928c-418c9e38859b | -4.00016 | -44.26448 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6de58112-9327-36af-b715-ac1015385e9b | -9.74365 | -43.9474 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 889935a9-58c8-3d4e-a6de-c183e7dc4c15 | -4.96564 | -44.04285 | 2025-11-16 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd549713-7d8b-372f-bc64-84021ad8e53d | -5.48577 | -40.98124 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 643c91b8-b5e2-3d33-9020-f89ff829d313 | -7.84186 | -47.18023 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca1c4095-786f-30e5-8de9-45b13db98ca8 | -7.37573 | -43.31966 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 466661a1-9189-32b3-a247-79a64f721ad8 | -7.0525 | -43.95027 | 2025-11-16 03:46:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06fe2686-794d-3bb9-a6f9-f968897d1246 | -6.56352 | -39.76892 | 2025-11-16 03:46:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3af86b74-88c6-3911-b54a-d4e4d3313148 | -9.72867 | -43.96611 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8ea9f991-7e8e-3617-8198-5597aa69cede | -7.34725 | -43.33726 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b2543e1-2a05-3934-a0c4-c5669542843b | -6.13465 | -48.05325 | 2025-11-16 03:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9117bbe8-d759-3659-878c-b0e423e1d446 | -4.94941 | -37.39086 | 2025-11-16 03:46:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0b9aafcc-e81d-3b00-b9c4-8d46a8ef2a94 | -7.43941 | -45.2275 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da30df36-8b4b-3190-9b6c-29f59db31d9a | -5.99023 | -41.91655 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a13e425-16cc-312d-bb15-00b6b5d4426c | -4.84442 | -45.42665 | 2025-11-16 03:46:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 382cbf8b-aef6-3e3a-bd7e-302e988b3d9f | -6.20881 | -44.6481 | 2025-11-16 03:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2df390f9-41af-3948-8bdb-2f9777967ec5 | -5.5913 | -41.0675 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6293491a-aabd-3de8-9ce9-239e6a32f641 | -10.00624 | -44.76939 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d8b001d-6aa2-3192-a176-1406744a5370 | -4.96254 | -44.04569 | 2025-11-16 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 167cf4b2-9cf2-31bb-98ac-3a9a37ac5491 | -8.25301 | -41.43813 | 2025-11-16 03:46:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dee85e48-fcb3-33c3-b258-767c5ba177b2 | -5.42305 | -43.26014 | 2025-11-16 03:46:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d59f891b-8f19-3c99-aff2-ea5f7e3a4026 | -4.89211 | -45.02184 | 2025-11-16 03:46:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe74385f-f588-3a5e-9e7c-18a132121868 | -4.42451 | -45.55409 | 2025-11-16 03:46:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf323dcd-a266-399b-9a66-2c9d1527430e | -6.04483 | -43.53468 | 2025-11-16 03:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de458071-726e-3ff4-9ba7-c35cce384295 | -5.20559 | -43.47184 | 2025-11-16 03:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7866bae-f697-3c97-8702-0fc17b9cf290 | -6.967 | -41.52761 | 2025-11-16 03:46:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9be653d7-fe92-38a3-ae33-a3b68f048ad5 | -6.98331 | -39.16252 | 2025-11-16 03:46:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 087841d2-60dc-373d-bc6c-8ce17ba0ed34 | -6.04482 | -39.66331 | 2025-11-16 03:46:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b07c569d-1c81-3b13-accc-e2e32bc96f6d | -6.5121 | -39.5267 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 038a06c7-b69e-38d7-9dfe-2d03013eccd1 | -4.66041 | -46.74847 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05b15f8b-f3fa-3262-bbef-3ff939590f7e | -8.34181 | -41.25085 | 2025-11-16 03:46:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 44db2bdb-bc18-3407-94ec-bf11fcaf8033 | -5.32359 | -35.93063 | 2025-11-16 03:46:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 20ca7d0a-3dd8-3041-80bd-b9d39c41f286 | -5.53117 | -41.77464 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6de0121d-432b-3a83-9e84-2af25354b84b | -6.36737 | -39.62526 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |


[Clique aqui para ver as próximas entradas](README20.md)
