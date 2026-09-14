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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33f4df32-98b3-3da0-b3d5-ec7041f06710 | -13.29416 | -51.31701 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0bfc8aee-1876-3a4d-b3b8-5eaff0b5906b | -13.56001 | -49.90198 | 2026-09-14 03:57:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 35c31a8c-6019-33eb-88a7-0e55bd491a52 | -13.77926 | -48.80785 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a183cf29-262f-3b5d-9592-2f2443d75f48 | -14.84602 | -48.14787 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08923356-20af-3c95-af42-9863bd5ada31 | -11.51581 | -50.25743 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae8b124-e327-3af0-bc1e-9a13d069f7ad | -17.7014 | -44.30832 | 2026-09-14 03:57:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbcc3d12-0bb9-317c-b8eb-a70355062e33 | -13.55644 | -42.41452 | 2026-09-14 03:57:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d75df433-b190-3069-a022-214a4ea312b5 | -13.56071 | -49.89844 | 2026-09-14 03:57:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 556c31ac-18f5-3647-93f4-08c85bcdd846 | -13.565 | -51.45952 | 2026-09-14 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7233731f-76f1-3abd-837e-e34ce52dfad8 | -11.51662 | -50.25334 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfce5b42-0045-3a2b-9503-7853ac77e1bf | -13.30102 | -51.31372 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f0a1e36-2ceb-3804-8415-81f006c03767 | -15.20046 | -44.07241 | 2026-09-14 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 466fa3f5-7362-3604-b0d8-8d19b1af795c | -18.25411 | -46.24715 | 2026-09-14 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18625cd6-d480-323f-9b96-f7d2b311a93f | -13.62514 | -47.90583 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d19832-5d54-369a-b439-b03342f38f9d | -15.06352 | -48.5617 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 562ccc20-0b4a-3ea8-aacf-383478225ae3 | -10.98271 | -51.4375 | 2026-09-14 03:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 391a8eda-1df1-3f90-bbd1-5ead0ed2ccad | -13.64629 | -45.99674 | 2026-09-14 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50c21020-8725-35e9-bc62-2f00c48685d8 | -12.76371 | -48.81146 | 2026-09-14 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f6c1498-1a53-3b70-8e83-6773b82e2335 | -15.25025 | -42.77412 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29956a6a-954b-3eac-a5df-ad3c1d7b8364 | -12.17455 | -48.96522 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b20b564f-f570-3191-839e-9cde80a757f4 | -17.37283 | -42.61461 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c00d2e11-0c7b-3570-9378-af2b124a1ab5 | -14.84124 | -48.14725 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96818ccc-7a46-3af9-81f2-0f8bf7fcab4e | -15.25332 | -42.79814 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b73b5577-eed2-39e1-9356-3c7ee51c5add | -13.5827 | -47.89599 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 83337955-a24f-31a7-9821-4e614681e0f9 | -13.58151 | -47.8996 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8fead51a-81ad-34c4-905e-b03f80fddbb5 | -12.16475 | -48.95969 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bccc4148-38ec-3605-b3af-3df4fa2c0d1c | -13.62722 | -47.89484 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e66b5b2d-aaef-376a-a3c3-cd45590b4523 | -13.31378 | -51.31176 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dbbd3cc-7461-3480-9b0c-76d55b9a387a | -12.15952 | -48.95867 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f138bcd1-b0f7-3c99-9a75-7a0bb849a3f2 | -14.17666 | -47.43823 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c092f89f-2d18-3809-83ca-536a8c2e846f | -13.59718 | -47.87173 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96ade06a-8ea8-3f82-a290-367f41ccd82b | -17.36822 | -42.62155 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da99f6e6-9dfc-360c-a64f-5b3961d08cff | -14.17885 | -47.40093 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 820e903f-9b39-3b1e-b5cf-5c26c7dcc2f8 | -10.98171 | -51.4425 | 2026-09-14 03:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01f48d7e-a860-3dc5-9669-b527035b5c95 | -15.08831 | -48.32719 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58d22d38-dfc5-3796-bc48-373f8f4a755a | -15.05394 | -48.55937 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5e1c47e-b236-33c4-9028-adfd45e498eb | -13.58253 | -47.89404 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 28bb5088-620e-3de1-b553-00722aa92b88 | -15.23697 | -48.06662 | 2026-09-14 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f51d8ce8-0f05-37b8-9935-a31e8b44fda7 | -14.18121 | -47.43915 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 838be26e-2e46-3b12-9928-39cc2ef53ae4 | -15.45178 | -44.84558 | 2026-09-14 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6cc5fc-80b2-34f3-aac1-3dd3a5369c67 | -15.08257 | -48.33144 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bfe1065-3442-310c-bc54-b63d350d9125 | -13.4678 | -48.46487 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ffae828f-e8d6-3c9c-aec8-422a3833b8b7 | -17.98622 | -44.3407 | 2026-09-14 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9dbd9a3-0856-3376-af6b-5f2d8f983067 | -16.4809 | -43.42624 | 2026-09-14 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34ce5e7f-cd93-3d8b-8083-ac5587d128ca | -12.76311 | -48.81459 | 2026-09-14 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beb44ecd-2861-376d-b5b8-063527653fb6 | -14.81459 | -48.15227 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc2791ec-a194-3957-b60b-691198491463 | -13.32678 | -51.71941 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79200169-27da-3b7e-8149-f204c50d4993 | -13.63199 | -47.89559 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b5c9cc89-e7b9-394b-953d-5b324faedd60 | -11.7793 | -46.40979 | 2026-09-14 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e563a1c-3a62-3b88-a3c9-9eee7e0b65f0 | -14.82126 | -48.14282 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94ea124f-5a1f-36b5-8cd7-0930604e561f | -15.23186 | -42.78362 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eac0c067-2259-3e6b-be34-e8e1e38007cd | -14.17427 | -47.40025 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f4e362a-8c1b-399b-8c88-ba81c17b88a8 | -14.82789 | -48.14031 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df64d8c3-4fbf-3c4c-ac16-1a2bab2980a1 | -16.04992 | -40.47727 | 2026-09-14 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5820b66f-ca51-3e10-bae6-f9836073dd23 | -13.46595 | -48.46872 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b179b096-fce8-315e-b02f-8c36056ce1ca | -13.5923 | -47.89734 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4cdd3f9-b947-3ebb-9e4c-4a051b693104 | -13.30785 | -51.31052 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ed43a5e-e4b3-34dc-bf3c-ea540edc84ba | -17.93617 | -44.25339 | 2026-09-14 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e82027-a5da-32b3-ae8a-20ac62895f37 | -14.61645 | -42.52893 | 2026-09-14 03:57:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 501eb789-4be5-3a38-837e-ca6c7ca8f9a5 | -13.63093 | -47.90126 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1557f051-0623-3452-b867-c44a92bc4387 | -14.19744 | -47.42784 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cfd5fa1-86dc-3e38-8e15-39f6771e390a | -17.35556 | -44.39666 | 2026-09-14 03:57:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cd9af18-88df-328d-8706-3f4dafdeb6fb | -16.48162 | -43.42199 | 2026-09-14 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47ad33b8-ade9-37fb-ab6c-14c268c7ba41 | -14.18441 | -47.39636 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9382df70-98d8-3a8b-af5b-99abe09d737f | -17.3676 | -42.62531 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1ceb792-7bdb-320b-bc95-7876f87bbff2 | -13.45688 | -48.46826 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2065ab6e-ec10-3b54-be76-3d61645a1368 | -13.0686 | -48.60202 | 2026-09-14 03:57:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b209f113-7055-32da-86d5-99ab47bfa678 | -13.62141 | -47.89954 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4eed148-2e4f-3248-b8c8-7f91953be700 | -14.91428 | -44.66996 | 2026-09-14 03:57:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e49cb91b-7554-3f34-95bd-4fe95ab6c1e6 | -15.27181 | -42.79352 | 2026-09-14 03:57:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c73c50f8-05ff-35d9-beb2-568c5406a722 | -13.58938 | -47.88684 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f9b40b7d-d12c-3fe6-a98f-1b471ba3cd76 | -15.2537 | -42.77471 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 70a217a5-0343-3d88-b186-a318fbd813e6 | -12.17044 | -48.95847 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c611f05b-c295-346a-8512-b6a10bf001e5 | -17.26948 | -41.50645 | 2026-09-14 03:57:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 82a25cf4-982c-359c-bf8e-5e3bc5443df3 | -17.37159 | -42.62214 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 165b20ed-1fda-3c84-8427-a639f4731188 | -13.56543 | -49.90303 | 2026-09-14 03:57:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c161c452-ddff-37c3-8c44-beb0697d3875 | -19.3638 | -44.30352 | 2026-09-14 03:57:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36b7e5f6-5355-3af8-8da6-1616361dd8de | -13.6204 | -47.90488 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2a34e0c-ba72-3351-965b-d4c872172ae3 | -15.81931 | -42.37398 | 2026-09-14 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07b95ca1-fc88-34a9-a995-f104ce1d02fc | -14.81933 | -48.15306 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74ff8e7d-6946-324d-a249-0db735ec190f | -15.26838 | -42.79287 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20f695ee-1da5-3081-bee6-cc13eb40e468 | -14.83645 | -48.14669 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62c8b54c-cf0c-3ee3-803a-9c9c9d2be687 | -13.58846 | -47.89167 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3d8359f7-36a1-3386-991b-010f8bc84a6f | -13.56614 | -49.89948 | 2026-09-14 03:57:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 989b1a23-e3b4-3898-9da7-3ed40f5686d3 | -14.17542 | -47.41945 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d4afedf-b9b6-3bc7-90e1-d166dc59fed6 | -13.77434 | -48.80629 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82affdb8-3032-385b-9dfc-f5f83c9ed81c | -16.99983 | -46.00872 | 2026-09-14 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dff5cec-1a31-3f1b-9c45-22918df35ead | -14.10411 | -46.35488 | 2026-09-14 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdcbb40d-8fe3-39a6-8689-7ed3c069a104 | -13.46285 | -48.46396 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c354e834-8956-3be1-9c22-a3d01dcef906 | -15.23533 | -42.78409 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 93411f40-93aa-33eb-8f74-da1780c36415 | -13.5599 | -42.41503 | 2026-09-14 03:57:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90650488-99b1-3212-bddd-d02b726d98fa | -14.18574 | -47.44017 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9bad3cd-01c5-39d3-bd53-f7f637529b86 | -11.80594 | -46.59272 | 2026-09-14 03:57:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db49cd0e-deff-3ed7-b1a4-cf91bd1062f8 | -12.17564 | -48.95962 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55ef6823-1cb3-311b-b807-75660f44c1ea | -13.59142 | -47.87619 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9db99a10-25ba-3d95-a4e3-04958b26dba8 | -15.4635 | -39.10793 | 2026-09-14 03:57:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5c4a063b-683c-37e7-b829-204a0258b847 | -12.85756 | -44.3864 | 2026-09-14 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63c9f45f-2aff-31ee-9955-938720d8372d | -13.46181 | -48.46926 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3b046714-b030-3d69-b68d-3688db4cd07a | -14.18799 | -47.40244 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1246aafb-1c0a-341b-baef-0d0922da5bbd | -12.16999 | -48.96064 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README16.md)
