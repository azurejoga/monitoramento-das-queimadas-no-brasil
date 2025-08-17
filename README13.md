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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 231b9f1c-e948-3bf6-8289-f51ac255ae10 | -14.93431 | -47.05895 | 2025-08-17 03:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db3adc95-318d-381f-bb03-80972bbfaca7 | -11.42742 | -52.22126 | 2025-08-17 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fe75da70-6b91-376a-b816-e5ee4f3ddcd8 | -13.56262 | -46.98703 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aafe7f6b-3d42-3226-8f81-bbe7e91c088b | -13.43369 | -45.90384 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 066b3012-bc10-3fd4-84ab-d4bfa5979210 | -10.85247 | -45.33251 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d03fbc0-10bf-32f2-9c8e-f4ccc740f84b | -15.6365 | -48.13661 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eab0206-28f8-38c8-84ea-4674a3feb8fc | -15.24364 | -43.85368 | 2025-08-17 03:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8c3cf7c-8008-3d27-be54-db6cc4cc4c03 | -11.09115 | -44.80756 | 2025-08-17 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ed54557-830d-35dd-8fd2-2355a597cebb | -13.60509 | -47.77685 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b2a4fac-52ea-3605-91af-f2c272e55388 | -12.89004 | -46.12689 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d980dc68-2963-3647-bc69-34bbea3bf9bd | -11.42629 | -52.22142 | 2025-08-17 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3128de04-7dc2-357b-9a37-0a5678ccfb55 | -15.85556 | -50.19262 | 2025-08-17 03:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2479002a-088b-37f2-98c1-b36108edf358 | -13.43844 | -45.90479 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a99108a8-c715-328c-bd0d-a323aedd6c89 | -10.84205 | -45.30869 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2768148e-f2a4-3927-8f16-5d1b150a4fa9 | -10.84671 | -45.33679 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0feb79d0-0eff-3f2b-baf2-2d63319f0d49 | -12.61534 | -46.90948 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e749d648-40bb-33b1-a274-087784354cfc | -13.57315 | -46.98735 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8353282-b54d-3b95-b9df-3fbe1182c1da | -10.83727 | -45.30776 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ef8964e-9d10-37cf-a80f-ecadd43c9807 | -17.62566 | -39.92994 | 2025-08-17 03:51:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2d21a4f-48ee-380a-a326-ff197a131435 | -13.61747 | -47.75832 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4cf4167-0092-3b33-8d09-b58a363da71e | -13.60963 | -47.78199 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cf8d0986-ac7f-33de-9ca4-e5283626a16b | -15.9691 | -43.89922 | 2025-08-17 03:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b21182f5-cdc7-34e8-b782-dfb031301de1 | -14.18203 | -45.31747 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2209f4fc-c72c-3495-87f0-38bf9fba4fc3 | -14.5925 | -47.95161 | 2025-08-17 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74c30133-4ee3-31f8-bb1b-a893eefc3abf | -10.83413 | -45.35091 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c42ae756-cefa-38c3-bd8d-f75e47334c9f | -12.8921 | -46.1161 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c8df660f-0e38-3745-ab12-abf0436dcfad | -13.43095 | -45.89252 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb4e0917-a162-3ad6-a41c-2957d7d7bf5c | -13.60308 | -47.74647 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b77eb497-963d-394e-a05a-9a4bf227d641 | -10.85458 | -45.32565 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00eea26f-685f-361f-a98f-d75882b9e232 | -10.84701 | -45.368 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 73ce4fcd-9379-3e8c-a063-e0a4cf8540cb | -11.89857 | -43.42628 | 2025-08-17 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4f000f8-047b-31c2-8399-369a5a46c59d | -15.53538 | -42.33693 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8abea39-d5cc-3077-b730-0b1318e1ae6d | -11.89789 | -43.4301 | 2025-08-17 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffacd89a-758c-3c16-aaba-6f207bf646ed | -15.76448 | -47.80122 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0882f02c-66e1-30a6-b390-4960f0699b5f | -13.5942 | -47.76352 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 319ec666-a089-359b-b89d-b3164b4e7e84 | -15.64512 | -48.12126 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3c1b60b-8ad9-3103-ac2a-633a88418914 | -10.83993 | -45.3465 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82e567f2-d913-373d-b36c-bfe3be4f4c94 | -12.8712 | -46.08015 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0cd5bfe-4602-379b-b54b-50969786e16b | -15.52803 | -42.33549 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 034f70cc-f1ed-32b0-bfd7-b74acf0e5d8d | -11.64756 | -46.6619 | 2025-08-17 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c016bcc3-5cc5-35af-abf5-d4305dfae792 | -12.82716 | -45.99287 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 074d941d-1349-3e08-a7d8-86b9fa59d27e | -12.13967 | -47.91982 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1c8c667-ebd3-31a9-9868-ef3840d5657c | -14.18658 | -45.3204 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c13e62d-f856-3fde-a849-4678348509f1 | -13.43178 | -45.89134 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51233445-63d1-3c21-afdf-605367aae5c1 | -12.89107 | -46.12146 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88ede453-9339-3a4a-961b-16e52b50742e | -10.84572 | -45.34206 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ace7b9d1-be2b-36e3-9845-0bfc31b043d6 | -13.01427 | -42.33043 | 2025-08-17 03:51:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0abe4754-53a9-3692-b2ae-90e41333bc07 | -13.47528 | -44.07967 | 2025-08-17 03:51:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37b4afea-58ae-382b-9b6f-91460b516a31 | -10.82753 | -45.33315 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cef31197-d6a0-34ff-a1d8-5f599d81d688 | -15.76378 | -47.80465 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2277f113-3e5e-30ba-acb0-7f2656bce91b | -10.83638 | -45.31657 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a1ef052-5327-35de-a999-5385d215ff51 | -15.52725 | -42.33999 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a11606c4-f755-3717-82ae-33f288045179 | -10.83833 | -45.33335 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f1bdf0d7-7787-34b0-b2a7-c253607a20d0 | -15.52357 | -42.33924 | 2025-08-17 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf393f24-d8e4-3385-82c8-859fc20b8a19 | -10.82953 | -45.32253 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16aa68cb-01eb-3739-b190-6b7895484e41 | -13.60044 | -46.90186 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd24a0d8-2c4b-3af6-9bae-c002bd761d28 | -12.55529 | -46.94069 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76c6562d-2f85-38b1-a981-c04ccfb03aef | -12.55428 | -46.94596 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d65ff04-ee40-3165-ab6b-589b3869ef32 | -10.84219 | -45.36718 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| be3656b9-80ea-3fd9-81a1-0cf5e6b54db6 | -10.28879 | -48.3382 | 2025-08-17 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26fed58c-2a40-3bb8-a425-1c3308a19dd5 | -12.56001 | -46.94407 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3288c7c3-ba9a-316d-915b-da8519cf6b71 | -13.8761 | -45.5431 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61eba7ab-d381-320d-940e-86e2d7bf817b | -12.19163 | -47.23599 | 2025-08-17 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 521a00d0-49c3-3ae1-83a9-ede8b730517c | -12.44032 | -47.00463 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6e90a0a-91ad-3ace-9e29-3cd428c422ce | -15.14266 | -48.74099 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b00d374b-ac04-3aaa-895a-efb6aa7e6faf | -12.57269 | -47.04508 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43ec8038-2bdc-3dae-b9ef-7adba33de5c6 | -12.81851 | -45.98554 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2797264a-6004-32f5-8888-52824efeb7bf | -10.8297 | -45.32618 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cb681cf-6625-30d7-b5e0-ffa5dbf4d866 | -10.84412 | -45.3564 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6047f5c8-7070-3e61-8648-3f3f35549965 | -10.84118 | -45.37282 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5ce39223-0332-3b3c-a883-e754946133e9 | -13.43845 | -45.88189 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f796cc84-6181-3e2f-81da-c0e5663e57c0 | -15.18197 | -48.77453 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b87c0cea-6c6a-32e5-81ef-778de6302d36 | -13.59207 | -47.77443 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05e550c4-e1f1-3b61-a0ac-a1d9d4c2058c | -12.8635 | -46.06727 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 133e070f-4a4d-3e41-9799-da567531f3e4 | -13.58512 | -47.78146 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4849f62-c593-37f5-93d2-ac5c18d1b9af | -14.18655 | -45.31835 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c53734e-f9d2-305c-9815-c11938a27ad7 | -14.18569 | -45.32507 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39e683a0-064f-3e84-b43f-747032823bfd | -10.99742 | -45.63186 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e33c9e3-ff0c-3dfb-a51b-7c844d13eaeb | -10.84602 | -45.3458 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6ca1e424-4dd9-3c82-af3a-8f5c8ae7fb4a | -9.76524 | -48.75399 | 2025-08-17 03:51:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 559c8b88-7aa0-3d0e-b3be-deac70808b1f | -14.19382 | -45.33149 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b5ecd74-a15f-3a6a-a9c9-b186878babe8 | -13.44244 | -45.88403 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78f373a5-1abb-3d7e-8d14-023695d9dc06 | -14.18482 | -45.32772 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4937b980-9187-359d-8fa1-f7e258b00d14 | -13.01511 | -42.32565 | 2025-08-17 03:51:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| c6908505-794e-39bb-b8dd-e64124f9b659 | -10.83629 | -45.31295 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d0a62a0-8f46-38a3-99bb-5902a67680cc | -12.14137 | -47.9111 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 198e1515-f2ee-3415-aedd-38178fe7910e | -15.76877 | -47.80174 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e1600b7-a5eb-3bef-bbe0-6dba72cdcacd | -15.76364 | -47.8005 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 867f3d46-9c5e-36cd-977c-55d0aa0ae608 | -10.84276 | -45.35794 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 524c2616-ae8c-3433-aa15-c067b6726704 | -9.69604 | -46.26077 | 2025-08-17 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d2cab1-29ff-334a-817d-6fc5d960c022 | -13.58793 | -47.76709 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5526eb1-465f-3636-9950-303c7d6cffbc | -13.4367 | -45.88828 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c891fa85-dada-3119-9aa9-11599fa65891 | -12.61063 | -46.9062 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 797c8964-141e-3750-9b2b-ae39aff72452 | -10.83432 | -45.32346 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beb29c59-179f-3226-982c-1a991cd59e77 | -12.88901 | -46.13231 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b57ff485-9b33-3fe4-9c28-b6dbe93cb5c3 | -12.89692 | -46.11728 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a1b7bf16-5d13-3126-b48f-c8b2d63b0e4c | -10.85269 | -45.33622 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9710860e-0d59-34eb-9d6c-002f901c01a9 | -13.61986 | -47.75891 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6868a35d-abe2-3e2d-97a6-6e9c0d936787 | -12.5657 | -46.94242 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67f1b886-c461-3144-9d0a-f454c447d461 | -13.60813 | -47.77779 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
