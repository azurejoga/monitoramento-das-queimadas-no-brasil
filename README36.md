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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3971a595-9cd5-3265-b003-5200d02be93a | -13.87586 | -45.57468 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 670d8eb2-019f-3fcf-a807-a6957ba965fa | -10.69389 | -48.21888 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 248824a8-4576-3f8d-aa90-b1cb0ded988d | -11.31594 | -55.22491 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca4444e8-37fa-3ec0-b75f-06db522580f3 | -14.88168 | -48.06656 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fdfc7da-7809-3d3f-92b1-fb2ac7149bfb | -13.10277 | -51.91098 | 2025-08-20 04:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12e6c68d-59de-3f27-be2a-ee0bec781b5d | -13.40278 | -46.36125 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a28e880f-6993-3568-812d-08ca64ab860e | -12.9028 | -46.0926 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fb16c7e-663d-31f5-ba22-bdfdee1d36cf | -12.66797 | -44.9523 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89fd17d2-7982-3886-a489-45fa6ff49390 | -12.09813 | -47.91173 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ec3bec-8b4d-3932-89b8-50abddc6e712 | -13.49448 | -47.07508 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c8b8d0-6f0c-30f7-9e02-95209bed5b17 | -10.59999 | -48.60003 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df2bdf94-5798-3002-8454-df67475fe16f | -14.49773 | -45.95992 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52987544-0e6d-3864-b4d4-1637643bbab0 | -13.18649 | -46.89534 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42c24732-5766-3fea-ab89-a2df1772aa57 | -12.10772 | -47.90169 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e254961c-8c60-3e01-9780-172519470524 | -13.57841 | -47.01946 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a721896-2679-3851-876b-ad3208b51489 | -11.3167 | -55.22057 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 285da156-6adb-3983-987c-6aa43eb21687 | -13.57318 | -47.03075 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6eaffa81-7f0c-3546-b19a-f4109ff1bc24 | -13.491 | -47.07455 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f6ed334-bdbe-31ce-ab9e-dbe16aa1c37f | -13.03435 | -46.78407 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8544e2b7-6563-311e-aed8-63a1cd7e94b2 | -8.69138 | -62.09737 | 2025-08-20 04:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69123592-ca26-3bdf-8899-9466d892f5a6 | -13.33084 | -54.41483 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f60bb141-e528-34c1-af7c-d669213ed6ed | -13.59292 | -47.55424 | 2025-08-20 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b811823-be09-3a20-b41a-2546989a7b9b | -11.31435 | -55.13136 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 311ddee8-49da-39f6-b2de-d33f989a8e08 | -8.88138 | -62.40042 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba1a838b-370c-3e51-a470-7f7264aef1e8 | -9.89389 | -60.28107 | 2025-08-20 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23e8cebc-8717-31e6-9780-256e04c972de | -13.87339 | -45.56493 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8e794c-7767-3196-9aa6-d650b0b511f8 | -14.34797 | -52.00441 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86a66e47-2d6c-3c28-9edd-63e44fdc0af7 | -9.19296 | -59.63327 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f88d3e02-6e92-33fb-9ad5-a84d9332b104 | -13.17654 | -46.89018 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c17592a-3c30-3846-9122-f5e9567934cf | -13.17604 | -46.86949 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc276284-1e96-3f4a-83f0-c9675ae6f299 | -10.27197 | -46.76896 | 2025-08-20 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1cf6968-7ea8-3284-af0f-a07be1920400 | -14.46025 | -48.47552 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c5da68e-275b-356b-9bbe-aed350299762 | -13.63023 | -46.88699 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ab2402-fd1a-3caf-80a5-3c60a87c95f2 | -13.02911 | -46.79546 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b35b0041-edbd-3781-9000-21a2bea5f694 | -9.22955 | -59.60713 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f805eb7-0c92-3eae-967d-9e1144892836 | -10.17712 | -47.90932 | 2025-08-20 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30c68193-53e3-3258-83c1-13eaac63e635 | -10.12589 | -47.43109 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a75bd3e4-762d-3af0-92c6-3355b04ef1af | -11.66586 | -60.18864 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee7a3348-9cfe-307e-a350-aafda6d9e49b | -13.0271 | -46.80381 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24db1c33-5199-3e6c-883c-a091fa2c63a1 | -10.81833 | -43.27749 | 2025-08-20 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 11111c83-9165-3fbb-8333-da7f58ba76a4 | -15.09067 | -48.4128 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3577484-c12e-3f8b-9289-3845cfd50533 | -14.63824 | -54.8849 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd7f62ff-44fd-39e9-b6b2-6189ae487f2c | -13.32746 | -54.41049 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7494e952-3ac9-3b07-9993-90afcd24409d | -8.69845 | -62.09882 | 2025-08-20 04:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef71f52c-08c4-3914-9df0-c4325177f78b | -12.97611 | -56.88772 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a21f723-14c3-372e-b4d3-bc360944eda6 | -12.9455 | -46.16151 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9db6c9f-92e2-3b30-94ab-d7f19c4410d0 | -13.56071 | -44.46146 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42cc85f5-bb1f-3aea-9c30-cf1d866383e7 | -10.60055 | -48.59652 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c13d2f62-d2d6-34a7-b92c-9853591a0ab1 | -10.87153 | -48.46688 | 2025-08-20 04:36:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ecbb4f3-c3bd-3dfc-848b-4ff8a23e92ef | -14.15093 | -45.28359 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 267afa21-aee8-3932-9edf-6a8c22acf134 | -13.17362 | -46.88584 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31aa1831-8217-3338-a0a1-cca5678e3f54 | -14.89247 | -48.08678 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46539e0d-f13d-3481-b549-80dfda7a8d06 | -13.15269 | -54.9422 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 244b61fb-3004-34ee-a857-9e92483aebf1 | -14.45911 | -48.3703 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f1f0924-eeb2-35b1-b4eb-26906145aa3b | -14.88508 | -48.06711 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b1b56d6-b572-3729-bccc-06b5859a16c8 | -13.64562 | -43.7883 | 2025-08-20 04:36:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e974c31c-b67b-3d24-b027-46cd0bce5855 | -9.18682 | -59.63239 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8a061d0-609b-388c-8e8e-fd77e68f172d | -10.69444 | -48.21536 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 747cf458-fbdc-33d2-b47f-b8851b71a966 | -13.6122 | -46.88766 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e4f95fd-cce9-3ffc-8307-334bb80c3afc | -10.90822 | -57.50217 | 2025-08-20 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a400e85c-b90d-318b-a400-a057afe4f656 | -13.18942 | -46.87561 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d9dfde-cc64-3e47-9c3f-fa4033644791 | -12.98306 | -45.19867 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21380cc5-385f-35a7-a682-b846c9bed2cd | -13.15205 | -54.92184 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e5338283-9d5f-3b00-8548-6ede3e16b340 | -14.34913 | -51.97586 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d4b14fa-94b8-311b-8cda-3165cf06ea4c | -13.13633 | -57.15504 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 806805ea-24dc-3712-9ca2-fe8b8217edc7 | -12.52721 | -45.61177 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b90fd76-2861-373b-9858-b86d1559b0af | -13.58538 | -47.02057 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b4e1e45-e06f-38cb-b792-f08cf13e1b71 | -9.21332 | -59.69094 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae7ec6f3-43b6-3026-8e37-bd75d7d83698 | -12.96863 | -56.85236 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a30b534-d5bf-3af5-a84f-0045198b02a8 | -13.15134 | -54.92575 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 042a11bb-5980-391f-9798-d981ccf6260e | -10.60387 | -48.59705 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 486e6917-0c0e-3a21-9e2c-985dc6fda76c | -14.98721 | -49.56363 | 2025-08-20 04:36:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edd28bcc-4bde-38e3-b11b-aa04306df4b8 | -13.14993 | -54.93359 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08cfd725-f729-3595-a2cc-074bfdb159a1 | -14.89129 | -48.07198 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80283fba-ae03-3c11-adc7-fa594857bacb | -14.6928 | -49.04947 | 2025-08-20 04:36:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9b5ded8-039e-34c5-a9e3-89138e4a6654 | -14.89303 | -48.0831 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d57d415-e03c-310d-8efd-1e343e196d79 | -14.30462 | -52.00493 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 566f2ebb-ad71-3d76-8bb3-db03954594a9 | -14.88958 | -48.08322 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a5c47e-c5fa-33b1-ac6a-6c41a2109dd2 | -12.91237 | -46.10265 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78a46029-c5af-337e-b51b-c51efdbd6345 | -15.5443 | -48.5677 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6844e2ac-d5ab-3852-8fc0-e038601238e0 | -14.34564 | -51.97524 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a94ccbb-5439-369e-8c7c-4ef265e7046e | -12.99599 | -49.11359 | 2025-08-20 04:36:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 351b3acf-68fd-3359-abc9-d1d622438c2f | -8.87397 | -62.40729 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 784b4d25-0545-34ac-9523-294a99bb96e9 | -13.58654 | -47.01277 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5fa73df-d993-316b-9b73-9599939d6032 | -13.40637 | -46.36172 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60304910-68ba-3640-95ea-c6f24a7f4cd0 | -13.33422 | -54.4192 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fa72edc-62ca-3bf1-91c0-0fc961807669 | -9.16999 | -59.62307 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9f614a8-9807-321f-be22-4570b515862e | -13.17598 | -46.894 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e023ce32-43f3-36c5-9ab6-4a364c39504c | -12.67853 | -45.82182 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad802f4d-57de-3d3c-9f6d-603422d30e28 | -14.62063 | -54.91196 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f82038d-59f6-3427-9add-5301fcfeba95 | -12.98184 | -56.88353 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f0f621-0f17-38a9-951e-034a0cb104c2 | -12.97719 | -56.85939 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17d1efd6-defa-3b60-b1a1-5cb05b8f303a | -10.27538 | -46.76963 | 2025-08-20 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 128699c8-7be8-3dc0-a2c2-397b39c9ab3a | -12.9716 | -56.85962 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d177474c-d394-31fa-ae20-854d012a8c9e | -9.18567 | -59.64015 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b17b15c-2938-32a1-8ed8-49637c3b9976 | -13.48578 | -47.0618 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d20e5708-5fa0-30c5-9fa0-3f34395b07ec | -13.5819 | -47.02002 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfe9490c-67b2-3527-89e7-5421afea1175 | -9.18652 | -59.63562 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43402bf4-8030-3332-81f2-46b86a8e0b7a | -12.97358 | -56.84927 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9dd96b8c-d21c-3513-8884-a963afa730e4 | -12.97334 | -56.88039 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README37.md)
