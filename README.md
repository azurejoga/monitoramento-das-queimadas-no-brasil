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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 935c1a17-ef9d-3ae0-a6cb-545879b02090 | -15.4409 | -56.3274 | 2026-01-16 00:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 591b65fe-4628-3514-a5e2-4b7f45a03a29 | -17.9194 | -40.0833 | 2026-01-16 00:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 6ce45d21-651d-37ed-b524-3f01f52fc447 | -15.4215 | -56.3296 | 2026-01-16 00:10:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 8b1e127f-214f-3d38-9188-610dd4968518 | -15.4409 | -56.3274 | 2026-01-16 00:10:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8bdf759f-9854-3ced-8851-cada8a902cf5 | -20.4298 | -57.8504 | 2026-01-16 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 1efe712e-ec3c-30d9-9b73-5989e78ece0b | -7.2408 | -43.0664 | 2026-01-16 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| dc2f04ad-be5a-30e1-adf5-b18fcef63cf7 | -17.9194 | -40.0833 | 2026-01-16 00:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| 110e149f-4f18-36b0-9de2-1febc34e4e8e | -20.4302 | -57.8295 | 2026-01-16 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 315578ce-9165-3ab0-aa7c-cc8b3ebd3661 | -20.4298 | -57.8504 | 2026-01-16 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.7 |
| b5deacc7-e751-379f-bd7d-f9ffaa36eca4 | -4.2183 | -48.479301 | 2026-01-16 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36b5bcfa-81a7-3858-8b18-6a8d24a1f5b8 | -7.2261 | -43.059101 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02107b73-3774-3ebd-98e3-cfd7fb0d49fe | -8.3674 | -41.783699 | 2026-01-16 00:34:00 | METOP-C | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 519ee561-986c-3f0f-afb9-152451c5a4d6 | -12.0913 | -43.770802 | 2026-01-16 00:34:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc66a42-d532-3c59-89a2-2fc9964c49fd | -19.9107 | -42.3946 | 2026-01-16 00:34:00 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a85b317-16cc-3753-986a-42891d2d1981 | -5.3804 | -43.194801 | 2026-01-16 00:34:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d475d25-ced4-3e41-84a5-5ab4275dc8d3 | -6.9868 | -42.876202 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18317c31-4fa6-3d1e-ab61-dfd30e0e598a | -12.654 | -46.758701 | 2026-01-16 00:34:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e33bf1d5-1a79-3d62-9fb7-bed53d5a37e0 | -12.6524 | -46.7514 | 2026-01-16 00:34:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f72ac5d-00c5-3e59-a999-5006d4b04651 | -4.9089 | -43.470402 | 2026-01-16 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d10c41a0-0858-38cc-b629-7ec98e177381 | -4.061 | -38.249401 | 2026-01-16 00:34:00 | METOP-C | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c62bfd33-b9ba-379c-b97e-c27e1e5d2ce6 | -7.9942 | -43.2519 | 2026-01-16 00:34:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3538fbee-d806-3f18-9b29-2d472f7b9137 | -12.0894 | -45.290901 | 2026-01-16 00:34:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebb5096-810f-3032-904d-592e2088ac67 | -12.6556 | -46.765999 | 2026-01-16 00:34:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 714f2bd2-ae3f-3793-9f61-4aa230441ed5 | -14.7767 | -45.936001 | 2026-01-16 00:34:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a938262c-daec-33a6-8aa2-669006d67c73 | -6.9756 | -40.083698 | 2026-01-16 00:34:00 | METOP-C | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0ef4bc9b-6eb3-3595-b9a6-b4484f1a89a5 | -5.0588 | -43.9338 | 2026-01-16 00:34:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8dd536b5-cf0c-3e37-906f-6671845d6a36 | -6.8862 | -42.8437 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c84ece8-19d9-3677-a9cd-037cf0616ce7 | -15.4518 | -43.167198 | 2026-01-16 00:34:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 9e944fb7-54e7-3b5f-af4b-98a17190ba81 | -7.4283 | -35.220901 | 2026-01-16 00:34:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7cacf80d-d79d-32b5-858c-7c24ddfbc502 | -14.4791 | -44.327099 | 2026-01-16 00:34:00 | METOP-C | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce4092fb-2175-3257-9857-899f61260fe9 | -6.0276 | -44.548302 | 2026-01-16 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2df7c66-1d69-3f89-b6dc-23788af2f27a | -14.7782 | -45.943199 | 2026-01-16 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 601916a0-c413-3a56-860f-9691a472df6b | -7.238 | -43.065399 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fed43d8-0f07-3acd-b38e-aba8137968c8 | -8.3697 | -41.793499 | 2026-01-16 00:34:00 | METOP-C | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bda42b43-7e66-336d-b1ef-80b482c18d9d | -4.9069 | -43.4617 | 2026-01-16 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a70a7dd0-1705-3a36-bc4c-523512a14d82 | -6.6443 | -43.436199 | 2026-01-16 00:34:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f75d99ff-2afc-3219-96a1-b32bd7cf50a7 | -12.0896 | -43.763401 | 2026-01-16 00:34:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 60d77839-c983-3941-a37d-9bfad959eae5 | -7.2241 | -43.050499 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 173f4d0e-9766-3b44-a8e0-a0c0a8aecd49 | -7.2359 | -43.056801 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e49fb0fb-e439-3bc8-978e-34224c0abea7 | -13.5957 | -43.357498 | 2026-01-16 00:34:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 44672dbc-bb29-3bbc-9dc1-b5d9be898c7f | -11.8367 | -49.192799 | 2026-01-16 00:34:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1407f2c1-f89e-37d2-946c-f6ef955beb09 | -10.7884 | -44.429001 | 2026-01-16 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c26ba6d1-d1b0-30c0-88a9-50be0be19394 | -11.8386 | -49.201801 | 2026-01-16 00:34:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbb50ae1-49e7-38e9-bdff-604a006765c8 | -4.9398 | -43.426601 | 2026-01-16 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5504d6c-25f4-389b-9465-b6373409634c | -6.9945 | -42.865002 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d416824-c8f9-35ae-8d75-ffb53174a5c9 | -5.0569 | -43.925598 | 2026-01-16 00:34:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 777be93a-1ebd-37bd-8a6b-ff70a9429798 | -10.619 | -44.633999 | 2026-01-16 00:34:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df949c38-a22a-3f63-8db0-69992f0ee4aa | -8.2803 | -48.184799 | 2026-01-16 00:34:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d571f13f-9d7a-389b-a3b0-789776d5861b | -4.9419 | -43.435299 | 2026-01-16 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac6adfbb-c6fe-3f3c-b4d7-0d4bed51db11 | -4.2167 | -48.472198 | 2026-01-16 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31edfe84-b498-3024-8caf-b1e7557d19fd | -12.0909 | -45.297901 | 2026-01-16 00:34:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40cbf7f5-75f2-3411-9622-89df97870cbf | -6.9966 | -42.873901 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 591bda6b-5fea-3225-bc35-edfc432ecca7 | -13.4349 | -43.866798 | 2026-01-16 00:34:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 771120e0-8d9c-346d-b5d0-e46c5f98e022 | -12.9228 | -49.490299 | 2026-01-16 00:34:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0e9f66f-91dc-3832-b8d5-01dbf724daf9 | -5.4536 | -46.169601 | 2026-01-16 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9156848c-0819-3b15-8ec2-db77dc9c9034 | -19.909 | -42.387199 | 2026-01-16 00:34:00 | METOP-C | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4877bcf5-8dc6-3e5b-88ae-19a8fd212a31 | -7.2339 | -43.048199 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d65c829-779d-3295-a348-e2c2323d583d | -6.8841 | -42.834801 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db6cfc7a-d6e4-3e41-8f58-b035f55a2337 | -14.4807 | -44.334202 | 2026-01-16 00:34:00 | METOP-C | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6b9aaf5-d450-361c-9ecd-ef16481647f1 | -6.9847 | -42.867298 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ae9f5188-f6b6-3edd-9bcf-51e3b45153cd | -14.7751 | -45.928699 | 2026-01-16 00:34:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c71ce5ec-b324-3490-afcc-a8811f05de46 | -6.8883 | -42.8526 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 778a19d5-ff0d-3d83-9930-751348054841 | -7.2282 | -43.067699 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1e57989-7ffe-3516-874b-4eb9dfd0380f | -9.3428 | -44.5149 | 2026-01-16 00:34:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa1111c6-2bae-3315-aca2-9d47ccb6122a | -5.4552 | -46.176498 | 2026-01-16 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04644da0-57e3-315e-8502-3fd265ba5bc6 | -13.4332 | -43.859501 | 2026-01-16 00:34:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4586db1d-76ac-3e8d-b44e-5e78b4642ecd | -12.0878 | -45.283901 | 2026-01-16 00:34:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33fa121b-e258-3b5c-a534-582694773bb7 | -7.421 | -35.1931 | 2026-01-16 00:34:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72f4bcc3-a985-3fd0-ab7b-9f9ee647cb16 | -5.3825 | -43.203701 | 2026-01-16 00:34:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02617bdf-7ef4-3191-b60a-a2ac4146a316 | -4.2151 | -48.465199 | 2026-01-16 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2b5e66-34c3-371e-b4b4-b5376d6670a1 | -14.4823 | -44.341301 | 2026-01-16 00:34:00 | METOP-C | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bcf47590-820a-3aa3-a9c0-318cddd6d703 | -6.896 | -42.8414 | 2026-01-16 00:34:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d7de4d4-2dcd-3c0d-8f0f-82c42d728812 | -11.9346 | -47.838001 | 2026-01-16 00:34:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98bf8f4b-4198-3428-a07d-999dc4536f29 | -20.8937 | -43.236099 | 2026-01-16 00:34:00 | METOP-C | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c325847-3efd-3b9f-bed3-e04f5abe78cb | -27.66846 | -51.24596 | 2026-01-16 00:43:00 | TERRA_M-M | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f3ad9237-cb60-31a1-9f1b-cf19948ee9ef | -25.78678 | -51.28513 | 2026-01-16 00:45:00 | TERRA_M-M | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 320e564b-0150-38a8-84f2-c4f77e1c7681 | -20.72574 | -55.16109 | 2026-01-16 00:47:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 5365e25f-32d8-3feb-8890-121f1abd09a6 | -21.22675 | -56.2578 | 2026-01-16 00:47:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 11a35297-6af2-3f40-bab8-6b4c2450f6a5 | -17.61512 | -46.66289 | 2026-01-16 00:47:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d28ec414-21ac-3ab0-9ab9-240d5aa8ded4 | -19.34 | -54.17792 | 2026-01-16 00:47:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 085967b6-684d-377a-b445-e3a97c69e10c | -19.17128 | -57.54865 | 2026-01-16 00:47:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b372ab5f-3e38-335a-93fa-0f513c316c2f | -20.72712 | -55.17207 | 2026-01-16 00:47:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d4655dbd-a3e4-33c6-9132-473ef1229b75 | -21.22524 | -56.24512 | 2026-01-16 00:47:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 85a098e3-ea6b-30a1-9535-5453c11abba3 | -16.10252 | -56.75164 | 2026-01-16 00:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ea8289b4-6712-347d-8228-b67a39ad7507 | -14.47389 | -44.33394 | 2026-01-16 00:47:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 0ad51cdc-f1f7-36c0-94f3-7c843a408362 | -16.11375 | -56.7618 | 2026-01-16 00:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 073c9810-46b3-3dc0-815c-c3819f9a444c | -15.54745 | -53.2465 | 2026-01-16 00:47:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d8e9974-0662-32cd-a9cf-ad60e9330c14 | -20.73521 | -55.15977 | 2026-01-16 00:47:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 158c57a4-4f7f-32b6-82c0-bed010971e02 | -19.13127 | -57.58352 | 2026-01-16 00:47:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e389ceaf-eae8-3851-ad95-305932a3543a | -16.10393 | -56.76314 | 2026-01-16 00:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6c8cc713-386d-381f-98a7-67dfe7d0c28a | -17.61419 | -46.65646 | 2026-01-16 00:47:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b57c3332-cd96-3792-a244-afd1bef796e5 | -16.11233 | -56.75033 | 2026-01-16 00:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 7c65c097-fc06-300c-97d6-58ffe2ace586 | -22.03543 | -56.30477 | 2026-01-16 00:47:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b0fd7247-4061-3b94-9432-36f594ecb375 | -20.42844 | -57.85596 | 2026-01-16 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 45817270-b30f-3c4f-9ec8-6f5c2086af0f | -12.92284 | -49.48169 | 2026-01-16 00:49:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b3324317-6ed2-3c7d-a21b-395684efd4d0 | -15.11824 | -52.95033 | 2026-01-16 00:49:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3f3d75c9-8f4d-3631-85b7-49d9ecfb5f29 | -13.69208 | -52.59618 | 2026-01-16 00:49:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 70bd87ff-b1dd-3e38-8347-c2ba65532c16 | -12.65691 | -46.76813 | 2026-01-16 00:49:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d4c1c6e4-42d9-3b36-8a96-270d2ccaefb0 | -12.92448 | -49.49041 | 2026-01-16 00:49:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f7ada94d-a6e3-3e11-a370-775c9ba94d47 | -11.84081 | -49.19633 | 2026-01-16 00:49:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |


[Clique aqui para ver as próximas entradas](README2.md)
