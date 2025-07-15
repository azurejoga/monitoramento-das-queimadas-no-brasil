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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97e0db00-1566-3399-85c5-5332c7c025c2 | -14.58543 | -48.12038 | 2025-07-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f0b5a00-4687-3214-9c14-eba433967fd3 | -12.28631 | -48.79255 | 2025-07-15 04:34:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6b1f1d1-bf5d-3325-96b7-adeaa669c523 | -11.73233 | -47.0591 | 2025-07-15 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7909751b-e16a-38b3-9c09-f2b9b2404f17 | -11.46025 | -45.09641 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 00f4cda4-1f5b-3cff-a466-d223437db6e8 | -12.40611 | -45.36829 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52fe5d45-d106-3260-bbf8-b441fad4683f | -12.10143 | -44.74007 | 2025-07-15 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c30ce4d7-8983-3cf1-b446-62b2b94cb072 | -12.40169 | -45.37239 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a7b10ad-8e13-3935-86f3-5e1989f1e19f | -11.90413 | -46.75062 | 2025-07-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a57c4809-7516-33e8-b589-e1a1bbb8e490 | -10.05862 | -59.11422 | 2025-07-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a66d67-bc8a-33c5-ab8a-10abce226854 | -12.70909 | -46.80214 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98833d21-7ae8-34f6-a039-3d46b7aff7e4 | -15.22608 | -46.96813 | 2025-07-15 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 675b4ad4-8faf-3d5c-9cd2-26f3ef193668 | -11.52684 | -48.95903 | 2025-07-15 04:34:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47fac748-b721-3fbd-a6c3-5f17635f857e | -13.04349 | -47.81218 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 831c38b6-61f6-37b9-8368-0abeb6083381 | -10.87028 | -54.06196 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18a60c98-8681-3f8d-b911-8393c6463fd8 | -10.86349 | -54.05351 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d0c2350-2346-36dc-8c60-e2d17acce217 | -12.40988 | -45.36882 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0b8195d-f6f4-3a45-a1f2-93a9cab5e585 | -10.87549 | -54.05566 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0826cfb-8e32-3aae-8599-733773c3664b | -13.65174 | -45.73272 | 2025-07-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0427d3cb-7385-3073-9eb0-11f4d312a490 | -12.34508 | -49.30706 | 2025-07-15 04:34:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a8ec2f3-7cca-36ba-bd0c-100f874a2ebb | -10.16747 | -52.61841 | 2025-07-15 04:34:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dba76ab-911c-35b2-9295-d7872676ad46 | -10.87889 | -54.0599 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74dec6c3-aeca-36fa-91a6-e94ac5d3c7f0 | -11.72788 | -48.51881 | 2025-07-15 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4adbd69e-71d4-3641-bf61-029f74fbe965 | -15.23091 | -46.98545 | 2025-07-15 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4cefc7d-8bd9-3291-be58-0b9e43246f2f | -10.64972 | -46.6296 | 2025-07-15 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c61564b7-2a1d-33a2-a334-4eb837cfa58c | -10.5613 | -49.13694 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a34ddb22-5d58-39e5-b149-f156f78504a1 | -11.45293 | -45.09285 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e18afa42-1d5d-3e03-8a55-ce8f2dac6f43 | -10.64914 | -46.63346 | 2025-07-15 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c61c46dd-15e8-3211-bf68-947509a699a8 | -11.35882 | -48.73039 | 2025-07-15 04:34:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a6009d-0b96-363e-bfb4-02325e401425 | -11.47142 | -47.30698 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 081feeb4-4271-38d8-bafe-d7cfd654c53d | -15.22728 | -46.95972 | 2025-07-15 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85519a23-1a17-3ed4-b62d-89e8dd94c135 | -10.66934 | -56.55235 | 2025-07-15 04:34:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bcbc906-6447-3f03-acea-ffd01845472f | -9.35048 | -58.8328 | 2025-07-15 04:34:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95675ff-f882-3214-b0c9-a06d050dce27 | -12.41053 | -45.36418 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| beacaba7-e646-312f-a34f-a790f5c88810 | -17.1403 | -45.93823 | 2025-07-15 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00840405-c122-3ad9-b6ff-08d565d65993 | -13.65549 | -45.7333 | 2025-07-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 25341468-941e-3380-879a-4ad64094061b | -12.68168 | -47.87006 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bffb820e-dc93-328a-9f2e-c9ff79f8635f | -11.46095 | -45.09167 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 5a504559-4269-3899-9dba-f7714ae8ebc6 | -11.45786 | -45.08642 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1461442d-c539-3bfe-9ed0-50bfe44a3b87 | -10.96766 | -49.25285 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c3acf32-45db-36cc-adb7-2ba7ff686c0b | -11.45984 | -45.09864 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 7ebc5d0e-e862-39c6-bac8-5c0a7544b905 | -11.46297 | -45.10386 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9b47c9f-e170-375c-899c-6ea7d916f59c | -11.56156 | -47.31215 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc136268-2d43-33e2-a82b-16f1a4e08003 | -10.79094 | -49.2527 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9d5f687-f0db-3d17-b091-61e0af8a3c93 | -10.06013 | -59.10617 | 2025-07-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5336c4b0-da5d-3d55-9bee-20070f7f0687 | -11.4551 | -45.10522 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| feab9a72-666e-3dc0-aa45-014c57da4f6e | -13.03448 | -47.82589 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a497fc5c-0f54-3392-9cb1-9a9d5a85d0bc | -10.13022 | -57.77442 | 2025-07-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b65961e-0840-30cd-a744-6cfea84aeb88 | -11.45338 | -45.09063 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| ed38f73f-f652-359d-86d2-2ce8ecc5fbc1 | -11.43968 | -45.13146 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32dda7a8-866d-3623-a0a4-c949de307b61 | -11.44705 | -45.13482 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f4cd6777-84a6-349a-ac10-ce9e5bc6f9c2 | -13.13195 | -47.2667 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 722843b2-6138-3b5f-bcd2-f5c6f1a87521 | -15.23739 | -46.96576 | 2025-07-15 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753e14f8-7528-3432-ba0c-8860181a7d06 | -18.65411 | -55.72438 | 2025-07-15 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bf464cb9-bb5f-3868-af0c-5612c35667db | -23.40422 | -46.55577 | 2025-07-15 04:36:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a3a5fcff-d3a1-3e18-8cf0-8b2dd3578897 | -18.44477 | -54.67613 | 2025-07-15 04:36:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 927fa6dc-cdb9-349a-9e0a-bc741683017b | -23.3367 | -46.77248 | 2025-07-15 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6fc7d524-656d-30b2-9559-bb913fb7f91a | -20.99477 | -51.79081 | 2025-07-15 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4486a989-3ba8-3d99-8734-71aecfdb3a50 | -23.33504 | -46.13942 | 2025-07-15 04:36:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2766684a-a15b-348b-b1cb-120dc61fc8a5 | -23.29548 | -53.17943 | 2025-07-15 04:36:00 | NOAA-20 | TAPIRA | PARANÁ | Brasil | 4126900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c618f27f-0f88-3954-b053-a22f8e6b40e2 | -19.658 | -46.18653 | 2025-07-15 04:36:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8725a101-5f56-3b36-9002-a952cb5d1854 | -20.37073 | -46.56409 | 2025-07-15 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf91b531-675a-3584-a64b-97cfd2903859 | -20.75929 | -46.01897 | 2025-07-15 04:36:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b358a2c-8b3b-333d-8853-f82ec3a24da8 | -19.15923 | -49.13957 | 2025-07-15 04:36:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 512dafc1-cfdb-37b3-8683-092d1b040954 | -20.71717 | -48.03373 | 2025-07-15 04:36:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26b4dcb3-e7fe-3bad-b6bf-7438aaef551b | -22.57883 | -44.08002 | 2025-07-15 04:36:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c01db8df-d04b-35ac-9ec2-cba12978196d | -20.14089 | -50.72137 | 2025-07-15 04:36:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b8d6fe78-7fd2-39a9-9747-02f9ebe81525 | -19.75362 | -53.99676 | 2025-07-15 04:36:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c2ae211-3808-33eb-97b9-65ce913308b7 | -22.67664 | -42.85376 | 2025-07-15 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ba582ff7-1d1b-37bb-8237-785d87ed0842 | -21.7703 | -52.75637 | 2025-07-15 04:36:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e11fec6-8db6-380c-b0c9-04db470bf2cd | -18.65114 | -55.71833 | 2025-07-15 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cb552875-2af6-398d-8fe8-5e23e73ba5a3 | -20.597 | -45.1074 | 2025-07-15 04:36:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 130b1bf0-89bc-36c8-9da0-accb5fd170f8 | -21.77302 | -52.76081 | 2025-07-15 04:36:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e43ef206-ba35-3bd7-acab-8c67398b1996 | -17.70539 | -53.84287 | 2025-07-15 04:36:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dabf5bc-7f91-3ab4-a7d3-1072385e641a | -18.6542 | -55.72069 | 2025-07-15 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eb8815ea-e7ca-367e-b842-50585533d13f | -21.76968 | -52.76018 | 2025-07-15 04:36:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d882f9c2-dc39-3b92-8380-bb6b476df737 | -18.32467 | -52.48678 | 2025-07-15 04:36:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71c767e9-0597-3f72-9259-9dc1d38c5c57 | -19.16264 | -49.14011 | 2025-07-15 04:36:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1172476-478e-3456-94fe-c5122e926611 | -22.67427 | -42.85709 | 2025-07-15 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f2b83a4e-9a90-3653-bb1a-5c7b33038e2e | -22.51477 | -47.01147 | 2025-07-15 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b8d2d4e-fc0f-3dde-a457-4cebca0cb8d1 | -23.59245 | -47.43909 | 2025-07-15 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f7c4908-12a7-3762-a740-3f9fb78ed783 | -20.14421 | -50.72194 | 2025-07-15 04:36:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9c0b3f2b-da47-381f-86cc-4b93008186c7 | -22.24971 | -49.61244 | 2025-07-15 04:36:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e3337274-0c01-3f88-a678-f9d5203ddc90 | -21.04244 | -55.98637 | 2025-07-15 04:36:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7087aa17-2a4d-3f38-8a56-a43571e37bcd | -20.3936 | -46.54089 | 2025-07-15 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70599fd3-a9eb-3d77-93bb-f8d31f700259 | -23.02584 | -52.64418 | 2025-07-15 04:36:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1966f104-8c86-361f-9b99-2e04688825f4 | -21.11318 | -48.40056 | 2025-07-15 04:36:00 | NOAA-20 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b2310f6-11e0-39fb-8b50-4c2fd5b0454a | -19.28888 | -55.15672 | 2025-07-15 04:36:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adc8b9c3-ec76-3457-992a-e5437f154045 | -19.75289 | -54.00094 | 2025-07-15 04:36:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 927cfe35-9d5d-34af-a173-67ebff56ddc4 | -22.94492 | -43.68943 | 2025-07-15 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5c9a9b3-695c-3e38-b5b7-a06343d52bfd | -21.85897 | -56.74776 | 2025-07-15 04:36:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 138d7fcc-3b87-30da-b0ed-c8e1dfc41486 | -20.76341 | -46.76679 | 2025-07-15 04:36:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcbb0d2c-7026-393d-a709-cd3a23c6ebef | -23.51267 | -47.21766 | 2025-07-15 04:36:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6089675-17e4-3cf7-8bb4-ef1adde53110 | -18.81759 | -45.74068 | 2025-07-15 04:36:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52f4812c-6b84-34a9-9dc9-5f9775716596 | -18.65322 | -55.72592 | 2025-07-15 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3a35572a-556e-3cf5-a30d-f62b2da0dea8 | -22.24626 | -49.61191 | 2025-07-15 04:36:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13862bad-b65d-3ef0-814a-29490a464340 | -22.6763 | -42.85693 | 2025-07-15 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9dc12703-c33e-3675-935d-af1b0372227e | -22.54033 | -48.81106 | 2025-07-15 04:36:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ba235f4-9125-314b-b13d-c68ed4365a8d | -23.20516 | -50.15442 | 2025-07-15 04:36:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea6d60ed-982c-31c8-95a8-32ed3912f054 | -20.47795 | -53.67516 | 2025-07-15 04:36:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f7d3608-0d5f-3350-a450-5f4d235a4086 | -21.76634 | -52.75955 | 2025-07-15 04:36:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README22.md)
