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

## Dados Diários - Página 233

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a529229-a509-386c-8c83-fbab952bd9bb | -11.328 | -51.0018 | 2024-10-09 12:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f10d17cf-713c-327a-b385-751347789b86 | -11.3232 | -51.3414 | 2024-10-09 12:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5503569f-2d43-3d6e-9d4a-395d979d13cf | -11.7749 | -44.5335 | 2024-10-09 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 885019a7-8f92-3424-abd9-4bfc97d5945d | -11.7041 | -49.9539 | 2024-10-09 12:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fd33da48-2fc2-3dc1-8f3c-498d01e58954 | -11.9746 | -45.1524 | 2024-10-09 12:56:14 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 57c431bf-0540-3edc-bbcf-77c8c5da1e9b | -12.1083 | -50.914 | 2024-10-09 12:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 37449cb4-0338-3d7a-a714-2f1110e9ef06 | -12.0895 | -50.8949 | 2024-10-09 12:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0f06b2de-edc0-3b04-9f02-e00bba8f910b | -12.1086 | -50.8926 | 2024-10-09 12:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 0cf640d8-5bf7-31da-ab95-42bbe9d2edde | -12.6875 | -62.9656 | 2024-10-09 12:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 37c65e44-e648-310b-9691-f607c2f523bf | -12.7501 | -62.269 | 2024-10-09 12:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8ec380c7-c476-37b0-ba6d-c97e095e881e | -12.7064 | -62.9645 | 2024-10-09 12:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fe07ac52-0bb6-3cc9-be78-9d675edb7296 | -13.2877 | -53.704 | 2024-10-09 12:56:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 74f1b6b7-1c53-3e16-91fe-8c8af6a241e5 | -13.3068 | -53.7019 | 2024-10-09 12:56:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 91a9492f-954b-3797-8ef6-21de300717ee | -13.288 | -53.6832 | 2024-10-09 12:56:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 8b2d3efc-40e2-3747-8ce3-66c6089c7ae1 | -13.3786 | -61.9582 | 2024-10-09 12:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a6b8f0c4-b761-357e-b95e-16047b8b9127 | -13.3976 | -61.957 | 2024-10-09 12:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1a4f3be9-f74b-3f40-ab06-95548c7ac1b9 | -13.8739 | -44.6564 | 2024-10-09 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b9db60d2-a7f1-30f5-b2b4-17b3adbb23bd | -13.8933 | -44.6529 | 2024-10-09 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 53aca56d-f16b-3515-99be-9522a2a25cdf | -13.8364 | -44.5927 | 2024-10-09 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a4cd604f-213e-3079-8ee6-6d8303ac6876 | -13.8369 | -44.5691 | 2024-10-09 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 39309e5f-9576-38a3-8b16-cad9795c3817 | -13.9143 | -44.5788 | 2024-10-09 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| e0edb9a3-0e4a-31b5-bb7d-52e821149191 | -14.2052 | -45.507 | 2024-10-09 12:56:26 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ca97c3e5-e62e-363f-bfc3-1b9c509554b0 | -14.0778 | -51.116 | 2024-10-09 12:56:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 88fe24ad-c180-3f06-8e2a-28e302c23433 | -15.6683 | -59.4163 | 2024-10-09 12:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 9103315c-90a4-3416-a8d7-9ea8376c583c | -15.6877 | -59.4145 | 2024-10-09 12:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1c622b4b-bc91-3f66-8b9e-6ad583563b31 | -15.7076 | -59.3726 | 2024-10-09 12:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 187.6 |
| b7230e3e-0e90-39b3-b473-a2ca431520a9 | -15.6686 | -59.3963 | 2024-10-09 12:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| f0b6e444-be24-3d56-8093-d48d124c3b3a | -15.688 | -59.3945 | 2024-10-09 12:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 7b0a13ab-5fe4-347f-a0f1-3afcad6ffee5 | -5.49 | -44.28 | 2024-10-09 13:04:54 | MSG-03 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68a1436a-44b6-3fb1-923d-6d12b98886dc | -6.7798 | -60.0552 | 2024-10-09 13:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 312.5 |
| 45abcbf5-1514-3d6b-b56f-41481d5d00c6 | -6.7799 | -60.036 | 2024-10-09 13:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 927ea5ad-a64c-366c-8dab-34c9991c44b7 | -6.7614 | -60.0559 | 2024-10-09 13:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 69619d8b-6fd8-34a5-8fc9-5c4337b98519 | -8.3406 | -44.0963 | 2024-10-09 13:05:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 9b99ac2d-afff-3ef8-8386-53dcc125ce45 | -8.3217 | -44.0983 | 2024-10-09 13:05:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 09b6ba5f-f490-3299-bec8-282e2fe93469 | -8.3403 | -44.1195 | 2024-10-09 13:05:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| fd5599e7-33dc-34f2-b736-c5cb4a6b464f | -8.4921 | -48.6259 | 2024-10-09 13:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 302c6aef-c860-38e2-9740-18940eed7a70 | -8.4919 | -48.6476 | 2024-10-09 13:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 236.0 |
| 4ee932f5-ab21-3ef4-962c-4c2fd75909db | -8.5107 | -48.6459 | 2024-10-09 13:05:55 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b5dce267-6fdc-3d3f-8cdc-8a43d115f2bf | -10.1003 | -62.5088 | 2024-10-09 13:06:04 | GOES-16 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 009f5a40-578c-3890-9964-c30dea79b2e3 | -10.5746 | -48.0178 | 2024-10-09 13:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 49a3cee0-6509-30c6-a39b-46e70b404f58 | -10.6256 | -55.9154 | 2024-10-09 13:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d0d9d8e0-5648-369a-b548-210ac1e9d500 | -10.6258 | -55.8953 | 2024-10-09 13:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b9c2119d-d75a-37fc-a031-3d293f729daa | -10.7434 | -50.8302 | 2024-10-09 13:06:07 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 23a6f2df-8cf8-3d10-b2d6-20ff46df564c | -11.1564 | -49.737 | 2024-10-09 13:06:09 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b5621a57-f80f-3f6f-9588-97e123e1fa2f | -11.3034 | -51.4069 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 59ba5c3a-c06d-3a90-bf2b-8f23fd632707 | -11.309 | -51.0038 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2184e930-a261-30b9-b476-bd3bd0602b5e | -11.3093 | -50.9826 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 86e40e0f-330c-30cf-b710-7432b3c84eac | -11.2094 | -51.3535 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 20a9ecff-95e2-3761-a9fe-78f139f7e69e | -11.3043 | -51.3434 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4b9057a1-d572-3f8a-8457-79dc65b5f087 | -11.247 | -51.3706 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4c600393-a855-3308-acc9-ea62b341e4af | -11.3031 | -51.4281 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4473c3a0-b4b1-37aa-8e40-6836402ba7de | -11.3046 | -51.3222 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4aade705-8010-3a73-b825-82d251490c53 | -11.2657 | -51.3898 | 2024-10-09 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 075d59e8-e135-35b2-b9a0-b874020dfd6e | -11.3232 | -51.3414 | 2024-10-09 13:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 9f383031-f6d2-3b1f-a66e-76107fa9eb28 | -11.3274 | -51.0443 | 2024-10-09 13:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c6ae1acc-330e-339d-8493-3f86497494fa | -11.3652 | -58.9961 | 2024-10-09 13:06:11 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 5492479e-eedd-3c68-9f6c-6d43550e3476 | -11.3283 | -50.9805 | 2024-10-09 13:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 40a122c0-41ca-3caf-b5e6-12c973c862fd | -11.3277 | -51.0231 | 2024-10-09 13:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a4874a74-8bf5-3da0-8d1f-849d65b6fe79 | -11.3235 | -51.3202 | 2024-10-09 13:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 2416981b-8c77-33f2-8d48-50979a1b8ff4 | -11.328 | -51.0018 | 2024-10-09 13:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 279165e2-0e64-3c67-8611-bb36863cb6b1 | -11.7024 | -46.4927 | 2024-10-09 13:06:12 | GOES-16 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 44a20fa9-b9ac-312a-9380-c983d0b49a13 | -11.7997 | -49.921 | 2024-10-09 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9a4e450e-813f-38b1-bf78-7bf9da52b950 | -11.7041 | -49.9539 | 2024-10-09 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2aaaa7a0-6df7-3398-86e3-eeff1c45d010 | -11.9746 | -45.1524 | 2024-10-09 13:06:14 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| aae0d5a4-5c36-3b70-ab07-f59a40a56bf0 | -12.1597 | -50.0501 | 2024-10-09 13:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 05f60453-6304-391f-8fc0-4a8caff20e46 | -12.1086 | -50.8926 | 2024-10-09 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 758aeec0-8e79-3905-ba27-66d9f5dc400c | -12.6091 | -42.1864 | 2024-10-09 13:06:17 | GOES-16 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 149f034d-a13a-3f01-b08f-43fa0f3a6d64 | -12.6821 | -54.7174 | 2024-10-09 13:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 98f4ce4d-07a4-3f5a-aa1c-7df0762bdf8c | -12.572 | -53.0544 | 2024-10-09 13:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e1c3cf6c-2354-3756-94fb-270bd2360fd8 | -12.6876 | -62.9464 | 2024-10-09 13:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c28bd72f-3902-357f-89a9-df50057f020b | -12.6875 | -62.9656 | 2024-10-09 13:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| d4ac1f21-0847-310b-9595-261e92456bf6 | -12.7501 | -62.269 | 2024-10-09 13:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a9a75fe3-3e49-35f9-9937-1e1e38fc66ab | -12.7502 | -62.2497 | 2024-10-09 13:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 971b3418-4149-3457-9eef-79f6229bc7e3 | -12.9756 | -62.4673 | 2024-10-09 13:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b92083b5-44d2-32bf-a6c9-4634a362ae50 | -12.9568 | -62.4492 | 2024-10-09 13:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a4008887-1059-356e-bce8-eec08e6b1b7f | -13.2688 | -53.6854 | 2024-10-09 13:06:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e40230bf-fe02-3ac3-b107-5798282bd475 | -13.2685 | -53.7062 | 2024-10-09 13:06:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6b47b7d4-56fe-35f3-945a-b4bcacd075a6 | -13.2877 | -53.704 | 2024-10-09 13:06:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| a0ba7594-231e-3a17-9d6d-3ce36f3caa28 | -13.288 | -53.6832 | 2024-10-09 13:06:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 59a9b8a7-44e0-3407-b28e-5a7f66d3860e | -13.3068 | -53.7019 | 2024-10-09 13:06:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6eaf27f3-d836-3fb2-b5dd-bc198af6f068 | -13.3786 | -61.9582 | 2024-10-09 13:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0f5423f6-d260-3489-b2b9-9ebe13aaf9c0 | -13.3976 | -61.957 | 2024-10-09 13:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 5085cd9e-aa4a-3743-8cc4-1b56e767c71c | -13.3978 | -61.9376 | 2024-10-09 13:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 9441464b-7fc0-3dff-8379-189347379df9 | -13.8933 | -44.6529 | 2024-10-09 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 82a4ca1e-aebe-3116-abd2-3ce293ef006b | -13.9143 | -44.5788 | 2024-10-09 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 9635b4a2-5646-3741-b2cc-9d4acbc320b1 | -13.817 | -44.5961 | 2024-10-09 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c30aa307-efc2-3994-97c3-ea78bf4a7ce0 | -13.8364 | -44.5927 | 2024-10-09 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8b781538-9f68-3a15-b209-5261250b0f16 | -13.8369 | -44.5691 | 2024-10-09 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e7426e95-1b4d-3ce6-86a0-8b9922412a17 | -14.1857 | -45.5105 | 2024-10-09 13:06:26 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f5c794ea-e870-3dbb-9be3-403613412a13 | -14.2052 | -45.507 | 2024-10-09 13:06:26 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f1a751b8-ee62-3025-ae4f-1f0ed841c966 | -14.1862 | -45.4872 | 2024-10-09 13:06:26 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c5d319a1-392a-3fd2-8bfb-a6b9f261ea90 | -14.2247 | -45.5036 | 2024-10-09 13:06:26 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b69d0580-128d-3920-9ec8-621ac40b2c28 | -14.8228 | -46.6419 | 2024-10-09 13:06:29 | GOES-16 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| abed3dcd-08b1-3cb4-9920-aa2611c2ea62 | -14.8001 | -41.6588 | 2024-10-09 13:06:29 | GOES-16 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 86.2 |
| e163bef9-d4a0-306f-8055-2386bb0149f4 | -15.7076 | -59.3726 | 2024-10-09 13:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 214.1 |
| 1764ae51-22f0-3c76-914a-63863ba82da5 | -15.688 | -59.3945 | 2024-10-09 13:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| de198497-1d82-320d-9d0c-443ba746fb5b | -15.6686 | -59.3963 | 2024-10-09 13:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 93561051-cb3a-358b-94dd-fc394bb92e14 | -15.6683 | -59.4163 | 2024-10-09 13:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 62075b24-97ca-32e9-8896-a76e3b879307 | -15.6882 | -59.3745 | 2024-10-09 13:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 249.0 |
| 89182076-d8d2-39f0-8897-30a3574ce784 | -16.96 | -57.46 | 2024-10-09 14:03:50 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README234.md)
