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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd46f818-8ea3-3c62-b7e5-1b607993e600 | -5.53676 | -43.18535 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a0b255f0-aef1-3253-b999-7b1904a75a1c | -5.15884 | -42.74289 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c1ee648f-82d7-37a3-9a33-5919a89e812f | -7.6372 | -45.43344 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ba282bd0-d560-31f7-a084-9e2c307a24b7 | -8.3901 | -47.18112 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 14d010ed-bf4e-38ff-ba64-a6b6e9dde66e | -5.23804 | -44.60415 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ab542bf-460a-3e5d-8b99-d99cf1ad7771 | -6.99361 | -43.30181 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| f3a821ab-7178-3848-878e-3b9145b8ca18 | -4.36505 | -42.69103 | 2026-09-21 16:03:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d419d800-63a6-39bd-955a-e9298ca6c7e7 | -8.30886 | -45.98997 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d4eeb872-165f-3fd4-a631-d42f828b98b4 | -6.23933 | -40.83027 | 2026-09-21 16:03:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5d7a2026-1475-3e80-9498-275f7dfcb5ef | -6.55168 | -43.29622 | 2026-09-21 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ca7304e8-3174-300d-bf0f-bbe0e58daf42 | -7.56367 | -42.6546 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 77c6c7d3-64cb-3d85-bc76-1b3fdec3b426 | -5.85032 | -49.78547 | 2026-09-21 16:03:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 608991e5-7b78-3273-b86f-ca64dd707abf | -8.13482 | -47.1287 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d28cf82-700d-3d21-b9d0-d3b87d6cb4fa | -2.94895 | -51.04474 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| a2403fab-b208-3a32-ab44-29268267222e | -7.18583 | -47.48011 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4b1afacb-3bbf-3bc3-8a00-2b31762efc7a | -6.2918 | -47.65709 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 988e2be9-b127-3417-851d-0e3572fc521d | -5.65416 | -43.1924 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e4009c65-47a5-3a73-8e59-e51464ff9dfc | -7.13592 | -42.07727 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 96180416-0a8e-3c5b-9124-5961c462b02f | -7.40489 | -44.79032 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 42d4ef7a-968c-300e-bfe0-272593e77307 | -6.93521 | -42.9007 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 18b7685c-adff-3d7a-83f1-3575fcc79622 | -5.64199 | -43.36453 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bfba7ba7-a3c8-35be-9818-eb1520290adc | -7.95111 | -45.6558 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b89efc13-8e06-397c-9d2c-28f80fd22a8d | -6.91765 | -42.89256 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 021671b1-307e-3ffd-9074-9ad1c1a53d15 | -6.91623 | -42.93945 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 566ba4ef-f17b-3dd7-a056-369c61bbbae3 | -8.0259 | -49.54741 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5955743c-0897-302b-88d4-6b1f2ccfbe9f | -6.66115 | -50.88999 | 2026-09-21 16:03:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8fadb45c-24cf-3215-969f-fa4c756705f7 | -4.84898 | -43.55095 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 577ba328-cc24-3487-8535-0067f4011260 | -6.80224 | -47.89457 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4614b3fd-22e2-307d-862b-6474538268c5 | -5.61544 | -43.3838 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 780c5774-d8d2-3bb0-8b7e-108286614d75 | -8.48689 | -47.0162 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd17a928-c1f7-3a67-87de-e22d71bf9776 | -7.59245 | -43.43036 | 2026-09-21 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0da528eb-c32d-377a-87a8-6bdeaf4ea1c9 | -2.47106 | -49.81409 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 5d6c054d-b3ee-3f83-a03a-5df434b8ca97 | -6.2538 | -41.65102 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 259.4 |
| b8448aab-d990-33f5-ac89-fcd6b24d5b60 | -3.0462 | -50.26968 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a5f7559-8749-3eee-8321-5bbc69292774 | -6.20203 | -45.35865 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ddf2a377-658d-3500-a78c-64a9efe4b9ab | -3.38416 | -50.41164 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 5c2155ec-a81d-3bdf-aa31-d1e0baf20ef5 | -5.84513 | -39.96456 | 2026-09-21 16:03:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| adbf6536-a910-3593-9280-6895f8c833c9 | -8.78019 | -49.95405 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 26bd1df8-afc1-301d-95d9-1fea77710a48 | -5.84547 | -35.29925 | 2026-09-21 16:03:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b73343c1-fe73-3dec-abf5-41e0b33433fd | -3.24583 | -42.79633 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66f5d17f-b62d-38d3-927a-18a03be1561d | -2.16798 | -48.32397 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 87e18d04-6e2d-356f-acbf-705d44896949 | -7.054 | -49.91568 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2365c866-70e2-377e-9022-6dac0bb16df3 | -7.74629 | -46.70573 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e7d13257-5391-3bdd-9c65-c96a1bb80194 | -6.98938 | -44.70517 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| cae3d3fe-9d08-3c16-9fe9-bc66b4c1298d | -6.8481 | -45.52837 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 729d6f32-245a-33c0-b018-21523d6d57e2 | -5.83792 | -43.85843 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 335f3f6a-042a-315e-858f-7fc3129bf8fd | -8.31667 | -46.00962 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f2a5dda0-46a4-3cec-9ba0-a73579932577 | -7.4205 | -44.7356 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b456a60c-dbe6-3611-9a6a-6397fdfdac88 | -8.43984 | -45.82627 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1d7f27a7-46bf-3da3-960e-03ba4cdbaa1b | -5.809 | -43.77597 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 91913f75-9424-3fc0-9da6-99d5085f8712 | -4.72885 | -40.56084 | 2026-09-21 16:03:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 964ccb7a-292f-3b2a-a5cc-8ea422bc120f | -6.9301 | -38.73155 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9d224226-f729-31fb-93e5-de4344326fa5 | -5.4082 | -42.96428 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 84d19001-751b-3419-b4e6-7c31e81afa00 | -3.57987 | -40.3107 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2e8b769a-59ab-38b6-8f37-f9efa8c48408 | -8.79087 | -48.74385 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3162062f-c3e9-3120-8102-74b6e8c35104 | -3.36908 | -39.63474 | 2026-09-21 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 4b0466c0-6a06-36a7-9ad9-cae7f7fadc5d | -7.73808 | -43.90673 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2c56946c-b862-3e7a-8a37-1c3bcfd72ea1 | -3.57691 | -43.46616 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d09108fb-fa19-3a18-a430-c2b502a0a76c | -3.43618 | -39.24761 | 2026-09-21 16:03:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 805a1983-1922-300a-ae4a-5603889fc01c | -6.55835 | -44.83715 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83e58bb3-ce06-3b70-bc65-56d15e45231a | -6.98351 | -47.48265 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e323131f-637c-3082-b5ae-1437d37f116f | -7.05336 | -43.65173 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e353fe76-f0ce-3931-a511-0ffa3e17b549 | -5.76275 | -43.68958 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4392643f-745b-386d-bd72-396bb5c042ed | -7.55169 | -48.68434 | 2026-09-21 16:03:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 963897a7-4c2d-346c-8eaf-3fdb5b2386de | -5.82529 | -43.86022 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8830770a-b708-3b8f-892f-12ae57908e32 | -3.37241 | -39.63425 | 2026-09-21 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| daa01193-9ded-3895-8f97-8a664c1ee912 | -6.68324 | -44.0669 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8da8557a-87a5-38c6-81f7-91ffcaaef66d | -3.25033 | -42.8004 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 200ac3db-d2f2-35e9-9bd8-97edad8ffb25 | -3.44498 | -50.61269 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 92a9b144-9ba7-3b07-bf9a-8c1149c14dc5 | -3.25086 | -42.95765 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c79e6b79-4a3b-3244-9d59-8c2255ed4f22 | -8.45008 | -46.40089 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 203b0049-caad-3340-b6a9-215ce7088257 | -8.5046 | -47.02482 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1f45798f-0505-3552-993d-cb57cd1da06d | -7.73254 | -43.89901 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fa1f8a37-ea34-3796-b637-fa3c01113dd4 | -3.67029 | -38.90759 | 2026-09-21 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 56823b61-05ca-3dc4-a65d-83f1cd9bd6cd | -6.93572 | -42.90422 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f7431e1b-8011-3c86-94d4-94192348a983 | -4.68721 | -40.14603 | 2026-09-21 16:03:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9f4d45e2-ba60-372f-853f-1f247cdddb46 | -6.25081 | -47.64412 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4c661bfb-760a-3601-9205-ef42e141f127 | -6.21323 | -45.35207 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f9921a32-6b0b-3d3c-b60a-3a0b579a2582 | -6.26119 | -41.65004 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| bd699d7d-fde2-3fa3-9a38-9e4c181c95f7 | -6.20666 | -45.35763 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8e44e865-3c21-3d04-a1d6-fde2a55e6f12 | -5.57364 | -45.29509 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fc444a67-f9cc-388a-a15d-f24593a6539b | -6.72012 | -43.95367 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f4bc3162-a4be-382b-a30f-415122dec08f | -6.79357 | -39.92956 | 2026-09-21 16:03:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 990df71c-e0c0-354a-b744-4a20c7d15be4 | -6.79082 | -43.90704 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c02f96ec-eba3-3760-9f55-ec6b12f594f8 | -5.83539 | -46.11829 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6763a3f3-24eb-3229-bbff-42c52a88ba79 | -6.93725 | -42.91473 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 63dc285b-9f4f-31b1-bc7d-e28e092d6ce9 | -5.4146 | -42.95308 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8f980576-ee5c-321e-98f2-a6c81b5f1bb1 | -5.3925 | -48.95665 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1d567a8b-5c6a-3125-b913-c67616eb1dc0 | -3.37983 | -42.97198 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 90470586-836a-3dea-8234-bced090487c4 | -3.71404 | -41.10978 | 2026-09-21 16:03:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| b546cd78-496d-39d7-a737-8be04c39deca | -7.73814 | -43.89434 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 79695ac0-4ec0-33ee-b708-1da28b0aef58 | -3.70485 | -38.84613 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 807db4cb-6b07-3437-b530-4bd55745914e | -8.48779 | -47.02322 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7e745c2e-43e7-3428-b703-05d250e7676c | -4.81471 | -43.62943 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fbd7a453-5be8-363a-adad-41bf0271d9ce | -3.47536 | -39.61804 | 2026-09-21 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7bcaabc2-651d-371b-921f-f041f707ec6f | -8.3124 | -46.01619 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 16de3761-9762-307d-80d1-d3c03da72b35 | -6.81192 | -47.88126 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3d001e42-4277-3f29-a56f-9e52140bd4e4 | -6.11009 | -37.85038 | 2026-09-21 16:03:00 | NOAA-21 | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 35df89a9-b255-3756-8166-36a7a80c64b6 | -3.57225 | -43.46884 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| e18a1ca4-2148-37bf-8bcc-3b34656c29ae | -6.07341 | -38.30111 | 2026-09-21 16:03:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |


[Clique aqui para ver as próximas entradas](README163.md)
