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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5815d847-6cbb-3912-aff5-b9c5593c9b15 | -4.0622 | -51.10056 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2de3b82-527c-3fae-bdd6-2a91904dfb2c | -8.00842 | -42.92055 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2203881a-cc59-3b17-92d9-8510a4931f73 | -2.91998 | -46.72337 | 2026-10-02 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9db97d2a-26f5-36d3-bfb7-9e0416384f70 | -5.23509 | -49.58479 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b44cee0-20ad-3acb-95b9-7dcc976d697d | -9.83162 | -44.84931 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e04ab9bc-7308-3309-8b67-22ea74a4b88c | -5.76333 | -45.14157 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 95ec2d8d-6faf-3ffb-b8c3-44c3caeca3af | -3.16748 | -54.08168 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fd47273-540a-3e85-8ea3-da884ddb03af | -3.29011 | -53.8556 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 140fba5a-297e-3fea-b01a-1463c19961a8 | -7.82713 | -55.12392 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79fa5368-f875-3ce6-9002-0f1c3fd31c42 | -7.8687 | -44.17589 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e4803d4-eb48-3713-b1ce-766a69dd03db | -5.73371 | -43.28416 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2176b979-ed1a-332f-97cd-4be21d1c92d4 | -5.75525 | -45.14462 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d1a868e-68ce-3976-9b9e-0c2edc4d26ea | -7.46517 | -54.99104 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06422700-8ce3-3b9d-90d8-fa5e698ec29a | -8.61928 | -49.46901 | 2026-10-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8c597a2-a5a6-3b35-9472-79b661bb9cd1 | -7.52163 | -47.33926 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 430d20c4-ca68-31fe-a65c-53b9601b11fa | -4.30187 | -50.78559 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08390f0e-78e0-36b0-9358-147154a5bd12 | -3.16641 | -54.08783 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eba68162-6128-34f8-927c-43dde9567fd3 | -7.39541 | -55.21384 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| c3b44b08-1483-38cb-9b46-3bb92bdd6673 | -7.3944 | -55.2206 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| d020669f-3da3-3ff4-9ce6-45dc511dcff8 | -9.78755 | -44.80257 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2aea5036-0729-332a-90fd-973944c722ce | -4.27874 | -50.75623 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b90e6f-b797-37ff-a4e3-b5b7f19e0b7b | -9.77651 | -44.80473 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a515438b-7ef0-347f-a13e-2dae3ada2d80 | -6.20416 | -53.26487 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e0692a-352c-3faa-9fd2-8bc8139e3e2b | -7.02864 | -44.50074 | 2026-10-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dc7a17d-e099-33a4-a30a-5133288f4c7c | -6.14086 | -43.16922 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50ed015a-7b1b-394f-8cae-8628185124f9 | -2.89299 | -54.15123 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94303856-a587-3814-bce5-afab6a50c1bc | -4.27387 | -50.75177 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbf87770-5151-39e8-90f0-0f6892e82e89 | -9.84681 | -44.84383 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41d37e12-e69f-374a-b831-4ad778334541 | -4.29213 | -50.77666 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e3bd85-11b3-36f9-ab39-135be8f00392 | -6.23665 | -53.15653 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 373db310-88ef-3076-b01e-ab36fa139d3f | -5.14106 | -49.86873 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8aa03e8-ce51-374b-8bb7-bba519241832 | -4.25266 | -50.7443 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32f01d96-9977-301d-bff3-342239e1b102 | -7.65885 | -55.10535 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 315f25df-2b8f-3213-a64b-5775afa15778 | -3.06714 | -49.3652 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9c8f049-7007-3989-87d2-da5a1b6df8a6 | -4.29029 | -50.7874 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa912004-f8af-3f0f-b08d-93cc1ec4e6d5 | -5.75749 | -45.15397 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4fa4171-b6d7-3221-80f4-3422822cdb6f | -7.46254 | -46.84463 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78dbade8-8b90-3db6-8ab4-be8ba7eb6893 | -6.33405 | -43.36425 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0b52360-35e6-3fc3-b9e4-1b48652395ec | -5.56048 | -43.96719 | 2026-10-02 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c8486b4-2d6a-3a84-8aea-f08b09b83ffd | -8.7309 | -36.85332 | 2026-10-02 04:14:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29ade0ec-410f-3ee0-ae99-c2ede517701c | -7.4624 | -55.01493 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a43ee16b-7685-3b31-8c1e-617a3c6a52c6 | -5.76118 | -45.1546 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d97ad017-d5d4-3c7d-bf01-909270ecd4dd | -8.91573 | -49.25885 | 2026-10-02 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8860b796-a64d-3528-917f-5e5c8f3f2958 | -5.74789 | -43.28273 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f8c19e2-0411-35cf-8eb6-987bd4b4a1ce | -7.74588 | -49.20825 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e69dcb12-1be6-35cb-b715-00ba52f5a688 | -8.01434 | -47.43351 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30fe71d5-9f93-3be4-b3a3-16473f3f41ce | -5.75227 | -45.13969 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d1adf078-aff8-347c-beae-8b2959bf17db | -6.08982 | -47.67545 | 2026-10-02 04:14:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ece33329-cc9a-3734-8863-040d44a864b9 | -9.8027 | -44.80863 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3b791c2-a21a-3fda-b83b-44af4fa602d7 | -4.29892 | -48.0689 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f487ddd6-1558-3d7d-b3f0-844b0358bd8a | -8.56016 | -44.13212 | 2026-10-02 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 910657ea-bfe3-31e3-8acd-e26305ff993b | -7.52689 | -50.53599 | 2026-10-02 04:14:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df7623a7-50b7-3d06-a6d0-85d153708292 | -3.29584 | -53.86281 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dad462c7-2666-3cb5-95ff-4de9e238efad | -4.29273 | -50.77311 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d812f9f1-29f3-3c2f-a99d-ea850c3d2af7 | -8.18048 | -54.79957 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d993c1e-66c2-3786-9505-40ab66386902 | -7.21072 | -46.54878 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a1f2e8e-6d18-339f-a349-40c001735f68 | -6.23824 | -53.14781 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c310c53c-4ed7-3eb5-97f5-bd84d7efd4ce | -8.20969 | -55.09634 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e2ccc66-6251-3f2f-a056-6860a53561e3 | -6.40392 | -46.20324 | 2026-10-02 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2046174-a4c1-33da-9077-4effd969e7ab | -6.24062 | -43.77151 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 528b3fd5-2df9-3284-a543-50106a802f20 | -7.56658 | -55.13956 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3bd8ab5-a0b8-3cf4-a624-3878057e2948 | -6.89601 | -43.68712 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 793d5fef-d96d-38bd-b8e0-cc7de7bc8b73 | -8.78008 | -45.82035 | 2026-10-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e7a5b86-a241-351f-8ebb-9280bd5224d6 | -8.00898 | -42.91703 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dec0e2bf-dfa8-355b-8179-03b767a30f81 | -8.02516 | -47.46947 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37f4f39a-2277-37ac-a22f-090c74eb7df4 | -9.83317 | -44.8615 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab59c66b-f190-343e-96b5-7cd9e66a006a | -6.54419 | -44.02193 | 2026-10-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0550a7c7-c52b-3a1f-830b-367e37c2e1cc | -4.4972 | -42.54793 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 175f2589-6e22-3e0a-9f0c-284861aad4b7 | -6.15028 | -47.47469 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f587959-0496-3040-879d-b8d1250f080b | -3.99756 | -48.40275 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ddc94c-ac46-3fe2-91f2-5fb39edb7ec7 | -3.29894 | -53.85912 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ca6788-5b56-3c76-a5fe-d4d6e64412d5 | -6.90805 | -43.67766 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fc06b06-83d3-39b4-a8a3-9f62eb594cbd | -4.26176 | -50.75673 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86991ca9-00a7-36f0-b6be-b9eb4a9a780b | -9.82184 | -44.84368 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 074730c9-82f7-3c98-b300-b5bedb4a1bcd | -4.27636 | -50.77 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4875eb3f-7556-3108-9c4b-47ced45eb675 | -6.24811 | -43.76888 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 636a6e99-237b-36c4-9808-5bbfe89ce89f | -5.00376 | -47.45171 | 2026-10-02 04:14:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 019812dc-2162-3eb3-a0d9-522544d68d27 | -6.21032 | -53.26635 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5947a6a5-a8ec-358f-b9d9-cae88ce5c2b3 | -7.1886 | -52.61244 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6eb070ad-3852-38be-8659-70556e1cc126 | -4.26661 | -50.76123 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6f15e98-4029-3fc6-bae2-33e5cd20c3bb | -4.33459 | -39.36516 | 2026-10-02 04:14:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d83e58eb-2672-3c51-9732-d4612f0e4944 | -7.27897 | -55.60118 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e5e98da-700d-3527-8a31-5d779ab9dc73 | -6.89422 | -43.69823 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 414915a1-ba60-37c7-8dff-816b14bf1427 | -8.07972 | -54.89381 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55a9a10b-96b5-33d5-9c4b-e8410fb82d26 | -3.01498 | -53.89503 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5dd15bf-9f5e-3d2d-b9e3-9be1d95fd3d7 | -6.98459 | -42.86017 | 2026-10-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f8b5c4e9-f819-3020-b679-3778e666c954 | -3.17429 | -54.08303 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 047f6899-fc32-3f34-ad1c-e4556ac011c9 | -4.29699 | -50.78117 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 933a896e-07e7-359e-a9a9-ed18c8969904 | -4.2703 | -50.77251 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6e5ab24-484a-3623-9be8-1b3e7bdb1469 | -5.85581 | -53.48384 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e3b5c37e-a8ef-3b02-98b2-dff169161f97 | -7.25149 | -48.06512 | 2026-10-02 04:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf52e73a-63b7-3906-bf89-279641c2eedc | -4.28605 | -50.77925 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d868b3d-f429-3d9e-82a7-ecf6ce506328 | -9.83445 | -44.85377 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccd4ff8c-4683-3034-85ec-6c6fb0a940b0 | -5.90101 | -53.501 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3bfcd6c-4347-38d0-b7b8-350eb27eee60 | -5.67605 | -50.096 | 2026-10-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f83a7e7b-bae1-37a7-b264-b3363e7caf27 | -6.40359 | -46.202 | 2026-10-02 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ef6e830-5192-3dea-8f6c-ccb2918d681b | -2.90127 | -54.14604 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1801fac-3cd3-3d68-a5b5-f723f119ca6c | -7.74318 | -54.81121 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a67872a0-2019-3d3a-8577-28a116c063b5 | -5.23013 | -49.58383 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dfea68b-7bd5-3d6c-bdc3-4167455dbb70 | -4.25988 | -50.76758 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README39.md)
