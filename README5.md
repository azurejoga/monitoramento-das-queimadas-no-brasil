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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36e5ee04-c6f0-3500-85d1-1b7d605c4ff2 | -9.6633 | -36.11094 | 2024-12-19 02:49:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 69491a4b-7f41-3502-9757-b0523e4a23f9 | -6.47608 | -35.25769 | 2024-12-19 02:49:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f2061803-1d8a-3321-8733-bb06fab5756f | -5.2108 | -43.3067 | 2024-12-19 02:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| aa514edf-94f4-37c8-92ec-f62d533d8446 | -5.2108 | -43.3067 | 2024-12-19 03:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5c8d9213-e3b5-335d-9c50-bb1f2c240aa7 | -7.915 | -35.1997 | 2024-12-19 03:20:00 | GOES-16 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 46.1 |
| 10471334-a4c8-31f6-8970-f211b905606e | -1.75954 | -45.5877 | 2024-12-19 03:42:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71ea48a5-7bfc-3e72-8531-ac3a260c2fb6 | -1.7596 | -45.82236 | 2024-12-19 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0458556-0fe6-3531-b3f8-c65cbf37f1fb | -3.42937 | -41.94971 | 2024-12-19 03:42:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2821ce47-c9d7-3f3f-b019-9621f42b18bb | -4.99255 | -37.09816 | 2024-12-19 03:42:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cbedf704-63a2-3b5d-a95d-28cbcb75aa5c | -4.71054 | -38.45023 | 2024-12-19 03:42:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e667bf85-c930-3ef5-92ea-f177948b8084 | -1.75341 | -45.82122 | 2024-12-19 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30b0dbd2-df7a-35e0-808e-9e5f3214758d | -1.75881 | -45.81918 | 2024-12-19 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb318ca6-a816-3cd8-8d92-5f3889e876d7 | -4.12486 | -43.56681 | 2024-12-19 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48debcad-5233-32c7-b132-1966eaa933b5 | -3.22091 | -42.08101 | 2024-12-19 03:42:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c752700e-adc3-3990-965a-5648028d6e80 | -5.22806 | -36.80914 | 2024-12-19 03:42:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 596dbc13-beb2-3454-8568-a25593bf026f | -1.758 | -45.82402 | 2024-12-19 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17477a2c-47a0-36d6-8fa5-54675a46292e | -3.78107 | -44.06739 | 2024-12-19 03:42:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e0f9b2a-f1a4-36ee-9cc3-4f0b5d13168b | -3.39981 | -41.64051 | 2024-12-19 03:42:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f87a6d2b-c6b6-3e2e-8158-28a5f73bbb05 | -1.75882 | -45.82719 | 2024-12-19 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d5336fa-3002-3399-afcd-fd819cea61c0 | -3.0165 | -44.39614 | 2024-12-19 03:42:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f05a250-3c40-3a26-b8ed-7562da982b99 | -1.75718 | -45.82888 | 2024-12-19 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c87785e-d7e0-3fef-934c-7b2d342c6b57 | -3.78165 | -44.06398 | 2024-12-19 03:42:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1136ccb7-ce2e-38b1-9f2e-92a02e99f03d | -3.94679 | -41.48944 | 2024-12-19 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a2446c0-cf6c-3aa3-90f3-9c422f5f03b6 | -4.47947 | -39.3422 | 2024-12-19 03:42:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bfb0d09-19ce-3623-9f22-dddbf5adcc87 | -3.85086 | -40.4514 | 2024-12-19 03:42:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a6f41298-368e-3fe9-8c9d-987c09a8f684 | -1.60969 | -45.85187 | 2024-12-19 03:42:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3e3c21d-31df-3134-8b75-2539231a75a7 | -4.39793 | -41.43641 | 2024-12-19 03:42:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 975a59fe-fb5c-36b3-a9ec-8e5e18b76bb6 | -3.74065 | -43.12581 | 2024-12-19 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bba81cfa-5ae2-37aa-b789-12dd5edeefe5 | -3.22262 | -42.07816 | 2024-12-19 03:42:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6a0dd73-3547-38d6-bc2f-ec99092d42e9 | -3.7457 | -43.12661 | 2024-12-19 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69c1a143-bf0e-32d9-93ac-4323b5d6cc66 | -4.12019 | -43.563 | 2024-12-19 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457d8908-827a-3138-aa56-d3cfd3ef8ab7 | -11.79936 | -37.9761 | 2024-12-19 03:44:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0fd5e696-6230-36c1-bc68-a07a63c34643 | -5.86654 | -39.17015 | 2024-12-19 03:44:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 01e6d09a-12f5-3bdc-98eb-6b04c3ffca52 | -6.26251 | -46.19833 | 2024-12-19 03:44:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48b9ca02-6c03-3096-95aa-6fad1aa065ad | -3.98985 | -46.37688 | 2024-12-19 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c005fa7a-c251-37ea-99cf-8a3571940bba | -7.57412 | -37.60094 | 2024-12-19 03:44:00 | NOAA-21 | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1eacc44e-266a-365a-9344-ba7419fde1e3 | -7.58778 | -38.32003 | 2024-12-19 03:44:00 | NOAA-21 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9f9c679e-81fd-3c7b-8d8d-949b6658979e | -8.3902 | -37.76893 | 2024-12-19 03:44:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64a88fac-6f3f-3cdd-b5a9-2faff1bc7aaf | -4.88657 | -41.40291 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fda144d0-e4ba-33de-913f-a5ac25fa4a42 | -6.79081 | -39.41105 | 2024-12-19 03:44:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4d848d9a-4191-3914-87cb-52081b4552d5 | -7.41115 | -35.23589 | 2024-12-19 03:44:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20e69e2d-bcc3-3148-b737-cd2535c091ad | -7.68859 | -35.26539 | 2024-12-19 03:44:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 97f26266-053f-37a7-8db9-77703ffa806d | -4.32653 | -48.29785 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f749a3c-7eae-3a88-aeb5-f349b5b8101a | -7.90694 | -35.23888 | 2024-12-19 03:44:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a686a43d-a5dc-38e8-a5b8-7cb3ad8cbebc | -4.33216 | -48.30621 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c51e80e-85a6-31cd-b045-1788a7a29d88 | -10.18119 | -36.18512 | 2024-12-19 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7f68fb92-c0d3-3c7f-9f37-4388845c7d20 | -6.21347 | -39.40213 | 2024-12-19 03:44:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7723b376-4b9b-3dd3-b658-d828134c447a | -3.99549 | -46.37278 | 2024-12-19 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dac2acce-85e4-3238-b7e4-d9f2f65b8b2a | -9.38444 | -35.95044 | 2024-12-19 03:44:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9bb4abaa-ab88-3bca-8647-c8de78bd6dcb | -7.37694 | -34.88496 | 2024-12-19 03:44:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d361cbf-8177-361f-8fbd-1586e7dfb9a8 | -4.79302 | -46.39747 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e767d89-2dae-3753-a735-4e5f801a3be7 | -4.32585 | -48.30498 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e46b521-f8b5-3d61-b1fe-29b8179d4c72 | -8.07349 | -34.97548 | 2024-12-19 03:44:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07a0db48-94bc-33a1-9162-535a1fe8fe82 | -5.95266 | -39.66533 | 2024-12-19 03:44:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 57013ec5-6be4-3e85-a92c-0d4b0866b4cb | -4.78132 | -46.39451 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e71e96aa-2d68-3920-9c77-6aa2bf39a76d | -4.78698 | -46.39585 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe54a4f4-58b4-38e3-9ca4-112e3636d058 | -9.58291 | -40.42477 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dffd03b7-c609-37d2-8710-eb301fdebbe6 | -5.9761 | -35.62517 | 2024-12-19 03:44:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d5be98f8-1129-3173-9ac7-3c49e6270fca | -6.49423 | -41.60265 | 2024-12-19 03:44:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cb5fb5a-08ed-3bed-8dd3-29d7ceafce6b | -11.88162 | -40.95513 | 2024-12-19 03:44:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0f48200-b723-3558-9af1-a5add953dd0a | -5.96449 | -38.26035 | 2024-12-19 03:44:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d1c44a9-9020-3fad-92d5-06d68047ebeb | -4.48031 | -45.42398 | 2024-12-19 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 775b9199-8bd7-32ac-a247-7a11b5d0affd | -4.80226 | -44.02897 | 2024-12-19 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a58a1c0b-a2f5-36fc-9143-ac363ba234c6 | -6.40974 | -39.94787 | 2024-12-19 03:44:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e6e47335-c985-3e74-b858-7f7dc5b27a02 | -4.88733 | -41.3984 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d00e4992-f41c-3db1-b65e-5b35be0b7725 | -4.77993 | -46.39989 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18f9a00e-19b4-3e71-b51e-f5738a4f1f52 | -4.99252 | -44.21134 | 2024-12-19 03:44:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c07d2e1a-4bff-3356-b394-4154e8752fca | -4.89094 | -41.40378 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 39c16f5e-2f4f-3d4e-bb08-de2a5d2d48b3 | -4.33403 | -48.29898 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1c00199-6ff7-354e-9065-09ee6fdda73d | -6.68134 | -41.03727 | 2024-12-19 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6255a0ae-4a14-38da-9311-0e2b42189da9 | -7.47532 | -34.84269 | 2024-12-19 03:44:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04c5b303-027e-3dcb-9443-1c398ec0c5e4 | -7.58427 | -38.31945 | 2024-12-19 03:44:00 | NOAA-21 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f1556ed-3c85-3330-94c6-765d56c01d54 | -6.31357 | -38.92959 | 2024-12-19 03:44:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48fa564c-e1c8-388e-a62c-112c30d20f2e | -6.24086 | -35.17228 | 2024-12-19 03:44:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44facffe-3026-3c37-a904-14061db09108 | -7.56412 | -35.2348 | 2024-12-19 03:44:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa1b9c7e-dbee-3130-add3-d9d9db27239d | -7.71338 | -35.084 | 2024-12-19 03:44:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62b0e059-5e8a-388b-8027-2bea1de5ded7 | -4.78611 | -46.40075 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db7421ad-5bf3-3ba1-a9fa-e780f10cb915 | -12.13384 | -39.7674 | 2024-12-19 03:44:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26c15d61-935e-3428-b52e-74fe5769325a | -5.17594 | -37.59426 | 2024-12-19 03:44:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 35e54fec-8cd6-3a5e-85e5-c65bffaa38f1 | -4.88292 | -41.39775 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e8e271bf-88f6-3bf7-9d22-2a488c9aac77 | -4.8858 | -41.40749 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b218d7d7-cb2c-3863-b893-8dba1dff99d7 | -5.17656 | -37.59038 | 2024-12-19 03:44:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 47f7cc72-a808-3674-a1e2-c509af88ffa6 | -4.33279 | -48.30613 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12eb51ba-0ae2-3365-94da-710af65061a1 | -6.26331 | -46.19386 | 2024-12-19 03:44:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a96db5-3062-35a3-89d9-f5d103fcbff9 | -6.20968 | -39.40152 | 2024-12-19 03:44:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2621db2e-80f7-3b24-9400-bded2c4bfe79 | -7.09595 | -39.03371 | 2024-12-19 03:44:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 179a9340-a6a6-33d6-bfe2-91cdeec0ad18 | -7.78119 | -37.97387 | 2024-12-19 03:44:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b345063b-399d-316e-8e98-c409afe771bc | -6.68551 | -41.03796 | 2024-12-19 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 939599a0-3146-32c6-9ff1-a0aa08bf7673 | -7.84404 | -38.417 | 2024-12-19 03:44:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f604b34c-89f0-38bd-9895-863f76b043f7 | -9.58478 | -40.42273 | 2024-12-19 03:44:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 76170dc8-b15c-3e4f-976d-a464fc802b4c | -4.53337 | -44.0529 | 2024-12-19 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 958aba22-ccd2-3588-a1a4-0e62f84d2e79 | -4.8028 | -44.02579 | 2024-12-19 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1cd36c16-5155-37f0-b145-8e46db31c4b4 | -4.78046 | -46.39958 | 2024-12-19 03:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68b7879d-cd6e-37fa-acee-6db853478087 | -4.32709 | -48.29778 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e59080d-65b9-30b2-9456-e382ae816335 | -4.35256 | -48.47327 | 2024-12-19 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83c516b1-54fa-319c-9b62-5d37256a5596 | -7.64498 | -37.57431 | 2024-12-19 03:44:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d7b92d5-7ead-311a-b414-840c44976a18 | -3.99067 | -46.37208 | 2024-12-19 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61442d03-5ea1-3453-8a49-f1b878f24bf9 | -5.34018 | -37.44989 | 2024-12-19 03:44:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c795c84-0e5b-36cd-8fbe-b3fba6315720 | -3.99461 | -46.37772 | 2024-12-19 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d9149a-c2d6-3e45-a0df-ab841e408188 | -4.67371 | -43.29848 | 2024-12-19 03:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README6.md)
