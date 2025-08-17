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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cbdb9bc-bdf2-3521-8f34-e4fe079f4d0f | -11.35697 | -55.39622 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eaad39ec-f301-3463-a574-9adedaa138bc | -11.88719 | -50.95095 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028a4d48-03f3-39bc-81dd-35474da67ce9 | -15.76515 | -47.80137 | 2025-08-17 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6c41f75-269b-3185-8f0b-a3c6ec29ac94 | -20.01159 | -47.70845 | 2025-08-17 05:08:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0440a43-cd95-373e-b9dc-019e15426e02 | -15.65228 | -56.86673 | 2025-08-17 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f6bda4e-8167-3b48-909d-49fdf7864e78 | -15.14915 | -48.7611 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f64a435-6641-350b-be1e-190cd39ba9a9 | -20.25989 | -50.63962 | 2025-08-17 05:08:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aaf72c41-4d2b-3274-a7eb-a821cb207e15 | -14.93003 | -54.68538 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 530b4f1d-af15-3876-bc67-a487eadd8c78 | -15.14951 | -48.75784 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2caaf073-0f47-3d10-b0ef-a2e2b524a51d | -16.03839 | -52.34713 | 2025-08-17 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f8c855e-6660-39fe-ba9f-eb69f070970b | -14.97627 | -54.74911 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| df36999a-5a55-3a4e-bc2e-6cd373fc38d3 | -14.93247 | -54.69423 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4b9bdfe5-3bce-307c-8087-09f7504aee1a | -20.77826 | -49.56503 | 2025-08-17 05:08:00 | NOAA-21 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e9f93e2a-244a-33c2-a5ac-6e6ad16d59ff | -14.80659 | -59.58733 | 2025-08-17 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dccdafbe-10b8-3518-87ad-16a4dfed4be2 | -20.8975 | -56.94797 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ceff82a-08b0-36f7-88cd-a54b8e780d24 | -16.62984 | -51.38644 | 2025-08-17 05:08:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8173e480-3844-3be7-b843-9ab900043725 | -15.1417 | -48.73793 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 287ae775-b274-3cef-82f1-0b4a0c41fb6e | -15.76758 | -47.80333 | 2025-08-17 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29fa44eb-bd5f-348a-9d64-173c46d537a6 | -14.95353 | -54.75378 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e23d1a6b-ce28-3c10-8650-0d6d033fe0cd | -15.98222 | -59.51262 | 2025-08-17 05:08:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c092397-2c65-3dbc-ac4f-4ca65b8a4a98 | -15.85945 | -50.19599 | 2025-08-17 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 25824fb0-a8ad-3a1a-93b4-d3d107a4bf96 | -14.93363 | -54.68597 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fcd7297-7872-31ce-be6a-8e6c1bdec488 | -15.18472 | -48.77837 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc3c4bb7-d2be-39c5-955c-742df848d1a7 | -14.63411 | -54.89404 | 2025-08-17 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1bf6682-0cd4-324b-82da-8cb2121cd9f6 | -14.97268 | -54.74844 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cafca180-3788-322c-936a-5858580e3aea | -19.35362 | -46.10928 | 2025-08-17 05:08:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09bb9308-b44c-3b5a-acce-9e87f5074d21 | -15.1851 | -48.77499 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d7d7c57f-5e41-3eaf-ac8c-d7c2862cdd72 | -21.07595 | -49.38724 | 2025-08-17 05:08:00 | NOAA-21 | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b0d53167-843f-35ca-af1d-035eb8f7c0c2 | -15.14006 | -48.74633 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6560bc0a-a4f4-36fc-ad13-10f71fa2aed7 | -20.01398 | -47.70942 | 2025-08-17 05:08:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70a92559-89aa-352e-b7b8-1b8c32677178 | -15.85878 | -50.20166 | 2025-08-17 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1df9acd2-3c4a-310b-9ec8-4af06def0dc4 | -18.64885 | -52.13448 | 2025-08-17 05:08:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9b6124f-a584-3a3c-82fb-f467a7d94a66 | -15.19039 | -48.77562 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66884aaa-68a1-397b-b496-d18c4c63eda4 | -20.89274 | -56.90589 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1acef48-e02a-341c-817a-b5958ea2b15a | -14.9721 | -54.75248 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2635518e-87af-3cb2-a5bb-3a048825f60c | -15.1802 | -48.77098 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c66b0675-4c82-359f-b70a-b88aa96b329a | -14.84019 | -59.64263 | 2025-08-17 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3be59f3f-ed2d-3252-a1ab-75019ab38b85 | -14.98344 | -54.7504 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 0b96ccf6-7c67-3815-a833-18623db97307 | -18.20982 | -45.24686 | 2025-08-17 05:08:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6be8cc1-6c60-3c8b-bdb1-5d18ea9a9771 | -15.64893 | -56.8662 | 2025-08-17 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f314ae1d-b33c-3d55-a028-02ab4ec3b413 | -16.0426 | -52.3477 | 2025-08-17 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c95792cf-acc3-3476-a96c-6c18d56ef979 | -15.1408 | -48.73969 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4108a675-7f74-3194-a0f4-59918398f905 | -15.14043 | -48.74301 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14ee0b8e-2ec7-3c12-8c80-85fe3a08bf07 | -16.84193 | -48.91118 | 2025-08-17 05:08:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861c0cf9-2fa7-331e-90e5-ba468b5bf830 | -15.60368 | -55.99306 | 2025-08-17 05:08:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bfc7cc7-4e92-3625-afdb-f5bcccd25000 | -15.45282 | -53.94361 | 2025-08-17 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8c7f599-134b-3050-897b-0c272add8770 | -14.93305 | -54.69007 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 58a54758-95ac-3b7d-9ad1-36197eb0ef62 | -20.99877 | -56.87182 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f880bd7-0d1f-3848-a0aa-a068f8c50485 | -20.26037 | -50.64079 | 2025-08-17 05:08:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4c67edb2-61d4-3098-a75b-cabfb564446c | -14.8442 | -59.63946 | 2025-08-17 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 742c2ed9-4b6f-3e02-b6b5-cbf68c4b5d72 | -15.6452 | -48.11912 | 2025-08-17 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3a7bef6-e448-3bde-9e49-f47b64bd7882 | -14.96013 | -54.75913 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0ddb08a2-e53f-30ef-9a39-8ff022c5ad88 | -15.19001 | -48.77895 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de3008d3-8fd6-367d-bf83-e454175f1696 | -14.92945 | -54.6895 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dd956f44-970d-3198-84f5-d6d274cbd692 | -15.73138 | -48.40745 | 2025-08-17 05:08:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7da0a4ee-490b-35be-bb2e-ebe08e6b13c5 | -14.97928 | -54.75376 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8dec1071-e6d6-3a71-bb44-1973bbcf15c1 | -17.40634 | -48.12167 | 2025-08-17 05:08:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 187c3f13-d930-379a-abc7-a6fcd8cd8d03 | -16.62756 | -51.36779 | 2025-08-17 05:08:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 152fb12b-dbe5-3bd2-8aa6-ee1ceec5adbe | -21.77924 | -56.49899 | 2025-08-17 05:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08606514-2fdc-3d3f-a598-271a7d5df796 | -15.98558 | -59.51318 | 2025-08-17 05:08:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc617b49-e354-30e2-b2d6-a31fe6b6e571 | -15.0533 | -56.04814 | 2025-08-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1572cf92-d41c-3866-9c67-0d7b7d94b44f | -16.6304 | -51.38189 | 2025-08-17 05:08:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aad07ef3-a844-31e5-a58b-d0568ac5b992 | -15.14091 | -48.74455 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b53ce0c4-86e0-3f8f-b630-bfce642ab076 | -16.63209 | -51.36835 | 2025-08-17 05:08:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acd95dac-bbde-30f8-b22e-d2bfa930ddce | -15.14701 | -48.7384 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce4041d5-7a90-30cd-bc43-04449bb474cd | -15.1413 | -48.74124 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b75f030-4300-332b-b9c4-23826fced346 | -14.70693 | -59.66308 | 2025-08-17 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afed1dc1-ccb6-38f4-95a6-cfb0a55a28f7 | -14.92282 | -54.68421 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d9358876-055a-3d78-a947-5e8c90b20737 | -14.98043 | -54.74573 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35323816-9687-3f66-a053-d03fe0c73548 | -19.53821 | -57.82192 | 2025-08-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 67999e2d-b100-362c-84cd-ebf454836cb3 | -21.0756 | -49.3909 | 2025-08-17 05:08:00 | NOAA-21 | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bb860ac0-e627-3bbc-98a0-ce18fc301992 | -15.05101 | -56.03993 | 2025-08-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61391d03-15bb-3c27-98bc-07466131875a | -20.01435 | -47.70515 | 2025-08-17 05:08:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed73a307-ce0e-364e-91ca-0b400411ee1d | -20.89459 | -56.94337 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5691db3f-905a-3f27-a4b1-f5ea03efa832 | -17.89445 | -46.12817 | 2025-08-17 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbbaa8ac-fca9-3246-be8d-23d475432394 | -14.96673 | -54.7644 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e74fe40-4150-3ecf-88fe-a3771e1be482 | -14.92584 | -54.68895 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cba6f6db-5637-39d8-b975-ce1d7e644d61 | -21.00225 | -56.87242 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b3cd887-46e3-3857-8fe4-0db434fc0514 | -14.92398 | -54.67587 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 261f3888-4fdb-39c4-ba69-44758439a963 | -15.14575 | -48.74348 | 2025-08-17 05:08:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a478aa2-3d09-3d56-965a-2beafc54ea7d | -14.95653 | -54.75854 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f971a0fd-e4a1-37ec-a9ff-a4a85cb2e3b2 | -20.9004 | -56.95258 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0421925c-a8b8-3473-b1d8-85d9d7c65a22 | -15.4526 | -53.94548 | 2025-08-17 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e521ba8f-b492-3237-b419-828d77ae0dde | -15.0499 | -56.04752 | 2025-08-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35737b8d-22c8-3c30-9d4f-3f2294664499 | -14.96072 | -54.75497 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd6a525a-8aa2-3fa3-80cb-4d1b9b4cf70d | -20.47769 | -53.67689 | 2025-08-17 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1ef09ed-334c-3ccf-91ee-b1436a8f98fa | -14.96733 | -54.76022 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02ff0996-0168-363d-ace9-fee2ea49978f | -17.49236 | -45.85444 | 2025-08-17 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03fdc265-209e-376c-8c5a-5270adb793ee | -20.86655 | -54.96553 | 2025-08-17 05:08:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8bedb31-3690-3047-9da1-70e527816c55 | -14.80259 | -59.59049 | 2025-08-17 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 995010b1-c18f-358c-a6d7-fd851400f73a | -20.89636 | -56.95608 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce0adf09-3b97-34d5-b2c0-fead4c326593 | -17.412 | -48.1224 | 2025-08-17 05:08:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb1ec692-c869-33b5-8daa-adfcd09e54bc | -14.97985 | -54.74977 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 85e52d80-e61b-3301-a533-74819bc86266 | -19.16706 | -46.58195 | 2025-08-17 05:08:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f00ccd-6eb5-3b89-8ce3-78bbb72fbfa1 | -20.92695 | -56.89043 | 2025-08-17 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45c4ead0-6da3-3257-ad34-f5c7f9e9230c | -20.87036 | -54.96622 | 2025-08-17 05:08:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fb972ad-2c68-3a1d-a15c-cca424492b83 | -14.92642 | -54.6848 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca035dc5-9c5d-3286-9a0f-35e8a697251f | -19.35411 | -46.10352 | 2025-08-17 05:08:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3e47e9a-13d6-36b3-9d78-17f0564792ec | -14.98403 | -54.74628 | 2025-08-17 05:08:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0cd5f8d2-c1e6-3a90-825c-51d8a0d8897d | -15.05045 | -56.04373 | 2025-08-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README32.md)
