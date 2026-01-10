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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34caf341-2f0f-3247-a766-0669da503b05 | -12.39392 | -58.03542 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d54f99f1-3a65-372d-9c51-e0da8639972c | -16.05201 | -47.21766 | 2026-01-10 04:29:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fc66184-f85d-30f2-90c4-ce443f746e1a | -14.191 | -57.24107 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efaecbf2-84d2-33b3-8f6e-79b4ef571e43 | -12.38455 | -58.0411 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64c4dbe9-3510-3349-a701-976e5d1922b3 | -14.19488 | -57.24855 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a07d19b-3381-3acb-b8c3-babe9f286405 | -12.40064 | -58.04817 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0cbcddb1-0b13-3ea2-8f16-a1b5ae19a57d | -19.20316 | -46.50106 | 2026-01-10 04:29:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcc43dd7-9519-3c5b-bca6-e2706eb12025 | -12.39089 | -58.05112 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 852208f1-0675-32a7-bde6-d011dfc47171 | -16.84181 | -46.82514 | 2026-01-10 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e9d5b3b-feae-3091-a048-d1163b9ce8ca | -16.10672 | -56.74887 | 2026-01-10 04:29:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 074341a0-c84f-3c07-a3f9-20446070f49c | -12.29414 | -57.39643 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b33e20f-a8f8-351b-b3d2-5e4b8b725774 | -12.38376 | -58.04503 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05ab64a3-4295-3993-9dd4-a18b35444d83 | -12.38677 | -58.04225 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f9794f25-bcde-358c-bcfe-ebecd44b471b | -12.28875 | -57.39534 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44b8b015-a420-3c93-abf8-b692e68f597a | -12.4086 | -58.03753 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| fde901f9-2597-3b8d-aa6f-37858923d9da | -12.40221 | -58.04032 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 20586809-7e06-305f-b758-a4444bc360e9 | -12.40665 | -58.02982 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 492f47b6-7d39-3467-8e53-69bbaf57b11b | -12.39345 | -58.0549 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e26aaeac-c236-3551-8817-9180367b1689 | -16.83839 | -46.82459 | 2026-01-10 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0841c395-2077-31f3-9d01-12980932ee9b | -16.10083 | -56.7534 | 2026-01-10 04:29:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb27f05c-9f74-324e-aed2-c432ed47bd08 | -12.30015 | -57.36494 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1e1c0d1-02b1-3f52-8810-ebc4ea591e8a | -12.3042 | -57.37302 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e20bc36-de53-381a-b6f2-ffdbf748c2ed | -12.40029 | -58.03259 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 122de0a1-a9d9-35e9-a163-c9fb317382d3 | -12.29643 | -57.36776 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cdcd7a3-ea03-378d-8793-4af629a621ab | -14.19037 | -57.24425 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d1ebd2c-c349-3bf9-aa74-82966c7a5ce6 | -12.39986 | -58.05207 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19d05b4b-088b-3e27-ae4c-2b8a49a686aa | -13.48472 | -52.94724 | 2026-01-10 04:29:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccace293-1cd3-387e-9e7b-156ca5c990f8 | -16.58914 | -58.21464 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 49826aa9-29ad-327d-b928-b6e2a7af2835 | -12.40104 | -58.0287 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65993ab7-a910-3cdb-8058-b28016ff7877 | -16.44199 | -58.16403 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 59c7c7bc-d1c2-3ba4-94c5-5c82978bd70e | -19.19138 | -49.04718 | 2026-01-10 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7903d894-c0cd-3271-bfc7-4cb3b247f457 | -12.30554 | -57.36596 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 446dfad2-23c8-3b93-aeae-a3619a7731c9 | -14.9764 | -43.42329 | 2026-01-10 04:29:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d437245-4cd8-3f94-be7b-005ac617c065 | -14.20447 | -57.25432 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45781eed-53ec-334d-8c7a-ffa8622ad115 | -12.39018 | -58.04212 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 204d679e-dbf9-3159-ac4a-87eebb199490 | -16.26947 | -54.35787 | 2026-01-10 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09d42c5a-046a-3c16-953f-06adcc6bf8a7 | -12.40515 | -58.03761 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4d330295-81f2-3cd8-8a74-8ed867fe5162 | -12.40377 | -58.03251 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc7952a2-882e-3bb3-8dd2-b71e594d3ffa | -12.39894 | -58.02755 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efeaac2e-2f02-3764-a0d7-f2fa76cb0cf6 | -12.38861 | -58.04995 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 140f237f-0d0c-382a-9551-9f03b71f204e | -14.31178 | -57.59188 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3a6715e-8469-3a85-be98-e946c23ecd5e | -12.40439 | -58.04155 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| be8efe5c-4158-3f6b-a437-73af3fa987ba | -12.40781 | -58.04145 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 726b16e5-5e5c-362a-9ab6-cf9aadcd4ede | -16.37036 | -57.20822 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b244216a-cd26-3042-8a5d-4a9b1290f516 | -12.29088 | -57.39571 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f13c8527-993e-3599-b1e4-7298be1f8719 | -14.31246 | -57.58839 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3200653-f14c-3496-b648-f801833911cc | -12.40142 | -58.04427 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d1677869-d139-3949-b50b-3530b0c2894d | -16.05256 | -47.21393 | 2026-01-10 04:29:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acb06c51-fa75-3d90-bac4-dcbc8903b304 | -12.39013 | -58.05504 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4aa7ac9-33f7-3ced-9a52-ca20951fb3d9 | -12.38601 | -58.04618 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 518f3ba2-05e5-3d82-a031-232e231ba4e9 | -12.38525 | -58.0501 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 433056e8-c600-312f-af21-d937401a90fe | -12.38534 | -58.03717 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6625bb2e-b89f-30f5-814f-e4e86ff4a699 | -13.89552 | -46.52121 | 2026-01-10 04:29:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 547bd879-e6fa-32e3-822f-0958d2dbc6a9 | -19.78224 | -45.39249 | 2026-01-10 04:29:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64a6e595-86be-3d41-9d69-2863a6228954 | -12.38782 | -58.05384 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c3a9253-f299-33c5-a7f7-30c8ba497625 | -12.39502 | -58.04707 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9e49379f-1e7b-39ec-9fa1-7f475cc9d6e4 | -12.29481 | -57.39292 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fdf5996-bb90-3453-821e-a881d239265d | -12.39576 | -58.05612 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 683a9afe-c32c-3570-a61e-862c87547eb9 | -12.3924 | -58.04328 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0961c454-e8d8-3a62-8a7c-6b5944a78ef3 | -16.59006 | -58.21423 | 2026-01-10 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a29d997c-68f0-35b5-8f63-b879b67e3798 | -14.19936 | -57.25304 | 2026-01-10 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1998bc8-ed13-3e08-a984-5269a6302c05 | -12.39164 | -58.04721 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4dfb7f1e-b0b9-31ad-be85-d41fb2e2acb5 | -12.40703 | -58.04539 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af2950f3-1235-33d4-8e2b-df003e0c22f2 | -12.39424 | -58.05098 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d91622-d94c-3294-8a82-39b9197aaa6b | -12.39581 | -58.04315 | 2026-01-10 04:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 88433d3e-0f95-3674-8684-244d9fa5bbe5 | -12.3946 | -58.0307 | 2026-01-10 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 150854f3-2a84-3241-b3ec-12c42b256b2a | -12.3756 | -58.0322 | 2026-01-10 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 8e0d6333-7ebc-3809-a197-acdba5b5104e | -12.4135 | -58.0292 | 2026-01-10 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a49aa84c-be80-3edc-a721-eb05940eda3e | -12.4133 | -58.049 | 2026-01-10 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e16e5675-b3ed-3da7-b082-8722e9a46a87 | -12.3943 | -58.0506 | 2026-01-10 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 6a53862a-0756-329d-a72a-094819214403 | -20.23955 | -46.44891 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4d46371-efd0-3cfa-b9bf-9e75ccfa2e52 | -20.26602 | -46.41699 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24bdfc89-810b-3dd5-b6f9-5413a10d5446 | -20.27114 | -46.41999 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72d801dd-c90c-3412-bf47-c80a1a1b6a55 | -22.82694 | -49.29095 | 2026-01-10 04:31:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aadc110-2f7d-3306-a118-ca633751d7a8 | -21.53186 | -47.14483 | 2026-01-10 04:31:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e68d4142-2cfc-38ab-921d-11aad6aab8df | -21.25588 | -49.17054 | 2026-01-10 04:31:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44aa65b9-3424-304a-87e8-0791c0fe58d3 | -20.63777 | -49.71561 | 2026-01-10 04:31:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7432e65b-d806-32ce-9c17-25aae5bbad89 | -20.26815 | -46.41493 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03715b0d-f45c-35ae-a705-c7557d308efb | -20.71058 | -47.28684 | 2026-01-10 04:31:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1022837-12d0-395d-8dc5-4fa1a92fc824 | -21.20133 | -43.75259 | 2026-01-10 04:31:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 30906efd-adf4-3935-b4eb-5547fe3248c3 | -21.52834 | -47.14424 | 2026-01-10 04:31:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d951b051-88ef-337e-a6b1-d853fff15f9c | -22.97796 | -48.64572 | 2026-01-10 04:31:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03b6d820-275b-31fd-9937-782e696fd3fd | -20.22692 | -46.48692 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a922b861-30ac-3fb9-bef9-5ea8d396cdd7 | -21.0483 | -49.59094 | 2026-01-10 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6c340519-bd37-373c-be41-ae61cb4db678 | -22.97738 | -48.64964 | 2026-01-10 04:31:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7220ff82-2d15-39fa-a1ea-a61da571bab1 | -22.8236 | -49.29037 | 2026-01-10 04:31:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 19ba4eba-b8eb-3b56-a5ad-bac43c790500 | -20.92376 | -48.78141 | 2026-01-10 04:31:00 | NOAA-21 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5dd29151-90b9-3c5d-97de-aff695b37a00 | -21.28964 | -49.03863 | 2026-01-10 04:31:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f354a370-3d64-3682-8d22-799e01f9ea9a | -20.39335 | -50.75369 | 2026-01-10 04:31:00 | NOAA-21 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26dde038-3ed6-322c-ab4b-4792eceaff6f | -22.82417 | -49.28658 | 2026-01-10 04:31:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2291132c-c425-32d0-90f6-09a1f3167c95 | -23.11209 | -49.11263 | 2026-01-10 04:31:00 | NOAA-21 | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b4ce2d6-61ea-3f7b-9436-b15fa32dc67a | -20.22334 | -46.48641 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93b72d9d-1fec-3f5b-a824-9f3be35aedd8 | -20.92432 | -48.77766 | 2026-01-10 04:31:00 | NOAA-21 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78c1d982-ecfb-3eae-a331-b984b774f5c0 | -21.04499 | -49.59035 | 2026-01-10 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f1838bfc-830a-31a5-9088-4d88ab19c62e | -20.33684 | -49.39981 | 2026-01-10 04:31:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbe7733b-b3b9-3c28-b4e6-007465ba028f | -22.72972 | -49.32903 | 2026-01-10 04:31:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 20150c6e-fee5-334d-bc24-64324655aea1 | -24.85743 | -49.23164 | 2026-01-10 04:31:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac263406-d354-3f98-a879-10828567d6f3 | -22.82027 | -49.2898 | 2026-01-10 04:31:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c429cdfe-cd7e-357d-a23d-e7c2e4795aa2 | -24.85405 | -49.23106 | 2026-01-10 04:31:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e2fb3e8e-2e34-3743-81c4-a7a3f3e2802e | -22.82303 | -49.29417 | 2026-01-10 04:31:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README9.md)
