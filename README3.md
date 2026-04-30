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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1063d3c8-f854-3748-ae90-d1b9c4e2bfce | -18.00205 | -53.00908 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c09027a-ee86-3b23-95c6-bfd798280f96 | -18.09018 | -52.99592 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a70930c9-8c26-3d49-928a-2f2c81265425 | -18.02018 | -53.01314 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 624ba6ac-558f-33b7-8c12-f22bb47de825 | -11.60704 | -47.10275 | 2026-04-30 04:19:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f224930e-552d-371b-a7fc-8691791412b4 | -10.96672 | -45.09771 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6f616e03-4cbf-3457-8a5a-f1b24ac59b76 | -18.06023 | -53.00163 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| e945cdd7-cbf2-314f-8429-d68a8053f941 | -18.0457 | -53.00352 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 49548748-ff2c-359d-bad4-f39708bdbf15 | -18.08474 | -52.99693 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fc348ecf-5a67-382c-9113-f58f2d96ca45 | -16.63686 | -49.35297 | 2026-04-30 04:19:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4b2e3cf-1547-3e19-936d-6d97a48d1056 | -20.67583 | -48.95646 | 2026-04-30 04:19:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2f36a5d-1613-3035-8282-fde3912a6a41 | -18.96466 | -49.02192 | 2026-04-30 04:19:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fc083e0-1198-3bf0-b95f-ed76efa0ec60 | -19.78299 | -45.39129 | 2026-04-30 04:19:00 | NOAA-20 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be86ad52-d007-3ae7-8470-a9f8ffb2fa1d | -18.06477 | -53.00261 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 10e8737a-44cd-3d58-8627-8e73a9d2e7a5 | -18.14838 | -52.08898 | 2026-04-30 04:19:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe7f5fc0-b017-3082-b78d-f7973d99c562 | -12.00045 | -38.66828 | 2026-04-30 04:19:00 | NOAA-20 | OURIÇANGAS | BAHIA | Brasil | 2923308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 82bdfb87-8130-35f8-9fdc-e121572799aa | -11.94861 | -43.3758 | 2026-04-30 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6fa06b5-336c-320e-ae9f-498feee98625 | -21.18268 | -48.63648 | 2026-04-30 04:19:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be429a64-2d4a-3001-b01b-b4c915234f44 | -17.97971 | -53.00218 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f07d13c-af9a-32c8-b70a-d624a73894f9 | -11.40557 | -48.42926 | 2026-04-30 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8fb1f6a-c920-3528-96dc-cb5c3982c258 | -18.02471 | -53.01415 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d88eaf5-3d64-36ca-b420-520737adf961 | -10.99216 | -45.08374 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7960aa5e-50cb-3155-b78d-e54e29061ac6 | -18.08926 | -52.99793 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 96aa37f7-d412-3927-b086-657cc80ef407 | -11.9514 | -43.37987 | 2026-04-30 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ea4f7c4-84c3-3214-b311-eb3d3ea0f19e | -21.17926 | -48.6358 | 2026-04-30 04:19:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 535bdaa0-4c24-3167-b1e8-4ed3110fd0fa | -10.99274 | -45.08018 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e7a43871-b8d4-3697-ac49-9cd61301202b | -11.9311 | -46.74945 | 2026-04-30 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8b58567-6684-351e-b52b-8d935d6c92a4 | -18.0557 | -53.00066 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 13e1d788-7d57-300d-96d0-fbdf4b340891 | -18.06117 | -52.99681 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 36063390-3dc5-302f-8835-b3d1f20327aa | -10.99608 | -45.08073 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c0ecde68-6f9a-3380-aab4-698947cf0472 | -11.0006 | -45.0847 | 2026-04-30 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| b872edf3-4e8d-3c6b-8fc1-0b5ccd08b043 | -32.10574 | -52.33183 | 2026-04-30 04:23:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 911bc206-e623-3ea7-8485-95708d883093 | -32.30568 | -52.43515 | 2026-04-30 04:23:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 048bfdae-6572-3015-9217-64424c81e0d2 | -11.0006 | -45.0847 | 2026-04-30 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3b8150fb-3375-3805-a31d-f2e492b73780 | -10.98667 | -45.08776 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30767062-bb1d-3a56-9326-efb429c45a22 | -10.97056 | -45.10272 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90a0e4b4-adb0-3311-b114-da821504cc2b | -10.96491 | -45.09679 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56f767d7-5a79-3137-857a-248e3d9dd677 | -10.99765 | -45.08702 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dee125c5-ce18-3e05-b712-4dcfaab0a057 | -12.05483 | -57.41916 | 2026-04-30 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58efb4ad-f054-3a32-8112-c33730782444 | -10.96629 | -45.09941 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 48eb3612-f55e-3b4d-b7a6-c293db045900 | -11.37951 | -55.17827 | 2026-04-30 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74a9cf5a-479c-30f7-b6ae-b9e89b378672 | -10.992 | -45.08105 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 934ca48e-0538-3499-8c03-47e0800622fe | -10.58883 | -44.33216 | 2026-04-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdb6cd4c-f073-3cf4-884c-6ad63c30a8d3 | -11.7954 | -57.013 | 2026-04-30 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29b8caab-a74a-352b-84e6-4390771589f6 | -11.93864 | -58.08635 | 2026-04-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070636ff-97c0-33b8-847f-e751e32c4c4f | -11.5565 | -48.26184 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eec14f31-6975-379c-80b1-4a599d6e694d | -10.97111 | -45.09791 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44473f24-6de8-3c28-9ccb-1be527f492ff | -10.59532 | -44.33303 | 2026-04-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f9147c0-d130-302b-aa97-c32bc9457f01 | -10.99288 | -45.0887 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d338d8e5-b221-38ff-a2cc-a667e9c33947 | -11.37612 | -55.17773 | 2026-04-30 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ce22327-222a-37f4-95e2-3c0d1cb40a4a | -11.12915 | -45.1397 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5fc8a412-c2c4-3bd4-b19a-009143217316 | -11.94198 | -58.08689 | 2026-04-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0f141b-729a-3b53-8002-796145eaa638 | -10.99259 | -45.07594 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| acbe70f9-a4ac-354d-8e78-fa9fab706b84 | -11.55688 | -48.25875 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21398824-0653-3002-9ccf-d6363cf6f482 | -12.3757 | -50.03197 | 2026-04-30 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 091979f7-7525-36fb-85d4-1efe88d1467f | -11.40975 | -48.42387 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3c6ae29-f321-3a02-b3c0-4284199eb58e | -11.41013 | -48.42089 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3908957d-63f8-38a4-80b9-723081f51f76 | -10.99972 | -45.08453 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c152ddd2-32e6-3ded-b353-c2dda05c7d8d | -11.12974 | -45.13467 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e4eac8b-6925-374a-89ad-fa71e53538ce | -9.46227 | -46.12373 | 2026-04-30 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b611fda3-fa6f-3880-8902-4bc4a64bcf48 | -11.55852 | -48.26104 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9623cfde-5747-3b70-acf1-966809f78063 | -10.99349 | -45.0837 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e46fe8c0-af52-3328-9ad2-e21f0717550f | -9.46801 | -46.12435 | 2026-04-30 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f706a6-7e92-30ee-9d12-43567f28a90d | -9.46976 | -46.12595 | 2026-04-30 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aec83f5-480b-3252-9e23-1eef105116c2 | -10.99823 | -45.08197 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5be1397b-4e5a-3d48-8da6-e9ab353df2be | -12.05428 | -57.42267 | 2026-04-30 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85f461dc-bccb-3db1-8ddd-4d1d92eeccc6 | -11.40936 | -48.42684 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7c60e1-b6e4-3405-9466-11dc4badf6b2 | -12.05815 | -57.41969 | 2026-04-30 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e232d70-2a55-3a47-913c-cb62a5b875b8 | -11.55812 | -48.26412 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c80b1a8b-a59e-3a18-9521-e8a30f3ea99b | -11.5681 | -54.56581 | 2026-04-30 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4173a610-8ef7-33dc-9988-ba02e8ed67ef | -11.40898 | -48.4298 | 2026-04-30 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a09fd1-ee24-36c8-a1dd-67042d21872f | -10.99411 | -45.07866 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d2f1b779-ee2e-3172-b265-cae586220b37 | -9.72128 | -60.20282 | 2026-04-30 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1dd871e-69db-3bd7-a182-041fb96cbe4f | -12.28749 | -57.38866 | 2026-04-30 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701f57d9-42ec-3b91-b370-577f3ba90d05 | -10.99142 | -45.08611 | 2026-04-30 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d762ee15-90c6-3c0a-925a-486dfb04eab2 | -9.46402 | -46.12532 | 2026-04-30 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf44e609-2705-3e60-aac8-72d4d4030c47 | -11.94141 | -58.09049 | 2026-04-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 345575a8-6e5f-3525-981c-1dd364f89177 | -12.05539 | -57.41562 | 2026-04-30 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44bbef8d-64f5-3c43-9266-a2f34552565d | -18.04998 | -53.00526 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3219cdaf-4322-381d-be66-e9aa4b05efc3 | -18.04556 | -53.006 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eec65926-aad0-3705-a4b1-92351f0df64a | -18.03548 | -53.01983 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 404b2586-e310-36cb-ac41-d8613da353ea | -12.6033 | -58.67088 | 2026-04-30 05:08:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9235eeb6-5b28-3b81-ba7f-14cb85df6391 | -18.00395 | -53.00771 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd22d459-8026-301b-aecf-d123e824ecb6 | -18.70552 | -54.98622 | 2026-04-30 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c91e5e6-b02f-37fe-a313-9a89bd68bda6 | -15.37313 | -52.23159 | 2026-04-30 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e1574ff-0404-3cfb-be31-61b1b577e5f1 | -18.08849 | -52.99546 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c30ce1b0-d714-37e7-80c2-2416f61e140f | -18.02736 | -53.01862 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8cc0651-38d5-33b9-a60b-94740f11ef20 | -18.03954 | -53.02043 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8e4629f-6c7e-3251-8cae-4fe4790c39fc | -18.02785 | -53.01486 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7177d6a8-8da9-34f0-bb40-fb5e746c7ff8 | -12.60389 | -58.66719 | 2026-04-30 05:08:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af3a7737-536c-3b14-b5ce-8332c438bab9 | -18.04507 | -53.00976 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 781ceb43-8408-35c2-a73f-62257a6446da | -18.03597 | -53.01608 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79a54cc2-3cc2-3eda-b432-8bb0cd309fda | -14.6992 | -52.95034 | 2026-04-30 05:08:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0d62d5f-f386-3e2f-bca5-084c21aa8646 | -18.0324 | -53.01171 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e841939b-cc70-39f7-a171-908c453bcda6 | -17.25201 | -47.0815 | 2026-04-30 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5470328b-639e-3490-906c-0dab2a7fbe69 | -17.99989 | -53.00713 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f159c7fa-5d5e-325e-a243-a4b1217cae70 | -18.03695 | -53.00855 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15349969-2ed7-3f6a-9ca9-dbeec7221d8a | -15.75774 | -47.7682 | 2026-04-30 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b769a0-89b4-3e63-a697-1069c4e06aff | -18.0415 | -53.00539 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ccc1f34-29c0-3a9a-9390-23f257f11840 | -13.69986 | -55.68633 | 2026-04-30 05:08:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62e5ee4f-95ac-3e62-8719-926ef5b1a550 | -17.25245 | -47.07705 | 2026-04-30 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README4.md)
