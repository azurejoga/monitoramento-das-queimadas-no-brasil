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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 422c04f5-40b5-36c6-a2b9-e578352e1ee3 | -10.06514 | -49.65738 | 2025-06-26 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ee19f52-ef01-3aff-a338-1bb58128f90a | -9.12114 | -49.43839 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d565209d-1235-37bc-a205-284da5e92d59 | -4.52535 | -48.05328 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cc39a590-2562-328d-aa0e-a5043df7f60b | -10.50765 | -47.20324 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1e73aec9-a51d-3818-b8b4-444fcb1526b4 | -2.44506 | -47.5017 | 2025-06-26 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6980962-3051-3ab1-8d1a-36e069e99515 | -11.61187 | -46.50717 | 2025-06-26 03:47:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c825f2ae-d4b5-3b14-a1cf-e177439c9066 | -9.87185 | -48.44699 | 2025-06-26 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6286ce8c-8ccf-3e91-a8b4-b04a38a064be | -8.06148 | -46.9724 | 2025-06-26 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f8ec87d-519b-33c6-875a-7f08f8c9d323 | -4.12354 | -43.07038 | 2025-06-26 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e015f4f-0153-34ab-a518-f22ddf781ff2 | -10.65532 | -44.48867 | 2025-06-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96009b50-dcb7-361a-ac25-c45131e38bdb | -11.09129 | -46.63425 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb48384a-1d37-3536-a9d9-45ecb4389b5e | -4.27504 | -48.18641 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b350be2-7bdb-3cb8-be52-b234114d5acf | -5.19413 | -37.69773 | 2025-06-26 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 580778db-33b5-3ab7-b311-7b07a4ff011f | -9.12154 | -49.44807 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f13e424c-8f08-393e-9100-503d4070844d | -5.03634 | -37.64017 | 2025-06-26 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f52b5e8a-31bd-3ffb-99ae-928adc39ef23 | -4.26961 | -48.1801 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bff48095-f5a0-34c0-8b3b-51a90e24a01a | -9.24044 | -49.30736 | 2025-06-26 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e5822a2-31d1-312c-91d3-5446d265a007 | -8.79734 | -45.00681 | 2025-06-26 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a39c9af-f2c7-3231-b4b2-f973ab1ece14 | -8.72522 | -48.01819 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39c552b0-c117-35c7-88a1-8e5c41c89049 | -4.18688 | -40.49712 | 2025-06-26 03:47:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5a140fac-8391-3cf7-a975-8f40c7aab805 | -8.06706 | -46.97308 | 2025-06-26 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0021ee4c-284d-32bc-91ce-f8af5ec97939 | -8.7202 | -48.01274 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac4c2398-fc7e-3491-82a8-a4f49e40cf0b | -4.12575 | -43.06423 | 2025-06-26 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1737963-e819-354b-a8eb-28d5bfceb90b | -9.85246 | -44.70198 | 2025-06-26 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2cd99abb-8f9c-36f7-ac82-3009667cb713 | -10.65085 | -44.48785 | 2025-06-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3173bda-ff3a-3552-8e81-a9e855bdf3c9 | -11.58723 | -44.63855 | 2025-06-26 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a118af28-429c-3b94-a705-f9f6470c6803 | -11.08935 | -46.63235 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc3c0931-0bf5-33c6-a6e0-97796cdec9d0 | -9.87103 | -48.45139 | 2025-06-26 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b7e5292-bdd2-340d-ad52-8a2e1fb69cbb | -10.61903 | -48.08081 | 2025-06-26 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dab36f7b-8cd0-33d8-bead-e89f7c46e8bf | -10.65613 | -44.48418 | 2025-06-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 213fff5d-d9bc-31a5-a3d5-c3a5601fff39 | -9.32916 | -47.82743 | 2025-06-26 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ada1fc6e-c42c-3d72-9e3d-b59f1d632ec9 | -8.70752 | -47.9838 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36e45e8f-26ce-3de7-8257-d590a847be33 | -9.3235 | -47.82608 | 2025-06-26 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15bf60b7-862e-3035-8042-edbffa31eb5c | -13.62299 | -42.91169 | 2025-06-26 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3e0b77ed-30a4-3116-848a-cd5fa90dd03f | -11.79998 | -47.53999 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3423257-eac7-3500-b63b-4c43fc5ebc40 | -6.22056 | -43.36435 | 2025-06-26 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf201303-d54e-3704-b7a7-2b5e583b305b | -7.36148 | -46.23728 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a21e823-a4bc-33d3-b647-9436b237857d | -7.36527 | -46.22771 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c4b6f66-4f1e-3ce9-969d-06c7cf0f923c | -13.10155 | -52.30033 | 2025-06-26 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c377f56-e4aa-358c-9e2b-0e2ce3cb8983 | -11.77336 | -47.40316 | 2025-06-26 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e8c1b04-6d73-3963-b89b-3a29b19d7c39 | -5.90506 | -43.44772 | 2025-06-26 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f840638-cdff-3620-8031-db9caa6ecc0a | -11.36033 | -48.70802 | 2025-06-26 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| f9a9d96d-f778-350e-8952-ce48abdf2d7a | -19.45522 | -45.30921 | 2025-06-26 03:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85b437a6-d924-36c4-865c-041cb7643ea3 | -11.57164 | -46.89954 | 2025-06-26 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9907f66-11a7-31f5-b574-284bbf24e2de | -18.6106 | -44.26183 | 2025-06-26 03:49:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9476299c-4645-38a9-ac45-abed3a0d2b0c | -5.90082 | -43.45282 | 2025-06-26 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 936707b3-ca15-35da-bade-bce865d33293 | -11.80541 | -47.5407 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beec979e-4c8a-380a-a077-51c2bbb0a8d0 | -11.95482 | -47.017 | 2025-06-26 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12511bdf-30e9-3714-8beb-29e80483957b | -16.67999 | -43.88557 | 2025-06-26 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b340572-5c93-3cec-af80-7f56c7bdb869 | -5.89978 | -43.45156 | 2025-06-26 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21f81b62-9fb9-3e4d-a8ba-96f6dd7b91b1 | -13.10113 | -52.29254 | 2025-06-26 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ad1ce58-8b45-3c22-88e4-5d33bea3794e | -12.76151 | -44.40481 | 2025-06-26 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2de15f28-43e7-3621-a95d-91bd04510853 | -7.31158 | -45.7651 | 2025-06-26 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45707c76-7d97-3950-a2e3-93819c17a875 | -12.7658 | -44.40562 | 2025-06-26 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f2c8409-28d1-3acf-a2d3-e1c5797e5bc7 | -11.36613 | -48.70927 | 2025-06-26 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b48a36fe-f242-3028-8dc4-6fcf916df621 | -12.4889 | -45.89927 | 2025-06-26 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b7e02e3-22b9-3cb1-a8fe-35ea94ccfac9 | -6.95601 | -42.8058 | 2025-06-26 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aec5e4fb-fa39-389e-81c2-9330764ab638 | -11.81456 | -47.55095 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d042751-45f8-3fdc-8d9d-1aedd940e49b | -17.20047 | -44.32988 | 2025-06-26 03:49:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f3b564d-8dc4-39b4-a56b-fb20465a6211 | -7.10528 | -47.85059 | 2025-06-26 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2771f8fc-7bcd-30ae-ab0c-841fb85e3b7c | -14.41189 | -47.87637 | 2025-06-26 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20b44278-21e3-3f86-909a-b71d11512b93 | -12.48319 | -45.90349 | 2025-06-26 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d37efc5a-391b-3d6e-8d9a-af047889d4ea | -13.62209 | -42.91677 | 2025-06-26 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c5c1ffee-d547-38ef-8564-6f0234b6f18e | -7.10698 | -47.8414 | 2025-06-26 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e0809c9-44cc-329d-b092-2355b7ee1ca5 | -11.81244 | -47.56197 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22d5a3d1-5a5b-39d0-af1a-84e815f5e7ee | -13.04366 | -48.82277 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a04a035-1ff0-353d-b1ae-07c6545373ac | -11.8107 | -47.54213 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a3d3997-27f1-38a7-bcec-5015ce4f95a4 | -11.57672 | -46.90096 | 2025-06-26 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 485615ee-e794-3fe0-bd2a-348369aa7072 | -7.31379 | -45.75257 | 2025-06-26 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2212df6a-0e21-3021-be9c-a6fb9fb667e7 | -13.32029 | -43.38605 | 2025-06-26 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 80878037-5dc4-3745-87d6-58f04b2a43a6 | -11.95422 | -47.0202 | 2025-06-26 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86f088a-4f1d-3f2a-8c6a-a67a09a9c111 | -13.09459 | -52.29879 | 2025-06-26 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5bf1dc4-844a-39a6-a160-44f6f0c05d65 | -11.56339 | -52.09524 | 2025-06-26 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fdb8d133-bda6-3c2f-ae52-981221eb220c | -15.31831 | -46.91102 | 2025-06-26 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1437bd2c-1e34-316a-b82d-bef4f67e1fef | -11.83166 | -51.25741 | 2025-06-26 03:49:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a28e25f-41fa-34e3-a3de-e82253945b75 | -12.80209 | -48.733 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5569a188-402e-3553-8886-825a02781943 | -12.50993 | -44.08631 | 2025-06-26 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f11fa98b-c74c-3bbb-8a3c-ef78ce98ff11 | -13.03474 | -48.82972 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab49665a-e100-3278-a063-7bfa360e3fed | -14.4069 | -47.87594 | 2025-06-26 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a3486a2-aa9b-316c-9b1c-7ebf7ff11e04 | -13.04284 | -48.82683 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14374c46-2683-3d4b-af5d-f992d84ea75d | -12.48416 | -45.89829 | 2025-06-26 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63784cb-f019-3e13-ada6-83e5b7f48693 | -6.8405 | -43.38014 | 2025-06-26 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfce57e3-0f16-3f44-bafa-64f7f3c5cfd5 | -11.35947 | -48.71234 | 2025-06-26 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| a14736b6-3328-3044-8f32-637e33f4470e | -6.95668 | -42.80182 | 2025-06-26 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 56cc1e86-d926-38fb-9829-f02948338db2 | -11.77866 | -47.40428 | 2025-06-26 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1a180bb-7af6-3578-b3b5-900b802edfd5 | -7.94422 | -44.8753 | 2025-06-26 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a47767f-5649-3432-95b8-2a4701fd0ae7 | -7.3633 | -46.22737 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb8d054d-2932-3ace-b882-56296b894d18 | -11.93369 | -47.8451 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d17c6f8-a21b-398b-ad30-67c434676dec | -11.81387 | -47.55453 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f3640cd-3666-3863-b667-0245c9cc0202 | -11.95301 | -47.0266 | 2025-06-26 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64708754-cd6c-3be8-8ce6-ebd0b18b357d | -9.56105 | -35.69245 | 2025-06-26 03:49:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f7c083d6-2d2f-3498-8a6a-0405e98f9ce5 | -7.35877 | -46.23341 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f524084-3e77-32bf-aef6-6e4093fb4dc2 | -11.81525 | -47.54742 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8315d286-e231-35ab-9007-a6e7c1e6b804 | -11.57383 | -47.43126 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8277f8fe-1938-32fe-881d-69654b91b10f | -7.3195 | -45.75041 | 2025-06-26 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ba4162a-cd8b-31ed-aa82-346e7aa33f58 | -6.17848 | -48.07933 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8f5c6ea7-ffd8-3254-874f-963755b16fe8 | -11.23353 | -49.50415 | 2025-06-26 03:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ede6057-805a-35e8-947a-304b308b7d1a | -7.36469 | -46.23102 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e8a19e9-9c58-3620-83fd-f2cf8218eda6 | -17.18871 | -46.85585 | 2025-06-26 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a374c8c-952f-320a-95aa-715cb721f2f2 | -13.03963 | -48.83498 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README7.md)
