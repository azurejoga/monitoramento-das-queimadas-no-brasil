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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 666e1669-747e-3647-97f4-23d2ca6bd330 | -6.3282 | -62.68153 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bb835ce-7fab-33ad-b971-a9a834c0fea9 | -11.19652 | -54.12296 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9dfbfb9-db89-3f6b-bf44-26661c367c2a | -9.02067 | -61.0165 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb74f4c-edce-360c-be7b-effa51fe175b | -12.61643 | -50.78103 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 491a05e5-89a2-3941-8306-60faf83f67f8 | -11.81424 | -60.4621 | 2026-09-16 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47653689-3d4f-3fa9-8890-071f8aef3996 | -9.02788 | -61.01406 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a19d596-7176-3e8f-be21-e13a3c9e4555 | -12.76492 | -51.2644 | 2026-09-16 05:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9c70504-bf22-31c2-976d-42653ad910db | -6.45054 | -60.01165 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424626e4-0530-3eb3-86b2-8da9331bc4b2 | -6.80979 | -58.99293 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd9b083-4f16-35ca-af9e-32778cd3cdd0 | -9.05868 | -65.92068 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53ac6b2f-b574-36ba-942c-e628110900eb | -6.80923 | -59.17543 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5e6090fb-3294-3353-854e-dc85bac220fe | -9.70415 | -52.02319 | 2026-09-16 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6d3931e-12e9-3031-aab2-e1ee21ee3d5d | -9.78469 | -60.4812 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3532be99-3713-3c53-8551-1fe1f68f71d6 | -9.85207 | -65.18732 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e62f8bbb-e46c-30ec-8998-880f659dfda5 | -10.89492 | -54.01391 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae58c28-457f-31b2-8fad-1cd1d6896cac | -6.02351 | -59.93012 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f888035a-4419-3495-9b9d-91d4320563d6 | -6.77105 | -58.81324 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a46881b-5fe8-3cfe-b516-c8cd322e7de6 | -6.79564 | -58.79045 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef0e597-5f2c-3033-ac6a-cd053a2cc736 | -8.33295 | -51.31064 | 2026-09-16 05:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aafca859-520f-3b2b-be73-fde6257ef086 | -9.81238 | -48.9172 | 2026-09-16 05:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cf507fb-ffe0-35c7-aa9c-517101c8a924 | -10.39892 | -61.1969 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8900afb7-f3d0-3c7f-9190-0732cdc99946 | -10.14563 | -61.17852 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e7d66f-0e71-33ca-ad01-056953918002 | -6.7539 | -58.81058 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df1b1426-0f48-3b53-9f37-918d498e4f06 | -6.69619 | -56.41171 | 2026-09-16 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b7d3930-8d10-3428-9005-8a2b3c65f1be | -6.75447 | -58.80686 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 551d388c-5986-3090-bd9f-8b92d7c8b297 | -9.56432 | -59.31181 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca7d94e8-b0be-3fdb-b786-9e4b3e367f9b | -10.86326 | -50.81212 | 2026-09-16 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4506b701-3bdd-3cf6-bae9-766a1db497b8 | -12.63689 | -50.76474 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dd31d2ad-fe5c-3fea-a934-41200ceceac2 | -9.71001 | -52.02043 | 2026-09-16 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 902910ce-6346-3597-8b42-e4e658c4f4ef | -6.80618 | -59.17183 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e00a7690-0217-3481-aae8-aad7116c7687 | -11.20037 | -54.1246 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86cf05df-cc7c-39fc-a45f-8654225da747 | -7.65292 | -67.16238 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00418415-9e3b-30bc-b85c-9c54e60ea468 | -12.61751 | -50.77174 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| eee88506-d099-30d5-8ec3-60c809791eb4 | -12.13677 | -57.18356 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28c1cd31-7f9c-3bd2-8e9b-4d6cfea83a81 | -9.67805 | -65.79644 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1627bfe9-ce85-3994-9717-585948052b64 | -9.14073 | -65.84618 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f7daec3-56ec-391c-9e4e-6717eb346056 | -7.64316 | -67.17152 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ff9cb37-be25-3112-979e-b1de1fdbe7ea | -11.1956 | -54.12382 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc06ba9-27cf-393b-be33-82aa54010bc1 | -6.12222 | -59.88097 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75ebd916-34ba-3595-801f-c31a18926c7e | -7.61592 | -67.2511 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f972f78-e768-35eb-92fa-943e70591629 | -11.98391 | -52.47235 | 2026-09-16 05:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97c1a5a1-7b60-34d4-a11c-d221dcebeb6b | -12.11556 | -57.19083 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ab3981c-ade4-347a-9772-8de8ab7a5df1 | -6.77048 | -58.81694 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa29b96-0bac-39c1-8d2b-f2143792c227 | -9.89704 | -67.00372 | 2026-09-16 05:36:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96708a84-770c-3fee-b03f-23b2cf2cd74b | -9.92248 | -60.46618 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0b29c3c-3da5-3f43-8220-3d09283f52bc | -9.51037 | -59.50292 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2102bdf-9282-3ab8-a197-54f8930f75f7 | -7.63876 | -67.17076 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4d5c516-6f00-3cb3-8aa5-0a027ac64e36 | -9.07084 | -65.93134 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea9eacc2-be6f-37ab-8f2f-6e40295994a7 | -11.80804 | -60.45735 | 2026-09-16 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba54def-94f7-39c6-a81a-8580f129761b | -10.90588 | -54.00491 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97f80a8-0516-339d-820b-2b7451343b74 | -10.41118 | -48.65509 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfa360d9-94af-328d-9618-041b11cc16ae | -9.84632 | -48.36049 | 2026-09-16 05:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f90f43b5-3e94-3f08-847c-8056144c2085 | -7.65708 | -67.16957 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cd69270-d4d6-3302-abc3-b8feeed6e12e | -6.92996 | -63.13464 | 2026-09-16 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69dfdf14-078f-38d0-b146-88869ba95dac | -8.32739 | -51.30989 | 2026-09-16 05:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a4d151c-d1b4-3d7c-98a9-2fc801ee8658 | -6.32187 | -57.74556 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d1c0dff-01b1-3f5c-aa37-13349b43247e | -8.64881 | -66.59598 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f72c708-6c90-3d2f-a79d-2eb206a7e84e | -10.41182 | -48.64992 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83fc52f1-4d74-3952-960e-11c4b1d39764 | -7.64829 | -67.168 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a91979e9-ed35-3f82-a7b9-c381ca5c3829 | -9.10925 | -65.55811 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8463dd20-1fa3-3300-a313-1c830ae367d3 | -10.90659 | -54.00362 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c88adf4-49cd-3f7b-971b-105962704e79 | -6.95577 | -59.53048 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d56981bf-23b1-32d9-80c4-4038162d9505 | -8.41139 | -54.71912 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce082a11-f4ba-3aa7-a9d8-33da189fbc82 | -6.33089 | -60.0173 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd6e6a0-8763-38ac-be03-a8c4a850e461 | -10.41798 | -48.65554 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5f7dbed-6fd9-326d-b3f4-565f8e0935a6 | -9.12803 | -65.84925 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47610904-21e8-33de-8137-9ed1edd84a5f | -12.12096 | -57.18117 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf9b2a21-cc73-341a-a84f-cf392d3596bd | -6.80675 | -59.16821 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144bd2f4-c4c7-3351-a448-e6f3f49ab449 | -6.69407 | -56.41418 | 2026-09-16 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e94be287-832a-3815-be1a-b0c96e528886 | -10.54419 | -57.45545 | 2026-09-16 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95e1d133-a46a-38c1-8dc6-fb80d7c26f78 | -9.22027 | -60.291 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d76472d6-38ad-30d0-8529-9c884b819abf | -11.41194 | -51.42437 | 2026-09-16 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76d037e5-8825-3fc9-92fd-198f3a02e4e6 | -9.80507 | -48.92206 | 2026-09-16 05:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 152bcca6-9f59-3d67-98f0-f5fb70e8854f | -10.39503 | -61.19987 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeb85cfe-c623-3456-9011-a6c5cd172c0c | -9.13198 | -65.84991 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cec64b07-1b0e-369a-959e-3b49e4b1eb43 | -6.76705 | -58.81641 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4158b746-00a4-3352-82b6-3254bafde330 | -6.80562 | -59.17545 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e94af9f-b7f8-3687-9f92-0dcfcf69b8f0 | -6.33105 | -62.68588 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 66c0f863-354b-3fb1-99eb-e7441be473fc | -6.71261 | -58.80848 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4413bdd-3806-367f-8fea-7f93253bfd9f | -8.64947 | -66.59219 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 880837b3-8ebb-3031-93a2-b451fedeccbd | -9.83549 | -57.70315 | 2026-09-16 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc07e312-48a8-3623-88b3-7f85b5445556 | -6.83199 | -58.98512 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec9ba2b9-14a7-32f9-bc18-7e6654a9f38f | -6.32698 | -62.68912 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcb10e26-43b7-30e0-8a98-10bc32b1be29 | -11.97849 | -52.47161 | 2026-09-16 05:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91d10ecb-c149-3863-85aa-a07de03e2846 | -9.26142 | -60.27885 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9089a91a-2da0-3991-9477-59f59ba883ed | -8.87744 | -62.51516 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9856f7-ed32-32fc-af91-8c955ae04b83 | -11.19417 | -55.02534 | 2026-09-16 05:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 051e27df-ab22-3adf-82d8-41c731ab4b44 | -8.66526 | -66.50186 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62daa751-6943-3842-a8f5-d668ab2126da | -8.71145 | -62.8459 | 2026-09-16 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77a8b84c-8cc6-3b73-b53a-0960dbca4e62 | -9.39239 | -60.31028 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 57353ade-4d4a-348f-aabf-b57befa25c22 | -6.34145 | -62.68758 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b4e537b-d7b4-3d1b-a4b0-60e01cf8e0ff | -10.54799 | -57.45602 | 2026-09-16 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb14774-ade7-380c-9c46-57146826ec4f | -6.34838 | -62.68871 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88594991-db0b-3904-bb81-40331d8c280f | -12.63134 | -50.75932 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 564fca9b-2698-3f6f-a4b7-905a213af652 | -8.85298 | -62.36325 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fcc6700-a8f1-377e-8950-0985e617f780 | -12.63744 | -50.76008 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7264a323-fb4b-3bdb-b79b-7e56245147ca | -9.13284 | -65.84484 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4101d12-3ecb-37b1-9807-85c8cf3316d4 | -9.72472 | -64.91096 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6f7c30c4-f7a3-3fd5-ae5b-e0fc15f0e4bc | -9.49351 | -56.75296 | 2026-09-16 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76bfd803-2266-3acd-a658-61bde4fa78c3 | -6.75235 | -58.68869 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README59.md)
