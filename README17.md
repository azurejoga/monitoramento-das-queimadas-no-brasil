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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16273b2b-1097-3c79-a93c-27f4552fd777 | -16.8096 | -55.9177 | 2024-10-02 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| ed36bed0-93d2-32cb-94f4-d50edf765e2d | -16.8292 | -55.9152 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 4599cb4f-71f8-3bb0-96d6-680bf6e7a913 | -16.8295 | -55.8945 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 154.6 |
| 4c779cd2-a1b7-34af-9507-4fe6e2519bc7 | -16.8299 | -55.8737 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 52b15abb-dd4b-3233-9a1f-cfcbb8e0998f | -16.8234 | -57.4789 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| e6693e82-e7a8-384c-85a0-5a0e89b5dc2a | -16.8488 | -55.9128 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| a4874a99-16be-38e4-8f55-bffc5f0fca52 | -16.8491 | -55.892 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 39dc57b1-f0bf-3d25-810b-164dad506c1e | -16.8386 | -57.7628 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.6 |
| 33ba1427-c202-3dfc-8648-208ccd9b4768 | -16.8695 | -55.848 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| b6fce6c8-becc-3d8b-a6e4-0945f1ef54bf | -16.8698 | -55.8272 | 2024-10-02 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 70cdbbf6-282a-370c-b4f3-eee1e1c14210 | -16.8787 | -57.6971 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| e88ecff3-0e90-3c3c-8212-eff4a911766c | -16.879 | -57.6767 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 60041850-a6f5-38a6-b2e2-b3af7423c81c | -16.898 | -57.7153 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| 6a150e21-bc86-3af6-a412-40578c2e43fd | -16.8983 | -57.6949 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 236.4 |
| ad14b00c-24db-3ab9-a769-6148ea7132b9 | -16.8986 | -57.6744 | 2024-10-02 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| d4de533c-7090-344d-91da-f545d68c68ef | -17.0612 | -56.0931 | 2024-10-02 00:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 3cec033d-f04b-3747-a9ec-d74b9386a907 | -17.1577 | -56.1844 | 2024-10-02 00:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 18691847-7bdc-33a4-8816-7a4a45588cd3 | -17.1581 | -56.1637 | 2024-10-02 00:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 644e0602-72e8-301a-90d5-966daec3ee26 | -17.1971 | -56.1795 | 2024-10-02 00:56:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 6d70fca1-c378-384c-b849-538da747c82a | -17.196 | -56.2417 | 2024-10-02 00:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 73682f24-4406-341b-8606-e19bcd0388a7 | -17.1964 | -56.2209 | 2024-10-02 00:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| e67626e2-1b96-364f-96bb-128ca950cfbb | -17.1967 | -56.2002 | 2024-10-02 00:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| c97b27bf-e3cd-3b8b-8f5f-f8a0684a15b3 | -19.2317 | -46.8687 | 2024-10-02 00:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 603a5577-34d3-35b1-a7fd-6f1d9aa62322 | -19.2323 | -46.8452 | 2024-10-02 00:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 2c728e9e-80e7-37ba-b5cf-029e6eac32f6 | -19.2519 | -46.8641 | 2024-10-02 00:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 8fcc1913-922e-3a11-a5ae-7ceafd276926 | -19.2526 | -46.8406 | 2024-10-02 00:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 8816c76a-788e-396d-a855-2ee8f159b58e | -21.2854 | -47.6277 | 2024-10-02 00:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 7cb3f99c-6e1f-32bc-b128-b46150ae78e0 | -21.2861 | -47.604 | 2024-10-02 00:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 164.4 |
| f5c7384f-5b87-3c88-aca0-f4d1a4b1e542 | -21.306 | -47.6227 | 2024-10-02 00:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 89c4dcdf-e93e-370e-b746-46c335cfa619 | -21.3067 | -47.599 | 2024-10-02 00:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6e9c964c-e77f-3e6b-95a7-9fd614cf47b9 | -21.3456 | -55.6841 | 2024-10-02 00:57:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 195cd69d-c4b8-35fc-a23b-f2b2de3d3647 | -21.6275 | -50.796 | 2024-10-02 00:57:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| a8835b5e-3b33-33cd-8e55-03aa22666a81 | -22.9277 | -43.7243 | 2024-10-02 00:57:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 115.4 |
| f6c85f47-396b-39c6-9a4c-bdaa7cfca4a5 | -22.9006 | -45.1029 | 2024-10-02 00:57:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.1 |
| 53f452e8-42be-336b-8753-34fae488e27e | -22.9014 | -45.0779 | 2024-10-02 00:57:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| f8ca9631-4f91-3267-89c7-b3c460918402 | -23.5075 | -51.1054 | 2024-10-02 00:57:15 | GOES-16 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 103.9 |
| f2e1866b-0fac-3d12-b0a0-744a71eb9cb6 | -13.08 | -51.47 | 2024-10-02 01:04:09 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0bb93b6-668e-3c99-833f-c11581c4a0f5 | -13.08 | -51.41 | 2024-10-02 01:04:09 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 224bb23c-ed4e-35fe-8320-0e7d62d49048 | -13.05 | -51.4 | 2024-10-02 01:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25148e17-223e-3858-8511-b4be31fad5c5 | -3.2136 | -46.7843 | 2024-10-02 01:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 57ce01c8-ba0f-3dab-8aa7-a4d43c05d39f | -5.9786 | -45.3847 | 2024-10-02 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e26674b0-d853-360c-8821-765e4c9d59e1 | -5.9788 | -45.3621 | 2024-10-02 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3f5bb534-24b6-32d7-b5a8-c3b632b2bd6a | -7.1794 | -46.9665 | 2024-10-02 01:05:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e7b33a40-168a-3991-8fb5-b5b63b8b18c1 | -7.1796 | -46.9444 | 2024-10-02 01:05:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 5786207c-06aa-3110-8a32-85fa23dec38f | -7.3792 | -35.248 | 2024-10-02 01:05:47 | GOES-16 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| e3d302c3-003d-3356-aa10-bf695e4a9a06 | -7.7129 | -42.995 | 2024-10-02 01:05:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 733b0da6-9aa9-3079-8cae-c812f1a988b1 | -8.205 | -44.365 | 2024-10-02 01:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e2735204-83ff-3fda-80e3-2a22cc045623 | -8.2053 | -44.3419 | 2024-10-02 01:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 27fe1a1e-94b5-394e-ae41-4ab70fecc360 | -8.2239 | -44.363 | 2024-10-02 01:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d79d3c3f-d790-3582-ab35-be1682bcc2d6 | -8.2242 | -44.3399 | 2024-10-02 01:05:52 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4e15edcf-2411-3993-abae-93e7ef9a4be2 | -8.4643 | -62.7124 | 2024-10-02 01:05:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| df70cb40-c3ad-3b5e-8603-1b06f5d5ad58 | -9.5397 | -62.8195 | 2024-10-02 01:06:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1f8367a3-22fc-3958-b0da-78e6d31a9a86 | -9.5398 | -62.8005 | 2024-10-02 01:06:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cf86f90a-b739-3c71-ade9-49460deee84b | -9.9367 | -64.9179 | 2024-10-02 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 229.3 |
| 188a8622-f9e9-3f22-8e8c-e42ef1a40bea | -9.9368 | -64.8991 | 2024-10-02 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 180.6 |
| f4e149a6-7d6a-3dd4-967d-443e163432d8 | -9.9553 | -64.9172 | 2024-10-02 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 136.4 |
| ec1a8a84-7994-31af-94bf-2888146cd01c | -9.9554 | -64.8984 | 2024-10-02 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 16646dfd-71ec-3aec-a3b0-b07796b47a38 | -10.626 | -55.8752 | 2024-10-02 01:06:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 7c9b2205-b5a0-3521-bcfa-4c70571d03c8 | -10.6995 | -69.3876 | 2024-10-02 01:06:07 | GOES-16 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 084a4212-97d7-3bb7-94a9-44ddd8b9a813 | -11.884 | -43.8142 | 2024-10-02 01:06:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4bf31edb-3159-33ac-8346-e06b076b9c4d | -11.6554 | -65.018 | 2024-10-02 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 20beb7f3-6ece-3c88-8867-bd79d35e5ede | -11.6555 | -64.9991 | 2024-10-02 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0720a99f-57b2-33ba-b47f-b8ad0c2d60f0 | -11.6556 | -64.9802 | 2024-10-02 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 04887936-26b0-3ade-8fc4-8ba107578c70 | -11.6742 | -65.0172 | 2024-10-02 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b49cf16c-c8a2-34bb-b153-2724a5393f5e | -11.6743 | -64.9983 | 2024-10-02 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| da1e68ef-7edf-324a-8735-c67342456561 | -12.4433 | -43.7242 | 2024-10-02 01:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| acfe17f6-5741-37eb-b998-17a0e6afa17d | -12.2754 | -47.6473 | 2024-10-02 01:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8f9bd8be-1018-337d-9bc1-f42b53e72ed4 | -12.2946 | -47.6446 | 2024-10-02 01:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 99aed73d-75da-3b3b-a4f5-aba3ca5f78ee | -12.6484 | -63.1214 | 2024-10-02 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 80370de5-faea-3874-8cf8-a34d82205973 | -12.6486 | -63.1022 | 2024-10-02 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 27836cca-cb4a-335a-a0a1-5bbdb81d2f32 | -12.7054 | -63.0798 | 2024-10-02 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1cb64b2d-39ff-324a-af7f-d965ec46347b | -12.8593 | -62.7826 | 2024-10-02 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0a7bf582-3e6d-3ded-9493-379bc17accf0 | -12.8782 | -62.7815 | 2024-10-02 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c2bf86c3-66ba-3d8e-b34c-691a3b9ba86d | -12.9167 | -62.7022 | 2024-10-02 01:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a602f8f3-cedd-31f9-a87a-8ba1e52d0764 | -12.9357 | -62.701 | 2024-10-02 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 8055aa34-82e7-3a15-bab8-acbb512fb1b3 | -12.9358 | -62.6818 | 2024-10-02 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 131.0 |
| b0671ea0-3fac-39eb-9194-9ca32fd12fa1 | -12.9546 | -62.6999 | 2024-10-02 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 206.2 |
| 8809344d-2b3a-330d-bde3-33b9eb22ac7f | -12.9548 | -62.6806 | 2024-10-02 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 214.8 |
| d7ba8ae1-aa00-36e8-ae20-e72175dd8516 | -13.5965 | -51.1367 | 2024-10-02 01:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 609884bf-67f2-345c-beb7-4fbca8446373 | -15.095 | -49.49 | 2024-10-02 01:06:31 | GOES-16 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 51768299-c908-39c5-a262-4de9aa2862dc | -15.1197 | -55.8307 | 2024-10-02 01:06:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9b5fac76-25d8-3adc-809f-553655b0b169 | -15.139 | -55.8285 | 2024-10-02 01:06:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8c125735-7fb9-3d09-84d4-d23d2568fb95 | -15.748 | -49.9586 | 2024-10-02 01:06:34 | GOES-16 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6afc025e-72d2-38ed-a59f-25dfd35d790f | -15.8933 | -57.1754 | 2024-10-02 01:06:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| ba66223c-981b-3c79-bf59-0c8643c9626b | -16.1086 | -53.5427 | 2024-10-02 01:06:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 9bcfaddb-d9e6-3b8d-ac68-c8273e45d790 | -16.109 | -53.5215 | 2024-10-02 01:06:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 5a0dc5cb-66a9-3281-80d8-c1a40e5152ee | -16.4533 | -57.4392 | 2024-10-02 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.9 |
| 6d1ceb4c-a2bb-323c-9dd0-20b412fa7547 | -16.4536 | -57.4188 | 2024-10-02 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 0be247b4-9e51-34c1-ba8f-5d89131a2b4f | -16.6691 | -57.3536 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 4f1914fe-9852-3198-9325-22b6a4b4895c | -16.6884 | -57.3718 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 34f57033-b598-3bda-ae40-6e6f315c8b1c | -16.6887 | -57.3513 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.2 |
| d4779206-e3bd-3a83-8ff8-0cb57e1a3e64 | -16.689 | -57.3309 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 3671c174-73d3-3e63-a870-f352f27923ea | -16.7063 | -57.4718 | 2024-10-02 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 461664d7-a195-38d0-bb06-f8b720875801 | -16.7082 | -57.3491 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 48c1d0a1-8cc5-310e-a82e-25232b79800c | -16.7086 | -57.3286 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| e4ffcb89-a055-3ff0-bf3d-5010e8a83e29 | -16.7265 | -57.4287 | 2024-10-02 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| cf1c3d94-18b0-3f43-a411-33d010d526c8 | -16.7452 | -57.4878 | 2024-10-02 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 5cf8a1de-daaf-3480-802a-6ee63ffebfd8 | -16.7461 | -57.4265 | 2024-10-02 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| b1ac7575-6a88-30f5-9312-e8a9b83fdb2c | -16.7663 | -57.3833 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| d08970ee-f7af-35f6-9b27-1d2c3c82e43b | -16.7666 | -57.3628 | 2024-10-02 01:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |


[Clique aqui para ver as próximas entradas](README18.md)
