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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0d4ee45-515c-31d7-b5f0-5c072f0305bf | -11.8627 | -46.0622 | 2026-09-02 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5b0d37a3-9e53-361e-9c0d-97e99e35ef7f | -11.3048 | -45.1575 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 6be4bdcf-a32d-3e9b-a4b4-7105ed6fbc0d | -10.802 | -50.6965 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e86885e6-553d-3903-be74-632c41b3d2f1 | -13.5724 | -59.7362 | 2026-09-02 13:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6bdcf24b-d24b-3171-b7f7-f86d2a09ed0d | -10.7774 | -44.7463 | 2026-09-02 13:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 908033ca-afb3-36ab-a640-ab799351319a | -10.7268 | -50.6618 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| be33e1fe-8d55-3d53-949e-47b71efdc51c | -10.4148 | -49.9683 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d4a4af13-fad6-3d7c-87cc-9620b4eda88a | -9.2141 | -48.0119 | 2026-09-02 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 63b23f8f-886d-3756-94af-70e3f21ca7a9 | -8.7613 | -62.5869 | 2026-09-02 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e8124c85-47bf-3722-a053-b0ededa24225 | -7.2258 | -42.7379 | 2026-09-02 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| a04fb47a-0c53-36b1-bcc2-17f7f4eb3125 | -10.3007 | -50.023 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 9eb0158c-a0ea-362a-a67c-65d71ae7de05 | -13.9662 | -58.6936 | 2026-09-02 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| a8bf341f-6bb4-380f-8ceb-311bf06660b7 | -11.5483 | -45.4446 | 2026-09-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| b8787cdf-8921-3cc3-b3e4-501c3c4b54cd | -10.5788 | -47.7306 | 2026-09-02 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| c5fb62ce-5c4b-389d-85d1-2c6952e18783 | -12.3615 | -50.5632 | 2026-09-02 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 605ae137-6ed4-3234-9b2a-4203ed7bd651 | -11.3579 | -45.4027 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.6 |
| d7e92b3f-7c24-327e-954a-9fa99390480f | -10.3004 | -50.0445 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6411138a-c936-3ee3-ac61-a7d1c19d334f | -11.3771 | -45.4 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 420.9 |
| 67421c23-4b0e-3094-813b-4ad5873a5440 | -11.3044 | -45.1805 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 06257eab-b16e-3e70-90cf-2f3e4f2e30c7 | -5.5648 | -60.2121 | 2026-09-02 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3c2d4e92-d5d5-3f87-8719-79d082ea4dd7 | -13.9853 | -58.6919 | 2026-09-02 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 43f5ac39-7b95-3e4e-b5fe-6bb1e285dbc8 | -10.9752 | -50.4864 | 2026-09-02 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a00ef438-3601-3116-bbce-bf0c3fa6ee43 | -10.301 | -50.0016 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1a997026-110c-3828-bfbb-fa2e14226771 | -10.9562 | -50.4884 | 2026-09-02 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 5e5ce8e3-9f9e-3a3f-b7b0-c2e38b1750a9 | -12.1504 | -47.1283 | 2026-09-02 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 87a7f611-d98d-3d14-9590-6f1b343a5956 | -11.5287 | -45.4703 | 2026-09-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 37f6f506-8a73-3112-a61c-2e99dc70e0e0 | -10.4145 | -49.9898 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 40c61dcf-1ef1-315e-85b4-6e4f8a9a98fc | -6.5486 | -58.5413 | 2026-09-02 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 3de0e5f1-a748-3fa2-9b5a-6ca9c01348a0 | -6.6542 | -59.426 | 2026-09-02 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| fd26970c-5f15-331c-944f-68c6090a29f5 | -11.5283 | -45.4933 | 2026-09-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a0284052-90a0-38dd-af52-083568b6f105 | -6.6764 | -58.7686 | 2026-09-02 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 24a5d6d1-2cfc-3d2c-8a5a-1da0dc3ab3a0 | -9.1533 | -59.5027 | 2026-09-02 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1199a696-eae2-3ea2-9286-6340decc6978 | -1.4761 | -54.2365 | 2026-09-02 13:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 0e1ea003-d718-3845-9060-fb44d5b80f4b | -10.7647 | -50.6579 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3c7c13d8-c602-34c9-ad1e-8f5d95fa0a0b | -11.1723 | -51.294 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7e150c25-4847-3151-b608-165b529558f0 | -10.7431 | -50.8514 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 552f0d17-5236-3b38-acad-91369ed79629 | -13.9664 | -58.6736 | 2026-09-02 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4eca1feb-b16d-3206-ba19-751e203960d3 | -10.4334 | -49.9878 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| d7f08618-77c1-31d1-85a3-2df3b8b1d555 | -10.4142 | -50.0112 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| eceb7828-e91e-31a4-b070-80c5d7043c59 | -11.3431 | -45.1521 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6578a64c-f69f-3bcd-b448-7b833b7724b9 | -10.3193 | -50.0425 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 3392e02a-a59d-35eb-9d00-6091eb6ededc | -10.3199 | -49.9996 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c42cb52f-89c1-3b9f-a393-b2d537082269 | -12.1312 | -47.1309 | 2026-09-02 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c94ff29b-1ac1-3b3a-a1cf-1cede53db2a8 | -9.2144 | -47.99 | 2026-09-02 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 27b08d04-cdef-37e2-bf2b-11c0f5a7c17d | -7.3671 | -60.6067 | 2026-09-02 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d1384d37-a206-3a63-b26f-80e94418c9a7 | -12.1504 | -47.1283 | 2026-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 35deaff4-e544-3889-b197-52f8b35d747f | -7.3007 | -49.8187 | 2026-09-02 13:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9e7eb058-5149-3764-ae68-1da845329779 | -6.6948 | -58.7678 | 2026-09-02 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 99a1303e-dccf-3b3d-a584-45fe77f26228 | -11.0563 | -51.4751 | 2026-09-02 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| aab279f5-a8b7-313b-ab0c-08302de4534a | -6.6949 | -58.7485 | 2026-09-02 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 71bcf491-90ea-3cdc-bf65-9b0c4786159b | -9.1955 | -47.9919 | 2026-09-02 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5079552f-9aaa-3aa0-bfa1-8907c2af8784 | -7.3486 | -60.6074 | 2026-09-02 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 2dbfb477-2e70-3470-a0cd-f4be1031230a | -12.0936 | -47.0913 | 2026-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d09d3eb2-e9ea-3233-a3eb-1f9b009ca011 | -6.6358 | -59.4267 | 2026-09-02 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 639ac267-04f9-3e52-a718-e91b4597ee80 | -10.4142 | -50.0112 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4806623a-0031-39ca-b7c1-e067f770bc02 | -8.4298 | -54.706 | 2026-09-02 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| bda12362-2ffb-3213-81f1-9393151422d8 | -12.1312 | -47.1309 | 2026-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| be0d8e3c-2242-31cd-9373-0672b0e34332 | -5.5832 | -60.2116 | 2026-09-02 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 278.2 |
| f2f94215-16d2-317a-9696-3873e5eeb5cf | -12.8843 | -45.8183 | 2026-09-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f8639c20-9b7b-3695-97e5-208ce89182e5 | -8.7613 | -62.5869 | 2026-09-02 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e00f6a55-3e17-387a-b212-aef85c893056 | -5.5648 | -60.2121 | 2026-09-02 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 119e6450-4a52-3f13-ae54-713fe169bfaf | -8.4673 | -54.6833 | 2026-09-02 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| cb33953b-a3f9-3c3d-894f-d734c11ad864 | -6.6765 | -58.7492 | 2026-09-02 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c779add3-7583-324e-ad71-8044e859a6a9 | -10.7774 | -44.7463 | 2026-09-02 13:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 49110498-9a32-376d-bb2a-a1c16bfed8df | -5.6016 | -60.211 | 2026-09-02 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 795b80a7-3caf-318b-88d7-8c9f024d8246 | -11.3431 | -45.1521 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7a95dc54-66ce-3d63-b3dd-28e337cb427e | -12.1132 | -47.0661 | 2026-09-02 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9ea37dee-ac2c-3d9a-aa0b-7ca85225b266 | -10.4148 | -49.9683 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 129cbed7-7398-3392-a338-22ce00a8c034 | -13.9853 | -58.6919 | 2026-09-02 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b4f00db1-df96-3059-828e-074a3d2ae071 | -13.9662 | -58.6936 | 2026-09-02 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ba4cdc5e-daa6-3f0a-934f-f66e885781d0 | -10.9752 | -50.4864 | 2026-09-02 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ef62c93b-21db-38ed-83a7-26ae9c10be69 | -11.1723 | -51.294 | 2026-09-02 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e6ce108f-0b6e-3928-a19b-e34cbb515641 | -11.5287 | -45.4703 | 2026-09-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| c1fdc4d5-d1c9-3337-b426-712d2ab019c1 | -8.7817 | -46.4623 | 2026-09-02 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| fb08bc14-a3ba-3fa0-8e43-cd39b568c65f | -10.4145 | -49.9898 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 08e6fa97-39ff-3a3e-8f64-2dc4741e89ee | -8.7819 | -46.4399 | 2026-09-02 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 916804d1-b167-3f12-b94d-ad928c2f6774 | -10.3196 | -50.0211 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 25c310eb-ac66-3dd9-a1ce-849302199a15 | -5.5833 | -60.1924 | 2026-09-02 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 209.9 |
| fb84b5f6-5144-35ef-9c22-617d4c307022 | -7.3487 | -60.5883 | 2026-09-02 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 194301f4-947b-3220-87eb-3077a47b8284 | -6.5486 | -58.5413 | 2026-09-02 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 984d0d0b-3e32-3594-baee-0bdad12e25d2 | -10.3007 | -50.023 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 825882ee-2a93-3224-8a2a-24c2b6fba935 | -9.4159 | -45.6271 | 2026-09-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| e5e39519-d68a-310c-be9d-bc17ed6bf9aa | -11.112 | -51.5536 | 2026-09-02 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 202061a3-ea0a-338e-8adc-c273e15314c7 | -11.8399 | -51.0513 | 2026-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c535074d-82a2-3a16-9240-bd4d3ef2067a | -7.2006 | -60.6706 | 2026-09-02 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a6798cc1-6120-315a-a4b0-f8b1c26aebce | -10.7431 | -50.8514 | 2026-09-02 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7347c334-acbd-352a-b4fa-81ad660e2463 | -6.1474 | -57.7605 | 2026-09-02 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 580c7b12-f682-365b-9f83-545cec0a81cb | -9.1533 | -59.5027 | 2026-09-02 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d4a06e80-bb12-308d-930e-1d0ba0ccc938 | -11.8208 | -51.0535 | 2026-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 813c32a3-b4bf-30cb-81c9-d02e98d269f4 | -6.6764 | -58.7686 | 2026-09-02 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e49cef9c-96ae-311a-a6fa-8a2b15e41bf5 | -10.5788 | -47.7306 | 2026-09-02 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| bcbeb8b1-ae48-322d-af4d-460ace774e93 | -10.3004 | -50.0445 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| eead0414-4022-3d98-8dc3-8ed0d82107c7 | -8.4481 | -54.7452 | 2026-09-02 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 042afbcf-8495-39aa-9271-9b2cc640aae1 | -3.2455 | -47.9187 | 2026-09-02 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f5020fac-91a8-3599-9a96-60223dc78a83 | -13.5724 | -59.7362 | 2026-09-02 13:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 62d044c4-686d-3928-ac9a-4e2dc2766283 | -9.2144 | -47.99 | 2026-09-02 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| d867d3de-5825-3b4a-9ecf-5374892e1c33 | -8.4485 | -54.7048 | 2026-09-02 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 61f96b8f-8de4-31e0-9796-e7b56f91505b | -6.6541 | -59.4452 | 2026-09-02 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 89c8cf5d-7330-312b-bb71-dc23fc61d241 | -11.5475 | -45.4906 | 2026-09-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 47c8d86d-78ff-37f6-9ec6-34675afce6a0 | -7.66 | -45.8764 | 2026-09-02 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |


[Clique aqui para ver as próximas entradas](README74.md)
