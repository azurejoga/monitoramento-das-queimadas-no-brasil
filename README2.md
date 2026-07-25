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
| 2c566c0f-b891-3c94-af41-9412633ab026 | -4.37433 | -47.78584 | 2026-07-25 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c03f17b2-7686-36d6-8478-d28292fd72ca | -3.96418 | -48.12523 | 2026-07-25 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 15024363-b193-3aea-949e-d850001a5908 | -10.00111 | -51.48083 | 2026-07-25 00:18:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ecd26872-1577-3adf-86ee-91d24b2cae3e | -6.43359 | -46.21452 | 2026-07-25 00:18:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3ed8eb8c-58d1-3460-b8e2-3cab1383758f | -5.15452 | -47.53845 | 2026-07-25 00:18:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1643fbdc-5e53-3fa7-bea8-9c17d6190c08 | -10.8222 | -50.49676 | 2026-07-25 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9fee525-65ef-3c83-bd0d-91da355ebdb6 | -3.80503 | -51.1871 | 2026-07-25 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aef02db5-dc72-3964-af23-b06a203e9153 | -5.0868 | -47.94341 | 2026-07-25 00:18:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 89e0b8ba-96c2-3034-825a-edf8909537e1 | -3.79596 | -51.18835 | 2026-07-25 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1ee6d754-7451-3f34-a4de-a91ff8fbc8cb | -9.88445 | -49.98588 | 2026-07-25 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 901120a2-89d4-3bd0-9b94-357ccb7c8117 | -4.36998 | -47.75642 | 2026-07-25 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 9dd1d84e-42ca-3532-9d00-04367e65a147 | -5.0888 | -47.95725 | 2026-07-25 00:18:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7c5824aa-f3ee-3d59-94a8-547c9c4be771 | -3.73298 | -49.27608 | 2026-07-25 00:18:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 20df2a6c-155f-33b2-aa80-b953ee88a697 | -10.81205 | -50.489 | 2026-07-25 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| aa8ccff6-6a58-38a2-9c7b-0dd20cb390ba | -6.4366 | -46.20737 | 2026-07-25 00:18:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e9a35d36-461d-3f23-92cb-13896937d521 | -8.37829 | -48.21325 | 2026-07-25 00:18:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8b554b79-97d1-3a2c-8615-e4b668672149 | -8.83739 | -47.08488 | 2026-07-25 00:18:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8e1a6845-a296-3d89-9ba7-1a73334819e3 | -4.3774 | -47.7627 | 2026-07-25 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| a3d7d42d-3ce4-33ca-92cb-e9f2fe91b257 | -10.8046 | -50.5046 | 2026-07-25 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| fc278bbf-b022-335a-a51f-c6748c018423 | -4.3772 | -47.7844 | 2026-07-25 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3e13170e-5467-382c-8abb-f56e68d47c14 | -11.807 | -47.0858 | 2026-07-25 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| da9ead2b-aeb8-351f-a025-0ed131e7f51d | -16.434 | -49.9125 | 2026-07-25 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ae5e84f7-6551-30a4-aab2-c72683715aaa | -12.8543 | -44.386 | 2026-07-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c30080e4-c1e4-304b-aafc-722faf5fb0de | -5.1006 | -47.9422 | 2026-07-25 00:20:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 756a8c6c-9ad3-3bcc-8287-7f55e5ec9cc7 | -16.4537 | -49.9092 | 2026-07-25 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 99dbd0dd-e062-3a73-b5c7-be9e6768664e | -16.4542 | -49.887 | 2026-07-25 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 1c9065f1-0c8c-3118-b795-b6e34887b4cf | -16.4345 | -49.8903 | 2026-07-25 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| f03da268-aeab-37fc-8908-d095b9caf1b7 | -4.3588 | -47.7636 | 2026-07-25 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8902fee3-0401-3cb5-98e4-f9e435992351 | -10.8235 | -50.5026 | 2026-07-25 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e04252f3-3160-31ff-92af-25a4698fc601 | -5.082 | -47.9433 | 2026-07-25 00:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0df97974-55b3-322a-b230-abf4e1c860ab | -1.78548 | -55.53143 | 2026-07-25 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 25dc8b1a-0d41-3559-8326-030da440e62d | -2.81512 | -52.2866 | 2026-07-25 00:20:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6c6beb4b-26e6-3d82-b4e0-5f0aab0ba843 | -2.91238 | -52.7306 | 2026-07-25 00:20:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f9897b8e-2b73-37e2-b010-99b05bd9d10f | -1.78406 | -55.52104 | 2026-07-25 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2d2e2a6-334f-30d5-8226-d4b31af432a1 | -2.81634 | -52.29544 | 2026-07-25 00:20:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad0236c0-68c5-3b12-bd5e-b07d5ae330a2 | -2.43206 | -51.85375 | 2026-07-25 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbb47d92-c90f-381a-8506-ac94abc8341d | -10.8235 | -50.5026 | 2026-07-25 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 2e7ae734-541f-3e04-8fd8-3db264ab9457 | -5.1006 | -47.9422 | 2026-07-25 00:30:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 8374a614-612a-30b2-9413-06344aaf0904 | -5.082 | -47.9433 | 2026-07-25 00:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c8ac41b0-621b-359c-8f83-427324c406c7 | -4.3774 | -47.7627 | 2026-07-25 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1f46a55b-09ec-30b9-bd94-9a91269c37cc | -10.8046 | -50.5046 | 2026-07-25 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 86d81270-ede1-3d1f-a82a-2dd2cd79070f | -4.3588 | -47.7636 | 2026-07-25 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fd6b4366-af70-3207-a15a-1cdcd9b0b2fc | -11.807 | -47.0858 | 2026-07-25 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 4fd6705c-c0e9-31b6-a0e6-84d2647befdc | -4.3588 | -47.7636 | 2026-07-25 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 927ac23a-1e5f-38e5-ba9d-be37a8f69c28 | -11.807 | -47.0858 | 2026-07-25 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3e976a3a-eb59-372f-83a9-c308ed1bca78 | -4.3774 | -47.7627 | 2026-07-25 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| b2c491bc-5b65-3452-82f6-d59cd8d653d7 | -10.8046 | -50.5046 | 2026-07-25 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d34e69b0-26a9-3b5f-a791-c2df014a7564 | -4.3588 | -47.7636 | 2026-07-25 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ab721360-fa64-313e-9726-5cd26b0f81ba | -4.3774 | -47.7627 | 2026-07-25 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| bd00c26d-3e62-3f63-995e-ec21d86a87b7 | -11.807 | -47.0858 | 2026-07-25 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6cd8e11c-77d4-3b22-aa67-f94cc139cb1a | -11.807 | -47.0858 | 2026-07-25 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b2beb7a4-31dc-3437-8170-ec8443392f42 | -10.8046 | -50.5046 | 2026-07-25 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 61851fc4-0473-3cf9-805a-3d3bdc764b5d | -4.3774 | -47.7627 | 2026-07-25 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| bd7631e7-9013-35c2-a794-1302ab0a192d | -4.3588 | -47.7636 | 2026-07-25 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d6a0528f-f68e-3975-a227-1288ebe05658 | -11.807 | -47.0858 | 2026-07-25 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 273201d8-df06-391b-a73e-e50d01a8a6c2 | -12.0194 | -50.4969 | 2026-07-25 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9f7c0580-3b2e-37d8-9066-823ece5c5de6 | -4.3774 | -47.7627 | 2026-07-25 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c904a418-859c-3de3-a15a-178180cd5f9b | -10.0161 | -65.039597 | 2026-07-25 01:15:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 335716bb-c0d6-37bc-89bc-489f08504d52 | -8.7174 | -64.040802 | 2026-07-25 01:15:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce372dd5-73e7-33a0-8ee2-fbce537684df | -10.0177 | -65.046501 | 2026-07-25 01:15:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c40ebcd8-ca07-35e3-8b5c-aac6a98ecafd | -4.3774 | -47.7627 | 2026-07-25 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| d865dba3-2e40-3414-b2b7-a136db66f332 | -11.807 | -47.0858 | 2026-07-25 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f6a5037f-cfc2-3614-81ed-b7397f53b4c1 | -4.3774 | -47.7627 | 2026-07-25 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5752ff22-d55d-3d88-aa6a-fa5d26817a2b | -4.3774 | -47.7627 | 2026-07-25 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ca81414a-2612-3c50-bcbe-7b9a2c4ad5fa | -8.8954 | -60.598099 | 2026-07-25 01:40:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1f5439-4617-34f1-8d04-848202bfa7ce | -4.3774 | -47.7627 | 2026-07-25 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8bee48aa-feb7-3da8-a528-30041957d282 | -4.3774 | -47.7627 | 2026-07-25 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9306a89c-b02d-3afe-84ff-2724c021dfa6 | -11.807 | -47.0858 | 2026-07-25 03:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 63bc0769-a68d-3de6-b513-f69d03d3137e | -11.80316 | -47.09446 | 2026-07-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e49b50a-4c2c-3743-b65d-af0bda83ce0d | -10.26699 | -46.73697 | 2026-07-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e4b01c5-2d1f-30ac-9721-acc64bce14ab | -3.11857 | -40.99079 | 2026-07-25 03:47:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1db6644c-bfc0-3f45-8f37-25e2b259991a | -3.99595 | -43.28263 | 2026-07-25 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5364156-07a5-3caa-831d-766dafc95f4d | -10.26608 | -46.74168 | 2026-07-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23e513db-01af-3aac-a141-7d5fb07c928b | -11.79687 | -47.09303 | 2026-07-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d0b5884-9cba-3e2b-9db1-1d0163ca4117 | -3.11812 | -40.9898 | 2026-07-25 03:47:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70b589a2-3d89-3536-afae-4ee869dc1a51 | -12.19055 | -44.50024 | 2026-07-25 03:47:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da492355-ded5-32f4-bfb0-0fda869a6579 | -12.19354 | -44.50148 | 2026-07-25 03:47:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47bc68ba-7601-31af-8640-75c61b7539cd | -4.0562 | -43.24801 | 2026-07-25 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d64664e3-0451-343b-bb55-2cca17e122be | -4.06251 | -43.24527 | 2026-07-25 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c746e13-77a5-3b27-8eec-fc2fd38d286b | -10.68108 | -46.34786 | 2026-07-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e453ba96-521e-37e3-91b6-23e79a09950d | -4.43427 | -40.92175 | 2026-07-25 03:47:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db7cf1d6-587a-347c-9dcc-0eb1291dcdfc | -11.83444 | -44.75024 | 2026-07-25 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ead8c8d1-6ba8-3c5a-9f63-2a6d878ce393 | -12.18818 | -44.50051 | 2026-07-25 03:47:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74c769d4-2d4f-317a-b093-ef5a840d1b02 | -10.68009 | -46.35283 | 2026-07-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 491e8082-25bb-3d71-abe9-246004bf4a81 | -12.34223 | -48.2182 | 2026-07-25 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6a4a55f-bda8-35ae-b7eb-cb6e015d1a0f | -4.63062 | -37.70628 | 2026-07-25 03:47:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8fcf8f0a-a7e8-33f9-b984-8e42c6b06a89 | -12.84984 | -44.39524 | 2026-07-25 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a557b5b9-ba38-3fc9-8a07-4d9189298638 | -12.84461 | -44.39416 | 2026-07-25 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b295a6ce-06be-3c9e-b52e-ea98eee61291 | -11.83382 | -44.75339 | 2026-07-25 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f066b6a-39da-38b6-899f-6ab76d466eb7 | -11.80417 | -47.0894 | 2026-07-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d45e63f3-89da-33e2-ae59-432b2be75f15 | -3.99661 | -43.27876 | 2026-07-25 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62176954-ba7d-3e4c-b753-928b8c9880f4 | -4.62675 | -37.70564 | 2026-07-25 03:47:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f91063e6-9456-3c9a-9338-2f4907f39165 | -12.34095 | -48.22426 | 2026-07-25 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad4570a2-a066-318d-af44-6e23d635fade | -11.79933 | -47.09243 | 2026-07-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| be1640a3-c52e-3321-bdcf-b2e863fcbba8 | -12.8488 | -44.39463 | 2026-07-25 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b76fac3-edac-38e3-91e2-772d97b98fc5 | -4.06184 | -43.24911 | 2026-07-25 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 673ababc-4903-333e-99da-8c45ac16500d | -12.70092 | -43.98789 | 2026-07-25 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d124701-ebfd-30e3-a743-c035590ebd21 | -11.80038 | -47.08734 | 2026-07-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 94878758-c8f1-3c2a-85dc-6d952c0b5b44 | -11.79789 | -47.08792 | 2026-07-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3551b0a-f27d-345d-b72a-2ad16937b47c | -12.00489 | -49.26731 | 2026-07-25 03:47:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README3.md)
