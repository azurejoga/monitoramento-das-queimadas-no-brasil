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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b10727d9-3b29-372e-afaf-c305c9784d27 | -3.44951 | -45.64692 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a74e87b-aaac-33ab-bacf-5bf22cdd24ae | -7.69776 | -36.39029 | 2025-11-09 03:46:00 | NOAA-21 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17162464-9517-3330-9303-c5f4cc41b0d5 | -3.45394 | -45.65679 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eca1e2ce-8bf3-30cb-a71a-596e49fced82 | -7.40851 | -40.07169 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c6ade25-48d2-3f24-bd63-fbb0e40dc850 | -8.62991 | -38.39676 | 2025-11-09 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 70b22c6b-7525-36c3-bf85-c2e8924914e3 | -7.12576 | -44.96732 | 2025-11-09 03:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45f62832-75a0-3d01-a218-1cb14fe0bbb5 | -6.88406 | -49.25257 | 2025-11-09 03:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c3700d9-20f1-35f2-bd89-140954270e40 | -7.91992 | -43.30822 | 2025-11-09 03:46:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| ef2d7b0c-73d6-3217-bf3c-645355b7554e | -6.87856 | -47.24044 | 2025-11-09 03:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3107299-f2ab-3d92-9a22-a30fa3dd0ee6 | -7.00065 | -42.78617 | 2025-11-09 03:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7274f051-81d8-334a-bb5b-599d2bf47907 | -3.48706 | -46.1081 | 2025-11-09 03:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71210979-7685-38fe-8a89-c8cc2799de50 | -4.91205 | -37.78637 | 2025-11-09 03:46:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b2c0ca0-9678-3c3b-b168-e16fe91d50bc | -2.26447 | -47.84435 | 2025-11-09 03:46:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f6c1b5ca-bc3d-382a-af06-648b659f0cf4 | -3.32951 | -44.37656 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| faed10d1-45d1-3fe8-b4b1-9896ab7516ca | -3.33 | -44.37358 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 174fc681-a748-3f40-a094-983dd1a176aa | -2.96781 | -41.57718 | 2025-11-09 03:46:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 394617e1-b02b-310d-a4b4-917c7f0d53a5 | -3.09557 | -49.26126 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d4ebd237-4943-3a2a-b9bb-2964753cb66a | -3.66253 | -41.46925 | 2025-11-09 03:46:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 068a3e2f-6e7c-32ae-958b-6a77b89244c6 | -3.33411 | -44.38041 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 16a4e4c0-2541-31c0-8b06-028706d8e562 | -7.40197 | -40.0663 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cb087490-7687-3961-9074-60308a5135c2 | -3.47375 | -39.57288 | 2025-11-09 03:46:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7650fce4-cfd4-35ac-b166-95a3e22a2dca | -3.34115 | -44.36929 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59ca82fb-67c6-33b0-8bb4-e156aec66cf4 | -2.60566 | -49.21636 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ccada215-acf8-3f9e-828a-c2584b47f52e | -3.1519 | -44.57582 | 2025-11-09 03:46:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e43dd23c-53eb-3d1a-a9c1-9aaa16d34b3e | -6.42927 | -44.68063 | 2025-11-09 03:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac6cc8b2-6303-3deb-866c-0d1eb8bd6053 | -7.84801 | -38.43314 | 2025-11-09 03:46:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a8ce968a-efa4-3c60-a808-e5b1bf6cfd02 | -9.51589 | -47.26963 | 2025-11-09 03:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19a3b6ac-a2de-31bc-900e-a9b7e79ea698 | -3.58808 | -41.66122 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cff686e2-4f25-3281-87ab-decf511dbacc | -9.51033 | -47.2686 | 2025-11-09 03:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 936f7fa8-9e6e-3100-8a88-b4aa44f62f51 | -7.09713 | -45.22396 | 2025-11-09 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc373e27-e003-3ad2-965c-8ca8cdfaf2d0 | -3.33557 | -44.37143 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d7923b76-db49-32d7-9b99-0d87de07b6fe | -3.3392 | -44.38125 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7d867da3-f5ac-3fe7-9b3f-3d11bd4afb29 | -2.61304 | -49.22365 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f843ad00-8332-3d4d-b859-e86933a76a10 | -3.4496 | -45.64861 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c890f608-06cd-3997-835a-2661a8e71104 | -6.76513 | -46.675 | 2025-11-09 03:46:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79bfe04c-32ec-3419-8910-b7c6427e4de5 | -7.82122 | -39.89517 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1310b832-3664-31e0-bd17-be2976f1491e | -8.01869 | -38.55401 | 2025-11-09 03:46:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdf5a95f-6f79-3667-9805-df1c89d6394b | -2.98573 | -48.70441 | 2025-11-09 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 100c5c48-b56d-3024-9395-df2b63c69c56 | -7.18647 | -39.66989 | 2025-11-09 03:46:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 595a5e22-8873-3f02-9924-e710b59f57ba | -6.68796 | -46.66566 | 2025-11-09 03:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ab1847d-dc82-355a-91eb-1eced1260a0a | -6.88346 | -49.24849 | 2025-11-09 03:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 58dab67c-5d31-386e-b5f0-3b0864a430c6 | -2.9382 | -49.35754 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7784d4ee-7ac3-308d-a198-07531b3eb497 | -7.41574 | -40.07288 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe2975c6-c7d4-3df4-9329-06638cbc447f | -6.88511 | -49.24685 | 2025-11-09 03:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d763535-e3e4-3e2d-8c31-e52fb941169f | -3.449 | -45.65228 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03f1ff5b-8ab5-39da-8b3f-3e684f20a348 | -3.33148 | -44.36448 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41092a7b-c59f-37c1-876d-eeea3f55fbf1 | -7.88638 | -39.56383 | 2025-11-09 03:46:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b46b9ca6-ea3b-3bac-a461-22cc84f25289 | -2.7093 | -49.54118 | 2025-11-09 03:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f704c0b6-198a-3501-86c4-4f2af9ba22be | -3.09443 | -49.26782 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c017ea5-6521-3dad-aa93-266da49d685b | -8.35882 | -49.94267 | 2025-11-09 03:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6503f2f-a0ea-3a79-af95-06052859787e | -10.06497 | -38.55638 | 2025-11-09 03:46:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4726316c-7bef-3110-8e66-0223dc67494b | -2.25901 | -47.87668 | 2025-11-09 03:46:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b881d406-3253-3e11-b49a-ac56aee58b1a | -7.40558 | -40.06689 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f014b886-8a2c-312b-8401-f410fd1869ea | -2.60379 | -49.23584 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc9d1247-a9a2-36c2-831e-d67be10ea7c0 | -8.63327 | -38.39729 | 2025-11-09 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0df21268-2c3e-3d0c-be9a-50fc117de202 | -6.22533 | -47.01423 | 2025-11-09 03:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d5743f1-f410-3100-8660-f39cf3e9cb7b | -2.59903 | -49.2215 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8c8c8f19-77d3-3b2c-b0ae-26849ddaa68f | -2.61149 | -49.2241 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 82295792-4fdf-369a-a70a-c2d9e1e722ad | -3.48928 | -46.10762 | 2025-11-09 03:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51764656-8293-3130-bf0c-c9b34ebcfe8a | -3.62729 | -43.15358 | 2025-11-09 03:46:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 041cda6a-0edc-341d-afba-19a2bb932c55 | -8.0159 | -38.54982 | 2025-11-09 03:46:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bcdddb4-702d-3e70-aa38-4c589b113bf3 | -3.32491 | -44.37271 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ee16d17-694d-3581-aa60-5534aa39d973 | -4.81019 | -38.69405 | 2025-11-09 03:46:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 206922bb-661a-32e3-aa05-e54407ae5ba5 | -7.41213 | -40.07228 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bbbe511-b984-335d-9c6b-5580e801d185 | -7.54462 | -45.85553 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92a3326b-fd1a-3642-88df-b45b96046de8 | -8.42266 | -36.25407 | 2025-11-09 03:46:00 | NOAA-21 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf2f19d3-eefe-3d03-b7b3-a88de3b59a84 | -7.54519 | -45.85238 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f49bc0a3-591f-3c48-ad36-87f029a8f9df | -7.9243 | -43.30899 | 2025-11-09 03:46:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4c154a2c-59dd-36dc-8fa8-6951cbb1f1cb | -2.97797 | -48.70921 | 2025-11-09 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3841e8a8-8901-3fa5-8e43-614a193626ea | -2.60717 | -49.21587 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0344ee5d-bcf3-3e40-a248-efb2fe5a941c | -3.4886 | -46.11152 | 2025-11-09 03:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f9c9576-9011-3077-85fc-1c3068df70e2 | -3.33099 | -44.36753 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5906ed6-78ff-3082-ae3f-6b18dc486761 | -7.4049 | -40.0711 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 532cfa7a-ebe3-35f0-8aae-8b6ed6ab49b8 | -3.7649 | -44.29191 | 2025-11-09 03:46:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d4fd6cc-2df8-3b9c-a26f-fd4d088379f7 | -3.45442 | -45.65145 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f36409a-b748-3fc9-898f-f64b8a5c3e27 | -10.06067 | -38.49735 | 2025-11-09 03:46:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1c0f643-4b8b-3279-a66d-3365815b5d7a | -2.60449 | -49.22301 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aa46e6ae-7563-392c-ab09-382fd32b7753 | -2.60333 | -49.22961 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e1db912d-c823-3eef-82ef-d20a195b92c8 | -8.99417 | -37.53848 | 2025-11-09 03:46:00 | NOAA-21 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17a9b385-c711-36d4-b16b-e9df860aa827 | -9.37994 | -47.08179 | 2025-11-09 03:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32f211e3-051e-3f17-8ba3-386eb1c0c9b7 | -8.19079 | -46.20364 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e3d870b-f3c8-3a4c-bec2-474f0a7cbff9 | -3.33752 | -44.38054 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| db90ff84-0903-374b-8847-bb9607d7e439 | -7.54987 | -45.85638 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ce9abea-d03e-3071-8608-0545c8fb0295 | -7.49876 | -46.60883 | 2025-11-09 03:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a281f224-b81d-316f-a1c7-c20195a5d3b8 | -9.4499 | -40.8096 | 2025-11-09 03:46:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e16dce4-cf1d-3ed0-aeca-f18e5af98858 | -3.61867 | -43.65546 | 2025-11-09 03:46:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 121936f9-259d-3106-88da-a8ebdab44496 | -3.59293 | -41.65802 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 03af5d3f-d308-39af-ac0d-02e3a085633e | -2.61848 | -49.22522 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edcc99ae-eb1a-38ac-a975-30ff3dfce8c2 | -3.15708 | -44.57667 | 2025-11-09 03:46:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e64720d1-0f12-3efb-a06f-62d55d72b7e9 | -6.99636 | -42.78543 | 2025-11-09 03:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 208288f5-b559-36da-b9aa-f466362cc121 | -4.38107 | -38.79588 | 2025-11-09 03:46:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 287d0777-8a09-3665-82e2-ff6eaf833b66 | -2.54493 | -45.15504 | 2025-11-09 03:46:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b82e951-26f8-38bf-b293-c1fc4ab9cb43 | -3.58388 | -41.66053 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93ea7b3c-8d36-3ff4-bbcc-33b67cad57e3 | -3.33956 | -44.36859 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 373fee3c-b195-34e6-8f4c-8133435ec3fb | -3.61955 | -43.65019 | 2025-11-09 03:46:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a1f7c7df-69fb-39c4-9329-ecb098cfeeda | -2.96294 | -41.58048 | 2025-11-09 03:46:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bb359878-c5e6-3d58-88ca-97d5f692b323 | -4.7585 | -38.682 | 2025-11-09 03:46:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 27a4e9f5-5dc8-3353-a906-f0561dde44ea | -7.56095 | -45.85489 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64b156c9-2122-39b4-8bcd-2f545c7f5d58 | -7.88924 | -39.56836 | 2025-11-09 03:46:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1a0f6f69-c57d-3cba-a271-16df7e5728db | -7.65418 | -38.67903 | 2025-11-09 03:46:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
