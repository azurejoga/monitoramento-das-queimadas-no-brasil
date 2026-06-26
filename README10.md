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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50a796c8-bb41-3e7f-9b2c-6f0eff78f7e2 | -13.73365 | -54.05102 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a07a0074-38f4-3ebb-8742-28c53892dca1 | -11.51429 | -56.13371 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85d02887-c041-3c57-b0e9-44e32884a04e | -13.2602 | -54.43041 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 47c0fd03-4cfc-33a3-b9cd-3d9feedd97e4 | -9.73827 | -47.89517 | 2026-06-26 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99210e16-cc50-3967-8639-9a98c08d1d1e | -10.63434 | -47.04593 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8be343d8-61d5-32ef-b6f6-1a741494455e | -13.25855 | -54.42506 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5a47fb3b-9454-382e-8338-236afe38ec54 | -11.20988 | -54.34276 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc88d191-1395-3663-adc7-2982e5eac56f | -11.51153 | -56.12996 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c86efe05-fc17-3e3f-b8b9-e06bcb7178a7 | -11.21185 | -54.33596 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2e88c24-083f-3310-8a6e-04626d044a77 | -13.25919 | -54.43587 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 44905195-a592-358b-8c6e-28319f7f90b8 | -8.69228 | -49.0935 | 2026-06-26 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe019ccd-cca6-3474-8865-5113e36a936d | -12.62014 | -57.89122 | 2026-06-26 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c196b80-f25c-32e0-9935-a682709ae70e | -13.25748 | -54.43059 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| eed1938a-dbeb-3688-95a3-315a952d88ec | -8.89476 | -47.99995 | 2026-06-26 04:32:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21611a61-55e6-3d55-b090-cb504eb9447f | -11.77536 | -46.44736 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0aa00d1-952b-3019-b14e-fd76d25c3a54 | -10.93978 | -56.8546 | 2026-06-26 04:32:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f48c5141-e801-30d4-a082-4319cfbbc4ee | -9.19907 | -45.32542 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 75ea9acd-7c0c-39db-9b95-05b1713a1c49 | -9.09495 | -47.52913 | 2026-06-26 04:32:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cee3776-5f43-3573-b154-fda532b3e3cb | -13.87133 | -50.39675 | 2026-06-26 04:32:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b842095-c1a5-3438-a2b5-68287a5a3b4d | -10.63492 | -47.04232 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03f6c777-9493-346d-b212-347ff9e7649a | -14.63404 | -54.46651 | 2026-06-26 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55c7685f-ad01-395b-9d0c-642e67683800 | -12.74406 | -44.48384 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91a7056a-e565-3d91-9e24-062ea4ef3e8e | -15.60033 | -48.35196 | 2026-06-26 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5c00846-123d-3750-855b-678a50698fc1 | -13.49502 | -47.87046 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d0ada1a-ed9b-3564-a344-690a63b1711c | -8.85797 | -46.92747 | 2026-06-26 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8be50e7-dd64-3770-8256-9f0bcf49f631 | -13.25535 | -54.42947 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 50a206b0-e1c0-326e-861a-4b7459e122f7 | -13.72992 | -54.045 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 59f1dd06-5ed2-3b78-912c-618c9dce6151 | -12.55091 | -54.59405 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1555e6b-cfed-3745-ab8c-04fca4e52372 | -9.40605 | -50.67327 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f5b0b2a-8ce6-317a-b120-6b76019ebd28 | -14.19197 | -47.68712 | 2026-06-26 04:32:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20fd2fce-e10e-3048-a895-4b992ab3c778 | -14.29095 | -43.82857 | 2026-06-26 04:32:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 958a6aca-4fe7-38ba-8b1e-218c623e9da0 | -11.51079 | -56.13384 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| baa76ec0-fa9d-3287-b42a-1b1d5acff697 | -14.84007 | -48.13053 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a72ac9e-5f2e-3a18-9240-e302d482d73f | -13.87859 | -47.14771 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 212631b7-8017-3500-b75b-5ad7becbd239 | -10.63155 | -47.04178 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe9e0711-17fa-39f6-9277-3c8ea9d9220d | -13.9115 | -47.32584 | 2026-06-26 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d38d2d6a-a315-3c3d-a53c-be0e0b0b0daf | -9.66178 | -50.7105 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb3fb35b-c38e-35ee-bb82-1bbbf5e3afbb | -10.79326 | -49.59183 | 2026-06-26 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52c9724a-30af-358a-99b0-027eb2e30b62 | -11.91463 | -43.78115 | 2026-06-26 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dafd39b2-dac5-3e95-8b9a-53f36ffed963 | -9.80557 | -48.91845 | 2026-06-26 04:32:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ac9c5ac-10ab-3b5c-94dc-2dab9a0622cb | -12.51583 | -48.27464 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ffae4aa-d1a4-3b2b-94b4-b94592335ee0 | -11.19855 | -43.35014 | 2026-06-26 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95f51c4f-a906-3837-b43f-0889730f5cbc | -13.92196 | -47.34598 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca7c0454-f86b-347a-bd86-c5f5f5ebdc3f | -11.51712 | -56.13105 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe90a512-4372-311a-b3f9-4beb66fbedea | -8.73911 | -48.92952 | 2026-06-26 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5552b589-81a4-3978-9912-bb12292d3c0e | -14.84344 | -48.13112 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbfb3e3d-5634-378b-86c0-3ee549c71e85 | -11.21079 | -54.34175 | 2026-06-26 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81f4589b-3429-3ae2-b6f3-b2754428202a | -12.76065 | -44.49032 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c04496cd-f82e-36da-9a4a-36fcf2a1aaa9 | -12.8696 | -44.34355 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8310f3a-b333-3062-b655-5d381049f410 | -13.8427 | -47.1459 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2edbcd8c-fb00-334f-9142-986a93f58ba4 | -12.51737 | -48.28664 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 412e29aa-3e78-3404-a3ff-cec7601b9216 | -9.9117 | -45.52583 | 2026-06-26 04:32:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16ddcba5-fd66-3a71-bdd6-a4fb27bd6825 | -15.6639 | -49.38379 | 2026-06-26 04:32:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8c5fb80-65dc-3946-95c0-e2e85f749878 | -9.80194 | -48.91782 | 2026-06-26 04:32:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4579effc-c25a-3b7f-bd9f-df7ea77493f7 | -10.12899 | -52.11336 | 2026-06-26 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b43985e0-7a75-3ca0-937a-3d2ff25f0519 | -15.60246 | -48.36013 | 2026-06-26 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2cbc79d6-6d82-3daa-b512-9f9cc357b898 | -10.80199 | -48.56289 | 2026-06-26 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8024dc55-989e-33db-96a9-760f34c301c1 | -10.39865 | -56.76512 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3942265a-7a4b-3f89-8b6e-f6f8a698219b | -13.9253 | -47.34653 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a620617-0261-3dfe-b0c0-06956a7b8545 | -9.36991 | -50.54596 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b9489f7-b6a7-3f96-b070-0a851c7d330b | -12.76476 | -59.00674 | 2026-06-26 04:32:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 177f129a-408e-361c-9702-d1a78d43611f | -9.2024 | -45.32595 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31353088-6aba-3232-9873-7fb3857f9938 | -14.87885 | -54.54921 | 2026-06-26 04:32:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ab17f4b-cebb-3133-8416-bfc78c1118eb | -10.17745 | -51.63025 | 2026-06-26 04:32:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470cfc12-38ad-3182-aaf9-dab48ffbcf69 | -10.25984 | -49.61028 | 2026-06-26 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de396e62-dc50-3c08-b609-3c4b379b4b30 | -9.89568 | -57.40189 | 2026-06-26 04:32:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df2a2c0-03e4-3eea-9e2f-e3f90f92987b | -13.72897 | -54.05006 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 15b43c35-d555-3202-bafd-b81274053229 | -12.74635 | -44.49193 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd86d5ab-bf99-3a46-8a69-62f15f62e77d | -13.72616 | -54.03913 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33865334-5044-3e6c-9b6c-63f9b4147b5c | -12.55635 | -54.59442 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bf9736d-7884-3c4c-964e-c50727ddda3a | -12.43913 | -49.58393 | 2026-06-26 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea5d70f-ae4b-36c1-9073-0858cd2b1032 | -14.83395 | -48.12563 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d121966-e9eb-30f4-9fd4-3d9c181e3b3a | -10.79403 | -49.58735 | 2026-06-26 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf61631b-ff22-3f89-8a95-e4735f8888c0 | -13.72522 | -54.04414 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b5256ac7-dd92-398d-a08a-a2413e0283e6 | -14.63406 | -54.46469 | 2026-06-26 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9ffb0fc-f093-3fd2-ae77-84274fbc1aa3 | -14.19256 | -47.68349 | 2026-06-26 04:32:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b521148-bf37-3b1d-9cee-0839937b7a5d | -9.19242 | -45.32436 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 614135bb-4104-332d-a615-8e5703ad99ba | -8.68028 | -47.85642 | 2026-06-26 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d87f898-dec1-33ce-aacc-f8fa26d8f101 | -11.47463 | -47.33987 | 2026-06-26 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32005782-5e8b-3ae0-96d4-d0bbb42f2ec8 | -9.8947 | -57.4068 | 2026-06-26 04:32:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21cfe26e-cca5-3229-bcb7-4ff2fbceb968 | -8.43817 | -51.5615 | 2026-06-26 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 446da4de-1006-3c0b-a09e-f9620721456d | -8.50737 | -50.15594 | 2026-06-26 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a33b167-7f56-3d29-bdfa-39731a1d61d0 | -11.7748 | -46.4509 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88f1eacd-55f7-3301-b980-0b4188ae04d7 | -11.7726 | -46.44329 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2694cc3-fa43-3e81-8407-3b4a3d58ea20 | -13.26823 | -54.42702 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b75ac7c7-a032-37ac-b5ad-e96ac629c4f1 | -13.93037 | -47.33626 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d93a6684-9f1b-3e25-bc27-7309cf4dabc8 | -11.19501 | -43.34962 | 2026-06-26 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c937ce51-6644-3b00-aa79-23dcb480b674 | -10.54226 | -47.71653 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4be956b7-f860-37c9-a8a0-7e83476a171f | -12.43622 | -49.57902 | 2026-06-26 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5b77b66-476c-3b85-9f15-35306e1fecd3 | -9.3659 | -50.54528 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d305396d-ea64-372d-ae96-cfee4262d76b | -8.68856 | -49.09287 | 2026-06-26 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20791b2e-3ef8-34b8-a27a-391265b4630b | -11.91171 | -43.77668 | 2026-06-26 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c24f0400-6192-3a9e-a5e6-7d6f0ed43156 | -10.39951 | -56.76067 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edd7fd56-54bc-3131-bfe0-5c04db5bbf85 | -12.55248 | -54.58759 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04158aa9-a346-379a-b410-13ef6aca12a1 | -12.35837 | -47.42674 | 2026-06-26 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d197154-dc31-361d-97f3-33d66d584797 | -10.12976 | -52.10907 | 2026-06-26 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b959d06-db66-3cc8-8a3e-a1e0eb39fa01 | -10.3629 | -47.34111 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0758016b-e2b3-3a41-a979-ef8b222fb53b | -10.12537 | -52.10828 | 2026-06-26 04:32:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2751e386-65e4-30d0-a209-2ad7c6f3360e | -10.93614 | -56.85555 | 2026-06-26 04:32:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7ac59d6-9d99-34f2-87d9-14d2a962a7d5 | -15.63979 | -46.42965 | 2026-06-26 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
