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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92ff4bf1-56a3-3aff-9f50-d34951ffa7f6 | -16.97425 | -56.81133 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bb951322-dd85-3a35-a13e-e15ace7ba29c | -16.97378 | -56.81565 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d1daed4f-73c1-33f1-8e6d-ea9ede23553e | -16.97333 | -56.80915 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d3c32925-d891-3c76-878c-944b9f599bcd | -16.97289 | -56.8135 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e02dec76-70b5-3f98-9e22-21047de80a5a | -16.96885 | -56.80636 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33f92e3a-419f-3517-93a4-25739c0c5ca3 | -16.96858 | -56.75351 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cab98481-41d7-396d-a934-92ead6ac9d32 | -16.96838 | -56.8107 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 16ab130e-7923-3293-a66a-27c834269190 | -16.96811 | -56.75787 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 928570ce-2d6d-3f79-8e12-25bcda33df9a | -16.96791 | -56.81503 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 621c80d7-6908-3a33-856f-c446a5875e7d | -16.9679 | -56.80415 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db3d9836-19dc-36ba-9064-8b983644b85d | -16.96765 | -56.76221 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f9c7c6a8-ef58-3186-8e34-07f735f99395 | -16.96746 | -56.80849 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fea0a4a4-a9e0-3f0f-b1a1-89726f6c2f47 | -16.96718 | -56.76657 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 19434733-da81-3b86-84c0-02c8f132e2b0 | -16.96703 | -56.81284 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1e316edb-72ed-3986-b339-6ecda2791f1b | -16.96683 | -56.75554 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3c27bb87-3877-3fd9-9aa2-f7aa10d48c9f | -16.96639 | -56.75989 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b015b4c8-1c41-30ec-a95d-da6454833d64 | -16.96596 | -56.76426 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ba2a4be7-78cb-392c-adda-01db584671cf | -16.96552 | -56.76863 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 036d7887-c6df-33eb-aa52-e96ee616996c | -16.96223 | -56.75722 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9bc846ee-a885-333e-b095-96d0230c0956 | -16.96176 | -56.76156 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f6fe9611-882b-37da-a906-70b244d45744 | -16.9613 | -56.76593 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1891e996-98e9-3355-b610-2bb407ecac54 | -16.96083 | -56.7703 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c786fcd7-8bef-339d-91c7-355c73d37506 | -16.96007 | -56.76359 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6903b6f4-a342-3d20-8fea-2cc3f354bb0d | -16.95964 | -56.76797 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e6f3a9fa-46ca-33bd-a72d-f543c163cc2c | -16.85196 | -56.74137 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e344165e-90eb-3b21-b77c-b17794a15044 | -16.8515 | -56.7457 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 26af7eff-2b40-3bdd-937f-e72d526c75b8 | -16.85134 | -56.73587 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 95ac3d90-c2e5-3fb5-bff4-057eb04ce25a | -16.85091 | -56.74022 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ee511bf5-338a-3ffe-ae4d-ec7f27f2ba5e | -16.85048 | -56.74456 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0de69c00-7162-35c2-b645-71f2707bff94 | -16.84654 | -56.73637 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 593fe0c2-c081-37dd-b189-fd1e5fd1e77e | -16.84608 | -56.74071 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dfefc0cd-7386-3cf6-bf9e-15ae386f2145 | -18.89054 | -57.74311 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fa3dc82d-aab7-3133-b5dd-699c57cf9d80 | -18.89014 | -57.74712 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8526b7ef-4d3e-3f38-a0b1-c0eebd8ea7ee | -18.8874 | -57.74313 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2ae06515-1b97-343f-b4d2-52ad06efbc44 | -18.88698 | -57.74712 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 592252f0-cf47-319a-99fe-c51375b42dca | -18.88488 | -57.74247 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 14692871-506b-33e4-b1ce-fb961358bfd0 | -18.88449 | -57.74648 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7306ce9b-9b16-3c85-b7fa-5e03e422431e | -19.1072 | -57.51092 | 2024-10-07 05:44:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cb778237-5abf-3d80-97a1-f1e13a91d48c | -18.71579 | -57.3045 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 154135a6-9c38-3c01-97f4-33061561909e | -18.71558 | -57.30313 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c72c6937-ab35-3439-a8c6-25c6f05c575b | -18.71515 | -57.30738 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3add51cf-8b11-3ac6-a711-24867a676e8d | -18.71367 | -57.26543 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 5ae79d25-ca2d-3583-bcab-93c959d6e42c | -18.71328 | -57.26842 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 051b9a78-78d9-3d7e-b730-f188a70a91bb | -18.71325 | -57.26973 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 0cebac3c-483c-3037-8024-4ab093982b26 | -18.71121 | -57.29111 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 91177ad4-0beb-3b37-a80c-25ac02ddbc01 | -18.71065 | -57.29402 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f2dd50df-9856-31d8-8264-431cd91a8381 | -18.7079 | -57.26352 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0bcb9619-145a-3583-8646-c7c9a3b4d125 | -18.70785 | -57.26479 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0ec50681-2b39-38fd-8597-ffa56dc75f07 | -18.70747 | -57.26779 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a737252c-76b5-34ba-9bf9-29507cbf50d1 | -18.70209 | -57.26289 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6b080222-fd22-3675-a6b1-62a39e67f066 | -18.70203 | -57.26414 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| caa8fbec-df79-3646-914d-c662a351fd47 | -18.70165 | -57.26716 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 41280b04-a586-3277-9986-00ac44cf8be2 | -18.69628 | -57.26223 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0ad5a244-9902-30e4-a7f3-63c02de120a2 | -18.69089 | -57.25733 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cece5e75-1ece-3e93-b9cc-9bde05fa4fc6 | -18.69046 | -57.26162 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0d5e7f8b-db39-3043-8da8-39db749a0626 | -18.67344 | -57.25541 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7033cae9-17f9-3599-b64a-8a70a3605dc0 | -18.66762 | -57.25477 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 470c58db-81e8-33da-a16e-0ad386126591 | -18.66223 | -57.24985 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0d9edc1f-b4c6-3089-a2a5-93ffbb3fd765 | -18.66181 | -57.25413 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1bcbe00e-56b4-3280-bb40-2f4964930443 | -18.65641 | -57.2492 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c333730a-eada-342e-a9cd-c7661fddf6a7 | -18.65102 | -57.24426 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5f18fb6a-4e2d-3515-80c6-c60d508b701b | -18.6506 | -57.24854 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| ab391eff-a09f-3cd3-b238-66e7562956b0 | -18.65018 | -57.25282 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 71bf5805-9263-3e26-ae39-2724bfea5d4f | -18.64478 | -57.2479 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 043526eb-fa1f-3689-b8a8-a58a7ad923d7 | -18.64436 | -57.25217 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0bf888d8-08f8-3391-9004-a5a7374baf94 | -18.64394 | -57.25645 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 42e2eb40-6099-373e-93e2-b7daa4958aae | -18.63813 | -57.2558 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 296518a5-de78-3adc-ae5b-dad5a9afbce1 | -18.63771 | -57.26009 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1d144afd-a760-3e7d-a6aa-cc13ef386fcd | -18.6319 | -57.25943 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 210a56a9-e7c6-3b74-b825-a55a44a320c0 | -18.63148 | -57.26371 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 0a8ddff3-1a06-3116-904e-5e69618d7c6e | -18.63106 | -57.26799 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d4571117-669d-322c-a0e1-9f76d230d1da | -18.63065 | -57.27226 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eeca8380-d737-3b36-981f-fba5cd67fbd2 | -16.6192 | -57.14895 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bfad1694-42f1-3da0-88c4-8b612e0c4dcb | -16.61875 | -57.153 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3a4f7ccb-5267-35c0-91b0-fca9e7ebb4c3 | -16.61657 | -57.13782 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 588235cb-4e8d-3371-9fb5-386563435dc6 | -16.61615 | -57.14189 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b51539d3-a914-3a79-bb0b-b2b2d665a4dd | -16.61573 | -57.14595 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 64333251-b5c5-3a44-b2a7-cf00f6b972ab | -16.61531 | -57.15001 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ac65d375-aefa-3c22-aa0f-5b3abcc28b8e | -16.61489 | -57.15406 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 661cff05-87fa-3944-a517-38e58e3b9c15 | -16.61483 | -57.13614 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 29705afa-ce03-39b0-bfc1-2844d835b643 | -16.61438 | -57.1402 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 90c7304d-f556-3428-8280-0e763ce0c2bb | -16.61393 | -57.14425 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 5d07f182-9646-36c0-a35b-8b180bf5b1ca | -16.61348 | -57.14831 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 5cee3855-b5b4-3525-acda-e82a094f969e | -16.61303 | -57.15235 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a801878e-36ed-37c9-abb2-1515476f6eb0 | -16.61259 | -57.1564 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f37c9299-f221-3e09-b47f-fbaf27665364 | -16.61043 | -57.14123 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 74e745f8-6a72-3ecb-979f-8f5cb0c4632b | -16.61001 | -57.14529 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 27a3466f-beae-305e-bd84-3fe910f0a711 | -16.60959 | -57.14934 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4bdc3a23-c7d6-3253-8756-02da1132fb68 | -16.60918 | -57.15339 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a048d2f0-b8e4-384d-851c-d2851142cb20 | -16.60866 | -57.13956 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ee5323c3-7e8c-3c26-b90c-b9cb4030a26b | -16.60821 | -57.1436 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e6d03000-e159-3187-bd70-99d549c80430 | -16.60777 | -57.14766 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3fa6cd22-95f5-36ba-9e40-868b4a1fe83e | -16.60732 | -57.1517 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 013f056c-c0bf-30f6-81ee-dd8400a6fb80 | -17.11896 | -57.37545 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 459c2c81-c519-34f2-aa1b-a10d059b8d25 | -17.11616 | -57.37196 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef36ecd4-88cb-37f9-b43d-8471100978f1 | -17.11575 | -57.37596 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d61ee8cd-9408-3f7b-8d03-4ed13a6496fa | -17.11535 | -57.37993 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6938341f-5fed-3802-af0c-fb47b3aabaaa | -17.11373 | -57.37085 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f28ce819-b7ab-33e5-a97a-7d4966be1d09 | -17.11329 | -57.37482 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e493621e-0d1b-3a80-bb1d-3097c5ebcb77 | -17.11286 | -57.3788 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README138.md)
