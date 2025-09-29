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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c66df77-e12c-3d2e-9d27-4daa1468b0b2 | -4.91842 | -48.16568 | 2025-09-29 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f74ef60-bc94-3de2-a39d-e2f1692b5f99 | -7.72437 | -46.99921 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0555de57-f159-32b8-94c9-04915b0c89c5 | -5.69228 | -42.62817 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9a6ebb2b-059b-39cc-a1af-614fbead02b6 | -7.86089 | -41.05863 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dbf3c4d4-8256-3e4a-b410-3c1e2fbd2e0e | -6.09689 | -42.65581 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5cf33f7-615a-3e18-b1dc-43ca62a51667 | -6.26246 | -43.63635 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 38c0b708-c064-35df-b498-4184284a04b6 | -6.11629 | -41.8272 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 65b6f84a-fd3a-3db5-8fd8-5d4216692e39 | -7.58838 | -44.79884 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d12eeacb-c93d-3f6f-a3ce-26b718e433bd | -5.67641 | -45.29349 | 2025-09-29 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9af549b3-36d5-376b-b78b-cdb2ee86f19f | -3.21665 | -43.36395 | 2025-09-29 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 115c9ed4-80d3-3497-bb1c-616b11b04053 | -6.11019 | -43.4685 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55a37282-8519-3ff8-9b1a-09abf5e0267d | -7.04854 | -44.75507 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8737521d-c71b-31af-b195-59fb605c9845 | -6.74887 | -44.75275 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f330056-0d39-3b60-b18b-5fc2b1fd4532 | -6.48039 | -42.91243 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cc26c2d-ad10-30a0-ad46-91455f42cfc4 | -6.76483 | -43.60714 | 2025-09-29 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81541ca8-e756-37a0-a411-29a353d85a4e | -5.14401 | -42.76406 | 2025-09-29 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b8096f0-76b6-3d43-891a-c52eb0193931 | -6.43006 | -43.50715 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 265eeb8b-8b63-3b67-b75d-8e535bb36479 | -5.72045 | -42.862 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc608cdd-3118-3cc9-95c6-14f787a708ed | -5.74771 | -42.82169 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3b34aeae-0d2c-3a4a-a0f7-e425a912f99f | -6.83118 | -44.08695 | 2025-09-29 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bd75c02-d64d-3818-8fdd-2b274ab8d48c | -6.08236 | -42.44559 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8dc2bef3-a5bf-3559-a19e-f4e4ef24b62a | -8.63425 | -43.99581 | 2025-09-29 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53257512-d0ed-35fd-9d0a-2d8d1be1d4a5 | -7.81264 | -46.99485 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5ea94568-dd8b-3e4c-9171-9891699492b1 | -8.29637 | -45.43493 | 2025-09-29 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 65b8990e-b695-3bc0-acf4-06aa09ae1079 | -3.09959 | -47.01773 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 65bad5e4-ed8f-36ea-b34c-dad5ffcb97c4 | -6.46605 | -44.21611 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c40b7bb4-2972-3f56-b5b0-67b89aefa3f9 | -7.90051 | -44.59497 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f017ed60-24f9-3c6c-9a5f-a8c562c0f078 | -8.29713 | -45.47543 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d29be17c-c990-3984-afdd-a359e62e0220 | -6.62359 | -44.96791 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dcc33c1-98d3-3698-ba31-1a02edae1bfd | -4.37774 | -44.08721 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a27d2e03-63ed-378d-b246-960d6800d8c7 | -5.71717 | -42.8391 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 865fc20e-2734-3371-ba64-be07cd54f237 | -6.28025 | -44.9404 | 2025-09-29 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb23ee8-fc7d-36c8-9aa0-1303de819ab4 | -5.90677 | -45.85353 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78476d7a-af9e-3c74-a809-cf1ce81f7bc0 | -4.04219 | -40.50583 | 2025-09-29 04:06:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 92e48c99-feb9-3075-8465-d40bca2061d0 | -5.30808 | -43.15941 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7dfd1ef-0500-3501-b973-d90a06580a92 | -6.28212 | -42.49188 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3cb03279-0d27-36c7-8fcb-7123486fbfa5 | -8.00715 | -47.03246 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 340d2a12-2a58-35b2-bdaf-1e5d4ee195e0 | -5.55746 | -44.8645 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08e9ee40-cc4c-3cc2-9a3c-b60e0166cd6e | -5.81716 | -42.82921 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e1e82857-8ced-324a-8bc5-60f16e704bc7 | -4.7673 | -46.59404 | 2025-09-29 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a82d2f3-998b-32ac-a12e-ec6753afea90 | -8.25379 | -45.4711 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfa6b350-837f-3b8c-b687-8b9975d88fa3 | -6.49205 | -44.25763 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e0b80a6-2485-381d-946d-48e144fcc90d | -5.41767 | -41.32644 | 2025-09-29 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12e5315a-a5d8-31c6-ba9a-811aa997f716 | -6.078 | -44.06253 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2047704e-22df-394f-97b7-95b862237ff2 | -5.97319 | -44.23583 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a5da463-600c-37bf-b247-fb360ea2433c | -6.89695 | -44.53222 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10f7794f-a7a6-33fe-97f1-dd7093211f50 | -5.70238 | -42.62977 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d92b6b5e-d3c2-3d31-8cac-33919c78c301 | -7.38312 | -47.03997 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1388dcb-58b6-3745-99bb-0481cf2c8536 | -5.7159 | -42.86872 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7ef8d1bb-33b6-3abd-a49f-94f9d32cfca7 | -5.74098 | -42.66881 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cd6ab9f1-2515-3f0b-bdb7-7ee4b020efdd | -7.50065 | -44.29491 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 793c1056-7085-388f-95ad-ec24e755d02a | -4.25807 | -48.55295 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aef814e6-ea5b-3260-9b94-5d6e94ae865c | -3.83391 | -40.4694 | 2025-09-29 04:06:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12c25615-6d93-3afa-9dc7-958730583766 | -3.74497 | -40.81884 | 2025-09-29 04:06:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74606a15-4c60-3a42-be22-3bc76050b268 | -6.11302 | -43.47281 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf6db4ec-792d-352b-9bda-619f196dea22 | -7.56203 | -42.41507 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fc00ca6b-88a4-3e4c-833a-de01671cf2e7 | -4.57119 | -37.86049 | 2025-09-29 04:06:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14543ad6-215a-3c66-bbaf-618dad1b6031 | -3.8306 | -40.46889 | 2025-09-29 04:06:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eb18515b-4c2a-3bf5-89eb-c841a63ab0e2 | -6.07505 | -42.46977 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ecd33d1e-0e50-3f55-bc4b-7fe6ad579e2a | -6.75911 | -45.61782 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0d39e0f-6a83-3c9e-b18a-d9d122a0cb78 | -8.00217 | -44.48429 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d6ad695-0b78-35a5-adae-5840b96ee5b1 | -6.4956 | -44.25817 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b6748ee-7ace-398a-8247-e5d99464feb6 | -8.05364 | -47.99518 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e37be9c-16bd-3ac1-999d-fc058030bda6 | -5.28064 | -43.15509 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7e2f814-baff-3b98-90b4-6ca22d233543 | -7.86753 | -41.05967 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6978218f-361a-3993-967f-3be0b8a91b3a | -5.81402 | -42.78406 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59c8957f-e668-3ab3-9f76-80b6d222438f | -6.1207 | -41.82079 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e9f5dfe2-d6d9-35bb-834f-5fde2eb27296 | -5.73819 | -42.6647 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44520a36-d279-3ad0-b7ef-c66c92eac460 | -6.426 | -43.51037 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f508338c-2c78-3bbe-87eb-95273fb2dd1d | -5.14681 | -42.76822 | 2025-09-29 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ca2f639-e8ac-3e74-b811-3144cc72e117 | -6.26593 | -43.63686 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad8f4d69-625e-3dd2-ba54-7c60cd72fa39 | -6.08172 | -44.17476 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b150de6e-ea95-3ea1-b3a3-f91bbf2688f4 | -6.57282 | -43.40705 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 17c158bf-a466-38e4-9ffa-5e622520b1a8 | -4.31007 | -48.09414 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8822d91e-e708-3d50-baae-eb72c02f68c6 | -5.71543 | -42.85001 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| adc2ecb9-8b67-39fa-828d-e8bfdaf4911e | -6.64407 | -44.03331 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e435b10a-8813-3714-86d4-071819785323 | -6.27639 | -44.91763 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 855bd045-7a32-385b-b13b-0e95f959e1b5 | -7.57366 | -42.40617 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc225040-c4fb-34ad-8f04-ec81fe59ea90 | -5.91414 | -42.94507 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 69f0d35b-00fc-3fab-816f-042bd8fa13bc | -6.62759 | -45.89731 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4927e282-5132-34a2-965a-c3a647792783 | -4.9312 | -47.45129 | 2025-09-29 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6db335dc-a6d4-3d7b-be8f-d7ced8bedbdc | -8.29861 | -45.46666 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6686f767-6995-386e-9914-18a886f03d2f | -5.48268 | -42.8804 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81d27186-9e50-3b9b-ac63-5303e4c47e02 | -6.28383 | -42.48121 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7aaa7c27-99ef-3b86-b68d-34206b199fa1 | -4.31088 | -48.08929 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e479e8fa-59a7-3612-b8f6-3e6669052bdd | -4.03834 | -40.50877 | 2025-09-29 04:06:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a1633cc-c9d0-32f6-8174-97ee286205b7 | -5.99455 | -45.80998 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8281ae3b-08ab-31ac-b0be-992387e51ed4 | -6.5664 | -44.17798 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89e6fe2d-ce45-304b-a7de-f03c71a03ca8 | -5.80632 | -42.85353 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f2d2ed9c-86d7-3678-967b-2f8105d1e472 | -2.8025 | -48.62714 | 2025-09-29 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a8de7db-cc7f-3f85-a887-96ddb5963a60 | -7.70277 | -41.2872 | 2025-09-29 04:06:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d2d7e93-b728-33ca-95cb-113b758eb576 | -4.93284 | -47.08742 | 2025-09-29 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ee703a6-75e4-304a-b2e6-005c0f92f43f | -4.92856 | -47.08662 | 2025-09-29 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69a20438-f95b-3504-9554-7addd46b8c40 | -7.89502 | -44.60611 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af49064c-77f9-326d-a45e-62d085f6b96c | -7.22159 | -44.7768 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15a8f09a-0ee5-3490-b18b-afed1688862f | -6.61944 | -44.95147 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e2ffcc97-7dd8-30e4-a5f6-78d80e1d4376 | -7.86808 | -41.05618 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0648ed3d-e971-3da1-bf7e-b66d302cca18 | -5.24223 | -45.35764 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faadc05f-ced8-3d27-828f-94962e9b8bc8 | -5.73737 | -42.86477 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfc3ab4e-f8d2-3367-90f7-c0a014f3420c | -6.06331 | -42.47878 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README34.md)
