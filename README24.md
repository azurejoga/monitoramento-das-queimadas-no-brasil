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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e8926a-699f-3623-b0eb-9ab5b8138b2a | -8.88412 | -40.81823 | 2024-11-18 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c5373e1-e8df-3a97-aa0a-0b5038732805 | -5.51233 | -41.07001 | 2024-11-18 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e777058-e361-3f3b-93c9-492ac4880a95 | -4.1088 | -51.06188 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e35bf5c-ec54-30f3-b0a0-73658d3c1bfd | -4.59516 | -44.58296 | 2024-11-18 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 420fac09-159e-37a4-888e-591387325f5f | -4.94918 | -44.84783 | 2024-11-18 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37a0c594-f62e-3fb5-bf95-90aa7e0a4564 | -3.3256 | -50.49596 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2ada9758-c808-3816-bbb9-aea137fbccdf | -2.99213 | -52.60307 | 2024-11-18 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65d07272-23a7-3aab-806b-b820ffbcfc99 | -6.58641 | -48.04002 | 2024-11-18 04:12:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8df8791-21b0-3539-a671-3eca74126731 | -8.5805 | -50.98307 | 2024-11-18 04:12:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df3a71ed-140e-3d61-ae68-5f3b749a2842 | -4.81615 | -40.31748 | 2024-11-18 04:12:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 06432ce0-8943-3bbe-8e86-fbc0eb16e4dd | -9.30344 | -46.20615 | 2024-11-18 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc4eb9db-f5e8-373b-a156-7a068b0abf7a | -3.37332 | -53.31991 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34bdcbdb-cff1-302d-9ac0-54ee0d6e78bb | -4.10376 | -46.87497 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b2808916-a033-35a8-ae0a-20a1b52d859c | -6.98552 | -39.66295 | 2024-11-18 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e333e453-03ee-376e-b899-3dff2086c47f | -5.3552 | -40.88435 | 2024-11-18 04:12:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1574db73-14ec-360c-853e-3145ace2c8d0 | -3.87638 | -54.356 | 2024-11-18 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bdafb96-82a1-3961-9301-9d18aff3839f | -3.62081 | -52.26535 | 2024-11-18 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3119e1d1-0449-32f7-8d60-cf60c8e0dd79 | -3.0974 | -53.10389 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58fdcd01-8c47-35c3-b4e5-298b7b9c310b | -3.04496 | -54.41241 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb2a3846-5826-3ee0-87d7-6e55d82063aa | -6.98934 | -39.65761 | 2024-11-18 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c886f025-1f9c-33ea-8142-efd87114d6ad | -3.94266 | -46.7144 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f52e1d41-4a48-32d9-bc36-c1c9496e4760 | -3.90051 | -50.08714 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00faa1e8-12e6-3e82-8632-2bfcae9e4b05 | -5.67166 | -47.3451 | 2024-11-18 04:12:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a142973-a153-3208-9437-0fc7b90f6cdf | -7.66444 | -39.29318 | 2024-11-18 04:12:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2202ca58-bae1-3859-a774-954b64293928 | -6.13334 | -44.72502 | 2024-11-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 703e0fcf-cb27-3727-a702-cb9484d0c717 | -3.57629 | -53.27679 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3730272-a095-30dc-bd68-a924fa60b2d7 | -3.18402 | -53.24435 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe10b227-9644-34f3-93bc-8bd7d35c8015 | -6.09065 | -41.94479 | 2024-11-18 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 26c24614-67b0-3045-a4bd-9b1c1cc22bc1 | -3.02511 | -54.10648 | 2024-11-18 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85d49252-2506-3bd6-80be-e087afa984b5 | -4.78861 | -40.40333 | 2024-11-18 04:12:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 31ee2214-06e8-31dc-abce-62149a0b5568 | -3.33814 | -53.30931 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d48566a-73e2-309e-986c-595147959413 | -3.8947 | -46.48607 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 331856ac-2d07-30d7-b09d-a12e15f7df0b | -5.17707 | -44.36979 | 2024-11-18 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ba14f22-0b24-3897-b5ba-22c427ce0e65 | -3.60421 | -52.22797 | 2024-11-18 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3beb64fb-d24a-3e8b-a43e-fc3ab2a041ab | -6.37343 | -41.54679 | 2024-11-18 04:12:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1267734d-9c71-3b0c-8915-d4169a79f0fa | -4.27712 | -50.88844 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c65067f-6f3d-3313-83d1-d51cc008ff1f | -6.47002 | -42.38428 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36bd29fc-89c5-3480-923e-bf316f5ec445 | -3.90524 | -46.49266 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d160bb1-cd1b-392f-a3e4-5422c428e90f | -5.52026 | -41.06377 | 2024-11-18 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e16ea2ac-5491-39f7-8542-6148ee494ccf | -5.3386 | -40.90117 | 2024-11-18 04:12:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd083fd6-d7e2-3b2d-a4fb-4cdfbabd34a0 | -3.88645 | -46.46551 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c11dc648-e32e-364c-baa6-00c870e9b180 | -3.89955 | -46.62393 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c1e00fa-00dc-351b-b9c3-8d846cfd5391 | -5.57172 | -46.42799 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 546b725e-17cc-3f3f-ab7a-e199fb78b857 | -5.24153 | -44.75153 | 2024-11-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e24f47b-861a-3a26-99de-b0c3381acc04 | -3.58576 | -53.78102 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25e94742-f0ed-3b1a-a4b5-fb44886ef634 | -4.8093 | -42.21014 | 2024-11-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44e52943-2f83-39fa-9759-3795f68d9da7 | -3.18332 | -53.24862 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3016b956-45dd-34fa-8915-3934ef3a8317 | -3.33558 | -50.49743 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 66d8303d-4256-3740-919f-66f69454054c | -3.38926 | -53.27675 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee603a31-9039-3584-b987-c2d40af10c1f | -7.39853 | -42.76846 | 2024-11-18 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d73401ce-2380-39d1-8a7e-437587dda99e | -5.56734 | -46.43174 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 760bc526-8e10-3509-97a9-d87cc615289b | -5.57101 | -46.43235 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbf42a7b-57fd-3590-aa88-17cb6a6e4e39 | -9.08357 | -40.52369 | 2024-11-18 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db53cf2b-89ee-3130-b00f-29e7746f615c | -3.18535 | -53.25115 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f8483df-2f1f-363d-b82d-c08d62e2b956 | -3.09902 | -53.10946 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b1eca87-7d80-3aae-902e-d0e47d623edd | -5.56626 | -49.56646 | 2024-11-18 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaeee9a8-a307-3b09-bda2-d338b01bda2f | -4.81745 | -44.48571 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bedd6a19-c3ec-369f-96aa-afd3e87bff14 | -2.79927 | -53.00082 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca983ec3-362b-3957-81a2-9b3fef75fb76 | -5.19193 | -49.61152 | 2024-11-18 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ce8a7b5-d4de-356f-89cb-2acd900eb3d0 | -4.94778 | -47.80419 | 2024-11-18 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cda3863e-d91b-33aa-a8b2-e49469258ca0 | -3.3298 | -53.35886 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 540eae5e-a412-34c0-b480-fb6bf8b7359d | -3.37558 | -53.32022 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43b7d109-9970-3a53-8a6d-12ccaf23e2bb | -3.05922 | -54.41182 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5587ee2-a009-3649-a7c0-c76ade5ae722 | -5.34474 | -45.5887 | 2024-11-18 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 352d2755-7967-3a95-a31c-3f7e7002a90a | -3.06562 | -53.27548 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed3bc81e-262c-30ca-9a38-14124c9d8789 | -4.83228 | -45.12173 | 2024-11-18 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 236e71a9-68bf-3bd9-9f21-78711867ff6a | -4.2776 | -50.88555 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4351af17-0a26-3bb9-8d4f-d30c958a6862 | -3.34338 | -53.31478 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ced045b5-5018-3d1e-80cf-246319d5305f | -3.94647 | -46.71504 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 243ce022-d244-3e05-ba89-c91e9a12f82a | -6.58036 | -42.00241 | 2024-11-18 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 11d907ae-93bc-3a28-9143-fa5c9ba5d079 | -3.88509 | -46.64096 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21645c2a-2e5d-3643-b890-440190754c0a | -5.00975 | -46.85485 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a41fa696-1730-3828-a46e-b3c5d6cf0f1b | -4.24867 | -49.19473 | 2024-11-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bcc1167-9f63-36fd-b9b5-287bc8597760 | -4.7149 | -49.61872 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7210893-9579-3962-aeb0-506e9b426c60 | -6.13673 | -44.72557 | 2024-11-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627e8eac-f8f8-328c-b69a-4ae5b0e48392 | -4.61139 | -50.91829 | 2024-11-18 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b96f7ac5-98ca-37b5-85a5-d070eeb74c36 | -4.90404 | -44.02553 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9f13cddb-6d40-357e-9c1b-770b2914df64 | -4.10366 | -51.06129 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4404c6a6-c61d-3a77-b39b-9f49d2b17eab | -4.37229 | -50.51528 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6b0a2b7-accc-3add-a822-1868860d5479 | -7.88769 | -44.21307 | 2024-11-18 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3664f2-07ea-306d-89b2-551d4c5ad457 | -5.33151 | -44.93357 | 2024-11-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 721d0dee-3d5d-351e-985a-71a5cf0a7ad8 | -3.98854 | -49.4045 | 2024-11-18 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf0bf3a-5d21-307e-ad05-3617eb7a956c | -4.90614 | -44.02508 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5e0f35ff-4a07-3137-b860-b0c8a9da18f9 | -4.27081 | -50.59358 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 833fc991-dc8e-38c6-872b-6ad06f2c7822 | -7.18444 | -39.11783 | 2024-11-18 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9e573622-4e05-323a-84a1-3d353edb408f | -4.94979 | -44.84405 | 2024-11-18 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| abdacfdb-1bcf-3471-b000-f18882703f4e | -3.52952 | -50.25298 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b926e7a-dbeb-3a59-8995-a7a7f928a8af | -3.84934 | -46.6445 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad46cbc3-e91f-3be7-8796-3a1492c5ebef | -3.50377 | -54.03703 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f0c6b8f-eb04-3217-ba7a-abfa45596313 | -3.13627 | -52.98314 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 698a4c3c-5a59-3f82-a5f5-27df8eb883b7 | -3.88735 | -46.62701 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32b372ab-a7ea-3098-a09a-524e7252e1f1 | -9.2092 | -36.11653 | 2024-11-18 04:12:00 | NOAA-20 | BRANQUINHA | ALAGOAS | Brasil | 2701100 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bbf803e3-2432-36ad-8f23-1428ab19aa07 | -4.16859 | -46.78074 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17ed6634-2a15-31b5-8586-6cf2ea055b84 | -4.37133 | -50.5208 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1e6ce69-4a25-3ea1-a877-dae26518f351 | -8.88353 | -40.82228 | 2024-11-18 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 572c6b68-48d0-3157-9126-1dcd7cd24a99 | -4.29875 | -50.44421 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feeee697-ff16-3aa9-99a3-3251104de2d6 | -4.99652 | -44.33389 | 2024-11-18 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 593e12f1-ddf2-394c-ab72-9fdbddd18907 | -4.38276 | -50.84126 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed67592f-ccce-38a6-8d0f-7fda748a1ccb | -4.10826 | -51.06509 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee78a42a-b395-32be-bfbb-fb5620628a19 | -4.61189 | -50.91533 | 2024-11-18 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
