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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c77961c4-be8b-3494-9c1b-88f603e36e67 | -5.1965 | -45.0768 | 2025-10-04 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| cad21f8b-cb3c-3be8-82e2-0735ed8f20e7 | -4.4258 | -43.2408 | 2025-10-04 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 2f13d5cf-0d8d-3d13-81c6-634a7afd324b | -9.9396 | -50.2304 | 2025-10-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e64197e2-c2fb-3d25-b305-136d8b112364 | -15.7297 | -46.2707 | 2025-10-04 00:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 112.6 |
| f48557a5-876d-3ca2-b111-91f1ea1b85bf | -16.0212 | -50.9425 | 2025-10-04 00:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 2c8d45c2-7a00-3514-9630-7d713c835366 | -11.8959 | -46.3526 | 2025-10-04 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| c59a08c3-324c-32f7-bdf2-35821500d753 | -8.2316 | -46.8066 | 2025-10-04 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ba616fab-99a0-3486-9258-aaf55554d566 | -9.9396 | -50.2304 | 2025-10-04 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7ec72245-83fc-357e-b847-0617b60f1f1f | -8.6138 | -54.976 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e5edb389-bc50-3033-8f96-8b50bdc1ec44 | -12.3813 | -54.4603 | 2025-10-04 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 324ca4d1-a52b-3e94-9e38-4299cfc0dfe1 | -13.9766 | -48.2016 | 2025-10-04 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1a3cbb05-72fe-3e2f-b276-8ef30839c323 | -17.0903 | -46.2347 | 2025-10-04 00:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 132.1 |
| da4f398e-3984-3abe-a8c3-64d0f98225fc | -6.8865 | -44.4923 | 2025-10-04 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| da36afea-10b3-3ca8-bd6f-d98b4f1547d6 | -15.6019 | -52.4888 | 2025-10-04 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 5ed25acf-2fa0-320c-b950-15719b8aff40 | -13.996 | -48.1987 | 2025-10-04 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 152.9 |
| d63e93ee-c80c-344a-aa0e-24797b7e7e42 | -8.6324 | -54.9747 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 1eb6e8b9-60fe-3a03-bef7-59138dd2a36c | -11.9151 | -46.3499 | 2025-10-04 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |
| bd9dac3d-c7eb-378c-9196-d199c76095f4 | -9.3276 | -54.5215 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| da4b83cb-361f-3c11-b1ad-e16c5aff51b3 | -3.8572 | -41.5719 | 2025-10-04 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 7e76518d-96d7-30be-ad10-5532c936313a | -4.9541 | -45.0468 | 2025-10-04 00:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 02e50f83-d50c-3039-8e1c-2bbe0ad08fea | -5.1967 | -45.0541 | 2025-10-04 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a2519be3-636d-33b7-837e-01375fd78696 | -4.4258 | -43.2408 | 2025-10-04 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| af80d741-00cf-38c5-81b1-1f9bba9affbd | -6.8774 | -47.2334 | 2025-10-04 00:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5a889946-194c-301f-b744-ade38fa6b37e | -4.3197 | -48.0908 | 2025-10-04 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e2bc7107-84b2-3435-9a11-17abbd5e9a27 | -15.7292 | -46.2939 | 2025-10-04 00:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b5c91efe-54a6-3e7c-9220-8845ce8a3172 | -17.0855 | -43.3564 | 2025-10-04 00:20:00 | GOES-19 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5fdd6858-c018-3888-b4cd-e55ee4a70f04 | -14.2321 | -46.0794 | 2025-10-04 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 08fef1b8-fc66-3977-970d-0dc447ce1523 | -4.4632 | -43.2386 | 2025-10-04 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 78dbf836-1f9e-3040-b2cd-155df797f875 | -13.9965 | -48.1763 | 2025-10-04 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 362f2aa2-218c-3b42-8cb4-72ada32ad749 | -4.4446 | -43.2164 | 2025-10-04 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2112d1c8-9924-34f6-bb54-5d0a69d7d0fa | -13.3229 | -48.0993 | 2025-10-04 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 70507d90-9a83-3015-9565-e0ff2791246d | -13.3221 | -48.1439 | 2025-10-04 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 403dec05-5111-3ce6-bebe-26b0e310e960 | -2.9013 | -50.7351 | 2025-10-04 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 06251433-a646-3f99-865f-6f0a1cb3d1d9 | -13.3225 | -48.1216 | 2025-10-04 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 140.4 |
| a86aea14-6ab9-3dd1-bf18-ae4b418a1640 | -19.5838 | -48.0212 | 2025-10-04 00:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 11370f61-d5c2-34fc-9edd-603e3c671d8f | -4.4443 | -43.263 | 2025-10-04 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| be77e208-547d-38b7-9071-1ed1b927bc97 | -5.1965 | -45.0768 | 2025-10-04 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f607078f-88a7-3dbe-8d28-9fd1477c67c4 | -11.9147 | -46.3726 | 2025-10-04 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 8c21e308-c9db-3d37-a06c-2932b7e9a549 | -9.3274 | -54.5418 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 3b3ebdf0-66e8-31af-8547-81ac71e31306 | -9.3464 | -54.5201 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| ef949d6e-418c-3af3-af38-6a8e0d9ca3b5 | -4.9538 | -45.0921 | 2025-10-04 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1696cc6d-d0d9-332d-b8f6-5e5592fd7249 | -15.6023 | -52.4675 | 2025-10-04 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1e270997-ff0c-3954-81d6-f92888ad2647 | -17.0897 | -46.2581 | 2025-10-04 00:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1b0770ba-7e1f-3ddc-b34f-f125cbe2f9b0 | -11.9155 | -46.3272 | 2025-10-04 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d42c4bdb-61eb-38d4-9851-bad535841894 | -11.8963 | -46.3299 | 2025-10-04 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 3965565a-3846-31cd-8960-774ffcd2a9bd | -8.6322 | -54.9949 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 55684d96-7875-30c4-a168-392e45b7eea4 | -4.954 | -45.0694 | 2025-10-04 00:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 190.9 |
| a41f53ef-c177-33ee-a10a-7ef33d0b333c | -16.0408 | -50.9395 | 2025-10-04 00:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 319a0c58-8873-3935-9613-4f8a723317a3 | -3.8384 | -41.5729 | 2025-10-04 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 54202cf2-0eb7-3616-9004-421e471199e2 | -4.9726 | -45.0683 | 2025-10-04 00:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1bb2f01a-d216-3d13-93ad-00e5f3da8582 | -9.3462 | -54.5404 | 2025-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ef5a30e1-faad-3c42-a68e-156824e3621d | -4.4445 | -43.2397 | 2025-10-04 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 432.3 |
| d712d06c-b3fa-3655-9e59-e4f72b8842ec | -11.9151 | -46.3499 | 2025-10-04 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 8447ebd3-8943-3f69-a462-96c51a40e7cd | -11.8959 | -46.3526 | 2025-10-04 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| a99591cc-cbba-3bef-ac99-63722c8d9cca | -5.4849 | -44.0982 | 2025-10-04 00:30:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4d35cfcb-7b42-341f-9835-3fb9bab9e8b2 | -11.9343 | -46.3472 | 2025-10-04 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b8c23259-ad1b-39c3-9427-0afa0e20951c | -8.5956 | -44.8062 | 2025-10-04 00:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9b92a457-d501-3461-9c54-5c274a7406af | -9.3274 | -54.5418 | 2025-10-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d2ea38c9-1cac-3043-8b5e-08f1f73fccbe | -13.9965 | -48.1763 | 2025-10-04 00:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a67ac5ff-247a-361b-a640-fac8e47e3a00 | -17.0903 | -46.2347 | 2025-10-04 00:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 741520f5-4c8d-39a6-91c1-288198af5e5d | -6.0621 | -42.4897 | 2025-10-04 00:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 2940a7dd-d323-3887-84bd-90f8bc6a6a23 | -4.4443 | -43.263 | 2025-10-04 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 00223f04-a856-330b-babf-a5e68a1fa7bb | -4.4258 | -43.2408 | 2025-10-04 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 325b8f61-cdfb-34f8-9847-5052baa10785 | -6.0618 | -42.5133 | 2025-10-04 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 207.6 |
| 96ff6625-cb8c-3da4-b456-8e6f2f1971d8 | -3.8572 | -41.5719 | 2025-10-04 00:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| c9a8ccc4-3186-336c-bff3-b62c5ed68b54 | -4.954 | -45.0694 | 2025-10-04 00:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 74e0f6b3-df6c-377b-ad5e-62690474b29d | -4.4446 | -43.2164 | 2025-10-04 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 79303a53-6b6b-3859-b53f-ca35629da612 | -8.2316 | -46.8066 | 2025-10-04 00:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2b06a30d-9b4a-3ddf-b7f2-734290c9663b | -14.2321 | -46.0794 | 2025-10-04 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 943b2b67-652e-309a-aa70-06675bebe7ac | -7.3357 | -41.4358 | 2025-10-04 00:30:00 | GOES-19 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| f4eafe37-3e9d-3d18-8ef5-eb7fb7cc12f3 | -10.2206 | -50.373 | 2025-10-04 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d9033768-38c8-30aa-ac72-e6425b35632d | -13.3225 | -48.1216 | 2025-10-04 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| eea47f46-2590-3b5b-9887-d32e9604fbf8 | -17.0897 | -46.2581 | 2025-10-04 00:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4b4b28d2-64dd-3f5a-b4df-ff03665abfef | -5.1967 | -45.0541 | 2025-10-04 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fbc1a7d3-7a90-32bf-ad36-b327cd677d27 | -6.043 | -42.5149 | 2025-10-04 00:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 491c0ae4-5aab-303b-a622-b3ad069ff89e | -15.6019 | -52.4888 | 2025-10-04 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c33d2970-dfbf-3981-854f-b0d1aa6b3a3b | -3.8384 | -41.5729 | 2025-10-04 00:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| fab1735b-6a3c-3262-aaa0-44ffbe0a8356 | -11.9147 | -46.3726 | 2025-10-04 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| cc32802c-8152-3f1e-8d95-65d1967044d5 | -6.8774 | -47.2334 | 2025-10-04 00:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f455ed54-d443-36af-a029-49c3b11ad2c6 | -16.0212 | -50.9425 | 2025-10-04 00:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1398eeff-35bc-369d-8f24-f05d9f1226bf | -12.3813 | -54.4603 | 2025-10-04 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a12e6380-b548-3758-b58a-68eee2fcd7b6 | -14.9347 | -46.8736 | 2025-10-04 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c98340ed-0758-3489-af5b-0c1621ddfbdc | -2.9013 | -50.7351 | 2025-10-04 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 194231e3-f266-39a3-9991-5a74115bd671 | -4.9541 | -45.0468 | 2025-10-04 00:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ab2e961e-ec28-325a-bceb-c59912a74f5a | -9.3276 | -54.5215 | 2025-10-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 19e92739-8025-32ae-8749-c9be9e921b13 | -9.3464 | -54.5201 | 2025-10-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 70ac9699-1c7e-3b37-8573-5526f73b87b4 | -6.8865 | -44.4923 | 2025-10-04 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 48862eea-ecd0-37bd-bf1a-8ae6f124721d | -8.6138 | -54.976 | 2025-10-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 09ae9eba-7dc9-3828-ba84-73975f3fc4b5 | -5.1965 | -45.0768 | 2025-10-04 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 92523780-a238-3eac-84b9-7330fcff6fb2 | -13.3221 | -48.1439 | 2025-10-04 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 980bc840-7368-319e-8fc5-22b15645a50a | -10.2209 | -50.3517 | 2025-10-04 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 95167f99-cb6b-3146-b29f-29187ed3bd0d | -4.4445 | -43.2397 | 2025-10-04 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| f39b5f3e-e4e9-3fcf-b76d-a4d47c9024ef | -8.6322 | -54.9949 | 2025-10-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| c5ea1f34-509a-3127-b2bb-c8c08162e42a | -4.3197 | -48.0908 | 2025-10-04 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 21804a82-0223-3022-8a7a-4dcb48234546 | -8.632 | -55.015 | 2025-10-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 772905cb-368c-357a-af52-b0146fbbb8d9 | -4.4632 | -43.2386 | 2025-10-04 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 5fbaeca2-4a3b-395a-bbb1-379b9f39a0ff | -4.9726 | -45.0683 | 2025-10-04 00:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c69eb2d2-50fe-3d92-b78e-d0d670a95a34 | -11.8963 | -46.3299 | 2025-10-04 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 399d3e20-cf34-32f2-b5e1-19c311f8d5d4 | -13.996 | -48.1987 | 2025-10-04 00:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| e9d5a29b-dec8-31a0-aad8-1bd82694a242 | -15.7297 | -46.2707 | 2025-10-04 00:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 84.8 |


[Clique aqui para ver as próximas entradas](README3.md)
