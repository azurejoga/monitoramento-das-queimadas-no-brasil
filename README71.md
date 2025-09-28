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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb452636-529d-3255-82da-05eaa1b0676d | -9.06586 | -45.53987 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de10de1f-bb37-33b5-af31-3739c160ae8b | -10.94833 | -47.78122 | 2025-09-28 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 440fcf68-315d-3e57-b9c4-02f75fae130e | -6.14131 | -45.72453 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da393fcf-c363-34f0-a379-8d817ef55ba5 | -7.33872 | -45.49368 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13704448-fcc9-3a2a-8c45-cb6ae4d6544e | -6.78688 | -44.08089 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7547af7a-dfaa-31fd-a161-9ae796a5bce2 | -6.06875 | -42.44093 | 2025-09-28 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a6a70cc1-71b1-3a79-8485-a7a0d232659a | -6.07481 | -42.45095 | 2025-09-28 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aa93b743-67a4-3d5f-9ae9-037963cf5b04 | -7.58202 | -42.33046 | 2025-09-28 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25ee3909-3c17-358a-9b24-e5692936fc5b | -10.90635 | -45.75208 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0306df2a-b05b-3e55-a174-82ccf8f15660 | -6.11531 | -43.19789 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 202e4558-b4a3-3bbc-b78f-8e8acdaab0a7 | -11.435 | -44.9222 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73a6b432-ff7f-32d8-b650-8be6b0f27c4e | -8.91468 | -46.09667 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68fbc963-153b-3c2f-868e-926300956cc4 | -6.23863 | -44.48229 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52154deb-54d3-3f54-be0c-455f9b5829fb | -6.69583 | -44.60406 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a457409c-d6b1-37ec-a0f9-968a73b4890a | -8.67037 | -43.98809 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68e16a43-5797-3038-8861-bf6a3d21289b | -11.4326 | -44.96195 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c58a7b08-27e1-3350-b9ea-8356511d3e40 | -4.8612 | -49.47144 | 2025-09-28 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e05546e-8a0e-32da-b1c6-605480a8e037 | -11.94789 | -47.92675 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 836fc539-0ce4-3670-a3c7-61534b7c807c | -7.53891 | -46.10136 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a5f4270-6101-37c5-87e5-81cef4a8b496 | -11.94233 | -47.94033 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7e2f0ed-ba6f-3abb-970b-36062d1d098a | -11.8442 | -48.25492 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 894be0e5-7106-3197-b8b3-07cc5ebda2ee | -9.67755 | -44.51937 | 2025-09-28 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e38dd2e9-3f2c-3529-92e1-bcc37f1bb5e3 | -9.04513 | -45.51825 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c11e0923-b731-350d-b031-eb5d67fe8d6f | -8.15749 | -47.6407 | 2025-09-28 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b18da95-05d4-3fdb-8882-22a2b55ee6ec | -7.74883 | -47.00961 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b02d1d6-0fd6-38c0-95d3-f9d23fb142f9 | -12.69382 | -46.87568 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13f00221-c94e-3acd-b2e6-7b87fd77c347 | -6.7009 | -44.57121 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d80de28a-489d-32cd-a354-04846bd089a3 | -11.95402 | -47.90966 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85e82cfc-b088-3237-b25f-b69ccb95ea2f | -6.15616 | -42.80095 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45661f15-fe32-3858-b4bc-9cae6d53dd62 | -7.17105 | -45.49966 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a678156e-c18b-3d0e-b9ec-f85ee14189d8 | -9.4131 | -54.69542 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53f49135-a461-3cea-bd18-301a09a12a9b | -6.09389 | -49.40093 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b94eeb11-f5f2-36da-a083-93e0aab8bf67 | -11.578 | -49.76556 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f71a159-9e7b-37f9-843a-d2376ffd4b45 | -7.15531 | -48.92601 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bafa2aa4-536b-38da-b9ab-9ae3c0faf724 | -12.69438 | -46.87207 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4afa82ef-0dd5-3d32-aa32-44d89bccb4ee | -5.47825 | -45.38253 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94bec3ae-62b4-3a53-9494-fb24004b55b7 | -11.58455 | -45.48462 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4590ae2-ee5d-3be7-974e-f4c872a9d15e | -6.12628 | -41.80026 | 2025-09-28 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6be8871-61db-36d6-9244-d61e876d995b | -12.69101 | -45.47458 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1fe2ca10-507e-38ac-885d-166f29fb1590 | -12.68605 | -46.88177 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 201919c1-bd1a-33b9-82a1-297f6acb4d9e | -5.45477 | -45.29338 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ac1ead6-6856-3a07-9ead-eff63d85801e | -6.47822 | -44.24289 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dde7e4b-7608-3fd2-81fe-fb8d267e492a | -6.6955 | -42.74366 | 2025-09-28 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 09e660b1-7977-3d2b-b267-b262a5b631f0 | -6.43352 | -43.93916 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 952efbed-d452-3b0a-8f0e-998670cfc1b5 | -5.9051 | -42.9476 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c0cd1e9f-7a8f-375e-9ec6-477648756e3b | -7.74938 | -47.00613 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1a5d5ec-c6c5-32a0-9d44-b090ab7e5a8e | -6.24487 | -44.4869 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e029558-3fd4-34ff-8841-c0354b636ea9 | -10.0058 | -45.39741 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2610648f-8a26-308e-8773-a4e2d1d4dbd8 | -11.94514 | -47.92268 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd818bbf-dc03-351a-8cb6-f150942f3dc5 | -8.20714 | -44.40271 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e37dfa6-3936-3b44-acc1-4b1d2c46d345 | -12.41315 | -49.36881 | 2025-09-28 04:25:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df859d5b-9ee4-3236-878b-909a74887899 | -6.40697 | -43.95877 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57b744cf-e5ad-363c-a86f-33fb67593c0a | -11.38835 | -46.97479 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 824a602b-afcb-3484-a780-5038a7a3391b | -9.04501 | -46.71765 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d17e1b-c22c-3c85-a021-089570167ef1 | -8.49128 | -44.72287 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0971dcf5-8422-383f-9a47-dcec4a2f3182 | -6.47842 | -44.24344 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa261cb9-0d68-3847-8ce7-b822ff6b8cfa | -8.5424 | -48.25227 | 2025-09-28 04:25:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88cabd0c-c919-3cb8-8b64-64b6ee69d3f2 | -6.12899 | -47.0485 | 2025-09-28 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df674ed-2f05-3639-9acb-4d5774f1bd7d | -7.80227 | -47.01455 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd0f887d-8954-3a4d-90cc-de6bb6353c6b | -10.16936 | -49.37731 | 2025-09-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e4b01fb-8e07-3f4e-8a6b-253f37a71b2e | -6.95646 | -45.3947 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74ae6657-31ec-314b-bebb-409a0bc2f305 | -6.15093 | -42.78389 | 2025-09-28 04:25:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a07dfe82-d8b2-3f18-ace2-7f1290eda012 | -11.98334 | -47.89636 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad93b428-c590-3acf-ac72-a59ae6ca5f38 | -6.7863 | -44.08471 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 14e19399-d224-3344-98da-0b9a3e9b363e | -11.14893 | -54.31003 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a47f18cf-b6dc-350d-a960-5a0f8af9318e | -5.81133 | -47.81374 | 2025-09-28 04:25:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a142abcc-2fe4-3258-98e5-4aa0cf923fc7 | -7.03276 | -45.18932 | 2025-09-28 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec7c0b04-d799-3e19-8ceb-96d29defa7da | -7.74828 | -47.0131 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af6cdbb4-3032-31ac-b6e1-25ff4771be02 | -11.99109 | -47.89036 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 75817209-72ec-36b0-ba34-2753caeb2062 | -9.28714 | -45.71276 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 487763ef-934b-3d9d-9159-4cc8b295e4bd | -11.33741 | -45.03966 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fd9ebc9-07f6-31a3-baf6-7f4d09b57eb0 | -6.99293 | -42.80132 | 2025-09-28 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 075caba5-bf1d-3cd5-867f-b0cd0e66105b | -11.50746 | -46.9506 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cf3b53b-ddef-3f75-928e-0910a5c911b5 | -6.44257 | -45.90353 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b8c4438-febc-3951-9fe2-35375cc0873a | -12.69495 | -46.86847 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c1bab0a-1cdb-3abf-88c0-1cbda59470d7 | -12.10132 | -44.31517 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c0343a6-b900-3d38-91ae-879e55b562a8 | -7.77314 | -47.02781 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a0e488a-8f2a-37af-add6-1027bc3e5c31 | -9.31262 | -45.67271 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 749ecbb5-0405-3dfe-95db-8c6690c82551 | -12.00949 | -47.96564 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35c75d08-0377-3d5b-b06a-8dc3cf0b57b3 | -7.74938 | -46.98471 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e8ce7b5-5f78-3ce0-a3ca-8e693bb2b4b6 | -5.90312 | -43.28771 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18efa0f7-9a2e-312b-957d-a3533d3ad5d7 | -6.01575 | -46.4551 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16241e9c-3aff-3777-af46-d858b34dface | -11.95846 | -47.90315 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e10e2c5c-944d-37e9-a3ea-7b2f80b3d674 | -11.09659 | -44.82058 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7fe03ab-0493-3fd7-96ab-e9a2d677049d | -8.27276 | -45.46424 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4120265c-ca93-3ce0-a3cb-cb9973f3cb03 | -7.58381 | -44.95829 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9402b50-10f0-3898-b24c-1a6963907756 | -11.44415 | -44.97975 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfd1948f-9c64-325f-8543-8c4638fb79c7 | -11.78976 | -44.86875 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eca9de0-2c9a-3bea-bd93-5fb5e5f2d4f7 | -11.98562 | -46.60239 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a6674d2-450c-3b52-9b8f-ed6c7d1aac2d | -5.91189 | -42.92746 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f318d8b3-4534-372a-9bea-0ce4f4a6b740 | -6.76591 | -41.75529 | 2025-09-28 04:25:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3fad41bc-153e-3077-999e-920a19a4ff6a | -7.37093 | -47.03503 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77aa1b4b-fffe-3974-9458-945208d7f7c7 | -10.28718 | -45.20219 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa87846a-eea3-35c9-960f-41171863facd | -8.29281 | -45.44547 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462c68ea-8b42-31b1-bce4-0de9a569b0b7 | -12.90328 | -45.15492 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 546ee508-1527-366c-91f8-c1e9d7939db4 | -9.6074 | -46.68237 | 2025-09-28 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a0d810e-da26-3da0-b3ba-ae06a1be0194 | -7.70625 | -47.67793 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ef90636-fdcf-30f4-8d1c-a9ee748bb944 | -8.93571 | -47.30009 | 2025-09-28 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77f538b3-9ae7-3b4c-a079-c302529f7fe4 | -10.58517 | -46.2691 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b0fafb2-d010-362e-bbb5-38b034300c86 | -8.9324 | -47.29984 | 2025-09-28 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README72.md)
