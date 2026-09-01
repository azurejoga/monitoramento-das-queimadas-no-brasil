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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af737431-bc20-351d-9b7c-42beba7a7310 | -8.4043 | -45.0097 | 2026-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 22e2f425-2380-3f42-877d-10e954b64f54 | -11.2295 | -51.2667 | 2026-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 6d8b3ad5-9807-37f6-ae39-2a9a799da49b | -14.7302 | -53.5966 | 2026-09-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 51978a77-0740-3774-b131-d3062529cf32 | -10.3577 | -49.9957 | 2026-09-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| a048aa0d-2730-3a9b-8661-dfcbb5437982 | -11.7216 | -47.6327 | 2026-09-01 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 926e0a0d-29fc-3eb4-b5f9-f3a00e4c398f | -7.3685 | -45.066 | 2026-09-01 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fc76c715-e547-3579-bef2-4dcb3694a304 | -3.5161 | -59.0597 | 2026-09-01 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7e37498b-8a8c-3627-a057-91a66c33dfcf | -7.8443 | -61.1413 | 2026-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 3993362d-bf78-30d3-8fb4-888c662c4b48 | -11.2292 | -51.2879 | 2026-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| cce1885e-f800-378b-a3fc-0808c6ed2059 | -6.9367 | -55.636 | 2026-09-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 843fa55a-8751-313c-b3cd-1d12bf148ff3 | -7.5474 | -61.3818 | 2026-09-01 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| be256730-6ab8-3d38-804b-b12389b667fc | -3.6398 | -60.5656 | 2026-09-01 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2362a2b0-4311-3d50-98c9-08298730e70f | -11.2439 | -45.3727 | 2026-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 221d0a0e-03cb-32d4-bd86-bfd3f0af9c4b | -8.7628 | -46.4642 | 2026-09-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| aa62224d-6fb1-3c54-8707-367262b7a7ca | -6.8009 | -59.5742 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 168c584a-6485-36f5-a2de-ce7f81cfe284 | -6.6542 | -59.426 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 455e187f-c427-38df-aa41-250304ea9499 | -10.8218 | -50.6306 | 2026-09-01 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 44a19342-967b-34e8-a502-00a51f5a162a | -7.445 | -44.945 | 2026-09-01 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 8e73e92a-5026-327a-ab57-213b7d0cedd5 | -8.9242 | -63.2804 | 2026-09-01 14:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 395e0d3e-3097-3c6b-856f-3556a7b91a0b | -14.4831 | -52.2151 | 2026-09-01 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 89ae0494-f877-3d29-9bff-fe2d83a96fb6 | -8.5962 | -54.8563 | 2026-09-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c55d9fd1-2627-34dc-babd-c6df6c4eee06 | -14.5214 | -52.2313 | 2026-09-01 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| dd426e28-cb96-3e96-8c92-a3dd4067c907 | -14.6732 | -53.5408 | 2026-09-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 41fac52b-99ac-3ddd-8ff3-eb73a36233cf | -7.9988 | -44.2711 | 2026-09-01 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 221.1 |
| ae74ffda-1e86-3757-9856-86f7667fb0d1 | -6.1659 | -57.7403 | 2026-09-01 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| df49025c-439e-37c6-b6b6-204bf2ce8ce9 | -11.6649 | -47.5957 | 2026-09-01 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7b30d3db-d0d6-326c-a272-be4a2be3ae5f | -14.6538 | -53.5433 | 2026-09-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 213.3 |
| a2410a36-990d-3649-ae74-51ae572d95ff | -10.358 | -49.9742 | 2026-09-01 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 78508065-2748-3d69-8c26-854d3793c10d | -7.3119 | -60.5706 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6daa7071-c80f-383e-b8d0-d2c8ce0b6359 | -3.2623 | -58.2367 | 2026-09-01 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 44fec4fc-7562-3045-b222-349f5e72234c | -10.8407 | -50.6286 | 2026-09-01 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| d5f15b12-b85e-3bc7-9dc7-d5df12a624a1 | -10.1528 | -45.7665 | 2026-09-01 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 244489a0-c02f-323f-a863-dfc91ec2dea0 | -13.471 | -57.0373 | 2026-09-01 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 14b69c4f-2965-3a49-99fc-d81f1e61ff8a | -6.8035 | -59.1114 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| fa4bb983-44f2-3e8e-89d3-12919aa16216 | -3.6216 | -60.547 | 2026-09-01 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ad75df0b-1340-3bc8-b8f1-14a646edea03 | -6.9553 | -55.6151 | 2026-09-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9e242766-70f9-33f7-9df1-69d4718accf1 | -6.6727 | -59.4252 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| fbdddac6-7bc3-3e0f-8d1c-c0edddc3c487 | -8.3857 | -44.9888 | 2026-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 420b39f3-b4f9-3f18-9531-111285162769 | -3.1266 | -61.2188 | 2026-09-01 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 894368aa-2c00-3f85-ab03-46e98a5ff977 | -8.4232 | -45.0077 | 2026-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e2638c54-51d7-3446-a7fb-ec5c10598ae4 | -6.6541 | -59.4452 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 61add9ff-a46e-30c5-b19c-63d4ff12390c | -3.8792 | -44.0346 | 2026-09-01 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b8ca5e46-dcf3-3cc9-87a2-3dfcbded4e82 | -13.9477 | -54.3971 | 2026-09-01 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f9ff8ba0-8012-35cc-8832-f08cf9cb5907 | -8.2415 | -54.94 | 2026-09-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 81be6a93-0b6d-3245-8da2-c89f79d27ede | -4.181 | -63.1543 | 2026-09-01 14:20:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 3db1c89a-f8cb-3f96-a5dd-01b58f5d632b | -3.1083 | -61.238 | 2026-09-01 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 73554e4b-498e-3ef9-8e4b-f535df76a6b5 | -13.4516 | -57.0592 | 2026-09-01 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b99c081b-07b7-36a7-9651-3bba50bd96c2 | -7.8716 | -47.0838 | 2026-09-01 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 168b2f13-eb47-39d0-846f-d962dc97b013 | -7.9239 | -44.2327 | 2026-09-01 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7acb2d49-b3cb-3860-b2c2-fc80d8ae091c | -3.8416 | -44.0824 | 2026-09-01 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d8398741-4baf-35db-a88f-ba46347cfdff | -14.7305 | -53.5756 | 2026-09-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 161cc7d9-c810-3edc-92db-f5df1263a573 | -10.1718 | -45.7642 | 2026-09-01 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 30614f01-db7a-346f-83db-c880208ed864 | -3.879 | -44.0576 | 2026-09-01 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 215.6 |
| 304f493e-764d-3dd4-888b-71c556f964da | -13.0897 | -45.163 | 2026-09-01 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 428.0 |
| d533484e-e068-394c-9b87-90b312dd9cd4 | -10.036 | -44.7056 | 2026-09-01 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 99277ebb-f73d-3d8d-88cb-dcc4c4bad534 | -3.6215 | -60.566 | 2026-09-01 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 78de17c0-fbad-3a86-b5fc-4f7ebc9d8aa2 | -11.6841 | -47.5932 | 2026-09-01 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2b8e1f57-7c8a-3fa5-a63e-d54529369f20 | -7.3487 | -60.5883 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.4 |
| d5c3bfb5-f7f7-3a4a-8b8e-610325d0d451 | -8.7819 | -46.4399 | 2026-09-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.4 |
| abe68bae-5017-3656-815b-d939746fc080 | -7.3488 | -60.5691 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| cab2aec5-922a-3b05-a7d2-d00545bc6d4f | -7.0979 | -45.7914 | 2026-09-01 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 04b0f929-63d2-30bd-9903-2f1a6fd5a85c | -11.2485 | -51.2647 | 2026-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d058fa58-79bb-3569-923e-a3b27649e4cb | -7.2006 | -60.6706 | 2026-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 196.4 |
| 0da2a50c-c890-3f2c-b2d1-4cd8d4d45246 | -7.3118 | -60.5897 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 82d89f91-096b-33ee-9e99-e1d0939c7577 | -11.213 | -46.0839 | 2026-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 5bea3576-53cc-3e61-85c5-f74e1b951e77 | -17.1146 | -46.8556 | 2026-09-01 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 7fcabad7-4a55-3b81-9ff8-14bb9710cec6 | -14.6535 | -53.5642 | 2026-09-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| af69946f-7c41-39f3-a1cf-fab5c6bd1938 | -7.182 | -60.6904 | 2026-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9417cba9-8a8e-3c21-9b3e-10e55a1c83f4 | -10.6769 | -46.267 | 2026-09-01 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| d790484d-f890-3d86-9a05-fa5a9f25bad8 | -15.4429 | -52.681 | 2026-09-01 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 220.7 |
| b7766ba6-94ce-3b97-8ef0-f67584029cb7 | -10.1525 | -45.7892 | 2026-09-01 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| cc2ab5d9-fadd-35b8-8bc2-d56d7ce1fbf9 | -13.4325 | -57.061 | 2026-09-01 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 76955c69-0382-36a0-a97b-0bdd32fea913 | -7.9797 | -44.2962 | 2026-09-01 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f6eba130-bc20-3d56-aa71-90aadc2e7f36 | -11.2478 | -45.1425 | 2026-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e0bd51ea-f073-3887-9f91-36c1ca295df2 | -7.1786 | -55.4837 | 2026-09-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d1a63b94-42d0-3aa1-a166-062741bf24eb | -14.4587 | -52.5151 | 2026-09-01 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f27586fc-f061-32f4-9923-668982a5e319 | -11.2673 | -45.1167 | 2026-09-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 44f33ba6-c6f5-3298-89f3-4170f189a848 | -9.4606 | -67.4531 | 2026-09-01 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8997f40a-7802-362f-9cfd-3ec6befb8e8c | -10.8404 | -50.6499 | 2026-09-01 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| d5761c75-c97d-3235-a54f-ceaf59eb16ce | -8.4235 | -44.9849 | 2026-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 94028c39-d11b-3d34-8be2-7f7afdcad23d | -4.1515 | -60.7068 | 2026-09-01 14:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9e3349df-0631-3dea-8301-7da5cafcadc2 | -9.4421 | -67.4535 | 2026-09-01 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 05cd14f9-7b11-32de-b3b9-40b8dac23363 | -11.2298 | -51.2456 | 2026-09-01 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 0b06386e-9f46-39e8-9436-b79c4033ee73 | -17.1345 | -46.8516 | 2026-09-01 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.0 |
| fefcc454-9192-3408-9702-55beaeb97f2f | -7.5709 | -60.4835 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 14392ded-7d2d-3f0b-bade-3348ffbd1716 | -8.4046 | -44.9869 | 2026-09-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 469fd4f0-fb41-3a8f-a00a-3eebce8ee768 | -6.6726 | -59.4445 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a498e4aa-7e9e-3236-ab1f-3bc22fbe8493 | -13.3946 | -51.7382 | 2026-09-01 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 643ba54a-c59c-380b-bbb6-b5183efd3b4d | -10.7856 | -50.5066 | 2026-09-01 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 8c6f685b-2c3e-3528-a455-8c6ced56aca2 | -12.9032 | -45.8382 | 2026-09-01 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 272.9 |
| 08a2893e-70fa-330c-a2e7-02f11b263377 | -6.8036 | -59.0921 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a33ca44a-c772-3a2e-a115-bcc50ac58b0a | -3.1083 | -61.2191 | 2026-09-01 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 40bcf482-3f80-3e7c-8286-8da172957eaa | -12.9589 | -45.944 | 2026-09-01 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 2142d284-835a-3a80-ad2d-8ede9b3a7310 | -6.369 | -54.7655 | 2026-09-01 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 466d41b2-0c43-3731-a1c9-677a745f487e | -5.5649 | -60.193 | 2026-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f4cb23f5-9eab-3527-8e1b-354c0ab5a06f | -11.2106 | -51.2688 | 2026-09-01 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0697a4dc-d0a4-3f68-a7e2-b3a3e3301eb3 | -16.1523 | -46.6749 | 2026-09-01 14:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 08e150b7-5269-3e23-b7bc-fd3def878a8c | -7.2005 | -60.6897 | 2026-09-01 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 61eb6e7f-07fe-3c99-aea6-cd9b70888a8e | -8.7817 | -46.4623 | 2026-09-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 9af47fc0-c75a-3deb-8bd9-727f7e9badff | -14.6728 | -53.5618 | 2026-09-01 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |


[Clique aqui para ver as próximas entradas](README101.md)
