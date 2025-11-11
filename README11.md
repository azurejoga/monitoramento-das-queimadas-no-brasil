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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f53ef0c-f405-3be5-b72e-568f2d878480 | -4.19902 | -50.63699 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b4820f9-68c2-311a-9f60-3971da7a3444 | -4.64652 | -45.75824 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e235d27e-662c-3ad8-bcb8-41cea396a65f | -6.10478 | -41.54071 | 2025-11-11 03:59:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48a5baf9-225f-3527-aceb-7edddd5c1828 | -5.0566 | -44.11097 | 2025-11-11 03:59:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2cd932-29d3-3524-9b39-fd7a5545fe4a | -4.59507 | -45.4926 | 2025-11-11 03:59:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d0556ac-5e1d-3fee-9e36-4321514897ad | -7.37173 | -39.1781 | 2025-11-11 03:59:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05f5fbf4-ccdf-3211-8cd5-5bd92ca0428d | -3.96412 | -43.78271 | 2025-11-11 03:59:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 482b2fec-6ac7-30cf-ad35-0648da8ba0a4 | -4.90718 | -44.33047 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5feeb61d-007d-3704-bfea-e5e751ed5604 | -5.43816 | -45.09352 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e350eb2-99d9-3281-a801-f140e7228581 | -6.81028 | -38.47118 | 2025-11-11 03:59:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53d0fb6d-6c61-371f-8668-c41e62f92793 | -7.19547 | -40.17256 | 2025-11-11 03:59:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e2d9eb0-8af7-3a9a-bbcc-a137106f785f | -3.71617 | -47.62648 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 550e53a2-038c-3a89-8ed4-127fa877afbc | -2.71956 | -48.34901 | 2025-11-11 03:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ea38cb2-5dc9-3884-927f-af0d19865b8f | -6.71875 | -38.54936 | 2025-11-11 03:59:00 | NOAA-20 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe72b01e-1e5e-3404-ba9c-015d3ecd1609 | -5.4204 | -44.65354 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3bdd449a-8c24-3968-9ac4-82ea481bbca0 | -6.1702 | -40.57404 | 2025-11-11 03:59:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6310f975-779b-3340-8ca1-52f4d1343977 | -6.10758 | -41.54492 | 2025-11-11 03:59:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 793e2a43-3ef0-3e8a-b223-52da52dd06ae | -3.54736 | -43.24368 | 2025-11-11 03:59:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cdc0e6f-62bb-383b-9828-ccd3e6627ba4 | -5.51243 | -44.39363 | 2025-11-11 03:59:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89d0b6f-1c1a-3f22-b06d-7460bce3ad6e | -7.0805 | -41.58023 | 2025-11-11 03:59:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec01f398-a883-3b21-bcaf-b6f04f9fb810 | -4.40086 | -44.08641 | 2025-11-11 03:59:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76a06bc8-bd00-3f3f-939c-987d8e80d1c7 | -4.68445 | -45.69012 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44f4baa2-5420-3ffe-8ac0-b83203e6025e | -5.7488 | -40.80855 | 2025-11-11 03:59:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7382d677-26a7-3997-8ab5-a272d5583b61 | -4.27397 | -50.53713 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e44331a-2491-3089-916b-0d7131587564 | -4.26489 | -45.96643 | 2025-11-11 03:59:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4a7b1473-d24d-3c2a-aeba-d3902f433c8b | -5.63401 | -43.2566 | 2025-11-11 03:59:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bfa10ef-b148-3c10-9423-3cafdf69481d | -5.05261 | -42.8051 | 2025-11-11 03:59:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbcbedc8-3237-3884-bd52-372be275a8aa | -6.36787 | -44.71936 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84ea29ac-702d-3837-9e49-903bdf040e1c | -3.954 | -50.52586 | 2025-11-11 03:59:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2eef3003-a3af-3818-b6d7-7a469e8a58ba | -5.42617 | -44.64362 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 988fd3a8-bf53-39ee-b4c2-11a04189d33c | -6.06796 | -45.81203 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ef18600-1129-3fa4-a0ed-c0c522ffd2ac | -4.91198 | -44.32606 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb704228-63f8-306c-8442-6a60695e16fe | -6.23629 | -44.16856 | 2025-11-11 03:59:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1926fed9-b32d-3c26-b587-b519b12ae231 | -6.08992 | -41.56839 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cfc28ec5-de6d-389b-b681-5ebcbb9a538d | -5.5085 | -44.39293 | 2025-11-11 03:59:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ca9819b-1823-3373-86b5-7b1bf7c1b454 | -4.40143 | -44.08458 | 2025-11-11 03:59:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb76688f-ce52-3f99-9de8-a84da5202899 | -3.71567 | -47.62938 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc7e5327-5c01-3702-8107-875959cc6a2a | -5.30025 | -40.91478 | 2025-11-11 03:59:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7d824d1-2772-3ea8-9ca1-5eee6bf1c2c0 | -4.91283 | -44.321 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c243771-1c79-38fc-879b-da9948c1287c | -3.60487 | -42.85895 | 2025-11-11 03:59:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fda88c17-75cc-3237-861b-44b451d0ddc6 | -3.54551 | -41.79936 | 2025-11-11 03:59:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab82f3c4-dc5a-3acd-9ab3-58c974c9b21a | -5.63825 | -41.07758 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 33bdbd34-a19c-3bff-859b-4852c87a5d2d | -3.95638 | -43.78141 | 2025-11-11 03:59:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 520dcb9f-2d85-3fd8-ac2a-ad8df266349e | -5.37988 | -44.72249 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fb77d7d-a62a-38c2-aa33-2600fe505873 | -4.10987 | -48.73034 | 2025-11-11 03:59:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d2e9a26-e639-3561-8eb1-2fa5b99ebefe | -4.91248 | -44.32901 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 276a9326-e161-354b-ade8-c6996d2205d3 | -4.90459 | -44.32761 | 2025-11-11 03:59:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 52121f58-6d29-33e3-9c8f-c0ba0df8d6f0 | -7.10326 | -39.35555 | 2025-11-11 03:59:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b42864d-0200-3300-9dad-51fc7f49c88f | -5.05271 | -44.11031 | 2025-11-11 03:59:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6a2ceb6-2103-3836-bb8f-6eac8e494203 | -4.59852 | -45.48711 | 2025-11-11 03:59:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5121cb6-bc40-36dc-9133-beeeeedc6693 | -4.71895 | -46.46144 | 2025-11-11 03:59:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2b84158-e464-305a-a40d-1b6ce167b147 | -3.95281 | -50.52861 | 2025-11-11 03:59:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30005582-a1a1-3994-9b63-f3d069595923 | -5.42441 | -44.65416 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a56cb86a-f167-3025-a0bf-0060e8a0bdb3 | -4.90771 | -44.33343 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61d8b2bf-33ac-33a7-90e5-b6b9e0dd3002 | -4.19986 | -50.63216 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80d360b4-9627-3a15-8168-ebfdd7b5fa5e | -5.42158 | -44.6465 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0c36778-657c-34c1-a452-fe99b40a7486 | -3.73734 | -47.65444 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7735620-4678-316d-a598-aba25e5ea1e3 | -3.77364 | -47.95184 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| addb4c0c-3a83-3b07-b2d4-697e0e6bf9ef | -5.71603 | -44.62501 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74d6f17a-49c7-3468-91f6-3373e173f634 | -5.75213 | -40.80909 | 2025-11-11 03:59:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b7ae0739-3022-349f-8b81-6e7727ed814e | -3.86805 | -40.98625 | 2025-11-11 03:59:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9629f35-b847-387b-b01f-2da3f7a239cb | -6.08653 | -41.56784 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 191ba915-82a1-3ab1-bd55-0429c5656036 | -5.30081 | -40.91123 | 2025-11-11 03:59:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3d3b4d6-7636-38e6-8417-21ee41e42977 | -2.71653 | -48.35108 | 2025-11-11 03:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bf377e8-588c-3c83-a30e-21d14de406e0 | -5.51634 | -39.55304 | 2025-11-11 03:59:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a42b413-913b-3bf0-bb69-3c5043fc530c | -6.23421 | -44.17085 | 2025-11-11 03:59:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61dffc8a-2956-3c6a-a84c-60e40e5e3e74 | -3.20906 | -43.32444 | 2025-11-11 03:59:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5c439c7-3765-328d-9f14-4a9169c051c9 | -5.65171 | -41.05776 | 2025-11-11 03:59:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4aa853b7-1bf8-3ea2-9078-696c7cddce6d | -5.63882 | -41.07399 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d669187-fa70-3185-9cde-013ea416f698 | -6.10081 | -41.5438 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c207fae-58a6-30b1-aeae-2dea24dc9408 | -5.12117 | -45.47961 | 2025-11-11 03:59:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f81d56-4960-3a78-b168-8cb8429b79a1 | -4.90323 | -44.32978 | 2025-11-11 03:59:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7362243f-4343-3b5f-85e0-2bc78f5fa2b8 | -3.44742 | -45.53405 | 2025-11-11 03:59:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91814a85-f827-37b6-97c6-4ec9cde2cbfd | -6.55046 | -44.46453 | 2025-11-11 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19e5ca50-4391-3282-abf8-9199bb1e67a4 | -4.75723 | -42.66331 | 2025-11-11 03:59:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| dc57d7c6-c0c1-3f86-9b0d-6a7f6882efbf | -4.90935 | -44.32319 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1d33bbd-ea25-3994-9a85-82bbb885b644 | -5.1232 | -45.60086 | 2025-11-11 03:59:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61ce9c63-99a5-31cf-9152-77585dc8e853 | -2.89038 | -40.49245 | 2025-11-11 03:59:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 732c85cc-2e98-3342-89d6-e86ec0be4a52 | -4.73697 | -49.53314 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab3238b1-0ba1-3e45-8f47-25386fcc9b34 | -3.85595 | -41.5864 | 2025-11-11 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 126ea862-f9c4-3a78-8128-dfd10caed35c | -4.45507 | -38.39015 | 2025-11-11 03:59:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| be51d423-8fcc-3803-9055-760b23b8d528 | -4.91112 | -44.33116 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21275312-8c76-3344-99f4-be938af8a605 | -5.40216 | -45.2458 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ec8e04e-a0b1-3a96-8de5-4ee87f4591de | -5.42559 | -44.64712 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ec5272b4-d537-3514-a628-171eb08a6d6c | -4.93626 | -45.46698 | 2025-11-11 03:59:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02c9696d-bd2e-3479-b3ca-0efdbeaa04ed | -4.74404 | -44.60036 | 2025-11-11 03:59:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eab55e8a-ee0d-31bf-bc79-49a677138c6f | -2.97137 | -41.58889 | 2025-11-11 03:59:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b55be42-e3ab-3046-95da-08e0b59380de | -4.59568 | -45.48886 | 2025-11-11 03:59:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73a1e0a8-8470-3fd1-a858-fb16f8db2275 | -7.13534 | -41.2581 | 2025-11-11 03:59:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d438f9e-151e-3abc-9727-343b98f9d0f7 | -4.82428 | -44.74812 | 2025-11-11 03:59:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 377b7b68-456e-3870-b9ef-5805f3b5e632 | -4.72272 | -46.46704 | 2025-11-11 03:59:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa49c62-a1ae-386a-9c35-4fbba28486c3 | -7.07357 | -39.67516 | 2025-11-11 03:59:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d42bb890-8c95-3e77-8a03-6dba1f8f76af | -4.45452 | -38.39368 | 2025-11-11 03:59:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 889a22b9-8590-3ebf-bfaf-94780c7622a6 | -5.64103 | -41.0817 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 543c8ba6-2f04-344d-85b8-568cbaa6e3e7 | -5.30416 | -40.91174 | 2025-11-11 03:59:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6973fb1d-3e28-3cb5-be1c-a2e5d9b4b3ec | -6.39438 | -44.50825 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e491e61-9f9a-3935-97e2-3904d119871b | -4.69027 | -45.6902 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b084617f-5806-3802-bc32-5ee94064d5bb | -4.64581 | -45.7626 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e4b860d-d904-3b59-a883-6d716821e85e | -3.63407 | -44.63123 | 2025-11-11 03:59:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bd0fd4e-e632-3dac-bda4-2636c0fae279 | -4.26561 | -45.96209 | 2025-11-11 03:59:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README12.md)
