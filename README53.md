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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f17d996-c91d-3f3f-8567-6682468bfeab | -6.11573 | -57.82293 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 201dcb64-aa17-3c04-a901-17fc94b00ec2 | -6.37225 | -54.94377 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77ca4b95-22b5-3966-ae2a-8df5b281585b | -6.11798 | -57.83058 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba1378bf-86ee-39d3-b48f-2d42d0c6d73c | -7.30175 | -49.54311 | 2026-08-26 05:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d214c94-b621-33a8-b0d6-880d5ad53297 | -6.14321 | -57.84549 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9c31e1d-46bf-342e-a6d7-56de8c6c1284 | -6.88825 | -59.04587 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2a2307e-db94-3c8e-ab70-496c70f30aae | -3.78096 | -59.28244 | 2026-08-26 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c2ab69-a17b-3059-9dfa-b8a2e9bf96f2 | -7.06145 | -59.23384 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5e43f2-61e2-3472-9eb0-d76d1a9a7436 | -8.16788 | -46.19757 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cc46bf12-9713-3213-8566-f2e4b94d5dcf | -6.14287 | -59.92364 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c408e0bf-a3f7-3602-8b76-fd9baad80dda | -6.40581 | -60.05203 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa572309-c5ba-3fa4-9968-e18af559f337 | -6.23273 | -55.48021 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 134f8fa7-3045-3b7d-b0ac-51ff3592e8c5 | -6.14888 | -57.94101 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfba0000-392c-3d3d-bf18-2733eb2bebab | -2.79863 | -49.58025 | 2026-08-26 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 537818f4-b2a7-378f-b598-7127897ccfb4 | -6.97018 | -59.08732 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b4a50e3-cdb1-3901-9059-22543d626f14 | -5.65545 | -46.95338 | 2026-08-26 05:27:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a8d8fd4-eae7-36e4-bd75-2c397f2c7d6a | -6.26984 | -53.37722 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f9037fca-f57f-3157-9687-a4f7164777a1 | -6.25241 | -53.37855 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 731538b1-6132-3874-a289-dbdf492b88ad | -8.14018 | -47.51267 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bfd3555-aff1-3b3f-b985-c36d89e3b7ae | -6.64232 | -58.5004 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dee7192e-6ccf-3f9c-a76b-524f6ebd8b57 | -4.92856 | -55.77262 | 2026-08-26 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22be15c6-beb8-388b-bd1f-33f99599fbbc | -5.346 | -45.1661 | 2026-08-26 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f36728bb-e3ca-3145-a6f1-2c292cda3b1d | -7.31547 | -61.14381 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aaba059-290b-34b6-9d01-2a35f5f5c082 | -8.01423 | -51.81998 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc1a7e0a-12b9-30c6-9b91-1a7fee53b14b | -6.77886 | -59.43746 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e0627bc-800a-3421-9197-f8dc2d385042 | -7.20911 | -60.61597 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73973b90-65d5-314b-8211-daec1973707f | -6.10993 | -53.84395 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b2ce43-cae9-3a4f-962a-464ae74861bf | -4.06028 | -56.33746 | 2026-08-26 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdafe0dc-4b30-3742-b2ba-ce6cd4b087d5 | -6.65438 | -59.11203 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fede5ca-698b-38bf-b2b9-43ad8506c002 | -8.01093 | -51.80838 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dadf056a-6384-3999-8511-17e8de471b12 | -7.01382 | -59.23631 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32c89b9a-63e9-3ec9-b091-501482ced0cb | -9.03641 | -50.79502 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f45ac269-51e1-3aff-9f35-5c25af66e05d | -3.10715 | -61.22257 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f598e07c-9cee-3bbb-b599-b7c5f166bdf7 | -6.30476 | -53.5742 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10d166a4-f10f-33df-bc5e-f4772736d152 | -7.52169 | -61.38031 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 10410958-896e-35e2-bc0c-5ebb20cabfa4 | -6.8581 | -59.40747 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79520d5b-2c91-33df-9568-6f727f142769 | -3.10035 | -61.19658 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb672181-9d62-39af-9e30-ee010728db9d | -8.77797 | -49.97247 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fdec39c-26b2-3eb2-ac3a-45ad9d71c8f1 | -6.70388 | -56.34368 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dd2baad-df61-32cc-a6b5-6beaf8e335dd | -6.60279 | -58.39032 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7905faeb-9883-369d-ac7d-7c84dfdd32d6 | -8.58808 | -54.83628 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11f7113b-d655-3ca6-98d3-f4edd88db76e | -4.2217 | -56.08225 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c67b56d-563c-3939-bfe2-e353e15535b5 | -7.02433 | -59.23442 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29d4e9f3-9b49-3f48-a7bf-e31609719339 | -9.01731 | -50.77807 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df8676e6-fda5-3082-ab03-5fcc9170df2c | -8.77845 | -49.96883 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 650e0390-e946-3424-a9ed-468907ad9cb4 | -8.64433 | -54.74535 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61f927e3-0623-38ee-8158-8c108d371307 | -6.73176 | -59.66902 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 839760a5-b83e-3ca3-99b7-87c024516fa7 | -7.31829 | -61.14811 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b3ad9ac-0af1-3b61-be80-74eb28d98cd0 | -7.37812 | -55.19461 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a86a91-1ade-3870-94d4-0c9c5a890f04 | -6.64286 | -58.4969 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be996968-4342-32bd-9539-9d2a6bd8ab9e | -6.25775 | -53.37143 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3746db7e-e685-34a3-a3d1-1dbae35147a3 | -7.11421 | -56.55775 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7d34c36-7f84-35af-9b40-53783ed865b9 | -9.02205 | -50.78258 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce1299a7-90c4-34a0-b568-9071ab17bb9f | -6.14553 | -57.94048 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0320655b-1720-3a02-b0aa-13b4e66edb57 | -7.39825 | -55.16405 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88551541-fb62-372f-8f4b-439f191ffb71 | -7.21306 | -60.61292 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0993cbf-6092-3018-910d-f7ead5d42155 | -6.12526 | -57.8281 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c9557183-2d12-38f4-a119-5fe80fd960d0 | -6.26677 | -53.36876 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 236285bb-7cde-3ace-ba5c-c6d999e8b267 | -6.30533 | -53.57044 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd0178d3-e9f7-3707-8f1e-808fdfe0f143 | -6.97559 | -58.32288 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bead10b-ebb0-3316-aaa4-26a7c172550d | -8.16718 | -46.19113 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4048489a-b8b2-3154-8dfe-533640fa6dc4 | -8.15094 | -54.98525 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e723332c-1074-339a-bd76-e881892caa6c | -6.81111 | -58.97667 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9afe1000-13ee-3e84-b32a-6b56388c9eaf | -8.61875 | -54.73995 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e13cab45-8fa7-30ac-b06f-853957c4db67 | -5.56077 | -50.49164 | 2026-08-26 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bd72677-1ff7-34a7-9c53-46c9a85d3198 | -6.30116 | -53.5698 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2463ff92-b5ee-342e-9ab0-2b8644f59323 | -6.72572 | -59.45036 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 104170cf-42ff-3765-ad54-3ed09223be9d | -8.53325 | -55.34763 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64bf8afc-bb4e-379f-bbd4-742b26c4f6cc | -5.94068 | -57.73418 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98914cd6-c3f3-3e94-bb2f-809ebcb22450 | -2.49926 | -48.13843 | 2026-08-26 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37d778e3-fcb4-3350-aa7f-87600752b226 | -6.70327 | -56.34767 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 355b8366-dcd6-3e99-85cf-8dfa396417ee | -6.63127 | -58.51308 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c7b8f91-b258-38e8-a624-7c2f22480be5 | -6.61111 | -58.38089 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37516d8d-a4e7-3f06-ac41-d7409989337e | -6.62403 | -58.49406 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0209249e-3517-315a-a1df-5a72fdcf38f7 | -6.23162 | -55.47397 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041bda44-b475-3146-8f96-516daf5bd292 | -8.16539 | -54.96815 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55bed633-21ba-3f71-925f-e04d92cccf82 | -3.09934 | -61.22547 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60b073a6-454b-301d-b3f6-ca3bf391ceae | -6.86861 | -59.40559 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ebe2f1f-3e7e-3df4-b5c9-5c21ee87cea4 | -7.21248 | -60.61652 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4f9a482-9503-3cc9-b5e0-6ce6d62453b3 | -8.56656 | -47.42348 | 2026-08-26 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18261aba-1696-30b7-b068-20f06f941840 | -3.21857 | -61.1563 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd88d737-8ce3-396a-bfa5-3e0af6a6e1ef | -6.80104 | -59.59439 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bdc6127-6ec3-3d89-b60c-132b91318652 | -9.03211 | -50.78731 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35f8a52e-f40a-349b-a57f-c7d0a01541c4 | -6.80319 | -59.68763 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c5a839a-4e68-3136-98df-ca58d05424cd | -7.06864 | -59.23143 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66e251a8-82c0-32fe-9bb6-2bab4ea988af | -7.10945 | -56.56516 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06c228a2-8fb2-3e83-abac-724085292988 | -5.78887 | -57.60793 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55774353-1c11-3aba-9bed-d069455a6190 | -6.71248 | -59.1319 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a37134-3df2-3569-af5a-ee323dafe59a | -6.25467 | -53.36298 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9195e0e4-f151-3934-a224-f35ef8f2fa55 | -7.49885 | -55.371 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db2a6d0d-6088-3e80-889c-d3181620a51e | -6.12973 | -57.82149 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e321b45b-2e8e-354c-844b-547b705c23f8 | -8.09608 | -51.67709 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56d870b5-31cf-3210-9332-6c6f68a9d92d | -6.26255 | -53.36814 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0807616d-c99f-374d-8e3b-9e73a345fee3 | -4.59355 | -56.05658 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 968501f6-f186-3885-87b3-70008938ba48 | -8.52656 | -55.3124 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d148ed4c-3fd0-38aa-adff-995ccd8e503e | -5.97039 | -57.63244 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a02cee7d-cacc-3d58-bae3-d06f4884dc5d | -7.86447 | -46.10461 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 754bae95-db11-379e-a559-015e9481ccb5 | -6.82264 | -58.65088 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ae820d4-33e1-3746-b679-0461f6a47c83 | -8.5931 | -54.72036 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aefb96d-ceba-3d8e-b7d6-6ba0ea1e541c | -6.99006 | -59.27878 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
