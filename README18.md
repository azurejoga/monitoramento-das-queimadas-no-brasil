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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01b0a902-c13a-30d0-804d-edde01b3cdc5 | -8.9588 | -47.27304 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53373427-5c85-3c33-981e-1cb6b593f86d | -10.62741 | -45.23853 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6c4cd3d-62cc-3635-93f5-7a146ce1f212 | -8.73902 | -47.15914 | 2025-07-10 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2bf099b-3550-382c-8548-51a5080194a8 | -8.50442 | -43.30008 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| e2284064-f432-3040-a74d-0e61716f9b38 | -11.06751 | -45.87085 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90c3bf66-960b-3fe2-983e-6a70ca9516e7 | -10.96495 | -49.25119 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8196d29e-4975-3ddc-ac7a-47c20c442451 | -8.99547 | -47.45007 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 913b438f-f82e-3ddc-abd7-0e7ae956dba8 | -8.51051 | -43.30998 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 4e8d97e9-ef5a-3989-9877-f689502de373 | -5.76349 | -45.79711 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 710c54b8-751a-3723-96b5-a88b53697eaf | -9.0054 | -47.45167 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab1e667f-4548-385c-9b01-b586870a86a0 | -7.00045 | -43.51559 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56bf8297-2e39-3ac6-ad22-6063b56cb56b | -11.06018 | -45.8735 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76c1ab65-94f8-32a7-a506-5b5a6f281760 | -6.67607 | -46.30201 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5eccec56-48b5-30f1-96b4-378283d61329 | -10.65361 | -49.45951 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e65d18c-0925-32f9-84ba-3b71327673a2 | -6.99515 | -43.50214 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c4b487e-3220-3596-b8b7-bf774cbeff36 | -11.3661 | -48.71007 | 2025-07-10 04:25:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e7635c-0043-3902-92ae-ded726a5f83e | -8.46911 | -49.60414 | 2025-07-10 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f33f23-b138-349b-b3f7-662e811f5de6 | -6.85714 | -42.79892 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| fb020e51-7f56-3e23-843f-4308abefa3d4 | -8.49659 | -43.28318 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 851e5af0-3f27-3264-974a-f6633808f180 | -6.99281 | -43.4933 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7348f86-b061-3a3d-93d4-bac862db3885 | -7.23387 | -43.08289 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c347021-02f1-33a7-8a38-9e0f2a37106d | -8.49895 | -43.29253 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| cca03eec-7dab-30ee-8eeb-608d4c64fb19 | -8.49526 | -43.29198 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3550398d-27f1-304d-9963-a5c89a3fdc94 | -10.65643 | -49.46388 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 953bc52c-8561-3e3e-86d2-880a71451696 | -6.95402 | -42.71982 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba175bc7-ac6f-3f46-97ea-248a602df835 | -11.44639 | -45.0983 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c2851f3-fa5f-3443-bdcc-3b2218d4b70d | -8.49792 | -43.27433 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a81577d9-93f3-3855-9b45-882ae5a7cbc8 | -10.5712 | -49.12595 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0632d63c-d60c-35fd-afdd-a4ff674796e8 | -7.80999 | -46.56702 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e00bd42d-f58a-39a7-bdbb-055a1219097e | -10.632 | -45.2314 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee840ce1-b40a-337e-8eb8-eebe3f36c5d4 | -8.96795 | -49.85595 | 2025-07-10 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57708148-6789-3056-ab56-107347187e56 | -10.6611 | -49.45685 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 29434b80-8395-37d6-a74c-b936a8fde083 | -7.70647 | -45.77192 | 2025-07-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdd0af3e-dc93-3314-b74a-8f8b4eade559 | -6.67553 | -46.30547 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c307143a-1f63-36fb-9bf1-3a71f53222d4 | -8.50131 | -43.30186 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| a7989176-6e43-3112-b266-ff4b9aab44ab | -6.85102 | -42.78884 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 24311060-7d13-34c7-bb16-38e08cd26112 | -10.98605 | -44.32932 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e1c0646-7d91-32e9-9e84-90f24a625aee | -6.8602 | -42.80394 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 35195108-3338-3a43-880e-8ceeb532cd1a | -8.49726 | -43.27876 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 59e04f40-4e97-312d-ab5e-d1dbb6bb0ee4 | -8.50329 | -43.2819 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 82d1cc5a-ab33-3fe7-a959-cd0e01a277c0 | -7.01497 | -43.49234 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 218d43d8-7163-36e6-8c74-82bd1e5f9753 | -7.70314 | -45.77139 | 2025-07-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b001eb5-f7d7-31d1-85a8-b5966a8d47f0 | -5.233 | -45.21498 | 2025-07-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb6fd944-7d87-3d90-9f62-471e494791f0 | -5.65563 | -46.58966 | 2025-07-10 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eeb8c61-195d-3166-afb8-8224dd8670d1 | -7.02575 | -43.49392 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a959686-1fb0-372d-b76c-f6899555bf0d | -7.23112 | -43.07222 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2453c972-d49f-3c85-9ec7-5d77cc2e8a43 | -8.73957 | -47.15567 | 2025-07-10 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 758d4a6f-5543-33cb-858f-6439b7816b9c | -8.28097 | -46.31401 | 2025-07-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34fba47a-1829-3567-8fe1-fdd6acd597b1 | -8.86143 | -47.95079 | 2025-07-10 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87f34ba1-3bb7-3372-8b27-0b4e5a5e3943 | -5.62012 | -44.00722 | 2025-07-10 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef734666-b767-388a-b1bc-dd98a0b3cddd | -5.02883 | -47.96856 | 2025-07-10 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 134a9697-ec55-3dd6-a898-9d1fff6e3710 | -5.76019 | -45.79659 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5b0cbd5b-5e41-3575-9eb8-3b28f878e5b2 | -5.96364 | -44.16606 | 2025-07-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f7f6581-c560-31e1-857e-a35e66d89d21 | -8.49357 | -43.2782 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 1a0d5405-3a20-3b87-924e-a9f317ab7ddc | -8.96152 | -49.85071 | 2025-07-10 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4eb2f3e-10e9-3153-b5d1-b0e403e956ff | -5.78196 | -43.611 | 2025-07-10 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 416ef513-d290-33ff-99a9-2cef02e586bc | -7.0471 | -43.27977 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 472c711e-a93b-3268-94b4-879cd93cbb40 | -10.6633 | -49.46503 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6fbc36f1-6606-3785-ad65-aa7bb46c7470 | -11.46325 | -45.10487 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07e4b6d3-fdcb-3481-8e86-e7d87fedef13 | -7.23086 | -43.078 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6ebba8eb-b13c-379b-a023-091dabacf102 | -10.57096 | -49.14874 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2b3afe04-dc86-320b-ac8a-142e89d5d11c | -8.50506 | -43.29568 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 417ac906-2b32-36e8-a5ad-787132f67077 | -8.50201 | -43.29072 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a5e2cdba-b6ca-3667-88f0-f3386d3d179f | -9.21538 | -48.59682 | 2025-07-10 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a5bd3c70-f8a6-34e2-8e71-7838b18905cc | -10.445 | -47.9507 | 2025-07-10 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb05a030-d6c5-3d9f-9bb2-4189a7e8d594 | -6.5498 | -43.62717 | 2025-07-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bca47ef-2b16-3bba-bd91-448fa8bcbddc | -8.49592 | -43.28758 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d4a08671-6984-3861-aa36-8b245a6d2af4 | -7.03293 | -43.49496 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c5aa220-cef4-3390-9435-b4c411ecb9ed | -6.91627 | -42.83525 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bed8da4-136d-3e72-8f1f-159143abf3cc | -7.08755 | -49.16341 | 2025-07-10 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a002380a-c762-3627-829c-0b3f4cf105df | -4.82014 | -44.35518 | 2025-07-10 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda0f36a-3096-32c9-95bc-ad9ca3bbe41f | -6.86086 | -42.79944 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 38e5d0d8-3174-32be-b2cb-1ad1fcf6a504 | -10.63545 | -45.23192 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc718337-e922-3b28-bc36-05092ccf4fc1 | -4.81618 | -47.31927 | 2025-07-10 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cf35319-82bd-3fa8-bed7-fef1a3b0d7e1 | -10.96155 | -49.2506 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb803f69-fdd4-3c8b-ab46-d3982f85f2ec | -6.64847 | -43.19567 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4fba1c0-8d03-33da-baab-ef5a1c60084e | -8.50378 | -43.30447 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| a5802aca-4b0c-3043-9a9b-53366249045c | -6.99764 | -43.48553 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ad5a8710-e86e-380c-8337-d19baabe661f | -10.66267 | -49.46883 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 94569a0e-6c91-3d49-ac17-cc632c48bcda | -10.57521 | -49.12277 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5323631-76db-3ff2-97e5-0b816fcab2b6 | -7.72824 | -46.61047 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a1db4f1-be5a-3ff7-ae4f-074daa7766e1 | -6.95323 | -42.71723 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c997acf-3e1f-3457-b7a0-c710b6295d1f | -5.41455 | -46.07116 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb9b3574-a3b8-32ee-813b-a390e1b976e8 | -8.50393 | -43.27747 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| b13a3e9f-b462-31ce-8e9b-abdb66616c3f | -5.57535 | -46.53771 | 2025-07-10 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76f742b5-7e53-3af2-a4ba-08abd75a6baf | -5.41533 | -47.56786 | 2025-07-10 04:25:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9540ff0a-5033-3b9f-a904-04522aa4a25b | -8.50923 | -43.31877 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| c124c960-0043-3c77-a5e4-64e45d4711f6 | -11.36393 | -48.70231 | 2025-07-10 04:25:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53be0c6a-0d78-3b64-a1a4-2085ed29efa7 | -8.50095 | -43.27931 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 109efa34-28d1-3a37-8594-676f96e4a22e | -6.95254 | -42.72175 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aced3909-b0ca-3345-abbd-f1999374278e | -7.64403 | -45.34801 | 2025-07-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4170223-a54c-34c0-a12d-d5a06b60b295 | -6.99625 | -43.51918 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c0d0d6a-d76b-3050-8c5e-6eef66da3420 | -7.22784 | -43.07312 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 468873a8-4764-3c4c-9129-5fca074f66f2 | -6.99156 | -43.5016 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19260a92-1f51-32cf-9510-8366e06548ea | -7.95434 | -49.64661 | 2025-07-10 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a9ff05e-aaed-30e7-8914-b83a38a74ac1 | -5.23245 | -45.21848 | 2025-07-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b82c7061-ef2a-3cf1-b52c-7505df3529f6 | -8.49718 | -43.27192 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4fc4c15d-6f46-3c43-85d9-fd1418196b64 | -6.5504 | -43.62326 | 2025-07-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7d5c4ed-fe73-3523-875e-eacab7448df5 | -10.99117 | -49.54155 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a5ae347-9278-32a8-97b3-7c63972cccc3 | -7.22985 | -43.08089 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README19.md)
