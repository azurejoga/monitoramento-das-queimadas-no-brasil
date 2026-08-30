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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 307ce0e8-bcb0-3eae-8e14-2d518634d489 | -15.3849 | -52.6677 | 2026-08-30 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a6b2386d-2711-31ce-8846-5c01d3a37a0e | -9.0615 | -65.4169 | 2026-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b81d2870-0e4c-3284-b29e-0f6ba54af4ca | -11.2314 | -54.0164 | 2026-08-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| f764b612-0070-3c2e-bc39-938cb0857db2 | -9.1718 | -59.5211 | 2026-08-30 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 223a7ee9-beb6-3024-9c3c-b69f033eb94a | -7.2932 | -60.6096 | 2026-08-30 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 07f4af9d-7345-3a46-8bf3-c4bd6758ba7f | -7.1315 | -42.7472 | 2026-08-30 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| cecad91d-2da6-35a0-8cae-a591d52befab | -11.0627 | -47.1385 | 2026-08-30 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| c2400667-81f2-34c3-a80c-a1ba0a3f01d4 | -14.4387 | -52.56 | 2026-08-30 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 27d5b056-7e5c-3a38-aa81-01bd055a2cdf | -3.4943 | -54.6567 | 2026-08-30 14:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d820c579-96da-3fd2-ab66-cbbeb5c8ed1d | -7.95 | -44.31 | 2026-08-30 14:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27ce94c5-5edf-373f-8e4f-ef34c70d8b34 | -10.78 | -50.69 | 2026-08-30 14:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| adebd968-a965-3aa8-9d10-566058440fc0 | -10.74 | -47.21 | 2026-08-30 14:15:00 | MSG-03 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6366d234-cca6-35e7-b99b-00914e777422 | -4.96 | -55.84 | 2026-08-30 14:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 015ee660-c017-387f-b2dd-5ab6985c5cf8 | -7.1312 | -42.7708 | 2026-08-30 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 193.8 |
| 3dce18ab-3f12-31ad-92c4-34cc3f01fe99 | -10.7618 | -50.8707 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| aff00d90-7554-3ee7-bfbf-31b64eed48c4 | -12.0921 | -47.1812 | 2026-08-30 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 839911ac-b53c-3c1d-916e-1d2ab9783e31 | -10.3337 | -50.3829 | 2026-08-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 72553cb0-1a8f-33f3-9a92-e020fddf516f | -11.2294 | -45.099 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 6fe2caeb-89e9-3240-b40f-69dbbbe8eaec | -6.8613 | -41.6532 | 2026-08-30 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 88f1b305-e293-378a-bb54-541c22a12f12 | -6.0 | -45.0889 | 2026-08-30 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e955ddd5-10ac-3533-b135-03c007a23b68 | -8.1348 | -45.4696 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a19e494b-9ecc-3c80-9753-ab7ee8cd3977 | -10.9935 | -50.5271 | 2026-08-30 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ebfb24a7-59bb-32dd-b123-f63f9b1916f5 | -8.1345 | -45.4923 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ebbd4393-e10b-3181-ac8b-3c2dd9382735 | -11.2506 | -53.9941 | 2026-08-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 3ce564d4-71a1-33d8-93ea-f6dcb47d8ff0 | -7.2932 | -60.6096 | 2026-08-30 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| d70bd5bb-2e2f-3624-bf99-baed151b6dab | -4.9605 | -55.8226 | 2026-08-30 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5ffabbc8-ab0e-3988-b774-85545c0f2c49 | -11.1534 | -51.296 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5f28085b-0d99-37bd-8ff5-d172a0fa3340 | -11.2485 | -45.0963 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 4bec5394-8fc8-33fd-838b-7072fb95a703 | -7.6963 | -61.1664 | 2026-08-30 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f9007bca-1a1a-3ef1-94d5-9771a3d4e314 | -7.991 | -46.4954 | 2026-08-30 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 52248fa0-e8b6-3ea0-b64a-627134ec2f3b | -14.1459 | -52.7871 | 2026-08-30 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4ee6d1a7-4eb5-3e3c-ae0a-32f0d627e292 | -11.2446 | -45.3267 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a923d4a4-b4eb-36bf-b0e7-57207b1237b7 | -10.8235 | -50.5026 | 2026-08-30 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 5c016021-6913-358e-98bc-30c7fbac7258 | -8.1534 | -45.4904 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a0e7b373-a042-3bcf-afb3-3dedf7c3b451 | -7.2933 | -60.5905 | 2026-08-30 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| f205e1c1-62a3-3c48-b1f9-c6d4c9d93ffc | -9.0615 | -65.4169 | 2026-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f909ef71-8c1c-3832-966e-d69e1feb5b0d | -9.5103 | -45.6389 | 2026-08-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a8f2335e-31eb-30e5-ac77-1c8c8ecce420 | -8.5971 | -54.7553 | 2026-08-30 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 429854ae-3f79-38ef-aa23-99defcc4466a | -9.1533 | -59.5027 | 2026-08-30 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ed70a635-e2d1-3ca4-ae2f-cfeb3fa8e891 | -9.7832 | -46.4202 | 2026-08-30 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 297.3 |
| 38449642-eb2b-33f1-8de6-fcea57413483 | -12.9027 | -45.8612 | 2026-08-30 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 964cdbe7-93d6-3875-af14-3a71d4af344a | -8.5968 | -54.7957 | 2026-08-30 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 08e8295a-98c1-3826-96d5-23a2df7c3da4 | -11.0054 | -49.6893 | 2026-08-30 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bfd48a5a-3dc0-31a0-80a6-d120b0680b74 | -9.1662 | -60.2752 | 2026-08-30 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 199787cb-113f-3fee-8bd7-42da45c10d8c | -7.3118 | -60.5897 | 2026-08-30 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 4a383cab-a013-35a7-9c9a-a801fb5373e9 | -13.856 | -54.1175 | 2026-08-30 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 1cad6fed-a4d1-3eff-91e8-488716c43216 | -10.918 | -50.5138 | 2026-08-30 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ca78941e-a6f9-3fe9-9983-8baed44a3429 | -11.7973 | -47.6672 | 2026-08-30 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0794af1a-6432-387e-a887-cff2821e697c | -9.1532 | -59.5221 | 2026-08-30 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8397829b-815f-3dc2-bb85-37a866715695 | -10.7434 | -50.8302 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| fb32588d-bda5-3393-b0ba-011c0b5253c1 | -13.3799 | -51.4634 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| f7ccd948-580b-3026-93c5-9379bf6950e3 | -8.574 | -66.9569 | 2026-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ac57bb11-79b5-312c-a00f-5426c8398fbc | -11.1723 | -51.294 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 8ebf8e41-71e8-33d5-9910-709924849c5b | -8.6158 | -54.7541 | 2026-08-30 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 845ae6a0-b0c1-3005-9ddc-1c88da244afe | -9.1718 | -59.5211 | 2026-08-30 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 005e855a-a20d-3ad9-8921-3bcb97cfeb51 | -15.3849 | -52.6677 | 2026-08-30 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| dbf5f284-a945-3683-89e1-c0992fc683bb | -9.043 | -65.4175 | 2026-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9d38f2a0-85f8-338c-ace6-7ab5c77b6d86 | -15.228 | -57.6719 | 2026-08-30 14:20:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f06aedef-d5aa-32a1-a05a-fcf9ed33912c | -14.1456 | -52.8082 | 2026-08-30 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b933509b-f9fa-3758-828c-a169f50c860a | -7.3117 | -60.6089 | 2026-08-30 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 208.4 |
| e67d8f6a-b3af-35fb-9cca-1f514d552741 | -13.4191 | -51.4159 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5428fe0c-4286-300c-bf3e-d74f49066ac9 | -10.7596 | -54.0384 | 2026-08-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cad6cafd-3cbc-3623-8c91-6b6e9afa01fb | -3.2361 | -61.2548 | 2026-08-30 14:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0eaf1322-30d5-30d0-92f3-d95dabe07060 | -7.546 | -44.3395 | 2026-08-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| da4089b9-2758-3107-b985-5b1db628067f | -9.1719 | -59.5017 | 2026-08-30 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 0bf970a6-f8cf-326c-b9d0-9d7db4f54892 | -8.5969 | -54.7755 | 2026-08-30 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 51bb5ab6-c463-319f-8b0b-234ac24a4992 | -10.8539 | -54.0301 | 2026-08-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f21757ed-b806-3079-8f52-6af2562c5ac4 | -14.7601 | -48.7467 | 2026-08-30 14:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 86dc9060-e6f2-3d89-83cd-4b1ef0b03aa3 | -15.4048 | -52.6437 | 2026-08-30 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 402.4 |
| 618ff0bc-d68d-3c53-bf9c-d1fe5d8d2322 | -10.8249 | -45.3382 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 63d4b5c2-61a4-3cc1-a2b0-b33cecbdb1ab | -3.6399 | -60.5466 | 2026-08-30 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 61ef8bbe-9a14-399e-9850-825c540f58bf | -11.1726 | -51.2728 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| cb96a36a-9016-3d7d-83dc-6e54cc4d4b1d | -11.2314 | -54.0164 | 2026-08-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 194.9 |
| 99461e24-c773-3488-b374-faee291714db | -6.861 | -41.6772 | 2026-08-30 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 348.5 |
| 2cd24e1f-39d6-32b1-bbc0-1b018ce62fb2 | -14.4846 | -52.1299 | 2026-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5f857688-ff95-3659-9e2a-eb34ad22341d | -15.6336 | -56.3876 | 2026-08-30 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 9ca82075-8a1b-33fd-9fc0-8528a197a723 | -13.8381 | -54.0365 | 2026-08-30 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 89043004-cb40-3dba-8176-bd49e895a67a | -7.9838 | -45.5072 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 39843f2b-7986-318f-a4cf-6e15bc495aeb | -10.9859 | -51.0807 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| a1ab4476-6f42-3b02-9d62-c8f462a18701 | -14.2989 | -51.7072 | 2026-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c2e6ade6-c8d7-3fbd-8981-c4f39eb4ec31 | -5.4876 | -57.1416 | 2026-08-30 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 8b00176e-ff15-3b56-a156-592ae7415037 | -9.8927 | -60.2752 | 2026-08-30 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 640ba366-6ea8-3f32-82d8-2bc99dad536e | -7.9907 | -46.5177 | 2026-08-30 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 3c57f0d1-e8e1-3c80-a701-23014374350b | -11.2443 | -45.3497 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 233.9 |
| 02b7440b-4fa1-3213-8689-debc99aefba0 | -13.8752 | -54.1153 | 2026-08-30 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| dea405a2-582d-3f43-b800-e2ffc3bdd295 | -13.3998 | -51.4183 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 495845a6-5b11-3ad3-8304-79707eb244ab | -11.2634 | -45.3471 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| da1ebae3-a456-30d2-b59f-baeb89617b3f | -16.2735 | -42.5653 | 2026-08-30 14:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 633187e1-2fdd-3c80-a78a-da027d19f7e9 | -7.495 | -55.3262 | 2026-08-30 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| dd7efc0e-2e3e-33b2-aeca-9d06529f1492 | -7.5644 | -49.5857 | 2026-08-30 14:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| e983111f-d1be-32d8-b73b-35f46fb672aa | -11.0057 | -49.6677 | 2026-08-30 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f9fcd94e-cb05-3179-b078-c87d766b87f6 | -11.0627 | -47.1385 | 2026-08-30 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 38bc80f2-1be0-35c3-855b-09bbc54dad75 | -15.0858 | -48.0241 | 2026-08-30 14:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 786d72ff-fe9c-3882-853b-c0ef8a56001f | -6.7699 | -55.6644 | 2026-08-30 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 04bf6b39-c48f-303d-a66d-982a2bb4af04 | -7.6964 | -61.1473 | 2026-08-30 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 88deee02-a80c-3f93-921c-7105062ac586 | -10.7431 | -50.8514 | 2026-08-30 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1da2aa78-b283-3961-b76b-3e85ca63937c | -14.1649 | -52.8058 | 2026-08-30 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 272de548-1495-3f62-b1af-c6c500132084 | -7.5137 | -55.3051 | 2026-08-30 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ffd5a949-b6ef-32de-a884-1e02420638ae | -13.3943 | -51.7595 | 2026-08-30 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5421b242-a6de-3f28-a83c-12428c139511 | -15.4044 | -52.665 | 2026-08-30 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 143.0 |


[Clique aqui para ver as próximas entradas](README85.md)
