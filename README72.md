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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f50529fc-0a47-372c-9250-fde4e3adac04 | -8.78125 | -46.80741 | 2024-09-30 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8c0c78c0-7ee1-31ff-8fef-d3c2787f4bef | -8.63651 | -46.70534 | 2024-09-30 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f1d02c79-cc02-3697-bb71-f4c30b1c7aab | -8.40527 | -46.3429 | 2024-09-30 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 628c26ed-b5ce-365d-a664-df9244df2b25 | -6.97713 | -47.63962 | 2024-09-30 12:32:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9f30f7fe-55db-350e-ac81-dd772000e3d6 | -8.23895 | -49.39087 | 2024-09-30 12:32:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 204.7 |
| 8a8776ee-9ab4-3d38-aa67-f133ceb2c3cc | -16.60096 | -55.97226 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| d1702685-46ac-3529-b3e9-c2ee2ba2cf0c | -16.71119 | -55.53863 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 5412f083-4bdb-35e7-8e73-bcffc8605b26 | -16.71768 | -55.5341 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| d6427114-1173-3d77-9700-ca66343f216c | -16.71772 | -55.50527 | 2024-09-30 12:34:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 623f9c85-1171-3dcd-ad6b-c880688e18a4 | -16.72392 | -55.50095 | 2024-09-30 12:34:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| db656685-1f45-37f3-ab22-eaf6486f4500 | -16.73323 | -55.50917 | 2024-09-30 12:34:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 946dcb5b-9e5e-3e4c-ade1-d048fd960e20 | -16.75421 | -55.82772 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 171.5 |
| fd2da10e-a83e-3cf6-87a4-9fe8ff81cc53 | -13.1868 | -46.32352 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 369.3 |
| bfde9575-9c3b-38f0-8399-6a78e2c97114 | -13.7172 | -40.09989 | 2024-09-30 12:34:00 | TERRA_M-T | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9aedfa82-f067-3daa-a72a-145910159c12 | -13.27194 | -40.55964 | 2024-09-30 12:34:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 15c2e72e-7c86-319a-836a-73c3b7db4b40 | -13.44103 | -40.57935 | 2024-09-30 12:34:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 35cf55c9-c5df-3659-8739-1e4ad83f2ac6 | -13.43981 | -40.58724 | 2024-09-30 12:34:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 41924948-0fb7-3812-8034-42c9e7caeb55 | -14.43062 | -41.55017 | 2024-09-30 12:34:00 | TERRA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 18d9a8b9-154d-33fc-960f-87a2828cfaad | -14.40363 | -40.74651 | 2024-09-30 12:34:00 | TERRA_M-T | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| d143bbdd-c7fc-3020-b4ed-a2bb095d7cd9 | -14.40179 | -40.76115 | 2024-09-30 12:34:00 | TERRA_M-T | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 55.4 |
| f29dfbaa-d9f1-338f-9ed5-1492420ec0aa | -15.39113 | -42.17587 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c09e4132-eeb6-3774-b573-fba7477dbd4e | -17.56478 | -42.85623 | 2024-09-30 12:34:00 | TERRA_M-T | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4b3c69e6-b944-3185-95eb-b736d10c488e | -13.46584 | -42.93033 | 2024-09-30 12:34:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1ca3af1f-709b-39dc-b0c5-461ec0022e36 | -13.01046 | -42.21737 | 2024-09-30 12:34:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| a3e503b8-85ca-31d2-a030-f783554090c3 | -14.49745 | -43.52687 | 2024-09-30 12:34:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 89782880-aba1-3d64-b59d-a1afbe0efcd8 | -14.49606 | -43.53706 | 2024-09-30 12:34:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 14c92a15-a2ff-30c0-a7cc-bf4f49efd756 | -14.42718 | -43.43823 | 2024-09-30 12:34:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 083875b4-76b9-3e08-bd02-e40161fc4ed1 | -13.76616 | -42.89267 | 2024-09-30 12:34:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 57.3 |
| a3b4a376-289f-3d55-a84e-caf4ecd4db40 | -13.76472 | -42.90324 | 2024-09-30 12:34:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| ce67893a-65bf-33c9-bcc1-4cfa9dcaf263 | -19.15656 | -44.11451 | 2024-09-30 12:34:00 | TERRA_M-T | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d23bfe45-7d48-38d7-9ee7-a85d3625992b | -18.77995 | -44.40611 | 2024-09-30 12:34:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8fb7f02f-bbde-32a5-9669-8df4945f220b | -20.05067 | -44.36979 | 2024-09-30 12:34:00 | TERRA_M-T | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| a39ad826-4064-3a49-8dcb-19d34b6086b9 | -11.0255 | -43.15305 | 2024-09-30 12:34:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 04136a20-72c8-3036-8c4e-1b7967981671 | -11.02415 | -43.16276 | 2024-09-30 12:34:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 95c8c032-ffd9-323d-bf9a-0107db20b871 | -14.53289 | -44.99042 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7afa545e-f218-3523-b3ee-f1945a3a37d7 | -14.52528 | -44.97989 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| dfed55b7-c54d-3dd1-9e3c-59d07c466c6b | -14.52397 | -44.98912 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 393b09dd-c86f-3caa-9d88-3bc18e0ffb30 | -14.49636 | -45.24715 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 42c2b060-58ce-3e7c-9854-2dd13d007102 | -14.49505 | -45.25629 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a16f342c-5a8d-3f38-8834-a5185e3be954 | -14.49375 | -45.26542 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| edc013eb-69e9-306b-98db-170215ce0ddc | -14.49244 | -45.27455 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7b9b4e70-ec2c-361d-aa41-5725a4cc42c4 | -14.48877 | -45.23671 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a6d8a191-8612-376d-b237-8f7065d357ed | -14.48746 | -45.24585 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 121e4151-c025-3fbb-85c3-6ec354955578 | -19.44401 | -45.87145 | 2024-09-30 12:34:00 | TERRA_M-T | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f5fad695-9abf-334e-9a23-95634e6d7519 | -19.43672 | -45.85452 | 2024-09-30 12:34:00 | TERRA_M-T | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d779519-1c44-36e4-87a8-5a8e319afd03 | -19.09158 | -44.82203 | 2024-09-30 12:34:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 05b64a44-8feb-377f-ae4f-d316ce1e8fa1 | -19.09021 | -44.83218 | 2024-09-30 12:34:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 8bc5cb4e-f0b4-3b9d-b07a-05e261428967 | -18.9766 | -45.45996 | 2024-09-30 12:34:00 | TERRA_M-T | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5487a909-f60a-3a54-ae5a-09d821a5d829 | -18.96889 | -45.44897 | 2024-09-30 12:34:00 | TERRA_M-T | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c0fcc93e-6d10-374f-abad-e2f191715651 | -18.96756 | -45.45864 | 2024-09-30 12:34:00 | TERRA_M-T | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b7f79349-ff21-31aa-92bc-af0352db4fb3 | -19.71642 | -45.3609 | 2024-09-30 12:34:00 | TERRA_M-T | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6cf40b53-dfe8-3370-a5c7-0bd9bbf4ddbc | -10.70375 | -45.90603 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2024fff1-fa9b-3fe6-b216-97a47afea5a5 | -10.70237 | -45.91527 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 7ecd4781-1a07-315e-bdd8-6c576b733385 | -10.70099 | -45.92453 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0bd186b2-e621-341b-ae93-db0ae500a5f6 | -10.69748 | -45.88631 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 925f697e-1c5d-3eec-83d1-bfc99f188edb | -10.69198 | -45.92319 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| ab89bfe9-61db-3a79-927f-015fd344c856 | -10.87485 | -44.80208 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 8bce89fc-1894-3b7f-8aba-c13739de8c3f | -10.87355 | -44.81105 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 77573b9f-499c-3630-b571-de9065b37703 | -10.86727 | -44.79183 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 716d519d-37e5-3195-9a55-8db6c1f7c7cf | -10.86598 | -44.8008 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 1e71e8ed-f3dd-37b1-9b57-aebd6fb3f9da | -10.86468 | -44.80976 | 2024-09-30 12:34:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ff0bba8c-eb92-33f1-b9d4-178a57748bf9 | -10.85711 | -44.79952 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4e438bff-bc03-3e89-b8d4-7ef107df1e0e | -12.22534 | -45.53103 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b49da25a-4ef5-3103-87bd-4529c2ab9c2c | -12.22401 | -45.54008 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 878edf08-0887-3bdd-99fd-24afe9de0290 | -12.09915 | -44.99617 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| bfdd4e75-005d-39a8-950d-e5968e830f7a | -12.09785 | -45.00519 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d1698087-87b5-3f13-90ec-a438c4cc3c5a | -11.97345 | -45.16495 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| dbbdba5c-5091-3032-923b-241f9c238898 | -11.97215 | -45.17395 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c2438ee1-f58c-33cd-ad6a-ec6733f56d1e | -11.79518 | -45.44553 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7ef9f486-a32e-333e-9680-75e2d17d9737 | -11.79385 | -45.45458 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a06b52c9-c3a2-3857-8463-85b00389f8fa | -11.79253 | -45.46361 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 936946bc-2f7a-35fc-8db0-425121911b2d | -11.78495 | -45.45333 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 4b1fff9a-8607-3e93-af6a-761b06d30be7 | -11.78363 | -45.46235 | 2024-09-30 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a067ccac-383f-3765-b36b-d774f74551d0 | -11.25579 | -45.66221 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b16e2772-5a0c-3017-8cd0-640496fc8be7 | -11.24819 | -45.65183 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 5255d60a-7bfd-3116-b368-57330439f9da | -11.24685 | -45.661 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5eae8c6a-253b-326d-b0fb-71d34e734af5 | -11.22899 | -45.65833 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9955ab10-ef37-30e0-8929-2a64bb51b8fe | -11.22678 | -45.6114 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| f95500aa-0799-373d-80ee-6543de3da6ab | -11.21919 | -45.60098 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b3f52ea3-d9a8-3d05-8bad-386278e5b6f0 | -11.21025 | -45.59977 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 422a6698-e064-3238-83ec-29ea777412ea | -11.20891 | -45.60886 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0b4a2ea7-1016-3a7e-a67b-e8fa1913e8f6 | -11.16904 | -45.62468 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d0d3e64e-3c05-3a01-9e80-a46c8f0f164f | -11.16144 | -45.61425 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 60c4aaf8-bbbf-36d4-9bc9-6e26ec446380 | -11.16011 | -45.62335 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 1dfa1f71-8222-3fcf-8f3e-d4a154989dd9 | -11.15208 | -45.67803 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3d054f7d-9793-3cc3-8c4b-676d85a886d2 | -11.15074 | -45.68716 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 432c0ad4-53d4-3087-ba65-97db9bf05888 | -11.1418 | -45.68584 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c5f62926-d351-3193-8369-d9a0d14e6f2d | -11.14091 | -45.62983 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 54868e4f-c25d-3c1e-86c5-ad13dbe02d63 | -11.13823 | -45.64805 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9870f5e0-12f1-3fac-8bcd-86f71d222bf6 | -11.13689 | -45.65716 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 7d8b8144-2315-32e4-b38e-96672c66f863 | -11.13064 | -45.63763 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 1c51ca6e-854d-37cb-b293-4dc1c080d2cb | -11.1293 | -45.64673 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| fa5d060c-34ba-3274-8797-0bb153cd7afb | -11.12796 | -45.65584 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 132fd058-40c8-3c20-871f-b8908d3307cf | -11.1074 | -45.67145 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1db0d0cb-5291-34a5-bd3c-783ff66901cd | -11.09845 | -45.67016 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6831cbb4-1668-3b7b-95da-168d338ba3f7 | -11.0971 | -45.67931 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0045ad39-ed43-3d38-9ac0-052bf32fed14 | -10.88498 | -45.48977 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b5c96359-7b7e-37cb-b33c-e0c4a4c5d571 | -10.88365 | -45.49881 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| d1a1c730-e85b-32c8-8d35-f947889d63bf | -11.21333 | -45.70262 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| b61a2299-7950-30d3-a199-cc431bea5aa7 | -11.21199 | -45.71173 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |


[Clique aqui para ver as próximas entradas](README73.md)
