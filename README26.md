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
| ecacec14-8fdc-3ce4-8ad2-d329070de0f5 | -19.66334 | -56.50702 | 2024-10-07 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d15d739a-2144-398f-b091-19e3aaa05a80 | -19.8245 | -46.82002 | 2024-10-07 01:28:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 29.1 |
| aaee7dc0-139d-3b6b-a776-edd2b5697fc9 | -16.90347 | -47.18624 | 2024-10-07 01:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 47abe2b4-cb28-3a11-9138-85f7e93ac63d | -16.90221 | -47.1534 | 2024-10-07 01:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2326ee67-484c-38a9-a0e0-c523a04b2c47 | -16.89892 | -47.16062 | 2024-10-07 01:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 33.0 |
| aa834b38-9252-3e5e-a150-40076ab59cf2 | -16.89292 | -47.1821 | 2024-10-07 01:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 760cde08-1696-39b5-afa2-b375411421e9 | -16.88816 | -47.15653 | 2024-10-07 01:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a197f3ac-2b9d-3fd8-94f0-aa6267daf96c | -16.88492 | -47.16402 | 2024-10-07 01:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e6a321d7-6327-331b-8b5a-a7a5ed7c5af4 | -17.88928 | -48.61206 | 2024-10-07 01:30:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 2b7961b9-bf94-37e6-9f54-2e89e6220528 | -16.50175 | -49.71558 | 2024-10-07 01:30:00 | TERRA_M-M | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 329e7494-dde4-31b6-95b9-ebe4beedfe2e | -16.49518 | -49.72276 | 2024-10-07 01:30:00 | TERRA_M-M | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 21ea4bd8-bcd0-37a9-9f48-576852f740b7 | -16.49235 | -49.70558 | 2024-10-07 01:30:00 | TERRA_M-M | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d0d815ed-5351-352b-81f3-e6fb881f4741 | -16.07979 | -50.21677 | 2024-10-07 01:30:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6e559301-1132-389e-8206-6bea876d9992 | -18.11281 | -50.15794 | 2024-10-07 01:30:00 | TERRA_M-M | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4188fe23-6f88-3397-a7e4-596a906214d1 | -16.31382 | -51.28522 | 2024-10-07 01:30:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a214fee5-58a5-35ba-9b87-e3ec21909581 | -16.31162 | -51.27165 | 2024-10-07 01:30:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 93f9bdef-660a-38c9-8f8e-6ea01ba34e17 | -16.30641 | -51.27898 | 2024-10-07 01:30:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7475404c-8e8e-3189-9ccc-443cb2e8283f | -16.18663 | -50.93703 | 2024-10-07 01:30:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5925cfe2-f749-3013-bb97-5971f93a8417 | -16.17587 | -50.93877 | 2024-10-07 01:30:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ddd4deb1-bb9c-3d6e-9522-97c516594778 | -16.05956 | -50.44405 | 2024-10-07 01:30:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4f833483-4fd3-302a-8cd2-fb2d398a7d8b | -17.13166 | -51.71096 | 2024-10-07 01:30:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 704290d4-8bf8-340b-8c54-a48f582499f7 | -17.77259 | -53.10099 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 38ef0262-5a2a-3fa7-b3a5-d922475be888 | -17.7711 | -53.09092 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f722bc28-12d6-3c35-ac52-59eb7de9e857 | -17.66975 | -53.09352 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f433ad79-de1e-3ae9-b3e5-7db8ca5e2fed | -17.66824 | -53.0834 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 84176b19-4c37-3fe0-a5f8-86489e4778e3 | -17.66374 | -53.05307 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 347e4f34-8cba-3fc7-8089-29d61dbd6f7c | -17.66222 | -53.04285 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3b9c00e1-5864-3efb-9ba3-7fb570f75520 | -17.66051 | -53.095 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8ab5b7e6-ee14-3479-a315-c18ac155df1b | -17.65902 | -53.08496 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 54395e81-4c6e-3304-8236-2be8d68292be | -17.6545 | -53.05464 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 87106e3f-099b-33b3-ad02-ef78b43e5273 | -17.6513 | -53.09661 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4667d9d3-bdde-37bb-86e8-b231268894b9 | -17.6498 | -53.08652 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| eb16c591-5f41-3772-b479-520ca003d37e | -17.64527 | -53.05622 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0ce3778b-80f8-3706-9d6a-689217f11aba | -17.63438 | -53.10981 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 297acdd4-df0c-3203-b9bc-75e3b8d0fcd5 | -17.63287 | -53.09976 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f8eadc23-f965-3fab-ab30-2a16b062091c | -17.63136 | -53.0897 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| de31d0fc-5b2a-3808-93e3-c258d9039361 | -17.62668 | -53.12145 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 875d2410-e805-31d4-ab51-7f10a118352e | -17.62516 | -53.11133 | 2024-10-07 01:30:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 530.8 |
| 2e132ddc-d806-3b60-b355-1c19882cde7a | -17.62363 | -53.10123 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 80d6bb7c-f585-3b38-a0f2-29ad10b87d9c | -17.61595 | -53.11294 | 2024-10-07 01:30:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cceb7cb6-4588-3031-b10e-110bf9ec505c | -17.83697 | -53.79266 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| d17fc92f-27cb-3be8-9576-df191f798c03 | -17.8356 | -53.78331 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 01277456-b37c-3552-85ab-5b634a5a2fc4 | -17.79821 | -53.77953 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c1976444-b38b-3135-8713-41da5cf5154a | -17.78857 | -53.77767 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 879aef74-5fec-3927-ba6f-1ae80eb669c1 | -17.78718 | -53.76809 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8416e2b6-85ae-3eb2-addf-1e23b5cdacfe | -17.78579 | -53.75845 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 13b57d06-1828-3952-a2f3-3dc7dc0dd661 | -17.77956 | -53.77902 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 3e9e1dc5-b6de-3638-a4d0-7c48c78fb12c | -17.77817 | -53.76943 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cf34ee08-b31b-3222-b6c3-06b23c89a3dc | -17.77678 | -53.75988 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ac44e834-6c5e-3115-ae73-e254c3dac6c8 | -18.46995 | -53.51816 | 2024-10-07 01:30:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 56fe54bf-2214-31b3-9736-03923ebd4ee4 | -18.46855 | -53.5086 | 2024-10-07 01:30:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 10b8d2cd-68ba-3c45-a3b9-79a30a48518a | -18.46714 | -53.49895 | 2024-10-07 01:30:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 795da583-e2ad-3959-99bc-8a4a63644344 | -18.46091 | -53.51954 | 2024-10-07 01:30:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 52.4 |
| d3aea44c-d749-3a7f-9cf8-35a49d7b8e21 | -18.4595 | -53.50991 | 2024-10-07 01:30:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| cd2583d7-2b4c-3bde-8f40-e2a7779aadda | -18.45809 | -53.50031 | 2024-10-07 01:30:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 15c9bfe9-80f2-3d8b-97da-fb1b02aaeb89 | -16.49591 | -53.95417 | 2024-10-07 01:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 24ca52b0-5f48-3edb-b221-f4f78ed045e5 | -16.48829 | -53.96529 | 2024-10-07 01:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0c9fccad-071a-3306-8ed4-946aaa45747d | -16.48689 | -53.95569 | 2024-10-07 01:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4a4ca3e8-4617-327e-996b-256ffd548a9a | -16.47023 | -53.96815 | 2024-10-07 01:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ddc95717-ff92-3d28-a5ff-38180023c685 | -16.46121 | -53.96964 | 2024-10-07 01:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 247c2676-5b16-3a61-a00d-d21e52ed7cb2 | -16.45981 | -53.96011 | 2024-10-07 01:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8422f30d-caef-3f65-9cd1-4f3ab6a4cd33 | -18.10064 | -54.27926 | 2024-10-07 01:30:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b704827-992f-334a-817d-a88f212da56c | -17.82797 | -53.79411 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 541e36ba-d490-3c72-8e37-2289afa1eb6e | -17.80099 | -53.79843 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1211636b-bebe-3e48-8473-3e93618b82ec | -17.79958 | -53.78888 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f3e1aa31-b495-3e2b-a59a-4be98ec0becb | -17.79405 | -53.81552 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 046b079f-6e9e-3d83-96bc-8a6d599cf48d | -17.79268 | -53.80598 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5267eb86-4306-3154-b508-2aaadecde43c | -17.79131 | -53.79656 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d83dec6d-3a01-316a-9d48-603de5c0811a | -17.78994 | -53.78713 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 05adf7d3-de83-3cca-a4ba-d453c1d6a769 | -17.78369 | -53.80749 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| bf66cc3f-23f9-38e1-bdc0-bf1fcba60a8e | -17.78231 | -53.79803 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| cfb6ef73-8280-3543-b27a-353a593e6073 | -17.78095 | -53.78862 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| be5c8d38-b11f-3623-9499-54b0dfff1258 | -17.77469 | -53.80891 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d9a094d5-6873-3b9b-9943-7b891f8526fb | -17.77331 | -53.79943 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2e11fc20-c49f-38b1-a12b-d8ef52c84e76 | -17.77193 | -53.78992 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1a3e4633-c9b0-3e89-ad56-612d45b595a6 | -17.77055 | -53.78038 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bedecddc-c40b-33c0-8488-a2b928b224e3 | -17.32316 | -55.04107 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 9477f09f-00a2-30a8-b57e-5aa7f8f316b5 | -17.30803 | -55.06226 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 19fcae23-93ab-37e3-90a3-30dd44137ea1 | -17.18278 | -53.92231 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f03fac4c-a8e7-3f5b-8668-de3c2d5f50f5 | -17.17517 | -53.93324 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4b95d662-8ef1-3e05-8520-c54d0d309227 | -17.17377 | -53.92371 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 170.6 |
| b47faf15-a798-30ff-8f67-d5f676124ee9 | -17.16693 | -53.9404 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 906e6f77-8e9a-35b0-bd73-9a5306f527d8 | -17.16555 | -53.93088 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| cff3e837-f8ef-359c-812d-f08373011ac2 | -17.16418 | -53.92134 | 2024-10-07 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f7859db4-ec9b-31a8-afb1-00443e765d1b | -17.15656 | -53.93229 | 2024-10-07 01:30:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 44f02b6f-6100-3cae-98bf-4e4990c82ed8 | -17.02475 | -55.07753 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 0d3edd86-f804-3ef4-a82b-665e78ba831a | -17.02346 | -55.06831 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 1569f708-243e-3044-a364-0529884e7bfc | -17.02217 | -55.0591 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8a6b4196-b5dc-37ee-be69-8852a163f862 | -17.01847 | -55.09732 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 32a8c7e3-d4f5-3fd3-878d-88f86f500437 | -17.01719 | -55.0881 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a71bcd91-152c-3cfd-b3b1-a8d62c4ad794 | -17.01332 | -55.06047 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 32448947-c2c1-37cc-a26e-d599878d36b3 | -17.01203 | -55.05126 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1770903b-0eaf-3c0e-9693-156dbcb2ef5d | -17.00962 | -55.09869 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 9820690a-a093-3c52-9164-fa3372bdc1e1 | -17.00945 | -55.03284 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| df021ab6-c276-39a3-a96d-c93018386dc3 | -17.0006 | -55.03421 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e84b02ad-3578-3867-8d25-3ae7000a0b61 | -16.91492 | -54.55664 | 2024-10-07 01:30:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4c25449-7595-3620-bcfc-910c97a2a2df | -16.90736 | -54.56734 | 2024-10-07 01:30:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 11f310d9-40c5-372e-9a6c-6ef205e43a8a | -16.90603 | -54.55803 | 2024-10-07 01:30:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fbaa00d5-1e23-3750-afee-d278b8337401 | -16.88261 | -54.52956 | 2024-10-07 01:30:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a2d169c1-700f-358f-92ee-4b4e5f25d99d | -18.90196 | -54.5415 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README27.md)
