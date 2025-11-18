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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e406ca28-c52a-3d0b-aae6-28a66c620765 | -3.18295 | -50.65247 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 969483fd-3b60-3f4f-9d84-03a8635d042c | -8.93371 | -49.8445 | 2025-11-18 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07a8a9c6-2b5e-3162-b8ff-a11264ead06b | -9.40262 | -48.44989 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8ce6b856-8803-341b-b4e4-8c2cb383dfad | -3.18235 | -50.64849 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7c3aeb6-9619-3109-829a-62696041ea64 | -9.88669 | -44.18666 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c528531-5c69-384a-8888-c03e4b70e9f4 | -4.2322 | -46.34264 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d32a0686-094f-39a3-a902-7919e82c0e96 | -5.08673 | -45.10669 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8cd01eb-d59f-3a41-ad26-ee34633b89d0 | -6.54779 | -46.90509 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cbee8a6-423a-3a87-8776-a7519545e2d0 | -9.03014 | -47.45945 | 2025-11-18 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f0ca9b-c552-3e50-85d3-760060267884 | -8.10896 | -46.06801 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61b7b10b-f713-30c1-92f6-73d1ac9d4c47 | -6.62851 | -43.90756 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cc55d0dc-3353-3e87-b35a-9bb791ab99fd | -6.37081 | -42.31858 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54de1290-5d89-344e-af35-61d5423a9537 | -4.45127 | -44.21604 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6b8720d-beba-323c-9fe6-5cbd4109bfe9 | -10.53795 | -47.99157 | 2025-11-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5e89763-6a55-3e56-a77b-05d3d9fdf997 | -3.23268 | -50.49358 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9196614f-c20a-3778-9c4c-4e73dbd60813 | -10.79938 | -47.64008 | 2025-11-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 025b8313-a62e-3c53-b965-c800f0ba19e3 | -6.66935 | -42.03841 | 2025-11-18 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| a9a53d15-0d09-3afe-a098-d29a4cc94fe1 | -10.5408 | -47.99599 | 2025-11-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6120a552-0857-3609-84cd-f968bff486d0 | -6.67516 | -43.76069 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 936113f9-b51e-35cd-a374-018ae63b4acc | -4.6045 | -45.95057 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a0be240-0fe8-3e10-bf02-6c1b0744b8b2 | -3.08943 | -51.26449 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d38ef43-b39c-3c4b-ac6f-09c5a055a765 | -3.52017 | -50.34225 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d18a527a-1f50-3721-ad9d-a849fe71286c | -10.8586 | -44.89238 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ab56e87-e983-3cc0-8a8f-7b3ad9833c4a | -4.40552 | -45.83316 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a89050e2-534c-335f-8d5a-a1b030f5f952 | -7.14686 | -44.92216 | 2025-11-18 04:21:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03080724-857a-3686-9b4f-d1ba7a0c20ec | -2.33386 | -55.80126 | 2025-11-18 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdaa7a7c-1dba-3f08-8b95-03d499e9586a | -11.57022 | -42.42116 | 2025-11-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2dfa2c41-7233-3842-b3f9-f8c8088f1322 | -5.03569 | -46.82816 | 2025-11-18 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05a565c2-12b9-31d8-9c26-2ec974de0ee1 | -7.33621 | -47.79298 | 2025-11-18 04:21:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d582e1ca-5236-3ae2-aa73-b7df3648ac13 | -3.30392 | -50.01141 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72a84904-7699-3099-a5f6-c0e32ac5489e | -6.83398 | -46.30161 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e8944f5-1d90-3d86-8023-0e8dc605454e | -7.62075 | -42.58841 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 93286a54-4ef6-3e01-acb9-f02034c7983e | -6.28765 | -44.73977 | 2025-11-18 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b11f63-aae1-3d35-9edc-0c784774df66 | -7.6313 | -42.5813 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d89b772c-21d2-30e2-9dac-9f3cb870e47e | -4.1895 | -45.61763 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44cc2cae-1bd2-36d3-b46e-813749b17237 | -10.50875 | -43.95653 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7261554c-c229-3064-92fb-86c8d1df5b14 | -4.97987 | -41.85721 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| c6a93437-0055-3b21-94c6-497f39f59764 | -6.44952 | -45.74068 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 740383e3-1e7f-3c0c-9f0c-9b385294827a | -7.41278 | -42.75481 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a1aeefe9-b935-3fef-bba2-2d7bb4366c57 | -7.44999 | -42.76437 | 2025-11-18 04:21:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23f0e556-d85c-375c-a2f7-851b87e02caa | -7.02447 | -39.36441 | 2025-11-18 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c7549b51-22e9-3a91-8168-f091dd6b28c0 | -7.65758 | -42.27652 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f514b88b-e18a-3927-bcae-737dc37e9ef1 | -10.73717 | -41.36815 | 2025-11-18 04:21:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2c53bef4-11ab-3484-935b-564eb57fd83a | -11.09356 | -44.82401 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d6c97d5-7508-321d-be83-604e5d95eba3 | -7.38135 | -39.1243 | 2025-11-18 04:21:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b916f10-452a-3b2c-a169-8245286c4d82 | -9.72933 | -49.13153 | 2025-11-18 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96059423-7ef4-3e20-af06-293300f8a3b1 | -3.69036 | -50.54261 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043f0317-b133-3395-bb59-9d8ae98080ca | -10.50931 | -43.95286 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b643da6-1867-3383-99cd-1552ea1e81cd | -4.0166 | -47.41553 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1da8d6fb-a82d-34d0-8487-18be5eea9fc6 | -10.51158 | -43.96072 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f90566c3-c785-3d89-9ee9-7464884b25d5 | -5.17625 | -44.34093 | 2025-11-18 04:21:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24508a79-e241-3c31-a04d-25d63e355361 | -6.71866 | -40.79788 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7cc04c69-0402-30da-a11f-6bea46fd462a | -5.56905 | -51.2015 | 2025-11-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7aab533-9f8a-324c-9a33-0e5d059d7ac2 | -10.91847 | -48.67237 | 2025-11-18 04:21:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff52312b-5d06-3f51-9739-6b2b41ffa6bd | -10.27636 | -47.97396 | 2025-11-18 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee842e0c-283d-3bb6-8327-c6811fae26cb | -6.40138 | -42.32725 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 89483822-3f22-3d01-ac77-a00c25e6a59c | -4.64644 | -47.95179 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42863910-f66f-3c56-a697-96ec5059d69a | -7.85728 | -46.86889 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7591b1b7-585a-3056-a008-9746741db382 | -7.46743 | -45.92899 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72959a77-6766-34fa-a0b5-3a53c9e7c6bc | -3.24018 | -50.50385 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 139992a8-4abb-3356-8ef0-0688881a08f9 | -10.54145 | -47.99206 | 2025-11-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60b4d814-762c-3ad3-a12d-e08be1b79536 | -3.19142 | -50.64996 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4584806a-f3c8-3f1b-a08f-6e379bceafd7 | -4.1895 | -53.43764 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3415fcf-9ed5-36f8-9e40-32a3ed2c43fa | -4.67458 | -50.71233 | 2025-11-18 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eab2ac1-b8a6-3e4a-8891-0a88d641b9fe | -4.65314 | -46.54384 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fa31806-e789-30f3-82a4-537ca847f04c | -8.38522 | -44.06675 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f1f2fa6-d79e-3895-941d-1f188186ffe0 | -11.42868 | -43.32866 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 210f67fa-3010-3fea-ba4e-ff5924aca100 | -10.61317 | -42.31916 | 2025-11-18 04:21:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd378521-530d-3e2d-b5db-dd85ac446dcb | -10.34026 | -49.63953 | 2025-11-18 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80fd44ac-8867-33ac-9c8f-e81449c49e16 | -5.77403 | -45.51392 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02a00563-ffe8-302c-8aac-5f5768c54f2b | -5.75386 | -45.10558 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e318dae3-8296-3913-8c7c-a885dc2a66fc | -7.92446 | -46.031 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf418d31-193a-3741-b35e-16909be0e00c | -8.29207 | -43.96523 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24c2074d-877c-3a2f-b6c1-e631c392f82c | -4.64273 | -47.95111 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9639e65-ad18-3a22-887b-22842b96a276 | -5.46373 | -40.99026 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f426c11-d67b-3618-9f02-3faf9312e266 | -9.16116 | -47.59916 | 2025-11-18 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c27a6a6-993d-3082-9d40-a77fcbec2deb | -10.85028 | -44.88025 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b9c9382-b80f-36f6-a2f3-2ff2a962b15e | -9.73227 | -43.94582 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abf5bfce-d86e-376c-af77-f70c0d0d57b7 | -7.53599 | -44.06343 | 2025-11-18 04:21:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6e0ddee-0b3f-37d9-8282-3920348672cd | -8.2972 | -43.99871 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fe3a922-96be-3c52-a7c4-45bab14d4b42 | -6.67128 | -43.76369 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9c7fb5a-33af-35f8-bfe2-d47918555896 | -4.49164 | -46.59387 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70240f52-6bbc-33f2-b935-cc7b9ecb72d5 | -9.72781 | -43.95252 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f2c402b2-83eb-3ad7-b200-61ec340b1a29 | -8.72428 | -48.535 | 2025-11-18 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10553c9e-89e2-3991-8dea-fa83f1282dad | -9.19086 | -45.79165 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ae395c6-d506-3f9e-892c-cc99f6fa24b5 | -10.3827 | -47.28772 | 2025-11-18 04:21:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93f9b379-8537-332b-a306-e54b35b232a4 | -8.38576 | -44.06321 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4a727f2-a987-3b2c-9ca7-e390c9bdc8de | -3.27359 | -50.02349 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a9054fa-3e02-33aa-b591-96c22991907f | -4.14364 | -46.34814 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b8aea4ff-0ba7-3c46-8b1c-fd031e8ba838 | -3.28377 | -51.42587 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90131245-dd51-3739-8748-383d4b6e5669 | -5.95927 | -45.35583 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f361aad9-2fc9-37df-86e2-a2e54b892e39 | -10.08256 | -44.72221 | 2025-11-18 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7a3c7a6-2a99-304c-90c3-dca87973643f | -10.75094 | -45.14898 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63071e8d-56f8-35f8-8010-ee718dd384dc | -4.64671 | -45.52385 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e8ab2ca-6310-3190-9e76-8a990aa54e9c | -5.63589 | -43.92641 | 2025-11-18 04:21:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e50eec37-4254-3a41-9fe8-78af1b4269b3 | -10.64697 | -49.73453 | 2025-11-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f2445b9-8a6c-394c-ab7d-cd7ff1a5de14 | -3.8453 | -51.05949 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97a257da-2ca3-3227-a4c9-79742b0fbb35 | -6.0822 | -41.68241 | 2025-11-18 04:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b9a2df2b-f44c-3560-b4d4-fff55911f0e8 | -7.1523 | -41.78664 | 2025-11-18 04:21:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5522adb6-4366-3c2f-98e6-d37025fa862b | -3.46073 | -50.12459 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README27.md)
