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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5147c611-b789-3610-a699-7d3277ce6912 | -12.44288 | -58.48514 | 2026-06-05 07:24:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 23755652-e57b-30d6-abe8-823219bf312d | -12.44009 | -58.47891 | 2026-06-05 07:24:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9f5cbf4c-fb3c-3fd4-a668-3d88803c51e9 | -11.55701 | -52.7841 | 2026-06-05 07:24:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 8b058e30-9398-3312-92f9-cf376fa6b50e | -11.55728 | -52.78949 | 2026-06-05 07:24:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 09e0d6d1-2195-387c-b94d-4ee0cb729a50 | -5.93232 | -43.48212 | 2026-06-05 11:15:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 8cb70a90-7aaf-3cfe-83e8-062316fb830d | -12.51771 | -46.26939 | 2026-06-05 11:15:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 016ed29f-ed23-3527-9f14-c6700f34fd0f | -10.52117 | -42.37152 | 2026-06-05 11:15:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 72e0cdf6-f5da-38cb-8eb6-efdbee9b458b | -6.9795 | -38.13908 | 2026-06-05 11:15:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 17.9 |
| eb5d7a3e-d239-3727-9f7a-7cdcbdf27e28 | -12.51807 | -46.27699 | 2026-06-05 11:15:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 0ea270f2-03e2-3bf6-8912-1c154d08a1d0 | -5.93622 | -43.47687 | 2026-06-05 11:15:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| a1a8388b-24df-3c43-88e6-eec55e059d84 | -10.51889 | -42.38023 | 2026-06-05 11:15:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cd0575ce-1898-3c0d-8683-662b2ccad559 | -9.00576 | -45.75853 | 2026-06-05 11:15:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b4d0679b-791e-3309-962e-36239fb8da7f | -10.9324 | -46.9538 | 2026-06-05 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 02920aed-544b-32a1-b790-6f3239fea857 | -10.9324 | -46.9538 | 2026-06-05 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6a6b6fc6-386a-3eda-ae11-5da570b25989 | -12.7463 | -54.1969 | 2026-06-05 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5d0fa070-01f7-30d5-8437-c172b2243506 | -14.2121 | -57.4098 | 2026-06-05 12:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cfde3152-1353-353d-a3bd-8a17b7318fcd | -12.7463 | -54.1969 | 2026-06-05 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 96fd1679-ff02-3277-a35c-842bb2c9ca60 | -14.2121 | -57.4098 | 2026-06-05 12:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 7bc3b6bd-1570-3ebb-b15f-a1a26a156aaf | -14.2118 | -57.4299 | 2026-06-05 12:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5aa99827-a0a1-332a-8bd6-f457cf2a2881 | -14.2121 | -57.4098 | 2026-06-05 12:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f82a6a8f-6f11-347a-998c-5f9ee72bf554 | -12.7463 | -54.1969 | 2026-06-05 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| bbf52875-a7e1-3215-b42d-2d923e5e4eff | -6.58411 | -51.0726 | 2026-06-05 12:51:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 80dff2b3-3164-3d1f-a657-3261aa7bac7e | -10.03401 | -59.34514 | 2026-06-05 12:51:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| afe08785-448c-31d5-999c-084bafe5cb42 | -10.85566 | -53.73799 | 2026-06-05 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 63c8298e-9db1-3b9e-a7c3-a5c8cfde222b | -9.18161 | -58.05545 | 2026-06-05 12:51:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 82a0d3d0-94de-37d4-b089-8ef69b139770 | -10.8688 | -53.74504 | 2026-06-05 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| de445a07-08b7-3709-af34-5a1c789eb29f | -10.87085 | -53.73959 | 2026-06-05 12:51:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 55a185f2-a61c-3d9d-bef6-f89ab7131c73 | -6.57881 | -51.11473 | 2026-06-05 12:51:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 9e61cba1-b61c-3a19-bce6-59961d720f47 | -11.63449 | -58.24549 | 2026-06-05 12:53:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 117ac52f-59fb-35dc-bf8c-a9ffc5ece8fd | -12.73915 | -54.20201 | 2026-06-05 12:53:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| ad99392f-65e5-34e0-8ff8-e28cad74fcfb | -11.55531 | -52.79925 | 2026-06-05 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| ad0b05fa-0288-397b-93f2-a09425d9907e | -12.44875 | -58.41908 | 2026-06-05 12:53:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| aa150571-78e9-3e4f-ae01-104450a7ea4e | -12.44201 | -58.47308 | 2026-06-05 12:53:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b620826a-c22a-3adb-8429-31e5d8a377d0 | -11.63418 | -55.16941 | 2026-06-05 12:53:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 636fe11a-2bbb-39d2-9507-5364ca62a42f | -14.21572 | -57.42677 | 2026-06-05 12:53:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| ac610e24-6084-367a-b679-f4f60988494f | -11.5769 | -54.57599 | 2026-06-05 12:53:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| b7c01f82-8b2f-3e71-bc76-12ca058f4a58 | -14.02703 | -56.79769 | 2026-06-05 12:53:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 68e9deae-f4cd-30a9-9942-2ba374c08a6e | -12.22168 | -57.28316 | 2026-06-05 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6db97ee7-e2fd-30db-8758-372b9aeec762 | -14.20968 | -57.41957 | 2026-06-05 12:53:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 22710f8e-e67c-393e-bb1b-fc3faf2b6f5d | -12.74072 | -54.19572 | 2026-06-05 12:53:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 9edb6640-faeb-3aab-b1aa-60d69c239dd9 | -13.54911 | -55.25117 | 2026-06-05 12:53:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| dbc45146-dc4e-34c5-8812-8d3705da5178 | -16.60059 | -58.23499 | 2026-06-05 12:53:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| a94ec0bc-7109-39bb-83d5-ae1762fc3b13 | -13.5583 | -55.24544 | 2026-06-05 12:53:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6e5860be-04d9-3b22-a0c6-85714e5d4565 | -12.44032 | -58.48662 | 2026-06-05 12:53:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 146f6010-7bd4-30bc-9708-7447ebaa522e | -14.21772 | -57.40953 | 2026-06-05 12:53:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 4331e38f-899c-3b44-8aa2-0fd35cbb1927 | -12.45043 | -58.40555 | 2026-06-05 12:53:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 6989d516-f11b-34e1-90ef-62de48ededbc | -19.17307 | -55.19088 | 2026-06-05 12:55:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 32.3 |
| 07980a89-881b-3201-9c55-c74491c1119b | -19.17565 | -55.1844 | 2026-06-05 12:55:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 305aec5b-d1a8-3ca8-b2c1-3fef4eefd3e9 | -12.5103 | -46.2863 | 2026-06-05 13:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 463d43e5-f576-311d-90fd-3252b0ffebe2 | -12.7463 | -54.1969 | 2026-06-05 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| cb989aca-1fd1-35a7-8e7f-1bab63d532ec | -9.0172 | -45.7624 | 2026-06-05 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 5bb3374a-8d94-37a1-81c2-c8dafcf3f728 | -14.2121 | -57.4098 | 2026-06-05 13:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1657f22b-a73b-3b9d-87b5-66239055ddc4 | -12.5103 | -46.2863 | 2026-06-05 13:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 8146c945-afb9-3194-b747-876bd17e97ed | -14.2121 | -57.4098 | 2026-06-05 13:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b8a96572-8f52-30e5-bd08-8a4fb0d9f5ff | -12.4473 | -58.4033 | 2026-06-05 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| aaed4d56-58ea-3eda-a641-83e9f83ab41d | -12.5103 | -46.2863 | 2026-06-05 13:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 74816827-e47d-3624-92c2-637f51d736ed | -12.7463 | -54.1969 | 2026-06-05 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 893f369b-bd06-321c-9fcf-e3459ac6358b | -11.9493 | -43.4019 | 2026-06-05 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 3c10e907-a1f1-37c0-8a04-2e9069ab465f | -12.7272 | -54.1988 | 2026-06-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0d3bb07a-42b2-30c5-9539-a3dd41e67703 | -12.4473 | -58.4033 | 2026-06-05 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 273584b0-96bf-3a86-aefb-97535642ce6a | -12.7463 | -54.1969 | 2026-06-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| cface776-fe81-3d54-9d8a-b83dc7de849f | -9.0172 | -45.7624 | 2026-06-05 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8a3dca3c-1647-3de5-81bb-82161b919de1 | -14.2121 | -57.4098 | 2026-06-05 13:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b8e222d0-26e2-3680-be4d-cff5f6c3ffd6 | -14.2118 | -57.4299 | 2026-06-05 13:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e9d254e7-b774-30ff-85cb-ede33b1b902a | -12.7272 | -54.1988 | 2026-06-05 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 83f9e182-597b-3143-824f-36b36253dc90 | -14.2121 | -57.4098 | 2026-06-05 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 3655f39e-df9f-3c85-a35a-6b972bc71545 | -11.0073 | -47.0338 | 2026-06-05 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 422fc72e-e7a0-3876-a18e-2696a32bfce6 | -8.9985 | -45.7418 | 2026-06-05 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a656a27d-7842-39bd-810e-465a62647045 | -14.2118 | -57.4299 | 2026-06-05 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ce3876b5-dc80-3ff4-beea-cb7bb3d4864f | -12.7463 | -54.1969 | 2026-06-05 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| e8406cc5-e6a8-3cdb-971d-1b6b4a1e9909 | -12.4473 | -58.4033 | 2026-06-05 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0f4d2ab8-8961-36ee-a9db-ceeda042dd2d | -14.3983 | -45.5657 | 2026-06-05 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 343903e4-2352-30c8-b5e0-93f30029060c | -10.9882 | -47.0362 | 2026-06-05 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 9cd64345-be4d-33f6-9960-d6cbd2590f56 | -12.4464 | -58.4825 | 2026-06-05 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 173186ae-e3de-3bb9-9078-b5fbfed09a0e | -11.0073 | -47.0338 | 2026-06-05 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| fae97f73-e9df-3e2d-8acf-751c93ad3784 | -14.2118 | -57.4299 | 2026-06-05 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 08c4e8dc-3bd8-31bf-83e4-d56d619b605a | -14.2121 | -57.4098 | 2026-06-05 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| cebd49e4-cd80-3dbf-80c3-45a8df26cc9b | -12.7272 | -54.1988 | 2026-06-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 30cba789-b2b4-3e22-9991-1904cf51e126 | -10.9882 | -47.0362 | 2026-06-05 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 423695ff-fbce-3bab-8972-84fe650a4c95 | -12.4464 | -58.4825 | 2026-06-05 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3711b462-a4bc-3576-b247-33b2fe53ec1b | -14.3983 | -45.5657 | 2026-06-05 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 135e761a-6178-37f8-87cd-fdbcf5df556b | -8.9985 | -45.7418 | 2026-06-05 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6ed9d813-dba1-3328-aa4a-1901dc7cf91c | -12.7463 | -54.1969 | 2026-06-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 6393f139-11b9-31df-98bb-0f0d31683a6d | -12.4473 | -58.4033 | 2026-06-05 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| eeb40dab-d1fd-3171-bb88-9bb3169c96b4 | -11.0073 | -47.0338 | 2026-06-05 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 7d34b8f1-7f0d-3789-ab98-62eefc770bfd | -12.4464 | -58.4825 | 2026-06-05 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 460cb666-2905-39ff-8591-4c9caed50dd7 | -11.6329 | -55.1844 | 2026-06-05 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9b7f7b06-7821-3057-9c14-5516ef7c44a3 | -12.7463 | -54.1969 | 2026-06-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 16f7cf7f-3774-399d-9341-18d831b18789 | -10.8573 | -53.7425 | 2026-06-05 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c7c85cb0-9fd4-3787-b578-fb3ef42b1842 | -8.9985 | -45.7418 | 2026-06-05 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 71505549-e509-3c30-b135-9c416d011b62 | -14.3983 | -45.5657 | 2026-06-05 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1854e6ef-1613-3ff4-9e6d-fca969b88928 | -12.4473 | -58.4033 | 2026-06-05 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7b331af0-fca1-3911-875a-8f18d7842229 | -10.9882 | -47.0362 | 2026-06-05 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 266.9 |
| fd7562bb-c229-30fd-9875-cf2b95a2ed01 | -14.2118 | -57.4299 | 2026-06-05 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| d6114c99-447e-3b32-a431-8311962a0fae | -12.7272 | -54.1988 | 2026-06-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 1780e5b9-8893-36e1-b48e-1c8d6f0ea3a7 | -14.2121 | -57.4098 | 2026-06-05 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 0afb1416-0baa-3dc1-b64e-f0675ddc9d3e | -10.9691 | -47.0387 | 2026-06-05 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 01d8b16e-cd7a-3366-a0f2-6ff279b2fe04 | -10.9324 | -46.9538 | 2026-06-05 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 415cd105-b37a-3d1e-9eec-1780faf844bd | -12.7463 | -54.1969 | 2026-06-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| be8fa850-c6b0-36f8-9a47-884d95bc3771 | -10.9328 | -46.9314 | 2026-06-05 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |


[Clique aqui para ver as próximas entradas](README17.md)
