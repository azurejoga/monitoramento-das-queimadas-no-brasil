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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42e8b7ad-d338-3f7f-827c-feee9e149c6d | -5.88999 | -42.90953 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 6fc0cd3f-573f-3e21-ba79-7677347fa949 | -6.12903 | -42.86479 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b62a92ad-ed89-3a41-9ab0-bee3250de8cc | -6.34179 | -44.03151 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3836bc83-c3c9-3baf-a1d7-beb0d2f80c37 | -6.66545 | -42.3844 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 834cc33f-e47f-349c-886b-65c03327697f | -6.40233 | -43.06026 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b7726468-a6da-3d41-8605-37e7043f9943 | -5.76836 | -42.9516 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 995bfcd6-9969-364c-88b8-f7eba57dce26 | -6.40676 | -42.69409 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8352c970-572a-3aa6-821c-58efb5f2e803 | -6.34282 | -44.02581 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c097666f-9f69-33e4-b651-fb93bd44fad6 | -3.84668 | -41.56777 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1d14bb71-59c2-3616-9149-9444e3eef6e8 | -5.78931 | -42.97429 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 250a642e-af85-3399-b610-0ff7124bbebe | -5.88205 | -42.91359 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 5a93854e-9fed-3c4d-ac3b-eafef8771607 | -3.67078 | -41.76461 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b44af561-a6ef-3afc-9665-a4ff227dbf38 | -7.05399 | -42.769 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b19e48c2-3e68-3948-ae2a-a7aa31125973 | -5.92028 | -43.32622 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5d91612-3b94-3912-a42d-bcbbcc17bf9c | -6.13204 | -44.64075 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d17412-c85d-34eb-8243-3b969350e5aa | -7.29426 | -39.26983 | 2025-10-05 03:32:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c2ba936a-324f-3ad6-af71-de0846e41318 | -6.22041 | -42.92805 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af028054-642c-3c08-9f85-f239d495df37 | -4.87557 | -45.86304 | 2025-10-05 03:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5aff9a4b-5f6b-34ec-9746-2289d80b0dd4 | -5.76355 | -42.97878 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f76a1a3-5b98-3e0e-8074-623b34c4fc5a | -7.02677 | -42.78552 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0d86518f-d2cc-3206-b281-2aae73e4836c | -6.15865 | -44.66469 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 776a5269-1c4b-3003-8a19-c9e53c72d0f2 | -5.77438 | -42.9528 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 12e645b7-7429-3946-99d6-2397712edc97 | -5.99421 | -44.36551 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 138b0462-ea75-358f-8bd4-2a8c7a4b2053 | -4.64712 | -43.18638 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 88dd38c4-426a-3620-ae78-f880f620c5f8 | -6.35591 | -43.91653 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3af1e7ee-8cda-3e31-ad70-66b928e6acc7 | -6.46076 | -44.58984 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 26b1fc3a-e233-3200-bd47-a2849c91937c | -5.49375 | -42.80497 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed11915e-cd15-36e5-b01f-c4b26bbae426 | -5.06841 | -40.47377 | 2025-10-05 03:32:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 930ac6ce-e6ea-317e-9cbf-6a88000237ff | -5.89951 | -38.48352 | 2025-10-05 03:32:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0eaf7ec4-17a9-36a2-b2bb-fb2f2d2cd159 | -6.34235 | -44.03184 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d82f4154-c9ee-38f9-9523-8b2a3ff37278 | -6.15001 | -44.65555 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 55f3a812-4f89-3c1a-bce1-3cdd1c096ac7 | -5.92177 | -43.3246 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 300918ef-1ee7-361e-bc9d-6a0181f416ab | -6.14293 | -44.63819 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 921e637e-ee59-3736-a2d6-e9ed83efb555 | -6.78647 | -38.75937 | 2025-10-05 03:32:00 | NPP-375D | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1a642a4b-a900-3547-80b8-84dfd98fc2f2 | -5.78249 | -42.97761 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80c9df71-fed5-351f-9ce6-283a11f8c9a1 | -5.77993 | -42.92811 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 68872611-95bc-3c73-ac4c-b0ce3f43f98b | -5.78971 | -42.97686 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8c8c2a8-f8fe-3642-881a-0d81ad8a62ee | -6.35724 | -43.91707 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa710c2f-f4d4-3c4d-8d2d-173ff4352aa4 | -6.2563 | -45.35926 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1aff87e3-bec5-33cb-948a-ac78cbe584bb | -6.40245 | -43.06779 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8888dbca-252b-366b-88f6-69a445eff5cf | -6.21292 | -44.08012 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da69eb82-5bf2-3c57-8251-57f588bb5d00 | -6.37973 | -43.89338 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbab8806-eb61-3699-923b-1404f0ccff72 | -5.78342 | -42.94305 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| a3d3cc17-df4a-3dfb-bddc-974c5b3bcb37 | -3.8433 | -41.58763 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a9a077b-d8c2-3042-aa47-ff416702b951 | -6.16527 | -44.66614 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 876eeed7-8b48-34b9-8391-712052f3e354 | -7.02093 | -42.78436 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6e3b59ad-3257-30fd-a32f-d7c685cbfabc | -6.15525 | -44.64595 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcaedfdb-e714-3fa9-9857-e0da967e9b4c | -5.90999 | -42.89589 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 97c267ed-46bc-3f9a-832a-611040eb3f9a | -5.98872 | -44.35851 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72debbc7-1154-3548-b4fc-7dead46f6aba | -6.70956 | -42.83106 | 2025-10-05 03:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8ed8cc84-ea2c-36d2-a25f-e45c8aacebb0 | -6.14796 | -44.66704 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 82afc9fa-f395-3245-a2c4-ca0f470f1596 | -5.87466 | -42.54416 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 01bb9c51-dbd1-37a0-ad7c-12b5ba1ef098 | -6.11713 | -42.86237 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b04476fe-392e-345c-aad9-61a7fa8d7ef5 | -3.67653 | -41.76581 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| beb11ef4-8ac0-3e57-95dc-2af258f74fad | -6.28966 | -43.9197 | 2025-10-05 03:32:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9774fd6-26a8-3c4b-a2ae-8be1b921cfd7 | -5.77643 | -42.97655 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d2c404d-37ec-3f06-b2d5-bf0c48bf5b1c | -6.43856 | -44.15818 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0b8295a-a7e0-3e5e-be5b-e550fc0ee908 | -6.41068 | -43.04824 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bb2fac33-a131-37c6-bcf2-d3863496f2e5 | -5.98115 | -44.3628 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f97de0a8-00e7-3171-82b9-27bf3fe821da | -5.91597 | -42.89714 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 401144e4-4189-3db8-92ad-d4150fd8a8ec | -6.02415 | -44.01901 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41c609ad-feba-3564-a5f5-7274e9684087 | -5.92793 | -43.32574 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5a230887-6d40-3959-b090-b17c691ce8a4 | -6.60982 | -43.72804 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa059879-4028-3d22-9d7c-cabe4084eb7b | -5.7583 | -42.97316 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4825032a-01eb-3cbd-a474-853419ac89b1 | -2.91053 | -40.46592 | 2025-10-05 03:32:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d8244d0-de02-3181-b010-ac70f82eeca5 | -5.49459 | -42.80035 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b4ef58a-599b-3ca3-8e2a-5162045ded7b | -6.06266 | -41.2435 | 2025-10-05 03:32:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c61f5a8-7928-3d6e-8eda-7c85564749fd | -6.40578 | -43.04987 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b14042d2-4ea6-3df5-9955-05dbde7a087f | -6.14238 | -44.65975 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2136ff12-1c55-3894-b40a-8d5f04876054 | -3.84968 | -41.58466 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ac19e4ec-aa07-34aa-982e-b6801d20100c | -6.25746 | -45.35301 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad12e7d1-e55f-3651-8092-40abad5c1851 | -5.98398 | -44.35657 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 874ec3fc-db92-3ac9-932c-9da8febd8eb0 | -6.14856 | -44.64491 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 7224a355-b810-3a50-8316-188d6ed93277 | -6.69436 | -41.95368 | 2025-10-05 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a291080a-0305-3905-8874-ebc8b8e84e6e | -5.26231 | -39.27163 | 2025-10-05 03:32:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f8cd2d50-d0e0-389c-a84e-36fecd7294bc | -5.9746 | -44.36153 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 345649c0-783c-367e-b464-22df24996f6e | -5.83324 | -44.45392 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e216219d-f99b-3da8-aba5-8291826c5b92 | -5.78446 | -42.97137 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd322d65-c550-3110-b955-a155762e9f65 | -6.40756 | -43.06581 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 15ef902d-d48d-36b3-9068-8d98362773e8 | -6.33114 | -43.45881 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6544b4a4-a6ba-3416-a911-377c2395fe7e | -4.64174 | -43.18036 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d8ca3efd-8bbe-3d5d-978f-7971b2065f32 | -5.58782 | -43.40593 | 2025-10-05 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6c7ad0f-ad1e-398b-9926-6dc27f8cf055 | -4.44896 | -43.23153 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cf976694-65c9-373a-85f0-ed550f135fa1 | -7.28964 | -39.26905 | 2025-10-05 03:32:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e2511d25-908e-3a0e-8e98-5e4764f41ed4 | -5.26892 | -39.26639 | 2025-10-05 03:32:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed30ed4b-219c-3d9f-b2d8-631fbd6801fc | -6.15206 | -44.64411 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5f915018-2175-39a9-9866-285840e236ce | -6.15204 | -44.66317 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| bd8978ea-2ca8-3e07-a5ed-82ab7f88a95d | -5.98953 | -44.36346 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6de0ee7-bed1-31b9-88b8-fcc928364504 | -5.77598 | -42.94374 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 7b79866e-ecc2-3f3f-87ae-51875bd9ba90 | -5.78077 | -42.92355 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 0565e0c9-c041-3987-ba44-84ffc8775e54 | -6.38065 | -43.88827 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aefb09c-55a4-34ba-b35e-bb1cb94129b6 | -5.98219 | -44.3572 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d8c32c4-9454-3d10-908a-bd340e2e6c3d | -4.44807 | -43.23648 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9302b0e5-b294-34aa-9918-889513230d77 | -3.86853 | -40.91098 | 2025-10-05 03:32:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8356e4e-d6d0-36fe-a793-baffb4a0c98d | -5.85101 | -42.81019 | 2025-10-05 03:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9aa7d3e9-5d26-3eb6-9a2a-ceb8d2b029b0 | -6.44504 | -44.15915 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 880aedf1-cc4e-3d31-aeea-e2fa59feb91a | -5.55002 | -42.66452 | 2025-10-05 03:32:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ee24339-d817-3d12-9cff-8adb3c014929 | -6.2529 | -45.33916 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d41ca9c0-9345-3fc0-8729-dea54a1f0f32 | -5.93259 | -43.32856 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0da12402-3610-32ac-8b7f-af62f9af8987 | -5.48689 | -42.80226 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README24.md)
