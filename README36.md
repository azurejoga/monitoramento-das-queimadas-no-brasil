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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfec82ff-1d63-39c5-a59a-d56293f0b952 | -14.4331 | -45.71644 | 2024-10-01 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba795970-a9c0-34d0-9176-cdb4f6676aea | -16.44781 | -46.99967 | 2024-10-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 253044b2-35cb-38eb-ad86-d3dbb5888119 | -16.439 | -47.00602 | 2024-10-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3ee5e9f-9ff9-359b-8953-daf3713f284c | -16.40494 | -46.86966 | 2024-10-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9f1995e-9d9a-3438-8c2f-cce1e467a668 | -16.39919 | -46.86819 | 2024-10-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ff198e4-1020-35b2-a9c5-8a0ef62cbb34 | -16.39793 | -46.86843 | 2024-10-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a65ed083-eaa0-384a-8fb7-005acc8712b9 | -15.19728 | -46.22816 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e630d9de-47e4-32a7-bb77-c2e083c2d4f5 | -17.20335 | -39.51289 | 2024-10-01 03:25:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 548b890c-13e8-3354-b1d9-bc83ce45a4b9 | -16.95112 | -40.76091 | 2024-10-01 03:25:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7c69cd74-41ae-3d4c-8030-0a5bfc941d0a | -16.95104 | -40.7627 | 2024-10-01 03:25:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 54ccf628-63cd-310e-b89a-3c75fd8fab8a | -17.78675 | -42.89296 | 2024-10-01 03:25:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239a0e13-e74d-3af9-9756-5e1bff9ff213 | -2.4048 | -50.3085 | 2024-10-01 03:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| bbff4155-5365-35d5-82e4-e4bd1d54e3b7 | -2.4047 | -50.3295 | 2024-10-01 03:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 06092e5c-4aa9-365a-bf49-91cb12c91a59 | -2.4046 | -50.3505 | 2024-10-01 03:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b40d6839-6306-3534-b9df-d032bc94b2f2 | -2.3863 | -50.3299 | 2024-10-01 03:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| e588a233-1586-37a3-891f-43c6d9675408 | -3.0282 | -51.3345 | 2024-10-01 03:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e2cec2d3-0acc-30bd-95be-a875db58ff3d | -5.9788 | -45.3621 | 2024-10-01 03:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| cfa446cc-cced-3850-965d-f4fa55678c35 | -5.9786 | -45.3847 | 2024-10-01 03:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a3b93fe9-17ec-385d-98dd-b43c0b98c200 | -10.924 | -50.0854 | 2024-10-01 03:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 28e9296f-ca1c-321c-9e50-23283726d198 | -11.6743 | -64.9983 | 2024-10-01 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 453eb74d-061a-398d-bf56-9c011ae8cdab | -11.6555 | -64.9991 | 2024-10-01 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 41089092-6982-354b-9b87-1c3bde50a841 | -12.1406 | -50.0524 | 2024-10-01 03:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7578d33c-b663-3dbb-b89c-b8951962bb03 | -12.1402 | -50.074 | 2024-10-01 03:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 79cafc12-c02c-30e0-a375-5a9d61fc95db | -12.2547 | -53.9792 | 2024-10-01 03:26:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f2018273-f54a-3524-831e-14e1697dd141 | -12.2545 | -53.9999 | 2024-10-01 03:26:15 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| df054dbf-1e7f-32a4-85c8-b07e9cd4d963 | -12.9783 | -51.428 | 2024-10-01 03:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| d84b187c-628a-3fcd-8f56-d8766769f1c6 | -12.978 | -51.4493 | 2024-10-01 03:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f937bb1f-492e-378b-be05-54a5a657db47 | -12.9591 | -51.4303 | 2024-10-01 03:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 4869af1f-b911-3b78-9f0c-995c158d70b1 | -12.9588 | -51.4517 | 2024-10-01 03:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 37823e14-230e-391a-bbd5-89628d75169f | -12.9437 | -51.1979 | 2024-10-01 03:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 49b59541-60ca-38e5-aa5e-c76b44e0dc96 | -12.9245 | -51.2002 | 2024-10-01 03:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 3ac504d5-d684-3c13-ae40-a36d99bd0f1d | -13.2308 | -51.2048 | 2024-10-01 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 99bd2741-5679-39a6-b977-58f0df843bc7 | -13.2304 | -51.2262 | 2024-10-01 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6de95453-d408-39c1-b71e-4e75a19e24a4 | -13.2116 | -51.2073 | 2024-10-01 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 88638545-ca75-30c2-a572-298740fca4a9 | -13.2112 | -51.2287 | 2024-10-01 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 607ee182-75c5-3b26-b328-dca8ea211c3c | -12.9925 | -62.6976 | 2024-10-01 03:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1c714e30-87db-38b2-a586-e5af11ce7e3b | -14.7406 | -48.7498 | 2024-10-01 03:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| be958927-c3c3-34c3-906f-5beb08197cae | -15.9127 | -57.1733 | 2024-10-01 03:26:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 6569d639-2f61-3d38-aec0-c4d4262a335b | -16.3712 | -50.0992 | 2024-10-01 03:26:37 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 6e91182b-6b88-3908-a923-9de93006795f | -16.3708 | -50.1213 | 2024-10-01 03:26:37 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b17914a7-3d5a-3845-bb8f-88a328638483 | -16.3515 | -50.1024 | 2024-10-01 03:26:37 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| bb67fb4b-46a2-3d2e-94c2-470cd2ad4fe6 | -16.6459 | -55.1908 | 2024-10-01 03:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| d7c0b6aa-deaf-334a-81f1-f2cf9a32c45d | -16.5134 | -57.3305 | 2024-10-01 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 50c72597-10e3-3f8f-9b53-309ffbb9fb8b | -16.5131 | -57.3509 | 2024-10-01 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| bea635f6-83ea-314c-b35f-12b967bb72d9 | -16.4939 | -57.3327 | 2024-10-01 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 0f0b5dfe-2112-346f-9bbc-4fd82a203504 | -16.4935 | -57.3531 | 2024-10-01 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| ad41bd77-98f6-3cf6-b8c0-c7aa21fe02d4 | -16.4743 | -57.3349 | 2024-10-01 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 5d0e1866-26d1-3aaa-b969-4a297e64b53c | -16.474 | -57.3553 | 2024-10-01 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| be500b02-b095-35ed-8ca3-a3088b4c67cb | -16.8983 | -57.6949 | 2024-10-01 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 995a035d-c5d5-3936-8eba-79c89bb70004 | -16.898 | -57.7153 | 2024-10-01 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| fabd14ce-68da-37b3-a055-48a4b04379df | -16.8787 | -57.6971 | 2024-10-01 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| a3bf2581-b842-36ea-b404-7ce5bdf3cd92 | -23.0793 | -45.3951 | 2024-10-01 03:27:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.8 |
| 9b34a4db-e081-3153-b88d-ef7994658132 | -19.05625 | -42.94769 | 2024-10-01 03:28:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3c7914b5-289a-3372-987b-98a2c5ce0c2f | -19.05558 | -42.95086 | 2024-10-01 03:28:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d15f5215-f9e4-3956-b2c8-d5bea6c3ef99 | -19.05031 | -42.9498 | 2024-10-01 03:28:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 01049883-4295-3330-a3d6-1005bb93371c | -19.04576 | -42.94538 | 2024-10-01 03:28:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a0322df9-ec06-30ad-a7df-4805c83caffc | -20.81836 | -42.31983 | 2024-10-01 03:28:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 22afbf71-1c14-37a7-bc6e-75db325c15da | -20.46532 | -42.95054 | 2024-10-01 03:28:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 081b9319-e59b-3c8b-8399-8d4abdfd08e4 | -20.46086 | -42.94639 | 2024-10-01 03:28:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6d5ecf6a-3dce-3334-b4d8-bc8151bd7529 | -20.19067 | -43.51783 | 2024-10-01 03:28:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d032aa2d-9acb-312e-8275-b16fa28b07de | -19.89481 | -43.16277 | 2024-10-01 03:28:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c0ea3689-a65e-3053-9183-156e51f34602 | -19.89413 | -43.16593 | 2024-10-01 03:28:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a145005b-685c-3ad0-8ff8-cc217170da8e | -19.8896 | -43.16147 | 2024-10-01 03:28:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0a89594e-6dc2-3f85-81f4-cfb01dbdfdc5 | -19.88895 | -43.16449 | 2024-10-01 03:28:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cdf3491f-c859-3c4e-a68f-02fc0ffe25de | -19.8844 | -43.16013 | 2024-10-01 03:28:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad41ac6e-4950-3cd3-8bf2-0798eb306f5f | -19.88373 | -43.16324 | 2024-10-01 03:28:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee240bc0-7307-3d9e-9bb1-f2eff14c4634 | -19.79505 | -43.17036 | 2024-10-01 03:28:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6a018d48-e56c-38fc-a854-4d8f27df6bcf | -19.79041 | -43.16637 | 2024-10-01 03:28:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| b72b266c-0cdd-35a5-938a-7e9b778885da | -19.78971 | -43.16964 | 2024-10-01 03:28:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| da8eaa56-2379-3821-a191-79652d6b4993 | -19.62668 | -42.83309 | 2024-10-01 03:28:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ba098452-bf9a-30f9-8d40-d96b36a88eeb | -19.53891 | -43.11937 | 2024-10-01 03:28:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 64206731-4668-3492-82ea-0246eb53dc43 | -19.53795 | -43.11955 | 2024-10-01 03:28:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 26ec3191-500e-3abb-a829-68cc62d97cf6 | -19.5185 | -42.87906 | 2024-10-01 03:28:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 18aaaf93-c6a6-35a3-890c-040cd847d881 | -19.51277 | -42.88052 | 2024-10-01 03:28:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 995166dc-0959-3998-8221-450220a5aae3 | -20.99814 | -42.60223 | 2024-10-01 03:28:00 | NOAA-21 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 53fd39a6-7e0a-3b70-bbaa-3dd4c85c6675 | -22.9462 | -42.89947 | 2024-10-01 03:28:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2f654bc6-3a4e-3114-aea9-0d1da1e54125 | -22.67454 | -42.85926 | 2024-10-01 03:28:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c029acb8-9ab6-332f-baaa-3cd62ef41cd3 | -22.61777 | -43.67158 | 2024-10-01 03:28:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a8606266-abbb-3fe7-a0aa-d680335436f3 | -22.61705 | -43.67488 | 2024-10-01 03:28:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c5c3f53f-75a7-36fa-b01c-a36e7ee7dc9d | -22.59925 | -44.0288 | 2024-10-01 03:28:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aa3aa4da-5c29-30a1-bfd9-515b16d3288b | -22.594 | -44.02766 | 2024-10-01 03:28:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e0199a0-6701-3710-b078-344abfdc9051 | -22.50848 | -43.84356 | 2024-10-01 03:28:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 4b9aa230-5e3b-3e86-b372-18ec340e3035 | -22.50615 | -43.82932 | 2024-10-01 03:28:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1411d5a9-d98c-35f5-a7d0-95e7a212943f | -22.50546 | -43.83249 | 2024-10-01 03:28:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2cf44941-42c2-33ff-84ca-742e076c8a68 | -22.50477 | -43.83567 | 2024-10-01 03:28:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ee8ea8ef-bae7-3b0c-b00c-e250e86802b0 | -22.50406 | -43.8389 | 2024-10-01 03:28:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 1a4286d3-a43d-3c6b-80fc-d2a002396032 | -22.50332 | -43.84226 | 2024-10-01 03:28:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b6b6876b-a947-3784-b9c2-ebbc65663ba3 | -22.49679 | -43.54104 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eaef18d8-4416-37b5-a8ee-a62759dd08a2 | -22.4962 | -43.54378 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d0ce1c9-a6da-3e61-83bc-d5d0bef8ad91 | -22.49559 | -43.54663 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 36c049fd-7408-3ddd-ba49-2d9099f845d0 | -22.4942 | -43.54099 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f10f8ce4-d1cd-38ff-9620-7ab0e1a5f00b | -22.49357 | -43.54383 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9556ac80-34d0-35ee-bb21-92f9e7e26ff7 | -22.49292 | -43.54676 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a3e67f3-0c30-3c20-847c-e0b0d74c5670 | -22.49227 | -43.54971 | 2024-10-01 03:28:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8567be4e-235d-35c8-be8c-a2eb244d2f87 | -22.49106 | -43.54284 | 2024-10-01 03:28:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ebb7dc16-a138-33f0-a284-9f35ae9b88ae | -19.2453 | -44.3666 | 2024-10-01 03:28:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 664a7209-25e0-3b80-8a18-e7a16f532500 | -19.24389 | -44.36716 | 2024-10-01 03:28:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73ec5cb0-a3f6-325d-98d4-d6bf1e90b728 | -19.25272 | -43.34962 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4ad4a01f-4f28-35d9-8387-5722607a7b8a | -19.25192 | -43.35327 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4da1a72e-5f2a-37f0-afb8-9b127a68ab62 | -19.25117 | -43.3567 | 2024-10-01 03:28:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |


[Clique aqui para ver as próximas entradas](README37.md)
