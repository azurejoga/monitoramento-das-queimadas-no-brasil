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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02fbfe24-eee5-3d0f-b47c-df297dccf328 | -15.81095 | -56.41747 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0cb1c7b-0e96-3e73-be13-337f16a98d4d | -12.9959 | -49.43135 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20dd13c1-9f21-3157-a6e1-34d915871e3b | -13.25573 | -48.45834 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68c64960-758c-3919-a7b1-7600a2debf47 | -14.33101 | -44.50051 | 2025-09-28 04:27:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2729df9f-7d8c-3177-a30a-6a726f01bc81 | -13.62866 | -48.10178 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd92dcd8-17d9-320a-807b-e0bc8405e710 | -13.61187 | -47.32164 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71087b19-6ccf-3fae-b687-691563358fc2 | -17.72551 | -46.6974 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 830eaa5d-ce13-3152-ba53-b48a58f0c76c | -19.60747 | -45.98956 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73d87622-8016-30bd-9d73-22698a815f41 | -19.86026 | -42.5938 | 2025-09-28 04:27:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c9d9477e-a4fe-3646-af97-d3c411502e06 | -15.53059 | -47.90421 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df1fcdbd-0c06-3434-9d92-2fccbef039fe | -17.4344 | -45.80766 | 2025-09-28 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac45e093-0325-3c21-af4d-a8e646877bb4 | -19.32574 | -44.16933 | 2025-09-28 04:27:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e69e6ef-34eb-314b-8c04-7dd6af72e2e0 | -15.60826 | -53.16528 | 2025-09-28 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac358d18-b3fa-39e4-8a8a-c4a8064066c4 | -19.48106 | -43.80266 | 2025-09-28 04:27:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77bfb8c0-8dd0-314b-b717-97fcb9bfbe05 | -15.18859 | -50.09515 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f350721c-73fb-3480-b798-2e0f3637f4ba | -15.44328 | -48.22292 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aff6dbf6-42ca-3a88-b6fe-ad67f85964be | -20.22688 | -47.51399 | 2025-09-28 04:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 463f17eb-4919-3a1c-8986-89bfcbd5adb4 | -19.31326 | -43.81929 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecc26413-4cd5-31bf-a440-b7e1659eca78 | -14.80848 | -48.75453 | 2025-09-28 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc27ba7b-ad46-38ee-a98f-bee203218102 | -15.29186 | -49.48694 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cf35981-6177-3f17-819c-64989822ab0e | -13.62182 | -47.3233 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 135ad464-2115-3d69-a04e-a8c7d8c3d778 | -19.95576 | -43.66602 | 2025-09-28 04:27:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b943fe3-611e-38fa-9766-56236d77768a | -13.71172 | -48.34771 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2af40941-40a9-3870-9c1f-8eeac21a12a1 | -12.65891 | -51.66133 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ba77f13-a35d-3000-9017-ca4d56fc9943 | -13.62767 | -48.06525 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 772cc7f9-6ce7-3837-8434-54c424da18b0 | -15.89607 | -50.29544 | 2025-09-28 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a94382dc-9821-375f-9251-5d5286a12d69 | -15.0203 | -46.96688 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67380453-a408-38d3-ad05-6825b04e037b | -15.81813 | -41.89033 | 2025-09-28 04:27:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c17d843d-10f5-31f2-9069-0a5f7043b26b | -12.65435 | -51.66531 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90732ebb-1184-3b72-8232-adf86324f5a3 | -15.25324 | -43.08624 | 2025-09-28 04:27:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 21.7 |
| ace882df-ecc5-3efc-a42d-3a822c74e5a7 | -12.98107 | -49.43657 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8af5bc1f-2e87-3499-82c8-43d014a9e598 | -13.25298 | -48.45419 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c9fc575-84da-3c78-b3c7-c0e998b9ce97 | -13.78368 | -47.89432 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eade7101-509a-3817-bbc5-416023ed8a51 | -13.5818 | -47.32031 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aa2a0b0-3fac-30cd-80b6-578d72607da1 | -15.80487 | -56.43098 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 397bd62a-4e33-3cb4-ad03-08fa80157a2b | -16.40475 | -43.72316 | 2025-09-28 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24d14540-7b86-3671-a453-1dc9a696d84d | -17.24637 | -43.87205 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc372e5d-5849-3211-a61e-2b44c64da153 | -12.98045 | -49.44033 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fde1aada-5c11-307a-b2e6-401bd819c85b | -15.57992 | -42.40973 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ae0c25e-5bfb-308c-948c-df39c8e9874b | -17.18678 | -43.37061 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4441dba-6132-3537-915a-622343cf68d9 | -13.78312 | -47.89786 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 606e2374-5740-3c1a-bd9f-236d612cddc3 | -17.73182 | -46.70244 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3b58a7a-b6a5-3cb6-936d-e017b1e71133 | -13.77985 | -47.87553 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd70ba5a-a1c8-30fd-ac8c-a512d6080e21 | -17.72207 | -46.69683 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c77b8e8-5916-3531-9f31-d3ad95cfe2ad | -15.31812 | -47.89533 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fcb295f6-8196-315e-838f-88cdb28ff3d7 | -14.81552 | -45.45808 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b72fa2a-90c7-39ac-bb51-4d12e959e141 | -15.44384 | -48.21936 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5611a9d-3d21-3551-9c84-7fa10a76fb8d | -14.771 | -45.68852 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa8efe25-fb58-326a-81d1-edc86b163fc3 | -13.65084 | -48.06905 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be196d1-e9b2-38d1-ad34-b7bcfe2ac440 | -13.39779 | -48.16514 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfcd7559-b910-3b24-9337-77d012ec7360 | -18.20062 | -53.31332 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5339c0e8-9f34-375b-b2d4-80fc8210f4a1 | -15.87607 | -46.22923 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cd2cba4-ce20-3195-811e-6dafeac47ba7 | -17.19698 | -43.38716 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17a2450a-8a7e-3586-b84d-4631f4d5f116 | -15.46768 | -50.23282 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b997c88b-29bc-3248-9d9e-e6441bcfc16d | -13.00305 | -49.45163 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd290c9c-29de-37b3-868c-031c7bb8a8e2 | -13.60218 | -48.09734 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b946111c-b90a-374d-aed1-49999dcab6b3 | -14.54209 | -48.40217 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69dc4a2d-8d11-3fdb-8830-5558574ced85 | -21.61701 | -46.92186 | 2025-09-28 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7981c50a-0d2a-350e-bd8c-e54bcec23a21 | -20.86728 | -49.35672 | 2025-09-28 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c256803d-f74d-3b63-8878-596114650b87 | -22.14261 | -51.37057 | 2025-09-28 04:29:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89833cf4-2914-3402-b009-b86d8431bedc | -23.52097 | -46.97599 | 2025-09-28 04:29:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7208b7f7-8638-36ec-ae2c-199e07475256 | -21.00122 | -50.03128 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ffda23cd-050d-33eb-a554-152ac37bcc11 | -20.992 | -50.00724 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f82dcb12-24f5-36d5-9ee0-962e06a005a5 | -23.18774 | -47.54071 | 2025-09-28 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 80178899-c2da-3a01-8ba6-54e77f5fde38 | -22.3559 | -49.47348 | 2025-09-28 04:29:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9202a840-598c-34aa-9625-867cf9d9a6c2 | -22.94486 | -49.87631 | 2025-09-28 04:29:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 5f6ea5cd-1b68-3788-8dcc-bfa70b9f67ad | -23.53581 | -51.48297 | 2025-09-28 04:29:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eb6b083a-4d1e-3ad1-9b34-ff85f217a5d0 | -21.51721 | -49.86429 | 2025-09-28 04:29:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a16f30f-2776-341d-9dd5-21dfe3740c9d | -22.61609 | -49.03548 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 751c3fcc-476a-31f7-abb2-14f482d0c040 | -22.73747 | -46.13259 | 2025-09-28 04:29:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c44708cd-b4c2-329f-9416-0f49209b0e26 | -22.53043 | -49.11019 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4437bd7-a9ed-37f3-a198-f61632a78042 | -20.99863 | -50.00844 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2dead77-40d1-3ff2-a51e-abe8dac0bce5 | -22.52986 | -49.11397 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b992d7b1-9ee4-3425-bace-3e57b0cca7a4 | -21.84768 | -50.5586 | 2025-09-28 04:29:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1cdb5956-d27f-348c-9b1d-70b5672b070b | -20.70052 | -50.71034 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46643748-e141-3c17-bd6c-cb9a152f5303 | -22.66767 | -46.9801 | 2025-09-28 04:29:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ad4bbae-ff3d-3153-ab84-088f6de12ec1 | -21.00194 | -50.00904 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11b59979-dfbe-3b82-8f97-13efee81605b | -22.05933 | -43.01421 | 2025-09-28 04:29:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1a6bd76e-8697-37e7-a52f-ebf4bfd3e075 | -21.44709 | -44.90369 | 2025-09-28 04:29:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b9af2bd-af93-30de-859e-cb8cb41cdba5 | -21.81923 | -47.20039 | 2025-09-28 04:29:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 75552262-fbbc-3924-8f20-d71ff1bc85ef | -22.62 | -49.0323 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a0c17f-df3d-37ad-b41f-223330b872f6 | -21.06914 | -48.66314 | 2025-09-28 04:29:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4f109d27-3c4a-34fe-9374-341d44f4f554 | -22.90742 | -45.39132 | 2025-09-28 04:29:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 53f6ddbb-39a8-331d-863a-ee97355d33a1 | -20.30662 | -54.64745 | 2025-09-28 04:29:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36f74e46-c367-3217-b8bb-e2b46594a03f | -22.34812 | -47.33434 | 2025-09-28 04:29:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f29a032e-d1d9-3e77-aca6-2dcf9e9c103e | -21.16441 | -45.74216 | 2025-09-28 04:29:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40105672-8938-3697-ae12-522c881c8008 | -22.9787 | -48.36008 | 2025-09-28 04:29:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69469578-c599-31a4-98aa-17bfc533e5ce | -20.69718 | -50.70971 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 93ca3484-b5d4-304f-a8eb-e9ca8e071de9 | -20.6999 | -50.71411 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2292b9b-cb39-3962-9e50-e538dab543f7 | -22.60778 | -49.02242 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c6fc1f9-a1c4-34d1-a825-5030c45f4779 | -22.61552 | -49.03926 | 2025-09-28 04:29:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c717102-2a26-3616-9c51-2dcfefd1cb1d | -23.53219 | -47.1632 | 2025-09-28 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9b6733b3-0f77-3ffa-9ca7-3c5448ecc3d7 | -22.87196 | -46.40216 | 2025-09-28 04:29:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7199b345-2ee7-30c1-b1f9-7fc651bd495e | -22.26319 | -49.56833 | 2025-09-28 04:29:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72522c4c-f36b-3c86-90f3-00369d8501a4 | -20.99141 | -50.01094 | 2025-09-28 04:29:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b2d4477-7cfb-3ebe-a645-79baf7ec8178 | -21.35541 | -45.78498 | 2025-09-28 04:29:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 38461eb6-3555-3503-91b3-584523bb95a0 | -20.69383 | -50.70908 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 8eff7994-a2e9-3008-9ee4-b7f39096b257 | -22.38189 | -49.48193 | 2025-09-28 04:29:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e348de7f-8671-32b0-8e48-a1a346892cbe | -21.85418 | -53.95499 | 2025-09-28 04:29:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a2c92b5b-6af4-3dae-a4ef-5fc16e075791 | -20.69655 | -50.71348 | 2025-09-28 04:29:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |


[Clique aqui para ver as próximas entradas](README82.md)
