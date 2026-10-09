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

## Dados Diários - Página 230

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efc6bab9-131a-3c26-b2da-606367c9d3e0 | -12.0058 | -43.464 | 2026-10-09 10:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 878c5a44-1f07-3ecb-903f-af6e0ac74b47 | -12.0054 | -43.4878 | 2026-10-09 10:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 78cbc05c-5fd7-34bd-bfc5-2888e32c8f6e | -12.0058 | -43.464 | 2026-10-09 10:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a5f00683-2529-38dd-9f41-67042df7bfdd | -11.9861 | -43.4908 | 2026-10-09 10:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 35524c86-c150-3e11-ac7b-3c61753caadc | -11.9865 | -43.4671 | 2026-10-09 10:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| f078ec7d-e980-39c8-8dee-bd415d4a3dcd | -11.4128 | -46.6897 | 2026-10-09 10:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 0d5128c6-fc0d-3140-b32d-59bcf0138731 | -12.0058 | -43.464 | 2026-10-09 10:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| cafccfc8-2d55-3623-bef0-ca6b9f151a86 | -11.9861 | -43.4908 | 2026-10-09 10:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1c87d79c-da63-3df0-9cf2-381613b8679a | -11.9865 | -43.4671 | 2026-10-09 10:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 2690ac73-453b-351f-b1c7-ca60b57702b6 | -11.4131 | -46.6671 | 2026-10-09 10:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 35323cf6-d982-3d7c-b80a-401eec677019 | -12.0058 | -43.464 | 2026-10-09 10:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 925d5553-db5a-39f7-bf4f-8ff22bb74631 | -11.4128 | -46.6897 | 2026-10-09 10:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| f0c8333f-b01d-3b38-806f-b02b8a39835d | -11.9865 | -43.4671 | 2026-10-09 10:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 83639e30-5681-3a97-b1ce-e1a35a3b3a10 | -11.4131 | -46.6671 | 2026-10-09 10:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 6d85a1e6-d50f-3461-b9ce-a482ce511b22 | -11.4319 | -46.6871 | 2026-10-09 10:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 8c84a392-ae6f-3b7e-902d-3a165ff9d717 | -11.9861 | -43.4908 | 2026-10-09 10:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a985c49c-90dc-3ad8-a01f-37dbfe27e4cd | -11.9865 | -43.4671 | 2026-10-09 11:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| cde9e7d7-7595-3c77-9c90-39b19a6cd49e | -11.5801 | -43.6492 | 2026-10-09 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8100b01a-01bf-3c24-bcbd-ba93fd681c8a | -12.0058 | -43.464 | 2026-10-09 11:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| e2b29caf-488d-3e99-abf4-3a28171ba7f1 | -11.0562 | -44.0561 | 2026-10-09 11:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f3a39efd-6d9c-3475-afe5-0b6bbf52ddf1 | -11.9865 | -43.4671 | 2026-10-09 11:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 2d51180b-629f-3a95-b143-18a4cebf2635 | -12.0058 | -43.464 | 2026-10-09 11:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| e22f3879-bd83-3729-8a57-f26ab6221166 | -11.9861 | -43.4908 | 2026-10-09 11:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ceb6aafb-fdb1-3c6a-b13a-5e92fb0b2921 | -11.4131 | -46.6671 | 2026-10-09 11:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d8765ca7-1e1b-3ebd-83f0-48bd1e14ea02 | -8.93 | -45.24 | 2026-10-09 11:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0d26a74-059d-3c39-9101-06d61ea5fe41 | -15.95 | -41.09 | 2026-10-09 11:15:00 | MSG-03 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41b2196b-6de7-316c-bb0d-30cb561a2cbc | -5.74935 | -41.34814 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2cb706da-fec5-32d1-a32f-48fce64ed9d5 | -3.98913 | -43.19427 | 2026-10-09 11:19:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fd08ea7d-1cb8-3769-a1eb-ca3d1362eec8 | -6.92617 | -45.87937 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c76e8797-2ce7-365c-aedc-dfdd8fcde8c2 | -7.10461 | -42.52534 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f0d4646c-950b-3bf3-a92f-406edf7a00d9 | -3.85384 | -44.12814 | 2026-10-09 11:19:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf3a9763-00fd-31f6-9673-95a03107b429 | -8.19848 | -45.79232 | 2026-10-09 11:19:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f54f3192-88aa-350d-94ec-d3407282fd20 | -3.04362 | -44.70139 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 89ba257d-d3c5-3b99-97ec-0b100fc5e82b | -7.48244 | -42.84197 | 2026-10-09 11:19:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 2b33bb57-fc8c-323d-bb1e-78515d04b273 | -6.9387 | -45.86794 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 224d5a8c-7c6a-3c9c-8ad3-b6582a7cbd17 | -8.09055 | -45.62038 | 2026-10-09 11:19:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 47bde219-8b5e-35c8-99f2-8433871b294a | -7.12102 | -42.53679 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8a2cc1a8-95c8-39c8-bf07-0cb2f510d6ff | -5.45726 | -42.36323 | 2026-10-09 11:19:00 | TERRA_M-M | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a86ba612-13a8-3e40-89cc-f75e46555cf3 | -3.67587 | -42.93697 | 2026-10-09 11:19:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6f8dbb7-0915-3a6c-87f3-cc7f4aa0490e | -3.56794 | -43.48768 | 2026-10-09 11:19:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b7ca2a6f-d9c4-348f-af3e-7f593854b1ab | -5.3636 | -42.88005 | 2026-10-09 11:19:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| de3e0f98-6aff-313a-a32d-3ce001e32e96 | -7.48893 | -42.79692 | 2026-10-09 11:19:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4cd96d9c-ca51-3f5d-a802-ae5379dbb377 | -5.15236 | -39.50581 | 2026-10-09 11:19:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| bad43228-d947-38dc-bb26-2d6c1ab2ab52 | -8.18265 | -46.354 | 2026-10-09 11:19:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cb373f56-ebdc-3a02-ac07-89fc82f869dc | -7.02195 | -45.30487 | 2026-10-09 11:19:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 73c753f1-6926-3e79-8b2b-2cf201f4d7bc | -3.77864 | -42.9286 | 2026-10-09 11:19:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06a772cb-33c3-3fe1-80fd-a07c552314ee | -7.11973 | -42.54573 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6db605e8-1191-3c97-8d95-b250b942c1aa | -5.43809 | -43.44964 | 2026-10-09 11:19:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 10d7e3e7-40cc-343a-8702-4d76903ae5b4 | -5.26803 | -38.22839 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 3a38c41d-83f0-3ff9-bea5-62ac25ea5dc1 | -8.30071 | -45.72655 | 2026-10-09 11:19:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5052ade3-12f8-3615-8864-ba4812ae5028 | -8.23027 | -46.40301 | 2026-10-09 11:19:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 466c2d41-88b2-384f-8c38-9d021ad83c6a | -7.47355 | -42.84068 | 2026-10-09 11:19:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 78a91dd4-dd37-37e9-a726-97ef14557572 | -6.65309 | -43.91334 | 2026-10-09 11:19:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 31d8424d-f2ed-3689-a6d5-31ef6ab669ca | -4.08288 | -44.11225 | 2026-10-09 11:19:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6257fa3d-0254-38ec-8bc5-a7ff4ae16b38 | -5.4847 | -44.26254 | 2026-10-09 11:19:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 70cbc388-d0c9-3722-b273-9108eaee3f77 | -7.58801 | -43.07351 | 2026-10-09 11:19:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 03a29045-6d6e-3595-b9d9-0e6b1ca7ecd0 | -6.93848 | -43.66216 | 2026-10-09 11:19:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5b5711e1-4a7f-3486-8821-99abc856764d | -6.33741 | -43.35525 | 2026-10-09 11:19:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ef53a6e2-8763-3105-b209-09452cf9fd05 | -8.3036 | -45.43851 | 2026-10-09 11:19:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7b14fe18-b3fe-3b23-bf6d-908f96fcdcb2 | -5.50535 | -43.04894 | 2026-10-09 11:19:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f6881f3-8f4c-3d02-8f57-a35684f64213 | -5.98548 | -41.38195 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| ab7b052c-3027-3f0e-897b-dd1a0dd465a6 | -5.71087 | -41.76072 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bb0b1a33-b610-38cc-8ad7-053e17fbb90b | -8.30239 | -45.44503 | 2026-10-09 11:19:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ba95b2e3-3fdd-3e5c-a2cb-f228a2b0c30a | -3.56645 | -43.49795 | 2026-10-09 11:19:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 04c376bc-8820-3ac7-9bdf-189a135169a5 | -8.32671 | -45.01149 | 2026-10-09 11:19:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fa0f18e6-e1dc-3c6e-a1f5-c379075921cd | -6.87978 | -45.89909 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 84f4ed89-6de2-36e5-ba95-19e422f346e5 | -7.48374 | -42.83295 | 2026-10-09 11:19:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d58a3ad5-4ce3-3788-8685-5fbc689e49dc | -5.51443 | -43.05019 | 2026-10-09 11:19:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 25da455c-9ad3-3c9e-b633-c404ac5a68e7 | -7.41178 | -44.75807 | 2026-10-09 11:19:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 11f028e9-a91c-3478-9d7d-f62ac1dc14e5 | -7.27129 | -45.56018 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 192be3f0-c9c3-306b-9522-612532b8ee52 | -5.88554 | -43.41611 | 2026-10-09 11:19:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3127936b-324b-3a83-8443-6e487e64e7cf | -6.78424 | -43.77676 | 2026-10-09 11:19:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1d9b0e1c-4a7f-39e1-96ee-7ffcb8eadd39 | -8.3042 | -45.43335 | 2026-10-09 11:19:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b9cadc31-6070-38db-8c5b-18a62ddd85e8 | -8.59673 | -44.00537 | 2026-10-09 11:19:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ef7c721c-9b0a-36f6-b836-5c55fd9f09a7 | -7.39398 | -44.74444 | 2026-10-09 11:19:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 23f6505a-0476-3d0a-a61a-bc7d788d1de4 | -7.66781 | -45.37212 | 2026-10-09 11:19:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 463cb3b4-b094-3004-8a7f-c1cc63969240 | -7.18862 | -42.00444 | 2026-10-09 11:19:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4d26c4e0-1441-34d8-989d-315790d15c75 | -8.19385 | -45.75366 | 2026-10-09 11:19:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 745ba311-7ec1-3957-acff-a6f327cb1299 | -5.97669 | -41.38073 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 68edeb70-2698-372e-8780-6e570bf8823a | -4.38806 | -43.36247 | 2026-10-09 11:19:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 448047d1-5cb4-383b-85b3-8f46226d9d62 | -7.26947 | -45.57254 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d31928a8-91f5-3dac-8f05-8c14e13bc623 | -4.75814 | -38.57855 | 2026-10-09 11:19:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6abbc084-277b-3f8b-bc47-300aa3eeee2f | -5.76496 | -42.08891 | 2026-10-09 11:19:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 63526765-8ece-3d60-8d56-8fad3574f44e | -7.6664 | -45.37782 | 2026-10-09 11:19:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a7eef174-a293-3ea1-9967-b1202adcb91c | -7.81464 | -38.82994 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 8084a3c3-894c-39ce-88bd-8b5991500819 | -7.48114 | -42.85099 | 2026-10-09 11:19:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 873ddb74-630d-3ca8-adc2-2e1684d77dc5 | -4.50032 | -43.61997 | 2026-10-09 11:19:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b1d7d22-025f-3c58-ac58-3d817e53ddfa | -7.1059 | -42.51643 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 31c5f383-15e4-3a75-b508-9aaac3db704e | -4.08611 | -44.15776 | 2026-10-09 11:19:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| aa18b583-48e5-30e8-8e4c-4c1775c0b48f | -8.30916 | -45.73993 | 2026-10-09 11:19:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 49dba282-f9f5-373c-b8e4-48d6e67266f8 | -8.84744 | -40.97106 | 2026-10-09 11:19:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8122bf45-44c9-3aa2-82e4-5a19fbf1c691 | -6.92812 | -45.86623 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 95610639-69f2-3687-b54e-ea2150cc3034 | -6.77496 | -43.77545 | 2026-10-09 11:19:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a7648d36-78c8-3ca9-b69c-0894907e3896 | -8.33254 | -45.44945 | 2026-10-09 11:19:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b279014a-171b-3979-9a7a-4f27f0644e1a | -8.33081 | -45.46079 | 2026-10-09 11:19:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e13b3169-d8ba-3514-b0d3-640d2ed3d589 | -6.93706 | -43.67178 | 2026-10-09 11:19:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3654788a-484d-3255-9efc-55ec07f0316e | -5.98673 | -41.37318 | 2026-10-09 11:19:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 23993bcc-2291-318e-a04f-86159c217e28 | -8.27838 | -45.73539 | 2026-10-09 11:19:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a92306e0-cede-3731-885e-d6fc9426f437 | -4.08775 | -44.14671 | 2026-10-09 11:19:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3a7a80f3-eed8-3a76-8d4f-8a6685df0397 | -3.55699 | -43.49659 | 2026-10-09 11:19:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README231.md)
