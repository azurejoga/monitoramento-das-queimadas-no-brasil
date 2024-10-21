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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec4d9375-7aa4-3470-926a-cd07a746f78b | -2.9049 | -49.5546 | 2024-10-21 00:39:03 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7387141a-b0d3-3fcd-860b-c6b493c3a0d2 | -2.9064 | -49.561401 | 2024-10-21 00:39:03 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a911e5d4-4c08-3d06-ba4c-8380b8a52e40 | -3.2164 | -50.9366 | 2024-10-21 00:39:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4847110-dbe0-3611-91c7-526215698182 | -2.6946 | -48.671799 | 2024-10-21 00:39:03 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed27ceb-7baa-3366-88e6-e669b35b9f06 | -3.1723 | -50.786701 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c95d23c5-8155-35d0-9023-568422b5a250 | -3.1739 | -50.793598 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8b66f1f-3faa-35c8-b090-684e71725d0d | -3.1754 | -50.800499 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c440be35-4025-3383-94f4-4b54757bc168 | -3.177 | -50.8074 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b942fa-8291-352e-866e-3712ec19fc6f | -3.1625 | -50.788898 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3130fc-af6f-39d4-a27c-1973fd932192 | -3.1641 | -50.795799 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7e844c-75d9-3868-9a7e-6ff3ec8fdc35 | -3.1656 | -50.8027 | 2024-10-21 00:39:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 876950e4-58a9-39b2-a40c-0418d4aca521 | -3.7326 | -53.388 | 2024-10-21 00:39:03 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c94980-1bd9-3f66-b638-2e6e879a0c61 | -3.7345 | -53.3965 | 2024-10-21 00:39:03 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00003bb2-f259-3cd3-838b-9c10ac4e367f | -3.7364 | -53.405102 | 2024-10-21 00:39:03 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b30eea5e-1daf-36b6-afd6-53908dcc0cba | -2.847 | -49.480999 | 2024-10-21 00:39:03 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26575efc-8b25-3ae4-8598-390011f21879 | -2.8486 | -49.4879 | 2024-10-21 00:39:03 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac18e62-f664-3ce7-8993-a3916f8cddf4 | -3.1996 | -51.137299 | 2024-10-21 00:39:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c96ad8db-1a42-3d16-846b-63bc74c58ba7 | -3.7051 | -53.402901 | 2024-10-21 00:39:04 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de14d978-a60c-32e7-8737-e318bb0c9ffc | -3.1882 | -51.1325 | 2024-10-21 00:39:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3824d925-5b5a-38bf-a132-8e654f72e791 | -3.1898 | -51.1395 | 2024-10-21 00:39:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a87a43-5ecb-3ab7-aadd-e1441a333060 | -3.4288 | -52.207401 | 2024-10-21 00:39:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67948c38-9832-36bf-9fef-f3542cf0fe72 | -3.4305 | -52.214901 | 2024-10-21 00:39:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67383ad-0da5-3c9d-9d47-8eed049afeb8 | -2.2275 | -47.0723 | 2024-10-21 00:39:04 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db37fa95-25e0-332e-9637-fc90d0e1a71e | -2.2293 | -47.080601 | 2024-10-21 00:39:04 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21daef5-50d7-36af-b8b4-dcbc3d9808c7 | -2.7316 | -49.2896 | 2024-10-21 00:39:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439bb394-e0a5-3c1e-90d1-aaa48b1cdf68 | -3.0082 | -51.018902 | 2024-10-21 00:39:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0623281-0b79-33d9-a591-853b3ec9f84d | -3.052 | -51.213902 | 2024-10-21 00:39:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb02fb90-7414-3b0c-9b55-40485e13e75f | -3.0646 | -51.269901 | 2024-10-21 00:39:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a90e79-e4a1-3d07-a397-d9345a7dda5b | -3.0661 | -51.276901 | 2024-10-21 00:39:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f96a94-1c9d-33b9-8cb4-8c65f67642d4 | -3.4198 | -52.858799 | 2024-10-21 00:39:06 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f05c076-cbf2-3cd9-85a3-7bd34a4d9532 | -2.6326 | -49.398602 | 2024-10-21 00:39:06 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c799888-02f4-3fb5-bf34-13c878496ad4 | -2.6341 | -49.405499 | 2024-10-21 00:39:06 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e62dd8-f4b8-3b96-a39d-a599fc7b31ac | -3.0548 | -51.272099 | 2024-10-21 00:39:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a165f2-dc48-3f7f-9f08-5d5f971e909d | -3.0563 | -51.279099 | 2024-10-21 00:39:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a569d848-b32b-3149-8a48-6cb0521594f4 | -3.0434 | -51.2673 | 2024-10-21 00:39:07 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df54ad33-9ca8-3e7a-8eeb-843f90157fc7 | -3.045 | -51.2743 | 2024-10-21 00:39:07 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b451ef12-65c5-3dcc-84a1-bba66844aed5 | -3.0465 | -51.2813 | 2024-10-21 00:39:07 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2fab77a-6c24-3166-9ef5-74966f68ba2b | -3.5282 | -53.531601 | 2024-10-21 00:39:07 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 618a1cfd-9997-3131-84e5-c32e955ad43e | -2.954 | -51.0527 | 2024-10-21 00:39:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a62eb43f-f709-36f3-bbe4-fd89282a5c0d | -2.9556 | -51.0597 | 2024-10-21 00:39:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2854dd-044d-37cd-9305-96fb11aa033e | -2.8097 | -50.456902 | 2024-10-21 00:39:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e244a63f-97cf-3e6a-bbf7-ea2e06b1fec9 | -2.8112 | -50.463699 | 2024-10-21 00:39:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd44e4c-e77c-3441-93bc-2a11e808501a | -2.0309 | -46.842701 | 2024-10-21 00:39:07 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6c0c35-57a3-3c4b-96a6-155d1313bb28 | -2.021 | -46.889702 | 2024-10-21 00:39:07 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c755a4-71a0-3e8a-b862-eb44772bd70b | -2.0229 | -46.898201 | 2024-10-21 00:39:07 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e411e87-ed79-33af-b2ca-233ecb600462 | -3.3653 | -53.168701 | 2024-10-21 00:39:08 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f183d0f9-c694-3a02-b04f-1bdb89121a9d | -2.441 | -49.098801 | 2024-10-21 00:39:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f6b562-b13a-3125-8031-894e5ab1df28 | -2.4426 | -49.105801 | 2024-10-21 00:39:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6122db6-f5a4-3910-b376-4dd0a949024f | -2.4442 | -49.112801 | 2024-10-21 00:39:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba037edb-756a-3e8f-9c93-e9ecc7369522 | -2.4458 | -49.119701 | 2024-10-21 00:39:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05279c8-6ff3-3f37-86c8-e4c883d3d9fe | -2.8196 | -51.2798 | 2024-10-21 00:39:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5b53103-1dbd-32a7-83ce-91e3a961aab0 | -2.8212 | -51.2868 | 2024-10-21 00:39:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e96693-b54a-31d8-a766-b70c13b80adc | -2.8098 | -51.282001 | 2024-10-21 00:39:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cea2743-7c05-3d08-8f09-eca0c28aa922 | -2.8114 | -51.289001 | 2024-10-21 00:39:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b919de0-e807-39bb-906a-97783b467a51 | -3.2768 | -53.371601 | 2024-10-21 00:39:10 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f088715-7aac-360d-ad1d-7cf6ef32e34f | -2.78 | -51.332699 | 2024-10-21 00:39:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c2b473-6a20-3817-a2e8-d3a6d5c73494 | -2.7816 | -51.339699 | 2024-10-21 00:39:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe732c6-6152-3730-87eb-6e7925df4b28 | -2.7832 | -51.346699 | 2024-10-21 00:39:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de9a0894-e999-37b5-9d7a-8bb2f88a03c5 | -2.7537 | -51.353199 | 2024-10-21 00:39:12 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 143d6d48-dfe1-3eef-b8bd-0e2e30ee8259 | -2.7553 | -51.360199 | 2024-10-21 00:39:12 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d846f65-e3b9-377e-bef8-031181727ae0 | -2.7569 | -51.367199 | 2024-10-21 00:39:12 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9540b2a2-e37a-30c4-a4da-b088e6396f68 | -3.3824 | -54.263901 | 2024-10-21 00:39:12 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b211d0c-bed0-3f10-a5c8-5b68ad0fd0f4 | -2.3882 | -50.2784 | 2024-10-21 00:39:14 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3daf674-f4d6-3bbf-8dd5-d997d9f0e06f | -2.3897 | -50.285198 | 2024-10-21 00:39:14 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa0ef7e-fc00-301e-8bf7-d81c2b6536d1 | -3.0062 | -53.033401 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5b80cd-7664-3494-aa53-c4c9e911830b | -2.3891 | -50.328201 | 2024-10-21 00:39:14 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 927d3e74-9b09-3db5-9b3b-97b53b8138c3 | -2.9439 | -52.846298 | 2024-10-21 00:39:14 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5abd6c2-7e95-3e47-9a37-ad86a319e7f7 | -3.0284 | -53.224998 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 770249b6-853c-358f-b9c3-c38b2223ece8 | -3.0302 | -53.233299 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc1adad5-e9af-3eff-8f70-758c773cdb9e | -3.032 | -53.241501 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75388c23-3220-353e-b708-45523d7c0934 | -3.0204 | -53.2355 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9246a771-2ba1-3fb2-94a0-50da5ca59d98 | -3.0278 | -53.268501 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2424f218-70fa-3227-adf0-2f1bdfd44a4e | -3.0296 | -53.276798 | 2024-10-21 00:39:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6a964c-d3a0-3a70-858f-0b317f923178 | -3.0709 | -54.1553 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1672f204-73f3-341b-8ecc-54bc202e4827 | -3.0729 | -54.164501 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09310967-0c6e-3d3f-9eff-0f6ef76bd973 | -3.075 | -54.173801 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09673c36-ee5f-3092-9076-48e73ff12bd0 | -2.9947 | -53.858898 | 2024-10-21 00:39:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6895f5-0eb7-32ca-a1e2-add843e2b25f | -3.057 | -54.139099 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 655fb462-8ff9-3777-98b1-7b940e922d7c | -3.059 | -54.1483 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dda3f7f-1933-34f0-89f3-1fc50d9f15ea | -3.0611 | -54.157501 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820fa051-4995-3246-9fb1-a0f77e79c605 | -3.0631 | -54.166698 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7575c88-a012-38ea-8288-96f75d559708 | -3.0652 | -54.175999 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3074c2-6c8f-3e01-b609-01b915ba8e19 | -3.0673 | -54.185299 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef66a2f5-514b-395a-8aa4-b23ca90b1e2f | -2.7922 | -52.996101 | 2024-10-21 00:39:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f28a1df7-e168-39c7-9d1e-66143c39c159 | -2.794 | -53.004101 | 2024-10-21 00:39:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 123cddf7-747b-378b-b180-f5ba36a4727d | -3.0472 | -54.141201 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2b3fbad-56a8-3bc8-bfb2-7fd6133d38f3 | -3.0492 | -54.150398 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f378a30-fef1-3de6-b24f-1c7803a8e8fb | -3.0513 | -54.159599 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90994718-990b-3397-a964-3d82055c847a | -3.0533 | -54.1688 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db756bb6-bf53-3d3d-a197-f3a7f82f46f3 | -3.0554 | -54.178101 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 698c3bbd-1f18-3ad5-b278-485c132f4ae6 | -3.0575 | -54.187401 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3989d390-73a7-3707-bb02-58db83784b32 | -2.7806 | -52.990398 | 2024-10-21 00:39:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3812669e-6325-3346-8b73-2d9615cd74d5 | -2.7824 | -52.998299 | 2024-10-21 00:39:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f4d36f-aeb2-34e0-b0bf-d9d7384e4799 | -2.7842 | -53.006302 | 2024-10-21 00:39:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f525f9d1-b7c1-317b-9803-6c69da91b254 | -3.0394 | -54.1525 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6a3ef39-371b-308b-bc89-4bd403ce982b | -3.0415 | -54.161701 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0f1ffd8-ea34-3e41-9016-c72b66abda5d | -3.0435 | -54.170898 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22b85436-7ddb-3307-94f9-a4c35b74583e | -3.0456 | -54.180199 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38f4b873-15e7-385e-a0e1-7f481fa315e5 | -3.0477 | -54.189499 | 2024-10-21 00:39:17 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d175fde-fcc7-37f8-bafa-53a66bda03ae | -2.1901 | -50.451 | 2024-10-21 00:39:17 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
