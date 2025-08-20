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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| debe154b-35d1-3f4a-91d3-3bab0cf44752 | -5.10815 | -43.15542 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 723a7a23-1a4f-3160-9653-95686a2399f1 | -4.72248 | -42.4505 | 2025-08-20 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7d33530d-a7a8-3555-af6d-8cc721747078 | -7.1272 | -44.64069 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 703953ad-fa1b-3bbf-8ff0-4b172996f301 | -7.21074 | -43.97286 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5a9b47c-3b18-3fef-be78-52af4576dbd0 | -8.78888 | -45.47826 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f48665f-b71e-33df-b61e-0b7dee494ffe | -7.60264 | -44.39518 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19e8eafa-9c83-3aa4-b86c-e98f82e67071 | -4.60399 | -43.32337 | 2025-08-20 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 632abdf9-a14c-3e27-aab0-3c9b851c3b24 | -6.76847 | -44.34524 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccb7bfb7-7d53-3d1f-a040-87c46e696c84 | -3.27065 | -49.14734 | 2025-08-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cee34836-43f4-363b-814c-eb1aa5a938e7 | -4.91325 | -43.23448 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 565562a2-2e35-3d72-b1f8-4aa4a835b6af | -3.98143 | -43.24242 | 2025-08-20 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| caebabd3-77f7-334b-94a3-ed26cd9ba030 | -7.57833 | -45.41647 | 2025-08-20 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ce61a4aa-61df-3fcb-a474-63538dbb8789 | -3.51252 | -48.44558 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36a59c84-b12a-34cd-85e6-95cc43d7605a | -6.85791 | -43.61217 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f80d8ff6-4a48-34a7-88f9-d740bcd5ca6d | -7.13141 | -44.39383 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2313f748-3543-3a94-aff7-807e94e55940 | -6.17023 | -46.14675 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 395c6465-6704-317c-8b66-3d8718617682 | -6.05397 | -45.05423 | 2025-08-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88321be6-0f98-3f97-af5e-3579f9d8cf62 | -7.2895 | -43.68032 | 2025-08-20 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab7ddb1b-14af-30f2-8394-fcb78b8368bd | -7.63715 | -45.28828 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2cb2479-deae-3005-8959-faed3a845887 | -5.42382 | -47.16139 | 2025-08-20 04:08:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3f1e59e-2a57-3225-a631-ac98590943ad | -8.80244 | -45.44171 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 889c5225-453d-30fe-8878-035f179fd271 | -5.64872 | -43.376 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cb98937-aa6e-37d9-9b73-b006d802a92e | -6.49215 | -42.98188 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1c11901-a9ff-3eaa-979c-21deb5fc5141 | -6.68081 | -43.68653 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fcd354f-deab-3c5b-9c3d-0b10a3535f0c | -9.14984 | -44.38663 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 064424b1-a989-3c2b-8cc0-187e7d91bfa7 | -7.63296 | -46.21996 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 979116f0-0de2-38d9-9580-67af3b512b67 | -7.69872 | -44.01918 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 419b4446-1e56-37a7-9917-1161c7d45162 | -6.3204 | -43.61352 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 387f1fe9-34c6-3657-b5a0-1c98d1fae001 | -6.86988 | -43.11521 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb9ebfab-3147-38d8-a6df-72c21e921a7f | -6.10035 | -44.37211 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e03be19a-066d-343a-a8df-268464418bd6 | -6.94806 | -42.87595 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 642abdcf-44d9-3866-9225-bb6b64f223ca | -5.67096 | -43.37152 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7adf9467-22ea-36c8-8206-ce5a129c5c5f | -7.64722 | -45.27251 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66d78dff-683c-343b-94cf-44b57d5184c5 | -5.65673 | -43.37308 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a524f1da-ce90-3b2e-93ab-4ed471dfc914 | -4.91667 | -43.23503 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc243a1c-bbfc-3578-9c42-e0400889060b | -3.97908 | -51.06507 | 2025-08-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3a5cb6a-4604-3cbc-8fca-4e0f53903f5c | -6.52882 | -45.47357 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af8fb16d-beee-3116-ab51-4b1914304617 | -3.82013 | -41.57198 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e7f5154a-e503-3972-a4ce-0b54f0462c93 | -7.24982 | -50.17845 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a90cceb8-8bd9-343f-aa46-10a054250591 | -5.63946 | -43.41253 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b368bf22-7db5-3304-8d92-7dd6efc7e7da | -6.09039 | -44.41145 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f5598c9-1d1f-3c77-8e3b-8a99fc45add7 | -7.65002 | -45.25566 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 676c1289-405e-3a50-868c-2e860dcb042b | -5.80509 | -46.55101 | 2025-08-20 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 340f02ab-2051-3003-a171-7ea2029359a8 | -5.6678 | -43.50027 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11a4e622-50b8-31ab-b935-58b24025ff8c | -7.66454 | -45.2579 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 59d0bde4-5161-3b45-b977-f3bd9d36dec0 | -8.34597 | -46.30035 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 941f4d98-8907-399c-bb99-e178573ae71f | -4.31187 | -48.0993 | 2025-08-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce5bf59-b8ab-31f8-b07a-73d2e38f9165 | -5.78497 | -43.89109 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54b4492b-c284-36e5-8b84-d3cdcf00781a | -6.26393 | -52.8215 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e72e5031-0dfd-36ec-b8af-8ed76c33e716 | -5.78771 | -43.88694 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f460a8bd-2234-3279-9abe-f89e1f7abb50 | -6.03848 | -44.35074 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624815f2-7a33-338d-a15e-31525f5a3019 | -5.06193 | -43.72788 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b43df34d-0555-3b05-be04-726cfc102385 | -5.99336 | -42.82557 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d410375a-3ad2-3065-90d8-b6b991e50cd4 | -8.02353 | -47.67235 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 78eaa0b0-8e7e-3634-a20c-337ca0295809 | -5.99272 | -42.85116 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee133701-3c4e-3264-ac5f-afd1f0472f1b | -6.28079 | -43.70695 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99e87d7e-494b-3a6a-8390-0c819f99c0e1 | -7.11593 | -44.64301 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c56328e-8fbd-3698-952d-f11f921c75ef | -8.30026 | -47.62529 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c6450d79-cdc8-3dd5-a6d8-c63c4da43185 | -6.46106 | -53.38072 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c4accd3-6141-38eb-9400-bd8e3b1631f5 | -5.61237 | -43.47296 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6933f022-62bf-386c-8f80-a8b6787fd1b7 | -5.9955 | -42.85525 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41a35766-6eb2-3509-a816-ef8ea3ddedf9 | -8.02837 | -47.66915 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 87534759-6048-319f-9701-430552be3733 | -8.29961 | -47.62915 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21084123-bb33-32c3-b881-b69487691af6 | -6.46279 | -53.37094 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7483178f-f4bd-3bca-a721-5110c50f4011 | -6.02861 | -44.39001 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca638d75-1b8a-313c-a552-1044f0739018 | -9.52453 | -42.93599 | 2025-08-20 04:08:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 33153e53-a180-30dd-ad69-5c0202a0076d | -5.61296 | -43.46925 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 856c35f9-70d9-3f54-ad19-974d11c03055 | -5.93173 | -43.49627 | 2025-08-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c797ce98-602b-3d9b-838f-107493735133 | -7.30299 | -43.70512 | 2025-08-20 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 949e756b-c2be-3ec4-a497-96fd2e61c2fd | -5.11645 | -43.21317 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de404ef2-19f0-3445-adcb-ca41f7a58c20 | -10.27688 | -46.77277 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 75304d2f-27b7-3275-bab8-42324fd07ab6 | -8.02705 | -47.67685 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5012d4ff-a86b-3bc1-a315-a9fcfc008fb9 | -10.27385 | -46.76749 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69ba62d0-080b-3886-8af4-eee7c24175bd | -7.81443 | -46.88927 | 2025-08-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9714f2f3-d064-3e34-9366-7e5a1cf942d2 | -7.64219 | -45.28036 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce8e446-9096-303d-b3e4-6ef1b9e4c350 | -6.85568 | -43.60426 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31420f4f-acdf-3764-b8c3-e7b956467d67 | -9.25175 | -44.49584 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86cd1bb9-720f-3fed-a339-f624c4299132 | -6.50636 | -43.43583 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f527e5c0-7e66-3820-bb8c-efc158f7c407 | -7.20609 | -46.24144 | 2025-08-20 04:08:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a4aaa2f-ffc1-3925-95a8-1bb1360b2d9e | -5.74241 | -39.77114 | 2025-08-20 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69f1ff4e-9c89-3ade-a7bd-3d03bf2da03b | -4.0217 | -48.06194 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42af0ff0-f5d3-34d9-9fe1-3ebbbfb98159 | -3.98487 | -43.24295 | 2025-08-20 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29d8304a-02b2-379e-8b94-f6c7581a487d | -4.07575 | -40.43633 | 2025-08-20 04:08:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 66446549-5aef-398a-9953-e423d6dfe1ed | -5.64531 | -43.37547 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965e1292-017e-34b0-8a7c-491e9957f9ae | -5.10757 | -43.15907 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c96aa3dc-6684-316e-a381-0c99282a016e | -5.99279 | -42.82915 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1340e1e7-36f1-3525-8167-d861104b1477 | -10.31612 | -46.67851 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c68968ce-9663-3063-a7ed-90d6ff0796b4 | -9.59867 | -43.79963 | 2025-08-20 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ba0cb0d-98a4-3013-a801-05dd5e8528ed | -6.72008 | -44.33322 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d75a876-8cf4-37f0-8804-ff6d8403ee5b | -7.58428 | -45.42606 | 2025-08-20 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc4c90ac-ebd9-33b3-ad28-d00a002d2955 | -5.68917 | -46.47119 | 2025-08-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a65166b-03e7-3801-9419-0ef24cc28d81 | -6.12086 | -42.72952 | 2025-08-20 04:08:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d86ca9b8-e924-30d9-9fdb-ec45bf4676ef | -8.30594 | -46.3581 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d09e87c4-7ee6-3246-9e86-f74983a95f67 | -7.15054 | -44.18984 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4217d46e-ae49-317f-b892-b70d6b78bcc3 | -8.29603 | -46.3468 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e90afdf-861e-3e6d-a2a5-ddc64237508c | -7.14565 | -44.18557 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db5e131a-820e-3cb9-8fa6-7ed05ccd8fd4 | -7.63995 | -45.27142 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed21ae6-6572-3975-8e51-4fc608c564bd | -5.63887 | -43.41623 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24817387-6c20-3de7-be80-d69d7e92779d | -5.11188 | -43.22002 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6de82372-c5b6-3642-95da-b81769b5b9a7 | -9.85939 | -44.69107 | 2025-08-20 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README11.md)
