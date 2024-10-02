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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd8fc5fe-2f6c-346d-8018-0a123aeac678 | -17.09751 | -56.10683 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b46f8564-8ce4-34ac-a639-01f5406ef94e | -17.09117 | -56.11373 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3d5bf726-7000-3bc0-9d23-680d1f3729a0 | -17.08603 | -56.1093 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a2de2216-1518-3ac8-97f2-4ea72057bf6d | -17.08563 | -56.11308 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7fa9be5d-b74a-3bcb-b7d0-a810b8d7b563 | -17.08171 | -56.09734 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 66df65b2-b444-381e-8e94-95a6878fb6e7 | -17.07616 | -56.09668 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b2b26598-cced-3409-942e-e0e9d3a17f11 | -17.07371 | -56.37676 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cb744e0a-acf3-3c53-be21-4c917a04ee6b | -17.07102 | -56.09228 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 14bf37d1-4909-39a9-8a2d-21848aeeb74f | -17.07062 | -56.09604 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 74f4fa21-1cc7-3b0b-a899-e0e4feaaf61d | -17.06748 | -56.38331 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 06b53ea6-1a04-3fad-8afe-e603a500f2b8 | -17.06588 | -56.08787 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f0644292-a20a-3d64-90dc-f4f3c8934ab2 | -17.06548 | -56.09164 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a92704a8-3adb-33fa-993c-2713d8649122 | -17.06034 | -56.08723 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| b620852e-f77f-37a9-be2a-f0d8a6512599 | -17.05994 | -56.091 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b2d81e50-4b11-33fd-ae82-8fbcfff1b07f | -17.05954 | -56.09477 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 20a29594-6e62-397c-996f-65a2e3badfd1 | -17.05492 | -56.09122 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 47434d0f-bc55-3585-b5a6-9840a68a4057 | -17.05321 | -56.10164 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5fcb636e-f2d2-3aeb-aada-82f15100da4f | -16.84301 | -56.08619 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 430b4013-7398-3bfb-ade4-d33b3eef5b56 | -16.84275 | -56.08531 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5b831926-0268-3d0e-8763-36861f6054a1 | -16.83748 | -56.08556 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b29d4add-aa4e-3e4c-a35a-fdb197d694a4 | -16.83722 | -56.08467 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 90c88662-05e9-3412-b56b-8942221fa9b2 | -16.81569 | -55.87505 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 23f9c743-582f-3139-992c-6d32267818ae | -16.81526 | -55.87894 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 33059dce-612a-3bec-afb1-29b36aa71ae5 | -16.81484 | -55.88279 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eafcf985-1b4e-389c-807e-d638be3e0c99 | -16.81443 | -55.88663 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f2023c47-82be-3b21-a591-066ff2856362 | -16.81401 | -55.89048 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 707d5625-b780-32da-a722-b4e70eebf331 | -16.81359 | -55.89434 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 729f487a-4c5c-32d3-a386-2d66eab57cc3 | -16.81008 | -55.87439 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 66f9a3d5-c275-3dfb-920e-aed474bc5eae | -16.80966 | -55.87827 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 24ec6fc6-a500-3907-abfb-cfdd4efb10c3 | -16.80925 | -55.88212 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5a830924-b7d7-3f03-904e-e2c2c78682bf | -16.80883 | -55.88598 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b0ddca49-5e2c-3ece-97ea-c07e6479c87a | -16.80841 | -55.88983 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dbc800ba-7b07-3245-8bb1-69085b6928de | -16.8049 | -55.86986 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| de190ec7-b5af-3ebf-a32a-b883eb2f7705 | -16.80203 | -55.79063 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 68c32376-18ee-3c74-98b4-a5303a35b99d | -16.7964 | -55.78997 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 56a2ad99-6830-3ac9-a3b1-6940ef4f47a1 | -16.78596 | -55.78083 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 20bfddd7-3924-38e9-84cb-0722540c3723 | -16.78555 | -55.78475 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1ad04a01-00b4-301e-a494-21fdfbe7b6ab | -16.72169 | -55.49284 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9b697b61-5ec4-396a-b843-b380f1fe56ef | -16.71508 | -55.5006 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d4a3841a-7d98-329c-a946-5165d8b9222f | -16.70806 | -55.51221 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 978e516d-bfbb-312c-9607-9e9acb8ebeba | -16.70191 | -55.51563 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e3613a8c-a11f-3f33-9b27-47437241a54f | -16.70151 | -55.51944 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 885feabe-b786-3b7e-a3bf-8e2ee4e61e49 | -16.84845 | -55.8866 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bab867c7-3d78-37c0-866b-57984099072a | -16.84802 | -55.89045 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7ef70df2-345d-3ca8-a4d6-91dd8ca67afa | -16.84759 | -55.89431 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ee9fe2bb-b5dc-33b4-9516-65cf85c4fa06 | -16.84717 | -55.89817 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5d79dc51-df11-3189-afab-102e611292ac | -16.84673 | -55.90206 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c2ce6d61-b4d7-3a93-8057-255d46e55deb | -16.8467 | -55.8511 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d64ae6e4-7301-381b-a099-e3cf935df8db | -16.84637 | -55.88914 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f8b70ed5-38b0-3a1d-bb28-c52e176a649b | -16.8463 | -55.90592 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 12df5f75-f5d7-39d3-968b-b5f736625e2a | -16.84597 | -55.893 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 146488fe-fe61-31bb-992d-e239b6b1a9cf | -16.84557 | -55.89687 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d36f6008-9711-3f05-aab7-8fc86b2e09e5 | -16.84517 | -55.90076 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5de7f64b-96af-3091-aeba-feec76a3b0fc | -16.84476 | -55.90464 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 40464c56-5fcf-3a25-950e-a09ce0930f7c | -16.84436 | -55.90849 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7ab2bda7-9e23-37b6-89ae-a227e7882548 | -16.84328 | -55.88208 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3018b3d2-ebc0-3c6a-a4e7-658bb2d03b65 | -16.84285 | -55.88595 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7c6541fa-8758-30a0-9302-0dc4e257a140 | -16.84242 | -55.88982 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b4b682d1-2a0f-38ce-aec6-49e57b845267 | -16.842 | -55.89367 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4ff138ee-1616-3deb-9ab0-53c7fabb566b | -16.84157 | -55.89753 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 98ceea89-d573-333e-9201-f7fe82fc8e31 | -16.84157 | -55.88074 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c2cd59b2-0f66-31ca-b414-58bcc9f87110 | -16.84117 | -55.88462 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ad1b1dd-536b-35e4-9fcb-36f40ca40968 | -16.84114 | -55.90141 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0c0ce9ac-3d6f-3c66-ad4e-66a3c8554057 | -16.84077 | -55.8885 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 90390461-119f-3d51-9f72-5309afe22703 | -16.84071 | -55.90527 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eb674337-13a3-39e4-94e0-872ad25c803f | -16.84037 | -55.89236 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4d21124e-5aef-33a2-9a7c-108541a9cc82 | -16.84029 | -55.90911 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| befd2bb6-0dda-3c23-a8c2-61648730739a | -16.83997 | -55.89622 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 553ab9b8-1e96-3787-a597-5055da61d9fe | -16.83986 | -55.91294 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eb5f5070-f5d9-3dc2-8907-1f22c653ff3b | -16.83957 | -55.9001 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3145d452-c657-37eb-bec1-f5893dad5eb2 | -16.83917 | -55.90398 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 54281995-b084-3ea1-83fb-21eb4ec49351 | -16.83838 | -55.91168 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ae12484c-d45a-3429-a060-5c425acade91 | -16.8381 | -55.87756 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6d674fd1-a1ea-3e95-b64d-20814d105afb | -16.83768 | -55.88144 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4daebb4f-5262-33ce-82c9-7101328ac74d | -16.83725 | -55.88532 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 920a0457-d42c-3d49-80cd-beaa15681b3d | -16.83682 | -55.88919 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 50c7e127-60cb-35cd-8c86-fd66257deb9d | -16.8364 | -55.89304 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b2c907f2-e447-3339-b5a9-5d3b63ca464d | -16.83597 | -55.8969 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a37e8c87-1e67-3509-a207-f77dd5704c7d | -16.83554 | -55.90077 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| de447508-06f6-32f3-b1e9-5e02b97b1c17 | -16.83512 | -55.90464 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c33b0a43-16cc-36ae-8036-1d1bde7fa400 | -16.83469 | -55.90849 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 375cd3d1-060c-3338-a549-31bada4c4f06 | -16.83427 | -55.91234 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6246c0db-32fc-33ba-9d1b-50c80f605c76 | -16.83207 | -55.8808 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 81d9bd76-f0af-3ee6-8017-2ab6e69d14fa | -16.83165 | -55.88468 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b6a513bc-8d00-3cdd-affe-dc61636ebf39 | -16.83122 | -55.88856 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| df61d6fe-e08b-3f96-8847-b121fd83a5ba | -16.8308 | -55.89244 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6ee1cf56-e350-3cb2-86c0-2df7cc5c4e46 | -16.83037 | -55.89631 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8d2033f2-d5f9-3f98-acf6-f754c61694ab | -16.82995 | -55.90017 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1e0757ba-0a1d-3952-8f48-ccc5192cbb13 | -16.82952 | -55.90403 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 8cc1b47b-89e0-396c-82e2-13e7c648cf29 | -16.8291 | -55.90789 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 4981d9b4-f123-3f2d-bf7f-5f0a3dbd247d | -16.82868 | -55.91173 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2f7652fd-f5a6-3769-80bf-bd5bed42eba3 | -16.82647 | -55.88018 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c51fbc66-0791-3455-b87d-7ec1f94df6c1 | -16.82605 | -55.88406 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1c53abee-abec-391f-8522-907089ec49a6 | -16.82562 | -55.88793 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 00ee2f3c-9512-370d-9b7c-f927161a5bfb | -16.8252 | -55.89181 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a2f3c49b-b61a-3fa7-9c05-dd24e4ebaf99 | -16.82477 | -55.89568 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d0ef0f2b-c294-345a-bd91-83e5c6c225a8 | -16.82309 | -55.91106 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 75fef500-4ddf-34b1-8833-dc408ab127d8 | -16.82086 | -55.87957 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c644961c-e83d-31d6-b667-e39a43ada433 | -16.82044 | -55.88343 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2de6928b-5050-3f7c-a9ce-c4dda6b9a836 | -16.82002 | -55.88729 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |


[Clique aqui para ver as próximas entradas](README177.md)
