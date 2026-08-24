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
| d53e055e-720a-3227-a52c-4100ab3eaf6a | -23.52318 | -47.36567 | 2026-08-24 03:53:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 40c2f676-8714-3c5f-ae91-1e9f0f3c5b67 | -22.95334 | -51.78462 | 2026-08-24 03:53:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 4e42252a-d2dd-3341-a79d-83ab20c40203 | -23.82838 | -48.71949 | 2026-08-24 03:53:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47e3a6ba-a435-32c2-ae04-5cb74e4a49dc | -23.20079 | -46.60547 | 2026-08-24 03:53:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 66a00735-ebce-3213-9231-ab0786b21363 | -23.3305 | -46.43827 | 2026-08-24 03:53:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9be5d8fc-e725-36ce-a20d-49378f63b922 | -23.13446 | -47.39887 | 2026-08-24 03:53:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5d6e2b61-01e5-3ed3-9aa0-4f708d294a06 | -21.55435 | -47.68769 | 2026-08-24 03:53:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b788490-8ad7-3f4d-8b87-31e21c0ee444 | -23.79725 | -54.5496 | 2026-08-24 03:53:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 463fec88-aa3b-33e0-84c4-72cfeaaa3119 | -19.97977 | -50.3816 | 2026-08-24 03:53:00 | NOAA-21 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| dba4777d-e4d1-3329-82c2-003da17a9529 | -20.64562 | -46.58164 | 2026-08-24 03:53:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac00d3a0-0061-3c2a-aa67-f5d981e4af56 | -23.79877 | -54.5435 | 2026-08-24 03:53:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 68627f0f-1f6d-3dcc-960c-6b2fee5ff5a1 | -29.0346 | -50.6395 | 2026-08-24 03:55:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4e2241c7-0fe2-3222-83ac-6cc508c297a0 | -29.03566 | -50.64405 | 2026-08-24 03:55:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 09a933a8-b4e2-310f-bec2-5bc2ee915014 | -12.1125 | -50.6358 | 2026-08-24 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b0ed4403-b654-30ae-a664-f4ddb7a252e4 | -7.3603 | -45.8136 | 2026-08-24 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6ff47928-3c49-3a8a-b630-99ddd008ef41 | -12.1132 | -50.5929 | 2026-08-24 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 85d92640-6a2b-3ae9-b430-697cb34b0877 | -7.2443 | -49.8654 | 2026-08-24 04:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 84e084e6-21de-3e12-8671-ef0113fe49b6 | -12.1128 | -50.6143 | 2026-08-24 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 205.4 |
| cc6dc0e6-153d-3a49-96c3-1395d79ee22b | -22.9454 | -51.7768 | 2026-08-24 04:00:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| e437d587-c8ee-343e-a4a2-ea067a929b29 | -22.9664 | -51.7723 | 2026-08-24 04:00:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| bac23055-1ca5-31ca-86e7-147440aa8641 | -12.0938 | -50.6166 | 2026-08-24 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 45dd1fba-fe24-31c5-b006-14f633bae5ed | -7.685 | -63.3255 | 2026-08-24 04:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| aaa00146-29a0-3dfa-a714-a45d70baab79 | -7.3603 | -45.8136 | 2026-08-24 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| be3e6c83-c9fe-34e5-ad01-2793eda8ffb9 | -12.0938 | -50.6166 | 2026-08-24 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 7e8a9606-c45f-3d00-bbf8-0f56814c5cd1 | -7.2443 | -49.8654 | 2026-08-24 04:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 04748671-0558-31e6-9a48-32c41797007e | -12.1128 | -50.6143 | 2026-08-24 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 956c0cbd-7703-3736-a34a-b4d31bd2b0d3 | -12.1128 | -50.6143 | 2026-08-24 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 33650ca2-a5c5-354f-bfd2-73e7956cdf1f | -12.0938 | -50.6166 | 2026-08-24 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e39289b4-9247-3525-b800-c30154ca8f71 | -5.13771 | -42.70997 | 2026-08-24 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bbde200-864a-3f2d-bab1-593ee416897c | -2.82751 | -48.65129 | 2026-08-24 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce85a1d-f90a-3d77-8678-2416c5df80e2 | -3.47432 | -47.69962 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf0fb474-d6a6-34f6-b5cb-dbd98aac70a5 | -5.10626 | -43.14442 | 2026-08-24 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8129a029-17f3-3442-87b5-776440589999 | -2.82682 | -48.65556 | 2026-08-24 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38f0d9bd-4f62-3df6-8f95-a1682634e9d7 | -3.53682 | -48.18419 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 968f2e08-778c-3ad2-bef1-9e153cabda1f | -4.02318 | -47.72279 | 2026-08-24 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18201bc4-954e-3ded-a06d-6cd6bd21964e | -3.30588 | -42.77792 | 2026-08-24 04:23:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c111992-8004-3fcf-8e46-a4d023386ac0 | -3.53323 | -48.17969 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6a8ac1d2-7bdc-3b0f-bb3b-e9f485e8de5b | -3.53197 | -48.18741 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bc51f806-b31b-389d-8875-d4ee10f6f93e | -2.11146 | -48.99931 | 2026-08-24 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d35487d-195a-3d11-8b8d-4748ccd936d6 | -3.04799 | -50.27234 | 2026-08-24 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f719d1c1-37f4-3953-a5b4-0b3ee44823cc | -3.30642 | -42.77447 | 2026-08-24 04:23:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0842fb52-94d2-3f18-be5a-8e07e93f1209 | -5.17504 | -39.24303 | 2026-08-24 04:23:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0f5d1642-da66-3107-8343-670eb4ecc035 | -4.80515 | -43.07879 | 2026-08-24 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f4fe378-644a-3c3e-82a8-fb199f237457 | -3.5326 | -48.18354 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56cd42b4-b5db-3965-a2ec-5a738c48489f | -4.18172 | -49.40055 | 2026-08-24 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aaa40eee-3eb8-3ef1-9831-5179edc3a3ff | -3.54103 | -48.18484 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 02b09e21-f058-3326-b78c-b7241666862c | -3.42505 | -50.09469 | 2026-08-24 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 803f89ad-ae3b-306f-8afc-91605682fbf7 | -3.26548 | -49.52612 | 2026-08-24 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16ec2ecc-5c7c-3c71-930b-5b43835df964 | -3.96799 | -48.95928 | 2026-08-24 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e4beb2-1932-307e-bb1d-6d3c29ceec71 | -3.26928 | -49.53191 | 2026-08-24 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77607516-fe28-35c9-8d55-e70042be17c8 | -3.53744 | -48.18034 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f2489781-44f8-3d70-a21d-240cdbb777ae | -3.26465 | -49.53108 | 2026-08-24 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b2984bb-b36f-37ed-8df6-2219dd049516 | -3.54166 | -48.18099 | 2026-08-24 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3df26e12-3414-3334-8eb4-66c57aa460cf | -10.2949 | -48.20467 | 2026-08-24 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02f69c77-a2c7-36d4-8733-e05fdc9a5a72 | -9.72265 | -46.0076 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6b2d793-b9b0-3bbe-ae68-5b9029b0964e | -5.57552 | -45.29108 | 2026-08-24 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fce4e1b-61fb-3afd-b6b3-d71f98784072 | -12.27302 | -43.19937 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a2f9d2a-ba4c-355d-b0ee-3d38ff500ed3 | -6.34744 | -55.86577 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a2f553e-a07a-3a10-aae7-97a4993def63 | -6.61931 | -53.35037 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5df78136-0a61-3cf3-b63a-760997e2cf99 | -7.18586 | -42.74403 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9749f88c-3282-3ddb-8763-2c337db1cc05 | -7.24524 | -49.86829 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3835105e-0c52-34a9-811c-fd78bb665744 | -12.27697 | -43.12895 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ef36488-f11f-3cdf-9fe8-76a7ebe0cf34 | -5.628 | -48.41977 | 2026-08-24 04:25:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbf55c3d-c24c-3fd8-a65b-8d2dd4b7a4e4 | -7.35774 | -45.807 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02568dd5-3588-3333-ae12-c413fa45db7c | -5.06259 | -49.37354 | 2026-08-24 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63ca4488-6c04-36d8-a4cf-fd4156263717 | -7.15925 | -42.76133 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab0b0460-25ce-3590-aeca-15a892fe6548 | -6.69891 | -52.08677 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9b6233-1c00-3369-880d-2fed71d50502 | -6.4162 | -48.58594 | 2026-08-24 04:25:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f1e26b6-211b-39e0-9d91-96d388b83193 | -7.18316 | -42.78304 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e85e260-0a4a-3b73-8452-1d356035be69 | -10.69304 | -47.7357 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78b9f95a-178c-37f0-9364-4a4541c7bbc8 | -10.79544 | -50.94754 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b65be0a4-ee85-3c22-b4d3-26a1cd5846d8 | -8.10672 | -47.49238 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50c1805d-274a-3bf9-a2e0-93965f7b5a2d | -10.29864 | -48.20571 | 2026-08-24 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32735d11-ba19-3658-b3ea-cb1464e856cc | -6.97685 | -43.74813 | 2026-08-24 04:25:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3f9c15c-0a17-3547-a29b-41717b97b38c | -7.29425 | -43.00491 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3ccac4eb-5e55-331d-9fcf-e85a168c9259 | -11.09898 | -38.60053 | 2026-08-24 04:25:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f469be12-decc-3bde-aefa-193d11b37444 | -7.15656 | -42.80035 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3551fc3f-a2f1-3ed6-8930-087edeaea74f | -6.18777 | -53.53057 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c60ffc8-7a46-382d-832f-5fa98b986d68 | -10.62639 | -52.25195 | 2026-08-24 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2235c51f-c00f-3d92-ae19-3aceeaa2b132 | -8.10371 | -47.48718 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f1293ad-5281-36fd-a5e5-485173818209 | -9.05031 | -50.77355 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b07f5eb4-2c8c-3090-b71f-80df0cd3ec79 | -8.0822 | -47.27061 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bd204e2-61c4-3d35-ad0a-6302b65cc475 | -6.80547 | -42.66982 | 2026-08-24 04:25:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1e8e3705-8024-3753-989b-f24d344b5dad | -7.29535 | -42.99795 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6c9ae9fc-d39e-3027-bbef-d00c6223fb2b | -7.36187 | -45.80371 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a97ca818-87a2-3229-b275-2d07c70e13d2 | -8.95444 | -50.75738 | 2026-08-24 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 766e83b3-40b1-349e-a134-325b41fde509 | -7.36504 | -45.82811 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c285b0d0-1885-3de3-89ec-80366024aec3 | -6.33866 | -55.87592 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f1798c-89c8-3a5a-a729-ecc5c1a8aa7c | -6.17628 | -53.53085 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41130e78-e7f6-384f-8cc9-b52fb85274a2 | -12.41306 | -42.90047 | 2026-08-24 04:25:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72f29235-1855-3253-9cac-a8558604d656 | -11.59573 | -46.93659 | 2026-08-24 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e70b5ea1-272f-3406-853a-5d22004c68bf | -11.58121 | -46.9584 | 2026-08-24 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2c13e8a-4862-3d6d-8719-8b51a129cab0 | -6.39814 | -43.83063 | 2026-08-24 04:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7e4b727-1edc-3547-9f09-8c29d6b985dc | -7.36219 | -45.82363 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 355a71e9-edb2-3358-b3b2-68f86fff225e | -5.50021 | -45.8385 | 2026-08-24 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b3b26be-9019-3cfb-b529-d7f9977ebd0d | -7.2617 | -49.91944 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2da3dba5-60fb-3c57-a54f-d1a126ed96d5 | -7.75197 | -46.15428 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2402b734-1b1e-391e-93b2-958a9110dab5 | -8.79425 | -48.32077 | 2026-08-24 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3e81c7-da2e-3ef2-ba54-93cd51407490 | -10.86425 | -50.98647 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3ad49d5-d0a6-3dbe-b32f-4c81f52dd468 | -6.34398 | -54.76703 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README16.md)
