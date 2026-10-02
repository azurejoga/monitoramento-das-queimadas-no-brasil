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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3190f68b-6dac-33d0-88c7-edcf0f3ef5a7 | -3.00638 | -53.8783 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23b08f43-0dd0-3240-9884-d69818f70f14 | -7.49519 | -54.97976 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9288d39f-fa5d-3f21-8808-eabfb5707eae | -2.8795 | -54.87978 | 2026-10-02 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b63432fd-f424-3c16-852c-30ef6bf43d37 | -7.49627 | -54.97285 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4c10097-4ca4-395f-b243-2c75506ed557 | -7.87832 | -44.18164 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f8ec4efe-f70e-33c9-81e9-db4d7da7a2fc | -8.06489 | -54.84031 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d78c04e-0910-3990-bbdb-7ef33a133bc6 | -5.87083 | -53.48421 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e05da95-4221-3240-b8fd-d3918bdfb0b8 | -7.88072 | -54.7158 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbe12984-5119-3851-a898-a6e4acc9078d | -1.61011 | -54.75217 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9db43159-e0c8-3a37-b870-fba69f9dab0e | -5.99517 | -53.53879 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ab9fbe9-8531-3f19-8d4f-f6298d65ffdf | -5.11581 | -56.01795 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6af0ea9a-5ddd-39e2-8dd2-5be0b3621e81 | -5.98461 | -55.36808 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35a89d3d-7bcd-377c-a138-c2d8a77328b1 | -6.75737 | -55.08624 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7130083e-ed7c-3a1c-b16f-85f2e821f20d | -1.25888 | -54.5589 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d413c56a-eb11-3bd5-b161-d4f07319ce96 | -3.16947 | -54.09405 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ed9f6ee-627a-35bd-933d-5df0125a5aae | -3.1368 | -53.74106 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2bf5d60b-0c91-3868-883d-9b0dc7f1afc6 | -3.18321 | -54.09643 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de0f4e45-a43f-3a6f-b367-fbeaf203809f | -6.33872 | -55.32367 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b8ae269-6b12-35fa-bb26-4c055accc640 | -6.79756 | -55.64993 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3db11998-9858-30bd-828e-5de424bd667a | -7.57638 | -55.1353 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 886cd37b-8334-35e2-9f2a-0efcd37a6c66 | -4.38843 | -54.8287 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fa1d223-08d1-3cbb-94b6-58267a5defe8 | -7.49248 | -54.99706 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6899cc32-ec17-3057-9615-6fb279cdfb8e | -2.93544 | -54.19827 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e1da1a5f-e2bd-3a7f-ab94-c2eb018481a3 | -6.43644 | -55.80088 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61093b50-4846-33ad-8346-4466f10b36a6 | -7.27266 | -55.59495 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99c4c3a3-dde5-3e82-bd57-aa12d75278ef | -2.89339 | -54.14233 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2aabe376-1db9-3496-91b6-69e368e19ca1 | -4.17452 | -56.34783 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029f1123-6eb2-35b6-8cda-62fb7a088251 | -8.23853 | -54.77617 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de36b989-69d5-326b-bfb4-f67e19fbf006 | -1.19109 | -54.21294 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 34c496f1-a9bd-39bf-b91a-ccbff41b0720 | -2.88341 | -54.87677 | 2026-10-02 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dacc6d2e-ebf4-3ba2-8835-b6c4361b3175 | -7.72195 | -54.81421 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e7502f1-c912-3059-adb9-bc8e2ec629a7 | -1.26614 | -54.55641 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37693112-ff6f-30ca-9111-9a6f13efc7d4 | -7.04239 | -55.63054 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705a2e28-1351-39ab-af62-6d362b663fe9 | -5.29699 | -55.87652 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4492916a-9b90-3ac7-b585-5f06169d73c3 | -6.24007 | -53.14156 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c563fb44-1a7f-31d0-99f4-218f1ccd6f6b | -5.86143 | -53.47915 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 14a5ecd6-e2e7-3191-ae91-ee29557925e2 | -3.29504 | -53.85701 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f59dd3-8aac-378a-b65d-1f88fe16fba2 | -11.69324 | -43.60836 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 529edab6-9d75-3c9b-8607-5dfab54a0587 | -8.55357 | -54.71982 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e23e035-2237-3e83-9c86-1038e417e9c0 | -9.75024 | -53.87804 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b210ebfe-6156-3480-a275-c615e08bc06f | -11.76814 | -43.57544 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42207f8a-5ac1-3293-bf15-604ce34992ac | -15.52402 | -46.12626 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3917bee-ee55-3b39-8bb4-87e9dd1940a0 | -8.54659 | -54.56526 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 753c1c4f-599e-38d8-bf2c-f64885dc418c | -10.82255 | -51.09663 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1451c5d5-2689-3144-989a-b551396f231b | -11.78996 | -43.57259 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e63a37f8-91f6-327b-9517-4668f92f0448 | -8.54989 | -54.56578 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d54aa037-beef-3fd6-947f-343c26bf0d44 | -8.26457 | -55.6925 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c33d0547-13f1-3023-9fe4-2de127dae1ad | -13.32992 | -43.86269 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 090d2977-1b4c-3174-a426-ee2ae254eadf | -11.13453 | -44.61621 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 571ec79e-a90f-3d4c-92bb-a27d2cc55969 | -15.25472 | -46.17019 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76e5748b-fe6b-3e67-8b0a-183a9acf85a1 | -11.68056 | -43.60632 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c74dab56-a709-3904-9f05-5d05789d094d | -10.82639 | -51.0972 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4e24641b-7fe4-3ac7-bc51-0bb28d4fc463 | -11.6679 | -43.60415 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 480ef2af-dca9-31a9-9858-248d6ab871dc | -9.65305 | -54.33892 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a82d995d-cd65-32b2-bc90-bea341fb1be6 | -10.57163 | -50.07976 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29468ca1-ca36-35f1-8045-84494d726487 | -9.68379 | -54.31549 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f3a3dde-e9a1-3cfb-a2a6-e8e02716020f | -15.31672 | -42.77064 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9ce4faf-c1c4-33fa-abaa-a3c816d2c668 | -11.13404 | -44.58867 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ef117c9-1f6a-36a1-b595-5b131632fb23 | -11.74385 | -43.57985 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 5f20bda1-0b8f-3bb1-9c36-a623ac3c4be3 | -15.32395 | -42.77327 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 10c33f31-f7de-394d-905c-9d51df627e94 | -15.30897 | -42.7826 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 721dfbc7-7088-377f-bb4d-093a658c45ba | -15.31534 | -42.78538 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 299025c1-3131-360d-ae02-9b23b1eb5286 | -15.52363 | -46.12971 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30c641e7-d970-3280-8393-2c1dd7c655ca | -11.66216 | -43.59774 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 445e8662-2a9a-3389-9dc0-50ba8f439918 | -8.26512 | -55.68898 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 002064a5-79aa-394a-90fd-67bf94121eca | -10.79936 | -48.7677 | 2026-10-02 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20bdfd90-6a89-33d6-adcd-c92ba3e37be4 | -11.25798 | -43.52321 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45ce583f-7942-36f5-80f2-146cb8c22d94 | -15.31639 | -42.77424 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 267.2 |
| c2e085d9-188b-32c1-8db6-68dec9c31f82 | -11.6785 | -43.6015 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ce31095-c85d-37b0-a376-3de32b4118fc | -10.30524 | -44.63923 | 2026-10-02 04:59:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a788ba2-ee57-34d4-a12a-bd8b1285e146 | -10.41539 | -53.76859 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 157f9427-5457-3478-8c38-6abc7eb837c1 | -9.82273 | -44.81448 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 267390f2-dd9b-301a-9504-9ac26f89a860 | -9.80269 | -54.29425 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ac2df77-3d59-3da7-b55d-cf7a5964487b | -15.63682 | -43.23085 | 2026-10-02 04:59:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 15ae697b-2739-3369-b6ea-a4f2f600a686 | -11.43205 | -43.39954 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a66e1d39-351e-3f43-9b6b-97db24218ba2 | -11.76186 | -43.57378 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3ed82e38-80ee-31fc-8872-9e4453491eff | -11.24387 | -45.19548 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a50da708-c5fc-3c67-9116-cf1ac35448ab | -11.46289 | -43.41447 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ead041ed-57ac-37af-b4b1-cf236e4058cc | -10.81555 | -51.09068 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8cc1df7-8977-3ffd-80e0-7d0bb85b8b2a | -11.31074 | -50.92534 | 2026-10-02 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3790e1ca-91dc-352e-8e9e-3f189ade9da5 | -11.7477 | -43.58425 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d5ea1feb-b837-3258-a783-0f4dc1bea6b8 | -11.65882 | -43.60416 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a69a870c-ce52-3f51-b95f-c8d078f03491 | -11.47383 | -43.43214 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f288f80b-6df1-3555-9b90-93b94a8e4b15 | -15.58692 | -44.40121 | 2026-10-02 04:59:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e6cec003-4e79-3cf4-8487-29f2e1bbce72 | -11.78768 | -43.57443 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c38db39f-1bac-30ca-b6a3-bb35a25b9a74 | -11.30684 | -50.92476 | 2026-10-02 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af81ee57-0135-3290-9fab-f68d86e1424c | -9.88457 | -50.18042 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de69eff6-da03-3d6f-a549-be36d561cbe1 | -11.67987 | -43.61258 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa54ffbf-3801-3350-adb2-c8170524722c | -8.30765 | -54.72318 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eb48e1b-029f-3c7d-9399-ee21fb75e9bc | -8.26849 | -55.6893 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e13345e-c195-3d72-b1ce-de7c9e878701 | -11.65522 | -43.60213 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04aae837-b964-3e8c-b836-152d1aba7645 | -8.23019 | -55.28617 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 961d7d64-744e-36a8-9914-166cfa9bf882 | -10.81871 | -51.09607 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25049d5e-9aee-3cf0-881b-7cd34f9e92c8 | -12.53361 | -43.09732 | 2026-10-02 04:59:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ce2d9bf5-600c-37a9-8942-a8251cbda129 | -15.5836 | -44.39968 | 2026-10-02 04:59:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4c490b28-b01e-36be-b15f-6ed994633cac | -15.31576 | -42.78499 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b0d7db0f-9b8e-334c-b2cc-0be4c1855e0e | -10.41876 | -53.76912 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 744bb847-5779-392c-8632-6ac586854d0f | -11.12811 | -44.61967 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9206ed77-3c13-3920-9324-a862fcc5f396 | -9.00315 | -54.9759 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76ce1699-3f1e-3bf7-9ccd-7d4d4a3ccafc | -12.32127 | -46.37932 | 2026-10-02 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README67.md)
