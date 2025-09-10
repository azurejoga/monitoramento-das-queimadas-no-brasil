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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf38235b-d67c-310f-ba0a-c6aaa7c6cbf0 | -6.2595 | -43.4129 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3defd791-a5b5-3c65-a081-6a5c669dc7ab | -9.0579 | -46.9688 | 2025-09-10 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9f33499b-804c-3b8b-8ac2-91a1e3411ef3 | -12.1889 | -50.6267 | 2025-09-10 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| bdc87dd5-f638-3d84-b2f0-67a7cbc24075 | -10.1467 | -46.1747 | 2025-09-10 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dddb244d-9e02-30c0-a6ca-3b848a64860d | -11.4515 | -50.3268 | 2025-09-10 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 2f17095e-5928-3230-848e-a2405718ef29 | -14.6658 | -44.0379 | 2025-09-10 12:50:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 25b60f8a-fe87-36a1-bbba-efc43e1e5d1c | -5.6788 | -43.3425 | 2025-09-10 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 43c3b817-fba2-30a3-96ce-6f2c2ee1e7bf | -11.4469 | -43.5988 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4d891cee-d5aa-3904-96bb-a1307ca7800d | -8.0416 | -48.6656 | 2025-09-10 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 118.4 |
| c9aa4781-b0f7-382a-aab0-f80fbdf7ea15 | -6.2407 | -43.4144 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 491eed7b-fbeb-3c3f-9eb0-98c73d41c807 | -11.446 | -43.6461 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e57f57cc-3488-3166-98f8-52009c490d27 | -7.5033 | -48.2334 | 2025-09-10 13:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 0f39c4ce-08c3-301d-ac92-7f1da0356c3e | -11.9535 | -51.081 | 2025-09-10 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 8bb4a327-42f6-3d1f-aaf3-488abe49b1a9 | -12.0495 | -51.0274 | 2025-09-10 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 293.0 |
| 0da99d87-3c6f-3b22-800e-995a59cc0d54 | -12.0304 | -51.0296 | 2025-09-10 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 88871bca-8a6e-3eb3-bfa9-45af007ed2ec | -8.721 | -45.3181 | 2025-09-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 5d3e5650-0838-3c11-9428-d22f10b5642d | -7.5035 | -48.2116 | 2025-09-10 13:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 1f37d461-1bef-3fa0-893e-3c7b15a520d1 | -11.4456 | -43.6697 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 9f6f35aa-96a9-3027-ba84-12bd7075f088 | -11.3905 | -43.5365 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| cfc17db1-3b50-3b10-b45e-8afd351bd7c2 | -6.8519 | -47.9361 | 2025-09-10 13:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 19f1c7aa-67c9-3b1d-b571-c3eb81240961 | -11.4515 | -50.3268 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 5efcba03-a15e-369f-a5f2-efa861e4e697 | -7.4639 | -44.9433 | 2025-09-10 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 148.2 |
| e8ddb431-40f7-36e3-b5e9-cbd1545ae81c | -11.1245 | -52.0359 | 2025-09-10 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 95babbb7-ae38-3e69-89ad-6f13f9d7c6a7 | -11.4705 | -50.3247 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 79e5d6c7-e21f-381e-9962-26d2b454e74e | -16.4573 | -50.6773 | 2025-09-10 13:00:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 35303c31-e581-3409-b318-0013ab925aa2 | -8.6776 | -45.7536 | 2025-09-10 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5ce1d485-2ee0-3334-bce4-53c848e51bd7 | -5.6788 | -43.3425 | 2025-09-10 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3eb9ec0c-d05e-3b17-aaf9-bbef464a376d | -9.3437 | -46.7603 | 2025-09-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f9b70876-5224-3318-b31a-18d1defeeae9 | -12.0307 | -51.0083 | 2025-09-10 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 0f07346c-e63a-3eea-ad1c-baba68bffda3 | -6.871 | -47.8911 | 2025-09-10 13:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a28b9d0a-2bb2-3be1-8eb7-e10560af06ad | -8.0794 | -48.6407 | 2025-09-10 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 287.0 |
| 033df268-7e3f-33f1-9e2d-ff82f21a440a | -9.8263 | -46.0549 | 2025-09-10 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 75a4556d-6896-3e82-8033-b7ddbc4cdd31 | -16.4577 | -50.6554 | 2025-09-10 13:00:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a12a9c89-214c-3a64-8ae0-26bc605aec20 | -11.4652 | -43.6432 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 941d95df-f7a9-33c2-88bd-7966dab7a198 | -8.49 | -45.6826 | 2025-09-10 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 53437a55-8c8f-33b2-b000-fa33d0fe9e84 | -7.4845 | -48.2349 | 2025-09-10 13:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 286.9 |
| afd5582d-e02e-3953-a28c-d6dc0c6dd0a1 | -11.1247 | -52.0149 | 2025-09-10 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| f07ce7bc-697f-3550-94db-9618b913fafe | -9.0579 | -46.9688 | 2025-09-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1a744880-20cb-3440-aa88-a026870014b4 | -5.2076 | -43.7019 | 2025-09-10 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4b6dc5fd-4fe1-357f-b6f8-76a9c215bbf5 | -12.1885 | -50.6482 | 2025-09-10 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 5c3769e6-d1f1-3da6-a23c-8a712b1cb84e | -10.1467 | -46.1747 | 2025-09-10 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 10e858d5-9fcf-39d7-aeb3-b2d8dc7afa17 | -11.4657 | -43.6195 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 672d1863-af36-367e-86b0-8b2fd2e924cc | -9.0074 | -49.5278 | 2025-09-10 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fb378089-87e7-3205-8e2b-9f4888bb588a | -8.0606 | -48.6423 | 2025-09-10 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 116.9 |
| deecffc4-e227-3dac-b239-5ea6a041c17b | -6.8521 | -47.9143 | 2025-09-10 13:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 460856c3-8db0-3615-83d1-c80ef1e5de62 | -11.4512 | -50.3483 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| f0824aa8-90db-37fd-8546-1a974c0bfac2 | -8.4903 | -45.66 | 2025-09-10 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a6178f5c-bb2d-3d95-a396-5eb275a8ea10 | -15.1021 | -50.1249 | 2025-09-10 13:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 0934b159-5eaa-34f2-868f-5bd263f5c17e | -9.0132 | -46.0563 | 2025-09-10 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 5acc9b6c-4c71-3872-a22b-9f1c3e851ebe | -9.1142 | -46.9851 | 2025-09-10 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 66c49598-cd3c-37a5-ae5d-c5a49e360cbd | -11.507 | -50.4276 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| b19554fb-d31d-3e60-bcde-54767403281f | -11.4452 | -43.6934 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 154a59e4-7cea-341d-b85e-5664d29c0493 | -11.488 | -50.4298 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 89031aee-98f9-39c0-97f8-5f86200e33e9 | -9.0768 | -46.9668 | 2025-09-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 16ab9647-f374-322f-9bca-9b81ebfeeafe | -6.2595 | -43.4129 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 3223eb24-e944-32d4-89dc-b1efefa8df68 | -12.1889 | -50.6267 | 2025-09-10 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 6d1b6238-ce2b-36ff-8fc4-3517f71a087d | -11.4702 | -50.3461 | 2025-09-10 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 1046de0e-206f-3de0-8dab-094d9bc64294 | -8.0796 | -48.619 | 2025-09-10 13:00:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 75d807c0-5ab5-3aec-a257-ba0998bd27f3 | -11.4097 | -43.5336 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| baf741ab-6420-3ccd-9ebc-4c5b98213624 | -11.4465 | -43.6224 | 2025-09-10 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 5033af34-a6ab-3c42-af9f-b47618000bfc | -14.907 | -55.8546 | 2025-09-10 13:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f9a447e5-c120-3fd5-8057-e9960b72a9c4 | -12.1885 | -50.6482 | 2025-09-10 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 4869c93f-839c-3f09-bdba-57b81212c836 | -8.721 | -45.3181 | 2025-09-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4b646470-ec27-38ea-9424-8c5e28b6f877 | -10.3885 | -50.5264 | 2025-09-10 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0d1403db-0110-3079-9168-406d4e2b0de6 | -16.4577 | -50.6554 | 2025-09-10 13:10:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 762822cd-3f1b-3ec8-889c-8e3189c4b431 | -16.4769 | -50.6741 | 2025-09-10 13:10:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 95498028-9d8e-3bb0-b495-4f2d60052d3d | -14.7536 | -45.339 | 2025-09-10 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 455a91d3-4862-3539-9024-4031bfd14cb5 | -8.0416 | -48.6656 | 2025-09-10 13:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 115.7 |
| a12b543f-341e-3535-b108-2ffad2a67e8f | -9.6821 | -46.8791 | 2025-09-10 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6c01a2b2-f42d-33d4-b081-a38ca2e39b4e | -11.507 | -50.4276 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 241.5 |
| 9d3a444e-b425-351d-89a2-7aa65c29db72 | -9.8263 | -46.0549 | 2025-09-10 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5da3b8ec-b2f0-3f29-8b79-6ee0b9c745e1 | -8.0414 | -48.6873 | 2025-09-10 13:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 101.8 |
| fdf84865-7503-3098-8c1d-28afa1c59ad2 | -11.9535 | -51.081 | 2025-09-10 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c5d1c57c-939c-3aac-a5ed-d0b435726147 | -15.6745 | -53.8745 | 2025-09-10 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 67963335-697b-3fb0-ab21-653563d5a19e | -11.4469 | -43.5988 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 178d39ec-4bf8-3f3d-ad8f-45a1587acde7 | -14.5125 | -53.9367 | 2025-09-10 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b5d2bf52-f64d-3638-95a1-ffa28f258aa8 | -10.3882 | -50.5477 | 2025-09-10 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 40990a26-dc18-3f69-ab48-aeb4ae6b77dd | -10.1467 | -46.1747 | 2025-09-10 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 731b0e21-0f28-3699-b2d0-6aff4440f0b6 | -11.4648 | -43.6668 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 52877575-126a-314d-9535-b1ed62911c94 | -8.0794 | -48.6407 | 2025-09-10 13:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 312.9 |
| bfb87f55-b0a4-31b0-b9c2-2b34b09616ac | -8.4903 | -45.66 | 2025-09-10 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b1a13989-221a-3222-81d2-36e445ee1885 | -9.0579 | -46.9688 | 2025-09-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e919af05-5de1-327b-ae50-48b9afe2a4ec | -11.4657 | -43.6195 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 54856ea0-97f1-3549-b224-10a271f188bf | -5.6788 | -43.3425 | 2025-09-10 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a6b60ec4-717f-3705-9ee8-75a6c2a01212 | -11.9345 | -51.0831 | 2025-09-10 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| cd47180d-6012-3f66-ad69-4474badff655 | -7.4845 | -48.2349 | 2025-09-10 13:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 8587103d-d059-36e9-a132-275035e3660b | -6.8519 | -47.9361 | 2025-09-10 13:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| f4abc827-43ed-3897-8271-2df2ad868b1f | -11.1247 | -52.0149 | 2025-09-10 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 525d8ae0-d64d-3482-ad62-d4571231922c | -6.2597 | -43.3895 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1079f9f2-3930-32ac-8b19-50d968a8d963 | -8.49 | -45.6826 | 2025-09-10 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 5f35f5d9-d0a4-30fd-9a0a-29bf9ecbd1d5 | -6.8521 | -47.9143 | 2025-09-10 13:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| e4d429f1-ccb2-364c-a6ba-94dfc56afa1e | -9.0132 | -46.0563 | 2025-09-10 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 43e67cc5-2f94-3a89-ac9b-55e45ce2bbd1 | -5.5697 | -45.1198 | 2025-09-10 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5b5bcc6c-38a0-3b57-b330-d8be411acabd | -11.4702 | -50.3461 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d079a8b8-4a88-3540-9249-d7f55081ab52 | -6.8523 | -47.8925 | 2025-09-10 13:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f31d598f-b822-3a5b-9e79-c006babb34ea | -16.5298 | -55.1225 | 2025-09-10 13:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| cb17c9d8-3f67-3160-8a8f-04498ac3f8bc | -7.5033 | -48.2334 | 2025-09-10 13:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 64e5a71f-bc2f-3093-bea7-7ba78f65b23c | -9.0768 | -46.9668 | 2025-09-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 426983fc-c72b-3522-a425-c9f1540873ee | -13.1367 | -54.9171 | 2025-09-10 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 314287d9-ba03-3ddc-8bf3-45a05134ac59 | -14.5122 | -53.9576 | 2025-09-10 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |


[Clique aqui para ver as próximas entradas](README109.md)
