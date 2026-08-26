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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82c0aeb2-d2bb-3332-8342-75a265107f50 | -4.8004 | -43.1476 | 2026-08-26 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d868d66b-b1a9-3a49-a8a2-fe01da3aaa4b | -8.1482 | -47.5218 | 2026-08-26 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| e572eb41-fcbd-3d51-8755-545829e3c061 | -7.6649 | -47.1242 | 2026-08-26 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 30d61b89-56fb-34df-8977-9b34b03dafd6 | -10.7787 | -54.0163 | 2026-08-26 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d4b21d6f-5b97-33ee-88ce-497a4f461a1a | -8.5363 | -55.3027 | 2026-08-26 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e0d4558c-94cb-369a-8c8d-2fb7bb68e97d | -4.8002 | -43.1709 | 2026-08-26 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 58c682bb-7ee6-3771-aa88-17b49905f241 | -9.7249 | -49.3296 | 2026-08-26 14:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 0c00e75d-f722-3032-b61e-29b9faba6287 | -9.6022 | -55.128 | 2026-08-26 14:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b85ed815-1193-3c98-9341-99253a87f77e | -7.1309 | -42.7945 | 2026-08-26 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 176.2 |
| 41a2a21e-610b-3c50-b6b8-c05599446bea | -8.1484 | -47.4998 | 2026-08-26 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c54e4943-fc90-31a8-8de6-6898ac5f9797 | -11.1165 | -49.8707 | 2026-08-26 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 98a23bcb-2b35-3411-9a81-413faa918892 | -6.2676 | -53.3768 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 6592ca67-665b-3001-8bbf-af75f553255a | -3.2178 | -61.2362 | 2026-08-26 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 0cb0722b-fde3-3fe7-a567-2492dd10b2b9 | -9.6588 | -55.0834 | 2026-08-26 14:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 3cfea0da-7388-3824-a9f8-79c300d49274 | -6.6409 | -58.5181 | 2026-08-26 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5f282555-9154-32c0-ad45-61e2752a0ff4 | -6.6226 | -58.4995 | 2026-08-26 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3d944f1a-f3de-3313-a4ae-e4a7ef8a1e55 | -8.5962 | -54.8563 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 8a8dee97-f5fd-38e6-a829-d09ab7b3e24e | -13.264 | -51.5205 | 2026-08-26 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| f862fa84-b5e3-3f69-8f9c-e509e0a05984 | -10.5596 | -50.4449 | 2026-08-26 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4e35c861-c7c6-3d97-8bc3-5a6715aef8e7 | -10.7598 | -54.0179 | 2026-08-26 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 29508382-3fab-3701-8e83-908ba481cb8d | -8.1671 | -54.9447 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0d5a2a64-ceda-393b-b4e2-6ba780fb119a | -8.1855 | -54.9637 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ea77b664-25a3-3c0d-a4ce-0ad5e0f7dfc2 | -7.6461 | -47.1258 | 2026-08-26 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 62e15876-09ac-3215-b416-3d02986a2091 | -7.385 | -55.1523 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 749bb192-1bf8-316d-a612-0fce6d6c0a08 | -8.5361 | -55.3228 | 2026-08-26 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5d7940d6-05be-3056-8f0c-2e75a6285746 | -8.167 | -47.5201 | 2026-08-26 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 67f399bb-ed09-3925-b327-c934b72a2722 | -6.0353 | -58.0376 | 2026-08-26 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 13ceaee3-7f83-3914-baee-f9ed0136bf43 | -10.7787 | -54.0163 | 2026-08-26 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 465277bc-b44a-3093-a4da-14bb32f07da6 | -9.1896 | -50.0032 | 2026-08-26 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 0190a153-738c-38c6-92bc-3e57b0e0cc8c | -7.1312 | -42.7708 | 2026-08-26 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 9445a332-3dd9-352b-898e-39410bf3604b | -3.79 | -59.284 | 2026-08-26 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4f957df5-864d-365d-b75e-8c8f3d099b13 | -9.6024 | -55.1078 | 2026-08-26 14:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 204.6 |
| dd10f84f-0d76-3ae1-b0d6-4f154dbbca22 | -8.1482 | -47.5218 | 2026-08-26 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 655b9d51-8371-3345-b7db-5b64c1bbca5b | -7.1266 | -43.1714 | 2026-08-26 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| b9bf2e38-0d53-3bae-90d8-655801176c24 | -10.7596 | -54.0384 | 2026-08-26 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 196.1 |
| b96dc597-1fec-3fda-89de-93fbdbfdea9e | -13.6817 | -51.7872 | 2026-08-26 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b14d69b1-fa55-371d-ac31-9d652b2891b3 | -12.6836 | -48.4116 | 2026-08-26 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f1b573f2-9d8c-391d-a39f-fe16691572f3 | -7.6649 | -47.1242 | 2026-08-26 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 1d01520e-bd45-37c7-9e42-0ef76dbe9f09 | -8.6344 | -54.7528 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ba4711f7-7dc3-3d1d-929f-f0b4ec7a6476 | -11.7973 | -47.6672 | 2026-08-26 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 30597b13-6e81-325b-a664-a122d17d8af5 | -13.3226 | -51.4493 | 2026-08-26 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 00d8811c-f08a-3670-94f0-46080029e14b | -6.3322 | -54.7473 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6d464648-37c3-3f5f-b517-a163e906232d | -10.7784 | -54.0368 | 2026-08-26 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a1ceddbc-42bd-32c2-974b-1f7c2f8c1a87 | -8.9418 | -45.748 | 2026-08-26 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| d4a62047-fda5-326f-b6a5-4b2c62339069 | -7.1452 | -43.193 | 2026-08-26 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 468e4c9e-fb43-3e48-beb2-19b9452580d1 | -8.8189 | -49.5879 | 2026-08-26 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7ed9ab8d-ebb1-313b-b1d5-91f339054dda | -7.5015 | -44.9397 | 2026-08-26 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8c32d7d2-ed3a-3467-b16a-f7dc6adacb7a | -9.7246 | -49.3512 | 2026-08-26 14:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| d5130f85-4c9b-395f-a7a2-733c0dece16d | -8.8187 | -49.6093 | 2026-08-26 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 8c81ce16-2987-3fc7-894b-81462af9db28 | -11.1352 | -49.8902 | 2026-08-26 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 7e512a06-ffe3-3568-a8eb-e4624627679a | -6.6917 | -45.1932 | 2026-08-26 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 0cfc5ff2-4403-3959-974d-d649091d7c3a | -6.2298 | -53.4805 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9cca8eb2-ee81-3fce-9a5f-4430dd233530 | -8.7584 | -49.9566 | 2026-08-26 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ec192b90-3ca4-3ab7-b5a5-368933b36c1a | -13.2835 | -51.4968 | 2026-08-26 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| bb5844d3-b286-36a3-95e0-2e40abf11e7b | -11.1162 | -49.8923 | 2026-08-26 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 09780896-9533-3024-ad6a-48452bd1623e | -8.1857 | -54.9435 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c5c9aa9a-e123-36ba-b80f-3f22686ae076 | -11.0037 | -51.1635 | 2026-08-26 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 6a0a444a-151a-3524-83ad-bffec814aec2 | -13.3402 | -48.2079 | 2026-08-26 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 58fc7ddf-077b-3278-a444-cf330401407b | -7.5289 | -61.3825 | 2026-08-26 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f9bd6afb-4a68-3c38-8ebf-a4f957b93c24 | -8.596 | -54.8764 | 2026-08-26 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c403ce2f-d1cf-3e6a-b26a-3caac064bad9 | -12.1417 | -43.3945 | 2026-08-26 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 59bdb58f-ada7-3f24-8186-c06a972fd064 | -12.1422 | -43.3707 | 2026-08-26 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 1f79fa41-cd7e-3405-a2cc-0870acf92421 | -9.6776 | -55.082 | 2026-08-26 14:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 02fc432d-5011-3406-bb8e-abc5f0fc362c | -7.263 | -49.864 | 2026-08-26 14:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c73b8454-c6f1-3697-86f6-a2f47829f213 | -7.1264 | -43.1948 | 2026-08-26 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 32eb0c7b-b047-3aef-868c-b312a165924a | -6.4113 | -60.0689 | 2026-08-26 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 26bee82f-10a4-3391-8d18-a980dc98c29f | -13.3038 | -51.4304 | 2026-08-26 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| af526953-06b7-3a7a-b609-eae715a7e562 | -8.6415 | -50.3495 | 2026-08-26 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 0a683e6d-b218-3cf0-8915-1eeb41a771ad | -4.81 | -43.22 | 2026-08-26 14:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fded37c-e50f-38bb-9195-b240b10e341a | -8.95 | -45.76 | 2026-08-26 14:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98d059f1-6cc4-3147-b5af-a1a0a5c5e2b3 | -7.15 | -42.8 | 2026-08-26 14:15:00 | MSG-03 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 05659157-d6eb-3c63-be16-7fdf1ad6f1be | -7.12 | -42.79 | 2026-08-26 14:15:00 | MSG-03 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3635f35-4f6c-39a6-abee-7717c5829325 | -4.81 | -43.17 | 2026-08-26 14:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0ebc01-b8f1-33ca-816e-3c60bc416a58 | -4.79 | -43.17 | 2026-08-26 14:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6228f5b6-08c5-32cc-abc6-fd67bdbbc34b | -11.7973 | -47.6672 | 2026-08-26 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ed9d9a72-cc46-394c-8b74-e0adfdf22e44 | -8.8187 | -49.6093 | 2026-08-26 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 8ba8e421-0d87-3570-b261-27c8320be9b9 | -15.3446 | -53.8752 | 2026-08-26 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 0ba6f323-2a0f-3553-87d4-185d60809f1f | -4.8002 | -43.1709 | 2026-08-26 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 5f96738a-cad3-3bc3-a9be-32f8194b656d | -9.6022 | -55.128 | 2026-08-26 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9658b4bc-add4-31a1-87ae-348ca228f4b0 | -9.7249 | -49.3296 | 2026-08-26 14:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 8ebce39d-3253-369d-a22b-ad4336cf30f7 | -14.5397 | -52.2926 | 2026-08-26 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 1465b774-9776-3381-89c4-fa7051b32d46 | -15.7878 | -56.452 | 2026-08-26 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d2cef896-19b0-3575-8c33-1db477e761c0 | -3.2179 | -61.2174 | 2026-08-26 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| cbe8c6cd-0f7a-3999-8fc8-5e46a2c60246 | -6.7648 | -59.4408 | 2026-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e3ba97c3-8e07-31ef-862b-8bffa75760f3 | -12.1704 | -50.5861 | 2026-08-26 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| da5dc833-10ba-3e69-9e94-be9d995684c3 | -9.1896 | -50.0032 | 2026-08-26 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 9f53d494-977b-3f1f-837d-d04bc9ba8f20 | -8.5962 | -54.8563 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fda471bc-fe9b-3f56-b34e-c64ec3ab5d10 | -10.7596 | -54.0384 | 2026-08-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 207.9 |
| 23604124-d009-3473-b373-d95004fb84ce | -6.1286 | -57.8198 | 2026-08-26 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 151c522a-36cf-3e6c-8b70-bab142bed65f | -7.5256 | -44.4795 | 2026-08-26 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| efa93e06-6ec7-3dc5-98ba-c53098f397b3 | -6.2676 | -53.3768 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 12aeee14-4023-394c-9dbe-019fc2c6c03d | -6.7661 | -45.2551 | 2026-08-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a035908d-a787-36e1-8d58-f1bbfa9cca60 | -7.385 | -55.1523 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| a103da47-b45a-358b-a225-7386497b4f6b | -9.6588 | -55.0834 | 2026-08-26 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 5108d3e3-ab2f-3fa8-9352-af8ba95ec962 | -6.2113 | -53.4815 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d3b305f7-5a6a-3d99-a828-195fcfb1dab7 | -6.7833 | -59.4208 | 2026-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7169be42-6532-3604-b6d4-3d2d752d2da6 | -8.6415 | -50.3495 | 2026-08-26 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 1c11380d-bdd0-3012-9c82-45c1e5ca7665 | -11.1162 | -49.8923 | 2026-08-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c639b782-cc87-37cd-bd0e-91b9e59d8cab | -8.7584 | -49.9566 | 2026-08-26 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| df69aa9f-d712-3af8-8c8a-aebdc289d6b4 | -10.4689 | -46.2028 | 2026-08-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |


[Clique aqui para ver as próximas entradas](README84.md)
