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
| 48e29f04-898f-33f0-99ef-5ecbba2b2d5b | -13.17215 | -54.91835 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7603499f-a0ed-3611-ab64-837ce2d16fef | -12.92954 | -46.11176 | 2025-08-18 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1948ec7-84d4-3974-af84-3283d392b429 | -9.51335 | -60.53125 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5c45c91-412e-3bde-b9ef-4b86519ecaf6 | -15.86821 | -50.20592 | 2025-08-18 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e57b5c6-be70-3554-b2db-260eb7ef39fa | -11.31942 | -55.21111 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab52f674-faea-3c5f-8b3a-f7e9e3a71089 | -13.20813 | -50.77138 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 211ba45b-a59b-34a2-85bd-649e2ac845fd | -15.00794 | -54.78918 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2cc4e878-e826-3348-bdb3-cd723bdd1da2 | -13.09658 | -46.8419 | 2025-08-18 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50404e47-d879-3d16-8b77-a6d9d5a77d04 | -8.9734 | -60.49875 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7609ac7d-d492-336b-9419-0ac3d97724dd | -12.99006 | -56.85318 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f1ae5fd-48c8-3436-85fd-c33f40d57a75 | -14.63397 | -54.90646 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16366fce-b76e-3ee0-80c5-3cae595fe699 | -14.63013 | -54.90597 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e2ac451-1a21-326d-aa0a-68e2bcff125d | -12.99407 | -56.84992 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b992d188-a7b5-34b1-bb3c-b2032745ba58 | -15.00926 | -54.77967 | 2025-08-18 05:14:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c451e5d3-e50c-3784-96f9-a554b0c7529b | -13.01641 | -56.84169 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebd7c17-a7d3-3f72-9f7e-48876dda40b4 | -9.51974 | -60.5364 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7476936c-27cd-30fb-87ab-1df3b551ab7b | -14.18796 | -57.5493 | 2025-08-18 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c1d5d88-9545-3810-95e8-ea102cd90dbb | -13.13072 | -57.14309 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cbd373b-d882-3848-bd5c-9c633f29e260 | -16.79938 | -50.09729 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edf26a7e-7fbf-3952-a51f-10a0cdf94a95 | -13.17083 | -54.92746 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1cf44830-862f-37e4-a5ab-fb08646479d5 | -13.02205 | -56.84577 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 208a1f71-8b69-3b77-88b9-bc5e8874b2fe | -12.99121 | -56.8456 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e19d638-6f32-3a1b-8c2b-7f6e2006ab7c | -12.99808 | -56.84666 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba91cd3c-e04a-345c-b10a-303fecb52736 | -13.21726 | -50.77827 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54eb5562-025c-3257-aa70-6cafa84b3f60 | -17.09607 | -49.88648 | 2025-08-18 05:14:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48ed1f5b-f7c4-320c-bcc5-18261069eba2 | -12.53595 | -48.49634 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a623e17-256e-306e-9fa6-41117e57e34c | -13.22234 | -50.75125 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ad03def0-84ca-3777-b0fa-418b93c43a1b | -12.93375 | -46.11527 | 2025-08-18 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39cecbc8-bd88-36d0-a3c6-f892ab560d30 | -17.09686 | -49.8793 | 2025-08-18 05:14:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e18fcddb-a8e7-3c4c-8899-ee501c11d03a | -13.01926 | -56.84604 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faaf6b2b-43f6-30b8-96d1-a0d5b5147490 | -13.22658 | -50.75755 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1fa34039-7864-3486-9b4a-d698f88960a8 | -15.86176 | -50.21529 | 2025-08-18 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ace48e6-15a8-3050-8c8a-17063aac0fbd | -13.01805 | -56.84903 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a11d54-2c3b-3627-9475-480c2ad4edb7 | -13.2158 | -50.78945 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5079b9a2-bf98-3556-b8d5-b67206807ce6 | -13.22027 | -50.76814 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 234fe783-636c-309e-a708-931e7c0f0532 | -16.62496 | -51.36187 | 2025-08-18 05:14:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fd8a103-a07a-3981-8bd2-f3f57e1374e1 | -12.50712 | -57.7781 | 2025-08-18 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d8ae8da-f99a-3170-a61a-e61314aaec79 | -9.52106 | -60.52846 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d3103b1-6ffa-367c-9241-f00c3066436b | -13.21041 | -50.7668 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c067adea-b46e-3ca4-bf77-528e5849a226 | -15.60811 | -54.30318 | 2025-08-18 05:14:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 571b6bb9-9588-3d1d-af06-c4f55cbe3251 | -13.20972 | -50.77242 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 92c3e506-0cd0-37d8-8350-dcd46584b7be | -14.99 | -54.77598 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5b72cf68-cb37-3683-a8c3-fd3c3b45595f | -13.01869 | -56.84983 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdff600b-6add-36b3-9f3a-b6f1b258ca53 | -13.43785 | -57.02468 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51684f90-d0cf-3cf7-b5eb-e6ad594e94bf | -8.97455 | -60.49522 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d9ae97d-e6f2-3a18-b8e5-8caae0ee3d2a | -12.9958 | -56.83854 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caeb55be-8f71-3a5d-bc15-863d7c5e5da1 | -13.17525 | -54.92348 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cf25805-234e-3547-9219-fa8f0492902d | -11.84281 | -51.57264 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51e78d92-3344-3f13-b941-e173cc2666f4 | -13.45218 | -45.90111 | 2025-08-18 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f80c976d-00b1-3e01-a21c-8b626f322fbd | -13.00839 | -56.84823 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc7a724a-46da-3a29-acab-a71de44822cc | -13.45281 | -45.89498 | 2025-08-18 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4562b794-6d72-382b-96a2-00e165255118 | -13.22018 | -50.75587 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2631594f-0e8d-3453-a2f3-f536490fa78b | -13.47568 | -55.76893 | 2025-08-18 05:14:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fe6a3875-eca1-3b30-ab0d-7a17b4b476f1 | -11.74466 | -58.32827 | 2025-08-18 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0065272-94bc-3c4b-92b9-d65f32b9c8b3 | -11.31422 | -55.21558 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 853d3bc8-2aa8-34ed-9c23-e1c8d7707f09 | -9.51621 | -60.53581 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e468a18-27e4-333a-8fd2-eac3a65d6c79 | -14.46116 | -53.03294 | 2025-08-18 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 545d328d-e6b9-307e-bef6-aa00555c9135 | -14.17106 | -45.29481 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ebfa031-fb97-3a5f-8db7-012b53b719d0 | -15.04333 | -56.03053 | 2025-08-18 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f18cf2a-5244-33db-977f-930b0f803950 | -13.43667 | -56.94322 | 2025-08-18 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcf2013a-fe2e-3979-95e1-1a30bf780574 | -13.12728 | -57.11967 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07294ea7-4362-3ea8-8b83-6e12bff7b25e | -13.21031 | -50.75456 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3c9c18bf-78d9-3cbf-9662-b2617e473aea | -14.31832 | -58.93589 | 2025-08-18 05:14:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31f7706e-b185-3748-89a0-1771e3d84e9d | -11.31846 | -55.21192 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52ebf285-9646-3723-9a48-d8926cf3598d | -13.16708 | -54.9269 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| d6fec032-a8a1-36e4-b63d-611f3a34febb | -14.9707 | -54.77255 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cd8e002-ff49-3ca1-ac54-61985970cc7f | -13.45079 | -45.89872 | 2025-08-18 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4a0b99a-3d85-3e35-8269-0c1b07be214e | -12.9832 | -56.85212 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4240fa5-0b03-3e5e-b777-c2fe6ebe798f | -13.17393 | -54.93259 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 87a03fe8-4e88-301a-8c1c-064f6902872d | -13.13354 | -57.12445 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ac47614-5715-38d3-b9c8-a300798fd1ef | -13.16642 | -54.93147 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 32ab1b8a-a76a-3d1a-b458-9c7f980b048c | -16.79979 | -50.09377 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 220fd4e7-e78c-3475-ae08-fd49a852f8b6 | -12.99693 | -56.85423 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ac47b57-032c-3209-8fae-1b81166a0764 | -12.54122 | -48.50067 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3519774-4aef-35f4-b05a-4905c9fbf92b | -12.6348 | -46.89265 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aecd9b7-4eb7-3817-b9d1-0755b48e8257 | -11.84554 | -51.58737 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f9113ca-986c-30c6-b3dc-0795250adfa1 | -13.13643 | -57.17441 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98f0e620-7cce-3ac9-a3f8-e7e03f374c48 | -13.22381 | -50.78001 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b74f9207-a73b-36af-a1e1-d558be8e7d5f | -13.22931 | -50.76278 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 001c9c26-3d81-354c-b278-549ba7c97cf0 | -13.13069 | -57.1202 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc167fc0-d615-35bc-8ffd-f78eadb2be9b | -13.1341 | -57.12072 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f61d559-5a38-311f-b09a-a0d27c29b028 | -13.59296 | -46.98544 | 2025-08-18 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a21fdd9-ac13-3c2b-95a8-7e411dcf02ea | -14.63597 | -54.89196 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a457eb9c-8706-39f2-9f92-ade40993e5d1 | -12.54739 | -48.49719 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7a845432-5bd1-3e91-8519-b9f73123255a | -8.97036 | -60.49864 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6e95cab-d2d4-32e4-94cf-a7d70df0bab1 | -9.51116 | -60.52271 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d43a88-91e2-3efa-8db9-599a7a23963b | -11.00252 | -45.65462 | 2025-08-18 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fc9c3b8-863b-35b3-b4ba-b8f8d5a979dd | -13.23151 | -50.75822 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b394817f-3b54-343c-9a20-030e40b147de | -11.85011 | -51.58802 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d7871da-5957-3cd3-87dd-074bc9da28f3 | -13.21452 | -50.76082 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0d436708-23d6-3bd6-a6db-16b3773c47b0 | -12.98377 | -56.84833 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d93b422d-e29d-3dd4-a0a3-63f261105a46 | -13.21465 | -50.77308 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 543f7804-0f71-38e9-8bb4-3cd831ef4b9d | -13.22584 | -50.75092 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 753e7217-95c0-3fee-880a-f3dc179359f1 | -16.79358 | -50.10004 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62720c6b-bef0-3162-b006-9c8b373bb3b4 | -13.01583 | -56.8455 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0e98f44-5bb2-3652-881d-cc7a1827e7aa | -14.28632 | -53.19323 | 2025-08-18 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41156927-0171-39b5-b235-0ebdd8f7b4a4 | -13.14152 | -57.1638 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf76a85b-8002-34e5-8ee8-d6eee37c53a6 | -14.63263 | -54.91614 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11394d13-c6e9-3e55-a4c9-e451e9ec1f8b | -12.99235 | -56.86126 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4520ef-3127-347a-8d44-a273679486cd | -13.00094 | -56.85097 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README28.md)
