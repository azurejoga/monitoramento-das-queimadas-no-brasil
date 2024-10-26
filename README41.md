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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f71de6dc-8834-3bca-bc8e-f1a1dd2bfb5f | -2.92192 | -48.95662 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 155a7038-e09e-360e-822b-af5a53917361 | -2.9207 | -48.95982 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cea6cc8b-7e5c-390c-8254-f789d066e1e5 | -3.45712 | -47.67134 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2234ec8c-57d7-3775-8437-b17cbf956e30 | -3.45702 | -47.66912 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8abcd10b-4dcc-3d18-a224-f9d3ca318fe0 | -3.45631 | -47.67363 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee077c17-620d-3299-8df5-c70d7eaaf40f | -2.66622 | -47.40066 | 2024-10-26 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b3c2bb00-4350-371b-bfa2-5e3e5ef85acc | -2.51304 | -47.58532 | 2024-10-26 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77d5fed1-b76f-329f-badd-2b825293624f | -2.34554 | -47.49822 | 2024-10-26 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa8af86e-1263-3639-90a4-0e33d7469cec | -2.34482 | -47.50274 | 2024-10-26 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2df92f9-b5b8-3edd-b268-b97115c9f2df | -3.48727 | -48.24385 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7db64b9f-9508-3d5e-833c-e4716b6ad7f9 | -3.48339 | -48.2433 | 2024-10-26 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aa353b1-66ac-32e8-a1b0-c34f80eca687 | -2.97541 | -47.99379 | 2024-10-26 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccd75e15-a547-36cf-8ae8-ad123ee618d0 | -2.97414 | -47.9916 | 2024-10-26 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2d00b9d-3c81-3654-a7f5-e5dadb047cec | -2.97158 | -47.99316 | 2024-10-26 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a38e224-dd60-3330-8947-e87f9991b71c | -2.89356 | -48.27504 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a82b4991-4b8a-3190-a356-c47945ee0c9e | -2.892 | -48.28488 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aeda991-7e84-32d5-baf7-476434eddd9d | -2.89121 | -48.28979 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1441cf9b-3377-30ba-80ad-e965533c7312 | -2.8873 | -48.28916 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6dd85e2-955d-30fc-b77e-77f225afd1bd | -2.77774 | -48.56546 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24796601-6acc-3231-83c3-4c1f2302b491 | -2.74976 | -48.71076 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a72e1ce-87aa-3e98-9220-c2f5507d6294 | -2.74629 | -48.7067 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 05877e01-e3dd-3688-9f61-04208f3ce8db | -2.74573 | -48.71012 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a685aa92-052a-3745-96a3-effa3e9ed179 | -2.74546 | -48.70657 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d92ec437-4051-375d-9da5-4b72c2eb3bb7 | -2.74492 | -48.71003 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e5bd049-15f2-3757-ab80-1369d0301e12 | -2.68604 | -48.63974 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ae89580-3a15-3abf-ae32-e9eacc25845d | -2.64035 | -48.56004 | 2024-10-26 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 618c6fd9-bebf-3943-87ea-4c0bcc1348f4 | -2.58393 | -48.15802 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9f4eda2-58f2-360a-8213-f05f9aac2d42 | -2.57841 | -48.44845 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab8dc4fc-555c-36c1-9a4b-c88c5198ef79 | -2.57638 | -48.45004 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fbfbd35-d4b3-314f-a7a9-6a388058e83c | -2.56834 | -48.13056 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76082015-0a22-3ca3-a548-2278299d1821 | -2.47669 | -48.05437 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2200de1-63c3-380c-8cc0-ff13642ce626 | -2.47358 | -48.04892 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c845dd3-557f-31ea-839a-064361d21935 | -2.47281 | -48.05374 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbb4c49b-0694-3b0d-b455-b62982edf446 | -2.44524 | -48.6147 | 2024-10-26 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff1d5b9c-da25-3d3c-af0c-f11f3f0033ea | -2.44265 | -48.39393 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| faa5c0b1-c285-3f28-b211-f32c4d6b4f2a | -2.44011 | -48.46133 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d06fe10-dca8-39f7-9709-6bd288a0de07 | -2.43614 | -48.46066 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a3ec2c-62c2-3200-a0e5-e3d9c676a883 | -2.36762 | -48.28695 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1557c89e-8825-31c1-8b3d-43d92d8c0d12 | -2.36684 | -48.29191 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 18e4cc52-f716-3d4a-bd0e-da223344aaa7 | -2.32777 | -48.43617 | 2024-10-26 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a89dca-c756-3d29-9dd9-f456307c7bd0 | -2.19978 | -48.81976 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b559d7ec-d92d-3998-8d5f-2c811c6f8121 | -2.19629 | -48.81549 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cc509bd8-1d15-36b2-9cc2-17021ee63530 | -2.1957 | -48.8191 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 40e669cd-69ae-3725-8ce7-1463423dea5f | -2.16715 | -48.82264 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e47f041f-0832-3773-a19a-36f1b1c13006 | -4.75253 | -49.24184 | 2024-10-26 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff93ce77-9e13-389c-9349-a4a330d6f61b | -4.75088 | -49.20164 | 2024-10-26 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50090290-94c7-34b8-9b6f-e9684cfa9ebc | -4.7503 | -49.20514 | 2024-10-26 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2445680e-adbd-380c-9e10-3d7bc29739aa | -4.71919 | -49.08929 | 2024-10-26 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aabacfb-0d60-3dcb-a30b-d986d6a344be | -4.71863 | -49.09277 | 2024-10-26 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c321b7d7-703f-394d-9876-76ee3ba64a8a | -3.90271 | -49.077 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad796df1-d543-39f5-a615-6218eeacd6f3 | -3.89866 | -49.07637 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1993f0d4-1fa0-3b50-bc59-7a6bce320471 | -3.82249 | -48.95957 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 018b41d5-da85-3610-bf04-329b18842f11 | -3.82192 | -48.96305 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c45d7928-21bc-3ab9-953b-706d9f090aac | -3.81847 | -48.95891 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c274e72-711f-3724-9a46-b15b5201cafd | -5.13048 | -48.09452 | 2024-10-26 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a54e29-558b-30cc-92ba-27602e3d0352 | -4.89347 | -48.72761 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6145f95-f10d-381a-a67a-905a24360de1 | -4.89008 | -48.64926 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 251471da-0a73-31a5-a8b5-d7b9c315a041 | -4.88771 | -48.66391 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffedd4b8-4d0d-3e73-86a0-f17758b9477a | -4.88382 | -48.66327 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7afb8bf2-2d2b-329e-b45f-a32e2c34a659 | -4.87634 | -48.56242 | 2024-10-26 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7925309-707e-32a8-b5ce-9c4337cc9f3a | -4.87248 | -48.56174 | 2024-10-26 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0c91811-05c4-3a23-b049-46d649ef7467 | -4.84734 | -48.64215 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87129fb7-2e97-3e5e-a708-093cb0435fe7 | -4.8436 | -48.61642 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43dc6555-8863-30f5-8543-f2d87f1b7ad2 | -4.84054 | -48.61086 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 50fda397-068d-33cf-b1d2-92f0d4462d48 | -4.83972 | -48.61581 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b08e424f-5f00-3886-bf8a-6c71a37c53c3 | -4.83891 | -48.62072 | 2024-10-26 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12405117-a405-3bf9-9982-4c799d6e79c7 | -4.70325 | -47.96445 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f48f7239-6f3e-35c4-996b-fcd198ec0252 | -4.7002 | -47.96237 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84d2cae9-3c27-3ffe-be73-04f5bdff545a | -4.6995 | -47.96386 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f5e4525-f026-3db0-9148-7f4f299926cd | -4.58354 | -48.01421 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30497cc3-029d-39ce-8234-bb0933a9cc5d | -4.58281 | -48.01628 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd4d14ca-b052-3735-91d9-494f114a9cef | -4.58136 | -48.02539 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 87e2d677-f52d-3af7-a8bc-8e7497da84bc | -4.58127 | -48.02785 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 78f1a644-3045-39e3-8465-6ebddb45d707 | -4.58063 | -48.02996 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| e76ff0a5-98d6-3fca-841f-5260ebf1d55e | -4.57833 | -48.0202 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 4d8f3820-41dc-38d0-afd7-e1388d663a04 | -4.57827 | -48.02265 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 9a51a789-deea-358d-9561-e01a7253ba81 | -4.5776 | -48.02476 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 8907f123-6ca6-33b8-95a4-f5f4ff7e6b33 | -4.57752 | -48.02721 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 29a9fc8d-cf72-37ce-be61-7db69945d8e5 | -4.57687 | -48.02933 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 7de82299-03d2-34e8-9a5c-fa07da7031c5 | -4.57676 | -48.03179 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 182357fc-4bc7-3e8b-ae33-daa8891216fd | -4.57613 | -48.03395 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| e5ef69d9-9738-373e-9984-06c116766738 | -4.57384 | -48.02415 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2c8e577e-43a1-3ab9-b055-9868ca1f020d | -4.57311 | -48.02873 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ca59783a-8e8a-3550-921e-6b063a5ff48e | -4.57236 | -48.03338 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 829abddc-1ed4-3d87-9f4f-a7302ae34430 | -4.57081 | -48.01898 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 65569ae8-b7a5-316f-8cd9-613168937e12 | -4.57007 | -48.02355 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 9a886377-71e5-3094-a8d7-964e3b958dc7 | -4.56934 | -48.02815 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| e3a54692-cf4a-3dd2-aff1-f2ccaa932f7e | -4.5686 | -48.03278 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ea4fea7d-f87c-36a8-bec4-526fde4f69a8 | -4.56631 | -48.02296 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6d2bd12-4b86-3fbb-a170-1db7746c14d2 | -4.52017 | -48.21324 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8bfe751-9b38-3235-a198-5e5769b1ecfa | -4.51942 | -48.21794 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02441b20-1a83-3f3f-b72e-cc428a068535 | -4.51181 | -48.21663 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c262d462-bdc8-3261-8826-a5f59c54ca3d | -4.51106 | -48.22129 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f742fbc5-5d65-3ba3-80ae-7a26a4aef3c0 | -4.48816 | -48.12264 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9de8748d-c7bd-3369-aefd-c0e3bb8d06a8 | -4.48438 | -48.12204 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 974c6498-599c-3558-8c20-f25d71ed02bb | -4.47094 | -47.84918 | 2024-10-26 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe1d6197-7346-3bb0-8c3f-0cfbf2d6c9ff | -4.34105 | -48.62945 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1ed24d0-b2fc-3040-aedf-00eee5f3dde4 | -4.33634 | -48.63376 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2bfd8a-d035-3511-9f42-7cb82f699a99 | -4.33553 | -48.63873 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec598771-651b-3444-aa22-1a6b422dd673 | -4.33242 | -48.63317 | 2024-10-26 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README42.md)
