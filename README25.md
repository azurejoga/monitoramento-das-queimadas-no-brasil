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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 534d2890-fa14-3959-aa8b-d18226295958 | -10.17444 | -41.99549 | 2025-10-26 04:02:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f16c1cbf-1c70-3830-80c1-211c46e341b9 | -11.33067 | -53.9389 | 2025-10-26 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68d12420-462e-375c-a8c7-4cb730f74150 | -10.40993 | -45.32096 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 20e81926-bf83-3230-b049-5961c27eb950 | -15.45573 | -50.47958 | 2025-10-26 04:02:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ce1901a-4996-30d7-8a0d-325807ebbbb0 | -10.42539 | -44.49397 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9bc1588f-5c40-3d89-a660-1acca92ce255 | -11.17854 | -41.05217 | 2025-10-26 04:02:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bdfc0bbe-3eb4-35e4-84e8-e914b8f27676 | -10.79147 | -47.61115 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b40794e-8158-353b-874b-9dedbb7e064e | -8.72532 | -48.57205 | 2025-10-26 04:02:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cd3d62b-1d52-31b1-8df6-f3745e1656fa | -14.50925 | -43.00305 | 2025-10-26 04:02:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 6143307c-7ab4-3470-b689-a3223d97a543 | -10.5123 | -43.25616 | 2025-10-26 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12131780-b785-3fa3-bef4-7d35f680a092 | -13.09083 | -43.04956 | 2025-10-26 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa645680-0905-33e7-9a9c-297b7b138931 | -9.26085 | -45.59208 | 2025-10-26 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c2944e2-dd01-3ff2-9966-ad7616b2175f | -10.41273 | -44.50101 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bbf6c6b-e301-3aa9-910a-e8defa176b5e | -11.52999 | -47.10136 | 2025-10-26 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0661ab7-ba92-3dfa-8417-81135de5a213 | -14.17008 | -44.33438 | 2025-10-26 04:02:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8851c411-e027-33aa-ad2d-e2d9bba08c75 | -12.90876 | -48.51311 | 2025-10-26 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5000bc51-048e-3818-b3d6-6a36a047c1d4 | -13.43566 | -47.39376 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b2cb3be-e9a4-3d74-aa87-eecd95798070 | -16.17592 | -46.46151 | 2025-10-26 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3d253bc-4603-3c85-8572-cb60a583fe56 | -9.15634 | -51.30994 | 2025-10-26 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efdaf6ea-a2e8-3845-96a5-0ac2a6ac0926 | -9.59714 | -47.69717 | 2025-10-26 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0065a37d-e31f-3b74-b675-f8db8822f2e8 | -9.68598 | -47.43892 | 2025-10-26 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79c62dda-8125-3e00-9f02-12c56aeb4c0b | -13.2338 | -46.54779 | 2025-10-26 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03b27751-d8f0-3f0c-b052-3ea317d59bdc | -12.00208 | -48.94025 | 2025-10-26 04:02:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2a2f6a7-df29-3f38-964d-228933f09744 | -12.44142 | -43.6934 | 2025-10-26 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef2f7a20-7895-31cd-a722-ffcb560dbf8e | -15.30348 | -50.75912 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc5237fa-cb9e-3882-81e9-ed531c96de72 | -12.8342 | -48.65849 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f510041a-a45f-3703-b2c2-41a3ee198e55 | -12.30223 | -47.45702 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95414e6d-a00b-3189-94ca-f907951259c5 | -10.79067 | -47.61569 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43c8ebd6-bc29-3e92-bd4d-3713b60cd206 | -11.56349 | -44.97571 | 2025-10-26 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0f61d5c-56b4-3043-92fc-72f115d620c1 | -12.84106 | -48.6474 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 864c792d-9ff9-3e5e-8b51-8ed87aca9482 | -10.90125 | -48.02858 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21a275c3-78e8-3289-bf06-d44f612c6a83 | -13.9439 | -41.43816 | 2025-10-26 04:02:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82d16002-d355-3b2e-aaf3-bcdbada4f6ef | -10.79294 | -47.61307 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0509c93c-07df-3b90-ad28-0d024e7f731e | -11.7686 | -48.18708 | 2025-10-26 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df636b2a-a6df-3dee-b4f8-7a9d4af31a1f | -10.57211 | -47.99669 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7abfa1d7-eb2a-3de5-97b3-a2badcb3aeaa | -15.21301 | -47.9287 | 2025-10-26 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a324d318-130f-3c44-b34c-12f39fa43e48 | -12.10752 | -52.49352 | 2025-10-26 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f27d56c3-fde3-3811-8080-4e011790ec80 | -9.26296 | -46.41541 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac2c3e1-63d7-3e57-9872-fb436893a446 | -15.18345 | -47.23111 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb8d673-be1b-3099-87e7-8dc53aab5ff4 | -10.80536 | -47.87994 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 001c8ec5-fc6a-3844-8eef-c1413d9a681d | -10.87232 | -48.03035 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e7cf2ee-491d-3e91-8b65-a5292faf5b98 | -10.76942 | -44.50211 | 2025-10-26 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25117c3e-3d2f-3e01-ab68-4d0fa6fa51cf | -10.94363 | -48.07777 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d5a37e1-5028-3c82-a524-da3de609b709 | -11.5089 | -48.24212 | 2025-10-26 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 179f4046-cb3e-3fb4-b84e-d992a4cf02e1 | -13.87862 | -48.47571 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 379ba3a0-91ec-34ad-9515-f5535737dc5b | -15.25399 | -50.76761 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2eba4ee-4223-3488-a81d-ba1493b6d437 | -10.74089 | -49.798 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecd64ccf-377c-3aaa-8229-61c6ff91f8f6 | -13.20187 | -43.12486 | 2025-10-26 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0805365f-813c-395b-ad8f-e7bf4415b838 | -15.29419 | -50.76384 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dde2f3b8-a782-315e-bd84-aef93939db55 | -15.58069 | -43.20015 | 2025-10-26 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b0268dc-5b3f-3957-8dca-15396c0cb4d8 | -9.22046 | -50.75704 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc98681e-a8bf-3f05-a84e-db9fa45530bc | -10.83091 | -47.6343 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d900668a-eb90-30ea-a099-935fa980e1d6 | -9.5693 | -46.9221 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5db432d4-4e3c-3c90-8b27-960a7e173cfd | -11.24844 | -49.86471 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbc88166-9dd7-3a2c-a416-2a7d34ed9fad | -13.32616 | -47.92974 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdb76d6d-b2ab-315b-9b94-490c898a69e5 | -9.26427 | -45.59636 | 2025-10-26 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d633b8d-4fdc-38e6-9991-de72d47c845c | -13.53173 | -47.15055 | 2025-10-26 04:02:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39768c5d-a408-39d1-a03f-c6b18e4f6a31 | -15.47795 | -43.12991 | 2025-10-26 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c2f7049-9839-33e6-8c3c-b1b1cfe976ba | -12.00374 | -46.78942 | 2025-10-26 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 795b70ff-9e7e-3e25-8219-557b5f3b831e | -12.13688 | -47.01965 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b976fcd-f3b6-3ca9-a679-a88f09931397 | -9.9275 | -47.6456 | 2025-10-26 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e055d001-8da5-3a70-a17f-da499060871e | -16.224 | -48.65512 | 2025-10-26 04:02:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c8c550e-8818-3e19-badc-ee9d053bde8e | -10.77793 | -40.3169 | 2025-10-26 04:02:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5632bc23-81d5-34be-87b6-2b3e2fb1701e | -12.13139 | -47.00169 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18880f11-0a97-3f09-a725-eb2d3a3f5436 | -12.90738 | -48.51503 | 2025-10-26 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2226c4fb-5e30-3c7b-816f-b3f92269c0fe | -14.83623 | -52.45333 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0277aa93-e4f2-30e0-ad43-2e1df3136df2 | -15.73858 | -43.89682 | 2025-10-26 04:02:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7cdbe32-f230-3a10-a3be-7b111ae4f6b4 | -13.79878 | -43.03816 | 2025-10-26 04:02:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4d383a74-e34f-3998-82a5-7592ab498053 | -12.00512 | -46.78155 | 2025-10-26 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88889ce3-988a-3a2d-8487-804762847d32 | -15.74359 | -46.22117 | 2025-10-26 04:02:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00973a93-b05d-3e2c-a670-50b7abf206d4 | -13.40106 | -43.02095 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3b6799f7-c5f8-3c21-b366-d1ba2ed1fd15 | -14.43511 | -49.95519 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ae81d9f-d108-334a-8157-a105e428dd84 | -9.05193 | -46.98874 | 2025-10-26 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5383e309-6339-3a63-b48b-53be3d5f0ce6 | -11.73803 | -47.62576 | 2025-10-26 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e45bc3e-262e-3d14-b20a-5a26cc3ff834 | -13.54966 | -44.01034 | 2025-10-26 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de4c61f5-88a7-3689-914b-0fb8d4678dcd | -13.53722 | -49.54101 | 2025-10-26 04:02:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a18798b-46e5-36f4-846a-9a01fe244fbe | -13.40384 | -43.02523 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c207317f-7da9-383a-b61b-6e53089970d6 | -16.26574 | -43.61547 | 2025-10-26 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdf06cf4-69ba-3dd9-bb05-45e60a6ef803 | -9.56027 | -49.63308 | 2025-10-26 04:02:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeab0462-edf0-3c2e-83d2-68ac5c58adb3 | -10.4291 | -44.49461 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d281f58-c654-33ed-b22f-fc7264a88c25 | -14.83159 | -52.44697 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a11a62f-2159-3aa1-9ea2-847e119ded4f | -9.72395 | -45.42502 | 2025-10-26 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5db35931-e608-3de6-aa25-666d2b0f3e1f | -12.05877 | -43.98927 | 2025-10-26 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.1 |
| d6d84429-ffd5-3052-bfb5-2b5d7e8cb1ad | -15.58558 | -43.21238 | 2025-10-26 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 97f31aec-294c-38db-ba9d-4f3e01f21543 | -13.89069 | -48.41983 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff2e9c0e-61de-323a-8222-eb0b153b2193 | -10.98788 | -44.86594 | 2025-10-26 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc5ed05-6b93-3288-8a27-3bf5b185cc06 | -15.35148 | -42.87948 | 2025-10-26 04:02:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 956b6e8e-ab02-3d15-bf6b-8fc5691daf7b | -12.10048 | -47.271 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcbf2162-4891-3ce1-9bef-7f64f1beceab | -11.75018 | -44.46777 | 2025-10-26 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba757b8b-ee56-350a-81be-d23b853b5d7e | -11.32534 | -53.93116 | 2025-10-26 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f3ce8af-ad9f-391d-b20d-14801eef2539 | -10.853 | -47.95366 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5acbbfe9-21f5-3219-9743-276887f121a9 | -16.53314 | -44.52303 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b134a5ec-0a5b-33e6-bc14-6efe6b6c6057 | -11.65951 | -41.44728 | 2025-10-26 04:02:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5f93b65-54c0-36a2-9c2b-7ae8c492f5bd | -16.61498 | -44.5781 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1328362a-28dd-3627-9fae-9e582119c8cc | -13.74802 | -42.74604 | 2025-10-26 04:02:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4393d2d2-10c3-3a76-900d-65dc76287c3e | -14.76953 | -46.61574 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6085c076-2644-3bd0-ab8d-e06563d63ec9 | -13.80647 | -43.0547 | 2025-10-26 04:02:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef2590f5-6d32-322e-94b0-dafd97a88a38 | -11.12443 | -43.24345 | 2025-10-26 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ae11647-0517-3d17-963d-b99178fbdc40 | -11.24783 | -49.86789 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6e27c43-e205-3809-9219-54655b4af750 | -15.25013 | -50.76023 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
