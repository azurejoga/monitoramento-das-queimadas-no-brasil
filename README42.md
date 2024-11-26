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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58c6a8d5-bc73-3256-a139-5a396ab75bb5 | -3.11379 | -45.08347 | 2024-11-26 05:01:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74a3f4a8-4ae7-3db6-8b7e-e6a4f8694830 | -3.96666 | -48.05238 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6dfebad-9b0e-34bd-9cf1-b46583c02713 | -2.45658 | -53.68536 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6196b58a-de2e-3f27-889f-7bd9a4ad97f7 | -3.17367 | -48.44436 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eaf3f8ae-536c-3ce0-aa3c-592853165540 | -3.50143 | -53.80697 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4175ca6-f2cd-370c-bbca-5144b5c49dd8 | -3.2246 | -53.83645 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5380ada2-a2fe-388c-b634-a6b91ed71bc0 | -3.79205 | -50.97002 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7ffb350-59d7-35b4-8388-fe2694a7feb5 | -2.24979 | -53.61762 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83f94b21-f8fa-327a-afbc-6fa9eb8435de | -3.05744 | -53.28337 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c77ce1cc-00f0-3cf6-944b-fe81730fde84 | -3.26978 | -50.55658 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ad225f-0625-3bf9-bbc5-fce1971dc41e | -3.3265 | -50.05656 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cea5a67-45bf-301f-9276-0d22df638e3b | -3.11434 | -45.07965 | 2024-11-26 05:01:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06a1d4f3-d5d9-3de0-aa07-5f09ac39a647 | -2.58229 | -53.97082 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89bb5c74-88a1-3601-b36d-8a6c68eb96f8 | -3.04649 | -51.44509 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee64960e-f98d-3621-b726-c74939fa2cdc | -3.98391 | -48.06443 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 3752165b-ed2f-3f11-9982-8b237cd1cdfb | -3.97849 | -48.06901 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1970673c-a131-3e1a-b6c6-6749c1499513 | -3.98028 | -48.08922 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3c344fc8-639c-336c-9b69-4c87dc7267f6 | -2.9317 | -48.02185 | 2024-11-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3582bf75-034e-3f03-ba83-bcfd7e19ec35 | -3.26473 | -53.82096 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e3b5d42-108b-3c1f-a3af-9460be514c36 | -1.72108 | -53.59033 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d21c3ecb-e783-3b5e-8575-f81e21b08b22 | -2.9261 | -51.45038 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f017fd7-e2cd-3c2d-bdf7-6fa09a09ea2f | -3.48844 | -50.06327 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc31027e-b8c2-3c44-9fef-7d430d34e3a7 | -3.38742 | -50.09803 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc09651c-0243-36f2-8bfb-c4c42f6b1c95 | -3.97313 | -48.07322 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 78cb8160-c8dc-3849-96c0-53dca6e28f0f | -3.71314 | -51.8512 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2570dbd4-61f7-3f68-96df-ab5eb5e2439e | -1.84185 | -55.30924 | 2024-11-26 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac93b74d-7523-303d-a095-a2e1edf73e0e | -2.79777 | -53.01891 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d920c81f-8700-32b2-9292-9ae15b9bedc2 | -2.24358 | -53.62038 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d3a14a7-30e9-3e55-8788-b857956f145d | -2.25314 | -53.61814 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04b2339f-50d7-3717-9f6f-2baeb252b373 | -2.80005 | -53.02682 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c81a19c2-2866-34d1-a1f6-e7f3e46b6900 | -3.27851 | -50.02066 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7a41883-1124-3a5d-9a61-9f7212be968c | -3.39197 | -50.09512 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b6901d5-e0ce-3a2b-859e-7e0f593a837d | -4.53085 | -43.29125 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 033287fd-f244-3712-b53d-5575ac059ebc | -3.73019 | -49.94986 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dccab02b-fb5c-3be4-acbe-3a395a724803 | -2.45384 | -53.70299 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af71ec97-a596-3f43-8164-fdccb65efe4f | -4.18523 | -48.44617 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde0e9a3-82c9-3489-8014-07ac24c0fb67 | -1.88575 | -53.31838 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 491aad70-f887-36cf-9772-c04e268c16d0 | -1.96947 | -53.13652 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbf531e7-2187-398f-abd7-2df039efd5e6 | -3.18393 | -48.43685 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| caf104a3-bf73-347a-9947-2201822489bd | -3.29162 | -51.15754 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3161718-ffc0-33b8-9537-2c8bdc583ef6 | -3.91028 | -42.42624 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f60ca5a6-8151-34ed-bcf1-e69491db9fdf | -3.97598 | -48.05361 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b35cc4bc-10e4-3c70-b69f-744091083073 | -3.06811 | -50.9477 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43954c38-9fdb-3fde-a6b7-2126fb680e92 | -3.34492 | -53.73878 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ebbfa77-4547-36a7-ba88-7a0550b9c387 | -2.80346 | -53.02734 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5262ce8-1a1d-3d2a-a885-fa261495010c | -3.29012 | -50.76172 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f767a65-ffea-32fc-9805-d667b6678a75 | -3.44215 | -50.00966 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58ce20e6-46a5-3200-9e7d-86ad5b97165c | -4.30449 | -48.17926 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e3b2ee8-3a73-3668-b47a-074c0cc41f9a | -2.77289 | -52.90923 | 2024-11-26 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdf14803-c008-30af-8f60-04d8ecb12e61 | -2.44015 | -53.96624 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da16ca6-9d3e-302d-84ec-ef835b4e531d | -2.32991 | -53.86761 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be838ab9-0c28-3319-9ea3-dff99cece444 | -3.42936 | -54.02679 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aaa7aab-7778-35d0-9732-ab4eeaad3686 | -3.28938 | -51.11767 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d027c452-3f76-3424-ac0d-8a8fa2cd099a | -3.55477 | -51.59355 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9625c772-1b02-35ad-87ec-374a501d1421 | -3.3337 | -53.72243 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05539448-f438-3c59-99d3-0cd61a77882c | -2.82053 | -51.79395 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d26ce22-1cde-3fc0-b501-f356cc242751 | -3.96064 | -48.06108 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a2014362-885f-3307-a5ce-83cd7e5e813c | -1.91752 | -53.0023 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e362fd0b-14e5-3e4e-8be5-0cdd5f0c40e9 | -3.07365 | -49.202 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b1d038c-b770-36d5-90b1-6ea3798bc7ca | -3.97635 | -48.08366 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 8f4483ed-4a9e-3c67-912a-d69cd2860410 | -3.68755 | -50.23178 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2e93466-9d30-3a95-9847-64896d0fcced | -3.06251 | -53.27981 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d012d869-1746-3e69-aaa1-279940c8d0ae | -1.98747 | -53.29699 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d93b2227-9441-39c4-adcf-2cb41046c009 | -3.80487 | -51.26386 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4594760f-ad9d-3c2b-8712-16361c9344a9 | -2.16758 | -51.96734 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 118a7969-67c8-30ae-bc45-acd9bd7733aa | -3.28701 | -50.7564 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0675c4c2-7884-3c76-8ee0-2c83f805af25 | -3.28438 | -50.27595 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c99d5f0-b066-3ae0-82d0-db9414410fd9 | -6.63983 | -47.34855 | 2024-11-26 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 66cc395a-6cd7-32ca-b8d5-a88770422b74 | -2.61099 | -48.36652 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76021504-509b-367c-a81c-03a39809eccf | -7.19208 | -48.59998 | 2024-11-26 05:01:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c38632-4749-3b7a-95f3-a5749ba54c17 | -2.98549 | -49.59061 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bbec4f3-3c5a-35d4-8244-6fffa3e5b642 | -3.28834 | -50.27652 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c255e6a0-66f5-3b5c-b5f4-01d0939d6bfb | -4.76268 | -45.59172 | 2024-11-26 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adf28f07-96af-3058-9b91-3214f6fc2128 | -2.38844 | -53.71147 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc39e691-5125-3eac-8d38-0192faf5eb88 | -2.70334 | -51.99071 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 877db63b-7f74-33d3-bec6-0c649a1c9c99 | -2.18093 | -53.80127 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e772286-c0d4-3020-b56a-c1d068f0c354 | -5.75424 | -46.26492 | 2024-11-26 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c974aa38-e89e-3555-8cef-18936080d30b | -2.24924 | -53.62116 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03c49ed6-fa8f-37c8-8c4d-bcfa53499e91 | -12.04121 | -54.6843 | 2024-11-26 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2e3a9dd-77a7-35b5-a0a4-8d3ac03aba08 | -11.93367 | -62.92323 | 2024-11-26 05:03:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d0fc489-85ce-3385-aea6-84d0b2ca728c | -12.04238 | -54.67651 | 2024-11-26 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c943df34-3636-3c35-8ca9-80aa755b64d4 | -15.07442 | -59.6349 | 2024-11-26 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06a0971-486f-3b2a-aa8b-992dcf57385b | -10.76457 | -56.28695 | 2024-11-26 05:03:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6e81482-a950-31ac-964f-52dd44e2918f | -10.76126 | -56.28643 | 2024-11-26 05:03:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80a814a2-f8ee-3a3e-8c76-0038807582df | -11.72685 | -57.44537 | 2024-11-26 05:03:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45ed3b2c-9d2c-38ac-8bf5-aa1217499ebe | -14.79728 | -57.55362 | 2024-11-26 05:03:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de1c0f19-8ff4-3156-a38a-0b67cafaef00 | -11.92871 | -62.92645 | 2024-11-26 05:03:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 639a0d0a-8bac-3ff9-8d09-5debecfa6a7d | -11.92944 | -62.92244 | 2024-11-26 05:03:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e011648-2e3a-3d1f-9770-059b1786c328 | -16.02493 | -57.58325 | 2024-11-26 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8701ff6f-377e-335a-a094-77275d71fc70 | -11.54592 | -56.43712 | 2024-11-26 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8493312-a4f7-365a-8ff6-d44abcb9077d | -12.03773 | -54.68378 | 2024-11-26 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36d7ec15-19be-30e0-be8d-76e160777fb4 | -12.33496 | -49.9937 | 2024-11-26 05:03:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 433ea197-06da-369e-bddf-136a047ba8bd | -11.54537 | -56.44064 | 2024-11-26 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe91d2b-bff7-34bb-a0da-08a99a383c81 | -15.51923 | -56.49852 | 2024-11-26 05:03:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbf4e42c-ce12-3b5f-8216-b6b80632c0f6 | -12.03832 | -54.67989 | 2024-11-26 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c70fe8b-7f9d-3bd2-a28e-b1f99925c0d2 | -9.70417 | -60.14785 | 2024-11-26 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d642db3-b178-359e-82c5-542ffc79eac1 | -12.04179 | -54.68041 | 2024-11-26 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b4f86fa-7f7f-3e3b-97c1-5c75c1c584b8 | -9.92886 | -59.92871 | 2024-11-26 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b8b5192-a1c6-3b9d-bf62-62bb7e094d1e | -9.74259 | -60.21391 | 2024-11-26 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f238c009-194f-302f-afd3-1bf3ae4df5d6 | -12.33894 | -49.99916 | 2024-11-26 05:03:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README43.md)
