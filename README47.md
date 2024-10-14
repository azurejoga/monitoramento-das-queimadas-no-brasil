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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f927555e-ba0f-336b-a27d-0887692902a0 | -2.645 | -48.42798 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f80445f-e992-36b9-9585-87066ff1ec64 | -2.64419 | -48.43293 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e1f476d-2aab-3e3e-a732-6138bed99bb4 | -2.63113 | -48.53851 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c6e80cf-b0b6-343f-8344-7f3c654ae56d | -2.47773 | -48.19144 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9604366d-48c7-3264-bcbf-0156cb4a1908 | -2.47696 | -48.19624 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb2e8f03-7fe1-3ce1-ace8-6e19fc697b22 | -2.47386 | -48.19084 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef51886d-75ac-3621-8775-912323bd02ab | -2.47309 | -48.19563 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 575c86ff-b657-3f8b-9e29-950d77053088 | -2.38287 | -47.59401 | 2024-10-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31cac6f2-f9ff-35fe-bdfe-00dac0061d16 | -2.32399 | -48.62338 | 2024-10-14 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a42c3417-c549-3208-829e-1603b0eb86c0 | -3.22093 | -48.92203 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b814deec-222b-365b-ba96-1c76b0f7f1ec | -3.22036 | -48.92553 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3804f685-aabf-3427-b763-c296f56cb1a1 | -3.21692 | -48.92142 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f439ef9-cb24-3be9-bda3-a7cb477cf2d9 | -3.13136 | -48.60728 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58009836-4908-3229-ae43-26f06dd1a81e | -3.13072 | -48.60947 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62e71d2d-79cb-34e5-b633-337eeb915355 | -3.12743 | -48.60665 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbbfe5db-ed41-351b-b7c7-621a8aadc7fb | -3.11251 | -48.59911 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d53f9e4-e0ed-3b09-8435-b1c2681ec87e | -3.08751 | -47.78033 | 2024-10-14 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 015b7d10-c99c-30bb-a895-eb1545905e31 | -2.99719 | -48.07872 | 2024-10-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9df20c8a-cdb2-3a56-9156-a3cc76a2bf02 | -2.99681 | -48.07653 | 2024-10-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5edd8bd-b59c-3865-aca1-eba637cc915c | -2.98802 | -48.72448 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04687542-25f4-359b-be7f-f6ed595d607d | -2.98686 | -48.72464 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c9f3576-6aa0-3607-8822-315eb2041423 | -2.96533 | -47.91209 | 2024-10-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15cfd8df-d021-3052-ada9-0fe1a28fc32e | -2.90906 | -48.91087 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f3f6302-89d5-367d-8966-4c7ea0702e53 | -2.88647 | -47.84561 | 2024-10-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e55ebe7-11ef-38f2-a720-4bd6b56e5c4c | -2.87688 | -48.90582 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46da8268-7c4c-3fe6-8c9d-0ff2ceda2bcf | -2.87631 | -48.90934 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffcebb4a-0de5-38e6-9d28-1ef848043739 | -2.76305 | -48.64544 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 510b9e44-9eff-3bc6-aedd-c874ef5b2a85 | -2.75909 | -48.64481 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02a64aa6-91c8-386d-a1b1-a63eb361eebc | -2.74984 | -48.40197 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a70fe85e-8672-3f0c-b4c5-8691a983db26 | -2.74904 | -48.40689 | 2024-10-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cdc9470-c302-3091-8ad1-902a7ea12242 | -2.73322 | -48.70469 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15bf8b20-8d20-3ecc-bd26-5de5950d12bf | -2.72116 | -48.0055 | 2024-10-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2511e791-dd7e-3ccf-abf3-11a6726d6002 | -2.69686 | -48.70242 | 2024-10-14 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87313ae1-cc42-3b7d-8fab-616596a04f8d | -2.17963 | -48.82246 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d53758dc-2491-3b24-b02b-d6b37f4e7cf0 | -2.17612 | -48.36501 | 2024-10-14 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01dbec35-2e67-36e9-9f03-019fa25bc704 | -2.17562 | -48.36788 | 2024-10-14 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e8135d-8135-3bc3-84bf-672d3e2ea4bd | -2.17559 | -48.8218 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 427288aa-7aeb-3ada-bac9-2202678fd993 | -2.17531 | -48.36997 | 2024-10-14 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a0e1321-2513-30cd-870e-bdc42f4725ff | -2.17169 | -48.36728 | 2024-10-14 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28bfa44d-27c9-3090-a287-d9f3589f15cb | -4.41144 | -48.71115 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| feccaef6-9bd2-3b04-aad1-2e0f6a45d3de | -4.40993 | -48.71352 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caebacbe-45b2-336e-ab1b-fb77064eac3d | -4.40755 | -48.71058 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 193d2fd6-9100-36fa-ae18-a29c70f55377 | -4.40684 | -48.70793 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ed781d-9bf5-34be-bacf-6faf6ff5d2ad | -4.40604 | -48.71294 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb50b42-7e3d-3bfb-8187-1ed59490f788 | -4.40366 | -48.71002 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20a39639-bc89-37e2-936c-3ac8afb4a228 | -4.32412 | -48.63003 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d974dc8-bba0-3687-ba12-2fecedee067a | -4.32294 | -48.6267 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e837451d-f68d-32f6-849b-5693dfc2f48e | -4.32217 | -48.63159 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2cc40d6-8b77-33d7-b527-122ac153f178 | -4.32025 | -48.62943 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abff4fb0-b88b-3143-8360-ea4dccae0852 | -4.31943 | -48.63432 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daece48d-130b-3cc4-ae96-11cdffe02415 | -4.31829 | -48.63099 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a599500-e4b5-3929-a5a9-1ef3c5e2bb92 | -4.31556 | -48.63372 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8cf9030-fba3-3516-93fe-d1c1d91c534e | -4.28655 | -48.63094 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9faf3f2-2069-38ac-b46c-c6eb1992f70d | -4.2812 | -48.59045 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bec5b043-06f7-316a-ac1e-176cedd8cdf9 | -4.27517 | -48.2191 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cfa1b32-76df-3d59-ad3e-46f232205cc2 | -4.27499 | -48.22175 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7f48b0d-cdc6-31b2-8054-ffedd8d91cec | -4.27443 | -48.22374 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63d9686a-25cc-324c-8bae-ea75e7612edd | -4.27198 | -48.21654 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 80d58f31-04dc-380d-b06e-b6d796ea5bc5 | -4.27139 | -48.2185 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 05efd828-bf23-3d88-b950-7955504163ed | -4.27122 | -48.22114 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6a2eb4f4-5aa0-3085-8294-cbd35d06f4aa | -4.27066 | -48.22315 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c62e40bc-ba8e-3417-a342-b91a950775d5 | -4.25033 | -48.25337 | 2024-10-14 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc45b27-3fa0-316e-8a5c-14a07e328960 | -4.22206 | -47.86061 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e76f9822-79a4-36b5-af65-4bf05b9aaca2 | -4.22001 | -47.85742 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 198ffdea-e878-3bd1-a1fa-53e955864a36 | -4.2193 | -47.86188 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47007893-3589-35d3-a0bc-122abc0890ae | -4.21764 | -47.86434 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f1bbb9f-e83a-3e6f-af2f-d2c5c6274199 | -4.21491 | -47.8656 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdb86c68-59b0-3b0b-8d29-a653857b4a14 | -4.185 | -48.0296 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a4aa1bc-2e3c-3b38-936f-e1b9cf084dd3 | -4.18126 | -48.02906 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da953688-3c41-3fbb-bd80-ca20b331e1a8 | -4.12281 | -48.27338 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecb0fb05-8d0d-30f9-9aee-85b6f94f073e | -4.12206 | -48.27802 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 07b36769-ae85-346e-b1ef-720376ef7ad4 | -4.12132 | -48.28261 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8aa86323-5f4c-3552-86ec-d2aa94f20846 | -4.12059 | -48.28716 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42937278-fca3-38b5-8ceb-aedf01e53bfd | -4.11977 | -48.26809 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c95c6534-4967-39f2-a94e-3558ff349bc9 | -4.11901 | -48.2728 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e80ef433-4e15-3a31-8961-15bea9e0f88c | -4.11901 | -48.24868 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa41399f-e78c-3181-9af0-e53c33d12cd3 | -4.11826 | -48.27747 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6f62fdfb-b7f2-349e-956d-96a09fae42e2 | -4.11751 | -48.28209 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 77d385e0-9a75-397b-aa1d-8bedc7521133 | -4.11677 | -48.28669 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff3ea4a7-1925-3c97-b9a9-fad1efb2db29 | -4.11669 | -48.23893 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 846b79b7-f827-30ae-9818-e3958c604bb8 | -4.11596 | -48.24347 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 44c291ee-a353-3b5a-be6f-9d32a8f7f6a8 | -4.11446 | -48.27689 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 35c0d8cd-06bc-3f71-966c-3dd53b868d91 | -4.1137 | -48.28157 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dddf7bc0-d5cb-397f-a5f6-d47d62ba991f | -4.11364 | -48.23381 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 42825aa5-834a-3ab7-8262-3d01e6287171 | -4.11295 | -48.28622 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 91da47b0-2300-33a8-89a8-843a59db4052 | -4.11291 | -48.23829 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 7e2b488c-94bc-379e-8e2e-84ef4f69d0f7 | -4.11217 | -48.24286 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 47a68d03-0a33-369d-8763-da31b148e19e | -4.1099 | -48.28099 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 284d3eb8-8967-3ac1-8d80-8ca8ef4548c7 | -4.10914 | -48.28569 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3dab3cf0-3505-35dc-a452-7f94acf1eb4f | -4.10912 | -48.23771 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b6e883c8-5425-35d6-be67-8dfcd60ce798 | -4.10838 | -48.24228 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| edfa6fd2-4801-30e3-9f69-86f34e8c3540 | -4.10079 | -48.24117 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11720704-959e-3765-aabb-8ca8f7c6a7a2 | -4.10004 | -48.24577 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97c1f45a-8207-398b-bc8e-b33834f8ed34 | -4.08335 | -48.27655 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a78275c2-027f-3614-bead-a7e46a0d9991 | -4.07122 | -48.25545 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef6cccb0-537d-3d99-9a95-6a8d5156ca26 | -4.06025 | -47.91491 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db6c00d-5ed8-34de-8101-808d373350e1 | -4.05953 | -47.9194 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5331b71c-5b95-3cac-a6ce-e3b19c59a0ca | -4.05654 | -47.91428 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86319c31-a0a2-37db-a8f3-362fd6933faa | -4.05581 | -47.91877 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8046274-1f15-36e8-a266-d3c31b3bf7a7 | -4.05451 | -48.2388 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
