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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42de211e-c22e-3913-ba29-ce6b39299956 | -12.68911 | -48.15535 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b68fdce5-d01a-35db-8fd5-e6733261961b | -11.56552 | -46.37904 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d117b3de-bc48-3dc6-965d-d2031a6d8fcc | -6.04295 | -44.47657 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dac17558-b92d-3e24-a4c8-696c123fd6dd | -13.19859 | -45.2848 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 183039b6-fc46-3c62-9198-3b7fc4453405 | -6.49295 | -43.52982 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a67b921-b856-334d-8300-3e155e95d957 | -9.96313 | -46.50102 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7881d236-d1ce-3d42-be2c-d8da652326ea | -11.56237 | -46.37348 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a685cf8-0b9d-34a1-96d4-2ea839a5fe50 | -10.67085 | -47.09297 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e97cde8c-521a-3efc-a05d-7aab05789b8e | -9.46017 | -60.57116 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 485b18ab-3e43-38a9-bfd4-3fd2cf06adb6 | -12.45256 | -47.99667 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1044f499-6b5b-3eca-98f3-c9c8da8b9a69 | -9.46804 | -60.30966 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62a7aad9-3c0f-357c-8845-43d7b40d7de7 | -12.86647 | -48.10044 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00647f62-95ca-3b9d-bd71-0f3e408d80c4 | -11.1665 | -47.15319 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f325921-7235-3cb7-9607-27caa40a5d65 | -7.45829 | -61.39814 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31f2903a-ea00-3e1d-bd50-fbd13ba189bc | -12.0677 | -46.62483 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12b18aa5-795a-3515-bafb-d5eefbb3b1c0 | -6.5397 | -43.10577 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46437793-c359-31db-9eed-484da5b8863e | -9.41907 | -60.57135 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21c7feff-e1c2-37c7-b2e8-d04331443d94 | -6.37589 | -44.32987 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31b8f19a-c985-3ccd-af24-a3887952db03 | -9.5982 | -40.35674 | 2025-08-29 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 6aaa46f9-e233-3310-acb2-25aa818ca16c | -4.41277 | -54.86223 | 2025-08-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf7af73-704a-30a6-ae7d-4be7353dbb10 | -11.58565 | -46.376 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf89cc14-25a1-34b7-a3fe-db51a3f35175 | -6.49015 | -43.53496 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0663cec1-82f0-38e7-9f85-00eab7e42c96 | -7.41488 | -42.05936 | 2025-08-29 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b032c73-a81f-33c3-9afb-9354351f6a37 | -12.91985 | -46.34429 | 2025-08-29 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68d8186d-4d1f-3f8b-826d-aabb6ace063a | -7.07704 | -44.2854 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa575553-a967-38eb-b7f1-2309354c4765 | -11.90347 | -46.7193 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3537a158-b9bf-3d02-b058-9ff6b64d0743 | -7.16585 | -44.15052 | 2025-08-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f97ff7cb-73d6-3fce-b548-d32dcef44907 | -8.1002 | -45.00475 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95da6236-a0c4-3e39-b54d-97e1735307a4 | -11.48732 | -48.55045 | 2025-08-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d58f0267-670b-3098-8432-a6a8212b071a | -11.55677 | -46.3573 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7daf427-1a47-387f-b107-e7421a820cff | -12.70447 | -48.19945 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 09b3309e-df90-3b13-b931-33deac7023af | -6.45034 | -44.55936 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc5e6c22-e86f-33d1-b863-396b599ff1f1 | -7.0732 | -44.83514 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 675402e7-342b-3cb3-9b5e-114898c9b189 | -8.69357 | -50.3838 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b0d2b99-d712-3ae0-8c26-81a9aeaad547 | -7.41091 | -44.06549 | 2025-08-29 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 751f4e49-9e2f-3573-977d-8ab6165300c6 | -11.27032 | -45.4925 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61428b91-f9aa-318e-a0b1-491d9c37a049 | -9.32104 | -56.90468 | 2025-08-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8626a60b-829e-3d86-bfff-9e141e219460 | -12.82211 | -48.13688 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f018673-3338-3cf7-a41a-052b8d74a4d6 | -10.8318 | -49.53109 | 2025-08-29 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d2d58f6-f04d-3bba-8c4f-4bbbe51681ea | -11.70577 | -47.73684 | 2025-08-29 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ec0b20d-0b98-36fa-8681-2f901deaf3f5 | -6.70727 | -49.47201 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 30b30446-a889-315b-982e-5d1ce8482def | -11.25136 | -45.00779 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35586a8d-b04d-349c-90e6-eba38b93e0a8 | -9.93668 | -46.35864 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d325ac5a-eeaa-3931-a3ac-77f8958899da | -10.98461 | -46.85329 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 161c41fa-4744-33b0-984c-fa68433ad3bf | -7.1074 | -44.59473 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d2d1715-8dae-355a-b168-454f2f61093c | -12.69497 | -48.19004 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| fe4fcaad-586d-3938-9b9d-ff6a753b29a4 | -7.40305 | -43.38349 | 2025-08-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ca45653-d1b0-3fc2-92db-5bbd0c298378 | -6.14906 | -44.43384 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf33280d-54bf-3e14-adbe-71ae196ccda6 | -10.68372 | -47.08167 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ca4f772-f1ad-3330-b501-5c6ba11cc0b0 | -11.15741 | -54.30774 | 2025-08-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecaa2d6f-d2cb-35e8-8c4c-c13db2bacb21 | -7.73857 | -50.26991 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2feea547-876b-3e8c-b9a1-b5a41c2f2a8f | -12.86364 | -48.14591 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4331ecb6-716c-3f73-989e-12ebdac9c427 | -7.68115 | -44.99338 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8583e0ab-4c64-3ba9-bb4a-ee1d6cc81150 | -9.43078 | -47.63783 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c5913b2e-4ba1-3d2a-9b7c-f3c6e92f9842 | -6.54611 | -43.91928 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fe335161-c25f-33d4-855d-0b7007e664eb | -12.91175 | -48.14042 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebfb1188-a611-302e-93ce-220411a8147b | -9.68939 | -47.05762 | 2025-08-29 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4aca428-dda7-3d37-b566-d18830227a08 | -10.85768 | -44.79854 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6604409f-8205-30dd-8d55-6505a6556ec8 | -9.45769 | -60.56585 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01623588-4ea0-321f-ace0-95b0888942ec | -8.18373 | -61.37576 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f7bd469-99d2-3bf4-a970-95d5acb7b885 | -7.6081 | -42.6788 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d08590b0-55bb-3f9e-8f6f-c8f1ffb833d4 | -12.88853 | -48.12457 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a118c00-8387-3c48-bc0b-99beb9dabe6d | -7.19208 | -44.05554 | 2025-08-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5212846a-b29c-3dc9-ab25-853b6da63bf1 | -6.79181 | -43.76928 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52aa2d63-f627-3b70-947f-d27cb3cf66b7 | -7.35884 | -51.75945 | 2025-08-29 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a47b3718-2384-3d25-b6e9-4c4fe52cecf6 | -12.85061 | -48.14111 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8286285e-04c4-3c32-8d63-c99c413a9919 | -11.08832 | -44.75045 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3658b73b-adba-339e-ac25-a97cce499049 | -10.98341 | -46.90093 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dfbabd19-83bf-3358-84f5-0e48a771c769 | -8.48916 | -43.68173 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a15d925-d3dd-32ca-acf9-b28ba671db47 | -8.19244 | -45.05757 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6184725-8b6e-3ffc-ae45-ee20f3432e66 | -6.54481 | -43.10195 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8080f4d9-cb51-3e9a-9314-602fcae34a83 | -6.22252 | -43.37148 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c39f8407-acb1-3315-899a-e54f181297df | -8.45793 | -43.71221 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36605882-3aae-3063-b1fd-bc7a733e88d2 | -6.16366 | -44.1917 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b4fcf14-0955-322f-9c97-53cc7edab3c8 | -10.64246 | -48.64592 | 2025-08-29 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c5b560f-4e23-3cc3-bf6d-645dd257ee4d | -9.21854 | -60.87162 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e516dbd4-bcae-3da7-b923-c2d7b9b717a2 | -12.67669 | -48.191 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1f94cf0-d716-36de-b1fd-9fd80e0914b4 | -11.4243 | -55.17495 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64b96863-f641-3ad2-9ee1-d0fe58ff665f | -6.7078 | -49.46856 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5fc688c8-fa4d-3df8-b761-505435ebf1d8 | -12.91469 | -48.12003 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1a8b017-fe9f-38f5-bd05-9f00541ff36c | -11.24297 | -45.00665 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 808e8f93-1687-365c-8684-cda8cb782431 | -9.84632 | -44.68262 | 2025-08-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b3e7b60-ee56-35f0-aa21-f684c0c46bae | -6.97389 | -59.33243 | 2025-08-29 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80bcdf52-bfd1-39f1-934e-0cb5498b9a2c | -12.69085 | -48.19337 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c4f9e417-afae-3d69-af2a-d580e2da281a | -10.98143 | -46.91436 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3854cb9e-1e9d-3d5f-af93-fb60ecffe8b6 | -11.28856 | -43.54888 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fdcdb8a-4438-3f91-8fdf-d14053a4ea14 | -11.16282 | -47.1527 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a7f8ca33-0785-328a-b05c-ca2b893d1c03 | -10.72633 | -47.02089 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51f619f3-1f8a-3972-b44d-5ae0fad211e1 | -11.32795 | -51.28347 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 138b3c5f-4bda-38cb-8cd2-e8b6756ee0c4 | -7.04287 | -44.37695 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0dc9448d-c694-35af-b2ec-0f8170e64cfc | -11.93024 | -46.69453 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a07f9492-07c7-36aa-9e44-e88963462d10 | -12.06319 | -46.62908 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81e6a8e8-3968-39d0-bc8f-5635aeeddf5b | -10.47503 | -57.93379 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf72a857-a6e8-3619-ae71-0e9c2049ef22 | -7.02458 | -44.67829 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76dec987-d54e-3d1a-9685-f371a7830150 | -11.12385 | -45.11677 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f90132a-b581-3732-b77e-7b68727b4695 | -6.04044 | -44.4654 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bf45968-1dc0-3a5f-aaec-ae896837133c | -9.43251 | -47.65032 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bab9d6f-85dc-3605-ba42-dd33562c1957 | -6.81299 | -44.35527 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b316201e-4943-323c-97c1-30c6cc9f5c68 | -12.93019 | -48.13882 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68c827c4-dc0f-3a11-b17f-192ba11b762b | -7.41129 | -43.38924 | 2025-08-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README49.md)
