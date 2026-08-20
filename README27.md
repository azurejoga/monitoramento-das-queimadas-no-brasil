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
| 0e7087a5-1ecd-35d6-b0d1-139ac5bbc7ed | -12.24288 | -43.17233 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a991dd2b-95d0-3220-9b3b-5344b28c109d | -11.39176 | -46.37666 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d98a18fd-f501-38d8-b3c8-34d779b3a201 | -14.20157 | -52.89129 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07936b56-8583-3af0-bcb3-df22124e772c | -9.75487 | -43.31867 | 2026-08-20 04:02:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f9272930-768e-3add-a205-b26dd1a72699 | -12.22785 | -43.16428 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fb305abb-a37b-3c44-8557-43746ad72d3d | -11.37583 | -46.37875 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 57f89d9a-2b09-3826-a244-15bdab70d4d1 | -14.43951 | -45.61819 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1adbf1df-204c-327c-b62f-216ff1ca41f4 | -12.36625 | -46.44496 | 2026-08-20 04:02:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8ed70a8-f744-356f-b1af-012e9fbf82d2 | -12.81784 | -48.44299 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfc33033-8438-35ad-b52e-a2542cd8d319 | -14.11711 | -44.38805 | 2026-08-20 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c74318f4-b96a-3bfa-973b-776f11b8114f | -13.35558 | -41.67586 | 2026-08-20 04:02:00 | NPP-375D | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 952f4c42-d6e0-306c-8349-eb1ecf3da4fa | -10.74329 | -50.35341 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f34876c-4de6-3ef2-8648-c9c4561f3d01 | -11.58364 | -50.53711 | 2026-08-20 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2b5e319-6b35-3414-be35-67a0bdf7fa73 | -8.72258 | -49.61687 | 2026-08-20 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8f13703-b2b6-3912-96e9-c1ef91f4a409 | -15.18481 | -48.76632 | 2026-08-20 04:02:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c92d049c-0cea-3b9e-8284-be855fdc0fab | -10.78589 | -50.31213 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1720cf0a-61a1-39b7-b453-7e36ec5f500d | -10.74372 | -50.35481 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 469ad0bf-8502-30c5-b66e-4e552ff1281d | -11.31402 | -45.21037 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58055082-ea69-3766-b9fa-bd124df2b6d0 | -13.56426 | -51.67523 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e876f1f-4516-364e-ae48-474edeb695ca | -13.47193 | -51.4422 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c52eaf04-65fc-3157-94c7-c25477a9276a | -12.25869 | -43.15294 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1ebf48f4-e9a5-3353-8a1f-3bda72aa8430 | -10.41621 | -48.33615 | 2026-08-20 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 926b104d-347b-3bb4-836b-dd4695c1174d | -12.77418 | -48.41236 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b285bf24-25c3-3c05-b31f-fb4455b7803c | -14.73392 | -47.14888 | 2026-08-20 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57c13b56-61a0-33b1-8bff-8db81ea6dc97 | -14.271 | -51.89297 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd55655a-b35e-3e9c-950e-eb65aec79240 | -10.79113 | -50.31759 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1259c2b-64a3-3670-b431-2c77c08453c8 | -15.54587 | -50.27482 | 2026-08-20 04:02:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2c21cb1-bcc1-3375-bd61-f5878227c66d | -10.75777 | -50.35207 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2f1c6cd-57ab-39ec-b821-dd949889d7b5 | -14.22602 | -51.92565 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15d7721-a3f7-36f7-9dd9-85352c1220f8 | -10.24084 | -40.50974 | 2026-08-20 04:02:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c53ffbe4-d8cd-31b2-a4a7-f63733338751 | -12.77307 | -48.41803 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20cb4049-a894-38d5-a2ba-dc20bc6c9ddc | -14.20853 | -52.89331 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bc968fc-0f20-36b9-a6d7-afec9c60d261 | -15.17939 | -48.76508 | 2026-08-20 04:02:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48999a41-215f-3a9d-b8be-6e12f5d2680d | -11.43246 | -47.24935 | 2026-08-20 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6a16787-a796-38cf-8062-9e10c4804e80 | -14.23268 | -51.92722 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28558e6a-3ea4-3823-8bec-e4e5f334a9cb | -8.71619 | -49.61544 | 2026-08-20 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b35b1aec-f042-327a-8c13-162e0cb3dd71 | -15.18436 | -48.76652 | 2026-08-20 04:02:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| befa9172-242c-37e3-a5be-e8fd979021d3 | -12.25774 | -43.15826 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| eb2a8290-915b-3a8d-9728-789af9712ac3 | -12.79766 | -48.42785 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a96090d0-59f3-35c3-b6b0-b62c79986936 | -15.56772 | -43.43346 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 079604df-ac6e-3345-9b80-d4e64583eb59 | -11.32093 | -45.20842 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bd1f3e6-c5c7-3920-8872-45e4670e614e | -12.82507 | -48.43571 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7d70633-1921-33dd-ad1f-b8496d75414c | -16.86257 | -43.23975 | 2026-08-20 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab44696f-488f-3935-9075-10727007620e | -14.21679 | -52.88935 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d044840b-6134-3156-8f46-f3d178f14f17 | -12.38006 | -46.45323 | 2026-08-20 04:02:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b9869de-0983-3978-a162-8466adcbcd04 | -12.78351 | -48.41175 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06c291c0-bd23-323d-99da-c0ffe0206c83 | -14.21554 | -52.8951 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fee6d551-67f7-3014-93f8-764895d4ff3c | -10.26086 | -46.99858 | 2026-08-20 04:02:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d06b629-411e-3f9d-8b3e-4e629dab7c1c | -12.19422 | -45.16197 | 2026-08-20 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc60a0d1-ba40-3474-816d-c7032339b71b | -14.27647 | -51.88669 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b894a0d6-ae06-35af-824d-801fa5e969f9 | -12.84931 | -48.4302 | 2026-08-20 04:02:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 760045f2-07bf-3e2d-bc8b-81f4b429aac3 | -13.56773 | -51.66957 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 368e88ce-4eef-38b5-8557-0eb6f1bcea34 | -13.44564 | -51.43613 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53920ea3-1d5a-339e-b801-cab735ed8a37 | -14.44851 | -45.61999 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6019abec-95b3-3254-8bf0-3c6b6b1cbfd0 | -10.78697 | -50.30666 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62492bc6-c518-3f95-9332-42f4a2a22a09 | -10.79235 | -50.31352 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8687ecb9-6e8b-313b-8bd9-e4861ad50ec6 | -12.79614 | -48.43547 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5394f3bd-924a-3ea7-b98d-86de5f8516b1 | -15.7127 | -47.80071 | 2026-08-20 04:02:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3f9917-9de6-3b00-b24b-24a1373ffcc0 | -11.31865 | -45.21125 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| edad229e-b20c-35d8-91a6-1c7536f8e87c | -10.42281 | -48.33311 | 2026-08-20 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a2d8c3a-6815-3c16-8097-cd2a1e7c4db5 | -12.23886 | -43.17173 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8f2e3b7e-d353-36e4-8395-5fb111cd24f7 | -15.36275 | -52.77213 | 2026-08-20 04:02:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17e37a11-5844-3990-b7c0-ecd4405b9ea6 | -10.25484 | -47.00129 | 2026-08-20 04:02:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed8a8a5-6dcc-371c-8f43-c4eb71b2a92e | -14.21198 | -52.89208 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be9eec9f-d903-3450-9dc5-4ce4300dd704 | -14.20986 | -52.88722 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27749b84-e77c-3540-8a99-01b7d0f4a497 | -15.53989 | -50.27374 | 2026-08-20 04:02:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19d8fbbf-408c-3aa1-a294-01fa3decccde | -14.73217 | -47.15849 | 2026-08-20 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c5b240-07d4-3783-8bd4-0459ca960651 | -15.71211 | -47.80366 | 2026-08-20 04:02:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3be7daa-7b08-3a19-b69e-0c7c24e3e39d | -8.71518 | -49.62066 | 2026-08-20 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a2433c24-29b2-390b-8787-127ad537d866 | -12.22699 | -43.16279 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97ab92c4-71cc-3417-9279-a3bfe7bfe3af | -12.23099 | -43.16344 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b71dcd37-6fa8-37e2-a97a-3b2483d0a3d8 | -11.58251 | -50.54258 | 2026-08-20 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0899b9f2-1286-39ef-9fdf-a997557df64d | -12.82141 | -48.42492 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 997c0d96-1ad4-3c57-950a-cdffe4e3152d | -15.38676 | -52.7291 | 2026-08-20 04:02:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ebe35dc-b515-32df-b96f-ecdf3a067a98 | -14.08183 | -40.96444 | 2026-08-20 04:02:00 | NPP-375D | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eeaaa10b-43b3-37fb-a1b2-bc2dbe46c3fe | -14.21894 | -52.89402 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfdc4351-5daf-3a88-bd09-2fd7ae12734f | -14.7316 | -47.16046 | 2026-08-20 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2c46813-48ab-3382-90df-097f55931570 | -13.54385 | -52.2336 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f3081fe-8f9e-3c22-bab6-8ca5d1f601f1 | -13.44344 | -43.84689 | 2026-08-20 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bb946b82-e703-30b2-bd21-61be8c442ce9 | -15.49167 | -48.43608 | 2026-08-20 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b31b926-8fb6-3708-8dae-d64bea56ba99 | -11.81076 | -44.80971 | 2026-08-20 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d3bf1a1c-2404-3dcb-91c7-2fa4d678b698 | -16.86713 | -43.23574 | 2026-08-20 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ca6dd46-ba36-3393-b8bf-d5c2cf96ace1 | -19.46181 | -46.81384 | 2026-08-20 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a3a06c7-0872-3d15-b283-e53c8d43c17f | -19.38835 | -46.40903 | 2026-08-20 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 000201f3-2de5-3ce5-b9dc-3b2326b92491 | -16.91524 | -49.42526 | 2026-08-20 04:04:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f9f3066-0744-316b-8078-7b4ec5ccc5e1 | -16.91605 | -49.42138 | 2026-08-20 04:04:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b18874-9f0f-36ea-bad5-e4e1a6821f24 | -20.26352 | -46.75039 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec9fc503-92c2-35b9-a5d0-fab53b1ed08c | -18.79168 | -48.55086 | 2026-08-20 04:04:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88764f78-7250-334b-a267-4fe4a5fa14e6 | -19.67295 | -42.10652 | 2026-08-20 04:04:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 333dad7a-c2bc-3b2d-941d-8c66cc1174ae | -20.80224 | -43.85954 | 2026-08-20 04:04:00 | NPP-375D | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| accdadc1-3757-3ec4-a006-cc88dbc0d558 | -21.98129 | -46.82643 | 2026-08-20 04:04:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3609d0ee-6cd6-3d37-9a2f-179190a62ff3 | -18.03861 | -44.62088 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 0b8b928d-0343-3dc8-a6db-2404199e87f8 | -18.22581 | -43.57672 | 2026-08-20 04:04:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fe1cee0-c799-3fc4-84ac-b992dcb51a32 | -21.71375 | -47.14019 | 2026-08-20 04:04:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a864f2e6-70aa-3edb-ac7c-e0669975c701 | -19.71603 | -46.2178 | 2026-08-20 04:04:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ac8584-3fd5-3c1a-b2e5-667581e7c2fd | -19.67227 | -42.11056 | 2026-08-20 04:04:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d7bc24c-3bd5-3cf5-8650-e0927ebd5fcb | -19.95607 | -45.0561 | 2026-08-20 04:04:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb49f99c-5195-349d-80a3-f9f8a76bcd71 | -17.95551 | -41.93494 | 2026-08-20 04:04:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e59fd8f-f9fe-34ee-804f-608fb34b7633 | -20.686 | -45.26645 | 2026-08-20 04:04:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f8e76622-fadb-37a8-81f7-020bf065c2b2 | -19.71943 | -46.22301 | 2026-08-20 04:04:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
