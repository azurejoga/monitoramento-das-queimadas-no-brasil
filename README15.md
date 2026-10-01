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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 968f9abd-8038-31cd-8674-f00e4e2fe71e | -14.4225 | -51.2624 | 2026-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a9073588-aa5d-3d39-8d4d-91c4e39ea08d | -3.1839 | -54.0839 | 2026-10-01 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 9b18c8ad-24c3-350b-a97d-4f65ab0863a9 | -2.9081 | -54.1309 | 2026-10-01 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 166f7728-e75a-39e9-a74a-193f616d39e2 | -11.4227 | -51.0127 | 2026-10-01 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6a94a7d5-91c8-3181-afda-84e5fc875827 | -11.8097 | -50.5214 | 2026-10-01 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| f718f14b-de9f-357d-921d-ba2ec1d04831 | -11.81 | -50.4999 | 2026-10-01 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4c6e4af0-85d3-37b3-b130-e0a4fb09cdfa | -9.1408 | -64.3836 | 2026-10-01 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| af7ea3ea-cfb6-3780-bbad-67c1b0cefc9a | -3.1245 | -50.268 | 2026-10-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7703d85d-6181-3e81-863c-d19dd705b13a | -3.1656 | -54.0643 | 2026-10-01 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4ec7f050-4432-302d-978c-258c1f890d2b | -14.4608 | -51.2786 | 2026-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8ec85962-e179-3e44-bb0d-64ad48da1af9 | -4.4506 | -47.9329 | 2026-10-01 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 70f97537-6eee-35c4-8c9b-8abcfdbd40eb | -8.5738 | -66.994 | 2026-10-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ace84007-16bf-3b47-9eb7-b87224749a44 | -11.8287 | -50.5192 | 2026-10-01 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e186a5d3-c6a1-34d6-b8bd-228af0d936c8 | -14.4414 | -51.2812 | 2026-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| fe399067-1aab-32cd-8c75-8bca4fbaab13 | 3.2742 | -60.6105 | 2026-10-01 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 03d4f8a6-f9a6-35e7-9387-93d6fd3e5e73 | -3.5623 | -51.4838 | 2026-10-01 01:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2b5d05a1-6dca-34a3-808d-e6396a8faa92 | -3.295 | -53.8597 | 2026-10-01 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c779cf83-d789-3bee-be1d-584fdec79848 | -3.1245 | -50.289 | 2026-10-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7e2d8d23-0bfa-3ecf-aaf4-7bb5051e8d7a | -8.5738 | -66.994 | 2026-10-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4e07c61b-9429-3fd6-98ab-4bd469037575 | -3.295 | -53.8597 | 2026-10-01 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3e538968-ee67-39b3-943c-21d2e2b2b909 | -11.4037 | -51.0148 | 2026-10-01 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 0d634784-cbf9-3654-92b6-487b86a0178d | -8.5553 | -67.013 | 2026-10-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b9c3cf5e-59b1-3736-9e20-5988614b1520 | 3.2924 | -60.6101 | 2026-10-01 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0b53f084-0530-3929-b931-87b425651832 | -5.7563 | -45.152 | 2026-10-01 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5d35db28-c88a-3a48-91c4-b3427222b295 | -4.4691 | -47.932 | 2026-10-01 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d1cf0e4b-47d4-306e-a030-48f5477e4d00 | -10.5461 | -50.0402 | 2026-10-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5dcf3aa7-57e2-3471-ab29-28ce740006aa | -6.0179 | -49.5648 | 2026-10-01 02:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ff517ff5-eaea-3843-90c3-e0c6f1b66d32 | -4.8551 | -45.8407 | 2026-10-01 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 84e2f412-afd0-3698-96e9-505d8696fa7a | -3.1655 | -54.0844 | 2026-10-01 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 0a3db4f0-76bd-3a1b-b4cc-9f8fb16a0684 | -9.1221 | -64.4031 | 2026-10-01 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 5a54fa7e-bc98-36e5-90c7-d29786f34a24 | -9.1222 | -64.3843 | 2026-10-01 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 35cccd22-56bf-3473-bc56-16019d321dd8 | -3.1838 | -54.104 | 2026-10-01 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 197.1 |
| 61f49da4-17cd-3672-a3ef-9ecd84e56107 | -8.5554 | -66.9945 | 2026-10-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| e2dff9d6-c481-35ed-9a44-3770edaf4fcd | -4.4693 | -47.9103 | 2026-10-01 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| aec64c5c-f79f-3883-8655-f1f0d4fc3fb0 | -3.1471 | -54.0849 | 2026-10-01 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e441f029-f761-3316-a585-40232aae666c | -10.7664 | -50.5299 | 2026-10-01 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2823e001-e926-34cc-9705-33c354664505 | -8.5738 | -67.0125 | 2026-10-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2ffed8ce-38a7-39f4-b3cf-c7a376fc381e | -3.2766 | -53.8602 | 2026-10-01 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1eb04802-f163-34b0-9328-f0ca43862b74 | -8.5369 | -66.9949 | 2026-10-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8bedeaf3-fd35-3566-ad89-b33c4366a637 | -7.6187 | -44.5624 | 2026-10-01 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2ffbe9ae-7488-32a2-98e7-dce0c32a990e | -3.1839 | -54.0839 | 2026-10-01 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6fc2c2b5-aca6-3b5c-8388-b1d04931dfd4 | -11.4034 | -51.0361 | 2026-10-01 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9cad8fa3-2dc0-3354-922a-02890b238e28 | -3.1655 | -54.1045 | 2026-10-01 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| b98e29c4-fe79-317f-9433-96f151c42b15 | -8.6497 | -62.6672 | 2026-10-01 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 44b80dee-a3fb-3b7f-be4b-7acbc825779a | -13.0968 | -51.2003 | 2026-10-01 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 55bc7763-1ae1-3e04-8246-c1a263f81a17 | -3.1245 | -50.289 | 2026-10-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c4f87dcf-e413-32d9-a59a-60d6a4bfa088 | -4.4506 | -47.9329 | 2026-10-01 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 66b36b7c-23a3-3fa7-b3ea-e2d5f120c286 | -10.5648 | -50.0597 | 2026-10-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3f785cb2-7176-3436-9547-d133e18947ea | -13.6671 | -53.9314 | 2026-10-01 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 94b106d4-d4bb-3bf4-af43-00229fbea41a | -2.908 | -54.151 | 2026-10-01 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 344a8476-de49-30e8-90a2-939bfcb567d6 | -3.106 | -50.2896 | 2026-10-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 31236920-5db8-3e66-bb7e-1d562dc191bc | -8.5554 | -66.9759 | 2026-10-01 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5f7d2ef2-83fb-3a85-b978-ae8dacb92dc2 | -4.4507 | -47.9112 | 2026-10-01 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2ff7a5b1-0927-343a-932d-b613e552b4d6 | -12.1857 | -48.4345 | 2026-10-01 02:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 842b1fb5-ffdf-3ea3-b812-173003bbce1d | -10.565 | -50.0382 | 2026-10-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b8f1830f-49af-3fe0-a351-2ef84c92410d | -13.6479 | -53.9336 | 2026-10-01 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| eb6647c7-d244-379c-86d2-3e1ccb111703 | -3.1061 | -50.2686 | 2026-10-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 57ea66cc-e17a-3a1c-8fdb-e2d5fd861eac | -15.4978 | -46.1294 | 2026-10-01 02:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1f059fca-87da-354c-81c3-1128c1a1af58 | 3.2742 | -60.6105 | 2026-10-01 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| db3f6968-9c8c-39e7-9b59-55269edf85d0 | -9.1408 | -64.3836 | 2026-10-01 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| ef16238d-4ef0-3e4c-a3c8-638f77c7a982 | -6.6758 | -58.8654 | 2026-10-01 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 1e1a5ee7-3386-3bbb-ac34-a02e944f1a2f | -20.1886 | -47.397 | 2026-10-01 02:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 99d557b9-3d37-36f9-a220-9f1bacbe372d | -12.0925 | -50.7023 | 2026-10-01 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 5990001d-25fb-3e37-a510-fc0f7c42559c | -5.7563 | -45.152 | 2026-10-01 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| aaf6058b-25db-3d07-a300-c74cae994b3f | -5.7561 | -45.1747 | 2026-10-01 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 31b188a2-6fd2-3119-b83d-d31f386321bc | -3.1655 | -54.1045 | 2026-10-01 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 578ca88f-81e2-3e07-bec5-55ad2cd51d94 | -11.81 | -50.4999 | 2026-10-01 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0a5a21f5-c6fc-367d-9848-0038844a16d8 | -6.1487 | -47.2651 | 2026-10-01 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2e653f2a-c7a1-3c21-a761-744814e6c31e | -11.8291 | -50.4977 | 2026-10-01 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| f03b67c5-4be8-373a-8288-94edcb9d82f2 | -13.6671 | -53.9314 | 2026-10-01 02:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6ec3ba3d-7ee8-3d3d-ae28-feeeaa640abf | -4.4507 | -47.9112 | 2026-10-01 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| ec3b8f23-9b7f-385c-b769-302f0493cc05 | -11.2087 | -45.1939 | 2026-10-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 93895ac4-eaec-317f-a0b1-1009b5aec60e | -11.8097 | -50.5214 | 2026-10-01 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 238071de-9f85-3197-8406-2e32fd1d004b | -20.1886 | -47.397 | 2026-10-01 02:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 88b2e8a2-e043-315e-8e36-af56a710f91c | -8.5369 | -66.9949 | 2026-10-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| eb6e2520-35c6-32ce-be38-7b2c5b6aebf2 | -4.4693 | -47.9103 | 2026-10-01 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b4b56e95-c22c-3f95-9bc7-c760092e70d4 | -13.0964 | -51.2217 | 2026-10-01 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d9667666-b810-36ce-9c14-82c396db0826 | -9.1221 | -64.4031 | 2026-10-01 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 742f3887-4fb0-338e-8463-26f0a6af1501 | -12.1857 | -48.4345 | 2026-10-01 02:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8362a355-d7a3-3a76-aa94-e5b92c9a7302 | -6.1485 | -47.2871 | 2026-10-01 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4449adac-95b5-3ce3-9af9-d6d4512813cf | -13.0968 | -51.2003 | 2026-10-01 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 997cf534-3c9e-3db3-9866-0292794518e6 | -8.5554 | -66.9759 | 2026-10-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 6cfe675a-31ef-3df4-99b1-73d32490fe17 | -8.5738 | -66.994 | 2026-10-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c831e48e-a19f-3aa5-ac9b-b986286f2f2c | -4.8551 | -45.8407 | 2026-10-01 02:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 718d17ff-4024-306d-9c4d-9c8a129772f9 | -3.1061 | -50.2686 | 2026-10-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 10177500-c2ef-363b-80a7-c434469d6cb1 | 3.2924 | -60.6101 | 2026-10-01 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5d278789-9cfa-35a8-bde4-32d3a799b586 | -3.1839 | -54.0839 | 2026-10-01 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 74ff4c53-6446-360a-9296-815dc34a1561 | 3.2742 | -60.6105 | 2026-10-01 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 7a72e795-8d96-3927-9cf1-59605aca5e20 | -3.1471 | -54.0849 | 2026-10-01 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 01526c31-2c14-3068-9ff6-81794093e2f7 | -9.1222 | -64.3843 | 2026-10-01 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 127.3 |
| ceb960f0-6c0f-3d6a-8a98-0727af65998e | -14.8762 | -51.8427 | 2026-10-01 02:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 84a082b0-d976-3575-9026-939e374d0d16 | -13.6479 | -53.9336 | 2026-10-01 02:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 794240c3-9c5d-3889-acc1-629f601f37dd | -11.7906 | -50.5236 | 2026-10-01 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 03e3ae23-66ba-365d-ad3e-df274c3173f9 | -3.106 | -50.2896 | 2026-10-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 3fc64b32-ba80-3042-b6f7-a768bb1da77c | -8.5738 | -67.0125 | 2026-10-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| bf553244-4184-3be6-80c6-bc6c70f00a37 | -11.791 | -50.5021 | 2026-10-01 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| a03525ab-be2b-34a3-8f2c-c74a4f5a1d7b | -3.295 | -53.8597 | 2026-10-01 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 6ace1423-a218-3b3e-b2ef-c515760c5900 | -11.8287 | -50.5192 | 2026-10-01 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 086cd578-8156-3136-83e1-98d68501a831 | -3.1245 | -50.289 | 2026-10-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| debf0331-8194-3753-8b92-c17dadc0c61e | -6.0179 | -49.5648 | 2026-10-01 02:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |


[Clique aqui para ver as próximas entradas](README16.md)
