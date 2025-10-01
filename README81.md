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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f92494aa-bfa3-32e1-8998-a1ae51d0fde1 | -6.42763 | -43.07475 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ea93d16-0845-384c-8cb5-64df8f226752 | -5.47002 | -43.07308 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26e68f3a-06a4-3e21-9efd-f164b710be30 | -5.7872 | -43.305 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a50858c-71ed-3739-9934-32320ead1951 | -7.83026 | -47.05592 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1a73e16-d7d9-39c8-aa1f-5abc126e0a8c | -8.33971 | -50.86231 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e90b0073-fa08-36bf-84d3-7dab55ca7520 | -2.89137 | -47.84509 | 2025-10-01 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1d7096f-6418-3114-b3e6-e18b45def32e | -6.68048 | -42.79964 | 2025-10-01 04:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69f18dd9-0b0c-3406-a1a9-4e77702eb1b8 | -7.87271 | -47.27665 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f13aff6-1098-3620-8bd4-321eaf2cc6b2 | -6.98457 | -42.80039 | 2025-10-01 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b212bd31-2f45-3299-8d73-8a16cd5071e4 | -7.05525 | -46.41994 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e1cc226-32f2-3ebb-9284-f884187d9c36 | -7.56452 | -46.77388 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f84a9967-95fb-3270-9dc1-4a8da6d67ca0 | -8.53666 | -44.70616 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4865d79d-cf5b-3664-b903-fa9a1969b99e | -5.90735 | -43.44393 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ae231e9-5dec-3078-96bd-fd8e3271e4e5 | -6.46256 | -43.93999 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e209a69a-7efd-396c-a053-fe5e9c68e085 | -3.49709 | -52.46172 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cf277348-d7ab-3b28-9349-5d96775284e3 | -6.2765 | -43.65031 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7cf30173-0026-3f1e-84a9-0a0e6eb192c2 | -5.68021 | -42.63529 | 2025-10-01 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1acbd4bf-335d-3abe-85a3-1d157f1a62f5 | -3.54159 | -51.15417 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dae0a0d8-0a36-3bab-99f3-83d17d92d02f | -6.61462 | -44.26474 | 2025-10-01 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 37500f38-8729-3442-8625-08622d6bdffa | -6.03401 | -43.80869 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af3b53e8-409e-352e-bdd3-08a7a79b05eb | -8.64945 | -46.61846 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3790e311-1836-3495-9b6a-74a6d3690ba3 | -4.25397 | -48.55355 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e14f5ac-91af-345b-b276-987c688b373f | -2.59469 | -48.12144 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a55c5707-ce70-332a-b72b-f594fe988987 | -6.2148 | -44.2276 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 595101eb-65e8-35c9-ad50-56ad8c5cc27d | -5.49601 | -42.7541 | 2025-10-01 04:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 943feb6d-9707-3f37-b239-8627f51956a2 | -6.25539 | -43.66175 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8af8294f-c3a2-3c32-8609-8fd980d7aba7 | -3.49649 | -52.46547 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03f911e5-a6dc-3bae-8d3f-91e5e6449393 | -5.62334 | -51.93714 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b785a88-4617-338f-9a60-dcef584437ba | -5.9806 | -43.61087 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78d97333-6bd2-315c-9702-e4244e375680 | -5.98524 | -43.61271 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3baaf3c6-eab0-3341-8435-8a3da3b361f5 | -2.69235 | -54.76685 | 2025-10-01 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 133a9f65-18fe-335c-a110-59376cfb45ac | -6.04744 | -42.45016 | 2025-10-01 04:49:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 513139ec-288e-3518-9a62-90c49cbd60ba | -7.01929 | -44.46253 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c50978a-a393-3ce6-9d93-2638b66cddc0 | -6.46069 | -43.93619 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11a83ff5-f27c-3ed3-9c51-65f8850a352e | -7.02514 | -44.45433 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48179c31-ef38-3d40-91c0-cbcb9cf8f29e | -8.56415 | -44.70986 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a35e322-8b2c-389a-a989-6bf336545f6b | -5.68063 | -42.63234 | 2025-10-01 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a652737-ce2e-357f-9652-e154a663e219 | -2.79001 | -49.62325 | 2025-10-01 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edaeb818-e124-374d-93c4-2f2354e1b5ba | -3.85789 | -40.43707 | 2025-10-01 04:49:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 022baf7f-df27-3630-9140-933176af99ee | -7.5638 | -46.77887 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6254009c-148c-388a-8720-3edd6f451429 | -3.82549 | -52.04364 | 2025-10-01 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 467d8403-5e2f-38d0-ad09-d4dafcab5e19 | -6.142 | -44.73789 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d527e618-dcd1-3309-aa43-621cd0322124 | -5.40799 | -41.32997 | 2025-10-01 04:49:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29ee717c-3527-3daa-a5f5-9ac505048e08 | -6.117 | -43.22704 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f4bbf6c9-405f-305c-83ac-60cb0db6a49a | -7.47534 | -46.46684 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 121d908d-82cb-35ad-82a3-f60b3a200ccf | -5.32146 | -43.32542 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ed7bca0-e063-31f9-a3ff-1e2a5e3f9511 | -3.35341 | -43.19598 | 2025-10-01 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c17b73be-1052-38a6-b6d0-c71fcb9c94f4 | -4.31539 | -48.09359 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64c32c22-7252-3e95-b304-4e7a237f8b32 | -7.56059 | -46.7733 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de4fee2f-10ae-3b42-8488-6fe77bb78544 | -6.98499 | -42.79738 | 2025-10-01 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3fe1e02-b439-3934-8701-349bedd6f269 | -3.46384 | -50.09082 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d3110a0d-4d62-39c1-9359-95175575559d | -8.52243 | -44.67397 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 668adeb2-5d43-3f75-85e6-709fe6b23a6d | -5.85024 | -43.40112 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 222ac5cb-b50a-342d-b2b0-c1ba8eb63f3b | -4.33367 | -50.85537 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5a0b48f-fb78-3fd1-8ad8-fe3f45f614b2 | -7.84578 | -47.05813 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 043f3322-dd37-3e13-8eb4-1d7bdce3b2ea | -6.61035 | -44.26255 | 2025-10-01 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06b10b07-c9de-3a17-b117-a45776a5cc39 | -9.03128 | -46.69219 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cc7c427-951d-35bd-9df1-1edcb515dbdb | -5.24465 | -52.03773 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8563763c-ceea-3543-b723-aa437606d4a7 | -8.55825 | -44.75156 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50f3f095-094a-343f-8dca-4b733dff2444 | -5.2045 | -45.45257 | 2025-10-01 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c6248f6-6bec-3d40-bb84-569264e2fcba | -3.51757 | -49.44557 | 2025-10-01 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 769483e7-a3e5-3530-8938-877c3cc94f03 | -7.06668 | -46.8463 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5275d1d3-310b-3847-a6d2-fd4b223fbd71 | -5.94187 | -45.86508 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20d5f443-3020-3a32-b390-0464f28d5863 | -6.89623 | -48.00346 | 2025-10-01 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c588e0f-ff85-360d-80bb-f81f11640bea | -5.94168 | -45.89392 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f126b886-402c-39c5-b098-cb738023feb7 | -3.94217 | -50.82897 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2642973-9bec-3a75-b211-9d046486fb3f | -7.8065 | -50.04313 | 2025-10-01 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14130ad7-0d86-3437-9df3-1ee6335a14e2 | -6.10079 | -42.68119 | 2025-10-01 04:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| edd5c147-0b17-3865-a89d-3c10de2cf338 | -5.53831 | -43.87582 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 031d883b-59c1-3ecd-95a1-13d6c390cddb | -3.68758 | -49.04952 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dce2ad73-f3d7-3bdf-9ee2-35462c5d69e0 | -5.6398 | -43.91689 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f0b1a0f9-87b8-3553-8317-c051d717a7fb | -6.11984 | -43.48906 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a05df579-b845-3e6c-97f3-0ad6c599d7bd | -7.82483 | -46.9839 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f18e02d5-ffd1-3f23-9615-5952a5eec6a6 | -8.86393 | -47.64785 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 357ebbf7-ecfa-3dcd-bc51-18ae33091e7b | -7.05282 | -46.40895 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 776581ba-7b94-38fb-b73d-8535ff25c706 | -6.55096 | -43.93998 | 2025-10-01 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 21f8d0a6-cb1a-30ff-acab-dd02dc76f83d | -3.89438 | -49.08833 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf62e340-d10c-3012-a850-3407bfc88442 | -3.42193 | -46.96827 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7867af89-e7d1-3714-87fd-9c3d64140be6 | -7.05315 | -46.41589 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b61126a-9527-353c-aa51-c4d58ac78bfb | -8.16022 | -46.24677 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02da8c49-dd0e-3c65-8a59-59473494cc73 | -4.40015 | -50.84451 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61074917-9173-3e49-a6b5-43b9ee15f5e5 | -7.63103 | -45.44806 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66269cc8-9833-3a7e-9d67-5b294433d1d1 | -3.49995 | -52.46601 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a00e04f-5418-3908-b85c-41052bca7d37 | -5.87553 | -43.56136 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aad82292-62b7-3c38-bd43-bd3b567fb800 | -7.05447 | -46.42513 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96f82365-1086-379d-8a92-819ce1976b8f | -3.49589 | -52.46922 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84c72a87-28a5-3c96-b5cc-a3e5272c0eb2 | -7.09398 | -45.55513 | 2025-10-01 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf2d0c22-40a2-3453-97ad-2b04647d692c | -7.02241 | -44.478 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9915cc62-abd6-351f-a26f-8f4812e28e01 | -8.15765 | -46.265 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6779924a-8ad3-3226-8b56-f780eb62823b | -7.02259 | -44.47165 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dae6586-b5bd-3856-a4ab-023d60d59c0c | -6.81442 | -47.3219 | 2025-10-01 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbd3a6c0-bbfb-34ed-be0d-ed7031e1ddea | -6.91071 | -55.45307 | 2025-10-01 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f9d28c2-cb87-39e5-bf63-d049c6cbbf69 | -7.77184 | -47.38854 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c1b57b9-d48b-3d2f-b93d-cbf7788b2357 | -4.31248 | -48.08916 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bf3439b-411e-3a4e-aad1-79807e1a1c78 | -7.12582 | -45.54398 | 2025-10-01 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30e464d7-8916-3d30-902e-fe9e33f1d210 | -6.72406 | -50.94818 | 2025-10-01 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98ef5cdb-7ec7-3880-baa1-dc922b7d5756 | -6.81725 | -44.47255 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a46ec5-323c-3189-9582-ab0298162d08 | -5.72683 | -42.88284 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5dbcdce5-7e4f-3331-928c-7e52d570b0ab | -5.24228 | -45.5934 | 2025-10-01 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06e8e4d9-e7ca-3266-a87e-654f2e430daf | -5.90005 | -43.92733 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README82.md)
