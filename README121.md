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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c246bdaa-d6d4-3f7a-9873-213e6fe3d2e0 | -14.7088 | -48.399 | 2025-10-07 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| a915d5d3-b9a7-302e-88f2-7cc5de31af30 | -15.5808 | -52.5769 | 2025-10-07 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6f21e246-6675-36cd-b718-d157f9404c9c | -7.7371 | -42.5668 | 2025-10-07 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 017552cb-5347-32ec-9e6e-967213f43b84 | -13.2426 | -47.2391 | 2025-10-07 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 1ba474d7-c1ff-3d85-897d-c232287f4d0a | -11.0262 | -50.9067 | 2025-10-07 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9acf5354-f86e-3c24-9835-ad928fbfe503 | -8.8986 | -47.6483 | 2025-10-07 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 08fe1465-8485-3603-9d96-c75023b87b6b | -11.7217 | -45.3738 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 095f18ed-2338-3ccf-a19b-a614b42424b2 | -15.3737 | -47.3201 | 2025-10-07 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 173.0 |
| c165ff98-2281-32a8-bf8a-695ecb1de469 | -18.2856 | -45.4587 | 2025-10-07 13:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| fc53500e-9c87-390b-922c-484e37acf5fd | -8.8792 | -47.6942 | 2025-10-07 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| fd21a68c-96ef-355d-b397-b00d0d8883ee | -9.1975 | -47.8381 | 2025-10-07 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 94d3e92e-41d1-3238-9bf6-cee319ad57dd | -7.7743 | -42.6103 | 2025-10-07 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| e4a36a2a-f212-3b9f-8174-ad040bc655a1 | -11.8221 | -45.1059 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f6a870a5-b613-342c-80ab-c1225e015373 | -12.9619 | -46.808 | 2025-10-07 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 8ba81517-b532-34f3-ad1c-83885ffde0d0 | -7.8119 | -44.1516 | 2025-10-07 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ab95c943-e665-32af-8d0c-f9883a3cd5ab | -8.5602 | -44.6264 | 2025-10-07 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dfa1d18b-090d-383f-82ec-387d67c522dc | -15.6202 | -52.5501 | 2025-10-07 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7c9a6b64-7662-31ac-a2cf-e1197f5d7ff2 | -12.7637 | -50.4921 | 2025-10-07 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 199.7 |
| f03222da-9cae-34db-80ac-53aa591e0257 | -11.0451 | -50.9047 | 2025-10-07 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 09642a47-2a67-3b58-8e28-66d225115f4b | -11.1644 | -54.8804 | 2025-10-07 13:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 469.2 |
| 0787644e-a58c-3ae9-8083-abe0641c01d9 | -8.1055 | -44.7891 | 2025-10-07 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| f3431e5f-2cf3-3d97-94c8-8abbcc723278 | -11.7837 | -45.1115 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 007a29f5-60bb-3ec3-b5fe-3cc9d9f745f1 | -10.4108 | -50.2683 | 2025-10-07 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 59183890-289a-3ccc-b2e1-acdd5d84f97f | -8.1894 | -44.1125 | 2025-10-07 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| cd90f64c-ff13-3199-b56c-1c3a9a99e02e | -10.8919 | -47.1153 | 2025-10-07 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 297.7 |
| 416fc6bf-582a-3a4f-9a1d-3244aaf610ba | -7.9011 | -47.8072 | 2025-10-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 2715657a-74b3-3b5a-b978-4dfc0218b2ee | -14.2949 | -45.8613 | 2025-10-07 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e9ebcad6-8eab-3c19-95e3-69b2e7b2d34b | -8.4824 | -46.2912 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| da0d2dde-890d-3e02-af49-19b2bd620041 | -14.5057 | -46.9242 | 2025-10-07 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c221778a-98f5-3420-ade3-e9fbbff9ea71 | -10.4054 | -45.3931 | 2025-10-07 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 96428f21-3a28-3116-a467-e9b11e36a163 | -8.8618 | -46.0949 | 2025-10-07 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 817604c9-a4da-3b35-8cf8-c47bbf862cd6 | -10.3665 | -47.9978 | 2025-10-07 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e59c8dac-db4e-3933-a0c6-be97d6f76e76 | -8.1136 | -47.2606 | 2025-10-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e58efc24-3eae-319c-a68e-545ffea211a7 | -11.8029 | -45.1087 | 2025-10-07 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 4291e6f6-21af-37d3-ad76-50af8951b309 | -12.2219 | -44.2308 | 2025-10-07 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| fccdccc5-a838-344e-b88b-6fa5553b7b8f | -18.2862 | -45.4348 | 2025-10-07 13:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| deecbc06-29c9-37ef-b936-23b8ac0cc668 | -8.5393 | -46.2631 | 2025-10-07 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 03408343-3dda-31aa-b6d2-591c2ded5239 | -8.4519 | -47.2509 | 2025-10-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5c69167f-12fe-39b3-9487-81591bab2743 | -17.9784 | -44.9817 | 2025-10-07 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0b494bd5-6293-3fc3-b95f-7ba4e112087a | -7.7182 | -42.5688 | 2025-10-07 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| f37bc9a7-9d04-3bb9-ae8c-cb2e2f92c83e | -12.4665 | -45.5386 | 2025-10-07 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| bf47b4eb-1e45-382e-9e8d-a03f4c3ea806 | -8.1615 | -43.3465 | 2025-10-07 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| a8b0913e-dc6f-342d-a453-eefdae5187f7 | -15.3737 | -47.3201 | 2025-10-07 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 8112cbfb-7a96-3c78-b862-da68907cc6dc | -8.8717 | -46.7878 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c363bde7-bbab-37f7-8379-acb1cd341d8f | -10.4058 | -45.3702 | 2025-10-07 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 938865bd-617f-3172-b1b2-506b08d3efce | -8.1055 | -44.7891 | 2025-10-07 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9eb4ecba-e1d5-382c-9d31-90bf19e848bf | -14.8645 | -51.4158 | 2025-10-07 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 8e9c9597-ee3d-33db-a29c-cf52d945b974 | -8.5395 | -46.2406 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 1c6097df-45c9-374c-98da-344018d1bbaa | -12.4916 | -54.7364 | 2025-10-07 13:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8029aaa3-1656-3313-8683-82b1a0432073 | -8.8792 | -47.6942 | 2025-10-07 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e2eeb52c-8e27-351a-b315-6d33397819be | -10.0868 | -50.5141 | 2025-10-07 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a364c2ed-1f48-3845-a730-1ccd2d5a8284 | -12.4665 | -45.5386 | 2025-10-07 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 3533060c-55e8-3df8-b1c6-843faeb7d4a4 | -9.6098 | -46.6416 | 2025-10-07 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| a97db7f4-4380-3347-980d-b96748303cd7 | -10.3854 | -47.9956 | 2025-10-07 13:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f2d51cd4-d0ae-374c-b10d-94e78083ff7b | -8.2346 | -49.8734 | 2025-10-07 13:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e2727de3-3858-3be3-98af-5a301d63bcff | -11.7221 | -45.3508 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| fd227cdb-15ef-3f87-85f6-230553212854 | -11.7833 | -45.1347 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e4a066de-df7a-3638-83e9-4989e22f0fbb | -12.7637 | -50.4921 | 2025-10-07 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 1c3b55fa-90f8-3d28-b1b2-87862b822f67 | -8.6397 | -47.2769 | 2025-10-07 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| cad4830c-48ac-3d08-832c-99d41a13230b | -13.2232 | -51.6744 | 2025-10-07 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| ecfe99a0-2e90-369b-a066-915f0b9e08ea | -17.9784 | -44.9817 | 2025-10-07 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8288af81-bc83-3cf3-85ec-9dc361b0442d | -19.5789 | -44.6198 | 2025-10-07 13:30:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 4015a134-e797-37a5-bab4-8d9317ab34cd | -14.3148 | -45.8348 | 2025-10-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 589.9 |
| 65f8eb90-a860-32da-a65a-246e94299a76 | -10.4108 | -50.2683 | 2025-10-07 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e21b2724-f2ab-32da-b273-15ea016f6124 | -12.2215 | -44.2543 | 2025-10-07 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f7507741-71ce-3c91-83d5-36f7292b9b3d | -8.4519 | -47.2509 | 2025-10-07 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 323d8bac-356e-3fff-820b-1c1718c85c33 | -10.9106 | -47.1353 | 2025-10-07 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f82a5983-ea8b-3398-b606-8343b07e61a9 | -14.7088 | -48.399 | 2025-10-07 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a4679578-3131-36a9-873a-9cfba9cc3d99 | -11.8025 | -45.1318 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a3425e9f-5c0f-3a23-95f8-d12208e991d4 | -8.854 | -46.7005 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ae97d758-f967-3291-88d2-b90db99fe427 | -8.5584 | -46.2387 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 14320bc2-8ee7-374d-ad5a-b4ff6d2f595f | -7.6932 | -46.2548 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a93c57d9-e987-3e1e-8fb7-54c9c6195ebc | -10.1573 | -45.4701 | 2025-10-07 13:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 21b5f055-98c8-37d4-8eee-0673aefea751 | -15.6202 | -52.5501 | 2025-10-07 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d1c35e80-7d12-39e2-9759-027b8bbc14cd | -9.7463 | -47.7144 | 2025-10-07 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 61c58933-d1fc-31f0-b118-ed4b20c817ea | -12.2219 | -44.2308 | 2025-10-07 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 83042fb2-3b8a-34d3-ba7d-c70c3537e27c | -8.501 | -46.3117 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2fcd00c5-aae1-3927-91e1-dc6c8b1c74b2 | -8.6519 | -46.2964 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bf8afc08-1e9d-3ecb-8081-0ba51e6fd722 | -9.1789 | -47.818 | 2025-10-07 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 6abcdc31-8ffa-3d52-b861-7ca56592ba67 | -8.1804 | -43.3445 | 2025-10-07 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 256.1 |
| 99ebcc63-c89d-3a68-97f1-5f8c5e7a230e | -15.5812 | -52.5556 | 2025-10-07 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e6fb2a0f-b50a-38bc-87a0-4e5ccfa3cc59 | -7.4666 | -43.0909 | 2025-10-07 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| d019757d-f0d3-33c6-a624-ddb9e27148c5 | -12.9101 | -54.7558 | 2025-10-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 241.6 |
| b28d7ede-ce7d-3fd2-a725-fc67fb3f7fa8 | -9.1713 | -49.9622 | 2025-10-07 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 888ca9b7-811d-3052-b15a-d6a00fd0096c | -13.7923 | -45.7859 | 2025-10-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 1cc1787e-c5e9-3079-a540-40bbe67627db | -11.7029 | -45.3536 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 464cbf68-ae4d-3ba5-9704-29c0dc41d77e | -17.9979 | -45.0011 | 2025-10-07 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a1290aec-1b87-35f8-ac21-b0971c005f84 | -9.1975 | -47.8381 | 2025-10-07 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| fb89d599-cb3a-3e84-b68a-202b47c10878 | -12.6159 | -44.7519 | 2025-10-07 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 3f8e3a37-1c0a-324d-9116-e5292b24b07f | -8.1879 | -44.2283 | 2025-10-07 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 0fc5b02e-a7a0-38ac-ac79-6a2049ad07cf | -9.1786 | -47.84 | 2025-10-07 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| b4d3b9d7-0f55-3b87-9a08-2adb195332d2 | -10.4054 | -45.3931 | 2025-10-07 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 6b3e4d49-62b0-3d7c-ab15-ca73420aff3c | -12.9106 | -54.7147 | 2025-10-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 486ee537-8b4f-3af1-a68b-34a7876a5dc3 | -14.2949 | -45.8613 | 2025-10-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| fdd59301-eecd-3bc6-844c-0447ebec60ed | -10.9113 | -47.0906 | 2025-10-07 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 04fcf0c9-5156-3e46-be92-8dcc3b76e2f4 | -15.2024 | -44.5026 | 2025-10-07 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0c46e462-25b7-30b0-982a-9617895704bc | -11.8635 | -44.938 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 2bf52c33-59cb-3fb9-9542-8d5a7a88e517 | -9.1978 | -47.8161 | 2025-10-07 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 97bf6b93-bee4-366e-9233-89a1d145d1f8 | -8.1801 | -43.3679 | 2025-10-07 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 3b6fe3c9-70bd-308b-962b-7066ca33e72d | -14.3144 | -45.8579 | 2025-10-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 320.2 |


[Clique aqui para ver as próximas entradas](README122.md)
