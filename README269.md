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

## Dados Diários - Página 269

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 051ece27-3fcf-385a-b08d-0efdce5c3814 | -10.50651 | -47.20783 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0569ec6f-b230-3bfd-b6c0-bc044dcddf13 | -8.98976 | -45.95763 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c3b150c7-a4a3-3703-af5b-cb878c587881 | -5.45891 | -42.36988 | 2026-10-09 16:01:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 78dd7a2d-b5ab-39df-b58c-fb95420b0114 | -8.32246 | -45.4506 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 927e352d-ce72-3470-ab65-c5b0fdb3b1f9 | -6.81886 | -39.54625 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c089a355-cb88-3e3d-beb7-cac868d4ba4d | -9.01507 | -45.12563 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e3872525-1812-3bca-a128-2befb2929088 | -10.45307 | -47.3049 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 895193c0-fc52-3f26-ba74-6ef54a3262af | -6.09576 | -35.6996 | 2026-10-09 16:01:00 | NPP-375 | SERRA CAIADA | RIO GRANDE DO NORTE | Brasil | 2410306 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| be41f64d-e1a5-3eeb-8dde-4f16411e535e | -11.06607 | -44.11161 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 96a71c32-400c-3ade-8e9a-c0b6619be363 | -11.19965 | -45.23178 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f11424d-fbb9-3de2-b48c-b3ac8b7ed2d6 | -5.98831 | -41.38701 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9f83d29b-5eba-3b14-9245-02408f41d43a | -5.49678 | -42.86167 | 2026-10-09 16:01:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c294316e-b615-3330-b540-f91a682bfc81 | -10.84252 | -47.34372 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6cb2760d-8122-3531-8f68-3b71832e4c3d | -8.32943 | -45.01767 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e7fcfe2f-0fc1-3296-ae2d-90809abad1f4 | -8.66557 | -44.88251 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6b3375dd-6861-3171-a42c-504589f79ecd | -6.95231 | -43.9464 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8376bc3f-9a45-338e-bf1c-48fa6f1e8e30 | -7.14109 | -47.56577 | 2026-10-09 16:01:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bdb5a8a-ebac-3a5d-b14d-75c7b8bf85ef | -10.61847 | -43.28245 | 2026-10-09 16:01:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 93e5e8a9-d81e-3cf7-b633-7a7cb751bc36 | -11.0617 | -44.02669 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f2be3ebd-a6b7-35d3-b1c3-aaa6115b713b | -7.07463 | -41.59903 | 2026-10-09 16:01:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e4b2d71e-e8d0-3a6a-9b43-bdcad47024ae | -5.8172 | -43.26889 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7562060-182e-3431-8746-09a549fa52a9 | -9.82067 | -45.74426 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4575c834-4e7a-31d1-bf50-6d669d8abd4a | -10.33925 | -46.22582 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 835b2780-bdfc-3015-9ef9-c20bd23c62b2 | -6.13203 | -42.88942 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 7b4539ae-0065-3e8b-b892-4c39970990c5 | -11.06658 | -44.11585 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 9b613149-b428-3c46-bd13-05fea9d1c2ba | -6.04833 | -42.61861 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a25ec3e0-fcc8-37fd-92d7-770796aaf478 | -5.1298 | -37.08965 | 2026-10-09 16:01:00 | NPP-375 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| add67027-6f7b-3ae4-8887-2a386ee9c37d | -7.93818 | -40.01576 | 2026-10-09 16:01:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2b964eef-4ec0-372b-8847-d7650e9305da | -11.07093 | -44.10246 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 1de5b2ea-b391-3754-8bc3-e4daf2a05d86 | -9.98924 | -45.94482 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7b8e757-740b-3ab8-b701-9a15635ddd85 | -7.0832 | -44.04396 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1abc1d65-c60c-3bf6-8a69-0ea1e29b868f | -5.99022 | -41.36765 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| baa1819d-49f5-3562-9f12-a0ff4318252e | -7.59943 | -47.04249 | 2026-10-09 16:01:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2aa69a77-ce64-302e-98f5-b1c530a3e707 | -9.32045 | -46.45408 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41fe6a32-7a71-3807-a98a-e3fa02da7f90 | -7.70802 | -44.72979 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 006b5bff-047e-3022-ab28-8d40cef88747 | -8.90424 | -45.23409 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 692b56ed-f13f-3ce1-998f-bbe78df3c060 | -5.95519 | -39.38617 | 2026-10-09 16:01:00 | NPP-375 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bec5dbf2-fbee-391b-bca0-3b9af8978628 | -11.07939 | -44.12295 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 22805fc4-1e62-34f1-a23b-7adc13d837ce | -6.04929 | -35.24233 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5cd889bc-6fa6-391f-a29f-da9ad0d564ca | -10.61247 | -43.27946 | 2026-10-09 16:01:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6952f20b-b9fe-3957-879b-d273c7cd34e9 | -10.96052 | -45.38618 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 111e5ae0-d08a-38eb-bd2c-e37d5c012752 | -10.49951 | -47.33374 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ee794073-7ffc-3fd1-b091-f72989bb2653 | -11.08494 | -44.07078 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8d652962-1cdc-3bb8-a71c-0897cca01a6d | -9.92042 | -44.86425 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3dc3c53d-48d4-33dd-bd73-0eaff9973e2c | -6.05856 | -42.5832 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 8c0dc106-afe1-3861-9015-7f73497519a8 | -8.52696 | -46.89472 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 77ac9bb3-fbe9-34cd-b556-cf66f9e5c35e | -10.47571 | -47.25122 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 90658167-bbf2-3d02-a874-b5a952d2b45c | -11.07991 | -44.12722 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e1558645-080d-3db6-be3a-495377f56d74 | -9.08032 | -45.10393 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 74d13d01-1423-3c10-ae48-8b5c1065975a | -4.91616 | -40.374 | 2026-10-09 16:01:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5933421f-5060-356d-ae28-0d4e28ebc70b | -11.06761 | -44.12436 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ad44a40b-cf35-39ea-b36a-876badb80149 | -6.89041 | -44.90481 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a07bdcf6-916f-3f14-b744-780a074601b2 | -9.9919 | -45.9753 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ab75a0c-032d-3e9c-bc94-17eb3322061c | -9.93724 | -44.80219 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e10e1c73-fbee-30e9-9559-9bec100d6e0a | -9.93377 | -43.57033 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 09fe5d96-b83a-3f5a-abe4-65f0efc30c02 | -11.06018 | -44.11233 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| ae000739-9134-3c24-8a6c-16e02f24417d | -10.46142 | -47.29109 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 254ac142-d716-3c22-a379-5460bac09a09 | -5.53032 | -39.85157 | 2026-10-09 16:01:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0e48b2c1-69ba-3d31-83a6-350072953434 | -10.61758 | -43.27522 | 2026-10-09 16:01:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 19b78c40-925f-3b72-b9b8-60e9570f0958 | -6.88505 | -44.90915 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ebc96faf-a181-30ab-a0fa-a0ffc489e593 | -10.50028 | -47.34044 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a12a1e26-006b-3f1e-b83c-58438c79009a | -11.24113 | -46.3163 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 63857775-2302-3d2c-816b-1af2b077b779 | -11.08321 | -44.10527 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 66f16941-e6cd-351f-ae01-5721e3e8b37a | -10.88146 | -45.53964 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2e2f1a9f-5d3f-3e34-b868-9a384f305492 | -11.41625 | -46.69001 | 2026-10-09 16:01:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| acb69969-ea49-3655-ac54-860e3d2f672b | -11.25732 | -45.17836 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 786721ee-d4f4-3eb7-ac1e-018b555d6792 | -9.09857 | -45.1498 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2ebf2ebc-d080-3170-9df2-92195a7913be | -10.39782 | -42.57323 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 989ec52e-0985-30b5-98db-68993b795ce1 | -5.50742 | -43.04415 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93f9ddac-ae96-30e7-ba9d-a39f467052f5 | -11.20783 | -44.87571 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c444dd3-3d43-310f-8a94-256af6b60298 | -11.34112 | -46.64449 | 2026-10-09 16:01:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5fad949e-200e-3a82-a434-37f2546e639d | -6.2868 | -43.8769 | 2026-10-09 16:01:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3af0b1f-1ec6-3c4b-aed7-0ad53ce647a9 | -9.10277 | -45.13394 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a3abcecf-07cc-3e1e-8369-6f7296fe1828 | -5.62366 | -43.0398 | 2026-10-09 16:01:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 352e00fb-c875-320c-a140-96c6dee0c2f0 | -7.24299 | -39.24567 | 2026-10-09 16:01:00 | NPP-375 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 4a314426-e71a-3589-a5f3-22108342b98a | -5.74529 | -42.0875 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 17010027-1068-359f-9325-8e61301b67fb | -7.74359 | -42.96704 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e5d10eed-7489-3468-913e-705cdf281cb5 | -6.0109 | -40.97185 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| e8a452e1-537e-33a4-9bb8-013397f45062 | -7.29154 | -44.01586 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 2e4be4d9-5104-3365-a153-c03c6f3fd965 | -6.32579 | -43.3601 | 2026-10-09 16:01:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 621dd780-65e9-3f42-bc01-59d74ed8049e | -11.42867 | -46.67626 | 2026-10-09 16:01:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1a012167-0fe3-3f2b-8d9d-86b8a019a754 | -6.31299 | -43.61616 | 2026-10-09 16:01:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 84cd0671-4157-3de3-b977-1b75d35dbf17 | -9.93796 | -43.55854 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 0c919e3a-96ba-3220-b3a6-65dcfcc146b9 | -9.0216 | -44.36605 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1b2cf831-07b1-3708-b5d7-7225cfe397e3 | -6.00647 | -40.97235 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 4dbfabcb-6fae-390f-997c-42692e3b24e5 | -11.05967 | -44.1081 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 551d07cc-7d5e-30f4-80b9-02913800e79d | -7.05166 | -45.43095 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 75461cd1-1780-3c60-868f-42a4c375af08 | -7.06797 | -40.95066 | 2026-10-09 16:01:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 70ca8f7e-f5b5-3156-bcd1-07c7c48d43d0 | -5.51772 | -43.99125 | 2026-10-09 16:01:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dda243b8-f6ef-3950-aa2b-b27eddffc5c7 | -7.00479 | -47.69932 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| de4ac705-d2f0-3ffe-8357-eef2410c1ef9 | -11.08424 | -44.11375 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5adc7e2-8983-36a9-9ee5-b188a1867cfb | -5.50236 | -43.04487 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f512b8ed-1c34-32db-808f-2d4f28f0729d | -5.33825 | -42.93224 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d11ae23-d3ae-39e0-9a86-a9d59ad2fd10 | -10.05503 | -45.89503 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 189ffcd3-7cc9-392c-a332-d7fe590d047c | -8.97686 | -45.95901 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 0afb0f89-6a9f-3678-8bbd-c2cca9a34bd7 | -9.01663 | -44.37253 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ab49f212-585f-3d35-949e-1f70d2d1ef70 | -10.99599 | -45.40028 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 021bbe93-168f-3b4c-bfc1-f6483a5c38ae | -9.58555 | -42.11975 | 2026-10-09 16:01:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e103acc7-c1b8-327e-a6bb-d273458eb18f | -4.58457 | -40.66861 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| fe42dfc7-58b4-3524-a9b0-bc0bf6ac8cbb | -6.01217 | -40.98051 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README270.md)
