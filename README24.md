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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06dbc795-cbcb-38ee-9866-17dc24006f21 | -3.73816 | -44.53615 | 2024-11-11 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77a37c04-4187-33c5-992d-95c407166e26 | -1.85041 | -46.58524 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a61f9751-a86b-3b28-842e-56997f46785d | -7.43681 | -39.7632 | 2024-11-11 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f12e6b97-4acd-35d8-9fae-d3140a4524ff | -4.6937 | -46.43557 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ad3dab7-cf8a-397a-a183-f14c0ced8d8a | -9.59589 | -36.01778 | 2024-11-11 03:55:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fb2a1033-6ced-3d8c-a6f2-899b8d0eec1c | -2.97995 | -46.98704 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3150a046-38a1-3a6d-bb1d-6d5478341cc4 | -2.26364 | -48.75654 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ebe72da7-e3f4-30c1-b29c-d23f94b91511 | -7.43293 | -39.76613 | 2024-11-11 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 111f8ab5-0561-3d3b-9da4-f321830d1e20 | -3.24478 | -45.37934 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 73eb5234-2829-3ce4-8088-cd66688d0fcc | -2.39563 | -50.31867 | 2024-11-11 03:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c72e8a2a-3d24-3c69-ba56-06b5c9f80bc6 | -2.22232 | -48.85261 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c58a21e-71af-3896-9921-d9089e3cbef2 | -5.53214 | -41.6789 | 2024-11-11 03:55:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d7f44c8-5f13-31d5-a480-30534c4473ba | -3.51912 | -40.90493 | 2024-11-11 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ee683e5-df10-3a8b-94df-b508c054c466 | -2.16753 | -46.42789 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0696b7a-fc13-3c84-a5c4-27d1f72cbcd6 | -3.24593 | -46.49051 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ee99603-45eb-3e5c-b994-9aa82d4298e1 | -2.19857 | -46.40437 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0d2289d-e74b-30fc-ab10-f742b315c2f8 | -7.6298 | -40.04855 | 2024-11-11 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| bff9ffaa-dd37-3ee8-8b75-118013ddd551 | -2.69621 | -46.81647 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82e2c9b0-e711-32f7-8742-3e0acc766916 | -9.51925 | -36.0879 | 2024-11-11 03:55:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bb0c0066-5ace-32a9-98b3-e8ab30112c81 | -2.24939 | -46.52074 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0d724f14-7c19-32fa-aace-ac94d00be3c9 | -2.05819 | -46.1419 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f59f9fd9-5e97-3fd0-b608-2c7ab2660892 | -3.23955 | -46.30465 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83738ebb-6952-335f-bfe1-91dc0a82b685 | -2.97938 | -46.9904 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b06a481f-594f-3395-ba3e-58728c817210 | -2.23042 | -46.43896 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 21537c7a-1170-306e-b933-4a89376289d3 | -2.19249 | -48.37554 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b1e33b52-c392-320c-b456-d9cf0dad2e5a | -2.37831 | -50.34016 | 2024-11-11 03:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c261e630-0cf8-3265-8ef8-480b958af450 | -6.57809 | -34.97917 | 2024-11-11 03:55:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 3ed0916b-a57c-3cbc-aeb0-b313dc3d1ff4 | -6.21456 | -39.40304 | 2024-11-11 03:55:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 36baf62f-95f7-35d1-af76-0080ab30de1b | -4.46301 | -38.75055 | 2024-11-11 03:55:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e884ddb0-a586-3ef8-a6ad-3db8be89aa20 | -3.20998 | -45.23114 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1160fbf-81da-38bd-bcbe-640515f0fa52 | -4.90561 | -44.65979 | 2024-11-11 03:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f10119a-f95e-3790-8567-0e023ef0d81f | -2.08254 | -46.48745 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d674fd6-127e-3b91-abc8-d7d3092eb82f | -2.41646 | -46.52048 | 2024-11-11 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4f6efce8-a731-3b13-b112-8862e3e84d6f | -2.16803 | -46.42475 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b50f7f3b-9b4d-3cfa-b105-cce69ef60b0f | -2.25042 | -46.51437 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ae740af2-fc50-36e0-bfaf-af9ed6f220b6 | -1.8518 | -46.58508 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b86eae28-2968-33c4-a353-23772272cb64 | -2.91779 | -45.63514 | 2024-11-11 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9decca8-e341-3c08-b3aa-02c85dd50a9d | -2.97581 | -46.99442 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e4f8ae3-a987-317a-af72-ed0667d555b0 | -2.87823 | -45.36694 | 2024-11-11 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9d744e4e-b162-3194-825c-17f9ad11876e | -3.50532 | -40.86206 | 2024-11-11 03:55:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 99256227-2c14-38ed-b569-89bd3dfb4c65 | -3.27336 | -46.32222 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbe0c22b-1404-33e9-85a1-897a409b960b | -3.55972 | -44.96088 | 2024-11-11 03:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9eaa68e5-c405-3f03-857c-24605408dd7d | -6.09823 | -35.11121 | 2024-11-11 03:55:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ec9d55cc-a74f-3a65-94f4-31114595f24f | -3.23437 | -45.38298 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84b755a5-02a2-3e70-b354-80623e8adaed | -2.30846 | -48.90262 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fe002b3-4d1d-3d67-ba58-88f4f64b739a | -3.3064 | -42.37687 | 2024-11-11 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e26fa184-8167-3d91-a7ae-116881707346 | -1.84564 | -46.58104 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 36b70cc4-1cee-39dc-bdf9-59cda457db0c | -2.36539 | -48.51712 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77fd7e50-7900-306e-bc46-a51657e3831b | -2.09819 | -46.5224 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 06e1a40a-9aa2-376f-bcda-f750e8c95442 | -2.83206 | -46.64783 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae10bcf4-1ccf-36ec-b314-37b8ab7022fc | -2.99407 | -46.93589 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0825b520-741a-3418-b66d-097df6ec40d9 | -3.11881 | -45.97655 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 543eeaf3-bb3c-3f58-b640-ceb4993ab402 | -5.54227 | -39.22113 | 2024-11-11 03:55:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d80af72-c037-39d7-a141-706d4a3c6910 | -3.98982 | -44.1353 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81f02546-c259-3b38-ad79-e16dde93b95f | -1.02584 | -48.85952 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 54af9913-8922-30de-bad3-4b6a8a79ca20 | -4.70681 | -46.38923 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 838385a6-a264-3729-9e3a-a3ed93430dcf | -6.21169 | -41.6511 | 2024-11-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af45a982-037a-3e1a-b67d-29b17f2ae615 | -2.06283 | -46.14581 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 487f3477-3f9e-3067-8bc5-c3ca747e2a4c | -3.53421 | -45.70833 | 2024-11-11 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 603c3282-9783-35ad-9964-837fc3623018 | -2.74178 | -45.20963 | 2024-11-11 03:55:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 04194c03-9184-3e88-b8df-e4828196bcb0 | -2.19108 | -48.38425 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d78b3b36-4e12-389e-9496-42ceed88e5d5 | -4.12449 | -43.58395 | 2024-11-11 03:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dead07c-2460-3bc8-ad12-34b48aeca552 | -2.06257 | -46.34357 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 841852a5-9629-328b-a38e-6e8707c6536a | -1.98645 | -46.44878 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b296073-2b7e-3f92-a6ee-3f053238c225 | -3.73442 | -44.53097 | 2024-11-11 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ceed25e2-ddb4-39bd-ae50-606a52d81e94 | -3.23916 | -45.38375 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d3fcbe79-2b1b-3c3b-bd69-f64a890afd6d | -3.68588 | -45.24374 | 2024-11-11 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34c3f35a-0685-373a-8471-2a371ac7e243 | -2.93369 | -46.71805 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5011dd9f-c717-350f-8806-60fe28854317 | -3.5905 | -44.55011 | 2024-11-11 03:55:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2c394d1-1706-39fb-a839-8ccc588234c0 | -5.82004 | -44.12466 | 2024-11-11 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| de8705b6-16c2-31f6-8e56-6d8dc6b200c1 | -5.51551 | -41.68935 | 2024-11-11 03:55:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e08e443-96b1-3745-a3d9-70f240077288 | -2.97344 | -46.99292 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7a52c24-4418-334b-8dd3-4d5f2c3f2a18 | -3.32428 | -46.10155 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b67690c-05bd-3a9f-99c6-4eca349b7534 | -3.12919 | -45.2424 | 2024-11-11 03:55:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6a7ef439-2e1d-388b-984a-161caca2d7d2 | -4.54397 | -43.56997 | 2024-11-11 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 897a9e9a-15bc-3aa7-b1ca-070cd3770ce1 | -3.21081 | -45.22606 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a7d1cc2-69fb-36c2-b371-12ac10236644 | -2.06778 | -46.34441 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7604e3c-301d-3060-9a12-fe2cc0435fd7 | -4.12386 | -43.58783 | 2024-11-11 03:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7bcc798-4526-327d-b1e5-983bfd7db701 | -5.55081 | -41.65564 | 2024-11-11 03:55:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c500aee-6f2d-365a-add5-28d7418057a3 | -4.06916 | -43.94971 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 913c8a90-c3cc-3cc0-ae35-333c556bd381 | -3.53024 | -45.70211 | 2024-11-11 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38dabafa-0a36-3ca3-b291-9697f2862691 | -2.41174 | -46.5165 | 2024-11-11 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 578c0dc2-2233-3a0a-81ba-332e86ba4c9b | -2.69726 | -46.81017 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72025f7f-5f25-3d54-9ce5-23950c1102df | -2.44121 | -46.24408 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82d972d9-224c-37c4-a74c-af54d58e7114 | -3.13519 | -45.97044 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2e4078e-b16f-382c-a490-467a3d14ecda | -2.98646 | -46.9811 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1cae630-bc69-3bf6-86e3-9794218d8a56 | -3.1463 | -45.96656 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a15214c5-2f34-3794-9bdd-f270b9ff5e49 | -3.29697 | -40.66528 | 2024-11-11 03:55:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53d00fd0-3727-3483-860d-0435fed561e8 | -3.2488 | -46.3121 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81ed9467-f390-3917-b4d9-322f448e4ba1 | -3.73368 | -44.53542 | 2024-11-11 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a37366bd-bd10-31e8-a0e9-e01485f4946e | -1.93635 | -46.35844 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dedbc95c-89a4-3a79-95b9-f2f33f905e47 | -7.37307 | -35.08736 | 2024-11-11 03:55:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f4daffc-2fe5-39e7-91aa-83febdf8e657 | -2.48217 | -46.34909 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c4b6d36-1eca-3e5f-abb0-90012f8d6622 | -5.8676 | -39.20819 | 2024-11-11 03:55:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64cd541b-3761-314d-ae9a-7b4387282cf3 | -2.98589 | -46.98449 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c9642b3-26bb-3f1d-b4a1-c73f681fe544 | -6.1339 | -38.90085 | 2024-11-11 03:55:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fc3b8846-070b-3dad-bb10-78f8d36bdfed | -3.03008 | -45.82561 | 2024-11-11 03:55:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb1f2c10-e201-3dfa-a62d-83f5aeb85212 | -2.3793 | -50.33425 | 2024-11-11 03:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eca770f6-68b9-3430-b514-48a48901e315 | -4.08825 | -43.94038 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b39efc2d-78ee-3a38-a468-96946d39b6e2 | -2.87737 | -45.37223 | 2024-11-11 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |


[Clique aqui para ver as próximas entradas](README25.md)
