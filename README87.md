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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a587162c-e696-3661-aed1-ccab0073fbc6 | -20.63754 | -45.93224 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| df507302-e748-3c21-b5a9-64ed12c53824 | -20.33171 | -46.2151 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1757ce95-eb02-3f6e-8e0e-54e5f8c4835c | -20.05196 | -46.3728 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b7ba85a-164c-3d0c-a2a8-49fbb0bf14b6 | -20.04808 | -46.37587 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6775708b-345b-3f91-b0a7-66adc0c1cadd | -19.79845 | -45.61962 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3baebe79-420e-3763-82be-aa79bfbc43c9 | -19.53755 | -46.09679 | 2024-10-09 04:17:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d3ce9d-8da3-35a0-a84c-5165c8a1bd83 | -20.38998 | -45.39318 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1b480bce-cd75-31ce-88be-ff225995a3d8 | -20.3541 | -45.319 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d443004a-4f8b-36fe-af43-6cca694650b8 | -20.39331 | -45.39376 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b0650726-f478-3908-a6d0-1681aee119e0 | -20.36077 | -45.3201 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4201b7c1-a76c-35ce-83a4-0d4b799ebaef | -20.81315 | -45.62783 | 2024-10-09 04:17:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9133e6c0-f301-3190-91be-fe9f73454d55 | -20.80926 | -45.63099 | 2024-10-09 04:17:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a37f5121-907b-3e0a-a1d3-3ee6c51b20bb | -20.66136 | -45.90996 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51cf292b-74e8-3ca5-82bf-bdc74e625b6c | -20.66079 | -45.91364 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31fc392b-acb3-350a-b9ed-35a7b3430191 | -20.65094 | -45.88934 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38f21e7d-1658-3bf1-a12b-a6af8a2ea1d8 | -20.63431 | -45.90906 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e53a71e-1a62-3637-985c-dbc93702f5fa | -19.80564 | -45.61708 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 30254fc0-9779-3b07-92ff-14eeede6acf2 | -19.75202 | -45.96489 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4c76eec-d790-3fab-851c-89c09145334b | -19.66539 | -46.23476 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fa6889f-8934-3dcc-a35a-901f1f3737e3 | -19.53424 | -46.09621 | 2024-10-09 04:17:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f834b7e1-0227-3f7b-9ce7-dd6a99a9e222 | -20.81259 | -45.63155 | 2024-10-09 04:17:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 33aeb4f9-6676-3c56-8bc4-657ebc6ee87d | -20.66694 | -45.89577 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e91b8b1-fde9-3f52-a09d-54ccd9aeaa08 | -20.66637 | -45.89946 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd2f00a0-5288-32ea-b260-aaed3dd79899 | -20.66524 | -45.90682 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9209ea6b-629e-3e4e-a58d-8bd716545d96 | -20.66467 | -45.9105 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4430adea-2eef-3818-bc36-9eebd23c081f | -20.66306 | -45.89893 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00831659-54be-3d3c-a611-ae35181fdff4 | -20.66249 | -45.90261 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcab1246-b275-3c78-b719-393605c72f3e | -20.66192 | -45.90628 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33c8ca1c-37aa-30ce-9759-ef65fa8ae9ae | -20.65312 | -45.89725 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be255870-4c46-39c2-b6aa-d1fc35e8030e | -20.64198 | -45.92549 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 753086be-fe8a-3abf-9483-8e2ec00e1d64 | -20.64141 | -45.92916 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 05af4ef4-47f8-3e53-aeb3-dfccb58885cf | -20.64028 | -45.93651 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 867c8554-213a-3dcd-83a7-f610efcc49c4 | -20.6398 | -45.91759 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ee3fd6f-d4ca-30f6-af1a-f6620a01dba1 | -20.63923 | -45.92123 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6424eb40-063c-3236-beaf-9d0a580ae1d3 | -20.63867 | -45.9249 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25b3ab98-f271-3a10-bd6d-5e0ada20aa3d | -20.63762 | -45.90966 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51e0ea23-eaaf-3ef6-a67f-7c60dbaa42a8 | -20.63697 | -45.93594 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57d5d6f9-973d-392c-87db-a32d4e1bb156 | -20.63649 | -45.917 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6816d4c4-6882-3f01-83a2-ee54a78d4736 | -20.63592 | -45.92065 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87150f81-3482-338d-9311-754aa5fce667 | -20.63423 | -45.93166 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1746d5a0-8cbf-3f8d-844c-656595278d1d | -20.63374 | -45.91275 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33ae60f5-de8c-3db4-8aba-0377df9107c9 | -20.63366 | -45.93536 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb9adaac-9746-3e47-9561-f9f87a84d1a3 | -20.63318 | -45.91641 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22cfff47-a581-3c42-b38e-a7f50e62c70e | -20.32318 | -46.16099 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e5e8d90-f1e1-3d8b-9a4e-1a2a0db4cd16 | -20.05411 | -46.38068 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc2dc87-6e65-34b5-92ea-8436b5e56467 | -20.05138 | -46.37645 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43f004c3-bbe4-3e35-a55c-715ef5298db3 | -19.80232 | -45.61652 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9e277a40-ff2e-3ba3-91fe-3aa6bf3caa81 | -20.35687 | -45.32328 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0b323c13-c8ca-301e-a38a-b10de24d3ac0 | -20.40507 | -45.33845 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 91d1041d-38e8-3cd4-b74c-2baa4189f94d | -20.39275 | -45.39748 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 015ac3c4-fd44-3341-85bf-51ac236ac6be | -20.38942 | -45.3969 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6cd73923-90cd-329a-b0fb-64c595a135da | -20.36134 | -45.31637 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 0d22b1c0-97cf-37bf-97d4-384d184abd52 | -20.358 | -45.31581 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 08179a43-7b00-3272-82e3-04d9e8ffe9f6 | -20.35743 | -45.31955 | 2024-10-09 04:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| bb7df758-b63f-35fa-b856-99686e033c23 | -22.28622 | -46.81096 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f55b4308-dd6f-39af-b61b-573301747c62 | -22.2835 | -46.80665 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c733d09-6ef5-371c-ae26-951da35cda84 | -22.28292 | -46.81036 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ece9688-d2cc-3469-82ad-8c009252312b | -22.28234 | -46.81408 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4539afeb-54a0-353f-b632-7b5366f8a4e3 | -22.28019 | -46.80605 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362e1951-7b89-3f6f-83f6-d71cb3ce864f | -22.27961 | -46.80976 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abf5e235-6dfb-3ba5-861b-e1f4f0f27661 | -22.27903 | -46.81348 | 2024-10-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4121886d-a569-34a1-a653-fe0faeaba042 | -22.27358 | -46.80486 | 2024-10-09 04:17:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5a63f5-adeb-3a99-b7c1-8c1b51f373f1 | -22.41121 | -45.95568 | 2024-10-09 04:17:00 | NOAA-21 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1264753b-7d6e-3ba2-a3a3-4ab549674c76 | -21.60343 | -46.61032 | 2024-10-09 04:17:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9eb0b39f-e9eb-30e6-8afa-70eac07f30ae | -21.52069 | -45.60101 | 2024-10-09 04:17:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 6db49495-4c8d-3539-a830-b18e50de9f54 | -21.52012 | -45.60476 | 2024-10-09 04:17:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b20fbc0-39c3-37f6-b123-390e5313d66d | -21.30503 | -46.12265 | 2024-10-09 04:17:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f83a9aed-f8fe-3f2e-8486-138b82274570 | -21.30446 | -46.12631 | 2024-10-09 04:17:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8096a43d-e68c-31a6-ab63-499547d7fb16 | -21.30172 | -46.12207 | 2024-10-09 04:17:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e59771d1-0dd3-3fac-90c4-a332b2bdf469 | -21.30116 | -46.12572 | 2024-10-09 04:17:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| daedd7e0-8529-32cb-931f-9290c93fd1f0 | -21.22721 | -46.66553 | 2024-10-09 04:17:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6552efe-3a7e-319e-bed7-983625b82ce9 | -21.15341 | -45.82655 | 2024-10-09 04:17:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c152f6a5-6156-3f4d-857a-23ae1c774fe5 | -21.12087 | -46.75671 | 2024-10-09 04:17:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 097b0b1a-cf83-3a5c-ae9a-b0caa64b3ee7 | -21.11756 | -46.75612 | 2024-10-09 04:17:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| faa638b3-b14b-3d97-9950-a7edce9d886d | -21.00963 | -46.12057 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0710a1ec-aa29-3052-9684-29432b4b5d8e | -21.00347 | -46.09357 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3982005c-99f8-3ac3-95e0-025dcabc0b28 | -20.92525 | -46.46517 | 2024-10-09 04:17:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8685d393-43d0-3973-b8c3-c4752f36e26e | -21.0101 | -46.0947 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| da905eaa-1a48-3191-83e9-e375b06a611c | -21.00953 | -46.09838 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f31e2cf6-75d1-3933-a834-390b2aeb84b7 | -21.00679 | -46.09413 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7f8b377e-1e44-3ded-96a1-b09368d752bf | -21.0029 | -46.09727 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79843976-0807-3800-ba8e-e4f34ad46934 | -20.99938 | -46.14201 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c6547a7a-a83e-354c-8d0f-ffdddade270b | -20.92195 | -46.46458 | 2024-10-09 04:17:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 14c1ef90-939e-35b8-886a-fb9eb42219c6 | -21.60674 | -46.61092 | 2024-10-09 04:17:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a2345c62-a4eb-3113-8336-9c26da04465d | -22.08436 | -46.9695 | 2024-10-09 04:17:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63203880-0cbb-3118-947d-974fe9f49d6d | -22.05957 | -46.88929 | 2024-10-09 04:17:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aeb8290-dde1-3fbe-bd25-b1d510926a46 | -22.05899 | -46.89299 | 2024-10-09 04:17:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3b27ace-aaaf-337c-90c2-738637088856 | -22.0869 | -46.71524 | 2024-10-09 04:17:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7d40da8-97b4-390f-b91f-ed8e6be67075 | -21.89031 | -46.71066 | 2024-10-09 04:17:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 286e9797-958e-3dd7-982f-6c2fb360dbb9 | -21.88973 | -46.71436 | 2024-10-09 04:17:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3817d904-ed5b-30b0-b5bc-1c3adda3b1a6 | -21.88915 | -46.71806 | 2024-10-09 04:17:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a556b742-2a6d-361c-a6db-3e77bb24cf9f | -21.88642 | -46.71377 | 2024-10-09 04:17:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bbe9cee2-d326-30ec-be88-6ba6f17c7008 | -21.88584 | -46.71747 | 2024-10-09 04:17:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b1df12a1-d9b8-309d-8403-2d750f5a4e57 | -21.00622 | -46.09782 | 2024-10-09 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 850de4be-065f-33fd-bc27-5fb8bf5fb182 | -20.91864 | -46.464 | 2024-10-09 04:17:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3aa956a6-48cc-3561-8adc-91f7d7cb0ab4 | -20.92252 | -46.46091 | 2024-10-09 04:17:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 95a43ba8-f70e-3e49-9798-4b49306d2a20 | -22.7501 | -47.12728 | 2024-10-09 04:17:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b21802da-a4df-3e32-ab76-ece90b7e1b4b | -22.74951 | -47.131 | 2024-10-09 04:17:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11539518-c1b6-3804-82a3-911e5b6e94c2 | -22.61335 | -46.98021 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f091462-2454-34da-9e9f-95b74d7a18fd | -23.05331 | -46.26655 | 2024-10-09 04:17:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README88.md)
