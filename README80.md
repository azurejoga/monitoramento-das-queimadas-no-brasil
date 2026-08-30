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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cedf1647-df19-36dc-91ae-7767c390f9ca | -14.1459 | -52.7871 | 2026-08-30 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 96396122-6198-356f-990b-17383e90bee0 | -11.2634 | -45.3471 | 2026-08-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a08ec4e1-3e6c-30a4-abd9-96b145feffab | -8.739 | -45.3844 | 2026-08-30 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| b27f0d2a-8ff4-3727-9941-a2f00f7e3976 | -6.8753 | -59.4557 | 2026-08-30 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 113658c6-efd7-326c-8c67-78130f030bfe | -13.8557 | -54.1383 | 2026-08-30 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 58ce64b9-2ab7-3b6f-ae41-9811a8c3208d | -6.8568 | -59.4757 | 2026-08-30 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 255.1 |
| a7800d92-e274-3c65-a364-6692d5003ea7 | -11.2829 | -45.3214 | 2026-08-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 972aa603-db8f-3113-b864-2c1ca8e57b16 | -14.4004 | -52.5438 | 2026-08-30 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e1350c05-293a-3fc1-a018-e4436d31c3cd | -12.9405 | -45.9011 | 2026-08-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 4df6ef34-0b93-3050-98f2-ae252758a3e4 | -7.5136 | -55.3251 | 2026-08-30 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 249.6 |
| a8091204-656f-3967-94b4-fa95307dbbc0 | -7.3117 | -60.6089 | 2026-08-30 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 206.4 |
| 482dbc0b-0a9b-3bd6-81b2-0ea87e836ba7 | -4.9604 | -55.8424 | 2026-08-30 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 295.2 |
| 28bc0cc1-ac4d-3d78-8419-a93a1900240a | -8.5969 | -54.7755 | 2026-08-30 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f3257be2-6d26-3b20-8917-de91ce4315cd | -14.4387 | -52.56 | 2026-08-30 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5e5a903c-dccb-3888-8f79-733412ea2707 | -8.6158 | -54.7541 | 2026-08-30 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8b742509-86eb-3090-bb0a-48b5f3a3f63b | -14.4387 | -52.56 | 2026-08-30 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 40d30cd1-47d9-35c1-8535-8fa0ecb127a8 | -8.2227 | -54.9613 | 2026-08-30 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7277b1b3-9947-3b08-a6ba-edaac5224bf8 | -7.5137 | -55.3051 | 2026-08-30 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6c4066e9-b9c3-324a-a4f4-c258fcc5cd28 | -10.7407 | -54.0401 | 2026-08-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ab223b78-acac-3fe5-9085-4d20eff5ed22 | -3.6398 | -60.5656 | 2026-08-30 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 75713add-4f23-3787-8bf9-2f84bfd5dd36 | -8.5969 | -54.7755 | 2026-08-30 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4b094399-12c2-3630-ae4d-d720591e32fc | -7.9907 | -46.5177 | 2026-08-30 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 13804606-c7b5-3b69-bc4d-f70a5b1a4715 | -11.2314 | -54.0164 | 2026-08-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.2 |
| cc7742b6-78cd-3ba0-8a27-c052ffc4cca3 | -7.2933 | -60.5905 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| df109b15-f3ca-3eeb-9e4f-2b40a1f41794 | -6.0 | -45.0889 | 2026-08-30 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 971499ec-8a9d-3211-b1bf-7120e5b0caaf | -6.8799 | -41.6754 | 2026-08-30 13:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 843c52d3-855f-3f73-8bdd-5052c0227cb1 | -11.2317 | -53.9958 | 2026-08-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 991868b0-b1ef-36d2-a071-0540800a8edb | -13.8752 | -54.1153 | 2026-08-30 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 09a6c525-fccb-3dd9-9aaf-4c745f600e78 | -7.5323 | -55.3041 | 2026-08-30 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d2dfc233-4c8e-38d7-a882-b1c87066a469 | -7.5136 | -55.3251 | 2026-08-30 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 266.8 |
| 76217fbe-f486-38ac-9e67-be52b8b5aedb | -6.861 | -41.6772 | 2026-08-30 13:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 438.7 |
| 63789467-662d-3b0d-9ae4-0f2f77d43647 | -7.3302 | -60.589 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 182c794e-74a8-34aa-97ac-0f719afb9f29 | -10.7867 | -45.3433 | 2026-08-30 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6ad31fdf-6ca6-34ef-b3d9-bb2f80f2f68d | -12.9216 | -45.8812 | 2026-08-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 46627c5e-f767-36e3-9aa1-4d23596858cf | -8.6154 | -54.7945 | 2026-08-30 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 040e2c9e-1003-35e4-9650-b192f71acfa1 | -7.3117 | -60.6089 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 431.9 |
| 2683152a-ad08-37a5-b32c-d02479808b84 | -7.3118 | -60.5897 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.4 |
| 3fffa8db-b0fd-3d8c-b26f-0a163a258878 | -8.2229 | -54.9412 | 2026-08-30 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| a5272b6d-07bb-31a6-86b9-f0cce85f9b09 | -11.2506 | -53.9941 | 2026-08-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fd5e361f-f023-307e-a722-d8afff9f1b09 | -10.8253 | -45.3152 | 2026-08-30 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3451b35a-df5a-3821-87aa-04c7964d386e | -11.2443 | -45.3497 | 2026-08-30 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 4257aa12-92cb-3998-8ac6-4da2e2e2b71d | -10.8614 | -50.4985 | 2026-08-30 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 687c4cfe-a9e9-3e4b-91c5-ffd57020a7c3 | -10.1538 | -45.6982 | 2026-08-30 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5cfbd8eb-065a-3d80-83ec-469805ed4f8c | -8.1348 | -45.4696 | 2026-08-30 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| eb14a776-bd84-32e4-9b5f-8ddcf118d799 | -8.1345 | -45.4923 | 2026-08-30 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 725acd4f-a8d6-3e59-b60b-d29ca47f082f | -10.8249 | -45.3382 | 2026-08-30 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 946f5020-39fd-3724-897c-605e7a504621 | -10.8425 | -50.5005 | 2026-08-30 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6167f4ff-3fa5-3ef0-9e0d-c5b19c1c39ad | -13.8749 | -54.1361 | 2026-08-30 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 20b29cef-67e9-35dd-8751-c75eb19ed415 | -4.9604 | -55.8424 | 2026-08-30 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 266.7 |
| 8778b6bb-7212-35c1-8463-d523b0de98f6 | -12.9405 | -45.9011 | 2026-08-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| a98d0d2d-2186-3a33-a798-419dce8ef376 | -6.8613 | -41.6532 | 2026-08-30 13:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 220.4 |
| c8e367ed-964e-3cd5-bb41-0d3fbd686b11 | -14.4197 | -52.5413 | 2026-08-30 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| ee85c333-7035-3f5e-9779-792c43e05731 | -7.5134 | -55.3452 | 2026-08-30 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| cb2492b0-210b-3066-ae0f-8a3d7d562216 | -14.1649 | -52.8058 | 2026-08-30 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 924f62a6-2f79-34f5-b98c-c1802c931156 | -4.9603 | -55.8622 | 2026-08-30 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 60cf8114-e480-3c0a-ad97-71a8f777fa4c | -5.7197 | -52.28 | 2026-08-30 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1573717d-b439-37d4-9567-11eb3e1c877a | -14.1456 | -52.8082 | 2026-08-30 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9924aada-0213-373c-8535-d41ef64af7fa | -8.739 | -45.3844 | 2026-08-30 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ddabcac0-92f8-3d15-87c8-5f689c6e8c14 | -13.856 | -54.1175 | 2026-08-30 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 21ea7535-916a-3cfa-bf8c-67847ddc564e | -13.4764 | -51.43 | 2026-08-30 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4e7ba14c-ed5b-31b1-8b64-2395db4ffb50 | -6.8569 | -59.4564 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ab70a9b2-b272-3492-aa5a-3ceb9313027a | -7.0998 | -42.2283 | 2026-08-30 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 38aadf15-395e-3fc3-83e7-812ac31e117b | -11.2503 | -54.0146 | 2026-08-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 0fa50b58-dc12-3fc0-ba83-e6e824ec90df | -8.1534 | -45.4904 | 2026-08-30 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d0a80cf7-c56b-3ce5-976b-ae9b9e6682b4 | -6.8568 | -59.4757 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 219.2 |
| d5dc4aca-68f0-35fb-8793-34fa85cd89a8 | -5.4876 | -57.1416 | 2026-08-30 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 429470f6-2d77-3f93-b181-9222ac72f698 | -14.4004 | -52.5438 | 2026-08-30 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 00dbf86a-b44a-347c-a0a7-59c17adfed18 | -12.3619 | -48.1903 | 2026-08-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 178bcf23-9126-394a-85cc-2a6d374c4c51 | -6.8752 | -59.4749 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 325.9 |
| 95b660b0-b120-3c6a-a818-20d2c9cc8813 | -15.4048 | -52.6437 | 2026-08-30 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 778a4933-ddd1-3e54-9077-1c59015c01b5 | -13.8557 | -54.1383 | 2026-08-30 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e9a7a675-9dcf-3f9a-a152-4616ee7b5979 | -6.8753 | -59.4557 | 2026-08-30 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| d3536557-bdea-3402-bf7f-33cb41111b25 | -11.2317 | -53.9958 | 2026-08-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| ef368c8a-c951-303d-bdd7-fa03ce708b45 | -14.1459 | -52.7871 | 2026-08-30 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8b93ceb8-54cf-362e-8609-afe656aef00e | -7.3117 | -60.6089 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 341.7 |
| 5c7626a8-8753-37f4-a817-c2d9d3d32a7b | -7.9907 | -46.5177 | 2026-08-30 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 262.0 |
| b0f25874-dd89-3bc4-afc5-b272029fcb33 | -13.8752 | -54.1153 | 2026-08-30 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 283.7 |
| bc71dced-8fdd-3372-8e9b-4db903680e49 | -13.8557 | -54.1383 | 2026-08-30 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 262.2 |
| 2dfb6bf4-55ad-37a8-8972-93af27fa66f2 | -7.3118 | -60.5897 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 2d8df8f4-50e2-320b-973b-55caca9c57f1 | -13.4187 | -51.4372 | 2026-08-30 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| df469846-f252-33e0-8504-b47056bcc649 | -6.8613 | -41.6532 | 2026-08-30 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 903e7052-d435-3695-b26e-7319d11b10b4 | -14.1456 | -52.8082 | 2026-08-30 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 043785ac-4a44-350b-989c-994d52076f5a | -11.1723 | -51.294 | 2026-08-30 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 70d07fd9-9f71-39b5-a1ba-13a1c56d94af | -7.3302 | -60.589 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| fd27ba3c-fb42-3473-9a8a-14eeda0c692a | -10.7434 | -50.8302 | 2026-08-30 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e8a674a8-3d3f-3945-9b56-7375336020b1 | -7.991 | -46.4954 | 2026-08-30 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| ac41d148-37a9-36b5-82e3-5d448549ae66 | -10.7431 | -50.8514 | 2026-08-30 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9f1a117e-eadc-390b-8ba8-8e8b45236ada | -7.0998 | -42.2283 | 2026-08-30 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 6b3dca60-f7d4-332f-abd7-9e6c7e6b803a | -3.6216 | -60.547 | 2026-08-30 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e254e184-036c-3550-817c-232db34f172c | -15.4048 | -52.6437 | 2026-08-30 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| cb1b49e5-9201-3eb0-b40c-c706eaf0f33f | -11.2443 | -45.3497 | 2026-08-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| e812b9a7-74a6-3300-927c-815a353b4af9 | -11.2314 | -54.0164 | 2026-08-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| f2129c30-bf35-30b3-a277-2ea1918e469b | -11.2506 | -53.9941 | 2026-08-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6dff1e0b-e0c8-3076-b1c9-c2e4e6705b63 | -14.4004 | -52.5438 | 2026-08-30 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c8a679cc-0322-3186-b6c6-4bc627c8d4be | -6.8568 | -59.4757 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 41fefc3c-f69b-3e61-9ca6-ce94df37c2c7 | -7.2933 | -60.5905 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0f989e44-bb14-3157-8145-080b85cdb939 | -6.8569 | -59.4564 | 2026-08-30 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 4c749628-8b27-3e73-8c88-abee24a99a6d | -11.1726 | -51.2728 | 2026-08-30 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 347d68c2-ca1e-3ff1-b1a5-43927897ddc2 | -13.856 | -54.1175 | 2026-08-30 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 7d147ae1-0ef5-347b-926e-9dae38f16495 | -8.739 | -45.3844 | 2026-08-30 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |


[Clique aqui para ver as próximas entradas](README81.md)
