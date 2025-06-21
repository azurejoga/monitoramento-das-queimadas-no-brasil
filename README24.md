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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1280019-45da-303a-a5aa-cf8840b2bbe7 | -21.69359 | -49.50497 | 2025-06-21 05:04:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 314d9bfe-9edb-3c29-8e51-a198f3fa34b2 | -21.69852 | -49.50549 | 2025-06-21 05:04:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1cbbad8-d651-3b8b-9571-58c5f002f214 | -21.69788 | -49.51133 | 2025-06-21 05:04:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ec1f5b72-c863-3fa5-b399-b624da892cd5 | -19.37491 | -51.41045 | 2025-06-21 05:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1fa2c6f-f93a-318f-8b90-5e32827d6b2b | -21.01233 | -52.82545 | 2025-06-21 05:04:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 850825c0-e346-3037-96e4-2b0f5b2af6cd | -21.44071 | -54.57825 | 2025-06-21 05:04:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d47588f4-cc81-3601-b073-3d0dfe6ca05c | -21.69296 | -49.51075 | 2025-06-21 05:04:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ebf616a8-58ca-3499-b999-1422236b6abf | -11.8663 | -54.6739 | 2025-06-21 05:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e8796d9e-bc8e-31d5-a7e7-6dadc860e66c | -11.8853 | -54.6722 | 2025-06-21 05:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6af853b9-0234-3701-a66c-c84b1234f7ee | -11.7791 | -57.2445 | 2025-06-21 05:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| db207f3c-21c6-33ef-b3bf-6ebf11b981ef | -11.798 | -57.243 | 2025-06-21 05:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 56d19db7-b4cd-372b-9870-ec940d8a9c02 | -4.5243 | -48.016 | 2025-06-21 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e769fa75-9c37-37a0-add9-57923dc8f63c | -4.5429 | -48.0151 | 2025-06-21 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 176.6 |
| a81508f2-8c92-33cb-a818-484d0660ae15 | -11.8853 | -54.6722 | 2025-06-21 05:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9c69f7a7-c759-3479-bff0-720a7c67ea63 | -11.798 | -57.243 | 2025-06-21 05:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 27cedea2-6d0e-383f-b0f5-10bb3520be98 | -4.543 | -47.9934 | 2025-06-21 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c7f0a3b9-77d6-31d0-8621-0e917908d20e | -11.8663 | -54.6739 | 2025-06-21 05:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4a3dde09-3834-3aee-abf7-f58161984134 | -11.7791 | -57.2445 | 2025-06-21 05:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f6b3fcb4-91c5-3106-9459-1be82148f9bd | -3.62677 | -47.51661 | 2025-06-21 05:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab647daf-3d2e-3c8a-b583-ea7c632eac0e | -3.96338 | -48.12829 | 2025-06-21 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 467ee822-c32b-3e23-9af8-ac48071c2424 | -3.62521 | -47.52742 | 2025-06-21 05:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0e6cda2e-c996-38e0-b300-97c26f263025 | -3.96899 | -48.13457 | 2025-06-21 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0453eb3c-d76a-338c-bcd5-957ca0deb51d | -3.03908 | -49.4403 | 2025-06-21 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fd0cab4-d897-347c-812a-36a6b4e20c21 | -3.03968 | -49.43628 | 2025-06-21 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5dea5eea-2c76-31c2-8d68-1799488b71a7 | -3.96971 | -48.1295 | 2025-06-21 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 02db26ff-ce73-309f-b647-d6483737e910 | -3.04488 | -49.44112 | 2025-06-21 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49bcc3a4-4c45-3933-9026-d9988dbd94eb | -4.54267 | -47.97311 | 2025-06-21 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 00d217e4-0ec8-338c-a9cb-ba10ff06178c | -3.31443 | -48.71856 | 2025-06-21 05:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cc38a91-6600-3a20-bb95-8c7a75eea263 | -4.54191 | -47.97842 | 2025-06-21 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9b8d7588-efff-33c3-86a2-ae0b645c11fc | -3.0443 | -49.44505 | 2025-06-21 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 330dc1da-5ff3-39bb-852f-a06e773c74d0 | -3.62597 | -47.52213 | 2025-06-21 05:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 180322fd-a300-352a-aac0-1f42c89edf2c | -3.96264 | -48.13341 | 2025-06-21 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3766abbd-6c74-3875-ab26-97f4bd01b52a | -8.02298 | -47.66518 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d88d07f3-49a8-3dc6-87ad-a8c4fccd6a01 | -9.01775 | -61.23302 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84e07d9f-4956-3b0a-bde8-b75eb28c016c | -8.97934 | -49.86759 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c154aa4-f7a2-3b6a-bb40-167d3caba244 | -9.46452 | -57.84161 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5fb931-1a69-31e5-8143-c07f55645a6f | -12.16494 | -48.68874 | 2025-06-21 05:23:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60fe6dc9-2eff-3d4e-8acf-c01c07a8d13d | -9.36827 | -62.04193 | 2025-06-21 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 186761d2-bf30-3b6a-8a62-c43af9d63f2c | -9.45785 | -57.83619 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c572987-c0a3-3f29-92f7-dc7d8af7b023 | -9.25188 | -57.5323 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a52d1118-6ab8-33cf-b91a-33e512544732 | -9.02325 | -61.21965 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a92f8ce-8d60-3cbf-ab38-cd352f431954 | -10.86276 | -53.76253 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6229a95-ca62-382d-9c6e-f5dddadf4b82 | -10.67865 | -56.55315 | 2025-06-21 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a41ae9e-4788-3029-a291-f9a3a8ab623c | -10.88585 | -56.46043 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d16ec5d-9882-3d54-86b0-37727b722ee8 | -8.01608 | -47.66417 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02204ad8-2495-3f3b-8424-4c37d060873e | -10.93677 | -55.33346 | 2025-06-21 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9809fac5-7537-313f-a89f-9363838324bf | -9.26911 | -57.82428 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a8bad6-d4de-397f-8065-db85b50fb0d2 | -10.52682 | -53.62229 | 2025-06-21 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fce73e7-b50f-3083-9f31-60a6b08ae95e | -10.85859 | -53.75657 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4280d908-4e90-35b1-ba23-e443488753ba | -9.25252 | -57.52785 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 33787425-49f1-36c8-84b1-92f7440aeef5 | -9.09491 | -50.03117 | 2025-06-21 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 862e26f3-5e6a-3170-a321-1500c43af99d | -10.67709 | -56.55305 | 2025-06-21 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df0f937b-dd7f-3d43-a109-b1d9596a5e7c | -14.86294 | -59.799 | 2025-06-21 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e66c282-d2da-3de9-99d9-73800c2372aa | -11.06772 | -49.62253 | 2025-06-21 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edac4383-2034-33d9-88d4-1b3e5ad5b4d2 | -9.01389 | -61.23597 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a146cf48-12da-35be-b65d-2d81fa42bddf | -10.86832 | -53.75775 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c78561a5-1037-3b2b-8ce2-b83037de21c0 | -10.8899 | -56.461 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d798c213-ee4f-344d-a74c-a63199ef2ee3 | -14.86338 | -59.79823 | 2025-06-21 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 297c84e2-2740-305f-9859-72fb16eedd80 | -11.14008 | -53.915 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4645c147-4fb1-3f79-a49c-3134dd51ff06 | -8.73513 | -47.98139 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f29ac15-3363-39d9-906b-854534348ded | -11.07923 | -55.05035 | 2025-06-21 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90fd8685-3b8f-3d49-8823-05f6512deac4 | -8.12269 | -61.41365 | 2025-06-21 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2b5e78d-08a4-3cfe-a9e5-65126adf5e59 | -9.25316 | -57.5234 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8c462c7c-db7f-3eb5-b0d1-6f3fdaac537d | -9.48286 | -56.08003 | 2025-06-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2639ee1-acc9-3235-9bb8-8196ce104ca7 | -9.46515 | -57.83732 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 117b6ecc-ab09-3914-b65a-ea9c8a54c507 | -9.48693 | -56.08061 | 2025-06-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4192fc38-d42c-3a52-bc18-26f4637d8a32 | -9.48337 | -56.07643 | 2025-06-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf491fb6-d59d-395c-8e00-b00114f5bdec | -8.73439 | -47.98738 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0bfed34-170c-3d74-9571-7de463958208 | -9.46579 | -57.83301 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 968dd97f-bb03-3112-aa7c-0cc1bbf0856d | -9.01444 | -61.23249 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f8419dc-8a7e-3c7a-9553-1c072e3d2493 | -8.01635 | -47.66404 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd204371-5ecf-3b53-a42d-7dd3be8cd889 | -10.02858 | -54.32606 | 2025-06-21 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 386b7714-3c1b-3864-936e-217ae17928da | -9.4712 | -57.84695 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f262dab5-6427-349f-bb07-a0ef79b8d5ae | -10.02474 | -54.32283 | 2025-06-21 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f6b8967b-9f07-3cf4-88b6-59d857644912 | -9.47246 | -57.83838 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d41ed134-9deb-3e87-9619-c3e9acc7a1a6 | -9.57113 | -62.46787 | 2025-06-21 05:23:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 061c874f-e8c6-3d0c-b6dd-50d2d6f392d3 | -9.44947 | -62.32042 | 2025-06-21 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dee8fd9-0fa8-3a0a-a742-e9f24771e88d | -14.81532 | -48.47236 | 2025-06-21 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f2b7cca-a298-3061-8050-5e6c74118af3 | -10.30154 | -57.13426 | 2025-06-21 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69740efd-1b2e-35b3-8c21-1bae7fc96a03 | -11.08307 | -55.0554 | 2025-06-21 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 935029ba-f623-3a1c-8110-3cd15b75ef73 | -9.09706 | -50.02545 | 2025-06-21 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e20b75d6-91a8-3466-bac0-2670fb3278eb | -8.02376 | -47.65889 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 083cdad7-0cf2-36f9-a6e4-33490c5a0b57 | -9.09649 | -50.03002 | 2025-06-21 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a29a0331-6c07-30a1-ab70-af36160068c4 | -9.39551 | -63.2641 | 2025-06-21 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb32740f-bdca-31f0-aff7-cb57fcafc149 | -8.98588 | -49.86559 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38c07636-a366-31a9-a42e-8f576e8d6b29 | -8.00945 | -47.66308 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef3de89e-364b-3326-b0de-570fb2885ca6 | -10.13403 | -58.21768 | 2025-06-21 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab2ef309-6b64-374c-9daf-6eeb4133760c | -9.01499 | -61.22902 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28557553-cca2-376f-9780-c30f065f48bc | -10.86207 | -53.76786 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d9493e7-78fb-306e-9a29-9e808a0c82fb | -12.16563 | -48.68255 | 2025-06-21 05:23:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb6c2fbc-5e3d-3b2a-a26f-f8f2e119555f | -10.29701 | -57.13855 | 2025-06-21 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acf8b81f-1c30-3e94-a904-76abc3edaa7f | -10.02936 | -54.32343 | 2025-06-21 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3f934232-a152-32e8-91c3-0687670ecf01 | -9.49454 | -56.08539 | 2025-06-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ff62fd0-7c2c-31fc-8a9f-a38e55a828b9 | -8.00839 | -47.66956 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b780177-8e5e-3d85-88fb-f574871713d1 | -11.13939 | -53.92039 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79f19b6f-fb42-3529-bc4f-58dc045593ab | -14.80831 | -48.47045 | 2025-06-21 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c69bcb85-0794-3efc-983c-606470fb616c | -6.53004 | -55.02058 | 2025-06-21 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2270248-5765-3880-a18e-628821b59b48 | -9.1707 | -61.40314 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 05bdca0f-1710-3517-a958-8dce8aa7c760 | -7.1602 | -55.45669 | 2025-06-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b0a0d0a-11db-32c0-95b5-b784e46d60d3 | -10.86345 | -53.75717 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
