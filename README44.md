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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 952e4e7d-56d0-3902-ba16-bf13e911840d | -14.13288 | -44.00083 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4bc02d4-0289-3de8-aa4f-4f3b0b4f303d | -14.09993 | -44.59804 | 2024-10-11 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c2f926d-72cd-3224-946e-bd653f140daa | -14.08831 | -44.13683 | 2024-10-11 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5d9bb00-9edd-3d01-8252-0745ed7c084c | -14.07269 | -43.69207 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf07cf44-0b4b-3486-ba40-376560834306 | -14.07205 | -43.69595 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1088088-c7d8-3225-be29-c226c937487f | -14.04108 | -44.16227 | 2024-10-11 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbfcae7e-9097-32ec-ad46-b8789aff193a | -14.04041 | -44.1663 | 2024-10-11 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b98f1307-ec17-39fd-b60b-70f118ca05f7 | -14.04004 | -44.03827 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15937083-0585-3f62-af8f-8fe9ca59b4fb | -14.027 | -43.90126 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 339a80a4-d9de-3997-9928-536aae1cde87 | -13.97755 | -43.86919 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2101a93-3a30-399f-9652-eac625e8b686 | -13.92408 | -43.8032 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ee99cad-f78b-3299-bf9f-1469c46c2507 | -13.92211 | -43.81496 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3ce3053-98fc-3cb2-ab32-4d9269606729 | -13.91863 | -43.81435 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41f4f158-d073-3728-b3a2-83376beac71b | -13.84283 | -44.1983 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ade1d6f-12fd-3a0c-b2b8-c6ba038f4031 | -13.80855 | -44.63684 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c75dbe10-41c2-361f-bbd0-9bef6bbde08c | -13.80783 | -44.64104 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c19d5755-4df8-3510-aa51-f6fdf9debe0b | -13.80494 | -44.6362 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b1d9953-a6d4-380e-ab2a-3bef512a2583 | -13.79773 | -44.6349 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92d9486d-a3cc-3ec5-b91a-999eb503dee5 | -13.79412 | -44.63426 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0866250-09a0-37f3-9a5b-1a859d77e13e | -13.74836 | -44.46309 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c87d118f-6c78-3f8c-a92b-a5e225bdaf08 | -13.74478 | -44.46246 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f371f56b-9322-39eb-9b73-27f7803da00d | -13.74408 | -44.4666 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 07b2581b-92a4-36cf-9d7e-d4c70b9c71ba | -13.7405 | -44.46599 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04e0126a-3ba7-30ad-bfee-c4412177074a | -10.87119 | -44.6139 | 2024-10-11 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8279d13-5f08-31b0-9233-107e3dfed75a | -10.82625 | -44.94503 | 2024-10-11 04:02:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 994cf54e-f63d-3687-9e04-c9b00cd05f4d | -10.82243 | -44.94437 | 2024-10-11 04:02:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 635e9357-1ff0-32d8-8730-8b7da9271893 | -10.58399 | -45.14123 | 2024-10-11 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d6c4273-5745-3933-bbcc-9ef73c89a939 | -12.31949 | -45.31068 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ef1eb4c-1614-3545-8452-f815bb41a88b | -12.31867 | -45.31546 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da10006-efeb-3c3c-b41d-ebd64995abee | -12.31567 | -45.31002 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21226515-465a-388e-b335-4cff08f5ef65 | -12.31485 | -45.31481 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 682f2308-afea-3b4f-9ab3-06d5bf48e1a3 | -12.31267 | -45.30457 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f88aee06-5f7b-3967-ac77-72d8a326b929 | -12.31185 | -45.30937 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 751ae642-2fb1-3b8c-ba5f-7667958ca65b | -12.31103 | -45.31416 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf1e148c-00da-3a05-9f41-784e3d9ded2a | -12.30886 | -45.30392 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c36d7258-dc06-37ef-be41-432a78524a27 | -12.30804 | -45.30872 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1827e88-ce91-3d83-9f95-a2310309090a | -12.30422 | -45.30807 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54baff11-5780-3e3b-bd63-24168bf7a3a6 | -12.29544 | -45.33628 | 2024-10-11 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b07d917-83a1-3d21-a3f8-94c46483148a | -11.79259 | -45.20073 | 2024-10-11 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a36efd02-23cc-3c55-bfca-39bd8f32bd45 | -11.7896 | -45.19524 | 2024-10-11 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 828dd3f3-368a-3f10-9a12-f4f2d4b96690 | -11.14008 | -45.38212 | 2024-10-11 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d4d3451-d535-3bf2-8d5a-047b69a4f996 | -11.13985 | -45.38412 | 2024-10-11 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf3d1387-a14a-3ecc-9cab-ba3ea239ac8b | -11.06301 | -45.36335 | 2024-10-11 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4000aaf3-6ea3-345f-aad0-c4068c53282d | -12.69043 | -45.87906 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eabb9aa5-f64f-3704-b149-087a2a6c8de2 | -14.84156 | -46.65279 | 2024-10-11 04:02:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a16c7eed-f486-342f-b0a6-8bb4146566cf | -13.97157 | -45.80573 | 2024-10-11 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27c33833-bd9c-3d2b-948d-9b50bb966c57 | -16.60953 | -47.29977 | 2024-10-11 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 155a94b4-2d6f-37a4-bf98-7b68892b60fa | -16.60619 | -47.2953 | 2024-10-11 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e75324fd-411f-3fa9-8726-9817b8a440bc | -16.60553 | -47.29891 | 2024-10-11 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 314227ec-4cc1-3791-89b7-dd02c45c7e06 | -16.60487 | -47.30252 | 2024-10-11 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dcb63952-7620-34da-abb2-652e09403988 | -16.60152 | -47.29809 | 2024-10-11 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6e312e7-f511-3090-889f-465a6961b997 | -12.17512 | -46.74485 | 2024-10-11 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70d22bcb-eb67-355a-ae27-187011ea3750 | -12.17095 | -46.74406 | 2024-10-11 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dab49762-6075-3049-b521-b63a1b2797b4 | -12.16677 | -46.74332 | 2024-10-11 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af98672d-1bc5-3b3c-b4db-f89794b0c745 | -12.16608 | -46.74724 | 2024-10-11 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c59a3a8-9e19-369f-9799-1b740e3734fb | -12.45487 | -47.30829 | 2024-10-11 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27b80676-6830-3fc6-9a0c-f77e779ea0d3 | -12.30077 | -47.20903 | 2024-10-11 04:02:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 172efbd0-94d8-3f34-8c99-8d51083f0fd9 | -12.30004 | -47.21313 | 2024-10-11 04:02:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8de2711f-0729-3a18-ba7d-8b0c25bbc7ed | -12.29648 | -47.20824 | 2024-10-11 04:02:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f81d844-7abe-3d32-9e3f-2d524740a000 | -14.87379 | -46.97917 | 2024-10-11 04:02:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b3c738d-8e50-3f3e-a2e6-d239b5dc70bd | -14.87312 | -46.98283 | 2024-10-11 04:02:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 432e51c4-cf70-3234-aec4-a1dd0f8ec33a | -10.82134 | -48.91002 | 2024-10-11 04:02:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aee6dee-a74f-3b6e-b723-19f8d509c6e2 | -10.63016 | -47.84816 | 2024-10-11 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 468afca8-fa26-3df2-8fb7-27245412fdc3 | -10.62932 | -47.85275 | 2024-10-11 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef24348b-c678-3922-8443-59753c11d792 | -10.62552 | -47.84745 | 2024-10-11 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ff5ef74-a909-3a32-a2c3-db55849e847f | -9.8195 | -48.04189 | 2024-10-11 04:02:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66c64aea-9974-3dae-99f5-1f6df95db64a | -11.68264 | -48.48785 | 2024-10-11 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e35113e8-ac44-34ab-8e49-4fdf3f0ef7d6 | -11.68168 | -48.49299 | 2024-10-11 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b7db198-5349-353c-9d8d-1545523fc9f8 | -11.67791 | -48.48696 | 2024-10-11 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e55aec48-e25a-3ff1-883a-acac1d819f6f | -10.47228 | -49.985 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5bd0053-e9eb-33c6-94c3-4428554d92d1 | -10.55529 | -49.94237 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cb162cd-caf4-376f-b368-66e0fb0b3878 | -10.54468 | -49.9403 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90eb5a7e-649c-35e3-ae43-2a99ed407d2a | -10.54136 | -49.93937 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d767f673-8165-36db-879a-6a13577bc6f7 | -10.54075 | -49.9427 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88e7d78e-3b7c-3a95-aa1c-1a94eebb33bc | -10.53938 | -49.93926 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40682054-8954-3d94-9849-355a21617713 | -10.53874 | -49.94259 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa62cec7-b62a-3c94-b3b7-6cc7891914bf | -10.46695 | -49.98396 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a558b0a5-820b-353c-9031-59c90b32df72 | -10.46226 | -49.97955 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a9a28e1-797b-38b1-a7bd-58070d10c648 | -10.45693 | -49.9785 | 2024-10-11 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7480276-c184-3c79-a60b-9ac1a100ac93 | -9.67434 | -48.91615 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff806b88-34ee-3cab-a45c-12a9fda32de6 | -9.67377 | -48.91926 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c01b455f-b53e-31fe-85c9-83a04e1f1b5f | -9.62659 | -48.98712 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 550a9507-dc36-3283-9c9d-b72da13ba576 | -9.62605 | -48.99014 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 143c7047-918b-3579-8caa-64fafe849abf | -9.62551 | -48.99316 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6efa1ccd-ab10-33bc-befc-9f3dd28237c7 | -9.62503 | -48.98474 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ae1050b-86a9-3a60-ba10-1d2d981e2195 | -9.62446 | -48.98779 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab714a78-614f-356f-9a1e-983e948526eb | -9.6239 | -48.99081 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03482e6a-51d1-35ce-acd4-27d77aee1c03 | -9.62333 | -48.99385 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e364234e-9935-3674-b2e1-49179834c9f9 | -9.62152 | -48.98616 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22519a7f-408b-3e6d-a4d8-23762dd0aaf6 | -9.62097 | -48.98922 | 2024-10-11 04:02:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84648e90-d44a-356a-a8e3-8fe00bdf472f | -12.12903 | -50.54482 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08c1e3e9-641f-3e7f-b89d-6eda3895ac17 | -12.12367 | -50.54371 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ec5375ac-e078-3e51-842c-e8b1079bb8fa | -12.12301 | -50.54717 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2821c3cf-efed-39e3-935e-0ff4350ffe52 | -11.53136 | -49.82841 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e56e48a-a4c3-324f-87e2-05f25b75ddb9 | -11.53112 | -49.82859 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e4116eb-3d2d-3935-8b93-2823abe10a3d | -11.52619 | -49.82738 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cca82323-5333-3382-bcf2-9cd882db0c26 | -11.52594 | -49.82755 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4acfbd8-6341-31b3-a895-b2915fbd861f | -11.52558 | -49.83054 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a575d9d-72b6-3cee-9dc8-01981597cf0a | -11.52536 | -49.83072 | 2024-10-11 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66e55061-7843-3b7a-8d0c-319fa013502d | -9.19635 | -51.52386 | 2024-10-11 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README45.md)
