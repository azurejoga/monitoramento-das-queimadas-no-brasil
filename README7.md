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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 392d11a0-6fe0-3b52-9bc8-2b99c6ac9a54 | -4.5451 | -43.552898 | 2024-10-29 00:27:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26dac3ef-4bca-3101-9b42-922b862697be | -4.5467 | -43.559799 | 2024-10-29 00:27:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe4e5e3-3032-35c2-bd51-b549c30fe192 | -5.532 | -47.696499 | 2024-10-29 00:27:59 | METOP-C | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2670c19-fc1d-3d6a-bb13-54243b0ff83b | -4.7152 | -44.1609 | 2024-10-29 00:27:59 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ace4631-30a2-3702-a042-01d85df85205 | -4.7038 | -44.1562 | 2024-10-29 00:27:59 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 341be1df-b03b-3207-9d10-1759d0363f60 | -4.7053 | -44.163101 | 2024-10-29 00:27:59 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 985092cc-5717-3cd4-ace3-cbac9cd9efb6 | -5.1111 | -45.9524 | 2024-10-29 00:27:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17c604b6-dc61-3e72-a645-c32860d338d2 | -5.1128 | -45.959999 | 2024-10-29 00:27:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1605764c-f7f5-3ebd-97f3-e308d316ff5b | -3.8993 | -41.0275 | 2024-10-29 00:28:00 | METOP-C | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ee6fda0e-40e5-3e1c-badd-1b9f09a91690 | -3.8631 | -40.6954 | 2024-10-29 00:28:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b32f557b-e5e3-3c4e-9fbf-c0cc36f0c0b9 | -4.4142 | -43.028099 | 2024-10-29 00:28:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7948f259-b5ee-3b6d-997d-7116f8872f2a | -4.4158 | -43.035 | 2024-10-29 00:28:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57cb7de2-ae16-380d-87b6-05e963d8f75b | -4.6531 | -44.1604 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbb6464f-2691-3051-8dbe-9337486d6804 | -4.6712 | -44.149101 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a667cd98-fe39-3ce9-a26d-6e0a54472835 | -4.6728 | -44.155998 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89faf762-2e0e-31aa-9811-c776519cbf57 | -4.6744 | -44.1628 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af019e0f-54d7-332f-bcbe-e44e0b4f1ca4 | -4.6759 | -44.169701 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27b57905-e35e-348a-a056-6d2f77dff6e4 | -4.6775 | -44.176498 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67237988-9f2d-3592-9435-5f098f3bd79d | -4.6791 | -44.183399 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 687281fd-ade6-31af-b35d-32a476b74f8d | -4.6806 | -44.1903 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9dc68b-57f6-3835-a97c-dbe24f3fb9ff | -4.6614 | -44.151299 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6c22ef0-bc69-3c1c-b623-d1c0cbf98b4f | -4.6629 | -44.158199 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6c7048-7dfa-3571-8fd5-1a239fa46a7b | -4.6645 | -44.165001 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 201e0495-abeb-332f-9848-c7d758d06a13 | -4.6661 | -44.171902 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f92505da-2e7f-33f1-8fa6-4026f44bcd11 | -4.6676 | -44.178699 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efede5bc-909c-3c67-9ff6-0b6f7afcad8c | -4.6692 | -44.1856 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3acec958-ef9e-354d-bc37-697308afdae0 | -4.949 | -45.4165 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adfb7b86-2867-32b4-a16d-85adb51d9572 | -4.9506 | -45.423801 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc6891f5-d485-3423-8e61-5921cd852e5b | -4.9523 | -45.431099 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf57a9d3-bd81-39ee-a562-115840c8f360 | -4.9539 | -45.438499 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37372282-f79a-3e03-9402-7ef8cbf98461 | -4.6516 | -44.1535 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 380157f1-f10c-3a20-bf1a-4801ae1282de | -4.6547 | -44.167198 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97c139f4-487a-3674-aaac-c77feed0d1b5 | -4.6563 | -44.174099 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 126a948b-f640-37ae-ab4f-3c79e136f733 | -4.6578 | -44.180901 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3576e5-a8e4-3343-b5a7-dc7542aeca00 | -4.6594 | -44.187801 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 827e0c9d-ab8f-3ecc-804d-d8291f752f1a | -4.9391 | -45.418701 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca7553e2-355c-3807-a13b-5a22577f9d47 | -4.9408 | -45.425999 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bed0cfe-2e1f-3e70-9942-daaab372bab8 | -4.9424 | -45.4333 | 2024-10-29 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5bb4a7b-da2d-32eb-9a5a-a05e8fcb8fe1 | -4.6433 | -44.162601 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bec20c82-057e-3af8-b8d3-9e736d6951c0 | -4.6449 | -44.169399 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a482d5d9-bd16-384b-99d0-78ac1cd1648e | -4.6465 | -44.1763 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7fa4124-85e6-3222-933d-a970f90da833 | -4.648 | -44.183102 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80fa56f2-0f26-3165-a9f9-4199149aea69 | -4.6496 | -44.189999 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0b843e-5b9a-381f-886f-c8b8e0644f68 | -4.6512 | -44.196899 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3063a10a-78a0-36d4-a6f3-5ee58def2e78 | -4.6367 | -44.178501 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03810604-d713-3c04-987e-94cecd641cd9 | -4.6382 | -44.185299 | 2024-10-29 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6a59906-de43-3e65-ac4a-8f6bd5112ce4 | -3.955 | -41.4884 | 2024-10-29 00:28:01 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 386cb7c2-ee3c-3ae9-bdfc-a19f3629fcfe | -3.9567 | -41.495998 | 2024-10-29 00:28:01 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 45456093-a388-3b28-8982-e5d4bc339a05 | -3.9585 | -41.503601 | 2024-10-29 00:28:01 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed7c7abf-aa0d-3ef7-9893-15a85a58a689 | -4.6225 | -44.297001 | 2024-10-29 00:28:01 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd803d1a-55fc-39c4-899a-536ba1fec951 | -4.6143 | -44.306099 | 2024-10-29 00:28:01 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7af1e7db-f7bc-366b-baa1-e82e88d65d50 | -4.6158 | -44.313 | 2024-10-29 00:28:01 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dac2336-aacc-382d-9ed8-901ff3cff141 | -4.4957 | -43.922501 | 2024-10-29 00:28:02 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c71c193-dd2a-3e11-a36b-7e7b861a2552 | -5.0224 | -46.472801 | 2024-10-29 00:28:02 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| daa3e350-5ec1-394d-8bef-0a1976fadcad | -4.3286 | -43.508202 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a318028-76c2-3911-a4fa-d5c5135711ba | -4.3302 | -43.514999 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc0b2371-7c66-3743-94ea-97f0b35c2a6d | -4.4379 | -43.9856 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a813073-3eab-3683-b3b2-51779b8a608a | -4.4395 | -43.992401 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87d5ca20-223f-3cd4-b4bf-08b36260b882 | -4.4281 | -43.987801 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12de48aa-3237-3d5e-9f64-a7e518038d51 | -4.3554 | -43.7603 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff0a2c09-f53f-3950-b969-a7fe810c4c49 | -4.357 | -43.767101 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87bdc04a-e421-3132-9a10-7c8c63bc2f62 | -4.3585 | -43.773899 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48d784f2-8350-3624-a87a-8b9e99bea3b6 | -4.344 | -43.7556 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe970eb-dbbf-3d6c-83b7-5bb818a6e438 | -4.3456 | -43.762501 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 178469ff-1d0b-393e-9e45-9c0d5c168921 | -4.3472 | -43.769299 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6cf3987-68df-3ae9-9807-bf63218abec1 | -4.3487 | -43.7761 | 2024-10-29 00:28:03 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef994e0-e38d-39a0-84c0-4f4240985951 | -4.4898 | -44.348301 | 2024-10-29 00:28:03 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73068bbb-b656-3ef7-b9a4-381683da7be9 | -4.9733 | -46.483501 | 2024-10-29 00:28:03 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f1fca6e-7dcf-39fb-8d50-104beaa240c1 | -4.3961 | -44.253799 | 2024-10-29 00:28:04 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 052b32f7-7d44-380b-ae05-7960ef826932 | -4.3977 | -44.260601 | 2024-10-29 00:28:04 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4dea2c29-644a-357e-a148-bc258c5b8e85 | -4.6856 | -45.800201 | 2024-10-29 00:28:05 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4c6a78d-06b6-35d3-a4a5-9fe7ad693754 | -4.6873 | -45.807701 | 2024-10-29 00:28:05 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90093a30-c032-3a98-a602-19c9e7f4a2ff | -5.6084 | -50.042801 | 2024-10-29 00:28:06 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 940432bf-eec0-3afd-8dbd-3d7ba5d65fb6 | -5.5219 | -49.787601 | 2024-10-29 00:28:06 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab3fcce-88ee-30b0-b2a7-f3d41f39e6be | -4.3396 | -44.548401 | 2024-10-29 00:28:06 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d96f1bb6-63a4-3482-bbdb-556aeae8d91b | -4.3412 | -44.555302 | 2024-10-29 00:28:06 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a66d20ec-8014-3b65-a2c3-8fc31f5e348d | -4.0323 | -43.251301 | 2024-10-29 00:28:07 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e75723bd-2924-3f47-a64d-9776f72cbeec | -4.0096 | -43.242001 | 2024-10-29 00:28:07 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 737c5082-bd56-3b1f-a002-9563bb10b354 | -4.0111 | -43.248798 | 2024-10-29 00:28:07 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 082c91b6-7409-38fb-aa22-bde150cf7abe | -4.1404 | -43.7225 | 2024-10-29 00:28:07 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29bf0cef-35ba-3ae4-b90e-57513d9a7da3 | -3.8928 | -43.138199 | 2024-10-29 00:28:08 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ffeb645-35ea-3186-8a87-fad5c08ae234 | -4.0892 | -43.948898 | 2024-10-29 00:28:08 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7c10848-021b-31c8-b480-65f65c6dcfe0 | -4.0908 | -43.9557 | 2024-10-29 00:28:08 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20dd0d9b-8bdf-3bd0-8006-00004e5e778b | -4.1454 | -44.194599 | 2024-10-29 00:28:08 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8989eb41-7fac-381e-b889-15989a9bd782 | -4.147 | -44.2015 | 2024-10-29 00:28:08 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eac86f4-9bb6-3d97-ac4e-a5f2b390c5b7 | -4.1372 | -44.203701 | 2024-10-29 00:28:08 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6cabc48-ae20-365b-8fed-d49660a30e58 | -3.1714 | -40.2062 | 2024-10-29 00:28:09 | METOP-C | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ca6a68f2-a9bf-3a69-a015-933e65abc1dc | -4.5222 | -46.0341 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b82c326-870e-3a66-b764-2b1827d068c8 | -4.5239 | -46.041698 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6a1c7e5-8cfc-3507-97df-0050926374bd | -4.6329 | -46.5247 | 2024-10-29 00:28:09 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2733ba57-7bd9-3b07-a760-38988be630b1 | -4.6346 | -46.5327 | 2024-10-29 00:28:09 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6c2d0f-7386-3fab-9298-f83b1f7eed39 | -4.6364 | -46.540699 | 2024-10-29 00:28:09 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 478d7ca1-e2d3-3841-8ce8-79d2f013971b | -4.4868 | -45.922798 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5fa446c-4dea-377b-9833-484d61f4596a | -4.4885 | -45.930401 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcf77f8-2a5f-3d94-b314-3564db0fd039 | -4.4702 | -45.895 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7466637a-7fbd-31d2-89e5-1fb1a600eb8a | -4.4719 | -45.9025 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd4a5b01-e9cc-3d24-909b-8a5049c6df61 | -4.474 | -45.957298 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd96245a-c3f2-3082-9340-775b8d0e1ff2 | -4.4757 | -45.964901 | 2024-10-29 00:28:09 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55b576ce-e3c4-3e3f-88e6-cdc1cab0ca24 | -4.5456 | -46.5942 | 2024-10-29 00:28:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1dd76af-6d7a-3441-bffa-f4fa25ffb349 | -4.5474 | -46.602299 | 2024-10-29 00:28:11 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
