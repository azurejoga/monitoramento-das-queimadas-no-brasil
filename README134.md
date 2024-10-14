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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2710391-6ff0-33da-b460-afda619d8ecd | -11.2254 | -44.2186 | 2024-10-14 13:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9dde83ad-f41c-3fc5-8d8d-0540cf4aa54f | -11.2258 | -44.1952 | 2024-10-14 13:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 6857ed1e-52fb-3a68-9815-9577e616fc93 | -11.245 | -44.1924 | 2024-10-14 13:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d519aa95-d167-3384-bca2-a54dbb31c60e | -11.4794 | -43.9234 | 2024-10-14 13:46:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fe010768-10e9-316f-86a3-745cc8926b3a | -11.4597 | -43.9499 | 2024-10-14 13:46:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3a545399-2f05-3218-922b-beaa9fcfe0a9 | -12.1073 | -43.1861 | 2024-10-14 13:46:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| e974c2b4-3595-36d0-9b86-bcae3a3dc7be | -12.2727 | -44.5967 | 2024-10-14 13:46:15 | GOES-16 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0f474817-7abf-3631-8e38-9dd65bcdcecd | -12.5962 | -44.7783 | 2024-10-14 13:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 1dc5eb00-7128-31c5-b06e-48e8ebb1dd4c | -13.3889 | -44.694 | 2024-10-14 13:46:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9f1bd000-38f1-3d5e-ada6-e53e1aeda82a | -13.8739 | -44.6564 | 2024-10-14 13:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 26d412b5-a437-3af8-a71e-101510e44a36 | -13.8734 | -44.6799 | 2024-10-14 13:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 856416f5-cd83-3b7f-96fe-cbdf0d577fab | -21.5621 | -48.0058 | 2024-10-14 13:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 5fb18816-573a-37a4-91de-864aa0711d8f | -2.4344 | -46.9195 | 2024-10-14 13:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| b96d7d28-7ee8-3956-acc1-4bfd40ac7e1c | -2.4529 | -46.919 | 2024-10-14 13:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 028a5fc1-ad6a-3b8e-90fa-f436ecf3beef | -3.0572 | -44.4605 | 2024-10-14 13:55:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 80fbe382-4be4-36e6-a2c3-cd69953da979 | -3.4168 | -43.3635 | 2024-10-14 13:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5a9d7224-5c91-349c-a4fd-dc0e7f5e7518 | -3.4169 | -43.3403 | 2024-10-14 13:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 65942238-a9ef-3f00-9e89-496a797eadfb | -3.9219 | -43.1525 | 2024-10-14 13:55:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| aebf020f-dfb4-3ce0-b8ba-86f481dcf22b | -5.3354 | -37.8139 | 2024-10-14 13:55:36 | GOES-16 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 134.0 |
| a65bb346-5bb7-34c3-a586-99b6045e2752 | -9.3149 | -46.0908 | 2024-10-14 13:55:58 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| b7236572-3298-3031-b4f5-cf8c2a51a791 | -9.4365 | -45.5112 | 2024-10-14 13:55:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 27058809-1141-3f81-a797-37ab3141b81f | -9.4175 | -45.5134 | 2024-10-14 13:55:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 6c76d339-bb57-36db-a696-b00b72d6fd38 | -9.4368 | -45.4884 | 2024-10-14 13:55:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 01571017-4fb1-3c60-add1-bd40c2640a4f | -9.7576 | -46.893 | 2024-10-14 13:56:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| eb68afff-8037-3d2e-a638-f4cf2e28ce59 | -9.707 | -46.4513 | 2024-10-14 13:56:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4228935f-cdac-3e38-a635-3746f42283f6 | -10.0443 | -44.1717 | 2024-10-14 13:56:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 35979b47-fbc0-3212-9b10-ca26143df18e | -9.9793 | -47.2684 | 2024-10-14 13:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e4daa935-9554-3405-b925-0a5ca1e8db2c | -10.0439 | -44.195 | 2024-10-14 13:56:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| b7cae5cf-4712-3943-aeed-2b44744dccd4 | -10.082 | -44.19 | 2024-10-14 13:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 9f1627dd-dea6-381e-8c96-d4a7e57b2860 | -10.183 | -46.283 | 2024-10-14 13:56:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c36d3a05-129d-383b-b29e-bf4c0d34cf0f | -10.164 | -46.2853 | 2024-10-14 13:56:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f929c448-4177-38e9-a6fa-14f7be9dfbb5 | -10.1637 | -46.3079 | 2024-10-14 13:56:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 707f2854-3b1b-38a8-9cc0-a738c71d2033 | -10.0738 | -47.2798 | 2024-10-14 13:56:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8278f6d9-41e3-3c58-8504-dad52ea7d718 | -10.0633 | -44.1692 | 2024-10-14 13:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7c4c0b66-e7f7-3907-bcb1-d740cbd3d902 | -10.3493 | -46.5777 | 2024-10-14 13:56:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 193237ef-aff2-33dc-b4f3-c95ccee37c9f | -10.2635 | -47.2579 | 2024-10-14 13:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 341d3824-a4e5-31b2-86c8-203691bdc2ac | -10.2641 | -47.2134 | 2024-10-14 13:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8ed219bb-4f4b-3125-b418-ac7107804efd | -10.3303 | -46.58 | 2024-10-14 13:56:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 439430df-3c59-3d07-b73e-bb8fc8aeef58 | -10.8925 | -44.7074 | 2024-10-14 13:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 42dab45c-0da9-36ee-b9d7-997f10bcac45 | -10.9307 | -44.7021 | 2024-10-14 13:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 7e9c8989-a2e2-3369-aceb-66adae430dec | -10.9311 | -44.6789 | 2024-10-14 13:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d2c4f564-8b91-3904-ae3a-7c1f9d08df53 | -10.9116 | -44.7048 | 2024-10-14 13:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| ab6b4de2-8b1e-3904-8b41-a87beb6e559e | -10.912 | -44.6816 | 2024-10-14 13:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f5ed017a-e95f-3d4d-a580-6545d423ca4a | -11.245 | -44.1924 | 2024-10-14 13:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| b78cfe98-e6c4-3456-b7d0-21b8325d4226 | -11.2254 | -44.2186 | 2024-10-14 13:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 40b6ef2d-38bd-36d2-af16-e7da77191f00 | -11.2637 | -44.213 | 2024-10-14 13:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d1e39072-6219-37f9-987c-c6ef79f31c46 | -11.2258 | -44.1952 | 2024-10-14 13:56:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8b69b076-df75-3245-b05f-1d50bdb4060a | -12.088 | -43.1893 | 2024-10-14 13:56:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 3ff26dde-0134-3843-b759-b1f550e79bbd | -12.1073 | -43.1861 | 2024-10-14 13:56:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 9a05b0b7-b6ef-3b68-a378-862275c74041 | -12.2727 | -44.5967 | 2024-10-14 13:56:15 | GOES-16 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bb79b5f3-99ce-3688-aebf-8062cb1bb4a9 | -12.5962 | -44.7783 | 2024-10-14 13:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ba9c3175-6f4a-3804-a2a9-60c6dd050c78 | -13.3889 | -44.694 | 2024-10-14 13:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 834d86e5-a5f0-3480-9997-b99451162bfb | -13.8739 | -44.6564 | 2024-10-14 13:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e7316b8f-c994-3b03-abcb-9141ca543131 | -13.8734 | -44.6799 | 2024-10-14 13:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 15ce04c3-778d-3546-991d-16e0eee3b6b3 | -21.5621 | -48.0058 | 2024-10-14 13:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 19234258-0721-3e19-b90e-4b3d911e1039 | -18.24 | -56.51 | 2024-10-14 14:03:42 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d7d30a28-ac97-3a68-88c3-52f2a9bdf4d8 | -18.0 | -57.35 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eac96613-ac0a-32e8-9a8c-33c264d4b408 | -17.87 | -57.41 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1cb42e9a-98fe-332b-a241-15fe686df1f3 | -17.87 | -57.34 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b387ca6b-2067-3729-9269-f6bc4876bb9c | -17.91 | -57.43 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d606b8d2-342f-360d-bcdf-335173389007 | -17.9 | -57.36 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 557267a4-8a12-325c-bea9-ab99bb1a9ba9 | -17.93 | -57.38 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0c055b41-05d8-3b74-8aff-69796e72e0e3 | -17.93 | -57.3 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6abb3557-17ba-3e5a-b038-691819db76bc | -17.97 | -57.4 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| afe95dfd-6ff2-30fb-9244-3793f3b93d3d | -17.96 | -57.33 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b9c43c64-5aef-3ef5-9a01-e3c3cb817b4e | -17.96 | -57.25 | 2024-10-14 14:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dda09194-ae26-37f9-a4e5-73c239778870 | -15.32 | -48.81 | 2024-10-14 14:03:58 | MSG-03 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6bd5c47-fcfb-33eb-aa7b-326da553c8dd | -15.32 | -48.76 | 2024-10-14 14:03:58 | MSG-03 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2646c4c9-0da4-38d2-ab0e-4adfc63c4964 | -10.06 | -44.26 | 2024-10-14 14:04:27 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| efc774e1-6a14-34b8-b5cc-6f4b28bcdb1c | -10.01 | -47.37 | 2024-10-14 14:04:27 | MSG-03 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 869a00f0-c0d9-3689-9ca4-c964a59368f7 | -10.05 | -44.22 | 2024-10-14 14:04:27 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 712cbaec-babd-3b25-ab83-848bacea5ddc | -10.01 | -47.32 | 2024-10-14 14:04:27 | MSG-03 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29caf6ff-6601-349c-adad-4c84020e4442 | -9.72 | -46.51 | 2024-10-14 14:04:29 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46df9d1e-f166-3455-8b87-b7e81a338283 | -9.72 | -46.46 | 2024-10-14 14:04:29 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41d9f977-cd3b-378f-9c85-75f5c4a4bd74 | -7.44 | -43.02 | 2024-10-14 14:04:43 | MSG-03 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 28165a6e-0e23-3bc3-8bfd-0e0edecd9130 | -5.33 | -37.79 | 2024-10-14 14:04:56 | MSG-03 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| b2882f6e-8706-3968-a43b-53d8f61fd6b4 | -1.3927 | -49.2939 | 2024-10-14 14:05:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2bc0231b-6d1d-3b50-9ca9-011edda8f97c | -2.4344 | -46.9195 | 2024-10-14 14:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 1e7cf2e6-dc69-3e58-a2dc-428a2c04a381 | -2.4529 | -46.919 | 2024-10-14 14:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 57c2c2d4-00ae-341f-bf1c-62d8dd26db84 | -2.6118 | -49.0985 | 2024-10-14 14:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| b722ca25-2788-3be1-b1ff-15fdaa999142 | -2.6119 | -49.0772 | 2024-10-14 14:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 1f046057-6d4f-3f67-9203-36f83215ca13 | -2.6303 | -49.0767 | 2024-10-14 14:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b3a5b221-0179-3847-9d1b-889812c238cc | -2.6303 | -49.098 | 2024-10-14 14:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ba725055-1fc1-386b-9ce3-603cdf5b94c6 | -3.4168 | -43.3635 | 2024-10-14 14:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 8d1b16bb-7a04-3802-a55e-27857ff7c0f4 | -3.4169 | -43.3403 | 2024-10-14 14:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| aad033e9-f6aa-3ed7-91cb-df26217792c4 | -3.9219 | -43.1525 | 2024-10-14 14:05:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 51e0f87e-2cbc-3ac8-99ff-0bf0ba97cbd1 | -8.7814 | -46.4847 | 2024-10-14 14:05:56 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d82f6d3e-02e5-387f-acf1-2d1828a44cd2 | -9.4699 | -45.8249 | 2024-10-14 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7e5401c0-4764-3466-a010-160ee973aedb | -9.4888 | -45.8228 | 2024-10-14 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| cc31db38-a6cc-3e1c-aa9e-e0c9c872a7a1 | -9.4365 | -45.5112 | 2024-10-14 14:05:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 709cfa6d-05b6-30fe-adaa-545e051ccf34 | -9.4702 | -45.8023 | 2024-10-14 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 69bbf4f1-2e9d-3fbc-8cfe-445f0f9d98be | -9.4175 | -45.5134 | 2024-10-14 14:05:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 0e9d5538-c4a6-34ac-a4ee-4b55f3d4fb4c | -9.4554 | -45.509 | 2024-10-14 14:05:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2053d011-26d1-3a5d-ab43-953ec113fff5 | -9.4885 | -45.8454 | 2024-10-14 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 91e99277-5561-3792-ab4d-1c0d810a0f4f | -9.3149 | -46.0908 | 2024-10-14 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 7d3cd65c-134a-34ab-b982-e55a084caad1 | -9.437 | -44.1554 | 2024-10-14 14:05:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| d6d656a8-33b1-34cd-aab8-3ecee518aa03 | -9.753 | -45.8826 | 2024-10-14 14:06:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 81538e89-8a12-328a-b39d-c3ed7f0afc8e | -9.6818 | -46.9015 | 2024-10-14 14:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 03e90b56-cd6f-3e30-8177-9d2b5699fa2e | -9.707 | -46.4513 | 2024-10-14 14:06:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 49f5aa9a-3359-3c51-b07d-0b2662040ecc | -10.0443 | -44.1717 | 2024-10-14 14:06:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |


[Clique aqui para ver as próximas entradas](README135.md)
