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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 753a706b-ee55-3978-82ef-9a98c9fc601c | -12.62146 | -53.13317 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9acf040d-b19e-3825-807e-6ac9e7ec822a | -12.62078 | -53.47808 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d0aba81-8410-32fd-b751-5959674b71d0 | -12.6202 | -53.48168 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5cce7740-383d-3788-b031-66e42980f1e2 | -12.6189 | -53.51109 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d97d4659-1a3c-3846-b40b-3c321c20459c | -12.61819 | -53.02777 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49655245-9fb5-3163-a307-3935e8bd17d2 | -12.61814 | -53.13262 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08fb62ed-35c5-3fa3-bf84-9aa9f5e7e748 | -12.61763 | -53.03132 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11a9513d-698d-353f-90ce-50e593de977f | -12.61757 | -53.13617 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4d472db-b338-311a-b21f-08ff0e0205f5 | -12.617 | -53.13972 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63f7b569-80be-32d1-a08d-a1bc5fd2a19e | -12.616 | -53.02013 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0cb9ddb-4cda-31ce-a693-1f4568043c23 | -12.61494 | -53.00541 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3deb6bc0-d3bd-35b3-ace0-3c3ea4a41d51 | -12.61488 | -53.02723 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc70aedd-2505-37eb-851d-daa82c59e9e5 | -12.61431 | -53.03078 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d177b94-17ac-3035-a7b5-f13c269d2701 | -12.61269 | -53.01959 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f7c4fe-f361-308a-a38b-f8371b9ecf7a | -12.61156 | -53.02669 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e30d95-f409-3878-9a27-81e8e7659c84 | -12.611 | -53.03023 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1d874c6-10cf-3fd9-b886-0566955ae115 | -12.60711 | -53.03323 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029f1f3f-9007-3b0c-9f15-b727bceb9fda | -12.60655 | -53.03677 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 998f17c3-6142-3a5e-9be2-014edf0e1303 | -12.60323 | -53.03622 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b343e337-8d93-34b7-bb91-90ea57ee2e16 | -12.58326 | -53.05474 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b64d6f5-c195-3b29-971b-818b98611b25 | -12.58269 | -53.05829 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73c664e-ab71-32dd-a20d-5642de5d5886 | -12.58213 | -53.06184 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12b59222-3ebe-32b5-9142-3816cb7475b7 | -12.58099 | -53.06894 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf6364c2-fe11-30e7-a80a-5a8398ac28f2 | -12.5805 | -53.05065 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a174f091-89ba-38c6-982f-72e1124cc190 | -12.58043 | -53.07249 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e42bb54-37b6-3775-a2ac-1aaf88e0a652 | -12.57994 | -53.0542 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c81273e4-9c58-3fe3-a8e6-b7e651e8b41d | -12.57937 | -53.05774 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb2e9971-0f7f-360d-8441-54a5f442d2a2 | -12.57881 | -53.06129 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a886a20-8ca2-372e-9294-c6df4a7bb551 | -12.57824 | -53.06484 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70c66b23-3edb-3038-a238-842f0b1e633f | -12.57768 | -53.06839 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5fa932fb-8366-3407-ab33-40108c73ee8f | -12.57718 | -53.05011 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a57ef53-28f3-325b-926b-bc5be97ee08b | -12.57711 | -53.07193 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13b2dc42-3880-37ce-b0e1-ac0c07ec0b21 | -12.57654 | -53.07548 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4605b1f-1868-3039-ac69-b47c65036f1b | -12.57605 | -53.0572 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d02bd5-9aa4-36d7-8c37-50f69e3ccb49 | -12.57492 | -53.06429 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f00aaaa-252f-3516-9cda-e7cd9281ece3 | -12.57436 | -53.06784 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f90372f-258b-3467-ac96-40c2a4d9fad5 | -12.57379 | -53.07138 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d053bfbf-8845-3691-b22e-feb49823aade | -12.57323 | -53.07492 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ea4abae-95d6-33e9-99fe-4d51403eebcb | -12.57273 | -53.05666 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95759a74-312b-3537-8898-daee4e458300 | -12.57217 | -53.0602 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95e3b5fb-2740-3596-86f3-e58f48b9598e | -12.5716 | -53.06375 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40b50b34-5d80-3b00-9181-3af7f80d653e | -12.57104 | -53.06729 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29262b27-f72d-39ec-94fd-33428e74093e | -12.56772 | -53.06674 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fa47877-3932-3f9d-8d4e-6f89fcf98328 | -12.5644 | -53.0662 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138962ac-1b8a-31a4-a049-c630f790c09e | -12.53851 | -53.29214 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9239e5c4-708e-3f00-a254-0725a37503c8 | -12.51817 | -53.24844 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46b739ce-d946-3c60-a2ea-e0c26f36c2fe | -12.51703 | -53.25557 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f671f7a0-36d7-36f4-9056-8b0a6dc3f2b9 | -12.4824 | -53.15452 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4252d7cb-ad38-3b40-8006-3e48ca57343d | -12.48184 | -53.15808 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eb10fb0-e3dd-3bfd-9376-f46322afbe9e | -12.48119 | -53.18356 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96e220b8-511d-3ec1-9d37-a9003b239e36 | -12.47908 | -53.15396 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d892adc-7254-378d-8622-23a0364bb5f7 | -12.47851 | -53.15753 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ba2507-9eee-33dc-b14e-670a6da02551 | -12.47786 | -53.18301 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 488bd340-8de2-33b2-ae70-cd5df8294361 | -12.47576 | -53.15342 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b42250c-65b5-3797-83bc-e9b830e30d3b | -12.473 | -53.1493 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8a72cf5-bcaa-35e2-8bc2-1e427bafea22 | -12.47243 | -53.15286 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16a87694-3299-396b-80e7-77aa2134fa40 | -12.46968 | -53.14875 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c19453d-2240-3f1e-bc32-1af96e41cc01 | -12.41498 | -53.53331 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf96b4b-a390-3850-b18c-47edfc03c246 | -12.35689 | -52.87559 | 2024-10-10 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f54e94-40d2-3977-8bf3-08fee29d77d6 | -12.35633 | -52.87912 | 2024-10-10 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9871f9e2-be3c-352b-8c78-c0989bf5017f | -12.35577 | -52.88266 | 2024-10-10 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 643ee8de-93f9-3d55-8bd0-eb079fe1cf22 | -12.28205 | -53.4706 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5abd76-0627-3060-838d-486b6f73e661 | -12.27871 | -53.47005 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9a0d96f-f874-3429-ae42-676d11e24fcc | -13.01584 | -53.66253 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b015ba18-2376-323e-8acd-5f22f7894b45 | -13.01308 | -53.65834 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8ebeebc-2576-34fe-a31f-e0ad164839bc | -13.0125 | -53.66196 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a42ee169-4639-3ee6-bd8c-2e0a790ff73b | -13.00974 | -53.65777 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f4569dc-747c-3076-9fd1-e7191b4d19dd | -13.00915 | -53.6614 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3837b54b-14ea-3d74-b222-caf9782814a4 | -13.00856 | -53.66502 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a047474d-f644-3aa0-acab-85f13ef9a712 | -13.00798 | -53.66864 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dda3db85-80af-3718-b7f0-48f28178882b | -13.00581 | -53.66082 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 640e7f13-7ad8-3e04-ab03-84066a82fe44 | -13.00522 | -53.66445 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24433b76-29fb-36b5-9fe1-ba88591d9578 | -13.00463 | -53.66807 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53d13b32-221c-3b3b-b6f1-4cbb94d0446e | -13.00363 | -53.65302 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8303d01d-00fb-307c-8062-c15a8e519809 | -13.00305 | -53.65664 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e7a35a0-ecbc-3ef3-8630-77de77e01269 | -13.00129 | -53.66751 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ad9cf75-a937-329c-9bef-45946488d8a6 | -13.00029 | -53.65245 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb89db19-910b-3582-ac6e-b73a331c2f03 | -12.98412 | -53.49794 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3435afe0-190d-31a5-8834-3bd5943c2f30 | -12.98079 | -53.49738 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddde54c2-a19c-3963-9666-e6e1385d29ec | -12.88491 | -53.48161 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee27296a-4a8f-326e-8eb6-3fe0eae1c9b7 | -12.88337 | -54.02323 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d732d71-0c6b-3e07-9d7b-f5430165658a | -12.88216 | -53.47746 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 453ef7ed-1c27-340a-be72-595d5362b9d7 | -12.88158 | -53.48104 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1863a996-5b2b-373b-8e0c-3d5912864285 | -12.87998 | -53.46973 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcbb948a-b0be-3708-a53f-3bfa12866b57 | -12.8794 | -53.47331 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df55e06d-3c09-3072-9ee9-10bb5b0e8848 | -12.87882 | -53.4769 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c043797-2a74-34f2-babe-0d62ab2c2b6a | -12.87824 | -53.48048 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30232c7a-e1b5-353c-9e0e-415d684a8524 | -12.8782 | -54.03373 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd64f735-0840-3c0f-919e-5a9317548a09 | -12.87761 | -54.03742 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de50e5cb-df40-3d01-895f-da9f321e92f5 | -12.87701 | -54.04111 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24ceb8a1-6ed0-37cd-bcb8-cdd10cd2ea96 | -12.87665 | -53.46917 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3902a450-bd93-3ab0-9b59-771bfdbfa5c0 | -12.87607 | -53.47275 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfc8738c-78fc-34cd-8d79-eaecd7afc45c | -12.87549 | -53.47633 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b37222d-6555-3bbb-84f0-a7d127010ff3 | -12.87491 | -53.47992 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a04b4a48-55aa-3c2a-9801-0ae207ba5bf1 | -12.8735 | -53.47218 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df303755-4394-30e6-92da-c77885bea3b5 | -12.87293 | -53.47577 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92f6d186-b24a-3cc2-8d21-ac800cbf92be | -12.86057 | -52.82766 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca58d09f-1e94-3c4e-86f1-4ef2600ce73e | -12.85837 | -52.82006 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce2bad1d-b52f-34aa-9cbd-3d1165596d7d | -12.85781 | -52.82359 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba4ff773-d00e-3db7-ba10-54097d5091cd | -12.85725 | -52.82712 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README122.md)
