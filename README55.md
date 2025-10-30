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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a82bfdf6-4999-3d8a-b96b-5a396c274ea8 | -17.1122 | -43.49377 | 2025-10-30 04:27:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cc6cb96-c574-3e35-bba3-5d6968ac9a07 | -13.92889 | -44.20129 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c6c0805-15ec-33b7-a44e-192fd6392d6d | -13.74469 | -48.38962 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14dbe2ca-11c0-366b-b0ba-f116293401f2 | -13.88534 | -43.93465 | 2025-10-30 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11703c88-98a7-3f57-8f7a-fc00e252d708 | -16.80891 | -41.2276 | 2025-10-30 04:27:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 82a768e3-d4aa-364a-9adc-097d9cac3970 | -13.6715 | -47.17137 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24887464-189f-384a-ba6d-462b95ba1f0c | -13.94882 | -48.43061 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0145e16-f820-3ad5-b4dc-7e843c246d27 | -12.69235 | -46.32792 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 687303f5-c098-3e01-88ff-c5c5927e10c0 | -13.20138 | -44.48532 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 206b905e-fcee-3cfb-878e-916a950f6cef | -13.62869 | -47.05464 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31ed19b5-d548-39d8-a37f-c973a914696a | -13.47064 | -47.9988 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5f78514-308f-3de4-84e7-7d047ff86707 | -13.41102 | -47.38461 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a7e1a7e-1a1d-37e0-969c-32d360ae30fc | -15.58726 | -43.158 | 2025-10-30 04:27:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b7eb39a-0cee-398a-b395-4a5a1ed13d29 | -19.33753 | -43.0612 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| ee247070-d0f2-3504-86b9-da19591501cd | -14.76415 | -44.96616 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12b29e57-825c-3b48-a984-47538ff9143c | -19.33233 | -43.06831 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d351ca6e-33a4-3a61-9951-37404514fa2a | -12.48439 | -50.60207 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c21e4176-eef2-3220-b63a-09890b3f9723 | -17.78517 | -42.93653 | 2025-10-30 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 134d2f7a-8ec3-35df-bd7a-471759e97674 | -15.28107 | -44.10768 | 2025-10-30 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 136b0bcf-3751-3542-8a65-2840ec3b516f | -14.24678 | -47.31563 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4579587-615b-31ba-8feb-af0ce481985d | -14.76355 | -44.97039 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7540383a-f0cd-3b82-9770-57dc459e2ce1 | -13.94277 | -48.42594 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d4601d8-9f9a-3578-b7bb-3069150f91ba | -12.48646 | -50.56828 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4c570527-8ec8-38e6-95f8-694b51f337f4 | -17.14627 | -41.93499 | 2025-10-30 04:27:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5c834d7d-d174-3fee-ad40-042b2d0dcc0e | -14.26953 | -47.30066 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 375fff52-1d1b-3b28-90dd-3d6128053940 | -13.62537 | -47.05409 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 260866c2-4f96-3c68-9b1d-0ad6c18e8fba | -13.67537 | -47.16839 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f4b49d2-1e75-345c-8eb7-7dc2b6d66b1b | -13.21703 | -47.73283 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 831d431d-774b-3a59-abcf-b994be60322d | -12.49716 | -50.57016 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 319a0951-8aca-3377-ad88-4939d743b6d7 | -14.68921 | -43.15304 | 2025-10-30 04:27:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1c395fa3-ba4c-3aae-8b97-d8e2155ae9c7 | -17.38145 | -41.03471 | 2025-10-30 04:27:00 | NOAA-20 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5301aabd-93b4-3840-8bee-e9a573354cf1 | -13.31484 | -46.77701 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4e6e9270-fcaa-3391-8142-3d97bcdf2098 | -13.21759 | -47.72931 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a21256-6933-37eb-a4de-39ec6edf053e | -13.30381 | -47.70024 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bafec265-c989-3f39-8f5d-154d86d21161 | -12.4829 | -50.56765 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fa1dc4ed-f58a-39aa-aca9-11812309925c | -12.03638 | -49.94736 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b668c2-f62c-3b7f-ae43-cafcab54af29 | -12.76979 | -46.65792 | 2025-10-30 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 033dec58-7be1-3a0e-9db3-deb458a91419 | -13.55237 | -47.13096 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da80b0a3-71e7-3357-86c2-9a2f614941d3 | -13.56677 | -47.3659 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6891bfc-6695-36f9-bbc9-14ac9fadc075 | -13.74413 | -48.39316 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cb92f18-8cbc-3bf6-b42f-45081727d305 | -13.36455 | -43.08757 | 2025-10-30 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 83cacc52-c770-3868-b949-a4b4a32f593e | -13.22612 | -48.55205 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd925c5f-05d7-3a0e-a132-61ea3bd10959 | -12.49003 | -50.5689 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5eeb0c11-45f3-3c76-ba7e-45f6d7c56f0f | -13.56405 | -47.31791 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b58929cf-97f6-31fa-aa22-5bd035c50942 | -14.77013 | -44.97575 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98eef11d-f1cf-37d7-a584-dfe1af7dbdb2 | -12.51351 | -50.56025 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9ef25a37-3b7e-3358-bb92-c2ddf550b841 | -12.47863 | -50.57116 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2aaeef05-40d0-3a1c-ad17-2b3384745737 | -13.90671 | -48.45988 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 152f68bd-9969-36ad-9fd3-bfbf93aa3bef | -14.33687 | -47.89144 | 2025-10-30 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c65d2133-5fce-31d9-b427-181104d00d0d | -13.21428 | -47.72876 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c8f2fb9-7e22-374e-86c1-c923d7641bd7 | -15.32319 | -42.99427 | 2025-10-30 04:27:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81372f8b-b1f1-3ab4-8ae8-3260f5140a97 | -14.71232 | -42.44917 | 2025-10-30 04:27:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49d6444e-e36b-3332-9c47-b67aac268df5 | -12.11493 | -47.13858 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbb7268c-e264-3f34-9e4a-32c8349f9cc0 | -14.12038 | -46.38451 | 2025-10-30 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2771a57e-6ce7-3660-be41-9143eaffde71 | -12.31477 | -48.0658 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ab79eba-de14-3ccb-978f-cdd6cb32000a | -12.18883 | -46.70842 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d174e7a-2aa0-3ae1-9e50-68498adf1c65 | -12.54525 | -49.5719 | 2025-10-30 04:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c25e3bd4-528f-361e-9cb9-7fe63b859e16 | -12.24337 | -47.93825 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86322f21-eb1a-3793-8ef8-14bfff77792b | -13.10752 | -47.10967 | 2025-10-30 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa99f740-7e36-3371-89c7-8196eb9ac0ec | -13.4441 | -47.23693 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7220fa0e-24bd-39c2-857c-1288408e7953 | -14.75559 | -44.96172 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 342d09d8-b527-333e-91e8-b7e2573a911f | -12.49786 | -50.56601 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a74a1792-f286-3293-9334-6000d79c5b76 | -13.6776 | -47.17593 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e4121d0-0201-34fc-909b-497c8eae2de4 | -16.81353 | -41.22841 | 2025-10-30 04:27:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fb0b0afd-e17a-345e-9b93-f0915471175f | -12.48219 | -50.57178 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 37a39252-9d72-3584-b42b-38285cb55bb9 | -18.12705 | -42.60824 | 2025-10-30 04:27:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 67e43cf6-2be7-31db-afc3-bb47a0c1b1ea | -12.75361 | -43.44937 | 2025-10-30 04:27:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d16442da-e99e-3a2c-85a7-b6b7eae860fd | -14.2325 | -44.32175 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fc56ec4-efcf-3854-80cf-57846e0213a9 | -12.68955 | -46.32378 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ad41363-fac7-354d-b736-9c8688e77fdc | -13.84207 | -44.15848 | 2025-10-30 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a88b027-209d-3c39-ab2e-ca24bedbf9ac | -15.63088 | -48.87764 | 2025-10-30 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3908d229-c2ee-39aa-8c79-334f75f74179 | -14.90171 | -43.10212 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1c6d2b9a-3ebb-3331-9db1-0d2a6372f628 | -12.28665 | -50.31263 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed6b351d-828a-3d9d-991d-2348a3a38e03 | -13.56346 | -47.36534 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33f3c5e4-b937-3d62-9d4c-85714398c05e | -12.88804 | -48.6424 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb709b09-d699-3d66-8f9e-ee52db177f1e | -14.24734 | -47.31203 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8a48755-4c80-3ffa-a679-9db817b208df | -15.02202 | -46.31969 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9493d431-3915-3a12-825c-50dabf4dec09 | -13.04177 | -48.46983 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b924fa7f-4a4f-3dc2-9bff-eae1d956dd31 | -13.61943 | -48.25958 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cd322c2-73ce-3df4-8a63-0f8c45d0dece | -12.495 | -50.56125 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 184d5d2d-800f-37fe-962c-6f29fa8aa204 | -13.65414 | -50.61755 | 2025-10-30 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7130c30-a812-354f-a364-ab6b725b1374 | -14.39111 | -43.71786 | 2025-10-30 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c735a169-4d73-33b6-bc48-98c35780da3a | -13.03628 | -48.46156 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46bb2833-8d9f-3738-bbee-4daddc5171d2 | -12.94506 | -46.5346 | 2025-10-30 04:27:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ba9da50-f502-36e2-8ea7-9ea42c703656 | -13.26845 | -47.75237 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 311877b0-1e30-3083-9259-a0c3fe13a74d | -13.35013 | -47.66446 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acf3aac7-9bac-3dbe-932d-0d08ce4abd51 | -12.39424 | -46.82864 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e980a1ce-3f70-3821-a91f-646bb21b79ad | -19.89317 | -42.63734 | 2025-10-30 04:27:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0e3afdcc-3197-378b-8483-84c20154c0ac | -12.84714 | -48.62424 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8cdcf16-cd2f-3578-b8ce-e95e20f5583f | -13.0435 | -48.45911 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 512ba7ea-3576-3bec-95e3-7d12063c0cf8 | -12.29843 | -50.26476 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a765fd80-eca4-3e84-a97a-66245a092d90 | -13.28558 | -47.72983 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a148151b-7747-3515-bedf-fefc57af2a79 | -13.03513 | -48.46872 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b91a2bf-f57c-3a2a-92bd-faa4fdd22dfe | -12.11437 | -47.1421 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 603b9ddb-85bd-3709-8354-5215f37ad890 | -13.17183 | -48.4441 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54ffc483-9b2b-352b-9e28-b3094fbe688c | -13.17286 | -48.45885 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01bbc562-e6fa-3309-b229-a6a65c8604be | -12.71076 | -46.2976 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd993b1f-c3f8-3091-b139-2882bd9cea08 | -12.48152 | -50.59729 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5853308-67e3-34a4-ab7f-55494732db8a | -12.88538 | -48.64185 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 621541a2-1891-3f7e-9aec-d3ab19f2759e | -14.12822 | -44.06925 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README56.md)
