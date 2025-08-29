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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b65cedc-7bba-3e5e-8e59-8809543f3e63 | -8.7064 | -50.37139 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e622f5e-29f5-3869-b870-aa0db207ae3f | -3.09904 | -54.59346 | 2025-08-29 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3689caca-bb51-3990-8bc5-07d5673c5b1f | -7.72529 | -50.2886 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fc4f8fd-cdf7-338d-bfad-f8e30ffa76de | -3.42107 | -49.0444 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 26cc67d0-bdaa-3bf5-b2bc-b295614d68bc | -6.8774 | -43.60265 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50a174bc-a14c-3015-911a-c9da00594f31 | -6.26818 | -43.81773 | 2025-08-29 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f54c527-f541-32c0-9c95-779592ab5ca2 | -5.6993 | -45.96375 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fecbabe7-4dc5-3b38-8cc8-1ada1030eb22 | -6.43078 | -44.57657 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d5b76fa-29d6-31fa-ac5f-60a9f36c5b40 | -6.54346 | -43.92894 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5bcc8492-dca7-30a7-93b9-95ddf9d95070 | -7.7446 | -50.27491 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c8402ab-3fde-3f02-9f2f-abd23903eb85 | -7.73013 | -50.28507 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ac876ef-d670-3752-9a14-638f981b98ee | -7.74091 | -50.27055 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89440cfd-c557-37e2-b2d0-74ed9e75ab70 | -9.52137 | -46.54229 | 2025-08-29 05:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80a101a3-93c1-3492-898f-cbf7c0fe4eca | -3.66487 | -50.95088 | 2025-08-29 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b118e54-2561-377c-9212-b5b6dbcc282e | -9.49927 | -45.37863 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c30bfbda-c973-313e-8c8b-585e1e5ca63e | -7.22166 | -45.4431 | 2025-08-29 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6abf9d3-c239-3bc4-93b5-340bcb1a8cc4 | -7.72215 | -50.28048 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 077b9d04-e473-3725-962f-d9c70dca9897 | -7.02787 | -44.67234 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ed96ef2-3366-3d87-aa4f-a353e856eeaf | -6.71049 | -49.45341 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe3c3c40-60a1-3175-92d7-0a1e157e4e7e | -4.08443 | -48.04451 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ad7e46-fd22-3363-bf3e-d16cc8361781 | -7.39632 | -45.92691 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3b29c2a-4e50-3b0a-94b7-d2dcf9929093 | -7.02682 | -44.68027 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74ea07b4-1912-35d7-95d9-0d29f91ca716 | -6.13518 | -44.4193 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce0f7157-80ed-3606-944e-dfe80c8a7e57 | -8.69944 | -50.38104 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2fe4e40-beac-3c8a-81ca-9efab5aedc0a | -5.61443 | -45.00169 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 420e093e-6fb7-3287-91c1-ab45adba1bac | -6.98114 | -59.33663 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e429302b-7a55-3290-82c0-c77c04a1cb0f | -7.05056 | -44.37327 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d5548d5-8266-3420-abdc-4264a5f9591f | -6.53776 | -43.92313 | 2025-08-29 05:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10fd1ba9-94a5-3514-86de-d8ccccd9e83d | -5.62679 | -44.99918 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4fb7da4e-5d8d-38ce-8ce7-2e158816e2c9 | -8.70272 | -50.36679 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad5bd499-01bf-370b-9e6c-0c5658991531 | -2.92924 | -53.6894 | 2025-08-29 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caed1d72-f055-374c-b3f3-b3503d509085 | -6.88224 | -43.61906 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dea9bb7c-0bab-3e35-b305-8fb93acab516 | -4.11211 | -48.01979 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04d7de78-fa53-3560-b44f-1e1360a4af4d | -7.39518 | -43.3816 | 2025-08-29 05:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8776833-630a-350c-85f9-2e9fb6cf0908 | -3.0985 | -54.59692 | 2025-08-29 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4385e3e-b89a-3b55-a0dc-563204659043 | -9.69363 | -47.06155 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9505e80-2f05-3ef1-b643-5d61751daa0c | -6.97077 | -59.33044 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e507e0fb-4111-39e1-8755-cc021df9e4e3 | -9.43268 | -47.64278 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fcca6de-b2a8-31ae-ab88-9c139a284d63 | -7.74522 | -50.27069 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b94a66d6-217a-3add-9880-92c8065522a4 | -9.69763 | -47.06621 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b5e8590-20a2-399f-89ad-4846e6e9b855 | -6.00172 | -57.85141 | 2025-08-29 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42a2ecee-b380-33cc-91f1-8c2de0825aed | -8.69461 | -50.38451 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f31b647b-b45e-317a-a8af-9ab915411cda | -4.06952 | -47.95254 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abef758a-9cc9-3293-9f7c-83d0a0b1fd17 | -6.53144 | -44.11293 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fb01538-0d19-363e-90dd-ef64cb344fff | -3.80361 | -48.64651 | 2025-08-29 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6005ea1-ebf3-3f68-ae07-85c14ba1b918 | -7.7278 | -50.3009 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2b1011f-8faf-3e69-b41f-e2c6fc6ee398 | -7.39831 | -43.3817 | 2025-08-29 05:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b24370ad-ddb5-393a-896c-874e5f0732a2 | -3.98269 | -47.88251 | 2025-08-29 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a68da5e-1b1f-3caa-862c-bdc4b4c6b976 | -7.39857 | -45.92948 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86030bc6-9517-3682-83e1-2b12ce1d26b0 | -7.81328 | -55.22655 | 2025-08-29 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f630378-9daa-3b5a-b545-d869369a3c7d | -5.75711 | -49.98633 | 2025-08-29 05:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ac2d934-a75a-34b6-932a-92814fd56070 | -9.44385 | -48.25047 | 2025-08-29 05:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3692b858-1145-3289-9227-4ce995aee7be | -7.72408 | -50.29681 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89cddd7e-7502-330b-ae75-55a4e9a09e1f | -7.04357 | -44.37801 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 213f9093-c221-3e7e-b76f-47a33237858a | -6.1458 | -44.43168 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55e45ace-169a-36b3-83dd-4eebaac1d070 | -5.61831 | -45.00858 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 60303fb7-7997-366e-843e-448c52fb382b | -7.3934 | -45.92492 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d50326b5-c504-3072-83b0-71b94173c5a4 | -4.11286 | -48.01493 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71495a7d-8dbd-3909-97c0-c6ad3335b36d | -7.73604 | -50.27427 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d7b6bedf-d1fb-3b61-bedd-800e511a8f40 | -3.76491 | -54.81438 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7bcb7ed1-dae3-3b83-b0e7-946a4ec0f77e | -13.19144 | -45.28753 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 83bc000c-4051-31b1-a19f-2254da32018c | -13.62633 | -48.20022 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa4c50a9-4d7d-3e5b-b5d0-28e49332df52 | -13.41836 | -46.97781 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 8d1323cd-2946-36a0-ac4a-f232c05dd4b7 | -13.42212 | -46.98381 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 61ff5f93-e871-315e-a4d8-f20fc24c9181 | -13.63085 | -48.252 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ec8339-0fb5-323e-84b1-7ad229ba0f60 | -12.81572 | -48.18449 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef70508e-7a54-31b5-a452-0166c77fc1ab | -10.4529 | -57.95458 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c07c3548-2c77-3959-a2b3-d11b580d8915 | -12.09256 | -44.72371 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8b6946f0-7bae-3396-93fd-127f571bdae9 | -10.45628 | -57.95514 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb41fe94-a566-3eb4-9fd0-cad29b841cdd | -9.08726 | -65.73601 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2148c4f6-8a0d-3694-aaff-6440e7397fb7 | -13.57141 | -46.86826 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89fc8978-64fd-31fe-9899-f211423f8405 | -15.13112 | -48.12001 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a9dafd3-1ef6-35c5-a7e6-1f2185f9ccf7 | -8.96272 | -65.95029 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae39a7ed-7f08-3ab4-8082-9e0e4d18493d | -13.63159 | -48.20133 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a76957e-9a64-3a22-bc1f-9b4aa49bb1a2 | -11.30729 | -43.55038 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2900ade-41f4-3c83-a9b6-c48eac473093 | -9.16299 | -65.78534 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8756b8da-15bb-3b6c-8f57-290fe14eec72 | -8.95556 | -65.96014 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c3a03c-6a3c-36e2-a442-960f0c110c39 | -15.04138 | -48.12638 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67df5618-6f05-34fa-9b17-62b13f41ab9f | -12.68795 | -48.18901 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e77e5723-9a2a-3778-a7ad-70835129234e | -13.50692 | -50.81049 | 2025-08-29 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2324015-d224-3c9d-9315-ade97b959546 | -13.37064 | -46.87672 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82602182-44bc-3c82-a9d2-88034ff30585 | -9.16731 | -56.99802 | 2025-08-29 05:08:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aefa4a0-7d02-349a-abda-395aa2977ce9 | -12.40026 | -46.49414 | 2025-08-29 05:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8bb70d6-bc28-3ac4-bc27-e38e21f391ef | -9.14857 | -59.56532 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b13ddfec-cd22-36df-b2e6-d0c50a5a0a30 | -10.85619 | -60.8151 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| becb6d41-4727-33fc-bec6-d478db97c9d8 | -12.06052 | -46.63064 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6316a946-0e73-34ec-9d2e-0e73b38d90d1 | -8.13489 | -61.21643 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69c90d23-2bcf-312a-8696-8854e5fc7d23 | -13.54528 | -46.9426 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af759fa1-ecf1-3eff-bb22-46f54904e8d6 | -9.11087 | -65.79105 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24b54f46-c2d2-36b9-a121-4fe55bd9d0e3 | -14.28941 | -53.30683 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8182421a-2e10-3833-b581-6395c98bd6b3 | -10.61763 | -54.91095 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2699b2c-2ff6-3370-8709-114e8cc21598 | -12.99937 | -56.92052 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0b645c-9be1-3be2-9ccc-6c6917793a8a | -12.83994 | -48.16222 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667c8ff8-1ad6-31d7-bd8f-cc9df43ea32a | -13.61563 | -48.24442 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44329456-e23c-3687-bc79-1c86d4c8d8fe | -12.8961 | -48.13695 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03160603-289b-3c2e-98c2-844cc9988e23 | -9.67767 | -48.32634 | 2025-08-29 05:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8892de29-787d-3504-85eb-14d118cd3774 | -9.1089 | -65.74006 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ac4b6b6-458c-3ed1-a964-25cc0812e814 | -11.34772 | -43.56528 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 864fff11-dd07-3a25-80b4-e20b12a74164 | -14.59018 | -54.52465 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b218000-b2af-33c5-b152-8dba702c217b | -10.46595 | -57.93816 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README63.md)
