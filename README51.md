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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c2ec889-a726-3ac2-bd7a-811d6e63b3e9 | -15.73524 | -49.44719 | 2025-08-22 05:14:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa98f0b3-dba0-33a0-a0b8-734c127afc1d | -15.15215 | -53.51185 | 2025-08-22 05:14:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46973e45-7675-3ecb-9776-8128e237732f | -19.6754 | -48.98943 | 2025-08-22 05:14:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c5a49a54-d5a9-342b-9b01-aab957791ac5 | -14.32115 | -52.01018 | 2025-08-22 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 437b35f8-1321-3e8d-9431-285369ea6527 | -14.59652 | -54.777 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f876d7-a4dd-37ad-96bb-dc2a0ceede05 | -14.76778 | -45.40772 | 2025-08-22 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 715a3f3a-2778-3d49-8add-7bf84de54de6 | -14.46656 | -56.47911 | 2025-08-22 05:14:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d16a25d-330b-3397-9b48-b3b4d23fffd7 | -14.75923 | -56.02448 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eab5bd6b-e5a6-3d68-9990-bb32a5593acd | -14.75372 | -56.03704 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2cb109d0-6a0a-3a95-8039-e2daf19fa90e | -14.83376 | -47.93222 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f0cfd18-9231-3b91-9481-8be7a4efc10b | -14.78115 | -59.66615 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f6355ea-9261-3cf5-8e31-3345f6749279 | -13.42655 | -57.17784 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76b450df-7ded-352f-9bc8-726be291e814 | -14.65298 | -54.86483 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b3f1a1b-925f-3dc8-835d-66d95c7721e0 | -15.56186 | -50.31623 | 2025-08-22 05:14:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6b63b11-ed80-3272-94e3-093e3a436a5b | -14.65081 | -54.91055 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18a92bca-7cdf-3bfe-88be-eca00a91e9be | -20.23391 | -46.61483 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f4485cf7-3c44-3381-bb0f-af2b4ed42401 | -13.43809 | -57.17097 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4877ef96-de86-3d2d-8017-446a6b5f440f | -14.75737 | -56.03761 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 019b2c00-d9c8-3cbc-b315-a91718d821ed | -13.14404 | -57.12294 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c77da3cf-2525-3600-9634-fa785e76c492 | -14.67633 | -54.86816 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ac70b95-4e6a-30dc-adc6-4fbbd2afbf70 | -16.28735 | -48.73007 | 2025-08-22 05:14:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da461539-bbed-3647-b86a-d60773c546fa | -14.91861 | -49.45511 | 2025-08-22 05:14:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa6cb927-350a-3a47-9ce5-de6c3428c506 | -20.43654 | -46.50142 | 2025-08-22 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3b778a8-827e-3e31-b037-4ca86b43af5e | -15.56142 | -50.32023 | 2025-08-22 05:14:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff84891b-0176-3e9a-bd57-99dcbad5292f | -15.03673 | -54.8345 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a0a2876-b552-3164-b5a5-569d41b251b3 | -13.43864 | -57.16716 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7b7cc9a-4fc8-3f00-956e-a67c389ae8d9 | -14.63293 | -54.83655 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 579c155a-3ef2-3ca7-865b-c8ec8e96015e | -14.62365 | -54.86879 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55f3b93a-124d-3965-af5d-dcdbb5857b47 | -15.15528 | -47.95193 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09f7e000-4f86-3b0f-b3dd-a2b92ad443d5 | -14.97743 | -54.53658 | 2025-08-22 05:14:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4278cbe2-c161-3c9a-acc9-96c0ede39431 | -14.62921 | -54.82871 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9d944b3-b58c-36a8-ad57-7253b3093dc1 | -14.88793 | -47.94968 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df7cac2b-cf2b-3cf2-a4f4-f51fcf207d8f | -18.30265 | -49.56591 | 2025-08-22 05:14:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1cabf7fc-a61a-3bd2-a794-7a409cd6056d | -14.89175 | -47.97215 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b142ede0-161d-3315-8350-3ceba2dfd09f | -14.78111 | -56.02788 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4ce3fa4-1e61-3979-86e7-c31f010c80ef | -15.73484 | -49.45093 | 2025-08-22 05:14:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60314c64-4bea-394f-86d5-b0c8fdae4805 | -20.3027 | -46.6397 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ffd12d73-d766-3e9d-9bed-cc92caf4f5f2 | -14.64774 | -54.87435 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cff54a18-dae6-3391-a24b-433e927d9349 | -14.32054 | -52.015 | 2025-08-22 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a7bc03a-7c33-3405-8873-32e638703873 | -14.64639 | -54.88441 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ffd3b6b-21cc-3a15-9d5b-1e1b3213d7c5 | -14.64975 | -54.85929 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d043d63-7740-3e41-b097-40021ac837a9 | -14.78943 | -59.65659 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0826591d-69db-3c29-ab94-678bdb0b9a13 | -14.63242 | -54.83426 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02d9fca9-43f1-30ef-94df-0561f2e1f104 | -20.35819 | -48.34591 | 2025-08-22 05:14:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1542fffc-3adc-3cb9-8107-ce66f487698c | -14.74519 | -56.04472 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6919999-2b05-3e9a-abc4-93d08c7207ed | -17.66976 | -54.05562 | 2025-08-22 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1705ac20-7716-3abc-9889-6d5971d92f20 | -14.88187 | -47.94812 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3aa9057-72bd-3c8b-8666-48135b54c119 | -14.82732 | -47.93364 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38f05c95-6eb1-3801-b764-8f688fba92cb | -14.78888 | -59.66014 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 181ee3fe-303a-3e9a-84f0-d5e2d6f34810 | -18.33176 | -49.44972 | 2025-08-22 05:14:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4632b047-3624-3db9-8365-939ff15509e2 | -14.74457 | -56.0491 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63107a53-fcdb-3d91-8f44-070f6d1caed7 | -14.99753 | -54.85874 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccafbb25-a635-3f31-94c7-9cc19edce3a5 | -14.25821 | -53.33657 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 049848c4-2862-3191-86b1-8384a503d0c0 | -14.91303 | -49.45434 | 2025-08-22 05:14:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0083d2f5-40ac-30cd-8efb-04633594dfa7 | -14.66668 | -54.85148 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f74f17a-2f43-3601-8994-29cb32c28dc4 | -14.6348 | -54.85244 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbb71927-9dad-307b-8dfd-c3d59a1254cb | -14.65602 | -56.59359 | 2025-08-22 05:14:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3dadd4b2-2201-3bbb-9df8-b06bb747fc67 | -14.63548 | -54.84727 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61481d9a-cc6f-340e-bf6a-f121b14762e9 | -14.7659 | -56.02998 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71ca9a3f-d579-32cc-bce6-5b4e3ccf0e4f | -14.76661 | -55.99877 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be5883f4-e149-3724-806a-7af2de0b8364 | -14.67379 | -54.8576 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e7dc085-5cca-3a3b-8e1e-1369ecfdbe15 | -14.74341 | -56.03099 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60a99679-d807-3e0a-b78f-c3e04c22d077 | -14.65148 | -54.90556 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 324164d9-5917-32c5-b07d-3cd51f38e185 | -18.74396 | -48.3156 | 2025-08-22 05:14:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7b1399a-f04b-31ed-a327-3da5d8b08bee | -20.30351 | -46.62933 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b3dac4b4-fb25-33f3-8f15-73daf56df77e | -18.74298 | -48.32637 | 2025-08-22 05:14:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e659e1c-b545-38d3-8ad7-e5258b784b52 | -14.65365 | -54.85981 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39a3c64f-52cc-3068-83a0-db609c96a4a7 | -14.76848 | -45.40066 | 2025-08-22 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d791f65-1ae0-3fec-b83a-74e395b7b1a4 | -14.33267 | -53.10503 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee618d59-e889-322d-8d02-d508cbab1985 | -18.54807 | -54.75048 | 2025-08-22 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b4d7eb3-4cf7-3eed-8821-05a85fc573f1 | -20.35397 | -48.345 | 2025-08-22 05:14:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbafd9f1-57d5-32d7-af7b-7edb8d77c9e6 | -14.65014 | -54.91554 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00fa7314-7462-370f-bc5a-054eb3a5b92c | -16.79059 | -47.6673 | 2025-08-22 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 604b1358-7691-38d2-814e-75113f54f106 | -14.60841 | -54.83548 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f87a8c87-5b23-314c-83c3-76c5632ceb6a | -14.59583 | -54.78202 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fff82b28-e87d-301e-b3f2-8b5ac5e42202 | -18.939 | -48.3486 | 2025-08-22 05:14:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 288e686d-682f-3172-aca9-0f1234f113b3 | -14.28151 | -60.39051 | 2025-08-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de411e75-56ea-38e7-ac82-c4000d3e7f5f | -12.58621 | -60.35316 | 2025-08-22 05:14:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33c3f0e6-c424-3b32-bcee-312ad3897c29 | -20.30311 | -46.63451 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7336285c-7ef6-36fc-b5d9-5164dbfa301c | -18.74346 | -48.32107 | 2025-08-22 05:14:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a37c84e-f3d5-30aa-aca4-ed91d6cf1092 | -14.99685 | -54.86377 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee27e30e-e64c-3d38-8bb9-1bb8405ebb72 | -19.67458 | -48.98875 | 2025-08-22 05:14:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef6de366-f339-3597-bc74-a175e1037fb6 | -14.63025 | -54.84985 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2082c29d-05fb-37cd-a911-7ee8fc1ee179 | -20.33617 | -46.57441 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 92d98f95-4e4e-3ccb-8012-d53c0c80bd02 | -20.33422 | -46.57042 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ca77bbac-211a-3ba1-86af-a3ca7fd24dd9 | -20.24148 | -46.60815 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de4b05ba-118f-351b-85cf-205c7d71a403 | -14.74155 | -56.04416 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39ce519b-cda5-3ea9-b55d-bcdae3237726 | -13.43853 | -57.16808 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5acef4ee-c7c8-3ca7-80ed-72c07ff5cd6d | -18.29686 | -49.56526 | 2025-08-22 05:14:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ced72a1b-a30b-36b5-9884-2c9c909d4f91 | -16.78517 | -47.65648 | 2025-08-22 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 85312671-8aea-3a32-947a-70384c2fa7ae | -15.73731 | -49.44997 | 2025-08-22 05:14:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20240892-1b5e-39eb-8546-675d2853dfe9 | -14.79274 | -59.65714 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 383139f2-a2d7-37d2-a14b-c424dcf2d01f | -20.30179 | -46.62703 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 90efe369-3e7b-3727-8ba0-c51459559802 | -14.78445 | -59.66669 | 2025-08-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3dca7f1-7cdf-3645-88de-83285e380c20 | -15.00788 | -54.87061 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3b13bd2-bd43-3e09-b2cb-9830962229b8 | -15.15033 | -48.11649 | 2025-08-22 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 851e83e3-474e-34fa-bb6c-4a9fae855bd1 | -20.27246 | -46.57289 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| feb3ef8d-bcda-342e-a5c4-685f9d417db0 | -15.55356 | -51.69847 | 2025-08-22 05:14:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeed041e-86c7-33e8-a052-eed219c492ce | -14.34524 | -53.12229 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a06f427-bb23-31fd-af76-507bbb24acbb | -18.27995 | -49.61861 | 2025-08-22 05:14:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
