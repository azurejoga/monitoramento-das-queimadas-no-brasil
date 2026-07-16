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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea8d7727-ec7e-347d-bbea-c23d2a4d0062 | -12.88387 | -58.28551 | 2026-07-16 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27eda6ef-844f-32a5-a643-2986062306f1 | -13.26725 | -45.14325 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 28b5ebec-248c-3a34-9a8e-23b938e2da27 | -4.27209 | -64.14779 | 2026-07-16 05:16:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 498b0fa5-1086-333f-99d5-78b179bb39e1 | -11.54256 | -50.30737 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c837594a-d542-3fbc-9a0a-69d539ec7536 | -11.78347 | -47.0929 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b5d1613a-3673-36c9-8b0b-e3ab9f440994 | -9.45641 | -63.87619 | 2026-07-16 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93f7a7c1-2761-3f9c-9b00-4660af0c6ef0 | -11.5476 | -50.30804 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0631d4e-f168-35d9-a10f-cf776612291d | -13.25726 | -45.13952 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| fda6f129-ec6d-33fd-bff1-6e5ee9248164 | -11.748 | -57.81623 | 2026-07-16 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85136c42-f924-3ae2-b294-00425e06634e | -13.52707 | -47.78933 | 2026-07-16 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 115f253a-1008-377d-b532-35516677a516 | -13.25454 | -45.12744 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 89600be2-dd1d-3263-b718-05b69090fee6 | -13.27003 | -45.15545 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 060dea04-e515-3442-8ef5-0852c1dcf6da | -9.4529 | -63.8716 | 2026-07-16 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 59e71184-7ccd-34b8-8c9f-db00d5eabf77 | -12.46112 | -49.58792 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0275c2cd-9255-3f6b-b332-4d94d378740f | -13.25378 | -45.13453 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 2a58fdf7-8f51-3b43-b96f-446d02427b2c | -12.07318 | -49.91696 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddc039d-7cde-3b3e-ad63-d2fb7185b896 | -11.79168 | -47.09088 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01c3f835-ab3e-3e42-83ac-c93389ff9c0b | -13.26929 | -45.16271 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ed1af3df-0e33-3fbb-8d40-4f53eaaa25f8 | -12.45574 | -49.58741 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cfaae06-cbb5-3599-b3bf-b69f6f416600 | -12.88719 | -58.28605 | 2026-07-16 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53f30066-f65b-304f-b9fd-497da036dda1 | -11.09999 | -47.80781 | 2026-07-16 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67881a34-e7a1-3044-b068-4c7fe8b97203 | -12.44586 | -49.57908 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94d20d93-ce13-3fc7-9735-3ed45f4ed4b6 | -13.25941 | -45.14914 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 3b1f34f6-be3f-3707-bbac-968e38c552cc | -9.45223 | -63.87546 | 2026-07-16 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3e161bfd-15cb-3cb2-a287-87c74f04a6bc | -13.26163 | -45.12857 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 85f2b66d-caa1-3cdd-89d1-2fffc2d6d19b | -13.25657 | -45.14631 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b9608a4b-61e5-3ab3-a2a7-ad2720cea6e8 | -11.78542 | -47.09028 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 80e0f480-e7d5-32ff-b405-6a3e55980478 | -11.78482 | -47.09518 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1bd6ed2d-6424-3afb-a9ab-cb87794a7c5e | -11.11956 | -49.77151 | 2026-07-16 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e8db58-4c3e-35de-ba97-19bdccb14795 | -11.54218 | -50.31031 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6dae3d55-8c91-364e-90f4-c0b60bd2195b | -11.53752 | -50.30669 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36fea98d-7294-34ff-b443-afa931bfe020 | -13.26088 | -45.13552 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 733e4e1c-9994-3286-a361-8db00d63a193 | -13.55032 | -47.80244 | 2026-07-16 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 097f1964-765a-3c1e-9168-b6529718293a | -12.45616 | -49.58394 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c0bf5b7-d545-31ba-8936-03f2d5604a7a | -12.41403 | -58.40265 | 2026-07-16 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5512475c-af88-31f8-9ac6-0d1f8df3deea | -10.03738 | -51.66011 | 2026-07-16 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac67b273-1ee9-3f19-9a84-3a0982bdea79 | -11.12071 | -49.77046 | 2026-07-16 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5da2d257-ef57-3869-9fc9-2b2c5d42c164 | -13.26015 | -45.14231 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 8aac4b8d-cac7-30d2-aff5-0c80f1988153 | -11.7903 | -47.08859 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 74dc6d3c-e4ed-3fe8-bab4-0a322c420355 | -13.42958 | -49.13358 | 2026-07-16 05:16:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 93ad3e27-1fc7-3c8d-822f-e17dbbf25813 | -10.95308 | -62.00419 | 2026-07-16 05:16:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af47ddc5-e0e9-3693-8633-9e5d5d32e4c0 | -10.04187 | -51.66076 | 2026-07-16 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52de4d66-128f-3c20-940c-c498682fdd3d | -12.45532 | -49.59084 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68a42c74-8785-33fc-983e-75d618a8a355 | -12.93446 | -56.64188 | 2026-07-16 05:16:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2761051a-18ed-36c5-be3b-a51ab21f3aef | -13.54921 | -47.81218 | 2026-07-16 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c7421f4-7bb4-3f80-9e5c-efa873f9886c | -12.44051 | -49.57826 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba2919a6-a5b6-3818-bc50-83eecb9fefec | -10.03676 | -51.66467 | 2026-07-16 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f097126d-b6f8-3e2b-8442-7d1393234193 | -11.09461 | -47.80268 | 2026-07-16 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed79e7b-ffd2-373b-9032-d6642c95f302 | -13.26437 | -45.14043 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 8097d8b3-6c85-3f68-a2e8-9f2a59eb5ac8 | -13.43005 | -49.12971 | 2026-07-16 05:16:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fd1f35fa-0656-36d4-8f88-2e5681bf6b19 | -9.47922 | -57.32102 | 2026-07-16 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb59bba2-b322-3f17-adfa-af878f8867c2 | -8.60635 | -63.4599 | 2026-07-16 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6a5b545-d9be-30c0-a9a2-bdda845cff4a | -13.27202 | -45.16552 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ccf37c04-b136-31f3-8e75-ab6ba5755044 | -13.26572 | -45.1573 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ac2e056f-8908-366d-b660-643a79c8b1e3 | -11.54722 | -50.31098 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acbca118-80a7-3a69-807c-ed351b3ee6d0 | -12.0736 | -49.91376 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95d6e6c-30aa-309a-a909-fa4f46b0f0ed | -13.26494 | -45.16451 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0227df24-931f-3e1e-9b5f-b11f3efdb624 | -18.42167 | -54.56208 | 2026-07-16 05:18:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35365d5b-8711-3008-8f8c-3578d5cd53e5 | -19.84178 | -49.07641 | 2026-07-16 05:18:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bff55076-fcfd-33a1-8195-b579b4f584af | -13.6613 | -59.83543 | 2026-07-16 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c3bfa6c-2936-3885-aec7-cbe8ec9a6359 | -18.62448 | -54.91391 | 2026-07-16 05:18:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38d1d870-748e-3b5b-a738-3ff5a66e46aa | -18.62386 | -54.91301 | 2026-07-16 05:18:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b5ce73c-1234-3587-9825-9b02cf6479f1 | -17.84196 | -52.4899 | 2026-07-16 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5b447fe-2c29-3087-a4fd-38c22eb34cc6 | -19.71639 | -50.20803 | 2026-07-16 05:18:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f95e988-c612-30cf-9cae-4ba60ee91696 | -17.84129 | -52.4884 | 2026-07-16 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee963526-8fbd-3845-b465-698a693319bf | -19.716 | -50.21206 | 2026-07-16 05:18:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 79822332-be3a-3d66-a7a4-536516c76678 | -19.83007 | -57.95592 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f56653b0-48eb-381d-acb2-57469229d2b0 | -19.82598 | -57.95632 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6d69a271-919b-3020-880a-7db7b4be1279 | -21.66577 | -56.31921 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f852661e-ea8d-34ab-adcf-f0f62f833046 | -22.18664 | -56.0788 | 2026-07-16 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea99d878-3489-324b-a6df-e3530ad4cc12 | -19.83416 | -57.95233 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22be0e65-bfda-381c-891e-5080109a97de | -21.66646 | -56.31397 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd92c97a-fb07-3a59-86fc-35d06d1cd5bf | -19.83065 | -57.95177 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 058db33a-a23c-3c1f-bf49-53a53c239d21 | -22.96499 | -52.70686 | 2026-07-16 05:21:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d9a7c420-d9f4-32bb-8d9f-c38bffae9b51 | -21.66632 | -56.31551 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a89998ab-846d-3867-92e5-4d2a126c8ddd | -19.8295 | -57.95688 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ce2f7ee7-e16f-3aec-857e-27fb5fb70d45 | -19.83358 | -57.95649 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 43ae03fd-1882-3f1b-999c-11eac556cc07 | -23.34185 | -52.33036 | 2026-07-16 05:21:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a7f27a9-a519-35b2-9e87-5dc0ae19b7f5 | -21.35136 | -51.04569 | 2026-07-16 05:21:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 874d12c0-b704-30e8-b241-34632024a5dd | -19.82655 | -57.95536 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a4c5ffa5-8773-3f7e-8f24-0a3a04e13601 | -22.24766 | -55.99461 | 2026-07-16 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 2f6752ab-6be5-3cbc-b3e7-070bc6f89160 | -22.24624 | -55.99459 | 2026-07-16 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7c2175e5-982b-3f68-83bc-e85f61ed8fc7 | -25.4259 | -52.89877 | 2026-07-16 05:21:00 | NOAA-20 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a6c53485-0c4d-3056-84a5-cc3264268a90 | -22.19133 | -56.07385 | 2026-07-16 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19412265-f488-321c-8d1e-d6505f78b2be | -22.25027 | -55.99505 | 2026-07-16 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8f4aa0da-5983-3e89-a88b-0292392cc2b3 | -19.8301 | -57.95274 | 2026-07-16 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d96a576e-7f13-3c54-80d3-adba915b3473 | -23.56322 | -47.51911 | 2026-07-16 05:21:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 340d82f3-02d8-3bd6-9544-03f94572eea1 | -21.66566 | -56.32076 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed3390ba-6dfb-3b94-9ace-fc10da3c19d1 | -21.25672 | -56.12281 | 2026-07-16 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e93666a-0b22-307a-a6ad-0b7ac32ec1bc | -21.25594 | -56.12421 | 2026-07-16 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad91f445-e3ff-3bf5-b0e2-b192a96d72d1 | -21.67038 | -56.31447 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91a0a5ff-d803-3877-89e7-a8f2336ab46b | -22.78904 | -49.35251 | 2026-07-16 05:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb38b3f7-b214-3100-9d2f-7624b7824265 | -23.33669 | -52.32986 | 2026-07-16 05:21:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c20b9391-a280-3ce3-8411-05eb7487695e | -21.66968 | -56.31971 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c50f943-5023-3be5-8f5f-aeeecc65c408 | -21.67023 | -56.31601 | 2026-07-16 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab31e1e-0cb8-39c1-ab3f-1508db01000f | -9.45037 | -63.87281 | 2026-07-16 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbcd1c9a-f70f-33fa-a0c5-3dba6a51d8c2 | -10.01417 | -67.70004 | 2026-07-16 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6371aa19-b39d-3593-ad0d-df07c69b56eb | -11.78136 | -63.03627 | 2026-07-16 06:01:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2885473e-0156-30c5-9e18-a032f5471313 | -9.45643 | -63.87056 | 2026-07-16 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d881cb0b-08cf-3b8a-92b9-974946805898 | -9.45128 | -63.87452 | 2026-07-16 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README6.md)
