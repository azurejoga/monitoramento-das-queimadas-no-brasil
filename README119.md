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
| c4b2e031-9ff5-3ce0-8d5d-2aaa9b836410 | -5.4734 | -43.2646 | 2024-11-09 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d0c9a6a1-1b9b-3c48-803f-6d608d688cf3 | -5.4544 | -43.2893 | 2024-11-09 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| cb2f3644-2450-3e0d-8fef-cdb13380c4f2 | -4.4491 | -48.1712 | 2024-11-09 13:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 43a1e681-5105-3be4-860a-b3ad82c854c7 | -3.525 | -44.0286 | 2024-11-09 13:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 67c1746b-9d9b-33cb-998a-afda82dd491f | -4.807 | -44.7606 | 2024-11-09 13:00:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| aed62682-831a-33ec-912c-f42d64e5bf26 | -3.9483 | -48.1724 | 2024-11-09 13:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a8804866-c063-39cb-97ae-37ebae1f17bb | -2.4104 | -48.5265 | 2024-11-09 13:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4224bed3-8bc1-33a3-b5d8-9d5c4e88ba41 | -5.4546 | -43.2659 | 2024-11-09 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 277.7 |
| f29d9680-001d-3239-917b-49b34d09f00e | -6.9613 | -42.8108 | 2024-11-09 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| ce9c926c-3a13-3942-9666-389e581d9c89 | -2.2804 | -48.7226 | 2024-11-09 13:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 54c0f483-2fe2-3e66-9548-6507b1afbcd2 | -1.5164 | -52.1696 | 2024-11-09 13:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 147f57a3-679a-3aaf-a5c0-056369127e25 | -5.4359 | -43.2673 | 2024-11-09 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d0698864-86bd-37ed-bafc-b1f2a27f5466 | -2.3604 | -46.8776 | 2024-11-09 13:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c4f5ec7c-0f8d-3f94-8963-daad2d91f9cd | -4.8068 | -44.7834 | 2024-11-09 13:00:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 0b727a42-0a38-3d5e-90a7-e7aeb6d32a14 | -2.4365 | -46.3241 | 2024-11-09 13:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 5aff5937-fd65-3234-a252-4aeb19389cfa | -3.9669 | -48.1716 | 2024-11-09 13:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 6c3598cd-f9e1-3d07-84cb-6235569fd24d | -0.2299 | -51.6455 | 2024-11-09 13:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c1b8d783-1761-3fcb-a01d-d4650b364f7e | -2.455 | -46.3235 | 2024-11-09 13:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 7f56c919-4187-33e1-b5da-c8dad2ec5a5e | -6.1838 | -45.4371 | 2024-11-09 13:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8c012e04-8f9f-387f-a097-5a9fc54433f9 | -1.3838 | -54.6373 | 2024-11-09 13:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5b7d4d32-f5b6-3a34-82be-e40277157f3c | -5.4548 | -43.2426 | 2024-11-09 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 97e393db-86f8-3045-9557-df199754c45b | -3.5462 | -43.5663 | 2024-11-09 13:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b64bbcdb-cf5c-3986-bc83-d638ac8a2c16 | -2.2295 | -53.7631 | 2024-11-09 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 815801be-5785-374a-a2f4-bd90458098c0 | -4.8068 | -44.7834 | 2024-11-09 13:10:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| a1889cd4-f00c-30dd-9334-dfc179daf269 | -6.9424 | -42.8126 | 2024-11-09 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 917973b4-2fae-3ff5-9cfb-d57e879bef42 | -17.6083 | -57.4482 | 2024-11-09 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 83fade1a-f0a6-31f6-a8d4-44cbccdd353e | -2.455 | -46.3235 | 2024-11-09 13:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 0ca93d44-6ee2-3434-abf9-0e7ce5d5fa60 | -3.9669 | -48.1716 | 2024-11-09 13:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 97756cd5-ec76-34ab-ad96-e3747497a415 | -3.5462 | -43.5663 | 2024-11-09 13:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1b0782ad-7e2b-3bdd-9c80-e4e26868b8e0 | -2.379 | -46.8552 | 2024-11-09 13:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f785ec27-776d-34ca-a10f-1e9357bdb65d | -5.4359 | -43.2673 | 2024-11-09 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 90266cf9-59e5-3951-98bf-51176429367f | -2.0478 | -46.0903 | 2024-11-09 13:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| f18b2933-9143-35b2-9ee0-c17e6f277412 | -6.9613 | -42.8108 | 2024-11-09 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 0cecd6c5-19c7-39e5-9b67-ead66ef17313 | -3.2353 | -50.2645 | 2024-11-09 13:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| ac46f687-044c-3d35-8a8c-7fed72bb30ec | -4.807 | -44.7606 | 2024-11-09 13:10:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 69820c5d-f3c9-3bd6-8de6-50832c73cc59 | -2.4551 | -46.3014 | 2024-11-09 13:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 86695104-14e0-3149-b4db-c9ad60964b08 | -1.5347 | -52.1899 | 2024-11-09 13:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 73349c8c-28fd-3e43-9e00-0d197e19de47 | -2.4104 | -48.5265 | 2024-11-09 13:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 8b7bb1ea-e6f3-3584-9ef9-82c2b576daeb | -3.525 | -44.0286 | 2024-11-09 13:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fec46814-a299-30a2-b0fd-9482d94887b4 | -2.4452 | -49.1881 | 2024-11-09 13:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 6347d974-5624-34db-97b9-e53551d9e0ad | -3.6602 | -50.2501 | 2024-11-09 13:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2a87b199-ca16-3b96-9f14-f857c104696d | -3.9483 | -48.1724 | 2024-11-09 13:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 29d5fba5-c3ec-3b46-a6fb-2d56eb76ad8e | -3.2352 | -50.2855 | 2024-11-09 13:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 746eb20a-0e91-32c2-8cd5-e6149494ff1c | -5.4546 | -43.2659 | 2024-11-09 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 1b710bba-6248-3a72-bc63-ec92554afcaf | -5.4544 | -43.2893 | 2024-11-09 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9985860d-b906-3578-a93a-42d5e57ba284 | -5.4548 | -43.2426 | 2024-11-09 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 73f17e46-f60e-3c3e-bdf5-d9824af531b1 | -5.4734 | -43.2646 | 2024-11-09 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 921950e3-4356-33eb-baea-62b9515c0968 | -2.3605 | -46.8557 | 2024-11-09 13:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e3d35fc5-ae37-39af-9cff-ff0b635e52e7 | -1.5164 | -52.1696 | 2024-11-09 13:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 21c88d5c-1041-3824-b088-f54d7b0b35bc | -0.2299 | -51.6455 | 2024-11-09 13:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f2b3661f-22ba-3d35-aa12-6a5e5932f7cd | -2.4105 | -48.505 | 2024-11-09 13:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| a3970f77-c645-3917-9a94-45269b8ee08f | -3.5339 | -42.4449 | 2024-11-09 13:10:00 | GOES-16 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 225.0 |
| d38b128a-8702-305e-8ad7-7a16bb6208cc | -1.5347 | -52.1694 | 2024-11-09 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4bcf751a-ad64-3a84-b0a7-2c2f63f92ab1 | -2.3604 | -46.8776 | 2024-11-09 13:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| e7266f5d-be98-39a9-aa7d-f86d02d56e16 | -7.4474 | -44.7392 | 2024-11-09 13:20:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7cdec56f-8c1b-394e-82f5-e6e910b2fcb7 | -6.9613 | -42.8108 | 2024-11-09 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 9cc473f5-1fee-3348-94d9-1d6f4bcc46ce | -3.9669 | -48.1716 | 2024-11-09 13:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 8c74215a-1f2b-3836-90ea-242fcd34ea43 | -5.4544 | -43.2893 | 2024-11-09 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b0d28760-19f7-39d7-9e6b-c4a9a70b5da2 | -4.8068 | -44.7834 | 2024-11-09 13:20:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 341.8 |
| 1a4d8278-ee43-3a6b-89d5-1e05bc544a21 | -3.125 | -50.1419 | 2024-11-09 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 050ac890-ed57-32f2-b94c-df02f00779e0 | -6.9424 | -42.8126 | 2024-11-09 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 96ad4884-21b5-3afa-8c0c-850ac1ad2221 | -3.5339 | -42.4449 | 2024-11-09 13:20:00 | GOES-16 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 277.1 |
| fb6a6192-3371-377b-ab9d-5ca020496683 | -2.3605 | -46.8557 | 2024-11-09 13:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| e36423fa-3491-31a4-ab1f-26a1cd9e9186 | -2.4104 | -48.5265 | 2024-11-09 13:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 197.0 |
| bb6495f2-a18a-387d-ad41-5f06eb989ceb | -3.0319 | -50.3547 | 2024-11-09 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3b3e5833-1928-3691-81bc-824c17bf1cc3 | -5.4548 | -43.2426 | 2024-11-09 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 22902ac8-18c6-3858-ad4f-a47a1d70d74d | -5.7146 | -43.5261 | 2024-11-09 13:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8edec896-dc94-3fcb-a6c5-d9df7b66ae87 | -2.4365 | -46.3241 | 2024-11-09 13:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4e1c35a6-b919-3e9b-9ccb-e325eb834f88 | -4.1246 | -43.5833 | 2024-11-09 13:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9cdbd277-b250-339e-b09c-2f1d070a4e9c | -2.2479 | -53.7829 | 2024-11-09 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 326.1 |
| 061c56eb-a02d-38db-a8eb-16969056cfd9 | -1.5164 | -52.1491 | 2024-11-09 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e8705111-3eed-3006-ab24-fc1457a7437d | -3.5462 | -43.5663 | 2024-11-09 13:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 768247ed-a8d3-3ee5-bb39-a3004b4767f8 | -1.4144 | -47.6187 | 2024-11-09 13:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 5d11e2f3-a655-3ebc-a222-63898c64f7ff | -5.4359 | -43.2673 | 2024-11-09 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1603432a-d901-3f14-979d-5473d259d029 | -3.525 | -44.0286 | 2024-11-09 13:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 773ae1d4-1bf7-3954-96cb-a8feb62e5e75 | -2.4105 | -48.505 | 2024-11-09 13:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4d89bbf2-2f02-3b32-9c95-711abd28c5e6 | -2.2479 | -53.7627 | 2024-11-09 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| fc86e594-9a6d-3960-9adf-168f9a74c8be | -3.2352 | -50.2855 | 2024-11-09 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ed5fd457-aebe-393b-85eb-eb801ad264e6 | -5.4546 | -43.2659 | 2024-11-09 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 205.1 |
| f25f4d97-e737-39b6-9902-1d81b114cf11 | -2.6758 | -46.7806 | 2024-11-09 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 342c5cff-9747-374b-9dc4-61cdb9f1a04c | -3.9668 | -48.1932 | 2024-11-09 13:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| d849f021-830b-3a4d-b579-f80105b9a8cd | -1.498 | -52.1699 | 2024-11-09 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 05bd9a38-0063-3f70-9993-5d290204aff3 | -2.455 | -46.3235 | 2024-11-09 13:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 171.9 |
| c0fef247-f846-3732-85d8-3421552cbdb0 | -5.7475 | -41.9927 | 2024-11-09 13:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| ae6d4703-4b7d-38a0-9f62-d0c3ec3d9f1c | -3.2353 | -50.2645 | 2024-11-09 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| c8d773b0-d2f2-365a-8fa9-6010c56841e9 | -1.5347 | -52.1899 | 2024-11-09 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 01a0bed8-7392-32b2-a2f2-17774baa7a3c | -1.5164 | -52.1696 | 2024-11-09 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| a7b7507d-1e9f-3679-a4c4-4ae3c7ad9f7c | -2.3555 | -54.7627 | 2024-11-09 13:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c063e14c-8233-3d0f-99df-f74231f1e9d5 | -2.379 | -46.8552 | 2024-11-09 13:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| dcbf9346-9529-39ac-9b4a-1488c561e268 | -4.807 | -44.7606 | 2024-11-09 13:20:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 5ac192ec-d52b-34ea-a08e-c2648fd15fab | -17.6083 | -57.4482 | 2024-11-09 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 64d94a9c-af96-3650-b604-209c4a497295 | -2.4452 | -49.1881 | 2024-11-09 13:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 22ee7b57-be8d-33df-b7bd-5b087fa11afc | -4.2058 | -48.5491 | 2024-11-09 13:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 129ca76a-f7f6-34dc-8681-d00b9e3b6aaa | -2.2295 | -53.7631 | 2024-11-09 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 92546414-1067-34e8-8847-82fd353c2ab1 | -5.4734 | -43.2646 | 2024-11-09 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 30235a08-5cd4-3f87-8abb-f12a799db9af | -2.4551 | -46.3014 | 2024-11-09 13:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1da507c4-888e-30b6-b434-c8f15386ae56 | -2.2295 | -53.7631 | 2024-11-09 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 46d36372-59d9-3134-8922-532dfe923a84 | -2.2479 | -53.7829 | 2024-11-09 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 869574e1-58f9-3c7c-b9b7-1dae1dcc3f11 | -3.9625 | -48.9883 | 2024-11-09 13:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b3c481d7-861c-3df4-b9c1-40ca0a5da710 | -5.7287 | -41.9942 | 2024-11-09 13:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |


[Clique aqui para ver as próximas entradas](README120.md)
