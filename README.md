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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd300fb-5035-3e15-bb37-43d5ea77b699 | -11.8176 | -45.3599 | 2026-01-17 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a2ab43d0-c54f-382b-b8e4-1db23dd5c535 | 2.7634 | -60.315 | 2026-01-17 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| fbceaeb8-dc1e-3eca-8a83-3fd3b88c838f | -11.7984 | -45.3627 | 2026-01-17 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a33dc1da-b57a-399b-a877-6cfee4d3ba2b | 1.1393 | -60.5222 | 2026-01-17 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f6b04624-0f24-3ecb-8b71-ffa2ff186d47 | -11.8172 | -45.3829 | 2026-01-17 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d5518d94-5200-3ccc-9324-d563b49ee21d | 2.7633 | -60.334 | 2026-01-17 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 90de419b-0b78-3d39-9b9d-d1634768bf1a | -6.3865 | -35.3466 | 2026-01-17 00:00:00 | GOES-19 | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 0e96a974-47a0-3064-875a-37658d506bb8 | -11.798 | -45.3857 | 2026-01-17 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e27fea16-ed41-38ba-94ea-112321804937 | 1.121 | -60.5224 | 2026-01-17 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dc1338a5-e802-3e65-a7cc-640e0c28d647 | 2.7634 | -60.315 | 2026-01-17 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7629fb12-330e-3e48-90c1-fff4f136e644 | 2.7633 | -60.334 | 2026-01-17 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a9bb25ba-6f64-3660-b26b-24a301e6a80b | -17.284 | -42.6479 | 2026-01-17 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 4db73a51-3d94-30a2-8e51-1e0d5894552b | 2.7817 | -60.3148 | 2026-01-17 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| fa9f629b-deec-37e6-ae2b-ad807e29830c | -12.6553 | -46.7633 | 2026-01-17 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 134935f4-3f79-3269-89ba-ee7a210371aa | -13.6993 | -55.6773 | 2026-01-17 00:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 84e4adbb-4b34-367a-a065-489e7e64fd98 | 1.1393 | -60.5222 | 2026-01-17 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e7e75898-2732-3da9-b370-39ac0255de13 | -11.8218 | -45.390202 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea1bb487-4231-3e68-91bc-1a9a89976c64 | -3.0109 | -41.8368 | 2026-01-17 00:14:00 | METOP-C | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 81f794c4-c082-3a1e-99ce-d6838cdf6865 | -6.3766 | -35.3494 | 2026-01-17 00:14:00 | METOP-C | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5704c618-0f60-3399-8c53-02bb36f4107c | -14.7851 | -45.944801 | 2026-01-17 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7b331a0-b725-340c-a1f7-27d74accf9ab | -11.8001 | -45.383499 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8e5e46b-26a6-3a46-9222-50c46017e293 | -10.1129 | -36.5037 | 2026-01-17 00:14:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 5a23ec77-9f63-371f-8beb-c7cd0a7a61b4 | -12.6658 | -46.776699 | 2026-01-17 00:14:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4312717-a106-3ffa-9608-3e0467892b9d | -10.1152 | -36.5131 | 2026-01-17 00:14:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| be5073e1-6c32-3e13-b597-8c370ef0faf1 | -5.8126 | -39.096699 | 2026-01-17 00:14:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ba1c03c-cd86-3e0b-8ef1-4179ba93388a | -6.9002 | -42.850899 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9175b90-1f7d-3ded-b351-0ab2bd08e234 | -5.8108 | -39.088902 | 2026-01-17 00:14:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5c45d9fc-7a2c-3458-8ff7-8a8d04d93e5f | -17.275101 | -42.664501 | 2026-01-17 00:14:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0a8306c2-2303-3564-bb17-644d1c086a6f | -11.407 | -41.4188 | 2026-01-17 00:14:00 | METOP-C | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b01a6d38-cac6-30d2-bf3a-da8441de7d1d | -11.8099 | -45.3815 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1761ffe2-3857-361e-ae95-f372d71ad10b | -10.1951 | -44.8993 | 2026-01-17 00:14:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9597707-e60d-3308-b389-f6e6c046e3c5 | -6.7021 | -43.0686 | 2026-01-17 00:14:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71151e77-f17d-3c0f-b33c-bf93dbbac301 | -11.3277 | -44.499001 | 2026-01-17 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 940db96b-5872-333f-858e-d295ec274d49 | -6.3669 | -35.351799 | 2026-01-17 00:14:00 | METOP-C | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d8ede447-25d9-3217-a31f-15f6c8150037 | -14.7877 | -45.957802 | 2026-01-17 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5b5ab35-7f06-36c1-b342-af4337529935 | -16.055099 | -39.1301 | 2026-01-17 00:14:00 | METOP-C | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3cfc6dd4-a9d4-3c49-8a01-abbfa4030a7b | -4.5921 | -45.998501 | 2026-01-17 00:14:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db41a0b4-20e0-396a-a254-5d72aeb087a7 | -17.284901 | -42.662399 | 2026-01-17 00:14:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53ae00b1-c371-3558-af68-db5617d1d7df | -6.9018 | -42.858101 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b6e686a-d655-3ae8-bce8-7e9339ae1897 | -11.8173 | -45.368698 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02b14891-7ef5-3f35-9b09-9b6679ac33ff | -13.7075 | -45.487801 | 2026-01-17 00:14:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd8ee29-4bd7-3974-9df2-aa47385ac884 | -6.3736 | -35.337002 | 2026-01-17 00:14:00 | METOP-C | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8531213d-9fec-3d10-9b50-d19de7eec264 | -17.286699 | -42.671398 | 2026-01-17 00:14:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31006a61-3d9a-35a9-b647-77d40eed4315 | -10.562 | -44.318001 | 2026-01-17 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 628cb9d2-73c1-3995-a3fb-2b93756ad85e | -11.8121 | -45.3923 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e605b74-2f55-36da-81d4-f8a6b5bb49d0 | -14.7508 | -45.9249 | 2026-01-17 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9e814ad-5294-38c0-a5e3-e06d2f984eaa | -13.7051 | -45.476101 | 2026-01-17 00:14:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c872409a-7582-31f0-85c7-ce6db89512a7 | -10.7811 | -44.431999 | 2026-01-17 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74ed6c44-bed0-3a0f-90d4-03adf490a853 | -12.6533 | -46.764999 | 2026-01-17 00:14:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1a704b7-b3a3-3dc7-b7ff-4f16cfaef78c | -11.8196 | -45.379398 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 362a8cae-1d62-3cf4-aaa3-01e9ffacbcbd | -11.3297 | -44.5084 | 2026-01-17 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 521e1a24-15cb-3cb5-b4fe-7ff07e1eea00 | -5.4908 | -39.531601 | 2026-01-17 00:14:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d7e9493e-4c60-3f7b-b053-0212242b71b3 | -6.3639 | -35.339401 | 2026-01-17 00:14:00 | METOP-C | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2214650f-84bf-3a74-a47d-6e7121a7003f | -6.91 | -42.848701 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d5d2203-cf2e-3f0e-afb6-dde1bb053310 | -8.437 | -44.027 | 2026-01-17 00:14:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8e6ad3-681f-3b8f-81c2-a7461a623a37 | -6.8986 | -42.8437 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 110da4c2-72a6-3bfa-b419-fa10364427d6 | -11.8076 | -45.3708 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3d38d25-8724-3564-8eae-4b6b9c41179d | -10.5022 | -36.963699 | 2026-01-17 00:14:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09e18eed-5c74-32a0-a590-ebb40c839b9c | -5.8902 | -39.297001 | 2026-01-17 00:14:00 | METOP-C | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 11cad579-455e-3d0c-a2d3-9b9d861e2928 | -15.2565 | -42.990002 | 2026-01-17 00:14:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1f7fba67-3a07-3977-9eea-9cf8d68f571a | -11.8023 | -45.394299 | 2026-01-17 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09cd5b2c-cf73-32ab-b531-1dd10376b7f1 | -5.4926 | -39.539001 | 2026-01-17 00:14:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 131ce4e6-018b-3104-ade5-e6da70901f17 | -8.4388 | -44.035198 | 2026-01-17 00:14:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd80f42b-9b9d-3cf6-97c1-cada25a0e762 | -4.3259 | -45.359699 | 2026-01-17 00:14:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb789ba0-67d5-3e63-8c49-a737eac1c47a | -6.3864 | -35.347099 | 2026-01-17 00:14:00 | METOP-C | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 2b0f0df3-441c-357a-a6e8-b4e1333f3e1e | -10.5043 | -36.972401 | 2026-01-17 00:14:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1bd9b73c-336a-3a72-bb2b-4f11eeb5a9de | -12.6561 | -46.778702 | 2026-01-17 00:14:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 777ab882-1b3c-3663-afa6-9a4f7d1bcfce | -10.6131 | -44.651901 | 2026-01-17 00:14:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76d75cca-9f87-30b9-95f6-4fe98bf848d2 | -6.9867 | -42.8694 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22ee8e9b-d34f-3de1-a2d7-3c43688eeee7 | -15.2663 | -42.9879 | 2026-01-17 00:14:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| b9ce1554-a3f1-3d3b-8d54-6007c995c4a7 | -6.9883 | -42.876499 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c418dc27-56ab-3f20-9b67-4a3802170479 | -10.5639 | -44.327 | 2026-01-17 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2b38365-b9d2-30bf-b1bf-af8a6b90f4a8 | -6.9965 | -42.867199 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 776ff604-54b7-37ec-b84e-3dc14af7abc0 | -12.0852 | -43.776402 | 2026-01-17 00:14:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4504ba9b-980b-3868-a8f8-845bbaaa6d10 | -14.7903 | -45.970798 | 2026-01-17 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90457d4b-e38e-37a2-b092-01122e3cf826 | -3.0125 | -41.843601 | 2026-01-17 00:14:00 | METOP-C | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 409908a1-f14a-37a8-8373-ae7ef22c76af | -12.663 | -46.763 | 2026-01-17 00:14:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9167f77f-25a8-3234-94da-35c79b8b24af | -8.4534 | -45.134499 | 2026-01-17 00:14:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78247ef4-3707-380e-8009-508a31cc5968 | -12.095 | -43.7743 | 2026-01-17 00:14:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9331f38d-1cf5-3b22-a32c-e5895225c479 | -6.9084 | -42.841499 | 2026-01-17 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 13fb1cc0-54dc-3899-8e73-d1b2e3ff6031 | -3.8918 | -47.596001 | 2026-01-17 00:14:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c02e00-3758-32ed-9f04-da2631551ff5 | -17.283001 | -42.6534 | 2026-01-17 00:14:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7b8bf6d-739f-3d9b-8a6c-2a64c3b69c0a | -6.3796 | -35.361801 | 2026-01-17 00:14:00 | METOP-C | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| dbf952a2-75d2-3006-a174-05a5cec542ef | -11.0153 | -44.714298 | 2026-01-17 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85f5779d-c916-3236-bb14-f63ae7128077 | -8.4352 | -44.018902 | 2026-01-17 00:14:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67e685b4-579b-338b-8a94-f956feca28d3 | -16.0567 | -39.137199 | 2026-01-17 00:14:00 | METOP-C | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0da6886-0bfa-357b-8b8c-2b5a191f319c | -9.6504 | -41.894901 | 2026-01-17 00:14:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 27e1dfd5-d61c-3735-ae12-ed552e0c3efc | -9.652 | -41.902 | 2026-01-17 00:14:00 | METOP-C | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f052d7d8-9fc7-3ad6-8af8-0730f7dfbc6f | 2.7634 | -60.315 | 2026-01-17 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ab6edcce-3a4b-3604-b28c-71598d3c1fe2 | -11.8176 | -45.3599 | 2026-01-17 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7e497153-50b8-3d7e-b9ac-ff9fc3dcaefc | -13.6993 | -55.6773 | 2026-01-17 00:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| cb029f6f-e7a5-3e5a-a45b-135f3b4a4098 | -12.6553 | -46.7633 | 2026-01-17 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1c5a0a97-af47-3064-9888-f918b9c9651b | -17.284 | -42.6479 | 2026-01-17 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f806ed86-0a46-39e1-b688-5c6efabb83d9 | -16.5841 | -57.8115 | 2026-01-17 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| d332fd1f-d818-3f97-9622-2a54ad1aa6ad | 1.1393 | -60.5222 | 2026-01-17 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 464b6632-df03-3180-ad41-ab10178d94cd | -17.284 | -42.6479 | 2026-01-17 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 6a84afd2-8a83-3e79-b19b-2935f3491b8c | 2.7634 | -60.315 | 2026-01-17 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 03e4a97d-ab7f-37eb-b576-d9023f2f1760 | -13.6993 | -55.6773 | 2026-01-17 00:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 22a61922-b417-3f6c-9aff-31d501742f9f | 1.1393 | -60.5222 | 2026-01-17 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3f1d901f-6bb6-3592-8352-44c41634cba4 | -12.6553 | -46.7633 | 2026-01-17 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |


[Clique aqui para ver as próximas entradas](README2.md)
