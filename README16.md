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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 590ca0e1-09ef-37dd-831d-2c01593b4457 | -3.7961 | -45.4927 | 2024-10-10 00:35:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| a15fd00a-8d3b-3af7-a57c-be509081f4a5 | -3.8146 | -45.5143 | 2024-10-10 00:35:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 92136870-ee9b-3db0-9b04-6db4b6c2f250 | -3.8147 | -45.4918 | 2024-10-10 00:35:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 160.1 |
| c3d7acac-d5b8-3d90-8bc4-6793d6d2cf13 | -4.0814 | -51.0292 | 2024-10-10 00:35:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8365043c-3bc6-30ad-8823-11eea11e80bd | -4.0961 | -48.2739 | 2024-10-10 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| f314e1e5-6ab2-358e-a917-eb0ba40e38b5 | -4.0962 | -48.2523 | 2024-10-10 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 29b0ad62-4a5d-3125-aac3-7ff44f23cc33 | -4.0998 | -51.0285 | 2024-10-10 00:35:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 07bdfca6-b14b-31c8-8498-4b0364ef707f | -4.1146 | -48.2731 | 2024-10-10 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 229.0 |
| 149b7a57-6aae-342b-816f-7c6e7612943c | -4.1148 | -48.2515 | 2024-10-10 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 16f4ec36-6710-38a8-b4ae-63491342950f | -4.4776 | -46.5956 | 2024-10-10 00:35:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 448e943f-146c-36ff-bd91-dac02955e114 | -4.9513 | -42.9973 | 2024-10-10 00:35:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 422e3826-3e6a-367b-a2dd-58cba48a72f4 | -4.9515 | -42.9739 | 2024-10-10 00:35:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bee9bd1d-0b04-3d31-a288-f0c00785068c | -5.3946 | -45.9865 | 2024-10-10 00:35:37 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 24d1d5dd-fe4b-3988-8f5b-91be6f2615e1 | -5.4833 | -44.2822 | 2024-10-10 00:35:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 74fd4165-831d-3e24-846f-f1fa45db7f8b | -5.9034 | -45.4353 | 2024-10-10 00:35:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e2891802-1633-3e77-8f59-9d6c57530160 | -5.9036 | -45.4127 | 2024-10-10 00:35:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| d04c66a2-cd39-3c13-9b28-2e2a3a92f832 | -5.9223 | -45.4114 | 2024-10-10 00:35:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 50d65e32-9a83-3e0d-b5b2-8ddd3bd2f6c3 | -6.5218 | -60.0649 | 2024-10-10 00:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d1213a15-d150-34f0-ad75-321cae2c3734 | -6.5219 | -60.0457 | 2024-10-10 00:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 47c100e6-4cac-3680-9b03-9c11dbc2a665 | -6.5405 | -60.0067 | 2024-10-10 00:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 46316701-0493-3a06-b6c4-5c41bb9b7968 | -6.747 | -59.3259 | 2024-10-10 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b738179c-9da0-360d-9c50-80c46cf13cfe | -6.7654 | -59.3252 | 2024-10-10 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.3 |
| fcb216ad-0493-3271-aa7e-6ae4f8935585 | -6.7655 | -59.3059 | 2024-10-10 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c16943d6-b38e-3ab0-8227-8f90bfb9b422 | -6.7798 | -60.0552 | 2024-10-10 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 57052950-4d91-3a77-a812-d93af8965579 | -6.7799 | -60.036 | 2024-10-10 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0531ceeb-17e1-31f2-9a33-36456e99437b | -6.7839 | -59.3245 | 2024-10-10 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| cca3cd44-edf0-387a-9b9b-35618c8be5fd | -6.784 | -59.3052 | 2024-10-10 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 357003cf-7ad3-3de0-987a-21af444d868c | -7.0416 | -59.4296 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| aeb49d13-82fa-3d27-a7fd-518cf12f456f | -7.0417 | -59.4103 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 07eb29fd-be4c-36cb-af7d-9fe4e3747fbe | -7.0419 | -59.3717 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b0c1445f-8e55-308a-a195-96548f34fd97 | -7.06 | -59.4288 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 3929dd4e-65ee-395e-98de-4c01122628b9 | -7.0601 | -59.4095 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 517f29cb-b988-3c7a-9954-1037dadec401 | -7.0785 | -59.428 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| aba20c34-dcfa-37c8-9723-dbd506015d71 | -7.0786 | -59.4087 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0bafa3bf-73e4-3c42-ab1b-41a868bacad0 | -7.1346 | -59.3099 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 19734642-5217-39cc-9a70-9a4e057cf210 | -7.1347 | -59.2906 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| af8bd0ca-ff1d-3b17-962d-6ae0a73120de | -7.153 | -59.3092 | 2024-10-10 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 69f3fd59-03c7-3155-bc6f-93c879dab504 | -7.5934 | -46.7984 | 2024-10-10 00:35:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4da1601f-98e5-344c-8789-6d47ce2e28f9 | -8.2325 | -61.1823 | 2024-10-10 00:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 536bf807-6803-308e-81c4-79bff7213a42 | -8.6843 | -63.1009 | 2024-10-10 00:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8080a9d7-419f-384c-835e-b068946a57d7 | -8.6844 | -63.082 | 2024-10-10 00:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 15b9cb4f-fb67-3a40-9fea-f84ab0d37151 | -8.8422 | -61.4992 | 2024-10-10 00:35:57 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9b964cc9-01d3-3222-9509-728bbe45bed0 | -8.9898 | -61.6261 | 2024-10-10 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d2548304-413a-327f-9587-46760a1de16e | -8.9899 | -61.607 | 2024-10-10 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| f69baf37-df9a-32c9-9b52-5d684ba31a60 | -9.0084 | -61.6253 | 2024-10-10 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 16ba2338-88e2-3b5e-9f76-2b306d021b81 | -9.0085 | -61.6062 | 2024-10-10 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fd50753b-9c81-371e-b263-eaf68dc2af25 | -9.027 | -61.6244 | 2024-10-10 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 05dc0440-dd73-3535-929b-2bf1123c0fec | -9.0271 | -61.6053 | 2024-10-10 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| a52aa63b-04a4-3267-a5ab-b239cd6681f2 | -9.0656 | -61.3934 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3a20ebd3-26f4-334c-8d30-abc43652cea5 | -9.0841 | -61.4117 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 16dcb234-2d4f-3555-8915-bba0e8909813 | -9.0842 | -61.3925 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 0e0d7687-4e38-33d8-bbb6-c22155c6fc58 | -9.0857 | -61.1629 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 5cf252e3-bc64-3363-a387-d8c53dc76f23 | -9.0859 | -61.1437 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| dcd95b7a-b577-378f-ba24-c7f50a45a903 | -9.1035 | -61.2769 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fd395e16-9880-34d8-b799-b06bfd28287d | -9.122 | -61.2951 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| f08677f2-ebb1-343e-8c26-a55c7a430dae | -9.1221 | -61.276 | 2024-10-10 00:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 38de9bc4-4e51-3c60-b6f7-2a9c9f65034a | -9.3736 | -48.8025 | 2024-10-10 00:35:59 | GOES-16 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 647f8336-9049-3d18-9edb-35b64e6daad7 | -9.8737 | -60.3149 | 2024-10-10 00:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c1b79901-d997-32ae-a7d7-1a15e0c3abfd | -9.9105 | -58.1313 | 2024-10-10 00:36:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 933de6de-a1d1-3a55-8c9b-190da0daeb16 | -10.4287 | -60.9979 | 2024-10-10 00:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a8ff65e9-6f1d-33bd-b291-99b33a4ab3a5 | -10.5746 | -48.0178 | 2024-10-10 00:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| bc15b23f-7c31-38df-8438-7712ef268d78 | -11.0252 | -57.2436 | 2024-10-10 00:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 56612d7c-015b-3a9a-9d11-c20304d508b1 | -11.0254 | -57.2237 | 2024-10-10 00:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 297.8 |
| fa940b22-cc2b-35b5-953e-513dff9edd7d | -11.0256 | -57.2038 | 2024-10-10 00:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 330.2 |
| 6da83dcf-522d-3196-b940-b560415f6945 | -11.0443 | -57.2222 | 2024-10-10 00:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 01b1f648-2aae-3397-b770-64503d8e304e | -11.0445 | -57.2023 | 2024-10-10 00:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 191.9 |
| f35c10cd-bad2-3d27-852c-72fa4e5b658b | -11.277 | -60.4067 | 2024-10-10 00:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e192abeb-f24f-31fd-993f-3b34dd81ea41 | -12.2893 | -43.7258 | 2024-10-10 00:36:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| cc55ea8e-e901-317c-b7fc-50889237a383 | -12.1958 | -46.717 | 2024-10-10 00:36:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c1074f56-e7b7-325d-9e80-c7c429070876 | -12.663 | -54.7193 | 2024-10-10 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ade932a2-5d06-3b5a-afc4-dee27e1d5990 | -12.6821 | -54.7174 | 2024-10-10 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b41f3f23-e43b-3062-aa87-976f9f303878 | -13.1842 | -51.7217 | 2024-10-10 00:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| bf5cb779-0b8b-32a9-9303-9db2ed5cde2c | -13.1845 | -51.7004 | 2024-10-10 00:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bad397c7-551b-3f65-b2f7-5df1f64d8f3b | -13.8184 | -44.5254 | 2024-10-10 00:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 995b7e11-0dc0-3352-8580-dfb9203b1784 | -13.8374 | -44.5455 | 2024-10-10 00:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 7f1549c3-6588-3e31-8d07-dc7d90872d53 | -13.8379 | -44.522 | 2024-10-10 00:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 86326ea0-1118-3eec-89b1-32ab1d9a7c21 | -13.8569 | -44.5421 | 2024-10-10 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 6961f312-d41f-3a34-99e6-db12b9e9f81b | -13.8574 | -44.5185 | 2024-10-10 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 85cd1fda-c42f-320f-ac9f-f2a390533b43 | -13.8579 | -44.4949 | 2024-10-10 00:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 443ac0a6-fe3e-365c-b3ee-282eb9d84093 | -15.2859 | -45.1222 | 2024-10-10 00:36:31 | GOES-16 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ba930f2c-15f7-3ab1-9e62-28227a312a09 | -15.3056 | -45.1184 | 2024-10-10 00:36:32 | GOES-16 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 61be4883-edc8-361d-9b51-ded093a01624 | -19.5724 | -44.1594 | 2024-10-10 00:36:54 | GOES-16 | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 30e1b7a4-6c4d-300d-bc78-deaaf97f884f | -2.7776 | -49.2429 | 2024-10-10 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e92e7b7a-ce5f-30c4-98a0-109ad71f2446 | -3.3341 | -53.232 | 2024-10-10 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1382fb0b-ba75-3195-859b-8f11e5bc3fd0 | -3.3342 | -53.2117 | 2024-10-10 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9e3cc39d-7249-38e1-b9d2-4d333d49c9c6 | -3.706 | -44.9782 | 2024-10-10 00:45:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5843a53d-a5a8-3a30-93ac-ddc3c6583ba0 | -3.7061 | -44.9555 | 2024-10-10 00:45:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| cc3cfbb3-d732-3e50-915c-0e0b39a6a291 | -3.7246 | -44.9773 | 2024-10-10 00:45:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 89f94329-ebb9-335a-92b8-852a90db724a | -3.7247 | -44.9547 | 2024-10-10 00:45:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 194.6 |
| 596d8009-1f47-342c-812e-c30f3e6603ee | -3.796 | -45.5151 | 2024-10-10 00:45:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 819e6e2b-6f7a-32b0-815a-db8559e1a282 | -3.7961 | -45.4927 | 2024-10-10 00:45:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| af36dd8a-1db8-325c-b139-82e9c2273a5e | -3.8146 | -45.5143 | 2024-10-10 00:45:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| be92af63-d26b-3658-8905-edad39364244 | -3.8147 | -45.4918 | 2024-10-10 00:45:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 353efcb0-a7b2-3bbc-aa5a-6a2bb071ea8a | -4.0814 | -51.0292 | 2024-10-10 00:45:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c0f6f2dc-1f21-35ef-ab0c-e7a18971dd98 | -4.0961 | -48.2739 | 2024-10-10 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| bbc05789-23e8-341b-aeca-891b7bebbab9 | -4.0962 | -48.2523 | 2024-10-10 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| c259ece3-ffe8-35ff-a8cc-2d8e4de3ba06 | -4.0998 | -51.0285 | 2024-10-10 00:45:30 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c88cd9a2-f5b0-3eab-b9d0-68d3e7e355f8 | -4.1146 | -48.2731 | 2024-10-10 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| e60ff45c-c8dc-33cb-8168-149812d41517 | -4.1148 | -48.2515 | 2024-10-10 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 8c668595-9333-32fc-9a24-288510303523 | -4.4776 | -46.5956 | 2024-10-10 00:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 141.7 |


[Clique aqui para ver as próximas entradas](README17.md)
