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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9477d1b-af95-3efa-a394-582633be41fd | -14.86729 | -47.96843 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 207592aa-1268-31be-835e-c4c3ae2d6829 | -14.99362 | -54.85817 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97c5b9b6-0f6b-3e56-9a23-f3f4c556c868 | -20.24104 | -46.61407 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec2650e1-acfe-3246-bf10-b8e2039c9012 | -14.28093 | -60.39412 | 2025-08-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fc838b2-4f00-392b-a908-dca947a754eb | -14.82763 | -47.93131 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76713e6a-0ec1-3b3b-8b5f-d4f79c557421 | -14.83392 | -47.93013 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 052e000f-8abe-368f-b83a-0444313ed53b | -20.94953 | -49.16279 | 2025-08-22 05:14:00 | NOAA-21 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2c3122b4-ba27-3b8e-9112-73c117dd95a9 | -20.27206 | -46.57808 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 598bd92b-3b17-3315-a4ae-a7e0e3ac8475 | -14.46715 | -56.47498 | 2025-08-22 05:14:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c2040fe-2e9b-3441-ac93-767bcb5fcd15 | -13.43453 | -57.17134 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bc62195-651e-3d5f-8d63-1f9b4f161bff | -15.13859 | -48.11055 | 2025-08-22 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 915dc028-513f-30a4-af70-36a6ad6162f3 | -15.13777 | -48.11237 | 2025-08-22 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35a05607-3982-367f-ba4e-f229f57d55e0 | -14.7648 | -45.40134 | 2025-08-22 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9afd24b0-8af7-3405-a885-8e4ca98bfc19 | -15.13909 | -48.10565 | 2025-08-22 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1be568e7-8bd4-3ec4-8ae4-6a0a48ec9d78 | -14.54676 | -53.1601 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 558c7590-d037-35a3-90e3-5b87af17ed31 | -14.65096 | -54.87989 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ea60333-8ea8-32e5-baa3-4b6d4e64ab64 | -14.89781 | -47.97353 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2392d912-3e87-3b9c-a2a1-8c4ddd307f6d | -14.63225 | -54.84175 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a92061cf-d235-35c1-ab2f-58e8962a4526 | -20.24163 | -46.69995 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f2f1954-936b-38e6-be37-a7abb3834285 | -14.67701 | -54.86319 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c8bc2ed-9ac7-31f6-9f24-414a97dd3b4d | -14.78501 | -59.66314 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 628baa23-adaf-31d7-8537-3ab51517584a | -15.65957 | -52.68776 | 2025-08-22 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b382c14c-f17d-3d9d-abe5-def8c1969732 | -15.00856 | -54.86558 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1cf3c148-3959-34f0-aef6-1c9b618f4c10 | -14.63418 | -54.85014 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f9ae9a6c-1a92-3d12-af0b-2e2853f8f74f | -14.78048 | -56.03226 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5eb59825-52ed-3bfd-8e0a-af2c43d1d0a0 | -14.76465 | -56.03875 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 474d5af4-f6c4-38a1-b934-2f83c7e5ad83 | -16.56035 | -49.26962 | 2025-08-22 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 696446b1-a499-3d04-9b81-1d96f18bcda3 | -14.76892 | -56.03493 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcf9e0a5-9ecd-3d47-9ad4-e03d7a809d95 | -15.15455 | -47.95438 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b003dbb-2f59-368a-9496-80d8baa16d5a | -20.94994 | -49.15801 | 2025-08-22 05:14:00 | NOAA-21 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0682a892-aaad-3bad-8457-72422ad45fca | -20.30404 | -46.62269 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7c40c63-a6d0-3cff-b648-62e66591274f | -14.75613 | -56.04637 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2312ea59-f64d-33fb-b489-175de21183d5 | -14.277 | -60.39718 | 2025-08-22 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e78217f9-a3db-3288-b344-bb9934685a21 | -14.74279 | -56.03539 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1626316-b1dd-311a-9ed0-f6aa6a4a2a0e | -14.65402 | -54.91609 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a08f7ed5-9fb5-3d0d-85fd-862581ea1850 | -15.02482 | -54.86333 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54da2717-c5cb-3483-9c33-6047e01df31d | -20.43614 | -46.50699 | 2025-08-22 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b21cb050-d0e6-358c-8f4c-629d89245032 | -14.33063 | -53.09812 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86039ee7-0860-3582-97ba-230b88ddead9 | -14.65163 | -54.87488 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d6571e6-d607-364f-b832-9de49e611a53 | -16.18812 | -47.98863 | 2025-08-22 05:14:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d34a4bc-410b-3408-9199-43333a21848d | -13.14117 | -57.11863 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dde1bd26-4bf0-3c72-afc5-628189fb8132 | -14.62115 | -54.85819 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43f0c2fd-b43e-3cd7-8e7a-fe048303bf3d | -20.2491 | -46.69432 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 27cfe199-ce14-3995-b186-9048be60fcbc | -15.02547 | -54.85853 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ffff6e1e-9619-3a96-80bd-c3eb7643de55 | -18.33217 | -49.44558 | 2025-08-22 05:14:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 395a3c69-dfa8-3bcd-91e7-b134b3133193 | -14.58941 | -54.7706 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff52923c-c542-3245-a902-621efced4b01 | -15.73774 | -49.44616 | 2025-08-22 05:14:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09eb0547-cd27-30bc-99ec-ce502790b112 | -14.75496 | -56.02829 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82b2d80f-4091-3d45-85ea-b64467321e15 | -14.59262 | -54.77632 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad4f1712-41d6-31ca-bfb1-ed027daa5275 | -15.00076 | -54.86436 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61ba03af-eb5b-3619-ac9f-fde66f0f0558 | -20.33677 | -46.5669 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f5f271f6-1d0f-3097-856b-04ceaa072f79 | -14.83344 | -47.93458 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d154117-fe50-37c9-8307-03e786b22666 | -14.33011 | -53.10231 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 331847fc-4a9b-3a6d-804f-43766677b158 | -16.55503 | -49.26465 | 2025-08-22 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 813d5f10-935e-3027-8736-86691b1e62aa | -14.79055 | -59.6495 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30e4bed-284d-36f4-abde-f96aa0c868f6 | -20.43902 | -46.50098 | 2025-08-22 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0fad0dc-1294-3021-9b69-1fc1932e5a79 | -14.34905 | -53.12705 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98d0e2ac-8190-34f3-b9dc-1c9f11b5ce05 | -14.73852 | -56.03923 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d04a1841-f52b-3f10-befc-37f5e22fdbec | -14.79385 | -59.65004 | 2025-08-22 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8058104b-87d2-3317-9eb3-19c1d6dcc497 | -14.89531 | -48.05447 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6c21955-6db2-36db-8fc4-205eaff7b98d | -15.15481 | -47.95629 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7e468c3-21da-3f1e-861b-588bbc8d6c94 | -15.03259 | -54.86477 | 2025-08-22 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 844fcbfe-efe2-38c7-9433-5c186a65a198 | -20.24864 | -46.60698 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 296d02d5-6d26-3ee2-a569-0be0b7e24f19 | -14.86929 | -47.94943 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e010f431-54b5-38f2-94de-4fe579a432a1 | -14.83447 | -47.92517 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbf130ee-e329-3ff0-a4a1-2a0438d0cb76 | -14.75977 | -56.04693 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f92c1df0-bdec-37f3-9439-18dfd7b1f6d2 | -13.79899 | -52.86871 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 719157cf-e8f3-3596-89cb-13f766ef29de | -14.63097 | -54.84465 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01a79c83-be76-36b7-889b-e424df632396 | -20.30136 | -46.63297 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fce0f606-d619-320a-a7b8-df595f119af1 | -14.74217 | -56.03978 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0aece62f-ff0d-3249-8098-c271a869f82b | -13.80336 | -52.86932 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15f77923-8a8c-37a1-89b7-d1f8644d77a7 | -14.62046 | -54.86317 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 026b389b-1e1c-30bb-8d86-96263d317c42 | -19.68066 | -48.98942 | 2025-08-22 05:14:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9ac0d69-35e9-380c-af40-97cb9faf64f8 | -14.86976 | -47.94499 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4aa646ae-ead6-3d81-b736-951cac30a7a0 | -17.6137 | -46.70216 | 2025-08-22 05:14:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e33d4d36-cdd8-323b-a535-d85fcede8eca | -14.32893 | -53.09997 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fce1da81-e39d-3fff-a589-206755e8f8a0 | -15.66294 | -52.69761 | 2025-08-22 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbe56961-a0dd-3848-8f82-6cf6a2237b27 | -14.76226 | -56.02942 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f356ff-4caf-3752-9f4d-1d3b0e8d4aad | -14.76288 | -56.02504 | 2025-08-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b7dbc6-2446-3860-8878-a19171ef094a | -14.67312 | -54.8626 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 824fe5af-92ed-37a6-b0a6-a58e551d8661 | -13.19297 | -59.16844 | 2025-08-22 05:14:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8aeefad-4885-3268-b0d6-f264fa092592 | -16.7842 | -47.66671 | 2025-08-22 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38831075-2e7d-308a-8cea-cccf79682a0d | -14.83424 | -47.92755 | 2025-08-22 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| affaa0cb-a8ee-3591-b692-acf1a4daf4c7 | -14.62568 | -54.85415 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 60d29c71-a9db-305d-8518-765a0ffd7b7e | -20.31025 | -46.63351 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecf5f5ad-43cd-3825-b655-7f2aee8cccca | -13.4351 | -57.16753 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb6c3131-e125-3c69-8cc2-c1e920452d27 | -19.67414 | -48.99351 | 2025-08-22 05:14:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1cd12abe-0dd6-3ec8-9f81-9b57a5246d0f | -13.43396 | -57.17513 | 2025-08-22 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c5aa809-3856-30c8-8285-2e5761212690 | -20.2344 | -46.60831 | 2025-08-22 05:14:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b27220d7-b90d-34b1-938e-580dee88f4ff | -16.50744 | -46.74072 | 2025-08-22 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a4a8e83-23ed-3cb9-91d9-2dee47f1fc59 | -14.33323 | -53.10081 | 2025-08-22 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b4b36f4-728c-305e-b962-ca7044aed2eb | -14.63156 | -54.84698 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79d97a31-9081-3e32-80ba-0da1198e84ba | -14.64707 | -54.87938 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b5fc389-9aa0-372f-a662-1434f02bf19b | -20.51344 | -54.63748 | 2025-08-22 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f90be74c-8267-3cab-ad6a-dd5ccb7f4431 | -16.78469 | -47.66154 | 2025-08-22 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b883f89c-78ea-30f0-91fa-4f301dece787 | -18.29727 | -49.5611 | 2025-08-22 05:14:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b7e22508-2092-390d-994c-19cd29c25753 | -14.65266 | -48.11347 | 2025-08-22 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0722b311-4555-3c88-852d-879835e64c11 | -16.5608 | -49.26534 | 2025-08-22 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9436810-af0e-30a1-9197-d2855de9bca6 | -14.61908 | -54.87315 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b678821-c0f4-32a5-9438-b142a400233b | -14.59972 | -54.78272 | 2025-08-22 05:14:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README53.md)
