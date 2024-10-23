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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2e69b5c-27df-36eb-a773-54d3f2551cd1 | -18.30963 | -56.22114 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 42acdc97-de3e-3675-afa1-fce3d9b493f1 | -18.30696 | -56.20916 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c9f96b78-0d00-3759-8ed8-70b15c780c10 | -18.30648 | -56.21297 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ee6edde6-ac77-37ee-86a9-9dba00530ea7 | -18.30601 | -56.21676 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 99d5fe25-b2fe-34cc-87b9-e4254240de2d | -18.30438 | -56.21004 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 16264a5b-f1b6-3d4e-ba30-bd1ff2abc933 | -18.30388 | -56.21384 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dd8f1b99-8e95-30a4-b409-d67646563779 | -18.30361 | -56.12049 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 05034f75-fffd-3c7c-bc3d-f16725956838 | -18.30238 | -56.21238 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ad61b1a5-e1b4-3082-a59c-a95867204a68 | -18.29949 | -56.11991 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 51b07a6c-e9a1-373e-827d-e4a53d27edbe | -18.27393 | -56.05738 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5f607caa-53a5-3ffe-9239-db7028171dbd | -18.27343 | -56.06126 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f5cb3514-f909-348e-a6eb-5189c4be1b36 | -18.27294 | -56.06512 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7ebc6580-b1cd-3021-aec3-119e48d170a2 | -18.27195 | -56.07286 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f80575d-4183-35a5-abf5-4e942ed0ba8d | -18.26979 | -56.0568 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f23d4c71-fb25-3af0-a2ec-29015021a6b1 | -18.2693 | -56.06067 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e1a7ee36-37fc-3c9f-b0ff-63f1ecfc64d4 | -18.2688 | -56.06454 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c26ffe0c-40f2-34ae-a40f-d5fa064ac460 | -18.2683 | -56.06841 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1ff0e840-f14d-3236-9a00-730aeaf59d5e | -18.26781 | -56.07228 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7a5d7473-2ebf-32ae-9e57-e662c8a84d27 | -18.26682 | -56.08 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 99dbe3a8-c138-3839-aa73-b4e22902d0c0 | -18.26516 | -56.06009 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2eda6134-f35a-345e-928a-93cb96fc3b55 | -18.26467 | -56.06396 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d358a06a-abfe-3ac4-84d6-4ae26251537e | -18.26417 | -56.06783 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f5361ee2-8f28-3fe8-b4ce-50d1fb2b7f1f | -18.26368 | -56.07169 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5fb7e070-5efe-32fd-ada0-3d5c16c9c6e1 | -18.26318 | -56.07556 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fd7cd3d3-5958-3111-903b-76956b834903 | -18.26269 | -56.07941 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 34955051-a263-3ed3-8fc3-5ec9d2dbd9b6 | -18.26102 | -56.05951 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9647eaae-804f-3e5e-9f97-0789e02b5e9b | -18.26053 | -56.06337 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 27f6d2b9-1556-3014-92d3-0256f5672eb8 | -18.26003 | -56.06724 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8e3100e-c82c-312f-9864-56efeb751c16 | -18.25954 | -56.07111 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 720f3a62-3e33-38d1-a6be-705f4abd3310 | -18.25905 | -56.07497 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a138af90-c0f2-3a71-a945-9c6f3bc67c12 | -18.25639 | -56.06279 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 520a7d8f-670b-3226-b399-629aa86acb75 | -18.2559 | -56.06666 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 190d1b2b-b6b1-3607-a67e-d4da9f957101 | -18.25492 | -56.07438 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 181ed20f-6335-3622-9855-b545ff6a8e39 | -19.63405 | -56.79721 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9cb483d4-55c5-37e4-befd-9fc7dbba72ae | -19.63335 | -56.80273 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 05129052-6f94-3d17-991b-252c0528ab0b | -19.63266 | -56.80823 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6542dd77-fc8c-33ae-8f42-70e6cf469f18 | -19.63153 | -56.77874 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 036694e1-eed1-3157-aecb-9846137e6fde | -19.63081 | -56.78426 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 621cd637-3394-315b-aaf0-7e870046fb99 | -19.63071 | -56.79112 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a40b7cf6-7ef6-340e-a94e-dbb15ae36301 | -19.63027 | -56.76197 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 41e32dcc-dd47-3d0d-a861-ece010200764 | -19.63008 | -56.78977 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 640a367c-f202-3bee-92f6-8b0fa9fa0582 | -19.63002 | -56.79663 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| cfb9b81f-ef6d-3b6e-8c8a-46a1f786017e | -19.6298 | -56.76566 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9c8cd85c-0a2d-3801-b5be-d71f79beae28 | -19.62935 | -56.79527 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e6df91b0-90ff-3ec7-bc81-cd528e8480e0 | -19.62934 | -56.76935 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 15ef2b1c-010e-3c2b-8081-514b00dfc47a | -19.62933 | -56.80214 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 80b72ac5-0efc-34fc-b752-079df84fd716 | -19.62888 | -56.77304 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8a6b3311-c503-3cdd-9afa-1823c8723e5d | -19.62864 | -56.80765 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 70ba331d-0c6b-3f9b-b742-21994a7d652e | -19.62862 | -56.80078 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 7861fc2d-636a-3cab-bc2e-075443de91c9 | -19.62842 | -56.77673 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| ce85a66e-a2b3-3c56-af56-d969781fbdaf | -19.62796 | -56.78041 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 20036b28-ac3b-3ea7-ab80-16031b9ba643 | -19.62795 | -56.81316 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 569e00d7-dd13-380c-badb-eb831e912199 | -19.62789 | -56.80627 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| a5e46dbd-2e9b-3912-b7d8-4e3a6daaaddb | -19.62751 | -56.77817 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 85f9011b-b681-3ddb-b751-0acb604eaf88 | -19.62738 | -56.78502 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| fb42dc16-666d-3f95-9d97-525b68db75b7 | -19.62716 | -56.81177 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 2471b14f-9988-3312-bd8b-d3e5c4800bc1 | -19.62678 | -56.78369 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 143fd625-6fde-3d4a-a519-b2f166b6820d | -19.62669 | -56.79053 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6286888d-a9b2-3c4a-8599-21505264e0f3 | -19.62605 | -56.7892 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 384850ea-c590-327a-98aa-300b0abd6a5c | -19.626 | -56.79605 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| cec303dc-77f3-3112-9680-85c2b77ecb19 | -19.62532 | -56.7947 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a0317454-a204-3711-ae7b-79c2f22a68cf | -19.62531 | -56.80156 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 3761e193-951f-37cd-8c70-8a77dcd90e2d | -19.62462 | -56.80707 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 40d04d83-eb33-369c-b090-8b4a7ca55139 | -19.6246 | -56.8002 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| eeeec2a9-f762-3d26-ae17-47217b689006 | -19.62439 | -56.77615 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| d185d3f1-3373-3e1c-bde1-490123988752 | -19.62393 | -56.81257 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 913a6f17-02c2-306a-96fc-2e7437cb05aa | -19.62393 | -56.77984 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| d43eb26d-62db-339f-8e82-ea8cb2351e5c | -19.62387 | -56.8057 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 89332639-a553-3311-a777-1b640e620bdc | -19.62348 | -56.7776 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 6b170989-041a-3296-b4b2-b07107fb102e | -19.62315 | -56.81118 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| eae3691c-fc0b-3d46-80d7-9e486f045775 | -19.62197 | -56.79547 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d9e3250b-94e5-3930-aec1-5cc0c0d3608f | -19.6213 | -56.79412 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 88be5cc4-ef84-3772-ac08-7e5d0a2931da | -19.62128 | -56.80098 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 798595ce-941b-3a2b-aab3-4f9adc53d1f9 | -19.62057 | -56.79963 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 220f1037-599b-367d-896e-dcf1aba8bb02 | -19.56227 | -56.6127 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8ec4c7f7-e3c5-3d0f-86ef-b655df55c4b1 | -19.56179 | -56.61645 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a0e244c8-ef0a-3e92-a717-d758ce6fe149 | -19.5582 | -56.61211 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ac9c9df9-77a3-32f2-8181-e6536e2b19ce | -19.55773 | -56.61587 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1329ce1f-6757-3851-b393-ceb4e0b72cb3 | -19.55726 | -56.61963 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d651feef-9c8c-3a46-96ac-cb55edd7769c | -19.55567 | -56.66512 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1700bb8f-f51b-3325-b8a8-98ab442bb863 | -19.5552 | -56.66884 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e79d270a-e5db-3229-8d54-3a706a90dad8 | -19.55473 | -56.67257 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 81314698-a296-389b-8195-671cdd95dc89 | -19.55426 | -56.6763 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 20ac33f6-b355-3e6f-a7c4-ccdebb4c5439 | -19.55379 | -56.68002 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c10c30f6-af8c-3c21-a64a-4b4a584b94c7 | -19.55366 | -56.61529 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e571522c-dde2-3b36-a9db-076b987b481b | -19.55332 | -56.68374 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 03dd7740-7461-31cb-8897-186e44904c3e | -19.55319 | -56.61904 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0d13637c-3ee4-30ec-a27c-7b0e4df075b2 | -19.55209 | -56.6608 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1dd2085e-1785-39c8-b1fb-9ac54daeb3a8 | -19.55162 | -56.66453 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 14ae0309-2193-3e9b-81da-b44bcb29d5fb | -19.55115 | -56.66826 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2226576b-9ad7-38f0-9cc0-1c67ecf10782 | -19.55068 | -56.67199 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dca97f6b-b338-3740-a18f-cae0a58cbc1c | -19.55054 | -56.60719 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 05b0f954-dc30-3026-810c-d4e7e49c3ff1 | -19.55021 | -56.67571 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f763916d-a224-3021-aaa3-0986e01f143c | -19.55007 | -56.61095 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c4e5dcc3-23e9-39f8-aa06-57f9107503fe | -19.54975 | -56.67943 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 53c1601f-5747-3c83-85c4-274ea255b2c0 | -19.5496 | -56.6147 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b8b069c6-5b0a-3ec1-930c-522e7a16da8a | -19.54928 | -56.68315 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 354c654f-73b0-3d00-a6d3-d9758fd3c2c7 | -19.5485 | -56.65648 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c55bc5c6-4fa5-33a5-ac58-4dcff031b4a2 | -19.54803 | -56.66021 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9e741944-7337-364b-9dfa-8aa0d5dcbad0 | -19.54757 | -56.66394 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |


[Clique aqui para ver as próximas entradas](README58.md)
