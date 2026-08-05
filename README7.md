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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 634a427a-0c3c-3152-bc67-fb78ff138c5c | -17.341 | -42.63132 | 2026-08-05 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a0259c2-c3b4-375b-af55-355b870467d8 | -21.53898 | -41.314 | 2026-08-05 03:45:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 3cb10e0e-853a-3a18-8f0d-e1dcda13f805 | -13.4429 | -43.68006 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 994bfd12-b191-3920-9335-d7f3210157e5 | -16.92612 | -44.91139 | 2026-08-05 03:45:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02fca8c2-c041-3e20-90fc-439f6d82c00a | -17.97975 | -47.14936 | 2026-08-05 03:45:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ae7431-0d83-3b4f-86e0-0b1229b24f18 | -17.98402 | -47.15944 | 2026-08-05 03:45:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 672cd83b-298d-33ff-8d85-4c2d1a365e82 | -17.98506 | -47.15485 | 2026-08-05 03:45:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 611089a1-2f6a-32d1-9597-cd84ad7d1180 | -13.43573 | -43.86122 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8668e460-0ad2-3b7e-a8bf-6ed69c9b600c | -15.14245 | -42.15788 | 2026-08-05 03:45:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| afc8b882-6937-367c-a3df-c6078f9c94f0 | -18.84365 | -47.92086 | 2026-08-05 03:45:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00d2766d-6d6d-3c60-bf2b-61a4c78a5c62 | -13.43742 | -43.67887 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 347faa0e-d66f-398f-8b18-12cc9e6119b4 | -18.88851 | -43.34531 | 2026-08-05 03:45:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a884b48c-d210-3e1d-a3a3-8672377a93bc | -18.69567 | -44.5535 | 2026-08-05 03:45:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e99bf38-2602-3895-a630-92ddba1e7fb7 | -22.19932 | -42.5407 | 2026-08-05 03:47:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 817f481a-d839-3240-9900-31e4785c0d8e | -20.38587 | -49.30953 | 2026-08-05 03:47:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 49db7e69-ebf2-3040-9c90-edace2b78069 | -23.14215 | -48.67266 | 2026-08-05 03:47:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f4194f-86eb-3082-830d-773f56b918c0 | -23.17428 | -47.03169 | 2026-08-05 03:47:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0cfd92c8-db71-3839-8857-d7f2effd7a01 | -21.33608 | -43.69965 | 2026-08-05 03:47:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aeef8896-f1e4-325e-8061-6f8a308a154c | -20.38433 | -49.3158 | 2026-08-05 03:47:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b27ed000-5e89-3dde-a54d-9587aa13d043 | -23.14092 | -48.67769 | 2026-08-05 03:47:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f3a091c-283f-3b75-9e2a-0bcb926368eb | -12.5947 | -46.9301 | 2026-08-05 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bebae471-b199-38cf-8356-f31779577eb4 | -3.05317 | -39.93304 | 2026-08-05 03:57:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f80d8d3-410b-3b60-887e-a0695598de45 | -3.02578 | -39.97129 | 2026-08-05 03:57:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eac3a19d-13ad-34eb-8040-49df13fa2c97 | -3.05378 | -39.92926 | 2026-08-05 03:57:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f47cf8a3-93fa-39ad-a031-1afef9667ab8 | -2.99008 | -39.95856 | 2026-08-05 03:57:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e01b2ecf-ad46-3a69-9bb9-d8fe7f23700d | -12.5942 | -46.9527 | 2026-08-05 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0de99431-de8e-35b6-8471-c9d625046f74 | -12.5947 | -46.9301 | 2026-08-05 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2b40c63d-08c1-39fd-a8ee-03a8b412b0d9 | -4.3935 | -40.43164 | 2026-08-05 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f92a19ca-a8be-38d3-8d67-aa1e8b4d25ac | -7.62771 | -45.31147 | 2026-08-05 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35ddd689-3dc8-3107-81ba-6d38340b4476 | -7.18141 | -40.17263 | 2026-08-05 04:00:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 8c862adf-f607-33ed-871d-d2c7d9a769ce | -8.34974 | -45.98758 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bd9b82e7-9ab0-3ce6-b7f6-13edba2f5a33 | -3.6648 | -49.47432 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cacacc4-1629-37c8-8494-00f75b425e61 | -6.89228 | -42.41402 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 082221b2-829d-329a-a494-f55ac73a60f0 | -5.61231 | -41.14104 | 2026-08-05 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57d55825-86c2-3fb5-8f44-c86a3a93ac1b | -6.14638 | -47.1763 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f44173fe-c0c1-3ead-8330-724d457d41ff | -6.89675 | -42.41014 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e5a77726-1fad-3be7-9545-f3dc0e5c5720 | -6.6504 | -43.91003 | 2026-08-05 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e4407b09-68df-3e1c-a8cc-06a99a62f069 | -6.00946 | -47.40014 | 2026-08-05 04:00:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16afb4c8-fb8a-3d21-b6f0-8008faabe397 | -6.30693 | -43.6194 | 2026-08-05 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9a2c56b-84c9-390d-b1e6-09b24cd8abc3 | -6.93592 | -41.92499 | 2026-08-05 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6721c685-b229-30b3-bc52-f389079ba1cd | -8.34682 | -45.97729 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d15b4341-3535-3a77-8403-fb4d7b850162 | -8.491 | -46.8567 | 2026-08-05 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec1cb8ac-1527-37bc-b91d-d45f3f86e373 | -5.33088 | -37.31699 | 2026-08-05 04:00:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d36cc04-7237-3f18-be9a-cc38392aaf96 | -2.88687 | -48.01992 | 2026-08-05 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b88edb7c-19df-3bf6-93cc-56a18e981bae | -6.41606 | -39.34806 | 2026-08-05 04:00:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 44d60729-b77b-33bc-91ca-f879ceebb754 | -8.49474 | -46.86374 | 2026-08-05 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f708511-2055-3b55-8365-5f6be16970f7 | -7.67627 | -45.95743 | 2026-08-05 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d84d4c4-2dd1-3703-b98c-16900bedbb36 | -8.22548 | -42.21937 | 2026-08-05 04:00:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83a7ef89-a9ae-3311-b674-897933787971 | -3.02964 | -48.41512 | 2026-08-05 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d7c3171-7087-3d5f-bd1d-94d253682ef3 | -7.48228 | -36.61678 | 2026-08-05 04:00:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1cbe87c9-f815-3dbd-a0a0-51b9ffb4544b | -6.64691 | -43.90571 | 2026-08-05 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 90ea3c4a-386a-38e7-a782-5d9765e1160e | -3.02881 | -48.40988 | 2026-08-05 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df6b762-45eb-3ab6-ba52-8da5420e2b15 | -8.37925 | -48.21348 | 2026-08-05 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49cc19ba-2939-3403-87c1-11343e40a501 | -3.24268 | -47.92558 | 2026-08-05 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b4dc15f-9f01-3172-9256-45cfbd93a394 | -7.223 | -43.3504 | 2026-08-05 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9713ace6-12f3-3267-9562-a6e6012475fb | -7.17804 | -40.1721 | 2026-08-05 04:00:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 28.0 |
| b5a44945-a411-35f9-8d66-e027ba908ecc | -3.24776 | -47.93009 | 2026-08-05 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a88304f1-0708-3c72-b3a1-e88f79983e34 | -6.24204 | -47.14526 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46a4516d-2451-3d19-94f1-36fee3353ddf | -6.00889 | -47.40336 | 2026-08-05 04:00:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 261c849b-0c07-3cc3-9a87-a250834b3cc0 | -6.89898 | -42.4198 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 69ffa1ff-077c-3381-ad64-948de7849715 | -6.15155 | -47.17715 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 44d8be74-fe2b-3fbb-817b-ca6a2b784f65 | -2.68776 | -47.36018 | 2026-08-05 04:00:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ffa9dba-51f0-3362-a860-fdf1a3924b22 | -6.89526 | -42.41916 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 533c80ae-bd4a-38c8-a662-fc2de61198fd | -7.50033 | -49.7489 | 2026-08-05 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| cad16037-6be6-3721-80fa-793627ef8fbf | -3.16382 | -48.14293 | 2026-08-05 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98c22c0a-d96f-32ad-96b7-f0566e6ddd06 | -8.3414 | -45.98123 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79069638-fc9f-3596-b6c0-6f7961b2df1a | -4.37605 | -43.3877 | 2026-08-05 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdd4cd80-f46b-3685-9b74-ed2d9d1e07b0 | -7.17862 | -40.16849 | 2026-08-05 04:00:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67df7d01-1c76-3cd4-83c1-0b6848deeebf | -4.9797 | -37.23721 | 2026-08-05 04:00:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8cad14f-6f14-3c69-be59-9a0a0b114b33 | -4.28105 | -48.03602 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e18ddb85-e008-3afe-abd6-bb41ded00974 | -8.35141 | -45.97805 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 21038096-3355-337c-8dff-1c9d12f1aa84 | -7.50445 | -49.74203 | 2026-08-05 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a72895f7-e090-3e93-a232-0c728ab7926e | -7.74036 | -45.05108 | 2026-08-05 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46ff9c03-1d79-3123-b05d-046a1b4009f8 | -3.67974 | -47.64954 | 2026-08-05 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb8ef02b-3370-31bc-89cb-e332509e8da3 | -3.99092 | -48.39939 | 2026-08-05 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb120202-31e8-3820-b85a-975925880e52 | -4.39698 | -40.4322 | 2026-08-05 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 550fb2cf-8a03-3739-8caa-1fa8bbfa5496 | -4.36661 | -47.77377 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bdad8183-aedf-32d1-bcc1-ddbad1d7666e | -3.67186 | -49.47054 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 258766ed-6da1-38be-9a0f-3e5009705b74 | -3.67025 | -49.46849 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e38cdf10-cf60-3134-b906-eff840781a11 | -9.4841 | -40.36833 | 2026-08-05 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c4c91de3-5af6-3978-8ad0-ad54c8878a06 | -5.82205 | -44.13962 | 2026-08-05 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a51a58-e5ae-3e31-b4de-bf1938611c22 | -6.65102 | -43.90637 | 2026-08-05 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2f651b29-b763-39d1-87b8-b7db8480fefc | -3.16434 | -48.14154 | 2026-08-05 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c62d52-85e5-354a-a0e6-0d8a901038ce | -8.33764 | -45.97579 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2eb70c0b-000a-3063-94ea-fda34c27ba2b | -3.24202 | -47.92945 | 2026-08-05 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceba3304-a9d3-32ab-b58e-ba3ad22508d3 | -4.46068 | -47.91998 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f53e6ba-86df-3010-9cb2-3e37845ddd19 | -9.48075 | -40.36779 | 2026-08-05 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b3ec2376-a79c-30f5-acc9-a56147383fb9 | -2.89263 | -48.02089 | 2026-08-05 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 150180f0-e32c-3bca-ae69-e485a7111788 | -4.46132 | -47.91625 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18f690af-e954-3c98-b5bb-cc801748a4bb | -8.3846 | -48.21431 | 2026-08-05 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bc597b7-3edb-33d8-be54-be47a69302cb | -6.39866 | -41.34027 | 2026-08-05 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ea31cb0-1c05-377d-ae2f-9c2ea2ee62ed | -6.9857 | -42.12267 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d67fbefa-d458-352b-ab74-5ffbe2cdc6d6 | -6.14582 | -47.17946 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e317013-f0ea-3c66-89eb-33c2de1887bb | -6.90121 | -42.40629 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 831c7abf-d779-3c77-9c91-fccdc7818628 | -7.22233 | -43.35225 | 2026-08-05 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f5b7360-e4f7-3eaa-b219-4a2f86f432cb | -9.48687 | -40.37246 | 2026-08-05 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 02955729-d602-3721-8b32-30bfc9dd5af0 | -7.50114 | -49.74447 | 2026-08-05 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fc419f7a-eee5-3399-85cf-477736a55a61 | -6.9042 | -42.41141 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dfaeb9e2-3494-3b4f-83f3-d529940eba4d | -3.68058 | -47.65055 | 2026-08-05 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00ba00da-2138-318c-932d-8b142ef2136b | -7.2232 | -43.34721 | 2026-08-05 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
