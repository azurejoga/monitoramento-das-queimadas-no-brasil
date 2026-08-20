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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c43db5c6-a33e-3c8b-b1ac-3a29c9dc7356 | -4.95756 | -56.27131 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f4fd1e1-0b3d-3f99-a1f5-b7304466f3d0 | -6.696 | -59.09738 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1703d725-6e88-3815-9185-a6a3c23f02be | -6.43408 | -52.76429 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3f37f7-7fe0-33ee-ac99-9e9fb42c4651 | -3.10826 | -61.21246 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 791c92b0-dee3-343e-b367-6e4b7cac43d9 | -6.34102 | -54.89836 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0ceecd1-1cbd-3fd6-83a3-959b9b113295 | -6.38195 | -54.94051 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 451e1f10-e990-3059-90fc-668c75fa5449 | -6.71828 | -59.09681 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b55bf7e-1829-37d4-befe-fc18b33b0249 | -5.80248 | -55.71732 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f411d25e-fd5f-37f0-a23d-5e11f1758347 | -3.93629 | -59.33176 | 2026-08-20 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f370d5df-2619-35db-a786-6e228eb4f337 | -6.34432 | -44.07631 | 2026-08-20 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76e171ee-e5d4-3982-8daf-fed971f43217 | -4.95701 | -56.27479 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a9753fa-87e3-3754-9846-e705a2267773 | -6.69792 | -59.09878 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b93c0b2-f7ee-3c95-91d5-69841224eeaf | -2.57443 | -47.23601 | 2026-08-20 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 655f4070-c4b1-3595-83f2-06dd7f8f2ee6 | -5.82342 | -57.64186 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 17849c4d-5966-30a6-a69f-1c8ed7a90f53 | -6.42977 | -56.18845 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a18711e-30ab-3034-83f8-9bfc0877c4f0 | -8.47683 | -46.96598 | 2026-08-20 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 019b7a61-dd6e-30e5-8109-ca17e013cdb6 | -6.23961 | -55.42213 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee79fe54-33dc-37c2-bfca-20cc3e6585ea | -6.43608 | -52.72623 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a76488f-068b-346f-ba9f-a7092d596d1d | -6.99644 | -48.0428 | 2026-08-20 05:04:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f7d8deb-be09-3fbf-b0e4-fdc153f49a67 | -6.36139 | -51.74146 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 482db00f-842c-3cce-a95d-b39445b82d98 | -6.7104 | -59.09975 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8635341-344a-377f-b588-478eb5b17311 | -2.07726 | -56.5541 | 2026-08-20 05:04:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cce24dc-5d3e-30f4-b2c9-ecd289af64e7 | -6.24561 | -55.40532 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f879f86-dc9c-35e6-bf06-0bfee9c50df7 | -6.0992 | -57.69643 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcd15104-2de6-3072-894f-743bbeefe95f | -5.49554 | -60.12969 | 2026-08-20 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f85bb272-0338-3c98-acff-0aeae03fca83 | -6.88862 | -56.42783 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f26e5cdf-2f73-3da7-8724-0b1c76f0d926 | -8.48863 | -46.96032 | 2026-08-20 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c524f1b-42b7-335f-ae79-2e022a27fb44 | -5.79749 | -55.70595 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a730bc32-30cb-3f3d-83f8-d370d7343a2d | -6.12534 | -57.70817 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f42f9047-6bf6-366d-b3b4-98df34833260 | 0.80838 | -59.86914 | 2026-08-20 05:04:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02a52fcc-3e2c-3535-96dc-ce3cc4375ffa | -6.13081 | -57.87327 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d930ec5e-f1a3-3f1b-9caa-28ec38fa0bc5 | -6.60891 | -58.38928 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 353b450e-428a-3850-aa46-780fdd5471bb | -3.10462 | -61.20764 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 960e23c8-859f-33e3-806a-80394bdd16ad | -6.41971 | -54.93911 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b090eb14-6011-3f58-913b-5b1d0261fd00 | -5.80079 | -55.70646 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c6ca37f-767d-3a55-a9d0-127cc9d7c9b1 | -6.38529 | -54.94101 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49b8450c-1ff5-3c0b-a016-49e9e3bc4ade | -7.34822 | -45.82925 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2235a19c-8286-3172-a9bc-f57a074611d7 | -7.0503 | -56.525 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 014381d1-371b-3149-8cf7-8aacdf1a2d6c | -2.64585 | -47.98808 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c132702-0836-36ee-8d50-8afda03d69f5 | -6.78062 | -42.88564 | 2026-08-20 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 23f59513-b3be-32c4-a40f-65d50e91bdc9 | -6.44179 | -55.63065 | 2026-08-20 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 396e3621-ab92-32ad-a982-f8582e116cfc | -6.39141 | -54.94556 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29a8e983-7354-3e85-90a8-fc1af9b11660 | -5.80472 | -55.72474 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebbc394d-1d06-34f3-896a-9f805332b53f | -6.88699 | -56.43823 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c95261b2-a487-35fa-b614-f202a09aed87 | -4.05957 | -56.3373 | 2026-08-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f44d530-039f-3cae-b0da-837e83547ea1 | -8.05472 | -50.10796 | 2026-08-20 05:04:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aed58578-f0c2-3a74-bd65-bc4ff53e18d9 | -6.71108 | -59.09561 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe5055b2-9e4c-302e-9f59-c220e9354957 | -6.25608 | -55.40339 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e60419-d8c5-3968-8e4a-5fb3b37026e5 | -5.79364 | -55.70889 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2c9c92a-a76e-3753-a509-91b7bb6337ce | -6.71465 | -47.78589 | 2026-08-20 05:04:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42002a07-8db4-3a8d-a282-a7d0d593e87b | -6.69301 | -58.94546 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c03e156-d150-38bd-93fd-56732acb65a2 | -7.35507 | -45.822 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53a803a0-1101-3314-a8cb-48ce6f236fe7 | -7.97146 | -44.67136 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2aabc0e2-0992-3312-a597-572f8f5057d3 | -6.70524 | -59.08619 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7360f083-9f7d-34d7-b3d5-b96f393af104 | -2.54223 | -47.16391 | 2026-08-20 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 914e4bf8-fe31-30f4-a0b4-fcb387e384b3 | -2.1698 | -47.48487 | 2026-08-20 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96175d44-a1f3-370b-a261-2fa0659ce322 | -6.5825 | -58.97887 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 99f1eac1-466b-3b0b-8909-165d0de41c9f | 0.80778 | -59.86535 | 2026-08-20 05:04:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3519c33f-700d-3a79-b9db-ad963bb764b7 | -6.43831 | -52.76066 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0084c0c-e60d-3099-bf1e-1c6c6ae74241 | -4.18533 | -49.40379 | 2026-08-20 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 260c1509-8473-36b6-a17d-e4f50c2dcbc2 | -6.08585 | -57.91227 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25fec2fd-5827-3952-b079-e1712004659c | -2.80985 | -48.59363 | 2026-08-20 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75ad1588-6162-39af-a32f-237eee7e7829 | -6.42646 | -56.18793 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e90652a-0a75-3e87-8e54-950d035a6afa | -6.58807 | -58.96707 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97d37a04-ca3f-3e46-8a5f-44fac3f6b4d0 | -6.87303 | -51.86732 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d63d54e-aa55-3723-85eb-d81358281cfd | -6.38808 | -54.94504 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cb5b4a4-84f6-3ebb-a616-ee60eff7f2d9 | -6.44143 | -52.73985 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b1638a0-7b1c-3ca1-8e37-7d0ad32bc25e | -6.7032 | -59.09855 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8910112-6b88-3c79-951c-73a6fc63f125 | -6.41917 | -54.94263 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 943df615-56e1-3326-b8bb-68d692cb6037 | -6.38862 | -54.94152 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15b4f681-8d28-3fc9-ac8b-0854dae307e6 | -5.42868 | -43.43713 | 2026-08-20 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fbcb3e3-154c-3534-ad8b-dc047c886421 | -6.01542 | -57.87072 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ccd49f0-00fd-3807-a967-76079971b903 | -5.80579 | -55.71783 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72a7d5b0-ff50-3f10-862e-486ec7755ca0 | -7.05708 | -56.61152 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab81cf03-0657-39b6-ac5e-5b3198f1f96b | -7.75738 | -49.20369 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b547fb3-2ab5-3d68-8983-2d13c6ea1114 | -6.69659 | -59.10711 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2474f84f-d5c7-392e-afca-8041820589b6 | -3.0976 | -61.22331 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e113a95-ec40-3ec3-a712-dc36223f69d5 | -3.09585 | -61.19456 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ebebc58-a954-34a6-a8f3-830707b0afe1 | -6.59391 | -58.97652 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2f12d6f-387f-3418-90ae-07f951fbf639 | -6.44455 | -52.71895 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a736d15-a1a4-30fd-98a6-fc56216274fd | -6.72097 | -58.59144 | 2026-08-20 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a951f49c-2ff4-376d-9ff7-9bc134cc0695 | -7.60731 | -45.16992 | 2026-08-20 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03935c89-2f5f-3d6c-b6b4-b27fa79ca4de | -6.74507 | -59.04586 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b0751e-d317-34e2-abbb-873a92a742f4 | -6.24453 | -55.41226 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57e6c51a-708c-3569-a6ff-278dd309a3f0 | -6.94 | -52.78709 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19afd1c0-1c56-31d1-996d-828eb94c4c1c | -6.11568 | -57.70288 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11e0a3ee-a577-3a10-a69f-93fc0d3515e9 | -3.97577 | -49.19584 | 2026-08-20 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd7fb8bf-761b-3f56-aa5b-555e8a7cc3ed | -8.46694 | -46.95745 | 2026-08-20 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8424d256-1f63-3979-940c-efdc0d6e7ee5 | -5.79864 | -55.72026 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e21a415-a3b0-34bd-8cdd-6253d83406a7 | -5.80356 | -55.71042 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46411880-69ab-35e7-80a9-9f2aa56b4954 | -6.40529 | -54.94409 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08692d63-fbf4-3c1c-ae8f-245fe0930465 | -6.10638 | -57.73932 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad73d1a9-6a88-329c-8ee1-73a77512bcce | -7.35452 | -45.82604 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| acf3423d-ab7f-36eb-aed5-0ac2bca13387 | -4.38861 | -55.47383 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e677f9e6-478e-3b68-b28c-d92b3f0a7a6b | -6.39195 | -54.94204 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00eedc24-709e-32a5-afb4-501a2dd0c83e | -6.69531 | -59.10153 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57aefb3b-5a3a-3814-a0f5-1bbae13cb27e | -6.63885 | -56.41638 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0223d3ae-0616-3f06-950f-d578a42bf5f7 | -8.36461 | -46.33639 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cfa2f8a-a9e2-38f8-a0e6-d888c77798aa | -4.09964 | -42.49848 | 2026-08-20 05:04:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9dc17f10-1f7b-36c5-9ed2-be8d5ec5403f | -6.6471 | -56.40701 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README45.md)
