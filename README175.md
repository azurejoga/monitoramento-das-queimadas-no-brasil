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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65993ced-f20b-3741-b789-62d36b9dcadb | -16.898 | -57.7153 | 2024-09-26 10:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 184.9 |
| fb87124f-e4e3-3a63-aa4a-18d878b5b2fb | -16.8983 | -57.6949 | 2024-09-26 10:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.2 |
| 9d39e96a-5bb6-3fbb-bdb3-1edf5a092e78 | -17.0795 | -56.1736 | 2024-09-26 10:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 50e82be1-21dd-3fb4-9a32-0ec1ee78f008 | -17.0995 | -56.1504 | 2024-09-26 10:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 163.1 |
| ee7cc46b-0031-3755-bf66-561c94fc4d79 | -17.0798 | -56.1529 | 2024-09-26 10:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 3319b2da-ef81-3b08-b766-6fb1a821f916 | -17.0991 | -56.1711 | 2024-09-26 10:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 193.3 |
| c4416ff3-1bd1-3a6f-ae97-3ae76f35ccac | -11.2034 | -54.7752 | 2024-09-26 10:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c3b5f80b-2985-31c7-94a0-a47db07e69a4 | -16.8591 | -57.6993 | 2024-09-26 10:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| b97b67fe-0b1b-3651-9600-a4dd7daeb4a6 | -16.8588 | -57.7197 | 2024-09-26 10:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 224.6 |
| dca9a76c-6c6d-3b2a-a5e2-f740f9e7047e | -16.8787 | -57.6971 | 2024-09-26 10:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 276.2 |
| a98e3858-fd8d-3b6c-a805-7db820f33435 | -16.8784 | -57.7175 | 2024-09-26 10:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 439.8 |
| c19edbf4-fe40-3d58-9e48-264d462c891e | -16.898 | -57.7153 | 2024-09-26 10:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.9 |
| 14085356-cee5-38ee-b738-e03fd06e155c | -17.0791 | -56.1943 | 2024-09-26 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| eb989fd1-c69c-38bc-9045-0aad95f70fcb | -17.0795 | -56.1736 | 2024-09-26 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 142.3 |
| 06ccf6ee-1cae-3b12-bbc9-cd91e0ba44ef | -17.0988 | -56.1919 | 2024-09-26 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 136.1 |
| 8bc19122-3cce-3f06-874e-39f4e4275961 | -17.0991 | -56.1711 | 2024-09-26 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 185.2 |
| ca037e5b-a3dd-31be-8d16-3f6cc62a6fc4 | -17.0995 | -56.1504 | 2024-09-26 10:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| c0e2b1c5-5d15-31bb-82b4-0950b39fdcab | -11.2034 | -54.7752 | 2024-09-26 10:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| df4743c6-60fc-383b-b4f7-0a8b0f1052be | -14.882 | -51.5207 | 2024-09-26 10:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| e6b09193-5632-313a-8e5f-9f66dd2e2459 | -14.9018 | -51.4965 | 2024-09-26 10:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e0dfc02f-3c8f-328f-b8f7-d76679ce13cd | -14.9014 | -51.518 | 2024-09-26 10:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 63b072e6-c685-3088-91ff-5e4f0391a734 | -14.8824 | -51.4992 | 2024-09-26 10:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ac5d0393-cb1b-3975-9163-6ea34680c794 | -16.8591 | -57.6993 | 2024-09-26 10:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 248.3 |
| 7e57107a-b183-3c0f-b636-d5e6ad655ece | -16.8588 | -57.7197 | 2024-09-26 10:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 243.6 |
| 6c8d5be0-9414-38fa-bbcf-e38e7853302d | -16.8787 | -57.6971 | 2024-09-26 10:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 308.9 |
| 94bb0f7d-d899-3e00-b82a-7119e10a0d34 | -16.8784 | -57.7175 | 2024-09-26 10:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 480.8 |
| 417fea72-6d2b-36e1-bc36-ee6ad0633fa6 | -16.8781 | -57.7379 | 2024-09-26 10:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| f12a9ee2-f233-3a04-9ca3-e90c0068932d | -17.1188 | -56.1686 | 2024-09-26 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 123.0 |
| 7823b982-f727-3e13-954e-a9768de270f9 | -17.0995 | -56.1504 | 2024-09-26 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 2977374e-e28c-329a-b7cf-bae0f5f37ee8 | -17.0991 | -56.1711 | 2024-09-26 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 227.4 |
| 6ebf0cf9-01c5-35ea-992f-aa14f918d821 | -17.0988 | -56.1919 | 2024-09-26 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 141.4 |
| b501360c-ae3a-38fa-b25f-1fcea927f504 | -17.0795 | -56.1736 | 2024-09-26 10:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| cd4df5e6-86fd-3dcf-a1d2-276e94517afb | -11.26 | -65.2801 | 2024-09-26 10:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 100.9 |
| bdfbd2ba-52b3-39fb-a084-6ecebd86f4e6 | -13.2147 | -45.6738 | 2024-09-26 10:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| e4a43ff3-a91b-3615-b046-f2190cc68614 | -16.8591 | -57.6993 | 2024-09-26 10:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 211.2 |
| ab4523a8-7f8e-3eec-8efd-6580689cdf4a | -16.8588 | -57.7197 | 2024-09-26 10:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.8 |
| 20280e8a-657d-39d2-a6ac-1f4e3125f085 | -16.8784 | -57.7175 | 2024-09-26 10:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 436.6 |
| 3f6cd275-12f5-3521-843a-5bf73908e6dd | -16.8787 | -57.6971 | 2024-09-26 10:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 287.2 |
| 92f02af6-5deb-36be-8e5a-6be12ca851f5 | -11.2034 | -54.7752 | 2024-09-26 10:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 9d0369fb-0306-30ea-bcb9-ce53e3b61f1f | -13.2147 | -45.6738 | 2024-09-26 10:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 198ebd0d-0cbe-3bf6-b563-24b761d20864 | -16.8588 | -57.7197 | 2024-09-26 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 207.8 |
| bd151a6a-7046-303a-887f-cc3b1670280f | -16.8591 | -57.6993 | 2024-09-26 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 224.9 |
| 8224eca0-ad82-34b3-9646-2082017ff3aa | -16.898 | -57.7153 | 2024-09-26 10:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.8 |
| 478fb910-f65e-33ff-8f2f-59109ec709b0 | -16.8787 | -57.6971 | 2024-09-26 10:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 275.8 |
| cda32d99-8caf-38c7-976a-c2575affd9ac | -16.8784 | -57.7175 | 2024-09-26 10:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 402.5 |
| 5881bd2b-c529-37f0-bb0f-54e6cb961cce | -10.0327 | -53.4448 | 2024-09-26 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1059.3 |
| fc30412d-d673-36f6-8707-6c3cddc1776e | -10.0324 | -53.4654 | 2024-09-26 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1289.6 |
| 078f13a8-ef9c-314e-97ed-438700dca3a7 | -10.0322 | -53.4859 | 2024-09-26 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1470.6 |
| ad1f486d-6cc4-3ea9-935d-db08f2313368 | -10.032 | -53.5065 | 2024-09-26 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 465.5 |
| ab111334-ca40-302d-a988-823a9ac0c04b | -10.0508 | -53.5049 | 2024-09-26 10:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 192.9 |
| 649bb4ed-c2c0-34b3-a763-f91b1268a4ed | -10.6452 | -45.8635 | 2024-09-26 10:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 331.6 |
| 275feced-f302-3ea2-bb0f-17ec29521c62 | -10.6449 | -45.8862 | 2024-09-26 10:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 420.7 |
| 29de12ef-f70d-34a7-b7e0-9bb24a7bc3dd | -10.6262 | -45.8659 | 2024-09-26 10:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| a7e35e65-c6c3-3aea-bef0-36fb8c29b462 | -10.6258 | -45.8887 | 2024-09-26 10:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 09d262bc-16ec-3795-9baa-e2a5c0ae5c98 | -11.2788 | -65.2793 | 2024-09-26 10:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4418e1d2-56ca-396b-97cc-9a2b7ae19972 | -12.8852 | -51.269 | 2024-09-26 10:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c85af4ea-4003-3858-baf6-3de753bcfe16 | -12.8848 | -51.2904 | 2024-09-26 10:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 062968b8-dfb7-356e-8d70-b8d4ba59a6b8 | -12.8657 | -51.2927 | 2024-09-26 10:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d9203766-5511-3495-87a4-14e0ff89bf6e | -13.2147 | -45.6738 | 2024-09-26 10:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 9c75d530-f871-37d9-8490-62ee349b5f59 | -16.8591 | -57.6993 | 2024-09-26 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 211.2 |
| 04cd777a-c9aa-3c3b-8fe6-95a915f572e6 | -16.8588 | -57.7197 | 2024-09-26 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 228.4 |
| 21639ded-95cb-3176-a00e-cb0f540f8bbf | -16.8784 | -57.7175 | 2024-09-26 10:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 369.1 |
| 68e93a45-63c6-3a08-b114-51274580c513 | -10.65 | -45.91 | 2024-09-26 11:04:24 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31b697f3-d97e-3c97-892b-2d171f6c91ee | -10.04 | -53.55 | 2024-09-26 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df822332-9d1c-3f15-a80c-9f95a211977a | -10.01 | -53.48 | 2024-09-26 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1c7b808-e1c1-3f37-8f2f-f1851bf6dae2 | -10.04 | -53.48 | 2024-09-26 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65e003d7-75e0-37ef-8bd5-e00bf1498da9 | -10.04 | -53.42 | 2024-09-26 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3871c49-6d07-3b8a-9191-9f04a1f24400 | -11.2224 | -45.5131 | 2024-09-26 11:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| c28c98c2-c5cb-37b7-a907-7c922eb93589 | -11.2228 | -45.4902 | 2024-09-26 11:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 75da75c9-1f93-3157-a6cf-3137b7b48120 | -11.2034 | -54.7752 | 2024-09-26 11:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 3e099303-d2f0-312e-b2f1-b254c1e09833 | -10.6262 | -45.8659 | 2024-09-26 11:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7945cb65-f089-34b7-806b-8e5ce0496ee3 | -11.2224 | -45.5131 | 2024-09-26 11:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 72a2c5e4-c5b0-306b-a78d-d1966ff8956e | -11.2029 | -45.5387 | 2024-09-26 11:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| c84f910f-91f1-3dc8-b700-04f3cd18c00c | -11.2034 | -54.7752 | 2024-09-26 11:16:11 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 24ccdd31-33be-33e7-a51b-29dc8277ea85 | -11.26 | -65.2801 | 2024-09-26 11:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f47b9003-7ecf-381e-9e40-3f75b9e32e50 | -12.8657 | -51.2927 | 2024-09-26 11:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e07265a6-d8b4-318a-8ca4-edab725f5585 | -10.032 | -53.5065 | 2024-09-26 11:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 229.6 |
| 58feefe9-8c3e-3c79-b511-8de037a67b6e | -10.0329 | -53.4242 | 2024-09-26 11:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ec381935-67ef-314f-a3a0-5907aa221e71 | -11.2034 | -54.7752 | 2024-09-26 11:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 45a484f8-08ab-32b4-a716-5e49c850c2b3 | -11.26 | -65.2801 | 2024-09-26 11:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 82cbffbc-ad67-3b81-a87c-5937720d00b3 | -12.4612 | -47.9774 | 2024-09-26 11:26:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 80f922ed-980e-3aac-ba88-92f844f8da1d | -12.7911 | -51.1739 | 2024-09-26 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 5c78a606-1cf0-3bdf-b450-305f936c005f | -12.7914 | -51.1525 | 2024-09-26 11:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 98a3b298-8147-3b7e-86d1-a484f7842184 | -14.1582 | -47.816 | 2024-09-26 11:26:26 | GOES-16 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 143.4 |
| ed2fd5d6-7435-3f1f-ac2e-c1880922f5dd | -18.9102 | -49.1674 | 2024-09-26 11:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 461a01ca-d24f-3e65-a530-0b630a0e3dd5 | -18.9096 | -49.1902 | 2024-09-26 11:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.6 |
| bf2b08d3-306c-399e-af98-fe7a9fb4cd28 | -20.60253 | -41.21967 | 2024-09-26 11:34:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 408571cd-29f8-3c0b-9425-bfbc08a8eac0 | -8.8579 | -44.9608 | 2024-09-26 11:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 84dfd3ab-c00e-3528-8f10-f4f081b4ed76 | -8.839 | -44.9628 | 2024-09-26 11:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 7c7ef6c7-8930-3634-bcc3-36377a748ceb | -8.8387 | -44.9858 | 2024-09-26 11:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 301.8 |
| 0932e3b8-aa3e-3dc0-b645-535fe9ff1f1a | -8.8576 | -44.9837 | 2024-09-26 11:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5b849d02-ba16-3a09-a7f4-8bfb21a60372 | -10.0136 | -53.467 | 2024-09-26 11:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 42003b9d-1d3b-3d88-9c0c-9d7b88e3c58c | -10.032 | -53.5065 | 2024-09-26 11:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 236.6 |
| e9926fde-2199-325d-97a8-668520a74307 | -10.8348 | -45.907 | 2024-09-26 11:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 915fd91f-9725-33f1-9fda-ed835047197b | -11.2224 | -45.5131 | 2024-09-26 11:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 3cafd703-64b8-3cd2-afcb-70b78146a8b0 | -12.2179 | -45.4844 | 2024-09-26 11:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7d1a6872-de96-37b4-b4e3-41e5b9b6a65b | -12.2367 | -45.5045 | 2024-09-26 11:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 289d4bf5-b869-3edd-99c6-04c1d2db0696 | -12.4612 | -47.9774 | 2024-09-26 11:36:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7dc50e29-ef92-3c27-82bf-6b14a6bff530 | -12.866 | -51.2714 | 2024-09-26 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f846fbf4-6482-3eaf-bdaf-16871f707b4b | -12.8657 | -51.2927 | 2024-09-26 11:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.0 |


[Clique aqui para ver as próximas entradas](README176.md)
