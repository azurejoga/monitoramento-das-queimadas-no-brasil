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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f66cf31-4de4-383f-bde8-afe8cc6b0245 | -14.44673 | -59.98008 | 2025-11-19 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08aa19cb-ba01-38e5-bef6-fe1e0c4305ee | -9.36982 | -48.41568 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35805c27-1d3f-3ef1-a842-df5d7a07759c | -9.76261 | -55.62196 | 2025-11-19 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad45ec4c-5d43-3b24-824d-f55118388090 | -8.13084 | -47.5857 | 2025-11-19 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 628e340e-503d-3d07-be43-789a2058f547 | -10.35152 | -48.93278 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12dc4a04-2761-3372-bc37-e04cec88892c | -7.18254 | -48.68227 | 2025-11-19 04:53:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7955fccc-4599-3960-9bf9-1402273f15fa | -7.69454 | -46.85503 | 2025-11-19 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 747812f9-9f09-3c65-9baf-11c9111bbc5f | -15.28327 | -53.15649 | 2025-11-19 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2032e270-4ddc-372c-ade0-d44935883dd5 | -8.87479 | -47.32781 | 2025-11-19 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5138fbb-9f01-32c7-a994-047e4d55ea03 | -10.34731 | -48.90618 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb14888b-ff03-3c58-9381-67362d2c3c0e | -17.61665 | -54.18166 | 2025-11-19 04:53:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f29c40a9-c1bc-378c-811a-562d4362f039 | -10.35196 | -48.90167 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c5de9bd3-ceb6-39ee-afe1-16e9c358bba4 | -9.39796 | -50.68702 | 2025-11-19 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede3b89e-5551-3f65-af6d-88a69781183e | -10.34659 | -48.91123 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f2072f-da62-3b45-95e0-b12cb83e257b | -9.65876 | -43.89521 | 2025-11-19 04:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df7192f5-6261-3b91-8b68-948930461f35 | -9.3738 | -48.41629 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2fdc439-515f-3a1d-adee-12b310ab6e69 | -15.78855 | -58.26297 | 2025-11-19 04:53:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c118a83-b155-37d2-8e9a-24fe0ccd5e3c | -11.61587 | -43.90766 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fdaee04e-8921-3149-abe8-1927bcc49e12 | -9.85091 | -48.90483 | 2025-11-19 04:53:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9076bfc-3cc0-3bf8-b3e7-7f72fe730e3f | -15.00853 | -55.68874 | 2025-11-19 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d472c90-eb2f-30d5-b839-ff2d73d5b066 | -11.6729 | -47.96996 | 2025-11-19 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 834b2655-4365-3130-b49f-9c27940ab1ba | -11.62146 | -43.90837 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 776134e2-6960-3b3d-ba92-f618edbe3ef7 | -6.34101 | -44.22314 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a54963c7-4287-34bb-b1b6-b8db6f87d57f | -9.39924 | -48.45188 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a644db1-30ad-3b6b-9824-85b181c239da | -8.35174 | -50.35964 | 2025-11-19 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 057649ea-368d-3135-bd78-428e51868818 | -17.61331 | -54.18108 | 2025-11-19 04:53:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 473c9f17-2fe0-3d61-86e6-c99ee8493d39 | -9.38425 | -48.4285 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c65002b-37a0-36c1-9932-3a4c44278437 | -13.06552 | -42.13885 | 2025-11-19 04:53:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| bccf1e50-4596-39c2-8f7a-f06f791b0e9d | -15.96303 | -58.23036 | 2025-11-19 04:53:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0597c3b6-395b-3aa9-9802-cb9a50484c7a | -11.01627 | -49.04114 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 043aec92-ac8e-3047-82e1-88ec4a9ee1c1 | -10.53975 | -47.99326 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f1620b-5aa6-3e1e-a3c9-71b37c704cc4 | -10.03032 | -53.75343 | 2025-11-19 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce3f5c3a-84ef-362c-baf6-f2369d14c791 | -10.77645 | -48.84084 | 2025-11-19 04:53:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecdd7e6f-ded8-3642-b615-2c3f42537b9e | -9.38823 | -48.42912 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bf68466-d107-305b-b173-37dc7ce77e5c | -6.31746 | -55.36192 | 2025-11-19 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8ba8c5a-e2a2-3062-9559-08812fa13a9b | -17.80263 | -54.69109 | 2025-11-19 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d778c4a7-5d42-372e-9260-d0b479f25659 | -9.38772 | -48.43256 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85692822-3501-319e-a466-3ce6ed0622dc | -10.83859 | -56.95923 | 2025-11-19 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fa8bd90a-cbda-36ee-a55f-d12cffe63d06 | -18.15611 | -54.55529 | 2025-11-19 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b56e3db-0a25-35c5-9c6e-65aba24501e2 | -17.53215 | -53.70307 | 2025-11-19 04:53:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47284a34-3a44-3e6b-8f5f-a234ae867ce8 | -11.62062 | -43.90435 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec84949c-8c74-32c7-9a93-86ec3e5c1e64 | -16.65247 | -54.57954 | 2025-11-19 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0777d074-908b-3f6a-918e-29d5589dca3a | -9.395 | -50.67909 | 2025-11-19 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0682b5bf-d936-3c6d-807b-03e6cd008f81 | -5.00732 | -50.91526 | 2025-11-19 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67b937c5-a7dc-36e3-802b-94374128321a | -11.27911 | -48.51001 | 2025-11-19 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28c78d79-81f2-3058-b0ed-47e4e908ede9 | -9.12418 | -61.77493 | 2025-11-19 04:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01e3188c-7a74-37d5-bc49-5b524f0c788c | -7.73295 | -47.25688 | 2025-11-19 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a44e13f-7d8e-3715-8d28-0650db42f96e | -6.31393 | -55.36133 | 2025-11-19 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3b1ba51-9e69-3769-897f-1ce6451d5c11 | -7.83411 | -42.1582 | 2025-11-19 04:53:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5d2bb8ab-f692-34d6-a60c-663bf2946477 | -9.39875 | -48.45534 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0782afd-5c23-3f0a-8e65-0e158fa43fdf | -19.41683 | -45.30496 | 2025-11-19 04:53:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66bc1a98-d8ae-38f8-955d-ad240e453578 | -12.00429 | -49.26619 | 2025-11-19 04:53:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2b5eacc-9949-346c-aa6a-c5ed61828d08 | -10.87434 | -49.5378 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 548cdbba-e9e2-3771-aaaa-d74a13ad7fb7 | -10.54558 | -44.12201 | 2025-11-19 04:53:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c87c947-f138-38f3-b4d5-e585e284b5a1 | -14.57257 | -59.70216 | 2025-11-19 04:53:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 267e2494-ccb5-30bf-8445-f436322a4ea3 | -10.88061 | -49.54835 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fc37cc4-3a88-3669-aa63-732468de85a7 | -5.09116 | -56.1672 | 2025-11-19 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb61dc48-9409-3c55-801c-cfe04d21f94e | -7.73771 | -47.25361 | 2025-11-19 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31d5b50c-a6c8-3e57-9f1e-93fe2a2dd06e | -10.29268 | -48.89585 | 2025-11-19 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2185237-da40-360c-889a-f3e8e2d8a4dd | -9.66422 | -43.89582 | 2025-11-19 04:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 060329cc-4c05-3077-86b4-664978404648 | -9.39713 | -48.45163 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51e4de14-9323-3eae-b7ec-efd6868cdb81 | -9.37032 | -48.4122 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54467614-0a1d-367d-af50-f9e405c7a624 | -10.03045 | -49.20901 | 2025-11-19 04:53:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d8d4b88-61d9-390b-a777-273c0f296f36 | -8.87422 | -47.33178 | 2025-11-19 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a11362a-82c6-3956-b0cc-d416cf5d62cb | -16.66437 | -52.14954 | 2025-11-19 04:53:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e5a6863-1311-3124-9cbe-a2345aaa7ca5 | -11.49918 | -48.23438 | 2025-11-19 04:53:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6974775f-67e6-356a-8c42-9545bd255a80 | -16.20405 | -58.74458 | 2025-11-19 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cda90330-e19b-3f4a-8493-d1bfd6c6faa7 | -15.54407 | -55.23114 | 2025-11-19 04:53:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e582c426-da76-398b-b4cf-7fac74e5544d | -7.73228 | -47.25717 | 2025-11-19 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3b2e358-c6cc-3db6-b3f9-0e4dc430c79e | -9.38722 | -48.43601 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8fb0c363-40fc-3ac2-a83b-dd82ccddecd3 | -15.28722 | -53.15331 | 2025-11-19 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1059d779-6547-3075-b28c-87d4ccff56c3 | -5.03252 | -56.96331 | 2025-11-19 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9539632e-9fb5-3f4a-ba97-df5f714fb6ed | -10.34804 | -48.90111 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77160879-a39d-329d-94b5-c434f7f90dd9 | -11.99966 | -49.27073 | 2025-11-19 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ba4cc5e-76db-3034-82be-fbd808386076 | -9.39503 | -50.6825 | 2025-11-19 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 778d540f-6d6b-3e9b-bbff-104d2d1f3336 | -10.76716 | -48.04015 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 152b0240-8a59-3645-89b5-b291a600398c | -7.78772 | -49.62109 | 2025-11-19 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 225220ae-bd2b-3621-b047-063f48f44c4d | -9.36634 | -48.41156 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f472f08-1f33-3b87-accf-11df2af28f05 | -10.84221 | -56.95987 | 2025-11-19 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 777a77e0-f008-3077-85de-e706c62b4eca | -6.34058 | -44.22626 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75a1b4d0-e03a-38df-bae4-7a605dd34e3d | -15.78808 | -58.26442 | 2025-11-19 04:53:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b68324c-6a5b-3078-a9b6-43ac3df8e55c | -7.45382 | -45.76547 | 2025-11-19 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68499c40-fe55-35ae-953c-e55573bc4baf | -16.05311 | -50.42813 | 2025-11-19 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3037da4-cce2-31cf-b47f-0d68bf0e460a | -9.8529 | -48.80907 | 2025-11-19 04:53:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe0ea847-7090-38a0-8c14-e5be1a18b7c2 | -6.34189 | -44.22874 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aed86b4b-50d1-366a-926a-32bcc18e6d3d | -15.28665 | -53.15704 | 2025-11-19 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3476557e-9d98-3553-b91e-6db3f5e4f578 | -9.38273 | -48.43887 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ecde6a7-8789-379c-b063-f82f959c2a29 | -7.79199 | -49.61742 | 2025-11-19 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71020117-a7b1-35ba-8554-75cd5baa34d3 | -11.61457 | -43.90742 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9cf810c-da2b-32cb-a9cc-5ddcdc21f41a | -11.8605 | -46.96383 | 2025-11-19 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fa17868-6b9a-33b7-a315-a123be6643b3 | -15.96664 | -58.23105 | 2025-11-19 04:53:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c6dcb70-8b49-3baa-af1a-844e2ad1778d | -10.79612 | -47.98457 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b03386f8-082b-3341-8b81-5ef491bb48fb | -10.87367 | -49.54253 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4d0f3d28-8709-32cd-8a70-98b96e794ab8 | -15.42831 | -48.06382 | 2025-11-19 04:53:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da344159-ca95-3809-887b-b3707c8494f6 | -13.06493 | -42.14406 | 2025-11-19 04:53:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8f21a9ce-ec91-3f61-bb9c-d656d7b56b8a | -10.30128 | -53.77959 | 2025-11-19 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22a65ce1-f35d-3926-afca-669aa52c1eb1 | -14.88597 | -54.2812 | 2025-11-19 04:53:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06111205-44ed-312c-9d8e-61271ce58d0e | -9.47645 | -52.1079 | 2025-11-19 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7373bbdc-76fe-3a05-88a2-1d5d6ada50cc | -10.66229 | -49.37093 | 2025-11-19 04:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a3b22d2f-2c76-3f7e-82b9-a3a51b4d2ade | -10.34979 | -48.91686 | 2025-11-19 04:53:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README20.md)
