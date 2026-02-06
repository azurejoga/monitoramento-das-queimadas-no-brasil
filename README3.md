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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c69e0b64-fb42-3986-9566-2df9bcb9f486 | -3.18272 | -48.01929 | 2026-02-06 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4ea41d40-108b-3baf-8f2f-bab3fb2a76e4 | -2.68318 | -48.82474 | 2026-02-06 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0619d4c-ef27-3939-9f57-4b137a89fcdc | -2.99127 | -52.36398 | 2026-02-06 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b284c46-a3e7-3ef9-97e6-f67463040feb | -7.46057 | -46.20623 | 2026-02-06 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d23691ba-31fa-38c3-a5af-0f4bfd04d666 | -16.58176 | -57.79746 | 2026-02-06 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a37cd7b9-85d1-3d39-8d45-4d9aeaf85b91 | -6.84245 | -48.83914 | 2026-02-06 04:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 586f3caa-5275-3391-975d-1cd8808a835b | -7.90509 | -50.3756 | 2026-02-06 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbbf63e4-83ec-399b-adbe-8e2609209020 | -16.58852 | -57.80379 | 2026-02-06 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4bb3433c-0535-3da0-aa91-922313b568e5 | -11.17285 | -55.92057 | 2026-02-06 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e924db5-de6f-3d57-9a37-6383497c483a | -9.18291 | -58.0583 | 2026-02-06 04:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e71ed81-b54f-369a-9882-31cbea6ccda0 | -15.46872 | -60.05743 | 2026-02-06 04:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368d78c8-4f91-3802-a1fc-1efb3d986adc | -6.83895 | -48.83861 | 2026-02-06 04:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7e90360-73e8-3dcc-9ec0-ee5454a9f736 | -11.17657 | -55.92117 | 2026-02-06 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a1b3fb6-1f34-324c-b72b-8652507d5fbb | -14.87388 | -59.4958 | 2026-02-06 04:53:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49efe670-d98f-3d72-be2f-67bc53b92a94 | -15.46958 | -60.05284 | 2026-02-06 04:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0ab514e-34e9-36c8-b0e3-bdca2f6a6d88 | -15.44667 | -56.32888 | 2026-02-06 04:53:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7650b3fe-b5df-3164-a53a-85ffbb508cca | -7.00029 | -44.8327 | 2026-02-06 04:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c99919f6-9dc9-3216-a8c2-a17bd658f3f4 | -11.18029 | -55.92179 | 2026-02-06 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 245e423d-b63a-337f-8dda-c3f754778f41 | -9.17853 | -58.05754 | 2026-02-06 04:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd77eb51-0c07-3e8d-8056-9073db6c7593 | -22.02674 | -54.00809 | 2026-02-06 04:55:00 | NPP-375D | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c705ca4-a77a-31ee-ba8d-7f7aaf6d49da | -23.47582 | -51.58807 | 2026-02-06 04:55:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d0a2526-270e-3d87-9fe9-011fec2cd23a | -23.41433 | -55.22536 | 2026-02-06 04:55:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a70699e-e149-3a89-8f40-3d9a6eb6cdc2 | -20.01067 | -57.38387 | 2026-02-06 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 90144d5a-146d-3188-929c-9119881e4f25 | -28.98074 | -50.68071 | 2026-02-06 04:57:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25bd6ee6-d2b1-34c8-ae1d-ac2c92465d69 | -30.10481 | -50.68939 | 2026-02-06 04:57:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 7625c9a4-3fa0-356c-ade9-b806d3ad4f95 | -31.78238 | -52.50468 | 2026-02-06 04:57:00 | NPP-375D | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 9004516a-98f4-3726-9a48-03c220fe242a | -31.43936 | -54.5672 | 2026-02-06 04:57:00 | NPP-375D | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 675f53d9-f874-3847-a809-ae64a7f03574 | -28.82634 | -50.3007 | 2026-02-06 04:57:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8542ba6d-3371-3e5c-b198-6e826463c4d8 | -30.32011 | -51.00908 | 2026-02-06 04:57:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 0373f36c-53f1-32f4-b7c1-1862f056359b | -32.14373 | -53.12561 | 2026-02-06 04:57:00 | NPP-375D | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 0dcab25b-2d79-3b21-9870-faaf73291104 | -32.13996 | -53.12498 | 2026-02-06 04:57:00 | NPP-375D | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 25fa57e4-8d4c-38df-b781-d58d216f317c | -6.5631 | -51.1126 | 2026-02-06 05:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2dab9353-5de2-349f-8ea3-ac313781704c | -2.98748 | -52.36035 | 2026-02-06 05:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0efb5fe-4a2f-3f82-89a0-cc5af536993a | 4.34213 | -60.94139 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6efc48b6-f0ed-3186-8855-ecd3e0c9d7af | 4.34011 | -60.92767 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc4cb50-a72c-3047-9a51-75dba1b80bc2 | 4.21037 | -59.97476 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d34ee910-0a48-317d-a6b8-89e84af663f7 | 4.41228 | -60.6291 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd9089cd-e5bb-3362-8f28-595da7cb3777 | 4.40151 | -60.64283 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69bfad8d-1799-30ce-abd2-2a9f617aa220 | 4.22203 | -60.40962 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09eb6b8b-1357-375a-9b57-234640699256 | 4.3379 | -60.94224 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c504fe7-2336-36c5-9540-ac52cddbbadb | 4.25068 | -59.87437 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dc5e8a1-87de-30a6-9ad5-34460997e4a2 | 3.74359 | -60.72143 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98c638cf-aa18-34a4-9848-2e94d8e622ef | -2.56536 | -54.74378 | 2026-02-06 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba04ba39-d983-3908-971f-122f1cd61744 | 4.34636 | -60.94058 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bf5941a-c841-35b6-aa35-672dab7986ac | -3.182 | -48.01842 | 2026-02-06 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 49dc3bb3-8456-38d0-b483-dacf5c99b254 | 4.41259 | -60.65985 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2eb7ce0-6951-35a8-9c9e-2df788acf177 | 4.37208 | -60.65382 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35a3e99-2851-3cc7-b111-6c03ff795dd6 | 4.25219 | -59.87582 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fefc7370-5646-3b87-8a3c-5a4f4befdf51 | 3.66477 | -60.71727 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98909376-2eb0-3482-a0ac-dc9314096fc8 | 4.21789 | -60.41003 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a978aa7e-2f8b-32ab-99f9-304c8b66a28a | 4.33587 | -60.92844 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3e9d800-c6ac-3eb0-a2e7-ad4bf41ec573 | 4.34321 | -60.91925 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14b320ac-24f4-3085-a2a1-d16d14cf179b | 4.21435 | -59.97408 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b5dd371-b513-3716-8cd0-160b441e945f | 4.59769 | -60.6587 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f9ea7f4-f511-3071-a520-67ad936b2be7 | -2.5751 | -54.72632 | 2026-02-06 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1fea96-0d7a-3093-abba-d2cace8c0645 | -3.18057 | -48.02794 | 2026-02-06 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4f92a64-3e43-3b8a-ab76-8773447983b7 | 4.24435 | -59.82508 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39faef35-69ca-3c9d-b920-d04a364d5dbb | -1.96608 | -54.69795 | 2026-02-06 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7efcb3b2-60b2-3ce7-a65b-9a07f42980cf | -3.12201 | -52.92618 | 2026-02-06 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d175a03-6da1-3da8-81f0-2cb7b0a7e067 | 4.20793 | -59.98564 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bcf5d0c-1563-387f-b8fc-dde8900f0210 | -2.91945 | -54.0276 | 2026-02-06 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a98e675-4e87-3a24-885f-920a3d9e25fb | -2.89596 | -54.20052 | 2026-02-06 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35940913-4d0c-3eb2-a957-da35263433f6 | 4.24394 | -59.82861 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d513cad8-fbca-3f39-93cb-52281f4a51a5 | -2.91592 | -54.02706 | 2026-02-06 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cb68437-0bea-391f-8c33-eab772e8bd33 | 4.4128 | -60.63255 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07037964-3339-317e-b94d-c5a4b4a94651 | -3.14678 | -48.14679 | 2026-02-06 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16f0cfa0-b1b3-365d-91c5-cad701a48fde | 4.57543 | -60.65326 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b9224dd-877d-3fff-a4e1-0501ddb7d18e | 3.70886 | -60.81157 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e8d41d3-8b92-3ca4-a05b-f3d6e91c9f6d | 4.2498 | -59.83423 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b142d118-a3fc-32df-8fe7-1f6837bbc9c1 | -2.56594 | -54.74009 | 2026-02-06 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe28f23-f1ad-3ec9-b9c3-6cc3370707c0 | 4.24933 | -59.83776 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2613bd1e-8cb9-3267-933a-6f52c28ba64d | 3.97849 | -60.0074 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51b9638c-8af5-3414-892e-38792c6c3cf6 | 3.74719 | -60.717 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 660f0070-a1e2-3618-b3f2-28776353b93f | 4.52699 | -60.95964 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8fee993-0678-3b4e-9d06-5b7d8a1da36a | 4.21088 | -59.97815 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a60e901-882c-3bdf-87d4-e68c17659d2e | 4.4062 | -60.64567 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ecfabfc-d58a-3552-b8fa-155555abe2ac | 3.66836 | -60.71287 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d52bf7d-a642-3fc7-9c61-3068875b047c | 4.21486 | -59.97746 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31556b05-efe5-3f8c-8222-16a46e6694a9 | 4.52292 | -60.96162 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b8c8454-fdd2-3f56-a3cf-fd1eaca67ea4 | 4.33955 | -60.9239 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fb9be01-272f-33e9-b297-820b4fdfe844 | 3.74303 | -60.71764 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 091db748-d793-3b18-8dde-8bcbb6493ce2 | 4.33365 | -60.94299 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13272b96-53cd-39c1-ad92-92d5a38fcba3 | -3.18249 | -48.01519 | 2026-02-06 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2479d380-0615-35e5-840a-73394f53a9cd | 4.33533 | -60.92478 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b754c25-959f-31ec-a63a-079b29a3e72f | -1.47628 | -54.11268 | 2026-02-06 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69aa50ac-115e-35be-aaa8-45f9aecb86a5 | 4.24513 | -59.83012 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b83b66e-4ba0-3f2a-92f7-bb314a2a263d | 4.13576 | -60.14365 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5b84b14-95c4-3816-856e-a2735bd796ef | 4.3976 | -60.61645 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17146d45-b2b1-3882-a61d-d6f496bf7d2a | -2.98675 | -52.3652 | 2026-02-06 05:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff0346a0-fa9e-3cac-a2ef-97fd9927edf3 | -1.60272 | -53.93125 | 2026-02-06 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d97f1506-a083-3d33-9a55-12d32ff316e6 | -2.44955 | -54.72193 | 2026-02-06 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac311275-b410-3eb7-b3bb-c01d6cab1367 | -2.78618 | -52.59577 | 2026-02-06 05:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 898f662b-bd89-36b0-bcfe-f1e8af26f896 | 4.13976 | -60.14291 | 2026-02-06 05:10:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4678fa0-fafb-3a95-a893-111be047b9ae | 4.2132 | -60.4068 | 2026-02-06 05:10:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9fe8d16-9f42-3b8a-8abc-038748d43854 | 3.66421 | -60.7135 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3369941f-2e42-38f6-a44a-db866d91e61a | 4.526 | -60.96093 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff629642-920f-37ca-ad21-6868281e5d4e | 4.57187 | -60.658 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e59f1ca5-635c-3991-b6c6-e0ff74065d25 | 4.34806 | -60.92268 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a52a400c-62b6-3c5e-b8c0-ff1f5c3d23ce | 4.40842 | -60.66063 | 2026-02-06 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bf56aad-ee8e-3593-98c4-9cb1f74c38c6 | -1.9452 | -52.932 | 2026-02-06 05:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README4.md)
