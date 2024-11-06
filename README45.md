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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71c660c6-d03d-3d56-99d4-07fc18f2393b | -2.91926 | -48.59737 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47050932-b46d-36f3-97d4-1278744003d8 | -2.32381 | -53.88649 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 123e6685-933c-32da-b06f-996f5e703d2f | -2.4759 | -53.98331 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9518474b-e7ca-3914-85b2-e93ea5ee46de | -3.89061 | -51.81839 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9da409b-168d-3f3e-a9c8-2974ea44c812 | -3.35414 | -50.12476 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f3a4b2f-bbad-3dcd-9696-dec287a20e4b | -4.30104 | -46.35183 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51b73530-0b3a-34fd-8149-927c50329707 | -2.85805 | -49.26786 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c347ba7-805a-39ea-8aa3-9a6945a276a8 | -3.18889 | -50.58836 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf0378bc-c5e6-3e5e-9c6b-b39e549cb0a0 | -2.42632 | -53.6647 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32710828-2a8b-3486-aa11-449fc4634515 | -2.28004 | -46.71204 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e4db7c2-9764-336a-9095-4cd68fbe3051 | -2.60494 | -49.25686 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1b7ed2df-e448-3122-9850-f5375841401d | -3.95361 | -48.15534 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d052a9d-1109-352b-8d70-709ddbcd494a | -3.16078 | -50.21171 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 2c0f45dd-cbdd-3d84-8ea8-fdf2dcfa65e9 | -3.96743 | -48.15395 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8478949-f3b2-35c1-90d0-a348e60673ef | -2.66573 | -48.56857 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8760698d-1db4-37b3-896c-8872a0ef45f3 | -2.43462 | -49.17313 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e1331d5-9e2c-3956-b641-b3a63c0e13ee | -1.05981 | -53.65971 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab0d267c-18a2-3bf4-b916-d60afc563fe1 | -4.20582 | -53.48696 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 318163bb-0982-3e9c-8b71-89b7171c7b93 | -2.90086 | -49.40586 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616e708c-f4f6-39b6-861c-940f5badcd3d | -2.89108 | -48.73359 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 174f1d38-5c7a-3b84-8b6b-c768cdc6d4f1 | -4.1362 | -48.24746 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8041889c-a8ac-3086-acb4-37b2b57c57e2 | -4.82504 | -48.10061 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0a403d5-b839-3591-a84b-4abae140a5de | -3.0824 | -47.57609 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b4c8290-0c50-3a6b-bbf4-d1f29604dd82 | -2.39683 | -46.16602 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da39e5a4-86a8-39e6-bc3c-75a9e9cf9cc6 | -2.9684 | -53.87219 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36e42ba8-7449-3a4b-9bd8-fe9f86af5ede | -3.96248 | -48.16383 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dba41fda-6cbc-35f4-aa3d-a5d897d96afa | -3.10318 | -50.29112 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f00a03d6-e80a-3038-a093-be2edaac2108 | -2.81295 | -52.92816 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bcab85f3-214f-3ca8-bad2-ec71dd43b87e | -3.5943 | -50.17712 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75f8fbac-35fd-336e-a7f4-842ca69a0931 | -2.15981 | -50.51002 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd12a302-7495-3ed9-94c1-3451088bc2c7 | -2.63996 | -51.74976 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| babd4290-60f7-3c5a-b51d-e46e80db4bae | -2.82823 | -49.78124 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eb49a74c-3476-379a-9c58-e031ece0301c | -3.1522 | -51.15333 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e85f071-1d1f-3a6e-aab9-3e8ff4ba8227 | -2.8006 | -48.65994 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6df54b6b-4b79-3e03-a6b4-fa949fb41318 | -3.65719 | -52.33891 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4a796ab-28b2-3468-9e4b-dac8cbeb8c3b | -2.40365 | -46.7943 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78587930-87e3-3423-b7a8-6712f2de7a87 | -4.88718 | -48.65931 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5b9b773-86c4-3e98-83f0-35764100d795 | -3.52344 | -44.7268 | 2024-11-06 04:36:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1d862ce-76cd-337c-afdf-5e8b5934b656 | -3.09371 | -50.26377 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 371899cb-6c30-39f4-8906-8a10c5729745 | -2.92938 | -51.05278 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 43bbc2e7-1571-3c51-bf38-7e9ec5d51fad | -3.67472 | -50.22588 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc1ba87b-e72d-3842-a40a-a8b0932b26aa | -2.50984 | -49.17112 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0607f94c-0a3f-3ab3-9fdc-1acd02c38f84 | -3.71163 | -41.68969 | 2024-11-06 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 918992cb-72d7-3b9f-a891-6e0dd633ce74 | -4.59186 | -44.04607 | 2024-11-06 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e8e20a0-4d80-38d3-85b3-8acd38eb5076 | -3.95747 | -48.15239 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fdd50c7-f63c-39eb-8e76-be7ce3a998af | -2.82833 | -52.93051 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e7027bc-e08d-3112-8169-7b58a669e100 | -3.54644 | -47.38537 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2507b66b-ce31-3a13-9332-9ba5192f7a0f | -3.7988 | -51.94275 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4d8601e-68de-3ccb-8721-68c2549fdd5b | -5.62856 | -44.18156 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6725be26-4986-3cbd-816d-9bc0354f9905 | -2.03227 | -53.57685 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0840ba24-a985-3383-ad70-cf4a4bdb0ec6 | -4.12657 | -43.58025 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 57fc9fa8-e866-3464-a600-6107222e228d | -4.65924 | -43.82178 | 2024-11-06 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0f2e4d7-1644-3cb9-97a7-b73bb888d0b7 | -2.77855 | -52.87369 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32a1db93-0fea-3e6f-9c3f-445e6adc1e5a | -2.62427 | -51.76992 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1255a530-8820-3338-81fb-6a7742834cda | -2.50653 | -49.17061 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37ae008-9171-3043-8d0b-53e5050850db | -2.75675 | -49.13527 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d328ab9c-b3f2-3d87-8708-a298d4073d05 | -4.33655 | -39.36443 | 2024-11-06 04:36:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6e88f72-3d48-336a-97ab-9267a1b8ada8 | -2.65583 | -46.75015 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6514ef6f-d7b0-3c08-9f40-880ae3fc92fc | -2.85115 | -49.44077 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac562484-f7ed-37f0-bd79-a868956bab6c | -3.95469 | -46.36925 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbc79bbe-bf3c-39d8-b412-1bbc3a83bb45 | -2.35286 | -46.67052 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f71c4ee-fdf4-35b7-a168-53c77bf59f3a | -2.91834 | -51.05495 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 71067344-7096-32cb-999e-bb708ecec4a4 | -2.82448 | -52.92993 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5545d238-dd13-3f0f-90a8-f312e8e59dd8 | 0.18619 | -51.06684 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9765a4a9-61e4-3647-8399-949566c6f110 | -4.07457 | -53.9444 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0d26f428-70ea-3bf1-9f30-79cd129becb9 | -3.21427 | -49.22877 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ffa7013-6144-3142-8068-a91741e15ac4 | -2.60756 | -49.19699 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94100d83-20cf-3b22-b5ea-55de364ad9a9 | -4.03474 | -48.28851 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b522d9-25fb-3a6a-b48e-727045935722 | -2.26936 | -49.18649 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5f1aaef4-c57d-3ea8-adff-8327a1bae523 | -3.53498 | -50.33294 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f5ad7e1-0e0d-30be-9938-ad4baa9beb0f | -5.12078 | -44.35626 | 2024-11-06 04:36:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f98686fa-f5a5-3d82-a8b3-2b2a0d869236 | -4.69686 | -45.64566 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd10471a-cbbb-3084-b340-fa80d442f10e | -3.59302 | -50.27217 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a682431-55fd-371a-ae39-dd506c9ef9d3 | -3.25705 | -53.41091 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 189f6c3c-d034-31b1-be26-6cfef077b0c7 | -2.3244 | -50.57723 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0e50b15-f40e-3600-a236-696fa99b9339 | -5.26569 | -46.16491 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 752d573f-e58f-3f4b-ba95-65f5ecc6ab23 | -2.81989 | -52.95848 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 04c8d11b-cc43-334a-a75e-0f5b02e73fa8 | -3.75751 | -45.93624 | 2024-11-06 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1577c9fe-11ec-35f8-ad8c-19c531da8b66 | -2.26496 | -46.47128 | 2024-11-06 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f7b9735-80f0-36c0-9a43-f11342424c4a | -2.89808 | -49.40187 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f0580a0-b4a0-3025-96db-7505d69bbe42 | -4.62774 | -42.80986 | 2024-11-06 04:36:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06884076-5cfc-3d56-8194-119de24d4632 | -4.49602 | -46.63484 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 153f27dd-fb8b-3448-b30d-f23454ee0675 | -3.18489 | -50.5915 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b453b01-13ba-3525-8d16-65c461585adb | -3.30128 | -50.14219 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f82f2f4-efe4-3712-a24e-b1c7a0c696aa | -3.20188 | -53.23198 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a9cf838-7051-3ee2-bcd4-1ae37aab21c3 | -3.86029 | -50.19652 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 172ffcdf-f988-3e6f-af73-169c808b6bb3 | -2.73325 | -51.74332 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67929b8-b089-3442-ad79-69260a360295 | -3.03423 | -54.08077 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58c7d302-bd82-3095-88f5-26878076adf9 | -2.9968 | -53.85157 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86756f38-f72d-38ea-8867-42f4b5bffc46 | -5.62451 | -44.181 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c7906af-cc93-35aa-8beb-bf5aeff47b08 | -3.00828 | -53.43769 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 01590394-d928-34b0-8e7d-c7b24d3c2af7 | -4.67163 | -48.77731 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3ba5cf5-cc8a-3b1b-afa9-19d5292361f1 | -2.58396 | -46.10678 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b7a0a4-cae5-3823-a2ba-eed168726ef6 | -2.62948 | -48.58403 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2438319c-68e2-33fd-b6bd-b67c80aaa9fb | -2.24044 | -50.71021 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b75d246e-a8d4-35b2-95ec-2cab57ef2eeb | -2.81451 | -52.9429 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d866fe3a-55b1-3ccb-addf-799cbeda3402 | -2.99423 | -54.12876 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc2b6bfb-b900-38d3-8eef-1a8041547c7a | -4.01985 | -48.29684 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 030b2f8a-4d58-3c39-bafa-7ee3417e16f0 | -2.58609 | -51.87086 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 444bc0bc-b8fa-32fc-8c21-6fb0256d9a7f | -2.71557 | -48.72754 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README46.md)
