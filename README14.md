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
| 1c209c33-d6e0-3e6c-a59c-680fcfe20fc6 | -2.27453 | -48.56893 | 2025-07-23 04:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b561284f-9a3c-35b0-899d-e9abdd2463cb | -3.18545 | -49.45257 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d75fc9cd-ec11-3255-9459-b61edf4ae230 | -4.77935 | -45.33826 | 2025-07-23 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a15a9829-2ed7-3bd3-a4ec-fe945825c513 | -5.67209 | -43.65976 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93468568-2896-3bd2-a88a-ed2d7955efc5 | -3.16818 | -49.46398 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 169263ee-351a-326b-92f8-3cdc7ebb3008 | -3.75047 | -49.04854 | 2025-07-23 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c76f50cf-02f3-3155-9368-ce34e13cd89d | -3.17618 | -49.43703 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b444d833-152e-300f-b215-7199dae3486e | -3.03662 | -47.85783 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edb28792-76fe-3899-b5d6-f1ad677e5b90 | -3.17407 | -49.45087 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91236270-8de1-3023-9f0e-b582e776eb9e | -3.18615 | -49.44799 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49559d63-549d-3170-a968-b03ef67a8599 | -3.16749 | -49.46851 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ba904b-bf9d-3e0e-ad76-c35694a1d50b | -3.18095 | -49.45657 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0ccbdbd-1bfe-35a9-8305-aed937de0387 | -3.74655 | -49.04798 | 2025-07-23 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0adbbf6d-a059-397d-8f74-ad3f3296bd54 | -5.48112 | -42.14984 | 2025-07-23 04:57:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d476ad0e-d16b-3e92-b75f-e234693f3b7a | -3.18306 | -49.44282 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fae926a-3b70-3ed6-b998-922c688c8b1b | -4.05007 | -42.51776 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 98508f2e-b023-341b-97c6-47e91d121c46 | -3.17547 | -49.44166 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f077e5d-ef9e-33e7-9c78-f981760be518 | -5.47548 | -42.14371 | 2025-07-23 04:57:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dfae4a5f-bfa7-36ef-8718-b584facb4be9 | -3.03465 | -49.42715 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6a1353c-30e2-3c84-8d2c-fbb3f06d5bdb | -3.1613 | -49.45828 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d22f156-a958-3ea8-a111-2a69a7e33da4 | -4.30486 | -48.10135 | 2025-07-23 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c3a57f-3bfd-36be-abdb-5240a1c0cec7 | -2.39096 | -47.62977 | 2025-07-23 04:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72631621-0e36-3735-b9d0-ac57dcf9f0fd | -4.30061 | -48.10184 | 2025-07-23 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6fe8247-1bbb-3bc9-84c3-ab58d9ac0198 | -3.17856 | -49.44685 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d24af10c-7950-393e-b987-01639fb71461 | -3.17998 | -49.43762 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aa472fc-c724-342d-8a28-8a585fc62e1d | -4.04396 | -42.5168 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 469d9c49-6721-309b-9655-4c43dadc3994 | -4.30481 | -48.10246 | 2025-07-23 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3828a626-4f87-313d-94ee-a5aa7007c3c3 | -3.16199 | -49.45372 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c458002e-d7c7-37e7-a0c8-93bb32073564 | -5.72527 | -44.50593 | 2025-07-23 04:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5496b1b3-415f-37aa-909e-a27a7d0af03b | -5.68856 | -43.66916 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9406b4bb-b1e2-3cb5-aa53-6bb26bf3083f | -5.6715 | -43.6639 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d56e5377-8109-3969-a48b-610eac542b50 | -4.04942 | -42.52234 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 17b22ddf-bc04-3ab6-b922-4d7787239b3e | -3.75841 | -52.66489 | 2025-07-23 04:57:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddce42cc-c87a-32bc-812c-4afa4846b985 | -3.32259 | -48.71652 | 2025-07-23 04:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c38537d-6f31-35b9-ac19-fb7ba1262366 | -4.0444 | -42.51629 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3adeb009-f06a-3a77-9fd6-dc6190f7d6b4 | -3.17168 | -49.44107 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f15ffc2-191b-3192-9eb2-7f77450cc299 | -4.09224 | -46.92709 | 2025-07-23 04:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c391173-333b-311e-821c-bf4ea750caae | -3.16339 | -49.44453 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c245cd2-12cc-36e4-b941-7dab4005eaa5 | -3.18236 | -49.44743 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20dc2a3a-3db9-35a8-907b-6bbe0c2fd1fd | -5.47741 | -42.14487 | 2025-07-23 04:57:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4b3a7592-3661-37fb-a30d-cdd4114a65b1 | -3.16439 | -49.4634 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d57ecbd-e3c3-3b74-b662-8c627089a1be | -5.67613 | -43.673 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb4fc5ca-e1c2-3474-be46-068eccf4b482 | -3.17786 | -49.45144 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12a9041d-46be-3fa5-bf48-f3762c5acae7 | -3.03602 | -47.86167 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 011bd4b1-8b5a-315f-90d3-aea56321fc26 | -3.13564 | -47.01185 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e1b9472-9eb9-342f-90e1-68e0dd2d4b63 | -5.83371 | -44.10155 | 2025-07-23 04:57:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82d0ab69-4b58-38e4-b0bf-540d63b211f9 | -3.82705 | -43.01941 | 2025-07-23 04:57:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e33ea39f-0993-3d38-84d7-517be79af4ac | -3.14572 | -53.13876 | 2025-07-23 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f347a8dc-3bc8-3181-977f-1b869f5d39ff | -5.68249 | -43.66994 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b425f4c1-d855-30f7-90b6-1dd7297ecfd7 | -3.17097 | -49.4457 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c48e78e3-da8a-3c06-a68d-efdde9b1bb90 | -3.41205 | -49.5346 | 2025-07-23 04:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f61b317f-f366-302d-9233-e80ed2ed7e80 | -4.04982 | -42.5218 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0deb83c1-8a9a-35ca-a0f2-899fd3475b3d | -2.44536 | -47.47433 | 2025-07-23 04:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c04ce788-25ed-3218-ace9-4ddaebfc75d7 | -3.18165 | -49.45201 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01965c4a-9c67-3c94-aa02-c0a54ea68e80 | -4.04372 | -42.52086 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4756ccee-51eb-30bc-9f08-92dc1c4d85c3 | -3.04021 | -47.86232 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3253ed0-ef55-3c8e-bd4c-54ed2a31dafc | -4.67537 | -48.15873 | 2025-07-23 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 702a0307-7aa4-3c0a-9375-befe05ad38b6 | -3.03085 | -49.42656 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 031094ec-dac7-3a4d-a57e-d4c8223f3ff0 | -3.97624 | -47.88136 | 2025-07-23 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df8f7fee-a1c6-3912-a8c5-39efb8317313 | -3.17239 | -49.43645 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caa192b9-27dd-32dd-903d-80eb9458e336 | -3.04879 | -47.3786 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6807ee8-2693-3a76-9df7-481236df5681 | -4.77424 | -45.33743 | 2025-07-23 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93e11ff0-660f-31f0-bb2d-fb59f47e659e | -3.40826 | -49.53402 | 2025-07-23 04:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c1157a7-a6ed-3101-b695-a5c4a439b1c8 | -4.0505 | -42.51722 | 2025-07-23 04:57:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9bef1c5a-b866-3191-b0c0-51d6c4160643 | -3.03544 | -47.86542 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a437ce1-fd24-39d9-afd5-a267ac721741 | -3.17197 | -49.46455 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f0ee032-0cbb-34db-88db-0d597be4fc46 | -4.10852 | -48.20575 | 2025-07-23 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f92d8c-4c1a-32dd-ae50-14e7593df488 | -3.16789 | -49.44049 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df6a6476-3d3d-3904-aec5-7954ae27e094 | -2.38674 | -47.62912 | 2025-07-23 04:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 961c55a2-9baf-3530-9ac2-2663c617a008 | -4.10436 | -48.20512 | 2025-07-23 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d75bc3c8-22d0-3196-b688-0c2bcc760528 | -3.11786 | -47.00912 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9b9c164-7ac8-3579-b8a9-305c7424ee5d | -2.58593 | -51.92226 | 2025-07-23 04:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d5875a1-aaf7-3149-acf1-97089d62eaa2 | -3.16888 | -49.45944 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7857e3fc-e140-377b-a7c6-7578e0fc126c | -3.16509 | -49.45885 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a55ba6c-cd2c-33d9-b5d8-dd574efc5db7 | -3.03183 | -47.86102 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e6c402c-522b-3087-beed-8e00d0ff7e08 | -3.03128 | -49.42947 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26ffb1b2-dc85-3741-b4b2-9fec1011cdbe | -3.1172 | -47.01352 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6d95fc5-d403-39d0-bab2-6fe8988602f0 | -3.03507 | -49.43004 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9273e231-e65e-3ed1-8b3b-5da74893b91d | -5.47671 | -42.1501 | 2025-07-23 04:57:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 73b75dfe-c9be-3944-a7b4-0ad023de9f34 | -5.67671 | -43.66891 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bd37e81-f318-3393-baf9-50e19172a897 | -3.16269 | -49.44913 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 057dd276-4096-331c-a5d3-02ab95dcc0e8 | -3.16957 | -49.45487 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03ace0fe-fbaf-3a9b-bc06-815ad44a06cf | -2.91869 | -48.24102 | 2025-07-23 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b69941f-76a7-3c3d-98c9-087160561e85 | -3.17267 | -49.46001 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 563a4475-7cbf-33dd-b3c3-bf05156b82d7 | -0.7596 | -50.26904 | 2025-07-23 04:57:00 | NPP-375D | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca1ca258-3dfa-350e-be84-e7fd61e758fe | -4.08769 | -46.92654 | 2025-07-23 04:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc26e657-1f30-3c8e-b1de-3bfb5055c632 | -3.69841 | -53.75516 | 2025-07-23 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e29404-14d8-3430-8ed4-410ad3f6f572 | -3.04222 | -49.42832 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 064027e8-4073-343d-a238-0709da00c120 | -3.17927 | -49.44224 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17299981-b7b4-3f4b-9c14-6f18d23a8760 | -3.18475 | -49.45713 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f482e69-9cbf-3076-b537-665b54327d30 | -3.16718 | -49.44512 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe27dcec-b78d-3bc1-843b-aae91ae33831 | -3.17337 | -49.45544 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4332481e-d891-3b4a-8152-5bbea6a9b006 | -5.68745 | -43.67733 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 134e1496-d4da-36e2-8627-5c02cc547d76 | -5.6819 | -43.67401 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 048c286d-b1d7-3c0c-9577-f47474c1788f | -3.04385 | -47.382 | 2025-07-23 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 20b07d66-392b-349f-a452-a4739aa5881e | -5.68827 | -43.67095 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d27e8194-867d-3460-bd94-a01172736cac | -3.0358 | -49.42545 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 510e3d0e-ed0f-316d-bbcd-31dba0cdb1ed | -4.09292 | -46.9225 | 2025-07-23 04:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c98d3af0-8b41-31c3-963b-4e11101aa485 | -3.17716 | -49.45601 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f1ff37ef-7a1b-392c-a62c-e5ddf1ccce87 | -3.17477 | -49.44628 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README15.md)
