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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17ca35ef-fc19-3102-b9a3-a023bf0e8aa3 | -11.49576 | -50.28653 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8ddb835-ae9a-3b05-8e0a-922a3fe53de3 | -7.06745 | -44.38765 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 078c55b5-529f-3b3f-b51e-3fea76831719 | -7.19516 | -44.48244 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62b00137-8beb-3257-8548-b29cb227664e | -5.427 | -47.1446 | 2025-08-06 04:19:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff04b09d-20f0-3ff7-878a-5d46269ad6cb | -11.90956 | -44.94775 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5f111e9-1068-3da9-9e24-b4b3d2be8ac2 | -6.44042 | -43.11609 | 2025-08-06 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47cb14aa-0526-3175-9962-b32d0464c909 | -5.80712 | -46.98941 | 2025-08-06 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cca8e9b-fa67-3a0a-a7e6-793f18f58f2c | -11.52007 | -44.36166 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c13bf39-fd0c-3608-aaee-8fc85392e832 | -11.48728 | -50.28998 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95a3da5b-2f4e-307a-8e2b-b04fd0eab16f | -11.42699 | -45.1274 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae4415b-40be-324d-8435-72b14ea2da6f | -9.07815 | -45.05793 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a0cf29f-3e56-31b6-8d62-a675759baf23 | -9.02373 | -51.12939 | 2025-08-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55f9b3fe-fa66-388a-bb28-455f14a4576f | -7.83904 | -45.22723 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eec3af67-d97a-3de6-8599-96dc94d6b27d | -8.84616 | -47.47666 | 2025-08-06 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eac6977-eedb-35f6-8594-b1c17b0df1fd | -9.70799 | -51.94902 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f94c4efc-9b89-3e32-8900-a8365f831d11 | -11.49494 | -50.29136 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e20dde71-e69a-3a36-afd7-935357ade69e | -7.06968 | -44.39511 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 342a6b62-68e1-3247-9dd5-30f0b7edad7c | -11.32951 | -47.30895 | 2025-08-06 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f82df97-ae9e-3626-bbda-607ce73d1933 | -8.52728 | -47.45292 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 236c223d-d2e2-3b06-8951-7818b3d9ec72 | -11.73178 | -47.53277 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06c40bb8-c7d3-3cdf-bf8c-d649c29c13d8 | -11.91067 | -44.94053 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a768158-a000-3612-a3e7-7ab99cec6b1b | -7.21555 | -41.84981 | 2025-08-06 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6f32c5c-2fcd-300b-b594-f23714a6ea16 | -7.85867 | -43.86511 | 2025-08-06 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7913df3c-4b65-3964-a5c4-41f06346e10c | -10.47596 | -44.34088 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b073c006-cf60-366e-bb00-01eefc3bfb77 | -7.50547 | -44.88673 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b90b31bf-2a98-3e9e-b41b-f059c147708d | -7.85587 | -43.86102 | 2025-08-06 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eada444-9368-3582-a220-6705623c95fd | -12.76118 | -44.41423 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1da8a531-f1f1-33e1-bedd-f3e0282c8aab | -10.47933 | -44.34142 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a70509a4-2b70-3d5e-8d41-a614fd1cb281 | -12.54813 | -44.7378 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 122d52dc-2470-3759-a8c6-b695724a5c02 | -8.52791 | -47.44913 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4cd3797-fe85-38f1-b49d-5cc045772c13 | -10.4597 | -44.33458 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94384081-a39c-3ae9-90e6-33e66ac3748b | -6.26741 | -53.63708 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 797d2e8f-6931-3f06-bc6d-6d21c3634756 | -7.63493 | -44.58013 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dcb98c8-ebd7-382f-8406-dd227c9b9350 | -7.64896 | -46.59392 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aca3003-9411-33cd-8069-2303cdc21c83 | -6.78631 | -43.23944 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f3ac574-809e-38a6-b3a9-bd9342465385 | -12.02399 | -44.82073 | 2025-08-06 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dcb69b3-254b-35ae-9e87-e3dca8b85b32 | -7.38584 | -48.08929 | 2025-08-06 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba007a11-b1be-3116-ae16-df96fefb5e62 | -9.62448 | -40.59079 | 2025-08-06 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 85fca9a9-19cf-3ef9-8d9b-d658a097a3ac | -6.91552 | -43.68651 | 2025-08-06 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 01a66340-c313-356a-9358-9b140a1712ca | -7.90663 | -45.52958 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f263221-0547-39c0-9e14-e220d0f49274 | -6.4158 | -53.36634 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99054abd-083f-32b5-bbfe-62c87b66716f | -11.4881 | -50.28515 | 2025-08-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d387062-4060-3bb3-9b67-6de7526ae132 | -10.44018 | -44.3722 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e5ef151f-a2c5-3a55-8e74-5d810f9f853f | -6.6716 | -44.44292 | 2025-08-06 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f70386-6f85-3917-b5f7-03ff194695fc | -11.51724 | -44.35745 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f286a652-c8c5-3336-9baf-77c228c73441 | -7.99788 | -43.23643 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 821dd3b3-139b-3192-beeb-b36e169a4056 | -10.46486 | -44.39082 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97c898af-87eb-3d82-a406-4df9de165468 | -6.69725 | -44.32257 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 702b8671-8ef9-3ab9-8af9-3210519bb68e | -8.9215 | -60.7297 | 2025-08-06 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| fd8701bd-2451-3550-ac68-43444b0f135c | -11.4393 | -45.1154 | 2025-08-06 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 6ec13950-f221-3bef-b6b0-2ac3e8c02a49 | -21.0754 | -49.9855 | 2025-08-06 04:20:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| 08186898-a71a-347e-b54c-ae17d5e51e0c | -13.0728 | -56.8729 | 2025-08-06 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 836b8bc3-9cf1-37b4-8bfa-4a65de248cdf | -8.9213 | -60.7489 | 2025-08-06 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| fc0c0d5a-8026-365b-8151-bc6030cf65fb | -13.0731 | -56.8527 | 2025-08-06 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a8bc9fcf-e0f9-3c66-8479-e3a5af660bc6 | -11.4389 | -45.1385 | 2025-08-06 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 11d42773-fb56-3c1b-9286-36b6a47e998e | -12.65215 | -48.10843 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8708f0f-8f8e-3060-989b-ca2a6189ec49 | -13.00265 | -44.89847 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbdb9844-b15b-3ea9-aa27-c05794d6ad41 | -16.81482 | -51.32523 | 2025-08-06 04:21:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8f7fa0b-954e-3e23-b76d-39bbe436bce0 | -12.97345 | -44.8864 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b42a296-b08f-3855-9911-279a032e6439 | -12.97008 | -44.88587 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8cd780a-203e-3c5d-bb45-4b20cd9307e3 | -13.05509 | -56.87246 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b335cfa0-9c1f-3b37-af59-d2af7d019c44 | -12.67291 | -48.13131 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06032240-3431-3c08-b776-4c8e863b649b | -12.71293 | -48.0799 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ea9a476-a53c-3388-889a-84231f6a2dff | -16.32892 | -50.35121 | 2025-08-06 04:21:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e926dd67-82a6-3dfd-8e96-e200a710f1d0 | -15.54182 | -42.65509 | 2025-08-06 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 121cacb4-0b84-3ae4-a75c-672ec3c34ba7 | -12.72655 | -48.08223 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f632e06c-4e0f-35c1-85ea-275169038ae2 | -11.37518 | -54.33628 | 2025-08-06 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ec9065a-9266-33eb-987c-585f7bc9f92c | -11.32146 | -55.22313 | 2025-08-06 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a6fbc9f-f54a-31cf-822f-ee540cb791ba | -11.87164 | -52.30014 | 2025-08-06 04:21:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 720d020d-aaac-383a-9be3-435e051c9594 | -13.06159 | -56.86967 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62b1dbed-10ca-3096-aa0f-4ae5f2b79da1 | -13.04856 | -56.87539 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70945467-5df7-352b-873f-592af4adfd5f | -13.72884 | -53.16454 | 2025-08-06 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e990577-fe0e-3e2d-a1ad-b92f2452ca4f | -13.05669 | -56.86451 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 610d8ee7-7378-38e7-9e64-53eab9c20fe2 | -12.54104 | -47.17241 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9618795c-57c7-336f-8b4e-f7a6bfa64ed1 | -15.11925 | -47.43354 | 2025-08-06 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb81b944-a265-36cf-aba6-06c5f8a63470 | -12.7083 | -48.12947 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c00fdeb7-290d-3e92-9c14-d308530372e2 | -13.06727 | -56.87099 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 598d4790-859d-3772-b06f-1ab3b183dad8 | -13.06886 | -56.86302 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2055f3cd-16b9-39e9-ba30-fb500380c27f | -13.05177 | -56.85938 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6537ba7c-8308-35d1-bd2e-64ffabe0b222 | -12.99873 | -44.90162 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a894cb73-a04c-379c-8351-7839520ac68f | -12.73329 | -46.39274 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d95d93d-5297-3312-9025-231d08b7bb56 | -15.70116 | -48.96593 | 2025-08-06 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cfb4563-9998-358b-93bb-2d3879483555 | -12.99084 | -44.88541 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb19fcd-0594-357f-9e5f-ebd5a310986d | -12.97401 | -44.88272 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58c4fb0a-50b8-3280-9e65-a136c4c264ad | -16.71502 | -49.45348 | 2025-08-06 04:21:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2369b332-9a53-3dcf-b9b7-51810cdf685a | -12.98636 | -44.89222 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3a55932-fea2-3a99-9aa5-e74d2c5a9471 | -12.53103 | -47.17078 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c743d73-4fd4-36d6-afc3-eab31b550974 | -14.34032 | -43.65659 | 2025-08-06 04:21:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7d39210-508e-3428-9d14-062e3aa0625d | -13.37271 | -43.75807 | 2025-08-06 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5732ad00-b275-3bcc-82f3-de2e36e3433e | -13.25668 | -46.9908 | 2025-08-06 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1445078-d3d6-3b69-a022-ef63444729a8 | -14.71035 | -47.86078 | 2025-08-06 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f90f340c-242d-3c68-9883-78fbf0f673af | -12.71731 | -46.38651 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75631880-fcfd-3b3d-bb8e-dfa1a23c8b4f | -12.70489 | -48.12885 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ba15736-9388-392a-a216-4ee572ea5d43 | -15.63956 | -46.95951 | 2025-08-06 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3fc2e05-3cd9-3c54-b77e-8c1e523b3b24 | -12.66239 | -48.11015 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8775819-bb5d-3153-bd68-1ce8b15ce071 | -12.52769 | -47.17024 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a67f03f0-6575-318b-b783-c812f3c81679 | -12.66115 | -48.11759 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06750ff7-63bd-3afe-bdd6-f6228331efff | -12.72995 | -48.08286 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ad559fa-c9a1-3998-8388-33c95738c957 | -16.54871 | -48.67979 | 2025-08-06 04:21:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7e44059-4450-3d6a-ba9d-02aa8afaa509 | -15.11982 | -47.42995 | 2025-08-06 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README20.md)
