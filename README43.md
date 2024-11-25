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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dee4d998-f480-3f3f-8ac2-453f7e2e2b0e | -2.92843 | -54.33232 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab99151e-7ac3-3757-a6ea-3c23c6b0701b | -2.90427 | -51.46662 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a836b205-c320-3cc5-aa70-2216c47298ec | -2.81669 | -54.09517 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea18a98a-7a49-335b-b17d-9e66cbbb8241 | -3.01711 | -51.43812 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2195aec7-53b3-394f-b429-3636ed92a97b | -2.58595 | -54.22816 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3c0e7e0-082d-32a1-90c6-04fd50cbfece | -2.44903 | -53.70267 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 214116bf-9314-3f44-a902-59499676b3a4 | -1.56581 | -52.00499 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60ab1928-9fb2-3e67-b134-1fce2d5e391d | -2.74586 | -54.07342 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e82ecda8-79bd-3fc4-96b6-ab60b5a0a1ad | -3.17981 | -46.25973 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b7c50c3-2d2e-3a52-91c2-a7ceb9e095ce | 0.05435 | -51.14055 | 2024-11-25 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 099af6fa-d506-39fd-b2b5-6ae7e89ceabe | -3.31918 | -46.66576 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8018f37-8883-3b5d-8725-15d3761be2e4 | -1.6907 | -52.60868 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3534e42-85e3-3f1e-84fa-fe12759e62fd | -4.30088 | -46.9042 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5aab067-7630-331b-8d62-cfa868fab10d | -2.85488 | -53.98325 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0deec068-1f6f-33f7-9717-5a33f4a80322 | -3.21625 | -53.83732 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a26baf1d-f73d-3b9e-9246-b9393b66ac2d | -2.61856 | -53.97867 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac6a461f-8d87-37a3-b252-d8ea1655722d | -3.64449 | -50.22435 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f361c02e-7420-3095-81fd-4368f07bfa5d | -4.70931 | -45.72115 | 2024-11-25 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45eb6605-6dea-304f-818b-4079713f043b | -3.49958 | -53.82166 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 560a0e8b-c4c6-3e15-a369-a42c315bc0f8 | 0.80858 | -52.01742 | 2024-11-25 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fde5c4e-e535-3729-88f1-137358e81976 | -2.87317 | -54.79824 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06e84a57-ad97-3e4c-b4fb-c5a5e0527dac | -2.4578 | -52.16061 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72a37958-d4e3-3554-bde2-904f1b6ada79 | -4.1264 | -46.85774 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4248ea4d-8f48-3e92-87b3-95d18e543083 | -2.84935 | -53.99666 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2124b0e0-1209-3c77-b44b-f528b33b80c4 | -2.88044 | -53.99438 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b82838d8-4a53-36c3-b166-c7fd9f0a26de | -1.61759 | -52.59733 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f4cd347-0965-3114-b214-42cd09bdeb12 | -1.62756 | -52.59888 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e40ff0-283d-3baf-963f-a8d31f11c481 | -2.75301 | -54.02807 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76a8c7e3-8920-3d4e-8804-137ca01b1a66 | -1.12157 | -52.39624 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b2827f-4f08-3954-a06d-abba34b3bfca | -1.36976 | -52.12908 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d2d251-4028-3690-8afd-1e9f69edbb3a | -2.91489 | -53.06527 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab3b801b-3e69-3d9c-a938-bbc2090cf510 | -0.96952 | -51.71106 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66206d5a-7d2e-3f97-86fa-8f772979790b | 0.04532 | -51.70567 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82590d8d-0cb4-39ff-8fe8-b1a40bc65b49 | -2.81113 | -54.10863 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbd2cf53-f6b8-3cbc-9091-e03a73917c0d | -1.19502 | -51.77435 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 115c2b4c-203f-3395-b753-06f6c0e2270b | -2.57965 | -53.96544 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7fcc185-14aa-3554-91fd-df60a8797ad2 | 0.04808 | -51.72319 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9a5086f-9009-339b-bfc5-291152cefa34 | -1.77636 | -52.73224 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff7d326d-556f-3289-95ec-f420a851f792 | -2.79822 | -53.0119 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61774c42-35b2-392d-8a95-aa38cf9d5c72 | -2.13868 | -52.27628 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6352c1d-e36f-337c-ac8b-7f3800ef36be | -2.85539 | -53.95838 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2a16e45-01a4-3fd3-9a3c-5ea6c44bb542 | -0.98693 | -51.72085 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 464ba0c5-7c49-34ee-bd08-504d43b5774e | -3.58183 | -52.18076 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e91c72f-e1bf-3beb-a948-cf3953665034 | -2.7844 | -54.0615 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab34ca91-6d63-32b7-99bb-81b76909e55e | -4.02656 | -50.50267 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 516e1ddf-a3a2-3cca-8d4f-5a32628e35d5 | -3.50732 | -53.81578 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0552bdd4-0c0b-38aa-954b-adb261df49a1 | -2.88323 | -53.99838 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc08e622-fcfb-3691-bdc4-7e3a45250d7b | -2.74253 | -54.0729 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcabc274-3df3-3c81-b681-2ab2fbdea878 | 0.97642 | -50.1259 | 2024-11-25 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33f771e7-2365-3998-88db-c140d388f1b9 | -3.31672 | -51.75377 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c200c55b-e34b-35ec-88c0-a9c29d9f675c | -2.42804 | -47.01787 | 2024-11-25 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89adefc2-39d3-345b-8163-dd278febda20 | -1.52226 | -52.49419 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c807039-dbe0-39f9-a241-4f919d28ad6d | -3.09948 | -54.00053 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bd93d61-de76-30c8-9c60-693ea8f53586 | -3.53732 | -50.45564 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63783ec4-302e-3974-8f5e-3e1814969cb3 | -3.21977 | -53.92314 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| baafc1a7-9e73-3bc3-82e8-e24896c78ff2 | -1.65997 | -53.81085 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75f8e757-62a4-3ed4-a4f4-06cf02767eab | -2.01053 | -52.33888 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a355a6e-3f61-3e97-9239-1911ee3df545 | -3.94129 | -47.99321 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d87360e9-ea82-36f5-b0d3-cd6f78795e46 | -2.80818 | -53.01345 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 495c7645-961c-366e-b188-58f8116bf861 | -1.48898 | -52.51382 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34426b68-335a-385a-8a81-dcef0a6a671c | -4.70145 | -49.63915 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 544ec762-05b8-3a12-8bbe-08e138b516fb | -3.22292 | -53.6223 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a05d8a8-2d1a-3d5b-8f17-5cdf6b141257 | 1.4057 | -55.88751 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 269aa990-81b0-33c1-9718-ce28695b2579 | -1.32311 | -52.23546 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2440660-c3e5-3ad9-9d2c-26a3207bfe1f | -2.82005 | -54.11718 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80fcdd8a-4f47-3bde-8d39-fd7695dfe411 | -4.23702 | -48.70208 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13359b2e-2b1d-3276-91b9-168850068af7 | -1.48313 | -51.96336 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac850d9c-517d-3a4e-93cf-9afab3ace6f9 | -3.31707 | -53.2837 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86f7832c-01d6-3836-bc99-439d6f9d67ab | -0.27742 | -51.49888 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 719f0617-8248-384c-b37d-d66459921766 | -1.63785 | -52.70657 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c778507-255f-34ad-bb99-59dbc3d9a800 | -0.95535 | -52.27129 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b8e7e86-e8db-3495-86b7-fbef83e1a5ec | -4.32175 | -45.89601 | 2024-11-25 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5cbb0599-12ab-3ede-8001-3151c09cfa99 | -1.73562 | -52.79655 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f11a212-148e-3ae1-9f1a-ca89ad19ed7d | 0.63494 | -50.56997 | 2024-11-25 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c4dae83-a5fe-316e-a02b-c56914d62bdd | -2.57521 | -53.97189 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58718f8b-194c-3667-a930-e26b50fe73f8 | -1.73271 | -52.32049 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cb1625f-c9e0-33d7-b125-9ed5e4f8bfa3 | -2.25247 | -53.61899 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b63383c-e5d7-343c-babe-cb5b548cca80 | -4.25939 | -48.67038 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 839a31ba-c203-3083-a641-e3b7128392fe | -1.12844 | -53.81361 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 879bee70-1756-3366-b98f-e562e7fd912f | -3.71475 | -51.77575 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4555d1ab-6c32-3951-91f7-f358437047bb | -4.20141 | -50.23597 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e43d5bc-0c92-32eb-b890-431c4a8805bb | -1.48457 | -52.52022 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9ca070-7eb5-36e0-89e0-83cb26fb8ef2 | -1.50618 | -52.0353 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 025da6a0-88bf-35dc-9de2-2d8594bebacf | -1.61503 | -52.35946 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 323c2fdd-2c2c-326a-879c-f61e32c9e8c6 | -2.75922 | -54.0755 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0237265-bc97-39a4-bf79-3d8b975b7cc7 | -2.90306 | -51.56423 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20507431-5010-3bb1-a19e-c77b7b9320fe | -1.2605 | -51.75188 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e9569a5-d3f1-361d-9d46-2e1003489fa0 | -2.61276 | -54.25402 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2f557bf-6241-3806-ba8f-06788729786b | -1.25198 | -51.6305 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d25274c4-cb3e-3a75-8791-f72687cd65a4 | -2.18961 | -53.80103 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b8bf21a-0964-3170-bec4-bc99adb203d7 | -3.85253 | -52.14899 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a17d180-da87-33cb-9fc0-d15e5037d9bc | -2.96786 | -53.88739 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f75a4b3-0252-38b7-a8cd-719a1ec8e990 | -1.61166 | -53.30301 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 681e8cff-d863-3a01-b719-c8c4193a1679 | -3.08889 | -53.98105 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53c7facb-6cfc-34bc-b021-bead85477c67 | -3.27085 | -51.2654 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b91041f0-8c9d-3c5f-8251-c191e0dbbe0e | -2.81726 | -54.11316 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8648d514-fe8d-3116-b4b0-441b6aa7d5e7 | -4.51454 | -44.59674 | 2024-11-25 04:55:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10f53f04-aaa0-3f5a-8a3a-92b793cc6126 | -3.29062 | -53.8595 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ade04f4c-9e5a-3fe0-bb48-13e9fe18bfe3 | -2.01041 | -46.50595 | 2024-11-25 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ea8b7f-cb91-37ae-af49-31032a110945 | -4.29184 | -46.90263 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README44.md)
