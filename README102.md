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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e7ebc06-6361-3e77-ab49-d9cf6ab63b22 | -8.74003 | -52.36578 | 2026-09-22 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a5c42bc-8b4d-3977-a298-dfe370ca4fc4 | -11.10284 | -48.31228 | 2026-09-22 05:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a321e01a-54ea-37f9-a975-8691390225ab | -9.67868 | -54.34608 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bfd40df-a54b-300b-8cfa-37fd28907379 | -10.71818 | -54.00873 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65f16aaf-2da5-3b7b-aae9-bc1db577bcf3 | -18.52032 | -50.33786 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| ca381cd7-284e-39d3-b2ed-b41b30aff022 | -16.04811 | -49.98431 | 2026-09-22 05:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d825c40d-148a-336c-b585-206990d615b3 | -21.45841 | -48.68078 | 2026-09-22 05:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec161ae2-0c36-3789-b5f4-c715d4ccf1dc | -8.48581 | -57.61584 | 2026-09-22 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09fc9c7e-26d0-3f2a-9a0e-b9a35d3fce86 | -11.42543 | -47.35386 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fd6b982-6cf7-3f47-aef3-f3ca2a2e01de | -8.62446 | -54.6288 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f8622cb-41d6-32b1-a703-ed11043f614a | -7.50885 | -61.37793 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 797e03ca-2415-3d22-becd-9bea0fb36b9b | -10.59558 | -53.97414 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 86659e8a-b5b0-3109-a5b9-e26b33e7cfd9 | -18.51402 | -50.34463 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| db006076-7293-3648-a2a6-1f2e9d1edfd2 | -10.60446 | -54.00196 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25ef4be-bc3e-3b63-b3ba-15ac8248044d | -9.67251 | -54.33605 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08aa8d12-f841-3aa0-adca-d49410060fc1 | -21.46131 | -48.68072 | 2026-09-22 05:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b2ba9aa3-2dd1-3701-bc2f-8fab5f8932ad | -10.60505 | -53.99044 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 31262e3f-6be3-3757-80b8-cfd8c0a6cdd8 | -11.15418 | -51.10408 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 602c2781-0fa6-38dc-a004-45703acd6703 | -8.26251 | -55.28683 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb05276a-9c48-3fcb-872b-b60dc681183d | -9.02716 | -60.36336 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5c255f-34d3-352f-8d9c-d69f062b7eba | -9.20618 | -60.2879 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 38738058-c54c-300c-bc89-86858e6ce3aa | -8.60134 | -54.63392 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d5e9531-5aeb-3296-8ccc-aa51ea0e7803 | -8.6178 | -54.62348 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 330367b7-f39c-391a-9ad7-b9a38a0ee1c6 | -10.75854 | -50.73013 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaf8f289-4568-3130-96aa-d00a5d92f1d1 | -9.7245 | -47.76406 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d131d830-5030-317e-8eae-ba4171fa7afb | -9.67898 | -54.31837 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3240aa62-8610-370e-a982-3a9e80e4784b | -8.48914 | -57.61637 | 2026-09-22 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 197e3081-495c-30f7-b30f-8d6818dbb06e | -8.2462 | -55.25228 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0faed0f8-4dde-3fcb-b4bb-004cdc4ae2c8 | -16.04853 | -49.98072 | 2026-09-22 05:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 335e712c-6f69-3eee-829e-09995de952cd | -9.68136 | -54.32815 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16fd12ea-bd8f-328e-9fc0-385401f051cd | -9.29777 | -58.9158 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cca78372-60af-3437-8fd0-994040aa4f65 | -9.29889 | -60.5313 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a7da7c5-1e4e-3ab8-82bb-42fdb3e9b38e | -8.6021 | -54.60367 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8fe0281-5bf5-374a-bb46-5baab5f267e7 | -8.62271 | -54.61554 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe9ebb2-1b67-3c0b-aab7-6f4c4289c3c8 | -9.30447 | -58.9169 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 048bdf95-6b80-32b6-ba1e-624fc5c64755 | -8.60498 | -54.63448 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0d140ed-14ad-3f47-b2dc-d509296b4ddc | -11.39648 | -46.77002 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18871a1a-daf1-358c-bbca-7890cffd0263 | -16.99497 | -56.44915 | 2026-09-22 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ece9c433-02bd-3a7a-9451-faa99ec199b4 | -15.44147 | -48.46025 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fabcbde7-7b30-38b8-b69c-c39542cb0d25 | -8.62811 | -54.62933 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d2de669-d2a2-3637-8c83-979709a08416 | -9.13169 | -58.88894 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e54b43e1-c1db-3c04-8036-e467d12758fa | -10.59904 | -54.00441 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc96e15-3356-369b-b2a7-c176961518e5 | -9.84688 | -48.31908 | 2026-09-22 05:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07c134b7-7ce7-3ebc-9292-1a10fd02b067 | -9.30504 | -58.91335 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82797f29-0b04-3bff-a1e4-aab55b772bbb | -10.60261 | -53.98019 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8f79c1e4-bafa-3658-ab41-05464b589dda | -9.11012 | -60.94672 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c1e431a-d76a-3557-bd64-9c8e4df98249 | -8.26286 | -55.28579 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d81c4cd7-7644-3a3b-9617-6fdc47604544 | -9.28878 | -60.63537 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 467811d2-d09d-3d6b-9146-18bad5f9ef38 | -11.5454 | -45.36823 | 2026-09-22 05:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a1f315d-e1ea-36d3-aa1e-96e94ae88ba4 | -18.52155 | -50.32642 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e5ac5648-5a27-3ce5-8d83-bf2444d36198 | -10.68445 | -48.71334 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef7c48af-dfa7-3ec1-94b7-abf2f1ec1607 | -10.84707 | -50.15296 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff98df9d-b5d0-39b2-b480-a4ad7774b06c | -10.60893 | -53.99101 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c1e46a65-0b2e-386a-b0a3-f66511228f96 | -10.71359 | -54.01301 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f154ec13-6f99-3803-9d91-edcfe753b9ad | -18.51362 | -50.3484 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d93e375e-1a88-3a25-a650-351550f4a5ed | -10.8428 | -50.14644 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4442f6fa-c0f9-307f-adb6-96b88346e31f | -9.88402 | -48.4671 | 2026-09-22 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e11724e-13ca-316c-b58a-2ea0e946026c | -7.69853 | -61.53632 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ae83748-0895-35d4-9c16-bbe52301da9e | -10.41922 | -53.79049 | 2026-09-22 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01ccbca-4a71-35c8-a56e-aa3c0b9109e3 | -8.63112 | -54.6341 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37e78481-f225-3475-8042-74a8e6a5d669 | -9.72396 | -47.76823 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2b33cc7-b3b3-3f70-9c33-92954d3d0876 | -10.45538 | -51.33422 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af7fc27c-423d-315b-b6dc-595b28df6e9e | -11.14945 | -51.10342 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e0d998c-3140-39ec-bb0a-907ab17880b0 | -18.51949 | -50.3455 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 0801c3a6-4bc9-3bbd-b390-6f5bb1303ce9 | -11.16768 | -51.11111 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3e375cb-01ec-3036-b785-7473cd79262d | -11.39929 | -46.80018 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94bf5799-74a1-327d-b954-78f9c8e07e58 | -7.51162 | -61.38057 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b42885-ba0f-32da-bc7a-2a301823d20e | -8.62937 | -54.62089 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01e4c3c1-4bc7-3d52-8ed7-e14d7146fda4 | -11.16701 | -51.11616 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d22de8ac-4fb3-3ef8-8ef6-b29df123c10f | -9.59312 | -47.78096 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56aca57d-494a-379d-9092-88c0b4c9290d | -7.69398 | -61.54026 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3311a122-3fea-363e-9d53-e1bf710ed224 | -9.68579 | -54.32418 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bedc1a5-f73e-3e21-b261-493257aebb8a | -8.5977 | -54.63335 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3d10e4a-da42-3895-adb2-295ba2701fad | -10.45414 | -51.276 | 2026-09-22 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9593e94-14f1-395a-87d7-86a1b8c363bd | -8.59895 | -54.6249 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09063b13-9482-3c90-b6a3-94ac1d487c13 | -15.60368 | -48.32688 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da7a22fa-67eb-3579-bc77-f16287a33339 | -11.16229 | -51.1155 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a90896b5-70d1-3c34-a788-39d333861dcb | -9.29823 | -60.53524 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbc6f1ae-7fbc-3b9c-a053-0be65a505135 | -18.03731 | -50.9262 | 2026-09-22 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7bbc1deb-1181-3ea7-8ced-80d5c3645dcd | -9.67934 | -54.34167 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b952f9df-5a9f-34a9-957e-cca7015e02d2 | -3.35869 | -50.76963 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c89ce2f9-4698-35cb-8979-e333a8416741 | -1.06587 | -57.34449 | 2026-09-22 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15647dd8-bbe8-302f-b974-8462385bbb8d | -3.44653 | -50.61969 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51af745d-6519-35ca-b20f-33baec8379ae | -2.9125 | -54.19102 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 082be023-357c-3545-aa3a-00fe21658bc7 | -3.39005 | -50.44176 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e7f47b4-c637-378f-9cf0-dd17a7bc2a84 | 3.67933 | -61.86695 | 2026-09-22 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 235f05c9-0b59-30c4-964f-a3157bfbbeac | -3.45403 | -50.61514 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac0c5da0-51f5-3a6a-ab38-15ad9c3fe738 | 2.77948 | -60.75838 | 2026-09-22 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 031993b4-f357-3faf-b67f-4c3b54f76c32 | -1.93775 | -56.59711 | 2026-09-22 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce2b2525-5c79-3ec1-a945-2952eda6d4c7 | 2.31904 | -60.92048 | 2026-09-22 05:40:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5648a3c6-ba09-3773-a90b-9b7bf25ee2a8 | -1.45313 | -54.24416 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7743c3e8-2439-3983-b4d3-8ec3137b61f1 | 4.31535 | -60.58476 | 2026-09-22 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19947320-23c8-3cb3-a93d-e94e44f0afd3 | -2.27598 | -57.99475 | 2026-09-22 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be857469-bd3b-34ae-93da-b4338718a367 | -1.33492 | -54.66547 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dbbf5a20-b11b-3a7c-a3d1-f8536374f3cb | 4.71163 | -60.87453 | 2026-09-22 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 996ca159-e7e1-300e-aa0f-4a52e802cf92 | -3.37858 | -50.40793 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 505074dc-7e5f-3710-a2a2-bd0e58616ca7 | -1.45558 | -54.24234 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4f7e8a6-4202-345b-b96b-18307dd8611e | -3.3653 | -50.77058 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6498e5cc-49a8-3e9e-ba33-016c96d41576 | -1.94273 | -56.59519 | 2026-09-22 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c961115d-08d8-3dd8-b3fc-380cd1bf4416 | -2.41439 | -57.90382 | 2026-09-22 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README103.md)
