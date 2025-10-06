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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8ef6a64-6f55-33f9-a79d-9ecbfd09ce44 | -15.20771 | -56.81028 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f294c8ab-4d0d-3a64-9fca-831b3b8c4781 | -14.34968 | -47.71936 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0be967b-c00e-3dd2-9d89-9b8406117052 | -13.34209 | -47.59525 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b30a24b-830d-34b8-a5e3-4fc2085c9f43 | -13.2799 | -47.57755 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78263969-a689-345f-93fc-d392a6d8c9dc | -10.85649 | -47.97026 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93f6f3ec-3a47-3146-8006-4dc9ec4382df | -12.81786 | -50.53116 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f3cb2bf-2e93-3979-958e-9fa1d19e51d6 | -14.64399 | -52.3649 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3881d68a-e041-3eb4-9f9a-21192ed64900 | -12.89568 | -47.29137 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 135ac949-93c8-3088-a7e0-4d689aa024bb | -14.75976 | -54.67714 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3972a935-e58f-3d24-813c-78827156b21a | -11.12681 | -47.76662 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa9734f6-f61e-3c6b-b0df-1f7b7ff328ae | -12.92018 | -54.72684 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7427a82f-8423-3d72-952d-a95c369fd4db | -12.25085 | -49.2118 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 899d5af3-0fd9-334a-b3e0-05008db6c898 | -13.05935 | -47.89895 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ebeb8d7-4712-38b1-a390-5517aa73806b | -15.34422 | -47.30658 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e1e9cd69-a189-3b10-958e-1e3964459055 | -10.02301 | -48.28823 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c17cc92-ce42-3e22-8fa5-a4490c3fefe7 | -12.57892 | -46.74257 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa688483-8f61-3083-8d01-4ef2327dc096 | -9.68352 | -48.40987 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea1974e3-d59d-3c15-9a4e-0381e6fbe2ed | -13.57514 | -48.1501 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f6865b7-ab3b-3083-ba7f-9cc7ea9c71d0 | -10.73829 | -47.8792 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c99c58d8-7768-3ef2-960f-8a910f11ca0a | -14.86831 | -51.50364 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e282e04a-99b6-3c3e-a2b6-9a826cf7bc8f | -14.28941 | -45.86243 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9d2a512-d7b8-3585-a275-7c1965dfebfe | -16.00733 | -50.95668 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3726fc85-4fed-351a-b98a-8929eccf5851 | -13.27993 | -47.62089 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5c1dd8e-f000-3d5c-806f-72778a109eb8 | -11.06395 | -47.9074 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7a701c2-231f-3140-86aa-9ac3072ce629 | -13.79577 | -44.08308 | 2025-10-06 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a0cbcb2c-c7f3-3b41-abc9-563093d05c65 | -14.68587 | -48.39888 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a6dc3e43-f2a0-3a13-af26-f30c07380ad0 | -15.15478 | -45.75809 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d263c344-0828-3aa1-b7f8-c557a7a246de | -10.85593 | -47.97381 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18402cde-c32e-3ab9-984b-c7da85744629 | -10.48094 | -49.08794 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a429ee58-bc11-3d4b-abdc-992e1d3ce687 | -11.878 | -44.9545 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 503e9151-31e1-394b-9682-afe7a0ace329 | -15.76051 | -47.76586 | 2025-10-06 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f776c216-c1cf-3c8e-a812-a26973684237 | -12.48108 | -45.55925 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 162c5ca5-8cb2-3e3a-8761-99e7bb5459eb | -11.15592 | -47.92932 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 527476bf-a2f0-3bb4-a591-3ecfc027fdd9 | -11.80575 | -45.08077 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f444bbe7-c98f-3146-bea3-de1aec14e4a5 | -13.36544 | -47.24361 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66d7a8ae-0f3c-37ed-8a2d-7cc1d8beccb1 | -12.60151 | -48.1306 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a705da5b-1843-3318-8355-be51bc1af594 | -15.75426 | -46.26202 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18635b2b-cccc-35e9-bab8-68ca421a2cfa | -14.68332 | -48.28587 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09781bb9-095a-3305-8e63-546a70d58bfe | -14.65185 | -48.35694 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67576715-f459-31d4-8b41-5d0fd9484871 | -12.59662 | -48.11495 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9342723-b0b2-35a5-a55b-2abc39347e2f | -16.03995 | -50.97494 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75d540a6-8694-3a5f-9c8c-f03796e4c4c6 | -14.75195 | -48.41322 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45b3b2ae-7168-3746-b149-85f7fb11f982 | -14.61831 | -52.53233 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a17b08f4-873e-3f10-930c-3770fed2a7f8 | -15.74723 | -47.69721 | 2025-10-06 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 902a969d-1621-39f1-aae5-7ff2175a0d67 | -13.13533 | -48.00147 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e48a8b5-1ccf-359a-a76f-8630a2970147 | -13.03555 | -49.162 | 2025-10-06 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2eaa48a3-6eb4-3a53-aa0f-fef5ece38e09 | -15.24376 | -49.28012 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1809d0b8-280b-3548-ac12-c0f11b3bee7a | -16.01331 | -50.83628 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8880aed0-04d2-3b64-ae53-cc1e607319b5 | -15.50711 | -46.83986 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 263f2598-76c3-3517-b848-d60191e71ba4 | -12.91483 | -54.73059 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c14fd2d1-92bc-3dc5-8bd0-edc96b8504ed | -15.33537 | -47.96405 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7078603-750b-3616-8928-48b343befdac | -9.34361 | -54.52426 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff2becde-7443-328d-b0c3-946cd6779823 | -15.26659 | -47.14497 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01baf1b7-71fe-3ae7-bf06-7411e4ddcf2d | -14.88261 | -50.12407 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70d12053-c3a7-3e2f-8ced-2c3a6f110616 | -13.85953 | -43.98913 | 2025-10-06 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d638b27e-e04c-3e33-bfa5-301e63617be9 | -11.10812 | -47.71338 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e41531a-bccd-3d9b-80dd-f7b250aa48da | -13.36104 | -47.25016 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfae7e9d-d493-3144-803b-1e3f2bdaabda | -14.68313 | -48.39479 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c56a002-8c54-30c7-afc3-9d961a24c0a6 | -13.49372 | -47.24987 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1426cf2-b92e-3834-b15f-1bfb10383bb0 | -15.46141 | -44.30733 | 2025-10-06 04:27:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4427ddc1-7641-3345-9e40-c9747437c679 | -14.54444 | -46.95583 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2aabc02-d1aa-310d-9105-c893228de983 | -12.25541 | -49.20504 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 380454e5-2e33-3d78-956d-ac1cd0746079 | -15.87704 | -46.26038 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55b8c52-5fc4-318c-a042-764f6b387d85 | -15.23936 | -56.75867 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88133996-98fb-32ce-a5ba-ee065f908fe7 | -11.00059 | -51.1512 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9cf32fb-f28d-3e47-ab0b-8e2e9dca26da | -11.81453 | -45.04531 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0a6c718-5108-3e9b-8362-a149c62367d2 | -14.34913 | -47.72289 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6d309e6-8a13-3554-9818-8814f8058b77 | -10.31447 | -51.46052 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4405333a-67ed-3cf6-9d85-fad70b1f3a3e | -13.27884 | -47.62791 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae00c708-f473-3385-981c-ce7e4b855b99 | -10.47883 | -50.44477 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc04c207-d8f8-3d07-9562-44d080c380ec | -9.54779 | -54.58984 | 2025-10-06 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3af70e5-21b1-311b-b48f-c5c27e15c3ef | -11.02429 | -46.5484 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d14240ad-5117-3a93-a834-be033e6ca2a0 | -14.34583 | -47.72236 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d7f4cdf-d6e8-3553-8b13-3043d9b8e2b4 | -13.23559 | -48.46688 | 2025-10-06 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b51f3ce6-7864-39d7-b856-ee8c9e7168bf | -12.98488 | -46.7994 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7a19f2c-da14-3f29-97a4-63136572fcad | -10.72798 | -47.64447 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f01dfd1c-0d17-35ad-9b19-17d2169c540b | -16.06165 | -50.93017 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe1c769a-774b-39ac-ab5b-ec432838e949 | -11.48677 | -45.03438 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0bc628b-578e-3679-8108-e0d64c61cc50 | -13.10463 | -47.91706 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5834bf40-f4d7-3dc5-9aa4-d05c41d7c1fe | -10.59379 | -54.35638 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d94282b5-0a57-3edc-ac95-8e69f9d48679 | -15.8805 | -46.26088 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 406d2561-1f18-390c-8ce3-915beb2e8ef4 | -13.23658 | -47.81237 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26aac878-a348-31bf-9e82-659c4f927c93 | -16.00518 | -50.94822 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7de7ac9f-f01d-3e21-838a-10995d5d8907 | -15.24946 | -53.78238 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03d011e4-f477-3d7e-be30-bb182a9e3fc1 | -11.80987 | -45.12512 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4685ae48-deee-3ea5-8643-0414c0ca8df2 | -14.53611 | -46.96569 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65eddfca-7ec0-3ab7-a430-ffb55e77d44f | -11.0672 | -47.95114 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f752bc7d-4575-3f5e-b7a5-9c2b0de2e80c | -12.89459 | -47.29842 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be4d12e6-d240-302b-8a4e-ab42d13e6580 | -14.65145 | -56.01795 | 2025-10-06 04:27:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecb1d61f-7a71-32e1-ae8a-757da781f8a6 | -14.6133 | -52.51627 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 725e1aec-531e-34c4-b602-72e828031d69 | -13.34386 | -47.18537 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 403ef5e2-04ae-3818-85cb-4be96a3dc1de | -16.01395 | -50.83244 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d28aefa1-3dcf-38a9-9fdc-5021e560452b | -10.2783 | -44.36981 | 2025-10-06 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b5d3cd3-48b8-344d-a655-243bba8b5237 | -10.59836 | -54.35724 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 509b64d3-b396-32ec-881b-e8344b834b86 | -13.03454 | -49.14692 | 2025-10-06 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c111f04f-3390-38b1-aa13-f513658673f0 | -11.23351 | -48.70026 | 2025-10-06 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c8b6441-78c7-3a3e-9e03-90d179fa8979 | -11.10556 | -47.18639 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5143b31-34ec-3786-94e6-5b10eb884179 | -10.67078 | -48.47509 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 331a7a23-3a96-3baf-84be-661b098f1a2e | -12.57559 | -46.74204 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 361e5295-d66a-333b-93de-2109c616ad00 | -14.68201 | -48.40189 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README48.md)
