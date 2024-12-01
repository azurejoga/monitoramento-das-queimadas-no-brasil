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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24154821-aac0-35c8-85a0-27cc2a9f9571 | -2.64438 | -49.91201 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac5c577-3771-3b90-a96f-1c098432bcb7 | -2.61305 | -51.81134 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a59d37e0-5a2d-3e3f-a57d-7940d36cf103 | -2.68951 | -51.99263 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3fa421f-f5da-3eef-a29f-ec5d128f648f | -3.09885 | -53.25808 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb85c8d7-5e9d-3d35-8cc9-e69d0b92a12e | -3.9628 | -48.8296 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e544b4c-6495-34fd-a8aa-227d946b0781 | -1.32145 | -51.67679 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 117d371b-f426-372e-ba03-2a2f8a6a2cf0 | -2.94134 | -51.50386 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10e536ee-536a-3a6a-b221-77fd1f733889 | -2.9835 | -51.45567 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a917a9b-ba72-3a52-b4af-72642bed5705 | -1.08273 | -53.20216 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 565726ba-5f50-33ab-82c9-6a518ee2b2c0 | -1.32203 | -51.6731 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f94c91da-ddd4-368a-940b-552612e7b257 | -1.42852 | -54.94807 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e669ad-807f-3208-a356-6d51c825ff7b | -4.06299 | -49.05907 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5df8edd-834b-35a7-83ff-920ad1779f63 | -3.79693 | -46.694 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ab61681-3d7b-3ce0-8500-4c9219b34213 | -2.87361 | -53.98894 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c44d7f76-faa0-3683-bb2a-842db062d526 | -3.82419 | -50.13581 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ba69d5b-c746-37fc-a0c7-0425e3cf1cf5 | -3.84932 | -52.31507 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c12b14e-0107-3bd3-959a-5f5a23794f06 | -3.40238 | -50.66374 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7be03347-a281-3df6-b711-6bd98b3d6855 | -4.01566 | -46.99565 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9016179a-0341-3dbf-a775-725977777d59 | -1.0481 | -51.81411 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f75b334-c212-3867-9647-b8dbfb6dceca | -1.51931 | -45.90688 | 2024-12-01 04:44:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ae8172d-bc11-350f-a7eb-4269f087ba19 | -1.49857 | -54.95187 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9a3dad4-e042-3c76-b940-059915d121f2 | -3.30467 | -53.83213 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52efc12b-af16-300f-b476-a057058bd7c8 | -0.60184 | -51.69642 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ede13537-020f-3ce8-8ba7-1a4999003a31 | -1.57681 | -53.86459 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 044f339b-7ed5-317d-90d8-a51946f1d97f | -2.5937 | -46.93773 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bf23cc6-a6b5-3f1d-87c0-3a8823246a0d | -3.00906 | -53.21069 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce9cd211-7aa8-3e60-8aa2-52dfb8d0310c | -3.84338 | -52.02438 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85b8e5bd-1aec-3cce-8ab5-b53a463cfac9 | -0.18293 | -51.41299 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c8dc961-6738-3b39-9096-9d1348b9d120 | -3.97355 | -54.08664 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f455baa-51ae-305c-8674-f5f31ae2ffc8 | -3.28431 | -50.16804 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6906bcc9-66d2-3ad9-8eaa-81e1d8d432fd | -3.4428 | -54.12398 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45deb756-ff5b-3b25-b6fe-4017b73f99e5 | -1.30246 | -51.73063 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66c4a3d3-3201-34fc-acf0-0394055c7030 | -3.5132 | -53.78683 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fc59cc5-c550-3b28-bdb0-86cfc3b1c009 | -3.30482 | -51.10784 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 566f1712-9726-36fe-9504-806e3d26f19e | -2.19255 | -50.54528 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ebe2a19-7383-323f-8613-ee92a25b9277 | -3.68108 | -50.24792 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb4225ed-da02-3cfe-b98e-498ccfeb6e9a | -3.96444 | -49.90923 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 975965ef-c5bb-3b80-80ae-d44fbee7cbe1 | -4.69616 | -42.39917 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9abc4f8c-c653-342e-892d-248ea9a36cfa | -2.11668 | -50.33857 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6de79811-73b6-3d7b-a3fa-7dcc4dde7acf | -6.30584 | -43.8472 | 2024-12-01 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3b63f01-0584-3cc3-a761-874830723cdd | -3.85157 | -54.22377 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7350bd7-bb5e-3b51-ad7d-60e56d207282 | -3.6931 | -51.80415 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1987caa-d2f7-370a-9199-a6564dfc4d40 | -2.39721 | -50.49199 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adb00413-b37c-3330-b24e-8f6bff928472 | -1.64269 | -53.86574 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91eeab6e-d00b-36c7-acf4-e6db2c866145 | -2.77199 | -55.34915 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c83e1310-84f5-3d2e-a87c-073faaea5009 | -1.64233 | -55.06634 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3883e23d-d066-32a5-82f5-65fe81894066 | -3.82094 | -52.25397 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 012544a5-5973-3212-b803-153cae0feded | -0.00879 | -51.16512 | 2024-12-01 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 94678f68-252b-3d3b-9d92-41a50fa86d7f | -3.34328 | -53.29007 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dabeed08-08e9-3413-951f-b51d3b8f3bed | -3.73276 | -49.94088 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f45ba513-e059-3066-aa53-e7878cbbb97e | -3.17761 | -53.25633 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf9c5b3-8caa-3164-b220-1ad8e9b586a0 | -4.01489 | -46.99434 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87e63f68-189e-396c-ab19-0abb9a353a4b | -4.20324 | -50.67297 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b163726f-cee8-3ff6-a540-030b580a4c44 | -1.25872 | -51.78465 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8da524f-c9d4-3e5e-b0be-7abfc2854d53 | -1.59782 | -52.28568 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9adc57d-5e51-3230-a405-61f30cc19483 | -2.44723 | -53.99954 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c925922-10a6-3c2b-9963-f82f5e1e7dc6 | -5.21882 | -47.20618 | 2024-12-01 04:44:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81ebffda-483a-3f93-8ed6-8dd3a83d3cf7 | -2.74746 | -51.75704 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e028db15-9ca0-3683-9b77-ed360501e5bf | -2.83584 | -54.10378 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37378a34-13cf-3766-93b5-df721c53fdc0 | -3.30089 | -50.27669 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c76be05-923d-3506-84a8-3d09a8f0cedf | -2.66909 | -46.60014 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95e18a50-71fe-3711-820a-e5d21946976b | -2.76858 | -54.19037 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18fd9bea-1e2d-3925-89cc-ad7641dee8a4 | -4.06216 | -46.67799 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5fed590-14ca-30e5-87b6-375d8a978cdc | -2.04651 | -54.6614 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b5b2a21-6473-3438-8d7f-0099c469c303 | -1.07072 | -51.76025 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 657048f1-e6b6-32c4-8888-1267e4430394 | -1.45723 | -51.50253 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd1725a9-5058-311d-9124-4f52ee1cf8f0 | -3.49579 | -53.82398 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f409ad3c-ad34-38e4-b299-86cec8cc735e | -3.09407 | -53.72655 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32027927-de4e-3908-a02f-abcab096cbb5 | -1.51861 | -45.91144 | 2024-12-01 04:44:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eed4a903-d553-31d1-bd61-b228ece4b77b | -1.48 | -55.38643 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 279fc324-32c6-35b3-9a1c-eb9af6965346 | -2.8562 | -54.0977 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 178d6050-75ba-3a72-872e-19deaad7bdb1 | -3.24904 | -53.64809 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1361d229-e445-326e-8786-aba42ca7e06d | -3.56144 | -48.67199 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bed4dbdd-9c68-3bd1-bdeb-28c5ac097d3d | -3.5937 | -50.37583 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acfeec09-3af2-341c-987b-8bb9cfaa5a5a | -3.86832 | -52.39434 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2f5be50-f19b-3af7-9a7a-61d97c126496 | -3.47956 | -50.34681 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1f32a77-5cf9-30af-bb2d-1a4d481623be | -2.27106 | -51.14444 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e248fed-8d0d-3a28-b3b0-d8bae67f1a7f | -2.6347 | -54.22863 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83436366-8628-38ca-a211-78fd4fdf451e | -4.3545 | -48.70913 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc268dbc-dee4-33f4-b7a1-b958b90af44d | -4.891 | -41.32043 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93208029-b1f7-3a54-9946-eeb33fe3893b | -1.32088 | -51.68048 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b329f33-4809-3ed5-b4c4-57f09c14224e | -1.44486 | -55.12803 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45edd17c-c51a-32cf-a414-35e3ea3f4d85 | -2.29111 | -50.69199 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2991930e-c21f-3f2c-97c4-639a494e67c9 | -2.63109 | -51.76535 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35a4b7ca-c9db-3c3c-929e-a92d2e0207dd | -3.69142 | -52.01524 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0127777e-0a8c-37cc-a8bb-8108f2fe1036 | -4.261 | -50.84125 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f64126d8-139c-33c1-9a24-9f4cdc8bee5f | -3.55978 | -50.31045 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f41f78-fb05-343c-bb69-ac52bb8a14b4 | -4.3698 | -50.92574 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 884b0a33-f0f8-37cb-83cb-ea222023cbf8 | -1.08159 | -53.39114 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27a825f6-49a4-33e3-9136-9ee2134e8348 | -1.43522 | -53.3974 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b8c2f1b-0259-3ab1-9abe-a4fa9ab6a05a | -3.14628 | -51.29556 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce21d33c-5dc1-374c-9941-b7272307adf2 | -2.33399 | -50.50687 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28ded21e-89a4-3a80-a5d1-08342bd85ccf | -2.99733 | -51.06377 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3b7748f-40b8-379e-b140-bcb166ae8757 | -1.89509 | -53.01785 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09d39d05-fa97-3043-aadc-dfcb8d8271d7 | -3.24728 | -53.92711 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03bf7312-a524-3ed5-abef-e0ac3f31a818 | -2.06418 | -51.19233 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d1b3d9d-cc3e-3e25-8f32-13159f508035 | -1.48121 | -55.37877 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b6a334-1858-37f8-8ab4-4a7bf56e050e | -2.12 | -50.33908 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38f9d8b1-fc7e-3e55-ad2e-726eda12d1dd | -0.9771 | -51.75784 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c87fc60-551c-3ad8-9484-5ef4ab96431d | -5.08568 | -49.83675 | 2024-12-01 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README58.md)
