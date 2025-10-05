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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4824b3f5-3e56-3e6b-92f1-b63b997693a3 | -11.82952 | -45.07756 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 387852c5-1ab0-3f04-a7bf-87f076d17b1b | -11.0031 | -45.59273 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 104824af-e84e-3087-ae08-a6faf73f2f02 | -10.7391 | -47.90107 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e62264f-eb3e-312e-bbb2-541549dd059a | -11.49123 | -46.79103 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15748d26-f54f-3198-bdcd-fa2ed12cc51c | -13.32399 | -47.79034 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6111663b-10d1-39dd-b4fc-5b621db9428a | -16.35623 | -47.05921 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b33a06c-f106-3f23-905f-a00ec922cf7b | -14.32868 | -47.67082 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb7f8f32-14c4-348b-8edd-170816891df9 | -10.6227 | -48.66749 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18aa7e00-71ae-3e66-9fb5-4adb12941c29 | -13.26627 | -47.62554 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ea05ed5-6fb3-3e28-99f1-f4f0b9d6e4af | -15.11929 | -45.74919 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b08d47e9-7035-3611-9acc-25143de3d7f6 | -15.38687 | -47.95607 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6bea29c-3037-3bd7-b242-4e91a1fcc5c2 | -11.53227 | -47.67762 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fd5fb2e-aea6-30da-a589-f7a89c0450c8 | -13.28641 | -47.1796 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| debcd312-19c4-3eb5-992a-86a144237e59 | -14.65908 | -48.35036 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a182d610-1b3e-3fea-b5ee-904ae6182e00 | -10.57435 | -48.71547 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad201118-c9a9-3d91-a3ae-343db13cc8e8 | -13.95601 | -43.07121 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5f5c8829-dd13-33ed-9a38-486691effad2 | -13.31998 | -47.62729 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2be2b52c-fabe-3ea9-bc4c-101702a0d4f6 | -13.12448 | -47.80445 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 991a1f24-663d-3369-b5f9-606d41248198 | -14.87184 | -48.13713 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5696c7e4-be7f-3cc1-9176-8b2c8a955810 | -14.66703 | -48.36201 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a536676-0b73-3f61-8134-a960e4fc9192 | -12.81438 | -50.53541 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 027eb21c-8feb-3841-995a-c3f984961e6f | -15.59911 | -52.50682 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c59d0a7a-7779-359f-90e7-84717c45ebb1 | -12.10461 | -50.89418 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3e1c8e-556c-3047-b7a1-2255472acf22 | -13.72744 | -48.08661 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8e3871e4-fb85-3cd0-bd7d-2536eaf61c23 | -14.66157 | -48.28402 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75790640-22b2-3f59-9948-c1cdc0905c6c | -14.68364 | -48.30116 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2add8fa0-1fb0-32ab-b585-9088b55d4005 | -11.8349 | -44.92863 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb609f87-b34d-3474-9abe-7a09f2b5d81f | -10.74243 | -47.89628 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56460fb1-8d08-34d8-aaf3-49fc85188315 | -15.36126 | -47.98135 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df8b094e-344b-3332-90e7-9944a12c4e89 | -12.80935 | -50.53622 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a711c52-7058-376a-9d22-98b3046b3fba | -18.13754 | -47.96621 | 2025-10-05 03:55:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed0698d-4ffd-37fd-aa2c-70a5dbbd4bf4 | -11.07116 | -47.90563 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6062519-0340-3594-8540-d43b71f73749 | -11.0802 | -47.91347 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5104451-1e5d-3065-8533-4660574a8dfb | -11.81669 | -44.896 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd549b9a-73df-32d4-a671-a0490c617ae9 | -14.67684 | -48.37307 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9f01f6ab-2b67-3aa4-8a1a-86e27e302189 | -13.57308 | -48.16635 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91aa0630-a012-3208-bfb9-535aa842a888 | -13.72152 | -51.46491 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 342d939c-c242-3769-8c94-c9fc76df946e | -14.69034 | -45.17735 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ffb5698-cdfa-3c8e-b19b-36ecbec20051 | -15.75683 | -46.26482 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 858d461d-c926-305a-88df-4aa2f6f3d0c7 | -13.5792 | -48.16111 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c93ec465-27ad-3969-a92b-80d4eb2367a1 | -13.32014 | -47.78421 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c446fb17-fb86-308e-aa18-7181cd11538f | -11.06022 | -47.77668 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d927717-813e-3e7a-955e-5394b5956ded | -11.78045 | -47.92565 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 056dbd53-77e5-3467-9cca-fc368f7f9e4d | -16.60468 | -49.38013 | 2025-10-05 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a73e15a-cde0-3dc0-9dae-6a52c1292bdc | -11.84999 | -44.93922 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 916af45b-7a4d-3a4f-a70a-df5a1ebde77b | -14.88613 | -48.26106 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbe38f6e-d166-341f-a7a1-1d1d3dcdf575 | -11.14706 | -47.92161 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f26f778b-643c-3b5d-9605-ad368f58bfd2 | -13.26846 | -47.61379 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b518baee-a18f-3215-b868-b29ced3620de | -10.73106 | -47.90042 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a100d78f-dfc0-3874-b150-64d782ac8c64 | -13.12344 | -43.848 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2eab21a7-c6c1-310b-97f2-4a582f383b30 | -10.94765 | -47.04557 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54ba1c11-de9d-35f1-b33d-8479e5ce85fd | -13.82693 | -48.05324 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f569bc8-b5d0-3f92-8856-1c82d01b46c4 | -11.80241 | -46.85442 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7de8c3d-777a-36dc-9778-0e445d8bd34d | -12.1157 | -50.90136 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3bf932d-042f-3c5e-a44b-255f15a54133 | -14.88514 | -48.266 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 230e787c-c2a9-36f7-88ba-97a9fc46b962 | -11.70002 | -47.50292 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df5e79b5-85fe-3777-aedf-1a24ff0fb888 | -10.94363 | -47.09454 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b080a27-254c-38a6-8ee5-4739db021414 | -13.92505 | -48.1622 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fc188de-c2cf-3c15-828d-5932fea99e10 | -14.32701 | -47.70567 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9766c74f-038c-3a3a-9ec2-a84795445168 | -12.39707 | -51.10986 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c98edb98-6ea7-3f7b-8261-a27e1d57ec48 | -11.83294 | -45.08242 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 572c22b6-c63a-355c-be14-b1d17aab254f | -11.09591 | -47.88601 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6918b3a0-261a-318a-a7c6-45b084435426 | -11.83213 | -45.06297 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afd86cd7-5980-3ce1-8e68-b9765998183a | -11.10065 | -49.85796 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e3fd9ba-d748-3d1a-8f75-8f93bf9e6859 | -15.53664 | -46.81101 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e7d4888-cac7-3ad7-834e-5559273b8949 | -15.13638 | -45.74858 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b54d99f-74da-3cd0-a51d-338e8364ebfa | -12.30873 | -45.36396 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee54c45a-0711-3062-9b3f-0290645db21f | -13.91907 | -48.16692 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa155c3-f306-3207-8e7d-54781b27f23c | -14.98821 | -49.98256 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c967bc48-a0d0-3d9d-a0dc-7109c2e08085 | -10.35433 | -48.17154 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c04ac5fb-e0b2-3bdd-9a26-a0bb6a8ef1e8 | -14.93021 | -46.92102 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eb1a7393-8ffe-392e-aad1-51eb10dec892 | -12.40507 | -51.10173 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 234594d6-7cef-346c-88be-b16052bacf47 | -15.12886 | -45.7432 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4db48c88-5812-3e91-bdc5-bc38eb4cb8cc | -15.56974 | -52.47361 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a1fdd58-10b6-32cc-becf-7b37e7ba2e8c | -11.83212 | -44.92055 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c36fe70a-4486-3e1d-9387-7999bd20a6f1 | -15.5612 | -46.97076 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a1022be-0c6c-3ba1-97f3-44014d6f1005 | -13.27658 | -47.59491 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a72dac9d-63ce-379b-8a46-c7ee60297ec4 | -14.66916 | -48.3508 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 896b13cc-4139-3614-9690-58aabfb1d1c3 | -14.79601 | -44.89779 | 2025-10-05 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b9aff6f-a022-3332-9492-72735979881f | -11.79805 | -46.84035 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ea3443e-9c7c-3335-93fd-fe7255b235fd | -15.74181 | -46.27549 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5da3858-2109-3cdd-a29b-d52510315027 | -12.61134 | -48.11797 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f32895-5a5c-3f7a-9946-651c6d7e8b90 | -14.74483 | -54.66543 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b56f11d-f4cd-32a2-b335-e1929898d9d5 | -16.53668 | -47.7695 | 2025-10-05 03:55:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2e4b957-b85b-30d7-a291-44b0e2eae4e3 | -15.23431 | -49.30582 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1837cc82-9ddc-32e9-baf5-7ed2dba028ea | -17.97217 | -45.0036 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16d2de04-9ab0-30ae-809a-a7f014b20135 | -17.20287 | -44.44682 | 2025-10-05 03:55:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a6d29e9-0c64-30a5-8fc6-500b9c4d23b4 | -14.97062 | -49.97852 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f049c4e7-3059-37ce-9dce-bc4624ac5f42 | -15.44129 | -44.29107 | 2025-10-05 03:55:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 423c07d3-52e3-3f5d-a403-08aa979fffca | -11.49812 | -44.98631 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5f4f474-6cec-3554-8405-1cf0df965a71 | -11.52364 | -47.67222 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 84158817-98a4-3547-b208-cbbfc06f6f6d | -11.02852 | -45.57613 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8834aa6-31e3-384b-b381-bee154bf6e55 | -13.27237 | -47.61658 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cd685be-6c72-36e1-92e2-df97455a57a7 | -11.91794 | -46.26054 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9630ec72-d100-3dad-b442-a4a19edcc2e4 | -14.67303 | -48.35718 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a5db3ca-b1bf-3c29-a3ca-62d824733e70 | -13.15948 | -50.88484 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f12e12ba-0ab9-388d-8f4c-cad22f882226 | -11.69443 | -47.49484 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a5bc155-a7aa-3956-b41e-ea197cf01f2c | -14.00579 | -48.20069 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 970dcefd-d03f-3235-b01c-bbffd09bd583 | -13.2614 | -47.62507 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 911ff909-ed46-3841-a563-e81ee54ce47a | -11.93299 | -46.4322 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README65.md)
