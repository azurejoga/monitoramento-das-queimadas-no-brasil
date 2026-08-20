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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75d74069-68de-3ef8-8b21-7c8dd5c7f0c3 | -12.01011 | -53.44358 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebaab1d6-7129-33c9-8477-f9afd9ede5f5 | -19.46073 | -46.81671 | 2026-08-20 04:21:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdf49e11-0e1e-3837-beea-3226d82f9ac6 | -13.40871 | -54.36604 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07793d16-1a05-3800-9bac-8c02edb0b6ef | -12.83793 | -48.42607 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cad25d5-cace-369b-adec-88653e31d705 | -14.02746 | -53.63454 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b41dd96-9390-341a-ac08-ba4afe9b323a | -18.78922 | -48.5533 | 2026-08-20 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ddb2cb6-4337-3263-849b-6acad8a0ecdf | -19.76989 | -46.04369 | 2026-08-20 04:21:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f35a1ae1-61b2-3512-a1b4-f20ff28de86d | -11.19978 | -54.00448 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb8e6df8-69ce-39e8-b059-522e8d67f934 | -11.21661 | -55.06338 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ddae425-361b-319f-aa55-b09f371303a9 | -14.2264 | -51.92525 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c748e09-f495-3914-9519-bd58c9edde8d | -11.90349 | -50.15688 | 2026-08-20 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76aebd88-3041-3b20-bef2-9b34764b6aa8 | -11.82948 | -58.83779 | 2026-08-20 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4707f21d-05e9-3b41-bccd-f6bbf9f1ab35 | -17.39329 | -44.91557 | 2026-08-20 04:21:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f99a6052-9b5b-3671-9e87-8408f8c2f2da | -12.84981 | -48.42329 | 2026-08-20 04:21:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf3f6b8c-ad84-3923-91df-b0e26a0ab691 | -15.36181 | -52.74955 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f3c2a41-11ed-3214-9a81-838070ed748e | -11.21326 | -55.04982 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7bf97ab7-7b27-3a83-82ba-5a0b781093c0 | -19.38967 | -46.4099 | 2026-08-20 04:21:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36a752a4-858b-3db0-b323-df65dcd319d8 | -15.44555 | -48.58966 | 2026-08-20 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc614e99-8635-3a4b-b572-6b271403e8c6 | -18.84413 | -47.13858 | 2026-08-20 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6935e58d-a7a0-3271-ac9a-0ead46653df0 | -14.19912 | -52.88684 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a6862f8-41b4-3805-8ae0-e2cd6421fcf3 | -12.83263 | -48.43467 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5653ea5-8df2-382f-9ce8-01de6e61af07 | -13.44438 | -57.08052 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 237d3a7f-8a9e-36e5-bb0f-05c78340ed8f | -14.22181 | -52.89744 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d10513e4-0337-3b77-b11e-fca915784153 | -11.4139 | -54.31229 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63bfcd26-0b92-31b8-8e32-532f84a1a6c3 | -14.23172 | -51.92156 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40da090b-d7d3-331c-87f0-638be1435813 | -12.47561 | -54.18075 | 2026-08-20 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e93b6a3-856f-3dac-b46b-2640cdbc9661 | -19.65541 | -46.18932 | 2026-08-20 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f9eee21-ff7b-3d40-8f92-8f81b985950f | -14.29144 | -51.91096 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de2bda81-5a7b-3b52-90ce-8e6c9c5dc918 | -13.54443 | -52.23325 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fea83a20-f99f-3e70-93d1-ad739ab79139 | -13.4736 | -51.43919 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c1f8a19-b243-3f61-a4da-316a16e5458d | -14.22725 | -51.92067 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae4fd44-355a-357e-90cc-77b27436193b | -12.84906 | -48.42761 | 2026-08-20 04:21:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23f91512-5f14-3600-8a42-025e432fefe6 | -12.80695 | -48.43691 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b3eaa3-04f4-3330-bc9b-a58912932e3a | -12.00042 | -53.43836 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81cf7f85-e8d7-3dc3-8c0f-5011d31844a2 | -15.36139 | -52.77689 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b477ebeb-3b34-33f7-aa2b-03ba77274d66 | -12.80171 | -48.44545 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b438897-df35-3518-9fd2-a073093e2c30 | -15.18258 | -48.76328 | 2026-08-20 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adee4343-4f75-36d7-87e1-523b7aae50d5 | -12.01151 | -53.44436 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2153637b-d0d8-3b25-9b7f-91cc868757d7 | -12.23235 | -49.39302 | 2026-08-20 04:21:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26622988-3a1c-3045-ae1f-0c221a0f115b | -18.85019 | -47.14346 | 2026-08-20 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 953e8d10-e95c-3871-a039-48907aea0d9b | -11.19303 | -54.01038 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d6f6d1e-3aef-3abe-b93e-4265c83ab1a3 | -16.07104 | -54.9674 | 2026-08-20 04:21:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 360d4bce-1232-3186-97a7-313ececf4e47 | -14.9438 | -44.31867 | 2026-08-20 04:21:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4008114c-89c2-35a0-b655-adee5ca0d554 | -11.21901 | -55.05111 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d139fea2-0afc-314e-830f-b07cefe1af6e | -12.79805 | -48.44455 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 565d7c1b-9886-322e-9bbd-8ea11e503e09 | -11.99528 | -53.43735 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79fff11c-342d-32c7-bd74-7405ea6e8189 | -12.79598 | -48.43434 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2821e1b-8f98-38ad-a266-ab515fe98145 | -13.5661 | -51.67025 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca857595-af6d-3de4-8f8c-e7cdfa2add3f | -14.11615 | -44.38424 | 2026-08-20 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2036749-e313-39aa-878f-c43a666c1a28 | -12.77736 | -48.45433 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71654465-b4e6-375c-ad26-6cd188b8ab0f | -11.99983 | -53.4415 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6965d732-a943-300f-b12d-c2a52ad36b6e | -15.5676 | -43.43455 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89feea8f-f255-3649-8689-5ca1e262ce2a | -11.20669 | -55.05265 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b10dc6ab-472d-3d9a-920e-73a73c9f4d16 | -13.4392 | -57.07383 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101d2982-0102-38d9-b631-6b5efcd5d069 | -11.19371 | -54.00687 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e6b87cd-c5c0-3de6-b458-6b522c944363 | -13.54539 | -52.22828 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b040fcb3-b41f-37d5-bf37-e2325a09701f | -14.31822 | -51.91611 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e1f6bab9-78b4-3a28-ad0a-88b623b2a8b5 | -11.81514 | -56.59972 | 2026-08-20 04:21:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ed8aa23-1015-32c0-bff1-bd5d95848394 | -14.2923 | -51.90641 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d1a7b18-b019-3d94-9976-91299b3c0f8c | -11.20517 | -54.00565 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02590f0f-d4e2-349d-b0d5-904ab0d382a2 | -15.36698 | -52.77285 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6e400b6-a73a-3944-a9d1-5c2e97b8a4da | -18.70691 | -46.45238 | 2026-08-20 04:21:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a6fa84c-4328-32a2-80a5-72dc4a709665 | -18.1775 | -44.70933 | 2026-08-20 04:21:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fded165c-9635-3f01-be10-abbe567e6085 | -11.4232 | -54.32082 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e703110-a1be-3781-a5a7-a2793b3af4b8 | -13.60746 | -51.79626 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 412807a1-c89a-3be4-96cc-a1ee70ea5bca | -13.44889 | -51.42525 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bf50047-3d6c-3f46-9ce8-7c2fc5fd02d9 | -14.73405 | -47.15546 | 2026-08-20 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcc879cf-3ffe-377b-9cf4-4ab73725659c | -16.06645 | -54.963 | 2026-08-20 04:21:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a529c2-aef7-387b-99fc-06a117d70794 | -12.82468 | -48.41492 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca3b0f0b-53fd-3c12-926f-c4d2b2e92297 | -12.82037 | -48.42495 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a72044-0673-38a4-8405-cdd32c145f25 | -11.99587 | -53.4342 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b9b8a82-fba5-3a63-a7d6-c4f97939d49f | -11.1856 | -54.01978 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7daa98a-1e5a-30ac-bcf8-6912eb6b7155 | -14.21329 | -52.89032 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60fdc377-6396-38ae-a5fe-4cc46c2b7213 | -13.56526 | -51.67475 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2134144-87d7-3f38-9a39-53a8e7e7e346 | -11.21124 | -54.00327 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f670d80c-5690-3a8b-84cd-5ed10c14bdba | -12.81629 | -48.44117 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a429085a-6e00-33d0-8af0-fc9952a04c24 | -11.18964 | -54.02803 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94e95907-7262-37a6-9fcb-41f118768b0c | -15.36596 | -52.77818 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb19aa2f-3cb0-3cad-8060-ccf828ed8b0a | -12.84683 | -48.41858 | 2026-08-20 04:21:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6abe96d3-0cf2-3f75-9d97-ee67cefa54d1 | -15.71399 | -47.80366 | 2026-08-20 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5191e79e-a7da-3524-a66c-988c6516fa16 | -13.40738 | -54.37277 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8cbe2b2-3213-3bcd-b3c2-341abc651d8b | -12.82897 | -48.4339 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc2615ad-17a5-3658-80b2-b7577128fc76 | -18.03815 | -44.61748 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 0f9e7057-570b-394b-9028-5923e0f7668f | -13.44171 | -51.80241 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad934af0-c121-3351-915c-f220be2756cf | -12.80488 | -48.42669 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e7f7862-6e82-37cf-9613-e216a1ac8b31 | -14.31754 | -51.94451 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a6f57c2-a9e6-3c77-b2e2-2081e277a177 | -15.85477 | -56.08606 | 2026-08-20 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f86e1747-50b2-37dd-b913-3048394dbb46 | -12.81063 | -48.4377 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ddea15d-29f4-3338-ac58-350951669fb3 | -14.21803 | -52.89139 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f087b0f-ad30-3ab4-92df-91b2deca2b3d | -11.19032 | -54.02446 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 751a83b3-4dfc-3696-be58-af637262656a | -14.01497 | -53.67245 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44487ef8-e523-3d27-bcb5-d43c107065e4 | -11.19911 | -54.008 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ceac28fd-bafc-3e5b-a69c-c52b8e0e2dad | -14.21236 | -52.89514 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b8985e0-f8bb-35aa-9ca3-69469b49c0cb | -15.44268 | -48.5848 | 2026-08-20 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e3389c-1f4e-3eb3-878c-cc4f995876e2 | -13.40069 | -54.37864 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9632391c-e3e3-3a56-acc7-e4d2cc0860c7 | -15.54203 | -50.27483 | 2026-08-20 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28dbde6e-eabb-3ba3-98c2-819106f9c078 | -11.21404 | -55.04581 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2c1c66f-528b-3ee8-8e4a-088a9cc1d0c2 | -12.00698 | -53.4402 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92175f21-0be8-3bb1-b9b5-027f8e482811 | -12.7953 | -48.416 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c64e3746-8e0d-323c-a912-84c161fe4587 | -17.9584 | -41.93476 | 2026-08-20 04:21:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README38.md)
