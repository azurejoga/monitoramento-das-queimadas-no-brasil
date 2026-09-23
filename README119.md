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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bf3ce1b-ae98-349d-af8f-ea364750602b | -7.04119 | -62.93946 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbb03e01-853a-3a75-a067-f004d22638a5 | -6.53128 | -55.35533 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b960f1b0-e255-3b5d-9fc0-6981a2142e59 | -6.08095 | -57.62636 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fee2fed7-4a8f-341e-93e2-b80770da9393 | -6.77328 | -58.60679 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c99e132a-dd6f-3f3d-b91c-56db0d8e600e | -6.28587 | -57.77213 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce667f7b-4193-32c4-8a2b-b664245dd52e | -5.65485 | -60.21357 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48ec3898-46f1-3454-93ef-e7a0049d6133 | -7.31559 | -55.22629 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e22e7a7-e454-3e4b-ae9a-6a686e66c275 | -7.02645 | -57.42216 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf07ae3-3c40-3aa4-85e1-a173177ee45e | -7.09981 | -52.75414 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0743f6ed-1abd-3b4d-a6e9-0560b7669400 | -6.62475 | -59.99545 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d910123e-9192-33ab-bd81-6e9c61b9a41b | -6.09613 | -57.68421 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c57bac-da8b-36fa-860e-d129000a6991 | -6.62426 | -59.93436 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4347a91d-ec3e-3fa8-b8ec-07713dbd5942 | -6.62531 | -59.99194 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f465e61-e958-3e42-8177-a62c87dfa8e8 | -7.14751 | -48.44986 | 2026-09-23 05:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87816bc0-bdd0-3cd0-9177-d6be48a8f62d | -6.35522 | -58.287 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff0fb2e6-6ca5-321a-80a1-a7f3faf5e18b | -6.30503 | -59.99864 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9dcd3db-189c-3b10-b409-76f774a14a39 | -6.64976 | -59.92409 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa22c008-3bfc-39e7-b70c-b62f93035862 | -6.29426 | -57.74034 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34136a6a-f32a-3e36-afa7-76d52975001a | -6.67031 | -55.06846 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff09896f-dbd9-3966-9817-16aef9db493a | -8.45722 | -51.48491 | 2026-09-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5eb1bf2-dca1-3cc0-a8ee-aa10c769b6ec | -5.81518 | -57.73964 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b492e76a-2341-370b-9474-67b45955eaf0 | -8.17159 | -54.79847 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afcc08a7-820f-3dd7-aef6-93b8b163f0c1 | -6.67715 | -58.57085 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b7443d01-5641-3dbf-950c-cf84aa53258c | -6.92763 | -59.6302 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3309f6ea-80dc-37e5-b6fb-6d1b89ea8055 | -6.44539 | -57.77806 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3072a2d8-56f8-3e47-a144-f4e549ae4691 | -6.4483 | -55.00089 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23dce32a-eeae-36db-bfe7-7035eca3d121 | -6.04641 | -57.82663 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64f70399-e2d5-32f0-8c0a-4c28599169e8 | -6.16072 | -59.94293 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2be3fef-d76b-3045-94ed-4de2d96ee446 | -6.84031 | -55.53703 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35566abc-ed2c-3437-86ed-f00678ff78a1 | -5.21889 | -60.05717 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88ee97be-af86-317c-9514-38a4d0a6c3d7 | -8.33068 | -50.82518 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae4e2703-87ee-354f-9e42-121f7cb3762c | -6.30269 | -57.75268 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2f9ca7c-b953-3aff-99f9-e7f4959e2c3f | -7.02342 | -62.93196 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815a2089-deaa-3f1e-b6a2-2c2961ddbb28 | -6.14075 | -59.9397 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66a51e82-d595-3f3e-a355-1da348c64034 | -6.73915 | -59.42551 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e11fced3-9875-33e9-b5df-54e33020db34 | -7.32772 | -55.59212 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bce63d0-aa8f-3f7a-962d-0a942ac67b30 | -6.13624 | -59.96779 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db857697-f861-30c3-8a5d-7ed36a057369 | -6.65197 | -59.93163 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e62b91c6-470b-3f89-8387-a20968688934 | -6.61371 | -59.95776 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f84b58e6-08a3-3980-aa35-a8d240e2b926 | -5.91976 | -55.69717 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e07fcf2-7c88-3ac3-b435-8eb9683ab034 | -6.09276 | -57.68368 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7efb4da-83ff-3c11-a37b-0ab8c2ef0dce | -13.91943 | -47.83429 | 2026-09-23 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acd7f13e-0479-39b0-8407-7f74d4b399b8 | -6.10512 | -57.67083 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 06e25785-9ba4-3e40-8048-04f011b1de60 | -6.12958 | -59.96673 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5899614f-ba17-349d-b476-06506e9fd96e | -6.94941 | -60.06956 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73e41b89-05b2-3075-aaf9-099c37e96c23 | -7.57199 | -57.67792 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e6a9c74-89a6-32ea-976d-20a0c05c054f | -6.54893 | -56.03373 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a678732-6acb-34fd-a24c-98de2ba331c5 | -6.62261 | -59.92333 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8da2ae4d-390c-3224-82cc-a701d543ab62 | -6.44664 | -59.9604 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fa2757b-9bdc-3c87-9c81-ae2addccee84 | -6.31671 | -59.96816 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2804946-2a2a-30f9-96ae-3f85c4c60ec0 | -6.01991 | -57.67619 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a1478d-3151-3fa1-aa68-94ef278d4ac0 | -8.33485 | -50.82687 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49e0a6c2-5fc6-3275-9183-896c31cdb8e4 | -7.78178 | -50.23081 | 2026-09-23 05:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 543f6302-166f-3a17-a20f-b9b48351ad49 | -6.44601 | -54.99829 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d325f25f-5439-3bfd-a05c-86a9d16fa016 | -6.61866 | -59.99087 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da900525-dad6-327f-8bcc-da2d4f888553 | -5.97898 | -57.78358 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff482a8-0f90-3ed2-9fe9-3e14662532b8 | -6.08714 | -57.63101 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0476015f-b38c-33ac-816b-b00b1f2930d0 | -8.83409 | -50.49338 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb9025d0-fb52-3951-8941-d95840c7f7a9 | -5.98005 | -55.36971 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfb3b8b9-a909-3f4c-8758-7aee6c97bab4 | -6.84251 | -58.98817 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 149d9453-1540-3d81-ba76-00079af3fe11 | -5.93027 | -59.91727 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 578b474f-3554-3c87-96b0-f8430c0036f0 | -6.33557 | -59.95312 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 073477f3-a87f-3170-9ea6-5117feb04236 | -5.93969 | -57.70417 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ba3761d-d17d-361f-a9d5-55d2c855f2c2 | -6.16349 | -59.94698 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b9f41eb-6870-3438-933e-8609c56c44cf | -5.98455 | -57.70382 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22aa2209-063e-38b2-94ff-3af9437c443c | -6.61984 | -59.9193 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6315694f-d671-3fc6-97aa-3417dfa2f23f | -6.71165 | -58.99912 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c0b4e0-cd16-3de5-ad2b-f0dabc751b2b | -8.27982 | -54.76916 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39d6a375-5c12-3d05-8232-7d5e9cfe2c17 | -6.63591 | -59.92546 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b7fdcae-8544-38c7-a4f5-2d8a7dac9c5d | -6.84002 | -55.30663 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cec12fc-6902-3cec-b6d6-cb7cdd7a6ca1 | -6.73253 | -59.42446 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f572518-eee3-3441-9224-91f12db0b620 | -5.16284 | -60.30072 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b341987-8bbe-309f-b697-3a5272665fc1 | -6.42542 | -59.98904 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2588897-c35d-3ab7-8dae-a4635692d5e0 | -7.43733 | -49.84212 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 45536c6e-2a84-3959-9228-b11f762fe116 | -6.75586 | -59.06287 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e572db0-26e7-33aa-8b43-b7019d4938d5 | -6.6292 | -59.98897 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77149d3d-d63d-330f-ba9a-762a5a227b69 | -6.73941 | -55.30804 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df71fdd0-fbd7-3965-9ac6-16d55e405088 | -6.68325 | -58.57537 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd0a3257-a94a-36fa-abcb-cdcd82f7f57f | -8.18047 | -54.82046 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a7ce36d-2344-31a5-a4ee-4f234de1d71b | -6.68047 | -58.57137 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9216ac4-99e5-347a-8750-b9805e2bbcda | -6.85908 | -63.01578 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d051128-d48b-3c0a-92df-88c59f365673 | -6.30155 | -57.7378 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff765237-15eb-3c40-b60c-c6c9dd17c56c | -6.63035 | -59.93892 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ec0f5168-e7ca-3971-ba5a-7e30d728a366 | -6.62254 | -59.98789 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35f01fc6-c2c8-36a3-a907-0c5615d44f37 | -6.56872 | -55.41149 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ae7d30a-c166-3684-81ed-8432ce005ec8 | -6.78464 | -59.65327 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa1ad21a-c5bd-3d31-bdfb-437e8f2f9e4e | -6.10456 | -57.67442 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1508d510-3c5b-37f7-a7e0-da8d049088c8 | -8.19888 | -54.72371 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f198027a-660d-3185-b888-f6fecdf7ca2d | -6.34997 | -57.77058 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38bbc77b-8e73-3a3b-bae7-b543c25d09bf | -6.74853 | -63.14252 | 2026-09-23 05:25:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62fa64cf-b498-3d24-8000-95e4c1cfaa59 | -6.43773 | -59.97338 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a0f653b-6a99-3aec-bcef-ff57285180ee | -7.28216 | -56.46817 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5bb72a2-d78c-31e4-b2a3-68f344314ab2 | -6.45664 | -54.99727 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d0535bf-9e14-342e-bd02-7bf94e88c126 | -5.65428 | -60.21712 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c4062f7-a880-3a87-a97f-b744143bacf1 | -7.11736 | -56.55121 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b0c6fd7-8a38-3fe4-b81c-5b9a78450588 | -6.67725 | -55.07426 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ec476a9-b9db-3dba-b108-471ade7a58ce | -6.12981 | -57.75549 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e3f0f07e-cb38-3dff-a539-a2e8d906e456 | -5.28036 | -60.20175 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e84b5271-2f94-3e9e-91ed-4caff000984f | -8.82875 | -50.49255 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d00b799-02a4-308b-855b-d9d30c94f28f | -8.83454 | -50.49 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README120.md)
