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
| 1624154f-21b0-380e-addb-03002c156e34 | -15.73 | -45.95 | 2024-12-08 11:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 482f63a0-6326-3ec0-87dc-9029945acb34 | -17.4 | -44.88 | 2024-12-08 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee8e54f3-97ba-374e-87b7-ff097dfb08a3 | -7.66043 | -46.85031 | 2024-12-08 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7c1f46ed-ea45-3b65-9832-35b0db1d14c5 | -6.30824 | -46.69273 | 2024-12-08 12:40:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5a96cd58-4a21-3a8c-883a-911a9e7449b3 | -7.70835 | -46.89323 | 2024-12-08 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 00409844-e6b0-31f1-8183-4472ee607a65 | -3.55012 | -45.33692 | 2024-12-08 12:40:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 31f86836-e8bd-3a8e-9610-3f8912e8df4f | -9.18841 | -43.39206 | 2024-12-08 12:40:00 | TERRA_M-T | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| b8a922db-2a6a-37e9-8c5c-8efffb21a195 | -0.68028 | -51.69584 | 2024-12-08 12:40:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 8db04747-3cd6-3354-8dcb-64336bcb0ab8 | -6.83616 | -46.16242 | 2024-12-08 12:40:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c955ce7f-e2ec-3c88-aa17-b1c0f8774552 | -9.22022 | -48.12375 | 2024-12-08 12:40:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4b65ea5e-c567-3588-b65d-084a6dec7e59 | -8.08809 | -46.0446 | 2024-12-08 12:40:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a2d212c2-5087-3302-9252-6040f97b747c | -7.60022 | -46.62661 | 2024-12-08 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 09bca423-eaa1-3a46-9faa-f412bf81f751 | -2.16362 | -45.60576 | 2024-12-08 12:40:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6a80c32c-85fd-33d7-8eb6-15f737614888 | -4.06886 | -46.28617 | 2024-12-08 12:40:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 07867e99-9eef-3416-9cbd-838b0f662349 | -2.58466 | -47.54319 | 2024-12-08 12:40:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e61737fd-99c0-3196-91f2-16ced3d12488 | -2.91298 | -41.91594 | 2024-12-08 12:40:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 12.8 |
| deff8c63-a19f-327a-9c87-af906c6f8af3 | -4.17598 | -46.49515 | 2024-12-08 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9f6d0324-9682-3be3-b047-39847fd86601 | -3.50194 | -47.20061 | 2024-12-08 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 56f96da9-26b6-3c60-b358-97d319980485 | -4.06455 | -46.89176 | 2024-12-08 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2a4f1b85-8e5b-3bfa-a7f3-e78e0f3b5877 | -5.57844 | -45.20879 | 2024-12-08 12:40:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 527d5a7e-ef47-3e84-98f8-b6371fb6dc3d | -3.55906 | -45.33817 | 2024-12-08 12:40:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f9049a03-2b0b-33c5-a650-086dbd09481f | -8.7451 | -47.70874 | 2024-12-08 12:40:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d359478d-6421-3cfb-bd3c-ec3305a2f09f | -3.14668 | -41.13358 | 2024-12-08 12:40:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |
| c8c1d080-ceaa-36e9-8025-0ab99f9c3046 | -7.69787 | -43.18419 | 2024-12-08 12:40:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8786265e-c010-3322-85ae-ae7ad2caf693 | -1.62609 | -45.49351 | 2024-12-08 12:40:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ac3178c2-4d07-37f9-8c1c-89b7d514ccec | -9.09634 | -46.86369 | 2024-12-08 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| cbd9dc4f-4e2f-38e4-a660-7dc6e9e448fa | -7.60149 | -46.61769 | 2024-12-08 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0ab450ec-d9f7-3ccc-8346-33859babdcb7 | -7.23615 | -44.61222 | 2024-12-08 12:40:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aeef5c3a-66ce-38cb-8390-98b258fa1203 | -5.41367 | -49.07757 | 2024-12-08 12:40:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a59a45cf-7bd9-3ff7-a81b-db4bb219e1fc | -7.63354 | -47.16246 | 2024-12-08 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 381a261e-bafa-35c5-8760-f509715bb039 | -4.07012 | -46.27739 | 2024-12-08 12:40:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 1f918d56-fd1d-3aa2-ab51-b1a341239fbe | -7.09111 | -45.20332 | 2024-12-08 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 014b5528-c32a-38d0-8f42-64101834dc9c | -7.87674 | -44.71127 | 2024-12-08 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5e509e2c-e871-30b1-92d6-c075610baaa1 | -7.13342 | -45.55797 | 2024-12-08 12:40:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4d94a3f8-6367-38ca-aa63-15bdc62cca26 | -9.56227 | -46.31087 | 2024-12-08 12:40:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c9cbf79b-5d86-31ab-88ea-47f173e7eee8 | -7.856 | -46.25225 | 2024-12-08 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 68a03b79-7de2-3cf6-8609-6ef6df0359c4 | -7.6617 | -46.84145 | 2024-12-08 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 29e70668-0cc3-32fa-925f-454cc74736ce | -3.86541 | -46.60321 | 2024-12-08 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18a35c0e-8228-3491-89c4-20529e6e8276 | -6.82724 | -46.16118 | 2024-12-08 12:40:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b5eb84fe-0f4b-3824-937a-53f161b8fa2b | -7.82433 | -43.81495 | 2024-12-08 12:40:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c2f16d7c-05a5-3e84-8b48-adb21d3949b0 | -9.6558 | -47.02301 | 2024-12-08 12:40:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 13360929-fa1f-37b2-a867-81afbfd0f231 | -7.86716 | -44.70997 | 2024-12-08 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cb511c20-3f22-315c-ba63-990fd9a96063 | -4.1139 | -46.79995 | 2024-12-08 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0e775936-cf27-30b4-8ecf-33c3d433e4c3 | -4.85633 | -45.23148 | 2024-12-08 12:40:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 790c4220-33a0-3f0a-8a9f-cdbc5af3609e | -8.03507 | -48.33141 | 2024-12-08 12:40:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9ec17b1e-6d43-3968-b53b-0027e826c701 | -7.08049 | -45.21184 | 2024-12-08 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| cb9cd1fd-725a-30aa-afb8-75457d0e064b | -6.67792 | -44.05481 | 2024-12-08 12:40:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 62361391-8d10-30f5-aa38-47ff7e07806c | -6.922 | -44.50282 | 2024-12-08 12:40:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f56eb4b-c7f6-3291-bb3d-ec3d8b1be1fa | -9.09762 | -46.85471 | 2024-12-08 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 89e75c91-51a8-3896-9050-3aa1b22b5e2a | -3.54883 | -45.34596 | 2024-12-08 12:40:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b9b3f6e9-d0ec-3149-bc8a-141ef1a9b73d | -7.08975 | -45.21306 | 2024-12-08 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0a5a3101-af29-3daa-bffb-016112112f3a | -9.27155 | -47.958 | 2024-12-08 12:40:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3511ec4b-3767-34bb-94bc-1abfc3b489af | -7.14897 | -44.04769 | 2024-12-08 12:40:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6bff42f4-982d-3e90-abf8-f748fd055a39 | -4.08127 | -46.71463 | 2024-12-08 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2241cfbb-ec4b-3aad-9703-e5c09400b1ef | -5.11867 | -44.01468 | 2024-12-08 12:40:00 | TERRA_M-T | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b5de9bcb-9e1b-3c34-8586-cb9d1d0c6952 | -17.30045 | -46.58754 | 2024-12-08 12:42:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c336d955-9a24-3803-a12a-ce2f62084f3e | -14.41267 | -51.16208 | 2024-12-08 12:42:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4fbe11a4-ea43-39ac-a05a-e37cd5138bab | -11.08553 | -45.47653 | 2024-12-08 12:42:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fe1c3683-6e24-36ac-9c39-453cd02d1ce7 | -16.14238 | -44.86927 | 2024-12-08 12:42:00 | TERRA_M-T | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b2ddcecd-1b9c-365d-8df7-7faf093d55df | -11.01893 | -43.34217 | 2024-12-08 12:42:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 84b339bd-7113-3245-ac02-a6d8aec9177c | -14.11086 | -47.97486 | 2024-12-08 12:42:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dcec2c4c-f690-3e92-9e54-3e7c526d8c9f | -11.10088 | -43.32961 | 2024-12-08 12:42:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9fa0420a-4bc8-3375-879b-aa199f92fecc | -10.50707 | -42.41777 | 2024-12-08 12:42:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 96b606d7-27c0-3fc6-885b-9d1feb0a7804 | -12.11775 | -43.52735 | 2024-12-08 12:42:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 164e4059-e819-370d-a5f7-22f48f7fa6e8 | -13.71246 | -42.68353 | 2024-12-08 12:42:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ffde2aa9-9d7a-37bf-b5b5-ec43cbcaf5dc | -12.29347 | -52.49182 | 2024-12-08 12:42:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1172f518-7a37-3827-b15e-746585b1c439 | -11.79737 | -47.38695 | 2024-12-08 12:42:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3747ac57-6466-3815-8ff6-828fdae90e41 | -10.26432 | -49.23666 | 2024-12-08 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e86b9451-539c-3504-b6de-6f32c9c34f8d | -10.66121 | -44.59641 | 2024-12-08 12:42:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9960745e-05a9-3e2b-9564-a64fa2121ecc | -12.78109 | -45.00904 | 2024-12-08 12:42:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2872e6a0-ddee-3097-972b-942cc8cd307f | -15.62924 | -46.42331 | 2024-12-08 12:42:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 999d2c0a-22e3-3501-99a2-21df9128d1b0 | -10.63522 | -47.4592 | 2024-12-08 12:42:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 445f8068-cd57-3005-b239-40c69c700642 | -12.89967 | -46.88908 | 2024-12-08 12:42:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c0940494-d6fc-36f9-a230-10e0567e971a | -17.24581 | -43.5901 | 2024-12-08 12:42:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 521a9c7a-4ec2-394f-a1fe-ecda4e2ba28c | -11.08695 | -45.46597 | 2024-12-08 12:42:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b3a3a00b-7cd3-3ea4-8100-ca6c1ff79853 | -15.08843 | -48.93664 | 2024-12-08 12:42:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fab4be05-c256-3dde-b07a-75bead3f1190 | -17.2513 | -43.59773 | 2024-12-08 12:42:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 88822faf-a195-3dd5-be52-3f41de6ff044 | -15.7983 | -51.75229 | 2024-12-08 12:42:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9556c5ea-6ef9-3cf8-9c23-7f4a32c748a1 | -12.89835 | -46.89867 | 2024-12-08 12:42:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d5f1b8a4-3531-3124-994b-e16b6156098d | -14.06374 | -46.99928 | 2024-12-08 12:42:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e3d94bd3-6d84-3a59-bb21-fdf36a931efc | -12.4654 | -40.70043 | 2024-12-08 12:42:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 089e12bb-a225-372d-ae1b-8120ca3bc6cd | -10.26291 | -49.24605 | 2024-12-08 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb5cb03f-e8fb-321c-a372-8f1b69aef347 | -13.71666 | -42.69071 | 2024-12-08 12:42:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0dc0615a-b642-3c20-991f-35edb1176602 | -12.21771 | -44.17251 | 2024-12-08 12:42:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a4dabd99-76c9-3c73-b1d6-7091323bbb61 | -14.97485 | -41.33744 | 2024-12-08 12:42:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 51.3 |
| 1a33fcea-3fa5-3fb6-b54d-783c6c7a245b | -14.98273 | -41.33157 | 2024-12-08 12:42:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| cbb2a47b-9085-344f-b00e-9ba1a1c1663e | -12.34973 | -47.45665 | 2024-12-08 12:42:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c208666-b429-36a7-b86f-e5dc69b46552 | -10.63394 | -47.46815 | 2024-12-08 12:42:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f9643966-a1a4-36b7-875f-bb2d74d3f3eb | -17.29901 | -46.59863 | 2024-12-08 12:42:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 568318e2-c50a-3873-a2e4-32500c29ba10 | -14.25973 | -50.54349 | 2024-12-08 12:42:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f9e217a2-5cea-3b80-bab3-204840765cdf | -11.82498 | -47.77516 | 2024-12-08 12:42:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9233466e-9d18-3659-aa52-be34c7b864fa | -17.31537 | -46.62337 | 2024-12-08 12:42:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e028b6e3-75f9-30ad-89f5-7a1c00e2f39d | -12.68849 | -46.75257 | 2024-12-08 12:42:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bee24f52-97cd-39d9-a30e-fb4857c6f8f9 | -17.25735 | -43.65186 | 2024-12-08 12:42:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 823283c8-3187-30f7-a075-01edf7eeb8fd | -12.50631 | -43.81182 | 2024-12-08 12:42:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c2796249-a02b-3448-935e-1d2d150d19be | -11.62301 | -44.26518 | 2024-12-08 12:42:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 42094660-f1cb-313b-bc38-2742dc325039 | -15.18944 | -51.57459 | 2024-12-08 12:42:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 40a70999-2b04-3db7-b3d0-fe47d03b42c6 | -12.41039 | -47.22824 | 2024-12-08 12:42:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a4eafa1a-fe2e-3660-9e89-c97fdf7d86b9 | -11.82627 | -47.76617 | 2024-12-08 12:42:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1dae1a57-6d3b-3fed-80c0-35250e51bbec | -11.27696 | -45.10326 | 2024-12-08 12:42:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README14.md)
