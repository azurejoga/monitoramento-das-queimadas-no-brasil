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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd78f6b-e6a9-336d-9c83-7e87783bcdc4 | -10.9579 | -46.5467 | 2024-10-03 00:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| fe914bf6-b115-37dc-a351-ce760d156179 | -10.9769 | -46.5443 | 2024-10-03 00:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6968832d-1efc-3f5a-b62d-e9a75fe796e3 | -10.8942 | -63.8971 | 2024-10-03 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 51d68cc0-fc5c-3526-8d07-f2d9848d4d31 | -11.2565 | -60.6019 | 2024-10-03 00:56:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f303efb3-b63b-3094-9d2d-b77408610a33 | -11.2566 | -60.5825 | 2024-10-03 00:56:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4b95fce3-b276-3bb3-a44d-906989450d37 | -11.6742 | -65.0172 | 2024-10-03 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d0e96ed2-0d22-3c3c-9a62-f818f26ae5a5 | -11.693 | -65.0163 | 2024-10-03 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 72428add-0b8e-3f0d-a821-9d76058e2086 | -12.4038 | -63.0009 | 2024-10-03 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 6c328001-d92e-31ee-8d98-16ba49212aa3 | -12.404 | -62.9817 | 2024-10-03 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c98be59a-63bd-3c07-b1e0-7b8253cdbed4 | -12.5329 | -53.1212 | 2024-10-03 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4fed2082-8404-3474-85aa-dd2fde155475 | -12.5332 | -53.1003 | 2024-10-03 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 09218102-87da-3d6c-bdda-2122c3285853 | -12.6484 | -63.1214 | 2024-10-03 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6cbdce6b-840a-3552-80d8-0f3de52d0955 | -12.6486 | -63.1022 | 2024-10-03 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c8849e95-c2be-3fa3-8d03-950780c6341a | -12.786 | -62.4982 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 910c4c40-0f3d-381c-90cb-04c39e805b9f | -12.8047 | -62.5163 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 520c1922-62df-3d10-baa2-b68b52fcd443 | -12.8049 | -62.497 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 32670c0a-bb05-39fc-ae70-c34762e9d5bf | -12.824 | -62.4766 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 014411c5-92b8-3b4f-a09d-7b8372949c6b | -12.8808 | -62.4731 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 784b710b-6786-3265-bdc6-326ae28d49f2 | -12.881 | -62.4538 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| f0609477-8760-3a97-b153-105042977d20 | -12.8996 | -62.4913 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 919fc930-8816-37a9-ad95-94bb68dbfdeb | -12.8998 | -62.472 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 3c9f0578-144c-3851-a115-566b26187d7a | -12.8999 | -62.4527 | 2024-10-03 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 6caa1240-2f2f-3f07-b9d6-3e94f1afd3cc | -12.9167 | -62.7022 | 2024-10-03 00:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0e756a4c-fd3d-3987-9c3d-81550bd673a9 | -12.9187 | -62.4708 | 2024-10-03 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d344d78e-243a-388b-8ba2-d0e3cd96d72b | -12.9741 | -62.6409 | 2024-10-03 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 42fb2ef9-583d-3ee5-b296-ee2dcbfe79df | -13.5195 | -51.1467 | 2024-10-03 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3b65defc-27e9-30ee-811f-af9d1e457710 | -13.5369 | -51.2514 | 2024-10-03 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b30da370-75dc-3954-8533-10261aaa1a60 | -13.5373 | -51.23 | 2024-10-03 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4f5022f5-5fee-3f3f-8efb-21123b259be7 | -13.5562 | -51.2489 | 2024-10-03 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 6322107f-7fbf-3f70-b902-73a9f5927f68 | -13.5565 | -51.2275 | 2024-10-03 00:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 76a6612f-0e19-3e2d-8acd-707473c642ab | -14.7017 | -48.7559 | 2024-10-03 00:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| e7a58633-cc3a-3496-b525-60f2c9f13f18 | -16.5778 | -58.2386 | 2024-10-03 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 4779830a-c834-322c-9686-34193be4a158 | -16.578 | -58.2183 | 2024-10-03 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| d5a3f13b-092d-39b9-982d-5d390d67bb1b | -16.5973 | -58.2365 | 2024-10-03 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| d5d15c34-04b2-3735-b8b7-cc1ec85c73b8 | -16.5976 | -58.2162 | 2024-10-03 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 5c219663-f345-3450-aa8a-b991ba2a693a | -16.7594 | -57.8328 | 2024-10-03 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 882682ed-65fd-3184-8874-de22f142043e | -16.7597 | -57.8124 | 2024-10-03 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 29836b40-82db-3bac-8a74-9f7787e64498 | -16.779 | -57.8306 | 2024-10-03 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| e227e018-5b84-3c67-a197-5379c8357e17 | -16.7793 | -57.8102 | 2024-10-03 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 6fe97cd3-7c95-343f-8391-b68cc6093a26 | -17.2717 | -40.2853 | 2024-10-03 00:56:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| b481bd0f-a800-3c43-9db6-b5e7c9b18415 | -16.7985 | -57.8284 | 2024-10-03 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 2f701c60-4480-37c7-a525-a6e27166784a | -18.8935 | -41.199 | 2024-10-03 00:56:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 5d02d983-0234-30a9-a680-ea94d02c1181 | -19.0344 | -43.1944 | 2024-10-03 00:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| a1672337-f096-3d7e-946c-6c65730745f0 | -21.306 | -47.6227 | 2024-10-03 00:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b669741a-9d76-37e4-9c36-a8fd04861164 | -21.3067 | -47.599 | 2024-10-03 00:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 71.2 |
| da91285d-f37e-3241-ac95-b54b5b73cad7 | -21.3875 | -47.6497 | 2024-10-03 00:57:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b1faf13d-af26-3f6b-916d-e1b183a3ce7d | -21.3882 | -47.6261 | 2024-10-03 00:57:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 40b9a9e4-abc9-3abb-bc8e-67821b819e80 | -21.346 | -55.6626 | 2024-10-03 00:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 9964fd92-4dfc-3e2a-8af5-db5f00f7f194 | -21.8445 | -48.2178 | 2024-10-03 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 48f686ef-2ac6-3379-9919-ce321f6d7b57 | -21.8452 | -48.1943 | 2024-10-03 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c4620642-f567-382f-8a9c-ceec930becbe | -21.8653 | -48.2127 | 2024-10-03 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4318a8ac-f6da-3317-a703-3a7046534ba3 | -21.866 | -48.1892 | 2024-10-03 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 347275a8-1dee-3997-800a-47f3001a5ce4 | -22.2515 | -48.4456 | 2024-10-03 00:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ba7bf5e9-d57b-380a-a2df-50efdaebcb19 | -22.3704 | -47.9462 | 2024-10-03 00:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e9133a40-525e-3e04-b606-9de1db72f571 | -22.3711 | -47.9225 | 2024-10-03 00:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e38f74f9-9ec2-383e-a005-bc97dd71a1d5 | -23.293301 | -45.299801 | 2024-10-03 01:01:08 | METOP-C | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b834207-62b7-3ac1-89e8-57fbbffec403 | -23.1472 | -45.125801 | 2024-10-03 01:01:10 | METOP-C | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac38ecf3-14da-35b5-81fa-1d75253e9b4f | -23.1495 | -45.135101 | 2024-10-03 01:01:10 | METOP-C | LAGOINHA | SÃO PAULO | Brasil | 3526308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9773ef99-b7eb-329d-86f7-b75f211df407 | -23.3398 | -46.985401 | 2024-10-03 01:01:14 | METOP-C | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 043380b2-091c-36a5-a319-c1247d5ac24a | -22.0723 | -42.093601 | 2024-10-03 01:01:14 | METOP-C | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68067411-1d0c-3fd0-a46f-3491f9020901 | -23.2104 | -46.7841 | 2024-10-03 01:01:15 | METOP-C | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8305a08-a16a-3e73-ba77-bc241262026a | -22.1488 | -42.540298 | 2024-10-03 01:01:15 | METOP-C | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0e1d21f-8f0e-350e-883f-5caef9c0ddfe | -22.7365 | -44.889801 | 2024-10-03 01:01:15 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff39b8b1-d35d-31ac-bd4b-fad6b22cf2db | -23.085699 | -46.603901 | 2024-10-03 01:01:16 | METOP-C | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0824589-2cdf-3137-ae83-197ffcf285ed | -23.087601 | -46.612 | 2024-10-03 01:01:16 | METOP-C | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a3e79c9b-f201-3b4a-83b1-8c074387cca2 | -23.0895 | -46.620098 | 2024-10-03 01:01:16 | METOP-C | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7505fe3e-f664-36e7-ae3a-4929a2d91bd5 | -23.077801 | -46.614601 | 2024-10-03 01:01:16 | METOP-C | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 390d88c5-f405-3edc-8934-901e8e70565d | -23.0797 | -46.6227 | 2024-10-03 01:01:16 | METOP-C | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 767e6229-d5f3-37b3-af30-1efba5306f24 | -22.6157 | -44.6535 | 2024-10-03 01:01:16 | METOP-C | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e50d9f09-7e34-34fb-b3a0-942783a27b20 | -23.0268 | -46.8843 | 2024-10-03 01:01:18 | METOP-C | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 936ee29f-0bce-3eb1-abee-645223d2f388 | -22.5357 | -44.833401 | 2024-10-03 01:01:18 | METOP-C | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2078365c-5666-3b03-8a77-aed4a27bf59b | -22.525999 | -44.836201 | 2024-10-03 01:01:18 | METOP-C | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f148aacc-143c-36eb-9d5a-068954232fe4 | -22.528299 | -44.845901 | 2024-10-03 01:01:18 | METOP-C | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7b2747c-f246-398a-895f-4038a3df4a35 | -22.3109 | -44.0583 | 2024-10-03 01:01:19 | METOP-C | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f3ad904-1c2a-3ab7-b1ea-c4d737bac5ca | -21.561199 | -41.240898 | 2024-10-03 01:01:19 | METOP-C | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2d16cbd-d428-33bc-a33f-81949e7308bc | -22.298599 | -44.0504 | 2024-10-03 01:01:19 | METOP-C | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34a0773f-d189-3a9a-bc45-1ebfd3b8679d | -22.3013 | -44.0611 | 2024-10-03 01:01:19 | METOP-C | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e073f24-78ac-3b84-85d2-3cf808026cf1 | -22.304001 | -44.0718 | 2024-10-03 01:01:19 | METOP-C | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7ba7c24-fba6-303e-a9e8-d5d4ca31484d | -23.0861 | -47.5471 | 2024-10-03 01:01:20 | METOP-C | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b52a2da-d1ac-3007-8252-d85f82b98694 | -23.0879 | -47.554798 | 2024-10-03 01:01:20 | METOP-C | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0782184-3670-3ed9-8b23-eb2d93d78e58 | -22.7847 | -46.821999 | 2024-10-03 01:01:22 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dff77814-523a-3486-9682-be88d2fa6818 | -22.7062 | -46.6632 | 2024-10-03 01:01:23 | METOP-C | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75429e18-2174-34c5-adcd-e4113826f311 | -22.708099 | -46.671299 | 2024-10-03 01:01:23 | METOP-C | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2b562e6-8617-3a68-a4e0-edea66c17119 | -22.6984 | -46.674 | 2024-10-03 01:01:23 | METOP-C | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad3c29bd-b50d-3398-9fcd-bda735e9090f | -21.5219 | -42.061699 | 2024-10-03 01:01:23 | METOP-C | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14578e6f-a6c5-3a50-bc85-ef0e52985383 | -22.6742 | -46.791901 | 2024-10-03 01:01:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2899f07-a1b7-39b6-9a8a-ba5982ccb672 | -22.6548 | -46.797199 | 2024-10-03 01:01:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ccd54ae-4904-3b44-a971-a2b8a85cde1b | -22.656601 | -46.805199 | 2024-10-03 01:01:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4aa87694-b23f-3270-9ae2-fd977c43871f | -21.4793 | -42.136501 | 2024-10-03 01:01:24 | METOP-C | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6fed7f4b-1830-3bd9-841c-c2c41afe3c1e | -22.4424 | -46.862598 | 2024-10-03 01:01:28 | METOP-C | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c3c7f755-a699-3524-b690-a072556cde48 | -22.4443 | -46.870602 | 2024-10-03 01:01:28 | METOP-C | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 78029462-370f-3e95-ace8-5da014f78d0b | -22.4461 | -46.878601 | 2024-10-03 01:01:28 | METOP-C | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4e2f0c98-21ab-33b1-bfee-e612d81d4516 | -22.4326 | -46.8652 | 2024-10-03 01:01:28 | METOP-C | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1804f1f6-ad80-35db-92a2-8ce22be312d9 | -22.4345 | -46.873199 | 2024-10-03 01:01:28 | METOP-C | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea74a9a1-325b-3906-bc9c-6fa23d681e0c | -23.5488 | -53.317402 | 2024-10-03 01:01:32 | METOP-C | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2c151e1-bdd1-304e-931f-0b78e4a1a03a | -23.550699 | -53.327599 | 2024-10-03 01:01:32 | METOP-C | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae40dd93-312e-31d5-b13f-f87cf1e4f493 | -23.552601 | -53.337799 | 2024-10-03 01:01:32 | METOP-C | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 60eb8f5e-0adb-386b-8d60-8b89cc7468ec | -22.371799 | -47.903 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 325ec90a-6958-3ac1-bae1-47eb4e66d6ea | -22.373501 | -47.910599 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 29d515c9-5523-3d36-b71e-c2042a7bb338 | -22.3752 | -47.918098 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README23.md)
