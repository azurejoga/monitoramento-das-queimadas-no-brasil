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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4279bd2d-b68f-3315-8742-4edd01bea9dc | -14.199 | -51.9122 | 2026-07-29 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 03e9e8eb-a29a-364a-92fe-d7faff6dce8a | -12.3292 | -54.0954 | 2026-07-29 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| eee71d53-4495-311a-82ef-b245ef68b484 | -6.8708 | -46.0126 | 2026-07-29 14:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9296cda4-7de8-37eb-b04e-c4b227bb36e1 | -14.199 | -51.9122 | 2026-07-29 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 23b6bc3e-7c50-3dec-8e77-a8cc9b55453e | -20.8346 | -57.8361 | 2026-07-29 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.8 |
| 8de45a6d-0f65-3557-b0f2-359ac878e150 | -20.6025 | -57.2611 | 2026-07-29 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 2ddc3a6c-3269-3f7d-a095-711cdc6841ce | -14.1797 | -51.9147 | 2026-07-29 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d536359c-df4e-38dc-b08f-fe7493a82dd1 | -11.4102 | -46.8473 | 2026-07-29 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2851a3e1-2065-391f-a87c-b042a9f324b0 | -13.3097 | -45.7505 | 2026-07-29 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 217.1 |
| c6f82d3a-5a69-3410-af12-49eb815e7a42 | -20.8346 | -57.8361 | 2026-07-29 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| a3d455e3-8a83-31ec-a855-3a145cb50dda | -14.199 | -51.9122 | 2026-07-29 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 268.3 |
| c5ebd119-44a3-3ab5-a4c6-f2577c11c667 | -12.3292 | -54.0954 | 2026-07-29 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 11e6aca7-363f-35f9-a360-a89985142cb8 | -20.6025 | -57.2611 | 2026-07-29 14:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 680afc8b-f13d-3679-bab4-5b6be8534bbc | -20.5822 | -57.264 | 2026-07-29 14:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 901d39f0-a397-3ef8-9224-e75f514d1934 | -12.3292 | -54.0954 | 2026-07-29 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 889fc80d-fc92-37fe-b7a4-ff33ecc3f72f | -14.1994 | -51.8908 | 2026-07-29 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 1c8d7fc9-1e90-3972-8ce4-1a9af137ccf4 | -14.199 | -51.9122 | 2026-07-29 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 338.7 |
| 529b8c7a-e931-3ef6-b70f-8ed82dc5210f | -6.8708 | -46.0126 | 2026-07-29 15:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2fdb00c8-c9de-351e-8a9e-2c5b04339c48 | -20.8346 | -57.8361 | 2026-07-29 15:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 4964c4e3-8ef8-3a37-be1c-c3f5220517ec | -20.6025 | -57.2611 | 2026-07-29 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e0c92df4-f037-3e9b-a33f-3bdc05b6ff25 | -14.1797 | -51.9147 | 2026-07-29 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 28d780d1-dda6-3948-adc9-cb544142c880 | -20.6021 | -57.2821 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6508b51d-111a-34fd-b8e8-418c5a7d160a | -20.6029 | -57.24 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c1577475-7380-39d6-b90c-01ea37d1a3ca | -14.1797 | -51.9147 | 2026-07-29 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 15206504-6c7f-34a2-9f70-12b3f6cdaed4 | -12.3292 | -54.0954 | 2026-07-29 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ce431a60-9c63-319e-8b66-80f578542f34 | -13.3097 | -45.7505 | 2026-07-29 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9c2a314d-c7cb-3e55-959c-90fdd4022c0d | -20.5822 | -57.264 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 87ec0669-00c2-3b44-889d-9c7f5b4ff066 | -11.5469 | -50.2945 | 2026-07-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cc2c25c8-a125-317e-b6e8-71ec4e2d47f4 | -20.5255 | -57.0621 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 108.6 |
| d0d95c71-3bfd-3948-b9e1-158aa8d7ee5f | -20.5457 | -57.0591 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c9fbbf17-842c-3059-98dc-8d698e838adf | -20.5818 | -57.285 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 14edb9a0-5645-39b5-aee3-ccabd0a6bc16 | -20.8346 | -57.8361 | 2026-07-29 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 22c38941-495b-3a02-aa3f-9d11a7d10a1e | -14.1994 | -51.8908 | 2026-07-29 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 66f8cc64-d1c3-35c7-9da3-88dac1e8c8b3 | -20.5616 | -57.2879 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5fe3b479-59bf-30a2-baf7-90f930fb73c0 | -20.6025 | -57.2611 | 2026-07-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 29317776-6c70-3e71-b11f-a72ec90b8705 | -14.1797 | -51.9147 | 2026-07-29 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a5fc91f0-cf31-3db4-8630-7bc19761b188 | -20.5255 | -57.0621 | 2026-07-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3d572e61-d500-3b7b-89d4-57f799aa3a5a | -6.8708 | -46.0126 | 2026-07-29 15:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b216f8dc-0335-3fb7-9605-f332ae21b1eb | -14.0698 | -53.9475 | 2026-07-29 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d87fd4b8-2506-36ae-879c-34d8ec1ff72c | -20.8346 | -57.8361 | 2026-07-29 15:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 239.0 |
| 40647b58-0f4d-3f2e-8d21-04a9bece8d2b | -20.5457 | -57.0591 | 2026-07-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3c88eabd-ea77-3efb-8735-123e72e73a0c | -11.6224 | -50.3288 | 2026-07-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e8ea09bc-7784-3019-84b5-f90460dfdfd0 | -6.1073 | -47.7495 | 2026-07-29 15:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| eaa413c5-dd76-378d-b452-eb18fd3c2240 | -11.6224 | -50.3288 | 2026-07-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 42a25d02-c411-3c70-830b-52949658aa9c | -18.6396 | -40.9123 | 2026-07-29 15:40:00 | GOES-19 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 141.5 |
| af6a49f1-8082-39d7-9b1e-b4c870f583d0 | -11.6221 | -50.3502 | 2026-07-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 157bb48d-7d42-3510-8938-84f91a5333c4 | -6.1073 | -47.7495 | 2026-07-29 15:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ea78a097-a91f-3439-a119-fb4d7160203c | -11.6224 | -50.3288 | 2026-07-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 0e077694-add0-343a-8c06-4b3e59cf1864 | -14.1797 | -51.9147 | 2026-07-29 15:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |


