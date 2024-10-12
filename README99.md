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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 024daad0-25d8-3053-b176-aa46b9c8ded3 | -2.57204 | -54.26272 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab453942-c832-3474-aad3-5b282a2e2a86 | -2.00059 | -56.0187 | 2024-10-12 05:21:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de9a5d2a-be83-38d3-a72d-b4292552ae2a | -1.85893 | -55.44033 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15f50e42-63ef-34b0-b8f9-bdf6ae6c6bd4 | -1.76384 | -55.15681 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9286065-479e-382f-8af1-7c2ab320e4bd | -1.72044 | -55.1437 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 306e7ee9-8131-373c-9a2e-f535a258d649 | -1.67043 | -55.13611 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47954799-3c05-362e-b122-8d3549494b84 | -1.66659 | -55.1355 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7999721b-6fac-3d46-8bf1-b1942c26b8a0 | -1.66586 | -55.14025 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d569968c-db42-305a-822d-0ec172a6f94c | -1.63655 | -55.12601 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b8104a8-62c8-3f31-b7cf-06815cc73123 | -1.63496 | -55.12466 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2f1079-f7a4-3467-80fc-cfef56bc5ba0 | -1.63421 | -55.1294 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf162f79-9849-3d0e-8132-8a496c9972a2 | -1.6327 | -55.12543 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8892385d-2a78-3a3e-bf19-a1c546ce484a | -1.63057 | -55.17709 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e97ef3-0d72-3b7f-9793-404530919039 | -1.62866 | -55.17794 | 2024-10-12 05:21:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 748d23fd-8758-38c5-bf8d-b65e21e8e0f0 | -1.53877 | -55.41386 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edee54f0-b02a-35bd-9801-173e60feef36 | -1.52982 | -55.42172 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7da3d5-899a-35c5-b50e-97e665caa954 | -1.52676 | -55.41658 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3de1493c-5377-3bdf-a142-acffb0058601 | -1.52228 | -55.42056 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c392d56a-9e08-37c8-886b-e669b442ba4e | -1.26113 | -55.90812 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6b6f007-9406-38d2-aeb8-9658b26c4e08 | -1.20846 | -55.86089 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5221a45-41d9-38a7-a400-72ee2e0e5a7e | -1.20478 | -55.86042 | 2024-10-12 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a797035f-77c8-3532-9b0f-a9969eebcde4 | -2.07599 | -56.66167 | 2024-10-12 05:21:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87b1bdde-fbf8-39d5-97e5-f8d9cf4ae9f3 | -2.4132 | -57.15954 | 2024-10-12 05:21:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8c6750c-2b90-389e-9903-6970ebed0cc0 | -2.39429 | -57.64599 | 2024-10-12 05:21:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d102f93e-d8d7-33d6-abe3-22f82b3f87c6 | -1.45322 | -60.26083 | 2024-10-12 05:21:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| becf7f07-85c1-3250-acc3-aeb7b70ac84a | -1.43218 | -60.39476 | 2024-10-12 05:21:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 593b70da-2a92-3558-b66a-c4f2a3cee928 | 1.96664 | -60.91266 | 2024-10-12 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3757375f-051d-3479-87f9-71e50b257529 | 0.83448 | -60.57443 | 2024-10-12 05:21:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 663d7bc3-6d9a-3b98-9a34-05c45c1d5f28 | 0.83403 | -60.61597 | 2024-10-12 05:21:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eebc9cdb-782f-3517-938d-707c7038a6c5 | 0.83345 | -60.61229 | 2024-10-12 05:21:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd4bb47d-28cd-30e6-a8c2-79cdebf69337 | 0.83106 | -60.57496 | 2024-10-12 05:21:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03ce9576-0f20-342a-a4b7-89d564a6a8ed | 0.83061 | -60.61651 | 2024-10-12 05:21:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4a45b3d-6f95-30b1-975a-5149e3c2ac06 | -1.52233 | -61.58949 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb89c935-3425-3299-86ed-24857f79fc6e | -1.51885 | -61.58893 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2643e483-4387-3b7e-8b38-1c996e32fec4 | -1.51824 | -61.59278 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa4a51cd-f20c-340c-b153-8d0dbc68ed6f | -1.51537 | -61.58839 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d654b5df-e553-3958-8a42-ee0b80f3b6c2 | -1.51476 | -61.59222 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4534fbd0-fd4a-3cec-be8b-2ed9c91d14f8 | -1.49385 | -61.58895 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6267255-92af-3fc1-a055-901491fec2a6 | -1.49324 | -61.59276 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4957e87b-dcc3-3081-a51b-3387ecfaa290 | -1.48975 | -61.59221 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c19d04b-e145-34d6-b029-e60cf506cfe7 | -1.48914 | -61.59601 | 2024-10-12 05:21:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99a8e391-c904-3869-b8f3-5b21cf54bc3a | 3.34652 | -51.31591 | 2024-10-12 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6d0f5d2-47fe-3b80-a4d0-cd0c71b9cfde | 3.3091 | -51.34614 | 2024-10-12 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f561a288-53fa-363c-8aef-a10c2f6d7a02 | 3.30452 | -51.34687 | 2024-10-12 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 502ec251-664e-3b21-95e0-ee7520611d88 | 2.8255 | -51.11415 | 2024-10-12 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8acb6d0-e5b9-3ba5-8754-ef2c25c81cac | 2.82468 | -51.10919 | 2024-10-12 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98458a5e-17e9-394c-bbfc-6ead5b1a4d46 | 4.39165 | -60.67121 | 2024-10-12 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d967bee-f920-3c2b-9daf-3b3ab45926f3 | -8.5684 | -67.07459 | 2024-10-12 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92813781-a200-315e-bd49-3bc865f8bf57 | -8.39492 | -67.24324 | 2024-10-12 05:23:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba3248d9-3759-3b72-9e87-e6f88ce4ea08 | -8.39417 | -67.24757 | 2024-10-12 05:23:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ccfeef5-a46e-3c16-a7c4-7c79ff3dbd6d | -5.88065 | -46.37422 | 2024-10-12 05:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ca920de-5d1a-3c8c-a7c3-db9e056913d0 | -5.87345 | -46.37294 | 2024-10-12 05:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ec04f29-72a8-34a7-852c-ac2418e05d7f | -5.65735 | -46.4122 | 2024-10-12 05:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75be7fae-e6a0-3c38-b81b-cd5fc997b817 | -5.65635 | -46.41946 | 2024-10-12 05:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cebcee5c-da3f-3e8f-a985-d9ba57059528 | -5.11106 | -46.18559 | 2024-10-12 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0749c8c5-e4f4-3cfe-b654-b4fdecf17dca | -5.1038 | -46.18476 | 2024-10-12 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c72a0e9a-b653-3abc-bf63-2f5f31be202f | -5.06747 | -46.07495 | 2024-10-12 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 144ceaaa-265b-3bd3-9bc9-2bf84bfa8447 | -5.06004 | -46.07503 | 2024-10-12 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf713785-68c9-3912-b416-9a51a78a6b59 | -4.58714 | -47.09721 | 2024-10-12 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e2db7bcd-ab6d-3357-b817-be8c2825f2ca | -4.58023 | -47.09686 | 2024-10-12 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e50756c6-85cc-330c-a8ea-fc00b2052cc6 | -4.57935 | -47.10314 | 2024-10-12 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 89e48fa6-db1b-3829-9eb4-f59adbf54bd9 | -6.12518 | -47.87124 | 2024-10-12 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a558bbe-b392-3cba-9c24-e9b6ea04d89b | -6.12181 | -47.8711 | 2024-10-12 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07e62863-8805-3bae-ba8e-d926ca8f3037 | -6.11851 | -47.87049 | 2024-10-12 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26b0c2bc-df32-3277-b88e-830c51b5bd1f | -5.6517 | -47.92649 | 2024-10-12 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac3e3c93-d6dc-3c67-9f23-5ebbdb0c4eb9 | -5.64514 | -47.9254 | 2024-10-12 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d5b2de-2e42-3233-81a1-d53d745e807d | -6.51489 | -47.83011 | 2024-10-12 05:23:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaa81322-f6ff-3d5e-aa6d-741e2d71bea5 | -6.50822 | -47.82903 | 2024-10-12 05:23:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cb01f01-ba80-35b8-ba66-5eb3cff4fc2f | -10.47557 | -47.66559 | 2024-10-12 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d82b8a2-a41a-3535-aeb7-c622e170e0cb | -10.47292 | -47.66382 | 2024-10-12 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69dc7e54-7fd1-33d5-b222-eff22b23d7c6 | -6.42254 | -48.26577 | 2024-10-12 05:23:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6414a6a0-376b-39d6-9cf5-212b074cd401 | -6.4218 | -48.27129 | 2024-10-12 05:23:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d477d95-9677-36e5-bf1b-66c6b5860540 | -6.06919 | -49.13022 | 2024-10-12 05:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d103f16d-132b-320c-947e-3005ccf85dbf | -5.51056 | -48.0843 | 2024-10-12 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0fa702e-ae7c-3d7c-a84d-1ab8e2770ab8 | -5.50408 | -48.08321 | 2024-10-12 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7b89b76-c22d-30d2-8c02-9f3bd0654aea | -5.50335 | -48.08854 | 2024-10-12 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcf4f48f-0ad2-3dbd-bc65-51119480ef1a | -5.25287 | -48.03806 | 2024-10-12 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6455f002-bb0d-35e0-8cc1-13b765137af0 | -5.24732 | -48.03684 | 2024-10-12 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f16b6f5a-dbec-3066-a4ca-e143d88ce6ad | -5.24655 | -48.04221 | 2024-10-12 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 501d26dd-cec7-349a-b5bb-3da6dbf59d60 | -5.24637 | -48.03713 | 2024-10-12 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a2b74c5-24d8-381e-9b1b-b0f726180993 | -5.24564 | -48.04251 | 2024-10-12 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fdae05fd-01d0-3242-8ae3-d648b42fb8d7 | -5.24491 | -48.04791 | 2024-10-12 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2799cf3-b0cb-3189-98df-1b9964d339c3 | -7.07417 | -49.24832 | 2024-10-12 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1131798-993a-3f32-8d6e-4470f8e5b5e9 | -7.07352 | -49.24712 | 2024-10-12 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c67099d-da2c-3542-b317-68aa518e2600 | -7.0729 | -49.25195 | 2024-10-12 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7a2b7f1-1bcb-3d40-8f64-4b9125a4beb7 | -9.94072 | -50.06423 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9af1ee83-4166-3534-9f4e-0cd88b954c29 | -9.94009 | -50.06282 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3462651f-5dea-3e76-a8c3-57f1bb3557e8 | -9.9395 | -50.06743 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fbf3d1f-73f0-3ff6-8cc6-7f760557e734 | -9.8405 | -49.56764 | 2024-10-12 05:23:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35fadab9-9e47-39af-aa01-cd23310c1105 | -9.83423 | -49.5668 | 2024-10-12 05:23:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfaa65de-d73e-3e8b-9b0a-aa04629869a3 | -9.83362 | -49.57176 | 2024-10-12 05:23:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c24e8a52-8a72-3c26-a9f8-19773352023e | -10.55053 | -49.9505 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6bf7168-3cb3-35ce-9a5e-18580f41ef60 | -10.54434 | -49.94971 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0e48187-46b9-3a41-96c5-26546adda062 | -10.51391 | -49.78288 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c08d120-a630-3987-aaff-71e25144fa2d | -10.51332 | -49.7878 | 2024-10-12 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb1fb1a4-b309-3f19-89ac-dbf8f15e6f64 | -5.01059 | -49.75676 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0ac2b6d-be46-323d-b0e3-6655c5d390e5 | -5.00593 | -49.75405 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55421f3a-7eb1-36ff-8ee1-353e7fe23e52 | -5.00532 | -49.75819 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 299f509c-7445-3b4e-8de5-9dfc7450b5df | -5.00477 | -49.75598 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0dadae5-fa2e-39ea-954a-45d09c3fae3b | -4.99953 | -49.75725 | 2024-10-12 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README100.md)
