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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52c3a369-a422-360b-b59b-1a1d258c2329 | -7.09213 | -42.73442 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 75058b8c-8fb0-368b-9466-f7df00822e42 | -4.64545 | -47.94754 | 2025-11-16 03:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46e83088-3dc9-3424-ba88-64f91889355a | -5.23296 | -44.35172 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b142421f-9a99-3e75-83f7-b2d73cf5c27e | -7.15283 | -41.75729 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1a295390-2330-3d41-815d-c140660550df | -6.71693 | -42.13527 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75757049-922f-3644-9a4b-ccefa38f9f33 | -7.1923 | -39.2073 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfcaecb3-766a-322c-897d-a054ede22e9d | -5.23965 | -44.3457 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5489b9d9-3145-3e19-85bf-530094038ff7 | -3.22293 | -43.35294 | 2025-11-16 03:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80567e98-fce5-30c1-9b6b-491ce54eb237 | -3.85596 | -40.77273 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c4a97cb8-bf6d-3f3a-9b8c-2b152892b517 | -4.83698 | -47.55256 | 2025-11-16 03:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a81b95e-a754-3a23-b233-b0cc5632a330 | -9.06082 | -44.75031 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c48c7799-834e-3375-b2c7-787c7d495d30 | -3.33043 | -45.85336 | 2025-11-16 03:46:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61ceff13-7001-3c85-9f0d-516bb6971fbe | -8.46128 | -45.14149 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86090720-6ff5-3fea-94ac-f59a30ed1756 | -6.72668 | -42.94944 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 64e2a1b8-6bb4-3f83-808c-af708d98af84 | -9.57652 | -44.61025 | 2025-11-16 03:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 57e21430-41b6-3c07-9703-86c641075e71 | -5.41802 | -43.25916 | 2025-11-16 03:46:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83488c59-98de-3cfe-bcbc-3d288fbeea62 | -7.3232 | -39.06728 | 2025-11-16 03:46:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38271d9d-d9b9-30ac-9241-f909b65c7a63 | -9.10841 | -40.46076 | 2025-11-16 03:46:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cb9fc008-bc0d-33ce-abd4-6e9acd0782c4 | -9.74259 | -43.95314 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb85ec9-d3f4-3ac2-8787-04afe676003e | -8.31471 | -45.41283 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 687f1e4b-6111-3337-ae60-cc16b15c01c8 | -7.04912 | -42.25116 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d17aad58-b268-3bb0-924e-d909bfb99eb1 | -5.48926 | -46.91883 | 2025-11-16 03:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00f222d1-1a55-37ed-8267-830404609311 | -10.00112 | -44.76821 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d31a35f-28f8-354b-9fea-9a60148738f4 | -8.57225 | -46.05176 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf17755-689b-3ec5-97b3-d97f4232854b | -4.8459 | -45.4317 | 2025-11-16 03:46:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bbcf185-cd1d-32ee-8d3f-3b132fb343e2 | -7.21892 | -47.98554 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e619b30-df89-3736-bcf5-02f3a4a43948 | -7.33685 | -39.33796 | 2025-11-16 03:46:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 917f3d19-d21b-373f-92a3-229ed3e258e7 | -9.72966 | -43.96054 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 318ddefb-cf82-3bde-be1b-bae35aff046f | -5.99985 | -41.91588 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 503b92e2-feaa-3c17-b402-2f97ade45f4e | -5.6466 | -39.74156 | 2025-11-16 03:46:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0f9e7ac-7b68-334a-90c1-940b7e454b72 | -3.93031 | -47.05261 | 2025-11-16 03:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9fd7afa7-b9e0-3d5d-a0d7-c35c70304291 | -7.19576 | -39.21043 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 2bfea862-bd48-375a-af72-fd90435bf848 | -10.00565 | -44.7725 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93bf5717-060d-33a8-8600-9b5092e5b49e | -4.46349 | -46.30854 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd5ee8ed-7c29-3b5d-8914-7a9eef478cc7 | -9.58166 | -44.61123 | 2025-11-16 03:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e1ec622-d9eb-37a4-ad6e-25b34f68a4d8 | -3.53795 | -40.65556 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ce46d3d7-cc5b-3b35-a706-e7d26af25d1f | -4.73843 | -46.3797 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b1cf5fd-3b8f-3f32-9cf9-ce14f378a2ca | -6.40193 | -41.46317 | 2025-11-16 03:46:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0b8c9ac0-2bb2-302d-b74b-175e3d1c39b8 | -3.8531 | -40.76282 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 820686d2-9e7a-3733-9ac7-02a758657117 | -10.00391 | -44.78171 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f91b6725-3149-344e-bc93-bebbb533db5b | -2.51978 | -47.81871 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c72b33b2-1009-3c34-81a1-c736bdb1275b | -6.72277 | -42.94326 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 674e577a-6878-3912-a3de-c284c8a744ad | -4.94074 | -44.53799 | 2025-11-16 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee985de5-374d-3519-b1b4-382df0f3f3ab | -4.22781 | -44.64096 | 2025-11-16 03:46:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89b75a94-8d3a-31bb-a2c3-04676ffe9318 | -3.94887 | -47.20318 | 2025-11-16 03:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3931505-6769-30c2-a647-440a3b8110e0 | -3.79307 | -43.37471 | 2025-11-16 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dea01c96-d02c-3e21-864d-f7ec18a5b563 | -6.30502 | -43.79113 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 773e062a-1a20-3e6e-ad44-af2e6beceb00 | -3.95794 | -44.85286 | 2025-11-16 03:46:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd2793d2-309e-30c9-83f8-81664f2735d3 | -4.96311 | -44.04233 | 2025-11-16 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18851154-f0e4-334b-8895-e4cf62fe7f23 | -6.90533 | -38.88325 | 2025-11-16 03:46:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 79957a61-57d0-30de-bd2c-c829961fbabc | -5.008 | -41.96646 | 2025-11-16 03:46:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 560c6459-fe52-3fc7-bf3d-bd69214f974c | -5.9953 | -41.91506 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d405c86b-bd79-31b9-bb5b-8ef7af630d3e | -7.19649 | -39.20599 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1e7df240-d8ba-3654-9199-76849e15994e | -5.71642 | -41.39781 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3713beb3-685f-33ec-8e6d-64f10fa1819d | -7.28514 | -46.71692 | 2025-11-16 03:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49d64ba2-068c-35ae-9059-6d22003e5bfe | -4.67598 | -46.73506 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67697257-696e-3b71-8927-e73c43c92b44 | -6.41446 | -41.46918 | 2025-11-16 03:46:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b7a96f0-43f4-3e8a-b1f6-15e9ef859092 | -6.72079 | -38.54982 | 2025-11-16 03:46:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fcd9cd30-817b-365b-ae78-f9956d6e2124 | -10.17056 | -44.49691 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a9df7a9-6a4c-3400-b4cf-b1c609dc7cd2 | -7.12268 | -46.15833 | 2025-11-16 03:46:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72d78db7-e167-37c1-b883-f1b6da7f2371 | -3.9921 | -44.27817 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d293d9f5-8a77-34b9-824e-af2682755bbf | -2.52795 | -47.81339 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 505e3632-ebdb-3c0a-b949-566600b486e9 | -3.32961 | -45.85818 | 2025-11-16 03:46:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab5d5926-9f23-3295-b46e-fe28188b0f6f | -6.46002 | -42.33088 | 2025-11-16 03:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1576a2cf-ea86-3c6d-9137-44bb07bb4692 | -7.26344 | -48.02478 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3aa6f286-525a-3675-bda1-310b197cf50a | -6.10679 | -40.37743 | 2025-11-16 03:46:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cced3a1f-1fe8-3ac5-bf87-40ebdd4d8c14 | -4.68808 | -46.31627 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 701a1e90-b376-3af0-a1fa-ff85f92065ca | -4.74296 | -46.39064 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 70a9ad49-c244-3fd4-98c1-78809f36486d | -7.04531 | -42.24593 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76088d07-7396-3b23-a988-8e311fec2267 | -6.31015 | -43.79217 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9eded4eb-70ae-3c72-a7a9-9bdc01decb02 | -3.99764 | -44.27913 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3198a1c8-ac17-34eb-9372-2bda4ccb7679 | -6.95368 | -38.72008 | 2025-11-16 03:46:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 891f4883-154c-3e45-b2ec-98e72b88e3f6 | -8.06615 | -43.10625 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| efce0b51-b54d-38ad-ba34-351e6edde620 | -5.23309 | -44.34885 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d759f92-d0a2-3315-b848-587095c9b54d | -6.68114 | -42.04559 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 35a6263e-01ff-3d01-aef1-ab0d17164dc3 | -9.5096 | -47.27663 | 2025-11-16 03:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69e4afc0-d114-3cff-95fc-f38b2c686646 | -7.36987 | -43.32411 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8243219a-b8fd-3dd2-926c-eab237a3a5ce | -6.69603 | -40.80879 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40d3542a-6628-31bd-9d85-abe864fd4477 | -4.69723 | -46.32137 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d7a3fec4-7a31-3797-8bc4-4fd048765cdc | -3.84722 | -40.77129 | 2025-11-16 03:46:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| adfa93bf-3b36-36b1-8386-8ddcbbb7a4d7 | -7.22663 | -47.98096 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b1ceca-f04d-37d7-b4f3-53bf543ad01b | -2.51273 | -47.81754 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6512383c-9507-33e1-bf6f-6454196beb2f | -5.47299 | -40.96769 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fdacb1be-6457-3406-bbca-9fee2c92b7cf | -4.69187 | -46.3154 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 812ee739-f36d-3541-b530-344f4ccf091a | -7.0183 | -45.16915 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9d5920b-6d00-3038-813f-85736d43342b | -9.33648 | -46.57773 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ad280ae-ba49-3395-9670-4b43bf4f30d3 | -5.23852 | -44.3499 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 154c359a-868d-3995-b8a5-da5dcf26343e | -9.99843 | -44.77672 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09c14f26-ce6a-3952-aef0-8e40f76f1b8d | -6.95132 | -39.55999 | 2025-11-16 03:46:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 738dc777-de60-323a-826a-22a298bfb2ff | -5.24799 | -43.90916 | 2025-11-16 03:46:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd3b21b-68b8-3244-a869-59701ddd7af6 | -8.41124 | -40.45311 | 2025-11-16 03:46:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| da89d286-ad8c-3dbb-94a0-69c2375e3093 | -8.14998 | -35.6931 | 2025-11-16 03:46:00 | NPP-375D | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0ccccef3-cf3f-3bef-958e-c15e8bd66612 | -10.00072 | -44.76412 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 574dc7a7-0e25-368e-b55b-7d1e537df518 | -6.0253 | -48.18631 | 2025-11-16 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca6dad02-4bc8-3225-87be-2433386edd0e | -7.27121 | -39.31437 | 2025-11-16 03:46:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40a88d0c-1445-33cf-99a9-ce4594337e57 | -5.18068 | -45.03931 | 2025-11-16 03:46:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa4e0462-6638-3fd1-a3d1-1044df1f2be6 | -10.16797 | -44.49477 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78dd9730-7006-32d2-a122-af0b2662d26d | -7.02683 | -39.29588 | 2025-11-16 03:46:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 098bb102-31f8-3032-9580-97ec4e6cbcea | -9.73562 | -43.96334 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e912e1e5-e842-306e-9bc7-23cd7f6230dc | -3.45839 | -46.12457 | 2025-11-16 03:46:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
