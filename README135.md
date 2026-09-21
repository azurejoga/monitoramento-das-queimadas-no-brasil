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
| 8d40569d-59c4-3568-a611-db4a0b805565 | -8.7003 | -45.4567 | 2026-09-21 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| f8f4b0ce-e4a1-34b3-80fe-dbd6a14f8b6f | -10.7061 | -50.7915 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 286.4 |
| 0a06f5eb-6050-32be-a9f2-6e0f20a994f4 | -7.252 | -55.5794 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 53ef24be-9c35-3509-a02d-32a8385eb42b | -10.7073 | -50.7064 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 891a0468-7437-3560-9874-df223e612f44 | -8.7703 | -45.8793 | 2026-09-21 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 5cec3b20-358e-36c2-b6c1-821dc5c4971a | -3.4599 | -59.5209 | 2026-09-21 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b52d877d-4af6-3ea1-9338-d947b37b62ba | -12.3018 | -50.7203 | 2026-09-21 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b2b5af12-8481-375b-a25c-da3d88b8bb32 | -3.6631 | -58.8835 | 2026-09-21 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b32f1db0-23fc-3ef0-a429-21e8c39ff6c2 | -4.5774 | -42.9512 | 2026-09-21 15:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| f93065a8-b536-352e-b02f-a5dd068813d4 | -2.9157 | -57.7983 | 2026-09-21 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 8641379c-d967-3836-97c1-2b2f95186bf7 | -10.2635 | -49.984 | 2026-09-21 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7fa1b24a-1b24-3cf6-a682-bdef84c3a1fa | -11.7159 | -54.5858 | 2026-09-21 15:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| dc9c53aa-744f-3eca-b0e4-33762b7eb9cf | -10.7842 | -50.6133 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c278e317-342b-3391-9a5d-b74ab054edfa | -9.5595 | -66.0172 | 2026-09-21 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 952fb2b7-2e4c-3a0b-9e8d-2d72f8629b6c | -10.7067 | -50.749 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 726aabda-e08f-33a9-9f96-ce77b45cf4ed | -3.3823 | -50.4486 | 2026-09-21 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| fdc993d2-c564-3fb2-9bdf-c99f95fb482b | -10.9361 | -50.5759 | 2026-09-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 65017d6e-2cc7-3eec-9a47-e521c8eae501 | -1.4671 | -48.995 | 2026-09-21 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 59e58702-ae10-38ec-83f0-f14b1b4c3865 | -8.1872 | -54.7622 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 6d0fff61-1a43-3714-9dd5-706736705e58 | -8.7911 | -48.7502 | 2026-09-21 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 4c5bfc42-ea80-30da-8d48-496509eac752 | -13.5075 | -51.8728 | 2026-09-21 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 65cb6d41-6251-3f65-8d43-fa437d7f9181 | -11.8362 | -50.0244 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| d804a758-2bea-349a-a6dc-8cc96067efad | -9.0868 | -61.0095 | 2026-09-21 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a2e2b0e5-49f1-3d3c-b8ae-8ce6a4d413db | -11.0804 | -49.7456 | 2026-09-21 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 819f03aa-78f8-390f-911a-1257c3b09dc9 | -10.955 | -50.5738 | 2026-09-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 49dfa124-efb1-34c5-911c-6142f561158d | -10.4099 | -50.3324 | 2026-09-21 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 693adcef-110f-3757-b281-c72b765e6929 | -8.1686 | -54.7634 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 3b0ccfb1-1a85-3d11-942e-26b4751c5829 | -11.8359 | -50.046 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2a4f6696-ccc2-3341-98bf-bde7682cb952 | -10.7115 | -60.7312 | 2026-09-21 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 25136d59-2dac-3394-8567-53fb80287d38 | -5.9152 | -59.933 | 2026-09-21 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7eee527c-ccd1-350c-a461-d7a56f53a9b8 | -11.2783 | -43.388 | 2026-09-21 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| b424b124-80cd-3112-a779-d023743d5921 | -10.9547 | -50.5952 | 2026-09-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| cd5004fe-33eb-30c6-9373-8625630c8f8c | -10.7064 | -50.7703 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 290.9 |
| daeb934f-da5d-3476-a685-4a50ab51c4e1 | -10.9098 | -54.0866 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 809228e2-ff75-3e03-a190-e048dd03f689 | -9.257 | -46.1873 | 2026-09-21 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 67b15e68-f2b7-361c-8daf-e028e3b0fac2 | -10.7463 | -50.6172 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 681e668f-5610-3b40-ac87-588d5a0df0a7 | -13.2219 | -51.7595 | 2026-09-21 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| e340c336-fe6e-3787-8ea6-1047265d715a | -10.7655 | -50.5939 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2310acf1-3dc6-30b7-869d-a4256918137f | -4.4112 | -55.2466 | 2026-09-21 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 36866903-b584-3e74-8af7-6f923fe9f286 | -10.8924 | -53.9652 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1e8f6d9a-24dc-3b7a-8ee2-62b56cd5abcc | -10.7262 | -50.7044 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 4236b52b-6798-3e40-bab3-3668dfac4ec4 | -11.801 | -49.8345 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8eb576c1-7d4a-3918-a896-df8ce8a315a6 | -12.1662 | -50.8646 | 2026-09-21 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 719fa0df-b921-3a06-9b3a-9575b4521181 | -10.7466 | -50.5959 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 6ac9d519-db32-37c7-afb2-b05d3bbb93b9 | -10.9358 | -50.5972 | 2026-09-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 54bf23aa-0470-319f-b137-3c480e6f0d60 | -5.8274 | -47.7898 | 2026-09-21 15:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| df43796d-9478-3570-a57a-e1d4d9d61b27 | -10.7076 | -50.6851 | 2026-09-21 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 987ae98f-46b3-363b-897e-72b24e1ac983 | -7.4124 | -49.853 | 2026-09-21 15:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 02ab150b-1a20-385f-a06f-487905e2198c | -7.4286 | -44.7409 | 2026-09-21 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3bb114a3-33b9-3ece-86a2-55512f4ff848 | -14.1815 | -51.808 | 2026-09-21 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c2e6f35d-5a4a-30d3-8507-e7650f99f238 | -7.2519 | -55.5994 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c869cb61-f24a-39ed-af8c-e0e7c83ca548 | -11.3419 | -51.3606 | 2026-09-21 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 50e2b9d8-85fb-3dad-b0a0-2af86c137838 | -12.2723 | -50.1657 | 2026-09-21 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 2aa79b98-c5b9-3789-85e5-dafabee2da54 | -3.5356 | -58.6939 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 160b7e1a-3501-37ca-8d97-08ff3301e68b | -8.58 | -44.5552 | 2026-09-21 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 31d0b05c-72c8-3439-96a5-47c03f2c83d0 | -8.1684 | -54.7836 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2804eef0-159a-39e3-b164-e226c0e13499 | -3.5539 | -58.6935 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| e2826b47-3c30-3020-aad4-77fd58db5d56 | -5.7692 | -43.7077 | 2026-09-21 15:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| e8b37dbd-9950-3dd9-8f85-3d7a2405eae6 | -6.8263 | -55.5421 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 01e9b488-359f-3ef8-a232-f6feac5e38c5 | -8.3167 | -45.9934 | 2026-09-21 15:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9f4ac491-e51c-3df1-8ac0-459ccd52bd26 | -3.4454 | -58.2327 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7e3cc77b-9a58-3861-ae80-96117e0c8d41 | -12.5039 | -50.0075 | 2026-09-21 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b030d635-a93b-3a52-bdac-078efddcd52e | -10.4294 | -50.2877 | 2026-09-21 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2fa67b38-19ec-3b03-a766-faf81232044e | -9.807 | -46.0797 | 2026-09-21 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4dfb31c5-da51-32e0-a289-0bd353c6a0a1 | -3.3367 | -57.8673 | 2026-09-21 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| eef27adc-20dc-33e9-bc5d-aaea248fe8c5 | -12.1853 | -50.8623 | 2026-09-21 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 216.4 |
| f145b8c8-e1b3-3641-91f1-bbf3ab791630 | -9.831 | -48.4292 | 2026-09-21 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 15d81ddf-0339-329a-9a92-3412fb433f24 | -6.9225 | -42.9088 | 2026-09-21 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 03b17d37-b24e-32de-9d69-524d73aafb4a | -12.9091 | -50.9672 | 2026-09-21 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.2 |
| d060a8ce-a95b-3d98-b11f-3c3586467c7b | -10.8911 | -54.0677 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8a4a72ac-4d75-31c0-8688-be1677d55473 | -2.8608 | -57.7994 | 2026-09-21 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5e3cd268-deb4-3c72-9156-e275caf9b1d2 | -10.8921 | -53.9857 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2ac3a7f0-1c2e-36a7-aae7-81f3de6468cd | -12.339 | -50.78 | 2026-09-21 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d21dd23b-3c0e-3b83-a6ec-dc42834729cc | -11.3817 | -44.0319 | 2026-09-21 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 2740b72b-56ca-3ff7-b1a7-582da5bbc81b | -7.2333 | -55.6004 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c048c5f9-8edc-3cd0-a7ad-f89a80e93b0f | -9.977 | -50.248 | 2026-09-21 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 382a9b0f-3bcc-3079-bc95-b6e9670dbf28 | -10.3725 | -48.9153 | 2026-09-21 15:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ba3f7dd8-0998-3171-b7e5-ca32d9014179 | -3.4461 | -58.0199 | 2026-09-21 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b0ac5e67-aee0-347b-8ef6-2418cfdde302 | -10.7715 | -46.3001 | 2026-09-21 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a7d446d5-6bc7-3ecf-9c83-6e3f8969fd8d | -1.4487 | -48.9526 | 2026-09-21 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8bcc84ee-7745-355c-a56c-2c5bc82edb53 | -5.7506 | -43.6859 | 2026-09-21 15:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 768aa364-b68a-325d-8b3d-e607eea2fd8f | -13.2215 | -51.7808 | 2026-09-21 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 883ee395-fdec-3521-872b-ff3f9a18ccf5 | -6.9393 | -43.0953 | 2026-09-21 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| d7503d89-6974-3238-af11-450359f50a21 | -12.5419 | -50.0243 | 2026-09-21 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 89586e92-b164-372a-8839-34b191f79561 | -11.8555 | -47.615 | 2026-09-21 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d1f8b5d1-765e-352e-91ca-3026b0dced3f | -12.2044 | -50.8601 | 2026-09-21 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8480162f-5c17-3a00-980c-107564c5ac44 | -7.3259 | -55.6153 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 09007b68-673f-3d79-8a92-36f60f11c9a0 | -7.3289 | -55.2155 | 2026-09-21 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2dfdb938-1217-3687-8188-244b97e6cc9a | -10.8735 | -53.9668 | 2026-09-21 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| c7f114f5-2c9d-32d9-9d4e-41732d3a53d0 | -3.0788 | -58.3948 | 2026-09-21 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f0cc2068-017b-3fcf-a62c-fec56fe1304e | -8.7729 | -44.2568 | 2026-09-21 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 62190c58-8813-36d6-8a08-f3b598955972 | -6.392 | -45.1948 | 2026-09-21 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8916791e-3e58-3b5e-888b-538a8066ec2a | -6.5634 | -44.9084 | 2026-09-21 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 1c9a9804-bcbd-3088-a0de-dc74cdc650ce | -12.5231 | -50.0051 | 2026-09-21 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 959dcf87-6b10-35b6-882d-0b4ab6ef3d04 | -9.5594 | -66.0359 | 2026-09-21 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 111.9 |
| e7b20f83-ccce-3774-bc83-6994f5105541 | -8.7914 | -48.7285 | 2026-09-21 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 9fdffd49-886f-3e92-8006-39f8c64c4c63 | -6.5451 | -44.8643 | 2026-09-21 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5a90c3d3-62a2-3676-92b4-f1ebf9b34b06 | -4.2239 | -48.6127 | 2026-09-21 15:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 536da97f-30f8-3355-a4bb-df574ba00897 | -2.2619 | -48.7445 | 2026-09-21 15:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 23b580d7-46bb-37d1-8861-d9fb2c6961dc | -5.7305 | -53.4446 | 2026-09-21 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |


[Clique aqui para ver as próximas entradas](README136.md)
