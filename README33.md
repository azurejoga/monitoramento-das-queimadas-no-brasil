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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dadad333-efe2-3f7e-8bd2-1d1c56bbcbc1 | -12.93674 | -46.99666 | 2025-10-13 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41c1157e-3da9-337c-8486-9bec45306815 | -19.99968 | -44.68512 | 2025-10-13 04:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f118548f-2b48-3e83-8253-eac341c28282 | -20.84606 | -42.80944 | 2025-10-13 04:49:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 32b237ef-8a9d-3717-93d9-25effd4b488b | -20.71903 | -57.78676 | 2025-10-13 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d894ef9e-e370-3e2a-a802-6a95ca092541 | -20.84561 | -42.81439 | 2025-10-13 04:49:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f21a376f-5eb1-3d98-8c05-bc7ede6a6c35 | -17.78124 | -54.93545 | 2025-10-13 04:49:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a7ad813-a87c-3765-be7c-4ddc47f85edc | -19.90006 | -54.17228 | 2025-10-13 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69eea011-9cef-30b2-abb6-5e6155444a77 | -20.83965 | -42.8136 | 2025-10-13 04:49:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 57f5ce56-02fc-35f3-a5bf-3cbffd2ea2b2 | -20.00003 | -44.68177 | 2025-10-13 04:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c870abd7-8888-33eb-9baa-04f1cc4d221e | -17.77788 | -54.93484 | 2025-10-13 04:49:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c246b81d-4f82-3777-8bba-03f61f09bbe9 | -20.84009 | -42.80873 | 2025-10-13 04:49:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5ad3c4f4-67ad-3ded-92b1-6b5e53ae2b7d | -30.83086 | -52.33081 | 2025-10-13 04:51:00 | NOAA-20 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| e98b6f27-4829-3672-b21e-6caa1ed18d61 | -2.5424 | -47.7893 | 2025-10-13 05:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ef59f7a8-f118-3b8b-9d52-36bc7f54c226 | 2.04488 | -50.85768 | 2025-10-13 05:31:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 849b78f5-4117-30ab-b6ff-7ba2b4d7976d | -2.88348 | -50.73185 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3140aa02-fcb2-3581-9839-3ab53989d922 | -3.25919 | -50.13576 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32adbe82-799d-370b-ba46-b292c6263b2e | 1.77755 | -55.80445 | 2025-10-13 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6370f333-cfd4-3465-93b8-933890370f2d | -2.87676 | -50.73517 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5e5cc11-ba4f-3c29-a412-3caa4d696d87 | -2.88266 | -50.73732 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf2b5f6f-8060-301c-aeb1-cbdf44e2acd5 | -1.89458 | -51.01186 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42c0cf34-7263-3641-841a-d035a28e4089 | -3.92483 | -50.01255 | 2025-10-13 05:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fb9200d-1931-3827-9e53-c3a63bf3fd6a | -2.88246 | -50.74171 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cfb46666-720e-3e76-a2e0-e39b5a9c2cb2 | -2.88403 | -50.73074 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 926dd57f-adda-3e12-9094-71510fc7a7c9 | -3.264 | -50.13466 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c3945f4-cb3a-3e92-ae6f-a4c5f281b00c | -1.90166 | -51.00776 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7060c732-8624-3006-b6f0-132003337528 | 1.78036 | -55.80611 | 2025-10-13 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5a911e80-b505-3130-8a57-f2cfa7ce73e4 | -3.2668 | -50.13071 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f384d048-f5ea-3593-8095-b3d50996fe41 | -3.26004 | -50.12962 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14f501ad-a176-30ed-91ee-821176625978 | -1.96775 | -56.8668 | 2025-10-13 05:33:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 754f04b4-3267-3ad6-b997-00a21aa1b395 | -3.12669 | -50.20622 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f8efe57-8fe7-3762-bbc7-00091991e13f | -2.88324 | -50.73623 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27501644-b8b1-3f97-9c8b-1f1ce9c406e3 | -3.06715 | -49.40689 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dcd0ed9b-bf90-3551-857a-a8e82be2f9a6 | -3.07179 | -49.41151 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18bee01d-13ef-34bd-ba29-54a0a692dc11 | -3.06576 | -49.40335 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1104e2a5-bef8-3b94-bb38-f7d7ee198974 | -3.14252 | -50.21351 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 149b8010-dbe5-33c5-8388-37ea73c1cc54 | -3.2649 | -50.1285 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10830394-b4c2-3eb1-b235-d9bcc3c90d85 | -3.14006 | -50.2087 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8cc9f688-7872-3897-b238-103232858bf6 | -3.09494 | -50.37725 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4fbe4a99-7ef6-3770-8fa3-16e27ee245df | -2.98806 | -50.28887 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ef47da4-6b97-3006-b9d3-82d4005bcf5b | 1.78862 | -55.77528 | 2025-10-13 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9fa1150-ad90-3812-9648-3f386011cbb5 | -3.14337 | -50.20743 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8eda1669-10b1-39f6-943b-ae479b958253 | -3.06817 | -49.4 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3e7bed56-a34c-3227-ba31-ae3b8f4b29c8 | -3.13338 | -50.20745 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c049a646-4752-3aa0-b5f9-2dd500cb91d2 | 2.18752 | -55.79502 | 2025-10-13 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14fd3546-cf7a-31a0-8e90-4cc1c62ccafe | -5.22245 | -50.94715 | 2025-10-13 05:33:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 647c943a-aec6-39fe-915b-d941236e7d53 | -1.89875 | -51.00772 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2425e454-a536-3124-b8c1-2e094a18a8e3 | -3.06479 | -49.41024 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 525d4ac5-d1f1-314e-9005-a2039b9752ad | -3.06613 | -49.41376 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 69290414-04f1-3f41-8230-a6eddf96d1e3 | -3.1325 | -50.21343 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 721b6fc9-baff-32d7-a3df-d9c1c1bf8f31 | -3.91796 | -50.01155 | 2025-10-13 05:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98fe9fe8-ccf2-3da0-8e02-1a17e2ad196a | 1.784 | -55.80138 | 2025-10-13 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7e8711f-4f1e-3b8c-ba5a-c117f12bc282 | -3.13917 | -50.21479 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7af285cc-d44f-380c-aaf5-653f070729a1 | -5.22166 | -50.95295 | 2025-10-13 05:33:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a2d23aa-43e2-3d7e-9093-4abe0a90f605 | -3.07277 | -49.40462 | 2025-10-13 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71e98ba6-d119-3778-ac21-c51e88b69324 | -1.89801 | -51.01278 | 2025-10-13 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23df2d18-0bc5-31b6-ba13-8a9ee3aef25d | 1.91529 | -55.69634 | 2025-10-13 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdd1dba3-ffa8-3c55-8369-62b9591298de | -9.85708 | -61.43501 | 2025-10-13 05:36:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acecbc46-8e8c-3347-91fe-0893f1786056 | -9.67047 | -62.51389 | 2025-10-13 05:36:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7467984e-7c1c-3b9e-8f1f-51bf0d2f5058 | -9.66706 | -62.51337 | 2025-10-13 05:36:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd9864f2-bc14-3db7-8a3d-d65f0b92b6e8 | -9.74273 | -62.33594 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95c73640-6839-3737-851d-d9d2aaf76f46 | -9.88696 | -60.35914 | 2025-10-13 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2db3c2ed-917c-3176-8bf6-0be62e28fcbf | -9.74108 | -62.37064 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a9120f2-df52-3725-b98b-72f4c4da1392 | -10.55785 | -58.95006 | 2025-10-13 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1df8aaa2-3fe7-3c52-a541-d66f19d052e6 | -9.88516 | -62.20443 | 2025-10-13 05:36:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 617011ac-d584-3feb-a6cc-2f460cab652b | -9.88628 | -60.36385 | 2025-10-13 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f33a7cb-2115-3f69-8d93-96a441ced89d | -10.55367 | -58.94936 | 2025-10-13 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05e4bf1f-1e53-3466-be58-565cb56c0482 | -9.70696 | -66.23693 | 2025-10-13 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc0b41dc-aba9-3572-96b5-83c0f76cf0d4 | -10.04906 | -62.25999 | 2025-10-13 05:36:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1619bbbe-05ec-3245-87b3-7e4353cfabe0 | -9.89027 | -60.36147 | 2025-10-13 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c28bc8-44de-3e90-92e0-5eaf73f7d8e3 | -9.66763 | -62.50962 | 2025-10-13 05:36:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a2661ec-bf10-345f-927d-d3f225911a8b | -9.41255 | -62.29457 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 245eff0f-bf28-3d92-b8b1-7ced5e419eb4 | -10.19055 | -57.91265 | 2025-10-13 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09617028-9a2a-3b34-b6ae-a2828a0bb9b7 | -9.42685 | -62.29294 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc8f6ae5-89f7-3d5a-a2a6-4989f707a5ff | -9.67445 | -62.51065 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b918455-2e6e-33b6-bd58-934bc4383a87 | -9.41598 | -62.29511 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d50585c-0d0a-3f87-99f6-66e6c10af7a6 | -9.30027 | -59.00639 | 2025-10-13 05:36:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6e88442-b78c-3ef7-98b8-5bef55e845c1 | -9.67104 | -62.51014 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41f4b78c-c52d-3e1e-938d-8e6a55e73121 | -9.8208 | -62.19156 | 2025-10-13 05:36:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 955871b7-6a18-3054-961c-1e02f784f612 | -9.82138 | -62.1877 | 2025-10-13 05:36:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 54411e26-a97b-3411-911a-3da34019495c | -9.67389 | -62.5144 | 2025-10-13 05:36:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26c7211-3edb-30ce-bde8-0021c52bbee2 | -9.73596 | -66.29487 | 2025-10-13 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e7b83b-1a69-3804-903a-4c9d5323969a | -9.89076 | -60.35972 | 2025-10-13 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57efa95b-409e-38c5-8c48-82752f79aeae | -14.70522 | -54.85462 | 2025-10-13 05:38:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98471e90-8dd4-391c-9151-75be77638e5a | -10.88127 | -68.21041 | 2025-10-13 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44fa5cf4-7f5b-354e-9647-314ecac938d8 | -12.3964 | -63.87127 | 2025-10-13 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de45e12a-77dc-37b4-a7b5-dd89c1580663 | -13.83934 | -54.84589 | 2025-10-13 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df6bb801-fe2b-3b67-b9d6-b24147325b21 | -16.12206 | -53.98054 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2437fcea-63b8-3eee-b651-a57e8c4f9d29 | -17.33158 | -53.80767 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8fe95d3-15ef-37e4-92d3-b6766f7ebaee | -14.2476 | -51.48846 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ab3066ed-a941-30b7-96ff-583e0167534e | -14.28671 | -51.52908 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f4205e3-9492-30f9-bd1b-f0d2544f8f0f | -14.26471 | -51.49905 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ec863d7d-b12e-3464-b54f-95044c21abd6 | -12.59181 | -62.94755 | 2025-10-13 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf21aa20-c90a-37c1-b1e3-3c375964bd4c | -13.51861 | -51.29995 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 0dd117d0-f79d-3541-a5ab-b8843f4baf5b | -17.32565 | -53.80188 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1315777-c1a1-3e10-aa8a-9d9cac711093 | -10.6341 | -69.13398 | 2025-10-13 05:38:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 167a076b-84b1-3197-8e07-c26a9bd081f1 | -16.12884 | -53.97639 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 37b0377c-1c75-362d-8d1f-0651761f7725 | -11.73495 | -64.96145 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 402286f2-84aa-39a2-9a0b-0de679cae437 | -14.26753 | -51.50525 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ffe6bc39-31aa-3033-aa04-01fc6d6f03e0 | -14.29114 | -51.5239 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe2660b8-c9af-32c3-be23-3e85667f0147 | -16.12259 | -53.9754 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README34.md)
