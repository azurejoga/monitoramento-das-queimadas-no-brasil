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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aa26810-b7a9-3c69-ac94-d9fa1cf661d6 | -9.3174 | -50.821098 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7d90fb6-8f38-33cf-acb0-d0386bc6b0de | -9.2998 | -50.786999 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e71cd02-b300-35e3-91ee-687e21fdf333 | -9.3017 | -50.796001 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662c77c7-3bc7-34a3-94d4-a6b0be9a5a7f | -9.3037 | -50.805099 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff607cc1-3e29-389b-8353-3e94784e4cae | -9.3056 | -50.814098 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b31c9f0d-ccf4-3fa1-88ca-6d9d7e4faa2b | -9.3076 | -50.8232 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fba96a27-4f48-302c-bddd-4f4454cbde9b | -9.2939 | -50.807201 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c6716a-319c-3788-a856-b1b82474b8ee | -9.2958 | -50.8162 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04c7f811-007a-3500-a5db-00c7ecd08859 | -8.5063 | -47.311798 | 2024-10-04 00:43:57 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd2eabbc-34db-3aef-a398-a0b3be721b3b | -8.4525 | -47.121101 | 2024-10-04 00:43:57 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63568189-b64d-3762-ae01-2df5dfb6f1d4 | -9.3128 | -51.131302 | 2024-10-04 00:43:57 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba18e495-ff1c-323c-ad08-b0fdabadd5ca | -9.0144 | -49.810501 | 2024-10-04 00:43:57 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04000cd5-b3e0-32f0-9f08-185cad70744e | -9.0161 | -49.8186 | 2024-10-04 00:43:57 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbf9075b-e209-31a1-9a3d-d6445187ebe4 | -9.0046 | -49.812698 | 2024-10-04 00:43:58 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd786483-cb03-3b3d-aef5-765e7bb3c104 | -9.0063 | -49.820702 | 2024-10-04 00:43:58 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61e21888-3aad-3d7e-abfc-458435931ede | -8.9108 | -49.666698 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c68a506-85f7-3880-b4a1-e38579d3ddf0 | -8.9125 | -49.674599 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd7db57b-f95d-35ca-a7fe-720e25ebc7d2 | -8.9142 | -49.682499 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ae2ad69-2e33-3be1-aa40-7206245bc391 | -8.916 | -49.690399 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9327189-016d-33f9-93b6-95f9430dace9 | -8.8992 | -49.660999 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53f5db80-dd3a-3c87-b0ae-36e09f411095 | -8.901 | -49.6688 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbc786d5-626c-3532-b481-82e0a4b1f276 | -8.9044 | -49.684601 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c60ffb99-34b8-335d-99d1-183a8cf03462 | -8.8842 | -49.639599 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46c1b299-9f08-39b4-a05e-a697ea159bc8 | -8.886 | -49.6474 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85580147-e8c9-3e3d-a4c4-148c633cff58 | -8.8769 | -49.699001 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18a43d87-5385-3326-abc6-16a0670d62ae | -8.8786 | -49.706902 | 2024-10-04 00:43:59 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 862a2c9b-e724-3b5b-b437-dc19e638ccb2 | -7.8544 | -45.333199 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8550bbcd-abb9-3001-b049-14e3e2cc2ef6 | -7.8561 | -45.340599 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e6b21413-2e17-361a-9b0c-673722dcf567 | -7.8578 | -45.348 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb5db636-a540-3750-b67b-918be6cd3202 | -7.8596 | -45.3554 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0ae92ff-3d62-328e-bd6a-97bbf1416b86 | -7.8463 | -45.342899 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc110196-f1a2-3b81-9668-d1455937be4b | -7.848 | -45.3503 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a7daa1b-7abf-34af-8f78-9b7dcd0e30e4 | -7.8498 | -45.3577 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 682f9bfe-8af5-326d-ae8d-4f524c893274 | -7.8515 | -45.365101 | 2024-10-04 00:44:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4692fcbf-3023-3714-9acf-f145cd3f5885 | -8.3624 | -47.540199 | 2024-10-04 00:44:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e89b6ef-c374-331a-b0b9-ef53ec42b9dc | -8.351 | -47.5355 | 2024-10-04 00:44:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be31ad03-aa10-3adf-be04-ee3ecd027c26 | -9.1001 | -50.905899 | 2024-10-04 00:44:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9be2c48f-d771-3363-839e-5a7b3abe4194 | -9.1021 | -50.915001 | 2024-10-04 00:44:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab90822c-440c-330c-80e6-bec296354d25 | -9.0883 | -50.898899 | 2024-10-04 00:44:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e83772c-61fc-33bf-aa76-0f919bc9e9b8 | -9.0903 | -50.908001 | 2024-10-04 00:44:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90a761bc-7e99-3e64-9ebb-b49e775e24d1 | -9.0923 | -50.917099 | 2024-10-04 00:44:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a573a9c-6218-30aa-979e-cda5e1791a6a | -8.559 | -48.869801 | 2024-10-04 00:44:01 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 945f8735-bd6f-3802-aabe-b9f66c285bc8 | -8.6395 | -49.0923 | 2024-10-04 00:44:01 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49f37667-0e18-3fa5-b0a6-9670d4a07bb6 | -8.6412 | -49.0998 | 2024-10-04 00:44:01 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf563e3b-2ca9-3a29-a1f3-da4b5f05bf3a | -8.7756 | -49.938599 | 2024-10-04 00:44:02 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5088a6-4ce3-31db-bc37-d0ac02e345e1 | -7.7294 | -45.416698 | 2024-10-04 00:44:02 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 020e2bdd-ed55-32cb-816d-d5062d665a50 | -9.1095 | -51.517399 | 2024-10-04 00:44:02 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed0e1edc-67ca-31e8-8d2e-3940b01b1902 | -9.0997 | -51.519501 | 2024-10-04 00:44:02 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7987ce7c-6b91-31f7-8c70-5356f03c44d3 | -9.1019 | -51.5294 | 2024-10-04 00:44:02 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db900cfe-4eb5-308e-b6b8-9ca2509d11b9 | -9.104 | -51.539299 | 2024-10-04 00:44:02 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8f0c67-0e2e-34aa-bef4-27d0338e0ae4 | -7.8508 | -46.206902 | 2024-10-04 00:44:03 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 563b3677-1644-390a-bb5f-cdc60df73e76 | -8.6429 | -50.0354 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d61c9c0-df79-39e6-8d36-e49ff3d9062b | -8.6447 | -50.043499 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f1d17b-6c41-3a6c-a230-04a08c016b7b | -8.6465 | -50.051601 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3a52ef-edac-3a42-92da-9321fcf9677b | -8.6482 | -50.059799 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986dba24-a399-35d2-a7c3-39fe5589cd43 | -7.6128 | -45.536499 | 2024-10-04 00:44:04 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2e68e9d-ca55-352b-823c-9cec89848844 | -8.6331 | -50.037498 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21977f5c-a9f7-3d1b-9102-2d1c34f72727 | -8.6349 | -50.045601 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f42cf080-edbf-3923-8a43-3e49c372c5a6 | -8.6367 | -50.053799 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| addb19f2-98c7-3ab2-935b-65df259adf64 | -8.6384 | -50.061901 | 2024-10-04 00:44:04 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f055ff-b85c-305b-acd8-9b78a9413244 | -7.7447 | -46.149502 | 2024-10-04 00:44:05 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32efa0eb-ff75-3c69-82ba-4ba8921f0e6f | -7.3865 | -44.7015 | 2024-10-04 00:44:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed3f233-1d99-364a-a0b1-4002fc007ae2 | -7.3767 | -44.7038 | 2024-10-04 00:44:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffa93ec7-0c4f-351d-b341-8b2dba815154 | -7.3786 | -44.711601 | 2024-10-04 00:44:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 872a1b23-f244-36c6-8da2-551e34ed0fea | -7.3688 | -44.713902 | 2024-10-04 00:44:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee4a547c-de1c-33fb-b430-f3c3b05b7767 | -7.3706 | -44.721802 | 2024-10-04 00:44:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83e8ecca-3b45-32fd-9cbc-7f7c38de944d | -7.6924 | -46.146599 | 2024-10-04 00:44:05 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca7265ef-8d35-386a-b205-c5ab24a5a6ec | -7.6941 | -46.153702 | 2024-10-04 00:44:05 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2def3a50-77dd-3a39-b2c9-fa7a8e7b54e7 | -7.6957 | -46.160702 | 2024-10-04 00:44:05 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9c0038e-62ce-302a-a01c-9f05e8e8f5d6 | -7.6843 | -46.155899 | 2024-10-04 00:44:06 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 204249b7-e119-365c-9623-081b9b81c0a6 | -7.6859 | -46.162998 | 2024-10-04 00:44:06 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcb233ad-c577-3fef-bd25-7c7f3fd3b1d8 | -8.3329 | -49.516602 | 2024-10-04 00:44:07 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b684c6e-663c-330f-8669-29e0101b1fd1 | -8.3121 | -49.561501 | 2024-10-04 00:44:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23cfcdcf-b7ab-3ef8-ac0d-3f83ba6b2687 | -8.3138 | -49.569099 | 2024-10-04 00:44:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b14f87a-a8cd-3a8e-90a5-3f6eb27a3145 | -8.3155 | -49.5769 | 2024-10-04 00:44:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1261630-ebcf-370b-bd26-858589eaf150 | -8.3023 | -49.563702 | 2024-10-04 00:44:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3358f7fc-f594-3257-acbc-4d13fcfdcb39 | -8.304 | -49.571301 | 2024-10-04 00:44:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a79289f1-2405-32d5-a8d6-82bb0ab9d3b5 | -8.3057 | -49.578999 | 2024-10-04 00:44:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fffd2218-cf15-34b8-8fa9-a137a681d69d | -7.8006 | -47.471298 | 2024-10-04 00:44:09 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddb78bb8-f5bd-3456-95d1-f2789b6ebd5b | -7.2224 | -45.588001 | 2024-10-04 00:44:11 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35d29103-01bd-3354-aed8-be7bc0ffc826 | -7.2241 | -45.595299 | 2024-10-04 00:44:11 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd90930f-7c10-32ec-87dc-f756c54c1f2e | -7.2258 | -45.602699 | 2024-10-04 00:44:11 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd4b6fe3-e1dd-3ef1-a893-9e9ed0a92ae9 | -7.2126 | -45.590302 | 2024-10-04 00:44:11 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4a03a0-70a0-3845-ae22-b78e9864b63b | -7.2143 | -45.597599 | 2024-10-04 00:44:11 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84787679-02df-3a7e-92bd-7b41d7c4a2c8 | -7.216 | -45.6049 | 2024-10-04 00:44:11 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a07437e-9b25-3366-a499-c97777ca4d45 | -8.3423 | -50.862999 | 2024-10-04 00:44:12 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9e89ea-2f37-3d7b-9ed4-8e1b0ff12ab9 | -8.3442 | -50.871799 | 2024-10-04 00:44:12 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1b0d3b5-6cb9-3dae-befe-1328f9ae5560 | -6.6928 | -43.947899 | 2024-10-04 00:44:13 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5c802f8-3ba3-382c-8f2e-d1ab54ac8c59 | -6.6948 | -43.9566 | 2024-10-04 00:44:13 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32ebde65-9e28-3dac-be44-1fc3f94bac77 | -7.0392 | -45.333199 | 2024-10-04 00:44:13 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7183d40d-d9fb-3089-804a-592083541aeb | -8.2914 | -50.911098 | 2024-10-04 00:44:13 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4255e960-7513-3f9d-8789-d26cdce23b50 | -8.1653 | -50.4771 | 2024-10-04 00:44:14 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83119dbc-6bc4-38bc-8b2f-dc3ade45da94 | -8.1671 | -50.4855 | 2024-10-04 00:44:14 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 647ac802-efe0-35ac-b386-6d6564c917bc | -8.169 | -50.4939 | 2024-10-04 00:44:14 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29ea55c1-6eb6-3e83-b6e5-d7685cf57a5c | -8.1573 | -50.487598 | 2024-10-04 00:44:14 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59af2273-ac85-358d-8e2f-666a11a48ef7 | -8.1592 | -50.495998 | 2024-10-04 00:44:14 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae851b3-0a0b-3605-b888-2ce8711048fd | -7.213 | -46.661598 | 2024-10-04 00:44:15 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5a663fe-beca-398d-893a-8a1aa25f3c79 | -6.9282 | -45.476799 | 2024-10-04 00:44:15 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17ddd59f-b09c-310f-9d3b-d0259ede01ab | -6.9299 | -45.4842 | 2024-10-04 00:44:15 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53977c5c-29d1-3a07-b121-d5191069db1c | -6.48 | -43.746201 | 2024-10-04 00:44:16 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
