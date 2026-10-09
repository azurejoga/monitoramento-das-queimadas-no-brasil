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

## Dados Diários - Página 245

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e6e48e0-1f64-37b0-a7fe-7e9ebf2ed447 | -10.9575 | -45.389 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| f99e0f88-f608-301f-a323-45565bbee04d | -12.0063 | -43.4402 | 2026-10-09 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 947.2 |
| 6e3d8a90-f5eb-3421-92a9-e60fce016e30 | -5.5127 | -43.0512 | 2026-10-09 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f458626b-9689-33e5-be0e-b57fa2974cc3 | -10.491 | -47.2533 | 2026-10-09 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 45089bdf-ffa1-3d3e-9bea-774bb4c4db12 | -9.1012 | -45.1393 | 2026-10-09 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 22da995d-456a-3247-a17c-c29cbd5645fd | -8.0575 | -45.6357 | 2026-10-09 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9e3c5f27-2da2-38d7-b618-d40197b5ed4c | 3.5493 | -60.2633 | 2026-10-09 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5fbffcc0-1120-38c5-867e-805010854d23 | -3.8786 | -44.1265 | 2026-10-09 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9794c8b4-f9a6-31e0-93e1-bcc4e867da7a | -15.2535 | -42.3741 | 2026-10-09 14:40:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 935.0 |
| 17b2bdd4-56d5-3908-852d-d6bb8f3886a7 | -7.3243 | -43.9913 | 2026-10-09 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 51f60b7a-ae26-32dd-8a87-ad45ce2c2aa2 | -9.7177 | -45.7055 | 2026-10-09 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 199.6 |
| b68021f7-a5a0-3f7d-b879-64fcc7c2e9e4 | -14.3608 | -55.032 | 2026-10-09 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 94f6ad6a-2cd5-3cd9-b155-d5091acea135 | -12.0251 | -43.4609 | 2026-10-09 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 055ebc8b-08e1-3720-83db-cd3a6c9ba3b2 | -5.7312 | -41.7309 | 2026-10-09 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| b2d6d1ea-f919-3b51-99c2-89f7281d6dcb | -8.6703 | -44.8669 | 2026-10-09 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 589234b7-e77a-3f69-804d-9b47768d7adb | -9.8629 | -47.4809 | 2026-10-09 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 52e04bba-293b-3d62-a1a7-89f717a20c78 | -6.7365 | -55.1474 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| bb6fb30b-d654-3a2c-8623-8c8b0050e476 | -14.4535 | -43.9359 | 2026-10-09 14:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 329.6 |
| 050a0be8-e020-3036-9f61-5442e4db34fd | -2.8306 | -49.8768 | 2026-10-09 14:40:00 | GOES-19 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a772b922-d201-3957-a8d1-65cda00e2027 | -8.2173 | -46.4292 | 2026-10-09 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 847d8edf-acc3-3429-9ff3-84a5424d10ee | -6.0611 | -42.5844 | 2026-10-09 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 206.2 |
| 6d81dbe1-1fe8-3c5a-9db9-d05098b12d2d | -8.9958 | -45.9454 | 2026-10-09 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 19d5eb32-dc23-3b66-a5f6-16301e08ec17 | -12.2302 | -44.8126 | 2026-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 299.9 |
| a548b6a4-56ba-36ea-978c-96180c37a901 | -3.8788 | -44.1035 | 2026-10-09 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 58177dc2-3c24-35a7-90a8-78303d5125f1 | -8.9299 | -45.2269 | 2026-10-09 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.4 |
| f8f18032-a66c-3a55-8caa-7fd05d2e5d11 | -6.6815 | -55.0703 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 72cb680a-03bc-395e-8e48-059e39935bf5 | -8.5313 | -46.911 | 2026-10-09 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 163b707e-45d5-3880-aed7-0c20cfa22cc2 | -10.9766 | -45.3865 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 4058f99c-109d-359b-b99b-77ddbdd5cd75 | -9.9798 | -45.9236 | 2026-10-09 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 1e03ee49-0fac-377f-a130-f63cffc8656b | -1.1094 | -54.1601 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d8d1875e-bf81-3698-aee8-98d16764566c | 3.9309 | -61.0906 | 2026-10-09 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4c2d4770-3e14-3e4a-84be-d2497926b5ba | -9.183 | -43.3688 | 2026-10-09 14:40:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 414.1 |
| 929cc9a8-892d-35ba-8db6-766b64ce1de5 | -3.0109 | -51.0236 | 2026-10-09 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| bb81d7d9-8109-3fb5-8c0a-b927fda3203c | -11.8787 | -47.3668 | 2026-10-09 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 219.4 |
| aa4015ec-12d6-3ffb-9940-31280d54326f | -8.9687 | -45.1542 | 2026-10-09 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 73679a10-56db-3cc8-a108-a4631ecccce3 | -9.8798 | -50.4918 | 2026-10-09 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| dfc86356-b66c-3525-9edf-edf95ddb0cfa | -8.969 | -45.1313 | 2026-10-09 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| ebef773a-9b33-3969-bd92-5062d84a0b5f | -5.9649 | -40.914 | 2026-10-09 14:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 1f3bff74-73a0-3f48-9553-e2c1bb52809c | -1.3264 | -56.398 | 2026-10-09 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| edd95d00-b080-32da-8825-7269fac4656c | -8.0764 | -45.6339 | 2026-10-09 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 39d8fcf4-217f-3786-b2b3-ea95e730536a | -6.9328 | -43.6799 | 2026-10-09 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| f7d78b45-99cc-31fc-bc98-380ad4bb2709 | -1.3447 | -56.3979 | 2026-10-09 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e1444bc2-d3f5-36bc-9290-7cc1c157608c | 0.5246 | -50.8991 | 2026-10-09 14:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2d155ccf-d38d-3505-846c-f988ba6e2aeb | -6.4411 | -55.0424 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 7146fec3-fc23-346c-8355-25763addf16c | 1.1507 | -50.7483 | 2026-10-09 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ab095323-14c2-38b6-b5a2-903f648abd7f | -11.8783 | -47.3892 | 2026-10-09 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 996.2 |
| fc0178e8-afc9-3964-aad7-5d6bc36179bb | -2.1544 | -54.4668 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 0d737ed7-8ff9-32d8-92a2-c80c56f527bc | -15.2738 | -42.3452 | 2026-10-09 14:40:00 | GOES-19 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 163.1 |
| 76d9a4bf-3b16-3d1c-be92-b0793d8776e4 | -1.4569 | -54.7562 | 2026-10-09 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ac22ee13-3e0b-3d9f-9c41-7e02f784786f | -15.3838 | -41.878 | 2026-10-09 14:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 746.7 |
| 3d204618-05b3-3dcf-b408-503439ad2d0c | -8.3011 | -45.7245 | 2026-10-09 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 226fee8a-202c-36ac-9019-838e563999eb | -10.4724 | -47.2333 | 2026-10-09 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d9191be9-4f93-36f9-8921-67a4ce2fe7e5 | -10.7479 | -46.5959 | 2026-10-09 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| d6c0c990-79d4-3497-aa30-299af4641737 | -11.3371 | -46.6547 | 2026-10-09 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 539b8e75-9872-3c60-bc86-d50c1b028665 | -10.3921 | -46.2575 | 2026-10-09 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 286.3 |
| 12dc7373-b00e-3d25-b9da-33824643ebb5 | -15.2541 | -42.3495 | 2026-10-09 14:40:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 282.4 |
| 7f94e647-d356-30fb-b774-ee00b40b9a24 | -11.245 | -45.3037 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 304.6 |
| 9e789a12-2523-3248-a5e2-e03ee265e39f | -14.0044 | -48.7743 | 2026-10-09 14:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 4c4fcaed-97a2-3ee0-b1dc-7d6d5e432f21 | -9.1015 | -45.1164 | 2026-10-09 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 69529785-37bc-3c6d-83a2-cf27e2f63880 | -12.211 | -44.8156 | 2026-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 271.2 |
| c9be8803-8b4c-3dac-9fca-1b661189d395 | -14.0238 | -48.7714 | 2026-10-09 14:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 5cf65132-9ac9-391b-8f00-a075a16534d2 | -13.1056 | -46.3321 | 2026-10-09 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 9cd989b4-1903-31e5-9d3d-b2cc9d20b30e | -11.2068 | -45.3091 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| c343bf6d-9119-3af7-b45e-31b3c812709f | -10.5281 | -47.3156 | 2026-10-09 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e73c8911-a5eb-387e-a142-b84a1252b284 | -10.4914 | -47.231 | 2026-10-09 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 80d60481-1ccf-39b1-8416-61ec954604a4 | -10.4334 | -47.3046 | 2026-10-09 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 24c514dd-7d96-35c8-883e-4bde8ab17c5f | -6.0421 | -42.6096 | 2026-10-09 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 2f65695a-de80-372b-95dc-16a6595475f4 | -18.3335 | -42.3598 | 2026-10-09 14:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 181.8 |
| f26a4a3a-dfe1-35d4-91fc-7ff63d4bc909 | -9.5502 | -46.8492 | 2026-10-09 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a9361f94-ad0a-3b43-baf1-2d9baae1cce6 | -11.318 | -46.6573 | 2026-10-09 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6a66dbbb-afb1-3c40-832e-7b1fab40be29 | -11.2259 | -45.3064 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 279.9 |
| e3e2b2e8-8c67-34ad-a402-cee61842b244 | -7.6656 | -45.3791 | 2026-10-09 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| cc9711a1-31fd-36b0-bcaa-57ef44360fb6 | -12.2149 | -44.6057 | 2026-10-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 1acb403d-0778-3339-a061-75f0c04504f5 | -8.9775 | -45.9023 | 2026-10-09 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 536a059c-c4f2-39aa-83b9-a08c09b77d29 | -10.7475 | -46.6184 | 2026-10-09 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 591.9 |
| 787d0dd6-8b9a-3004-b3ce-3ae2ded25d92 | -12.1729 | -44.7983 | 2026-10-09 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 32efcd29-92a2-30eb-a680-f2f9362fafa4 | -10.8909 | -44.8001 | 2026-10-09 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| cde4e39f-2ac2-3da5-96df-f7c449f61f01 | -12.0256 | -43.4371 | 2026-10-09 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 272.1 |
| a0bf2d04-2a92-3294-b042-72d708b1120c | -1.383 | -55.1944 | 2026-10-09 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| b1c0c6b9-dcc9-3821-9e00-28752a5e2d93 | -8.9955 | -45.968 | 2026-10-09 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d9ebc261-5ffe-3f32-b178-1b7bc6528476 | -4.0838 | -44.1159 | 2026-10-09 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 82880da4-1995-3870-a78f-d8a8a88e41b9 | -10.5091 | -47.3179 | 2026-10-09 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 3319ff4e-09d8-3357-8fd6-1209a692be90 | -2.1361 | -54.4671 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b08c3743-9ab7-39b7-a025-01f29c7745c9 | -2.063 | -54.3082 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ced293a3-295f-3645-b1ea-b869d1b76042 | -8.655 | -54.5494 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 17e14c90-e5bd-3c95-840a-6e5750e587a1 | -1.494 | -54.5363 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 7ab8a755-02e6-37c7-82fb-1cc35d956189 | 4.0595 | -60.8985 | 2026-10-09 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8d8aa62c-015f-3797-916a-f427ad044928 | -6.4413 | -55.0224 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c7c05b45-0c5a-3855-97b1-68d2a690d13f | -4.4979 | -43.6083 | 2026-10-09 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ce7dddf0-f2b9-3938-8257-25d2f73b1225 | -10.9388 | -45.3687 | 2026-10-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 36c411a4-e736-37ba-bf33-be33efd830af | -6.7366 | -55.1274 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d2ccfd49-8da2-3763-b4e2-52e1f0870d02 | -6.0609 | -42.608 | 2026-10-09 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 194.1 |
| b1071f86-4c68-3e43-9a3a-95fc997ef10b | 4.2064 | -60.7055 | 2026-10-09 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| fe75de68-40b1-3ded-a0fb-bde0d602b45a | -1.4939 | -54.5563 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b2fdc7e4-d777-3bb3-b428-97af568637e1 | -1.4569 | -54.7761 | 2026-10-09 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cd37aa6d-e4df-33c8-b18a-a9464fed9ad0 | -8.9302 | -45.2041 | 2026-10-09 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 39016a0d-6f4b-3208-a16f-bbe13efe9498 | -1.5123 | -54.5361 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 8765a346-44b6-39ed-8500-8a492fe5ce76 | 4.2067 | -60.6106 | 2026-10-09 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d262bf37-8034-3743-9e22-9564b94b9680 | -8.0766 | -45.6112 | 2026-10-09 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5e91e420-9a16-3751-886f-cad9564e7013 | -6.0423 | -42.5859 | 2026-10-09 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 147.6 |


[Clique aqui para ver as próximas entradas](README246.md)
