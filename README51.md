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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 355ddae9-d19c-3a04-86f9-923ee903f24e | -2.58923 | -54.22738 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8eed9735-3938-3c3d-9bc5-dfb094d0ff42 | -2.66623 | -46.13942 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3976901d-5ce9-32be-b937-b9851106233c | -2.16021 | -50.45541 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c7b13cf-f1e4-3389-a5b3-0429dcc4aa20 | -1.23036 | -51.79482 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| afc23e6e-ed9f-3959-9386-947d0c45c90d | -2.60014 | -46.26266 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 899cfdfd-7f17-3f90-a833-c77f441ce3bb | -1.19188 | -51.9329 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58501ed7-ad87-3c08-8f8d-9701a18043ac | -1.42227 | -51.13137 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef1563d2-6d06-35bb-a29c-affefd02c30c | -1.27707 | -52.17126 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0065162f-f5e1-3ec7-9c10-039522751aa1 | -3.88193 | -52.37211 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a51d36fa-afe8-3a06-9dc0-4d215c93f517 | -3.44149 | -50.0216 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e36c2f88-3a24-369a-95f5-2232b38e697f | -3.18424 | -54.77199 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01ea0d62-1a5d-371f-8651-af9f03bb11db | -3.28804 | -50.04128 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f27093e9-61b3-3014-a6e7-1b44a61c216b | -1.1508 | -51.6941 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 787dc34f-dc5f-349f-8911-36cd83484a28 | -2.08851 | -50.49559 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14947175-ccf5-3f1d-9a25-fd6146aab5b8 | -2.70097 | -46.11189 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d23ba21c-3b03-317d-bacc-b2194f970d33 | -3.24723 | -53.61968 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c771e2d-05d8-3c93-b83c-98356a3f8492 | -2.23631 | -50.46671 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d9bbf08-2a7b-3930-b37f-aee79b1a2d39 | -2.17653 | -53.63954 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09dd0e04-9ead-3349-92fb-ebafcf3de67e | -3.09765 | -53.98773 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb3d7b3d-3330-38d7-9134-0571884f54d5 | -3.39226 | -50.32274 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 31141ba7-7132-348c-b413-6a3003307f62 | -1.73302 | -55.24654 | 2024-11-24 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20c03874-c878-3f5d-aba8-7e953ce61279 | -2.31425 | -52.17166 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4204b75c-a8c3-34b7-931b-62f4fce0cf13 | -1.94999 | -49.53001 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82d6519b-fd36-3bd5-9ae8-d12b32f81e68 | -5.35952 | -45.03598 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9233ebf2-2fb6-37f9-b689-e6d4987610fe | -3.22857 | -53.93647 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 748fb957-510f-33d3-b29b-b2135d33f7c6 | -2.17539 | -49.26964 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc0467ae-9b72-327b-a867-d7ccc6e946df | -2.25021 | -50.35484 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4e8ff4b-9316-3b7e-abbd-aa8ea7b535bb | 0.23653 | -51.66682 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d394dbf4-6baa-3c95-8746-157c8ceaa81b | -1.38379 | -52.33617 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f70bf1af-fcaf-3884-95ea-d49efb9a43c7 | -2.43694 | -50.42028 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2c6aae5-5369-3cbf-876b-1e65f8498286 | -1.56734 | -51.20327 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b93ca20-918e-3229-a126-d7fe043c22a2 | -1.56276 | -53.52261 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c29eb2c9-05f0-33a5-a80d-18ae2012c8ac | -3.50538 | -53.81116 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f14b333c-e26c-3d22-bdb2-3addcfd40f3e | -0.95028 | -51.64898 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fba50e97-bda3-3308-8233-970227457e4c | -1.45719 | -55.45152 | 2024-11-24 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50055f07-8415-3bf7-b1b4-8a05a4b308f1 | -5.41272 | -45.76117 | 2024-11-24 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 932187a1-536e-3bb1-a6b4-7aca5067848a | -3.2807 | -53.83258 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc76efbe-96ef-3d3c-a8a6-0b1d2110d2bf | -2.19871 | -50.68674 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6e27a21-5561-33c6-981b-5ea53880c13f | -1.45566 | -54.51311 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a782a69a-1983-3db3-b0a5-f65179f77aac | -2.47167 | -47.08799 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 24bbc32b-68f0-3361-9e1d-365ee3a16251 | -4.14122 | -54.338 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc61430-e5a5-36db-ada3-860743b68b66 | -5.08062 | -44.16872 | 2024-11-24 04:53:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49e5ac7b-a0da-3a85-a175-868048dd644c | -2.19728 | -50.78404 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b32d05f-25de-35bf-9a37-d3c68999c1b0 | -1.68789 | -54.26325 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67dec7fa-a02b-36e2-9cc0-d882402b89bf | -4.27194 | -48.60895 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43a43f9d-2283-3b20-9eb7-37f9a42ff1b6 | -1.50173 | -49.68301 | 2024-11-24 04:53:00 | NOAA-21 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c844e9fa-a824-3c30-b8c7-c7ba190d515a | -2.58863 | -54.23117 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b334668f-cca3-3f7f-9a02-57b796893053 | -3.49949 | -50.46981 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e651b6-4fcd-3ab2-a392-2fad01402760 | -2.21129 | -50.8258 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c6bf299-680d-3f4a-9254-f27ca11a987f | -2.70705 | -46.27027 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 481b9e58-33c1-3ce7-8664-dbb4ea53602a | -1.27791 | -52.25257 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe88ae6-fbd6-31f4-bf4b-fecec98cea07 | -2.9035 | -54.59745 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdca02b0-73d1-3352-ab80-05074ffef0fd | -3.79157 | -47.48695 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe7967a1-f9c3-3f20-a73d-fc33f0820ce5 | -6.35851 | -47.91074 | 2024-11-24 04:53:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2df50365-3a07-333a-abc3-31d40f90ef87 | -1.24134 | -51.78949 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3ef044a-d48c-38d8-b511-a475bb7516f4 | -0.92915 | -51.71942 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23ddaae9-95fa-3fbf-8859-9b945c7b3822 | -0.98653 | -51.76334 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935e6437-092c-32fd-be4b-0a69e81c0a70 | -1.4614 | -51.1197 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 44bb45b5-90d5-3fc6-a2ac-857d78481011 | -5.16461 | -46.20535 | 2024-11-24 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba00f539-935d-3d17-9311-dbe8b70bd187 | -4.40877 | -45.89616 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 855acd15-edea-3967-a6f1-7b307a60929d | -0.23146 | -51.47995 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebe55fb2-d599-3c2f-8f90-63403cca5768 | -2.45839 | -53.70153 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e99e5b5-7bbd-357e-9589-921ac317b80b | -3.5784 | -54.71496 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a185cc8-802a-3828-b113-623a5306ec61 | -3.97109 | -46.73248 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ecf6e7b-a649-34f9-952b-2285c33ff92c | -2.41595 | -50.35428 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9032e54e-66a1-33c9-a330-64b8c5b86390 | -3.58622 | -51.21012 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb39dc09-7e0f-388a-a3f9-cf98f4f07f38 | -3.06992 | -49.19938 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d7def894-b899-3f7e-b341-4bab57da2e10 | -0.57146 | -51.72333 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e1c737bb-a332-3ee4-a56b-6835e91bc971 | -0.05709 | -51.59686 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe019d2b-031b-35a7-a3ae-be61ca6a378e | -3.10614 | -54.00042 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a917888-7ccb-3a27-af00-beedc079c73a | -0.81863 | -51.49126 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0b73fc6-9d12-3ca7-9abc-0cfab718568f | -3.75689 | -49.93635 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2790bd54-7f15-31c9-8258-1c88a96b8e1d | 0.08315 | -51.49026 | 2024-11-24 04:53:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6db38fae-b99b-38b6-828e-e12a2f83240b | -2.14932 | -50.91679 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4409e19b-f3d1-3c4a-b063-71a6ce3d1824 | -3.26121 | -53.70655 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb1863d7-c6e9-34af-864b-b80d46729d0b | -3.49607 | -54.02275 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb4b9c4a-1322-3a33-9909-4f27755adf9a | -1.38433 | -52.33272 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a012af76-ef89-3e9f-b20f-2080e26d198e | -0.92057 | -51.64441 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51e299cc-3d36-3c59-9fa3-192fcd258eb1 | -3.01553 | -51.38288 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1327f016-28d9-35ea-9c20-dbd5e91899bd | -0.27442 | -51.59944 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1216460f-c237-3421-a1fc-161fb474f617 | -0.37377 | -51.55171 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96243738-7a77-3d88-a1fb-408daf31a7eb | -1.64102 | -55.25966 | 2024-11-24 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6409b7b9-c16e-3923-b5d6-419d7bb7d765 | -3.85842 | -50.05205 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecddad72-0470-3330-b51c-c27f550e04cf | -2.31564 | -51.31305 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5381cf0a-2eb6-3db6-adc5-ce36bb7846cd | -2.08399 | -49.61126 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 85d49ed0-4051-3de1-a573-1871210db02a | -2.41653 | -49.11407 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0472e7d-6779-34ba-8ddb-fd2d72514bd3 | -1.24443 | -51.61799 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f95e482-cc54-36a8-9cd1-3cbd3aee5de3 | -4.41827 | -49.83098 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a003d24-809e-3358-83b9-173a1a6e1152 | -4.14032 | -51.06103 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ad07de-a502-3379-810a-79f587fbfb43 | -0.33303 | -51.54879 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0282460-bc10-33bd-b1a2-d6ac211ff122 | -3.47972 | -50.43378 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 954452d0-0975-3aac-8da9-1ae53a8f518e | -3.26786 | -53.81898 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 25bc6f15-8e94-31d1-baf7-8288c4c1d167 | -2.13123 | -50.21855 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99942ed6-b0de-306f-a632-aa842be04333 | -1.10369 | -51.736 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c208ab-e545-3cdd-9baf-aa93e025c324 | -3.57902 | -54.71111 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f111b689-8660-3fc4-83fd-343e51e0442a | -3.52101 | -49.94089 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb3e45f-c641-338f-b9f8-5d2745903a85 | -3.38469 | -50.73385 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9901ca56-2f5e-33ba-a7e7-1eb38fc95561 | -2.78266 | -54.04922 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f99121aa-4b55-352b-9f87-fef0e9b6e602 | -2.37507 | -50.40692 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9099c941-8d01-3f69-b311-e27bb863fd29 | -3.62926 | -55.46413 | 2024-11-24 04:53:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README52.md)
