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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 790d7e90-8fbb-3a8d-ae8a-9d723342e7db | -9.81354 | -46.62115 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26562050-ebcf-3527-913b-7a8b7d2dbe46 | -10.28077 | -48.23417 | 2026-08-19 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 410c1717-fe80-365a-a03a-21308f13c47c | -9.49689 | -51.67887 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f98eaa0-e60b-30d0-b1f0-87c64fd3bd39 | -11.40638 | -47.23822 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78522d1f-3d9b-33af-ba5c-267b5565bd6e | -8.57374 | -54.69042 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abfa3d3a-7416-3e35-9cac-2893e0218b8b | -8.58225 | -54.76917 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abe87536-38e2-31e1-b4f2-99d72c05cb7f | -11.19786 | -54.81487 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a115499-4ed9-3a4e-a814-b86a1c1775d5 | -10.76712 | -42.08907 | 2026-08-19 04:40:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c08524a-a9ad-36ec-83f4-9a81931560bb | -11.19165 | -54.82569 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfe540d9-673d-39e9-bab7-6bf265fdaaf6 | -13.29436 | -51.65062 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 738dd4b7-da4a-3321-8be2-c362751ced21 | -10.29184 | -48.22872 | 2026-08-19 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48b6fa37-36fa-3180-83f7-40ee9a8c32f1 | -9.38844 | -60.55209 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33d0f9aa-b9b3-3341-a839-3817189316d4 | -14.73991 | -48.74173 | 2026-08-19 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0771c3d-52ca-36ca-9b50-b461979c373c | -8.53018 | -54.7599 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da86f42-fd82-3882-a271-3e60bc414de8 | -8.57283 | -54.77188 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 50069078-9bfb-3eb0-9768-2760cf353575 | -15.31882 | -56.45514 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 354e17c4-9e4c-3b31-aa5d-f942dccafcfc | -9.40661 | -60.59275 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb9e42ac-141d-3e16-a88d-c6852f3bd09b | -15.77354 | -55.56851 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce71bbed-9024-3f80-8830-33cc54b30b09 | -9.39704 | -60.57486 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 719a6fe1-a832-3651-ac72-0add6315c1be | -15.7845 | -55.55409 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9922d911-3f35-3f79-9b5e-412a947236ba | -12.23926 | -43.1666 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1bac6a5b-5aad-329f-9729-04799aeac1e3 | -8.53106 | -54.7299 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 414735e8-c667-34f0-8468-30c6162619a3 | -11.19651 | -54.82256 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27630c82-d2d9-3c77-81d9-e6f284929a22 | -11.1082 | -47.26631 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bc2b76f-0e9b-3d9f-acf1-b5e8e42bcc2e | -8.58374 | -54.7351 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f48992b-0214-32eb-88ba-41eea92edb02 | -11.09426 | -49.91673 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9ef1b35-6672-3385-a2bb-4a587166b75b | -9.06939 | -50.81952 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09193c1f-412f-3ac2-9b57-706ed7513db2 | -8.52882 | -54.74246 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb82aba-39dd-3d82-9a32-708b325b2e3c | -11.48855 | -45.10356 | 2026-08-19 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2c5d409-9189-3a76-8fc8-9d881e4e17db | -8.54256 | -54.74058 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c565436-4722-38b4-988d-42b4b183f686 | -11.16519 | -49.62405 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47ee16f0-24a8-38a4-b0fd-b9bcbc0f51cf | -9.72886 | -46.78738 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85b628ce-3f07-34a9-9fe6-cfbe0264f2d4 | -9.1683 | -59.67454 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cad6bdb3-aeca-31d0-8516-d97c1d52d4d2 | -11.31498 | -45.21146 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 740a8584-8327-333b-a6a4-6c108aa8349f | -8.58659 | -54.76994 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e0a9ce1-695b-35c1-a1bc-b4de1cc71fb3 | -12.84211 | -48.42056 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc3dbf76-dff8-369f-ab38-1d5c3572139c | -11.48862 | -45.10569 | 2026-08-19 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5337e852-bb04-3a46-9eeb-5338f8344f58 | -9.39391 | -60.57577 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c56f53-586f-388f-b876-9beaa4605877 | -9.41048 | -60.57243 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34186664-a4c4-38f4-8ec3-c6f762fd7b22 | -8.53749 | -54.74398 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f45e42e3-5ee9-3b0f-ba3f-65036e20e41d | -8.54603 | -54.7715 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2cab339a-bba9-33e1-a167-758db27c7fad | -14.21422 | -52.91507 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1414c30a-6a6e-3eb2-bfc0-1ff25906ad6b | -15.77903 | -55.56019 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2343f58-610f-31f0-b9a9-9c7fe482910a | -8.54047 | -54.7272 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aeaf7856-ef0c-3754-8a1e-2d2cb48e86e3 | -8.56715 | -54.75322 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c757fd25-d248-310c-b69b-464ba5149d00 | -9.46537 | -51.63289 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1c7c97a-1c24-32cb-9206-22fe90a66a0c | -9.40213 | -60.56706 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a371e46-9b74-3512-95e4-3799360ec8cf | -12.23979 | -43.16269 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61ae6700-7e2f-300d-94eb-2f2133feba0e | -11.31807 | -45.21663 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8de4dc5d-a5d6-318a-bf0c-170bf518ced4 | -14.45212 | -45.62449 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bb1e724-7dab-3241-bb4f-7ebc6a914b6a | -8.57805 | -54.69123 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42a78191-4666-3042-8a01-a854cbf24c72 | -8.5649 | -54.76603 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 98d8abad-94b5-353e-965c-bc2a025361dd | -11.22076 | -55.0779 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a330fcd-61fb-3145-b09f-3dd616606090 | -13.43912 | -43.84571 | 2026-08-19 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39fff390-1fce-3c6a-912d-bd8c840d048e | -8.54617 | -54.74547 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c5c7a25-8dea-3160-a350-4b7ca10128ce | -8.53257 | -54.72144 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ce6e040d-9b1c-3909-acbc-5fb5f7a24948 | -15.43757 | -41.3839 | 2026-08-19 04:40:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93e9ffe7-fd14-395f-8025-c18fab45d72f | -14.21853 | -52.91145 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 62d418c7-f1de-3d43-8c3a-f09adbd4f44a | -15.43723 | -41.38688 | 2026-08-19 04:40:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 06ad94a7-81ea-3388-9a47-d27ef7e09431 | -11.10764 | -47.27003 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac1978da-434b-3c42-a29a-b3a3e3afcf6d | -11.12586 | -47.28807 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 816dc159-cb59-3191-972f-d685481a956b | -9.62827 | -47.95797 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c430575-e78f-3c4c-9d17-ccfe66748fd7 | -10.64409 | -51.60825 | 2026-08-19 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b8c9572-2eb6-385a-bbd1-285907ba642a | -11.19616 | -54.01675 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0439782c-aca5-3e41-9303-b7210ed3e8f5 | -9.81296 | -46.625 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70149875-65c3-3c0c-81a2-88528f92ddd0 | -8.57003 | -54.73684 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83a70452-5979-36b3-af8c-9843bda1fbc8 | -8.57219 | -54.74998 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47674ba6-fbcd-3bbd-ab92-175529c7f939 | -8.53601 | -54.75228 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 922681d2-3fc6-3b22-a8e4-785c6368e68d | -12.05231 | -46.46438 | 2026-08-19 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c01fff2b-8818-301b-bd18-536dc712d412 | -10.8975 | -50.25482 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75b1848b-08bc-3aba-9f17-7c737204cef5 | -11.22428 | -55.08266 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6deeabd-65d1-3c5d-ba69-a3bf70c72af8 | -8.56079 | -54.6881 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 593a2221-3014-34a7-9892-72d129326b5e | -8.57732 | -54.69539 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68f9cdf5-e171-368b-a4b5-c29c63240c27 | -8.55558 | -54.74281 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df7638c3-c788-3078-a77a-b945dce7851c | -11.90974 | -55.45103 | 2026-08-19 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 413ec497-c622-35c0-9b43-63f486043103 | -8.57364 | -54.74174 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a427c6ee-2146-3b5d-bde5-8a9dfe33c0f1 | -8.56849 | -54.77108 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a1dd2f03-7610-3a82-b4e0-657afb82d00d | -8.5542 | -54.72534 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e139752-dbf0-3f62-a916-b407bdd9564c | -11.22295 | -55.0657 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df5f7136-8260-352f-bd45-a76788d480cb | -9.39466 | -60.55342 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a1cec91c-bcf6-33a3-be7a-6469fe600b63 | -9.4554 | -51.62693 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78755060-7450-3990-bbb8-cf3f01056150 | -13.72736 | -51.87295 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1749d4f-4a34-3ebe-b162-d8bc1b527aba | -8.57791 | -54.76841 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40848ca8-fa37-3c82-ad3d-1e8f1680f3cd | -9.45881 | -51.60633 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9693c1e2-9c67-3c3d-81a2-bbef0681f16a | -12.00374 | -53.44403 | 2026-08-19 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9733439a-d1e4-37ab-8d91-a2193858499d | -8.56792 | -54.7235 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5541f136-cc33-31d2-8625-c006100226af | -11.08117 | -47.60307 | 2026-08-19 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0600707-b2bf-3afc-a1fb-371685877158 | -10.55889 | -56.32819 | 2026-08-19 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f51cdf18-1bf5-3d77-9f7a-078ffb5c0d7c | -12.00519 | -55.52437 | 2026-08-19 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f9d14c6-d1db-38ce-b68e-58f79660af49 | -9.38748 | -60.5571 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97e1dc79-ad3b-3ce5-8c53-18b1c32076a2 | -12.37279 | -46.4457 | 2026-08-19 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f28df7c0-4bb4-33c3-8909-1511fed7efb5 | -11.0778 | -47.60252 | 2026-08-19 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 057bcdf2-444d-33f4-9640-47a5dd3684a3 | -9.39067 | -60.55942 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5b5084d-5e68-3b03-8b8a-2784fa42d11f | -8.5433 | -54.73641 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f340f605-9b20-3d36-8285-fbeae94c29bc | -8.57868 | -54.73845 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4917af08-9e30-301c-9815-cd45ae352e0a | -9.46251 | -51.62812 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be416336-0a9f-3a92-a8cd-efdbfda16734 | -11.20498 | -54.01308 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0833d000-f4ff-3e2c-9b25-4ab155f40ba5 | -8.89 | -60.57038 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8e854ca-1d36-36e3-aa2c-7820873874d3 | -9.637 | -48.20461 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c874d8-6209-304d-89be-d0e017020217 | -7.60285 | -60.95684 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README43.md)
