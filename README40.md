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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20e2da00-add2-359f-a748-04592d0b08c8 | -12.84321 | -47.01379 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23d1807b-c6ae-3f45-84ca-ba5b1c5fd777 | -6.4968 | -44.26381 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9d97748f-8b8b-32cd-8f0f-a7726c73ebb3 | -14.53815 | -48.24265 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88cf9dec-caf1-320b-b7dd-6fde952abf73 | -15.17273 | -46.41446 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40a43e74-11fb-3cd2-b0ed-6beb7b1e05bd | -15.2756 | -49.25235 | 2025-09-30 03:49:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f1eafcd-badb-3a94-807c-d9b721daf82a | -11.97159 | -46.58214 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2597ef38-e545-3cd1-b4be-461788c87fc9 | -15.82845 | -42.02026 | 2025-09-30 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f9330dce-74b5-3817-abbb-cb39e2ba3844 | -14.54274 | -48.47989 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ea5c631e-0ab8-3e19-9f5a-4f3752bf946e | -17.73334 | -46.67843 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 632cc9fc-68ec-3a47-8bf3-a1601fa5a306 | -5.70471 | -42.67451 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f2bd744e-0bfd-3bad-8602-67d73e8b55af | -14.70742 | -48.17251 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a7e317c-25b1-334e-bf7a-fa3f095cabdc | -5.86576 | -45.77431 | 2025-09-30 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce1ae25-9f39-349b-8dfd-0a911d4ab932 | -15.26533 | -47.8554 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2975c0e-14b0-3911-8f3c-3c55c549e9b0 | -13.62592 | -42.53651 | 2025-09-30 03:49:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2127e3dc-9082-3033-befc-0a6d12ca2a4a | -15.26899 | -47.89054 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6749e53-caa3-3659-9716-3e485c1d75fd | -11.05983 | -47.83647 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 993a4c02-2b26-39b4-94f4-f3ef44205bd3 | -13.79267 | -47.86613 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 515cb12d-071d-39a1-afca-ed16fe09659e | -12.23287 | -47.79744 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8328320e-9968-3821-9d62-553becbb4a16 | -15.46277 | -47.92388 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af1fa7ee-c2af-321e-932a-dfc7ed174f29 | -11.9665 | -46.58126 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba47e4d7-df43-3ee1-bfee-d013d13a8e8c | -12.94877 | -48.41388 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60700213-a940-386b-b195-570b5e9b6a96 | -12.93243 | -47.13925 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f58f07ef-92c2-36bf-bc10-5a5c90bf625b | -12.74752 | -46.85256 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3d0c728-0fee-3d2a-a78d-f5434ab33b29 | -15.49941 | -45.8688 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a87857c4-36fb-35b0-ab10-2b4b6f4101e0 | -15.2509 | -49.71878 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b65a82a-1518-3af4-9d02-c9cfbcb32540 | -15.26676 | -49.50005 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1d7f398-2018-365d-b431-06551e934fd6 | -12.83713 | -46.97962 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67faa87f-afd5-3b48-ba1d-3e75d416b8b3 | -6.5521 | -43.41697 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d9093f4-e8fd-3f8a-bf3a-828de3941156 | -15.39059 | -47.07648 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daadc168-0535-36e8-b8df-a3ba8d582384 | -13.62359 | -48.02959 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f45bea14-d1d7-3bbf-a00f-949f94db30e3 | -6.07954 | -42.43824 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a07daeb4-5925-3318-a5b5-9d7a5d49cfc5 | -12.83743 | -47.01612 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3465548-6c0c-3c7b-acb0-08e026066e24 | -6.36942 | -45.63809 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcfe3db2-bde0-39f4-903a-7e0a5ac0373b | -13.36597 | -47.30609 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02a40543-a8a8-321e-a692-547085d0b331 | -6.05363 | -43.60218 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24e4488b-577e-3793-af09-b04b8122f9d9 | -5.77797 | -42.85302 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f7ab71fc-409a-38bd-8740-c8a1c9fbdedd | -14.03981 | -42.15154 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3a546e72-3c69-3997-9a21-4dea2c92ad33 | -13.66133 | -44.31177 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb29465f-6f7e-3016-a08e-3f96f92e7424 | -11.94434 | -43.9201 | 2025-09-30 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38e2a50f-9d78-37fe-9b88-b72a319e2ca0 | -16.14929 | -48.42129 | 2025-09-30 03:49:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47676822-a047-31c6-b58f-48bc246b7c18 | -5.66823 | -45.29778 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 339aecbe-0b25-3f01-873a-0f4168aa494e | -6.50732 | -45.22188 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39b92a76-dfde-331d-949d-102a6a5d5149 | -11.19138 | -47.23423 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0a6ba5f-7f84-3b9e-be8b-02442731abe6 | -15.24423 | -49.72154 | 2025-09-30 03:49:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8575297-a214-336d-9c98-55425f46d883 | -15.46309 | -47.92522 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 143b0b9f-075f-3c1e-83e0-90e6205f9211 | -14.51417 | -48.45229 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0bfc2990-6c0f-3c8d-8051-4530db0543e9 | -15.2685 | -47.89101 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 511d2a4e-2e47-3930-8425-8876b714bb0a | -14.74763 | -45.66852 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3eedf742-080b-3c1c-9bb9-af747f75a9e6 | -11.88566 | -48.03602 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b386e8a6-6fa9-37df-aeaa-965264d65ef2 | -15.27478 | -49.25635 | 2025-09-30 03:49:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76951fb6-bcd7-348e-ac51-1ccfd6f22ad8 | -7.2953 | -42.86233 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac08106c-ac45-3aac-976c-a235eb8b3e3b | -18.47768 | -44.01801 | 2025-09-30 03:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44a6e04b-1fde-3228-9ecb-ed5a2a0f5be5 | -11.06069 | -47.82019 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4912025c-c528-3542-9e15-89857bde0ed4 | -12.83957 | -46.97797 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fed7958b-be65-36d2-9114-f8b2716384cf | -15.2035 | -50.1208 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5a1a59e-dcbc-333e-b064-a0fab4ed94e9 | -15.27416 | -47.89174 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ab19290f-8777-369d-9943-57c499837599 | -12.85016 | -47.00555 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01988ebb-3f34-3f23-9ee0-8c6e713f05c2 | -5.70097 | -42.64436 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1698e2ab-e95d-3f81-a0f7-293181e52f05 | -13.804 | -47.97798 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b2e0d8f-4f88-35e9-8f76-c9e1d878a9c6 | -14.72431 | -45.21736 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51a0d31d-d464-3359-87b6-0504d1888109 | -12.94523 | -46.75887 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3147604a-a097-312f-87fc-24e4311cf379 | -15.20106 | -49.55547 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 050e63b5-a321-32ed-8bb8-8806c99c0775 | -16.38717 | -47.03434 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed60aed-3d80-3eaf-9154-61c47c4a1a98 | -11.21455 | -47.20037 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 723f1a62-c165-3bef-a540-91ce7b2029d3 | -15.74802 | -43.84953 | 2025-09-30 03:49:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2fd6791-21cd-30b5-8c43-caeb03fce6e4 | -14.58156 | -48.28738 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d02f11b-07de-3dab-adf6-b84c6650a9e0 | -6.73035 | -39.1168 | 2025-09-30 03:49:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12eab174-7630-3144-9ba2-4b7ca417c534 | -14.51449 | -48.39125 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faadd342-9e5d-3050-bad8-af13b8f8519c | -13.82187 | -47.47205 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecee615a-9fc9-3c99-b6b0-83c7b742fed0 | -14.65707 | -46.96608 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c8edc57-d42a-39b4-91b5-1f4e456d1168 | -5.22142 | -45.23203 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6846976-ab23-3f31-b64d-fb5a35e65a53 | -12.85313 | -46.99029 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9df2d6a-ebb5-388e-a984-52abdc2ebfb2 | -13.7833 | -47.96959 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51ad12eb-97c5-375a-bf13-3882d7bca13e | -15.87815 | -46.21443 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a26bbf1c-9479-307d-b285-d53b33a12468 | -12.92555 | -43.20008 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 029c19f1-9b07-37a7-bfe7-4a120f08ba52 | -17.46076 | -46.2079 | 2025-09-30 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca4a0b04-fc31-33a3-8c85-c1a9cc0ac0d2 | -15.26461 | -47.8557 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a230fc5e-f22c-3f38-958a-9a8cf9868ae5 | -11.97219 | -46.57899 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e961dc9b-528b-3342-b7ca-ee4f2c384694 | -13.34012 | -47.82109 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fecbbd5b-90f2-3c96-8b5b-cf5290af815a | -16.40939 | -47.04057 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d7177d9-d893-3357-be38-58971d4c44f3 | -14.54055 | -48.2402 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ab3337a-d95a-3b7b-b0e3-4ab149e3cdb6 | -15.38177 | -47.06923 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 863be288-c45e-3972-a30c-89890d724e44 | -13.00845 | -49.44519 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 603e8cde-7240-3043-ad35-00e920e936b4 | -13.81691 | -47.49684 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9631011d-c5e7-377d-9e3e-11164b52c66f | -15.82112 | -48.16847 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6efaae6-eea3-3566-851e-53ba573910ad | -17.61595 | -40.6785 | 2025-09-30 03:49:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29c0ebdb-0a82-35c7-9840-d02111807112 | -14.50608 | -48.46273 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfc7dd20-48e7-3ed1-a66d-cce88dfab453 | -11.71957 | -44.4393 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a6fe4dd6-2594-3a4d-ac9a-b3c84435d1cf | -14.51189 | -48.4356 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce8d4904-d4e2-330f-8ebb-8f9aabd03ab6 | -11.16652 | -47.23585 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1768cdb1-edf0-3fa1-b465-b4824e5568f7 | -7.05155 | -45.19782 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fcc9baca-d83c-367d-ac38-315f69567b82 | -12.96478 | -48.42141 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 87ddd9a5-d58a-3c7d-944a-3b4d09dcf499 | -13.79152 | -48.01299 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbbc5b66-a67c-3e37-9f3a-beb84fd131e6 | -6.08736 | -42.44361 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a7d2843-07c7-34c5-bf2c-63d3d361e9f8 | -16.42604 | -47.01459 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d5e60d4-4774-3418-83ed-5e254cffebdb | -12.8435 | -46.97398 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d565ecb3-aed8-3dba-8b96-26c76b02fed8 | -11.20143 | -47.21085 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 982123a8-3b2f-3527-92d6-627ebc882335 | -6.7942 | -44.08168 | 2025-09-30 03:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6891dd1-1a76-3396-8dee-8e175cfa75e9 | -5.73947 | -42.68021 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d56d3771-a140-3d3f-964e-1a935b72a38b | -13.80865 | -47.4819 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README41.md)
