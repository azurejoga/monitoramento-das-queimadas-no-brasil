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
| af8e3ac6-00ac-3f3b-bf3a-7236c4852bba | -5.84616 | -45.02475 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 77f614aa-b8e0-3a5c-b7de-f4da4b4e25ec | -3.93681 | -42.99118 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2d84a99-723a-3f7d-b425-6c6466007c9e | -6.82062 | -39.311 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a52ef9cc-db0e-38e1-96c6-3df2ee058ccc | -6.82392 | -39.30407 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b9a26b2a-1808-36b2-a340-665136ff55b7 | -6.61911 | -37.89565 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c7f4b22a-3ca8-3659-a415-24828a9de927 | -5.61603 | -44.84563 | 2026-10-06 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8241adad-9016-3ed0-afda-bc301a3bfd73 | -6.82139 | -39.30638 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 85996939-0cc7-3117-9d7d-e563e3d96f69 | -4.50724 | -43.69684 | 2026-10-06 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb48455e-3048-316f-8820-8ea16f645870 | -6.19307 | -44.86365 | 2026-10-06 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 440fd689-2be3-34e6-a067-6bd3e0c57720 | -5.83211 | -45.00715 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 97a83738-2251-35d2-a0e3-16df15aec909 | -5.84592 | -45.02426 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c66d26ad-da32-3190-a3ed-e09d0f2b82c7 | -5.85142 | -45.02536 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5a227d4-6620-3130-98fd-7365557dd4fc | -5.83635 | -45.01556 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f4530f9e-be15-32df-b6f2-0ed0325024f7 | -3.07915 | -44.45716 | 2026-10-06 03:42:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb8807d3-5a13-3803-a762-318448d8729d | -6.62043 | -41.56537 | 2026-10-06 03:42:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04718cbb-4098-3519-a0ca-8fc2fac501b3 | -5.96418 | -41.35655 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09ecca2f-784c-35f5-881a-3ec98b58a84c | -5.08987 | -46.04567 | 2026-10-06 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eefa3663-0033-3de7-bc51-9fb89a0ee5de | -5.95061 | -41.31721 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| baa8ea1e-d2bf-357b-963a-0dec714e17ce | -6.45129 | -43.82951 | 2026-10-06 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a43167a-e856-3560-b584-ce6d32fcc948 | -4.99641 | -42.42669 | 2026-10-06 03:42:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 01c8ec27-8dab-34fc-8838-84fa262353e2 | -3.7811 | -41.59729 | 2026-10-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dc807a9e-88fe-30ff-820c-f3a81058c66c | -6.82052 | -38.53244 | 2026-10-06 03:42:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8e91603e-7974-3321-9a1d-56316fffe38d | -4.99883 | -42.42398 | 2026-10-06 03:42:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 827a7610-6244-309f-96b3-fbb4c824bc25 | -5.95272 | -41.37189 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fab811ee-b5a9-3228-b918-a1d326c18617 | -5.40716 | -39.10722 | 2026-10-06 03:42:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 774baed0-dfd9-3ac2-9248-9c55b47ad4ac | -5.88703 | -43.45488 | 2026-10-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f591874-8280-30e1-995a-48dff0b5376f | -4.45572 | -47.91863 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 82623d87-a78a-3477-847e-2492b3a67709 | -4.4546 | -47.92477 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ebbb8414-d91f-3234-9130-b56c83d45d8a | -6.34614 | -42.5472 | 2026-10-06 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b0e6213-9a73-3d91-a44f-3175fe182df8 | -5.64995 | -44.12017 | 2026-10-06 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a700dd1-afc6-367f-b126-7e89954d7325 | -6.19255 | -44.85916 | 2026-10-06 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c6e32e6-53ad-3d76-ac19-21797a257191 | -6.25345 | -39.37472 | 2026-10-06 03:42:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 990b109f-2de8-3bf5-b689-62cd3400767c | -5.94898 | -41.31603 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 107b7142-4473-31b2-9eee-114e42bdff64 | -6.62032 | -37.88825 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ad5972e-e308-39a2-8c37-f24364e47229 | -4.50776 | -43.69374 | 2026-10-06 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 883ad0e2-6417-3cc4-a154-5c4ef92b5b7e | -5.43 | -43.44788 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 100a7264-4a08-39ec-ac88-abc6d6d88bfc | -5.61054 | -44.8447 | 2026-10-06 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e112c35c-994a-3bc7-b469-905b3ecf8ec7 | -5.75533 | -46.67923 | 2026-10-06 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 69fa5bab-9b60-3ba7-bacd-d1a73e97f786 | -5.44049 | -43.44683 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d86096b9-092f-33dc-97bd-bde5c5e05d83 | -4.99796 | -42.42907 | 2026-10-06 03:42:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9a250e73-1861-3fc3-90c0-515821fa19be | -5.98231 | -40.91189 | 2026-10-06 03:42:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a47a96f3-63f9-3fb4-b814-487b9264ad48 | -6.19251 | -42.9578 | 2026-10-06 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfbcdd82-f82b-3fbc-b86d-e2188695fae5 | -3.07852 | -44.46088 | 2026-10-06 03:42:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63be5e73-368e-3874-a1f3-e277da3b41ed | -6.19193 | -44.86274 | 2026-10-06 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 492a6bab-d731-34de-9859-5f68b88d15bf | -4.79223 | -40.04239 | 2026-10-06 03:42:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76721a0f-79e4-3a34-8a6f-ad0ab9257850 | -5.75407 | -46.68389 | 2026-10-06 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b3475ddd-702a-39f7-9a4b-f6f7ed47439a | -4.50438 | -42.06909 | 2026-10-06 03:42:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9e47acb-0599-3dc6-bdac-219cf25e4184 | -6.60814 | -37.88647 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9fad6a9-3939-3c4e-a5ac-25269440d6b2 | -6.19372 | -44.86005 | 2026-10-06 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84d3f718-7e32-3594-9153-fb94d7106004 | -5.06605 | -46.11117 | 2026-10-06 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 528ae863-6673-3614-b3e4-2d155d767641 | -5.41649 | -44.35122 | 2026-10-06 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74bda353-0415-3e17-957b-2c584af09eeb | -6.61971 | -37.89195 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 13b33d70-f408-3220-85c1-a8f2e14c23ad | -4.72282 | -44.08199 | 2026-10-06 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11506c7f-6892-3c51-9bcd-91452632cbd9 | -5.74917 | -46.67815 | 2026-10-06 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d815ce27-46cf-3cfe-bca0-ba057071fd04 | -5.4305 | -43.44495 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11ea410-0875-30e9-adc5-c36e53632164 | -6.61742 | -37.89543 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7a406201-808f-32c6-9f2e-26299e56ef2e | -4.45354 | -47.91746 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3400be67-6e05-3206-91a3-556fd904a4bd | -3.77657 | -41.59657 | 2026-10-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 75ee036a-4c65-3d8a-9175-d25336fac105 | -4.45247 | -47.92361 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 13ca4cb5-91d8-389b-92fb-d78ece2f48de | -6.32296 | -43.34722 | 2026-10-06 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66d58f40-a027-3d67-a4d2-3f15aee2b0bf | -5.84745 | -45.01727 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| d361195a-7660-36f8-8ce8-c3f083f08c96 | -5.94969 | -41.31194 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8abfc3da-3dc5-3ead-9d96-ebe3fc6cbacd | -4.35686 | -47.78156 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e15a7b3-be5b-3e50-b452-f088972eefb4 | -6.18646 | -44.86196 | 2026-10-06 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fca4fda0-a5f2-3b5e-87ae-ba1434ccea26 | -5.84681 | -45.021 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a4b84be8-91a4-3187-a802-a8288f341556 | -6.35071 | -42.54844 | 2026-10-06 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e60e98e0-cda1-3ca5-82a4-b794a3fb0ac5 | -5.66899 | -42.59205 | 2026-10-06 03:42:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b475421c-b4f1-3e35-a744-fc2dc46b2183 | -5.81781 | -43.41105 | 2026-10-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3392faf6-8074-39d9-a3ca-a72e64766c40 | -4.50748 | -42.07219 | 2026-10-06 03:42:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 674955c0-6b3e-3da7-a29b-66f6052762f6 | -6.18769 | -44.85485 | 2026-10-06 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1420c7e2-52dd-3f95-8b0a-e9691b8ed82e | -5.46178 | -45.52562 | 2026-10-06 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 057fc456-52d7-3cac-a8f0-ffff0ca65001 | -3.93633 | -42.99402 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58af8ef2-517f-3a75-b386-03d36be4064b | -1.69499 | -45.79134 | 2026-10-06 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83bdf03b-f5b8-30d0-b836-07ac94126c96 | -3.96212 | -41.55026 | 2026-10-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ddc56bb1-4c72-3994-b4fb-a6ccdc80bcc3 | -6.60346 | -37.89339 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d7b0082d-bf19-3815-b6b1-8d4285ef0ef6 | -0.9446 | -47.55183 | 2026-10-06 03:42:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4527dae-c546-38fb-8839-e94a67bd4c11 | -5.837 | -45.0118 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ea0ddf18-1f5a-3725-9f9b-8cb902b683b2 | -5.81832 | -43.40817 | 2026-10-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cf0bb07-bd7c-33fb-a2a0-1cbfecaf61c4 | -5.84126 | -45.02014 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3923504d-2049-3c6d-8ca4-433a71808009 | -6.82409 | -38.53305 | 2026-10-06 03:42:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e90a02b6-d2bc-3e4b-ae8d-5c0e302bf1b1 | -6.60405 | -37.88966 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 021aea20-4afd-3297-989b-64ae86ae9095 | -5.75448 | -46.68402 | 2026-10-06 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8c7d253f-f907-36db-8681-794b77768593 | -5.435 | -43.4488 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 81da2109-d62e-32e2-a702-408ea420a68a | -5.22994 | -48.39583 | 2026-10-06 03:42:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00c69af4-75ca-307a-b740-adca660503aa | -5.84659 | -45.02052 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6f1bb231-9a9e-358d-8632-a8a1e0906fcc | -6.42642 | -43.4645 | 2026-10-06 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e0560e8-ce1a-3fe9-96fc-fc49bbd95c5a | -5.88607 | -43.46053 | 2026-10-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79bb0c43-e1ca-378b-8384-6568c1c641d2 | -6.81944 | -39.30813 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e9fe193-1f5e-320e-907e-daa2c701ce0e | -5.66987 | -42.58691 | 2026-10-06 03:42:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfb52632-82d0-3bee-ab7b-7e6377b7ec68 | -4.19019 | -44.25981 | 2026-10-06 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8aeb7b9-b857-3199-9076-78633cca53ab | -5.67076 | -42.5817 | 2026-10-06 03:42:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ed26593-6686-32e7-b10e-134bf499d4a3 | -5.82594 | -45.0099 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0c03c957-ac0a-3752-b2fb-0cb7ba1a7117 | -5.95128 | -41.31311 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d28055c3-e972-38df-b211-198e5221d0dc | -4.19557 | -44.26084 | 2026-10-06 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c169b1a4-f41e-3a67-83c0-b233a2a100b4 | -6.82319 | -39.30861 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 12c81d1b-a9b6-3c7e-bcff-164211972bbc | -6.62381 | -37.88874 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a7873fb7-f674-3e17-8b57-555671eae808 | -5.96128 | -41.3476 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 440f6dd5-946c-32cc-a878-f5b84b823409 | -5.85232 | -45.02208 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8f250709-6de3-3ede-914a-d8dbb823e087 | -5.85167 | -45.02588 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0e80426-105b-35e0-a6f3-9e1819fef505 | -6.42545 | -43.47021 | 2026-10-06 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README20.md)
