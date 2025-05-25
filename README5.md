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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2929fac-a12e-3278-ab7b-10878ca2555c | -7.95075 | -44.8659 | 2025-05-25 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37fe8428-14a1-377b-b707-756c68cb9e26 | -7.66234 | -46.10184 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9a912c8-5e7b-3eab-bdf1-9a86a353d993 | -15.60349 | -42.67268 | 2025-05-25 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c24faf4-2363-3faa-8939-64e066be4315 | -15.54397 | -47.16532 | 2025-05-25 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4100b286-91f9-3473-a64c-dd81f02a279a | -19.36463 | -53.21402 | 2025-05-25 03:49:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ced2ce16-3547-3bbc-abfd-1a68c7f3119e | -13.09719 | -52.28893 | 2025-05-25 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53e3777a-303d-3bed-93d2-802337b77277 | -19.95122 | -49.11444 | 2025-05-25 03:49:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d114da8-0b21-318d-a3da-27c5ba29d306 | -23.34001 | -46.77233 | 2025-05-25 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b8ad61ab-f2cc-3de1-921c-a760e858d67c | -20.70753 | -50.06643 | 2025-05-25 03:51:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1c6249d7-661f-3b1c-bd8b-b399f0ce8b06 | -23.58934 | -47.38722 | 2025-05-25 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0504f13b-e8f0-365b-95e1-5562827ef62a | -19.87229 | -54.37365 | 2025-05-25 03:51:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1840de2b-3428-3ff5-afbd-4f0e66a333a9 | -21.2191 | -48.60752 | 2025-05-25 03:51:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b083fbf-bf75-3f71-8ce4-adca51fdb15a | -23.33586 | -46.77142 | 2025-05-25 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 00560012-aff6-32a8-b22e-6d81c3cc7043 | -19.87413 | -54.36615 | 2025-05-25 03:51:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4bbada7-c360-35c8-b795-68a4629aeab5 | -22.96769 | -49.91139 | 2025-05-25 03:51:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0c3dd383-6a38-3cbd-bb5e-6722addc8758 | -24.29002 | -49.94049 | 2025-05-25 03:51:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15ed7472-6563-3acc-954e-1b697183e495 | -22.53815 | -48.81076 | 2025-05-25 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0168bc9-a974-3afc-9a55-ba07119411ec | -20.70675 | -50.07008 | 2025-05-25 03:51:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 46a7e81f-9861-3216-ba98-2c86879f1057 | -20.70367 | -50.0698 | 2025-05-25 03:51:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 25b09c51-bb0c-308f-a10e-74bab01471ad | -21.21785 | -48.61336 | 2025-05-25 03:51:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d6f29cf0-5e3e-3d53-a351-6e40f9fb11e6 | -20.70448 | -50.06612 | 2025-05-25 03:51:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3ea562fd-ec3d-31e4-97c6-bbeab1cb1297 | -22.96838 | -49.90821 | 2025-05-25 03:51:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 060b6c30-7035-39c6-b66c-78cbccc47ec6 | -21.62961 | -49.78081 | 2025-05-25 03:51:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 54a03ae5-8e36-391b-a965-0ef523ed3f39 | -21.21547 | -48.61068 | 2025-05-25 03:51:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3c7c32ee-d745-361e-b700-b2c9bf8c4e50 | -23.40605 | -46.55561 | 2025-05-25 03:51:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b78cbb65-4454-32b4-a678-a54210ed7158 | -7.6574 | -46.1013 | 2025-05-25 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 962c7c81-c348-30d9-90ff-f9c2bcb1e684 | -7.6574 | -46.1013 | 2025-05-25 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5f6cf005-1c5b-32ed-beea-7dfba12ca88a | -7.6574 | -46.1013 | 2025-05-25 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 8a2b34d8-bb87-39e2-a783-dfe212b9bfc3 | -4.29245 | -48.27636 | 2025-05-25 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fd25fb-1718-3bc1-b81d-a6ac164ecea0 | -4.13935 | -48.75661 | 2025-05-25 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb0a90ba-e980-37b5-83a6-edb251e8f9d7 | -7.22262 | -43.11612 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d4700998-2a7d-396f-a9e3-8011e90d9b82 | -7.20445 | -43.12479 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cebf1adf-8eca-331c-8f3f-9f179716127e | -7.48312 | -43.37421 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46639807-7e7f-3c79-a0d7-98429ba43c21 | -7.33897 | -43.31386 | 2025-05-25 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd4b8680-e3c5-3d86-b805-2c053f0a4899 | -7.46872 | -43.38084 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8f8e781-11c1-3e55-b694-b9ccb785baff | -6.95149 | -42.80701 | 2025-05-25 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9ce23474-98eb-3d22-bc2f-72f0c0c69e3b | -5.58213 | -43.45163 | 2025-05-25 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8109416f-5cb3-3c57-92c9-404bb5d9a3eb | -7.20299 | -43.12672 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 412a0eda-62e1-3501-9fc5-9c109a6ce161 | -6.22707 | -43.3537 | 2025-05-25 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9568d828-bf3c-3f71-9fb7-a299ce004700 | -6.96126 | -42.06447 | 2025-05-25 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ee0f64a4-956b-3dc2-937b-08826b3800e1 | -6.83833 | -44.62624 | 2025-05-25 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a15ed6f5-35fb-384c-a188-8864ad558a38 | -5.61093 | -45.33477 | 2025-05-25 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37b20398-ca7d-3a92-b890-0a16abd35d67 | -5.58426 | -45.20133 | 2025-05-25 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8854adf1-8dbf-37f2-acea-2ec35662b8c4 | -7.22707 | -43.11683 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b158e119-f809-3c4a-9964-f087ab8f4b6b | -7.49204 | -43.37753 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a03164c-823b-30f1-a683-64a45e69ff93 | -6.84283 | -44.6234 | 2025-05-25 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d70a669-fb99-32ad-b7bc-5c9e5ed1e4f2 | -7.2125 | -43.12363 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 641eaede-d52e-30b1-95d1-146013dbd9bf | -7.4731 | -43.3815 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b55049e9-0410-3c10-b328-feb8fa9117cb | -5.58156 | -43.45558 | 2025-05-25 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adffdeee-176f-39eb-adb3-e7eea4d3381b | -1.33671 | -48.35528 | 2025-05-25 04:38:00 | NOAA-21 | ANANINDEUA | PARÁ | Brasil | 1500800 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5d9e3f0-3f88-3856-b9cd-f7f2fd743245 | -4.29299 | -48.27289 | 2025-05-25 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ae42752-07b3-391d-8a49-3d4a6d4d0bec | -7.20889 | -43.12546 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 13d90a69-2ee3-315c-8289-4f0090853ec8 | -6.83783 | -44.62965 | 2025-05-25 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 61787f45-e8b6-3ca2-89a4-808666c40bc0 | -6.95602 | -42.80767 | 2025-05-25 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 829d968b-a102-3346-b306-f58f84ba245e | -6.83884 | -44.6228 | 2025-05-25 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f24a196d-d393-3c78-80bf-e4e315a02742 | -7.51143 | -43.36697 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460cbc4b-ba30-3e4b-9909-7a80944ddbb5 | -4.28968 | -48.27238 | 2025-05-25 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 09f46d8d-b931-33b4-9bfc-08878134905b | -7.52111 | -43.17414 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d2334c1-d8af-3e0e-983d-ac3a713b2a90 | -7.4781 | -43.37787 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1a1b999-c2a9-3ab4-a12e-b81314f3c47a | -7.34455 | -43.46266 | 2025-05-25 04:38:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f2daf80-d074-3016-83cf-8c277b221151 | -5.68403 | -44.12277 | 2025-05-25 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c27262f3-fc61-3b65-8df4-c8a6b21cc40f | -7.4875 | -43.37492 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b488ada6-7107-3522-9adf-2284a65440d5 | -5.44092 | -46.28792 | 2025-05-25 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77d830b5-4972-3dd9-bfa0-92863bdb2621 | -7.48327 | -43.37614 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63ee68bb-6c71-3937-a643-fa44f335e814 | -6.55742 | -44.49533 | 2025-05-25 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd69db5d-517d-3245-8a99-1fe53a3278ec | -5.32351 | -55.94414 | 2025-05-25 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c33cb6b3-1b99-3aed-bcc2-3a4af6cde7cf | -7.20744 | -43.1274 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4b6047a1-6759-39d2-be0f-9f5cf6b16c26 | -4.28914 | -48.27584 | 2025-05-25 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ea6753f-14df-3afe-9ec7-fe0c3dd548ad | -7.52479 | -43.17194 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e21e0873-43ca-36ca-adac-a2ed442e2088 | -5.44026 | -46.28641 | 2025-05-25 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0599fa7d-55fa-3f48-9af6-7bf718bfed5d | -5.60717 | -45.33421 | 2025-05-25 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe5e146b-a97c-3b57-8cb3-bf9b6a22a1f6 | -7.21311 | -43.11919 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 55d3249a-2adb-3d49-acc5-7439dbd75f79 | -7.34394 | -43.46687 | 2025-05-25 04:38:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e345277f-c4fe-36ad-af17-05b2828e4cc5 | -3.27548 | -43.53952 | 2025-05-25 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dea2de36-0e7a-3e15-9017-8e5213878085 | -5.58497 | -45.19668 | 2025-05-25 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8e99851-2823-36f7-965a-2b6793bc658d | -6.84233 | -44.62683 | 2025-05-25 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 250447e8-e975-3e42-bb56-3570ca7b1ad9 | -7.2038 | -43.12921 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1956b507-aa84-34ac-8c6f-0bc99a02e7df | -7.21695 | -43.12431 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4230077b-c564-3a10-b4f5-ab9dfe43ec8b | -6.22647 | -43.35787 | 2025-05-25 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcfe8d38-61c5-388e-87e3-11fdfc518663 | -6.58051 | -43.69324 | 2025-05-25 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d6739b1-1966-3b84-8b69-65020fec26cb | -7.52024 | -43.36813 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06abe3de-87ad-3910-add8-947a7e212837 | -7.20954 | -43.12103 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3ddbb665-8615-320a-836a-197a6afe162a | -7.48765 | -43.37684 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4acc2666-3297-34e0-afc5-59dddce515f0 | -6.55897 | -44.48489 | 2025-05-25 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7e82399-62cc-322d-9490-c48e3295ba13 | -4.30833 | -47.55792 | 2025-05-25 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b31a12f-934d-3f38-badc-4f74c4d2a235 | -5.54945 | -45.2008 | 2025-05-25 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5f00049-2b41-30cb-b06c-1eec99c08e95 | -7.20805 | -43.12295 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b9f2126a-99cb-348b-940e-bdc47b28a153 | -6.55794 | -44.49186 | 2025-05-25 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 250d6d30-41f9-3cfe-b12d-1011d6b9623b | -7.23152 | -43.11753 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7107b0b-f47d-3a42-919a-f762c69cda2a | -6.55845 | -44.48842 | 2025-05-25 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b4250c4-ad69-30a4-b8ee-ac9131da177a | -5.68351 | -44.1264 | 2025-05-25 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c520852e-6cc9-3937-8565-fa0913e98e2b | -7.22645 | -43.12126 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4e00ea2d-913c-362b-8190-803360a19fd5 | -5.579 | -43.59135 | 2025-05-25 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff0195f7-4e6d-3fa6-ba36-bec512728a1b | -4.81861 | -43.22784 | 2025-05-25 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 664d6acc-0aa2-3ec0-86ab-783bf8c14908 | -5.12355 | -56.1188 | 2025-05-25 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c573326-d066-35e8-b983-fad101e6b8a4 | -7.28056 | -43.25029 | 2025-05-25 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dd7dff2-e1e1-39a7-a2d0-952ade2aa74b | -7.39416 | -45.9268 | 2025-05-25 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53d9e6e5-e22b-34b3-8904-8ef834a76963 | -7.23214 | -43.11309 | 2025-05-25 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c48e843f-c5f5-3e2a-96d2-68ca0005d75b | -7.51644 | -43.36322 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f719f4b4-b4a0-320a-8732-765211aae15f | -7.52556 | -43.17483 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
