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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9de453a3-59f0-391e-843b-26bd2eebf078 | -10.08649 | -53.86201 | 2025-07-31 06:12:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28a45e19-32c5-3d50-8dda-535160defdfb | -6.66996 | -56.40347 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 25326076-24f1-340b-9998-7ce253b270bd | -6.67396 | -56.395 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 0641c3ec-e4ed-3254-8acc-cd0ad20f8ddd | -11.74854 | -48.17711 | 2025-07-31 06:12:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 65a7c12f-982f-3e73-ac75-6573305c90b7 | -6.52118 | -56.19929 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8c8aed3a-9c76-3c25-af6f-5cb7b1be4dd9 | -6.50742 | -56.19153 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 50076ba0-c37f-38f7-a642-b011e34868b8 | -6.67162 | -56.40926 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bc2f61fa-cc53-3a71-8e8c-a4c3288773e7 | -6.66119 | -56.38724 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 7bf860c5-d24e-398a-ab6f-b09e975f16ce | -6.62178 | -59.97309 | 2025-07-31 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 53af8771-7497-36e9-8d55-5aab50e53801 | -6.67219 | -56.38926 | 2025-07-31 06:12:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 7f8e8926-d059-3ab2-8bb3-66f8305c02f8 | -20.1931 | -50.50593 | 2025-07-31 06:14:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 6fa1c81e-c99e-3a9f-9c01-891a37b4458d | -20.18632 | -50.51221 | 2025-07-31 06:14:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| c1e879ad-1cad-3955-88f8-a2d0ca7b5050 | -6.62584 | -59.98169 | 2025-07-31 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d503e07e-021e-3b17-b163-e92effc1ab00 | -17.02269 | -49.2317 | 2025-07-31 06:14:00 | AQUA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ba41058c-7d9c-388d-8570-87459ae6639b | -20.19486 | -50.49223 | 2025-07-31 06:14:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 326990dc-8e1c-36f0-8b69-a2cf5bcff9cc | -20.18798 | -50.49853 | 2025-07-31 06:14:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.1 |
| def65ab3-3914-3f59-8b49-9c551f064a72 | -6.61881 | -59.98102 | 2025-07-31 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d7f837e-57ca-372f-a051-f7fad05edac1 | -8.07 | -43.1216 | 2025-07-31 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| f930591a-b3fc-3f45-a2ad-0a4daefd9f38 | -8.0703 | -43.0981 | 2025-07-31 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| fc028b49-0193-3d94-890a-6cc198dcd6ed | -8.0513 | -43.1001 | 2025-07-31 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 71976b03-09ca-3d65-a5bd-24a7d4776841 | -6.6725 | -56.4029 | 2025-07-31 06:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| eef012f0-9f91-312c-b692-e35ca84b083a | -13.5233 | -45.6925 | 2025-07-31 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| eb8dc4f2-1d18-3eb3-b615-0ef9928ca7d0 | -8.07 | -43.1216 | 2025-07-31 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 27c53e0f-c9cc-32a5-8072-8b849a5740b0 | -8.0513 | -43.1001 | 2025-07-31 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 65e2866d-8a41-362f-9c92-b79892c4b259 | -8.0703 | -43.0981 | 2025-07-31 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 77f5a96a-dded-3a7d-9d85-eb2808c24e9a | -8.051 | -43.1237 | 2025-07-31 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 69772a53-305a-3407-bd49-5e8cb6214ba1 | -8.051 | -43.1237 | 2025-07-31 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| aa9f8288-0fd6-3caa-b175-35f914f603ed | -8.0703 | -43.0981 | 2025-07-31 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 612a274c-0f0c-3b3b-a922-9c08555622d0 | -8.0513 | -43.1001 | 2025-07-31 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| f6cb1763-fba6-335e-8d6e-526f760e9229 | -8.0513 | -43.1001 | 2025-07-31 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 70911317-c462-3fa1-879b-43e294f69886 | -8.051 | -43.1237 | 2025-07-31 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 0df66c8a-0cfe-3e72-9b6e-2c363a962c48 | -8.07 | -43.1216 | 2025-07-31 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 5caff196-676b-3df2-a5e0-40b7f8608059 | -8.0703 | -43.0981 | 2025-07-31 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| ba54024f-1a44-3289-a30d-d50c9694186b | -13.5233 | -45.6925 | 2025-07-31 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f6c330f4-2ae2-3af4-b993-ec6d74d5ac94 | -8.0513 | -43.1001 | 2025-07-31 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| 8bbf121c-2090-3c82-b6ec-122d9ce5d30f | -8.051 | -43.1237 | 2025-07-31 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 6c7eae29-5f45-3c83-84cc-3a9668139466 | -8.0703 | -43.0981 | 2025-07-31 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 0bff54ae-8f34-3c7e-b86b-ef70c9145bde | -8.07 | -43.1216 | 2025-07-31 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 1f5f8f47-6e77-37ea-8008-412235848727 | -8.0703 | -43.0981 | 2025-07-31 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 4ec00f9d-1a38-3dc6-bef9-5389c27d5daa | -8.0513 | -43.1001 | 2025-07-31 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| c129b54f-3288-3bb8-9a82-cd29bea4f9ac | -8.07 | -43.1216 | 2025-07-31 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 5be83927-aa13-3d0c-ac5f-305d073a5ab1 | -8.0513 | -43.1001 | 2025-07-31 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| eb60ff48-8bc9-383f-af97-aac45dcd4d32 | -8.07 | -43.1216 | 2025-07-31 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 9422c30e-3fac-3a29-94cf-3e5cc6c36eee | -8.051 | -43.1237 | 2025-07-31 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 57bb557a-e25f-342a-8612-ac7f3ffe70ee | -8.0703 | -43.0981 | 2025-07-31 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 53a8c4d8-aa6e-3efd-a053-7bd44ad9b681 | -13.5049 | -45.6494 | 2025-07-31 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d60c5fb1-ecb5-31ba-9fa7-720000140c0f | -11.5495 | -44.2876 | 2025-07-31 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d1a93606-b111-3bde-bd53-7c429e54b980 | -13.5049 | -45.6494 | 2025-07-31 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 821207fc-e220-3285-8730-59b5af3059a0 | -7.7363 | -51.0959 | 2025-07-31 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 2966a24d-4c17-33e8-803a-7722af148cf8 | -7.755 | -51.0946 | 2025-07-31 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 42fcbea1-d8fa-38b8-9373-179ac3acfdd9 | -11.5495 | -44.2876 | 2025-07-31 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 95da2f41-e08b-38ef-971a-f5408c28ea70 | -7.755 | -51.0946 | 2025-07-31 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 28a8fac5-8280-38d0-b0f5-6c89a9425150 | -11.5307 | -44.267 | 2025-07-31 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| efac537d-0bf1-3290-b461-a5511003b0dc | -11.5495 | -44.2876 | 2025-07-31 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 40a6dcd1-237a-32fb-b404-b4f62be7752d | -7.7363 | -51.0959 | 2025-07-31 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 865e4978-3333-3ce5-9aac-bfc07795acb4 | -13.5233 | -45.6925 | 2025-07-31 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3038f3e9-474e-3b3d-a161-aed522530a6a | -11.5303 | -44.2904 | 2025-07-31 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 82294b22-0441-327e-b57f-182be611e1ba | -13.5238 | -45.6693 | 2025-07-31 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| bf61ef96-aa83-3d04-8148-03a670c0d47c | -11.5499 | -44.2641 | 2025-07-31 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| a31068c6-9e07-3e6b-b203-12912584b204 | -11.5303 | -44.2904 | 2025-07-31 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 56a074ad-a506-357e-94eb-bd8c118a826e | -11.5495 | -44.2876 | 2025-07-31 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| c2e10b30-6ba8-3c27-a03c-f0c14e20efe6 | -10.6169 | -45.2512 | 2025-07-31 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 010b8677-f565-3708-b7e2-105d226877dd | -11.5307 | -44.267 | 2025-07-31 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 9c59ace7-906d-34b3-b31e-b66932e2c922 | -10.636 | -45.2487 | 2025-07-31 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 317ec1ed-bb19-3780-aa27-1176714b410a | -11.5303 | -44.2904 | 2025-07-31 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 225.1 |
| a59a7731-e63c-33a3-86da-d9f509998df6 | -11.5499 | -44.2641 | 2025-07-31 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c04f7c28-b1e1-3566-ac3e-be8fd8376e99 | -11.5307 | -44.267 | 2025-07-31 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 043e9312-9ed2-3cac-b1c3-9c85d15b9d43 | -11.5495 | -44.2876 | 2025-07-31 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 1df03278-07ff-3489-8088-e70c46c54375 | -11.5495 | -44.2876 | 2025-07-31 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 303.9 |
| 96a75f37-cd37-3ffb-944a-0dba7145df6c | -11.5499 | -44.2641 | 2025-07-31 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 5724efd6-ab92-3e74-9fa5-ae818b0e1376 | -11.5307 | -44.267 | 2025-07-31 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| a9688943-837f-36de-802e-9e1dd0e18d21 | -10.6169 | -45.2512 | 2025-07-31 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3e034938-a990-36dd-a33a-8f02f94ab5d3 | -10.6165 | -45.2742 | 2025-07-31 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 992260d5-f137-398e-a8bc-4093fffa2c98 | -13.5238 | -45.6693 | 2025-07-31 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 45e0d0a2-bf11-39ff-8477-02f1b9597e0b | -10.636 | -45.2487 | 2025-07-31 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f4202188-c22d-317f-be96-ea1ba18e5968 | -11.5303 | -44.2904 | 2025-07-31 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 261.9 |
| 3f2eebd8-48e1-3915-a316-d3c2630a67d9 | -13.5233 | -45.6925 | 2025-07-31 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 88cb6f7c-e70e-3dcd-ad34-50427d920d39 | -11.5303 | -44.2904 | 2025-07-31 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 5f09ecf7-5c5d-3376-8cd2-3d6a7ec8640f | -10.6169 | -45.2512 | 2025-07-31 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1befb5c3-3cdb-36cc-a77c-8417d4986419 | -10.6165 | -45.2742 | 2025-07-31 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8cdd5574-72a6-325e-bffe-70eb7ce545d8 | -11.5495 | -44.2876 | 2025-07-31 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 866cc8ae-8065-3428-b496-125e81135afb | -10.636 | -45.2487 | 2025-07-31 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| fc215121-e52b-3008-a215-b2a69b15e472 | -10.4534 | -47.2356 | 2025-07-31 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9d45026c-2225-3ecc-abfd-f7cf4990e7b3 | -11.5303 | -44.2904 | 2025-07-31 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| bc7d7b22-7c8c-3dce-b59c-a11910c8bd9d | -11.5499 | -44.2641 | 2025-07-31 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5388a709-c173-3f5d-b8d5-81153893c33b | -11.5495 | -44.2876 | 2025-07-31 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 308.8 |
| ed12114e-4b67-38a1-873d-b8b6776e5bf3 | -10.636 | -45.2487 | 2025-07-31 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 17ec7ab9-15b0-37f8-97c1-cb4325ad836b | -13.5233 | -45.6925 | 2025-07-31 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 0c76c9d7-e9f1-3f60-be5f-4da4d8848cf7 | -13.5049 | -45.6494 | 2025-07-31 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 3d7907f8-42a1-39c1-998c-27885f9a6664 | -10.6169 | -45.2512 | 2025-07-31 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c4ecac80-a3da-3edc-913a-38ce4330766f | -11.5307 | -44.267 | 2025-07-31 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 61ddf854-cb3d-3379-803c-5aba4f34ee46 | -10.6165 | -45.2742 | 2025-07-31 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 7ad5612d-1ac0-3ca7-b7ec-1864e41cb546 | -10.6169 | -45.2512 | 2025-07-31 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 8ab8f395-3ffb-34e0-81d0-f6cf6df1c4c3 | -13.5238 | -45.6693 | 2025-07-31 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| df4a4037-6c27-3707-a964-d864378361cc | -13.5049 | -45.6494 | 2025-07-31 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.8 |
| bbce3738-2fb3-31c6-be0c-5bfeea08ec0d | -11.5303 | -44.2904 | 2025-07-31 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 1cf26586-3450-371c-baec-279c9ef539a3 | -10.6165 | -45.2742 | 2025-07-31 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3ae2c115-5001-34cb-a51f-6241f683146e | -10.4534 | -47.2356 | 2025-07-31 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| babba4b9-37b3-3d4a-9767-f9764ca9d8eb | -10.636 | -45.2487 | 2025-07-31 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 57db601e-bbd6-31b2-9fa0-06073af3e408 | -11.5499 | -44.2641 | 2025-07-31 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |


[Clique aqui para ver as próximas entradas](README19.md)
