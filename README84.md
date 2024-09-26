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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d58618f0-b4fe-350b-bb50-23ae20c40a0c | -20.82279 | -47.22187 | 2024-09-26 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93046dcc-11a1-3683-954f-f0cac3c0c21e | -20.82208 | -47.22599 | 2024-09-26 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce51de10-ac20-3b35-b3ca-80735cce3c56 | -20.81862 | -47.22523 | 2024-09-26 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a30277b7-0e77-3712-8670-82c19ec516b5 | -19.99153 | -47.15466 | 2024-09-26 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| eb833d45-cc1f-3bf5-8295-7963150bc352 | -19.99083 | -47.15871 | 2024-09-26 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 163e441e-2346-3515-8108-813f35f6c588 | -19.92892 | -46.94504 | 2024-09-26 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d31a805b-da9e-3f0b-8eaa-31a421386c61 | -19.92613 | -46.94041 | 2024-09-26 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf909d61-ce9d-35ea-88a4-335c03356d57 | -19.9178 | -46.94736 | 2024-09-26 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c3028c-b028-3f6e-97f1-57c932431183 | -19.87489 | -46.88458 | 2024-09-26 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fd27c7b-9dfc-3da4-b631-5905ffecb817 | -19.87144 | -46.88393 | 2024-09-26 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c277fea7-2b09-34ae-868a-098bfe260ba9 | -19.75719 | -48.00971 | 2024-09-26 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8dbfc580-e1c3-3f85-ac0c-442a2b1a0448 | -19.7569 | -48.01138 | 2024-09-26 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8385d75b-3e76-309d-866a-d63abce41576 | -19.75404 | -48.0062 | 2024-09-26 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3fd4bdc-a52e-3725-b00a-04ae5cb8bc03 | -19.75356 | -48.00901 | 2024-09-26 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4476365-da07-384d-81b4-e823da188971 | -19.75326 | -48.01067 | 2024-09-26 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88bd90e0-26d2-3681-9318-dbda89f63a01 | -20.70348 | -48.18622 | 2024-09-26 04:10:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 299bcbf5-a12a-3bad-a2c2-759a58d7ec96 | -22.3681 | -47.63614 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9da8b13b-244c-308f-ba85-1d4e2a45ef98 | -22.36738 | -47.64025 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a41ff7fb-7e5b-383a-9915-4c61f28c1602 | -22.36667 | -47.64438 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93ca5325-58fb-3f14-8c01-99b10a61b56b | -22.36464 | -47.63538 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3ee0f206-ca7e-31e7-8915-e3fba3010ef1 | -22.36392 | -47.63951 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ff3c3ca-9ec5-354d-a348-f448eeb70e63 | -22.3632 | -47.64365 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c90cf036-b5f5-3b40-83f9-5d63b4eea01b | -22.36045 | -47.63881 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8588d318-33ae-31c5-80c7-f7f9dac7696c | -22.35758 | -47.7797 | 2024-09-26 04:10:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48b8e2fb-785e-34cc-acda-6ba5012186a8 | -22.35488 | -47.77448 | 2024-09-26 04:10:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0659442-e867-3181-bf71-fd1d694c1cf5 | -22.35425 | -47.75733 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8f29966-cce8-3b9f-9bd1-d03190998aca | -22.35413 | -47.77882 | 2024-09-26 04:10:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2102420b-061d-3cb3-8e68-392efd5fdd39 | -22.35142 | -47.77364 | 2024-09-26 04:10:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7de20768-f197-3634-97c7-c6a74822d681 | -22.35076 | -47.75666 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d09ff8b-9458-3527-94d0-1b1f256010fc | -22.35067 | -47.77792 | 2024-09-26 04:10:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1c6944d-efb6-3520-bb58-e4c296003828 | -22.35008 | -47.7606 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 098ccfa7-3773-3d1f-b9ce-33acbe3af1e4 | -22.34938 | -47.76461 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0907d511-2a9b-393a-9306-2de14b762d14 | -22.34727 | -47.75601 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6410850d-c86c-3404-8e98-0c800896b703 | -22.34659 | -47.75991 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f473833-6d93-32ce-9659-19306a0d48f2 | -22.34589 | -47.76393 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 741fd7d9-422c-3d4c-b10f-144fa315883b | -22.34308 | -47.7593 | 2024-09-26 04:10:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05284c12-2bf9-394a-af5a-65a853c914bc | -22.34238 | -47.76335 | 2024-09-26 04:10:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca59bbce-0f65-30bf-a652-dff2ceba14e2 | -22.22863 | -47.57627 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ae60f3d1-190f-3161-a2bc-5eb17e800ee6 | -22.22517 | -47.57553 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a408b0a-0fcc-3663-8bd6-21eeb1216f39 | -22.22446 | -47.5797 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ae8a37c-d0d9-37eb-8c33-c6efabe59523 | -22.221 | -47.57895 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55bf83a4-7d3a-3951-bc04-0b4900a14636 | -22.21754 | -47.57818 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03dc46e0-7a7d-3132-9325-56bdfa4a8e98 | -22.21965 | -47.56584 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| f578f39f-b574-310d-ba8b-a145fce4d6c3 | -22.21619 | -47.56511 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 58f3af6b-9626-3faa-9921-4d98a595d167 | -22.21548 | -47.56923 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 653c138e-1e2c-3616-9d75-156eb38b10b4 | -22.21343 | -47.56024 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| 8505ad25-e97b-3463-a0d1-70eae3cf5b56 | -22.21273 | -47.56438 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 9417c98a-e856-3cbc-86ca-052e1be701c0 | -22.21202 | -47.56852 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 10f60c09-18a8-3fcd-9181-64003c316598 | -22.20926 | -47.56367 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 727eb59c-d9a1-3eb9-8d8d-5627978f1f2a | -22.20855 | -47.56782 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b1ef3e6c-d1f9-38a2-9230-edaf1efde193 | -22.20579 | -47.56298 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5b558818-b3f9-3a40-a402-50e5c4ba77d1 | -21.93801 | -48.5601 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 749f4b6a-f8d4-3cc1-bdac-95fafff78589 | -21.9352 | -48.55474 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e87320e0-cd0c-37b7-93cd-4bdb1bc3abab | -21.93439 | -48.5593 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 217cadcc-6003-3c2e-bffb-9c5215e18307 | -21.93157 | -48.554 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0b3c757-68a4-3f4b-b87f-08d8f67579f2 | -21.93077 | -48.55853 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f761cd4-cbb1-331d-94d1-73b8dcc780bc | -21.92714 | -48.55779 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36dd80c7-c123-3cc7-96c2-4d52116bfad1 | -21.92351 | -48.55706 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a27f1c7-98e5-33ac-a726-5cd985fca220 | -21.91988 | -48.55634 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fef383a7-7c98-35e8-b60b-ec3b992c7353 | -22.74025 | -47.47833 | 2024-09-26 04:10:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b80b655-d44c-3fe7-890e-6b141dd5d032 | -22.5634 | -47.55094 | 2024-09-26 04:10:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44b966e3-6ed2-30ad-88d0-146872446841 | -22.83859 | -48.41968 | 2024-09-26 04:10:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c301525-a618-3e34-8f29-d120c32b0fd7 | -22.49741 | -48.31023 | 2024-09-26 04:10:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7929248-00e3-3350-a485-ff7afc8a2c73 | -22.49385 | -48.30952 | 2024-09-26 04:10:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4903fc86-cae6-3bee-962b-f8a239a17ae6 | -25.19126 | -49.32649 | 2024-09-26 04:10:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2db02d2f-5ff7-3966-b8e0-fd16636e1d0c | -25.19015 | -49.32813 | 2024-09-26 04:10:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8184025b-61c9-3b08-9e41-baff71223b4b | -19.45202 | -49.14183 | 2024-09-26 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6419382-6536-3674-9515-9df8a955e717 | -19.45301 | -49.13834 | 2024-09-26 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d059071-63ed-3c77-82a5-d78038c04c99 | -19.45296 | -49.1366 | 2024-09-26 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13d8fdbe-d9fc-32fc-b3e1-5e15c168b094 | -19.95062 | -48.33686 | 2024-09-26 04:10:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a99176-2893-33bc-b9fb-80b25671808d | -20.02194 | -48.91298 | 2024-09-26 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bde5457-e7ea-373e-a496-91115534d7b5 | -19.45592 | -49.14436 | 2024-09-26 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79c544a4-0d52-3f69-bdfa-ce61b28db3a3 | -19.45204 | -49.14357 | 2024-09-26 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d7b07cb-cd4c-35a6-976c-9db8aa810e57 | -22.37982 | -49.03333 | 2024-09-26 04:10:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b3337b-a397-3c5c-8cff-7c4679ebd0a7 | -22.33763 | -48.97081 | 2024-09-26 04:10:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b231f49-7003-3a70-956e-2dfbb0ea7c34 | -21.95132 | -48.56945 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b75ac3e7-2801-324d-a920-83fbfc728ae7 | -21.95088 | -48.57244 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| db9d3962-1850-396e-a4dd-fd308a13be32 | -21.9505 | -48.57399 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d0a8f8df-cfcc-35d1-ab50-d541336585fb | -21.9477 | -48.56868 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 206259a5-0c40-3956-a7f7-1c60ac89eedf | -21.94725 | -48.57167 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6076b990-4cdf-3090-a662-23e9170f01fd | -21.94687 | -48.57323 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d94d167c-4959-3582-be20-94003e650f8a | -21.94645 | -48.57622 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5e1a1194-ba54-3ed4-9924-81877a42eef8 | -21.93921 | -48.57464 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d141df1-7059-30a5-9877-b3f6be5cd4bc | -21.9372 | -48.56468 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f7e31680-d3ee-3db2-a93d-5e895f443200 | -21.93639 | -48.56926 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 63eb53b8-98e6-32e0-9444-743cb2b61ce9 | -21.93358 | -48.56387 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d2e200d9-e449-35ba-b346-c3347bc408d1 | -21.93278 | -48.56843 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 17fb4c17-ee2b-3e56-9522-a70f4a22d2fa | -21.93197 | -48.57301 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f60bbad-d461-3f17-a154-e79731057b2f | -21.92996 | -48.56306 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c97df34b-c06e-366c-bae7-4b1e1e64288e | -21.92916 | -48.56762 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a2177332-e4ac-3093-a576-e4edf8377e06 | -21.92835 | -48.57219 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b59bd294-0ddd-313a-9594-b8a7405eaf29 | -21.92634 | -48.5623 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cbb6ec55-1c39-32c1-a11e-55bc63091e23 | -21.92553 | -48.56684 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5d3297cf-433a-310c-9cc2-e564d65998f3 | -21.92472 | -48.57141 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1945a43f-5898-38a1-82e1-bd7d95e43c41 | -21.92391 | -48.57602 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a91e4853-9dcd-3865-80fe-3ccbc0ce73b2 | -21.92271 | -48.56156 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dafeeded-1045-320c-9eac-1cdee682c9c4 | -21.92191 | -48.56609 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d62b1a3f-014f-32ad-a5cf-add983d7f326 | -21.9211 | -48.57064 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ac13183-e910-3a22-b41c-415bb0f8e045 | -21.91908 | -48.56083 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6e32a89-1113-3758-9a75-559501e32770 | -21.91828 | -48.56535 | 2024-09-26 04:10:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README85.md)
