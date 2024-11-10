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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ab66537-e7c5-39f1-8d88-a30ed0cee6be | -1.20503 | -53.63504 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1beb986f-08d4-3b1b-b2cc-1a8ba5e50814 | -2.53144 | -46.06868 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a31cb7c-31fd-3ef8-9e9e-9090fd517a2b | -2.37051 | -46.80113 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c71925b-523e-351d-80a7-7067e1d945a9 | -2.23802 | -49.55381 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e304fb0e-577c-359d-84fb-56443f5683a8 | -2.07062 | -48.62419 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 005b1ef7-4468-3f0e-8ce1-d069d8a8c1d6 | -2.62679 | -46.76885 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9623b1f4-4192-3032-832e-7a913932e6ac | -2.4892 | -47.22685 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d034e029-d2d6-30a6-9b3d-cf755235bb48 | -1.39592 | -52.07464 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5332af96-610d-3362-865e-7148428259cf | -1.1616 | -54.08067 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 071ab2e4-0df6-381a-8900-c89535ca427c | -2.29037 | -48.21713 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d7e1dd2-b420-30c6-ac0f-ebc7d5c439ff | -1.50978 | -52.16066 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65659933-c3eb-39f0-a8e2-6a7303dc5720 | -2.40682 | -48.52864 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859ff514-f32e-3a20-851f-e4e3ff91b05b | -2.21323 | -48.85508 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ff44562-21bc-3d29-bebe-b5dc38b990da | -1.44799 | -54.29234 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fcbcef9-0750-38b3-b237-3c47ce31c16c | -1.64242 | -52.05372 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4048fc5c-8223-315d-bcda-162c3afc32fa | -1.72371 | -51.16193 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 474a751d-3546-334e-95c5-6e0422ece3ac | -2.31635 | -46.45446 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef1e7cf8-5a76-3d4b-be43-d5fc453c8497 | -2.02319 | -48.92491 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 487ff8be-b7d2-381e-b28f-d3a065a62755 | -1.82541 | -51.35093 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 215e9870-e7f2-3a74-9043-a7b23d378271 | -1.43055 | -52.27298 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b768f1e9-8fce-30ee-8336-07aadd1fbb5b | -1.76263 | -52.68075 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25003cc9-22f6-30bb-9b09-003f6c085451 | -2.6351 | -46.80378 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1f7f591-a535-39a7-9931-9daf71d38b54 | -2.10777 | -46.47239 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3e05397-157f-3e86-9331-65ab0973326d | -2.49873 | -47.232 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05b32c67-f054-3dcc-b330-1615f895c0c0 | 1.56556 | -56.03538 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f798c292-fe8b-36b8-87db-7be7fc161dd7 | -0.46632 | -52.02352 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 563dd596-8fc8-304f-88b1-06d2c34f82ed | -2.23867 | -46.5524 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5dfd89d-c388-39c0-b1c9-7c33f6a71e5c | -2.39788 | -48.88783 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6a58a9-dc69-34ba-9dda-50aaede69f9a | -1.64688 | -52.04984 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68dd3531-7faa-330d-9df7-5de094d1064c | -1.98401 | -46.43846 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1d6aaa1-7925-352f-89db-a3880b98c87e | -1.66455 | -50.4835 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40eabe03-f27b-3c4e-87d7-8d4cef7f32b5 | -2.10471 | -48.55886 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de72a0d6-f962-3604-81a8-19e0e49ab995 | -1.76574 | -52.68622 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 896ef1fe-375b-3c6c-8756-c9ae0cb498f1 | -2.19895 | -49.29123 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 876f55a3-1923-334d-9223-83acf5cd838b | -2.27812 | -48.18698 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ab3d52f-b2e2-31cc-bb3e-48d39395e740 | -2.12474 | -48.90152 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 772b397b-7c91-3b57-a8b4-529b680dda44 | -1.1986 | -53.70342 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2597a1d-d7b2-3ca9-9084-7ea4fa61d9a4 | -1.12941 | -51.9553 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2393e8ee-aa16-30b0-89aa-1dd94d4e8ba0 | -2.35691 | -46.79903 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dc610c7-fa2d-3e15-8342-1a91f4ac6240 | -1.48881 | -54.39938 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee6f1ec6-66c2-37b2-9850-38cd14159410 | -2.17486 | -49.16214 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d66fc1-a4ca-33d0-8946-1a35ccafa800 | -2.0961 | -48.82982 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 85690e05-83ac-303a-915e-90eefaa1d8ef | -2.63788 | -46.76308 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aeff656e-2828-3e1e-a2b8-5c90223c5a34 | -2.88774 | -45.37035 | 2024-11-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d698a29-e027-3b71-a385-be8649598f74 | -0.30339 | -51.70892 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cf1f85e-b483-376e-a6f7-9da8539cb8f9 | -1.21619 | -51.77561 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 456d1fbd-7686-3f5c-bdfa-dc1a7606bb18 | -2.16713 | -48.39557 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa08444-b8a3-3a14-acad-8cae15fe892b | -1.58134 | -48.03244 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5939fdf-a485-3b4a-b2cf-90677bc29a87 | -1.6234 | -46.15598 | 2024-11-10 04:36:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d760bc4d-da73-3348-bb97-36f98020d717 | -2.33614 | -48.48543 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d5d45a-3287-38b9-9a98-38d026d80938 | -2.10904 | -50.56671 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| abd1e77e-d85c-33cd-b838-e9bcbbeff499 | -0.61831 | -49.52609 | 2024-11-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d346ed56-0c70-35bb-a6eb-581cd6961845 | -2.38356 | -46.7845 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c36a45-3f9c-3acc-b060-ec3f9ec5602b | -1.92446 | -48.52306 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 027ddeb6-ae03-32e0-9e61-fba0a404a1f5 | -1.16137 | -51.99729 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad75d0b3-69c7-3b39-98a4-1f125d19c618 | -2.17772 | -46.42549 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13975ef3-3b8c-3b7f-965c-13a8b2cc7be6 | -2.20626 | -48.36285 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 775d7038-3143-335f-814c-c388dffd8cd8 | -1.69706 | -52.17162 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 277ad34f-26bb-3bb9-b1d7-183bbb346835 | -2.35167 | -46.52069 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cb18eec-3963-3d1b-8214-4dd3c67329ec | -2.29222 | -46.4964 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf563a42-36c9-36a5-8bab-c573c02b976b | -2.29917 | -48.50438 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f021369-8d5f-3d16-8ec2-1d50c48c0a7f | -2.63225 | -46.79962 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f580f6-a361-3d81-a4d5-fbbff6794638 | -2.61667 | -46.16747 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c69761c-87b4-324b-bb1d-2917a1fe6339 | -2.43723 | -45.98295 | 2024-11-10 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb03f400-5392-3457-8884-b22de99dec3c | -2.50733 | -46.29855 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 014836fb-7ae3-370c-905c-6202195a75e0 | -1.54673 | -51.20168 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9286cc4-2098-32de-b5fb-c270946d1b1a | -2.45288 | -47.16319 | 2024-11-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af289904-13ee-3803-8bd1-289a88d84c86 | -2.37901 | -46.81356 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a70ea048-37e1-3465-9db1-13347a8fd9b5 | -2.36883 | -46.74494 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37bd5fdf-159e-3ccb-8714-6449eb383135 | -1.43555 | -48.14341 | 2024-11-10 04:36:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c880050-0467-39c4-832c-0d6541dc000b | -2.2328 | -48.36698 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89f8a6ff-9958-37fe-86c9-3c50ee62e37c | 1.61754 | -56.05658 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6ed710a-cab8-3260-8a3b-c9ed31ad2c46 | -2.14468 | -49.14315 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4656b84f-c7b3-316e-bab3-7b452f1d6286 | -2.04449 | -51.15977 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22103df5-c35e-3f74-a26d-5056d40e7175 | -1.20285 | -46.54182 | 2024-11-10 04:36:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3943460-b775-36b8-ab7d-db70da7804fb | -2.61379 | -46.1631 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41b0cdfd-c312-3d98-a060-9621b5ba0b31 | -1.13568 | -54.10538 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a3c4714-bf81-3b2b-8a87-0bdc30c084bd | -2.19724 | -49.85464 | 2024-11-10 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 888c096f-29aa-37af-b25e-0ee563433bde | -2.15924 | -48.53193 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7860cfe9-a5b3-3e22-a97f-76f669dc6ef6 | -1.51838 | -52.20426 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b6677caa-4719-3c6a-8b77-f44495eeece8 | -2.01104 | -46.37809 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79ee087-0ed7-39df-bc6d-9298f169b672 | -1.66023 | -52.6469 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ed09c07-65c9-3531-a3ba-3c66dc3516d5 | -1.47069 | -51.49126 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f266d39-881f-3cae-ae82-0ea71d084b39 | -1.97786 | -49.01744 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0c2cdac-73fe-3a07-9d23-e82fa864acb2 | -2.11191 | -50.57105 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2e19d494-9684-3e43-a17e-2c9380c9da97 | -2.19774 | -48.84906 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 537b68be-f41f-3579-8018-9d9dc5251073 | -2.00894 | -48.39206 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b68b3f83-6200-3cea-ae1e-fac08ad64529 | -2.17028 | -48.31503 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c85f7e-7472-3071-aa4e-361e40ddca69 | -2.33148 | -48.92002 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2b13eef-7cab-30aa-9870-939dec11ddf7 | -1.41986 | -54.7738 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dbe2478a-a6f8-3fec-aab1-69eede2b6060 | -2.32916 | -48.87002 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6f387c7-186e-317b-b0b4-7050c1523c16 | -2.14429 | -50.14421 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ecbc310-fe35-3962-b10d-c94b895ada73 | -2.26347 | -48.28001 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d7eed5-4ddb-3f60-8040-e0bea69c5462 | -2.40868 | -47.78571 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a8d8569-4554-3563-a1d5-e70a9d494c81 | -2.6896 | -46.81221 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4b89f8b-ee43-3774-b248-59cd13896b2d | -2.40628 | -48.53209 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a6498af-9a6b-3bcd-94cc-8e650b0a4312 | -1.94627 | -46.40988 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35dc5516-810b-36ea-904f-6e3aaf344f3c | -1.45658 | -52.69559 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cecc474-0d0b-319d-a7d1-297c262379ba | -2.45011 | -48.05863 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0792fd0f-4be2-30ab-838b-9dac007b1195 | -2.19258 | -48.19499 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README63.md)
