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

## Dados Diários - Página 268

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba9b53b2-ee69-3bb8-bd68-cffd5b23bb08 | -7.29756 | -44.01867 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 259c297a-cf8c-34d8-951b-db8755c11f82 | -7.20833 | -44.34209 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd2ec3f3-ee41-3320-9811-6d0e8486d636 | -5.51536 | -43.06364 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f74ea12-cd40-321b-a16a-5ea147534e54 | -7.321 | -43.98252 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 054b48d6-1160-3bc5-8f61-8bde68f32680 | -6.81978 | -44.12766 | 2026-10-09 16:01:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d733f27c-a85c-3f59-9d49-fa23361858be | -10.87895 | -45.53168 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| adaaa1df-8d4e-33fa-9d4f-6b673cdc7ab5 | -10.49247 | -47.2101 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 3e4a3f91-1fc6-3946-8034-3e8b7c46d467 | -10.44696 | -47.8575 | 2026-10-09 16:01:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d71ec182-4b6d-32ff-8ce3-3f8aef59b72f | -7.00925 | -47.67938 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d10c447c-3cd1-3ffa-bfcb-c4606dc7c9d4 | -11.19396 | -45.29308 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 292f798c-1006-32dc-8e43-e8cc11029a8f | -9.89879 | -44.83925 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4dd675c2-8939-3ef9-a259-343dc981021d | -9.22082 | -45.65858 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ae293a2-a6fc-39fb-972e-7c68ad50e631 | -6.59232 | -44.2954 | 2026-10-09 16:01:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d94985b-414f-3125-9da4-54dcab2daa5e | -11.04768 | -44.05813 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4bce5dc1-2936-35a7-a16c-6c2a0f8a9c21 | -11.04081 | -44.05044 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 35973875-c022-33a0-be07-1663230d2aef | -7.48177 | -42.84193 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b7a5fcea-ac4e-3478-8caa-12b05f1d59d4 | -11.24953 | -46.25308 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e42ffc74-a723-34c3-950a-ec191b42e099 | -5.96193 | -40.91345 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ef29f38b-c816-32f0-9eba-9c5acf5d4c0f | -4.98879 | -43.15763 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 44f0a987-0f6c-38c7-ba8c-53b331c0341e | -7.4834 | -42.85406 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| c6124d57-7776-39ab-8ed7-ab717f6ec8df | -5.71052 | -41.663 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ed7d61fd-47f1-3a56-8fe6-6478cc360d5c | -10.47202 | -47.25973 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b2ce3343-c665-3bd4-8d69-34cf3a9b49aa | -5.82022 | -42.62484 | 2026-10-09 16:01:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8cf04aa6-11d0-3565-9115-6d9c35d57161 | -5.71077 | -41.76562 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 873fff90-463d-393f-8034-320ebd96ca80 | -6.00393 | -40.95505 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f21db1d9-d338-3e69-940f-72d6b07f3d5e | -6.85763 | -41.75898 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 05fe1a75-0424-354a-8594-1af3ea6db8ec | -8.66185 | -44.87936 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a2a7a5eb-e2d0-3eda-b548-0f12901a5fac | -8.36535 | -44.20082 | 2026-10-09 16:01:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e84adc14-3569-35d1-a966-52993032ad32 | -9.93774 | -44.79415 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2043d645-82e1-36a0-a4ed-2a75f2de2947 | -7.79422 | -44.57281 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1f5f0ef7-d3b8-3404-b153-e154d0ee1da8 | -5.496 | -40.5447 | 2026-10-09 16:01:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7539d88f-3c72-302e-8fe5-1044264bf3ee | -5.9725 | -42.84604 | 2026-10-09 16:01:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 171f0321-7120-3ceb-93ed-38f141153a48 | -6.88178 | -45.03382 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 365fb001-4256-3a5b-981c-1ea83601c3cd | -10.50736 | -47.21515 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3e865be7-9d74-3e36-83d9-8787d166efa8 | -5.08066 | -36.93766 | 2026-10-09 16:01:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 834.8 |
| 45a2469b-67b4-3ac5-9784-f54d8e13ae5d | -10.44888 | -47.30647 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e3c9f46d-fa62-3516-b02b-a9ba0ace7258 | -10.86141 | -45.53508 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dccff4bb-538f-3cea-9158-b0b1329b82fc | -10.87286 | -45.52146 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| d0cf2fd8-5ffc-3286-bd6d-a5ac38bd208d | -6.01154 | -40.97618 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| eeec0aa1-d4fe-3e35-9cf0-0c0ee977e4c7 | -7.29831 | -44.01914 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 20550e28-8a59-3751-8cfa-d8a0da873a96 | -7.13289 | -41.8131 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 24e3a307-ea8d-347b-bf5b-9ccef039d0e2 | -5.49973 | -43.06276 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 155edc83-0ebd-39c6-aaa5-cdde83e7609a | -5.36271 | -43.19991 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93281107-15c6-320d-9b7f-8cb39832c7bb | -9.98795 | -45.94191 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bc1cd817-78a4-324c-a460-78460df938de | -9.22372 | -45.65773 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d8a1495-7f32-3d9f-900a-d77c17838983 | -5.50521 | -43.06495 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4c25cbd-20fa-3f96-9e99-2a2c7d20f864 | -6.85289 | -41.75953 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| e384b0d4-f517-331b-b530-3f142b284ee1 | -10.87166 | -45.52527 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 83c23da4-8306-3d21-83b7-c4fa608860b2 | -5.6694 | -43.62765 | 2026-10-09 16:01:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ceb75e2f-b1d3-37ca-a1c4-f50daa367a04 | -10.3095 | -46.28146 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9cdee58a-3c16-3006-a52f-1ca285971eec | -7.49206 | -42.84057 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| dec92fc5-0648-3a74-8302-d52b4513c8cf | -9.98667 | -45.93105 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 46bea69e-b911-3a45-a776-a7798b967fe3 | -7.24296 | -43.74148 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cddfb157-11b6-3796-8bfb-5b523bcd65b0 | -6.15175 | -47.92387 | 2026-10-09 16:01:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 60afe0d8-e6d0-36b2-923c-d23300dc4835 | -6.83378 | -39.39256 | 2026-10-09 16:01:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c9716edb-47a3-336f-b420-38a4b001e7e7 | -7.19648 | -44.3398 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b17d5fd-669e-3c28-87a7-1beecbb9a4aa | -9.09589 | -45.12875 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6dc4cc62-2b4b-3dfd-ac37-c27b3ab06420 | -10.45708 | -47.19501 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| aa987ad9-100b-3f22-8b31-73377e7a9893 | -9.87074 | -44.86179 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5d9841af-e175-396f-b08c-7744240ce353 | -7.32798 | -43.99245 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5d71cb4-6822-34c0-8334-0d2dd5adc2d9 | -5.20695 | -42.71887 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c9f24e33-6b38-3081-b6fd-3ed39b88ecd3 | -6.58245 | -43.05492 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd135b32-8458-3145-bfcd-604fdde38163 | -11.08875 | -44.0533 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bad22a8d-dcae-3cda-9b6a-543635e107f5 | -10.91749 | -45.51381 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a60659fb-da3c-3da0-acd0-c1ad4cec9dbf | -9.92281 | -44.78544 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 249e57f0-be9d-330f-ade5-6b61bdcd3b66 | -9.88716 | -44.79518 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 569a6533-dcec-3b51-82bc-c343a97eab01 | -9.48584 | -45.55297 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d42b20fb-34be-3c77-9004-0e08c3d96226 | -8.90985 | -45.18077 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 364dab65-91b4-3616-b4e4-cba9a2ece3d1 | -4.54772 | -40.70589 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 7f6acfbe-597c-3724-8fc9-9df223c3822b | -9.92999 | -44.79362 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 806d56e1-34fa-39d5-9a26-175d66510137 | -11.11712 | -43.99965 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 28eafbf4-4c4c-3e4b-af7d-4473cb098731 | -5.29557 | -42.74002 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7e0b2606-f002-3750-a6bd-f633dcbc88dc | -11.07732 | -44.10598 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 428.6 |
| 4ed2b94e-0291-37c3-9ad6-c141319c1917 | -6.88536 | -43.70322 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1689505d-f5ca-3fb9-99b9-21d0eeff9a2e | -6.84339 | -41.76048 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 734f55c7-1d9e-39ed-a434-61ed3354eea0 | -11.24185 | -46.32257 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 860a0673-6841-3f82-a2e2-c3f32c52cf73 | -6.70162 | -44.12102 | 2026-10-09 16:01:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a2e597f7-bda0-3d7c-8ade-46bec233865b | -9.75334 | -45.69381 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e30ee59b-8b0b-3286-ae07-00542cf10e94 | -7.85972 | -44.96835 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19220bd8-4270-353a-b7a1-e5538e21b11b | -10.82668 | -47.33165 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 37c15db9-c575-34c3-89f1-8bf59aa65ec2 | -4.30854 | -38.10752 | 2026-10-09 16:01:00 | NPP-375 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 66eabb4c-5f02-3694-a0d3-582ea32cdf18 | -10.34592 | -46.22527 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b45d0c2d-a4c8-3db3-be65-d1ca3da60105 | -10.84679 | -47.34919 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 343041d4-f7ff-38bf-8ac9-367a0957532f | -6.96797 | -43.85712 | 2026-10-09 16:01:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f392a1a5-02db-3c05-8bb1-9c6752a13652 | -8.08595 | -45.63994 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 177fa2df-84ef-3562-bdad-99773a06adba | -6.21235 | -37.87427 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 8c877180-5123-35a7-b4df-7dcc2ff39e4f | -9.83208 | -45.78601 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29bd670e-44a2-390b-94ef-ad547f3d329b | -5.98891 | -41.35836 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bb1db21f-2cc5-34d7-b307-59f33fce3589 | -6.48242 | -42.70372 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| c607f720-98e9-369f-9dc2-eb922997a9d9 | -7.29708 | -44.01501 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 5fed03f6-a7fc-3e30-aa68-cbc18319f644 | -5.01649 | -38.49702 | 2026-10-09 16:01:00 | NPP-375 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| cf8087e0-5fbd-3d8f-9a48-cdea26256b72 | -6.88125 | -45.02974 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 42813f7a-7154-385a-99b1-654ef7e14a6e | -6.08577 | -44.00327 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c03eb2b8-14a6-307f-8053-31d43eb9b622 | -8.90865 | -45.1715 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bb235e80-6267-3112-b094-fed6131d7629 | -9.92942 | -44.78908 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e2a26a5-826c-3f81-ac6c-3e2dddeef385 | -6.00249 | -40.94736 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 03b8ece8-f3f1-3172-bed3-3bb94e28184b | -8.96942 | -45.89953 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b9bd44c6-37d3-3fd8-b42d-074e585eb311 | -6.70764 | -44.12378 | 2026-10-09 16:01:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d5944594-e7d3-353e-bc2d-da135a3bcb95 | -5.6186 | -43.04058 | 2026-10-09 16:01:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5f4adbf7-0111-33c8-80b8-c7d3a1e8deaa | -9.33579 | -46.46916 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README269.md)
