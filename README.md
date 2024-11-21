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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a50056a-7711-3ff4-892b-ab1907c0031d | -2.5132 | -45.6316 | 2024-11-21 00:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 69e48cb9-d89c-3166-9b13-fd3e4ddb0c70 | -10.1223 | -65.0237 | 2024-11-21 00:00:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| ac97c6eb-9980-372d-bfec-bda2792b6d73 | -4.5614 | -48.0141 | 2024-11-21 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 60e2593b-a188-3174-b348-c6cb7fe09393 | -3.5885 | -46.0609 | 2024-11-21 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 122.6 |
| bb9206b3-626c-3062-a2ac-ba59f57c2bac | -3.5884 | -46.0832 | 2024-11-21 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 6747d0a4-0efd-303a-93c9-93130f9a2e51 | -4.5799 | -48.0349 | 2024-11-21 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 06b073a1-4017-3e3b-9c89-6e9d96599db3 | -3.5513 | -46.0625 | 2024-11-21 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 8bd47501-0927-3a14-b757-c78ea40dab17 | -3.5698 | -46.084 | 2024-11-21 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 374.3 |
| 0bdfa98b-268e-39ad-93c7-065db817a7c0 | -3.5699 | -46.0617 | 2024-11-21 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 292.6 |
| c7560f58-5d6b-3518-9335-0946e7733f05 | -3.374 | -52.4568 | 2024-11-21 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 4d48ded3-1aad-3c15-8f70-b010f54363d3 | -3.2768 | -53.8199 | 2024-11-21 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 71609693-6c13-3ce4-bfe8-fe20a47f6ef8 | -2.5133 | -45.6092 | 2024-11-21 00:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3e21e967-7448-3873-aa22-f1f7a0622ec9 | -4.4899 | -44.7564 | 2024-11-21 00:00:00 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d02af844-fd90-36f2-a19f-3735bc9978d3 | -2.7676 | -52.1045 | 2024-11-21 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ddf36635-75e2-34e4-bbd4-75f57b7494a2 | -3.5512 | -46.0848 | 2024-11-21 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 184a64a6-2cca-3494-8372-b8a4b179736b | -3.3924 | -52.4563 | 2024-11-21 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 173557c5-a5c7-3c57-b081-394e2d3480f6 | -7.3352 | -46.3982 | 2024-11-21 00:00:00 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| ca2b7f8f-2b06-3079-8cb3-285886f7b2e7 | -3.1831 | -54.3247 | 2024-11-21 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 69d62076-dbd8-342c-b2a6-2c3eb959a3b8 | -3.0098 | -51.3143 | 2024-11-21 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 396a170a-7501-3ae5-8b7f-3cd3c68a9f75 | -2.0075 | -54.5292 | 2024-11-21 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 7861583d-dccb-3523-b797-5a9e19e6e129 | -4.3911 | -45.5977 | 2024-11-21 00:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 2177b03b-0438-306e-be3a-73a520631790 | -3.2014 | -54.3243 | 2024-11-21 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 526324b6-57db-3c81-a98c-7074910fb74f | -3.2954 | -49.1841 | 2024-11-21 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 79a3d991-9186-3e96-9cf9-dd1426dc17aa | -4.16 | -43.8818 | 2024-11-21 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| b5f97856-e8e5-3dd7-87f2-6b56141e62d4 | -1.364 | -55.6893 | 2024-11-21 00:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 310ec985-de8d-3cfe-8a4e-9bb62b810605 | -3.3923 | -52.4767 | 2024-11-21 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1916c05e-fe1e-3df1-a4a7-5df5a251c938 | -3.2952 | -53.8194 | 2024-11-21 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2bdaadc0-3248-3416-990a-5143309130b8 | -11.1109 | -54.6204 | 2024-11-21 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 848f8d74-11ca-3eb8-b3b7-c50de5871529 | -2.0259 | -54.5289 | 2024-11-21 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| cb912742-f4d7-3185-9f67-ed387dc1ef03 | -2.7491 | -52.105 | 2024-11-21 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a8c66e11-407e-3bb1-9d19-31245ab1d4bc | -3.2767 | -53.84 | 2024-11-21 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 4028be8a-0020-3f7c-9dc8-871a43ce8e87 | -1.9672 | -48.3865 | 2024-11-21 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 8dd343fb-c593-3dcf-9469-8527ae58b0cf | -4.1413 | -43.8828 | 2024-11-21 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 9363f13a-07db-39ce-8014-bcdbd269ddce | -6.8258 | -46.7737 | 2024-11-21 00:00:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bc1d8353-20bd-39c4-a10b-43db5255b60a | -1.3639 | -55.7091 | 2024-11-21 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c6334a7a-32f8-376b-b014-741dd63dad68 | -3.8021 | -47.7887 | 2024-11-21 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9fa3f9ce-6679-3fa9-8397-572b23015afe | -3.2526 | -50.5574 | 2024-11-21 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 8ce99e66-e287-35a2-a366-1b9924f8f698 | -3.2951 | -53.8395 | 2024-11-21 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 8ac29a90-9719-3a93-b675-310974f8568c | -3.0354 | -49.4688 | 2024-11-21 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 42926443-379e-3ae8-ae1f-31f04ac6f0f6 | -9.4115 | -43.3167 | 2024-11-21 00:00:00 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| b75b4021-22d0-3da7-87cc-b2e2fddc0e61 | -2.7675 | -52.1251 | 2024-11-21 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3dab0ab2-0044-39ae-a566-8bae00a09907 | -10.2304 | -36.7167 | 2024-11-21 00:00:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| ffcc9369-578d-36d5-baf4-34365965b1eb | -4.5986 | -48.0123 | 2024-11-21 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| d9d67eec-09b7-37ff-bb3e-f67bbba477cb | -11.1106 | -54.6408 | 2024-11-21 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| bac3b199-2e13-3763-bd8f-80e6f97863e6 | -1.1833 | -53.7174 | 2024-11-21 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5f666d01-bf23-316e-91c4-367d381a6bc5 | -3.2379 | -45.5615 | 2024-11-21 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| bfc93c48-f3a4-333a-8339-1788e85a97a8 | -4.58 | -48.0132 | 2024-11-21 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 1ff10590-93ac-3c98-b7ce-8be5558b9ea6 | -3.3925 | -52.4358 | 2024-11-21 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a356fb19-e75e-3ff6-9f5e-7d2cd64167dd | -3.57 | -46.04 | 2024-11-21 00:00:00 | MSG-03 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 591f3b9c-18a6-394f-b0c1-60e48f19901e | -3.54 | -46.09 | 2024-11-21 00:00:00 | MSG-03 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7a4abca-d028-3860-9453-ec4ebbbc3b69 | -4.58 | -48.0 | 2024-11-21 00:00:00 | MSG-03 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4235f6ea-4bce-350f-a773-bb875740fe44 | -3.57 | -46.09 | 2024-11-21 00:00:00 | MSG-03 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 161c3903-55ab-36dd-8c0c-2339d20d52ab | -4.6446 | -49.5544 | 2024-11-21 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 45b082ab-997a-3dcb-8df1-8a82e19ac324 | -4.1414 | -43.8597 | 2024-11-21 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 090ba694-ddfd-34e4-b4cb-d89399086423 | -4.1413 | -43.8828 | 2024-11-21 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 729c29dd-dae5-39c6-8ac1-b17d8bc43c56 | -11.1106 | -54.6408 | 2024-11-21 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c8757d20-a2df-31b0-94a0-da2f9dd9ac52 | -4.5799 | -48.0349 | 2024-11-21 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 84a5f0df-145d-31b7-953e-a31e3ad77c5a | -3.1831 | -54.3247 | 2024-11-21 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 63b74142-7c88-306a-bbbe-de46ec85a4ca | -3.0354 | -49.4688 | 2024-11-21 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0d961c5b-5c2f-3b31-8d20-529eb6b6a977 | -3.2954 | -49.1841 | 2024-11-21 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f9436543-f8af-342b-952f-197ca3fcbca0 | -7.3659 | -48.8718 | 2024-11-21 00:10:00 | GOES-16 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d73999c6-f02f-3b98-a84c-fa31522d2082 | -3.3739 | -52.4773 | 2024-11-21 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ee6e0179-4eba-306e-9ccc-5b7d3d7fd7b7 | -2.7491 | -52.105 | 2024-11-21 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ce1e76d1-0435-3c87-a812-4e80d8812adc | -2.0259 | -54.5289 | 2024-11-21 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 392fdb31-430d-3fe2-806f-36bf5629fa6f | -2.7676 | -52.1045 | 2024-11-21 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| a5ef7856-b8d4-3559-bcd5-1d57f216bd07 | -3.2014 | -54.3243 | 2024-11-21 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 6c00dcb8-05ca-3b39-a4d8-9462bc24b40e | -4.16 | -43.8818 | 2024-11-21 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 161bef4d-c778-317c-a60b-1ae3b6b3a003 | -2.7675 | -52.1251 | 2024-11-21 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| c07d973a-b80c-3b8f-8df4-d4ac03581154 | -3.3924 | -52.4563 | 2024-11-21 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| a8e987e4-b1b0-344b-a6fb-f421e3a31162 | -2.0075 | -54.5292 | 2024-11-21 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| abedf13c-016a-31f2-9322-e034b4af50ce | -3.374 | -52.4568 | 2024-11-21 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 994477c2-6c1b-3c11-9fdb-6e10e4472d55 | -4.5986 | -48.0123 | 2024-11-21 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 8b32342e-9daf-3dd1-8c0d-a98b7f1ee530 | -10.1223 | -65.0237 | 2024-11-21 00:10:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e878f6e8-d31c-3b6d-8844-16063e5a6da7 | -3.2767 | -53.84 | 2024-11-21 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 756bc569-4426-3e74-9e23-b9cd10acc43d | -3.2379 | -45.5615 | 2024-11-21 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 34a52a07-8591-3ca4-ad0f-5072c0e9348e | -3.2951 | -53.8395 | 2024-11-21 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 75f3e7d5-753d-328b-a50c-df0e7372e720 | -3.2768 | -53.8199 | 2024-11-21 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 18c948ad-f6e2-3625-91ac-d7122200efa8 | -3.2952 | -53.8194 | 2024-11-21 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 59bcce57-8a72-3b2d-86c9-a1fcc53b089a | -3.2526 | -50.5574 | 2024-11-21 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 17187457-0469-3c91-9461-2683e5ab7ff1 | -1.1833 | -53.7174 | 2024-11-21 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6c7c0880-27cf-3b8c-8f4e-b67301e6382a | -4.58 | -48.0132 | 2024-11-21 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 278.0 |
| 94c7219e-1273-3a5e-8450-d8645407c9fc | -3.5699 | -46.0617 | 2024-11-21 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 189.1 |
| f26f1d89-1b8c-3398-af67-161476611ffa | -3.5698 | -46.084 | 2024-11-21 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 200.7 |
| 96c4f112-b60a-3b6a-af67-3a117bbaf892 | -4.5614 | -48.0141 | 2024-11-21 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| d4d8824e-de60-3163-95ef-964e2061df2b | -4.3911 | -45.5977 | 2024-11-21 00:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ef8f1442-a004-30a1-89a7-0f87b2df0532 | -4.1413 | -43.8828 | 2024-11-21 00:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| f52e9df6-3202-3922-afff-89cdbbdde12c | -2.7491 | -52.105 | 2024-11-21 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| bd4737b5-d19b-39d1-9598-22c6d122740f | -4.16 | -43.8818 | 2024-11-21 00:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 437fe1f9-286a-358c-8ae9-87e35ce23056 | -3.3923 | -52.4767 | 2024-11-21 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b75a8789-1b71-3ea0-8c74-cbe790433420 | -3.2954 | -49.1841 | 2024-11-21 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d98bc910-8e95-384a-8789-69efff59a91a | -3.3924 | -52.4563 | 2024-11-21 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| a38b3c96-0cdf-35cb-b9a7-92228e067cbb | -4.5799 | -48.0349 | 2024-11-21 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 5df57ffa-dd4a-381e-991d-a4b99b67e930 | -4.58 | -48.0132 | 2024-11-21 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 225.1 |
| c7c992e7-f675-356c-9c1f-3d729d1a46bc | -3.2767 | -53.84 | 2024-11-21 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 888cfab1-661e-310a-8d29-6d2664556508 | -2.0259 | -54.5289 | 2024-11-21 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 98764a0a-c7e3-3837-a70f-3a5029049b44 | -6.8258 | -46.7737 | 2024-11-21 00:20:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c05fbb6a-10d3-320f-80bb-0e526a398764 | -4.6446 | -49.5544 | 2024-11-21 00:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f9b12c4e-e96c-3d22-9abb-b94255ce5247 | -3.374 | -52.4568 | 2024-11-21 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| d2bc384c-1906-31dd-821b-38af979a4224 | -3.5699 | -46.0617 | 2024-11-21 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a223de0e-87ec-3eb6-8a8e-357a07dca9bb | -3.1831 | -54.3247 | 2024-11-21 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |


[Clique aqui para ver as próximas entradas](README2.md)
