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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3d57756-a6a4-39d8-8056-7d4cc2c8c8b3 | -4.5613 | -48.0358 | 2024-11-19 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2cd210a1-0a88-32c1-a610-4b583a5581a5 | -13.264 | -56.8149 | 2024-11-19 03:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 407ffd86-aad5-3ce7-aa7c-87edc7cb25f2 | -23.97 | -54.1595 | 2024-11-19 03:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| d7b6d709-6f44-3e1b-9fc9-0053825ec199 | -4.58 | -48.0132 | 2024-11-19 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4cdb9c72-cde0-349f-9e32-b31fad55e9b9 | -23.9706 | -54.1372 | 2024-11-19 03:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| 788753e7-37c7-3af6-99ea-460101db4cd6 | -4.5429 | -48.0151 | 2024-11-19 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 10273058-3946-3284-8c05-9c010ab6ae4c | -3.5125 | -50.2343 | 2024-11-19 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5ef1d6f6-65b4-30d5-9518-5c3b110bc57d | -4.5616 | -47.9925 | 2024-11-19 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1baaaf90-a36e-3adf-86ae-fbc5b5183e55 | -23.9506 | -54.0968 | 2024-11-19 03:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| fd66be78-77d9-3392-99c6-daed9807bc85 | -4.5614 | -48.0141 | 2024-11-19 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 01403aa7-6339-33c1-8418-b794b47534aa | -4.1059 | -43.5843 | 2024-11-19 03:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2f0443e2-972d-3213-b0f4-ba47a995bed6 | -1.5869 | -53.7933 | 2024-11-19 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9b37967d-7fc1-3f98-abe4-f1e126421617 | -3.98724 | -49.91653 | 2024-11-19 03:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dde04f1-e637-3dd5-94a0-3effcb6e4682 | -4.10689 | -51.05972 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7e39b5a-3436-33c1-a18e-ee807bfb6594 | -2.31884 | -45.6451 | 2024-11-19 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fc8ac7d-e36b-3a69-a3b8-2938c06dca8d | -3.39608 | -50.10142 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d35c86f5-8e30-3074-a31a-03eca8a0e7e1 | -3.03453 | -49.47367 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a28b214-6b8a-328b-a79b-689dd0449a97 | -3.38109 | -50.3358 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c84c4f7-6465-3a23-99ad-4c1e4e9b910c | -3.0426 | -49.46461 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58596160-927c-37dc-9e93-9a95f4518855 | -3.88653 | -46.93963 | 2024-11-19 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| af57dba8-5e87-39fb-a078-ad274fb2f57c | -11.76685 | -44.63705 | 2024-11-19 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4b0bce9-bb9c-3198-8743-4c49bd6becef | -3.51197 | -50.23422 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3aee9bd0-2f71-32d8-9fa8-3351bbd5608e | -4.57877 | -48.02267 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a372cba3-ad61-31a7-b6d0-c9a3c131c26e | -5.98154 | -45.35852 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5c145ab3-6ce6-3891-b04f-3bc69a2ab946 | -4.57109 | -45.64759 | 2024-11-19 03:53:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4da5e82-d065-348e-9715-0d0126db0cf5 | -6.88106 | -45.48957 | 2024-11-19 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81d6f168-7502-33f5-b17f-ad3fa839f4fb | -5.71319 | -41.64172 | 2024-11-19 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7307f959-9f46-3e1f-9d7c-1b0790239d31 | -3.50636 | -50.22722 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 34a10935-3b13-39f4-bbd4-f4336b4f60f0 | -3.32644 | -50.49148 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42055f59-1926-34d3-9c6c-2ab7928e2a8f | -5.65466 | -45.20235 | 2024-11-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9210cdc2-a9b1-3343-8171-bf837524dc70 | -4.39137 | -47.7773 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad7fad1a-efda-3fe9-a679-e472303bf05b | -10.81875 | -44.36642 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a298c45f-7d37-3fd7-ade4-ed804d75c86f | -5.95573 | -38.62897 | 2024-11-19 03:53:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b33a43f-2fe0-323a-ab5d-8aeee3c9b573 | -2.69024 | -46.23 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbd9831c-8bbd-3fe2-b3d9-963df559c3c8 | -4.82094 | -47.32196 | 2024-11-19 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de611ba-6ece-3993-b7b2-eef31ea8609a | -3.91761 | -42.41669 | 2024-11-19 03:53:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 17024035-8bd2-307d-b049-ae1ca7a033f2 | -2.67935 | -46.23133 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23e9b50b-d4b9-3cde-b1ca-5dc64c558d6f | -6.04735 | -46.60342 | 2024-11-19 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f46b8872-d476-3225-a9d0-3f737b7e3eee | -12.68989 | -43.37735 | 2024-11-19 03:53:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08e3c83a-2bdc-3216-8c0c-8f30e05dce16 | -6.70395 | -43.95089 | 2024-11-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 664da3d9-fb32-3203-96c9-06dd1a03fb06 | -3.34159 | -45.36714 | 2024-11-19 03:53:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 390e6eea-eadf-3b2d-a817-6cc0edd7fcf5 | -4.38212 | -47.76384 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbcd5a25-8ddd-325d-af96-a94e1ee59c4c | -10.54428 | -44.67345 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 679d4687-b12c-3f89-9417-dd78191986c4 | -4.54741 | -48.02113 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5f39519a-f974-31f7-ae00-1d0709b8f769 | -13.00713 | -40.18385 | 2024-11-19 03:53:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e65dd95e-4bf3-3692-9187-a63c5804eb3a | -5.70515 | -41.64485 | 2024-11-19 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7c4b79bc-7994-37ab-a06e-147fb1a8c9a5 | -10.78366 | -44.33091 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e944398e-cc17-3982-be64-2c497d0c75cd | -3.47661 | -48.25418 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35f6cf39-1e1b-3c25-89ce-e2dd490d96eb | -2.68557 | -46.22597 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb8a502-d38a-3e7c-8f83-4995762ad2e7 | -10.75871 | -44.3555 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 090857cf-bae0-380a-8a8c-62d80c99abdb | -11.76283 | -44.63632 | 2024-11-19 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29f5f2ac-5ca8-3eb2-bf02-e89a0582ccca | -5.97142 | -45.36194 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a15e8232-8df0-320f-94f2-45061a6241d6 | -3.32387 | -50.49199 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d333c00c-f946-3c75-9d75-4b9c1a947eb7 | -3.39515 | -50.10698 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b26796-b90b-3599-8271-3b41578ebfde | -2.48713 | -49.02819 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa10fe15-634e-39c8-9fea-f36d0d7351fe | -4.99274 | -44.33825 | 2024-11-19 03:53:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3cc511af-be95-3a78-b005-1a0fb9aa3c98 | -12.64476 | -48.82454 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c2284f-b9d0-3575-8a53-4fe8b394368f | -1.39835 | -47.45625 | 2024-11-19 03:53:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b004b339-ac2f-3c40-af27-a3dc3e5bb30f | -2.68608 | -46.22287 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57ba2d26-ba27-30d7-99bf-95b7f9f3a23e | -4.57238 | -48.0257 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 991523bd-64b6-34a0-a49b-8b9d603c1f7d | -3.04372 | -49.4704 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e47305c9-d3d9-34db-a377-19932f131cdb | -6.98468 | -39.65745 | 2024-11-19 03:53:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f9107af7-4553-3599-a422-efe27ca830e5 | -4.58015 | -48.01484 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d600fc88-ba2f-35d3-aae3-443b56d346be | -6.88187 | -45.48491 | 2024-11-19 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f5fe711-6fef-3507-8480-cbfea48c5a52 | -6.04682 | -46.60643 | 2024-11-19 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15fe5b43-e007-3c53-af6a-f5e8a3700616 | -10.41756 | -44.48786 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2dcafd6-d0e5-34db-b1a8-0b0d87e71a23 | -4.57277 | -45.64565 | 2024-11-19 03:53:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e042161d-33d5-32e6-99ec-05a70201c30c | -9.69077 | -47.86876 | 2024-11-19 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc42b74f-6143-3841-a709-cd36600066b8 | -10.41415 | -44.48343 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3764e47e-2abd-3d34-8c8d-bafb8d56d847 | -10.97391 | -44.53395 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7340d9b7-fe73-3494-a823-ac29d8ffff35 | -3.3332 | -50.49252 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 448e70d8-db86-3ed1-aecd-f54606d18926 | -10.97454 | -44.53034 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 802317c7-add2-3f48-a10d-596d181b861b | -5.58339 | -44.87518 | 2024-11-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d53cece8-38b8-3b2d-8678-8086c546f9ae | -3.29662 | -43.54571 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63e32a43-66c3-3d57-9ea8-a7c0744533f0 | -12.64078 | -48.81701 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6589183f-81e2-3fba-8514-13dcf97a02e0 | -4.5424 | -48.01623 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bfeb62fe-561f-3fec-84d2-ec83dda3b3c3 | -3.47551 | -48.2534 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52c858c-9154-3898-a771-0605bef2ac5f | -4.57778 | -48.01434 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531d7f6c-8d70-381f-99d4-d32ea9f12041 | -10.97051 | -44.52959 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9adf908d-5718-3cf1-a337-91a75e46bb16 | -6.69916 | -43.95387 | 2024-11-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ae61202-763e-3188-ae52-af21b5697852 | -4.55306 | -48.02223 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e832f74e-40f2-33dd-b8b3-1359637e61b9 | -2.95925 | -51.46124 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13a9e9a4-bee5-31d7-97b3-69d8cea41674 | -3.88709 | -46.93628 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 467154f7-685b-3435-951a-c2330adbfdff | -11.03797 | -44.66966 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9ee2c83-64cb-33f0-8882-a28f145fdce3 | -4.65104 | -44.08652 | 2024-11-19 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0743059b-cdfb-3594-a600-a4a561266069 | -4.54808 | -48.0172 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 80c2558b-d9da-3a39-8e1c-6d5ee572e1ef | -12.64583 | -48.82094 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a1d36b4-23e1-31fe-8e5d-39c4ac73a018 | -2.31836 | -45.64801 | 2024-11-19 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90b3a128-574c-3731-9b47-c0a7f76cb079 | -3.70748 | -43.47572 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3de73438-7717-3590-a0bc-7cbcb8f11890 | -10.07167 | -44.26419 | 2024-11-19 03:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d9cb70-02bd-35ee-81a5-758887dd438a | -4.55107 | -48.03392 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 674f518f-be15-32c1-9dbc-206f9f76273f | -12.45337 | -43.57594 | 2024-11-19 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69053ffe-6f3a-356a-adf9-4b680c77ba9c | -10.82275 | -44.36716 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f926b8c-d82b-34f2-aa7e-8ba955d3b3b2 | -12.64997 | -48.82555 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc664187-a84d-3b94-9485-4038db6651ee | -12.64537 | -48.82127 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a420817-0bbc-39f2-ba95-d469c3dffde3 | -7.51524 | -37.21267 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8973086-3e35-316a-abef-f883ad5ab0fb | -5.29538 | -50.89232 | 2024-11-19 03:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ba43013-813c-33e2-a9d8-85149a46861c | -3.39356 | -50.10633 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58206ad9-b788-3d71-ac83-df02d91c2366 | -10.00693 | -47.5581 | 2024-11-19 03:53:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5558db-6804-30d9-b2a7-eebe1fcb73fa | -5.29647 | -50.88636 | 2024-11-19 03:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
