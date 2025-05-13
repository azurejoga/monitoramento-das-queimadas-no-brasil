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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 941b1a11-da77-3595-b8ef-3f78efdf2bab | -14.18571 | -45.48259 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f317fec0-467b-3691-8e65-ad9949a74dc8 | -13.62303 | -54.87994 | 2025-05-13 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdf29589-2e37-3c22-a5d0-401b6120f2d1 | -13.97238 | -56.7877 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d512c8b-e6f8-32be-ba20-3c4e3c064eb0 | -12.29006 | -52.4934 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b868bec4-dcf6-3150-888c-2fd73006b4d2 | -12.81648 | -51.58193 | 2025-05-13 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6be8d959-b792-3e94-a6ee-aadddbf8353a | -13.97737 | -56.79948 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c48e281b-509a-31c0-a293-28ca19e09dcd | -11.25871 | -52.47507 | 2025-05-13 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a353fbc-ecb9-3ab4-a889-442e8e074b85 | -11.39707 | -52.94451 | 2025-05-13 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2248859-b183-3aab-ba68-16f844f83668 | -13.984 | -56.80054 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f4a3a8b0-f65e-3906-ba27-46f38ffaa0fd | -14.185 | -45.46593 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12143cfc-64ec-3975-8775-1492e0c47bb9 | -13.06767 | -52.02071 | 2025-05-13 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b7b66a-d328-3390-817d-4af900cd6884 | -13.09365 | -52.29229 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ca529c-e4a6-3b89-9ac9-0432d7173791 | -14.19657 | -45.47805 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d22bd756-d0be-3f5a-a05c-25dd39630584 | -13.55233 | -52.86393 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41ee8b01-0bb8-3079-a0f6-5b340563be2f | -13.96906 | -56.78716 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9eaa9582-c606-31bc-8bba-767f150c5fc9 | -11.25554 | -52.46966 | 2025-05-13 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 731adbed-4f1b-3475-b359-e0b62b541400 | -13.57562 | -52.86736 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a800866c-a9fa-388c-87ae-9edf3717e6bd | -13.09717 | -52.29642 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64013391-6719-3bbf-a82c-0e81f4161319 | -13.57493 | -52.87241 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ddb05f78-54fb-36f7-a13e-a42834420dcd | -13.57425 | -52.87738 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4618fb2f-91ee-3e42-8e31-7b8201d3bb7b | -13.55941 | -52.87013 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4f0d98e-5f37-3ce5-a556-8599900141d3 | -13.09317 | -52.29583 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f93fef-1dfa-319f-b0cf-59c11f9de0c8 | -11.06024 | -60.88617 | 2025-05-13 05:06:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3659696a-538d-32c5-bcf3-e1af3e4a79b3 | -12.82065 | -51.58253 | 2025-05-13 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff1aaa7c-c9c4-3f1e-b249-cb70729529ec | -14.18678 | -45.47192 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0c11af1-d0cd-39df-8dae-8bfa67e15f80 | -12.69082 | -58.12732 | 2025-05-13 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d066a91-d8e1-32ba-aeaf-723401e9f0a5 | -12.68349 | -58.15179 | 2025-05-13 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 990668ce-7212-3f54-89cc-e40c878e186d | -14.19207 | -45.48334 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad03a7ce-566a-3ec6-9d24-1133fb74307e | -13.06717 | -52.0244 | 2025-05-13 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdbeee91-4607-397f-9eb0-26d734dec826 | -12.2889 | -52.47258 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aed19e55-cebb-3f84-893c-8949cb8791a0 | -12.22181 | -63.78085 | 2025-05-13 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808103ef-720e-3b6e-96a8-62f90aa921e0 | -14.18443 | -45.47128 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3349419d-b73d-339e-ae13-db032807fe87 | -12.00536 | -62.83986 | 2025-05-13 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f05e62b3-f6a8-3326-ae22-657336d3b72c | -13.06818 | -52.01701 | 2025-05-13 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb8a6393-1d64-3891-a772-f05875fa682b | -13.98014 | -56.80357 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37bbc428-bbe3-3268-acb0-dffe66636c90 | -13.39777 | -47.63316 | 2025-05-13 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e34943b-1ed8-3bbd-ac53-342062b11345 | -14.18385 | -45.47659 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2406353a-fb19-3f16-af65-35a7c6198f14 | -12.18213 | -46.71442 | 2025-05-13 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60e245a6-85ee-33ce-85c4-e777511ce362 | -13.04531 | -53.72608 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3e1d38c-3c91-30d8-8e09-1fe202dc66b2 | -11.7808 | -48.69844 | 2025-05-13 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64353ba7-03fc-36b3-9441-319774578c02 | -12.28879 | -52.47107 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7ece1c-9bc8-3067-83d7-e71d33af9f75 | -13.06412 | -52.01638 | 2025-05-13 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c84e34d3-23cd-3ef4-bb6a-ba4b178150a7 | -13.98123 | -56.79645 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 175651a4-49ea-3fa3-9b79-89ddd2acefd1 | -12.29672 | -52.47377 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bcada612-f17a-39b5-95ce-2efa8754996a | -13.97682 | -56.80304 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 204bc641-03af-3f27-b349-733c70791dec | -13.55553 | -52.86955 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 174615e4-2bf2-306e-b65d-441844b35327 | -12.15105 | -48.01358 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 03326d83-9464-35f9-8c0c-0d34e6b4da5f | -12.15065 | -48.01685 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 26c2655a-fc40-3368-94ab-42e7e2568576 | -13.04962 | -53.72218 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c2a96b9-159b-3ca9-847a-33d64f35438b | -16.17753 | -57.69921 | 2025-05-13 05:06:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e219620-1986-3fd7-bc20-02125e6ef359 | -13.56397 | -52.86567 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b72cd21-9d5a-3bef-a78c-63436024f7a9 | -16.55263 | -46.84844 | 2025-05-13 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce2c584c-1b6f-3384-a347-9f4eb4adb258 | -13.57036 | -52.87686 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ae4bd7ad-6c3f-3099-bc6b-6a7486736b56 | -14.19261 | -45.478 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97fed463-51d1-385a-b2fd-861a433946c3 | -13.55872 | -52.87516 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2645df3f-229c-3dbd-ba65-d11e74e02f58 | -12.68968 | -58.13446 | 2025-05-13 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1a691ac-3c53-34ba-82e0-7cb73c51f03b | -13.55165 | -52.86896 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 563a30be-69c4-3ddd-b7ce-07e3cffd2aad | -12.30063 | -52.47435 | 2025-05-13 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 87655656-58c2-3890-bf9e-887ec724f2ab | -12.15145 | -48.01033 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 38c8d240-2d51-376f-bded-d7d09bd21f08 | -12.63251 | -54.90002 | 2025-05-13 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c277f98b-3d15-39ec-8a59-081063197497 | -15.42726 | -60.27444 | 2025-05-13 05:06:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed84da16-7403-3dc3-bd56-58880ad5afbb | -13.98455 | -56.79697 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 827b706f-eeb8-36d3-bd42-37f2aa0fceb1 | -14.19021 | -45.47733 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9effd9a-ecc0-3fd7-90be-c2aacb562672 | -12.35101 | -49.95421 | 2025-05-13 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85c57e85-043b-3354-8626-aeb5a0d5fa03 | -13.98291 | -56.80765 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ea333e78-c3ad-3924-9e39-852c54e027ec | -12.68682 | -58.15233 | 2025-05-13 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1df58f9-b433-314c-af24-7049752d88ab | -12.15711 | -48.00775 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73784fec-6fad-3fe2-a643-354d62557b25 | -20.21869 | -46.73104 | 2025-05-13 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bed52360-f3f6-3366-bfa7-de8f5dac935f | -19.36482 | -55.25779 | 2025-05-13 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c855ca44-72e5-33d5-a63c-ddcabdd314b9 | -21.79045 | -52.73904 | 2025-05-13 05:08:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c64b600f-db9d-3274-9e4f-5002ff7f7036 | -18.34229 | -55.59328 | 2025-05-13 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9cbd0f03-9d43-31d9-a3d0-d1964ebf4e15 | -21.78994 | -52.74345 | 2025-05-13 05:08:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1759bb5-fa41-3765-bac4-edcc6e0735a2 | -18.33896 | -55.5867 | 2025-05-13 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ee0cd333-d3ba-3c98-96fc-52a452bc0451 | -21.04867 | -55.7685 | 2025-05-13 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98ca742c-d034-39c0-91ff-af47acc880b5 | -18.34193 | -55.59146 | 2025-05-13 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cc626c16-4961-3f27-a607-965624260f3a | -18.33934 | -55.58852 | 2025-05-13 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9d111d48-b350-3211-87e0-e79c908ee182 | -21.78068 | -52.74667 | 2025-05-13 05:08:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9a00907-2bf8-33a2-8747-ca15928b745e | -20.4788 | -53.67539 | 2025-05-13 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9501f6d6-397e-3d2e-a21f-c12f5120768f | -21.78506 | -52.74726 | 2025-05-13 05:08:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2539f056-ed69-3671-aefd-ba6554c7ee83 | -19.36427 | -55.26025 | 2025-05-13 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5412d67e-da30-38c5-9cfd-d3c45c47453d | -18.14041 | -52.3588 | 2025-05-13 05:08:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1018c23e-e82f-3d29-9153-4a59f23ce41e | -20.22453 | -46.73712 | 2025-05-13 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e694dc4-2288-3647-b2e5-22213967647b | -18.33838 | -55.59091 | 2025-05-13 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 15f78d64-3ae9-35e1-b4e3-5d80f8c85a17 | -20.22098 | -46.73683 | 2025-05-13 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2111b87-f1aa-30d8-828a-a3cde6abb4cc | -20.22147 | -46.73142 | 2025-05-13 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00108ed4-73ae-3946-a273-f6edb6ac2bb6 | -13.971 | -56.8077 | 2025-05-13 05:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 4db2103f-9c56-32db-8b98-9661554ce346 | -13.9905 | -56.7855 | 2025-05-13 05:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 835cebec-1f4c-3e69-accf-99316f6c13c3 | -8.07 | -43.1216 | 2025-05-13 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 2a54af03-4206-36b1-ae75-cbe7c7c20219 | -8.0889 | -43.1196 | 2025-05-13 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 0c313796-c553-3a79-85e6-270d74500409 | -13.9902 | -56.8058 | 2025-05-13 05:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2f5f7aa7-7da5-319f-a363-884de82d1eef | -13.5683 | -52.8783 | 2025-05-13 05:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 11bb8754-442c-3bfb-ac44-4234d87fe75e | -29.32827 | -51.91399 | 2025-05-13 05:10:00 | NOAA-21 | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dc19c40a-0eaa-3600-bfb9-69b8e169cd7d | -29.32796 | -51.91753 | 2025-05-13 05:10:00 | NOAA-21 | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6232d067-0244-3cc2-834d-93c5ddf6d433 | -8.0889 | -43.1196 | 2025-05-13 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| d37657a2-db09-3332-85de-3dcddb9db4d4 | -13.5683 | -52.8783 | 2025-05-13 05:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 255a0401-33f6-3516-906d-a353fcbe8427 | -8.07 | -43.1216 | 2025-05-13 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 3d9ed4d5-40a1-30f5-87d9-0c1bdc56369b | -13.9905 | -56.7855 | 2025-05-13 05:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 13a7b44b-2991-33ff-8be4-95db95d20ccd | -13.9902 | -56.8058 | 2025-05-13 05:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fe218fc3-a72c-30db-a3af-039a0fb747e3 | -13.5683 | -52.8783 | 2025-05-13 05:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| dbe028ce-e132-3ad0-9a17-00452e14a8b0 | -13.9905 | -56.7855 | 2025-05-13 05:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |


[Clique aqui para ver as próximas entradas](README11.md)
