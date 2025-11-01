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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fb1c9ce-5280-34e5-b7f5-c15227ce6538 | -10.87206 | -47.55961 | 2025-11-01 00:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1ed3ca05-47af-3c7d-ad01-15ccca0165d7 | -5.26105 | -45.6166 | 2025-11-01 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0c6f6e2f-476c-3b4b-b641-4ddc2464d028 | -5.53359 | -46.53413 | 2025-11-01 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d177c09-4050-3f82-bca9-bc3386cf49f8 | -6.46665 | -43.30133 | 2025-11-01 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 98e1ef07-8f44-3002-ba49-e8500b2e1d56 | -6.31874 | -43.62563 | 2025-11-01 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0001c847-beb9-3291-9660-b3ffdd6d02ac | -6.34378 | -45.25571 | 2025-11-01 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c583d65-04ce-3307-9b06-0d558352f608 | -6.7344 | -45.95525 | 2025-11-01 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 817f5d59-4e7f-3de2-8b6d-67dc43459533 | -6.88476 | -35.0214 | 2025-11-01 00:13:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| 8485fab6-01ee-3124-a8b0-174ad94c9f38 | -5.54131 | -44.52442 | 2025-11-01 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1d7239ca-4352-31c3-b588-f50d5c45060d | -6.6775 | -44.67925 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 506b89a6-8526-30a4-a730-ac63569ac349 | -5.14934 | -45.81588 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| b3838174-a6b4-3e78-a3f2-d6c6011eb044 | -9.11937 | -48.45689 | 2025-11-01 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4f507f34-7a46-36f5-9ad0-2554e2a172d3 | -7.55717 | -45.23959 | 2025-11-01 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6cebf922-432e-3d17-84b6-8ed56cfcc633 | -6.36147 | -42.39493 | 2025-11-01 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 39b78c0a-4beb-374c-b57c-de299bccbfb0 | -7.21898 | -45.05276 | 2025-11-01 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e19b6844-3c68-3d80-8f38-234848cbf4b4 | -5.00657 | -42.09772 | 2025-11-01 00:13:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| d9cceb96-813a-369b-a6d1-336edc19d100 | -4.91598 | -45.59061 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28c4c619-848e-3b45-9dda-72923e437609 | -4.12094 | -46.7753 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 678b7c76-597c-3a5c-8021-ecd75dd89d32 | -4.33807 | -49.01447 | 2025-11-01 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 07ade17b-c571-3f5b-9e28-98616d16fb33 | -1.10783 | -48.10803 | 2025-11-01 00:16:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6802f1aa-c386-3c5b-acaa-b28b55747cb2 | -1.49904 | -47.80769 | 2025-11-01 00:16:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d07a8c6f-5edf-3d31-956e-5693b8f290ef | -2.57847 | -45.34481 | 2025-11-01 00:16:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 86b80cde-ee7e-3193-95fe-d494761c5d4a | -4.30345 | -43.6422 | 2025-11-01 00:16:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8de03a3d-59ad-340b-849d-94589a3dc7f8 | -3.0858 | -45.74583 | 2025-11-01 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19ccbc1c-3c39-3c5b-86be-c3835c3e6740 | -3.12474 | -45.76722 | 2025-11-01 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64e180de-1cba-37a9-a235-458b23327a09 | -4.29945 | -46.26783 | 2025-11-01 00:16:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c74250a7-8adb-3d0e-a57d-2e6cea6100d5 | -2.18932 | -46.59382 | 2025-11-01 00:16:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cce762a1-4575-371d-bbca-955e4dcdb888 | -4.56661 | -45.40394 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 65040319-2a54-32cc-9aa5-bfc220a94ffc | -3.23723 | -50.58439 | 2025-11-01 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| e8417d25-2d29-3515-917e-8b676afee0fe | -3.34909 | -44.66134 | 2025-11-01 00:16:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a1d04074-c1b3-31bd-ae05-4d178076aa26 | -4.95104 | -48.25958 | 2025-11-01 00:16:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b1a71ad0-c2da-30d9-a682-89e1167454e0 | -3.58824 | -50.80973 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8dbff0ae-2ce1-3e5a-b920-770d817e2ffe | -3.88378 | -42.54913 | 2025-11-01 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e06271ed-9643-3b3c-a27d-4bbe24feb728 | -3.0157 | -53.96717 | 2025-11-01 00:16:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5c30d19a-0eb1-38b2-af74-679188fd63f3 | -4.43443 | -45.91087 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| c97aaf87-427a-35da-b524-a5734b135366 | -2.79795 | -43.34415 | 2025-11-01 00:16:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 60a4d9aa-2d66-3e4b-a32e-98e92ad09561 | -4.42605 | -47.60342 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 33cda6f7-e550-39c1-bada-49d1637e57ea | -3.4342 | -42.54697 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2fdcb4ce-0441-3c7f-9681-1818df2b3780 | -3.62025 | -45.9538 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9465ea6e-79e9-32f1-bf1f-b896e9d77684 | -3.9785 | -48.91916 | 2025-11-01 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c4a14109-a9ec-38a8-8f75-20d966b23af4 | -4.44268 | -46.03605 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 52a00bf4-c81e-3c13-945f-057f57a9bfc1 | -3.63156 | -45.69521 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6ad8846-cc73-38f2-abfc-2917d239784c | -4.98523 | -48.43552 | 2025-11-01 00:16:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ab56d48b-33ed-3ce1-a609-8c601b03becd | -3.89012 | -47.17271 | 2025-11-01 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 51a48510-65c8-3d8f-87a5-db0f12e4b9c3 | -4.5921 | -47.05535 | 2025-11-01 00:16:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c430945-3020-3218-968e-46f847e45640 | -3.89143 | -47.18213 | 2025-11-01 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| adcd77ef-742e-3f8e-a760-6e3d98750de3 | -4.44757 | -44.21143 | 2025-11-01 00:16:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f905d54b-305c-3bbd-9982-2b014066ff0f | -3.30915 | -50.01147 | 2025-11-01 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| efdaa32d-a5a4-3243-b271-02d53eb7187c | -4.55291 | -45.63017 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 466ea86b-d9e9-3db6-b239-617e9dda1907 | -4.61261 | -45.80156 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f0bc9f5-7de7-3b52-8686-01db8302bae9 | -2.99594 | -45.22858 | 2025-11-01 00:16:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bb435ce0-156d-35eb-82e2-b9cd84f964c8 | -4.5304 | -46.40011 | 2025-11-01 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| becf2a8c-381f-3766-a8f9-3c938c2aa20f | -3.19789 | -45.75958 | 2025-11-01 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6398a68-ee31-3e98-8a66-1875cd444be3 | -3.57426 | -50.26977 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a22e364e-b272-3a9b-9833-68837d96c4a1 | -2.79938 | -43.3545 | 2025-11-01 00:16:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1876034-28e6-38a0-9689-d6573f0acbf2 | -4.09201 | -44.04025 | 2025-11-01 00:16:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bee6c963-1983-3cc0-b5c2-778f200f1f6d | -1.49069 | -47.80514 | 2025-11-01 00:16:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 95cb4a57-385d-38ea-96f6-bff6d98b1e68 | -3.52683 | -47.54877 | 2025-11-01 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b10bf504-b923-31da-bebd-7e081380327f | -2.57969 | -45.35364 | 2025-11-01 00:16:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b6d3647-6552-31dc-a227-78251c389374 | -4.29822 | -46.25888 | 2025-11-01 00:16:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 08a75ddc-c65c-3065-97c8-c5b1fe16ae3b | -3.53784 | -50.17945 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b4627346-a56e-39de-918c-4ce13ca4f2cf | -4.44627 | -44.2022 | 2025-11-01 00:16:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d8233cab-bb53-3349-87f4-06b7b6e296b4 | -3.45366 | -46.01627 | 2025-11-01 00:16:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf4de1db-72d1-3efc-97f9-6695c6054331 | -3.83701 | -49.39309 | 2025-11-01 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 17954fe3-8e72-32ec-b5d6-d937251a4bce | -4.77405 | -46.50171 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b64e0358-649b-387d-bf5d-44ee51f8c81f | -2.51947 | -45.5842 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 866d9d10-e555-325b-b9a8-920540c85594 | -4.43565 | -45.91967 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 112275fa-6f73-3d36-92e9-9f51086f7d5f | -4.40542 | -48.21052 | 2025-11-01 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 37be6cd8-553c-37c9-b868-2cc0a3cba2e3 | -4.17878 | -42.96254 | 2025-11-01 00:16:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ef8dd7f5-977d-333a-ae74-37e5981996b8 | -4.5693 | -45.87968 | 2025-11-01 00:16:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8bae6fd9-d5e9-394a-876f-89395f9d90b3 | -3.42204 | -50.00357 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f2aefdc0-4c7e-3160-93e2-69edaddab647 | -3.97938 | -45.41561 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7e041ac7-60af-37a2-ae92-5db980ad5302 | -4.21631 | -48.09755 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 91bb7187-087d-3470-b876-67df84925fbf | -3.52815 | -47.55846 | 2025-11-01 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 855915cb-283a-3e4c-83cd-b85b59be04e4 | -3.79277 | -47.68306 | 2025-11-01 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 848156e8-8a48-3c41-ba08-5169c7d10205 | -4.44121 | -44.42664 | 2025-11-01 00:16:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 219bf002-43d2-3e79-9cb4-2639325a8168 | -4.67548 | -50.44722 | 2025-11-01 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4c293de0-d36c-3abf-aa46-7d23e326c913 | -4.5517 | -45.62137 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d1243427-22f2-3bfe-9795-3a2ee6c1233d | -3.85578 | -45.44794 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 33b48196-24a4-35d2-af3a-1fcb2e984ebc | -1.35117 | -49.06536 | 2025-11-01 00:16:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2b680110-acba-38a5-bed0-1d6eb986bdc8 | -4.55891 | -46.6806 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9172e351-3621-356c-a305-99449fd76e39 | -4.1762 | -47.65597 | 2025-11-01 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e9e69cd3-0b9a-35d9-8804-c138486d2e06 | -3.73141 | -44.09706 | 2025-11-01 00:16:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ca81bf0-12bb-3cc1-bcd8-ad23813f69ff | -4.56144 | -45.43159 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bba343d9-54d5-371c-9e3d-e83a43f5d22e | -4.56019 | -46.68984 | 2025-11-01 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 7c09148b-c6bd-30c9-808c-2be7d473ec26 | -3.04128 | -45.82963 | 2025-11-01 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 93fd563c-99ac-3384-aabf-e685a194bdb5 | -3.28553 | -45.32248 | 2025-11-01 00:16:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b66cce08-735f-31ed-9ea0-7867a16057a3 | -3.16422 | -49.16928 | 2025-11-01 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7084b16c-7788-3067-aad3-e67108aaa1fe | -4.79721 | -46.47082 | 2025-11-01 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e2e02d54-a2dc-35e5-ba32-c3bfb7aaf89d | -3.24777 | -47.32347 | 2025-11-01 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bb36a88b-5f5a-3584-8ba4-413540a1ce82 | -3.88534 | -42.56023 | 2025-11-01 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ea539a77-83de-3446-9173-0fe25e1f73a3 | -4.09691 | -44.99975 | 2025-11-01 00:16:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36d3d0df-4528-3c99-9c32-5e1a77d5ffa2 | -4.54951 | -45.80139 | 2025-11-01 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2323e7f8-9fab-3447-b7ed-890fb558b534 | -4.56782 | -45.41274 | 2025-11-01 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 286cac43-bbff-3d4d-9909-482e65063648 | -3.95835 | -48.92204 | 2025-11-01 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| abb8c683-d6eb-30a9-a034-565ae13801f7 | -3.69774 | -49.56583 | 2025-11-01 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4c2565e1-9836-309a-bc7d-59ef3fe55f2b | -2.75978 | -45.3882 | 2025-11-01 00:16:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| db88224f-0f4a-35b5-bc1b-17b389b0de1b | -3.15643 | -50.83414 | 2025-11-01 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a9f7ab34-cb53-3538-a01e-c4ce2a6455eb | -3.50584 | -49.94483 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3a6e0205-d5f8-3c5d-a2c9-9c52330cf61a | -3.65427 | -50.18043 | 2025-11-01 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README6.md)
