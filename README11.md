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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a845224-d802-3f54-8dea-b89519d33170 | -10.46 | -46.7885 | 2026-10-01 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 73670288-7664-346d-93d5-551a58c120b8 | -8.9861 | -65.6993 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| caec4c8a-be26-3934-ba9e-e3e35732ce25 | -14.1547 | -51.1271 | 2026-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 42814d70-8c92-3430-a610-8fa0bc29b39d | -14.4228 | -51.2409 | 2026-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| b35834f9-35af-3da0-89ef-0658528465b9 | -9.0046 | -65.6988 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.2 |
| ffb97db3-918b-347b-a5d3-75afdbb211b5 | -5.7357 | -43.2682 | 2026-10-01 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4f6c4d37-4c6c-3c82-895c-93dd4f77ffd2 | -4.0477 | -54.2394 | 2026-10-01 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 13e00f1d-f91d-306d-bedd-3698e7c400e3 | -8.5554 | -66.9945 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 222.6 |
| 88cc3a56-302a-316c-923c-8ec848d1b7b0 | -3.1245 | -50.268 | 2026-10-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f13e9539-34a4-3766-808d-6dc735170804 | -6.6757 | -58.8847 | 2026-10-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9c081877-5537-3d7f-bbf0-ea816c4f3935 | -5.7355 | -43.2916 | 2026-10-01 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a6f5ad49-cef0-3960-81ea-8d3e4b66dd79 | -5.7563 | -45.152 | 2026-10-01 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 164ba11f-8be1-3603-af93-d973827649fd | -5.7376 | -45.1533 | 2026-10-01 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 417cbbe3-9e69-36b1-ae1b-50727fccc2a7 | 3.2924 | -60.6291 | 2026-10-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| fa986bd5-dc54-30c8-be50-c2da3f4b8db2 | -14.4422 | -51.2382 | 2026-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 62a63e79-8374-357b-b86b-95ee545ba1bc | -4.1667 | -48.894 | 2026-10-01 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4d26202e-69b6-316e-8e4d-65e65d20d078 | -3.1245 | -50.289 | 2026-10-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ecb3f451-808f-372b-9837-5712ab1c442d | -9.0045 | -65.7174 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 40cf33ae-190e-375f-8bb7-dfcf66378c09 | -10.7474 | -50.5319 | 2026-10-01 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 59f5eceb-d663-3af1-9a69-7bb7a3ee4f37 | -3.5623 | -51.4838 | 2026-10-01 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| ebb45dbd-05be-3f76-bbf7-5304ffd040cd | -10.4604 | -46.766 | 2026-10-01 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7d21273d-882d-3245-9527-c0d335cf326f | -14.4418 | -51.2597 | 2026-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 364.9 |
| 62a048c6-3560-33c1-8752-4a3879e5bc81 | 3.2742 | -60.6105 | 2026-10-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 4b36a56d-ee7d-3112-8673-01b9f3ac13b6 | -7.108 | -43.1497 | 2026-10-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| f8dd56ff-b13e-3dcb-97db-c9a3b037dd05 | -10.7285 | -50.5339 | 2026-10-01 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5bb9875e-18a5-3e7f-81d4-cdb8680e04f8 | -9.1221 | -64.4031 | 2026-10-01 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 43864438-554f-3b67-9843-45d4c2f8df2c | -4.1482 | -48.8948 | 2026-10-01 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 97e506d8-4cf1-3f17-9840-ac7637c4da52 | -17.5682 | -40.4116 | 2026-10-01 00:50:00 | GOES-19 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.8 |
| 6d5ead07-af56-39df-9eb6-19825fd1e347 | -7.1266 | -43.1714 | 2026-10-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| ca56de65-c6f4-30a4-af14-6f840ce6a109 | -6.6758 | -58.8654 | 2026-10-01 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 77d3bbf6-cff9-35c9-8854-94fd28636bc6 | -9.1222 | -64.3843 | 2026-10-01 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.6 |
| c6d2b9cb-86be-3537-a5ad-1957bb97c2d2 | -14.4225 | -51.2624 | 2026-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 443.6 |
| 2ffb056e-3328-382a-89c1-cdc5e5e43f66 | -8.5738 | -67.0125 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 47645dda-56bf-3851-b5f0-fc3075f6aef3 | -10.7282 | -50.5552 | 2026-10-01 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bdd0aae0-175f-3c54-85a6-e33fd311d5e4 | -8.5554 | -66.9759 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 55b928cc-8480-376e-b201-36930dd46d20 | -2.908 | -54.151 | 2026-10-01 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 664d9727-57dc-39c6-a6fc-dd79bd1bfe72 | -13.6671 | -53.9314 | 2026-10-01 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4b3dcc14-fbeb-33c2-a201-f970eff10bdd | -6.9317 | -59.2798 | 2026-10-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 36071158-f5e1-3a5b-bda4-e426a1d27105 | -8.5738 | -66.994 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 8c3cba85-fc1d-3d8a-b284-444f44e4169f | -6.914 | -43.6816 | 2026-10-01 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| feb7b1a4-16f2-343d-abad-085cbc61e0cc | -10.7472 | -50.5533 | 2026-10-01 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 517c61e8-e8a4-3414-9756-6fd9af92fc44 | -6.895 | -43.7066 | 2026-10-01 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 9cb083c9-649d-3b79-bf01-54d502958f8b | -13.6479 | -53.9336 | 2026-10-01 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 0b5dd587-6eb3-37e8-b6c0-13b3c4205bb6 | -3.5809 | -51.4625 | 2026-10-01 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c25fc27f-b2bf-3de4-b83c-0520a38de6f4 | -14.4414 | -51.2812 | 2026-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| acb6b54b-ac98-3f73-b431-cbd7e5fe7c63 | -5.7542 | -43.2901 | 2026-10-01 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 10b7b0fe-84cc-3a25-bab6-91278596c4dc | -10.4791 | -46.7862 | 2026-10-01 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 77a61963-16ad-3082-94a2-14b5296154e5 | -6.0179 | -49.5648 | 2026-10-01 00:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 6ee8ae9b-028a-339d-a6f0-7734342dc0d5 | -13.6668 | -53.9522 | 2026-10-01 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| bdcd2703-3fb1-3d64-b06b-5e9b5f4ff4a9 | -7.1078 | -43.1732 | 2026-10-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 3a0d8548-38d3-3494-9977-4ad2ac18a988 | -3.295 | -53.8597 | 2026-10-01 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 6c1d3a3a-f647-32c6-9d4c-229937dc50a2 | -3.1061 | -50.2686 | 2026-10-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 31f3d57f-9598-3ba1-a410-e710628841b3 | 3.2924 | -60.6101 | 2026-10-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 4bf92432-62f4-3a11-94f5-66cb378056db | -3.2766 | -53.8602 | 2026-10-01 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ede41f88-6b48-32da-beba-8e6c9bc98720 | 3.2741 | -60.6294 | 2026-10-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 8770226e-cce6-36e4-93cc-ec2f07aec016 | -8.5739 | -66.9754 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0308f86a-41f4-35e7-9748-3d89cb243a38 | -8.5553 | -67.013 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5c8915bd-5684-3a5e-be9b-86699dafcbd2 | -8.986 | -65.718 | 2026-10-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b74c06b6-6ffe-3fc6-a758-0b9e59279e5e | -3.106 | -50.2896 | 2026-10-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 5a0adc08-ad63-3c22-933e-68739f002f71 | -3.5808 | -51.4832 | 2026-10-01 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 49ad9879-803d-3b73-9cb7-1869fbd71f80 | -10.4794 | -46.7637 | 2026-10-01 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f91bd378-85c5-3562-abfe-492c38551e21 | 3.2741 | -60.6294 | 2026-10-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f5418920-40de-38fb-83aa-cdf2f8cdc3ba | -3.1842 | -60.0607 | 2026-10-01 01:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4f80e0a4-e24e-364f-b5ed-2341a8d5513b | -3.5809 | -51.4625 | 2026-10-01 01:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 87e6be8b-c4fa-3220-9a29-7561358bbfe5 | -3.1061 | -50.2686 | 2026-10-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| cbf69fc0-51e7-3b31-b3ed-bbc50f59ed54 | -9.1221 | -64.4031 | 2026-10-01 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| adebcadf-d5ed-383f-8cbd-8ece7545a92a | -14.4418 | -51.2597 | 2026-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 120bceaf-e219-392c-b85d-845d86cfc3d4 | -14.4228 | -51.2409 | 2026-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 61841a8f-4283-3486-9a3f-e344ebd8fe6e | -9.1222 | -64.3843 | 2026-10-01 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 30e37a05-94d0-3ab2-ab3a-e5e9336d59e5 | -18.0658 | -51.1301 | 2026-10-01 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7b1c273f-b1bc-3f66-9326-55337ac4c40d | -3.2766 | -53.8602 | 2026-10-01 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0bd8c635-eae0-379a-90ef-572ebb6cdc72 | -9.0045 | -65.7174 | 2026-10-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 77a709dc-8a1a-3265-8205-c1fbf6a63ec7 | -9.0231 | -65.7169 | 2026-10-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6d49ae8d-26e8-3406-9fe9-88282f9bff86 | -18.0458 | -51.1336 | 2026-10-01 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| cea80355-46fa-304d-9ded-a62027c106e3 | -5.7376 | -45.1533 | 2026-10-01 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a2f30352-abdd-3592-adb1-9608a7fc6654 | -9.1076 | -67.7215 | 2026-10-01 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c46dda44-cffd-3300-b8d2-56caeabf04aa | -13.6479 | -53.9336 | 2026-10-01 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6531a586-f3a4-31bf-8151-8cc19b37faa0 | 3.2742 | -60.6105 | 2026-10-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 73becb85-1074-3b6b-a08c-bdebde7db59b | -3.1245 | -50.268 | 2026-10-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fd180375-f8e8-3fd4-9ecd-07e172fa3ba8 | -8.9861 | -65.6993 | 2026-10-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| ac05d1ee-d276-3bc5-a771-62c2dd0ef317 | -6.6758 | -58.8654 | 2026-10-01 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 29543f87-e0e8-30e1-a928-dc6d39d5069b | -14.4225 | -51.2624 | 2026-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 8e0595f7-8f80-3cea-ac7b-75d929a73e6a | -3.1245 | -50.289 | 2026-10-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1f587a09-fbb5-37f0-a4d7-1fb9383dcdb6 | -14.4414 | -51.2812 | 2026-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| ad5e6036-0b5b-3b2b-99d6-9c1752a12196 | -3.5623 | -51.4838 | 2026-10-01 01:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 0e682444-fd98-3eaa-87b4-966df8f2790c | 3.2924 | -60.6101 | 2026-10-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4bc187e2-24c8-3e0f-aee3-d49766e70778 | -2.908 | -54.151 | 2026-10-01 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5ff2a69a-f2bb-341a-b0cb-86c60ebf480a | -5.9993 | -49.566 | 2026-10-01 01:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| dec3af1f-3c42-37df-9424-15182992620b | -9.1408 | -64.3836 | 2026-10-01 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 372b9811-f460-3cd4-a4d5-cdb7494fc2dc | -3.5808 | -51.4832 | 2026-10-01 01:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 13ee6388-5fbd-3604-8a29-ec89a9458860 | -9.0232 | -65.6982 | 2026-10-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9adb601d-fba0-359c-b28d-c92d69f51f14 | 3.2924 | -60.6291 | 2026-10-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5f9d6803-635b-308a-bb94-20adc9ae077a | -10.4791 | -46.7862 | 2026-10-01 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 4f8cc78e-7e53-39ed-8040-778499fdf120 | -3.106 | -50.2896 | 2026-10-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| c1addd76-2c77-391a-8b8e-43c170843e91 | -9.0046 | -65.6988 | 2026-10-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 182.3 |
| fac5bb5a-f626-38e9-87a8-4877689010ba | -8.986 | -65.718 | 2026-10-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 38b24377-5d15-3c79-9406-7882a834002e | -13.6671 | -53.9314 | 2026-10-01 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 72ba8113-a605-3280-8f73-74b660ce4223 | -6.0179 | -49.5648 | 2026-10-01 01:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 84fbdf2c-68bf-3dad-b976-4a385558fee4 | -10.4604 | -46.766 | 2026-10-01 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 580699fd-953e-3e7a-99da-5b66ba6ca7f3 | -5.7563 | -45.152 | 2026-10-01 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |


[Clique aqui para ver as próximas entradas](README12.md)
