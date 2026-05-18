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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e4f0a96-5485-351e-8efd-1861041cad25 | -12.06725 | -45.28027 | 2026-05-18 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c290224-1a74-39fb-b0f0-40ee85e844d9 | -9.32084 | -50.40159 | 2026-05-18 05:01:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8ad03b2-2869-3c07-b560-32371d84aa7b | -12.06162 | -45.28283 | 2026-05-18 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02831bb1-bad1-3c1a-b6c3-07a8bc30bc22 | -11.44142 | -54.08916 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb566809-895b-33d2-a3e2-ef5969f33ded | -11.88431 | -43.80878 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51602c50-8e00-3709-a818-9a667102d1ac | -11.11255 | -49.73132 | 2026-05-18 05:01:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fabf468e-bbb3-35ab-ade0-9cbf825e2161 | -11.44696 | -54.0973 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2a979b50-fd87-3eb4-92f3-01089a2cc097 | -11.45085 | -54.09431 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aa4d065-2bbb-3f1f-b484-817fa0b12c82 | -11.45141 | -54.09079 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0165ea5-e770-3c56-b54b-9eaf6598506c | -11.44307 | -54.10028 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de1b5bc7-a506-3e88-baf2-b8c88819618a | -11.44752 | -54.09377 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd0cd097-3ba7-311e-9395-2d5292d79c6b | -14.07522 | -53.44442 | 2026-05-18 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f46556ce-ba49-3822-9607-64d3daecfda2 | -14.39782 | -44.37087 | 2026-05-18 05:01:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d130d6d-d612-38ca-9699-21e33feede76 | -11.8848 | -43.80484 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f65acf4-26b2-3a65-a6b8-35ff636c241b | -8.47021 | -51.4804 | 2026-05-18 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c860d7ed-669b-3366-b2c2-9d2790ee7f49 | -12.06685 | -45.28348 | 2026-05-18 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e31163b3-d376-3271-b2e0-6634345cd318 | -10.91289 | -54.11814 | 2026-05-18 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e3c3317-e7c4-313e-af73-5f40d41ebdd5 | -12.44484 | -54.47742 | 2026-05-18 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82288bfe-6e4e-38b1-b841-86e3af54ae59 | -11.44086 | -54.09268 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f90ddfc0-5da9-33c7-8d66-163236416d92 | -11.87989 | -43.80827 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5503bbfd-b35c-34fd-8ed6-505ecc336af0 | -12.44873 | -54.47443 | 2026-05-18 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5890f0c-e0ad-31e3-8699-a88d86c40a56 | -12.05641 | -45.28212 | 2026-05-18 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6600fc8-4a62-3eb7-a3ed-d98877a3a7cb | -11.45029 | -54.09784 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df711dae-ef5c-3db7-a0bb-5b942eafee6c | -12.4454 | -54.47388 | 2026-05-18 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37b2786c-6662-3782-ac58-1d2f72a11465 | -11.44808 | -54.09024 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32f7caf8-dcd9-3343-878d-0bf21b99069b | -14.07915 | -53.44132 | 2026-05-18 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eeedf90-a19e-319e-afdf-52868a7dfd76 | -10.91566 | -54.1222 | 2026-05-18 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff2d41c0-602e-3af7-b655-c6f51fe363ec | -11.44475 | -54.0897 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3b601b9-73c9-3ea7-8d1d-47519ece54af | -11.88036 | -43.80431 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5b6630d-d441-3eaa-82a5-490977aaa6ac | -11.4342 | -54.09159 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba6220f0-9747-3473-b0b5-569aae407501 | -11.84173 | -43.96296 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80cfbedd-7ad1-3b03-be2b-444dd0b3f193 | -10.40857 | -44.94026 | 2026-05-18 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 343eea7d-0174-3f78-bb6a-fccac2b46b6b | -12.06203 | -45.27959 | 2026-05-18 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 803263c5-21cc-328c-a431-47afe01cb5b1 | -12.45206 | -54.47498 | 2026-05-18 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d7216b-28a6-3c72-ab18-87cde5a7c4f0 | -11.44419 | -54.09323 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1f77815-6f45-38ca-8f61-88ce16e89f7c | -11.44363 | -54.09675 | 2026-05-18 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f2cf4f7c-b977-3112-91df-e7af04268982 | -11.84124 | -43.96682 | 2026-05-18 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f148659-0829-306e-977f-f563c952f973 | 2.94843 | -60.25553 | 2026-05-18 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45fb5158-9de4-341d-8bfb-b48ecb4eec62 | -2.14379 | -53.64474 | 2026-05-18 05:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17376f9-2eb0-335e-99b3-f4db2db73955 | -10.90893 | -54.12175 | 2026-05-18 05:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f36756bc-d328-3526-822d-3df3e3633730 | -11.44594 | -54.09834 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93f53b19-a58e-3761-ac57-af235487d724 | -11.44648 | -54.09431 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34228e9e-a6f3-345a-80ee-afa46a7705d6 | -11.44276 | -54.08968 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c252703-bb68-3ad0-a4f2-619e49ad619c | -11.44167 | -54.09776 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb5eeb84-520e-3417-954d-334a558baf6e | -11.47771 | -52.91507 | 2026-05-18 05:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911bcbab-a56f-3ea0-b8d8-ca3965fddb5b | -10.03836 | -51.68491 | 2026-05-18 05:21:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0167ae31-ecc2-37dd-b15f-42c802454a42 | -12.44986 | -54.47432 | 2026-05-18 05:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 218e6bcb-895a-3c29-8acf-769fbe959cd6 | -10.91316 | -54.12238 | 2026-05-18 05:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0e9405c-005c-389e-b03c-d2991b2783d1 | -11.44539 | -54.10234 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237e1f37-cf2b-3cb4-95dd-cd1aa9b5f04a | -11.30826 | -54.04033 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dfbac03-6209-3ec3-9126-e901ef431e02 | -11.44221 | -54.09372 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36b2f20e-8db7-38fb-bf0a-9241496f795d | -11.44703 | -54.09027 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 124b6d46-6060-3f02-b405-e0636ea4bdbf | -11.79905 | -57.35743 | 2026-05-18 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52497054-b05c-375e-9c03-ed36026c91f3 | -11.4502 | -54.09892 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbbfa327-0e73-3c3d-9e56-a18094acbbd9 | -11.4513 | -54.09084 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42c23aed-6d4a-3fff-b848-7b2c54e5e9a6 | -10.9137 | -54.11846 | 2026-05-18 05:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd012c1c-314f-33ec-8ca7-b1835c24e004 | -12.44548 | -54.4748 | 2026-05-18 05:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15b0ad15-e8e8-3557-b9e9-d062e5d3420b | -11.47876 | -52.91379 | 2026-05-18 05:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b232a1d3-b0ae-3ed7-9ed2-18809f6c327a | -11.45075 | -54.09489 | 2026-05-18 05:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f32850d-05d7-3ea8-83ee-fe98d1b501e7 | -12.4497 | -54.47536 | 2026-05-18 05:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e737d6-5464-3d2d-82d1-7e219e2f2fbb | -14.08134 | -53.43962 | 2026-05-18 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca601cdb-f896-314d-8399-12142a7140bd | -14.0761 | -53.44383 | 2026-05-18 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b8ff69-d81d-35e7-837f-36a58f8fe47b | -11.45053 | -54.09079 | 2026-05-18 07:26:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 9e4f2436-c914-356e-8166-3c5c3dbe928a | -8.886 | -45.6861 | 2026-05-18 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 8a560f40-b21d-3cd9-b98b-ed1edf553d46 | -10.6467 | -42.3141 | 2026-05-18 11:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 27871ad9-db3a-3aff-92a6-a80d794d2f03 | -8.886 | -45.6861 | 2026-05-18 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 616974e4-6938-3a39-b1bc-26e01ef02c75 | -10.6467 | -42.3141 | 2026-05-18 11:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 176.1 |
| 84f48627-d31b-3bbd-82a8-353153bc3a56 | -10.6467 | -42.3141 | 2026-05-18 12:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 219.8 |
| cfa4bfc9-dcf9-3295-acd0-08c90e5e4d00 | -8.886 | -45.6861 | 2026-05-18 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 235260a3-7002-35f4-96b3-81469996fbf9 | -10.6467 | -42.3141 | 2026-05-18 12:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 275.4 |
| 8b1a7e4f-abb6-371b-9a13-5bf11b783c36 | -8.886 | -45.6861 | 2026-05-18 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| fd3ce0ed-054e-3b1b-a592-c42014c90646 | -10.6467 | -42.3141 | 2026-05-18 12:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 271.0 |
| 81ef4fc7-a981-3988-b554-aee098df27b1 | -8.886 | -45.6861 | 2026-05-18 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 9d70a75e-f221-31ab-bb6f-f0e9418dfdcc | -10.6467 | -42.3141 | 2026-05-18 12:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 331.7 |
| fd8bf1cc-a6e8-3961-889c-309d3428acb9 | -8.886 | -45.6861 | 2026-05-18 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1467cece-5a9f-3d9b-8124-047480ce4312 | -11.44974 | -54.10061 | 2026-05-18 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 2e495b2d-0f04-372f-b060-4c1700a79091 | -8.54266 | -51.57087 | 2026-05-18 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| f93eca75-a197-33a4-9c67-820013f2bba2 | -11.4514 | -54.08783 | 2026-05-18 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 60316ac3-c347-3778-aaf2-ba86be61bc25 | -10.0927 | -47.9967 | 2026-05-18 12:36:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 370f5e6a-a5f4-368c-9e82-906ce7fb29c8 | -8.54042 | -51.58869 | 2026-05-18 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e0e93225-bd3a-39f6-bfff-e14c3df26572 | -12.55514 | -54.6173 | 2026-05-18 12:36:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2cd1e7d1-5027-393b-91de-fcd3755d3d85 | -11.37181 | -52.73814 | 2026-05-18 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b2c25ba0-390b-3d12-9c00-cad38883a71e | -10.0886 | -48.03266 | 2026-05-18 12:36:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ff0cea16-daf0-39c9-a587-a58c92096d82 | -10.09829 | -48.0042 | 2026-05-18 12:36:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 4845addd-ae3e-3e3a-a81c-e3cc1426bc3f | -13.68048 | -52.91502 | 2026-05-18 12:36:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a1e48332-b7f2-3297-ace3-d56b9b7a976f | -9.4352 | -50.69776 | 2026-05-18 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0d1e3ab8-2d56-30ad-977d-9f5372af5695 | -8.886 | -45.6861 | 2026-05-18 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| f7f9785d-0b4e-32a0-afe3-f85d8c0fb668 | -10.6467 | -42.3141 | 2026-05-18 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 340.5 |
| 07df9f79-73a3-38d1-85fd-b816011d5855 | -31.3959 | -53.7119 | 2026-05-18 12:42:00 | TERRA_M-T | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 73.3 |
| 5066c5be-f577-38f1-91b7-4ee706b76bc4 | -8.886 | -45.6861 | 2026-05-18 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 120fc41a-d991-3687-90a1-df8c915ed401 | -10.6467 | -42.3141 | 2026-05-18 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 344.4 |
| e27728ed-b59f-3eea-ac11-412754b5e816 | -8.886 | -45.6861 | 2026-05-18 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 0e0fbde6-0c14-39a6-a449-42f6b78ee825 | -10.6467 | -42.3141 | 2026-05-18 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 307.2 |
| c666f4bc-9583-376f-8f60-92e90cdfbc06 | -8.886 | -45.6861 | 2026-05-18 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 638ab59a-1639-3ee2-a199-9419dd85354b | -8.886 | -45.6861 | 2026-05-18 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 952f8cd3-5656-3708-8048-9e3ccd11ad0b | -8.886 | -45.6861 | 2026-05-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 740e2755-0c69-30cd-b7be-50661bfcba7c | -8.886 | -45.6861 | 2026-05-18 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f468e29a-0974-31d7-a739-c55a7b12493c | -8.886 | -45.6861 | 2026-05-18 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 1a5de0ad-979a-343c-9424-9deef32a6ed0 | -11.616 | -47.089 | 2026-05-18 14:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ab397d19-5dd3-3d08-b507-f8de4d4daada | -10.1014 | -48.0056 | 2026-05-18 14:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |


[Clique aqui para ver as próximas entradas](README3.md)
