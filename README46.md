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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a7af1bc-97f6-35c9-9248-a59c063c1c82 | -3.85704 | -46.65044 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7efc7e9-26ef-3a56-9ac6-b3dee16bae5c | -5.27601 | -44.90956 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e07cbe47-5a16-3335-9e7b-7c4d9adff562 | -2.25084 | -48.39109 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3cd4c60b-0652-3668-af3f-1e965fa8cb9a | -3.08676 | -45.21115 | 2024-11-17 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fec784e7-562e-3d80-9ca3-845b9b530c3a | -2.11618 | -46.37884 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c34cb0-2662-3389-a050-2b8905b26c01 | -4.51472 | -45.69703 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75b3ebf6-9481-3424-8aae-f21f9a082a1e | -2.98786 | -52.60096 | 2024-11-17 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b5b934d-a5dc-3698-9d66-2b14deb27a2b | -5.06097 | -44.22861 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3b0e8cc-2339-3988-8a3b-d243a698d08c | -3.0741 | -45.38171 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9de426ec-1c48-3c4d-bf9f-a8cb7cfbd315 | -0.82697 | -52.29733 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 064d9922-2370-36e0-861c-abcc9393f710 | -2.57421 | -47.57077 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a85023a4-cdb3-3ba1-a35e-425c4f657bc9 | -2.24123 | -46.8382 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c7fab7-bb1e-3926-959a-ff0eae64c8dd | -4.40111 | -45.5252 | 2024-11-17 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9879a7b6-720b-3b33-91cf-623ac4fa51f4 | -4.20668 | -48.70298 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d67d132-8302-350a-b5a6-8896d8fbb5d3 | -2.51311 | -46.27425 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e4b9766-fb04-3aa8-85aa-06a6f039db41 | -4.45644 | -44.54396 | 2024-11-17 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 853882ff-9f5c-38ba-9787-8b2af41ab580 | -2.67023 | -46.81092 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd53c57-94ec-32b8-8cb0-fd1cb2842a12 | -3.91191 | -49.03864 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1b623b22-2694-3ccc-aa58-0f1ced69b2fe | -3.39454 | -50.73429 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| becef27c-591c-32c5-ae3b-bbea4000e76c | -1.04546 | -51.74637 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd35ecdb-2596-383c-bb7f-e25a8888432c | -1.29653 | -51.73914 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 76674e64-f3cf-337a-9c24-dbb27f4438d9 | -3.62984 | -50.22199 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6349925a-95f1-3c7e-9894-378ba8eefda2 | -2.83292 | -45.49003 | 2024-11-17 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d40b02-9f3e-3af6-92dd-ee736bf1745c | -3.1849 | -53.24877 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| de2f708f-120e-3e6a-9ea6-339d1dbd43bf | -5.27122 | -47.18662 | 2024-11-17 04:29:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e71e0130-ff06-38eb-b6a0-3f14837ec46f | -3.69409 | -50.11043 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f794b677-ad08-3811-bb3b-28af87f79161 | -1.13695 | -51.69182 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0b8454b-ad0f-3c5c-bbd4-a3dd0733a9a8 | -4.18429 | -50.41715 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0162aa8-dc3a-368b-886d-3ee53c3ec7aa | -4.58214 | -48.02491 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e1973693-597a-3f6f-81e7-2bacfdd6ea7b | -3.38911 | -53.27035 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9dc7be6-e9f7-35d1-8c44-eac2fd31cdac | -2.27235 | -46.59685 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8970c7-c90d-32e8-98a1-9cb782619e53 | -4.0073 | -46.5811 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49dcbe5b-2079-34c5-ac71-7029f075dc45 | -5.85847 | -46.44999 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc73297b-4728-3a2e-9212-fb739b5cbdc4 | -3.24705 | -51.52383 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d70a26e-abb5-3b03-95af-eeef9f314ffc | -2.18652 | -50.32768 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51c908c5-492b-3cfa-a28a-09478c8c6372 | -2.08465 | -48.95441 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7cfa02f-1c14-3a26-a34b-39815c7c38ef | -2.90455 | -46.85426 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f97696af-ca89-3e8d-bcd0-907740e3ac30 | -3.94906 | -46.71413 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daa9c7bd-1171-3734-add0-633bd995d046 | -2.07738 | -46.47511 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b4f3420-3855-3747-907e-13a1505f6153 | -2.36746 | -48.5387 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11e4a5f2-0598-33b7-8936-565634084cb2 | -3.21368 | -42.08778 | 2024-11-17 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e004a53-99b9-3fc7-bbfc-c9552e34a182 | -0.9939 | -51.78258 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e563662a-f14e-36e4-b95c-ff9d9edea990 | -2.93646 | -53.30558 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a9fcdf-f71a-3d2e-90c0-eb1eab577990 | -3.90497 | -47.08148 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4487392d-37c1-3eed-9728-093bf31a0763 | -6.38115 | -45.88214 | 2024-11-17 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c83d9ca-d035-3330-b2d2-40f10de3a4f6 | -2.67192 | -46.1925 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6658ad7f-1422-3057-82f0-1e041b73f587 | -3.91133 | -49.04231 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4541b97-a217-3eef-9914-562d323ba505 | -4.29495 | -48.09997 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 477dbaa0-d8d0-3416-9711-3ee0c36130e2 | -2.81226 | -46.66375 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cae0ac20-6d59-31d0-9132-b127efaaab2e | -2.13121 | -48.12032 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa44590e-7ae4-3b35-a007-52b920c06c97 | -0.10434 | -51.61092 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc66fd87-e082-36f8-9512-facdc031aff2 | -4.1301 | -46.09752 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c368aeaf-cfb6-38d6-86d5-010b12d32015 | -3.41867 | -46.13285 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f706884d-6209-35c7-ac18-cf7191e46386 | -4.26127 | -46.97529 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e756ff9-8660-31a4-953d-92182cd5c794 | -2.98724 | -52.6048 | 2024-11-17 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f549afc-c11a-3cdf-bb62-1fb41fc9851d | -4.29882 | -48.09701 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2da6519e-c321-3043-b0bb-218320e77249 | -2.67299 | -46.81487 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ae8a20f-30c4-3e29-90f9-910f373f6fdc | -1.95883 | -48.97327 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c269ba18-4863-3fac-92b9-9542299f19a8 | -4.45522 | -44.552 | 2024-11-17 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ed0bdfb-862e-3e4f-80c1-3ebeff0c4748 | -2.79083 | -46.64654 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 454dbc2b-ec3e-3e30-8cd9-9a8a9912e4db | -0.10661 | -51.59657 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7116f848-3999-3676-a3bc-e0574e4a8142 | -1.83226 | -47.92586 | 2024-11-17 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f248708-3184-371a-a107-8936ca290da1 | -1.39454 | -45.95469 | 2024-11-17 04:29:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32eb82e2-853d-3475-93ad-9f45545e8ab3 | -6.82224 | -46.77625 | 2024-11-17 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c1b8273-fae3-3872-8dc3-29cf1d75ad2c | -2.17043 | -47.95326 | 2024-11-17 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b8cf342-476e-3de1-b5f1-a55a4e39dad5 | -2.62779 | -48.55986 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 819fc69d-75c5-3657-a5de-42797b306122 | -5.33853 | -44.99866 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68e2871a-d90f-3e53-837d-fda57427055c | -2.74699 | -46.08274 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5aa3d5-7101-3767-b8ad-7fdcb922394e | -2.82218 | -46.66529 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f1d5636-9e65-3aba-97d8-fb7cd54b4201 | -3.58103 | -50.52966 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85463bb1-7030-3fcc-925d-937c0932b68f | -2.14918 | -46.92627 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37eb2494-43db-3959-90c2-502eaa9789ce | -6.97972 | -46.8153 | 2024-11-17 04:29:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16a46cab-4913-337e-b872-ff539d2054ff | -6.3742 | -41.55254 | 2024-11-17 04:29:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9dbc1b90-f145-3032-ae31-29eba1015f2c | -3.33887 | -46.42431 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0cfa479-65ce-36b9-bc99-4b1adf7c0be8 | -3.10932 | -54.6837 | 2024-11-17 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eeb7218-ca25-3eac-a475-a83356c82a37 | -3.13237 | -45.90067 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86d3c6bd-54d9-3fd7-b734-6581b0ec16be | -2.62823 | -47.91703 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f45a14fa-7f8c-391b-ba78-8df571b0e537 | -2.5847 | -47.56886 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5a1d206e-ca2f-33de-86ff-d30379ff9738 | -1.62624 | -48.68244 | 2024-11-17 04:29:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e24a97f-1fbc-3b8c-bcf4-ddd88ce6a478 | -1.36758 | -52.25245 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3efaab34-5b1c-322e-81ad-c32eecf16d3a | -1.79399 | -48.44239 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e629b4f-fb43-3769-ab51-9db9529ef1af | -1.5179 | -55.36935 | 2024-11-17 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2e5b64e-3c06-35ac-bedd-9b8bc491278e | -3.95184 | -46.71809 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16bf7912-56f7-3aa1-92fb-a065bc55949b | -2.15704 | -46.39927 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d8c540-fa77-352c-9909-ce2b8527fcfa | -2.39319 | -47.94157 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f57e6dd-07ff-3da9-a2fc-b22f5256a295 | -5.21796 | -46.08837 | 2024-11-17 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da73a054-bd79-37b0-9f12-a6de7713f5a7 | -2.14629 | -50.70327 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d93dd48-9eca-34db-9234-0a7bdb7f73af | -0.88201 | -51.72507 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be9811da-2a0a-342d-abf3-6bb61221a844 | -2.65129 | -46.84305 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8380cf36-03c1-3316-bdf7-a9255ac2933f | -4.44743 | -45.90886 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e9119c5-beb0-3f62-97b2-e53dd8c7847e | -1.32614 | -51.86824 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6dd2eb74-543b-3045-9159-ced541cb3f23 | -2.07561 | -48.52658 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89d90fe2-6ec6-351f-90f4-144f93f54d33 | -3.71293 | -51.84681 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f497e8d0-96af-3603-8cfc-08390f90d10c | -2.08565 | -50.49557 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bd29026-d813-358c-8a26-cd27c449e01d | -2.46356 | -45.6127 | 2024-11-17 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f1aa0ba-f711-3ca4-99ad-a3610b42d97b | -2.70852 | -53.17923 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d04842-f363-3a8f-8c22-5b9dbfe7d128 | -2.17556 | -48.55342 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b78f3ce7-34b2-322b-a744-b19297cda01c | -1.91241 | -46.57222 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3dacba50-8d10-3dda-b503-85bdd7a08407 | -3.9353 | -46.17268 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af8b0efa-ecba-3df8-9714-9755025c2248 | -3.71135 | -51.173 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README47.md)
