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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f519f37-6a47-391e-b34a-b16413b4b783 | -7.32686 | -44.15938 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69c4e1b0-caa4-340e-8bf4-4ce951fbc1ab | -5.45778 | -43.46716 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d08564d-c1aa-3192-81e2-ac472437e1e0 | -5.84493 | -43.88775 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2905dd5d-65c5-374d-8404-7cdec091d80a | -5.51067 | -43.87097 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c24474a3-a1f7-3814-bebc-0be41f5db681 | -5.72977 | -41.31326 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a25a84d-0d1c-3375-8ae1-7a24848ff500 | -6.58327 | -48.77276 | 2025-10-17 04:19:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 498f65da-f2da-3f29-9431-9fd242589e3b | -3.65529 | -50.26506 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf8379fc-e07b-3f17-a5c6-e576f1bb3713 | -6.94679 | -47.72245 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bddf4c78-e60a-361f-b20f-dd779d0b78c5 | -5.6525 | -42.99958 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 72c1b975-e84c-3d4c-83c1-21aae406b9e4 | -10.1047 | -44.62717 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eefca47c-086e-30b4-96c5-942f591abd0a | -6.306 | -46.05957 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3cc1af8-6814-38d2-adcc-fc12de465581 | -8.57013 | -45.4357 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1407d84e-040d-36ad-913a-e3999e64a5d5 | -10.05671 | -43.87065 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68c23080-9718-30e2-a034-12331499332e | -6.96448 | -39.67024 | 2025-10-17 04:19:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a2b865f-66ea-318f-967b-f72534ecb6b3 | -5.49005 | -43.80754 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0d8c926-c378-3b58-803f-84cfe28d42fb | -10.59467 | -47.40358 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ceaa5f1-d3c6-39ea-97c4-297fe7d428ad | -8.08375 | -45.43546 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 691cc050-3530-37ab-a0aa-d96c16d3ac8a | -5.50535 | -43.77442 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53962bc7-a820-32ff-aa26-70f1bff380ea | -3.7842 | -49.42593 | 2025-10-17 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 083a684f-235f-349d-b2df-e6d5d305eddf | -6.3185 | -44.32024 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcac7e99-598e-35a3-be40-12bec8632db2 | -7.44958 | -47.13731 | 2025-10-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeefc2bc-684d-3acb-9012-771f150a291e | -6.47396 | -41.84704 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6db84312-9610-3e9c-9e90-4159d3d54efe | -8.49464 | -48.49483 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5564fc7-a685-3187-86da-7ab1ee3d9211 | -7.20361 | -45.49073 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe5e8d2b-7455-3649-83b6-8384ad119fc2 | -7.46484 | -42.1459 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fe7a7f80-78b0-3527-b52d-2e86337eee56 | -7.17735 | -46.93081 | 2025-10-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f89ee51e-0821-36a3-8248-47cbb7c0595f | -10.15909 | -44.53791 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6fad532-7c50-3dc4-bb1f-2c569e74fa50 | -3.69862 | -49.56156 | 2025-10-17 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d6615c9-0ec5-30e8-9aea-96f0d689d31a | -5.90898 | -44.74213 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dee4089-052d-384b-90d9-991ece25c2b2 | -7.1833 | -42.18705 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1bbdea7-dcab-3783-b0e3-250065c2d3e8 | -9.83679 | -47.54617 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d49edd3a-77f1-3622-b915-cf8e220ef5a9 | -11.40992 | -44.2001 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e52a7f4-91ed-34ad-abc6-70dbfc287421 | -6.135 | -41.766 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02f3ddd1-1baf-3f76-8b51-62f4c6279b46 | -5.88227 | -44.82616 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41aca079-9535-3cf1-bca1-0112ea304535 | -6.12853 | -41.76086 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7dd3a0b6-01cd-3b14-8f4f-28dc5902f748 | -6.40423 | -41.49191 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44157c24-f7d8-3c06-98b5-5bf26fd9e5fa | -6.24187 | -44.40005 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee7ce99f-b224-3646-b4c1-f9a162efb48f | -8.29453 | -43.39357 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d83d25e2-b15b-344d-9dc9-4b9769225001 | -2.8799 | -50.72049 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c45241f-9ba2-3579-a420-08cf9c1ae088 | -5.28801 | -47.92287 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 942eef3e-e4ac-3153-a0f2-801f38a155f5 | -9.54524 | -42.86025 | 2025-10-17 04:19:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 94a9b384-af1b-3d18-829d-9542f8b9f71f | -10.85873 | -44.4313 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc29e50d-c239-3aea-9da8-4b4725d5ce89 | -5.87627 | -43.8606 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a14fddc2-72b6-309c-8509-eb58e54f96e8 | -5.72561 | -44.52241 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 195781f9-2866-3de8-aea1-641ea0c41f57 | -9.16 | -41.05742 | 2025-10-17 04:19:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 7aca184e-6cd5-3e69-9fad-266d8991b85b | -10.29987 | -44.04227 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 274a5002-c17b-3654-83d7-0fd6bd06421b | -5.73166 | -41.31253 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5382881-8a6a-33ba-8e57-ba280684e355 | -10.5084 | -43.40858 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5422be6-68e7-3015-b7b7-48b888bf48e0 | -6.26473 | -44.34007 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 530459f6-7c4e-3e27-bbfc-8272f443e31c | -8.24555 | -43.41981 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 996296cd-277b-3d31-9665-00b71642c4e4 | -6.45316 | -43.3861 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| facf4e4f-d029-3977-84ea-b10ddbe24b53 | -8.29225 | -43.38575 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ca8e777-223d-3ce3-b38c-491f82c4fe77 | -7.8087 | -47.91514 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6308d32-4c50-39db-bb4f-4ce7d7991605 | -6.51689 | -42.18753 | 2025-10-17 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6abd018e-5049-351a-91f0-223a940d80f9 | -6.31871 | -40.93996 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 49f2749f-1c60-3230-af86-5253269ccd6c | -6.1345 | -41.74515 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 70175163-3d45-3316-99ba-e13321eb29a0 | -6.46981 | -41.85051 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5db808bc-7c17-323c-9581-f02b672ff093 | -8.43798 | -48.70223 | 2025-10-17 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401c2d35-f459-3889-bb3e-fcd83350cf7b | -5.8916 | -43.89508 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2d93164-c046-3a29-a7cf-c902b474109e | -5.69147 | -42.67881 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cfcab987-9a3e-3567-b2b9-e41c362482b6 | -11.45326 | -44.21061 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44cf6470-db02-3d65-b1bc-416fbf0330ed | -5.76968 | -43.07955 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1ef6e272-647a-38d8-abc3-1ae2f91e445d | -5.36484 | -42.74859 | 2025-10-17 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c7212f4-5f06-36e0-8a38-2961ad9f097e | -10.71227 | -44.54453 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4aa6ce08-5359-30d8-98dc-ecb405f2583a | -3.84421 | -47.0691 | 2025-10-17 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d74794e5-3752-388d-a0f7-f5b0f33b3b0a | -8.49015 | -49.04428 | 2025-10-17 04:19:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfc9dab1-76bf-3588-bc22-ec8a914c10ae | -6.20775 | -41.76411 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7228bb54-f2ee-309f-9ae3-283a236fbc8a | -6.89097 | -43.98718 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92005dec-a30a-3d2a-b9b8-479d1d80227a | -9.89868 | -47.79137 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cfa1c92-8877-3912-b774-e2176d50a034 | -6.24551 | -44.02495 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b89a128-227c-3359-9a59-c48d43c2b49b | -8.21211 | -43.97735 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9da32b24-94c7-3e73-ac00-6f7783568a46 | -4.92309 | -41.51616 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af21d66f-076f-3838-959c-03361d161fec | -5.75399 | -50.00133 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e344474e-c074-3900-8997-f90ef47906b9 | -6.84499 | -44.39228 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c6f1cd7-6c42-33ba-9b11-aa44de3c95de | -10.46489 | -45.06898 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8243875a-9ec3-3725-add0-099b901608fb | -11.40889 | -44.22998 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 755aac36-1967-32fe-9e3f-7e8ac83f7156 | -11.47294 | -44.19486 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af1e1d84-9a49-353a-a17f-8f407d53701c | -5.44632 | -44.17541 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec91c131-9551-3d0a-8fd1-1ffe1fdbb5d8 | -8.35351 | -40.33255 | 2025-10-17 04:19:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a3fc23be-c07b-3448-a76f-5aad19f63d55 | -7.85449 | -43.80159 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8d3c76cd-870d-3490-9ede-366bc8b43f59 | -8.96502 | -48.42863 | 2025-10-17 04:19:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1f3a573-812f-3bb8-ae05-10c761ab51f3 | -11.47471 | -44.27398 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89939b4e-f20b-30f4-b87e-49031c49f322 | -8.30867 | -43.41444 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd87275d-1832-311f-b260-3f9f88f8fb8b | -11.39224 | -44.13329 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93521cc8-1598-3ebc-a4f8-526c5b016351 | -5.32509 | -43.18317 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6694729-9e9d-34a9-8843-0721f93a60e3 | -9.04135 | -49.09552 | 2025-10-17 04:19:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0a64c11-f809-30e1-8313-460fdeabc18e | -9.01927 | -46.61932 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba83b4fd-fe8d-3b66-9a63-a00bd423d2e5 | -6.25648 | -44.50105 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec5323d8-9bdb-3691-8e3b-a86050878a2b | -7.16113 | -46.52889 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 567ea74e-4d80-3761-9edf-1ca16120a5ae | -11.47246 | -44.26613 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 451399eb-7050-3302-872f-f41bbf77f3e2 | -9.06593 | -42.45473 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9205212f-6d94-3ea6-abe4-c1917d6b0772 | -7.20306 | -45.49421 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96040b48-b895-3d46-9dd5-2332d5b23128 | -5.16073 | -46.2701 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd3e9496-4e2e-366b-acf4-2ac672b81f68 | -10.92484 | -45.41503 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee501670-c765-3ff5-834b-57c93ff69f26 | -5.30058 | -41.08379 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0cd15aa9-91ae-3e23-bb1c-636c19c011ec | -5.27217 | -42.166 | 2025-10-17 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8c6f1157-1320-3c1b-8a54-bcd3a72eb53e | -7.00861 | -42.00024 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0400d7b2-545b-31f3-8352-e8e9f17fc268 | -5.4685 | -44.64369 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0de4e59a-6ae5-3403-8e23-475dad5ac047 | -8.4761 | -50.1074 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a962db8-784c-34ef-ac5e-2c16fe7d9efd | -3.28614 | -52.54746 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
