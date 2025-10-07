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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413294c7-367e-3822-9c11-0ef90c3900d5 | -13.02816 | -51.03438 | 2025-10-07 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| e743590c-78d5-31a9-aca1-bac9507d7157 | -13.02005 | -51.02259 | 2025-10-07 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 288276cb-d276-3187-8a7f-1aefbe4eb337 | -10.28503 | -51.51403 | 2025-10-07 12:38:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fc4b4341-fac8-3079-8db8-f71b98a3d631 | -10.41145 | -50.26862 | 2025-10-07 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 791b2d66-b7fe-30a0-b730-52c1772f591e | -13.7133 | -48.33601 | 2025-10-07 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1a69c796-eac3-36f0-a480-ba4af00135cf | -13.25781 | -48.05637 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9bc145e0-0e21-3bc8-b828-a5476e167753 | -12.34291 | -50.26567 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4f77b1dd-b6ed-3e5e-b484-2970a228d46a | -11.14246 | -55.20033 | 2025-10-07 12:38:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| efdf0cd8-11bb-38d1-80a9-be828f6da9bd | -13.40611 | -47.59039 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2e783912-a934-3ebc-a268-145ca8bcb2fd | -15.39433 | -48.006 | 2025-10-07 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 62b2b47a-2476-3389-a7ca-89a74c713f17 | -12.48623 | -54.73506 | 2025-10-07 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eba4da93-fc5a-364d-92d7-b00c69c648e9 | -10.80878 | -48.59117 | 2025-10-07 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 89403409-ec06-32c9-9dcc-78862d43fb1a | -15.63531 | -53.82156 | 2025-10-07 12:38:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d7ec56ff-ae5b-3914-b804-79036f15c210 | -13.66738 | -47.94865 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f8aa12e5-4e93-3e25-8248-74a09aaab976 | -10.24722 | -52.69225 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 454977db-3ef8-3440-b34d-f74cfa9f04c3 | -10.40296 | -45.38873 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 74e29e23-30ec-3254-a5df-4954edc968f5 | -15.25739 | -50.20649 | 2025-10-07 12:38:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e705ddf5-e41d-367b-8da4-804b2a6239ec | -12.4089 | -51.13794 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 2bd69fac-15d2-3c3e-8740-d0a8c60630d7 | -10.89257 | -47.12225 | 2025-10-07 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 1edb226c-2f33-3f3a-a628-2e0c2d2c3c7c | -14.78842 | -46.04928 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| f1a2001d-c636-31ee-998b-16853f6f568a | -10.42782 | -50.39538 | 2025-10-07 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 9d44f0b7-375f-391a-bf2f-d64a32d04d9f | -11.95439 | -52.62309 | 2025-10-07 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b435b2b1-fd10-36e7-8736-1613625e7766 | -11.95312 | -52.63215 | 2025-10-07 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aeaf207c-3134-3271-8fd3-4dc3f0e54386 | -14.64652 | -52.53574 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f102e5f-beab-32a5-bbae-eb06c7ac1923 | -10.38252 | -47.98953 | 2025-10-07 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 1c45e78a-9264-3623-b1aa-5d48d421fd7e | -12.91043 | -54.73742 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 26162f34-a86e-3d52-93de-5d73a3d6355e | -11.94734 | -51.47644 | 2025-10-07 12:38:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cf54d37d-c10d-3ab9-8c87-9c73a8c0e48f | -10.80032 | -50.57701 | 2025-10-07 12:38:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9d773da2-6ea1-3ed3-883f-3445f84bf6c2 | -14.28998 | -45.84773 | 2025-10-07 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 19aeda74-0526-3423-82ee-295e5c2a7fd2 | -10.94104 | -51.10308 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 105db1c4-7ab5-355f-bb1d-609caf4da800 | -11.40716 | -50.85017 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0417bd4f-c297-32e5-8569-9cb4f80d1a97 | -10.40586 | -45.365 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 12733ce4-3b42-3682-b653-2897544add39 | -12.62862 | -44.76026 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| a48cb36b-84fd-37e0-8dd2-037601863125 | -15.60512 | -47.28122 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| d8b50f59-c563-3171-98ca-def1981f8824 | -13.66549 | -48.73507 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| e7b77001-95d0-3db9-b5d4-ce70af6a2d72 | -16.01608 | -51.04642 | 2025-10-07 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 1792449c-b4da-3892-8d67-cade0a08e95a | -15.6293 | -52.55283 | 2025-10-07 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 6ccd79fc-4053-3072-80cc-12e0dba36824 | -10.41987 | -45.36674 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 4b498aaa-0b43-3c29-b331-abeaeccdffb9 | -12.93172 | -57.62094 | 2025-10-07 12:38:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 784db38a-cb32-3b6f-bc62-e50a14eb3eb8 | -14.74173 | -46.03873 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| fee20596-1fb8-3ae7-a3ea-183c1602f740 | -15.36583 | -47.32367 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d0c77ea3-f68f-3bf3-927f-80471513bbf1 | -13.71276 | -48.07491 | 2025-10-07 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3f3dbab1-2663-346a-b7c2-e98ed073c165 | -11.95233 | -46.44683 | 2025-10-07 12:38:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 9424ce2d-d325-34c0-979d-2475398ad72a | -11.95057 | -52.65026 | 2025-10-07 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0baaec8f-cf6e-3f01-a33d-75b4cd902201 | -13.98232 | -53.91511 | 2025-10-07 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3a48f649-ef75-33df-bb2e-c752011d08d2 | -10.92691 | -47.07817 | 2025-10-07 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d698c608-3b50-3f6b-8b1c-c18c206861ae | -13.71488 | -48.34566 | 2025-10-07 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 30feca4d-f3d0-38e4-a86e-d213fd303ddd | -13.71148 | -48.35144 | 2025-10-07 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 96044d23-19c0-3855-843e-32679af79110 | -11.14399 | -55.19023 | 2025-10-07 12:38:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 9e26e85b-2a24-3fd2-af16-f1074e4801fb | -12.73581 | -47.93699 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 7d00937a-54e1-392c-b742-3d151f9f18bb | -11.514 | -51.484 | 2025-10-07 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5f9a6868-f702-3c7a-b52e-8f6178ebc6d5 | -12.89099 | -54.74409 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 229.5 |
| 65e38dd9-80d3-3de3-9693-4a5e271b0a0c | -10.42476 | -45.37423 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 37662fae-1b9c-31d3-849a-77cd59d60793 | -10.42193 | -45.39848 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 222.5 |
| b876e2c3-1b47-39d5-b5f9-b09ed6f56e62 | -15.21866 | -49.31218 | 2025-10-07 12:38:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b651d878-15f7-3916-8491-1c908be572c5 | -15.59443 | -47.25869 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 56ebc212-1355-324c-bfdd-a9a0cf0d4bb5 | -10.73965 | -46.67372 | 2025-10-07 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 589db31b-0b81-3798-9571-23a1fe4703f2 | -15.36803 | -47.30332 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 6eb3047c-9cec-302b-a125-7237d316fe6c | -13.01054 | -51.0213 | 2025-10-07 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 6c54943d-0cb3-3791-acc8-bb3c3efe1cbb | -12.41405 | -50.27006 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| bb58d11f-894b-3991-9dfb-1a338237543b | -11.04859 | -50.92125 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b5c28d1a-b905-3011-a9d4-bd1ca119c676 | -16.24477 | -44.05019 | 2025-10-07 12:38:00 | TERRA_M-T | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c699e727-ff52-3bfd-a1ad-5a08fcc55b71 | -14.29352 | -45.85325 | 2025-10-07 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 257.7 |
| fcabeb42-b5cb-35a6-8132-82e9a3983f7f | -11.13465 | -55.18885 | 2025-10-07 12:38:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 5df5f5fe-e89a-361b-9229-09e988ceb9c6 | -14.62558 | -52.48781 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f35ce6a5-1cba-32fb-8546-348119e50c61 | -14.7302 | -46.01241 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e8401796-12f0-3360-882f-6f8f7be6c1dd | -10.43083 | -45.39283 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 0bc79850-267a-3476-8b44-a4b2df5de582 | -10.80706 | -48.60437 | 2025-10-07 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7346ff56-dde4-3a20-9f7b-8a6ac5ab2813 | -12.41556 | -50.25871 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| accbcd29-997c-30dc-8810-a4b760f98baa | -10.44194 | -50.28947 | 2025-10-07 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 5f98eefd-d3d7-3182-bac3-81ecf811ae2a | -13.31393 | -48.05158 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ef09fbf1-6c77-3927-9bac-cc5aa355866e | -14.78429 | -46.0435 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ed9aa029-a4b3-3eb5-9ad4-b4a4a0206a3b | -12.39813 | -47.17908 | 2025-10-07 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| b2b5e083-8533-3e73-9940-3f6ead28cfb3 | -16.37915 | -48.99251 | 2025-10-07 12:38:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| aeec3c83-6478-3992-bffe-4839e12c99ae | -15.39092 | -47.99861 | 2025-10-07 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 11a47f01-8c66-3240-b2b9-9f1184a882f8 | -13.24156 | -47.22885 | 2025-10-07 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| fc8aa180-b5f6-30da-b42f-6478e159e127 | -13.09305 | -48.00673 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 55992580-38fd-3162-a381-58faff33cc36 | -10.64565 | -46.69505 | 2025-10-07 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f5e8667d-42d4-3cbf-acdc-507d03cd8e6e | -16.28937 | -50.98407 | 2025-10-07 12:38:00 | TERRA_M-T | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 58ecdcd2-34d3-3b39-a93d-daebc4178b71 | -14.74444 | -46.01377 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 2722e97b-53cf-3452-8ad1-2e0b6848cc1b | -11.67904 | -46.33265 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5e574ad9-3113-39bf-9e01-62c9293c7188 | -12.38798 | -47.15868 | 2025-10-07 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c91da899-48df-3345-bceb-a673d97f1ec5 | -12.05553 | -54.40289 | 2025-10-07 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cea1135d-d31a-3cac-b761-d2f63a7706ef | -13.67379 | -47.9437 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| af737e95-f5c5-3e84-aee0-26909b62709b | -13.78796 | -45.75941 | 2025-10-07 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7e27a8d0-5e7f-34ca-b1a7-076212d5f0a4 | -11.03401 | -50.88844 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5e0ed021-8f47-3d7c-a686-aa3d059098f0 | -13.31593 | -48.03494 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 9be0dc8e-1302-34c6-8fd9-38e2b270afe4 | -10.9503 | -51.10434 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d9151802-2118-35e3-8cd7-63187b071dfd | -16.28103 | -50.97046 | 2025-10-07 12:38:00 | TERRA_M-T | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 8156df51-b91d-38b8-b075-247cf7d659e1 | -10.89479 | -47.10439 | 2025-10-07 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 248.6 |
| ddfdc91e-d7c4-3c7e-b5b2-bafb89c3f508 | -15.74041 | -51.04792 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5ec4dda6-e443-3347-b8d6-ede0abf1f88c | -13.05005 | -49.15823 | 2025-10-07 12:38:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 990be037-5e12-31ff-9078-09868f392112 | -11.23629 | -44.76447 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 36da79ef-cf86-31c2-b8aa-dd9ba9a9c9f5 | -15.99 | -50.93743 | 2025-10-07 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cb71bc7a-66c7-3004-81e0-e49a98086939 | -14.2929 | -45.82232 | 2025-10-07 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| fd5dbd06-834f-364a-b1e6-bfec15dd7693 | -12.89239 | -54.73467 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 26bcdaed-cbc6-37c7-856c-9aa368e5288f | -10.39681 | -45.37027 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 2d5fc386-52cf-3c60-aac7-9df6d5bdb58c | -12.72622 | -54.48702 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 248c6bb5-38c5-316f-a52e-de63a1714bfa | -9.86528 | -51.68056 | 2025-10-07 12:38:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5326ad6b-4f1d-3bb8-8447-2da74cad7579 | -10.24594 | -52.70116 | 2025-10-07 12:38:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |


[Clique aqui para ver as próximas entradas](README116.md)
