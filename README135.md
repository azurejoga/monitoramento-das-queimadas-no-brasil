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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cab1ba52-a524-3b1c-870c-da1c91a00c18 | -9.997 | -47.3551 | 2024-10-14 14:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 83aaf85f-0c9f-3b92-a5b4-d391439295d0 | -9.9793 | -47.2684 | 2024-10-14 14:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0a3dd65a-28d5-3909-849f-10736191d8b9 | -9.9395 | -47.4059 | 2024-10-14 14:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| bbc98886-466d-3787-98e4-69911e0801a4 | -10.0439 | -44.195 | 2024-10-14 14:06:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 08cf6e65-724c-3c0a-b80a-9e167d2c3841 | -10.183 | -46.283 | 2024-10-14 14:06:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| be636995-a1fd-3c6a-a04b-dda7bb4807ef | -10.1637 | -46.3079 | 2024-10-14 14:06:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e1604766-e4fc-33fb-bcae-6d87c167f225 | -10.0735 | -47.3021 | 2024-10-14 14:06:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 68ce9979-1719-3872-a17c-f24fd376e65f | -10.0738 | -47.2798 | 2024-10-14 14:06:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| df87b3e1-e542-3699-8641-698ffb6f56d1 | -10.3303 | -46.58 | 2024-10-14 14:06:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7cd6777f-0956-394e-880d-4264eed7395d | -10.3493 | -46.5777 | 2024-10-14 14:06:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 49ba919f-d4c9-38f2-9424-d1985bfec2d7 | -10.2664 | -47.0573 | 2024-10-14 14:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2a677221-b23a-30cf-a98b-fc425e4af32a | -10.2854 | -47.0551 | 2024-10-14 14:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| da55a1a7-0b38-3369-b0fa-37adbe20e4f8 | -10.9307 | -44.7021 | 2024-10-14 14:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 568c9fea-2d50-38e0-a388-c50dfaa9d304 | -10.8925 | -44.7074 | 2024-10-14 14:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3c35ff42-d4e9-3b70-bb0f-3fa9b4bd7d0e | -10.912 | -44.6816 | 2024-10-14 14:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e7ab6913-58ef-3502-b433-da581e2f5f60 | -10.9311 | -44.6789 | 2024-10-14 14:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a6880ae0-b993-3b69-9a68-aaf1c8c2f673 | -10.9116 | -44.7048 | 2024-10-14 14:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| ed1f228c-78dd-34fc-89f7-5d5ea5e25403 | -11.4794 | -43.9234 | 2024-10-14 14:06:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 2d4f6523-6596-335a-87c1-1ccddcc3fd45 | -11.4602 | -43.9263 | 2024-10-14 14:06:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| f7326c5f-e3c1-3a14-84a3-ca5c3c530cbf | -12.1073 | -43.1861 | 2024-10-14 14:06:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 63a70f13-482d-3efc-b3d9-5bb1183f78e6 | -12.3992 | -53.1564 | 2024-10-14 14:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 2e715943-9109-307e-85f3-e85533a2280d | -12.3997 | -53.1147 | 2024-10-14 14:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 34b32ec9-8bed-3b50-a23b-ca88823e8e62 | -12.5962 | -44.7783 | 2024-10-14 14:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 7c3c4b4f-841d-31e8-9c65-97b672f12a6a | -13.3889 | -44.694 | 2024-10-14 14:06:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cbd83d50-fccf-3ac9-84d4-2bdd503fc501 | -13.8734 | -44.6799 | 2024-10-14 14:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 88424705-cb12-3da2-9ee2-9f0c208407f3 | -13.8739 | -44.6564 | 2024-10-14 14:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8c979ca1-1a13-3ce3-a9db-0ab5774ffa2c | -15.3237 | -48.7671 | 2024-10-14 14:06:32 | GOES-16 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 6c3849e8-c8db-3b8d-a96a-5888e1be4ad5 | -21.5621 | -48.0058 | 2024-10-14 14:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 6d672e81-acaa-3c7e-b9e3-f678707dad48 | -2.4344 | -46.9195 | 2024-10-14 14:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 326240b1-d866-3993-a5de-6e902e18bc1b | -2.6118 | -49.0985 | 2024-10-14 14:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| fc9124e0-b55f-3747-97c5-5bc5ae2915fc | -2.6119 | -49.0772 | 2024-10-14 14:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 2a8e5988-9dbe-31c1-a30a-880e98420a85 | -2.6303 | -49.0767 | 2024-10-14 14:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| bbc9b422-db18-35b3-ba17-48b8e9cca42c | -3.3815 | -42.9923 | 2024-10-14 14:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 0f5718bf-d2ec-3a99-8c74-b0fb55eba28c | -3.3816 | -42.9689 | 2024-10-14 14:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 866dd3d2-0392-3e5a-bbe0-5007c05892ba | -3.4169 | -43.3403 | 2024-10-14 14:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| a16efe86-91a4-3bb6-a72a-048cb0699e3d | -3.9065 | -45.7118 | 2024-10-14 14:15:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 269f6c66-c394-303a-b967-21acc5a1c3e5 | -3.8386 | -44.5858 | 2024-10-14 14:15:28 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 71e2e869-4659-34d8-bf31-9aaeba1ae6b9 | -3.9219 | -43.1525 | 2024-10-14 14:15:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 8e86efb9-c397-3eb3-a896-8324ab6f4644 | -4.0957 | -42.2969 | 2024-10-14 14:15:29 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 135.3 |
| f1e916b7-25ac-3e8b-96ac-baa819920273 | -5.3226 | -43.3687 | 2024-10-14 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 56038616-e138-35aa-b142-262b53a5ec7a | -8.7735 | -45.6303 | 2024-10-14 14:15:55 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7cae9d13-e0c6-3690-a523-40350f2d76aa | -8.7814 | -46.4847 | 2024-10-14 14:15:56 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 03fa7230-3f06-3ddb-a351-e59613ee6f94 | -9.1216 | -46.4265 | 2024-10-14 14:15:57 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| e5046680-9c60-3683-af7a-178ac66ab98a | -9.4702 | -45.8023 | 2024-10-14 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| adb446c1-d66e-335a-a17b-38188b372f9e | -9.4365 | -45.5112 | 2024-10-14 14:15:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| e6d0da92-7926-378f-9897-d45b16b2b7dc | -9.4888 | -45.8228 | 2024-10-14 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e2cb9c18-511e-3c0c-8b24-4a7e81ce350e | -9.418 | -44.1577 | 2024-10-14 14:15:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 1d7225f5-e131-31e7-ac91-5be5025e4a97 | -9.4175 | -45.5134 | 2024-10-14 14:15:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| e3307012-f47c-341d-a0b0-82e5f5767644 | -9.4368 | -45.4884 | 2024-10-14 14:15:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b654b166-f966-3461-92a6-f6c21a044e83 | -9.4885 | -45.8454 | 2024-10-14 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7cacc9fe-8857-3015-b6db-7e50f56a8ba8 | -9.4699 | -45.8249 | 2024-10-14 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e91e1b1f-0d4d-34ae-90bd-e6868fd1a467 | -9.437 | -44.1554 | 2024-10-14 14:15:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f33435a5-5a84-306a-921f-e9a84cc37b56 | -9.4696 | -45.8476 | 2024-10-14 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0c7cc7d3-2bf3-3ffb-8025-8befcc58bad6 | -9.3149 | -46.0908 | 2024-10-14 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 77941379-fc8a-3fdc-adeb-88ee55185878 | -9.8315 | -47.0183 | 2024-10-14 14:16:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| aeb24215-4930-38a0-abdc-7c61f8a8e2f7 | -9.9392 | -47.4281 | 2024-10-14 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 5a971974-7453-3d0c-9927-f26be8466957 | -9.9395 | -47.4059 | 2024-10-14 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| baa98685-565a-3e8e-bf95-e90f7e4e9e24 | -10.0439 | -44.195 | 2024-10-14 14:16:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 75a9a648-5f8e-3159-ae47-3ad3a1678a31 | -9.8685 | -45.7556 | 2024-10-14 14:16:02 | GOES-16 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3a69ba63-08cc-3b76-8691-c1133daf838f | -10.164 | -46.2853 | 2024-10-14 14:16:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 1939cf10-f719-33d5-ac12-e87116a71d28 | -10.0735 | -47.3021 | 2024-10-14 14:16:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2983f6ab-aec4-3b4a-9375-3bfca7ef693b | -10.2854 | -47.0551 | 2024-10-14 14:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 016f092e-35b4-3672-8d53-9f0a547fc81a | -10.2641 | -47.2134 | 2024-10-14 14:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 1b19fd3e-0716-3e22-98d8-a47ba5eec92d | -10.912 | -44.6816 | 2024-10-14 14:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 021886e3-daae-3495-8f4d-143113945209 | -10.9311 | -44.6789 | 2024-10-14 14:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4beec3cc-d7c7-3d66-8a46-2f9bd388a90f | -11.245 | -44.1924 | 2024-10-14 14:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 5a9a62be-1092-3bfa-b360-0fdc7ffb0508 | -11.2254 | -44.2186 | 2024-10-14 14:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 46e5b7f6-f885-364c-bda0-03be4fdabf25 | -11.2637 | -44.213 | 2024-10-14 14:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 5078375d-f29a-3b8a-9967-cefee71aa4c6 | -11.2454 | -44.169 | 2024-10-14 14:16:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| e751365b-e1e7-3e34-b747-afad9624d5cf | -12.1073 | -43.1861 | 2024-10-14 14:16:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 0a2d3c48-eecf-3f61-9970-4b847e5eba95 | -12.2727 | -44.5967 | 2024-10-14 14:16:15 | GOES-16 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a151e31c-e6d2-3960-9198-65736fde9ecb | -12.4182 | -53.1544 | 2024-10-14 14:16:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9c1d5996-25c4-3ee5-b20a-a8b71aa856dd | -12.4376 | -53.1315 | 2024-10-14 14:16:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0852d819-8224-37f5-9c96-7f2115afeb1b | -12.3997 | -53.1147 | 2024-10-14 14:16:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a1d6b8af-847b-3af6-8000-7aebbac5f4ca | -12.5962 | -44.7783 | 2024-10-14 14:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| bfe2d897-5436-3e0c-9670-8700347c7ef1 | -13.8734 | -44.6799 | 2024-10-14 14:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1dee37ea-28e6-37d1-b72e-1fe4e9eda3ec | -13.8739 | -44.6564 | 2024-10-14 14:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| dd07c9e5-411f-394d-8e68-6c2f5ca16317 | -21.5621 | -48.0058 | 2024-10-14 14:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6a96cc80-c27b-30a3-aac9-007b4f2175a9 | -1.3927 | -49.2939 | 2024-10-14 14:25:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| bbcfe238-7243-3dd5-b52d-9a9f5fb9da03 | -2.6303 | -49.0767 | 2024-10-14 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 8339d912-9df5-38ad-867e-bdc68dab182c | -2.6303 | -49.098 | 2024-10-14 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3b20ec0c-dc42-3802-9e0c-c11e22ee80cc | -2.6119 | -49.0772 | 2024-10-14 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 7c0aa901-c21d-3a2e-a850-69280722b1a5 | -2.6118 | -49.0985 | 2024-10-14 14:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| a3af1bca-6216-3f67-ba1b-b599712e7817 | -3.3815 | -42.9923 | 2024-10-14 14:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 33893ea7-67cb-3de2-b985-7921663844c6 | -3.3981 | -43.3644 | 2024-10-14 14:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ba38fc2f-9b07-3928-b621-0ce1d312a155 | -3.4169 | -43.3403 | 2024-10-14 14:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 7de7a79d-7039-3ff5-8b58-8ca7cd28a052 | -3.4168 | -43.3635 | 2024-10-14 14:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| e4b03ce3-99ff-3542-b19f-955787bb7914 | -3.9219 | -43.1525 | 2024-10-14 14:25:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 36f06923-dec5-35fa-b2d2-93e23f075c1f | -3.9416 | -49.4365 | 2024-10-14 14:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f67d456f-e8ba-33b5-8f7b-00978f7b7534 | -3.9844 | -42.161 | 2024-10-14 14:25:28 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 57154cf1-73ed-3441-a279-478031d68982 | -3.8386 | -44.5858 | 2024-10-14 14:25:28 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 253cacc5-4efe-3c6f-b4ef-2f1ffdb937f6 | -4.1149 | -48.2299 | 2024-10-14 14:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3d93970a-611a-3b4d-9882-de0a1e2994bf | -4.0348 | -43.0296 | 2024-10-14 14:25:29 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1b61a38b-06af-3b0b-85f7-20754be13600 | -4.0957 | -42.2969 | 2024-10-14 14:25:29 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 523582b9-8c48-30a6-bd67-1e9f381a0a38 | -4.6436 | -46.8077 | 2024-10-14 14:25:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bff9072f-c5ae-39d3-b96d-3af2c9e671d5 | -5.1306 | -41.7056 | 2024-10-14 14:25:35 | GOES-16 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| c6d518a0-191f-3228-8758-9b9e9e9ddf35 | -5.3226 | -43.3687 | 2024-10-14 14:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 00d851cf-eb9e-357e-8847-22c47f26d264 | -5.675 | -43.7611 | 2024-10-14 14:25:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e034720d-443c-3ec9-8619-15ac523eb045 | -5.6938 | -43.7597 | 2024-10-14 14:25:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 54e604a5-2f25-3148-871e-3ce2cf21cda9 | -6.3909 | -41.6016 | 2024-10-14 14:25:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |


[Clique aqui para ver as próximas entradas](README136.md)
