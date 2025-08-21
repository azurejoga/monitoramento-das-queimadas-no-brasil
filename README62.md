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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aa987ba-a8fa-32fe-a366-ebb76d5b298e | -12.47312 | -47.30016 | 2025-08-21 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cb71dceb-06d5-3012-8b63-dd97788a8103 | -14.31184 | -52.03242 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 41375db2-aff7-37f8-9a2b-4831e2eae1c2 | -12.21449 | -53.60038 | 2025-08-21 12:55:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c220aafc-584c-3c25-84f8-efa79265a712 | -12.94466 | -46.2492 | 2025-08-21 12:55:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c188bae2-1e5c-3895-b725-152186093e12 | -13.14915 | -54.91074 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 395bd159-c82a-34fb-9dee-5df32d184cb3 | -13.57807 | -47.03843 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 7d19236f-302e-33af-b32b-4dc3e15103ca | -14.85016 | -47.92821 | 2025-08-21 12:55:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d61198da-1f9a-3365-8bea-20977cff3efd | -12.02846 | -57.09228 | 2025-08-21 12:55:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e81417a4-3e0e-35f3-863a-dcd70e2ddaab | -14.86268 | -47.95966 | 2025-08-21 12:55:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 57c87258-a9ae-34a5-98b7-6fcfa48bc1bf | -12.46337 | -47.29361 | 2025-08-21 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 383a200d-baa7-344d-8aec-efc49ba661b5 | -12.89004 | -46.07421 | 2025-08-21 12:55:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 96c0dda0-e411-3f81-b321-ee376c451633 | -14.99231 | -54.82332 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 919902af-b723-3bb4-a6d3-214f3c9438ba | -12.45731 | -47.29818 | 2025-08-21 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 04d4030d-b787-3af1-833a-44f1905e7c65 | -16.51457 | -47.87073 | 2025-08-21 12:57:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| d6d009a9-07ee-3e62-9d86-583174e8cb7b | -15.93735 | -52.20762 | 2025-08-21 12:57:00 | TERRA_M-T | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6885e190-b2fe-39ae-8c63-8dc50a252452 | -16.52328 | -47.8774 | 2025-08-21 12:57:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a5fe7bc4-03e0-3318-8fdd-0ea8a81c7687 | -16.00899 | -56.59682 | 2025-08-21 12:57:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2f06dd1-1c37-3b96-9756-7b79b84f8b9f | -25.04974 | -48.90001 | 2025-08-21 12:59:00 | TERRA_M-T | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| d9b98969-7f13-3d92-924f-3a2e6edb9b77 | -25.04368 | -48.89239 | 2025-08-21 12:59:00 | TERRA_M-T | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 8136e189-5e37-3850-9ac1-1f83e7cb368c | -13.0307 | -45.2189 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| fb32c62d-f817-3d5e-90a9-af4c6ed98454 | -13.1367 | -54.9171 | 2025-08-21 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 89d8b4e8-b386-3d89-b0eb-c960c610cf92 | -12.9533 | -46.2419 | 2025-08-21 13:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 490f4151-158c-3266-80ea-cdc624562e67 | -7.0164 | -44.6413 | 2025-08-21 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e23cb338-f1a5-3ba0-a9da-ad4363769809 | -13.0123 | -45.1756 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 324.2 |
| 8cc62fb5-b6ed-3066-9e42-791cb51c7f4d | -13.0321 | -45.1492 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 259.2 |
| a808c60c-74dd-3742-a4ef-4f04997dc329 | -14.8538 | -47.9504 | 2025-08-21 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 500c0be9-447e-3342-8818-cad27840e8d2 | -18.3038 | -45.5257 | 2025-08-21 13:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 166.5 |
| b3daa04c-3be9-3eac-9990-c5d30ff48e54 | -13.0505 | -45.1925 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2aa0bbcb-679d-3488-8675-f66f3f5f526a | -13.3346 | -54.4233 | 2025-08-21 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b2e195c8-9f9f-39e3-8c0a-a4f77a961bd9 | -7.0354 | -44.6167 | 2025-08-21 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2eea106a-b5b8-3027-bb78-933ed6014f03 | -7.6296 | -45.2464 | 2025-08-21 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a35069bf-fc5e-318d-a0c1-0e2eaf9ccc12 | -13.051 | -45.1693 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 22c2d8d0-f657-30ec-ad65-fc4389343be5 | -13.1558 | -54.9151 | 2025-08-21 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 315ca279-9fa2-3cca-a78a-a9da31677c4c | -7.0166 | -44.6184 | 2025-08-21 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d591ee1e-5f4c-333b-8c59-2e73d267f951 | -13.0312 | -45.1957 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 600.1 |
| 5c62e932-274d-3963-ab7d-a64df7f2525b | -13.0317 | -45.1724 | 2025-08-21 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 972.4 |
| 6f48e9d8-2f40-30c3-9280-83253ff7fb6e | -14.8543 | -47.9279 | 2025-08-21 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3151f398-b79f-3990-bf7d-cdd9207b679c | -13.0321 | -45.1492 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 241.5 |
| bf848de0-d0fc-3361-82b5-71292cfcddac | -13.0505 | -45.1925 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 56365575-b042-33dd-9406-8fdc3241b4fc | -13.1367 | -54.9171 | 2025-08-21 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 67618b41-da5e-3de1-ad0f-ae0a3ca53ae8 | -7.7004 | -44.024 | 2025-08-21 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 533cd92d-3759-3dd0-90db-27cb7bc99620 | -13.0307 | -45.2189 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4a9cd7a7-41d3-3324-b4f2-721366944e45 | -13.051 | -45.1693 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 194.7 |
| a8ac21fb-9db0-33b6-aa03-ad5435719fbc | -13.3346 | -54.4233 | 2025-08-21 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7ca6545e-02b8-306e-b11e-d3bda5f292f3 | -7.0354 | -44.6167 | 2025-08-21 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 10acaa0a-bead-3073-b91a-b08364f4ad3b | -13.3349 | -54.4027 | 2025-08-21 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3458aaf3-af60-3ac0-b369-24b4f1be53ad | -13.0317 | -45.1724 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1045.9 |
| e08d97f3-551d-3b77-8809-5537dbb51a44 | -7.6296 | -45.2464 | 2025-08-21 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| edd712a3-4137-362c-a18e-5706ab9f7294 | -13.1555 | -54.9357 | 2025-08-21 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 120f0479-9589-308f-9074-ac2a57934f65 | -13.1369 | -54.8966 | 2025-08-21 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 95c628d1-1b19-3c5e-a725-5e0840a5bc1f | -14.8543 | -47.9279 | 2025-08-21 13:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 26ebfd65-496b-3036-b341-810500ac9dae | -13.0312 | -45.1957 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 624.7 |
| 3dc6131c-c5be-375b-98eb-81411be8f2e3 | -13.1558 | -54.9151 | 2025-08-21 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 259.3 |
| 413c3097-3526-3bbf-9531-42ace9962153 | -14.3321 | -52.0224 | 2025-08-21 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9bc806b9-3811-3b65-a33a-8ccb2de90f5c | -7.0166 | -44.6184 | 2025-08-21 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0ceb0ce8-fc60-367a-b660-8102b97c3ca8 | -18.3038 | -45.5257 | 2025-08-21 13:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 40d22476-eb04-3268-8dde-2f036d6bce98 | -13.0123 | -45.1756 | 2025-08-21 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 398.5 |
| eb9bdc90-77c0-326e-a6a1-8daa925a84b1 | -14.8538 | -47.9504 | 2025-08-21 13:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e132ad44-70dd-3e30-ac68-6f8174a4dd7e | -14.3715 | -51.9747 | 2025-08-21 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7df6430a-c1c8-35a1-8d3c-75edf1aea9d2 | -13.3349 | -54.4027 | 2025-08-21 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| bb6aff1e-2823-3dac-a1b9-3e829138d896 | -11.6028 | -50.3739 | 2025-08-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| ed09d6a7-2dc4-3c22-a148-6873c01c9d27 | -14.8543 | -47.9279 | 2025-08-21 13:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3e7f0934-1258-3982-af00-61a4c2855fd0 | -14.8538 | -47.9504 | 2025-08-21 13:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a362c43d-87b0-391b-b91c-005df383798f | -13.1369 | -54.8966 | 2025-08-21 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| a2878420-e0c4-3847-9ae4-194fd4ce9c5c | -13.1364 | -54.9376 | 2025-08-21 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 1468688a-37ef-3945-a26f-a3d4df9e35cf | -7.2715 | -43.6714 | 2025-08-21 13:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7998b2f4-73d7-37ff-9a48-98a2fe3fc549 | -13.0307 | -45.2189 | 2025-08-21 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a0676a90-7f01-3aa9-a0b4-141268a89b05 | -7.0354 | -44.6167 | 2025-08-21 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 3c114d9c-efd7-3466-88c7-1125b2a6c5c0 | -8.8737 | -62.3925 | 2025-08-21 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 68a86439-b342-38ba-97d0-5bfcdd62272c | -13.1555 | -54.9357 | 2025-08-21 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 255.0 |
| 4dc9a655-f6d5-3e4d-9598-d8e6c5627935 | -14.3715 | -51.9747 | 2025-08-21 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| de13e59d-1500-3871-8d15-0665c52345b7 | -8.0152 | -47.6656 | 2025-08-21 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 3503c789-555f-321f-bfb1-e7dda8cee142 | -11.3468 | -55.4124 | 2025-08-21 13:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 56b969ee-0468-3d41-81cc-30c1fc722181 | -15.6754 | -41.2648 | 2025-08-21 13:20:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| 0f94b640-9b04-386f-8c56-08ce26716cf6 | -7.5832 | -44.3819 | 2025-08-21 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c08e257c-07f3-3572-975d-7e31c2f0b572 | -13.3346 | -54.4233 | 2025-08-21 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 4e90a7dd-ae26-3bbd-9b01-360293e191ed | -14.3321 | -52.0224 | 2025-08-21 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 27982dcd-bd50-3a81-8d14-139726454110 | -7.5641 | -44.4068 | 2025-08-21 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 7ecb52d1-5325-3ba0-aeb3-7bb8d08ca1dd | -8.8736 | -62.4115 | 2025-08-21 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 12626907-179d-3cdc-ba2f-3d502e8fb456 | -14.5843 | -51.9464 | 2025-08-21 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 288c8a3a-ca5d-37bf-96ef-99ec784226c6 | -7.6296 | -45.2464 | 2025-08-21 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 67b2a457-34e5-33c2-b0bc-967e9de0816e | -13.1558 | -54.9151 | 2025-08-21 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 806.3 |
| 08ebcad2-4926-351b-93bc-712ceefbea9a | -13.1367 | -54.9171 | 2025-08-21 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 336.9 |
| 7e121d42-01c2-3c02-aec8-96ae29f2f995 | -8.8737 | -62.3925 | 2025-08-21 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 03f9dbcb-d172-363d-a7b5-ba8cee5c360a | -11.8078 | -50.6499 | 2025-08-21 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 2dd9a528-e534-3dfc-919f-80210ded0d7c | -8.0152 | -47.6656 | 2025-08-21 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 48e8ab04-28d8-3760-980e-13154f14c2a5 | -14.9999 | -54.8343 | 2025-08-21 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ea32e0ba-29c1-3b85-aa85-822914804b19 | -4.7152 | -47.2216 | 2025-08-21 13:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 654d6fca-5445-3aa0-9260-b92df9076887 | -12.8988 | -46.0677 | 2025-08-21 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f6bcc65e-f2c8-306f-b870-2f60964d2e27 | -13.0307 | -45.2189 | 2025-08-21 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 160d1998-3929-3aa9-98c2-5a387ba19e0b | -13.3154 | -54.4254 | 2025-08-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 03f02b71-25ca-398d-acbe-2898d22bde1d | -7.6296 | -45.2464 | 2025-08-21 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 95f6460f-5f90-323e-85f5-35fe974228b8 | -7.0166 | -44.6184 | 2025-08-21 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 220736fe-fe78-3e39-8c92-186c33cb8e7f | -8.8736 | -62.4115 | 2025-08-21 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dd825b4e-aa07-3987-9656-84b7f1a5c481 | -7.0354 | -44.6167 | 2025-08-21 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c7f4779e-1fcc-3c7d-a4d2-9b2bac551661 | -14.3321 | -52.0224 | 2025-08-21 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 9d0b9d1f-1596-3fee-9f9a-2bb68d3d2b9d | -14.5843 | -51.9464 | 2025-08-21 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8679cc0c-4d4e-32da-8c56-7697238dd1e5 | -7.0164 | -44.6413 | 2025-08-21 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| deb82db5-d27f-34fc-b371-fc08fb0923f0 | -6.5678 | -44.4738 | 2025-08-21 13:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| cfe4a84c-a35e-35d8-83c6-403619a3d5e1 | -6.539 | -45.4772 | 2025-08-21 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |


[Clique aqui para ver as próximas entradas](README63.md)
