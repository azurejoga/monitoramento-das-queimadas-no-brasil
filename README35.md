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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 951ff36b-1bd6-346c-91ee-c39eecc13d5f | -11.3447 | -45.57533 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06ad1227-7786-375f-a082-08f69d6c6d7e | -11.43595 | -43.61469 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e68bd247-06ef-39cd-a4c8-0e0ec7d91629 | -12.82917 | -47.98036 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 148bb836-48fd-3d28-8270-4853cce62b57 | -13.74912 | -46.90604 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7445edf8-a732-37e8-82ed-4a11a5371658 | -11.1184 | -48.37482 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69457d95-48cb-3190-bc3c-16b0167cac2c | -11.16138 | -57.18694 | 2025-09-09 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ce1a59f3-cd12-3ddf-96b4-d61868826278 | -9.15269 | -45.5749 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a1935c8-75e7-3ec9-8b20-529b006cd3ea | -12.95243 | -54.80757 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08d5b79b-e268-3c97-b170-c27a33bcdf4a | -12.18243 | -53.88083 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5292bb35-7896-368b-a79b-4209272f68c7 | -14.27035 | -45.03693 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b142fd33-4c7e-3e40-a602-c160386a1dec | -6.61956 | -53.37476 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18053799-53f1-3ebf-8293-bf3fe6626db0 | -7.91183 | -46.85155 | 2025-09-09 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f50e88a-92a3-33aa-b24c-93d197f81080 | -12.92593 | -54.76874 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fe3ded4-eea4-3726-92ea-b85511437e25 | -12.83297 | -52.94452 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1d6d25e-056c-3c21-80fd-f8facd99a770 | -11.11617 | -48.36726 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7da0ab9-f926-36e2-8793-2567308cd5d5 | -7.77179 | -50.76913 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29410a5a-2ad1-38bc-a1c2-b4a1269f1ced | -13.12932 | -54.92013 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 559151cf-43ff-3eb1-b417-86d659a810bf | -10.90442 | -55.70438 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4458d861-af74-384e-bc83-f4219df9296d | -10.28142 | -48.81519 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31d9754f-0d12-30b3-be6d-f1e0e8e9d71f | -14.24534 | -44.95336 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b03cf34f-5c87-37cd-9bc2-d82131d0dda4 | -13.65482 | -46.98299 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c512e50-fa15-3bbf-bbb6-d40466bccd3b | -12.83445 | -52.93584 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f8d839-38a3-339c-b228-366fe2e309c2 | -12.83253 | -47.981 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25acdb4a-30e2-3909-9662-12e203125df3 | -10.29518 | -48.8138 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7047023c-fad7-31c8-9ac5-a846d058631c | -12.90273 | -47.99583 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25167dc1-e693-36ae-94bc-6f0ec313bdb2 | -10.41462 | -59.59955 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77e1a6bb-115e-3a55-9989-9aeee519cb57 | -10.16181 | -46.21253 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b02b014b-f385-3052-9a86-8157b9a8b956 | -10.97325 | -45.1105 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 83045ba9-a0b2-3e3a-b05c-d4d5ef326df3 | -12.8611 | -47.97456 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 396d365c-7a4f-37c6-9a6a-21b6dc0057cc | -12.19255 | -53.92067 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71e08feb-1a41-36af-9fc2-6f7fcd08c89d | -8.3564 | -47.65574 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c63a1fe-f054-3cd9-9240-58616c3f2884 | -8.34039 | -45.05139 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85d35d9f-8351-34bc-95a2-63f5867d3559 | -8.3391 | -45.06005 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3923dfdc-0baa-32c3-8987-0be833026e12 | -12.61297 | -56.96699 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6a4315b-685a-3916-b9bf-17568608c014 | -13.13473 | -54.91344 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 866bcb8b-cbc9-3042-a2d1-d67886c483d5 | -12.83645 | -47.97786 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d04ec3c2-c613-3725-aea2-a3b3a7b43078 | -7.87281 | -46.24976 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9292e90d-20bd-38fe-8fcd-5fe97c1b1d0e | -11.20693 | -54.9957 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 284bf876-5a39-316b-8885-61e6bfd53fe0 | -6.55121 | -54.99215 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0be8e26-9c39-3ae2-bd7d-5b16698faefd | -7.72725 | -50.34791 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3b8aa89-4633-351d-9fef-74d76cf41cdc | -11.31302 | -46.52684 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e33a0a78-ab39-3160-a3ca-67bec7f380ad | -8.04271 | -48.64133 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf209e00-c6f5-38ab-824f-3c91fe276611 | -7.71615 | -45.15479 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0f14b57-c249-3922-8a39-4958ceee0869 | -10.15559 | -46.20004 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 943e9bd3-d5ef-376a-b368-4f712f4901e9 | -10.74987 | -47.74115 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38d1eacf-900b-38bc-95cd-1ce3232ddd3f | -9.09571 | -45.7124 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab2653ba-d411-3556-a2a1-8add639160ce | -8.21365 | -44.76731 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2c5105b-da0c-3a03-ba7f-0a155bb19aa3 | -10.74638 | -48.1857 | 2025-09-09 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60d35fbd-2c4d-332b-995a-87e38d69f18f | -11.42611 | -43.59363 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb3673b8-3168-38b1-9312-81af65ef2b96 | -12.84099 | -52.94146 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 05e2649b-850f-3388-9393-44506ceed3fb | -11.41571 | -43.57658 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddc8b7f0-f00e-397a-8831-fd55b8bd156d | -10.89315 | -55.69929 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fcb32c0-d12f-3542-b3d4-4e526c854158 | -14.35384 | -47.32646 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b7691a2-ddde-3249-9a36-975fbf7f054e | -12.82203 | -52.94262 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44c1d81e-d373-3def-b223-80dee21d2726 | -11.43338 | -43.63354 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7177b89-afe2-3156-9183-19feeb9487ce | -11.16481 | -48.36092 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddf8cea9-a13f-3f79-b6b6-c3d8574fd1b6 | -8.61006 | -54.66796 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b91be823-3dbc-3b87-9d8c-f1cd3122b672 | -10.74692 | -48.18216 | 2025-09-09 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7d9259cb-036f-3bfe-93d3-30a696b1b954 | -11.31007 | -46.4977 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9c79e60-563d-3a43-9e09-01ac3918a222 | -13.8225 | -43.86323 | 2025-09-09 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb9ef91-13be-35e9-afd4-4535ec4ae22a | -11.20345 | -55.06556 | 2025-09-09 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96d9083c-652d-3f29-b465-64f5f16f1249 | -7.78923 | -46.08231 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 018dcde9-3312-32fa-8473-3dc25a7e3f02 | -12.83589 | -47.98165 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea0ec09e-25f5-3341-9fd7-025f90de54b4 | -11.12512 | -48.41922 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84b03e9d-5083-3d0e-94ab-e657040923bc | -10.96757 | -45.12372 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e52452c3-a86b-3c03-9258-00245b3a9637 | -14.32773 | -47.32314 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7d0d4426-bf1b-30e2-8601-3930655d2534 | -8.36218 | -42.23524 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0054ecdb-7d9e-39cd-8e68-45eb41658a09 | -7.4369 | -49.26772 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7331611a-4fc6-358c-8ba5-c7082357a95f | -11.66298 | -46.89355 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9e8c4a9-5208-3a79-b585-9dab578473e8 | -14.16855 | -48.98818 | 2025-09-09 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be3a9c67-ef02-3797-86dd-ad9712558d0c | -8.60574 | -54.66722 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b7e71cf-9b4e-3190-aa72-24d1c823c962 | -8.6781 | -47.20105 | 2025-09-09 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 043a42eb-d8c7-372e-b36e-ffc90933ad10 | -11.84366 | -46.77983 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc68f55c-bd6f-3edc-bd06-2838f9bc662f | -7.82482 | -44.92074 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc055c2b-ae32-3282-9115-e317bf6206c0 | -9.14552 | -45.57383 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f54ebd2-4d0c-3e48-a32a-0954f40b4b5f | -10.97196 | -45.11969 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| dc4bc33d-f473-3822-be9a-a3fe434194c7 | -9.16841 | -60.79905 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76656b57-8101-3071-8947-7b9aec2ad65b | -12.85556 | -52.94399 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39c0c619-91d4-378c-8651-69fcfb2749a7 | -12.90326 | -47.99228 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ac29ee2-3bfc-391e-991d-496f967034ba | -12.88466 | -47.97847 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deaa1ca3-9b64-33a2-84a1-8b3588147d80 | -9.48051 | -60.49368 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9979813-1313-3c5c-b178-f83172ad545e | -12.19623 | -53.89359 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 65395955-23b8-3b89-a359-7963cb4e46c0 | -9.71158 | -46.81882 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3eefa350-630e-3112-b534-a553ed47e86d | -7.56813 | -44.66127 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9d8c525-4d19-3b87-9863-dc4f47d0b8f1 | -9.25149 | -57.07016 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4501d78a-3026-3723-93fe-f26b73d69569 | -6.54664 | -54.99137 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a305002-c290-3607-ae23-43c7ae7e13ed | -13.82462 | -46.23545 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3452d0f-b454-3752-a036-3d3d6a65976c | -10.02348 | -48.30925 | 2025-09-09 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2b6a359-a8cf-3f0f-a957-511958000b06 | -11.8448 | -46.77206 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a646319c-3ed0-3336-959f-5400ef55fd49 | -8.06756 | -48.63815 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e42a25e2-ce95-347e-8e5c-2726c5d0f301 | -8.48252 | -48.26768 | 2025-09-09 04:34:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b5054b9-dda9-397a-95c0-b1bf613b6e0e | -11.437 | -43.60698 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a90b0f36-2af8-3a81-8d44-e06978f95d88 | -7.36557 | -44.31116 | 2025-09-09 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec584f1d-4e51-38c0-b1fb-fc91944e8af6 | -8.9196 | -47.8837 | 2025-09-09 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 608f20d9-7bfb-3597-966f-d60d56aa9c5f | -7.74714 | -50.74497 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0c75654-1e3a-3633-b06c-4df02191a4a4 | -13.91502 | -48.05268 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e3fe915-24b6-31b6-9e44-a3c7a300e4c3 | -12.41031 | -47.79575 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0963d67a-363b-310c-a39a-5d384d50c322 | -10.71863 | -47.94566 | 2025-09-09 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3182e083-61fa-358e-ad38-ed3ddd6501bc | -11.9456 | -50.97033 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ab23ff7-f7bb-3a5b-98ea-e08fd25d9052 | -13.04691 | -47.15105 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README36.md)
