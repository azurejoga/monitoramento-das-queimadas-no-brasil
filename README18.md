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
| b48e3206-656c-3722-8f08-d3b10758d2cf | -7.71582 | -44.17322 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94af61a4-7dff-3dbf-b41e-081b2e4218c4 | -6.24251 | -48.54959 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdcbff12-2389-3732-bdce-c4570665ff0e | -10.24785 | -48.46339 | 2025-06-07 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83fe1d8f-3a39-3fcf-8f5c-da773bb9a019 | -9.07396 | -47.14654 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7d6f637-cd23-32a5-af62-412bb6dbe759 | -7.86662 | -47.90345 | 2025-06-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 77e5929a-edf9-3e37-a047-94f8cde6ff63 | -10.46554 | -47.95237 | 2025-06-07 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 10d1df7e-ec17-3008-b302-f34162683879 | -6.59602 | -43.89437 | 2025-06-07 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb516d10-2b69-34ed-9455-6f3f7030565a | -11.81505 | -44.26566 | 2025-06-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 16e65ba1-db60-31ab-a6ab-98b8a01a4b9d | -4.11992 | -54.91815 | 2025-06-07 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d15d877-58d3-3541-aef5-05a30f5b1598 | -6.23961 | -48.54523 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 740d1c23-4cdf-3bd6-a640-400cbf814853 | -7.86295 | -47.9029 | 2025-06-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1edcb808-c83c-314d-834b-dcc950bcd53d | -9.55306 | -47.77422 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 922786f2-966d-3da8-a5e7-5601aea20ec0 | -9.40037 | -48.43678 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35bcfab4-b0c4-37a2-b88d-632da9acef2e | -6.2025 | -43.33271 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcedafc7-7efa-307c-ab35-176cbb81c352 | -8.31634 | -47.91976 | 2025-06-07 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f78dc5c-6a5e-3dfa-a2f3-2e94938d1721 | -8.30549 | -55.10898 | 2025-06-07 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c508733-2b98-323b-b212-40e70a6a460c | -9.38003 | -48.39894 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45bf9e6f-fa92-30b2-a81f-e9c0253e5ed5 | -9.60933 | -49.01947 | 2025-06-07 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0086b092-1486-39dc-af5a-a48ce6359ba3 | -7.72046 | -44.17391 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e28297cd-8fbe-31e4-b830-5d33a76411cd | -8.20596 | -48.97943 | 2025-06-07 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f826e50b-3dc3-35d0-b00d-55b2d93aa43b | -9.00722 | -48.72151 | 2025-06-07 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5742bc5a-23a6-3c74-a318-d8ffc2c3d206 | -10.64596 | -44.48588 | 2025-06-07 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaee0bf0-a400-396d-b625-95ebb7de2a55 | -5.63999 | -43.71081 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c565713-2934-3076-b6c6-9795decd23e4 | -7.95409 | -49.64848 | 2025-06-07 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f486b471-e792-30c6-b6df-a1f79979e517 | -10.41334 | -54.00074 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a07ad8aa-d57d-3fe2-99f7-92f935fd2d1a | -7.21918 | -43.11417 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 23cefc4a-8d4b-3f87-b744-5f52badfff53 | -9.12496 | -46.8758 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a2fabfe-fe61-31b0-b588-9442de59d26b | -10.73542 | -47.61386 | 2025-06-07 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f6a8d14-c436-3043-8208-926b3dc7240c | -9.07976 | -47.13934 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| adbe9e50-b5a3-3672-a2f7-16ffc75226dc | -8.61371 | -51.5697 | 2025-06-07 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb61cb7-67e0-39de-ae10-676f6a0f392b | -8.87294 | -50.1865 | 2025-06-07 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4acb80f1-a2bf-3075-8344-00bbc1245dfb | -6.95628 | -42.91096 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| f7e35bee-b282-335f-9e98-1583088dab8c | -6.06474 | -44.23881 | 2025-06-07 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7e8472d-4aff-324e-bf0b-671909a0e390 | -8.07867 | -46.40026 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c7ff922-15e7-34a0-afdf-037e43f79171 | -10.49748 | -53.65609 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6999f20-f3c0-375f-8c18-93969e44150d | -7.01276 | -44.61197 | 2025-06-07 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c32eff2-98b0-36d6-81e1-dd818378a858 | -5.64534 | -43.70669 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39e26984-8519-3894-acfe-7cfa23e8b8e3 | -10.49348 | -53.65923 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0830eb9b-e398-30c2-a927-d0c551b63aea | -6.21153 | -44.50603 | 2025-06-07 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09802e33-1ee2-3244-8e89-e5f1ac8340e0 | -6.60478 | -54.99443 | 2025-06-07 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b295d9a0-467e-3548-8bc6-32b7687521ee | -6.59673 | -43.88943 | 2025-06-07 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e620d05-e217-3f74-ad5e-f57e3f0e3e66 | -9.40463 | -48.43312 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35d894b1-e001-3c84-ada6-328700b96156 | -11.81015 | -44.26498 | 2025-06-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12904a9a-5744-3832-811a-f161deb6d11c | -5.65163 | -43.59752 | 2025-06-07 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 674c16a9-720c-3684-9c3f-f96c2cc72903 | -10.50027 | -53.66035 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fc3a9ec-0d49-3088-8543-c9f2f3869e54 | -6.66244 | -47.73602 | 2025-06-07 04:44:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f4b832f-73b3-3be0-832c-b4ce4e4478ed | -9.01078 | -48.72202 | 2025-06-07 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae5c27ac-ba4d-3a30-b461-3cb388231c3f | -7.72648 | -44.16484 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c7d9adaf-ccca-3ba0-b130-8c2ea70b7151 | -9.1263 | -46.87412 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd9b6036-ee21-3a68-98bd-3ba6337e8506 | -9.3794 | -48.40322 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e45affa2-1275-3961-b869-e23ee2bdce91 | -5.78075 | -43.61327 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7353250e-d070-3c17-8cb1-1d2211d33134 | -9.84265 | -48.60814 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72840dc4-d0f3-3fd7-819a-897c04eab570 | -6.94749 | -42.90075 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3290b753-10c3-325c-8beb-be0bd3de6e21 | -9.62678 | -48.60403 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5f9bbf1-c029-323d-bd5e-3f292d49441b | -10.75605 | -48.5618 | 2025-06-07 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8dde6a1-78f0-391d-96d8-85f5d59ddc20 | -9.06081 | -47.90985 | 2025-06-07 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 026f1109-f45e-3b45-8036-bfd2bcb6a2ce | -6.45016 | -45.7203 | 2025-06-07 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf045646-42c9-3dc3-bd77-9b96febeefd3 | -10.49287 | -53.66293 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc1e0b2b-01ac-30d4-a103-d35dfcfc0dd6 | -8.16669 | -46.50835 | 2025-06-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 004fe8a2-2189-3f26-a78c-bdbe0e3e6595 | -8.17068 | -46.50895 | 2025-06-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33ebd018-ca4f-340b-bdcf-b5b145e065f9 | -7.73114 | -44.16544 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| de356188-a804-3d50-aa75-a3d03bb8e335 | -9.07784 | -47.14709 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cf61046-542c-3afc-a8f2-1d9ea24b2542 | -9.36632 | -57.4392 | 2025-06-07 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cf6e784-d0c8-35b3-8a35-5084797cc730 | -5.78472 | -43.61886 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f00cf8ea-d46d-3e89-9d76-6df8432cbe6f | -10.65666 | -49.36005 | 2025-06-07 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 107034b2-1664-3356-aadc-061f37fe6b67 | -7.90236 | -50.3661 | 2025-06-07 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 366aaf05-7b00-39b0-8375-5c852ad5e730 | -7.18987 | -46.23065 | 2025-06-07 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f1301b3-8f5c-3bbb-8bb6-b922ba82eb75 | -8.21294 | -48.98051 | 2025-06-07 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fde89239-3fb6-382e-a5cd-67aa4d7e57cc | -6.95251 | -42.90149 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b44777b3-41fc-3cc5-8eef-97a46fed8e0a | -9.07587 | -47.13878 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e18d7299-a8d3-3579-9503-c96ded6693f3 | -6.66308 | -47.73175 | 2025-06-07 04:44:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b229a55f-12ca-38a8-bbc1-d6aab888c8e8 | -5.65092 | -43.60246 | 2025-06-07 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8614123e-99ef-3f44-9509-7d07dd34fb9c | -8.59197 | -45.8705 | 2025-06-07 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b7afe4d-14c9-3018-908a-81f9a0b8530b | -9.07906 | -47.1443 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0b2a56bb-9c44-3f8b-abeb-ab8ec5c8b5bc | -9.50335 | -47.39381 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a53ccf1-787f-3983-b2b2-b75d84cdc9cd | -6.23902 | -48.54908 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58d718fb-9e70-3aaa-bdf4-dc4c5773667d | -6.95752 | -42.90226 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 29c9694a-01f4-3705-b2b7-3e2c5d892d8e | -7.73372 | -44.18077 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b05ce948-1584-3b17-97b3-6ba0b84cc76e | -8.45309 | -46.48674 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a129b87a-f914-3aa6-8948-1bd0a20110d8 | -8.44555 | -46.48212 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2dbf48d-2d78-35d6-a66a-73fbab3a14a8 | -9.54553 | -47.77309 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd6d3c5c-9299-3dd5-9c21-2145bf461535 | -6.21217 | -44.50172 | 2025-06-07 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cd27d3b-27de-384d-9261-89618202dee2 | -9.401 | -48.43256 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4208c42-9346-3382-a505-59aef082860d | -10.49687 | -53.65978 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cd63974-4314-35dc-8aa1-4de830d41d24 | -5.63858 | -43.72053 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fe1600b-9c12-3e1e-bbe3-dad29d13cc22 | -6.44962 | -45.72397 | 2025-06-07 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 912c2f52-ca4f-383f-8ca4-acfeb8374691 | -9.4995 | -47.39323 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7924a22e-7792-3aa3-a9d8-9e5261afa9d5 | -7.72183 | -44.16419 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 885fff62-0a07-379f-b325-54cdd4014c5a | -5.64857 | -43.71717 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13f8bd53-b90e-3a6e-8da3-65e784e81259 | -8.4566 | -46.49084 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 664df388-bfc6-31a3-b26a-06210c63466d | -6.24134 | -48.55723 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 61a1d0bd-7e47-30a1-a79d-afa4c8066423 | -6.94546 | -42.80544 | 2025-06-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0eee114d-67e5-3555-aa2b-e6eb3a8de41f | -8.94865 | -50.00859 | 2025-06-07 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdfe50c8-049e-3e8c-b5a7-c1ab3559bb88 | -7.72252 | -44.15926 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b829d450-8b88-3240-8403-32b6c1cb9d72 | -8.4571 | -46.48734 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45d208f6-3581-3532-b8be-7e0b85781cb2 | -5.77534 | -43.61749 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a2b0c95-3939-3b13-93ac-e94abdd455a2 | -8.44957 | -46.48269 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0108f8a-de64-3b12-9996-35be7638942e | -8.72218 | -47.90131 | 2025-06-07 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fc010fc-7c2d-3532-826b-0f5795d99392 | -5.784 | -43.62378 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa036c5-cce7-3eb5-a6a5-f1d36bcf4f77 | -9.55684 | -47.77472 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
