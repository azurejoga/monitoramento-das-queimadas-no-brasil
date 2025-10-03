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
| bf00f8f4-8812-3fbd-9135-2e70410b24c4 | -13.77413 | -47.58389 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 910d500a-0bdd-37b7-bb31-bf8bb2cc5e7c | -10.88562 | -44.29955 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d871b1-9e43-3910-a717-1143271b311d | -12.63466 | -46.97462 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6139311b-eb84-36d1-90bc-8f3d39bcbf67 | -11.08974 | -47.70639 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82916064-3c4d-35b1-98ef-f8061f6346be | -10.00538 | -48.26794 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b35b5c2-7619-394d-84c2-6b77c5617820 | -12.93789 | -48.43557 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98df6b8b-0dfa-3dc2-b2f6-40422649f362 | -10.92772 | -46.73339 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64ebca83-fc02-3670-ac30-8ccb031628b7 | -10.44282 | -49.35722 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 912aa9ea-a1d9-3ec4-80a4-b2cf00940e79 | -14.35778 | -43.84492 | 2025-10-03 04:12:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d168a3a-171a-3f01-9429-d34fa5edff22 | -12.64007 | -46.96569 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd4904b5-e19e-3e03-9949-0e3481d7a0c6 | -13.55958 | -47.28978 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41a57279-b1f2-36ab-bd77-9578ec3771fd | -9.76149 | -46.3109 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7e086b60-d82a-36c6-be43-f7d1cebac69c | -11.13313 | -47.19732 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 674a9573-cd13-374a-b69c-a01578a74e97 | -13.56247 | -47.29581 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7548e6ca-7384-3f0c-bdc8-02228f07fa31 | -11.79519 | -41.19754 | 2025-10-03 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5d3f1dd-6ad7-3bb3-9a65-ab241cfdbf69 | -12.64222 | -46.88489 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb7eeb33-8120-3b4a-a409-6b0fd3b1b46b | -13.47857 | -47.24319 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 409d29f8-487c-3d8b-8e72-b81342e5139f | -14.46877 | -48.41269 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a893cc4-25b6-3589-91da-409c331518aa | -13.5764 | -47.28289 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 784c26ef-25a1-34bd-88f1-b236c0df1dcb | -11.4632 | -44.95825 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3491cbb-142c-35ff-9a46-daf2c011425b | -11.34681 | -44.94348 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaa23f56-b1f9-32ee-8363-8968ba860a63 | -11.82535 | -44.91391 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4e482e9-bfec-32d5-a905-2da3cda69d2e | -13.5727 | -47.27459 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc9b8d8f-84c5-3590-9e9d-8031a9811fc4 | -9.58717 | -43.32591 | 2025-10-03 04:12:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 51692bf5-4ed6-3492-9044-1d35b578937f | -11.42443 | -42.11217 | 2025-10-03 04:12:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 689ab3fa-2fbd-3e50-a31b-4b174e7d3073 | -13.19057 | -47.81923 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d8a4510-1743-331e-a7f2-67197a8add48 | -10.89118 | -46.71741 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51faf07e-06c6-3477-82b5-cfa0a6e159ce | -11.55729 | -46.99989 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aa0b36e-49bb-331a-af32-911ff62a231c | -10.01019 | -50.24736 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0df7ecf1-8159-3973-9ddb-2ab116f61252 | -12.20035 | -47.78664 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd3f29f7-2222-31c8-8a3d-bdb660b7d280 | -9.87627 | -47.81566 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7219760c-1880-366f-845a-36a87c8d102e | -13.32927 | -47.60219 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| edb143e4-9579-3c09-bc0d-2bbeb92576d7 | -14.30801 | -45.87661 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0967d5cc-12e1-3322-9055-8de59a7658ad | -11.56853 | -47.66064 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e7ddc02-090f-3e79-8af9-a560817c63bb | -11.49799 | -43.50453 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f883b3fe-3b99-3a0c-b637-c756dbce98ec | -9.04502 | -46.67577 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41316d6e-9e08-3b10-8b03-4920059347b9 | -13.58003 | -47.59042 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| daceca8b-75b3-30ca-bb03-b674489532b0 | -11.55749 | -47.65323 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd8a0cef-cabd-3600-a8b2-5a2f49b0643d | -13.96698 | -48.16681 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6e44431b-fff4-3657-b10d-f23583149e70 | -9.93109 | -43.76272 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1bad37c-5480-36e1-bd96-17a7ee0b7f30 | -11.55258 | -47.65765 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ae600af-77d4-33a3-b375-2f0316f9f065 | -10.87864 | -47.82162 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 206cb044-e7ad-33c9-8159-54f809d84e85 | -13.55693 | -47.58604 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30e09d05-5a87-33da-91fb-88698f69fa3a | -12.93522 | -46.39204 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f64221a-1c4c-3479-87fe-41cf41e3abc5 | -14.1173 | -45.65769 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca17bcec-f54a-357d-9a2d-f587afeb39f0 | -12.38043 | -46.51521 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c734be33-2eee-3f4e-9b94-960f6ce7f85f | -9.94328 | -43.75734 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80286279-d49d-3dee-bf3c-a5f19eac0a91 | -13.76902 | -47.56792 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f1f4ea7-784a-36e4-a7f3-48a22964ce8a | -13.38504 | -48.12996 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a37d1e-5978-3bb6-a1c2-242b6ea146ac | -9.41142 | -47.53521 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 747c8db3-d18a-3c02-917a-70ba8fc2fbe7 | -12.63924 | -46.97057 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| adfdd0c1-641d-3a2a-b749-f687b5856d27 | -13.14287 | -47.83604 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3df4cc81-9157-3056-b4e6-bddbe8a8ffd5 | -8.12744 | -50.23972 | 2025-10-03 04:12:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7ab38eda-bb51-30b8-af62-7581a275ff1e | -8.75364 | -47.33255 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ed23e1-b68f-337a-8ee3-ee382a706491 | -11.82474 | -51.77669 | 2025-10-03 04:12:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d6df8f8-03d1-324f-85c2-4c22bd0531f1 | -10.75635 | -45.3486 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdc1e646-8ab4-36de-8ddc-db2be4722cff | -14.35827 | -46.13522 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbcf54e3-4deb-3515-a248-5ee890d119eb | -12.75691 | -44.90743 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0373dbb-41ae-3cdd-a9eb-cf8234829dac | -8.64913 | -47.71421 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c9c7ce9f-1fa0-3886-8c50-1f41a4d3ef8f | -11.59152 | -47.67044 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0ef0e0b-2afd-3bfc-9d66-191d211e410c | -12.91988 | -46.37193 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 385e655e-e356-3d9f-8b51-bc33e514284b | -15.17674 | -43.62442 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d19b175-fdbb-3fce-a8ea-383477ec26cf | -10.9378 | -51.0675 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19075dc0-5eb5-3f35-b941-6b7195144dc4 | -10.43829 | -49.35631 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0eb6a67-81fa-3a43-ab1c-0e6badeedc40 | -14.23233 | -46.10884 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a72d5de-34c3-3a8d-98f6-a727cc7b93a2 | -10.10638 | -50.35593 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 49e29a66-d846-3a47-8017-7a46b029565b | -11.62765 | -45.03604 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e91135af-5ab2-396a-986a-05e5315ea63f | -9.18474 | -46.20239 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1be9c21-fb41-37dd-9f92-d734a487294d | -11.07029 | -48.36343 | 2025-10-03 04:12:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7f2ba8a-972c-3704-9993-78e29901a8d6 | -11.14011 | -43.39871 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4e72648-1b92-3161-923e-04f67eb61286 | -9.44601 | -47.3659 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a556b188-a50c-3083-ac95-282dfceac4c4 | -11.91076 | -46.75274 | 2025-10-03 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a0af966-6be6-384b-9c3d-cad921f794fd | -10.96508 | -44.32762 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efe52ff3-7f37-3c83-a694-c5f15078809c | -10.06673 | -48.18698 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eef179a-e405-394c-a426-c2d3e6886dab | -11.56079 | -47.65244 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c4489ec-f5c4-38f6-8d35-ae5fdbfd6afa | -14.46475 | -48.4121 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89c0e1cb-41f8-3737-8460-f2a7a44f2be2 | -12.75286 | -44.91062 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c95f7a55-9fa2-3418-ab12-8803c026a24d | -8.81156 | -46.66833 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2ede6ca-ba00-3c2a-917e-aa50aa009013 | -11.61896 | -45.06686 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbcf3fbd-f7eb-3b5b-90da-890bc7d5fc6d | -13.96242 | -48.10178 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b662d693-3ead-3668-aec8-ebbbfa15aa28 | -12.76159 | -44.90046 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 730d9a00-16d7-391c-b3f0-3ef065a1c04b | -13.31763 | -47.18705 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78c7b56c-abca-3203-8978-6e291c24f70d | -12.62042 | -46.96689 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e26c9dc-5146-3b7e-987b-b5c7540e948e | -10.16852 | -45.49687 | 2025-10-03 04:12:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a8293a2-8e6a-3c45-8dc3-4a11de7bd05a | -13.96463 | -48.11211 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a48f22c0-f35d-37e7-bac2-092c67ec6cb3 | -9.95083 | -43.66148 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b7c6231-cf5d-3074-9827-abb9cdb2d556 | -9.94001 | -43.57806 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5fc4b4d-220c-3bcf-a73b-f942fc9f6dfd | -12.72452 | -48.58171 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2a01695-8919-359c-b687-94f3cf20941b | -11.90658 | -46.29289 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f024588e-4f92-3eeb-bf37-ebad5eac6663 | -12.8093 | -46.85922 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e76133ff-9e8c-3e90-aa03-5405114fd99d | -11.67308 | -44.27243 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63744570-9570-36af-8b78-466a761fcf66 | -13.56934 | -47.58333 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4cf9ca28-6546-30c5-b838-b172e7e72349 | -11.9029 | -46.26965 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b40875e0-f64c-3d0f-8fd1-71f104d4b864 | -13.17679 | -47.87389 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8744070-a3d8-3044-b9d0-27d4ac748e48 | -13.3397 | -47.79379 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b3e62ab-a8d7-3a5b-b3ea-8bb3c3f845c6 | -8.80998 | -46.67096 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25156640-34e1-3a83-9b9a-5203d4e5a9cb | -14.5765 | -48.33978 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb4f5837-6668-3410-984b-6f99ded54649 | -13.75699 | -47.97796 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85ff3ae9-e2b7-3f0f-a14f-7a69228e7aa1 | -13.66814 | -47.30984 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b39b21af-e24b-38a1-8ee0-1dbddb66659f | -11.13617 | -47.203 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README63.md)
