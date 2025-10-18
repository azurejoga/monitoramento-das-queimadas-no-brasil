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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7bc43af-ab8c-398a-94cd-95592b132761 | -4.11687 | -42.90733 | 2025-10-18 04:27:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4a94ef5-674b-352c-a890-c22dfcba54b9 | 1.75709 | -55.98721 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2647ccef-3ab7-32ee-be8f-273ed241ffc1 | -3.69608 | -49.56417 | 2025-10-18 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dc05e5a-2c54-3a14-9a51-e09107f68f3c | -2.68944 | -48.70709 | 2025-10-18 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37e8c362-2109-33cd-ab85-312900c019a1 | 1.76858 | -55.93521 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52ce3408-813f-32bd-9efb-f298024c2ad5 | -3.06315 | -43.21892 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 546bcfed-3724-3cf1-9b2b-184b2e1dc757 | -3.1227 | -49.21806 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b674d029-d7e9-391d-8db6-b0897db2c554 | -4.14707 | -44.05729 | 2025-10-18 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fba77e1f-358b-383d-ab0c-5a1a7eccb397 | -4.00035 | -45.50705 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91395989-5845-32fa-8af5-3d6a4c3df430 | -2.66058 | -47.86728 | 2025-10-18 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 415e2dc6-358a-3110-8883-47293a06da80 | -3.35041 | -40.42259 | 2025-10-18 04:27:00 | NPP-375D | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 747e35da-4d95-31f6-9952-63032ef333c2 | -2.87541 | -50.73082 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cec81218-c6e1-3522-90b7-e3779d1de04c | -3.85332 | -41.586 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1512eac-e016-3ced-9fe9-a44be79bd17a | -2.34624 | -44.83982 | 2025-10-18 04:27:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46b6e511-dec8-30eb-a6ae-18f3bf67af05 | -3.46903 | -47.68256 | 2025-10-18 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2455c1e0-b36c-32b1-89df-2bdc10469eb8 | -1.18441 | -54.2139 | 2025-10-18 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c93f44d9-72c7-3265-9c58-503d75a876c2 | -2.87659 | -50.72355 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90548a35-1e09-3a59-a606-99c86dbf588c | -4.45535 | -43.23013 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 65d00b5b-19ec-377f-8a52-4d8005001578 | -3.29583 | -50.00673 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54cda5a8-54c8-3738-a084-e75be9db8ccb | -3.14847 | -50.24996 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 19889279-55a0-3c0a-8e0e-04b83e5d5c40 | -3.84848 | -41.56604 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f8fddcc4-7fe2-3f14-ad08-4821e271f3b0 | -4.45414 | -43.23805 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 837a9073-d96b-3425-af5a-e5577d2d9e44 | -3.05795 | -43.2063 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 006dec04-cfeb-38a1-90cd-a8b91183458f | -3.45319 | -50.09616 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 195d5291-9133-3356-b3fe-f3b5f08a95c0 | -4.40111 | -44.08447 | 2025-10-18 04:27:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f42aeaa5-e46a-3b8b-8c5c-541213a79cde | -4.53391 | -44.79913 | 2025-10-18 04:27:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab8b71c3-e5c1-355f-9a4d-dbac1f8eb6e2 | -3.8385 | -47.40305 | 2025-10-18 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b6ecbc3-3f2a-307d-b1fa-51da47aea8fd | -4.05501 | -43.21291 | 2025-10-18 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2b12b1a-1586-38ef-8c33-a73a1741f219 | 1.76707 | -55.92512 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3177ddde-f04e-3901-b77b-ba74f89b242a | -4.44827 | -43.22903 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 117d6d6c-d57f-31ca-9c2b-7b5795f44c0c | -2.15094 | -51.96424 | 2025-10-18 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 245ad94d-2a7f-3b9a-8866-f489d83f6c3a | -4.49781 | -46.49029 | 2025-10-18 04:27:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02a88bc9-f0a4-3877-b18e-ebb80d724369 | -2.11929 | -56.88977 | 2025-10-18 04:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ec6d8aa-de61-3b4b-b2b6-645ac9f0fc94 | -2.686 | -48.19961 | 2025-10-18 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9042d05-86c5-3898-9a31-81a48002c029 | -1.83182 | -44.88745 | 2025-10-18 04:27:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 660f26a8-7c08-3219-a7d3-04bbb47de2c8 | -4.45181 | -43.22958 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0026bf2a-7f06-3ede-a57a-3ed753959525 | -3.53709 | -41.71595 | 2025-10-18 04:27:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 351df0a7-81ca-3642-9828-02fa8d587650 | -3.25092 | -45.9663 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2d5d483-26fc-38be-9d76-2a7b32433423 | -3.06724 | -43.21563 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6c4c898-0c89-3acc-869e-6b51aaf01533 | -3.59433 | -43.04601 | 2025-10-18 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88ede4c0-bff2-31f1-a50c-03c3bf2c2da8 | 1.76743 | -55.97047 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11371aa0-edc9-31da-af4e-390ae01c17f6 | -4.44533 | -43.22451 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 434b64f3-0cde-3e77-a959-c7ca4f8d9aac | -3.06434 | -43.21125 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00dc18f5-ae40-3920-bb8b-b7cf4b5e2559 | -4.66617 | -44.80126 | 2025-10-18 04:27:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48a69173-e46f-397c-876f-693943f07c2f | -4.44948 | -43.22109 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37466e93-497f-386f-898a-64986d4ac83b | 1.76597 | -55.96069 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20487f58-45c4-3a7b-a207-8bb58f1e39d6 | -3.49746 | -51.54835 | 2025-10-18 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb7f26cd-a21b-3bf3-b4ba-0e03c9950afe | -2.74367 | -49.38812 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a623095-7645-3011-a44c-d24f6f02f6ad | -3.35495 | -43.17105 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4794be35-3dc0-3e25-ac82-a3fd0d57cb23 | -4.00422 | -45.50411 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4b7bf86-ccbc-3280-811f-1c9f9eb09bdf | -3.99165 | -42.48873 | 2025-10-18 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c87a2e66-b540-339f-b017-b967fb650597 | -2.709 | -49.41059 | 2025-10-18 04:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9402561b-c83d-361d-9853-25f1fc6267ac | 2.02312 | -55.83479 | 2025-10-18 04:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 949e8f8b-f615-3d5a-b26b-1f88b64e8ed5 | -3.65675 | -50.27062 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b67df3d-b437-3be2-9c02-efadb268e4ec | -2.91018 | -52.72605 | 2025-10-18 04:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d4fd89d-0eae-3886-995e-e68c431afaae | -2.12016 | -56.88467 | 2025-10-18 04:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d86ff58-7162-375e-b201-d59c1708d21f | -2.74745 | -49.38874 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd579aa6-f5e9-39e2-824b-90c5e92d9510 | -2.02123 | -47.55066 | 2025-10-18 04:27:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab2cf35a-0f20-32a1-87f3-302d8c2a0ed7 | -2.70739 | -49.85867 | 2025-10-18 04:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd19ed86-acd2-3f06-9fb0-0802666bc919 | -2.7399 | -49.38749 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1dce8cb-c9fd-3689-be4b-60f7f0e91622 | -4.45475 | -43.23409 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0aedf081-657c-3816-917f-83da41e808e5 | -2.74293 | -49.39269 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2e9dac9-c9dd-3256-bf3d-9fe9f243a512 | -4.45121 | -43.23354 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b4678a0b-d32f-301b-8049-c9d1106c014e | -5.06501 | -41.21053 | 2025-10-18 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c9f1433-a440-35d9-95f0-c88b9019e2f5 | -2.86605 | -50.73671 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 634d4af0-3ea1-3080-b3e3-b2a69ae04210 | -4.07338 | -43.39538 | 2025-10-18 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc71f0e2-46db-39c6-afb1-bd6f64d81d49 | -3.99775 | -43.28033 | 2025-10-18 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2f88404-ee30-302d-be6e-c8329e9dd2fc | -4.40579 | -44.36484 | 2025-10-18 04:27:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbc79aa5-c434-35ae-85aa-c1f1ec6a7e58 | -2.70662 | -49.86349 | 2025-10-18 04:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f4e3431-3035-32a8-a116-b1927106c938 | -4.46183 | -43.23519 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0eae3f84-8f56-352e-a411-6c1b0596e413 | 1.76116 | -55.9714 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b23dca20-4565-3fbe-b21b-deb8eb51e339 | -2.80826 | -48.66452 | 2025-10-18 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de43d003-f2a3-31df-813d-83e8ee6f201b | -4.00449 | -49.0197 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a8c1f749-5e16-3bbc-abdc-477c2cb7f62a | -3.45673 | -47.62691 | 2025-10-18 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 627da815-bca3-3620-9296-dde8f2e1ff88 | -2.876 | -50.72719 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2500ed72-bae0-3ff2-802c-c852601cbf6b | 1.50336 | -56.07008 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bf276de-2ad1-35e7-b5d4-ef61d76426a7 | -3.8509 | -41.57603 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4e3dc758-163b-3ef2-98a9-d55a94e164fc | -3.1493 | -50.24491 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 678de378-a6f9-3607-a01e-8191b07707cc | -3.46017 | -47.62747 | 2025-10-18 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e0ebcd4-c475-37a7-995d-a8329e00299f | -2.37247 | -48.29248 | 2025-10-18 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52244325-411b-3659-b56e-cdddd9f1645f | -4.21693 | -43.40009 | 2025-10-18 04:27:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80df6b1a-68be-3fcb-a70a-c5e333780bc7 | -2.73916 | -49.39206 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6003b9a1-648f-3e36-a338-3c2d6ab00d8b | -4.41356 | -44.85619 | 2025-10-18 04:27:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82c23812-0d3b-318b-8144-ef861af97498 | -2.8801 | -50.72786 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14756911-8904-3752-9590-fe8cffeb75a2 | -3.97573 | -42.49494 | 2025-10-18 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f7ff342-2eca-3597-8b8f-a86b8db78cb0 | -4.44594 | -43.22054 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80ebc450-2acf-3d60-a64d-69aca6bb8dd1 | -4.82308 | -44.42098 | 2025-10-18 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8547202e-8ca6-34e3-815e-c1effaf04a00 | -3.52637 | -50.30845 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fcbb7e4-aea3-360c-b114-70f1fe947195 | 1.75821 | -55.97283 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afd15300-259d-3897-b5cd-a9c9c88cff97 | -4.00127 | -43.28087 | 2025-10-18 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c99dec5b-208d-3d42-ab20-c547698a3b94 | -2.15616 | -51.9605 | 2025-10-18 04:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e06a2c6e-3a46-3912-a761-e414a503fa0b | -2.86956 | -50.74101 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e7b4ae2-87c3-367a-ab0f-ebfde187405a | 2.02237 | -55.82984 | 2025-10-18 04:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35a5234a-2cbb-3a95-af66-44a2b83d549d | -4.37281 | -46.53149 | 2025-10-18 04:27:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abb9101e-b428-3793-a2d0-cd0a9dfe4576 | -3.49676 | -42.72419 | 2025-10-18 04:27:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68a9e35a-1d7f-39da-b6ff-1186a8e8d9bb | -1.61618 | -46.66461 | 2025-10-18 04:27:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c8d51f0-9b84-372d-b358-eb6976dc93f9 | -2.36652 | -48.51394 | 2025-10-18 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce771cb0-cd02-3cc5-acf4-e22a51139e16 | -2.35951 | -47.54316 | 2025-10-18 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3cc8718-30a8-3ef3-b253-8f4b6dd180a2 | -2.71203 | -49.41578 | 2025-10-18 04:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d02412e-36c3-3dc3-a95c-1ad643ace475 | -0.90369 | -47.55117 | 2025-10-18 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
