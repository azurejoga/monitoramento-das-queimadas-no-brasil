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
| ac95af93-125c-3a20-8bd7-cc3ebf50f095 | -6.82596 | -43.58789 | 2025-07-08 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 309911ba-f67b-3705-8b48-06f417e2939e | -8.2184 | -44.93466 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 175f6050-8905-3af6-8a1e-2f0a383944a3 | -6.86553 | -44.07043 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c43dddb1-e36c-35c3-a242-9f3054f9429e | -7.23003 | -49.59865 | 2025-07-08 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 199da986-8749-3bd4-b451-be8b4155c055 | -7.10095 | -43.91565 | 2025-07-08 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbf68882-51dc-3757-be12-7ca05732a335 | -6.34915 | -46.36454 | 2025-07-08 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43e725c1-78e3-3f93-a78c-d3d2735e8bf1 | -7.10005 | -44.15806 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe114ff6-439a-3349-9c30-0e905a346ced | -6.436 | -44.80476 | 2025-07-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09656b84-9e5f-37e6-84d0-72466a8eae5e | -7.67197 | -44.35009 | 2025-07-08 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58de648f-95d6-3480-9592-4db2866197db | -5.4149 | -46.07453 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2d70af0-003d-36d6-a964-69042d977cfe | -7.44869 | -44.59938 | 2025-07-08 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee4b22b4-d406-36cd-adb2-d0a1544371b7 | -7.19034 | -43.12897 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee485464-445c-32d4-82be-c8ffe393f1f4 | -6.93276 | -43.05621 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b6f6914-d102-3247-9c19-5878f2da19ba | -6.67873 | -43.76678 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0151ceb-01a1-3fd6-a90a-9395ecc3af3e | -4.28218 | -48.18667 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76510258-1266-38d0-8b58-a5f09ea6fe86 | -7.25567 | -43.07889 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| de282bda-962e-36be-b3c6-1fda3a8142d9 | -8.98078 | -49.18007 | 2025-07-08 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45c92327-dc3f-34c3-9c28-8631853ee6c7 | -7.58093 | -45.22252 | 2025-07-08 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7bc525b-6fed-34b5-b7ce-6a81eb08b9c1 | -6.38304 | -43.57063 | 2025-07-08 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81c7b144-d496-3b08-b473-000faea64ae6 | -5.25106 | -44.46303 | 2025-07-08 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 403240ab-4b43-35ae-8aef-cec5bf33abbc | -6.73554 | -44.33342 | 2025-07-08 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7965b7b2-2645-3328-8899-cb83d101fb0c | -8.70503 | -50.02036 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca1cac2a-127b-3a3b-ac4a-3ffb78e92dcd | -9.22216 | -48.59122 | 2025-07-08 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a5605cd5-2821-3a3e-b20b-dd2eb1d02ad5 | -6.83203 | -43.59237 | 2025-07-08 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d14da815-8f17-3989-8312-274b74acd81c | -8.06937 | -43.11811 | 2025-07-08 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 5eb8a578-371c-3b4e-9125-fe8bd2c9d282 | -4.81898 | -44.35416 | 2025-07-08 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3c0e020-4446-35e7-807b-5f5b18e5f51f | -4.2863 | -48.18734 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c8c6346-6cad-37a6-9ee3-ccb3f4f1533a | -6.69344 | -44.06116 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a054f9b6-5393-3378-9618-4edee02f2327 | -7.19641 | -43.13347 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5d170373-0723-3c50-afe3-4a61da74e698 | -8.71157 | -50.00851 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb47a446-2ffe-3651-97b5-81ab77ec8b16 | -6.34556 | -46.36393 | 2025-07-08 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70ce334f-45d7-3a8e-8856-404e557c3cd9 | -9.00926 | -48.72546 | 2025-07-08 04:14:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca2d2b33-0662-325a-a883-083be69ce964 | -6.66125 | -43.89912 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7409275-e757-3a11-9630-a53b76c2d155 | -6.34204 | -43.74493 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d16b31f-5b25-3647-ba6a-c1c0fb9b09a4 | -9.00606 | -48.72039 | 2025-07-08 04:14:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f2cb8c6-11b1-3056-b8c2-df1a6001c321 | -8.06606 | -43.1176 | 2025-07-08 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7cf75d25-e288-3d79-8857-06a62af4e2a0 | -6.49705 | -43.64535 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e28a5849-7c68-353e-b79d-ab2b12c272ee | -9.23 | -48.59261 | 2025-07-08 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 615870f6-30f5-3523-a652-d1077017c19f | -4.29017 | -48.05931 | 2025-07-08 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fefbcce4-d401-3a6b-b505-55abff8806b8 | -5.98457 | -45.36321 | 2025-07-08 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21a6a447-85d4-3ce0-b018-260533172b71 | -6.67157 | -43.7692 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 945c0124-3af1-34f9-be8b-454f613062ba | -9.29223 | -44.84145 | 2025-07-08 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbd13b7f-a3bd-3fb5-b4c3-159ae9a6a979 | -6.67488 | -43.76972 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7efabfc-38e8-3d55-8483-ba26592141b6 | -7.19257 | -43.13641 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c0678006-36b9-37a1-8395-1ceb318d21bb | -5.14468 | -48.88859 | 2025-07-08 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d53cae01-04a6-3b3e-9dd9-0ca8623d7aeb | -6.67819 | -43.77024 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2574f926-d4be-3d06-8385-dc697d99a031 | -8.06991 | -43.11463 | 2025-07-08 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 6f03ef9c-c8be-3571-9c79-70f70b8a7ab4 | -7.11056 | -44.15615 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b24f56a4-b106-3c35-a1a2-f64fdf8491fc | -7.24629 | -43.07388 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c574114e-83d7-3c82-95a3-c1880d14733a | -7.87237 | -44.91187 | 2025-07-08 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4626370c-b2b4-3820-88a8-bd57503230ab | -7.64 | -45.35969 | 2025-07-08 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 182a3e31-9a42-3c2c-ad6c-15cce2a5f6ba | -6.01009 | -44.52765 | 2025-07-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2167c717-fa49-36e0-b143-47ca68e0155f | -6.82158 | -43.59428 | 2025-07-08 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a41f13a-4632-3692-9509-d91f88f24eed | -5.23901 | -46.04333 | 2025-07-08 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e7da138-21cc-3395-aed0-befa71f9fa79 | -7.22223 | -43.11978 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d357f3ef-c6b2-35fc-9d1b-185f8d02c4f0 | -5.90922 | -42.99029 | 2025-07-08 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85e58745-458d-3689-9a94-042181ce7537 | -7.313 | -44.03807 | 2025-07-08 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 938681c6-44e1-3588-921b-44fad95a4ee2 | -8.74352 | -48.03456 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d4eba72-f649-3979-8d07-e382ccb018ca | -7.25459 | -43.08582 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2ff30f5b-518c-3fb2-bef0-bdc8b0798b4d | -7.21892 | -43.11927 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9dd85ac-5052-3ecf-a3ce-ce26fe990f4c | -5.41133 | -46.07391 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 882bea8e-2fd5-3fdb-84a1-0bfddd7c4abe | -6.01288 | -44.53176 | 2025-07-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86f01a3d-9777-37cc-8f55-e87749c7e1f1 | -7.63659 | -45.35917 | 2025-07-08 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50d5105e-96a6-381b-bdbf-c0dd878fe372 | -7.3141 | -44.03111 | 2025-07-08 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed41e00b-37fc-3814-9968-e935a579692a | -4.30068 | -48.07222 | 2025-07-08 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98b9321f-e34e-3eb4-b0bf-785d320215f2 | -6.88977 | -47.40236 | 2025-07-08 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fafa6610-8d56-370f-8d21-3c8b5b634f40 | -6.67651 | -43.75934 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ff4b03f-1d84-3a86-a29d-fee5f960a043 | -9.21737 | -48.5957 | 2025-07-08 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5d34a8b0-5a57-3ad0-a5dd-275fde275690 | -8.86655 | -47.27301 | 2025-07-08 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b78a0664-9b27-329d-80f0-c45b0afa124a | -6.86608 | -44.06695 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b4c4428-7720-3585-ab09-14800e715eb2 | -7.24906 | -43.07786 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e501e751-bcd4-33cb-89a0-0e4940334258 | -6.53315 | -43.54477 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ea4d29c-9ade-3040-909a-820f5fe34863 | -8.50172 | -44.76096 | 2025-07-08 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ae95bc7-2697-38dd-9b2a-25ce90857e1c | -7.19748 | -43.12655 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ca31d73d-e1dd-36e2-a37a-d5b4b15e0046 | -6.9366 | -43.05328 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f86d4ed-26da-32fb-baa0-5113fa0beeb2 | -5.412 | -46.06979 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79929e9b-dfbe-3304-81d6-c9f0e02421b6 | -6.85447 | -44.07585 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2ee30c-7eeb-3897-93a4-31aa2527ced0 | -6.95313 | -43.22927 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61f38ad2-569e-3115-b5a8-85d6e0766595 | -7.19971 | -43.13398 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ee4bf713-dfa2-3d76-8c43-eeab425be9d3 | -6.33874 | -43.7444 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 620772f1-872d-3204-9135-0643bcf9c400 | -6.53369 | -43.54132 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e862f81-a770-356f-9fcf-5fac8e356346 | -9.12865 | -47.59232 | 2025-07-08 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db444b03-f7bf-3db2-ab16-32fefafe3230 | -6.85944 | -44.0659 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95d1b13b-312a-3bda-98e1-a6e8512455d8 | -7.31556 | -43.8713 | 2025-07-08 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aab5f3d-01e4-356c-8b76-7117c99ee410 | -7.14685 | -44.01188 | 2025-07-08 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 828ae383-56e5-31b4-af58-78e149d12240 | -4.68991 | -47.00569 | 2025-07-08 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 598b7f6c-9c8e-3220-84a9-350c02141114 | -7.6394 | -45.36338 | 2025-07-08 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03ff5a8c-cab0-3ac1-a423-f739f32e32da | -7.2496 | -43.07439 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 765a37d4-22b3-3de6-b7b8-cce7dd149196 | -5.41327 | -46.07092 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b2d1e99e-70ef-3445-aa90-17703046db45 | -7.60785 | -37.81551 | 2025-07-08 04:14:00 | NOAA-21 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 41dc9dcc-e183-351c-8bb9-64cc6de4e2b8 | -4.68649 | -43.259 | 2025-07-08 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a530fe3-a553-33c8-9163-0cbd97ae6b72 | -6.8823 | -45.24331 | 2025-07-08 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebaea472-43ab-3b8a-90b1-a7949ed7aa39 | -9.22608 | -48.59192 | 2025-07-08 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f15bdd15-a9cc-30e6-bae0-5a0e18abb21a | -7.63879 | -45.36715 | 2025-07-08 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38f8c871-5df6-3fa5-9f07-60e4d9eafd36 | -9.22915 | -48.59768 | 2025-07-08 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b1fc9b28-5d33-376c-856e-987b5cfcc77e | -7.27771 | -44.64519 | 2025-07-08 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b640f50-211d-3070-b390-0e48bd723adc | -6.37055 | -43.65007 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c890a50c-8b4b-31c3-b1aa-48966f751245 | -7.40781 | -43.73677 | 2025-07-08 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec76aa2f-d46d-308f-b906-8e3a11aa1e11 | -6.53261 | -43.54823 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b937470-f2e6-3bc2-8059-cf0529540b33 | -7.24575 | -43.07734 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README7.md)
