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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08ccb253-01b2-3526-8ca9-d2c5990fe4f2 | -13.39663 | -47.03677 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac6c5c43-32fc-3efc-8516-26be429e0dc7 | -14.27634 | -51.88686 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 95357360-cbb8-3484-bfe1-0b1d64976aab | -11.90061 | -46.47009 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d32709d-bf67-3daa-a4f3-ea57d5df771e | -12.6373 | -48.20054 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 762ff1dd-c0e1-388f-81f5-0c8dbb496f27 | -14.81013 | -46.72896 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8498a174-4dc0-3955-8282-6401d5011bdd | -15.21529 | -56.05689 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b03bacd8-bc85-3937-9dbb-99aba2452b1f | -15.71647 | -42.60046 | 2025-08-31 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 903e7b93-fe95-3529-adfb-e1f3832db7ad | -12.41157 | -46.46386 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 971abdd2-86b9-3bd1-8a5a-12ec541fcd9d | -12.9887 | -44.85489 | 2025-08-31 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7880b99-2a22-3ef5-a5b6-cd8b8f4e3009 | -13.30494 | -46.91404 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bbec38e-6dd7-3d46-a4df-7a55a136ac83 | -14.55397 | -51.9843 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 727536db-77b6-3d80-a85c-a6a3ac42e8d4 | -11.89922 | -46.38477 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2dfe8985-ba22-34ce-aaa6-1993692028b3 | -11.86861 | -46.50425 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d706b0c-d3f2-3eb8-97e9-6d01172b83fd | -11.89276 | -46.42107 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0cba820-4139-34c4-82c2-c8161be86e75 | -17.15122 | -46.0835 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5e26b2e4-62c3-3d3a-a4ec-77ef500f68c8 | -13.5398 | -46.96396 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61b3493f-83fb-3ed0-ad77-ef2befe06de1 | -12.3155 | -45.72842 | 2025-08-31 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 5b616cb5-6965-3040-b00f-b16fc7f2f9d1 | -17.91637 | -46.83949 | 2025-08-31 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c088066-6fe5-3b27-bae7-9bbcff2a9486 | -11.91259 | -46.40231 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0bf73356-92c9-3741-8150-98c5c7f8628f | -13.34342 | -46.93585 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6082d28b-6bbf-3b09-9e9a-96f5ded8086f | -12.85747 | -48.08473 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a66de55-d76f-3cb8-b222-1fa24fbdf3f6 | -10.95707 | -50.85559 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1224b8c3-a7e4-3edc-8869-9e5f995d2698 | -13.6764 | -46.92595 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00c98c49-4a74-3cc7-bc5d-531a5a01375c | -15.2141 | -56.06234 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17afea74-aa24-37c7-860a-f81a419caa63 | -11.91619 | -46.69036 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f89c3c8-dddc-3894-bf16-512c65c1fbfc | -14.22766 | -48.06599 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 754778e9-4a6b-3dc1-a11e-cf320b22efbb | -13.51982 | -46.97853 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b22f3218-75a9-3bbf-b6cf-7bd2bbf2bafc | -14.81453 | -46.7495 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29beb0b2-b652-3080-953a-41483ab7b9ab | -14.99142 | -46.70632 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db212c8d-283d-344c-9bb5-abb484320af1 | -13.52447 | -46.97578 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25c5795b-234f-3ec4-8621-0b956372a974 | -11.8986 | -46.38824 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e50156a-c82f-3f82-a879-7c7bb0dab8d4 | -14.03843 | -44.55183 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 699fbdb1-b0c3-30f3-9c28-1f3866c8a2ea | -11.84062 | -46.78439 | 2025-08-31 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea15de87-0fc7-3ac4-9d4f-347a4e84f9de | -10.9673 | -50.86129 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dacbeb8-7698-3261-88b4-21b0a506dd97 | -13.52903 | -46.97739 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f3cb056-52f6-339a-ae5e-71f57e9610fd | -16.21781 | -52.65684 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c7484bd-03b5-3c4d-b727-5363f15f77bb | -11.79952 | -46.47216 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82af70bf-ddce-3f2b-b4be-875575a57897 | -13.30603 | -46.88403 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b22d739-6fbb-36ba-a93c-7360e4148be7 | -14.54186 | -51.98785 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2826cc4b-e239-3011-86bb-052b6d0dc92f | -16.22438 | -52.68126 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 928fb9e5-db0f-3423-9ae7-799c5b6335f2 | -13.47055 | -46.97421 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa0342ad-1b6c-312e-b7a7-9c97c51afd5c | -15.94345 | -41.40074 | 2025-08-31 04:04:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0533b53-eb18-3a9a-a10c-6eb73f893295 | -10.95774 | -50.852 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f0121a24-df30-3c00-8a29-5e197944d6af | -12.86181 | -48.08577 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95b82030-b405-385b-94c7-a0fd027cf17f | -12.68119 | -43.16516 | 2025-08-31 04:04:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 18476264-497c-3908-90de-c6c84196e967 | -18.79629 | -46.82783 | 2025-08-31 04:04:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 962ae9c8-9659-3ba9-a176-3fc8d80850cd | -11.89342 | -46.72448 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31124d94-32c1-3a13-ac75-d4790119d00a | -11.82743 | -46.52624 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 476a9848-e66b-398f-a8f2-179835f44e6c | -17.61824 | -44.25101 | 2025-08-31 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9348c07f-a439-3b95-a985-5789e138fc8c | -18.05855 | -45.94581 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cd72399-b8f7-372e-a0ee-38abd316c57f | -13.46583 | -46.97724 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8fd95419-5444-301e-a909-0fe6581af690 | -16.23472 | -52.65251 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64c47efa-7fee-39e8-8e4f-0b94ae1b7216 | -13.97433 | -46.3211 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b58f6587-2b49-3c6b-9943-4a8028c6391a | -16.22411 | -52.65435 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df6b4710-0028-3e9f-869b-219b55da98ea | -17.72116 | -44.39334 | 2025-08-31 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84f1f99f-192a-375f-8ca2-9f571793fc47 | -11.89648 | -46.37701 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f37d37c-b3d8-3924-9dba-d2f06e1074da | -14.03226 | -44.48046 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82d0159c-cf2c-38e2-a20f-7f288cd15bf1 | -11.8968 | -46.72918 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0506d983-0361-3bea-bacf-5b5a5258967d | -13.48028 | -46.94295 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97c4d7bb-50a9-37fb-b4a6-44dadec9e811 | -13.65597 | -46.92435 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ede958b4-08cd-3a14-9348-fca27eb124a5 | -11.88467 | -46.72636 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a2d32c5-eaa8-38cd-9850-96d5f4cde568 | -13.36051 | -46.95705 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 898b37e4-defb-36e0-8ce8-104c54e50df3 | -18.06212 | -45.94648 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30811277-f60b-3808-9b3b-3a3e2cddf4d3 | -16.08044 | -43.61808 | 2025-08-31 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c778075-8a55-3852-b613-ccb3aa28130c | -11.81066 | -46.45592 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 288b8aec-64b3-375f-91d4-fb11a09f84d0 | -11.88127 | -46.72172 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ef5258d-ffad-35f4-84be-a1c4fe1ed97a | -14.04261 | -44.54841 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 152bcc91-f5c8-3839-b9a5-f74fd6205bd8 | -18.05498 | -45.94514 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8f661cd-6e3c-3f04-a94a-ba9ba9bf4c64 | -14.26055 | -48.05556 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bddff9ba-81ad-376a-90e2-de9f795343ec | -11.89662 | -46.46925 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90ab7176-160d-3ffd-ac62-9a4fc0c84727 | -13.57748 | -46.91619 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5f55cfc-11e8-3da0-aeec-b4f0ee40b4e2 | -11.80605 | -46.45861 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1572f939-22c3-3592-b824-e653d36b6d49 | -15.71978 | -42.60101 | 2025-08-31 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 541a8697-2cd1-3f65-8dcc-c011322653ce | -13.35228 | -46.9563 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 884eed17-cc22-312f-b9ad-4c6a4388329a | -17.96559 | -42.98532 | 2025-08-31 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6b3c200-18b7-3293-ad7f-ad46959e5a3a | -11.0605 | -52.04639 | 2025-08-31 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a38f2a74-6a0b-3212-9d25-9bac89ce2649 | -11.88789 | -46.708 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffe170ec-d6be-3c5b-a632-4b87662bb2b7 | -13.33123 | -46.86495 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 514ced28-770c-3d89-be82-ddb7354850aa | -13.3301 | -46.86505 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e666450-2633-30cc-bcac-c932a76c7869 | -15.94622 | -41.40492 | 2025-08-31 04:04:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45a8827b-3cc5-35c7-9a62-816c2fa79c25 | -11.83711 | -46.42294 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fcde0c4-3a23-3235-a85b-e79ae9ee093c | -11.81188 | -46.44895 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2df237a8-7214-39dd-add7-e0a084fdfac5 | -11.48637 | -48.29454 | 2025-08-31 04:04:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24fc2801-74f8-322c-bcf0-56bd94f60159 | -13.52835 | -46.97743 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0b37786-deab-3565-a144-80e54e619962 | -14.23773 | -48.0594 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41550514-ab50-3d3f-8e53-4f97f9cc90b4 | -19.45386 | -45.30785 | 2025-08-31 04:04:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2acc50cd-e29f-3620-b6ed-f56c6f98d7db | -13.36115 | -46.95343 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eea11147-4ad1-3afc-9a6c-e2cbafc6d481 | -10.95229 | -50.85094 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4c56b540-d369-3082-b741-4e73a1a14489 | -14.81937 | -46.74491 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d96e487-b909-314a-8879-530dbd47cb55 | -13.34702 | -46.98574 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d405b5a-aab3-3b8f-b65b-1a216c2eebd6 | -11.90338 | -46.69159 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28eae294-31c6-32ff-981d-194ce84fa5b3 | -13.32374 | -46.88334 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5710c3e5-31af-3629-a945-07f24af967d6 | -12.56591 | -44.79922 | 2025-08-31 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b9d1d5e-be70-31f3-a02b-88a8cc7b2ed8 | -17.14632 | -46.06845 | 2025-08-31 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12170f65-c019-36d4-beb7-d10e71eb57b8 | -11.88331 | -46.73405 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04ac936f-6e0b-3e94-8903-ef3a4baf197f | -18.66159 | -49.09225 | 2025-08-31 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cf905c4d-c601-31e7-a4ed-7816e6aed3cc | -14.53827 | -51.97721 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a1b7d65-174e-34ff-a614-925235694d47 | -13.48558 | -46.95998 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57db0b00-52e0-3e45-8353-d68d769fa20d | -12.4076 | -46.4631 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01804a00-1354-3562-a158-741d3b5543e5 | -10.95364 | -50.84377 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README28.md)
