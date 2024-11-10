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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c35b8b62-c53b-322c-a797-8c4a6991cb35 | -5.56682 | -43.9679 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c07b0e1-fe3e-380c-a1c1-974c28508985 | -2.60023 | -54.19312 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e25810e4-7f6f-3ab2-b568-7d0af6b2f312 | -3.24905 | -50.46808 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90e3ad8b-926b-303f-8072-6a856c8c04bb | -8.4008 | -44.1443 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a072df3-a3ef-3744-8042-ffca875fc82e | -3.68682 | -50.19621 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f849a8d-4097-3d57-89a4-c8411362c4eb | -3.86113 | -52.38037 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d4429e1-b4be-373a-90fa-e6e3edff97d0 | -3.12138 | -50.15292 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61d58c51-5509-31aa-82b2-11153204d9f0 | -3.79154 | -47.46995 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8611779-0172-3803-b653-260ca22892ad | -4.61965 | -48.89964 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c64c54d6-0394-3b3a-969f-49d2d2c80790 | -2.23314 | -53.73841 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3096db8-f251-3949-83f7-a99a9a7e355e | -3.68863 | -45.80984 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09d6ab69-56ec-332b-8d50-4a17939d8c6a | -2.89206 | -51.74932 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d161145e-8ef5-36a1-86b8-a46e05ff5ad8 | -3.96203 | -48.99128 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e21a624-b87c-3fc5-baf7-edcd631f464a | -2.78179 | -49.38982 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd0b73e6-e8cf-3452-93a6-e76260c3ee4c | -2.91319 | -49.82986 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b27faae-8ff2-3b2d-8144-2103fcee1154 | -2.69229 | -49.86511 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a790b23-4378-3a10-a0a9-e4e67c9485ae | -4.51062 | -45.72051 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129fd166-877a-3c57-8cb5-40e19ac11686 | -4.10784 | -50.73398 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0af0b565-387d-3acc-81e2-60aedd02dbcf | -8.38677 | -44.12227 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0aee6270-0ba3-38ec-9ce9-e08e82a560ae | -5.66566 | -41.75278 | 2024-11-10 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ceb7be82-81a7-3f2b-8d6f-3fabbb500c23 | -3.87226 | -50.2618 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0eb449c7-6409-3018-85fa-58e685878446 | -4.3114 | -45.48962 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad2ead2d-1b05-3ffa-9b42-c9b9513e2907 | -2.84465 | -49.82641 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c692e99-4f4a-3f1c-8dbf-ef94da0c6d93 | -3.22212 | -50.63522 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6faa3e17-b1ce-3dc8-bc0a-c8df81932668 | -3.98423 | -48.15884 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3280e807-df8c-3595-ad07-e7f8972970d7 | -2.65902 | -48.49706 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ab9624a-1640-327a-9bca-fd19d831aa2d | -2.89894 | -49.24702 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a112c41-4891-3e21-bf70-0d638cc7c73c | -2.9792 | -50.29831 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc04343-d78a-35b0-a37a-a01c812a1438 | -2.93187 | -51.4763 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 062fbc92-90f0-359a-ab5f-d4d93fcc0510 | -3.28582 | -51.52036 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 672e24f6-9ed7-3363-b418-6dcdce9cf3e7 | -2.71941 | -47.98318 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5cde7e7-1636-311e-9808-a573ba1c88d9 | -4.40136 | -48.60768 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab559bd6-74eb-3388-b9e3-9dd11dbb3289 | -3.23169 | -50.27032 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3efb96f-ab76-3c1c-b262-1f92d81c39e1 | -2.80383 | -52.53904 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58ed45e5-9e28-3db9-a0f4-0eb637833d9a | -3.06663 | -48.05891 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82c49cdc-5d37-3f82-999f-a60d623147f0 | -3.02085 | -50.45582 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 497b9480-f182-3e1f-9d6d-607a28c81b35 | -2.85613 | -49.22264 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab7b475e-d0f1-3f6f-b9b3-dcf7547054a3 | -2.04299 | -51.45916 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1497f478-0c1a-367c-a96d-97570c71bdc9 | -2.4213 | -50.49008 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f888ce8a-0b12-3e0b-ad71-e68f26267cbb | -4.38867 | -47.24382 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d3e1a5a-964b-3b50-a41a-27658ac356f5 | -3.43977 | -50.43346 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9ab329-51db-3b88-837b-07348350d62c | -4.38188 | -47.22036 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96967b96-2b91-3455-801c-75060835c275 | -8.38763 | -44.14625 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60f14af-6c3f-35f2-a1f5-173f99aee770 | -2.46366 | -50.40106 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9beed285-c2d4-346b-8a1b-fb5365293a94 | -3.98513 | -46.41119 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25e3979e-6166-392b-a48e-f2dc44fe68ad | -3.09387 | -50.23804 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 505a3796-8cbb-3af7-bbd6-622c781f2f05 | -3.24146 | -50.58086 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4819390-279f-3808-87b8-b0aa811c9842 | -2.71888 | -51.71144 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8701b383-c62c-3b91-a47a-71fe128c7f3d | -2.22517 | -50.63099 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b7b9854-4a0a-3a6e-9b82-cc871af301f4 | -7.39607 | -43.60056 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2778c860-8e96-3ab0-a7af-1e95fb9cdb42 | -2.38472 | -49.378 | 2024-11-10 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10b5e7db-ea0d-30ae-a4dd-46d665f0c8d1 | -2.61908 | -54.40442 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5007b40-edc4-3914-87b6-902aa1a7328e | -3.63602 | -50.18819 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcadaa08-1f42-348e-9d8f-97b1171a18e7 | -2.44636 | -48.96632 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfbf15b3-d5c6-3806-a888-76dacae5c5c7 | -7.63424 | -43.56288 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a915c330-23e4-3ffc-b473-f68426343544 | -2.853 | -48.44611 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 015363e5-3b18-395f-8063-68b00dfbb79b | -3.09313 | -53.32215 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2b95eb7-024e-3011-a2a2-8af40c07a763 | -8.3893 | -44.13459 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51200080-8bdb-3012-9ae8-68c106a57642 | -3.57151 | -45.82265 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b397b7-cebf-3f23-88ed-05af4aab411c | -2.87359 | -50.41448 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 803f035a-bf27-339f-95a6-dfbe1fbacd42 | -4.90571 | -45.86491 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ee6c013-94f3-3fee-a8ac-d61ab6d7bec9 | -3.18183 | -46.52187 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78cd35e2-392c-36a0-a4fb-121f76c32dcc | -4.10271 | -49.13002 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22201242-60ce-31d7-865d-65ac31559795 | -2.19423 | -50.22749 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6dd6a79-caf4-3d37-b62c-536d9bc63b24 | -4.95694 | -42.98488 | 2024-11-10 04:38:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 433b3217-cb04-39ef-ba7a-e481e891fc35 | -2.82862 | -49.44021 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| def7ee38-bacc-3ce7-9587-f689ccf28c28 | -8.60131 | -48.13966 | 2024-11-10 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4d56c45-a92a-305f-9782-7bd69a6956af | -2.88011 | -51.30337 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f254eac4-79ed-3d0a-8605-4b0f75f7c751 | -2.91191 | -49.489 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c697d97-6198-392c-a64e-a5d0956c709e | -2.1167 | -50.75129 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9362628b-3c74-39a6-be42-7cf56534ecd6 | -2.88738 | -49.62223 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aae11ad-9b74-39c1-adb7-9df78cd8c120 | -7.20575 | -45.03236 | 2024-11-10 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60440372-81da-369e-aac3-f1d52e00de5a | -2.22285 | -51.9951 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e745854a-21ba-3924-8599-5bb71d4c5fd6 | -2.21106 | -50.76614 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 457c636c-5c8b-3b41-8a8d-7631d52915e0 | -4.07125 | -48.31823 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346c387b-77fa-3fa0-98cb-6ed6ff1e1705 | -5.20972 | -48.34534 | 2024-11-10 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a3427c2-3815-3145-b30a-5ba183ecc30b | -5.2254 | -49.68776 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd41e6bc-9807-39bd-b55a-d6e165c2c70a | -2.43983 | -48.66441 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96058de1-3de3-31c4-acf8-2d4cb04eaba1 | -3.03167 | -48.04284 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab0169a8-5997-3927-a1b6-363aadca005a | -2.19051 | -50.33649 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5167d204-5959-3c69-ac71-e812f0d1d808 | -3.03137 | -53.27608 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f4f638c-20b3-3578-a8f6-2562fd9d4b93 | -3.23816 | -50.1857 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce8c4bb3-1449-3601-8429-f2d233fae905 | -3.24453 | -48.75462 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a830391-23fe-3b01-86b5-a3653f6c29a2 | -4.11133 | -45.70126 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee4af81c-4ddc-3c03-9b8a-eaa77b3f51b8 | -3.09773 | -49.42431 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6394c3ba-a6a1-3b69-9574-26fa9ebdf82a | -4.84956 | -48.40421 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cab7e78d-77e1-3a4e-a072-b3e7e82d3285 | -6.48658 | -46.85303 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2182b030-2067-31ba-9ddf-df3a0545ab60 | -2.71543 | -49.29647 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fbff456-9e03-35d4-ac51-d2afa0b38e22 | -3.3584 | -53.40751 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9dbf7c64-d291-3f94-bcac-bed2f60a08d5 | -8.382 | -44.12554 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f3b2c65-0bcb-31db-981d-45d4a6c5b541 | -4.38247 | -48.57639 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48f82657-d40c-39b2-9148-b93eaf18fd12 | -3.19512 | -48.6624 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c366832-3d0f-3cd0-b73b-1183b55380ee | -3.90178 | -46.44183 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67d2b154-dc38-384c-b47f-c53f067193a9 | -3.51055 | -53.79849 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d94f972b-4463-36e8-9680-9d21196b60ae | -3.69208 | -55.48949 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dce5fb6-3378-3d6c-9685-7f8e566ae61a | -3.19289 | -48.65499 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81dc581b-6e36-327e-b0c2-decbe8a4834c | -2.31889 | -50.58634 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30877675-6aa3-3df8-88e2-75b8b37b3be1 | -4.10342 | -45.7016 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95e1cfb7-6b65-379d-a582-371272689b73 | -4.24362 | -48.01673 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dce940b5-bf44-327a-9cb6-2f74f8fca70d | -5.27781 | -45.37533 | 2024-11-10 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README81.md)
