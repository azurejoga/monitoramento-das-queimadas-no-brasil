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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10a0a410-de88-3ccd-9179-9c1bdde292bc | -14.20843 | -57.41503 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5940b0ed-1e6d-30ad-a1d9-9d4f45031e9e | -10.51873 | -59.39145 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f927c9c8-716d-3b16-87a8-9ac83614a1ae | -13.90326 | -54.61657 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 54357e69-bf8e-34ae-8cae-7182d4f7ee22 | -13.50426 | -55.65783 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25e260d9-6154-3d1f-97fb-8c99b2efbf58 | -10.92219 | -54.78519 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ebf60865-9374-3001-bdb1-ac4f0cf6517a | -11.89829 | -47.4601 | 2025-06-14 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3618848b-f644-3cfa-a990-26e297e52e6d | -9.46319 | -57.85331 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c60fec88-e247-37aa-a9bf-4c0f8ea7030d | -10.05545 | -59.36137 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d7d6c2-6d32-3ca5-ae56-370b73fd2714 | -14.53625 | -46.03169 | 2025-06-14 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a773d4b-af5a-386b-a65c-1a277eea1328 | -13.50029 | -55.66106 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a29f3e93-e162-3b9f-a91d-202b7b845477 | -12.51593 | -57.18648 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0011a1c5-5780-37c6-9c0f-2b79d92ec15d | -10.28825 | -60.5556 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56e4e92f-9abd-343d-a89f-a123ee39f2d0 | -10.56037 | -52.0167 | 2025-06-14 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2d70ab4-c0e9-3255-8e5f-3424136ba601 | -14.21338 | -57.40495 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ff2c391-02d5-369f-a54d-c2d890214acb | -10.94385 | -56.83887 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 647a9224-7e13-3e31-978b-dcc375d9b2cf | -11.80119 | -56.96952 | 2025-06-14 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b313c4ce-cb05-3fcb-aead-f6470f794bdd | -13.9574 | -54.44051 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 228683c0-deb5-3ce4-b924-61ea69e1e700 | -13.90267 | -54.62076 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b44a32df-0607-3c26-8984-b46eb4123f25 | -14.07233 | -53.38989 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57a73db2-a199-3eff-9355-d0331b06f173 | -13.22708 | -49.83788 | 2025-06-14 05:06:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 437490fe-30f7-3cae-a021-ce13b06686af | -13.89532 | -54.62583 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29d6e4a2-c776-381a-b082-5599b4fb3953 | -11.81213 | -54.50056 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e59651f-7ce1-34c2-a78b-b15b93480047 | -11.88626 | -54.68527 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b980df24-9783-35dd-8691-573a3584e57b | -11.80449 | -56.97005 | 2025-06-14 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b5144c5-d3aa-3c0a-a996-3a6eeae0210b | -14.21559 | -57.41256 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16184b62-667c-3e01-9266-a8e821358d7e | -10.36655 | -57.22443 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0194b87b-8a1e-35a4-8b53-e6a1ea515721 | -10.6225 | -52.58546 | 2025-06-14 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 189bea39-d397-3d86-9675-ddfed5bc6db6 | -14.0285 | -55.12388 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f9a4494-4dd0-3bcd-9dec-17cc2b45630b | -11.92128 | -57.46334 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3dc865-c44d-381a-bdb5-69c1709d4bb3 | -11.77046 | -54.3672 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 023c76e4-df73-3c3d-b065-11cae9e2eaf0 | -9.46711 | -57.85026 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38d19a33-bd27-36af-a7a9-cb110b48e2e0 | -12.47277 | -58.55333 | 2025-06-14 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4311b469-030f-3c8d-867d-57abd4b0b8a1 | -11.13733 | -53.94659 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4de1c81-d3bc-39d5-aec7-e036d0768237 | -14.31018 | -59.89273 | 2025-06-14 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62f4cdc6-ce93-31b2-9a95-1b15f65936da | -11.81077 | -57.34488 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e87ab53-bb81-3284-9ba4-8a236c05c57e | -13.96518 | -54.43745 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 165c58c1-286b-379e-bfcb-3bd29c660f99 | -9.68535 | -56.98917 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33c0ad0d-ad77-3cff-bd3a-7084fb8c6212 | -17.75702 | -52.42992 | 2025-06-14 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3133a71c-03b7-3467-bbb4-3fc72a494e72 | -17.37917 | -53.82028 | 2025-06-14 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24dacc6d-b977-3c49-b429-b4206eac1e98 | -21.44143 | -54.56998 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3a47f1e0-6460-3ea3-ad0e-52a1fdae5b0b | -21.43685 | -54.57471 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 722d5c8d-92ac-32e9-a5f9-139c724eea1d | -19.52549 | -46.09182 | 2025-06-14 05:08:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16b9ff4c-be63-36c3-9352-e00cb037062e | -17.93422 | -52.69429 | 2025-06-14 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62bcc582-ec4a-37ec-8e0d-7da5c88c1e11 | -17.58221 | -47.49491 | 2025-06-14 05:08:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44e1f2c9-66b0-3a76-b8c4-a1b4d7e77f4c | -16.14303 | -60.08327 | 2025-06-14 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f9d92b3-2935-33fb-b4e8-5f5393bcb62a | -18.73742 | -54.19535 | 2025-06-14 05:08:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da18db50-c0f7-3a07-981c-3d3481b018e4 | -17.93475 | -52.69016 | 2025-06-14 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37817e30-c709-3ac5-8261-96a4b3e00424 | -21.44859 | -54.57637 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63bfb679-4d0a-3a80-af9a-ba33e0027eb4 | -21.44535 | -54.57053 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 950fef95-054c-3d57-9340-e816bbf6fb7f | -18.73358 | -54.19466 | 2025-06-14 05:08:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e1457de-d3d0-3469-9bd5-33bdc46e9573 | -17.37852 | -53.82527 | 2025-06-14 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a06fcec-3afc-315d-a478-a8551d33005b | -18.74128 | -54.19602 | 2025-06-14 05:08:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9b3098f-2791-385e-86c6-496fe107e884 | -17.58161 | -47.49072 | 2025-06-14 05:08:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d5f206e-16c8-32fd-a9ae-af1fbaa4a287 | -16.14707 | -60.08003 | 2025-06-14 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab2d2bc4-21ea-3b47-bcb8-a1f061d2f4fd | -17.93843 | -52.69474 | 2025-06-14 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd9cf41f-a842-35cb-8cab-ad0498413255 | -21.44603 | -54.56523 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 903c3c55-43a9-37e7-9c48-3f6290bb097d | -16.14366 | -60.07946 | 2025-06-14 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59fd5c84-2e31-3962-b83d-cc4d09e8889a | -21.44927 | -54.57108 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45d6e1ad-3b6c-3a00-9c3e-b15468c5de91 | -17.38305 | -53.82087 | 2025-06-14 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5029ac12-616a-33bb-ba6c-7346dfd16cfc | -17.58116 | -47.49532 | 2025-06-14 05:08:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae078bdc-e572-3653-a1ad-fd63771ce0e5 | -21.44467 | -54.57582 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 470d089b-cb09-37d9-94ae-71056587240b | -21.44076 | -54.57526 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f3f6957c-16f8-3346-9b16-853a8350ae0d | -17.38692 | -53.82144 | 2025-06-14 05:08:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c554651a-62d4-3f4b-a4d8-2ff200938830 | -21.44211 | -54.56469 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89b84b26-0925-33af-8866-730efbaa8be9 | -21.43752 | -54.56942 | 2025-06-14 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ac84724-1e0e-38a5-bd73-d309cf8509c1 | -16.14643 | -60.08386 | 2025-06-14 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5289f130-8027-333e-a878-38869022ce28 | -16.13962 | -60.08269 | 2025-06-14 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8af9b2e-985e-39e3-8666-84d266a3b62b | -16.14025 | -60.07887 | 2025-06-14 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b791f282-9b9e-3aaf-977a-9f3bb24a7ca8 | -13.887 | -54.6106 | 2025-06-14 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| dd54e8a0-b93c-3749-8677-c4ab6d08b679 | -13.9062 | -54.6084 | 2025-06-14 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 351cb5c9-967f-3204-b65a-ea6096e10040 | -6.9605 | -42.8816 | 2025-06-14 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| c1d2f1ee-78f1-36ff-ba79-211ae2e76186 | -14.2121 | -57.4098 | 2025-06-14 05:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 3daad902-3c52-3df5-8d1d-3729ec622196 | -10.9355 | -56.8322 | 2025-06-14 05:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f550c145-c5c1-3019-b835-d205e8267bad | -6.9416 | -42.8834 | 2025-06-14 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 9586165e-4d1f-3127-b70b-0ac78e84f146 | -29.95234 | -51.61841 | 2025-06-14 05:10:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| f08c73ce-fd3a-3a22-a49a-58be12f32491 | -6.9525 | -42.80276 | 2025-06-14 05:14:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 86356644-d62c-31db-98c3-cff509f1f359 | -7.45061 | -45.4863 | 2025-06-14 05:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d4ae3b1d-c9da-3e1f-8724-1befe2e0c09f | -5.8959 | -43.44757 | 2025-06-14 05:14:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b5d26d82-9349-32a7-9ff5-7d63e76f7fd2 | -6.95694 | -42.81019 | 2025-06-14 05:14:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b600c3ec-2b35-3676-9f33-75f3860e142e | -7.44725 | -45.50626 | 2025-06-14 05:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2f77bc2e-c670-3088-a800-481de7dfc731 | -9.40152 | -48.40366 | 2025-06-14 05:14:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 48dcd442-01bd-30dc-b74e-41785c641443 | -7.44982 | -45.49947 | 2025-06-14 05:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| bf077bea-fa7f-3861-9534-d31b0d1defe0 | -6.94233 | -42.90049 | 2025-06-14 05:14:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| d6519930-21bd-3e5d-aae7-0aec44f9ee61 | -10.64502 | -44.48022 | 2025-06-14 05:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 36f98e76-641b-3d16-969d-5598fc994090 | -6.59778 | -43.88047 | 2025-06-14 05:14:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9c2c76ea-6c94-3545-a7f9-5363d42207d9 | -7.06673 | -43.55059 | 2025-06-14 05:14:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 98a9ca0b-1eaf-3163-a9ec-f9b5928428f7 | -4.5695 | -37.81301 | 2025-06-14 05:14:00 | AQUA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 716734c4-9d69-38a1-a9f8-68c2c9b1c1ea | -6.59525 | -43.89584 | 2025-06-14 05:14:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| e31d1d16-0efc-30ae-9937-3eaedbb73d1e | -10.65312 | -44.49101 | 2025-06-14 05:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d43d54c7-2964-319e-bfb5-a6e96accf41f | -8.20854 | -42.83195 | 2025-06-14 05:14:00 | AQUA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ce027dbf-7475-3728-b4d1-8c360ea33c62 | -6.955 | -42.88904 | 2025-06-14 05:14:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 5c394479-6920-38c6-b410-5ff41f4a5214 | -9.39769 | -48.40763 | 2025-06-14 05:14:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| e342242e-bc60-3740-ae3d-e282e9b40888 | -6.2141 | -43.32269 | 2025-06-14 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4f921ee5-9f53-3558-94dd-7c062b8bb52d | -8.07275 | -43.10063 | 2025-06-14 05:14:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c03c7324-41c8-36e1-80f4-f3a279f47771 | -4.56818 | -37.82183 | 2025-06-14 05:14:00 | AQUA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| cd08d2fc-64d3-31e0-a4a8-7f92111583b6 | -8.07071 | -43.1135 | 2025-06-14 05:14:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| e0e29b2e-8338-3cae-81dc-9d05497ff3b4 | -6.59914 | -43.88947 | 2025-06-14 05:14:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 60c8744f-0ca0-3f3e-b8d2-091e1c4b5187 | -6.94444 | -42.88746 | 2025-06-14 05:14:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| dd573924-b5ec-32dc-9fb0-c56f6a38d250 | -16.18731 | -46.46324 | 2025-06-14 05:16:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 04b55f2d-a250-396b-b7c2-18a157c67383 | -6.9605 | -42.8816 | 2025-06-14 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |


[Clique aqui para ver as próximas entradas](README23.md)
