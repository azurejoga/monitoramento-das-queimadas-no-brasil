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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66d39530-11b0-3315-8706-81d2e012477d | -15.3849 | -52.6677 | 2026-08-30 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c74a1b1e-4b9d-33fe-94d0-e0dd6c73a24d | -11.0627 | -47.1385 | 2026-08-30 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 249.1 |
| 7de917c2-3ea6-3343-9ca0-847b925ab046 | -8.1345 | -45.4923 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 47896e2f-d128-3453-b068-70de35ef159f | -10.8235 | -50.5026 | 2026-08-30 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a1035fb3-42c4-30b0-a733-41be42e840cb | -10.7457 | -50.6599 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 95f1f0d2-daec-3ad0-ba5a-1d94398767d0 | -12.9032 | -45.8382 | 2026-08-30 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 35311e49-2ab1-31ac-a3d4-09aefdfb4cb1 | -14.5627 | -52.077 | 2026-08-30 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c85d4702-bce9-35fb-83a9-7f930863bcf2 | -9.1533 | -59.5027 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| edb42ba7-1563-31a6-921b-95afeedc00ba | -14.1456 | -52.8082 | 2026-08-30 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| a0d2f596-839e-3de5-97cd-6237bdadfba7 | -8.5971 | -54.7553 | 2026-08-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4bb74cbf-ffe6-3e75-88db-b0357b733b40 | -4.1516 | -60.6878 | 2026-08-30 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7d00bb61-2543-3e76-8276-3e7da8babe43 | -10.8425 | -50.5005 | 2026-08-30 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 34bae574-62cc-340f-9d8e-28a53bccebe0 | -5.8894 | -57.7708 | 2026-08-30 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0c40477c-c7de-32de-909b-f0d2265eb891 | -15.4048 | -52.6437 | 2026-08-30 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 290.2 |
| 931958d2-5dec-3f02-848d-fd73842a997e | -13.8752 | -54.1153 | 2026-08-30 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 74d3c3f7-659a-3e2f-ae93-7ce5f2da96b9 | -11.2485 | -45.0963 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ca74eb76-3f06-356b-8f9e-56c7a01fc920 | -16.2735 | -42.5653 | 2026-08-30 14:40:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 127.3 |
| cbfb7456-24d3-3030-b13b-b3f97b07adcd | -14.4004 | -52.5438 | 2026-08-30 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9500f18c-c78b-38a8-9289-7b4a5a8cda48 | -10.8046 | -50.5046 | 2026-08-30 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 4cadb762-6efa-3818-acbd-a884ac819917 | -8.5969 | -54.7755 | 2026-08-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| a7885af5-29f6-3bb5-ae5e-d4c23644f406 | -7.3302 | -60.589 | 2026-08-30 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5ad0117a-e6ba-3a6f-809c-a39fd5bc0d08 | -5.4876 | -57.1416 | 2026-08-30 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4386785e-f21a-3c34-bb59-b669ff398505 | -8.2229 | -54.9412 | 2026-08-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| e023af03-8b1b-3dbb-ad60-fcc445a7ecf6 | -12.9221 | -45.8582 | 2026-08-30 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 5d401d9b-444c-304b-9921-c4d8a12be5c6 | -13.856 | -54.1175 | 2026-08-30 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| b66a7934-b59c-394d-9688-bee4932a9571 | -11.2128 | -53.9976 | 2026-08-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 14a30424-910f-3dc6-b512-65be5f159b72 | -13.3995 | -51.4397 | 2026-08-30 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 9a2a55c7-708c-349a-bcb3-cf3cbe33c35c | -14.1649 | -52.8058 | 2026-08-30 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 3632c803-414c-38c0-97c5-06d3c9777e8c | -9.1719 | -59.5017 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 7956f3b6-1d79-3fec-abb7-def8e9134f80 | -7.991 | -46.4954 | 2026-08-30 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 237.5 |
| b5a13637-d992-36ef-8f50-cc3447ecbe08 | -10.8253 | -45.3152 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5b5a498f-99a7-339a-b07d-7a5e863d40d9 | -15.4044 | -52.665 | 2026-08-30 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 4d464b69-74d5-3416-a785-33081bea78ce | -11.2314 | -54.0164 | 2026-08-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.5 |
| f1bdd266-ffa9-3b21-b326-31d3fe5e29c7 | -6.7698 | -55.6844 | 2026-08-30 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7376cf52-f20f-3ebd-9a0c-f40a3dbe9dd6 | -13.4379 | -51.4348 | 2026-08-30 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2b4d0d24-436f-3f23-af90-7d65334646e4 | -6.7884 | -55.6635 | 2026-08-30 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fa2b7e1c-4f76-3666-a75e-3482dcba2a68 | -10.8249 | -45.3382 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| aa7307f0-dcd3-3ec0-9818-3800c2dbf22c | -7.9611 | -44.275 | 2026-08-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 297.3 |
| 330ba5fa-d1a5-3925-ab95-f70bfbc1e08e | -11.6396 | -50.4553 | 2026-08-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c206b57d-7ab7-3937-b91b-a49f741ab099 | -9.8927 | -60.2752 | 2026-08-30 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 670e8dd5-2851-3045-9ace-0d6611572a6c | -12.3807 | -48.2099 | 2026-08-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| bf0b1fcf-cbc9-3872-b5a4-14369fa192d7 | -13.8749 | -54.1361 | 2026-08-30 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 99d6ccfc-d0fa-3110-9171-4a21eb26bec6 | -9.0722 | -60.434 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| ebb5ed76-4d56-340f-9117-c0dca331ba54 | -11.8021 | -51.0343 | 2026-08-30 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5d0f2a2b-07fb-365d-9617-05d374510280 | -11.3427 | -45.1751 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d5a26976-ee3d-3bf5-81b0-e8e75fd6ec1c | -7.3479 | -55.1544 | 2026-08-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1f917f01-5f1e-3a27-8c39-0aeaeb806701 | -3.2361 | -61.2359 | 2026-08-30 14:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fdbdd126-ce17-3613-bec4-007c41e70b39 | -11.0057 | -49.6677 | 2026-08-30 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 69e7f87f-5b5a-394c-95dc-b438080488db | -10.7867 | -45.3433 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7103aed3-bb88-31e7-89c2-2b43b5406a4c | -11.1913 | -51.292 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4cf133ab-78fd-3035-bc26-0be27c3a600a | -10.7839 | -50.6346 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 560edcb3-613b-3eb5-86cd-bfa55ca04dc9 | -13.3611 | -51.4445 | 2026-08-30 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 6294ab7b-4713-3e62-97ad-3810b0f28f46 | -9.0723 | -60.4148 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 173.4 |
| be841e65-59e1-3df4-a093-f47dddaa3ca2 | -11.0627 | -47.1385 | 2026-08-30 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9a2aba81-6fca-3815-9756-683be1d4f3d2 | -13.4187 | -51.4372 | 2026-08-30 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 182.0 |
| d45ee073-080b-3c2c-bd81-229c43eb37c1 | -14.5445 | -52.0156 | 2026-08-30 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e0c10430-e776-360b-bd99-2fb22129c8f0 | -10.844 | -45.3356 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4ac30a26-eba8-31df-a1a0-01586a20ea02 | -11.0054 | -49.6893 | 2026-08-30 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1b424819-3801-35f5-ab3a-d617151bbe5e | -11.2317 | -53.9958 | 2026-08-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 3cf7541a-6408-37c0-bf8f-15af051c8b0c | -12.3619 | -48.1903 | 2026-08-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4f070526-2fd9-3392-8965-862be26dda6c | -14.2092 | -45.3207 | 2026-08-30 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 9cdde357-839a-3e76-95ea-dd5d6e89bbbf | -7.1121 | -42.7963 | 2026-08-30 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| f01f2212-e68a-3946-8272-2414bf2f863f | -9.7832 | -46.4202 | 2026-08-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9c7255fb-7acd-3531-8c6b-e81c1879a6c0 | -11.1916 | -51.2708 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 1d412794-39bd-38e0-8b44-3cae98106cca | -7.1312 | -42.7708 | 2026-08-30 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 165.4 |
| adcc28a9-d6b7-335c-b865-c4485c904ace | -5.8708 | -57.791 | 2026-08-30 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 85389d51-a4c0-31a6-a6a9-edcf7bcfdcc9 | -15.228 | -57.6719 | 2026-08-30 14:40:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2eeddb75-a2bd-3d0b-b17d-1bc25a4f498f | -14.5634 | -52.0344 | 2026-08-30 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 0281a178-5139-31ed-a47e-12fc455dfcea | -12.9027 | -45.8612 | 2026-08-30 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 9e3c7515-1e64-3bcc-b81c-8d6943fca934 | -16.2729 | -42.59 | 2026-08-30 14:40:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 59996d7d-2612-37d0-a036-aa731865c4b6 | -6.861 | -41.6772 | 2026-08-30 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 419.6 |
| 7d58d0af-ca09-31c3-86a6-12b17af49892 | -8.1534 | -45.4904 | 2026-08-30 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 42666a34-c858-32ee-bee3-249c57dcfd9f | -11.6586 | -50.4532 | 2026-08-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 54ef371c-2b2d-31f6-a8f7-ff6165eac578 | -3.6399 | -60.5466 | 2026-08-30 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d332f5f1-6d5f-390d-8e8f-44d736ca450d | -14.7601 | -48.7467 | 2026-08-30 14:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0e72d9a8-e2c4-373b-a0c2-114ea83c1143 | -9.8928 | -60.2558 | 2026-08-30 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 28e7ac7a-f56c-3e62-9dbc-28a4c2f6678e | -14.4846 | -52.1299 | 2026-08-30 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 788d9bb6-5692-382c-9fe7-be39f6bfa2a7 | -14.4387 | -52.56 | 2026-08-30 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 5bdffd93-a1c1-382d-a42a-5f3ae9a097b5 | -3.1998 | -61.161 | 2026-08-30 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 77cbc53e-8fea-3c06-ad26-c96542b7f7f1 | -7.6963 | -61.1664 | 2026-08-30 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8c489da0-6fbe-3b77-9211-bb5046bb581a | -7.9425 | -44.2538 | 2026-08-30 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5f162ccf-28b9-3e9f-a9ec-e299bef31421 | -9.1718 | -59.5211 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 37c00eee-bb02-3c90-b8db-534b26c06e48 | -8.0098 | -46.4936 | 2026-08-30 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2e8c5e67-1800-39c8-b0ad-8f11f5b7578d | -13.3041 | -51.409 | 2026-08-30 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| aa4bd066-64c2-3d4b-a440-b8300315af92 | -9.0614 | -65.4355 | 2026-08-30 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b39e1291-c631-3e27-84a7-c0f0cfefe277 | -9.5033 | -66.1123 | 2026-08-30 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 181.0 |
| c5d8f58d-cdcf-3193-a0ab-5feefac44f37 | -9.0536 | -60.435 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 15b06840-4dac-3b1a-b60d-44b437bda733 | -3.2361 | -61.2548 | 2026-08-30 14:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 334cabfe-b46b-3447-b2f4-0dd1f1a15645 | -7.9422 | -44.277 | 2026-08-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 0bb0e1b4-60ad-3267-8107-354149db81c1 | -10.7454 | -50.6812 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| caa65c36-a59c-3ee4-8417-64e8f46f226d | -11.2107 | -45.0786 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2fc6aff2-d50a-3d69-ad76-9f7d558cf65f | -9.043 | -65.4175 | 2026-08-30 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 82adb833-0635-34eb-bf52-173d27ee8a09 | -5.9635 | -57.6899 | 2026-08-30 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 17921d5b-bc41-37e7-926a-239b04adf53b | -15.3849 | -52.6677 | 2026-08-30 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 198b2f2a-20a5-31a5-8501-49ddf0bcc327 | -7.2933 | -60.5905 | 2026-08-30 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 08ef479e-6480-398d-aa22-440a053545f7 | -3.6215 | -60.566 | 2026-08-30 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6db75d50-13f3-3054-b6ae-47c4fff30184 | -14.1459 | -52.7871 | 2026-08-30 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 7e9f6b5b-d2a6-38fd-bb47-cb1223572a67 | -11.8211 | -51.0322 | 2026-08-30 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 8bb00d51-0770-32e4-9a0e-93a8ec40b242 | -6.0 | -45.0889 | 2026-08-30 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| eaa12035-2f80-3a8b-8370-a31a22cfad0a | -7.9419 | -44.3001 | 2026-08-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 677.3 |


[Clique aqui para ver as próximas entradas](README87.md)
