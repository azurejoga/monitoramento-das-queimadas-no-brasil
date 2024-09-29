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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b74dc5-777a-3747-a9c4-51a90d16a3d7 | -4.84373 | -50.92842 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a49c8c4c-2963-3b60-98f9-bfba017dd81b | -4.83613 | -50.93849 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9e145cde-d977-3291-b105-80aa01cb87e1 | -4.8349 | -50.92968 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 083b485a-03ef-3f92-b08b-a03e0aa1120c | -4.83367 | -50.92087 | 2024-09-29 01:07:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2eb54bb8-6389-3f58-a1c4-a9d93919c562 | -4.49362 | -48.11612 | 2024-09-29 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2ab5b944-2776-3399-944e-3339de9344ed | -4.45052 | -46.12984 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4fd907fe-51b0-39ef-93f1-ab1db8e41966 | -4.44823 | -46.11427 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 54c27615-8b3a-3664-9ebc-951099bbc003 | -4.44782 | -46.3461 | 2024-09-29 01:07:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 554cd4f0-c266-341b-bcf5-666d1fd48b02 | -4.43748 | -46.35405 | 2024-09-29 01:07:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 614f6a81-1f45-30be-98d4-c80ae50ea2d4 | -4.43657 | -46.3478 | 2024-09-29 01:07:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 124.9 |
| fff4fd72-f4c3-320b-9a31-0ed8b6acd69d | -4.43537 | -46.33927 | 2024-09-29 01:07:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 4bd54b59-1200-3827-8001-66ab5cee5fda | -4.43433 | -46.33295 | 2024-09-29 01:07:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 88f1938c-89f1-33ef-ab7d-7a716c520948 | -4.38023 | -47.61179 | 2024-09-29 01:07:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 38223581-af90-3fb6-b07b-ae1e11fe5858 | -4.22595 | -48.5928 | 2024-09-29 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c7c0c98c-7f6d-3c04-b0bf-61d4564858ec | -4.15152 | -51.05768 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0050a2a8-9e9d-31bd-8266-ec0a29276e16 | -4.05161 | -54.01897 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5255cea3-c1a7-3482-9521-ac632e5751f5 | -4.04188 | -54.0202 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0447f208-1cb0-3380-a0d7-f30ca5cb53cb | -4.04046 | -54.00962 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b2d5c837-eae8-3b02-be09-d18586e42fea | -3.91313 | -46.46307 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6170e21d-b98f-332f-b92a-e807ad0d73a5 | -3.7331 | -53.80798 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19476465-9f15-3b44-8baa-92a140ccf733 | -3.73164 | -53.79755 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| db676e17-6a93-3b0e-a69f-43bd0215a157 | -3.70474 | -47.61726 | 2024-09-29 01:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 69a61ca6-a71b-3cc8-9c25-cdf59f61b51e | -3.69807 | -47.62468 | 2024-09-29 01:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4ac95850-2dce-393b-873c-fb23d005929c | -3.69633 | -47.61231 | 2024-09-29 01:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cdac187f-e745-3e9c-9ab5-6abd5f5e4f80 | -3.66617 | -53.81684 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 90dd71d4-0b26-35b4-81f7-b31171616054 | -3.63681 | -50.80081 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75c0c0ff-605c-3691-b619-e56fe202d8c8 | -3.63557 | -50.79195 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 98f027dc-d1ee-3f6b-81dd-07ae36bae00d | -3.57003 | -50.58344 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 48ad11b2-d079-3b32-a13e-d40dc3e5ec91 | -3.56893 | -50.38209 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 907c66a3-5183-3bfb-8820-55d92d4187e8 | -3.56876 | -50.57449 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a1a55394-3b62-3f7d-b2e4-c46db8ef58ce | -3.56765 | -50.37305 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 84b0cca6-4a5d-3510-b134-ebef4708190a | -3.55871 | -50.3743 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f66146a8-3b11-3ab7-9228-991f209d9141 | -3.50835 | -51.20035 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 9d2c8919-0bb5-3a68-950c-4272d3fcfbfa | -3.50712 | -51.19155 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6978c63d-2fb1-309c-9b5e-d3d2349fb2bc | -3.46601 | -47.65809 | 2024-09-29 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d2f391a7-6d38-3345-9610-6ac20a269722 | -3.45825 | -54.10067 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 37e5409c-8eb7-3194-a15a-b89cfa8915b0 | -3.45676 | -54.08985 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4291594-7028-3314-9ca7-0ec202142997 | -3.44707 | -54.09115 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 3c4c2079-1720-380a-847d-e022fdd28a0e | -3.41369 | -47.59007 | 2024-09-29 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7b8f97d3-f2f1-35a4-8bf0-32c54f0cf591 | -3.40759 | -47.59679 | 2024-09-29 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a418aca-e7bf-36b8-a996-a32dbf438575 | -3.3363 | -50.30439 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 84cdc0d4-608c-363b-87b3-e4c782a81d5e | -3.33357 | -49.03314 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 778c668c-055c-344d-9db3-cc9bd91c0289 | -3.32733 | -50.30566 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 796dee54-226d-3d01-a4dd-5fbc224d6503 | -3.3052 | -50.66696 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 51d99d9a-bfc0-390a-9f04-d0818aa54711 | -3.29575 | -50.67426 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 227997d5-310b-3bd8-8fe0-cd06b55f4d10 | -3.29451 | -50.66533 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e94fae05-39c9-32b1-8d60-b0c4b1c859f5 | -3.26957 | -50.15546 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 59fe54ae-3c95-36b1-9baf-32db28e2e15b | -3.24098 | -50.01824 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 92e06d70-36d8-399f-b8ca-3ba1eae3a476 | -3.19937 | -50.44075 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 10e8649e-8222-32b2-91e0-ba061638dbb8 | -3.19841 | -51.15498 | 2024-09-29 01:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 163a5871-67e1-399b-84ce-fd48a8faddd3 | -3.19169 | -50.45099 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cfd2d1f0-f0de-36fc-926d-3b579930f8e2 | -3.19041 | -50.44197 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 70126503-b8a5-3b84-865f-4c4241cc019b | -3.14838 | -50.27831 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 88e2fd1a-94fd-30cf-8160-86872c006fba | -3.14711 | -50.26918 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3cbbb776-0405-371e-b022-f33f0c370f81 | -3.13939 | -50.27961 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcc3b4b4-eff0-3047-b4ec-7fba4150d7c4 | -3.13512 | -53.75945 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5159553a-56a9-31d3-94d1-b40ed4fbb86e | -3.13372 | -53.74929 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a62af635-0e86-3fc8-aa1f-f9787a9f87a7 | -3.12566 | -53.76075 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 238079c6-aa94-3125-afb2-dc3766b019eb | -3.12427 | -53.7506 | 2024-09-29 01:07:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| dc15a41e-4d5f-3288-b7ba-80ffe301d859 | -3.11362 | -50.48684 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66b90239-8a1e-3d87-99da-ded49c3cb933 | -3.10469 | -50.48811 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9885a96a-334c-316e-a720-1677fe05bda8 | -3.09592 | -51.28943 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4cca6ef-3994-311b-9341-1654ccf455c8 | -3.09575 | -50.4894 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 572347be-86be-3752-b2be-0436e9283582 | -3.09447 | -50.48037 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| d4e8064f-7c99-38ab-b3eb-dda7ef9949e5 | -3.0932 | -50.47134 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b4fec69a-8c94-3143-80bb-8d4a613f6932 | -3.08545 | -50.48761 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 62f22219-379b-3d70-8abf-80d351a74418 | -3.08419 | -50.47858 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7ae3ae0d-112c-3db8-9b12-21cb269bd07a | -3.07651 | -50.48889 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 108337b1-c7f0-3b83-9224-ba47901af52b | -3.07525 | -50.47986 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 21f5ad61-daa1-3161-85e1-1d58df0ce980 | -3.06757 | -50.49016 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a31b89e4-2caf-36dd-a646-17460a536dc9 | -3.06631 | -50.48113 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6b7e36db-28e6-3963-aa45-ee9115838ada | -3.05667 | -49.56744 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d09cbe32-76ca-3fa7-abf2-333b74ea0265 | -3.05658 | -49.36784 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ccdce3f5-1ffa-3e94-8505-383646fe9e3b | -3.05529 | -49.55778 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59d37aa4-1f07-3073-a031-984cd4a92249 | -3.0384 | -49.55658 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f7765ac-0845-315d-b5dc-1d4ed1c3c2ec | -3.03705 | -49.54689 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 246d5b6c-5b92-383f-8aa2-1c6a31d0a39f | -3.03569 | -49.53719 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7143934-a664-378c-b6e7-f90ffdbbb6e1 | -3.01851 | -51.05784 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09fb09c6-1202-3c28-a9d2-49a5178fab9f | -3.00843 | -51.05026 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3dabf1b7-abf9-3fd7-a931-99f2e96f7ea5 | -2.96218 | -51.65231 | 2024-09-29 01:07:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 198a4cec-2137-3c3d-bf6e-5c208f3d66d1 | -2.96096 | -51.64352 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0e961806-d906-3d45-a9b6-9920ebb470df | -2.89447 | -49.11635 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f5ffe1da-02f2-3f33-8050-382edacbeeb4 | -2.88933 | -51.58192 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 51d3eb78-91bb-3765-b4c5-7109dc9b45af | -2.88148 | -51.66951 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f479b0ce-546a-3439-a73e-f8a201cd827d | -2.88026 | -51.66072 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff78c3fc-a9fa-388c-9d4b-5c9be14fe797 | -2.88004 | -51.38607 | 2024-09-29 01:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 621aedf0-2897-37d6-9560-4af2a470704f | -2.87388 | -51.67955 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 328cc244-0eb4-3f23-94f7-fbb20a636832 | -2.87265 | -51.67076 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ddea761e-676c-3112-8506-89ca2f3be27f | -2.81748 | -51.93647 | 2024-09-29 01:07:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 37d46222-14cf-35fc-b664-4524e27d0d45 | -2.72099 | -46.72363 | 2024-09-29 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ea411d4a-a30c-3cbf-8d62-d14d16f0bdc8 | -2.64093 | -48.25269 | 2024-09-29 01:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 692db35f-929a-3c61-8793-6461572b8154 | -2.59514 | -47.66086 | 2024-09-29 01:07:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9b8a366b-0f4b-36f6-8456-98bf9add09f4 | -2.58782 | -47.65534 | 2024-09-29 01:07:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 56de8696-1928-31ad-ae3f-570eca054609 | -2.47545 | -49.16962 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 73bcfb0a-7016-33e6-9e9b-2849020b1319 | -2.47399 | -49.15937 | 2024-09-29 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 223a7cc6-9686-35ab-b0e5-494582507b02 | -2.36504 | -47.60884 | 2024-09-29 01:07:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| df0c9283-e758-303f-bf02-700e82b950b1 | -2.3632 | -47.59594 | 2024-09-29 01:07:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 911aa4e6-9494-31bf-acdc-55c650eb881f | -2.35447 | -47.61035 | 2024-09-29 01:07:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 1a4dcc8b-3501-33bb-a662-c6c547d9fe99 | -1.88159 | -52.09329 | 2024-09-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 8bd254ef-e144-3074-a297-8e5f3b1855d3 | -1.87275 | -52.09454 | 2024-09-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README15.md)
