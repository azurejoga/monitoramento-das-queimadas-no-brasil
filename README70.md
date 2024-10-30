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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0db432e4-186b-346d-bc8b-7073495d7edb | -5.60558 | -41.72313 | 2024-10-30 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30fd0c46-acb8-36b0-a207-c3aba2788455 | -5.40361 | -41.41817 | 2024-10-30 04:44:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d590071a-41a3-35b4-856e-831afa577866 | -5.3982 | -41.41735 | 2024-10-30 04:44:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2279c56e-10a6-3553-9566-629a32a2de4b | -7.33227 | -41.86115 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8a663507-dfbb-3cfa-b87f-36eb3e2a538b | -7.33182 | -41.86452 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e969d458-469e-3a1c-b14e-bd45ca8ee157 | -7.3264 | -41.86381 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb56d71c-6fdf-393f-9223-c1728da71759 | -7.32594 | -41.86717 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9176708-6af3-32e3-b448-b79dd8bf56a9 | -7.32548 | -41.87054 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c075387-378a-39f5-9ce5-69e50506a8e4 | -7.31959 | -41.87331 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb6b1e54-9952-3e35-bebe-6514d3e1994b | -7.31914 | -41.87665 | 2024-10-30 04:44:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7dae9d79-8836-3f13-a681-47da5d4a4fc7 | -7.05098 | -41.37793 | 2024-10-30 04:44:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4911e8c5-2d30-3ca6-ab3f-c4ee4a1d30c3 | -7.0466 | -41.37645 | 2024-10-30 04:44:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2defdb91-6171-3f31-9b01-bae7441bda90 | -7.04608 | -41.3801 | 2024-10-30 04:44:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6d839817-109c-310d-8c16-96e948c513a2 | -7.04542 | -41.37709 | 2024-10-30 04:44:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7d007f4b-95c6-3461-a7f0-a745c3335e38 | -7.04493 | -41.38073 | 2024-10-30 04:44:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f2e728bd-c595-31f9-849d-35b48c3a482c | -6.98839 | -41.34574 | 2024-10-30 04:44:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 127ed31c-f719-3c0d-97fc-2051a77adcf9 | -6.98478 | -41.33062 | 2024-10-30 04:44:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8616a45c-8b2e-3c6c-9159-743cb14e4285 | -6.97874 | -41.3332 | 2024-10-30 04:44:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86e09fae-fb2f-3c5a-9725-9892f18617a5 | -6.53812 | -41.56332 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 822cb803-83e4-3eb7-85d9-134d876502cc | -6.53764 | -41.56672 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b1aa43c-2d0a-328f-b836-d067687033d3 | -6.53717 | -41.57013 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bf50bb2-34e9-36cf-a787-9f563eb83548 | -6.53315 | -41.55903 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1fb75798-e945-30b2-bf87-434b11d6d8b5 | -6.53267 | -41.5625 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9644c1b8-8cb1-3d48-aa20-4516147a452c | -6.53171 | -41.5694 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5514f60-914c-341b-a4f8-774f04841779 | -6.52722 | -41.56167 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd293942-d082-3e22-b795-71585912532d | -3.44858 | -42.00449 | 2024-10-30 04:44:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b47c67f-7f62-3f8f-a42d-06c2b8570b29 | -3.44815 | -42.0074 | 2024-10-30 04:44:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed80d5a0-d577-392d-8002-2534f0da1d34 | -3.40237 | -41.62894 | 2024-10-30 04:44:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f8462f5-a63c-3389-892c-468d00951488 | -3.40192 | -41.63203 | 2024-10-30 04:44:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40d70a83-671c-369a-8609-422a66f83df3 | -3.3972 | -41.62806 | 2024-10-30 04:44:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b3570fc8-136a-3a53-92d9-c240e1a0746e | -3.22087 | -42.69633 | 2024-10-30 04:44:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e18bfe1f-8756-3613-968f-e9f5e1f467b3 | -4.52584 | -42.05721 | 2024-10-30 04:44:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 073755c9-d215-32ea-81ae-c04c27984556 | -4.52072 | -42.05647 | 2024-10-30 04:44:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1242aa7-73e8-37f0-acf1-c0c7fb454d4e | -4.51095 | -43.13108 | 2024-10-30 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae15f0b5-7b6f-3364-8ea2-0b7048452bd6 | -3.93931 | -41.4966 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98d4779f-2b10-3e42-829a-2d11f10016db | -3.93885 | -41.49982 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3e84964-af15-30bd-86b4-51da25626e9e | -3.93838 | -41.50306 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 985eba0a-ed65-3c03-a1a2-23f8442c5a83 | -3.93682 | -41.48662 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f38108fd-75c2-37b3-8654-da94dd85fe57 | -3.93633 | -41.48983 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc2b2a91-c30c-30d6-9112-768ec688e0f7 | -3.93584 | -41.49306 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3944a777-bb95-34e9-8e48-2043f984a118 | -3.93542 | -41.48615 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85f39a88-f71a-35ac-ba7a-4dfdc58f1fda | -3.93536 | -41.49628 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ddbba01-ea70-38d9-bdaa-48a19ef647e7 | -3.93496 | -41.48937 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 059c7b70-a7bc-3de5-9f0d-bfc73428e09e | -3.9345 | -41.4926 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 08edccfc-1016-3801-ae1f-c38d8203d34f | -3.93154 | -41.48584 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0be7fd0-a292-34d2-9aef-50e24b0f83a2 | -3.93105 | -41.48905 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 72cbede2-a8d8-3c55-9d50-4b9ff7d0d87a | -3.93056 | -41.49229 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c047542f-6d9d-3402-87c6-d408b77e23f4 | -3.93014 | -41.48536 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c6dbd04-5877-3e6d-b65d-26f736bb340f | -3.92968 | -41.48857 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b190f2c2-4935-3d97-a8ff-3382bb10603a | -3.7848 | -41.60514 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f29576a7-2e41-3f05-b518-59dcadd0c7d7 | -3.78433 | -41.60823 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77e54d80-e8a6-36c1-8efc-0256157b8b2e | -3.7791 | -41.6075 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 082a39df-4660-3685-aeb2-ebc8bbc3e5a2 | -4.85708 | -42.47697 | 2024-10-30 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74b2271b-96a0-3981-a31e-03ad8c9ce912 | -4.85289 | -42.47042 | 2024-10-30 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0c993bea-357d-37b5-91e7-26e35cbdf4f9 | -4.85285 | -42.47573 | 2024-10-30 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 67523ca1-b4ec-3a1e-a9f8-a756512d4a30 | -4.85208 | -42.4762 | 2024-10-30 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dbc49419-75ee-396b-be77-57fb37bc07ba | -4.93663 | -43.18531 | 2024-10-30 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43fae7e5-d047-312d-b18a-5a68a908dd7a | -4.93187 | -43.18461 | 2024-10-30 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 714f223d-d2c2-3960-96b7-b78b59fe2d5d | -4.93111 | -43.18974 | 2024-10-30 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8251da24-100d-35c5-b4e5-2e3402689029 | -6.42056 | -42.09605 | 2024-10-30 04:44:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 65b2febc-9b65-3e28-8ced-bb62251f08cd | -6.42015 | -42.09902 | 2024-10-30 04:44:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e040b464-1842-3890-8b01-3731227e3873 | -6.41974 | -42.10197 | 2024-10-30 04:44:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e2f25618-ee42-356e-8d77-e2cbc94f4b28 | -6.41491 | -42.0981 | 2024-10-30 04:44:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 305ada8d-b007-3f14-bb29-7a0ccb825f06 | -6.41451 | -42.10101 | 2024-10-30 04:44:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 75985290-4c4f-3ba3-ab58-e47fb3e353a4 | -6.17309 | -43.18118 | 2024-10-30 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 914c6f42-3899-35dd-a5ba-45572f27f119 | -6.05949 | -42.65282 | 2024-10-30 04:44:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9e789e2d-4ae6-387c-b9d7-1cd3596cde9e | -5.36515 | -42.66594 | 2024-10-30 04:44:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2caddbfc-bab4-39d7-9cdc-7d27d8d7ab5a | -6.32969 | -43.44927 | 2024-10-30 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f18833c-fe31-3068-895c-9a51537ae6a3 | -6.32935 | -43.45172 | 2024-10-30 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30571f2b-28c7-3ed8-9d5c-ef5ec89fc0bc | -6.32488 | -43.44874 | 2024-10-30 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88559a50-25f6-3ec9-b7cc-1673cf8a6c1f | -6.32455 | -43.45119 | 2024-10-30 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1e8d482-067c-3d6f-a018-5195810b8e27 | -6.21277 | -43.28407 | 2024-10-30 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 065b7961-7291-3a10-8713-1061fdb64979 | -5.45877 | -43.17587 | 2024-10-30 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6ca0e87-cd02-3b6b-af12-e949630eb914 | -5.45801 | -43.18109 | 2024-10-30 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7838c040-745b-3153-a6f0-eb5e53e17181 | -5.30864 | -43.07475 | 2024-10-30 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 005b204d-8dba-30b4-b748-cc833f4a3fe9 | -5.30729 | -43.07592 | 2024-10-30 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84f13925-0058-3931-bf64-c0d4b588b3ae | -7.92457 | -42.83865 | 2024-10-30 04:44:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbeb0ece-5772-302b-8943-4e29246bb673 | -7.92415 | -42.84174 | 2024-10-30 04:44:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3def7270-dfe5-3f07-89d5-58e31d6ba902 | -7.91943 | -42.83813 | 2024-10-30 04:44:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 51960409-596c-35f7-a735-0952d4b51a8a | -7.91901 | -42.84125 | 2024-10-30 04:44:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| da688385-4214-36fa-874d-5fc7f8f2fda1 | -7.34182 | -43.55209 | 2024-10-30 04:44:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 76853979-5e1f-37f4-8ea5-d569a0e804f4 | -7.01401 | -43.02563 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a75eb3a7-9106-3004-a789-377dd23c2532 | -6.97121 | -42.43346 | 2024-10-30 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41d752d0-7800-3814-a404-022c003105bc | -6.97079 | -42.43648 | 2024-10-30 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9506e0cf-ee78-37d5-83ff-6b3bc9f821a4 | -6.84536 | -42.81849 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d88c180-90a2-384c-9601-f1d8812bd530 | -6.8452 | -42.81476 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc336bf0-c11c-37ed-8f13-659e23ffb481 | -6.84441 | -42.82056 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91d95938-75ae-33b6-a872-802887d1f37a | -6.84117 | -42.81194 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 74b536a1-960d-31ef-9877-08664724eeae | -6.84116 | -42.80677 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d616fd91-17b7-36db-94ec-7d830b09b4b7 | -6.84077 | -42.80963 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b5ad267-ec9f-3c8a-91f3-35f185390fe5 | -6.84018 | -42.81396 | 2024-10-30 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7cb0151d-2260-3f4c-a42c-8b7b0eb7327a | -7.32331 | -43.25736 | 2024-10-30 04:44:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7f9e7e3-d3c1-37dd-8416-ca0e753f111c | -6.63978 | -42.82962 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e91a9b5e-2711-38d0-a517-c94cb3081340 | -6.63596 | -42.8222 | 2024-10-30 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7f23b1f3-bd58-363c-a01d-d2a782050499 | -6.63559 | -42.82293 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c34f9783-fbb1-3807-bf9f-abf6d58c791a | -6.63509 | -42.82816 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 175fd620-3977-3bac-b9df-7f8b5ba7d031 | -6.63477 | -42.82887 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1b5abba1-2b00-3ee2-a874-578e9db4e088 | -6.47415 | -43.14188 | 2024-10-30 04:44:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a62dc9bd-561f-371d-80ec-492767319dfe | -6.47261 | -43.1407 | 2024-10-30 04:44:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9816e816-7fb0-3700-8d9d-45236f80465a | -3.42145 | -44.45301 | 2024-10-30 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README71.md)
