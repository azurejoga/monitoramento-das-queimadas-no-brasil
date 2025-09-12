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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a0c60c8-88e6-343b-9143-4609f3ef3520 | -18.98145 | -41.53122 | 2025-09-12 04:27:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0e8072b2-d38f-3fee-97df-1e36e4bca0c4 | -19.999 | -44.23236 | 2025-09-12 04:27:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ba838a89-c25e-3236-8f87-f5b311f20a29 | -15.78773 | -52.23545 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c5b9ecc-3ba3-3252-900c-ae85653b19b1 | -15.48984 | -47.34906 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3185b10e-ebe7-3f70-ba00-3b8766b8bb0a | -11.18472 | -55.09119 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e00660fc-4901-3793-a399-9f61a3301950 | -16.21952 | -50.82561 | 2025-09-12 04:27:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 262f904e-ba6c-3d93-8e2a-4f03f2b08eb3 | -14.32781 | -54.12519 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d1840572-9b6f-3f79-891f-64fbddfd208e | -12.92139 | -54.78679 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13dc31e8-0323-395d-8e74-4b92690f8280 | -19.93264 | -43.87514 | 2025-09-12 04:27:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 418430c4-3384-32eb-8676-777c536126a7 | -20.27434 | -42.11426 | 2025-09-12 04:27:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| ed06146c-1cba-3383-901a-7b8cf68983ee | -12.83647 | -52.97382 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf63b93c-8a45-3dcf-a520-347676b1a1d2 | -17.90734 | -47.02639 | 2025-09-12 04:27:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04a71b5d-f7d6-39bb-b345-a1ded6b3e0e2 | -17.14814 | -48.494 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89cf0a16-9669-3fd0-8c8f-baa7214e0a70 | -19.87783 | -41.41859 | 2025-09-12 04:27:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d80c6c5c-0513-3af7-9f56-a4140ab79dc5 | -12.82248 | -47.97627 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e318b62-80c0-359b-9e93-f4cd5bf8cff7 | -15.13003 | -52.44187 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a80c546-1bd1-3e73-9b14-cb7bbf0ffd9e | -19.23933 | -48.03833 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51b75fcc-9742-3de6-8f0e-09b91ec0c29e | -15.66472 | -47.03804 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55653072-a8fb-342e-9ff3-a68b3c5fc6d8 | -15.13122 | -52.45713 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce320ac2-d259-33ba-a170-e9a0741c10d0 | -13.00181 | -48.00151 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35baac51-d094-3667-abd8-85a0bfcfbd64 | -16.59425 | -49.81258 | 2025-09-12 04:27:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79f6e560-b5ac-3629-a926-e69c5865ac2d | -15.79295 | -52.22732 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d078e10b-29ec-3f9b-9135-ad7313b6346b | -12.46881 | -47.48439 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30f6c6e4-bb85-3887-a3aa-65c51df7fd58 | -15.24527 | -44.03828 | 2025-09-12 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6ea61c3-7a01-37e4-b7ab-dfbed1fb6da4 | -20.11688 | -42.3498 | 2025-09-12 04:27:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d87bf476-82ce-3fcd-9f0a-752982263e2c | -18.31266 | -50.42196 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4e9c717f-c151-3ebd-9b8d-0ef811c864c7 | -15.54157 | -49.74622 | 2025-09-12 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba312827-ff26-3af2-bb66-d8d12bc46312 | -13.3166 | -44.64994 | 2025-09-12 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef868b20-886f-32e9-9957-310560b0e90c | -15.12221 | -48.61522 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55ecd53a-6b7b-3593-a282-cb637385ca1a | -18.31125 | -52.07783 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7272426d-bc3b-3566-9d6d-c68978331a2a | -12.9865 | -54.76841 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bd19be0-862a-371f-8576-92e70c3d0482 | -15.15355 | -52.39717 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a555a9e-8f16-3168-aefc-4295af78a364 | -20.27723 | -42.88377 | 2025-09-12 04:27:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ff97bcab-0c6e-3db8-a0d5-735c68604a2f | -14.4497 | -47.3161 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 615cbd70-fbe0-3fe2-a3f6-ab45984f05d8 | -11.98642 | -51.13971 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef5989a0-e127-3bd6-88fd-3a2758b81dea | -12.15369 | -48.69089 | 2025-09-12 04:27:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3729492-3458-3c0b-ad8d-1e396b9b74da | -18.44672 | -47.18516 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcc21f88-f57f-39fc-ab7a-45bbc21c53f3 | -17.93941 | -46.9284 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90fb319d-f879-3265-95e0-ef8135fa4a5e | -12.96782 | -46.74181 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56bc3fc7-8f44-3c79-88c8-e2240269c931 | -12.82474 | -52.9677 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b82756b5-c10f-388a-80c1-7a76b441fa50 | -14.55973 | -54.51824 | 2025-09-12 04:27:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82a1ddca-72e4-3b00-99a1-bd236dcd26b9 | -19.85684 | -44.59472 | 2025-09-12 04:27:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 14817617-4dcd-352a-bd52-7670f43945f9 | -17.72005 | -46.13559 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8ab08a2-a479-37c1-a4b3-c4a0cb62cf1a | -15.15147 | -52.4753 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8af8c702-7b19-3f0b-a45b-55740b049826 | -17.35531 | -46.69149 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1afb1731-62c6-3bba-98c1-dda261adaa3d | -12.62414 | -56.96283 | 2025-09-12 04:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee25b5e-6735-38dc-b7e1-90ae2d2a131e | -13.25527 | -43.76775 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00f524d0-adcc-347e-90bd-d43994e621f2 | -12.92117 | -54.76225 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b39db369-a125-3c9f-88b5-6ec3d3576ce7 | -12.91576 | -54.76616 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b61393f-f84e-3ac5-a64a-eec752ec2936 | -15.09525 | -48.0108 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01be3991-1b16-3a8b-aab9-ff6f91a8d24c | -18.53766 | -48.41628 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| caf00bbc-8174-3251-9684-488d6e9e8fef | -11.9567 | -51.18002 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 911a6c99-70a7-317e-939c-3f043795fa7f | -11.97019 | -51.14595 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da76f751-32b7-3079-abe5-3cf9450943a6 | -12.54414 | -49.15503 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7c412c8-eea2-3999-90a6-23e75fd83551 | -13.31961 | -44.6547 | 2025-09-12 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b35153c-ce64-3c47-9a83-552ace0e1a4f | -12.90474 | -47.97171 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 063c267c-10bf-3ebf-9a09-3b787ae22049 | -14.43599 | -48.42357 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235a4247-8718-3881-969f-44873403f534 | -12.93068 | -47.97885 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f6798a12-89af-3b3a-be89-c6132b4e641c | -15.16028 | -52.31515 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcf3be98-f753-36f4-bd58-edea987d3825 | -14.18646 | -46.21038 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d353f19-3108-350d-9823-bee9520a9011 | -17.35018 | -46.70259 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad00ba2c-fbe5-3bc8-b59b-b32129d5c1ef | -14.43543 | -48.42712 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11d0e0fa-6f3b-3d38-8796-38f37fd3cee6 | -17.28009 | -46.08491 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 434c0170-88dd-3410-a37f-4c554ea89893 | -16.07101 | -49.96955 | 2025-09-12 04:27:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bea55be5-7a4b-306b-8be8-5deb349be64e | -18.62499 | -48.26522 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 26e5a27b-2b8c-3768-b974-97beedf3d122 | -13.20882 | -51.75654 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5096a069-4405-31a0-aa22-80ee9db71deb | -13.92007 | -47.9715 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e1071f7-efdd-3b1f-b236-2abcddb9a0bb | -13.89242 | -48.23235 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0221f241-ded9-390b-838b-f978f08c4ddc | -19.22685 | -47.22529 | 2025-09-12 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35eda267-b955-37a1-adb3-ad2f77652115 | -14.7444 | -46.29034 | 2025-09-12 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d5bb15-d06d-31ad-b3ef-4f3b353654c2 | -15.66416 | -47.04179 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f02c91a-7c72-32f2-9933-f021dfd39d5f | -13.9841 | -48.21044 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18c11852-d898-3c86-93bc-f79ce4f98556 | -12.15034 | -48.69034 | 2025-09-12 04:27:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17608da6-498f-3331-8085-1dfb8de79743 | -15.53694 | -48.54871 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5b0e7cc-f1e5-39da-9560-7f4fd08236a6 | -12.46716 | -47.49497 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df84f55e-24a6-33e3-a344-cb782c32e67b | -15.79589 | -52.23246 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1eb30d99-0b0b-3bca-864d-40bc65df29fb | -13.31396 | -44.09018 | 2025-09-12 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 51a75a52-3650-3e1f-b8e6-e0d511d1958a | -14.42257 | -46.40759 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be9a6b7-f093-3d7e-80c8-b9efbdd5e131 | -14.38419 | -47.34609 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2832a37e-9d88-3e3a-be6f-07983930ce97 | -16.43567 | -49.02782 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f318fa7f-771f-3b2d-a3ad-c67c28504c77 | -15.70377 | -53.64682 | 2025-09-12 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09fb10c7-5c06-33f8-9f3b-177a5bbb444a | -15.65805 | -47.04954 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc92f944-2370-38ab-88df-80d5d740b011 | -11.79442 | -50.56863 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65a914e6-4e06-3c78-bcc1-de934c4d1686 | -14.40129 | -52.93055 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 855b2d5e-3450-3480-9ea7-3ea6b5b77795 | -15.15015 | -52.46059 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 881681ac-53cf-3353-ae8c-ec3187429685 | -12.23753 | -47.33524 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cbcb096-4cf5-3109-97be-4321367430fe | -13.89624 | -48.25116 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39424c3e-b541-37da-a54f-71253b2b87e3 | -17.13764 | -48.49593 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cfd8d31-08ed-3032-b797-4651917508d4 | -14.43758 | -52.93214 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79c32587-45c2-3a45-9e6f-c11296b7b575 | -13.26616 | -43.74527 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98ceb0f4-6fcd-3c1c-b6a1-cda34d4f274c | -18.04953 | -45.44629 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7472b79-485f-3507-87b5-968b5d303b34 | -17.43231 | -49.23093 | 2025-09-12 04:27:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a65a5185-d95a-3882-90e3-e8eea4e66ca5 | -18.65701 | -47.65209 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1581481e-7802-32f2-959e-13748b609fc3 | -15.48372 | -47.34429 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86040dc4-58e2-3d36-b342-fbbccfb61911 | -14.43848 | -52.92707 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff121d67-f47e-3b9e-9a0f-6c7651c7dc9c | -14.49895 | -53.92529 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b438bafa-bb2b-3dd4-b426-ed72ee88e3fe | -12.86337 | -47.95409 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bd06da45-4fbc-3a00-9dc6-d14b0fcd7c2b | -12.96113 | -46.74075 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965d1c4c-ee72-3f52-87da-d3a52e00d921 | -19.7421 | -45.94438 | 2025-09-12 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 956f08d7-c5d1-3fde-a1f0-604c5171ba43 | -15.13167 | -48.59852 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README90.md)
