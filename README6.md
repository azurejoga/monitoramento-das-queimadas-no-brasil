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
| 85515308-0750-3171-bb02-becc57a74672 | -8.58141 | -44.32537 | 2025-07-22 03:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e621eaee-2c68-3344-889c-a9deef58ba82 | -9.55831 | -40.60213 | 2025-07-22 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 37ca5564-6d4a-3fdf-87a0-0aa157fcd5c9 | -6.20406 | -44.38911 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43e7a825-d8fd-3a65-a8b5-e9d3bb713f8f | -5.51354 | -35.58319 | 2025-07-22 03:38:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 198941ea-9f4c-32d5-937c-5a7f6df18f43 | -6.19541 | -44.38865 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7a843e2-86dd-3c91-97f2-b5f99fbcf149 | -5.69109 | -43.67691 | 2025-07-22 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69072ee8-c0fd-3dbf-bb6d-e80dc4f1d693 | -6.9781 | -42.80806 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49a05c22-4ee7-3677-9bc1-2e6cf35d642d | -6.71163 | -38.96347 | 2025-07-22 03:38:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9758e0e7-35a9-355d-993f-6c10e6757532 | -6.97396 | -42.80051 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac24e714-47f3-39a1-a0f4-2974c975894a | -6.19386 | -44.39733 | 2025-07-22 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4cdab95-7bf7-3b97-91c5-23888d6fe445 | -4.37881 | -43.2848 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11818ae6-f857-36c0-98ef-eae37f5522a6 | -6.84005 | -42.73193 | 2025-07-22 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b684f891-f71c-3176-a139-8a1c212ac61e | -5.5615 | -45.22123 | 2025-07-22 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b19f2345-d1dc-37b0-920d-10b6275a652b | -8.5211 | -43.3063 | 2025-07-22 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ae40a29f-c30d-3db2-bdea-0a3b152465f8 | -9.6254 | -40.5875 | 2025-07-22 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 3b021f6b-d49c-3ea8-941d-022d51ce37aa | -11.7317 | -48.1849 | 2025-07-22 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d79d882b-35bc-3f5f-b201-a8909893c415 | -8.5022 | -43.3085 | 2025-07-22 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 45ed4291-e121-3921-86ee-4bc27f69b22f | -13.6934 | -45.67667 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b0711152-0c6b-34a2-874b-0056b61e8cdc | -12.65374 | -45.05624 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d0eab40-bc82-3b5b-94c0-f2a49c1600ec | -18.20014 | -45.04567 | 2025-07-22 03:40:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4315d452-0f66-367c-9bbb-ca2ff4889fd8 | -11.57182 | -44.84264 | 2025-07-22 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f82cf03c-aa64-3542-9eae-05e28f431164 | -13.66787 | -46.53318 | 2025-07-22 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db119005-bd3b-3da0-a6ec-928ac115b85a | -15.61444 | -41.33698 | 2025-07-22 03:40:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b40ba57-10ec-3242-a6a1-c725d87fde21 | -12.65448 | -45.0524 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aedfbc41-58d7-3867-907c-80868007c4b1 | -11.56623 | -44.84147 | 2025-07-22 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2da3c58-4ef8-381b-ae8d-4ddff4e3fcee | -14.38542 | -47.75525 | 2025-07-22 03:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8befd569-d40b-38af-9f7b-6e0ff6aa7243 | -11.19355 | -48.61821 | 2025-07-22 03:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4a88437-3179-36f9-ac65-81053478e0e7 | -11.81165 | -44.26938 | 2025-07-22 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52050f31-7db7-31d9-8942-83fb430cfd7a | -12.65677 | -45.05743 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2285f7f7-7a32-3c3a-b2be-b9d5600a5e5c | -13.69342 | -45.68395 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 52791669-3f01-3601-8aa1-ead02f8b0460 | -18.4806 | -40.34778 | 2025-07-22 03:40:00 | NPP-375D | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 88b322f0-de9b-3b2e-b57e-2a822eaf9b05 | -11.18844 | -48.62408 | 2025-07-22 03:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d549912d-998e-33d2-b92c-1eefb98fd4c2 | -14.64317 | -46.83763 | 2025-07-22 03:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f836d20e-c1db-35c8-862e-1161f3796f3e | -12.65753 | -45.05361 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eccf36e-3e3a-33df-824f-5fafe389f586 | -11.18985 | -48.61721 | 2025-07-22 03:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d2304589-5435-3532-b99a-51895e088623 | -11.81258 | -44.27507 | 2025-07-22 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e93fd2f-ef09-3fe9-a32e-8d4f3601d53e | -18.46551 | -40.54198 | 2025-07-22 03:40:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a956e900-9a67-3099-ad78-d3a0d988c948 | -11.72718 | -48.18192 | 2025-07-22 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0b21d1d2-a04f-34cb-845f-8312e064acd5 | -11.81099 | -44.27286 | 2025-07-22 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5e68d51-a6f8-3f91-8caf-8ed0dc8b96d1 | -11.734 | -48.18335 | 2025-07-22 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1c0d4546-b8fa-3aa8-a4fb-8616674a7f94 | -13.68774 | -45.68274 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c6325fa7-30a8-3dcf-822d-b8e5f2a08215 | -13.36677 | -44.77365 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4afb590a-5a29-31f5-8498-6bd21a0dd49b | -16.69653 | -41.00686 | 2025-07-22 03:40:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dff07a3f-a836-3d1c-bde8-fda1a11de2d4 | -11.1865 | -48.6167 | 2025-07-22 03:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cab18417-f7e2-3952-97b6-60805ed0d83f | -11.86208 | -44.51288 | 2025-07-22 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b287f899-442e-382a-87ee-81874f03364d | -11.72589 | -48.18804 | 2025-07-22 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e6246989-b45c-337f-80f1-ee47d59739f3 | -17.02311 | -47.19983 | 2025-07-22 03:40:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0e75054-ebaf-37cf-b245-c63971399b95 | -18.61559 | -44.2663 | 2025-07-22 03:40:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed8170f0-861b-3470-a3d9-f411797de12d | -13.69261 | -45.68066 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 98fa2db6-bb45-383f-a427-d07ff28caf24 | -15.61374 | -41.34086 | 2025-07-22 03:40:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 15e00b0b-df7b-3c97-b8e0-b112eb527285 | -13.68693 | -45.67944 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9a8093a3-e8be-3d42-a2e9-2440c25d1089 | -11.1921 | -48.62506 | 2025-07-22 03:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27acc1c7-78f1-3bac-a2e3-f52dab639f67 | -15.61861 | -41.33769 | 2025-07-22 03:40:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e60a99f2-0732-32f4-951a-3472e7d5a92c | -11.45999 | -48.16315 | 2025-07-22 03:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a61429ce-32cc-34d5-9723-90491bbe762f | -13.65448 | -45.72299 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b15d5a3a-eda6-37d4-8b72-d72560440b3a | -18.12902 | -44.27998 | 2025-07-22 03:40:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af252bed-f564-3cfc-bf3e-a3edffe5ebd7 | -13.69581 | -45.70113 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb6f60a5-ee18-3299-b0e9-f784c98a67c9 | -12.7156 | -47.80292 | 2025-07-22 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2046dfcb-9d5b-3a11-a2c4-dba5192e4cc9 | -15.92821 | -43.51974 | 2025-07-22 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1cf1045c-e172-3191-8f9d-0300efdbe01f | -13.69181 | -45.68466 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 44de4f14-4a09-38b8-b621-8199fd29d1cb | -16.3048 | -42.98116 | 2025-07-22 03:40:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76486cea-486b-39e8-8509-035b4fc8fe4f | -13.69424 | -45.67996 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 77c6ccaa-bef9-3872-9e0c-e25f2b15acad | -12.65123 | -45.05613 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97603ede-711b-3b72-ba16-42185f2dda95 | -15.80029 | -42.02861 | 2025-07-22 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6a225ab1-b24d-3475-9afe-ffd62f94db2b | -13.6553 | -45.71889 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08b09008-e971-3c42-8cc7-2e3b8c168ccb | -13.69431 | -45.70191 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0416c152-9bb5-3f5e-88c0-76909026d4bd | -13.66019 | -45.7241 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88bedb1d-2d9d-3b7c-80c1-96e83636892f | -15.8011 | -42.02425 | 2025-07-22 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea3b7415-6283-31fe-afb7-9e555318e527 | -13.64792 | -45.726 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85afcc0e-fdab-3573-8a00-664d3ba05a4a | -18.47332 | -44.35968 | 2025-07-22 03:40:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82dd6d54-aa51-3a3c-8bce-b603a4253715 | -14.20885 | -43.95723 | 2025-07-22 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 815fed54-3535-386f-9a10-d96fd4db35e5 | -11.81326 | -44.2716 | 2025-07-22 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80162e74-ef1f-3b39-9873-ae735debdce3 | -18.19511 | -45.04466 | 2025-07-22 03:40:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac8c2220-b228-35cb-8d4f-bb8de7d648a6 | -13.68533 | -45.68745 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 69e30d3b-3a36-3d70-af45-4f0777060e2b | -14.64527 | -46.83229 | 2025-07-22 03:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 296409ff-8f86-372b-bd3b-af74a19e35df | -16.69473 | -41.01664 | 2025-07-22 03:40:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31b309ad-038b-320c-96a9-208d64edecc6 | -14.3823 | -47.76986 | 2025-07-22 03:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56f73681-903e-3785-b9c3-abcf58993f04 | -12.71686 | -47.79702 | 2025-07-22 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d9f229e-b6ad-3d8f-aa30-2a2cfdd24404 | -14.39172 | -47.75695 | 2025-07-22 03:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d5da5d9-4372-32f0-bb38-59633c338897 | -18.6268 | -40.09153 | 2025-07-22 03:40:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ff32fa7c-67de-3275-9bcb-d4c595f28841 | -13.69351 | -45.70592 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3678d0db-3e9c-361a-ad78-a3e040dc874b | -17.02133 | -47.20812 | 2025-07-22 03:40:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 475ffa7e-aa14-386a-8111-f1ec9fdd1599 | -13.69999 | -45.70314 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3bce2bd-7fef-3d57-b49b-8c82c38ac5e0 | -12.652 | -45.05229 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8c869d7-d379-3997-aab8-e1cf563bb659 | -13.68691 | -45.68674 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 17d6cf52-9ef8-324a-9f85-bd467f699926 | -11.57109 | -44.84645 | 2025-07-22 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f72cfa08-dc18-3664-82dc-6718b97fc839 | -14.64428 | -46.83693 | 2025-07-22 03:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2480d6f-d2a0-3fe5-a02e-5d938ff6bb54 | -12.68554 | -45.66051 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fba566d-4ce2-3663-b1d4-da61a62dc435 | -18.37038 | -39.95831 | 2025-07-22 03:40:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37c71c78-9105-3d64-a1b7-8309d43f630e | -18.16621 | -39.64654 | 2025-07-22 03:40:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 83972a8b-9b3e-36b0-bfb2-3c6c31eb285f | -12.68637 | -45.65635 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e37d5aa-a46b-38dd-a9db-a5bade529220 | -18.1957 | -45.04177 | 2025-07-22 03:40:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2dbf1005-d369-31b9-b7b8-1079dc155101 | -14.38675 | -47.74907 | 2025-07-22 03:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba4ae01f-1aa6-3bcd-a4f2-c981314810ae | -12.71311 | -47.79546 | 2025-07-22 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36dcfa88-83d3-3102-8b15-39ec7a2021a7 | -13.64711 | -45.73004 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d36abd4-1b10-33ce-91a4-2da3547ba0f2 | -17.02222 | -47.20398 | 2025-07-22 03:40:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b8b521b-441c-3173-9d46-2b395c7762e2 | -11.86276 | -44.50927 | 2025-07-22 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abcaa164-3b31-399b-bd14-16b1969c8d0d | -15.93295 | -43.52075 | 2025-07-22 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a3d8b204-814e-36d5-9881-550ad9f235dd | -14.64412 | -46.83299 | 2025-07-22 03:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18c52c78-0cdf-3b59-be2a-3a16e79d9ef8 | -13.68857 | -45.67875 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README7.md)
