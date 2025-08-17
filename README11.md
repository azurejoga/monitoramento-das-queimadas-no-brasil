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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83f04e5e-5687-36a6-b3ae-fdf0376a0f6f | -8.50629 | -44.74126 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d19aff49-a9fc-380f-bb30-35e01492f6f0 | -8.57699 | -39.425 | 2025-08-17 03:49:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 403138c3-073d-3478-a00e-d98195ff446e | -8.74811 | -44.04286 | 2025-08-17 03:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 361eeefb-31ed-3a95-af8a-eeed2a85443a | -4.77707 | -45.32522 | 2025-08-17 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4094225a-417c-3ed1-a01b-543f68b8dd23 | -6.72542 | -44.05124 | 2025-08-17 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab0416fd-9ef2-30c3-b634-4afc936b0656 | -6.61415 | -44.46615 | 2025-08-17 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1caf45e-2660-3f38-8042-b3a3e84a55d3 | -7.41755 | -42.02751 | 2025-08-17 03:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe439272-abce-382d-9d78-e5fdb5bd99cf | -8.50724 | -44.73596 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2393126d-6f53-3bd1-ae64-9fbdd2a7da31 | -6.18457 | -45.44157 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 29e91b99-f49f-3e8e-8cad-682c6eb8deec | -6.54361 | -43.03198 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7a41fa2f-39cd-3e42-9581-7d88936fb422 | -6.61899 | -44.46716 | 2025-08-17 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3d7a7b2-ab5e-3901-89cf-35464d8490da | -6.18919 | -45.44593 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eee30bb-f9b7-34a1-b520-2e5a366001b1 | -7.15276 | -44.38425 | 2025-08-17 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a200c4d-e0ec-38e6-9bd8-895c7ad778e5 | -6.19115 | -45.43951 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e4c4628-a519-315b-827c-9ae95a891bef | -4.92186 | -43.24781 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c611f9e-5dec-31d8-b92d-15303f6fbf97 | -6.19059 | -45.44276 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cbc02c5-e641-38d2-9f70-51f49976d98d | -7.12481 | -41.3959 | 2025-08-17 03:49:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5a3774e8-97e8-34c1-9c95-f7adab0e7e56 | -6.55244 | -43.03351 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25f125dd-95f7-3087-b220-048841a72248 | -6.07305 | -44.63029 | 2025-08-17 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b883dac-73b1-3120-b82f-c5cdbb58df11 | -4.77175 | -45.32427 | 2025-08-17 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 882ecafd-c2ff-30fb-b1d4-0991fe495964 | -4.77763 | -45.32193 | 2025-08-17 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e4b8c3f-6993-3699-9754-4909b9c77a9f | -3.14729 | -45.65163 | 2025-08-17 03:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22fae7bc-c638-39d1-a4a1-921abf344198 | -4.91568 | -43.25641 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8a41b70c-88ad-3b76-91d3-aaa0a6d7f1ea | -8.74438 | -44.0373 | 2025-08-17 03:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4cc92d8d-c907-3f5c-a4bb-624da14738f7 | -8.51204 | -44.73681 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae47b4a3-5290-3c75-abe7-365e72358ce1 | -6.18977 | -45.44268 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 785e1bb5-d61e-3c58-9d71-b53c295c5b39 | -6.6189 | -43.87645 | 2025-08-17 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d8f6266d-0c41-3b43-88b2-e35823d936bd | -5.1001 | -42.79762 | 2025-08-17 03:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0443eb76-80df-35c9-956c-4b4cf73362cb | -6.61508 | -44.4608 | 2025-08-17 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e75ceb4-8a67-3c10-9638-154de914fe5d | -6.19003 | -45.44603 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cd628e9-d2b3-363f-8f3f-6b9030265406 | -3.15287 | -45.65256 | 2025-08-17 03:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61b29936-d835-3c00-bedb-65ae11de26ff | -5.95423 | -46.15791 | 2025-08-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12388fd6-d1d8-3d39-bac4-7e07f126dcf0 | -6.55022 | -43.01989 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4dacf86-6dc4-35be-8bdf-5f684f1610b2 | -8.03678 | -47.66911 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71e113c7-4947-3d1f-907d-9a5e2359b77b | -3.97234 | -42.528 | 2025-08-17 03:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 78845de6-7e32-35d8-aed2-2c14599a7b8b | -3.97751 | -42.52435 | 2025-08-17 03:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| ac893a01-6453-3a3b-a4cb-296829c939b7 | -7.19414 | -43.9718 | 2025-08-17 03:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd8d8d01-8fb7-3e74-8018-10b403713d41 | -8.57288 | -39.42828 | 2025-08-17 03:49:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4da393ff-50d6-3d68-aea2-31b180bf159e | -7.60908 | -44.93549 | 2025-08-17 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca901a6a-d26c-32af-b21f-7d0f481edb4c | -6.72628 | -44.04622 | 2025-08-17 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60b9b80-1107-3073-9840-59f34298d19b | -8.03248 | -47.66981 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f95958a7-9322-3403-b901-d7ee1c32de0a | -7.60412 | -44.93473 | 2025-08-17 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd71568c-c55c-3351-a6db-25630bec13d0 | -9.34971 | -40.58496 | 2025-08-17 03:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2f48f4fb-e344-39f6-b538-98fdc3dd9f38 | -6.18539 | -45.44162 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 718ed307-1219-3cda-a1cd-47e91fa4ad3a | -6.18009 | -47.27541 | 2025-08-17 03:49:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 142fc400-4e18-3e9f-9068-efc78e23418a | -7.42163 | -42.02819 | 2025-08-17 03:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c5b02bb7-557d-3b24-a397-cf3557b07cf0 | -3.94353 | -41.82933 | 2025-08-17 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f570ea0d-ae5d-383b-8bf9-fd6ac2156ed7 | -6.61992 | -44.46178 | 2025-08-17 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e806c9-3923-3c06-8d47-439b038ecec4 | -6.54433 | -43.02772 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1dc7defd-a425-35ab-b030-def03d06cb24 | -6.54506 | -43.02346 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a671f1c2-dd27-3eb4-b958-0df3acad7bb9 | -4.91725 | -43.24698 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9889ebc7-59d4-3c09-9d6f-b78ed3d70cef | -6.18649 | -45.4352 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ff9685c4-c42d-35fb-9038-e4271f753690 | -4.92108 | -43.2525 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 312651ef-06a6-37ee-acab-425e4ff722d8 | -8.50149 | -44.74039 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08f65136-3af3-3b41-a6ce-ebea455e33b9 | -4.92568 | -43.25333 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c3f153e4-e55a-3f00-8ddb-32df8d8d237b | -8.36298 | -41.4716 | 2025-08-17 03:49:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cba7b5b9-6d19-3e9e-9b95-653a9a7e9463 | -6.1793 | -47.27973 | 2025-08-17 03:49:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 210b42e7-911d-3563-9ea1-afb7d1591269 | -5.95533 | -46.15496 | 2025-08-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49ce4eea-1b53-3b70-9b8e-2b053d5f36ef | -4.91107 | -43.25562 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc3c3bec-cf22-3120-a1ba-15e3bb95921b | -8.9788 | -60.4964 | 2025-08-17 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5878ad1c-3f76-3336-b6c5-ff7db8a964b0 | -9.518 | -60.5268 | 2025-08-17 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d6c5986a-d71d-3fc1-ac60-c9f6ab433403 | -9.1895 | -59.6364 | 2025-08-17 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| cbe005b1-a91c-35c9-853c-e9461676a2ab | -10.844 | -45.3356 | 2025-08-17 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ed1f9916-c4b7-35dc-9b1c-8b4a65fdc142 | -10.8436 | -45.3586 | 2025-08-17 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 593097a5-8e24-316e-bb9a-9651ee0f0160 | -9.5179 | -60.5461 | 2025-08-17 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 16e8a4f5-a87b-3538-b07f-4aa4c662390d | -8.9893 | -61.7024 | 2025-08-17 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f5907a5e-7a35-3dd8-a699-077a7032e430 | -15.7681 | -47.80516 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3de913a-2ea4-3ccd-8751-0de7a268e5c1 | -13.59275 | -47.77093 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13ff7d6f-6e05-3269-ba2f-c2c416d09c8a | -13.59956 | -47.76458 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be1eb954-6230-3377-a2f8-8217d6fe8540 | -10.84602 | -45.37357 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9336a433-b6b8-3134-83bf-cee02fee5cdc | -14.58794 | -47.94675 | 2025-08-17 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64ea9f4a-e33e-3da5-957a-9d216126427b | -13.59063 | -47.7818 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0a8dd54-084f-354c-9e35-437673d79eaf | -13.57837 | -46.9877 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04ff3094-2cea-334a-9b63-b1ec29813530 | -10.8353 | -45.3182 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeedf900-9335-3378-9e37-c56940cf3550 | -13.59138 | -47.77793 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c81e1c1-3ad0-318f-8408-65c3942359bd | -13.60578 | -47.77345 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 059a2d75-7fa5-3450-acfc-68e6c2c0ecce | -14.18478 | -45.32976 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b16cc570-2d13-3ad6-adb8-c133b74aab6c | -13.60351 | -47.77289 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71fc1987-ab43-3b41-8f8c-0e3f4d8b4d9c | -9.27531 | -44.55978 | 2025-08-17 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aecb2cf7-76d8-309d-81b0-673f4d7a9c42 | -12.14053 | -47.91542 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5b6ab63-1126-3df7-9a10-d9a9cbaec501 | -10.85724 | -45.33351 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4ee5d551-7c24-3998-ad02-047db4b46af8 | -9.27616 | -44.55509 | 2025-08-17 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 211d2b1e-ed3a-3539-912e-b5d386f3c2ef | -10.83965 | -45.37457 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0a28ff80-8ccb-3ecd-a563-85a674b64ebd | -10.82854 | -45.3278 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e3b7102-5cde-38f3-b406-e26a98e570df | -10.82394 | -45.3306 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 024a672b-5b1a-3716-8c0f-c799377c4497 | -13.43469 | -45.89865 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cd323bc-cb7b-3553-a00e-386dd3a966be | -16.76191 | -41.93338 | 2025-08-17 03:51:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 14db4d6f-771d-3cc1-8bf6-8c1de5d68dac | -13.43556 | -45.89749 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e11a17db-0393-31b4-9e21-60fa04f72e1e | -14.93548 | -47.05886 | 2025-08-17 03:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97fb415c-f4cc-3104-a865-d5eeb0bdb8ec | -12.87306 | -46.08366 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0e617dc-c942-3c16-b03b-0e806d9cff57 | -13.4346 | -45.90269 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 014bcdae-5bb7-3d4a-b0dc-3f182d68f24f | -10.28964 | -48.33387 | 2025-08-17 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf06ec3-66c6-3b2e-8370-c250d3873bbf | -10.83836 | -45.36082 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a3a4446f-94fa-36c2-83de-d14257815474 | -15.14503 | -48.75735 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06bbef1d-da1f-34df-8a31-9dac2951795b | -14.93313 | -47.06483 | 2025-08-17 03:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98241a8c-4e03-3a31-92f7-230dbbcf6221 | -15.10619 | -41.0694 | 2025-08-17 03:51:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57a95e01-a598-3f1c-90bc-47fcc2c3f652 | -10.83932 | -45.3555 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7e715541-ffc2-3318-9f61-607e8c5762d4 | -10.83894 | -45.35176 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 493bd08f-5619-334e-8603-98aaa17fa143 | -12.82235 | -45.99176 | 2025-08-17 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95b1caf1-e229-3573-befc-dd72deceb941 | -13.58983 | -47.78591 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
