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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2143303e-c083-3ba5-98f9-52629fabc0b6 | -10.09882 | -44.55758 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bf143c7-0de1-3b6f-8e7f-db6d64c7f55f | -11.13884 | -47.71694 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f175bd23-f403-347f-95ae-30ff78392238 | -11.14608 | -47.7144 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 329610b0-0224-311a-836d-a8c28d571fff | -6.78913 | -46.47276 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74f41c65-50bd-3b06-b931-82c3eff5c176 | -11.64532 | -44.08406 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efefad68-1911-3fb8-9e7f-57b8ae28c660 | -7.93982 | -39.85439 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 049c0069-92b2-340b-a810-87756fd21074 | -5.15139 | -48.10047 | 2025-10-19 04:32:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae1e1b8-0197-3f1e-a26d-aadc69e5141f | -5.2049 | -49.25442 | 2025-10-19 04:32:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c17fb28e-a342-349b-82e0-9876b05dd72c | -10.72193 | -44.55067 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e513ba-2a93-33a9-bba1-836fd1b81a99 | -6.25254 | -47.30431 | 2025-10-19 04:32:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d0132cf-6311-37e8-b62b-7e5e23969c76 | -6.5591 | -46.36425 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8554cc5b-c034-3480-afd6-a76e52d37784 | -7.12727 | -46.15865 | 2025-10-19 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5778381b-6892-3bf2-a6c3-21a95adc6a37 | -7.16719 | -42.36243 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 527a1881-6024-3786-bf93-d810a1437858 | -6.10012 | -44.02132 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ab20baa-52a0-3b78-9f5f-cf337ce511a7 | -8.24464 | -44.00267 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52f575e0-599f-37a0-974b-3ecb11bc3607 | -8.4359 | -44.14513 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 277523eb-0d3d-3b8b-b62c-476a10ebdbfc | -6.37584 | -45.76264 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5326656-01b5-396f-bc25-0971fbf249b9 | -8.24463 | -44.00061 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5831406-6c8c-3fb0-8e14-a69a32d1a4d7 | -5.30399 | -44.84554 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c23f715c-141d-3bdf-87d9-7fa825153d24 | -5.10313 | -46.13735 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8170338c-0e2f-3aac-b8ea-3c6578a569df | -12.33366 | -41.3904 | 2025-10-19 04:32:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44805acd-5191-34b9-95e3-a3d8f910ee32 | -9.22216 | -46.06157 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0614527d-7bb3-377e-9921-95d0d61c0236 | -9.23195 | -46.06703 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7f74ddf7-e14a-368d-885f-0eda39c60aab | -9.90546 | -47.65781 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7a0ace1-ae8a-3efe-9a3a-c6e986f9b1ad | -5.67557 | -47.98785 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0e9ea49-466f-3379-b70c-c8a21ebc65c7 | -6.61588 | -44.2192 | 2025-10-19 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03746edd-8422-3495-87a8-cb954367da6f | -10.36085 | -47.47794 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d949c69c-8dc0-3990-bed9-519fa9994cf5 | -6.9281 | -59.28232 | 2025-10-19 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d744389b-974e-3bae-aa4b-49e2dc4fd046 | -9.90784 | -45.95888 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19e60cdd-972d-37bd-a3c1-f1ad887c8fa8 | -5.97964 | -42.96587 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| edc9d4a7-f06e-3460-ad8e-06dd4f7cbec6 | -6.24136 | -44.15214 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f068e64c-ea84-3f32-b91b-bed22218c74e | -7.19755 | -42.21487 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0368d033-7457-3a0a-9cac-ba65b5d9498b | -7.44207 | -42.69613 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7971cbfe-d8d3-3e46-a427-14e5fb094d3f | -8.43663 | -44.1403 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e579afa-8ebc-342d-8913-0e04db605560 | -5.36015 | -47.2095 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 28570e4b-c617-3d39-ba38-22a6880804af | -5.76453 | -49.94027 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39299ca6-da9c-3204-8b14-2f67b212b221 | -7.97242 | -43.88072 | 2025-10-19 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 24674b69-3ce9-3e97-ab11-77d35cc2b553 | -7.95897 | -45.9407 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ead2bd84-3ed2-3ff9-9d65-781bbbe63467 | -7.13544 | -44.26601 | 2025-10-19 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d5bfd066-3353-33ab-b4bb-2dff91884617 | -9.10783 | -43.20898 | 2025-10-19 04:32:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0371c19b-865b-34a2-b3ac-577379da0e14 | -10.31886 | -48.78882 | 2025-10-19 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed16a1f0-244c-3a9f-bcbe-8f46a413fd21 | -9.52338 | -49.1132 | 2025-10-19 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32774c7b-1eb9-3469-9940-b135a0d3813a | -7.83348 | -49.30987 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f8bd6f-7b5d-3f09-9444-92ee39feab05 | -6.00156 | -44.18026 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b842d82a-7ef0-324a-8ade-cfd98cf59fae | -5.24146 | -47.18736 | 2025-10-19 04:32:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52725e57-ad90-3366-b7b6-c48fdb2fce3d | -10.88664 | -46.07992 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1daa416f-8009-388a-95b5-d2e68da79eb1 | -6.43598 | -43.92122 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2635945f-2623-3e60-a3d8-ab074461d5a9 | -5.10143 | -46.13324 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| baba572a-0cbf-3901-a7ae-ec9d80cc903c | -5.89519 | -42.80829 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c16378c5-8ede-305c-90ea-a89fd26ab982 | -7.31299 | -42.46636 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4b0fb833-5e6a-36e5-9d13-91e266e080a5 | -12.15079 | -45.05997 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e6f3615-50cc-302a-901c-08d8e6423d63 | -10.23561 | -44.89138 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab249d61-51a7-3ae5-81f9-75a158e4983d | -11.4543 | -49.10638 | 2025-10-19 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfc8334a-e1de-35f5-b655-5078239fde5f | -5.38161 | -46.4261 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f835b971-6c46-3f51-9ba5-8fcc050c1d22 | -11.87573 | -45.46657 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee693b9f-d2d0-3141-b0be-492ff4635994 | -11.99702 | -46.77549 | 2025-10-19 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afa73b48-cb5a-392c-ac4b-766a53151050 | -7.20098 | -42.19169 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f3e27aef-cae1-3e4e-a973-f55af8243ffa | -6.50136 | -54.88916 | 2025-10-19 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1bd8c10-a53d-3f34-bffa-029de98a325c | -7.19984 | -42.19944 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b00ba506-4c0f-3950-9359-d5283110b87a | -10.61696 | -48.016 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b084cfbb-72d0-35ef-b8aa-e21cd2eab17b | -5.54278 | -46.52315 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac6ca764-7fdd-38f0-98fe-f0bc077b1694 | -8.42832 | -44.14425 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f35779e3-47f3-3aeb-8998-dc028e35ea63 | -8.2491 | -43.99646 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 28a50c2d-f6ef-3279-b412-fa89398d96a9 | -10.63299 | -48.02222 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aff5c6c-005f-3547-bda0-ef50ffb27d04 | -5.75924 | -44.00103 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b5dab44-1723-323e-87a9-4630d121dca5 | -11.62627 | -44.07602 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b153135c-3929-3a28-bb2c-6ed1181f140c | -8.9039 | -47.76576 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b9ea4f4-6013-30a7-89d6-7cb4b1f68ffa | -6.14756 | -44.30386 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51bd04a3-e00f-3a27-9d90-49199652d2f4 | -11.8918 | -45.43328 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63611abb-c6cb-318a-a4b6-c8e249f42807 | -6.79304 | -46.46971 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d77d0f13-bd07-384a-a72e-401be0ac431a | -8.21915 | -43.96542 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69c092c3-d8fe-3b4b-956e-5c389994aeb1 | -7.4514 | -47.12903 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 101cf6c8-fb8c-33f9-9a80-3b919c5a0131 | -7.02037 | -46.8029 | 2025-10-19 04:32:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd20f47b-a845-36a0-99cd-61cc4ff86213 | -8.66635 | -47.08738 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12c80c9f-75e5-3dfd-8295-b146fa1386a0 | -10.72018 | -44.536 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac8b4ef1-165f-32f7-8fc0-c88d770a7936 | -12.46896 | -45.43663 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a453dd5-04f8-3f36-807e-a7b353c3deb4 | -8.04889 | -55.09453 | 2025-10-19 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c47fc0e-e342-3303-be68-bda8b19c766a | -7.4458 | -46.83974 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 447229d5-7765-3672-be5e-3976d4e33c2e | -12.45449 | -45.44096 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7009b717-baaa-31cf-9cf8-649fce9d7f7a | -9.90721 | -45.95518 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af24b8d4-8249-3253-bbe1-df156296e2f4 | -12.18249 | -40.62431 | 2025-10-19 04:32:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86962a69-e4a7-336c-813d-534bd14136ec | -7.08647 | -46.87817 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40fa62b9-a76b-342a-8b44-7de775b3669e | -10.71516 | -47.9306 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7445e282-850e-370c-a5ca-dccd2ca22130 | -4.96678 | -56.26601 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d045609-d5d0-33e1-80b0-c56b6a567f6c | -9.60636 | -49.01786 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf9d559b-0a4f-3cf9-884d-945bfc875c54 | -7.8723 | -45.71138 | 2025-10-19 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a9f61c8-45e8-3dc0-b662-db3677d4e063 | -10.1646 | -42.20881 | 2025-10-19 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66e69027-039d-3627-a24c-8f3e671c6a3e | -10.5622 | -45.1596 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6ed576e-003b-34c1-a9ca-e4f601e7f4ce | -6.41622 | -43.91584 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf8e7251-39a1-3427-89db-df11c7bcff42 | -7.62176 | -60.93866 | 2025-10-19 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f19c0042-1f2d-3fa1-9534-81a7453eef04 | -10.10257 | -44.55824 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c20daf5c-b05d-31d2-9098-f281f4afe67a | -11.64927 | -44.08464 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ead6be45-2024-3717-86d6-dbaecff77f93 | -6.53316 | -47.57139 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de352c0b-c5ed-3966-aa0b-1419ec8b97c6 | -8.51474 | -49.50765 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9bbec68-e20a-364d-9180-23c3ad64259b | -4.96514 | -56.27584 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7b850ff-db0f-3abd-a961-68fa0db1e1eb | -7.15723 | -42.37248 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6315ef5b-92e5-3363-86da-26a4440af3da | -11.6349 | -44.07205 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f86dc415-8533-37aa-b294-45bebdccc838 | -8.34878 | -46.20975 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e66be5b-1b86-3309-96a5-5315ff43560d | -11.98101 | -46.92924 | 2025-10-19 04:32:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef02e67-284e-3772-a78d-155413c5a8a3 | -5.98613 | -42.78725 | 2025-10-19 04:32:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
