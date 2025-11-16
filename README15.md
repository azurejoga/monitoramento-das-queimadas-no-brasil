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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75468727-b0ef-3525-a19d-5dc8a4d96d53 | -2.5238 | -47.8332 | 2025-11-16 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 562e8eeb-cc50-3440-b8dd-4cfa28daa706 | -2.5238 | -47.8115 | 2025-11-16 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| e3d7cb94-7a9d-3b23-98ad-d90a42a9b57f | -4.4246 | -43.4038 | 2025-11-16 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 1b9ec144-d3eb-3556-96d6-79f3776f8794 | -12.0004 | -49.2683 | 2025-11-16 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f3a41d88-aff4-3167-9e2d-5a8f51eb6d43 | -8.0703 | -43.0981 | 2025-11-16 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 5030554e-158b-3001-9219-414c388abf7f | -1.99348 | -47.35196 | 2025-11-16 03:44:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46fd33b2-53d6-321e-bcc4-53d1ef657496 | -1.93335 | -47.04121 | 2025-11-16 03:44:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e27f526e-b2f4-3d9d-b966-4c02d496c391 | -1.94117 | -47.03625 | 2025-11-16 03:44:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c9d2098-4f05-3f79-86c3-a9ff41c6adbb | -3.34504 | -40.20789 | 2025-11-16 03:44:00 | NPP-375D | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2872c62f-bd52-3580-89a4-b3cb40196d27 | -1.98657 | -47.3508 | 2025-11-16 03:44:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0a65c67-ee5c-3cf7-9890-037fb707630f | -2.48237 | -44.18925 | 2025-11-16 03:44:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f45fde2f-8a03-3724-b9e3-a52834fea80f | -2.78948 | -43.34824 | 2025-11-16 03:44:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab044808-b85c-307d-b5a3-7ba85f6d1e3e | -2.55195 | -45.34041 | 2025-11-16 03:44:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bbcf33a4-e0de-3c18-b085-4bb5c1f0af33 | -2.48432 | -44.19178 | 2025-11-16 03:44:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 291aa0f4-2faa-36db-9063-144771a55080 | -2.55272 | -45.33585 | 2025-11-16 03:44:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c78fc08d-7569-395f-892c-b55a17be6026 | -2.488 | -44.19029 | 2025-11-16 03:44:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 973d1730-16d5-3b04-850a-aadb2ed42bb5 | -1.94013 | -47.04242 | 2025-11-16 03:44:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 50c2ca9e-7325-3a97-bdfc-a19d1f7bc63a | -2.48496 | -44.18805 | 2025-11-16 03:44:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd96c702-43f9-3d1a-be7f-8c3395d5d08b | -2.14349 | -45.34579 | 2025-11-16 03:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef8c5ddd-fffa-3a8d-bf12-9d5507c6c5af | -2.14273 | -45.35039 | 2025-11-16 03:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc3854c1-183e-32b8-85e5-745cc15bcd7b | -6.85298 | -42.84115 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 09810b12-1719-39d6-805d-f64eadb503f5 | -6.67738 | -42.0402 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e1d90707-2c49-3de3-969a-1efcbf96acc6 | -7.35809 | -43.33336 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06e1bd89-f82e-31f1-9180-268069a8e120 | -6.57273 | -37.95205 | 2025-11-16 03:46:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 02cc4b7f-b4ad-3148-874e-3027423d6ab2 | -7.04993 | -42.24652 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b491c372-a632-318e-acce-1ccc9aa16953 | -9.34738 | -46.58435 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50173536-9305-38fe-be02-bc53f8e4a7b9 | -6.40042 | -42.28711 | 2025-11-16 03:46:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8aa9dc39-a811-3712-843c-a5136fa809b9 | -6.95001 | -38.71949 | 2025-11-16 03:46:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec636396-06d4-347e-aa19-e922496f52cc | -7.11276 | -42.72793 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 33e672bc-ce6b-3e77-b60b-75e16eec6778 | -7.01273 | -45.16806 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17d64f95-299c-3b92-b50c-ea314e93127a | -7.19604 | -39.20801 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 743ff2be-cb53-34c9-aaed-115247d0c2e6 | -5.34079 | -43.04777 | 2025-11-16 03:46:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 17c7fb60-9963-32da-bdc6-2830f5bca096 | -6.30567 | -43.79548 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d11671e0-f415-30f9-bb8f-43e915f97d28 | -3.83635 | -40.78267 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6cc4d1b7-99ad-3cc2-8bed-5d425f2beb3f | -6.71779 | -41.74944 | 2025-11-16 03:46:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7209c932-2ffd-3d54-bfb0-7ef2a5adec64 | -10.00449 | -44.77869 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb2f0efa-5aa6-3d07-b2b6-456a7f07a566 | -6.27602 | -41.72821 | 2025-11-16 03:46:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d03ccab8-94ca-3e3f-8055-9e427e860109 | -9.84543 | -44.17426 | 2025-11-16 03:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c88098d7-5645-3a36-8c95-20625c8079f6 | -7.00997 | -45.16477 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09bd3669-d24e-3957-aa0c-f78e2d695920 | -6.3996 | -42.2919 | 2025-11-16 03:46:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6653354d-1b26-3227-a869-05c9a888e34a | -6.95454 | -38.3996 | 2025-11-16 03:46:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57b72a27-3ade-3f45-8ff4-4c3c0c5a7b6c | -5.23913 | -44.34634 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1391b79-159e-372e-bebd-2af28d2a3979 | -4.69096 | -46.32045 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96af2275-7c47-3e30-8479-5e5c721a25d3 | -6.41516 | -41.46513 | 2025-11-16 03:46:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1586fa2-1216-341b-a39d-f0f1fec7b426 | -7.71596 | -47.29726 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82dc5700-e53d-3548-bad3-973ea1049ea0 | -7.26554 | -48.03009 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce5e61e7-4c00-370e-bc9a-56435da8e8c2 | -6.20093 | -39.73486 | 2025-11-16 03:46:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 749147f3-d5d5-3d25-91ec-10d92fa5775d | -8.58382 | -46.05354 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 492b81c2-7480-31ea-b308-6d5b04577132 | -3.66129 | -44.81647 | 2025-11-16 03:46:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72e081b5-0f2c-3af1-8d72-1330edf6df43 | -9.44907 | -44.86306 | 2025-11-16 03:46:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e7cb88e-969d-334a-b2ca-460118267252 | -6.69796 | -40.79719 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd68ecea-fecd-3ebd-ad7d-6f37ab0ec517 | -9.73665 | -43.95778 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 1c11f91b-4f71-3ff4-a174-70b4eea062f6 | -6.70149 | -40.80179 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 609def87-6d08-3b76-8274-6abca27d80d9 | -5.4723 | -40.97184 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d3dae3b-a8df-3aed-ac15-ff825fa39554 | -3.79819 | -43.37639 | 2025-11-16 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 406c9260-de24-36eb-8ea7-e100f8bc0b2e | -10.16693 | -44.50053 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80255a75-608c-36e9-bb34-5cbf9f556f7a | -5.66149 | -41.07919 | 2025-11-16 03:46:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6455fe81-7653-3590-9485-324bbfcaad5a | -6.26671 | -41.41368 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cd7414b-4e53-353c-9386-9e624eb92d3c | -7.21999 | -47.97983 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e96b600-4664-3241-b5d8-445ea441a54c | -6.71775 | -42.13058 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c9f6ddd4-6b4a-32f8-8fbc-7b87ea4a0203 | -3.95988 | -44.84571 | 2025-11-16 03:46:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6afbb229-ecfb-3203-aafc-998fad82b5d9 | -6.06186 | -41.55718 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d27c1a0e-9dd0-3c72-956d-78dfa6396bb0 | -8.90402 | -44.43323 | 2025-11-16 03:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24d32ac3-b7f3-3387-abc6-63126b63284a | -4.84003 | -45.43059 | 2025-11-16 03:46:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4affe2fc-66cd-3541-be73-07c5885888ce | -9.45367 | -44.86745 | 2025-11-16 03:46:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c888a64-7f19-3e53-a1b2-928c3f2976d2 | -4.26225 | -38.08373 | 2025-11-16 03:46:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2722a42f-744c-388d-9fb7-e15b56fa94e4 | -8.33763 | -41.24998 | 2025-11-16 03:46:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2c8fd60c-897e-3f61-ac68-9e2692a23452 | -8.75149 | -45.64605 | 2025-11-16 03:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef22c0b4-c429-3865-a897-2ee5416e5222 | -4.84365 | -45.43093 | 2025-11-16 03:46:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5736345-7ca5-31c9-8b63-c5f5ac386fd3 | -7.35123 | -43.33691 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0c16f8-a651-3800-8fd6-a6e7bfcf63f6 | -7.34626 | -43.34275 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa343662-476d-3277-ba3f-c35277bfa84b | -7.05074 | -42.24185 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b4b36dfc-ccbc-3da9-b285-4a95a6ebeaa5 | -5.51518 | -40.99092 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee7634c3-cba6-3deb-bb00-15183987f750 | -3.93432 | -47.05301 | 2025-11-16 03:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86ac5432-2e41-3321-b1e4-bd0c63e3e227 | -4.80759 | -48.3446 | 2025-11-16 03:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19cda921-6209-36df-a717-862f77f619c5 | -7.04452 | -42.25047 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9931574f-9ac3-3b32-a058-18957b7f97aa | -3.85669 | -40.76827 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe8e9082-986a-3ad2-815d-2a9cec56bd4a | -6.14261 | -48.04797 | 2025-11-16 03:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58cd92df-c77c-3312-b7a8-09b92e646664 | -10.25364 | -45.06063 | 2025-11-16 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7010037-d5b4-3d7c-aa4e-27332519f84a | -3.997 | -44.28281 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e77464f5-8514-396a-aad5-f52a26f08921 | -9.65932 | -43.90052 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1cb81b2b-65e0-3408-8b62-4e693af9d4e5 | -7.28515 | -46.7143 | 2025-11-16 03:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb4b3134-d60a-30d5-9e16-77be930de34b | -6.93481 | -39.61093 | 2025-11-16 03:46:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef62245f-7758-3f4a-b63e-4a047e872dcb | -4.75017 | -37.88482 | 2025-11-16 03:46:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5c607f1-776f-3d9f-9cb5-aa4119d2edcc | -6.28577 | -41.72513 | 2025-11-16 03:46:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c16a295-cf9b-3541-a644-e59932c4624a | -5.53038 | -41.77929 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 13d826ca-0fe4-3481-8d65-6b9e3e71607a | -7.04884 | -45.9441 | 2025-11-16 03:46:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bf2ead7-bee1-3b89-92d7-6430965db429 | -6.82515 | -39.81091 | 2025-11-16 03:46:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9a4aebe6-bbf2-3aaa-ae6e-a5025565c021 | -9.74053 | -43.96427 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6c5d2ea5-f187-30fe-9cd0-4bd5296ef065 | -7.29555 | -45.11018 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 047f64ec-895e-3858-97d4-1ba2551846cc | -9.06022 | -44.75353 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f223c27f-6b73-3365-b89e-f322eecf4a3b | -7.01342 | -45.16432 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e32a2508-d1d1-336b-8bae-1d855067c307 | -6.07399 | -42.87199 | 2025-11-16 03:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0a8e8b7a-ee90-3989-8598-facafd61428b | -6.07672 | -43.00172 | 2025-11-16 03:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0573e1b0-a73e-3b97-894a-29d0591c8b42 | -6.44884 | -42.36893 | 2025-11-16 03:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9cb2b4f4-1a88-32b3-bc7f-35b4e8985a76 | -9.34573 | -46.5929 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe2dbd85-757a-3b9f-8e4e-758600f7166d | -5.71567 | -41.40229 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6c3fccab-6101-35b5-909a-b248cd4dcc6c | -3.21768 | -43.35196 | 2025-11-16 03:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efd4991e-d956-3128-a53a-b98b615bc4f4 | -10.00584 | -44.7653 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc16aec-406c-3fc8-8174-b6c212be5e9c | -3.85159 | -40.77201 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
