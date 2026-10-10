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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db0ea6e1-5ecd-3a13-ade5-88811999ff10 | -3.47487 | -50.08754 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef6c02be-fc76-31be-8c2f-0e0050c09913 | -7.05301 | -40.95191 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5256c70-7205-3d74-8508-605bcbe969f5 | -2.56884 | -57.4192 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 496a3613-c984-3057-b131-0118af414ed7 | -5.24692 | -42.23264 | 2026-10-10 04:44:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 744cf20e-9777-3500-9284-ef35b258880e | -5.72246 | -53.49468 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c4eda3-4574-358c-aedf-e41b856d7d17 | -3.19112 | -50.54665 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e585ec70-1e6c-3c76-8fb4-64d831c1f714 | -3.03486 | -53.8898 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2984b716-894f-3f45-8d43-b2c01b640b63 | -4.68668 | -47.43723 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d73875fd-ca89-3e0d-bfc7-ce0ef8ee2a25 | -4.40421 | -49.78577 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 368f4d57-d2e7-3ed4-b133-1fe016056f5c | -3.45784 | -50.58672 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6c4f6f0-22ce-3e1f-9379-29c44b024813 | -3.30929 | -53.70222 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 734949b9-cb87-3eb3-a909-95327401d80b | -3.85757 | -44.04527 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f309718-b47b-337b-b0ad-3ce4175c5670 | -5.74791 | -45.13074 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4fc2935c-290f-3ecc-b37f-50fc6fa23474 | -1.27017 | -55.7531 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f856e427-2315-333e-851b-67870f1e154b | -3.17345 | -49.45456 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 157e0438-6124-3623-bdc7-d34e927d2945 | -3.10536 | -51.36459 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83c9fe4d-e9ac-3acb-8fcc-dbbc1031edf2 | -3.46753 | -50.59726 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0735450-70f3-3ea1-a946-10118a8fa385 | -7.0661 | -40.95918 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 538234b5-7b14-35b1-9323-c4de11ecc0ac | -2.82534 | -51.03917 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb48f484-1982-3d01-9812-a4645ec1abf4 | -4.64136 | -48.85816 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630c49f8-7a53-3a06-b1f2-838c944bcd5f | -3.54508 | -54.74089 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 70052c70-c292-3455-8222-8e23d7e98356 | -1.74302 | -47.16402 | 2026-10-10 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef32307a-4e20-3238-9955-9a0c9d91e1c7 | -3.21702 | -50.55082 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f7ecc6c-6be8-385b-a175-78a069c234ee | -6.46056 | -45.80977 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e14e46d7-dede-3cb2-9e06-56ee94920b74 | -5.69443 | -53.46321 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7964ac28-1152-3fc7-9dd2-ded058fae8f2 | -3.73286 | -57.16191 | 2026-10-10 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea8f8131-780d-3b5d-847c-8206068870a4 | -3.84732 | -55.79387 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c9b305f8-cf0b-3239-a4f5-5a149a9bc99b | -3.12293 | -54.16962 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a23c2a5-ece8-3a4b-9673-78b132ea95a8 | -3.74753 | -59.39721 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb46c174-f609-350c-a440-35797dd3a53c | -3.31509 | -54.00698 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b03a7e5a-a540-35fc-88f7-9bcbec6e9c02 | -5.958 | -40.9146 | 2026-10-10 04:44:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c998eb2b-2a0e-3dee-b986-fd9d34ce0c30 | -5.74087 | -45.12968 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da0b3365-552f-3cb8-8459-deab3cb91989 | -3.9931 | -59.362 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cdb9c44-2633-3741-ac37-b62749a94bf9 | -6.04134 | -49.65995 | 2026-10-10 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f10c5b7-03ab-307f-a7d9-71634165b10f | -4.7379 | -55.67086 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52759b3-fc6e-33fd-a159-0f5ee80c0252 | -4.39909 | -49.77292 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69f274ae-4454-355b-8e32-183598088c12 | -4.10391 | -54.01923 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 41fb2f97-3230-3b9e-992e-66941749a668 | -2.39071 | -51.30463 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b1bfc5-0e2f-3996-892b-7ce796a7a569 | -1.27664 | -55.74731 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5dac4a2-02b6-3325-9292-51baed71c5c3 | -2.74695 | -54.10307 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d594472-2044-305b-96ae-d1bc6e6108d4 | -6.96385 | -44.9582 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a4981ab-b7a9-319c-9f9d-1a6d7152fa30 | -3.89782 | -55.81354 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04297f49-dc5c-3045-9805-d9cd41f319f2 | -3.11707 | -54.93536 | 2026-10-10 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b60785ba-deac-349e-bbde-0f10cc69ed8f | -3.43714 | -54.5436 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afac5481-9f26-3376-b9a3-b8b2f4f4185f | -3.91278 | -55.81942 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54ba17cb-24af-3ead-8b78-e74fcf2a3614 | -5.95846 | -40.91679 | 2026-10-10 04:44:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ffe2bced-8b23-319c-8858-4fc465e4c180 | -3.10188 | -53.93695 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f9c3d80-49dd-3e25-b917-582db45da0a5 | -5.99307 | -41.36596 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2561d5cf-10a4-3e3a-8462-9188c9b64d79 | -5.74427 | -45.13316 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed820dd4-821c-31ac-9b6b-6baff711575a | -3.57856 | -54.7193 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c396d3e-2069-3d47-be21-1b9de8f3eddf | -4.39348 | -46.53311 | 2026-10-10 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abfb8f11-79f2-3779-98c1-053e00c22293 | -2.60878 | -56.48374 | 2026-10-10 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee5bdb6e-d527-3ab9-961e-ef7e3d88453f | -3.19183 | -50.54231 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70981578-14c4-3354-b5dd-000ebbc5e672 | 0.30047 | -51.40232 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40cd9dc-6274-3fc7-b983-4a495abb1dd9 | -3.85737 | -44.04781 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 40b0bd81-9d38-3b40-b6db-15a403ab615d | -3.69772 | -47.68208 | 2026-10-10 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4072e6b-4aaf-3aa1-88a5-3f2eac48fdad | 1.16495 | -50.14865 | 2026-10-10 04:44:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a105032-5078-3e0d-b04f-94587b0d38cb | -3.11111 | -53.79492 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59e217bb-aac4-356e-93ec-d8f80816f0e1 | -3.10479 | -50.31851 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0d3747d-d81b-3562-85d2-0d457dd1d512 | -2.99318 | -51.04725 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98346180-fbd7-3dbd-9d39-41042ed5062e | -3.21402 | -50.54589 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a5876ae-ce34-34d9-90b4-5ea84163441b | -1.45249 | -54.47287 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c389bfdc-3e84-3b51-b9a5-582ad42558b5 | -3.50249 | -49.58405 | 2026-10-10 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7421454e-2326-30a3-94fb-9d1a005e4ca8 | -3.2526 | -50.42377 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c6e0173-d6a2-346c-a914-19db761e6f47 | -3.25701 | -54.18555 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2b9e5d1e-c6e9-327d-9742-bf9470b7248f | -4.39737 | -46.53016 | 2026-10-10 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e72a65a2-2ae6-31c0-8e59-b53dbb32f46a | -3.24483 | -54.02977 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f23eccea-fb99-30a4-a6c9-37c63225f89b | -5.79173 | -53.79832 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6af037cf-5ef9-357a-8079-1b2766096887 | 0.48596 | -50.78972 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55fe080c-98ac-3539-9ef7-ac5b4dde2e86 | -3.17633 | -49.45903 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9953e27d-6a0d-3152-a1a4-c205f8fdcc95 | -6.06798 | -44.66362 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06cc43af-dc21-3813-aab9-76c807909d01 | -3.31698 | -54.17111 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 535e9fbf-0d75-3d96-b8b9-7b147aaee077 | -5.49413 | -43.97733 | 2026-10-10 04:44:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81d7999d-e6e7-3bbe-a94b-350c6417e343 | -7.067 | -41.60081 | 2026-10-10 04:44:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2aeda57c-c8ee-33aa-a5ef-3124a85aa310 | -6.4953 | -41.81527 | 2026-10-10 04:44:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b73adc2-0d9f-347f-9a55-4159d3d35716 | -4.41026 | -49.77074 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9333c476-a250-36ba-9705-7ea38c20583d | -3.98108 | -59.35428 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4b148fd-9550-317a-b10e-b35b1550505e | -4.39403 | -46.52963 | 2026-10-10 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf9ef81d-bb69-335e-bbc5-6d989f0443c7 | -2.99421 | -53.90719 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5006a5fc-f8fa-3289-ac06-1c4e98484d63 | -6.20893 | -46.64271 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 924b1a40-3664-37bb-bc94-9dcba0467d2a | -3.27928 | -54.69682 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cb41799-7294-37bb-9057-2ed3c42d35de | -3.56589 | -54.68342 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e6f90fe-4a1a-3f20-8cf8-6e83e0ea9364 | -2.22485 | -48.35732 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dbef553-4d70-33ce-a885-354624e80d1b | -3.38449 | -44.4812 | 2026-10-10 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84f34acb-59a6-38ee-8246-0df6006bf4ad | -4.0999 | -54.01627 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 06eea162-fac2-30d3-961d-701e8c2901f8 | -4.40324 | -49.76959 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c880606d-13e3-362f-aff5-10c23a38fdd1 | -3.90937 | -55.90131 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8dc35ad-18c4-3ab4-b234-341aefb75950 | -4.36364 | -54.76258 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15045659-5f03-340e-8714-cc7be7b3288b | -3.35426 | -50.41616 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aab84463-6a82-333a-8023-85216e46b918 | -3.48728 | -50.33245 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 148662b5-56a9-3487-aac6-36d613bae8eb | -5.11512 | -46.22591 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 037970d1-f008-3074-ae3c-25651585c200 | -3.20962 | -50.54964 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21bc1b4c-ec5f-3753-bbef-8354e0453719 | -4.68568 | -48.51927 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5775460-a69b-37ac-b924-543d707a8b53 | -3.23183 | -50.18222 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5929ae65-eca0-3a5b-87d3-ff8b67713e3b | -3.4706 | -50.09103 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1bdded74-7f4a-311a-b9d5-ecf84ce778f6 | -3.10839 | -54.19089 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a2c1cc1-4522-34a0-b3cd-f442b81b185d | -7.23721 | -44.16416 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 801a3c3a-99b4-3c87-8ec7-933d44def9d9 | -3.94318 | -56.05076 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae28b633-58cc-34e7-8a2e-6ea90c9e0b5a | -3.35196 | -50.40707 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4651ff56-9a5f-326a-906b-a269400baf15 | -3.12023 | -53.79647 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README70.md)
