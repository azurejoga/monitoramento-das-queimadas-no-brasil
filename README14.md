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
| 0e6eabb0-dd68-30ca-80dd-b09c98750bc4 | -2.63326 | -46.16514 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18fe0dd0-d173-39c7-8e8a-9ed42acfa4a0 | -2.11974 | -50.69419 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 03df2e9c-59ee-3453-aa62-35102dd633b8 | -3.25301 | -49.89401 | 2024-11-12 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d01d7da4-e242-3290-8c16-416e35ccc06f | -3.16398 | -50.44861 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 798ba919-fc7e-3488-8f22-6d122ea99ddf | -2.12327 | -50.69859 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| cae47aa7-3115-361b-8ced-ba577b00463c | -2.86844 | -47.90594 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9298ed6-350f-3ed5-93e5-c28a10faade1 | -3.34924 | -49.15137 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c24280bd-6132-3964-9c34-3644583203fa | -2.74561 | -45.99125 | 2024-11-12 04:25:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d9de439-9c3f-39c9-ba77-1443da1258f4 | -2.13565 | -50.70057 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 407d1532-1fa9-323e-932f-c5ff699a339a | -2.77894 | -50.29789 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c98d4a45-ad63-3d03-9214-0a508f0cc450 | -3.21429 | -50.38955 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d5f2405-a8c4-3855-b765-9371921f06f0 | -2.91667 | -49.76528 | 2024-11-12 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c10e6cac-e54d-32d5-9538-7e6bac0b1818 | -3.24551 | -48.74495 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 923b937a-0e1d-32cf-b2a1-54f813564a26 | -2.63491 | -46.15474 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6be6049b-1a52-3872-b4e2-282101ecdb44 | -2.77785 | -50.30476 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e2c3d70-cdc3-38cf-a5b6-24bca3b1ff81 | -2.21383 | -48.37791 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bcb2b796-b3f9-3130-a9c7-0bae01d9ea89 | -2.6555 | -46.82047 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab051a22-a672-3aef-a0a6-650dacd829c8 | -2.15321 | -50.91238 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4456313-b85f-3dc5-97b4-895be6463f34 | -2.62995 | -46.16462 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf19d5c6-f32d-377a-bfdd-79560031e407 | -2.2329 | -46.43897 | 2024-11-12 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af36bfa-b34c-3161-8ea4-64aef6ccab06 | -2.64878 | -46.81939 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12a9d186-deba-3817-b8d0-44b4a25451a7 | -3.04904 | -50.33731 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56ae5d34-90b0-3e66-bb2e-de4269c14d22 | -2.11149 | -50.6929 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8adf2469-6cd5-3bc8-b93b-3a1302d6a998 | -2.68971 | -46.82205 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83445cf9-a718-3d00-b3a6-cfd8316804a6 | -2.35941 | -48.95303 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e38e80b-9919-347e-91fb-abfb465bb745 | -3.0783 | -49.36555 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e89cc5e9-38f5-3199-b885-8579cda2309b | -3.67072 | -39.57854 | 2024-11-12 04:25:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6998e06-f16b-3f9a-b243-5113e276e4c0 | -2.65106 | -46.78324 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73690940-2922-338b-a48b-4c5229aa3358 | -4.06301 | -43.95291 | 2024-11-12 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c82668fb-0495-3ba8-a6bc-a64da6ac0bf3 | -2.72646 | -51.73734 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d07aac63-dc18-3ebf-891b-eb4831115a6f | -2.46467 | -50.39289 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 127a95ae-5537-3b1d-aad8-1b4bc91877b3 | -3.02527 | -47.98574 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63dc8130-6418-3288-b971-52a8a58eea49 | -2.13978 | -50.70122 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32436f6f-066d-39ce-b4c4-d94e16dbd670 | -2.65158 | -46.8235 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 185088b6-b83e-336b-8ef2-09774873b2f1 | -2.69026 | -46.8185 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0a9259b-7d4d-3517-b200-07d4db7bbe64 | -2.83263 | -46.64837 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c91ea14c-186c-3e7b-839f-30271d0de964 | -3.13145 | -50.44686 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dee52cf-9aa8-3522-b04e-84da1465bb78 | -2.13271 | -50.69249 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| d0baf664-0f31-33df-9228-d931dd2629ba | -2.78763 | -51.75057 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aaa5bee-1613-35c1-8a33-dcf45fb3e49e | -3.54168 | -40.37302 | 2024-11-12 04:25:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c42149d-5444-31b0-b7eb-4f67519899e3 | -2.65778 | -46.78428 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193096b2-6523-3fdf-ac2a-4ca8adfb9ffd | -2.6981 | -46.81248 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ec043d09-c247-3945-a6f3-04ad6b4838f6 | -3.13315 | -50.43647 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 036f4ad9-0ed8-3365-87c9-cd54f0144754 | -2.23479 | -49.88116 | 2024-11-12 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6c564dd-90f6-3679-ae3f-28bcdd666cba | -2.78237 | -50.30197 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e67c32ad-fa21-3e3a-869c-247f2b931fb6 | -2.11622 | -50.68983 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93329074-6e13-33ca-9752-71cf410a9631 | -3.12859 | -50.43927 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6219cd3-5148-3586-9872-a675b858ee71 | -15.88809 | -43.45891 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 18603db7-7804-3590-949e-fb15c7e219fb | -2.62885 | -46.17155 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a521cc84-2ed8-397e-ba3f-a22371187706 | -2.12146 | -50.70978 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 904b85e0-98fc-3aa7-8a11-efff672cdfca | -2.59871 | -51.7195 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4eff5d67-1960-3e70-aba7-522a07d28a97 | -14.79321 | -42.71817 | 2024-11-12 04:25:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7d17e0e-6d25-3ec2-a0a3-6f8a2dc72436 | -2.65607 | -46.81689 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1162181-4492-30b8-b348-280f2ceffe0d | -1.8623 | -48.01174 | 2024-11-12 04:25:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89b6bb0-7910-389b-ab5f-2d37c00078fd | -3.12802 | -50.44275 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bdc1144-7405-3f01-ba13-8c70676dd764 | -2.80419 | -46.65479 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e21f287b-434f-3fff-8ec6-b9a760c34b1f | -3.16204 | -49.7361 | 2024-11-12 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fcb500b-1a06-3492-8b5e-322d351b1e00 | -2.12213 | -50.67941 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 480a0eb7-59c3-38b4-b330-364fc892bbda | -2.11854 | -50.70168 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52519c07-9882-3221-abc9-519be0bcfb6f | -2.65887 | -46.821 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d38b6add-043e-3c6f-97ec-1f1707b8af89 | -2.12755 | -48.95096 | 2024-11-12 04:25:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b1296fa-a55b-3c1e-9fb8-9ae1dda77cc6 | -2.82483 | -46.65438 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 988cf85d-15ca-3538-86aa-de2c25260e2f | -3.24978 | -48.74137 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde22b27-388c-314d-a97c-d825cd8286f4 | -3.00349 | -49.11084 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f65895b-79fd-3924-8527-bf47f71cae95 | -3.16343 | -50.45204 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c415af1-e103-3c99-a70f-4a6781cd694e | -2.784 | -50.29166 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73dfa905-78fd-31e8-bc40-8774ba545d2e | -3.48039 | -48.24573 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e79b36a4-e071-3c49-beee-7aa475678190 | -2.6294 | -46.16809 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b9c07d4-2112-3fa6-90ef-8810e73167c7 | -2.69473 | -46.81199 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a4ba3571-2e06-35a1-aa7a-1f3738fa7190 | -3.26369 | -48.75532 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1734e864-c7e1-3d74-8434-c42ce7fb2ac6 | -15.89365 | -43.46359 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 35380a65-e16c-33d4-b261-1923ff094646 | -2.6331 | -46.80963 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2b832c1-4bc4-38ef-8c48-a818db0451ac | -5.12673 | -37.85987 | 2024-11-12 04:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d77d45b7-2bb7-3b51-a6ee-c28bfadab1e9 | -2.82204 | -46.65033 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5ed15cc-43db-3502-a68a-3d6c9e6537d2 | -2.12566 | -50.68375 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36df7ebc-ea4c-37a6-96a5-89a8ef3b1473 | -2.23968 | -49.51876 | 2024-11-12 04:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9afcfdef-a64d-3373-b0c7-d00454569457 | -2.45429 | -48.59079 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b922834-6fbc-3866-bb20-571afb2f7968 | -2.91587 | -49.81908 | 2024-11-12 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d1f7f21-a2d6-3a3f-a4a4-5da887aed191 | -2.53068 | -46.31994 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a327050-2ae8-3c69-87cf-ee8ccb6ae8ae | -2.64233 | -45.9787 | 2024-11-12 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7103ee99-c3f9-398d-8453-1f6caa6667b0 | -2.63436 | -46.1582 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de6b1f4e-3882-3873-ba60-d59acd7a51f5 | -2.6012 | -46.17434 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80f680cd-f8b5-379b-9f49-21d0551245ce | -3.03232 | -48.0546 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b0d71a-99a5-357b-989b-7a9006c4099b | -2.17016 | -48.32904 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e128eaf-9321-304c-b2c1-9fafdfaeface | -2.19101 | -48.38271 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27295be4-59f6-39a4-a7ad-5128abb67388 | -2.48466 | -46.35217 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3499f914-598b-3c72-b695-12c306215934 | -2.7773 | -50.3082 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05077364-3038-3072-b52a-5175af0574ca | -2.78315 | -49.2239 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67099481-50b4-3111-934b-d63809077072 | -2.66114 | -46.78479 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d044969-e76b-3275-aa54-2990aea09729 | -2.46812 | -50.39705 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb761b36-6555-3c44-b047-a9c56151c35c | -2.90635 | -49.34724 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 495f87c9-4977-3a92-8d02-43db9f0310d1 | -2.12095 | -50.68676 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 31779f46-ae0c-33a3-ad9b-b3f94adc5ef1 | -2.65329 | -46.79088 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a36c91-817b-3c6c-ae2a-979ee2d57e99 | -15.8864 | -43.45712 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2e1a3ba-a210-304c-b0fd-93f0dac718c3 | -2.39788 | -48.89536 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e863c2c9-3e34-3191-80cb-1e743eb1d60c | -3.19445 | -50.28417 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 740372c1-cc90-3006-9718-98b2d175a65f | -2.1138 | -50.70478 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b2af212-0729-390c-97b8-69361069c820 | -2.66394 | -46.78887 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c6309a9-5cdd-329d-b6b6-91db242eecd9 | -2.69893 | -46.82004 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f9f65e5-531e-3946-a598-93153da048b0 | -4.06642 | -43.95343 | 2024-11-12 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README15.md)
