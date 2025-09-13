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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bf096ce-6927-37fc-8964-9b08700b2703 | -9.99377 | -51.73415 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94ff480d-a31e-33b9-a4da-96bb056bda62 | -9.51492 | -54.63791 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 800a2db3-e374-3340-9b1c-cf9f5691b326 | -10.22466 | -48.63757 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6485f263-1e0c-3d58-95e7-862e566daa31 | -12.84578 | -47.94758 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0122426-2738-333f-a391-53db7d75e5ab | -9.23449 | -51.22296 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1eaa84a9-f9ed-3af0-a210-608eeda76ed9 | -11.93768 | -44.29643 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cab795be-63e1-35ab-9c03-70353c879779 | -9.49143 | -55.97697 | 2025-09-13 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f71822ea-e217-3b17-ac4d-3903e13432b1 | -9.91297 | -51.61643 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f738e0-fce0-381e-abc4-e2f546e4b9e5 | -15.24417 | -44.04321 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dcd7ffb-5808-371b-895d-2dc03a4bc3f5 | -14.2238 | -46.27251 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4b19692e-3c38-3688-9c8e-e06b66e93b3a | -10.70938 | -50.5139 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 044e5541-67d9-3cbc-88fc-a2e2fca396a8 | -13.22374 | -51.74229 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8807ecd8-50dd-30f0-a730-20e4063899d0 | -14.19472 | -46.24958 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 94a9bec4-cb90-3295-8d2c-861399709a30 | -11.69848 | -46.90545 | 2025-09-13 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a82cf55f-25a4-3251-a076-d21e7009be67 | -11.43497 | -43.56111 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ab3ece-2d14-3a5b-9b8b-83ce60f5b034 | -12.81578 | -47.93158 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| deeec610-b8f9-3808-8e05-d2192d711a2b | -12.10959 | -44.89774 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c85305af-1401-34ae-91a4-88a359c6bdb6 | -11.87235 | -50.57492 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b91e2d47-5be3-3b88-9e3c-dc641e657e43 | -11.07704 | -51.43797 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e203a541-b475-3ced-a8f4-eb23dc59852a | -14.18048 | -46.26849 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| cfb99808-e8cd-38e1-830b-42bcadb0deb9 | -10.79031 | -50.54097 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 7d7f734d-f0d2-3087-8098-6e0681e28a30 | -9.79239 | -48.90425 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5e1c39b-fa66-3486-a816-230d98ae25f0 | -10.50087 | -51.53698 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5930a354-0337-322c-8dc9-4b775f192ce4 | -11.4768 | -43.61483 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 360438ed-a362-31d2-be33-3bb7f85219ef | -12.9987 | -46.73945 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99904f0c-5d30-355b-a4c7-85b7e77a2576 | -14.17762 | -46.28514 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60a862b1-04a8-3379-8ac7-f7e7664591e9 | -9.2351 | -51.21963 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cb2066c-53de-3c3e-8875-086a07f26c7f | -13.08318 | -48.26111 | 2025-09-13 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e7e459c0-3adb-3157-80c2-7573708c180c | -14.4348 | -46.3983 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 827e53f9-84e6-33ff-b4d0-d448500f2d75 | -8.53351 | -47.65461 | 2025-09-13 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a36f9a08-8c72-3154-882a-81c22e80bc14 | -12.10616 | -44.85385 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0117bc60-d6fb-3291-9176-f2dc01185005 | -13.45427 | -51.78068 | 2025-09-13 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23ccde6c-7a9e-339f-9995-34c9c358656e | -11.87035 | -50.58102 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 6a352a58-31c0-321d-8cab-261cf4b49e38 | -14.23248 | -44.24938 | 2025-09-13 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae01adab-0fa5-329a-acd1-1adb3d28d786 | -14.22669 | -46.2987 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4bdce0bb-f669-36a1-8eba-e74572eab120 | -10.65564 | -46.27803 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9c2283f-5fc4-3cb1-b66f-730b36740024 | -9.51359 | -54.67886 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 490b3acb-fdd4-3c02-a69a-ffd8d3cfa865 | -10.78542 | -50.54002 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0b1171d2-e489-314c-bac2-6f3527fd2fc6 | -12.09277 | -47.57598 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e007fa51-19a7-3a42-b4af-d17951d1110f | -12.53931 | -49.15582 | 2025-09-13 04:08:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82fc2094-70be-3bc4-a2fd-83e63eb64535 | -11.78797 | -50.54732 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 11ececb9-438d-37ad-9c1b-e3ae133c8cf2 | -10.68996 | -48.66352 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfc8b11c-7efc-3440-b593-54ee170cb61f | -9.96916 | -50.30505 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09a133d6-e8ed-3bb5-ba94-c37d9ad21141 | -14.18336 | -46.27312 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 971d6f0b-f6c2-31b5-9641-17cd7840629d | -11.84738 | -50.57555 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59d6b32d-4a53-3fd8-90e1-261edac7a4f7 | -11.73077 | -44.21 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23c70e85-b050-3367-ba07-43cf538b4f1e | -12.09491 | -44.87949 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e31b9b6f-926f-3cbc-950a-69d9d1ec34a7 | -14.60794 | -46.33681 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a47786-53df-3149-ac62-999a78c4e7ce | -11.47461 | -43.60714 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1b3ffcb-e252-3bf9-99b0-586c0ea86b15 | -14.2607 | -45.0459 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aedc7020-21aa-3b50-8452-05fbe8e6dbfb | -11.43221 | -43.557 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c39fa0d-d2c3-3569-ab47-b74f4e8ec7dd | -14.43408 | -46.40253 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 015f9edb-44f6-3aea-a140-5da224b52799 | -8.42475 | -47.24494 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57cbc068-5023-31f9-aaad-698f52160a81 | -14.17339 | -46.24582 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2348d8d3-ca24-3daa-8086-9851ee620316 | -8.20278 | -45.58687 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44771b75-bc3a-3372-8482-0f7c65e3aea3 | -9.70453 | -47.52748 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4c91364-c5f7-37e5-b4f4-6d9d19bb8cdf | -13.23821 | -43.75587 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba51b507-b0bb-3fa9-be9b-9f9b84cf27d9 | -7.93054 | -46.90776 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54a9abb8-58d2-34d1-8f7c-0c3a45961fca | -12.92432 | -54.74763 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe7ab32f-3fce-311e-b386-3f9f5cc6d459 | -9.00551 | -45.76874 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 550ef3b5-6edb-3e9e-8103-73f2a3f616f8 | -10.75328 | -50.52236 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 959c8069-dccb-3a9b-9256-2b0c4192aee2 | -14.18902 | -46.24013 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6abe8fab-7955-3559-a797-9fc18c013d6e | -14.21957 | -46.29741 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 740a4211-6d0e-35ce-84c4-e94fedc06279 | -11.4231 | -50.74595 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de19b273-c49b-3c42-a01b-4cbad1b10b1f | -12.12635 | -47.59266 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5998d0fa-bf2d-3c91-964c-378f0c7ba652 | -10.76489 | -50.54177 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7b11750-1307-3c5e-9150-794f011bc2e0 | -9.90147 | -51.89059 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3323f8dd-c071-3acd-920b-c46fb7f69789 | -8.19908 | -45.58623 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6be243a-69f0-34d4-8a9e-9232ca6bff92 | -9.81529 | -48.90466 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1f2500e-3960-345f-9ae0-7995171df7c3 | -10.74556 | -50.50943 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2673752b-887e-3b7e-a368-65237f4c90a5 | -14.18474 | -46.2864 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8051e7c3-ed2f-39e0-9e55-1646bb3ff21e | -11.85021 | -50.58719 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc7e56fe-d315-3c75-81a4-a2e3286ae583 | -8.10686 | -50.19369 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76268386-80bf-3e84-b630-50395962f1b8 | -14.17691 | -46.26792 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| fa77d68c-2104-3524-b0eb-606a4a7fd6a2 | -10.76847 | -44.77162 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62fb822b-409d-3099-a5aa-d9c758ab4c81 | -10.24277 | -48.63644 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6579774c-2897-3ed2-b780-acc37529bea2 | -9.23629 | -51.21311 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1810859b-1678-36d7-9f50-da340c34354b | -10.78549 | -50.55209 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb20a29f-7d62-3aca-b25e-6f4c580b3582 | -11.98171 | -46.65935 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3116c599-a62f-37c4-97c6-b203838f114c | -14.21164 | -46.23632 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a57a70f5-c4b2-302b-9315-40bd9229628e | -13.58149 | -44.88596 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e8a9e804-fd5e-3ca0-96b5-0368bb7d1ec1 | -9.69923 | -47.53402 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38394e06-82a5-310e-824e-6f9568458e8f | -9.51366 | -54.64432 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fcdb5e15-512d-3f26-b889-c1e37d7f5082 | -9.25258 | -51.24308 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f12b2c4-028a-3464-b297-208d19470f20 | -8.96594 | -44.92897 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97034385-9c3b-3c29-9f28-c9b3537e5233 | -10.34029 | -48.82719 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcac5983-2705-3d53-9e92-a07a7f022054 | -9.48578 | -55.96888 | 2025-09-13 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e97dfed4-7a54-3bc1-a876-a8f3e4ee04b6 | -9.05853 | -47.03373 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7dcfee78-2e8f-3c6b-8273-59e6c762c870 | -7.94261 | -46.90987 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a12f814-3705-3e08-872b-23978f1d6632 | -9.03093 | -47.03959 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| d238c785-fdef-3075-b2d8-4b0e8fa32762 | -10.36142 | -50.49989 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8581561e-0c14-3d60-a295-b52920091fa2 | -13.99717 | -44.77191 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59641a0d-84d6-35d9-9806-be363be8d48e | -12.95517 | -47.99009 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04e1cdcd-0ca7-3050-b772-a7495b95458e | -10.36391 | -50.50412 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cc09ae4-577a-3841-afe3-24522ae7075c | -9.79466 | -48.90093 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 453b2af5-b061-3933-b983-ea486fe601e4 | -13.14963 | -47.1419 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8479e713-7358-3051-85fe-ad9bcdcb828c | -10.36491 | -50.49853 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5905cd66-90f0-37dd-bde7-30f9720bf61c | -14.6115 | -46.33746 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c860c123-a5c2-32a6-b872-95662d36d294 | -14.18549 | -46.28205 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| c1e1de40-ec6b-3178-9e12-b791ef815d88 | -13.26746 | -43.78637 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README57.md)
