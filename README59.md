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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e9e49e4-ec50-3099-a7ef-5198d68d5278 | -21.36774 | -48.48109 | 2024-09-30 05:08:00 | AQUA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6a2488e2-113c-3a85-835c-7780bc1d15a6 | -21.36594 | -48.49206 | 2024-09-30 05:08:00 | AQUA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fb6288e4-f628-343d-85a7-e752afff0b97 | -21.36413 | -48.50303 | 2024-09-30 05:08:00 | AQUA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5187dc18-9c70-35d7-a11a-307029ac38db | -20.63643 | -48.74977 | 2024-09-30 05:08:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 472a326e-60c9-34f8-96c9-83067dbc521a | -20.59633 | -46.23374 | 2024-09-30 05:08:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5d6bc32d-375d-3974-9161-183cc623e907 | -20.5949 | -46.24313 | 2024-09-30 05:08:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d27a4a5-3a3a-3599-b42c-5e4aec140165 | -20.3198 | -46.65174 | 2024-09-30 05:08:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c6612d6-4b2d-36c0-b409-737f9fff719f | -20.31826 | -46.66158 | 2024-09-30 05:08:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 41d4883e-d9ed-39d8-9c8a-ea89baa90585 | -20.30894 | -46.66288 | 2024-09-30 05:08:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 88f9756e-f0ab-3c75-ba18-e460c1978b37 | -19.88863 | -43.15956 | 2024-09-30 05:08:00 | AQUA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 33858c5f-8ab2-3dd9-8e44-280972988f73 | -19.88709 | -43.17075 | 2024-09-30 05:08:00 | AQUA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 50c58148-7fb1-3041-890d-ea7d7be58ae9 | -19.87761 | -43.16926 | 2024-09-30 05:08:00 | AQUA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 6caea9e3-bdf7-3ac4-90e7-46008b317011 | -19.84197 | -42.75063 | 2024-09-30 05:08:00 | AQUA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 5ab86a00-9d09-39d2-a415-28ca9303a732 | -19.44281 | -45.87248 | 2024-09-30 05:08:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0385cb23-a910-3b26-a294-738c40ae6ce2 | -19.43395 | -45.87098 | 2024-09-30 05:08:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0c3f811-3c34-30ec-a72d-beaa9865662e | -19.43252 | -45.88036 | 2024-09-30 05:08:00 | AQUA_M-M | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b9e81e07-2c78-3201-8b1d-8fed0163e760 | -19.35673 | -48.8955 | 2024-09-30 05:08:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c1c26e0d-54e9-3bfd-b60f-7d0acee1c020 | -18.97075 | -45.45166 | 2024-09-30 05:08:00 | AQUA_M-M | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c50d35cc-9299-3110-b550-2e25732f813b | -18.96935 | -45.46097 | 2024-09-30 05:08:00 | AQUA_M-M | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 74e82f04-9932-3b89-911b-1608647f44b6 | -18.00398 | -44.31591 | 2024-09-30 05:08:00 | AQUA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9b399d11-487f-3781-8bb0-96d7a87c9a87 | -17.62992 | -46.66329 | 2024-09-30 05:08:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 77928b06-ee04-3fde-9a95-5f4ed9969dd3 | -22.71987 | -44.8232 | 2024-09-30 05:08:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| cbb4a34f-5cee-3244-a9bf-fca037c74a5c | -28.51018 | -50.66928 | 2024-09-30 05:12:00 | AQUA_M-M | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 8233b93d-5b55-38e7-9ce0-a71325314438 | -1.73433 | -47.12846 | 2024-09-30 05:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fac1ff1d-1684-39b3-8379-253e4dbc04ca | -1.72949 | -47.12263 | 2024-09-30 05:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d16896d8-59b6-3c6d-be36-43e90090c091 | -1.72864 | -47.12814 | 2024-09-30 05:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8dbe0877-8c60-3bed-a1de-cdde3a7bdbad | -1.7286 | -47.12188 | 2024-09-30 05:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a92079a0-9d58-316d-8421-527ce8c22603 | -1.72778 | -47.1274 | 2024-09-30 05:23:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64944e14-2df5-3d1a-93e9-b48ad17077e5 | -4.60778 | -46.65061 | 2024-09-30 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bfadcd0-a87b-3615-a6f6-4eb8152caab4 | -4.6018 | -46.64225 | 2024-09-30 05:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19bb748b-8453-3c2d-ab2e-f52e7f0c4350 | -5.32793 | -47.90015 | 2024-09-30 05:23:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec1494cd-d8b1-3a41-9429-e5d5bd7e3cdb | -5.32138 | -47.89914 | 2024-09-30 05:23:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b453c9f4-a41f-36b0-bf7b-0847c613c43c | -10.84424 | -48.14154 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49b247d4-a014-393c-b49f-8eb4cbee5587 | -10.84295 | -48.15285 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5c7e894-4e45-3431-9472-5111f6e65aa2 | -10.83799 | -48.13474 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7036cf8a-aa1c-392a-a8d4-547f32be37bc | -10.83728 | -48.14104 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 822d70df-5a73-3c14-8f35-2ba26de89504 | -10.83667 | -48.14632 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66c707f6-1251-3cba-a087-2113e5486c17 | -10.82432 | -48.13136 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92cc9bba-cf0d-3b15-94d4-81326e6a6fd6 | -10.82369 | -48.13695 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45aff176-f95b-3096-8393-0323777778d0 | -10.72198 | -47.98843 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67dab8da-b863-3c7e-b7f9-f9ef9b37370a | -10.72111 | -47.98668 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5bca7b5d-36cd-3516-bf9f-17e4875a4aee | -10.71515 | -47.98636 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 140959e6-05da-32e9-a73a-12a14f977e5a | -10.71495 | -47.97838 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4ea3b20b-cbad-339c-893d-49c597643a22 | -10.71428 | -47.98438 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f135b19-c21a-31ce-8b52-fe1bf001d26f | -10.71356 | -47.99088 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f31a1983-3f32-3c33-a32e-3a7fca99c8d1 | -10.70902 | -47.97828 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 92ed5141-aaae-39d0-97e6-f13c0095f4f1 | -10.7081 | -47.9763 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4dfd4695-abce-38b8-9f8b-ca062404d5d5 | -10.56761 | -48.0453 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 773d5c5a-1861-3110-ac39-7bcba6b282ea | -10.56728 | -48.04567 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bb310f7-13e6-3008-958b-c9687c1e09f3 | -10.56705 | -48.05014 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00ff702e-f321-39da-b2df-b4f510fd32ad | -10.56674 | -48.05053 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ce1ecab-0fbf-35d4-9d93-0847c617e5c1 | -10.56648 | -48.05497 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b1e3719-85f0-35a4-933f-c0efbfac1e2b | -10.5662 | -48.05542 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 093e8736-eaeb-33fb-ba6d-627efd380ba8 | -10.55962 | -48.05344 | 2024-09-30 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ecaf9a7-53bb-34a1-b1da-d6b6976d7c28 | -10.45135 | -48.20565 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00237856-8638-3cad-8502-b540eb222926 | -10.45079 | -48.21066 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4f3bde89-f7e4-31f5-aae0-4e759d9d5667 | -10.45048 | -48.20712 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f6aa2557-d118-31d7-a5bf-e32ae97a0bae | -10.45015 | -48.21638 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cdde9f0c-98ec-317f-8eb3-36c7a5a5fd91 | -10.44989 | -48.21209 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 81a04e7d-48e4-34f5-9539-a4632712d131 | -10.44919 | -48.21809 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1284a1e5-7e5f-39e2-9ff1-4a020172f73d | -10.44493 | -48.20089 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a28b6a6d-fc61-3cfc-ba61-afcf3915498d | -10.44436 | -48.20596 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9833d29-1b10-3f3f-a204-20d82c9bf03f | -10.44382 | -48.21076 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ca879345-4fe2-3b3e-819d-bec5c7ec0cf2 | -10.44351 | -48.20715 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dea1ad95-cdb5-3ec5-8821-8bf9f2019f75 | -10.44323 | -48.21602 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 036dcf5d-9a41-3d8d-94c4-d71895dd9465 | -10.44293 | -48.21207 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15df48c7-c0e8-3a8e-bac4-9eb396932747 | -10.44263 | -48.22145 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 31aa536f-a870-34b8-a9dd-b8d1ce6d38a7 | -10.4423 | -48.21742 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 29f950de-1905-30ec-9b34-86b151269994 | -10.4355 | -48.21606 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 92d67f69-5184-38d7-90c6-ff340497418b | -10.42944 | -48.20831 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bb4c923-6401-34e2-a98e-ec8e43f8fe8d | -10.41924 | -48.17616 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 380c249a-c2d4-346f-9d43-9f1ab5796848 | -10.41852 | -48.18236 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e743b48-5730-3832-bde7-bfcb853d7b0d | -10.41788 | -48.18785 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d208e324-cfdc-3d4a-904e-b6a8e85165f0 | -10.41655 | -48.19933 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7102c87a-84fb-3d10-be24-d26743ba408f | -10.40979 | -48.19749 | 2024-09-30 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15826bb7-c934-3490-bce8-88bde4aa6873 | -11.17666 | -48.49715 | 2024-09-30 05:23:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa9b2e76-86a1-31bf-9f13-6d4a13245c8f | -11.17598 | -48.50333 | 2024-09-30 05:23:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 811a6a3f-d80d-38c9-b621-5384dfd7029f | -1.97786 | -48.69261 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb84e90a-a33b-336a-89c9-3d8967ce0ba5 | -1.9719 | -48.69164 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b13acfc-8534-35ce-b1a0-c8d4ac634459 | -1.41935 | -47.4086 | 2024-09-30 05:23:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4156a34a-302e-3386-ab5a-b30cd90afe23 | -3.47042 | -47.66362 | 2024-09-30 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df28b61b-6311-391a-9a1c-f09351040ed3 | -3.46961 | -47.66939 | 2024-09-30 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b074112e-4011-340e-aa5b-88302bd33091 | -2.99201 | -48.07796 | 2024-09-30 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 136c81bc-24ff-3f5c-be6a-1ce0e07a0c03 | -2.64106 | -48.25509 | 2024-09-30 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbbf9ab2-4efe-3721-ba35-c48662e57464 | -4.63706 | -48.5327 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 57a7728c-7dd4-331d-a7b0-36a97e66118a | -4.63082 | -48.53168 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a4949d-2803-3f94-b410-1b9b784d7b23 | -4.48916 | -48.11496 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68e80973-c452-349d-9a7f-7302ac8e3cfe | -4.28253 | -48.65289 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 45b959ab-3d53-31fd-9f96-4e59974fb829 | -4.28239 | -48.64875 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b84e348b-388b-3324-a6b9-2e923aac46c6 | -4.28173 | -48.65351 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5072850e-0d42-39c7-be8e-365ae2c6c982 | -4.27705 | -48.64723 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d8805768-8004-300a-a194-8c714e61121c | -4.27636 | -48.65197 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cb817514-b963-3173-8b03-2eea170408f0 | -4.27622 | -48.64778 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 93146740-f429-3f93-8aef-a08c9da89065 | -4.22221 | -48.58942 | 2024-09-30 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 021b064f-afed-372d-9bdf-a20f9f39fa25 | -4.18871 | -47.9359 | 2024-09-30 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b171b1f-0b69-3517-9e54-1399beb302dc | -5.66591 | -48.83316 | 2024-09-30 05:23:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed1f94ce-3dfd-3a2a-9952-487041e12a12 | -9.58524 | -50.20638 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f11755c-0232-30fa-9418-ccb5f3ddeacb | -9.58469 | -50.21091 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8309c2b4-eee4-30b9-9390-7e4800efa4b0 | -9.58369 | -50.20066 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01b8ea67-1030-3e00-be07-c38de1d3157a | -9.58311 | -50.2052 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README60.md)
