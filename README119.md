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
| b8c94842-03db-3ebe-9ad6-c60af3d67312 | -6.93692 | -48.17759 | 2024-10-09 04:38:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c764bc-80c6-3f23-9d9e-a9e7cf519e08 | -6.92847 | -44.57104 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51f2a472-0c84-3ecc-bb0b-343167d8debe | -6.92769 | -44.57629 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d00b71b4-88fa-3e61-99ea-9f71142bb5e7 | -6.91483 | -59.03501 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46f7ce56-c0e7-31c8-b23c-2b2a0a460d33 | -6.91386 | -47.65368 | 2024-10-09 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 547fe9aa-0c15-34a0-8ad3-ebf0b1e4b2e9 | -6.90932 | -59.03405 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd67f5fe-64ba-3a3a-a086-ae3c6e6048a8 | -6.908 | -51.25849 | 2024-10-09 04:38:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bac95d7-b4ef-3fdd-90d0-3e96f4c1769f | -6.89903 | -52.19444 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b278adf5-7fa0-38f9-93bd-d2f409787b51 | -6.87268 | -55.31366 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63b59e94-a04f-39f1-b186-206f37f42f4d | -6.87199 | -55.31779 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 524596eb-e6a4-30a8-ae8d-5b8b6398a461 | -6.87115 | -55.31197 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f16d5d13-12d7-3d41-9804-f27dbf873635 | -6.87043 | -55.31609 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3859221-c91c-39e6-b2b7-63709eb39778 | -6.85194 | -46.93528 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbb080d7-cb7e-34cf-8dd8-c91aec14db61 | -6.85191 | -47.33153 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a983bbd-67b8-3330-8bef-6b56d3c547fd | -6.84116 | -51.06621 | 2024-10-09 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea590cb4-d53f-32a0-b051-c28b40e36ece | -6.84056 | -51.06989 | 2024-10-09 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27de8ce8-48c6-36ef-8457-f84dea7aa77f | -6.81009 | -59.1469 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d76c635-cf7e-30db-afef-2d49da039331 | -6.80455 | -59.14582 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b70496c-2a67-31cd-8984-c0a3cbe84f40 | -6.8024 | -59.35309 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f21a24cc-7b6b-3976-8bb1-7953a2a508b3 | -6.80172 | -59.35691 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f20f00bb-a8ce-3913-b570-c5843cc07551 | -6.79679 | -59.35195 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a180ede9-35ba-3f2f-97f2-cb8b8c2027b5 | -6.79611 | -59.35582 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d22d9e0e-251f-34d7-ae9f-816b7e4e98ad | -6.79186 | -59.34702 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e148735-35a5-3624-8265-fb68a20bc937 | -6.79118 | -59.35083 | 2024-10-09 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c02feb9a-65fd-3549-86bd-5f1fd157dc2c | -6.7843 | -51.6575 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84946e6a-9942-3961-a247-6506f2ca5b0d | -6.77428 | -60.04896 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| dc6b6032-c03e-3ae5-8ef1-15ac934e30c6 | -6.7735 | -60.05334 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 74952e29-702e-3985-8ac7-f3e7a48e4a8d | -6.77272 | -60.05774 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| aebc3bfe-3036-3f13-b4af-b3327effc5f0 | -6.77195 | -55.49008 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02a9805c-5dac-30be-a336-538ae418e26c | -6.77193 | -60.06215 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f971a019-1a78-3793-9cc3-21d51f245164 | -6.7684 | -60.04786 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 80372cfa-1936-3684-971f-be79d276c6da | -6.76762 | -60.05223 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5f980950-d9fb-3f87-b3fe-b9784394a147 | -6.76683 | -60.05664 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1ca77328-619d-3b73-a562-00da870309ed | -6.76602 | -60.06115 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b5497299-b467-3376-ae63-56e55119dfd3 | -6.76171 | -60.05127 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a206fdab-c051-349b-b1bb-da886331e906 | -6.76092 | -60.05565 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9351da11-3f87-3aec-88e0-ce45a3df91f8 | -6.72946 | -44.29271 | 2024-10-09 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30c24939-c660-34a7-8702-60fc81eaac77 | -6.72516 | -47.22387 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5970913-ac9e-3e27-a976-d265a0c3df73 | -6.69933 | -46.46673 | 2024-10-09 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c761c85-f587-36e2-a47a-189caefbd3b3 | -6.67043 | -47.10689 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dd112ea-0292-3451-8fb7-3b90004972c6 | -6.66695 | -47.10633 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ec038ee-98d6-3de9-83f6-7431a42e0bf7 | -6.66634 | -46.33668 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edb66b25-04ac-3c94-94e9-d277341cfcd2 | -6.66572 | -46.34074 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bc8f7d0-5e59-3059-b6b4-108294152988 | -6.66348 | -47.10579 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a888ce39-bf3a-37c2-8ad2-eb981dc58b10 | -6.66274 | -46.33612 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22f752a1-c23d-3c74-9a83-ae6494e2c629 | -6.66 | -47.10526 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb15590d-cb9f-3e13-affc-c9fc8ac1a910 | -6.65941 | -47.10908 | 2024-10-09 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e77679d-e788-3aa7-91b1-9667c2086f26 | -6.63635 | -55.3835 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27494af1-2333-3134-a84e-a98f71f2ea33 | -6.62115 | -47.07977 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30c69569-91bb-350d-a66b-c3bda7be98b9 | -6.62057 | -47.0836 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9e8f184-57ed-3683-9c59-337d08b1d134 | -6.5758 | -49.66203 | 2024-10-09 04:38:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d69399c5-8a31-31a1-8c86-6d24b2f0b680 | -6.57248 | -49.6615 | 2024-10-09 04:38:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01faac18-5010-380e-8108-dc58ca0de2b1 | -6.54518 | -59.99711 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82a62361-6353-3ad4-843c-29ed6f8030b9 | -6.54442 | -60.00137 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b78c908b-c549-35b2-915a-6e2894aab9b1 | -6.54365 | -60.00568 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e8eb7a8-f7b7-3e53-9a6f-d89f94ac22db | -6.53082 | -58.41972 | 2024-10-09 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4efb3369-7c3f-3fe6-9f24-9e34351bbfd7 | -6.52552 | -58.41865 | 2024-10-09 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ad5f78e-447d-37d8-baa6-dc38af3c25c8 | -6.52493 | -58.42202 | 2024-10-09 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f2d0f08-2701-3cd9-94bb-c7f504062f79 | -6.52435 | -58.42534 | 2024-10-09 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55222180-ab91-3472-a208-a05ad440041e | -6.52256 | -58.40422 | 2024-10-09 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b755033f-3bca-36ac-ad41-9386d1b64b52 | -6.52198 | -58.40752 | 2024-10-09 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5febfd55-aa43-3685-b01d-7d9df19d696b | -6.51265 | -52.54876 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0fafd8a-7e1e-3fd9-aaa1-6612a8933ba7 | -6.50954 | -44.00817 | 2024-10-09 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da877bd4-0275-38b3-9f00-efdd45fc3f08 | -6.50168 | -44.15006 | 2024-10-09 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ad7f5b-1ccb-3d35-b4be-61eb98a6cb7a | -6.48782 | -49.91598 | 2024-10-09 04:38:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb84f42c-5cb2-350d-a953-5d1a55c6b4e4 | -6.48504 | -49.91195 | 2024-10-09 04:38:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e967ed0-5e4e-381d-9f54-7d4ad63ad46b | -6.48449 | -49.91545 | 2024-10-09 04:38:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9c09ace-3d09-386c-a9e2-33f5c6b04ce7 | -6.44335 | -47.06153 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4c8fc3c-c88d-3c40-b9da-fa3e69a24acf | -6.43764 | -50.12357 | 2024-10-09 04:38:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d7a421a-f36b-3da1-bf9e-7ea95ce6dfde | -6.4343 | -50.12305 | 2024-10-09 04:38:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b118c7f-573c-351a-b8d4-fc4df73bbf16 | -6.433 | -55.63164 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8d7c960-f2a2-3fea-bed4-7d1a73fd2c02 | -6.4286 | -55.63087 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9802b7b-3d14-387d-acb1-c16d59214340 | -6.41802 | -44.59642 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9966b156-d582-3bb8-aac1-ff13991d40b1 | -6.41623 | -44.59867 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f198e1f9-ba6c-3ea7-8d58-bdc446ee85ba | -6.41406 | -44.59581 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81b10429-7f43-3307-a386-b8a0e173b64c | -6.41329 | -44.60085 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d466c26-c15c-3afc-9605-e06400d6f280 | -6.40892 | -51.70512 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e763cce1-1392-3fd5-af91-cb2efa3af50a | -6.40829 | -51.70895 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba828258-de99-32c9-a4a7-ebdde625b0b4 | -6.40766 | -51.7128 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f93820f-dc73-391b-8e78-24aa4b7e626e | -6.40478 | -51.70844 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce39edf-9740-35ce-8250-56c2e1cd35ab | -6.40416 | -51.71227 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65e02ba5-5155-381c-8fbe-8200953ffbd9 | -6.37085 | -45.87563 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0f9473b-15a0-327a-a18c-32cd10555137 | -6.32439 | -45.71947 | 2024-10-09 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48e53d7c-5351-3158-acd3-521a5bb1cda9 | -6.32287 | -46.38917 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e281390-69d3-3e5b-aa1f-1c31c890c4d3 | -6.3083 | -50.81711 | 2024-10-09 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5340c3-a50e-361b-a365-c2e2e866b415 | -6.30772 | -50.82073 | 2024-10-09 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00881ea8-8eaa-36ff-885e-f9336b8aba2f | -6.30714 | -50.82437 | 2024-10-09 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2aca72b7-25e8-373a-8497-ba0fd8ada199 | -6.3049 | -50.81656 | 2024-10-09 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2459161-5086-3a32-9158-a2eee77e8c72 | -6.28909 | -46.99182 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea2edb02-2067-384d-a8f8-6428f38155ba | -6.26869 | -44.04955 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd1d0ce0-a953-30a1-99e1-60ca42c71c4c | -6.26743 | -49.06565 | 2024-10-09 04:38:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e6f4653-b738-37fb-9d83-bb3df8d2f3fa | -6.25333 | -44.815 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 227abab6-27f1-3f66-a608-f53e30b5f74c | -6.23579 | -49.45557 | 2024-10-09 04:38:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a0ed009-739a-312e-8417-7b890d455b25 | -6.22367 | -44.18338 | 2024-10-09 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c9529b5-83e7-3e88-92ea-eb516e6765af | -6.20899 | -51.5158 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e91e9f7f-5024-318b-8e9b-8e06d6d566ba | -6.18003 | -44.44884 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 336fc6b8-1047-36f0-b073-87c4e96d6851 | -6.17692 | -50.89762 | 2024-10-09 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2432b76-7786-3288-a7a4-065ef0c43c3d | -6.17602 | -44.44834 | 2024-10-09 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2faf59f5-058b-3958-9337-a5cf9c5cb097 | -6.16996 | -55.4854 | 2024-10-09 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44f75375-e5cb-307a-a619-eb6b6149cc82 | -6.16769 | -55.47202 | 2024-10-09 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README120.md)
