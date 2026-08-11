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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03a8e876-403c-3102-a5cf-9cbb7cf7d992 | -18.01187 | -44.37109 | 2026-08-11 04:36:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5afff1f-89da-35e7-968b-e4f69c6fc9dd | -15.87809 | -56.25816 | 2026-08-11 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 548a59ca-571a-3305-9769-e91b65e5980a | -13.86012 | -53.79936 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ddf60d62-a879-36f3-a1a3-6d403eb4f777 | -14.09894 | -46.36201 | 2026-08-11 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bf4c0da-f8e9-3ec3-8dc9-8cab62fe5f05 | -14.44755 | -45.67588 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c88d44a8-780c-3c0d-801e-3672935d86ba | -14.45068 | -45.68119 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5846d775-b576-3cc5-aa81-a4d6059b1312 | -13.42943 | -57.05145 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5265e46-07c1-3f35-8523-782f73b769ab | -15.77454 | -46.79009 | 2026-08-11 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f7415d-106f-393b-a9ce-b071dc9f3c72 | -14.40428 | -53.39339 | 2026-08-11 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48b9f305-98a6-3b43-8a8c-8de0b567037f | -19.00275 | -46.17762 | 2026-08-11 04:36:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fd4cc49-7fe7-3e1e-bd49-59d6db1b412f | -17.45423 | -48.90644 | 2026-08-11 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e89e6920-c24f-3eb0-be4c-24d4a7664fee | -14.27733 | -45.30727 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c6571cf-aa8b-37a8-9ff4-1c38800c966f | -14.76435 | -56.37135 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b5a53d0-dab3-30c0-9c18-79cbb40ad136 | -20.09355 | -44.31386 | 2026-08-11 04:36:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d25e54bb-ea50-3c47-9be3-a7b55eec4b04 | -13.85932 | -53.80393 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c9071ca-a519-3977-bb3f-c84cc837b1e6 | -15.06215 | -45.32769 | 2026-08-11 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 980b6734-5736-3e73-9847-766d9c815705 | -14.45631 | -45.69652 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65271e50-d9d3-3b54-97dc-b79792042ba4 | -14.40352 | -53.39782 | 2026-08-11 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bc195d3-5d05-3647-83d6-d638e73ae36a | -15.77029 | -46.79396 | 2026-08-11 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c148c07-e688-3475-90c8-fd44d7cfb1c9 | -15.04551 | -46.55931 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac6ef80d-4527-36cb-a26c-7e956d63d3bd | -13.87632 | -53.77337 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94f4259a-7ece-35bb-9222-111796e062e8 | -14.75997 | -56.37051 | 2026-08-11 04:36:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b744de82-ead8-3b21-b9a8-37603adb9431 | -14.27799 | -45.30235 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a82899f-e772-34a0-b1e4-b0db8ff9e517 | -13.43661 | -57.04967 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7bf683a3-64ba-36ca-a673-8e430635a176 | -14.12059 | -45.63983 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3a12559d-ccdc-3d92-b9af-4b76d1ee47bf | -18.42399 | -45.4978 | 2026-08-11 04:36:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1e1fe5d2-e155-3288-8f45-642431ae34a0 | -14.50061 | -49.29311 | 2026-08-11 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f67d67d-6a18-30d0-8132-98d300fc9d00 | -14.12818 | -45.6124 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e943049-e989-37fc-af5c-e4636019539f | -18.00385 | -44.36507 | 2026-08-11 04:36:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9d86917-56fc-3246-8eec-fd833a41a999 | -14.45944 | -45.7018 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c87bfdf8-04d1-3237-80dd-9323372569ad | -14.46765 | -45.69818 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75a735df-269d-3221-8d89-a765014805d2 | -15.03514 | -46.58011 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7143c26a-ed64-3ba5-ae61-e5fcc52bdf6b | -14.46894 | -45.68873 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6fd4eb1-5210-3716-844b-fdbe6c03e5ab | -14.29069 | -49.28805 | 2026-08-11 04:36:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e84c0a-4e02-3651-be60-f396ccafcdd1 | -17.04075 | -45.90009 | 2026-08-11 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 508d541c-2de6-3bf7-a888-111c683c32cb | -13.8647 | -53.79542 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd5c0473-5346-33bc-bcbb-202d464be9a2 | -17.44691 | -48.90915 | 2026-08-11 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2865ffa8-0bb5-3f6b-92c9-5228984dd7e1 | -14.62968 | -47.66331 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fde05ebf-8532-3eeb-a26c-e781c18f324f | -14.25549 | -51.96833 | 2026-08-11 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3db8c9b-beef-351b-878d-baa632b73d1b | -14.46451 | -45.6929 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d4bc7d0d-3ea1-37a8-be5a-0953dc0e7185 | -16.70615 | -49.15116 | 2026-08-11 04:36:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 855d9226-fa93-35bc-b1c5-5bfc9f541dab | -14.4576 | -45.68704 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ca68167-4b48-3158-b3df-fe6e3d162bc2 | -15.7774 | -48.71078 | 2026-08-11 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69225862-e7d5-33e2-87a8-4cbae8da2cc5 | -15.77516 | -46.78569 | 2026-08-11 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df298515-38c4-32bf-adae-7542d819ff9a | -13.43758 | -57.04462 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ae36347-57d4-325f-b47f-4334f3d81778 | -15.77091 | -46.78963 | 2026-08-11 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9d11736d-13ef-39cd-af9e-178b7855e7a2 | -16.965 | -47.73613 | 2026-08-11 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c90285c2-d18c-3f6b-ad03-278361da88d2 | -14.61592 | -47.66106 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ced7df9-66c6-3986-bef3-89fa454bf4b3 | -14.99948 | -46.59662 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64226de5-f951-3030-b6af-a0548f62e7dc | -13.87606 | -53.79742 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5073a97f-b11d-3756-a41e-b3b5c2a0c18b | -13.43881 | -57.0532 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a293000-47de-30c6-b1e7-f7857a6cc084 | -14.45502 | -45.70597 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a17dbd0e-f22c-383c-b5f6-e5cf6c520936 | -15.76667 | -46.79345 | 2026-08-11 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e8eacf8-37d8-3123-9930-d3427ab1c3ce | -14.12123 | -45.63517 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7759e22c-d359-39a3-b42b-11f8c209e650 | -13.8273 | -53.89757 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c2142c2-805a-3024-9333-aadce5f088f1 | -17.89157 | -43.89503 | 2026-08-11 04:36:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a52d1c9-be34-3de2-b492-e9f98711308b | -15.01827 | -46.56843 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 805f6487-8858-3c04-98ec-60985b689f57 | -15.00311 | -46.59713 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fceb62c-8686-3f82-a92f-eb34e5632201 | -14.45566 | -45.70124 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d5ba63e-67ea-3091-8e10-0a6a31edcd44 | -17.45761 | -48.907 | 2026-08-11 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f55d5c-6936-31c9-a9ec-0b5137b8ecc4 | -14.45004 | -45.68592 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 478a834c-10ce-3113-9804-e7f141a2c73a | -16.48644 | -54.65688 | 2026-08-11 04:36:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4546dc9-16b5-30ae-8011-4b9f4c1b5a46 | -14.46829 | -45.69346 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44433f79-9e02-3e2d-93e8-06738c25694b | -17.89764 | -44.45933 | 2026-08-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e41dd52-0865-38c9-93a0-c01d061f7dc9 | -14.45879 | -45.70653 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe134e36-6260-38f8-8ccc-342b78af0e25 | -19.00222 | -46.17551 | 2026-08-11 04:36:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b83bc9d-bb2d-34ee-a9b4-0dd8e0ac13b0 | -13.43037 | -57.04631 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fb197d9-eec6-3675-8d92-0c06e09ffd31 | -17.73149 | -46.2133 | 2026-08-11 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce792b78-7cf2-3ad7-b32d-3482c4ac01e2 | -15.01762 | -46.57303 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b2d0ab2-aa7b-32fe-9021-10f8142c6dfe | -18.42802 | -45.49834 | 2026-08-11 04:36:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ba82420-14f9-3d74-a9f1-5607c1bbc1e6 | -14.09531 | -46.36148 | 2026-08-11 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39aea2bc-d7cb-312e-8bc6-5d1185740f28 | -15.01826 | -46.59467 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 168132a0-2223-37c4-996c-f51cfe295e20 | -15.04988 | -46.52867 | 2026-08-11 04:36:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ec14657-4fb8-30c6-886b-6dd18b5837e8 | -14.47142 | -45.69875 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a03458b5-4cd3-3987-8795-a70242fe959f | -15.05156 | -46.56891 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86514d06-8aff-385e-b1d1-65da0fbf2286 | -14.00814 | -53.98238 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d03ba82b-8ec4-3514-8815-69c6e9202e72 | -17.99844 | -44.37346 | 2026-08-11 04:36:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b8c6c1b5-622e-3dc4-b75f-cf734021b5f7 | -14.45695 | -45.69178 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27dca5be-ba1c-359d-9131-6b0ec4611ed0 | -14.4973 | -49.29256 | 2026-08-11 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b9b89d67-a72e-3bd9-ad74-bbbcd77d3836 | -13.8685 | -53.79604 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8402119e-fbe4-3d27-9252-66befab8cf00 | -18.41948 | -45.50092 | 2026-08-11 04:36:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f6e4724-178a-3fbd-8cb7-4edda1c97534 | -15.87712 | -56.25667 | 2026-08-11 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97756a16-6aad-3a66-a773-5b66ce3eb1f1 | -15.0419 | -46.55864 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37bfc98e-f9e6-3a00-9fa9-a081e05d25fb | -17.03755 | -45.89461 | 2026-08-11 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 037111d0-5e11-35fd-b754-b2ded802966c | -15.01215 | -46.58549 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7db23a81-f7a8-3a94-aa47-5a4b23fcd57d | -17.13281 | -51.68053 | 2026-08-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01237232-1d38-36f0-9a14-04beb947f318 | -14.49952 | -49.30023 | 2026-08-11 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9155cce1-95cd-308a-a88c-2719d755d374 | -16.49027 | -54.65756 | 2026-08-11 04:36:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 702c791a-07fa-37f6-a362-8f761d2f68f5 | -17.1322 | -51.68427 | 2026-08-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5ead6312-6201-3bb8-a8b6-58ae81d27419 | -14.46138 | -45.6876 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b69c9b3c-2038-3dec-94e9-b219c5f8a507 | -18.25172 | -42.38788 | 2026-08-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| acd38188-f780-3fde-9d8e-c4019b081af1 | -14.46387 | -45.69763 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3aad455f-76e4-34b2-ab3b-514914cfd091 | -14.50338 | -49.29723 | 2026-08-11 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 838ecaae-0123-3f1f-be8a-841a633de231 | -17.87628 | -44.45632 | 2026-08-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf88944f-5762-3334-9a50-e95de00a346d | -13.44065 | -57.04314 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 203fe585-250b-3fd6-9305-45b05e3a3c69 | -15.01461 | -46.5943 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a09dcbb5-b5c7-3196-a4ee-8bdcaecd47d3 | -13.84789 | -53.69105 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a483a5e-814b-3879-ad25-bee455794dcd | -17.46037 | -47.14536 | 2026-08-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d374dcf9-9b90-35b4-a051-64fede7db690 | -17.74938 | -44.40266 | 2026-08-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5165852b-dbc5-3c78-be12-e2607113dd1b | -15.06101 | -46.55989 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
