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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ab55571-2bf0-3690-a635-ffcef8b8e5ad | -5.56403 | -42.14942 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f79b3aa6-8ea0-325a-ba5a-529deb093ea7 | -2.89887 | -51.47245 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc460d69-8f87-3da7-9cb5-dab072dbc2da | -3.30892 | -48.71453 | 2025-09-21 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06cbc9ee-34fc-39e4-b549-a2d4118e4c3b | -5.26163 | -48.9092 | 2025-09-21 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f88195d-2f8c-37fe-917f-dd1cca792c60 | -3.65326 | -58.16064 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3353dc1-9c38-358c-82a8-cf8f4f2d0bdf | -3.76207 | -54.81534 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ab558e0-b1ed-3030-9714-590280a808b9 | -7.91976 | -44.10184 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16f14ec1-7dbe-32ee-bd39-9b506aaf89b1 | -5.56656 | -51.79393 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 088f4301-72f5-3d99-a23f-819d1ce7ed12 | -0.90963 | -47.54615 | 2025-09-21 04:55:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3247a75-8bc7-3ea4-8182-f178ca466047 | -3.8051 | -47.57525 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75b7c2e2-5dde-375f-b747-2e11bdc3c868 | -5.35867 | -49.20146 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| eeb3319c-d86f-3318-9102-83531f419089 | -3.20587 | -51.59397 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f13706d-8088-32bf-aa66-3e7a21359490 | -5.27528 | -44.81762 | 2025-09-21 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65236e33-db4c-3ecc-8382-8f02ed2da1b6 | -3.5906 | -43.9129 | 2025-09-21 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83971f45-a500-37b3-8892-7327081d9776 | -7.71902 | -44.45616 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa89862-1f45-308c-808c-8fb36c0cf044 | -4.36961 | -56.02939 | 2025-09-21 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f1666bd-626d-372a-9714-c2a3532531d3 | -4.47924 | -55.08854 | 2025-09-21 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abc0ade4-c090-33b9-bc1f-672305da6ffa | -7.7231 | -44.46857 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6f88463-c529-3dc3-ab19-f9e99081e257 | -3.65302 | -58.16411 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 66d90b14-edd9-355c-887e-5a53496a1c98 | -5.6309 | -45.95376 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d9c974a-e9b1-3d1f-b79e-6de3d968214c | -3.35238 | -48.3869 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab536431-634b-3fec-8e07-d738f4f5ecb7 | -2.69157 | -59.42662 | 2025-09-21 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7765ab7d-b1b5-3637-89e6-8615d1494e6a | -5.14518 | -45.70935 | 2025-09-21 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfe24fdb-12c9-3174-9ee1-4e3880110581 | -3.76149 | -54.81892 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4d338bd-17b2-326f-9e13-0419492a7f22 | -2.74401 | -49.54799 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 896c9a6c-469c-360b-8906-b57096ed7280 | -7.72414 | -44.46083 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95b2efe6-d248-35c1-a943-0c990277196d | -4.29737 | -48.27023 | 2025-09-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33f641d2-216d-37a5-b28d-f780356d8a99 | -4.19657 | -48.55252 | 2025-09-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77260d8c-cb5f-3c26-b7e1-4f6ce2765b39 | -2.93469 | -54.08106 | 2025-09-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3846b541-2e0d-3c3d-bf8d-96bb37f87629 | -7.92613 | -44.09843 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f30f22a5-1247-3504-9bc4-2527839c3c63 | -1.7944 | -48.07222 | 2025-09-21 04:55:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59fdd6af-3510-3c15-9972-a057d60eb224 | -3.3474 | -48.39 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 687177cd-c897-3d89-af63-fcc5b7514e1a | -3.8395 | -55.59903 | 2025-09-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fb67a31-acfc-3480-af2b-367b65c853c8 | -7.9192 | -44.106 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08a927e5-1d6a-3aa8-a7fc-3324fcfe5e72 | -7.61989 | -44.44206 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 804e7878-fe23-38a4-a6d9-1b5e3ca2c0f8 | -3.45157 | -52.56993 | 2025-09-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd056de1-e5bf-304c-a365-6fd3a145498f | -3.51788 | -47.20621 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6520777-f0e8-37a2-9c17-8697a10d1d46 | -5.52964 | -43.8749 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ba18f85-5761-3b09-8dee-ff852e731d64 | -5.55696 | -42.15353 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5c8ef105-a01c-3870-bcd2-d74bf1fda186 | -5.79908 | -50.20253 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99724ca8-8c0c-36fb-9e31-23f50e630b8f | -7.38879 | -47.04113 | 2025-09-21 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aa82d37-e0ca-30ed-a8ea-ca372125bb4e | -5.69745 | -51.76276 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d33df746-c503-3450-a9b1-15da18bd42c8 | -6.30561 | -42.362 | 2025-09-21 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2864252a-e0e6-38bf-a83d-8c728cc191f7 | -3.75946 | -54.81841 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5f7b5b81-57d0-36a9-8231-0af6d172f35e | -7.72362 | -44.46469 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45c59b22-cf72-3672-8d1d-63409d1dc1e3 | -4.00646 | -54.32832 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0675d58-7546-347a-afcf-2ae600f1d81d | -2.30277 | -48.14876 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c4d10c4-c41f-32e9-bd26-100139fb5e37 | -3.6485 | -58.16502 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f61894b-33b6-3f4a-a05c-9724c19a3c89 | -5.57113 | -42.14512 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 979c4fdc-01a2-3682-a158-01e951dfbb4c | -3.76058 | -54.81125 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 20cecd4b-50b3-33d2-bb7c-dfb20bebd917 | -6.53416 | -49.5115 | 2025-09-21 04:55:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a30f9664-29fb-3660-82dc-969fb31c4de1 | -3.45824 | -51.07765 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 394a1042-db64-3860-8941-d1f018e941f4 | -7.09235 | -47.34815 | 2025-09-21 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dd222cc-2d6b-3864-865a-e55656fca8e6 | -2.30649 | -48.14947 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c2c9b19-32a0-3503-9da1-af1fc08e6228 | -7.23324 | -46.62274 | 2025-09-21 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a540c5f-e5e3-34e9-895d-806fe0ddcabe | -7.23254 | -46.62765 | 2025-09-21 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c98f965-28d0-3671-aef0-80ee8f7549a6 | -2.62074 | -46.8395 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2f7c9da-8fe4-3bed-ae01-84562422b280 | -3.60509 | -47.528 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b09b3af-812b-3ab6-940e-a372d7c0cfa7 | -6.17119 | -43.68893 | 2025-09-21 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc229b28-b1e9-380d-8d04-f743db6f67f9 | -6.17107 | -43.68749 | 2025-09-21 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd577e13-7f8f-3495-b615-ab0425bfbea3 | -2.73668 | -49.55401 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fa3b947-27aa-328a-8a49-ee2a8d6aa8e2 | -3.35089 | -48.39417 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c721228-4d18-3b7f-87f1-20a48f2426b7 | -2.16203 | -52.10738 | 2025-09-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bc171b2-ef53-39ca-92c7-47653ed83d9f | -3.72314 | -51.33144 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bcf75fd-4e98-3111-97a7-2e250cb01044 | -3.76264 | -54.81176 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bc495be-581f-3e36-9757-f98176d50ebf | -5.63503 | -45.96003 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ff4bf7c8-e894-3cc9-a6f7-ba8e3d5da40c | -2.73887 | -49.55635 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a0e8c1f-4a35-3a17-9c45-de495df7712b | -7.91807 | -44.11427 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edfc47b1-46ee-3dc6-941b-323132d51588 | -2.61802 | -46.85683 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bba088d-15fd-3a24-bab9-097fb050e7ce | -5.64847 | -51.4683 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cd56362-fbd7-3556-b1af-9d373e42b50d | -5.55928 | -42.153 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 25cc2680-6d04-3257-9001-a2d58b7d074b | -2.61724 | -46.85544 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6bfe0ac-8d00-3464-8a7d-41673a921dd4 | -6.392 | -50.90818 | 2025-09-21 04:55:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc112cce-54ff-3fdb-a6b5-b89fab4b5181 | -6.94727 | -44.76129 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9126bc5e-09ff-3fd2-ab54-2fb4f2ad863b | -4.41357 | -55.10034 | 2025-09-21 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d529129-dd1b-34a5-bfc1-3820c26da308 | -3.98311 | -51.05558 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0abea2cb-f9e9-3107-abb3-f4d5e8a0ecef | -1.79386 | -48.07574 | 2025-09-21 04:55:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eed8bb08-6337-3337-a3e6-4cba143eb18e | -2.30242 | -48.39534 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c3f4840-2ca8-3c5a-acd6-32e200c2198b | -5.33927 | -44.90164 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53c22ed6-5e11-3d9f-9f4e-a70de7f17700 | -2.73735 | -49.54953 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1e4fe54-6e94-31f0-8134-ee442588b0ba | -5.56563 | -42.15392 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 239cf9d9-3604-372e-9ede-8ad5f89ab654 | -4.70851 | -46.47013 | 2025-09-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de15e2b8-b961-3c83-b00a-f6f6ccb095bc | -4.80123 | -47.28449 | 2025-09-21 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bc6c4cd-3e44-3661-8700-c09d3c804f3e | -2.6037 | -48.13897 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1385e3e-7645-31f6-abe6-77ed37498166 | -1.12127 | -54.14456 | 2025-09-21 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72739189-90e9-3b2d-9ecf-8d3df00bceae | -4.94278 | -49.92603 | 2025-09-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d6870b6-c689-3fda-8253-813675564528 | -3.75693 | -53.34859 | 2025-09-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 308558eb-0b11-347b-b381-ffadb18d5e8a | -3.68997 | -55.95614 | 2025-09-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a19edead-95ca-3157-81db-c76459b7b08d | -3.81172 | -51.61709 | 2025-09-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c1af526-8617-3d60-8e4a-db4fa5769b42 | -5.6911 | -51.7579 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fff76387-3256-31eb-8ac5-304f1c00afb9 | -2.60427 | -48.1353 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c19280e-a321-3e4b-a1a8-896ee34c5566 | -5.52807 | -43.8716 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d2e0f92f-fc37-3b5d-b550-6adda72eb43d | -6.39136 | -50.91241 | 2025-09-21 04:55:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 252be95e-c14d-3459-8712-562cee02db91 | -5.69803 | -51.75897 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8426b095-56d7-3ea5-9d40-a5374501f5c0 | -3.98602 | -51.06002 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80b7a33d-1d06-3667-9218-876833f2bcc5 | -5.52298 | -43.86663 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 167d0d22-0322-30f9-8133-43854a6a33eb | -2.26136 | -47.8458 | 2025-09-21 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 555bf213-ea58-36d5-85db-bb229eff8180 | -5.01152 | -45.20983 | 2025-09-21 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 098b94dd-da3d-324b-a5f5-0c0e23d5f433 | -5.33971 | -44.89856 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16479732-75da-37d2-ab9f-b76fe806dbcd | -5.01077 | -45.20196 | 2025-09-21 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
