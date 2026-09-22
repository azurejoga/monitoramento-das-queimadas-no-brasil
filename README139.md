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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbb74064-4846-3c33-a254-ce70009a9456 | 4.0579 | -61.4095 | 2026-09-22 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 26821043-6e5e-3a55-b1c3-7a9fb05b61e9 | -6.9414 | -42.907 | 2026-09-22 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 6a8d3581-2025-3016-80e1-ba8e2bcc77ab | -12.8 | -44.2073 | 2026-09-22 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 79f1686a-9614-3751-a047-9191e333ddbf | -3.7364 | -58.8626 | 2026-09-22 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 152.9 |
| fcbb57ab-11e8-3b2c-9080-53fdeb4289a6 | -6.7589 | -47.8995 | 2026-09-22 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 094cc90e-7f5f-35c9-b9a2-cfc7cba29eee | -7.5945 | -43.4296 | 2026-09-22 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| fb1b2101-5a54-3c54-a11b-e2be40cdd5ef | -2.8285 | -50.4653 | 2026-09-22 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e73e566e-6aab-32e2-83a7-9c440842489f | -6.3436 | -55.8243 | 2026-09-22 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| bcb48dec-f8de-3113-8ed6-c3c5a3a99443 | -7.1745 | -47.4517 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a1e94289-ecc3-3629-b447-d853371d75af | -3.1698 | -58.5859 | 2026-09-22 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6f0f2367-b782-3671-bbfe-221d9647b5ce | -13.2787 | -51.795 | 2026-09-22 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 02713570-14f8-3653-98df-0d5c4d051b82 | -8.5803 | -44.5322 | 2026-09-22 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 181.9 |
| dcb5e096-4b55-3f58-8f58-d433c0d16f60 | -3.331 | -59.8483 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1f1930fb-e8e2-325d-a09d-2cf410c9840b | -5.6223 | -43.3701 | 2026-09-22 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| fe65022d-572b-3fdf-808a-34cb1ef0aa41 | -5.8678 | -45.2346 | 2026-09-22 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ecd181c0-4bf4-3cb7-9be0-1db8b65375c5 | -3.6065 | -59.4413 | 2026-09-22 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 146bee82-1769-37dc-a3ed-ad679ccdb09e | -5.841 | -53.5205 | 2026-09-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 85fe2f6d-f7d0-3631-8b38-5605919ca252 | -10.6878 | -50.751 | 2026-09-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 337cceb1-54dd-3bb8-989a-8e93a25bdfd8 | -3.6215 | -60.566 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 7558434c-25dc-39ac-abd3-5bb5e3d8c272 | -6.8985 | -41.6976 | 2026-09-22 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 192.3 |
| 8a3173dd-0a09-31c6-8f18-ca6cd33f9f33 | -9.6006 | -45.9456 | 2026-09-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 614403d0-a369-391d-8901-da30b5e48aae | -6.3926 | -45.1268 | 2026-09-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ec94dc1a-4e4e-32db-a23d-08efe6f59478 | -11.3784 | -44.2195 | 2026-09-22 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 321.1 |
| 0f375c30-5440-3e2e-b89e-369c2a5c1dd8 | -6.4485 | -59.9909 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f2d3d644-9e45-329e-968d-30fc54bcc7ce | -3.0717 | -61.2764 | 2026-09-22 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4c807b91-8f05-3544-bf2a-cd806da0dbd1 | -11.6793 | -43.4684 | 2026-09-22 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| cb228cff-e4d8-34c7-8a22-6fe77cc524c1 | -3.7856 | -60.7335 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 235.4 |
| a4452fba-feac-3520-abf9-077244cf3f64 | -10.4536 | -51.325 | 2026-09-22 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4029cb8f-b439-3894-9025-9cbf48990781 | -4.6587 | -42.0964 | 2026-09-22 14:30:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 184.9 |
| 73317fc9-a151-3224-9234-62de585be5c1 | -10.5748 | -46.7296 | 2026-09-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| d2e5c469-28ed-3b3f-962b-a961c0ca949d | -12.8053 | -54.0669 | 2026-09-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b5fc6fa1-217d-3810-b7fb-ae5fe8c1ed11 | -9.5356 | -47.9349 | 2026-09-22 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 137a0568-c1e9-3909-a375-45e4d9431170 | -3.6452 | -58.7685 | 2026-09-22 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a482a135-40bb-3d49-9415-304ba7d6bfb6 | -12.8056 | -54.0462 | 2026-09-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 254.0 |
| 6858f80f-5c20-3101-a0fd-fc675683ee6f | -3.2396 | -53.9417 | 2026-09-22 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 222.2 |
| 6e4532f6-a9ea-302f-a629-d259b86f1595 | -8.7706 | -45.8567 | 2026-09-22 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c8ce4062-fdd0-3d3d-afcb-fa4645d38903 | -9.3797 | -48.3232 | 2026-09-22 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 9c0e54d6-98ef-3739-a693-8fbdf9838603 | -6.3199 | -59.9381 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 34282cb8-851a-3f75-a0da-244cc2807a0f | -3.478 | -59.597 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 93014490-4b7d-3402-864e-1165be5ad3e1 | -12.2726 | -50.1441 | 2026-09-22 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 4f8e4525-8152-3f1f-8d45-666ab7498a2d | -10.8911 | -54.0677 | 2026-09-22 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f026d438-b927-3d32-9662-8545fdd619f4 | -6.1111 | -57.6645 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 8c1ecf5e-61f9-3c8a-aedb-2bd01cece733 | -10.5908 | -53.9713 | 2026-09-22 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d7827e3a-c886-3e15-af2f-e4fe7f340040 | -10.872 | -54.0899 | 2026-09-22 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1c5adc88-5770-3397-8865-d786ce74827c | -12.8246 | -54.0442 | 2026-09-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1fa27230-6d4c-35fb-89d3-4816512b2ce6 | -3.7547 | -58.8622 | 2026-09-22 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| bc9dd0da-99b0-3321-9734-e4f119e8dc61 | 2.2923 | -50.9377 | 2026-09-22 14:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 17e813e3-9c4c-330d-84c4-a88ae7647da5 | -12.4016 | -47.003 | 2026-09-22 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 2c3a952a-6e96-3097-b1b5-83fe77ce0cee | -11.7076 | -51.0024 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 562669cb-ed62-3046-8179-f1bba884db0b | -3.3309 | -59.8673 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3b126f25-14e1-38c3-92de-d488d5d50442 | -8.4799 | -57.6085 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d0a945b3-bea4-3cbd-9193-74dae7545818 | -2.8791 | -57.799 | 2026-09-22 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 56e93737-a1ec-30e9-95c5-e907bca4c62a | -6.7989 | -43.9008 | 2026-09-22 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 37441abf-afa2-3296-bacc-83d3be9f4597 | -8.7916 | -44.2778 | 2026-09-22 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 87e41c51-8cc8-3022-b94f-d70370775592 | -6.3197 | -59.9764 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a8d10896-afae-3890-85b7-d0dd09c34af5 | -7.5247 | -46.2252 | 2026-09-22 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a5c2f05a-1d6f-33d6-a18b-4a67ef6bef19 | -6.9871 | -47.4885 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 50613549-518e-3ac4-870b-180bfafba3c1 | -6.295 | -57.735 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| de63f17f-a436-35d0-afb4-ce13986e6bae | -11.7159 | -54.5858 | 2026-09-22 14:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a0127c98-ee74-37f5-884c-b82348b61e7d | -9.859 | -46.4114 | 2026-09-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| c3822ac7-2c44-3407-abf2-8116cc3132aa | -11.3226 | -51.3838 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f4ec0731-a4a0-354f-8c56-62bf9d71dde3 | -6.1838 | -47.5258 | 2026-09-22 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 908e6bd3-b873-351f-b5fa-0a04d92cb3bc | -6.3013 | -59.9771 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0973cdcd-9f59-352a-b47e-2da1bd9115a5 | -3.3183 | -57.8677 | 2026-09-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f50c67c3-c40c-3863-a7fa-3679cfcd1e60 | -6.728 | -59.423 | 2026-09-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 50cf9c50-3112-3141-a6ec-43c448edcd00 | -6.5829 | -58.9851 | 2026-09-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 52a70716-0ee9-364d-9ecb-cf52b220139c | -7.5548 | -48.6843 | 2026-09-22 14:30:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2e11db92-c307-3b0d-bd72-1e9b62838bef | -12.7865 | -54.0482 | 2026-09-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 934c67df-6183-3838-a206-325dbc393957 | -2.8608 | -57.7994 | 2026-09-22 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 174.5 |
| fdafdcdf-0ee6-3496-b72c-7a400a6fefa6 | -3.405 | -59.5411 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3ecd806e-a704-35d5-8cdf-c1933c2acf95 | -5.9333 | -59.9899 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 330.3 |
| f0396b46-5a3d-34a8-8e4a-6fad55f33e7f | -9.257 | -46.1873 | 2026-09-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| ad05e700-133f-3918-8e1e-035b6700ad12 | -6.0925 | -57.6847 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| b400605c-e5ff-3851-a2cb-10dfbeb32dc8 | -3.4599 | -59.5209 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b2a29d57-c390-30d1-b9e1-075b4a061804 | -6.4671 | -59.9711 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bf23b612-874e-3ff6-a92d-e8c3cca98b93 | -11.5105 | -51.5116 | 2026-09-22 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ad2d2202-3a0e-3b41-91aa-f3c10f3078ff | -6.9683 | -47.4899 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b3ab6f4a-a2fb-3879-a356-0c126b35b5e0 | -12.2918 | -50.1417 | 2026-09-22 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d5a67c70-845d-3bd4-bf32-c2e11094f889 | -7.917 | -61.3481 | 2026-09-22 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d6ca9f37-92a1-3bd8-9c33-6c9bd46e0d20 | -7.1742 | -47.4736 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 9411dd00-b57f-3426-b683-dbbe341e30ec | -7.1553 | -47.4971 | 2026-09-22 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8a87913f-5400-33a1-bced-81f201b4dfdc | -8.4797 | -57.6282 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 206e091e-1516-3687-9efd-3b8f8b7d086a | -5.9151 | -59.9522 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d56dcacf-0227-3d12-aacb-3da48ed21847 | -9.3986 | -48.3213 | 2026-09-22 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4373efeb-1e75-3435-a491-f35be3c97b48 | -5.6411 | -43.3687 | 2026-09-22 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 505b46ee-348d-302e-bb8f-990c69c402bd | -11.4209 | -47.3603 | 2026-09-22 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7ac68de6-171b-3a91-93af-2d7aaa727d2c | -9.6009 | -45.923 | 2026-09-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 15492d35-0220-3043-8ab5-9c8bbb68d1f6 | -6.7776 | -47.8981 | 2026-09-22 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4a887955-f390-344e-bfdb-7c7686336045 | -13.5911 | -51.458 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3de9c7a2-1a98-332c-8100-242916757749 | -6.6704 | -47.3811 | 2026-09-22 14:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| b5f8dfb0-76c4-3bb7-bd3a-0b51b258c944 | -3.6033 | -60.5664 | 2026-09-22 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b55520d7-ce81-3d59-ab5d-0fad241241d4 | -5.9518 | -59.9701 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b8888771-ce5b-3e03-a95b-761ae38c4f43 | 3.7498 | -60.4684 | 2026-09-22 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e218606b-c353-3dd7-97df-7c6d0bc2797a | -10.4675 | -50.2624 | 2026-09-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 85631b97-e92c-3a2c-8b91-c15af2359dfe | -3.3 | -57.8681 | 2026-09-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| c487eb0f-d265-31ed-9e32-d8e25f178b6b | -3.0358 | -54.4085 | 2026-09-22 14:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5c073e1d-34f6-3b29-b8e9-3a6df91f03f2 | -9.6108 | -43.9477 | 2026-09-22 14:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 990f58d7-8459-3e4c-894e-11a35e476752 | -3.2212 | -53.9422 | 2026-09-22 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8524680a-b30b-3dfe-961b-e4afa07c3054 | -10.8569 | -57.1568 | 2026-09-22 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 13485dc2-f488-3766-b8a5-615eb3983f15 | -2.8608 | -57.8188 | 2026-09-22 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |


[Clique aqui para ver as próximas entradas](README140.md)
