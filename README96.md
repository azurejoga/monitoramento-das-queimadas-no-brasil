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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1eeee29b-fbc7-3ad3-9445-b9fcb740819b | -7.59842 | -55.69988 | 2026-10-01 12:42:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9071d6bd-d6d1-348d-b44a-42c7623b625c | -7.62926 | -55.05328 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5fd06216-719f-3c3d-be51-4152cbbeec4d | -9.43106 | -55.77107 | 2026-10-01 12:42:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| adc9d2cc-b423-3f50-aa03-24b5071279dd | -10.4096 | -53.77222 | 2026-10-01 12:42:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 5ed54f6f-4998-312d-ad70-40bf910582aa | -8.15895 | -54.80346 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 197f642a-bc50-3053-a39c-2eceebb7f9bc | -9.7816 | -53.84113 | 2026-10-01 12:42:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a3cbe0fb-8763-3224-8bcf-aa25e808b1d0 | -5.85679 | -57.75206 | 2026-10-01 12:42:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 25b528ab-498f-3d07-9ee3-e31bead68c4c | -6.60302 | -58.59166 | 2026-10-01 12:42:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 19639b5b-2545-3715-8dfc-298b341611da | -8.96428 | -62.35093 | 2026-10-01 12:42:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0753d7c4-df27-3c46-b38d-3e4b0643806f | -5.91552 | -53.46377 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 83a94056-7e7c-3bd4-9c92-b893724ce8c1 | -7.35106 | -55.59711 | 2026-10-01 12:42:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 05679169-d928-3cb3-b436-a602d5fd4ab7 | -10.53535 | -57.75604 | 2026-10-01 12:42:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 85fdbea3-91b9-3467-ba0f-5be567959301 | -9.76421 | -61.97942 | 2026-10-01 12:42:00 | TERRA_M-T | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cde440b9-9cdc-3e33-a3b0-15f5e0b070b8 | -5.98254 | -53.53338 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 2c008a97-45b0-3060-a1d7-368095da917b | -6.70205 | -55.05194 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 27b6d398-af73-3816-9cd4-c6e4cb193d3a | -5.85268 | -53.47736 | 2026-10-01 12:42:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| d6df934b-c372-39ab-aea3-78e2ee6f78fa | -6.90673 | -58.91933 | 2026-10-01 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e05a0d0b-c9df-3f6c-9dc7-2a9dbb7b19ff | -7.62651 | -55.07502 | 2026-10-01 12:42:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6194e8df-4be7-349a-be22-8ecde9cd203c | -5.9152 | -53.4762 | 2026-10-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9674aa3a-6ceb-36fa-9b79-b6c6fa5e692e | -8.34 | -44.1427 | 2026-10-01 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 195de134-0a9e-30ff-a9db-296dc60f785d | -9.861 | -44.9807 | 2026-10-01 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 44f41287-b1ce-3f8a-ba81-00f765895c8f | -9.7843 | -53.8344 | 2026-10-01 12:50:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4f074ced-5766-3219-bbe7-dbe648a06256 | -8.6259 | -45.3737 | 2026-10-01 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| c16d73e1-b671-3a06-88d4-c86b9e2569e2 | -10.6688 | -50.7529 | 2026-10-01 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ea3b3837-7791-3dbb-8f40-4c5ac25c64fd | -9.3881 | -49.1473 | 2026-10-01 12:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 93b085ac-17ab-3352-b4ba-fbd6ff633359 | -14.377 | -44.7534 | 2026-10-01 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 478cf8a7-d9bd-327a-b50f-b38a411c8cbe | -9.9973 | -50.1393 | 2026-10-01 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3a39900c-f5a5-3c69-804c-d051801dedfc | -16.9909 | -45.4594 | 2026-10-01 12:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f8365392-c3e7-3441-b13c-f37555cbd88e | -5.9151 | -53.4965 | 2026-10-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| fb97f446-1836-3f8f-87c7-229fcb194fe7 | -12.1857 | -48.4345 | 2026-10-01 12:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 28aa3040-3151-3291-a7eb-e95b749a8c8d | -7.0798 | -42.3255 | 2026-10-01 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| fb8825c4-46ec-3cae-b6d9-4064a6aa9599 | -11.2275 | -45.2143 | 2026-10-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 50c8eb94-0d46-3ad8-b5e9-52d27ae86802 | -14.9215 | -41.5086 | 2026-10-01 12:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 03a30924-b2b5-3277-b682-4d1f5daf5e05 | -11.6203 | -43.5485 | 2026-10-01 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 53dcb1fa-1a59-397f-aba2-0818d63e8fe4 | -9.9026 | -50.17 | 2026-10-01 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 9fa34db3-8a8a-3bae-ae2e-469fce81dfdd | -9.9784 | -50.1412 | 2026-10-01 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0fe0ae6a-f20c-3302-9b66-16703c922497 | -9.224 | -45.8301 | 2026-10-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| cee4d58d-11d0-3a7b-9e62-8bcd80837a1a | -8.0159 | -42.9154 | 2026-10-01 12:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 327.3 |
| 418fc765-5bcb-33ec-b97d-892ff80e2fc3 | -5.8597 | -53.479 | 2026-10-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f6031459-f3a6-3f36-a2e4-47da2159b987 | -6.9419 | -42.8598 | 2026-10-01 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 7dcff2bd-fcd7-312d-ae2d-779c82eb02d7 | -8.3074 | -46.7549 | 2026-10-01 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5d07cd4a-b163-3a35-b78a-7fdd30ae7d4c | -8.2099 | -45.4848 | 2026-10-01 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 04335c96-247a-312a-bb7d-4ff4efece898 | -11.5384 | -47.1664 | 2026-10-01 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 65eccdf7-92d6-3652-8780-d3be38da4e5b | -14.3574 | -44.7569 | 2026-10-01 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 909b70b8-69ae-3cc6-8f1b-15e25f5c1550 | -14.3379 | -44.7605 | 2026-10-01 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3fb3ac61-0b32-31fb-a494-739d0f28c7cb | -6.3215 | -51.1274 | 2026-10-01 12:50:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 40739d87-8e73-3e82-b7f2-3aef62c80335 | -14.3384 | -44.7369 | 2026-10-01 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 1ab49676-2f0e-3e6b-ad40-4a5e070df964 | -11.2278 | -45.1913 | 2026-10-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.5 |
| e3d1c7ad-aa31-3c25-8ae7-0380123c85f8 | -6.3401 | -51.1263 | 2026-10-01 12:50:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 70b30da6-ed73-3d76-944f-8d4032b53822 | -8.3211 | -44.1447 | 2026-10-01 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 61d9d0b5-2a13-3452-a958-209af33f0632 | -12.5518 | -47.1837 | 2026-10-01 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 69922c29-47b8-3fa4-ad15-bd4c6aee9729 | -8.1908 | -45.5093 | 2026-10-01 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7632bc1e-57e1-3b29-8a97-10f6b86a1220 | -5.8412 | -53.4799 | 2026-10-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| d682cbdd-8543-325e-aa8e-141855443349 | -8.1401 | -43.5361 | 2026-10-01 12:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b200255b-d58f-3f42-84bf-28482eff7de6 | -8.1212 | -43.5382 | 2026-10-01 12:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 42385167-c0d0-3f15-8d04-aeec1c34cd52 | -11.2282 | -45.1682 | 2026-10-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| da82a23e-eb62-31fb-9a30-306cba34ff5f | -8.3208 | -44.1679 | 2026-10-01 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 8722dd90-c7d7-3147-af7d-c25ed5c827d2 | -5.8596 | -53.4993 | 2026-10-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0edcf79b-2c7c-3ea1-99b2-d4a0667bdf16 | -8.6265 | -45.3282 | 2026-10-01 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fa131a41-907b-332d-91a6-be0dde81d434 | -8.1911 | -45.4867 | 2026-10-01 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fb0f8012-ac9f-3358-8b22-b7b4546ae798 | -7.0801 | -42.3017 | 2026-10-01 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| b439c002-c435-3f39-9567-77f95e75de37 | -8.0166 | -42.8681 | 2026-10-01 12:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 2f544102-5f1b-3d7e-95c3-02c29df12f8e | -14.659 | -41.0175 | 2026-10-01 12:50:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 2a5cf767-63fe-3bd0-a1ff-bcf28bf84c94 | -9.8064 | -44.8265 | 2026-10-01 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f42d5d2c-d836-3f59-9fe8-da7765f44f94 | -8.1215 | -43.5148 | 2026-10-01 12:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 07adc2af-5981-328a-bb1d-dceed09adffb | -8.3397 | -44.1658 | 2026-10-01 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 1f9fe9a6-9d4c-3065-85d2-a43fa3822999 | -8.6454 | -45.3261 | 2026-10-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 28a6be89-2604-33fc-8c87-4571e64e0d42 | -8.2886 | -46.7567 | 2026-10-01 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 24ea1d4e-6f9b-3609-ad34-e011d3a60ad5 | -8.0355 | -42.866 | 2026-10-01 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 773b7d95-ec4b-3e68-a0e7-5608f5184ab0 | -8.6265 | -45.3282 | 2026-10-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 11857f14-9b0b-3d86-8c72-ee629737d676 | -8.6445 | -45.3945 | 2026-10-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 84dbc972-2129-3885-8bed-8644c9a4c316 | -15.6481 | -44.7217 | 2026-10-01 13:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 88afd146-0d00-368c-88bb-d51272a0c193 | -7.0798 | -42.3255 | 2026-10-01 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| e246fc88-a76a-33c3-9b30-f17103bf09cb | -10.0895 | -50.3009 | 2026-10-01 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9af1018b-0f15-397f-bceb-b42917abe7af | -9.8807 | -44.9323 | 2026-10-01 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 3bdce823-c6a3-39f4-bc86-c457b11abecc | -14.3384 | -44.7369 | 2026-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 12890208-56d7-3cd8-aa3a-ad0debca64ed | -9.8064 | -44.8265 | 2026-10-01 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| aa9c9745-b402-3bb9-9613-a2237cc72338 | -9.3879 | -49.1689 | 2026-10-01 13:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 34508ce5-7fd6-3023-b9a9-9210e1803827 | -8.0162 | -42.8917 | 2026-10-01 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 582.6 |
| 88144dc0-3a2e-38bc-b054-5d60591634fc | -8.3397 | -44.1658 | 2026-10-01 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 386073a6-10d1-35ae-93f7-d68f1ef53134 | -8.34 | -44.1427 | 2026-10-01 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 86864354-6519-3283-8f11-ddee6f89dd44 | -8.6268 | -45.3054 | 2026-10-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0208f8d8-8452-308c-8de7-3acd3d3311f6 | -8.0166 | -42.8681 | 2026-10-01 13:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| a29c7857-f8ff-36ff-b93e-570fd5c06744 | -7.0801 | -42.3017 | 2026-10-01 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| ee6bf892-76f1-3710-97bd-1710fcb6909d | -8.6262 | -45.3509 | 2026-10-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 1ccbefc7-477d-3eaa-a880-c8c14555e937 | -15.4978 | -46.1294 | 2026-10-01 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 143.2 |
| c407085f-9a6a-3338-8d7d-e495656498fa | -14.659 | -41.0175 | 2026-10-01 13:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 2a7242e4-5eb7-3b5a-8920-20fc18a9a1d6 | -8.3263 | -46.7531 | 2026-10-01 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 9a774b2b-271a-36f2-b5dd-832a44b1be59 | -14.3574 | -44.7569 | 2026-10-01 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 5df95f42-1071-3ada-a6fe-e3024e36ebef | -8.2099 | -45.4848 | 2026-10-01 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2b59ce25-c4b5-3877-b9ce-c1a54f1028e8 | -5.8597 | -53.479 | 2026-10-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 3795702a-4f43-3d22-948c-d0188412128a | -5.9151 | -53.4965 | 2026-10-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 9b748232-1668-34f4-af8b-a2ecab237d25 | -15.5175 | -46.1257 | 2026-10-01 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 2788be2c-210c-31ff-a8c9-6ead61d8a382 | -8.1215 | -43.5148 | 2026-10-01 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 47528ea0-0212-3fbe-9725-b70b398003d4 | -7.0609 | -42.3274 | 2026-10-01 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 16969ffd-21e6-3139-960b-c9c5e811dae3 | -16.9909 | -45.4594 | 2026-10-01 13:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 64abf3fb-a253-3144-a847-3a08c056576a | -11.2282 | -45.1682 | 2026-10-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| a948009f-515e-3fb3-809d-44c8c448acb3 | -11.6199 | -43.5722 | 2026-10-01 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 0ef4acd4-c752-3555-b856-ddebdc6e96a7 | -8.1908 | -45.5093 | 2026-10-01 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a54a420d-bdda-37f9-9fab-2c86e67d5b60 | -5.8412 | -53.4799 | 2026-10-01 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |


[Clique aqui para ver as próximas entradas](README97.md)
