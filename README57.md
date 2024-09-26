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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be1b0f4b-5e4d-306d-8408-396264081600 | -2.71797 | -46.72995 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0cc1fd4-0af2-37a5-88a7-cb73c9006d38 | -2.71728 | -46.73415 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c9bbb5b-d121-31e4-b9fb-62c96c64d766 | -2.71223 | -46.73763 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db2186f5-8852-37d7-a53c-ca4c79db3a89 | -2.68085 | -46.73396 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb32decc-5cab-312f-9694-3af1ac2bc9bb | -2.68019 | -46.73813 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 282c343d-c151-38b8-8972-5caae695e3b1 | -4.47464 | -47.73804 | 2024-09-26 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01cd6cf0-6621-33a9-b92f-5916f4ecaed3 | -4.73313 | -46.59909 | 2024-09-26 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36b8bcc3-ba3f-3ef9-a03e-8691513a1237 | -4.60674 | -46.47511 | 2024-09-26 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b49d2bd-70eb-3b1a-a153-99984e5c1ce1 | -4.58144 | -46.3052 | 2024-09-26 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32446d26-9034-39bc-8fc0-877e1b4575f0 | -4.58019 | -46.31286 | 2024-09-26 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3e20642-1d98-35d3-8e8e-69ef324bcfc3 | -4.14079 | -46.69547 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56dd60b5-c412-3df6-8188-90b8832d057e | -4.14014 | -46.6994 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee25c45-a81d-320e-aeb2-2e6d24015bdd | -4.13589 | -46.69864 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b438e209-b053-316f-b96e-9b88bf050c66 | -4.10574 | -46.80046 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d7ab0aa-1c01-3266-9fe4-236655a20046 | -4.10509 | -46.80439 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5131a72a-cdf1-3ded-860b-a51137e4f09f | -4.10081 | -46.80363 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6daef18-324d-3721-b002-675cc5c79d56 | -3.92251 | -46.43993 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b6665ca-6d3a-394d-af21-5bae0e9df7d8 | -3.9219 | -46.44375 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 372d7891-0a7e-3f6c-b01f-2ddfb730adbf | -3.91832 | -46.43922 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b9930a5-1855-3b15-8ea3-390d7316f7cf | -3.9177 | -46.44305 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1cde2bec-ff33-31d8-965b-f5343d0a51d3 | -3.91708 | -46.44689 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 847bbe52-87dc-38ad-a3dc-e34c3e15babc | -3.91646 | -46.45075 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ccb08a0a-937b-3b67-bbaf-5d04429c7d64 | -3.91584 | -46.45462 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 41.3 |
| c1c9b2c1-f126-3fab-877d-70f3c4d382cc | -3.91522 | -46.45847 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 329a79e7-adbd-3766-b3f5-ba1999788de3 | -3.91226 | -46.45007 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a07facc4-b30b-37ca-beea-153b51ba9200 | -3.91164 | -46.45395 | 2024-09-26 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 110be437-c4a3-3163-be38-c1cc62736982 | -5.38348 | -47.52669 | 2024-09-26 04:04:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78ea4570-eacf-321c-9133-61b2d6019743 | -5.38315 | -47.52469 | 2024-09-26 04:04:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daadf911-2ea1-3f39-a504-8a2374d16438 | -5.36534 | -47.81758 | 2024-09-26 04:04:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8446449-db2c-3822-ba52-ee8a9c82c8f7 | -5.32512 | -47.82707 | 2024-09-26 04:04:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68db9dd1-16f9-32bd-8b4c-adb8928aa3f1 | -5.3225 | -47.82426 | 2024-09-26 04:04:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37523121-53c7-307c-9f25-dc4d3e4b5dc8 | -5.46256 | -46.4709 | 2024-09-26 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d9bd365-e81c-3bc2-ad6e-863c9115c28b | -5.38027 | -46.56703 | 2024-09-26 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e4bb55f-ec32-3d86-b64b-8b33e50b4452 | -0.72564 | -47.52845 | 2024-09-26 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d04eafa5-f56b-3cfd-8905-389c328f2911 | -0.72522 | -47.52718 | 2024-09-26 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a90609d9-0bd2-3fc9-acc1-8c1da3e58e7b | -1.90856 | -47.88705 | 2024-09-26 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22f52cde-c6b6-3e97-8414-4c61b0754525 | -1.42168 | -47.4114 | 2024-09-26 04:04:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8bd975dc-0040-3aeb-9b35-4761fa5b4ed0 | -3.70045 | -47.61507 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8937cf5-22d9-31bc-bf5d-0ba3d1027377 | -3.69589 | -47.61428 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f0d6377-31cc-33aa-a66f-7bb15be506c4 | -2.92324 | -47.83176 | 2024-09-26 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 186cdad2-9a44-37af-809c-8ec3a420dcc0 | -2.89477 | -47.88825 | 2024-09-26 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f301f11-4aa9-31db-aa23-047866096a64 | -2.7765 | -47.63869 | 2024-09-26 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9094176d-41fb-3d2c-9108-9ebf4f40a6a0 | -2.46092 | -47.8402 | 2024-09-26 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa9a58dd-5862-3458-9eb1-27d81e415e5d | -2.35262 | -47.60597 | 2024-09-26 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 84170370-da2f-3e48-b3c1-c595f743cb55 | -2.35013 | -47.60487 | 2024-09-26 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b83bbed1-1bd0-3dfc-a814-8a2238041334 | -2.34936 | -47.6098 | 2024-09-26 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57300153-7705-3073-9d66-27870db23d18 | -3.21308 | -48.92192 | 2024-09-26 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0103c420-f807-377c-a073-21da5eb0012c | -3.21258 | -48.92485 | 2024-09-26 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 353d40d0-712e-3063-b827-2989ec60a154 | -4.66344 | -48.15645 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8b1030a4-9aa6-3e7d-a2df-0836a20c33c2 | -4.65877 | -48.1557 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f7d8b4f-82e8-3b9d-9d43-636a5baea41a | -4.62908 | -48.53507 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7513063f-12f2-392a-8a72-dd6e08b7acea | -4.61646 | -48.83634 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7b2bdd2-eafe-3733-937e-a1fe99140fce | -4.61434 | -48.83393 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b79a82e3-9a3d-3346-8c6b-9aef8f5e0782 | -4.50911 | -48.34449 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53331ac9-bc25-3c02-808a-0648d35e281f | -4.38597 | -47.76514 | 2024-09-26 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c4e0e2c-00d0-3a59-a715-8649bcec58c9 | -4.28855 | -48.06983 | 2024-09-26 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d65211ea-a5ee-3d54-b215-801f1979f198 | -4.2839 | -48.06899 | 2024-09-26 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54e8a381-a5bf-37e4-bd36-24a21ffc23de | -4.28005 | -48.06327 | 2024-09-26 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0c7da5d-e148-3d19-96a0-554345b8c7e8 | -4.27924 | -48.06816 | 2024-09-26 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9607b548-569b-3efc-a2a7-748977902b19 | -4.26708 | -48.22977 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4bc44fa-8063-3c91-8a1e-6210670dd3b0 | -4.26622 | -48.23499 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3c5d3b-64cb-3bfe-8a17-b18741ca68aa | -4.19811 | -48.6188 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a2cc7e5-d1f1-39d0-b90c-626f5a5ecd75 | -4.19722 | -48.62418 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c9b4d79-8509-3c2c-9760-a4da9930cc82 | -4.19327 | -48.61787 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a35dc7c-8b5f-3403-a9ea-6481ff73e12e | -4.19239 | -48.62323 | 2024-09-26 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9ff68bc-d741-35a5-a114-e6c15a90104f | -3.78251 | -47.63174 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31c829cd-cb39-369b-a336-4435aa94c60c | -3.71943 | -47.7298 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b86bfa70-7bbb-3fcf-8d1e-2658c869ce2f | -3.71939 | -47.7277 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c63f4749-fbf4-36a1-bce0-2b041ca9b2b0 | -3.71859 | -47.73243 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7c09c665-f733-3b5d-948c-df214b8aa42c | -3.71484 | -47.729 | 2024-09-26 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 039e2753-ac22-39f2-925d-61063273df3b | -5.22194 | -47.9701 | 2024-09-26 04:04:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39e57bda-0516-312e-bc23-00d54b8818c2 | -5.219 | -47.95984 | 2024-09-26 04:04:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a7215cb-d811-3e1e-9d0c-beb911c0436d | -5.2182 | -47.96453 | 2024-09-26 04:04:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05c71bdd-f32f-3a06-87db-29ed6fca72f0 | -5.2174 | -47.96925 | 2024-09-26 04:04:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad21a346-f47d-3750-b073-9e6d6baebe70 | -1.18278 | -48.81562 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20529cb0-e470-35ea-b9cd-9954836dff2d | -1.18228 | -48.81869 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90626d20-4cca-3016-a2cf-2849b5834484 | -1.18178 | -48.82176 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1208718b-75cd-383b-adca-31e42866918a | -1.18078 | -48.81703 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3eb707d8-b64b-3e82-8584-c8f579986186 | -1.1803 | -48.82011 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82c4e3a0-2bf8-3dfc-90d3-d3e511bb1899 | -1.17983 | -48.82317 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33e007bf-9600-334c-835d-969adbabc189 | -3.24534 | -50.47573 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f334478a-74a4-3b24-8d18-70f8917f1a0c | -3.2447 | -50.47958 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51738de4-0867-3dcb-8bb7-457b99e307bd | -3.23599 | -50.46288 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 933c0078-dc72-33a7-93a1-0ef4ceee0989 | -3.23041 | -50.32524 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dee8db1b-d959-34b2-b6c6-d28799dd2778 | -3.2304 | -50.46201 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b31a02f6-2b82-3bc5-8ca5-7cb206f95878 | -3.22977 | -50.46581 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52fc08f4-b701-335e-999f-b382217a3101 | -3.2255 | -50.32064 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96c3144b-8799-3009-ba54-367d57b3bc0e | -3.22489 | -50.32428 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f33013c-e0d7-354a-a93b-9da6cf3515a0 | -3.22428 | -50.32792 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07b2cdae-990d-304b-a72f-535484175eb0 | -3.18075 | -50.2832 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fe2739d-1a57-3099-ab48-0c608489ded4 | -3.18043 | -50.28753 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8420c238-4e48-3d53-b378-e837ffeb3a81 | -3.18013 | -50.28683 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09864c37-0b9b-3b63-b9ed-efb610c94e8a | -3.17432 | -50.29023 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7d9009-03b2-3586-94e7-d236e5606adb | -3.14672 | -50.28553 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91daf595-25a1-38ae-939c-db238b995417 | -3.14612 | -50.28915 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab9e7f8f-3807-30e1-a290-b40eb7603238 | -3.1412 | -50.28457 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6dcdd0c-7ebb-3cd6-a7dd-d473ee582102 | -3.1406 | -50.2882 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad98de0c-60ac-3b65-a1c7-56045a6b1071 | -3.05734 | -50.41777 | 2024-09-26 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1212768f-a34c-3bc8-baae-d8f5c83ae993 | -2.95566 | -49.36034 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 206b02f1-0690-362e-bdb8-1133463ded39 | -2.95513 | -49.36352 | 2024-09-26 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README58.md)
