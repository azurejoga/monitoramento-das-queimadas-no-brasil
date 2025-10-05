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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1105d19-2fda-3f14-9055-710df04b09a6 | -11.20472 | -54.85067 | 2025-10-05 04:46:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16a16e6f-0ad0-36f7-96a2-9d3827a19c5e | -7.72364 | -42.55687 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0076b387-204b-3b23-8566-5e9e9bcdbfe8 | -8.90921 | -46.59437 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f550fba-fd6e-3242-88ff-f1444dd219cc | -8.57337 | -47.65985 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe4e7caa-80a7-3174-91a8-67a72ec003e4 | -6.71581 | -42.82545 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ef00b31a-4b4e-3419-89e2-749361b93cd6 | -9.20956 | -46.9311 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4ab4a4b-08be-3176-8d2a-fa6e0e65ab86 | -12.9765 | -51.03414 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5982b83c-0a51-3dcd-8a08-6850a72cbe68 | -10.49463 | -48.103 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b25eea1b-fe1b-3fcd-88d0-46a0492f9891 | -7.24993 | -46.94019 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b91d333-77c1-3aed-bb51-18106cb312e0 | -13.32202 | -47.62579 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7c04a96-ce37-390f-8691-73d9397d2d9c | -10.94457 | -47.06219 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36b114fd-19af-353a-a94b-4c69cb362d6d | -8.59153 | -46.31335 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 37c18b84-ab63-3c1f-b9c0-58fffef8c54a | -12.86485 | -46.86707 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea3cb6d-a81a-30a6-ac43-9995ea45f5c3 | -10.59393 | -54.3526 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78246cc4-416a-30af-9740-682a70a47268 | -10.64897 | -46.33992 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77d17d23-1fc9-3cab-b6d9-74173b8df95b | -9.54649 | -54.59605 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22ebdaab-e155-3fb7-b971-8f6c428234ed | -8.60223 | -46.26713 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7f0497c-8486-30ec-b8fb-294bcf61a7fa | -11.93544 | -46.43288 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24f2995c-13ae-38bc-8366-ddf97966009b | -10.49836 | -48.1036 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72f547c9-55f1-3491-ac71-e8a6de02c82c | -11.1226 | -47.17545 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7d6aa88-eb11-324e-a01e-9f66404f6174 | -8.6043 | -46.28194 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2c8b569a-26f6-3548-8897-f4bb6ec05638 | -13.54575 | -47.23349 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3bd3a9e-8772-3fa8-bc0c-4b69509b5c7f | -9.21029 | -46.92608 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86091ac8-f6f6-3418-a984-e67ba992aaf1 | -8.92104 | -46.06467 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dacca2f0-a4c2-3b7e-9af9-170adc52f85b | -13.10594 | -47.82744 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfd306e0-c342-340e-9272-2330331a8cce | -9.05461 | -47.31918 | 2025-10-05 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aad0d928-ce1a-3407-b983-a50daf2ae60e | -7.05434 | -43.21716 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9717d5c6-6c7e-3c07-91b3-ba9ba8f65c4f | -12.59759 | -48.13679 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9759d7b6-0ea8-33b2-9eea-599ea2997b4c | -9.14941 | -59.53783 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7951ed38-14d3-3d04-9b06-d49094a6d36a | -9.05227 | -47.02094 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b84e13-a58c-333b-9091-6bf61f423811 | -13.21441 | -51.1502 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4f1c7b0-30a1-34e4-a66f-c715527583ac | -11.45589 | -51.51534 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdc6305a-58d2-35ff-ab76-9530f1c9d8ff | -13.54548 | -47.29822 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86212b09-1e1c-3398-8c9b-76645da8e946 | -8.55183 | -47.66846 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4dcda22-eb82-377a-af22-63999c2b4f59 | -7.31455 | -45.5607 | 2025-10-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1fe8f826-8b69-3aa2-8b14-055a5eb0b60e | -10.72618 | -47.8601 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff1348ee-08d5-36ad-92d2-ba7a3367f5e8 | -13.44135 | -47.26914 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c894b20c-4b3b-3c07-8a35-fdb33f028bed | -13.10832 | -47.86591 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fe43d54-0299-348d-af28-588e5a0048bf | -11.88926 | -45.00716 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f98f6b6-e4ca-3872-b58c-6f8b90620bcd | -11.6272 | -47.74645 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75d2ef28-4d3d-335d-92c5-c2665b984ddb | -10.83917 | -57.16993 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9856ffbb-8606-361b-82bb-3461c6c2f0c3 | -12.32419 | -55.1355 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f1ac2db-7393-33ef-a3cf-f1b876e38448 | -13.59673 | -48.16261 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3827ad12-ef66-359f-8e27-34fd490c0705 | -13.30255 | -47.61897 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a51c27d4-481f-3046-a406-a201726c6657 | -12.44973 | -44.74278 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7503ed7-17e6-364d-92f7-980e0d17128d | -13.07894 | -47.90627 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a83be8c-c264-3b8f-97c0-bf1a98ea6b63 | -7.71845 | -42.55599 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8cb11fe4-a759-3427-9d20-6b9d003e7f87 | -8.56913 | -46.32478 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e87f9308-1fa6-3984-8d48-01408542f744 | -13.33468 | -47.78969 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4af1ed-0669-3d50-982f-cc1f41383f3c | -6.72812 | -50.94075 | 2025-10-05 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36ba2e46-4047-3cbd-9959-79ffd9aaa027 | -13.37893 | -47.54994 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3015129d-f6bb-3c4c-a9d8-451650c53ef8 | -12.37335 | -50.25611 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a836e2-04c0-394e-a8ba-f263cd1890cb | -10.66511 | -48.47893 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90498b20-d24c-3e01-8b3c-6d0c1a52492d | -8.55668 | -46.26777 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e056ed74-cff3-3e77-a4c6-1db88a8e8c56 | -7.60832 | -46.09131 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c945f69-ddc3-3e47-9ec4-19b2f96b3e94 | -6.83692 | -45.4875 | 2025-10-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b762121-ba8b-3659-87d0-2c57bcf7c1c5 | -11.75749 | -44.73706 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 161e4a4b-9a00-3f6d-8dde-166306f01800 | -13.6454 | -47.29445 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4cc5bd0-20a5-391a-93f8-9f376f2e5eab | -12.89865 | -47.32205 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03595568-338f-3aaa-81c0-3a5eae2d2a36 | -6.73454 | -45.97422 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 308853c3-7a18-3626-b0af-2fbba25d17e1 | -10.57519 | -48.68534 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30835b66-478c-3d5f-975b-5e8d7b45f1dc | -12.40927 | -51.10057 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08c29e4d-26dd-33b3-a82a-9a9ad640c626 | -8.56862 | -46.3284 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93959129-32d9-39a8-8643-789881916c1b | -13.31684 | -47.77989 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc5752c5-8a47-349e-b242-6ae0afa221e0 | -8.58745 | -46.31275 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c9c19b0a-ca33-32f2-b18f-61d0ed82a46b | -12.30742 | -55.14922 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6539104f-9457-3b75-a2f8-73a916dea2c7 | -11.79654 | -47.91499 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9acf8547-6471-31f5-853b-4c05eaf47f53 | -12.31338 | -55.13042 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48c3ea4d-9aef-3bfd-bc6f-c4e562c22d1b | -6.76395 | -42.24262 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d7d29b52-4b01-30a3-9dd6-e6968b3ff926 | -9.40927 | -56.89376 | 2025-10-05 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c9304f8-b639-3fc4-b358-2683884a5709 | -11.46252 | -51.51638 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6606e7da-52e7-3a50-8d6f-ebf0ad7af58a | -13.46392 | -47.28776 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd9c0fd4-a819-324e-b061-1bb40a25ba81 | -13.1396 | -50.90062 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 233eab74-ce03-3453-934a-568d5f3896ac | -9.95555 | -48.7586 | 2025-10-05 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b6b90db-624f-3249-8d42-3f7e7338a61e | -11.87065 | -56.87287 | 2025-10-05 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00d7c894-64f3-3316-b4ab-8e84f7a808a2 | -6.87579 | -44.49833 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 210cad4e-2f34-3200-bae7-38154d7ad55f | -11.45203 | -51.51835 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a032e34d-6efd-35ed-8a5e-cbe63233fe54 | -8.55336 | -47.25887 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edf5aaf8-dddf-37ae-ba44-57c62e8df62b | -6.87671 | -47.23566 | 2025-10-05 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 268331f5-13fe-3f7d-b656-73267f577bb3 | -7.47558 | -43.02893 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44034ecc-d743-3686-bce9-9bc0a516fb82 | -9.79716 | -48.2753 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4f43f19-64bd-346d-b706-f4ba5a286eb7 | -11.11426 | -49.86248 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07118b8f-438a-3ac9-a9bf-dd46ec1b0160 | -11.83185 | -45.09541 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c795fccf-06e7-340f-9420-59de59af9365 | -10.46443 | -57.49892 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b7d7e8a-f017-3681-93cb-002e1d249b9a | -11.95188 | -51.47393 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f50028b-6dcd-3942-b013-178c9443c5bf | -9.12353 | -44.4003 | 2025-10-05 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ce6fca8-7c7a-3de1-beac-5223104a06e3 | -10.49024 | -48.10697 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3cd0756-7125-33f3-a00f-a36d47733115 | -11.11136 | -47.87422 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d44be35e-bb10-3a52-a217-b958eab35449 | -10.82975 | -49.38797 | 2025-10-05 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67a60411-77a7-3657-9b9f-3e3f60e23d53 | -11.63414 | -46.8774 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a3325f-39c2-3651-a804-bc0271f47aba | -8.08995 | -45.6992 | 2025-10-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cad7aaf7-616b-303a-825b-9d14eb80b8db | -7.71284 | -42.55828 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d4b8ee9d-c50e-35d1-8205-86ffcae4442c | -10.75693 | -45.33883 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c09a43eb-bae1-3e21-ac0d-b2ba89d359c7 | -10.35387 | -48.17075 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9c51832a-8f85-31b1-ba29-e7ca14b5e6ff | -12.32566 | -55.1482 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea5f5a24-3428-3bda-93ba-bb91a162c1af | -8.61241 | -54.7099 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5428fda2-4905-3448-9220-6be6739590d2 | -8.86564 | -46.81293 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 80b9ef6a-eaaf-3c32-9f96-e128830045ac | -7.79752 | -42.56724 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b07d579-c6ed-3f98-9d91-9cabf06ba395 | -11.91066 | -55.90792 | 2025-10-05 04:46:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a99988b0-aa6a-3d56-84c3-488b9b4fa38c | -11.93434 | -46.44104 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README88.md)
