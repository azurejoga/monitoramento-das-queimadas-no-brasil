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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 381927be-b2be-3f33-9633-757a1368e7d9 | -17.5139 | -46.7513 | 2025-05-20 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 49f2596b-6eb4-3b75-ad6d-f933a477856a | -20.9597 | -56.6179 | 2025-05-20 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6e4e1538-b39a-3a3a-81ac-b14ca46d0d1d | -20.9601 | -56.5967 | 2025-05-20 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 9bc08839-9886-357d-98dc-24a89fcac7ca | -12.4433 | -43.7242 | 2025-05-20 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2b23fd65-c468-3185-971d-87971dc78d5a | -19.714 | -47.6916 | 2025-05-20 00:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 35c193d7-575b-3508-bd3d-59bae6306685 | -14.0328 | -55.13 | 2025-05-20 00:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 85e978eb-ef14-3e1b-b7a7-0931772376f3 | -6.2414 | -43.3444 | 2025-05-20 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1931037f-2e17-3faf-8dea-819de5643469 | -12.2946 | -52.4785 | 2025-05-20 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8b978c3d-95fd-32a5-a932-3ffdfb3f71c8 | -17.5145 | -46.728 | 2025-05-20 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 22b0f588-f2eb-3b52-93a9-c10e55617fa6 | -12.2946 | -52.4785 | 2025-05-20 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e43ef447-4c61-3ea8-b7cc-36ff21b0da50 | -14.0328 | -55.13 | 2025-05-20 00:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6aca8945-f12a-3089-abe2-0e94e88476f0 | -7.0698 | -44.9107 | 2025-05-20 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| ece74f4e-6788-3106-9965-6c2265b151ba | -20.9393 | -56.621 | 2025-05-20 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 9244efd5-bb3b-34d5-8ce5-ffab58203b3b | -12.424 | -43.7274 | 2025-05-20 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 070327bc-37c1-3b26-a7a1-6bed7219e339 | -20.9398 | -56.5998 | 2025-05-20 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6f5d10e3-7aa5-30c5-a884-8f468962885c | -17.5145 | -46.728 | 2025-05-20 00:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 831e88b1-8ae1-309f-8ba8-97870ea4b80f | -20.9597 | -56.6179 | 2025-05-20 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5d9b782a-03cb-3e2d-9019-4ed9252e415c | -20.9601 | -56.5967 | 2025-05-20 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 136.3 |
| e8078f01-7d98-3529-ae3e-c48ab62a0e90 | -19.6937 | -47.6962 | 2025-05-20 00:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |
| e0a10872-724d-3f90-8f3d-f18a95bbbc9c | -20.9393 | -56.621 | 2025-05-20 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 54.4 |
| bda8b318-ae9f-3c35-8bc6-c2a7fcc76ef6 | -7.0695 | -44.9335 | 2025-05-20 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5e93c7bc-ccc9-3941-b72b-534c4b34f038 | -20.9398 | -56.5998 | 2025-05-20 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ecf6d59a-e017-3a09-93d8-ef5d370c9945 | -14.0328 | -55.13 | 2025-05-20 00:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 62c28259-51cf-3bd0-b350-e5194e60ba6c | -7.0698 | -44.9107 | 2025-05-20 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bdc63285-8f59-3cc9-a8c5-4bc08e0e453d | -20.9601 | -56.5967 | 2025-05-20 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 93e3ab1f-53a9-3d08-9b6c-3245b326081f | -6.2414 | -43.3444 | 2025-05-20 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 7e4f2e16-fc57-3e25-9d53-e10809a5d89b | -17.4945 | -46.7321 | 2025-05-20 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b086ee6a-ee68-3dc9-88bb-704fa3e7770f | -20.9597 | -56.6179 | 2025-05-20 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 04a66503-a2a7-376d-a0d5-ad7d6498707a | -6.2224 | -43.3693 | 2025-05-20 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 09099e17-bf5f-3dd3-b80a-8e3e835e86c7 | -6.2226 | -43.3459 | 2025-05-20 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 64a85acf-6eeb-382a-a6e1-10dbc74711eb | -12.2739 | -44.59 | 2025-05-20 00:21:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f486671-0fec-384f-a9ef-3f821d8744ff | -19.6999 | -47.715199 | 2025-05-20 00:21:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 65cec6f1-3b46-37e6-972b-950249b32875 | -17.5065 | -46.749699 | 2025-05-20 00:21:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 64eef929-4e44-3b04-8eb2-14720626c1a4 | -6.2356 | -43.357899 | 2025-05-20 00:21:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 410bff70-9138-3d0b-94f4-048a294f0379 | -7.0617 | -44.910301 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57de5bf1-567b-3c95-840c-39f382c763e0 | -17.4967 | -46.751701 | 2025-05-20 00:21:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 089fffe7-94e9-312e-9daf-59752f6459ce | -9.0329 | -47.761799 | 2025-05-20 00:21:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc63231a-8347-39f6-8f5d-f348234ca53d | -11.4142 | -44.696098 | 2025-05-20 00:21:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f672b50-ee62-3536-acd4-156954b99693 | -7.0731 | -44.915501 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce0f8152-eb25-3d65-8508-bd7fb9e05a1a | -12.2756 | -44.598 | 2025-05-20 00:21:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3b8e73-eeba-3744-a786-148f13fa0c94 | -13.3133 | -45.375801 | 2025-05-20 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b275ccbe-748c-346e-9fe8-15fa8f970962 | -11.4364 | -42.249901 | 2025-05-20 00:21:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bf4f6588-f848-37a1-a6e8-53d3d58f64d4 | -13.0256 | -45.081799 | 2025-05-20 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e78ca26-9224-336e-b377-8a5132b02913 | -11.438 | -42.256901 | 2025-05-20 00:21:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7b8d28b2-8c7a-34cb-9d6b-0afa65666b67 | -9.0427 | -47.759701 | 2025-05-20 00:21:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d10c8ba8-845b-3598-86ca-605e0f4afbbc | -13.8998 | -43.803101 | 2025-05-20 00:21:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d05d04e5-46d3-3f0d-b26c-aac9690a6a3a | -17.494301 | -46.7393 | 2025-05-20 00:21:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c60517ed-2c74-333b-af20-80b5544b851b | -10.3537 | -47.9683 | 2025-05-20 00:21:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a40d4009-f813-396b-9702-6da89af10ab6 | -17.501699 | -46.724998 | 2025-05-20 00:21:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f10479e1-8d6c-3b86-8044-770515750c9d | -11.5112 | -48.5858 | 2025-05-20 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1a349fc-788b-35d4-b276-8354ef52eafd | -7.0747 | -44.922798 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd09bff4-fad7-3dd8-92b9-e6facc676344 | -12.8363 | -47.401501 | 2025-05-20 00:21:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9be4430a-f1d0-3079-9b9c-e91d75e52298 | -13.3114 | -45.366901 | 2025-05-20 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b27ec772-1253-32d5-b4fc-0a506559ac4e | -7.0682 | -44.939499 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e223664-d9f0-3e6c-874b-e291fda88c43 | -17.504101 | -46.737301 | 2025-05-20 00:21:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95690fd6-b7f4-3139-b4d9-eac00a6cec98 | -11.2286 | -49.490799 | 2025-05-20 00:21:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d103c98-5c43-3791-b295-802df8c32c2d | -12.2773 | -44.605999 | 2025-05-20 00:21:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4395e790-91d8-3ebd-bd26-2cd532679328 | -13.0238 | -45.073299 | 2025-05-20 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab23a520-8eb9-343a-a9be-47ef77efa6d9 | -13.0336 | -45.071201 | 2025-05-20 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff82e799-17b7-3219-8392-4c07dc50ab05 | -7.0633 | -44.917599 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32cc621a-055e-3cb1-bd92-82d671c605d3 | -13.3092 | -45.404701 | 2025-05-20 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95f2113a-bdce-3a87-b507-310a3d986bd9 | -7.0666 | -44.932201 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40dd0aa3-d6c9-3ad5-ad5a-297264414fc9 | -11.4159 | -44.703999 | 2025-05-20 00:21:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ef00d0e-5af3-3a04-bfb3-362f7ab913fb | -11.2256 | -49.4758 | 2025-05-20 00:21:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 871a47a3-3134-3a69-80bb-60e87fbae97a | -7.0649 | -44.9249 | 2025-05-20 00:21:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1058aeae-6d0c-39cc-841c-b67223542e42 | -19.7069 | -47.6978 | 2025-05-20 00:21:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0d25ee86-c5fc-3f33-97ef-62895c6f4e24 | -11.5086 | -48.572701 | 2025-05-20 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bfcf56aa-6971-35bf-b56b-3127624c4cce | -19.6971 | -47.699699 | 2025-05-20 00:21:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3d45ba65-809f-3a17-966d-d6459549b81e | -10.5498 | -42.430901 | 2025-05-20 00:21:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b90dd316-80df-372f-b551-93a5f206b3de | -8.7396 | -49.743401 | 2025-05-20 00:21:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f42e355-e767-3951-9cfa-333f52020274 | -13.8981 | -43.795399 | 2025-05-20 00:21:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2602e487-8f2b-3307-b835-f2c10ca611e5 | -20.9601 | -56.5967 | 2025-05-20 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 63786a4d-1c03-3a13-b4cd-312d7f8bdb40 | -12.424 | -43.7274 | 2025-05-20 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| bca05432-344d-3415-9e55-0b41972ac724 | -20.9398 | -56.5998 | 2025-05-20 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 13527910-5245-35a3-94b3-8bf2e8bd10f8 | -20.9597 | -56.6179 | 2025-05-20 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 396bdbe7-9831-3531-a26f-01a7cc7597c8 | -12.2946 | -52.4785 | 2025-05-20 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 01097ea4-1133-3e5b-8e1c-7a0b6289dce6 | -19.714 | -47.6916 | 2025-05-20 00:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| ef4a6f5e-6b1c-323d-bc12-d9a4a9d674c7 | -12.4433 | -43.7242 | 2025-05-20 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6c45a131-6b67-3862-a9ce-9516ea39d365 | -19.6937 | -47.6962 | 2025-05-20 00:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2f1be2c6-4c70-3693-96d7-32d52b0ecb9a | -14.0328 | -55.13 | 2025-05-20 00:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e3360160-e041-3169-b0f5-d96f9ccde207 | -12.2946 | -52.4785 | 2025-05-20 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2aefbbc3-b08f-309c-ac27-33e344c3d8da | -20.9398 | -56.5998 | 2025-05-20 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1fe2d323-d95d-3de4-8180-16f2c0e2f26e | -14.0328 | -55.13 | 2025-05-20 00:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| de51bd59-4789-376f-8467-4fb4acfbdebc | -17.5145 | -46.728 | 2025-05-20 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4c8f3b30-560d-363d-8e2e-3f35f6ac6413 | -12.4433 | -43.7242 | 2025-05-20 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 25df9d88-36d4-3b12-b6bf-9052b5420963 | -20.9393 | -56.621 | 2025-05-20 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9ad7a6ed-4879-3cd4-b347-63575e6473d6 | -20.9597 | -56.6179 | 2025-05-20 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 38287967-f2e3-342c-9cbc-7ea34fbc1d78 | -5.9748 | -43.7613 | 2025-05-20 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d87b973d-3e4e-345f-bc32-6243f9d7d66c | -20.9601 | -56.5967 | 2025-05-20 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 159.9 |
| ee83b762-6389-31db-950f-af0a33884d08 | -20.9601 | -56.5967 | 2025-05-20 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 9327ed24-d1aa-314a-922f-0ec69672d178 | -12.2946 | -52.4785 | 2025-05-20 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 40f49f3c-1ee5-3d85-a8b7-dc549f3ed0f0 | -20.9597 | -56.6179 | 2025-05-20 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ee19aae5-d4e9-3171-8cd8-741288e63603 | -14.0328 | -55.13 | 2025-05-20 00:50:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 1dcbf43b-f65f-39cd-b184-f79d34019a14 | -12.424 | -43.7274 | 2025-05-20 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| aad4c46f-842c-32ce-adf8-094e4a49be9a | -20.9398 | -56.5998 | 2025-05-20 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 12993c29-a445-36e9-824a-25643948667c | -7.0695 | -44.9335 | 2025-05-20 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d1d67264-e24c-383d-983a-bc7a3277f401 | -7.0698 | -44.9107 | 2025-05-20 00:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 852b649c-101e-386e-8e31-d4322d3d6ab0 | -12.4433 | -43.7242 | 2025-05-20 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e6745fd9-59c6-3ab6-9b91-77b389b180d5 | -7.0698 | -44.9107 | 2025-05-20 01:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 7820b07a-a864-3127-aff2-7e5e5c3ec7fa | -14.0328 | -55.13 | 2025-05-20 01:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |


[Clique aqui para ver as próximas entradas](README2.md)
