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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41fedfd1-0906-3757-981b-90c2e9c15101 | -1.5128 | -54.2561 | 2026-09-06 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f203de9a-c571-33e0-a706-448fd4e48e1f | -11.2864 | -45.114 | 2026-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d4dd0526-3c5c-3f2d-ac74-c7d42637f148 | -5.4914 | -60.1953 | 2026-09-06 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 283.8 |
| 2e26ece6-6737-3044-be1c-8f18b3f07f79 | -1.4944 | -54.2362 | 2026-09-06 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| ed69517b-497a-3973-a7d2-b77ad90dfa30 | -1.4761 | -54.2365 | 2026-09-06 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 130b0589-6582-3ec8-83c6-302f473b01c9 | -1.4944 | -54.2563 | 2026-09-06 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 207.8 |
| b7d2f1cd-bead-3d11-a34e-25fc92d60fda | -4.6651 | -56.0307 | 2026-09-06 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a608c7e4-a9ca-34c0-adba-a0d8a16d184b | -5.598 | -43.9978 | 2026-09-06 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 53d7bc6c-4e4a-3164-9e57-7ac9832541c5 | -10.2025 | -50.3109 | 2026-09-06 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8419cb63-1257-33f4-a65b-ac5ad086be55 | -5.6565 | -60.2475 | 2026-09-06 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 7b6a98a5-7ce6-33de-8944-feddec837906 | -7.1372 | -42.2484 | 2026-09-06 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 1a17bce4-e1f7-3bf4-af25-d2314f3aa329 | -11.3052 | -45.1344 | 2026-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 64b32381-6360-3c08-8968-6ed2e14c12f1 | -1.4761 | -54.2565 | 2026-09-06 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 22c3bbf2-9e86-3ab6-ba52-e1109b0480ab | -5.6382 | -60.2289 | 2026-09-06 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 596c2a0d-0066-37e1-ba86-7390e5c2bc2f | -3.7645 | -61.7548 | 2026-09-06 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| fb587448-ad3b-3397-bece-d237511b3282 | -5.1623 | -55.9536 | 2026-09-06 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| acdd8572-e3bb-3199-8a68-e517c94ff135 | -3.7645 | -61.7548 | 2026-09-06 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d7996895-94c1-3a48-bc81-493186d1ff15 | -3.6215 | -60.566 | 2026-09-06 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f8132d14-8972-3746-bb5d-475199bcd19f | -6.1176 | -59.9261 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6e6d5dc6-0b6e-313d-896d-01acdfb1a637 | -7.5086 | -44.3201 | 2026-09-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f133166d-062d-3909-b3fc-6bc8278f83e5 | -3.6215 | -60.585 | 2026-09-06 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 20af0d28-b24c-3c7f-ad90-32cf53465a20 | -3.3871 | -59.4075 | 2026-09-06 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3aed1bb3-4d50-3917-8bb1-75e37ff583c2 | -5.5098 | -60.1947 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 4b38eb47-8c23-3575-a989-34ab973daf23 | -11.286 | -45.1371 | 2026-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d5505381-fd24-30c8-a8c6-30e1e70339fd | -5.6566 | -60.2284 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| d40767f7-7e5b-3e93-82a4-5d4d4d10b76e | -5.6565 | -60.2475 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 0892b2f8-3a1d-3c76-992c-a366ece99aa7 | -6.6514 | -59.945 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c5401651-805d-3de1-b92e-b801c21a7381 | -10.2818 | -50.025 | 2026-09-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 4e7af895-adf7-310b-acf1-c3a50fb2fd71 | -12.1132 | -47.0661 | 2026-09-06 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b2c9db32-589f-370d-9451-ef654698dd89 | -7.1372 | -42.2484 | 2026-09-06 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 65da373f-fbc7-3512-8834-dc998dabf598 | -5.4731 | -60.1959 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 10512d67-d8a5-3333-b39c-61b05942b609 | -5.3647 | -56.0051 | 2026-09-06 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 8172e6b0-f773-33e3-91fc-f79baeb166c3 | -5.1623 | -55.9536 | 2026-09-06 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 6804def3-573b-32dd-84a1-a5c132f9fbb5 | -5.4914 | -60.1953 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 295.8 |
| c44da03a-d71a-3dee-817d-c2bfef5a8f9f | -5.6382 | -60.2289 | 2026-09-06 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5162b419-2d0d-3a20-9f13-65c8885909e4 | -10.3154 | -50.3421 | 2026-09-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 98eb4970-3401-3df4-9d2a-36d6d22f6ef2 | -5.2897 | -60.1441 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 19627e80-bb6c-3c00-80b9-fa670af0fbc1 | -5.5098 | -60.1947 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b61980ab-8b13-3c64-abb3-fbbe6b940f9a | -11.2864 | -45.114 | 2026-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 2d1c397a-4701-3a8d-a24b-c7a253b640b5 | -10.6452 | -45.8635 | 2026-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f053da26-e68b-3744-9916-409fb2a0c746 | -3.7645 | -61.7548 | 2026-09-06 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 43690750-6b98-394a-8522-98f6203ba21c | -3.7828 | -61.7545 | 2026-09-06 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c00c990e-4eb8-31e3-bb20-a9466a00b370 | -5.2898 | -60.125 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3b801fa8-7f4a-396e-b297-5c11ae387bc4 | -8.9601 | -44.3973 | 2026-09-06 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| d778e015-cba1-3945-a72a-152be1e27a95 | -3.3871 | -59.4075 | 2026-09-06 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e67a92a2-e52e-346f-938f-2dc25fec77fd | -6.0992 | -59.9267 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b5d06113-83a2-3cf1-8b38-155d7cc7774a | -8.9787 | -44.4183 | 2026-09-06 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 22810632-e9db-3e31-98a6-64e2304ab1f7 | -5.3647 | -56.0051 | 2026-09-06 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 6044f919-8019-31da-b8a7-685b4cddc387 | -5.6566 | -60.2284 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 1d1dac0d-9fc0-3e9a-a7e5-c36544b5d806 | -5.4914 | -60.1953 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 306.3 |
| 7c6bbe53-de22-3c82-a932-f1d495048692 | -7.1372 | -42.2484 | 2026-09-06 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 1a2c779b-9de8-341b-b2bf-871f3d2e8724 | -3.1462 | -60.6317 | 2026-09-06 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3acc4b26-668c-3e29-bfcd-9543979a3e3e | -3.4269 | -58.3104 | 2026-09-06 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 22f24e61-92d3-348b-b459-efd5ed81ddac | -10.334 | -50.3615 | 2026-09-06 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 113632eb-9bb1-35f7-af01-d7437af627bc | -5.6382 | -60.2289 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ba56986c-29bd-32fd-a657-b0f0ac0374ef | -3.6215 | -60.585 | 2026-09-06 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e6a9c6a3-6386-35e9-bb02-64afa1e04b0c | -11.3052 | -45.1344 | 2026-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 822aa935-66f9-3185-a6a8-ccfd7b79759f | -6.6514 | -59.945 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 372d6156-d256-37a5-abbe-b3f1883ce035 | -5.4731 | -60.1959 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| fa00bf2f-12e8-323d-9db1-c50c1b19c9db | -6.1176 | -59.9261 | 2026-09-06 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 44d2c26e-6117-32b4-ab46-80a9a4adc5fe | -3.6215 | -60.566 | 2026-09-06 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f3eb5e24-8b1c-3be5-9801-ba42c7bfc0a5 | -5.9998 | -57.7859 | 2026-09-06 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 3b278b6b-d7e3-347c-9134-1f16dac1916d | -3.3871 | -59.4075 | 2026-09-06 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e0ae2a48-ce0a-3264-9903-0e18aa0e7181 | -3.4269 | -58.3104 | 2026-09-06 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 04451b41-21f4-314a-97c1-3c43aa749123 | -3.7645 | -61.7548 | 2026-09-06 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 141c8b85-c126-3d69-8e30-bbbdb25253c8 | -8.9791 | -44.3951 | 2026-09-06 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 83eb8026-bcab-3909-a651-6e3b14822ce0 | -5.1623 | -55.9536 | 2026-09-06 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b647f8b0-e6f3-361d-a5d5-e46ec4f4c01c | -5.4731 | -60.1959 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| da04151b-5be3-3327-a80a-8e7819d98295 | -5.2898 | -60.125 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c4a3e0e1-91fa-307d-b7d1-22cf9953226a | -5.2897 | -60.1441 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e80f7fee-b7f3-3d57-b01f-03b3e973a6cd | -3.6215 | -60.585 | 2026-09-06 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e05cef34-7731-3406-b245-d8523c583f67 | -5.3647 | -56.0051 | 2026-09-06 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 50507307-68cf-3111-9e4a-283316ccd42c | -5.5098 | -60.1947 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 320c3a1f-8d6c-3f0a-a701-5d9a29668321 | -11.2864 | -45.114 | 2026-09-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| d18c1245-15be-3e11-9362-76fd2c0690ad | -7.1372 | -42.2484 | 2026-09-06 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 1be5f502-8b07-3fbe-bcaf-00b10274d700 | -5.6566 | -60.2284 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| e945bf11-6371-3211-9188-0ead022bdc73 | -5.6382 | -60.2289 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c38f0504-30b0-3a63-9250-30802dd73bfe | -3.6215 | -60.566 | 2026-09-06 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 82541f27-1f8b-3a22-9914-15d05ee23329 | -5.4914 | -60.1953 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 323.1 |
| 4a139027-9b92-3190-9014-04fb6794ab91 | -10.6452 | -45.8635 | 2026-09-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| edc6c636-d0df-3d6e-92fc-8a765cf90dbf | -6.6514 | -59.945 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3934e658-fffb-36de-843a-d74bd3af876d | -8.9601 | -44.3973 | 2026-09-06 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 96918920-4a45-3824-a355-0094b7640cc6 | -3.7828 | -61.7545 | 2026-09-06 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8e7b2807-4cac-38b4-9db1-f83cc60c14d5 | -6.6515 | -59.9258 | 2026-09-06 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e599e270-4eda-3e2e-9a64-c5090affa2bd | -6.7648 | -59.4408 | 2026-09-06 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 27fa4c25-c07f-3078-a334-a4f5308cca4c | 1.4453 | -50.7446 | 2026-09-06 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6beaee1f-eaaa-3fc4-a5b6-a3ef7aa08931 | -6.9475 | -59.7414 | 2026-09-06 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 605454b4-8e67-3c90-98a5-69e50676a9e5 | -2.9338 | -57.8949 | 2026-09-06 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c3451510-41b7-36c4-ae94-5f3d264a2b7e | -5.5098 | -60.1947 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 05be9d4b-3674-334d-a9df-5627297f9d4e | -6.6514 | -59.945 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d208373a-2999-38fb-90de-c1f44a8e05b1 | -5.3647 | -56.0051 | 2026-09-06 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 219.6 |
| 655f5e26-b205-31ed-a191-840c35958c43 | -3.7914 | -58.8613 | 2026-09-06 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7c04cf4d-4bf5-3246-a02f-0d51cd05f7d4 | -5.6382 | -60.2289 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7dca5e76-3208-3098-af1c-d5c2887442fb | -7.6779 | -44.3266 | 2026-09-06 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 775027ee-de70-3b11-9f98-87725649461c | -3.4269 | -58.3104 | 2026-09-06 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| df5d37ad-bbe3-314a-acea-0b07ea6ff56e | -5.4914 | -60.1953 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 205.0 |
| 3cf46d04-a2b5-3d90-8685-20b3bb18a8c2 | -5.2897 | -60.1441 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0004c3a4-192e-3337-b561-3dfe9b145675 | 1.4453 | -50.7446 | 2026-09-06 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a22abc1c-8e6a-30a3-90c7-3029c76219cc | -5.2898 | -60.125 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 516f0250-7e89-3e9b-bdb4-df1ad314d112 | -3.6215 | -60.585 | 2026-09-06 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |


[Clique aqui para ver as próximas entradas](README38.md)
