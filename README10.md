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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5767993-fef2-3f65-8dd8-ea4581e7742f | -9.64129 | -43.84166 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5831283c-d0f9-34cf-a025-77c2811afaac | -8.16053 | -45.0135 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2218334a-6da0-3f90-8f6a-d21eaf645f1d | -10.52749 | -42.54776 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 70c8c9fb-5753-39a8-ae77-2e924c1d7d11 | -12.62902 | -48.09485 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 675d4761-eebd-39d9-b430-1ed70316b4ee | -11.12734 | -48.64113 | 2025-07-31 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af57f2fa-f2ab-3b54-a59a-1b027df1757f | -10.6056 | -45.25768 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5f07bc4-e0b6-36bf-852f-9701cc866b19 | -8.16848 | -45.01044 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07391177-f3a3-3617-837d-ee8619fe03b9 | -7.58824 | -44.81435 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63db6c75-aa45-3008-b929-bb3b7e8878e0 | -13.15678 | -47.34127 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aff56420-566c-3773-b5a3-a9cfcf990571 | -13.51093 | -45.64447 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eed91769-33d5-3684-9cf7-52d04c006084 | -9.62992 | -43.84793 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60cfcee3-6355-328e-9885-32bf59a79f95 | -9.63272 | -43.85221 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb32ba04-8376-358e-acff-ab26598c7eeb | -7.59319 | -44.8068 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19a5dc0c-bb0e-3cbb-aca6-61cb89d5ceaf | -9.01688 | -47.97431 | 2025-07-31 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 891d4c2d-77f8-3a9e-806e-42d998024b47 | -11.97997 | -46.67951 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0685233c-c2ea-3f07-8cd1-139d6196f19f | -7.64754 | -49.79699 | 2025-07-31 04:10:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a05a2c6e-c267-336c-9550-242f8ec82ec8 | -10.07805 | -53.87227 | 2025-07-31 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ef92e2e8-2778-3585-ad46-46dfd4f65be0 | -7.58035 | -44.81731 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9df6a21-e92c-3f97-897e-b651d1aab6ca | -8.80733 | -45.63325 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5582a46-a050-3d16-b9b6-60d8547358ec | -8.83223 | -44.53999 | 2025-07-31 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 101332b1-88f0-3442-9613-14544cfcb3e7 | -11.99257 | -46.69627 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6bd7691-8a05-3f96-9cde-57ddd340a2b3 | -11.98454 | -46.67554 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7222b5b-a798-3305-9c86-49bac75ec473 | -7.32296 | -44.67764 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70bc8ed5-ebc0-33f8-9708-7111e4c96a17 | -10.055 | -46.54141 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7c2c295-0a2e-38bf-b8de-d36a13698d85 | -6.40958 | -53.37355 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6b7f7bc-239b-34d7-9d05-d9e7f2ac6eb8 | -6.38546 | -53.32626 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07c4e408-87e6-36cf-ae59-b5e45e4d01e9 | -7.33274 | -44.66952 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 887a5f1c-0689-3100-87a5-680410eb0911 | -13.07041 | -47.39723 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6cf44ed8-a35f-3714-870e-8dfc4dfb99ac | -13.67511 | -44.22506 | 2025-07-31 04:10:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e17f70c8-c24d-37db-a45f-2d4a45e201ce | -8.59228 | -45.52111 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cd1e9af-79d2-3fa6-bcbd-05a6724478a1 | -10.61971 | -45.23908 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa782e81-65dd-38b9-bb9a-9244c6a42091 | -7.59679 | -44.80745 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55210baf-4cbe-31f0-80d8-e1801f444512 | -11.74949 | -48.18922 | 2025-07-31 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ab3bfe4-21ec-3f7b-bd02-528f58b1e6e3 | -11.75016 | -48.18545 | 2025-07-31 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8ad1630e-8f78-3114-ae00-14cb0319c951 | -9.21225 | -44.53626 | 2025-07-31 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a965f0f-76bd-3347-9bff-4d046bd14219 | -9.63388 | -43.84423 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc3f06de-f2ef-3914-98a4-11a03ca5308a | -6.39113 | -53.32003 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 282d0bd1-9895-336b-903b-6f1428cb3970 | -10.61296 | -42.92908 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7e2e28d-bf24-3f9d-91a0-99552a9c847c | -8.05781 | -43.10968 | 2025-07-31 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| aea17bdf-b9e6-38d4-9d05-2bd0caf25578 | -10.10166 | -43.95464 | 2025-07-31 04:10:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 838ad0b4-5325-33a9-94b5-4352b6b69a85 | -9.39502 | -45.49517 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| af2a1828-aefc-35eb-8752-68e19ccaaa6b | -7.58464 | -44.81374 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95fd7b90-04e5-37ba-a8df-9c5f8f242134 | -13.1522 | -47.33841 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89bb24b3-80d5-38e3-9c49-9c4936f6c761 | -12.76444 | -44.41087 | 2025-07-31 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f18836ab-2688-3567-9c69-62211dfd24c3 | -11.7467 | -48.18092 | 2025-07-31 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 566a53e1-3903-34b8-bd27-95bb336f384f | -8.9531 | -46.74677 | 2025-07-31 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cd1e986-fd05-38eb-a923-fd88cb8a5c82 | -10.64239 | -45.23462 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bef287fa-249a-3c2f-b72e-57b7041b7082 | -8.16345 | -45.0183 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1241ba13-ee9e-34de-a94a-c1a03cd79611 | -8.17933 | -45.01223 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53453b42-bb9f-31ac-b929-c9eafe089e74 | -10.64307 | -45.23057 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 913fded1-2eba-30b3-afcc-b1e4a8cb042a | -11.53992 | -44.24636 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edfeb983-080f-3b7d-8de8-77c61cfb38b4 | -10.05223 | -46.54263 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 416d2228-4b3a-3ecd-a4eb-0308c44a3afc | -10.52306 | -42.55423 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1ac79dc8-0083-37f1-b570-f32c61708c48 | -11.52362 | -44.28168 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 98589f49-f04b-37be-9f23-60355a2a06c5 | -11.52911 | -44.24835 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6412359d-831f-39f6-9330-d8bfddb9f09a | -11.91987 | -44.55009 | 2025-07-31 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aac679ad-1e3b-35a9-8b5d-60cbeed8d92b | -13.50609 | -45.65178 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b99ff0-d644-34a8-901b-c71b0691f6c7 | -7.33206 | -44.67358 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bd03c68-424b-3266-bccb-bbc906ee9bda | -10.22593 | -47.98869 | 2025-07-31 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa63e538-12e2-382e-9347-0be893f38098 | -11.96864 | -46.68018 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0669d0b5-4283-313f-b5b0-422cc09dbad2 | -5.72259 | -49.1029 | 2025-07-31 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1613e196-5147-3f7d-a7e6-339590aaa63d | -10.52694 | -42.55126 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 949cf554-795f-3791-8f1d-96da4339e66f | -8.05839 | -43.10609 | 2025-07-31 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 3a4db2bb-de08-3cda-af91-28866d267d76 | -10.61203 | -45.26296 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a29513f-42f1-3b08-a4af-1e7e07ddbecf | -13.50675 | -45.6478 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3df1f08-3cff-35d1-a2c2-1dc3d517918b | -7.32916 | -44.66889 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42221e12-8a7b-3156-b942-e00aed5e9862 | -9.63266 | -43.85165 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a20bd5f-6d83-3de2-99be-ead9480b0169 | -11.48601 | -43.22315 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ffe61390-79b5-392d-b5e2-46aae508b2a2 | -8.17863 | -45.01643 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65ed4927-4f6a-3cae-a635-9629eccbce75 | -12.7076 | -47.7925 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb26926d-1665-3db8-9344-c946047526eb | -12.82039 | -43.08977 | 2025-07-31 04:10:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| abded4bb-a7af-3a5b-acdf-3c3bc57cd623 | -10.93239 | -44.50127 | 2025-07-31 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4518c45e-4e8d-3cce-80de-740f20b0eeb7 | -11.54053 | -44.24267 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef89594d-6618-3431-889f-44e5a59e95c5 | -11.74602 | -48.18469 | 2025-07-31 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 869f9d36-78db-3033-a0bc-f336d6869c7e | -7.74897 | -51.09215 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 100f38a7-3f35-31e0-8b33-10d6c595ee7f | -10.69966 | -48.86531 | 2025-07-31 04:10:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4bf45b0-65b0-3fa3-9d64-eea0775666b9 | -7.87463 | -45.53947 | 2025-07-31 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1abd40e4-496c-32d9-9f5a-9240fb6a3da5 | -10.22241 | -47.98407 | 2025-07-31 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00d0f6fc-d649-33ad-ada4-5f5fcf2e42dc | -10.82953 | -42.69344 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a56fd21-94f9-31a9-8f5b-d2782c60cdba | -11.74535 | -48.18847 | 2025-07-31 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 74a1aaff-907d-3993-b4d9-40f302f99b1d | -11.13091 | -48.64609 | 2025-07-31 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4173f9d9-d5f0-3b93-bc2d-0a149e107ed5 | -10.61001 | -43.30199 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f73f8d26-949b-3e92-8dd7-22b70c816ed9 | -6.38203 | -53.33428 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22668acd-cd92-302b-969d-58655cea1e80 | -10.88934 | -45.80957 | 2025-07-31 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4417898-d332-326e-ba56-4f3b215ce872 | -12.60407 | -48.09377 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74bd6fa7-3446-3028-9ba1-d3638a2fc72e | -8.59086 | -45.52972 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 538e0b5e-5960-3ab5-9141-e151ad3eae7b | -12.55949 | -44.72132 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7399c587-c4df-34e8-a9ee-2bbd5c7a1ddb | -10.61559 | -45.26357 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c65dd374-f06f-30d5-8dcf-af4045adcefb | -11.9883 | -46.67626 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58e66643-0377-3cf7-82de-ded44d696476 | -7.64697 | -49.79525 | 2025-07-31 04:10:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 449b0f55-50fe-3e21-9421-30ee0863907c | -10.6144 | -43.31731 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e66a53ce-bd51-3da7-99e4-d096e0803612 | -6.46325 | -44.57079 | 2025-07-31 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3033dcf-91eb-3f3c-9c98-c39bc0571da8 | -10.98835 | -43.12048 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed8a1f21-f333-33b8-a8e3-8d7eda986e27 | -8.4449 | -45.14437 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c126b9b-f11e-392d-83f9-54b16c4bd41f | -11.96784 | -46.68491 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97914311-8c05-3ccc-9525-572bb8b4f58c | -8.06118 | -43.11023 | 2025-07-31 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0110c585-bcb4-38a8-8009-9c5a41fdf2e7 | -9.01618 | -47.97832 | 2025-07-31 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b42bdb0-f8a1-3e35-bb08-f0eab9ccea98 | -11.98523 | -46.67378 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e355836-c718-3a28-a586-bae6fde5c873 | -5.72165 | -49.10824 | 2025-07-31 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1795d2-4415-3720-9234-3a5ba81483fd | -12.55607 | -44.72074 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
