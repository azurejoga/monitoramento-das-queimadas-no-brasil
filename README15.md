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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06c6bbab-cabe-34f0-a37a-de57a2066d63 | -11.60752 | -55.34085 | 2026-06-05 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c9b76698-757f-3d91-b196-35e2214a7ebd | -12.43378 | -58.48509 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 194634d4-80a0-3a1d-86c7-859ecad7666e | -11.57139 | -54.57744 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8680435-f658-346b-a485-9ab0f7d03285 | -12.72957 | -54.72966 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c6f020c-6b41-3f15-a231-c74b0e2e4bc3 | -12.43705 | -58.49089 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae27eb42-7721-3161-8046-d4b065739d14 | -11.05837 | -56.92358 | 2026-06-05 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8e46d98-bb09-3023-b600-4d0ec848de0e | -10.03157 | -59.34253 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecac9f0e-7ace-3359-ba64-1645ee6a591a | -12.4471 | -58.4161 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39204124-315c-36bf-bb22-c57d531c5675 | -11.60822 | -55.33544 | 2026-06-05 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39d28916-85fa-3367-bccc-5eed41819e6f | -10.03462 | -59.34741 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddafb391-c1ef-3d0b-85ca-00977447df74 | -12.44757 | -58.41257 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b695e971-8820-35a4-85f2-ac2b4830e79b | -12.44749 | -58.47358 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c98e1fa-8e86-3590-a252-fab0f1668e8f | -12.09091 | -51.99858 | 2026-06-05 05:31:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50271e97-0e9b-3775-9259-c7535ab0c0a5 | -11.88676 | -57.82606 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb2e515-c4ee-354f-b9fd-e81904266fdf | -11.56714 | -52.8027 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ade203bf-7530-3b00-9e0a-3061fdfac570 | -12.444 | -58.46942 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 43dcc401-55fa-3db4-8849-f2b29e70af0a | -12.43847 | -58.48037 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 728f537f-9603-300e-b506-b89a20a6d506 | -12.73357 | -54.7398 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3eb7c1c-6a38-3731-ad6e-ce28245d039f | -10.90903 | -54.13843 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50239fb3-bc7f-3ce8-8472-0b4ef41282d4 | -12.4599 | -58.47186 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95d8e255-35bf-39b2-b09f-836517d731c5 | -11.56186 | -52.79791 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83cde6b7-12e8-3595-94dd-22c4d540580b | -11.55515 | -52.80536 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 79e08098-2d00-328f-82da-f94a19e7b769 | -11.60336 | -55.33477 | 2026-06-05 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9031fe9-debb-3980-b540-e8c6204e7233 | -11.0095 | -54.31306 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe107f07-f8dd-3156-a81e-df8e5a04bd36 | -11.55468 | -52.80941 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| be87cd75-c8c9-375d-b950-299174a329c4 | -17.77747 | -50.46766 | 2026-06-05 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ed64439-d8ee-3d14-b3d9-7e44db47ee1a | -12.43051 | -58.47923 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4007188f-3e9f-3610-ab05-46ddd4a8a16f | -12.44173 | -58.48626 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d51c33f-dc25-30f9-88da-27414ae64783 | -11.33721 | -53.96444 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30d0919f-3f09-30e8-b1ec-0e5ba7c01763 | -16.19139 | -58.46941 | 2026-06-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 111527b2-ff1c-3399-b53a-dba385ec704c | -10.8452 | -53.754 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff413374-6642-3092-b467-20cbc633623a | -11.55563 | -52.8013 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6bb719d2-87c8-3bf2-91a3-b90a8c208765 | -19.73577 | -53.5453 | 2026-06-05 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a39e70d3-a783-3435-9700-b1d551ed930c | -19.74183 | -53.546 | 2026-06-05 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c0203de6-b703-327d-a512-98d9cdffefeb | -19.74037 | -53.54521 | 2026-06-05 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 01bac7bc-020b-351f-b61d-0a8188d61403 | -19.74141 | -53.55067 | 2026-06-05 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e0252290-51ae-3e4b-bfe0-c6eaf8c2bd6a | -19.73993 | -53.54993 | 2026-06-05 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 95e498ae-4856-3d40-8832-f5fb6c77e080 | -19.72646 | -54.65293 | 2026-06-05 05:33:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8fcbc0a-3279-325e-813e-97c3058c787a | -19.72395 | -54.65373 | 2026-06-05 05:33:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 856ce564-43cd-35b3-9f8f-db5917824094 | -19.72079 | -54.65242 | 2026-06-05 05:33:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd2ede89-3af3-30ad-824c-f5794098b41b | -19.17049 | -55.1832 | 2026-06-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5428660b-01d9-3790-ab9e-ffa8a410d13e | -6.98479 | -42.87752 | 2026-06-05 05:44:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 818d7dc8-b9aa-3a2f-b3fe-94f25877d498 | -10.5226 | -42.37135 | 2026-06-05 05:44:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| fb5fcdce-27c3-39fc-93da-8a000745eba1 | -12.4515 | -58.47121 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ee451c2-8d28-32f2-ba3e-5a6953ea7399 | -12.22969 | -57.28219 | 2026-06-05 06:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c793de6e-eb8e-390d-ad05-273532b2c157 | -12.43104 | -58.4841 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 628447b4-aa11-33fb-8646-78af8261999b | -12.45091 | -58.47641 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b167b93a-00d8-30a0-8b47-9741ec5c28fc | -12.43728 | -58.48484 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e69f8650-c7e2-3911-a2a0-c50b1918e732 | -12.43968 | -58.48132 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edcfab80-286b-34f8-b471-a82a1ac92b9d | -12.44522 | -58.41497 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e2ab35ef-e13d-36bd-ada3-7b93863f55ee | -14.10186 | -59.37985 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d39b95fa-8e47-326e-b119-ee87ff0be78b | -14.10085 | -59.38918 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c488e5e0-4d03-3b83-8b50-82f215a0dd58 | -14.0994 | -59.39035 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79534f51-2e27-3361-b993-7cd1506b478c | -12.44121 | -58.416 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 600d00c8-067e-33e2-b480-e63f36710f8f | -12.22709 | -57.28254 | 2026-06-05 06:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6b08a49-9832-3352-be22-3944a8be6509 | -12.44092 | -58.47104 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7938244f-91f6-3153-82da-5a9881dde8e1 | -12.43893 | -58.41442 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edb7382c-f003-378e-80aa-c81ff91f66e2 | -12.44468 | -58.47546 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ed2af74-a84b-3cf1-9cdc-85be63c3564d | -12.43786 | -58.47974 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3c84cae-9d36-33e3-80fa-22332359e75d | -12.43282 | -58.48564 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a20c34de-5609-3bd5-91f7-f036b9d7d035 | -12.44636 | -58.40499 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 067a2c0e-dd88-3f5a-928f-1499d9404b62 | -12.44297 | -58.49047 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e359dfd7-c651-30cc-9d07-5a8496bd0b68 | -12.43672 | -58.48975 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b524171f-6213-329f-9f7e-3eb93ac4964b | -12.44241 | -58.40604 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 508423da-47ca-34c6-b7f2-adf4f6f1b86d | -10.01177 | -67.76288 | 2026-06-05 06:05:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f724cb04-39fa-364b-a801-071ffb969185 | -12.44751 | -58.41652 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca87f446-49f1-3e06-80f0-6318d2d9e837 | -10.75466 | -68.32938 | 2026-06-05 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a03d56ca-bb32-3556-a48f-8cec26c6b1bb | -14.09993 | -59.38571 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ae4c218-1f0a-393d-a20f-bdd22aeda044 | -14.10048 | -59.38102 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb125f40-930f-3166-9795-b9827294da7d | -12.45774 | -58.4721 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fed5d84-5688-3216-be39-26f9ac0007fc | -12.44579 | -58.41 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5eaa5aef-e922-3ba8-8bf6-c6a4def1885c | -11.88706 | -57.82798 | 2026-06-05 06:05:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54843070-e358-312a-951c-81625da50a07 | -12.44352 | -58.48563 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d33de5e2-87b9-341a-9adf-388fc5512403 | -12.43848 | -58.49118 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e3425cd-6b8b-3a1a-b6cf-98307d62769d | -12.44006 | -58.40444 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09a36352-2a60-3b04-b777-d614f8e91b3c | -12.23446 | -57.27753 | 2026-06-05 06:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e694a3f2-1e40-3f35-b4ba-be05a5d8e5ce | -10.00834 | -67.76235 | 2026-06-05 06:05:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1e9bb3b-410a-3819-afbc-ec7094f87b10 | -12.44181 | -58.41104 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64b1a182-0242-3124-81e7-43199f6a0f9a | -12.44527 | -58.47028 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2749e5a8-6363-342a-9ab1-4dd143ae308b | -11.88059 | -57.82734 | 2026-06-05 06:05:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d67c4441-24fe-3671-9af2-d18f21d1bd77 | -12.4481 | -58.41159 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa4e6940-5efd-3345-a371-27e4e0e7f032 | -12.44409 | -58.4806 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a077efb-cdfc-37a6-99b5-6e22c5e74565 | -14.10135 | -59.38453 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d34bb38-3d66-356d-abcf-8d94bc9e02f5 | -9.54461 | -64.5064 | 2026-06-05 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed812270-9d16-301f-9561-129ac8b85053 | -9.63306 | -67.21584 | 2026-06-05 06:05:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bebc5000-f449-30f4-aa37-486a810c747d | -12.23032 | -57.27636 | 2026-06-05 06:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8690c332-1207-3186-897a-3b30e047edb7 | -12.43343 | -58.48059 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 685535bb-57b4-3b90-82f3-326228e1a6fc | -12.43161 | -58.47902 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 674e63a7-1f1e-3665-b30d-523ed4654f5a | -12.22299 | -57.28139 | 2026-06-05 06:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d6168fe-823e-372f-bb5a-491e1e8133b2 | -12.22777 | -57.27671 | 2026-06-05 06:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edf50998-8568-3c8d-8204-012d43ef4f52 | -12.43907 | -58.48635 | 2026-06-05 06:05:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb412b03-b911-30a1-911d-83666a1fe04c | -12.44871 | -58.40659 | 2026-06-05 06:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cbd30d8-7da1-36ac-a3b1-9f1ddd5b100a | -14.09481 | -59.38858 | 2026-06-05 06:05:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bd7e27f-1c14-3247-bf30-ae8d44121988 | -16.19018 | -58.46893 | 2026-06-05 06:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5642765e-fcd8-3d25-9951-c325c4619e81 | -16.19076 | -58.46867 | 2026-06-05 06:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5be01c14-1aa1-37a7-940f-89ee723f73db | -12.44441 | -58.47403 | 2026-06-05 07:24:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7b120c50-bfbf-30ac-b0cb-2f6d2c6403be | -12.4414 | -58.40006 | 2026-06-05 07:24:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8a1b904c-dfc4-383b-bd94-f5259c61a63a | -10.03521 | -59.34356 | 2026-06-05 07:24:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4dd0f08d-93c0-338d-8d99-8b52668286fe | -16.60527 | -58.23563 | 2026-06-05 07:24:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3156a1c6-f028-3aff-a497-55ab05c678f7 | -12.43982 | -58.41117 | 2026-06-05 07:24:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README16.md)
