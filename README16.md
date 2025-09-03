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
| 4508c064-3c8f-35bc-83a9-e06b9857879a | -11.1224 | -44.6521 | 2025-09-03 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 364b1a50-5db0-3d35-af72-4c23dcf6f9ed | -4.1604 | -46.7881 | 2025-09-03 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6741b6cd-9e4b-36ac-a549-6bf0af445685 | -5.6268 | -45.0025 | 2025-09-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c06ebfa0-70c2-34b8-b155-8e0940c935e8 | -7.7226 | -48.7355 | 2025-09-03 01:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2aa95e37-81a1-386a-8865-7e7bad59c5a5 | -6.4648 | -49.5151 | 2025-09-03 01:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 7fbe54b7-b6a8-399b-b1c7-17277f1fe45c | -9.3394 | -55.2277 | 2025-09-03 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| d4657560-dc50-3fb2-87ea-eeacab3f65e6 | -7.5305 | -47.4222 | 2025-09-03 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a4dcfa1f-9812-3d58-ab0d-f85b0109e6e6 | -3.2121 | -47.1138 | 2025-09-03 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b04d017e-5040-3be6-956c-9234c5daef8d | -7.7039 | -48.7371 | 2025-09-03 01:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 97.8 |
| c8cd17bc-85c0-326c-9010-439fed4f3ba5 | -11.1228 | -44.6288 | 2025-09-03 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4e335232-c60e-3a92-861e-d777f2f7e722 | -12.6339 | -57.0127 | 2025-09-03 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d4c176cb-ff30-3810-b87c-5b8383f57939 | -7.7036 | -48.7587 | 2025-09-03 01:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0d1eb371-91bc-3dd9-bb67-80d2ade92c44 | -5.6266 | -45.0252 | 2025-09-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1c2a4a4f-c7ce-3fc5-87b1-64f9dd5f36f9 | -3.2306 | -47.1131 | 2025-09-03 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 0dfe1661-3238-341d-9d8f-64ce4963a3bd | -5.6081 | -45.0038 | 2025-09-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 919e8131-b6e9-3efb-8161-b9dcc7011eac | -3.2305 | -47.135 | 2025-09-03 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.1 |
| affb6284-94e8-3bf9-8d1c-249de8663c42 | -15.5656 | -48.3918 | 2025-09-03 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6eb83b3e-f655-3b6e-99a8-daa04b7ea271 | -3.212 | -47.1357 | 2025-09-03 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 0ba0ed59-7fbf-3aaa-9696-f63d7222f09b | -7.5302 | -47.4443 | 2025-09-03 01:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 547f0430-bdfa-3cee-9343-5879614873cc | -5.6081 | -45.0038 | 2025-09-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 66347a13-59c7-31e2-bda2-8fc47de60d84 | -7.0964 | -63.0625 | 2025-09-03 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e2d62bf4-d9e1-3064-a5f9-582c56db4fa7 | -9.3394 | -55.2277 | 2025-09-03 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 448ed615-9420-3a31-a0d6-19a141aad279 | -4.9122 | -43.2103 | 2025-09-03 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6b9fa942-114a-3200-8f1b-3b3349fcda38 | -3.212 | -47.1357 | 2025-09-03 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e6553b02-4f4f-359a-b020-21710d76bc73 | -4.8935 | -43.2115 | 2025-09-03 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5959eca0-b1d7-3f05-b6da-a0578c60fbd5 | -3.2305 | -47.135 | 2025-09-03 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 2d2ae540-ef32-3684-8ea9-024d29d66055 | -15.5652 | -48.4143 | 2025-09-03 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| eea3bb32-d2da-3327-a37c-72103d49fc7a | -4.1604 | -46.7881 | 2025-09-03 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 1d6ec453-2782-3d53-b0db-92ccfb2ee8c8 | -15.5656 | -48.3918 | 2025-09-03 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 19f13f58-5cd2-3629-bab6-36fba712b791 | -9.1949 | -45.1972 | 2025-09-03 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| bbc15f12-42f6-3ee4-b05d-84dc1e7b4789 | -7.8977 | -46.4371 | 2025-09-03 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 5731c1a1-ba1e-39ac-9c6f-4ba30838ea4f | -7.6783 | -61.0908 | 2025-09-03 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 29469824-9cac-381c-92cc-7c95b8d86964 | -5.6266 | -45.0252 | 2025-09-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 58471559-92bd-344c-9e38-751902a347d5 | -14.9839 | -50.2082 | 2025-09-03 01:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 273debfd-6bb4-31b0-a8cc-1baa1ed8dbd7 | -7.7039 | -48.7371 | 2025-09-03 01:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 86.3 |
| ae6f2b9b-613d-3ccb-a095-e1349f7988e4 | -6.4648 | -49.5151 | 2025-09-03 01:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 6eab34b5-0d3f-33d0-8f19-a8531c4167bc | -7.7036 | -48.7587 | 2025-09-03 01:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 6e1b7779-c05f-35a2-a5ca-779d61e7983c | -4.8936 | -43.1882 | 2025-09-03 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| f659dd2d-5385-3b3c-ae23-069b679bf457 | -7.7226 | -48.7355 | 2025-09-03 01:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 57c1c134-161c-3577-a10d-140466b5a154 | -11.1224 | -44.6521 | 2025-09-03 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 1a64aa72-f627-3a26-9a76-96c07ae13fdc | -3.2306 | -47.1131 | 2025-09-03 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 3e9bd83d-f24c-3d52-af9f-e529905594b0 | -5.6079 | -45.0265 | 2025-09-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| fec783e0-7e96-3038-9470-9bbb5825e704 | -12.6341 | -56.9926 | 2025-09-03 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 07859089-34df-3f89-8da1-6006decd205f | -14.9645 | -50.2111 | 2025-09-03 01:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5c7218e2-c501-34c0-925e-008cdefbbf10 | -6.4646 | -49.5364 | 2025-09-03 01:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 75d0706b-bcc7-34cd-9072-f7b8a43064ce | -11.5338 | -52.150101 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdb69868-14cb-325c-bb05-b518b50306fd | -5.844 | -57.731499 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e283c9e6-0a85-3dfb-a5c5-ef65cc8cd85f | -11.3742 | -55.1814 | 2025-09-03 01:17:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eed4278a-2a14-3d25-a738-ed15ec9c3627 | -5.8187 | -57.7542 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3243d70e-9278-39b0-b405-3f5223b5eb57 | -7.6395 | -61.089699 | 2025-09-03 01:17:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb27a48-f667-3648-a359-c7251a7c1d31 | -11.5256 | -52.119801 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2901b275-5a6a-3142-b5b8-0de87f705aec | -6.3944 | -58.139999 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b55fcbf-5f99-3904-bbc1-a16f907f2424 | -12.5871 | -56.995499 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4620820-c117-3937-94bd-fc5c46eaec58 | -12.885 | -56.947201 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b5a8cc5-7b6f-3c61-8b28-346f37ba93d6 | -12.8953 | -56.9883 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b0f5b3a-0572-30f1-91e4-7247104298c7 | -12.9016 | -56.972099 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5af8013-5432-39c9-a3e0-558b7ea7149b | -12.8753 | -56.949699 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22330798-c84f-325f-aad6-88831d9a4eb4 | -12.9084 | -56.999401 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd10198-12d9-39c1-a623-0a98bcbc4354 | -10.9713 | -51.513401 | 2025-09-03 01:17:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6e1dd7-9283-3d43-83e1-0f670f6ef9ae | -6.3909 | -58.125599 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34fa3157-f294-34ef-a922-bfde75080464 | -5.8321 | -57.767502 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 572679cf-b382-3fdb-bdda-aef20a84a17e | -12.8656 | -56.952202 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1adbd19d-bfb0-360d-83f5-e855acdc8c39 | -11.5364 | -52.0839 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13573386-d5b8-38fb-8444-5a4489cf68d4 | -12.8793 | -57.006901 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd27de7a-6840-3779-b33b-8985eed50413 | -18.094999 | -51.742901 | 2025-09-03 01:17:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de3c1471-aae9-39d5-8f0f-46d60dff647a | -11.6305 | -57.343899 | 2025-09-03 01:17:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8403b9a1-5434-32f9-9fa9-63cfcc9864bb | -11.5269 | -52.086601 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42b83de5-b336-3432-98f5-cfc32f33239f | -5.8224 | -57.769798 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a20c637d-a7be-3e71-af50-90fa96987f7f | -12.5905 | -57.0093 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 274a5fd3-c21b-3a28-9c71-0764d1545706 | -12.8947 | -56.944698 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 918f22dc-9802-3020-a1eb-2f63eea86576 | -6.2875 | -58.165699 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f329f1f0-7741-3810-92c6-5dd6e717b6a3 | -5.8126 | -57.772099 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfe19287-3775-34fc-8fd8-55e0aea19865 | -11.5352 | -52.1171 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f895ea88-13f2-38a0-be7c-ee5189800e3c | -6.8598 | -71.484001 | 2025-09-03 01:17:00 | METOP-B | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3ad7727-818b-3ddc-a8c9-da1a9881eb03 | -12.905 | -56.985699 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad5fb2d-f309-3fa1-aa02-dcbb00cf8098 | -7.5035 | -61.346901 | 2025-09-03 01:17:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5813e0-4c67-3127-94cc-45122b4e4274 | -11.6338 | -57.357399 | 2025-09-03 01:17:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be1fdfd9-74a3-314f-9a9b-c1effef0242d | -7.4994 | -61.3293 | 2025-09-03 01:17:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c84e8d99-192c-3445-8b8e-017e39aa0263 | -11.5747 | -52.0732 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd6f7d2a-b65f-3400-9c1b-4e27352bafdc | -13.0555 | -57.132999 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccf6de04-55bf-3d7a-9ee1-324f85fb3d1a | -7.5112 | -61.3358 | 2025-09-03 01:17:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f38f8bd4-7b4f-3cb9-b9dd-c42e62c46aee | -5.8284 | -57.7519 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a349de-4946-37af-85b0-04788cec4952 | -5.8731 | -57.724499 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c16959-77aa-34e8-8962-1d6158a97628 | -7.0646 | -63.064602 | 2025-09-03 01:17:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e37f1bf-08b4-30ef-8181-0c962f4a56ab | -10.9619 | -51.479099 | 2025-09-03 01:17:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73e3b540-a5ee-3355-9ce1-ca744e85a178 | -11.5556 | -52.078499 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4d18e93-182b-31a0-96bf-7c11ff1f1ac3 | -12.8827 | -57.0205 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acb79007-a2bf-38f0-bc16-2d32c8008386 | -13.0588 | -57.146198 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| caa18ac1-db4a-3dc4-b32b-308e8d6a51c8 | -7.6374 | -61.0807 | 2025-09-03 01:17:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be87463d-7d69-3474-8234-824943a25278 | -7.6297 | -61.091999 | 2025-09-03 01:17:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac304413-ba02-314d-a5a7-dcf7642b350c | -7.5015 | -61.3381 | 2025-09-03 01:17:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07aa3a37-35eb-34a3-9409-3a9c9891a4c1 | -12.8559 | -56.9548 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8b69b48-d0a3-333a-8c8d-b23b0878ccce | -11.5542 | -52.111698 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2140bf-8e5a-3125-88be-928f0e333463 | -7.5133 | -61.344601 | 2025-09-03 01:17:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c8b84e7-b7b8-33e4-8fd2-ab239724cd19 | -11.5434 | -52.147499 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 659685b3-43ec-3a5c-992e-969e9514d040 | -12.889 | -57.004398 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 768f8888-78c6-3fc1-a807-9be053102143 | -5.8634 | -57.726799 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6943de-83f4-3998-8c62-a505879e422d | -6.291 | -58.180099 | 2025-09-03 01:17:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32c97642-a45a-3346-b09f-69d1c8f299cb | -12.6002 | -57.006699 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0acfc5e-36f4-3dab-8067-22db4beea375 | -11.5529 | -52.144798 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
