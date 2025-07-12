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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5641353a-79c6-3cf6-9a21-a9a64b81f986 | -3.4096 | -43.367298 | 2025-07-12 00:24:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb03e402-8208-3a12-8c46-0b9052edfaf4 | -4.2773 | -46.936001 | 2025-07-12 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2433ec52-9155-3f67-a2f2-94dc27c5bec2 | -10.8497 | -49.102699 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c020fbe6-2629-381c-89b5-bfcadc5ba769 | -6.8752 | -42.781399 | 2025-07-12 00:24:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 475874a2-8a40-3caa-986c-aded382e7658 | -11.7329 | -47.4702 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e92577e8-5029-36b0-9004-907a1b4fe385 | -10.5685 | -49.123001 | 2025-07-12 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d1310e7-97f2-3cf0-903c-9b11096b5517 | -8.4611 | -49.627499 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 383491e0-68fd-3ef6-88c0-922dd5ae11f0 | -11.8316 | -47.501499 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd149f4d-4986-31f3-8d06-768adec69c1d | -7.4629 | -47.527302 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac26214-4c2a-34aa-8fe7-53c8a9d5221d | -12.418 | -43.484798 | 2025-07-12 00:24:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c48825e-d9a0-33a2-b48a-c0f2cb9d7abd | -4.6073 | -43.326698 | 2025-07-12 00:24:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0de32cb-c372-3bad-91fd-0273e22ea016 | -7.2287 | -43.105999 | 2025-07-12 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7da8b58e-57ea-35a5-a0f8-c654eee00f43 | -10.6591 | -49.509399 | 2025-07-12 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d54a6af4-e6a6-316e-ac32-cdc99783185a | -8.4708 | -49.6255 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78b1c798-5631-36d3-8a06-747d0b720ae3 | -7.2173 | -43.101299 | 2025-07-12 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 853282a0-486f-3944-a356-4d723340d153 | -6.854 | -42.778801 | 2025-07-12 00:24:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| acc8d5e5-1253-3782-ba2a-97b8a5ccd59a | -12.4196 | -43.491798 | 2025-07-12 00:24:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c998f8d-5bc3-36a9-ba21-446047370329 | -3.3828 | -43.117699 | 2025-07-12 00:24:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46ee3d4a-26a9-3524-a46c-57a2f7190a77 | -11.8973 | -44.897099 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6161eff6-12c2-3ba1-9d1e-31bede6f6b38 | -10.8302 | -49.106701 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6884ee42-deb3-3b18-988a-ffb4349869b4 | -7.9349 | -49.650002 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb1c05b-95e5-363a-8881-e4a08b5fe845 | -3.9995 | -43.241402 | 2025-07-12 00:24:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9b208d8-edf2-353c-91ae-716147636062 | -11.4242 | -46.405201 | 2025-07-12 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6baca80b-711c-3571-a6d6-9c661a115ac0 | -10.6662 | -49.4944 | 2025-07-12 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7897044-a7cd-3776-abd9-97c3ba1053ec | -13.1226 | -47.323502 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6be45e7e-2741-3d6c-8e54-4f8502243125 | -3.3845 | -43.124901 | 2025-07-12 00:24:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba5ec6c-2df0-3f4f-a355-c5660d8a3fb4 | -4.2692 | -48.177299 | 2025-07-12 00:24:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbe920b-3db2-39b0-a5a3-cb2412200adf | -10.8898 | -49.197201 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8acc7cae-76c9-3f47-8dea-8f042c20f4d6 | -12.4089 | -45.3596 | 2025-07-12 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0b087c2-320d-359f-8f58-4064e7e95471 | -4.0077 | -43.232101 | 2025-07-12 00:24:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4ca506c-737e-3377-a362-b3beb3f73d98 | -10.566 | -49.110901 | 2025-07-12 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1a8bd34-cf73-3252-9273-297403157e5a | -10.8924 | -49.209702 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebd73622-13b0-359f-9613-c75f20e56157 | -4.2711 | -48.186001 | 2025-07-12 00:24:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a98781e-f6e3-3009-870e-70b2735503ac | -13.1595 | -47.305 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01f29259-f77e-3ae8-9c0c-25443d37e61f | -11.899 | -44.904598 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39716fb1-f367-30c6-9d6e-604d5c516d1d | -8.4657 | -49.6012 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0c5ab9-1706-32e5-b7ee-8095169fa3a4 | -10.8327 | -49.1189 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b995927d-631c-32fb-9081-693715120db4 | -11.7252 | -47.4823 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3996b139-f425-3010-88ad-f4a62470dd5a | -13.1162 | -47.2929 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7286156a-53ec-3404-aa7c-974dc6afc6d9 | -11.4205 | -46.387901 | 2025-07-12 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4be47c1c-3957-3129-a8c3-50f8dc2691be | -12.6031 | -48.364899 | 2025-07-12 00:24:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19494765-1b56-3fc0-80fb-08f68c18ab41 | -13.1574 | -47.2948 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95beb81c-901e-395c-992d-5ada64bf7297 | -7.9886 | -46.420601 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 467a4987-574a-300a-812e-a953464d23e4 | -11.9392 | -49.2999 | 2025-07-12 00:24:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ecdc2a8-38cc-3a91-b66d-3b267c02ca0b | -10.8548 | -49.127201 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9db7086c-94cb-336f-92c9-7d68fe61a51c | -11.4224 | -46.396599 | 2025-07-12 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a60ce75-4e15-31d5-96ed-7401c2064595 | -12.417 | -45.349499 | 2025-07-12 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd2dab74-db2a-33e1-8c03-150560b2350e | -3.7518 | -47.1161 | 2025-07-12 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43246713-9ddb-3acd-a83b-44074a23eafb | -11.721 | -47.462299 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 940618a9-066a-36c8-aac3-d27fdcbe57c0 | -7.4825 | -47.523102 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08355db5-2fd0-37f9-a49b-d51705b4c062 | -7.9869 | -46.412701 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9217626-ffe5-33f0-93bf-4957593f93cf | -6.8523 | -42.771801 | 2025-07-12 00:24:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ae3af3f-b9c1-3fa3-84cb-153a5bc86a4d | -4.5364 | -38.6777 | 2025-07-12 00:24:00 | METOP-C | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d643bc01-4701-3d7b-8a39-a83af69b95c1 | -13.1302 | -47.311199 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 565070fe-043e-3e27-8da9-24f598eaee27 | -10.9021 | -49.207699 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1126dc8-29ee-37a0-969d-1f93eb2ee361 | -7.9851 | -46.4048 | 2025-07-12 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abf153e9-3a62-3281-8ecc-2f917991bcba | -3.3862 | -43.132099 | 2025-07-12 00:24:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f49fd316-1101-34f2-9833-585d697a6b9f | -3.7501 | -47.108501 | 2025-07-12 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a754ef-3ad7-3144-90f6-1d907f284005 | -10.7963 | -49.631001 | 2025-07-12 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d4bbbd1-f9d9-387a-ab26-7f5bf3eafdbf | -10.571 | -49.135101 | 2025-07-12 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 241e4bdc-f551-3524-899c-e93c60ff7af5 | -9.85521 | -47.87165 | 2025-07-12 00:24:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7e220b48-589b-3308-94c7-520a2cdd591a | -10.90397 | -49.2026 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 748fb677-761d-354a-8878-7113678a1714 | -5.83973 | -48.39758 | 2025-07-12 00:24:00 | TERRA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| cf5b0f78-601c-3f8b-bc58-674c544ed9a9 | -11.94578 | -49.29795 | 2025-07-12 00:24:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 38d4a86d-8be8-3bb5-bd1f-65da98a89f9b | -8.91657 | -47.347 | 2025-07-12 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 63959a3e-deeb-349d-869d-33853ade8349 | -13.68223 | -44.27711 | 2025-07-12 00:24:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99ce9b65-3acf-3b9a-9307-9339e027adf7 | -12.42137 | -43.49905 | 2025-07-12 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6a0ca2e-d1c7-3a00-bdd8-2e6803d6905e | -7.94886 | -49.65837 | 2025-07-12 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bf1c331f-dcf9-344e-bf3f-60e68a4d2ee1 | -11.72115 | -47.46914 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 31c1b7b4-2ebf-3a1e-9d07-407dc76188a1 | -7.46815 | -47.51874 | 2025-07-12 00:24:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2185b01f-d861-383d-8d36-20eedb838abc | -10.57384 | -49.11844 | 2025-07-12 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b36ca8d9-e464-33cd-8f76-74901717db4b | -10.57561 | -49.13263 | 2025-07-12 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 8ccb621f-eaeb-37b3-b052-aee757b040a7 | -11.73103 | -47.46776 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 0edf0080-fd7b-3572-b1b3-d789cb0b7224 | -7.95066 | -49.65179 | 2025-07-12 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| d758cd5d-6651-3476-9782-1522bd8c6e7f | -10.9058 | -49.217 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| a8950d27-145a-3ae2-a250-ff437ffd4c4c | -12.03891 | -48.7607 | 2025-07-12 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2f42718a-7b4f-3db2-ae70-eae712d261c9 | -10.79949 | -49.63926 | 2025-07-12 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d2142688-905e-3eea-a9c6-e7eb54f2821e | -10.89473 | -49.21854 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e6042d79-bd2f-344a-a526-569591efedec | -10.84718 | -49.10743 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 960cd927-c7aa-388b-b0e3-3968d216afe9 | -13.00268 | -46.27474 | 2025-07-12 00:24:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1f2d25a6-ee84-3568-b2d0-852c1d35a2e8 | -12.42008 | -43.48992 | 2025-07-12 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 51f63113-3a65-3d88-a08f-ea83293a2ce1 | -7.47892 | -47.52751 | 2025-07-12 00:24:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3cdbf627-492c-34a9-902b-fdbe1766f8ca | -11.93478 | -51.70095 | 2025-07-12 00:24:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 56a0e9a2-f2f2-3f4b-876c-ad1332aedf57 | -11.72258 | -47.48043 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fa24915b-a1d3-310e-a92e-5b001e661e97 | -7.99142 | -46.42599 | 2025-07-12 00:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e312dd1d-a333-3cf2-a27c-b9548a7ea0c9 | -13.12834 | -47.31606 | 2025-07-12 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 630d602b-d806-309a-8c83-e2302ff2d7c5 | -7.99669 | -46.39699 | 2025-07-12 00:24:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05c3d364-7d5c-337b-b60d-bdd11ab54ad1 | -12.41035 | -45.35243 | 2025-07-12 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 23660477-78a1-3cab-b0fe-b1da7cda519d | -7.99017 | -46.41672 | 2025-07-12 00:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 727efe02-e429-35ee-acae-0952d2e5a7e1 | -7.47619 | -47.50739 | 2025-07-12 00:24:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 22fa70c9-9a2a-3dc1-97ca-930a3478f2e2 | -13.00405 | -46.28508 | 2025-07-12 00:24:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 083a83b4-78ba-3b50-820e-973417a472f2 | -11.89714 | -44.89654 | 2025-07-12 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c1403184-7929-3506-a06e-f0080c0d9dcc | -12.46596 | -46.90837 | 2025-07-12 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e15726b5-4e00-35ca-9793-4a9ec9d23ea2 | -13.12666 | -47.3031 | 2025-07-12 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fbed548b-fc28-3377-b193-ba44eec2dbca | -12.41896 | -47.50897 | 2025-07-12 00:24:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4b32ba57-0003-3e63-9453-12b8f5be576f | -11.94517 | -49.28884 | 2025-07-12 00:24:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a166e27e-5234-384a-84a8-85227d07d252 | -13.16654 | -47.29326 | 2025-07-12 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d252088-5c15-3765-91c2-286b360d77b8 | -13.12516 | -47.2914 | 2025-07-12 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| da424dbc-eec5-3f40-ba63-2c3cb3ba6d0c | -10.3759 | -47.55989 | 2025-07-12 00:24:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c57c116a-21d0-3bb0-a51a-36d4d4e0707e | -7.47755 | -47.51743 | 2025-07-12 00:24:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 292.8 |


[Clique aqui para ver as próximas entradas](README3.md)
