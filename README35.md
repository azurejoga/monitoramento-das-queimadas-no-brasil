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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a41a98d-1894-3a79-96b2-d99c44f95fda | -4.89815 | -48.06704 | 2024-11-01 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86b5c2d3-08eb-3154-b1a3-538f061f3375 | -4.8976 | -48.07052 | 2024-11-01 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 559d90ed-6f94-321f-88f9-970d23526861 | -4.81056 | -48.68336 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec907d7-e071-3891-a7ef-724f8bcdb02b | -4.48503 | -48.12202 | 2024-11-01 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a09320a4-512a-358b-a3f6-91d6cf733b7c | -4.36133 | -48.21725 | 2024-11-01 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db78252-b0d3-364b-830c-4545d2926c13 | -4.36078 | -48.22073 | 2024-11-01 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec5457af-0549-3a32-b5a7-c470a07a4420 | -5.04278 | -47.9692 | 2024-11-01 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a879f383-6114-3b29-a70b-a1f6ba4d493e | -5.04223 | -47.97265 | 2024-11-01 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e66ab07c-9bbd-34c3-8614-9de0f0346b9d | -5.04169 | -47.97611 | 2024-11-01 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b8df45e-38f8-35b9-b8ca-2ad8db076556 | -5.03948 | -47.96866 | 2024-11-01 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d33c3b3d-c924-3859-9475-391bb04fdbc9 | -5.03893 | -47.97212 | 2024-11-01 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42bc86e9-ac8b-31bb-8701-f5c5cc53492d | -4.97032 | -49.37291 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8fb44d6-8ead-35be-9239-df3c7b591a7e | -4.96691 | -49.37236 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9f6e5e-2868-3267-8613-31a6a2a97f51 | -4.96633 | -49.37603 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26fcb78e-1168-335b-844a-e004dd9b8b03 | -5.98597 | -48.15009 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6f6d9fc-1f23-3735-9c5d-46d947090905 | -5.9728 | -48.19054 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 474b8bd4-288c-316f-a0b0-2f5e21a51dd1 | -5.98267 | -48.14957 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d73bc7d-6567-3ff2-9cd7-eca702f58298 | -5.8645 | -48.16691 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 396da1f8-c8c8-3194-b277-9205ad89f93f | -5.86119 | -48.16639 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01df299a-030b-3661-b47b-2d438214d49a | -5.71244 | -49.3173 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64785570-142d-382e-9f6a-58b8e8f836ec | -5.7108 | -49.30589 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01a00c59-0262-3080-a938-326c6b09a53f | -5.71022 | -49.30952 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7dafae4-84bd-354d-9c05-74c5cbf5a21e | -5.70906 | -49.31676 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e2d104-2a09-34b5-b1e5-7ab55cebf670 | -5.70848 | -49.32038 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 113d5b8e-0b2e-31da-8275-4933e7d96643 | -5.70568 | -49.31622 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28648ed1-0774-3a68-8bcd-221929af9397 | -5.6967 | -49.30737 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bc469e1-e6f7-3e85-b691-b5d447aadf14 | -5.52381 | -49.4893 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c315726-7865-3863-9333-d2b54431080a | -5.50965 | -49.20357 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fc34f01-86f1-382a-b136-d177e9b25eb3 | -5.46987 | -48.85603 | 2024-11-01 04:29:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6000a92-77f4-371e-bccb-7eaf5367f06b | -5.46208 | -48.84027 | 2024-11-01 04:29:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb19045-831d-3560-8b4f-08ca417dadc8 | -5.44841 | -48.0905 | 2024-11-01 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d679bd19-b75d-3ee8-8bdc-0819dd0a9265 | -5.38863 | -48.95611 | 2024-11-01 04:29:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46252e64-b7d5-377b-96f5-ed66812e3ee8 | -5.3133 | -49.13614 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af759597-508d-3fa3-b7ca-beb51a07579e | -5.3105 | -49.13199 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e89c0c51-1e2e-30c9-8ebd-5c47039a0255 | -5.28898 | -48.32431 | 2024-11-01 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59a7a0f7-57bf-335e-b372-379d4f0897be | -5.20503 | -48.23277 | 2024-11-01 04:29:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 229c21b5-cde2-3031-b766-36cb65560f9e | -5.17463 | -48.95561 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f480d338-f070-333a-946e-9661e9034bb7 | 0.32357 | -49.74169 | 2024-11-01 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e418d3f-aa53-3f4c-9191-a8185e879345 | 0.08907 | -49.86958 | 2024-11-01 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9f30709-e0a0-39fe-b525-8e522e9a82c4 | 0.08843 | -49.86656 | 2024-11-01 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 838a9010-691e-3bc5-b3fc-0a3548b74158 | 0.08839 | -49.86531 | 2024-11-01 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99620dfb-be1b-3815-acff-eb58b08c4c2e | 0.08541 | -49.87016 | 2024-11-01 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd4b3295-c871-3e26-8ecd-f39082bbb24a | 0.08473 | -49.8659 | 2024-11-01 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b5fc65-ee50-3273-94b3-23593ab79d46 | -2.19256 | -49.15891 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9a41a9a-bdc3-30d2-bf13-859be421870e | -2.00142 | -49.01037 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d2c63fc-e2d5-32e9-ace0-c111857ebcdc | -1.72319 | -48.75387 | 2024-11-01 04:29:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57e7616b-f733-3afd-a204-55cf5f8e8740 | -2.18867 | -48.84794 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2696bdd5-663d-361e-91a0-9bb414bf1eba | -1.03026 | -49.32361 | 2024-11-01 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e589e21-714e-3758-a591-97999eca385d | -2.19159 | -49.15849 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e0706ba-e68b-3aa5-a075-42793e33f0af | -2.17086 | -49.11674 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1140cda8-50b0-3d3f-9e29-e1f30f5d2bcf | -2.00202 | -49.00662 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 171270c6-8138-30cc-b172-ecda8592561c | -1.99617 | -49.02108 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0caa2f4-ddb8-3093-8a26-2861a665c734 | -2.89201 | -49.80327 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67f3f38d-eaca-3f6e-bbe2-bbbc39ef9016 | -2.85617 | -49.54965 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89046c4d-b927-3a4a-8e12-8ca0db41a133 | -2.83359 | -49.53416 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5b65029-765f-3b4f-a244-78be7798ba5a | -2.83009 | -49.53363 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c20cb345-4b9c-3d8c-a1d2-97c1e3b5dc3f | -2.81795 | -49.76816 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe1b20f1-25a9-3c88-a0db-67c77d47bd35 | -2.81733 | -49.77208 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b49daa6f-2ecc-37ce-ac87-d870e5eeb119 | -2.81443 | -49.76758 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 20c7ac5a-0505-3f51-a449-be7b059a6dda | -2.81381 | -49.77151 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d09b4e80-24e9-372c-9d69-31aac674a3a9 | -2.8109 | -49.76702 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 13b6c621-d9f5-34a1-8c8e-698e61b943e3 | -2.81028 | -49.77095 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a31b927a-4ea6-34b1-a8d5-0c9276d92e9d | -2.75728 | -49.17519 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6d5b482-4898-3a08-b66d-387aea3e9bd2 | -2.75668 | -49.17894 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 081973c6-a87d-3c2b-99a1-cae0aedafed4 | -2.75607 | -49.1827 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a67cba54-5bcc-395d-94b4-38e032154924 | -2.75239 | -49.45065 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2770c39c-3797-3432-b80c-badd19221c32 | -2.75066 | -49.82663 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47940ca7-3be4-30b7-b225-a596b8c389b5 | -2.74926 | -49.62889 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a610b3c-cf93-3d19-b7e7-24fb323d5c6d | -2.74864 | -49.63281 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c2ce641-7389-3972-86fd-7e6441c4c433 | -2.74616 | -49.80958 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09972e3c-a23f-371b-ae00-29a95f338834 | -2.74305 | -49.30831 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c148c0d-9b75-3c83-abae-9214a2f93381 | -2.65769 | -49.84121 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21898d09-cfd2-33d6-9653-e32445abc715 | -2.64426 | -49.24675 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 177deb16-10e4-3897-81a9-a5a730852764 | -2.64365 | -49.25053 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6bf91e6-8666-3f99-869f-150afbdef1b6 | -2.64305 | -49.25431 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9629730-f5f4-3dfb-9109-9d06670dc008 | -2.64055 | -49.20362 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8757dd5a-aad0-31bc-a0d9-771c42a76030 | -2.64012 | -49.18424 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c19390c-7cab-30cb-8af3-875e91c36356 | -2.62638 | -49.24781 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c5fe237-d97b-35f9-b23c-a0d9f9e9e6be | -2.62108 | -49.19763 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc1c2e5-0eb6-3a4b-b68a-62172c55164a | -2.62047 | -49.19658 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 297a0558-4e87-31ab-8fb4-e302f586e84a | -2.61763 | -49.19707 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02fbd4b8-2cf7-3746-a7ac-e86cd9d78205 | -2.60201 | -49.09457 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c55617d-d7cb-3e43-a0c1-abf4b750c9d0 | -2.60142 | -49.09832 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fed9bdb-ab6c-3f59-ba1d-062fc8918b9c | -2.5998 | -49.19811 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23484bef-d3e3-3a5d-97d9-bf7e7c236f4b | -2.59694 | -49.19379 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fae57b5-3550-3b9c-b32b-67539c30ce43 | -2.59635 | -49.19756 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1889e253-ad32-361c-8897-9a0103a572f6 | -2.59349 | -49.19325 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fed6e15-18d4-3ce3-a117-c8db79b7df3f | -2.57855 | -49.63492 | 2024-11-01 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd3321eb-925a-3ce1-8aa0-0d2aa9d29cf6 | -2.57724 | -49.11751 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb6e259e-08e2-370e-90e0-e3320f4ca6ac | -2.57691 | -49.07529 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0601af02-99f5-3edb-ae0c-94a82de151f0 | -2.57665 | -49.12126 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3927d774-203a-32cf-b8e0-428fb3975879 | -2.57347 | -49.07475 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd44f7eb-778b-3707-ab27-adc742ed4ef3 | -2.57324 | -50.05716 | 2024-11-01 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b2401b-ce3a-3873-a218-ccbae1fc8ee3 | -2.5732 | -49.12072 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c83e5ca-542a-34b1-81b8-6e99c3aa4870 | -2.5726 | -50.06126 | 2024-11-01 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02d1439a-ec0b-30b0-ae76-d7a4c97e24b1 | -2.56787 | -49.24341 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd564a6a-4b06-32ed-b6d8-16e1a799deb0 | -2.56543 | -49.8072 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23fa6d62-0db8-30b9-bf86-cc71a082de9e | -2.56441 | -49.24287 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 001bdd8f-b86d-3d71-aab2-d180c1c10c72 | -2.55975 | -49.16096 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5079f598-648b-3844-9fae-b72b81574615 | -2.55765 | -49.21855 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
