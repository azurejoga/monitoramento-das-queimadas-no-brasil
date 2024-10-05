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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72927288-8fa1-3af8-a5cf-d6741d64a3b0 | -16.474 | -57.29485 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 08cd4557-1975-390c-bb86-f3ccfc71da42 | -16.45828 | -57.2877 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2ad3b350-b5f9-3b3b-99bf-11f73eac7379 | -16.45418 | -57.28688 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 15dbc822-5bd7-3ca5-a3f5-9d55fe673b9f | -16.45063 | -57.30611 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0fe9a5fa-c3cf-31ec-9985-afcbf3740608 | -16.45007 | -57.28605 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3b138d66-e537-381f-9f09-e8a911649cd1 | -16.44922 | -57.31379 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 360885ba-cf24-3642-a7ff-482f7a0b6e2a | -16.44652 | -57.30529 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cfb0d8ec-49a9-35ae-8fb3-290bbe5167f2 | -16.44581 | -57.30912 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6be6ece8-4002-36d9-a3f1-12e9a85a0e7d | -16.25948 | -56.65391 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c3aa7a77-a948-3f8f-8655-f365f682fc0b | -15.87546 | -57.13484 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc3b425b-793b-3659-b423-326e3172772a | -15.87481 | -57.13842 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab61b692-d167-3130-93b0-0bbd7e2ee690 | -15.87418 | -57.14192 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9180b088-cee4-3bca-a576-891973dab80c | -15.87143 | -57.13357 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d77f06e-f89e-3539-93e7-6a2c1ace93c8 | -15.78395 | -57.35439 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d930efe0-0fdf-3288-9273-943d344f643e | -15.78132 | -57.34525 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| af1d0dbe-b9fd-35b1-90c9-21029976feb0 | -15.77973 | -57.35386 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ce49300-47c8-3332-b94b-fabe0fe6e023 | -15.77633 | -57.34888 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9b262bb-1721-33f9-a522-4678ce119645 | -15.77289 | -57.34407 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2492f3b-e6ef-3a7d-a558-e5c5a5fd05c0 | -15.76941 | -57.33953 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73b43935-0fb4-3cc8-acb6-0423be97a74d | -15.76866 | -57.34358 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 463a4dd6-7070-3126-ab4f-321aad1832ec | -15.76519 | -57.33898 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c75b53bc-de2f-3cc0-a6bd-5ab0c2a5d06f | -15.73125 | -57.42785 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c83cc31-c66e-382e-b80c-cb3cd69401f3 | -15.72858 | -57.41891 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8207bf45-f947-38c5-abdd-63a3c0fdb7d6 | -15.72825 | -57.42006 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c08fd55e-281d-36dd-89b0-f7389e61cd3f | -15.72784 | -57.42282 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5f478e4-d103-353b-bd6a-4c402d96da6e | -15.72754 | -57.42402 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afa79e75-3f78-390f-afdb-2937e4508f2d | -15.72709 | -57.42685 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5eb8daa2-bc04-3ae2-935e-69c241c06611 | -15.72681 | -57.4281 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93f40c7e-273a-3f73-a602-f8060b9ba9cb | -15.72442 | -57.41792 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d3a2e22-c46e-331d-89b5-98de5d49f180 | -15.7241 | -57.41897 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d713d4c6-5394-34c6-bab1-aa761a74192e | -15.7237 | -57.42172 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62ed108b-3dba-32a4-aa08-bb7da04104a0 | -15.72339 | -57.42294 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e4098f3-2e45-3325-81ec-0fc7a701bbc5 | -15.72215 | -57.42998 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25b64a44-c862-377f-97af-3605d40a1e5c | -15.7219 | -57.43121 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b687f7db-9348-3e8a-8f6c-2c2d0b73d40a | -15.72095 | -57.41321 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e76dbd6f-bfa1-3141-ad63-5bfcdbe38452 | -15.7206 | -57.41433 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f616495-e24b-30b2-b992-667f017b39e3 | -15.71876 | -57.42486 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f914bf4-58a1-3d05-bcc5-5c77d8894591 | -15.71847 | -57.42611 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 685a9ae8-5919-3a03-a87c-0152f093a7d4 | -15.71796 | -57.42909 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a17b8980-00c8-3966-bf64-560c43a8db24 | -15.7177 | -57.43034 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb135f94-5ba9-3740-a172-38a4442223fc | -15.71713 | -57.40951 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0de19e5b-fcbd-3548-8020-1d4853b8125a | -15.71644 | -57.41332 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7173cb3e-0e00-3960-a378-b2d06c815d72 | -15.71427 | -57.42525 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8a780e5-c495-3c5f-904d-c8aefac9f8ea | -15.71351 | -57.4295 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9938d276-ea0a-32fd-91b8-77c4b91ba63b | -15.71296 | -57.40854 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac133144-e749-3c47-aff9-7288b65ab2e4 | -15.71276 | -57.43362 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35a170a4-0bc3-3be6-82ad-7f37cb8c2d11 | -15.71009 | -57.42433 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 739d6401-2745-378c-9fa9-238c8fb74a55 | -15.70931 | -57.42865 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e81b617-fc51-3862-9ae0-9e499f442823 | -15.70856 | -57.43279 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8223e369-40c9-3185-90ca-5d31fa0990bf | -15.7067 | -57.4191 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04e9a556-ace4-323f-bcba-bdab83ebaf0b | -15.70592 | -57.42337 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4be520e8-34de-30b8-9123-6701f980b7fb | -15.70529 | -57.40299 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 558cdd53-3671-3691-90ac-13238671fc2c | -15.70512 | -57.42776 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b200dc7c-ef76-3cb2-9dc1-17ad11884a4a | -15.7033 | -57.41384 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85198aa5-75b8-38a2-a885-241dace7ca2c | -15.70181 | -57.39828 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa66abf6-31fe-3c17-84c2-294b70cc4f88 | -15.69981 | -57.4092 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdecc619-fb16-3187-8b06-457bd15ed335 | -15.69762 | -57.3974 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a729ec96-bbb1-36c7-8a2b-661cf4706b41 | -15.69628 | -57.40471 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fbe4a25-5722-3112-9dab-091d1f2181c2 | -15.69215 | -57.40357 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0480c9c6-c7b5-39ca-8a1c-28b339bc9b36 | -15.68801 | -57.4024 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e117b57-fcea-3e99-8d92-abf2800d6cf0 | -15.68316 | -57.40515 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c9bc3c8-f480-3d81-8b74-c80656843543 | -15.67901 | -57.4041 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 302998c7-d4e0-3411-9c49-bac8c6bf6671 | -15.67131 | -57.39875 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd749107-d8a6-3a52-912f-80e677d8fe32 | -15.66715 | -57.39774 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0796d25-56d7-317a-b31b-a00b8fbf1d05 | -15.63841 | -57.3887 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a03dc1e6-7697-3457-b06c-bf090dfdcc1c | -15.63757 | -57.39323 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca451ec0-1241-3921-8ea4-e19deb4a8626 | -15.63503 | -57.38355 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f2120d1-7778-34f2-9115-1ee70cc25be5 | -15.63417 | -57.38815 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f1854e9-6e97-3314-979d-3d02a0c45c54 | -15.63335 | -57.39256 | 2024-10-05 04:40:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69247899-6798-3a07-8596-355ea088c04f | -16.58913 | -57.2613 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 887b2a3b-16a1-318b-afd4-5dbdd357103c | -16.58261 | -57.18141 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 62d5060f-3180-3d7b-a7c9-d4f0e59f5059 | -16.57923 | -57.17683 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3385a3c2-9429-3ce1-bd85-a23f07922370 | -16.57655 | -57.16848 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3326b416-b3d9-3f3f-b9da-6950029522e2 | -16.57586 | -57.17224 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f2442e6a-64e8-39ad-9758-740438d8e6e7 | -16.57248 | -57.16766 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 53875f36-9ef3-328e-bd69-f04ad651f9db | -16.57178 | -57.17143 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 71d3fce9-3992-3f9b-a342-b47a3ea03203 | -16.56982 | -57.15925 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aa252839-2259-3ebb-bba3-c677f1a5c8bf | -16.56772 | -57.17062 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7b04aaea-44d4-3725-9a62-2a75cd19790d | -16.56295 | -57.17358 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1e490349-e751-3b10-acb8-8b9ac4dabdda | -16.55724 | -57.22729 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 67b200f0-3669-3daa-b93a-e3663de7e688 | -16.55455 | -57.2189 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3f664dc1-8c9d-3507-add3-94f2555486d1 | -16.55385 | -57.22269 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a4ef53e5-6dfc-3e87-b3d7-f32cc56a4907 | -16.55315 | -57.22648 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3f9fb58b-6495-31bf-a1c2-48417ebc9615 | -16.54977 | -57.22187 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 7bbf5fd2-2b6a-31a9-828a-625dd3ea8383 | -16.54907 | -57.22567 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 063141cb-aa70-3282-ad5c-5afdfd4c7824 | -16.52153 | -57.25959 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3c44bd3a-3686-371d-8d62-c5b14adf62d9 | -16.51925 | -57.25635 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c7169616-c8bd-35a2-938b-55663967f959 | -16.51447 | -57.25933 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c31aa0c2-2062-38e0-8290-aef225b281b0 | -16.51408 | -57.25403 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ca588de2-e1b5-3954-a086-28c9824fc5d7 | -16.51263 | -57.26175 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0d4e2404-0b12-31d7-840b-3ec96651d1a2 | -16.51191 | -57.26558 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 599282ea-3100-3eb0-9ee6-12d6510596df | -16.4699 | -57.29403 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a1fbc65e-bc12-314a-87f1-856fbc969547 | -16.46579 | -57.29321 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 96b24cfc-6815-30f0-b6fa-d70585d242bd | -16.45333 | -57.31461 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dd01ed8b-63af-3acc-92ab-1eee9fc7ee90 | -16.44992 | -57.30994 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ef351fdd-4d9b-31f6-95eb-d6bbcc8ec083 | -16.44668 | -57.28138 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8404500f-0570-363a-882e-319bfc7f311f | -16.44596 | -57.28523 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d4138015-e5ee-37ff-8617-265e74c057f4 | -16.44312 | -57.30063 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 29ec5c0d-29c8-31f8-a2d0-ff163d17a0ac | -16.4383 | -57.30365 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4e6b2be4-8fa2-34b0-98cb-7468239b2c1c | -16.42324 | -57.38488 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |


[Clique aqui para ver as próximas entradas](README123.md)
