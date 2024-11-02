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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79a22c0d-92a1-3b55-9ae4-d768a1c1ec79 | -3.9473 | -48.3666 | 2024-11-02 14:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| c7793a8e-d925-394d-a59d-ab4ddc14e1ae | -3.9474 | -48.3451 | 2024-11-02 14:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 6b175513-39e9-3306-a1fb-cd3169949d4b | -4.2628 | -55.5097 | 2024-11-02 14:15:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 35f15179-5477-3569-8163-62ef82127d07 | -4.8919 | -48.5803 | 2024-11-02 14:15:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ce0dd857-49d0-3478-8b0a-28715e400373 | -5.2299 | -48.0651 | 2024-11-02 14:15:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e836d349-3f88-3a93-bf91-43ec844abd03 | 2.2003 | -50.8773 | 2024-11-02 14:24:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d158eb2e-2dad-3958-acf6-5f0063752ac8 | 2.2003 | -50.8981 | 2024-11-02 14:24:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fe2ea2b5-ddc2-3136-b7a5-a4e35ca158b7 | 2.1819 | -50.8777 | 2024-11-02 14:24:54 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7b9b1a66-c999-33c4-8a83-35cd472a58de | -1.0059 | -48.8089 | 2024-11-02 14:25:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1e4d74de-c1ff-3d43-aeb9-891da073f284 | -1.2014 | -53.8983 | 2024-11-02 14:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 6d385866-0bca-3c43-8da7-1d2b76ea6954 | -1.2014 | -53.9184 | 2024-11-02 14:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 010b99b9-2f09-3c25-81dc-444d4554c062 | -1.2541 | -55.6904 | 2024-11-02 14:25:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 3e707691-03aa-3cd2-9024-163d308b5007 | -1.2724 | -55.6902 | 2024-11-02 14:25:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 764043c9-7c55-3763-adea-58a98bde0134 | -1.3846 | -54.1172 | 2024-11-02 14:25:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 11a8ce79-6fc6-310a-ba68-12da625b3847 | -1.4244 | -52.1913 | 2024-11-02 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 95d2f1eb-dd9d-3bde-8092-7cc667bc0d0c | -1.406 | -52.1916 | 2024-11-02 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 86fce64d-2524-3b8a-9711-858fa9bed665 | -1.4427 | -52.2116 | 2024-11-02 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 243d1a0e-0856-3897-b5ca-ac745737b6bb | -1.5532 | -52.1076 | 2024-11-02 14:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a24e9a3a-3831-3936-9dfb-b510d3ff4240 | -1.5127 | -54.2761 | 2024-11-02 14:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0ef81917-936f-3e3d-8132-554805d351e3 | -1.5351 | -51.9642 | 2024-11-02 14:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 04510322-8972-33a4-873c-3cc951fcdeef | -1.5127 | -54.2961 | 2024-11-02 14:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 09b9c940-f459-37c3-9b21-5639ca8add18 | -1.5716 | -52.1484 | 2024-11-02 14:25:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0a20e8e0-e07f-373b-9b4e-cc9401f56502 | -1.7837 | -47.8507 | 2024-11-02 14:25:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 830458c3-bbad-38d7-a87d-46ed0cc8aa12 | -2.1563 | -53.6838 | 2024-11-02 14:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7637e273-e31b-3077-9d06-9d261a2e3cc6 | -2.1695 | -48.7252 | 2024-11-02 14:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6816e4e4-3a76-3f7b-baa9-23a48b3bfc68 | -2.2703 | -46.1068 | 2024-11-02 14:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 07c1bf09-c19f-3b22-ac70-bf37c109a9d8 | -2.2384 | -50.438 | 2024-11-02 14:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 401ccda1-7b6a-3cc5-b7b1-580d5392d817 | -2.193 | -53.6831 | 2024-11-02 14:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b991f6ce-12e1-3c8d-9e3a-81a343fe5391 | -2.3052 | -46.7472 | 2024-11-02 14:25:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fbe2081e-d2d3-3e30-800a-c561db6b8ae1 | -2.2684 | -46.6821 | 2024-11-02 14:25:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d0840e53-df35-30b7-962d-c52d67aeb1cc | -2.3246 | -46.5041 | 2024-11-02 14:25:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 4d0f7a95-a14b-3e3c-85e0-b78eeaf95f48 | -2.3239 | -46.7247 | 2024-11-02 14:25:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 84f7a0ad-7d7c-32a6-a8cf-a1a10cac9d52 | -2.3245 | -46.5262 | 2024-11-02 14:25:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 923df866-d9d3-3e12-8a97-f190e1dae9c3 | -2.4251 | -49.6975 | 2024-11-02 14:25:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 757e959a-9504-3155-a84c-b8c0cc985937 | -2.4103 | -48.5694 | 2024-11-02 14:25:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9698d53a-cc0e-3e8e-9074-f39df2c5d0c2 | -2.6507 | -48.5414 | 2024-11-02 14:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a1372874-d064-3806-a0b3-6b13977d4bf7 | -2.6507 | -48.5629 | 2024-11-02 14:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| facbe7af-7756-3f7e-b32f-b502d100d2c0 | -2.6944 | -46.758 | 2024-11-02 14:25:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a2bea527-ebdf-3b89-b239-8c1d7a6814cb | -2.6574 | -46.7591 | 2024-11-02 14:25:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| cffc115b-0989-332f-ac42-b2ab212debbc | -2.6759 | -46.7585 | 2024-11-02 14:25:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f91be066-a634-3daa-ad95-61a7b9c2a5b6 | -2.6322 | -48.5634 | 2024-11-02 14:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 83baa89f-2a0c-39eb-9c18-ba287786a183 | -2.8259 | -57.1584 | 2024-11-02 14:25:22 | GOES-16 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 35a8a21d-b420-3934-a8e0-2ea9d480927b | -2.78 | -48.5806 | 2024-11-02 14:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 3ae0728e-09ea-31d9-a7b1-118d843f9629 | -2.8545 | -48.4495 | 2024-11-02 14:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 738e0bcc-ccd3-36c8-bd7e-08c89462d76f | -2.836 | -48.4501 | 2024-11-02 14:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| da866747-5db5-3050-ac44-78c648b4d26f | -2.8361 | -48.4286 | 2024-11-02 14:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d18fbf33-1213-3da1-b8ae-9625a71a9079 | -3.1282 | -54.2459 | 2024-11-02 14:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| a11817b2-9532-3146-b8f5-7d803b63581b | -3.1098 | -54.2665 | 2024-11-02 14:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 681e1da2-6669-38b3-aeab-52ecd552f1af | -3.6421 | -50.1667 | 2024-11-02 14:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 79d3432d-a5c8-3ed8-895f-f1e663c24a5e | -3.9473 | -48.3666 | 2024-11-02 14:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ef945c65-ddf5-34be-a0de-e7a7e8d78311 | -3.9474 | -48.3451 | 2024-11-02 14:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 508af592-8775-30cb-887f-86c7b9f1a5dd | -4.7293 | -42.6597 | 2024-11-02 14:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| a7f8c290-5a1d-3151-a648-ef30b6aa5cf1 | -5.1728 | -48.2416 | 2024-11-02 14:25:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c2ce17f3-46a9-39b5-a43e-0e391484154c | -5.2299 | -48.0651 | 2024-11-02 14:25:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| efb32cfa-27ad-34df-a0db-27bb7c9dd4fc | -0.1196 | -51.3359 | 2024-11-02 14:35:07 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 5aa84471-8120-3b62-9e26-7b81b1068542 | -0.6896 | -51.6847 | 2024-11-02 14:35:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.4 |
| bebac175-bf85-3814-85ee-81bca7656cf6 | -1.2014 | -53.8983 | 2024-11-02 14:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| cf65e025-9c0d-3ab2-89ff-ed19c37340db | -1.2014 | -53.9184 | 2024-11-02 14:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 52a00e12-f027-3822-a9e1-daab158c9054 | -1.2541 | -55.6904 | 2024-11-02 14:35:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| fc5ed756-5987-3d0d-a3cc-188a0550cb20 | -1.2013 | -54.0188 | 2024-11-02 14:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cc3c3d65-e3f4-37f0-849a-9d02054dd648 | -1.2724 | -55.6902 | 2024-11-02 14:35:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d5ae5a2b-795c-39e2-a82b-00cf3cb78de2 | -1.3846 | -54.1172 | 2024-11-02 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 7b073f1d-beef-3162-9c63-ba6b61a337fb | -1.4029 | -54.117 | 2024-11-02 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 489fc797-babc-36e3-b0d7-54ed4229b161 | -1.406 | -52.1916 | 2024-11-02 14:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| feaa3b2c-a170-39c3-b6e5-d1f677749527 | -1.406 | -52.2121 | 2024-11-02 14:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e0fa5120-480c-332f-8f4b-2799c19fdb60 | -1.3845 | -54.1373 | 2024-11-02 14:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f3663dd6-8c85-3172-b21a-0ef9dfb7d043 | -1.5311 | -54.2759 | 2024-11-02 14:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e4e916b5-ba86-3cc2-a93b-bf283c38c668 | -1.5532 | -52.1076 | 2024-11-02 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 34bdf3e6-2208-3341-a06e-ed863d3f6d3e | -1.5352 | -51.9436 | 2024-11-02 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8de18e0d-eef0-33dd-9351-f6da2a5e1316 | -1.5127 | -54.2761 | 2024-11-02 14:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6115cb13-e3b1-3651-941e-22864d8d1bfd | -1.5351 | -51.9642 | 2024-11-02 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 45fde4f6-9027-35cf-b842-7ab225344e87 | -1.5127 | -54.2961 | 2024-11-02 14:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1d30aa02-4f81-32f7-8e32-e555544bbf7e | -1.5351 | -51.9847 | 2024-11-02 14:35:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 90328404-cb81-3b73-a5d7-79fd734c4692 | -1.7837 | -47.8507 | 2024-11-02 14:35:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 90461501-a962-332f-9774-0c1e9704390f | -2.0818 | -47.1259 | 2024-11-02 14:35:18 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0dc1e007-15bf-3229-bd15-4c0bea6d7121 | -2.0565 | -49.5367 | 2024-11-02 14:35:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c0600059-df94-3e57-be45-80c2358fd0a4 | -2.0471 | -53.2411 | 2024-11-02 14:35:18 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 73491137-fbd6-348f-acbb-42b25c6cdfc6 | -2.3246 | -46.5041 | 2024-11-02 14:35:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8f233e89-2fb3-33c5-8a45-3f4529ca29af | -2.3431 | -46.5257 | 2024-11-02 14:35:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 317b287e-a286-3126-8c50-c93f510f0bf0 | -2.3239 | -46.7247 | 2024-11-02 14:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5daaf5e0-42f5-37e1-b293-e67e3c734e60 | -2.3245 | -46.5262 | 2024-11-02 14:35:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 6391a8e1-17e4-3ae6-a94b-edfbccf83947 | -2.4825 | -49.0807 | 2024-11-02 14:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 30975e21-3b1f-3952-a7b5-3d3d1254e9a4 | -2.3709 | -49.3387 | 2024-11-02 14:35:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8d06e138-0a1a-3418-89a6-515454e2ae99 | -2.38 | -46.5688 | 2024-11-02 14:35:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| f6b17ef5-a1e5-3c4f-a157-2d830e67ded8 | -2.4251 | -49.6975 | 2024-11-02 14:35:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ed8aac81-1be0-38ec-8949-b68620977c60 | -2.5171 | -49.8008 | 2024-11-02 14:35:20 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4549fc40-aa1a-37da-8d7e-1ca2855ed481 | -2.6574 | -46.7591 | 2024-11-02 14:35:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9ee9d758-cd3a-3700-b492-88747568e67a | -2.6069 | -45.4044 | 2024-11-02 14:35:21 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f7920190-0eb2-392b-b17e-b3ebcd4e99b7 | -2.836 | -48.4501 | 2024-11-02 14:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 62bb1c01-1bbc-3def-9a20-7c5129ca188d | -2.8361 | -48.4286 | 2024-11-02 14:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 799a2889-a7d2-3676-b1a4-5dfd44c1b46d | -3.1098 | -54.2464 | 2024-11-02 14:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| bdeef5a0-c35a-3939-b05c-936cbf9d5463 | -3.1098 | -54.2665 | 2024-11-02 14:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 87a6752f-b376-317c-8be9-3e7fc805b3b8 | -3.6421 | -50.1667 | 2024-11-02 14:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6548b6f2-27f7-3684-b555-67de9361e386 | -3.8467 | -49.9061 | 2024-11-02 14:35:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 24c45748-6c5f-356f-b8e5-d0ce70617990 | -3.8877 | -49.1194 | 2024-11-02 14:35:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e1b99d00-4898-3ec7-aa0a-2fdc61e4aa79 | -3.9474 | -48.3451 | 2024-11-02 14:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 779acd69-58fa-3eae-91f9-18cf5894cc72 | -4.3693 | -49.1201 | 2024-11-02 14:35:31 | GOES-16 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ee742aaa-a79c-3595-bc3d-850c29499b65 | -4.5953 | -48.5308 | 2024-11-02 14:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4f737331-a806-377e-a0d7-d02bb7fbaca0 | -4.8921 | -48.5588 | 2024-11-02 14:35:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 5fab55ef-f26e-3cbc-ba4b-ee5d7b8c4fb5 | 2.2003 | -50.8981 | 2024-11-02 14:44:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 61.6 |


[Clique aqui para ver as próximas entradas](README105.md)
