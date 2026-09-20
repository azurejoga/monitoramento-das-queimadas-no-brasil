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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8c94851-937c-37f1-984d-c60fc47282e3 | -2.91655 | -57.80039 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a2a0c27-e302-37c6-a461-3914d07f1d71 | -4.87729 | -45.60433 | 2026-09-20 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 383374c1-c321-3f93-9425-038e1ff51a52 | -1.50022 | -48.94048 | 2026-09-20 04:38:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c79c37-a7e3-3a9c-89b7-b5e07515f4ed | -3.50704 | -43.35794 | 2026-09-20 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a39988d5-e535-378b-9d59-3ceae74c6f30 | -3.55324 | -50.29307 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fb6c8d0-b8d8-38ed-852a-1e56452c2611 | -3.88752 | -55.88796 | 2026-09-20 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca5db47f-d594-302b-aa55-330c6fa11dc9 | -6.21286 | -45.33982 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86dc02b6-74aa-324d-b4e6-b8221bd30515 | -2.89409 | -57.8266 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce4c60fe-9d7f-3752-ab3b-508433fb7de6 | -5.34816 | -44.82545 | 2026-09-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e676c415-a50d-364b-b9ad-171dfe8e4925 | -5.41619 | -48.44243 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ea8af8b-c6da-39da-9eeb-d199d4d186a6 | -4.98694 | -45.15019 | 2026-09-20 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca945f96-d07f-37c5-b4c9-e1e0012b7aa2 | -3.6718 | -54.27503 | 2026-09-20 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e21dda5d-a967-3e23-82cf-5333f2c91c18 | -6.51412 | -46.77443 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8506439a-0877-31ec-86c0-9f076d81fbb5 | -3.09495 | -48.68142 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbc0a6d-36cd-37db-b4a2-2c37cdaff52d | -3.44433 | -58.22929 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c826beca-1ac8-3883-8a60-44e5b717d821 | -5.83889 | -52.03302 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da369607-e148-3cb3-856f-176d9f646817 | -3.16259 | -48.61456 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff36c15-1fe5-3ac5-b101-d47f335404e6 | -6.49023 | -47.58151 | 2026-09-20 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73c556bf-4053-339e-8580-3fb522699862 | -2.82705 | -50.46814 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314b20c1-b698-3dab-a2e5-bb124f821a55 | -6.19748 | -47.5206 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc4816ca-0bd4-367f-be69-ceeb0ff3043a | -6.04557 | -47.51469 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f89d5a6d-1879-3df7-b351-22b8a6690503 | -5.38718 | -48.73131 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4a46511-112b-3887-ae9d-3b4417a1ff87 | -3.68983 | -60.6101 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7b93adf-2826-35a0-b2eb-044ba17a24ae | -5.22417 | -47.57635 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 624991a1-bc72-3bcf-8fcc-d1a82180d79d | -2.25556 | -48.75296 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4997f8e-8955-3610-b2b5-741a8a798d23 | -3.57047 | -43.47336 | 2026-09-20 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d98e4b5-a823-315e-8c69-7f3cfd2c588c | -5.35048 | -44.83418 | 2026-09-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 883709ba-cf75-3f3c-b947-87a422c384eb | -3.39985 | -54.07099 | 2026-09-20 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e26ac52-d81e-3de4-a95f-78b8120a4c14 | -5.23791 | -47.55376 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8e2394-2e21-3073-9159-85264d627643 | -6.17409 | -47.7122 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 386dada3-4bd8-355d-8017-466901858499 | -3.38024 | -39.20274 | 2026-09-20 04:38:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a47e845-35fb-3513-b8ee-308820d7f17f | -6.206 | -47.35795 | 2026-09-20 04:38:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca1cb1cf-c4ba-3df6-995b-e2d114302943 | -2.88008 | -57.80267 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 61a57b7e-1dba-3193-8b30-c4a6571b4faf | -5.9275 | -35.62172 | 2026-09-20 04:38:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4acf38d0-e54a-3f7c-9e04-8d57f76d9933 | -2.82083 | -54.71566 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c714adf4-08b7-3de7-827e-f232d6384a82 | -5.79287 | -51.86534 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7244f806-647b-383d-87f0-8f3bf68a8c3c | -5.99805 | -44.95041 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e578b4a-8608-3a8e-b222-6cc687b00bd8 | -5.55183 | -45.54547 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e1bce24-5934-3036-97f1-f13071ce3857 | -3.13304 | -52.71757 | 2026-09-20 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82883076-1bf3-3b80-a4db-bd43d73baf6c | -5.80107 | -45.21904 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ab7efe7-fecc-3505-b665-973ea5e0496c | -6.30259 | -47.60857 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81fb92e4-839b-3705-a145-9fa66c561875 | -2.97934 | -54.76754 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b426a627-f3aa-38a9-b7bc-0dfaa80b651d | -3.49974 | -53.44272 | 2026-09-20 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce6b857d-cab7-36d5-806a-7b423c580ae3 | -2.17568 | -46.38134 | 2026-09-20 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| babe6610-3b3a-388b-9450-653ade2a179f | -3.37343 | -50.44667 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5feda35-7a52-30ed-a202-f0dda5375430 | -5.46444 | -45.61428 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06489f4f-1818-38f2-b924-3eef0524a3e4 | -5.8684 | -51.57375 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3662f56e-ce18-3b20-9fe3-d3375df18f35 | -6.88881 | -42.9281 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| abfaabd4-9a5e-3a84-8435-29657c00a19a | -6.36056 | -43.36463 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96354e9a-d33b-3ccc-8b95-c8269872f621 | -2.14541 | -50.90421 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad91eb4d-b9fc-3007-944d-4755c554818a | -5.92586 | -46.00235 | 2026-09-20 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7c0b7d-bba7-3184-896f-c1ed08a0c723 | -3.038 | -51.37414 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 223c7a35-1e88-337d-bb53-ba35e354542a | -6.16747 | -47.71116 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65ac6579-f070-39b6-bbcf-b9995dba67a8 | -2.88309 | -57.82035 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 145de153-99da-3311-8153-1a67fb4f36e4 | -6.30979 | -47.62749 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae30e4d9-3438-3584-9709-e1c953d337d1 | -3.46291 | -50.61271 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6035efd9-c782-3e50-a00d-34e3bbf37041 | -3.55389 | -50.28907 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e133ee5-1184-3f97-a6d8-8a98a0e7635b | -6.31439 | -45.61852 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2575b9f-599e-39bf-aba3-a27b12b4d474 | -0.84301 | -48.57534 | 2026-09-20 04:38:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60186e82-482f-337a-9a81-b80661c35252 | -5.66865 | -45.30446 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52abe06c-5ec6-367b-93db-0f5567d83b0c | -2.17046 | -48.32075 | 2026-09-20 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd2109c-2a2f-307d-bb8b-f697c3d3ed4f | -5.83249 | -47.78954 | 2026-09-20 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba8d1b1d-4c5a-3b9c-a401-477b6a2de38f | -2.82343 | -50.46756 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6832351-f276-3ad9-917e-a2d4c9e2f9ff | -2.96895 | -54.77118 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6012b5d2-7a32-3979-8683-f5126e1f8e0e | -3.08601 | -49.04298 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a50c517-cbf8-3757-97e7-619a0c7329b4 | -4.19872 | -47.89436 | 2026-09-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 673d3231-ccf4-3114-8cb5-524ddad06f0b | -4.26047 | -48.63522 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34c8885-4476-38ef-af93-8be186489a83 | -4.18128 | -49.40854 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88a47138-ada2-3b7d-a241-b09e65c760ea | -3.72647 | -54.64835 | 2026-09-20 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ad970b8-4485-364b-9a65-b6e76a4ec7da | -3.5568 | -50.29362 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 526290a8-267f-32c3-8404-400d380094b4 | -5.57506 | -45.5333 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f6f04ad-0495-34c9-ae2c-4e77a962bff3 | -5.22695 | -49.29997 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caf3db0d-ee5d-3b6c-bdda-36e1051965fc | -3.73909 | -51.81747 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 018ac28a-70f5-3ef0-9006-c79c436b8162 | -6.95639 | -43.09307 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bf04618-1a6a-3e81-bd95-b8e4e7c27c08 | -6.0425 | -44.03413 | 2026-09-20 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d60afce6-9793-3958-bcf7-dd78a51ee999 | -7.12137 | -43.09908 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2eec0725-1e35-3263-ad32-a3fa86fc98cc | -3.37475 | -50.43846 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f1d8904-ae8a-3d28-b2ac-b19d171f5410 | -4.81858 | -48.22676 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba8c46a6-e087-3160-88c2-bcc0e2187113 | -6.39804 | -43.19036 | 2026-09-20 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55fa291a-e843-3229-a905-5dafb0a6485a | -7.03727 | -43.69147 | 2026-09-20 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f771617a-844b-37ed-bb4f-72e1381788e5 | -5.93404 | -35.62279 | 2026-09-20 04:38:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ace79c7a-d45b-3286-9572-6990eda8f8b1 | -5.24158 | -49.40257 | 2026-09-20 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 751eb3fb-841d-395f-afee-d73f8155df0e | -5.46495 | -47.64295 | 2026-09-20 04:38:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d88d0a24-fb35-363d-a229-6c8636339800 | -4.80404 | -56.08494 | 2026-09-20 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31472284-3071-309d-b280-7411072034f7 | -5.4072 | -44.26937 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41bcd1d7-719f-32b7-a8cb-16eed082d48f | -3.34013 | -57.86748 | 2026-09-20 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84ea9465-96f3-36a2-872d-4ca21298a16a | -5.80862 | -49.08794 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e25f77b9-3d49-34bb-a742-1bcb56127a80 | -2.99716 | -49.09645 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42f9f421-49a0-32f2-93c7-14e47eeb0b42 | -4.78151 | -48.07549 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c416223d-c052-3ec6-b212-ddd675ab4b6f | -5.80805 | -49.09149 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18b59adb-d750-3b86-a2d2-48bb33793250 | -2.19221 | -48.3787 | 2026-09-20 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c91d08f0-3896-3a62-9d94-d39f9244d083 | -6.29596 | -47.60754 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad6e8ef4-b599-3c3b-808c-08e83a4967e3 | -5.2786 | -49.3452 | 2026-09-20 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 027959cc-f071-328f-815a-76ba33efccd7 | -5.28594 | -49.34271 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60af4ad5-120c-368b-b8ed-8765324a9196 | -4.29558 | -48.62995 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abc320bc-9d76-348c-86a3-b06d4267bbec | -6.17146 | -47.49158 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d28e8d9e-bacd-31d6-a31a-5ea2169e102c | -4.38567 | -55.25397 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891d5137-badf-3040-a4c9-e16011a4d8f8 | -3.43532 | -50.66859 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 354d5c28-2601-3678-aca4-2a2f7ef9ab42 | -3.85817 | -58.89291 | 2026-09-20 04:38:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 134f0ac9-d885-3252-8119-0a4e6ee7fcad | -3.72321 | -60.62293 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
