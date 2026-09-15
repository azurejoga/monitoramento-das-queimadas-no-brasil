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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86fc2e01-89bf-3e9d-a421-fc9d023852f5 | -9.35611 | -50.1317 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d31ab80b-aac3-3642-b578-d7316c18c30f | -6.88194 | -59.63737 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e27a00b2-9e41-3390-b8fe-0afb8b335d62 | -6.07601 | -57.8655 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f7d274b-e85c-3faf-97c9-034da5c3c02c | -9.25604 | -59.63855 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5702711-b5b7-31ce-beb7-13abc8dc0752 | -8.30825 | -50.88899 | 2026-09-15 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed864667-8f03-3257-8fc6-f5768b3d8a5e | -9.99003 | -50.27217 | 2026-09-15 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ca536d0-2f22-36e7-b862-0f7149969a22 | -6.11306 | -57.69237 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73fcb6e5-515a-35f8-a0b3-5bc26f99c22a | -9.6922 | -54.34015 | 2026-09-15 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eddf87e-abd7-301d-a519-4efae028e5c7 | -6.31125 | -59.95668 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce128a7-2a8d-3236-bbcc-5bd4b569cb36 | -6.16159 | -52.73816 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e89ce68-67e4-31d9-be8b-4143bdaf9ff2 | -9.35968 | -50.10398 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2c96c1b-2137-356b-9d11-2b36c3a33445 | -9.53953 | -62.37062 | 2026-09-15 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a9defa8-ad4e-3812-87ae-d7f5ad2fb247 | -5.44981 | -60.21852 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a675805f-8faa-3564-8320-66bde3825ffd | -10.80101 | -46.20457 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6b213a6f-f94f-3e0c-8d2c-3d670c6bfd2f | -9.59157 | -60.51397 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89c77d3b-2608-3228-b73f-6af986996746 | -6.37195 | -55.26176 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5045dfca-29be-31a2-876d-22ec7f26a938 | -6.22581 | -62.4433 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb79db75-f922-37c9-888e-e3f8f4410a25 | -9.35584 | -50.1331 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53bd2fd3-0e69-3d32-8606-9e9139cc0154 | -9.36031 | -50.18757 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cd6796f-b7ea-3903-b607-8dcce8ad5a8f | -7.87001 | -54.71966 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ec0676b-21ea-3a4a-8420-8a41ec29d010 | -10.58184 | -47.74621 | 2026-09-15 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef9559c8-80a7-3edd-a043-64eab4a72a52 | -5.92784 | -53.54638 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa7f925c-fd5c-3729-99a4-5279cf0acc07 | -10.30236 | -54.17233 | 2026-09-15 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 135571dd-164f-3527-a87c-3b829e174821 | -8.80385 | -50.49301 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 383f9794-6e49-3cb9-bab3-3e66daf9f0db | -6.06887 | -57.71125 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834c44d5-be1d-346a-b5e3-0d8c46f7ad51 | -8.95591 | -63.90246 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b047641e-be2b-320e-a4c2-d90abcf05174 | -8.29167 | -61.40599 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1be73715-8624-3a05-81bb-a9bfb18efbfa | -6.57302 | -58.95773 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b195ae08-cb42-3a03-a386-0f6e553f2353 | -6.13191 | -59.88548 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d91bfb3-ebe2-3add-8ffe-d925f27ae42d | -10.90129 | -51.54026 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2973e050-8133-39af-ac5a-999d3f70567a | -8.90201 | -62.33842 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 296b0a41-7b93-3396-a4d4-dca18886222f | -5.93144 | -53.55072 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb859069-921e-313f-9b8f-6b8b336b57bf | -10.80811 | -46.20588 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 26cfab52-3dec-3084-84df-94262f8a7445 | -7.55687 | -62.33073 | 2026-09-15 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dcfbbc9-e337-3620-aef1-7579f8bd3519 | -6.2824 | -59.92347 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 158e9b0d-c136-3464-952c-852773f6ecee | -9.10029 | -65.56028 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af95b40-4729-3aa3-b391-5c060f151f65 | -8.08843 | -50.97059 | 2026-09-15 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e642de5d-e1c6-38d0-ab49-fb51caf47060 | -6.15595 | -55.7018 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc9caaa3-6ea4-3a80-961e-dddf441e48b0 | -10.66431 | -54.14068 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6b5b66e-339d-30b5-ad18-b021bcae0cb9 | -10.80405 | -46.20858 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ab9aa847-56c7-35b0-800d-4a7a20b2ff39 | -10.6664 | -54.15756 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8433cd0-0a6f-3270-87f3-2640c84041d3 | -5.12485 | -55.93972 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4373e72-5ee4-3b17-8827-cd11550320b6 | -9.41073 | -62.71107 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| d22b8d3c-1c27-3691-985d-5a42c6d32e0f | -6.68523 | -58.69592 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9faf5eb-20e1-376d-b327-d0e4a3887c61 | -8.09173 | -61.79922 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4244d16f-2926-393d-b890-ebf0ce81ebd4 | -6.70125 | -58.70196 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5c117a9-e1dc-3722-bedb-079f0baf5198 | -9.54302 | -62.37118 | 2026-09-15 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43f85764-a516-3715-9eb7-058f284d5f52 | -10.67286 | -54.14184 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9defcd4-09f9-3100-8f89-3f5946313c4e | -6.15896 | -55.70661 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f870783-f063-3c46-af77-d565472b7748 | -5.12841 | -55.94032 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe8b7893-0c4d-33d1-8592-a86373e0624a | -9.35566 | -50.13531 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9396f04a-f25d-38a8-ba15-90f033bdc4f5 | -6.11417 | -57.68521 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4723767-842a-3045-af5e-469dfa7c9b05 | -6.03327 | -57.76423 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e005aa5-fad6-3949-b85f-a6cbeb3b7f76 | -6.68308 | -58.70979 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e492407f-822c-36a6-b73c-30364afa381d | -10.81117 | -46.20961 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9e7deead-b739-3ad3-b503-7da8ccd8d08e | -6.68908 | -58.69296 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9004b7b0-59de-3ee3-9a60-85e396f7accd | -10.86481 | -46.31484 | 2026-09-15 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1875d12b-f945-363a-a47b-3ac15892c1f4 | -5.13073 | -55.9491 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34122842-1a69-3adb-9bff-681da7bc8075 | -6.90983 | -57.62881 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cac5197-af45-398e-99ca-c0ed376422b3 | -10.25891 | -57.70155 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99b985fa-afb1-3452-87a0-111f7cd36f13 | -6.15632 | -59.94669 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99763ac5-97e1-3120-8dfd-76324771b1a8 | -5.80718 | -53.80393 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00529093-3af3-3640-a668-c84e43adf326 | -6.74109 | -59.4304 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76d643e6-0959-354b-a2c0-7729bbdf39eb | -6.35716 | -55.83246 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b3c20c4-b490-3ef3-bc13-fa48484612e6 | -6.01823 | -52.16941 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aa1291e-744c-31a4-8bd8-a875ffad0747 | -9.57624 | -55.14248 | 2026-09-15 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4c34140-85d9-36e7-ab2a-a17c4b084d17 | -6.11421 | -57.70722 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfa38547-7d49-36f7-8219-fa90d9552ad9 | -8.54303 | -54.71428 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0d1f370-337d-3886-9eb1-829e9a7a8f4e | -6.11077 | -57.66265 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 610e4497-a11c-3713-a1b5-83bab3153850 | -10.6744 | -54.16277 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c07666a1-9ae5-3784-80c6-79058148f422 | -6.13295 | -57.71053 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03b2e909-f24e-384b-a440-da4722a75b59 | -10.68457 | -54.15184 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ff3dc8-6378-337b-835d-e239cb371737 | -7.23494 | -46.17521 | 2026-09-15 05:18:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0996cb6d-62aa-3020-b1fd-7e5426bae6f2 | -6.268 | -59.92839 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 797349ff-20f9-34a9-9968-199772d404c9 | -9.64915 | -59.60478 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5f5e5b9-fd75-334b-955c-1116138cf160 | -6.01364 | -52.16889 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83974ab2-c734-3717-9ca9-2e7f5d763c1a | -9.03581 | -60.52139 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee7e9af7-12a2-348d-b158-b6bdcc21a76e | -6.67315 | -58.70824 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76d91d13-1902-37f1-848d-1e48a5f4e5c4 | -9.3543 | -50.14622 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 718f2376-61ac-3d1d-93bf-8da55a23c33c | -10.24187 | -50.91262 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 633cd899-d9ad-3e73-ba40-b3b740c7d3ea | -6.07267 | -57.86497 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b49879d-f1ce-3323-b40d-96e7b9738ff0 | -6.6299 | -58.37288 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1df22339-2a97-3654-82cd-9855a2360926 | -10.89312 | -51.56409 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81690e57-c261-3545-befa-c757b2ce99e9 | -6.84381 | -55.55497 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1a3fea0a-96b5-3448-9210-ad9bc93f82c9 | -11.33296 | -46.78216 | 2026-09-15 05:18:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 698c72f4-660c-3b34-a1bd-cea2a3d686ba | -9.4114 | -62.70699 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 42e768e1-af55-3e7b-b8d9-ea0f9ad6b084 | -7.87319 | -54.72546 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b589875-0bce-333e-a3e3-d06ae1dd3355 | -6.10633 | -57.69136 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84bd07ae-8f1d-3390-adbc-be5443c16fd0 | -9.35986 | -50.19118 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75434577-b62b-35e7-a07d-327e3f118252 | -9.36481 | -50.10691 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59afa5fe-bcec-3ef0-9949-691d851fcb57 | -9.25803 | -60.27729 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01d02013-ad2c-3b1d-a93b-c28defd09b95 | -6.69185 | -58.69695 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da4b4d09-65f0-305a-854c-dba8c7efa3fa | -5.44254 | -60.22104 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac9a20ba-e198-3e1f-a4bf-8ca31606486e | -9.45426 | -48.91139 | 2026-09-15 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4113a3ad-39bc-39e1-964b-f6311a4d00a8 | -6.07321 | -57.86143 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e12e430d-f467-3228-a385-e6eb17136832 | -6.11136 | -57.68113 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18c750f5-8548-3ae1-a68c-cacc69beff70 | -6.10578 | -57.69495 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 635054ba-f90f-3f33-bdd7-81ab8903a53e | -8.54177 | -64.00935 | 2026-09-15 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea45ab78-aa10-374e-ae9b-b4643dedf3da | -9.35964 | -50.18882 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4638d319-de1a-3a05-ad2a-38c076c6636c | -8.51103 | -50.14834 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README59.md)
