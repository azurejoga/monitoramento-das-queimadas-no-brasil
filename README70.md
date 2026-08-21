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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bfc849c-df06-3ccc-980b-4621a8e7f44c | -12.80444 | -48.41175 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32fa123f-b908-3e56-99d1-28298182b0df | -12.12482 | -57.20583 | 2026-08-21 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 436f4a2e-5d23-33ea-b265-fbe68ad91ff6 | -9.21303 | -60.77264 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87cc9818-fc62-3318-b94f-d71148450e41 | -12.00312 | -53.43102 | 2026-08-21 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ec26cf4e-268c-33b4-915b-6c5ed28fd931 | -11.99953 | -53.4267 | 2026-08-21 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c21ef937-821f-330e-9d89-673c2aec5566 | -10.39519 | -61.20512 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888c52aa-0999-3146-b882-2ba0930f077b | -9.20274 | -60.87777 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31bd0d5c-0fe2-33d8-b1db-4724e4ba12c8 | -12.49552 | -54.75681 | 2026-08-21 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| cf534559-243b-3fc0-a25f-7bd72a32aace | -9.41237 | -60.55063 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 565fbab8-34b9-3c88-b54c-a7824d34ec5e | -11.17027 | -54.02204 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ea137445-55cb-3e99-b923-54f91cbfe912 | -10.75521 | -50.3171 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41f0db29-8b6c-3ce7-89ad-c40006533e08 | -19.75564 | -57.97845 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a9c02c60-7a2a-369a-b5d8-2e1eb25f1bbe | -11.1928 | -54.00476 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d640be-6f50-3092-8b81-9e4a584a95e1 | -9.41623 | -60.43998 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4d40d80-72de-3f52-a2d0-cd366ddeb6da | -12.79908 | -48.40298 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09ceeee8-28e0-3ad4-b354-c22e03b56d27 | -11.20671 | -55.0697 | 2026-08-21 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf18471-a6bc-3caa-8611-38f2f11840e5 | -11.2104 | -55.07026 | 2026-08-21 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8a11e32-a386-36be-bd72-24a366f8f2a5 | -11.20927 | -55.05215 | 2026-08-21 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8fa6692-d972-3344-a464-247fa6983e77 | -12.75079 | -48.46402 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35112ac9-7ec5-3f13-a4ec-bcd7de93ae17 | -10.7608 | -50.31747 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e4fc6029-0520-3bc6-a975-9d9798480a74 | -9.41309 | -60.41572 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| d063c287-f496-397b-9020-24db11227487 | -11.23801 | -54.82817 | 2026-08-21 05:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4351bd8-2e64-3be3-b726-45f4a86a77a0 | -11.19133 | -54.01485 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94aede8a-f22d-3117-868e-c81aa19f13c4 | -11.81453 | -56.6035 | 2026-08-21 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9be66905-58c3-3f93-aab6-f621d194728f | -12.8604 | -48.43545 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df7f9cd0-c293-3fd7-88b3-4159d52c3798 | -11.19672 | -54.00535 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a46c0e9c-3664-3e9e-a816-952ce4b053cf | -19.06872 | -57.37573 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| a92de8e3-e13b-3a41-b207-80098283562d | -9.38722 | -60.59445 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3687a822-aa69-3af6-ab36-5ccb9830c749 | -11.20065 | -54.0059 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bd3c110-24cb-3010-aa5c-76a34b4b61c0 | -10.75845 | -50.33469 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cfafc82-fadd-3275-aa0e-bacaff530afd | -11.17884 | -54.01817 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d73b3aee-6efe-366a-91b9-e561d618f8af | -10.76595 | -50.31272 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e535d8fb-154a-3322-8a00-173ad8b364dd | -12.8039 | -48.41613 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10b1988b-9e7a-32f1-8928-80e2083e6e6b | -9.42224 | -60.42514 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99577352-5664-3924-b38d-cd86bb09543c | -12.00671 | -53.43536 | 2026-08-21 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 200d07a2-d877-3cfb-8353-422e86499243 | -10.24761 | -54.36188 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c83986b5-0104-303c-9d85-bed7628533b4 | -9.38667 | -60.55428 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ad47bc9-71c9-3818-8bfd-c81111fe1671 | -12.74297 | -48.48008 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bee1d858-25cf-34ad-ae53-b26fd970e79d | -11.17348 | -54.02757 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 069f790e-a684-3657-a78b-e4c8b45b7cba | -12.74454 | -48.467 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39d4d3f0-fe65-379c-8720-91b95d627ca3 | -11.17957 | -54.01313 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d59906d4-4f50-3134-a7fa-064245d0ea8b | -11.68666 | -54.56836 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7df45a4-cff5-37d5-b6d2-6cdce4f0d987 | -12.84815 | -48.43895 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50b77aec-f050-3b2c-b58b-d790b6bee38a | -11.18888 | -54.00416 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c81933f-dc08-3c01-b054-e05f0295cbd4 | -11.17637 | -54.00752 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd7cfaf2-dddb-33b4-86bf-54b743aaeb4a | -12.78784 | -48.39774 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56ad723b-acd5-37a7-a714-9e8587b5ba9d | -9.21523 | -60.7812 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6e27130-6246-3c38-9c7e-1b014f1d8ca9 | -9.40551 | -60.41841 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 471a74c9-3d4b-3d0a-b93d-402ce93a4b80 | -11.16956 | -54.027 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5aef5c0b-0c5a-3270-9804-cb29c7f498e3 | -19.6602 | -46.04853 | 2026-08-21 05:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f249825-3476-305d-ba51-affaa7218ad9 | -9.41364 | -60.54287 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6fb5a05-4593-32e1-9474-163c3a403e56 | -12.47415 | -54.17974 | 2026-08-21 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 736d6d43-8fd6-3a60-a092-158ca1f70f7b | -18.03347 | -46.4704 | 2026-08-21 05:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2014cbb-3ae5-3681-9471-62597c0c33ea | -9.39428 | -60.55158 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51ab4a3c-957b-30cb-982a-031b54a926ca | -9.41649 | -60.54734 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd03b1fd-eac0-3f0b-887e-c46720129056 | -11.81799 | -56.60405 | 2026-08-21 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66d1ed69-b6e9-38a8-a8fa-88e99f4dc673 | -9.20311 | -60.7669 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 46225cdb-c14c-34d6-aaad-5a9c12fa7f76 | -22.18578 | -48.73857 | 2026-08-21 05:25:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 71e60df7-4550-3301-bb97-29e6d06bca4c | -9.41173 | -60.55453 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3fde447-cb80-35ca-abca-698e8d9b450f | -23.53557 | -47.31359 | 2026-08-21 05:25:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 42efd5ee-62b6-312e-99e5-5a33c17624b6 | -10.7558 | -50.3168 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeb52fdd-232f-34ed-9141-0360d5079476 | -9.40644 | -60.43439 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 61d227f1-c9b1-3e14-8aaf-24a67bcc6009 | -9.11921 | -60.92731 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286ed5ee-ccc3-34be-aa01-f164e5c6f620 | -9.39236 | -60.56327 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d2626d6-6696-38d8-b5f8-df3c2cee4efc | -8.73742 | -63.95058 | 2026-08-21 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0281bb8f-668e-32be-b7a2-c59886a25048 | -10.75346 | -50.33401 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e1675d-8e2f-3eba-9b5a-9733964eaf84 | -12.79815 | -48.41109 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e98f6b5-0377-36fc-b877-b4a847f5d848 | -9.53922 | -63.56641 | 2026-08-21 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7465b9ea-4fc1-3a9c-9a45-3338a3637ad8 | -11.18422 | -54.00864 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b09baae0-cd38-357d-b89c-54031ada8392 | -11.1803 | -54.00807 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f117b5f3-fe46-3c9c-bd28-d4e865ff645f | -10.39941 | -61.20166 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0c10ab2-319c-3212-bc48-1ff1f8736e81 | -9.41118 | -60.42727 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3ef8fbf2-c775-3793-a4f4-84d4c2f0832e | -10.76659 | -50.31241 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44fb93f3-5a66-3b97-b5ef-a08bdb7c631f | -18.69923 | -47.47036 | 2026-08-21 05:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1e34009-85a5-37f7-a1ef-37d4d6e3a227 | -9.12316 | -61.59867 | 2026-08-21 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc5de2de-9b3e-318d-9e5b-211f4f31bf5a | -12.75632 | -48.46711 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2343825b-0bcd-3ddd-a8c4-4cfb2d00274d | -12.83504 | -48.44976 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5de803c-82d1-389a-aec9-2ed278580afb | -12.80497 | -48.40745 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69e1e995-abe2-3120-9338-499380b1c2ba | -8.73316 | -63.94976 | 2026-08-21 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 686d210d-a3d2-3965-aff1-89d96408ab1d | -20.25554 | -46.76018 | 2026-08-21 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c5263aa-77d1-303f-9a5c-e2b64ced3895 | -12.84709 | -48.44785 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc75c37-9c4f-302d-a59c-679ec6ae8261 | -9.38731 | -60.5504 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e429cabf-b3ba-32c5-b6d2-2b03e75b4d26 | -12.50003 | -54.75263 | 2026-08-21 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e7ae175-7508-349f-b078-dd653c8027be | -10.25248 | -54.38147 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 428d9e0c-8315-3700-b553-5a3c8110b7ca | -11.17172 | -54.01202 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e25ea43c-42a0-3c3a-bb7f-202895833d1a | -9.40771 | -60.4267 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 40e643d3-d2cf-347c-b84e-4fbed6d1e5db | -20.2578 | -46.73191 | 2026-08-21 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ce2dd66-6dbd-3c48-ac2f-30d589ace76c | -9.42129 | -60.40918 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f60462da-2834-31a6-849e-b8fbd8e73f4d | -9.41813 | -60.42842 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f26bfdb6-54ee-33e3-bcbd-015679a3fd0c | -19.73215 | -57.96621 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7b583662-37e1-369a-9e08-8e1541d21807 | -9.40581 | -60.43824 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 24441d7d-f570-343d-9e71-3b51e2aa83f2 | -11.48878 | -45.11141 | 2026-08-21 05:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ebfb859b-a78b-32bf-8834-1d3eef1742d9 | -17.95769 | -49.3745 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d36f63f-bb2c-34f4-97ff-eaf38a03df66 | -17.95707 | -49.37195 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a0c2d1f-f09b-3e3b-af34-850a69352407 | -12.5016 | -47.84793 | 2026-08-21 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0e887dd-867d-35c7-b09f-5b1dcb70ae8c | -10.81828 | -50.99394 | 2026-08-21 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a649d1f0-d528-380d-94bf-ecaebf165ac6 | -10.39164 | -61.20451 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d2c90ec-3014-363f-af23-a6957ff8efa4 | -19.72981 | -57.95734 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| da41ee20-6810-360c-bd60-b6140de80cb9 | -11.16635 | -54.02148 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c7141696-5e59-3df6-8ec7-62f7e3c0a1c2 | -12.49934 | -54.75739 | 2026-08-21 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |


[Clique aqui para ver as próximas entradas](README71.md)
