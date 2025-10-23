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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 854db0ba-63c0-3df8-9ccd-54cb66efc2e3 | -19.7099 | -46.07375 | 2025-10-23 04:40:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 395b44ec-210f-3e15-bb07-41329758019e | -17.61912 | -46.62833 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39983ad2-16d2-3862-9651-6eea59a985d6 | -23.72631 | -51.69699 | 2025-10-23 04:40:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5fe07d4-d9d7-3bfb-a46a-7233fcbfe0ed | -18.13729 | -44.46215 | 2025-10-23 04:40:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d3003f2-68b3-30da-8695-4232563773c4 | -18.71603 | -46.83269 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dc6894e-02e1-3673-987d-0fea385d96e5 | -17.6465 | -46.65151 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b320be0-770f-3c02-9001-acb7d8661719 | -20.97789 | -47.36209 | 2025-10-23 04:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dbbfef6-93a6-3e33-89fb-0113dbd7ad4c | -22.3978 | -49.09355 | 2025-10-23 04:40:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d077bb00-7c02-32d0-8ffd-7d90d7a7328f | -19.05341 | -49.53035 | 2025-10-23 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c2b205b-379c-39fe-ba7c-e684a8421ef7 | -19.96323 | -45.60139 | 2025-10-23 04:40:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 875e3598-cca0-3f5c-9e6e-11d195fbc760 | -15.90208 | -56.75851 | 2025-10-23 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40fc1489-cb59-30ac-acb2-de4a5d830c05 | -17.11833 | -52.02295 | 2025-10-23 04:40:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01c63559-adcd-3efc-922e-cace08d7aedd | -19.95912 | -45.60084 | 2025-10-23 04:40:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a37881a6-5764-377a-93b2-e52c22c8648f | -17.61175 | -46.59842 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae7132b9-91e9-3ad4-b552-84be6d2bc4d7 | -18.69402 | -47.05532 | 2025-10-23 04:40:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86e8494b-78d8-3c1e-9895-66f47de5ca4a | -17.60295 | -46.60671 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32538a92-c3a8-314f-8ffd-1a969b273f97 | -23.65016 | -51.69105 | 2025-10-23 04:40:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3f028fcd-4505-3043-a527-f93d68a49d89 | -18.22559 | -47.41611 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbd7bff4-724e-3dce-9517-971a76664b9f | -20.98164 | -47.36266 | 2025-10-23 04:40:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d833124b-2728-3d5b-ae55-ebdbd1f32a21 | -22.30842 | -45.90409 | 2025-10-23 04:40:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbbc7b36-74c4-3e87-9602-8d5cee2e1aa6 | -17.5552 | -51.04399 | 2025-10-23 04:40:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 327a602f-18b6-34fb-95c9-2f535b0a5bd2 | -19.26762 | -49.35801 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e947aae0-439d-3b5d-b564-dcc323dcb263 | -23.77 | -51.72452 | 2025-10-23 04:40:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9b04f7e8-fbbe-30d1-865a-2d6a8371e43f | -17.60916 | -46.61726 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c71b7acf-0e4c-3ed8-a394-8c5cb9705cdf | -19.38306 | -48.32267 | 2025-10-23 04:40:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 075eb77f-9ce8-3049-b3d0-ae646836b6b2 | -19.79413 | -50.96838 | 2025-10-23 04:40:00 | NPP-375D | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6894d350-2cd1-3c28-915b-716b751f4a09 | -17.60981 | -46.61255 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 34d8889d-c469-36fc-87a8-cc7406b294aa | -19.26819 | -49.35419 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7c9b5019-1059-3df6-9988-7052a918d173 | -17.61615 | -46.5943 | 2025-10-23 04:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01d62aa0-2cf9-318f-a9d1-bda5e6494fca | -17.61797 | -46.60892 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1513eea5-fa78-3a8f-abee-e944942da5b7 | -19.15804 | -49.13211 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd9e2e65-a069-3dc9-8c48-b7db43730f68 | -22.23637 | -56.10803 | 2025-10-23 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73efee29-058c-3d4a-a374-818379a22846 | -17.65025 | -46.65209 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4075e24d-6754-3bb5-b8d1-fcca11d2e5f0 | -23.38457 | -55.14362 | 2025-10-23 04:40:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b7307464-ae0c-3ba8-b783-1da8607ac21e | -17.61472 | -46.63244 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab73e97-e085-3600-9e12-e54dcc685a17 | -17.62613 | -46.60535 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04fd6bb5-a964-36e2-a8d7-78356151eed8 | -17.61732 | -46.61363 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9ae40db-3991-386e-8340-3aa1f1c2a9df | -21.02123 | -48.41817 | 2025-10-23 04:40:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f06d85fc-8367-3860-8a84-c0d3bd84063d | -19.48394 | -46.58084 | 2025-10-23 04:40:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5b5092c-eaa2-3fed-8a87-c843fd3aeddb | -21.56168 | -43.99139 | 2025-10-23 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80ee52d0-433b-3027-8bfd-c9d7c1eef4b4 | -18.46443 | -44.45051 | 2025-10-23 04:40:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9e8cf61-2262-312b-9735-b690399dbdc0 | -17.61239 | -46.59374 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26e44cd2-bcd7-3a6a-9853-9f8fac4f9554 | -17.61226 | -46.62253 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0be43171-4ca6-3f85-9c6d-7025d170c70d | -21.94911 | -42.9272 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cae64890-7c42-3121-bdaf-3523b3dfd891 | -23.72689 | -51.69321 | 2025-10-23 04:40:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 77285f67-9e35-3125-b12b-5233c0ada1c2 | -17.59855 | -46.61089 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45e87de9-b371-3085-84f7-3107863560ff | -17.60476 | -46.62141 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1e67e3e-9bf6-3230-a322-6329cf2051b5 | -21.95415 | -42.92755 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 35e64bc5-d686-3f62-8d4f-401811b33f7f | -18.46498 | -44.4462 | 2025-10-23 04:40:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 527cebf4-fe0a-3153-b3c5-23d5ab15c787 | -20.4923 | -45.97902 | 2025-10-23 04:40:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 378e4878-cf4b-3597-a9d7-ceab5a853cf0 | -16.54469 | -52.62197 | 2025-10-23 04:40:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8321adb8-14e3-365f-969f-068f080d656d | -18.71661 | -46.8308 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cfb8e15-1dc9-3222-9a1d-12c72b0e037a | -18.7198 | -46.83319 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8588b155-678c-3250-a24b-42e5991de53b | -19.26479 | -49.35364 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bd7fd9fd-9327-39cc-970e-a7f8a1df6fea | -17.61019 | -48.58057 | 2025-10-23 04:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3fbd105b-c241-3a8e-9e2d-60f660bc2726 | -20.23715 | -47.38879 | 2025-10-23 04:40:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d800d73c-9302-38c1-8925-6dfd1378f8b5 | -19.15405 | -49.13546 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fde21810-e070-39d3-92bc-d49308a5a533 | -21.95419 | -42.9225 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| efb94eb3-274c-3f87-8632-018ea54de70c | -18.71975 | -46.83596 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90417e5a-13ec-323f-88d0-83189399c336 | -17.60916 | -46.61727 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ecbcaa52-29be-371e-978e-236e919826e6 | -20.48828 | -45.97834 | 2025-10-23 04:40:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90954e65-7678-337f-8494-6f07c41fda22 | -17.61862 | -46.60422 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1d28efc-8e0b-3108-953c-5d3f2965495d | -20.22024 | -46.33382 | 2025-10-23 04:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c4a8936-1f04-3280-ac12-df8a8f8f5b6d | -21.84823 | -43.71313 | 2025-10-23 04:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 75113814-d191-3830-8015-331e05ec6574 | -18.71668 | -46.82807 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ed328ee-b7c2-3aed-94ac-4f759bef18ab | -17.40478 | -47.5175 | 2025-10-23 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ba04ade-9631-3fbf-bc9b-f5c5eea1ceaa | -17.61421 | -46.60837 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de31446c-0f1e-320c-a3bf-9ccc6fffad0d | -17.21147 | -47.65594 | 2025-10-23 04:40:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4625a63-cb63-33c4-838a-addd6c7e54b1 | -17.61977 | -46.62362 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df6128a6-5e1e-3348-a711-28efd33d3624 | -21.95472 | -42.92233 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b415a3b7-e62d-3a75-bdde-baf6f726fea7 | -18.721 | -46.82664 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72d847ac-4974-3810-8798-cbe5c67c8f2f | -17.608 | -46.59785 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65b5de24-41c1-3b69-8494-bc345cfefb3a | -17.21205 | -47.65183 | 2025-10-23 04:40:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40488b1d-52d5-3768-be7b-81b09a040b0c | -17.61291 | -46.61782 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5c8bc55f-31eb-3294-96be-505f6b73970e | -17.61098 | -46.63187 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60a9834f-8b2d-3a7f-a198-289c1714951c | -17.60048 | -46.59672 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11b04763-4bd9-31cb-816b-aa4de86796f0 | -19.37234 | -45.84139 | 2025-10-23 04:40:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ff15cf0-bddf-3495-a417-76aef2aaaa01 | -17.60363 | -53.84719 | 2025-10-23 04:40:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63d757b8-9dce-3885-9c6a-e029063350da | -18.18426 | -46.19547 | 2025-10-23 04:40:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f26e0b38-65cf-3ac3-b9f8-877200ca7308 | -20.57337 | -45.89285 | 2025-10-23 04:40:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b111d90-126a-3fa8-935d-0f0a0aa55579 | -18.69464 | -47.05073 | 2025-10-23 04:40:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49ea5294-5112-3248-8b21-2e4f4c675c9a | -19.48011 | -46.58015 | 2025-10-23 04:40:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eaa1842-6f68-3bfb-b2ed-d23ff43dcaf3 | -15.90208 | -56.75852 | 2025-10-23 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb40d890-d89b-3cc9-8434-b581c75b3bc6 | -18.14161 | -44.46272 | 2025-10-23 04:40:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b51efec4-c9d3-3b43-af80-b82468007c8c | -17.20792 | -47.6554 | 2025-10-23 04:40:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cf85286-380a-33e1-b1ca-20d0a95ea156 | -17.61537 | -46.62776 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72b8d77a-ed22-385d-b683-c7c223865f61 | -17.61551 | -46.59898 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f57bc486-96ed-3c61-95e6-50d68298e617 | -17.60735 | -46.60254 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef4707b2-2d6f-3415-aeb2-c10170d7bed1 | -16.87158 | -51.52575 | 2025-10-23 04:40:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fdb2d59-5a2e-326a-97a3-803ead27d389 | -20.4878 | -45.98206 | 2025-10-23 04:40:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11775014-bc2c-318f-b781-442469712a8d | -23.72356 | -51.69261 | 2025-10-23 04:40:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6990bd82-9c66-3980-8f66-6d94875a336b | -17.61046 | -46.60781 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5f93ccc-7297-3fe6-82dd-2de00b8f0506 | -18.46443 | -44.45052 | 2025-10-23 04:40:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d7529a4-5a1b-3689-afaf-2cf0b7aa79f5 | -18.2286 | -47.4211 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85d3d49-78af-30bf-9ca0-49d5042e7caf | -18.69836 | -47.05124 | 2025-10-23 04:40:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a73215b-50df-33eb-af17-c69654cae2aa | -17.6067 | -46.60726 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6397090a-7695-362e-a421-8a5414ff8203 | -20.69927 | -55.43623 | 2025-10-23 04:40:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 584af945-2d92-37d8-a4b9-b98231ec9094 | -17.8623 | -54.49736 | 2025-10-23 04:40:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3eeb0a0-f24f-36ce-a3cc-157941442561 | -17.6509 | -46.64743 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| efb6464a-1e9f-3ada-a0c2-01207fa9c6b8 | -17.59984 | -46.60143 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README27.md)
