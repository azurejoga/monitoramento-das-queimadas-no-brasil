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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0319f3c-bbd5-3ade-9112-22dc5e3d03c3 | -3.28342 | -50.03928 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f791ded2-5a2b-3a13-b538-a81700953ca3 | -3.25109 | -53.63448 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 07959e9b-decb-308d-8373-3dbc596ff7f4 | -3.46907 | -50.52544 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6d247ad4-7367-374a-a78e-4293f397ec46 | -2.29905 | -51.98392 | 2024-11-29 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 80093d6e-929e-3b85-8246-e7f178d47dc0 | -5.04755 | -43.61485 | 2024-11-29 05:44:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2070c667-1855-32bb-9f6c-992017fccb40 | -4.05045 | -48.33583 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0df7236f-ed4b-32a2-9867-62c969f56010 | -4.16702 | -48.62325 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0d90a3aa-4ee6-3a09-b6d2-93bd9467090a | -3.20105 | -46.56992 | 2024-11-29 05:44:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| fb7eb743-9938-3768-a36e-15ba0cfebeca | -4.20194 | -48.56357 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c870fc27-8243-33fb-a258-150751e37f5c | -3.15228 | -49.43467 | 2024-11-29 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64aceefb-23e0-35f1-8383-9ff96d9e26aa | -3.47658 | -50.5355 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68e5faee-f171-3cd2-b464-7a5d728241a1 | -3.02723 | -54.02743 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4196560e-89ae-326d-81fe-d5d14432aad0 | -4.66213 | -49.51993 | 2024-11-29 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f433545-8892-3f06-8cb2-c50abc8bf832 | -2.20649 | -52.09803 | 2024-11-29 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c2152139-2360-32f7-a4b6-56c2c917dd6b | -2.98008 | -53.2677 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a9e50be-8952-3a43-a51d-b57c0e262546 | -2.22687 | -53.69344 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 27a7573f-ebe8-3db1-bc47-99a72d03b961 | -3.38203 | -50.11415 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3c7e67df-d5c1-39ef-9e19-0f6274e424d1 | -4.43428 | -46.58157 | 2024-11-29 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c9cb13db-5dea-3eca-8f2e-24406b896312 | -2.23038 | -53.61483 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 415b6c86-dd3c-341d-a5c7-aefe0336170f | -2.87116 | -53.9793 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f35dc547-2b60-3740-bfb8-8b8e66916178 | -2.98656 | -53.2908 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1b8938a9-9a61-3c18-b857-269c5dafa659 | -3.28186 | -50.60227 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85e28f8e-8590-301b-a358-30dd23f7b6bf | -2.84305 | -54.02504 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb997563-2e62-36a9-b490-d57d9a2efd8c | -3.02911 | -54.0153 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 24068777-0c6f-364f-96a0-e34366b326da | -3.37281 | -50.17579 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b3d38696-fc83-3c88-b194-cf330cb5b2b4 | -8.13053 | -47.98284 | 2024-11-29 05:44:00 | AQUA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2873f397-c74d-3c77-953b-c3f9da54d410 | -3.41381 | -50.1606 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a6cddab4-0235-3682-95d0-a5473f6bc278 | -3.19862 | -46.5622 | 2024-11-29 05:44:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 640ab93d-1fac-3910-a706-708f6f6827ec | -3.82079 | -46.59725 | 2024-11-29 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 36df08ff-9104-31f1-a240-3f2e17bff503 | -2.97841 | -53.27863 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 22477c21-d77e-3592-b41f-78698ce92359 | -3.2532 | -53.62881 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b3970d80-9baa-3910-97ed-68c9f172d962 | -3.78744 | -50.13166 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 042ae360-6144-3280-a3a1-3349b256632b | -2.70384 | -49.83082 | 2024-11-29 05:44:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9654a23e-1cfd-3df5-9fbf-f2394ea3fdf6 | -2.59517 | -53.96973 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| affcb321-9b1b-33d7-90a5-7f589f5e7990 | -3.53801 | -50.1853 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1d5c1c18-097e-31a0-907c-047c7bb43067 | -3.61479 | -49.85308 | 2024-11-29 05:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 53ee2872-6b68-3692-b5a3-6d2150cbe5b6 | -4.48133 | -48.10704 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4bfac44a-b67f-3f57-9528-eee339919d04 | -4.17632 | -48.6246 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 84685e0b-54ab-30ad-97ea-27c06837283e | -4.47879 | -48.19186 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9f58adba-43ef-3402-8a62-e0f1a5e7764f | -4.05462 | -49.06735 | 2024-11-29 05:44:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 968e921c-5fc9-3c42-8d7e-276e39cb6bc5 | -3.46775 | -50.53422 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3c402cad-0c4a-376d-852b-5590fe305b49 | -3.61306 | -50.184 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0ca13123-ebd4-3ca0-8c77-9ab2cb6e6132 | -3.10281 | -53.80691 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5eb78e6b-033c-3b07-9084-cbba5e29d381 | -2.26292 | -53.46555 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3ed9e325-29c1-3379-a204-bdf6db4075cd | -2.62061 | -51.80524 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ee8946ac-e340-3995-953f-99c96366790b | -3.29224 | -51.15108 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5b01e103-1664-3564-bf2e-233567226e3b | -3.86577 | -50.15205 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8efeec02-1d59-356a-a012-518cf1095ae8 | -3.74311 | -50.79011 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9f579ebe-ada9-3591-ba75-50542f810023 | -3.30361 | -50.75819 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e85ef362-f441-3b24-b9c6-efceee69eaf7 | -3.09191 | -54.13193 | 2024-11-29 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4e923605-f8dc-3ff5-b5ee-5367f477287b | -2.5696 | -49.99372 | 2024-11-29 05:44:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66f2fd18-d6a0-3505-aa22-e23d5b044c5e | -3.34931 | -50.51341 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05eee223-8045-3677-a443-2680e605fbb3 | -2.69407 | -51.98628 | 2024-11-29 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b3ac9a6b-13a2-3205-ab19-5a025bc9da3e | -2.84007 | -54.11278 | 2024-11-29 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0f21b28a-7108-3c92-919a-ae20c8de1779 | -3.23587 | -50.17628 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d85ac312-9edf-388c-99c7-32699f04b6f1 | -3.39219 | -50.10664 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2084c96-948c-3b44-847f-92e48ef7ced4 | -3.39018 | -50.31886 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f43bcf25-5504-34e5-a3f5-92f9e74c2c07 | -3.59562 | -50.36119 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57c6f0f0-c65e-37eb-819c-4d554649599a | -3.32958 | -50.22341 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 234283d6-d4d9-385a-a649-fc9c1b6792d7 | -4.43619 | -46.56825 | 2024-11-29 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 53f8aff0-6f72-3b2b-8be3-0f0c5ed6671e | -2.95346 | -48.3378 | 2024-11-29 05:44:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5199f75a-4908-37f3-9dbc-14c9a4187b0a | -5.23339 | -44.91166 | 2024-11-29 05:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ae039228-6ccc-38f5-86dd-0136d929a4f7 | -8.12883 | -47.99482 | 2024-11-29 05:44:00 | AQUA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a5216ce4-cc84-3741-a961-f40f45785d86 | -2.43895 | -50.4263 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44a1baf5-b461-3a75-a770-b803ab6c9ad6 | -3.34593 | -50.23478 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5090ff0a-15bd-3412-91fb-7f7da2dd0476 | -4.40753 | -47.26866 | 2024-11-29 05:44:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0d966c4c-1b66-38e3-b44d-241e81f1b5a9 | -4.07758 | -50.03922 | 2024-11-29 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f49901d9-2a7f-304e-b8ba-712736a51a8b | -2.9882 | -53.28 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f812e5ee-1a48-314a-b5b0-23db81b8d097 | -2.96696 | -53.28809 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b3226d0a-592b-32bb-bc69-2af60320dbcf | -4.48031 | -48.1814 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6ec91cd5-731e-3a2e-80d3-c6d5cf815058 | -3.25143 | -53.64014 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 8275e13e-bf52-37c8-8147-b09c2b3776e2 | -3.38335 | -50.10535 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 549dd3b6-fd44-3f08-9711-e85d4db8f3fc | -3.9718 | -47.94277 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 34fd7f4c-a0d5-3044-82ec-ff0b69136b43 | -2.44027 | -50.41753 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 988602d4-5149-32cd-a811-9bc77b27452c | -2.58497 | -51.91897 | 2024-11-29 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5eaa03f5-91b0-3ffd-a8ac-d9ffc5d1ef7a | -3.05647 | -48.51857 | 2024-11-29 05:44:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b66fcfaf-114e-3e2d-952e-2c8005558135 | -8.28723 | -48.02935 | 2024-11-29 05:44:00 | AQUA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f75180a-1413-3203-8676-c60fc0ab09cd | -3.93577 | -46.70406 | 2024-11-29 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 59d76a83-0868-3ed2-84c8-04931aff56d5 | -2.57031 | -51.83024 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 985f7954-0b77-3a9a-8e97-6fb825dd788e | -2.22871 | -53.68159 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f87fcd22-eb97-329f-a972-81d2ccbc7d38 | -3.33787 | -53.21278 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 91a7075e-b495-36be-8138-4a69445a490e | -3.24112 | -53.633 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b0a3215c-258c-3a8a-88c9-9f56bd2e5b60 | -4.47981 | -48.11754 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ab1bd102-6371-3484-97d0-5b135ad1de19 | -3.33551 | -46.69045 | 2024-11-29 05:44:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f488a955-d392-34ca-8fbf-3a967b358c5e | -3.10677 | -50.35806 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c43412f6-fbdb-3d45-b2e5-b40eab39bda6 | -3.3309 | -50.21462 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 975ea1aa-add5-3716-aa3a-1a0f81c96b69 | -3.87232 | -48.35922 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3b3f834b-c5a1-3fc7-a453-9f5bedc65386 | -4.06372 | -49.06868 | 2024-11-29 05:44:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d54e9c66-1a53-3a98-a56b-330335cd6440 | -4.44494 | -46.58315 | 2024-11-29 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a164e01d-5466-3915-8235-dfbbeaeefa73 | -6.70657 | -47.27006 | 2024-11-29 05:44:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cb0496f3-0d87-35a1-9299-3335b5a16089 | -3.25279 | -53.62314 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| b86392a2-195b-35a0-9933-ead5bfdfec5d | -3.5819 | -50.33226 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98eda4d4-1d47-3e4f-bd12-4b50839a4c85 | -3.97404 | -46.7351 | 2024-11-29 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6e41d3bf-ac8d-34b6-9932-5048cb697b0f | -3.15361 | -49.42565 | 2024-11-29 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1c848f7-c98f-3ff0-880a-4e8eaf3900a1 | -2.73462 | -48.88839 | 2024-11-29 05:44:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47352e1b-e991-3137-ad5c-a861f7ad3174 | -2.57712 | -50.0038 | 2024-11-29 05:44:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30760bce-00a1-39b0-8090-9b41d4a3b812 | -3.20293 | -46.55731 | 2024-11-29 05:44:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f2d6823c-667b-3dff-9d5c-0752394aef37 | -2.61863 | -51.75731 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0e274bd8-6948-3b6d-b97a-c226f07ce77f | -2.75654 | -54.12012 | 2024-11-29 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 50bdf90e-4a9d-3f19-ab65-af3e77de2cd2 | -3.28094 | -50.5483 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README103.md)
