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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1730cdfe-dfb3-3712-924c-4834fd08ca68 | -4.66882 | -55.63125 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 704286c1-6952-35e6-a812-7937ea42919f | -3.55382 | -48.18099 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef46133e-e734-39fb-8468-a0287e02e93a | -4.47435 | -55.08792 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fef9a89-e2a0-3ec2-9bc7-0c6c130ccb91 | -2.8613 | -50.45811 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3df94276-3335-31a4-b6da-1860f37cd28b | -4.3478 | -48.97454 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 397580ef-bfd2-3680-b562-ef637651d495 | -5.4402 | -42.22948 | 2026-09-07 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 544273b8-38ba-349f-80d2-298b8772951a | -3.64048 | -49.70609 | 2026-09-07 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e386cc2b-e54c-37ce-8b7b-fc8e9f579a7e | -5.16764 | -55.96468 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aca53eab-33b0-38cb-a721-d1e788d3d422 | -2.96526 | -48.70689 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 676b623d-636a-35fe-a954-a8d944a07eff | -2.87052 | -50.45164 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f0443ee-119b-32ff-994c-f477b83ee5be | -4.66946 | -55.62751 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d26e3f5-e982-3a8a-885a-68a7646f08de | -1.49351 | -54.82679 | 2026-09-07 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a797338-f474-34c1-b9f2-36117737a14a | -2.55983 | -54.74712 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e24788b-d584-3adf-92d0-c0be6e563557 | -2.96166 | -48.70634 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ca8e8847-7ac8-301b-9727-db7af19ed4a1 | -2.88175 | -50.45778 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dda241ca-6551-3d3d-aad9-3583dc55f80e | -4.07949 | -48.95604 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d21e7c6e-2dcb-3a9a-97de-21a22127f81b | -4.38321 | -44.39054 | 2026-09-07 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 588284f2-ddf1-3e04-95d8-e5d8d720365b | -2.8793 | -50.44778 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6a6bf2c-6f30-3b7d-a55b-bcba813071fb | -4.03154 | -52.07612 | 2026-09-07 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bddb68fa-447e-3dae-861a-6cc2e46bc8c8 | -4.04129 | -50.87695 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9fd5ce4b-f28d-34ba-99b8-8b424ca4f443 | -5.14345 | -55.97224 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f179455-b49e-38ee-b71f-99de55fc8212 | -5.15652 | -55.96285 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8805fcf-a12c-3c39-b4a8-ae5a3c48dfd2 | -5.1503 | -55.96573 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c9d6c59-a5b1-30b2-b98e-12d875b3841f | -4.12412 | -54.41388 | 2026-09-07 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d369549b-66bc-3d38-b0a1-8a663483a6e3 | -5.92014 | -42.98632 | 2026-09-07 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef0bfc7c-56c4-3ac1-a97b-d37e55377ca9 | -4.59529 | -50.98574 | 2026-09-07 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03a577ce-9947-33ed-8d3c-24e199907d7e | -5.82917 | -49.18988 | 2026-09-07 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e8b974e-4752-3931-9177-d4187ad25867 | -2.9121 | -54.12017 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fb19068-2753-328c-aeac-733bdaa93f5b | -2.94332 | -50.3022 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44a04e20-f31c-3b9f-a77c-337786b3dd3e | -2.9177 | -54.11802 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b01733b-8300-3ccd-9a6e-1d7ddd7349fc | -2.86982 | -50.45591 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf41443-61f2-3e44-b73d-bf0de55d6c14 | -4.47544 | -55.08917 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6817404f-bda3-376f-b329-82d61fe9baf8 | -6.7819 | -41.17235 | 2026-09-07 04:25:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b9f92f7-3a3c-32bf-8ce8-9de9b94fc7e9 | -2.87777 | -50.45716 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd463cf-3747-3370-9f65-68597b1aa69e | -2.63558 | -46.77302 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 48954dae-9f41-33dc-b3d3-5623df751abb | -5.60994 | -44.36994 | 2026-09-07 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cb061dc-a8a4-31ab-b9c5-c39a3cde2e37 | -2.87699 | -50.43693 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 44af8c3d-7cdd-384f-8c1e-4eb64a166ef6 | -4.98204 | -50.63247 | 2026-09-07 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab26b4d7-2981-3906-a0a6-efb5cf87ab11 | -3.48264 | -39.09808 | 2026-09-07 04:25:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3328d808-b563-35e3-a6b2-63251b0830f5 | -6.56391 | -44.78031 | 2026-09-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09050513-5194-36db-b926-f28c08603db5 | -4.6798 | -55.633 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a2345a-b6dd-32a9-92d9-1c8de62c05e2 | -5.14473 | -55.96485 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 110ea20a-93db-3102-a0aa-94f0ff19dcca | -5.28652 | -50.25965 | 2026-09-07 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81f0329c-087d-3921-84c8-b57de5ba3557 | -2.9126 | -54.1172 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 487c4954-607d-3b21-9dea-b6544f6e4951 | -3.96464 | -55.40277 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1cb7082-84c8-3153-b8f6-c675d24693a1 | -4.11222 | -49.08696 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0422ac11-a7d7-3d35-870e-8845ad91e959 | -4.98514 | -50.63804 | 2026-09-07 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afa856ed-4945-3f75-8de7-25af0e647c8a | -0.47248 | -51.83218 | 2026-09-07 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15781c44-e31c-3d5d-b7a9-7cdaa434b52c | -3.53316 | -49.37821 | 2026-09-07 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20625b94-f803-3912-8e42-e6763e2f20e8 | -2.87616 | -50.44203 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c98d8781-9745-3677-aec0-3127a0ff2e4c | -5.14665 | -55.95373 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 236c4eae-9e80-3607-bbfc-059d7733b467 | -4.07821 | -48.95472 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9b6047b4-f41f-3f65-834c-9d28679b4156 | -6.5673 | -44.78083 | 2026-09-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3378b2b-9137-34be-8f96-60c93f85d16b | -4.35072 | -48.97921 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a63a8802-cc68-30fa-adac-638ede1d3b2e | -2.95873 | -48.70168 | 2026-09-07 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f1c5695-bbf1-369f-bdb7-17a362b04b98 | -5.16147 | -55.96731 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8836144a-93e4-3d72-b46b-b9abfb2e4c89 | -3.23366 | -50.57439 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9061fc4-9c97-3c64-a2f5-083190b0e19e | -2.86186 | -50.45469 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7111f7a-66e4-3600-ace3-347076ba4658 | -4.08014 | -48.95193 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| faac6333-72a5-3aa4-a29c-e65e9618b083 | -3.54785 | -48.18467 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b48aab0b-26d1-3d82-b9a5-6f31e82d452a | -3.50086 | -50.60796 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ad8da5c-6068-3c58-81ef-63653ea51169 | -6.78148 | -42.73362 | 2026-09-07 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 35bcf985-0df9-3098-a7e7-c90411d5a22a | -4.12259 | -56.34688 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8619270-b5e1-36ac-a17b-a21fc6f230ba | -3.70207 | -58.93459 | 2026-09-07 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4e97db8-9d0d-3a0f-91e1-63a742d22c06 | -4.9569 | -56.25945 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f314a85c-3d87-3e37-927b-e9239a58522c | -4.109 | -49.06087 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c782d915-2e1e-3b52-abbe-403ed563d093 | -1.86277 | -47.97808 | 2026-09-07 04:25:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b71a7cb5-4030-3df2-b75e-a00d2410b8c5 | -2.86926 | -50.45932 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb06a4a-9a9f-3ca4-a00e-16117dce42a1 | -2.9172 | -54.121 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31e194dc-a8cc-369e-bdd9-10e47c612a0f | -3.79161 | -55.88125 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4c1c924-9dc8-3711-84ad-3952a9a53d0f | -2.86821 | -50.44079 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2e1af1c-b8f1-3f6a-8c07-604e97827d2a | -2.88096 | -50.43755 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| fda7a2cb-2b7a-305d-aa32-822589856d77 | -5.15094 | -55.96203 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b35483f8-ec32-3b56-97cb-64525fbff0e0 | -4.66819 | -55.63492 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c0af820-3126-308b-a940-6b7b34bac0e6 | -6.78244 | -41.16862 | 2026-09-07 04:25:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f60959d-0cf2-3d4d-9d97-17a2d2991adb | -2.98069 | -54.02147 | 2026-09-07 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41d10f68-173c-3d4f-86f8-78cd452714cc | -6.57463 | -44.7783 | 2026-09-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5a31af2-3fbd-38dc-a384-e46319f4713f | -3.54972 | -48.18432 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1edfd59-1b7d-3be5-bebc-766c37fd4f98 | -4.35496 | -48.97568 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7a1a76f-9ab4-304c-b68f-f2441cdb11ef | -2.03334 | -48.57471 | 2026-09-07 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98c97f03-94e3-33b3-871f-7f808be37357 | -4.12927 | -54.41439 | 2026-09-07 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53bfeda7-5e9f-3d21-b1b7-5d3e85b532a3 | -4.38265 | -44.39415 | 2026-09-07 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 69bee383-3e45-3587-96f3-f855c0e834e2 | -4.51319 | -55.71294 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a58f83a5-d9a1-3826-b9f4-b6f46df6cc36 | -5.82851 | -49.19394 | 2026-09-07 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff284545-b395-3da4-b8b8-f04763c7d9c9 | -3.06003 | -51.24828 | 2026-09-07 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926be219-f5eb-3d9d-999c-2fd583794bcd | -7.09015 | -39.67121 | 2026-09-07 04:25:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9394cbca-e209-35fc-b62d-6db6cf7a36b7 | -2.87847 | -50.45288 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0be0de0-50a1-394c-8626-97f9b59dbd03 | -6.62723 | -38.34803 | 2026-09-07 04:25:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f80f7bfb-c1d7-3c8e-b9d3-264c2de71d48 | -1.19908 | -55.74231 | 2026-09-07 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7935378d-dc0a-327f-9a45-f60539ee48d5 | -4.12462 | -54.41083 | 2026-09-07 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b69debbe-c75b-31bc-a292-2582794591f2 | -4.33353 | -47.58702 | 2026-09-07 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dff5be31-8467-33c8-8ad9-4f1068865f9f | -2.82585 | -49.23214 | 2026-09-07 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98d74743-e47b-36cf-81ce-0adf64ebf810 | -4.51905 | -46.41114 | 2026-09-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d19cc764-87fc-32c4-b0d4-6966cf5826f4 | -2.86528 | -50.45872 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ea10706-1194-39a0-a877-9586a692fe3e | -2.06517 | -56.42423 | 2026-09-07 04:25:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47f798f3-e7ea-3472-8ee2-84248d20938b | 0.21123 | -51.28587 | 2026-09-07 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62f4310f-e857-3565-b3b8-658fc22f5c71 | -3.7709 | -47.54865 | 2026-09-07 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09626843-dd60-32be-ada4-9fc54c8d7192 | -6.40288 | -42.96049 | 2026-09-07 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8259c0bc-9caa-3918-8cb8-fdd2ee1a520d | -4.21434 | -48.56031 | 2026-09-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1716c71-4565-30c7-92de-de73fcb68b35 | -2.87219 | -50.44139 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README14.md)
