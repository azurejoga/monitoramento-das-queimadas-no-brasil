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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2e9d3d9-450e-391f-9b93-e34bc0d833e7 | -8.9583 | -48.90728 | 2024-10-08 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3420b200-3391-3d71-a825-8b6225e1515f | -8.75151 | -49.77935 | 2024-10-08 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee5719af-cf9e-34f4-89fa-237d16b8b196 | -8.75093 | -49.78296 | 2024-10-08 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fdc14cf-ba90-3bb9-a40e-192876a39053 | -8.60713 | -48.84714 | 2024-10-08 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d414b064-649a-3391-af35-d6a9b189a2dd | -8.60383 | -48.84662 | 2024-10-08 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a83b0d9f-c84c-3adb-8361-51c1f21cb9ec | -8.60328 | -48.8501 | 2024-10-08 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af7766fe-3835-38b9-950d-c58d977193ae | -8.60107 | -48.84261 | 2024-10-08 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5145715d-2b5d-39e8-ba9d-1d82db8becb9 | -8.60052 | -48.8461 | 2024-10-08 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b64a39-35dd-32ba-8f98-e91666a038ca | -8.43329 | -49.08369 | 2024-10-08 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0f2592c-b49f-37eb-9b77-1a81618a9663 | -8.16798 | -49.46489 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0109d2b2-91d6-3a00-878e-4236e927cd23 | -8.1674 | -49.46845 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 11c91cdd-0b22-3c6c-a44a-11e7e544041d | -8.16464 | -49.46434 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| faf5f06c-2d1b-3e30-acdb-86503c206620 | -8.16406 | -49.4679 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2eb9025b-a8f2-307f-9609-3d02d8668ecd | -8.16206 | -49.46352 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 88729ff3-f81b-3cc1-ac41-f70bd9737b23 | -8.16149 | -49.46709 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cb2d8e64-2c0e-3e64-b369-405a4e85f885 | -8.15871 | -49.46299 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bc5f9c27-cee0-3eb5-99d8-7911de148bc9 | -8.0741 | -49.6699 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ae755cd-bf7a-3962-a991-4490e3b8c9c1 | -10.52578 | -49.1114 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e4c2a9b-c9b8-3f4d-82cc-d8c82f2d951d | -10.52303 | -49.10738 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eef1638-28ae-3098-8f5d-6aaa7cc4edeb | -10.52248 | -49.11087 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 624a807e-9a43-3e23-b338-b6455f284a1e | -10.51973 | -49.10684 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad33649e-6074-3964-9dc2-7d23e0d0f823 | -10.51918 | -49.11033 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eed4ee4-afcd-3190-a139-48ec636c8ecf | -10.41161 | -49.42281 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24bfdea2-e725-3c87-aff4-dc7a957ee29b | -10.41105 | -49.42632 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc2a917-4a87-344e-8083-fc6ba7894650 | -10.41049 | -49.42982 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2ec8de-36ed-3150-b867-a2d16f2ebd0a | -10.40829 | -49.42226 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a549de73-a417-31d9-973d-b2c1c2777f0a | -10.40774 | -49.42578 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| caf53d0f-1da4-3704-bfaa-6162479fa4c7 | -9.94615 | -50.07351 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a4b106b-7c15-38b4-8324-f143de6051b3 | -9.87365 | -50.14739 | 2024-10-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67aa290-b09e-3617-9a52-c47d47287811 | -9.57254 | -50.23314 | 2024-10-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c075759d-af5c-39b7-9d9b-22867bc0ba4c | -9.56916 | -50.2326 | 2024-10-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc67973f-aad3-3d81-a744-9c03608a5e07 | -9.56856 | -50.23626 | 2024-10-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee58d03b-3b4c-34ac-b6c6-5c8d38b53fae | -11.91247 | -50.12749 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afe5a47c-dcc4-35c6-bb6d-f6a50e9bc5a3 | -11.70524 | -49.95476 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 700a4049-48d5-390d-9c04-510533fa05ab | -11.70467 | -49.95831 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7c26526-f674-3345-8080-ac4efe526db1 | -11.7041 | -49.96187 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 197722a8-7ec8-3b8e-b189-5be4756f38a0 | -11.52829 | -49.82695 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14e1c205-a3ed-3e6b-894b-a0f0ab009499 | -11.52497 | -49.82641 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d658b74e-7db7-37f6-88f2-ea9434122349 | -11.1866 | -49.64387 | 2024-10-08 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f5cd299-6ad1-3f2d-b634-c7695c581dc5 | -11.18603 | -49.6474 | 2024-10-08 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c6f9630-7bf7-303d-a21c-7ff16ea013e6 | -11.65182 | -50.47716 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7825bb5-93d2-339e-bbf4-0f2aa0bb8c1f | -12.2049 | -50.57579 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0128e48f-2e66-3e42-a566-dfbb155a799c | -12.18316 | -50.56096 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f085236-4187-3f90-835e-2cf717f3a806 | -12.17981 | -50.5604 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e32bb4dd-2d08-3968-95b5-640b41deb45e | -12.16638 | -50.55817 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b230920-e020-3478-befb-2ea7eb7606ac | -12.10784 | -50.89563 | 2024-10-08 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b5ad0dd-da94-3b64-b08b-21b0626304e0 | -12.10445 | -50.89506 | 2024-10-08 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ed50f4d-6dd8-359a-b02a-6e459fda8206 | -12.09 | -50.91937 | 2024-10-08 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68c904f4-ead2-300e-acf4-60d68cd3f46c | -12.81581 | -50.54334 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f3e6c63-8e79-3b0e-a2ba-7eb609247cbb | -5.85149 | -49.83278 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ef134fb-269b-3150-8ce5-765dde5f9361 | -5.84079 | -49.81184 | 2024-10-08 04:34:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c2b816e-9b65-395f-96f9-3234fb1fb5ba | -5.82609 | -49.96797 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41e727ae-56ff-36bc-9a69-062e98788160 | -5.58388 | -51.06085 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e9edbe7-45b9-3e1c-a94f-05b2f1f9f069 | -5.49536 | -51.07374 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c01b660-e728-314f-aa99-7117cd996341 | -5.49241 | -51.06884 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23a6825d-bb09-3b3f-b50b-527cb1846cab | -5.49172 | -51.07312 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75d550e1-0fc2-3fb0-9e4c-175e166c9fe7 | -5.46539 | -50.66577 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04c856e4-9d31-3abb-b420-3d448cbb3459 | -5.46284 | -50.6664 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b1af2bb-ffd5-3520-a65d-b2c3ca6ac328 | -5.46182 | -50.66518 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be30d70c-1de4-3033-b456-8afa0f1ce2fc | -6.4523 | -49.87737 | 2024-10-08 04:34:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cc60a63-bab9-307c-b372-159dfe7f3da8 | -6.44544 | -49.87635 | 2024-10-08 04:34:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1dee12fd-14c5-3270-b37e-b31f9416c9d3 | -6.44485 | -49.88006 | 2024-10-08 04:34:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d17a8bc9-0d09-31f8-b40b-13c52db4d267 | -6.43992 | -50.12642 | 2024-10-08 04:34:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5463587b-9c17-3988-a546-1358dacd9974 | -7.05732 | -51.23518 | 2024-10-08 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 370bc9c4-2391-332b-a869-d06f4c9466e1 | -10.61726 | -50.91653 | 2024-10-08 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f4c3b34-c30e-3443-8060-1d0de6defdde | -10.61383 | -50.91595 | 2024-10-08 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f9ad366-dbda-3fc7-95da-603c375a3708 | -11.40618 | -51.24912 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e5204a1-40d0-3a27-8f64-a7a2e1d94c8a | -11.35414 | -51.05265 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40ede990-a7e4-3a5e-b968-c3bbbd086083 | -11.33388 | -50.98319 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d38ff917-d45d-3226-ba89-be57e7fc8187 | -11.33202 | -51.08016 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36018fa4-f4b5-3c2f-8665-e185686ecb0e | -11.33046 | -50.98262 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d864328b-a377-3dad-92b1-16976217a4cd | -11.32858 | -51.07958 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc6e2fc6-226a-31b9-a04d-2ae01081e6df | -11.32704 | -50.98205 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e777198-8b79-3a29-8045-55e8e1b76b6c | -11.32515 | -51.07901 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfbd92e0-7e3c-304e-a691-18f1e4fcb69c | -11.32492 | -51.33944 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97524c89-ec1c-3198-9a88-c785228ea215 | -11.32453 | -51.08281 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 866a3b64-033f-37ea-a5a4-490fa9e452bc | -11.32429 | -51.34332 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd34084a-7887-3c6a-93a4-c10feb479667 | -11.32362 | -50.98148 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5b8f3d5-b049-3b2a-a748-d20b83cca310 | -11.32172 | -51.07843 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64cc24d-920d-3b5b-bbf1-f20f0565068e | -11.3211 | -51.08223 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c8a3e04-c3cf-331c-a63b-bea4aa50d181 | -11.32082 | -51.34274 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 399a82cc-8f84-3144-af4b-9d31cf2fa67c | -11.31767 | -51.08166 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9be16e77-f219-3672-a9b1-03bfe79ce861 | -11.31728 | -51.38611 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2893742c-d932-3aaa-b8f2-23d1bc304604 | -11.31423 | -51.08109 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e1a418a-651c-3110-88a9-939601cb7fd2 | -11.31114 | -51.05715 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dc0f8ac-5b2f-32a2-b235-358a5066f096 | -11.31084 | -51.03761 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5d8a382-4096-3445-9d0c-8d5d468511cf | -11.30994 | -50.97919 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50dbb9a4-9cb1-30f1-889f-97b09c3ccb83 | -11.30959 | -51.0452 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ea2ecf0-9723-3ca3-8013-320bdf7f6ece | -11.30896 | -51.04898 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d92d943-b773-3c7d-8329-c400dddfa289 | -11.30751 | -51.38046 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70b4e42a-8687-3d7d-a639-a51bd7e12140 | -11.30708 | -51.06036 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 50677494-77ee-3233-bfe0-1dfb1737715e | -11.30679 | -51.04083 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3f0a612-6e69-3a23-b3e5-83e7e5e1e1ed | -11.30645 | -51.06416 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| abffacbc-229c-395e-ae58-e48d40b9039c | -11.30616 | -51.04462 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76c395a9-6096-301e-849b-025a135dad54 | -11.3059 | -50.9824 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cb75ea6-371d-34c8-8a1e-9a3374478130 | -11.30583 | -51.06796 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 323c1c18-11db-39fd-8ff3-1bcecaec08fb | -11.30527 | -50.98618 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 097e8f51-1381-3aab-ab8e-ff1de6e8d1d9 | -11.3052 | -51.07176 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 47822d12-5db5-313b-808c-b8ae49951c3a | -11.30457 | -51.07556 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48d238aa-3d03-3fc4-81b0-06cb90b41e60 | -11.3043 | -51.39997 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
