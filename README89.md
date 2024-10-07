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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec9c09d8-2ef8-3844-bffb-2a7c037756de | -19.81115 | -48.02934 | 2024-10-07 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc8b7501-a31c-3b7f-b580-a7af50db053b | -20.51608 | -48.1219 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a51c5e24-13f4-3aee-bfcb-bf2f4440cf7d | -20.51548 | -48.1274 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 445727f2-4119-3d45-bb96-4e7f8091f199 | -20.51135 | -48.12125 | 2024-10-07 04:55:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0b987c67-d9d3-3c85-8761-fdbaa5f79aaa | -20.51077 | -48.12663 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| b7e0ce6a-9376-378c-87ab-998a03e7b8fc | -20.51017 | -48.13209 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 67f672a9-66d8-3d62-80a4-75c91a877cde | -20.50603 | -48.12598 | 2024-10-07 04:55:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 5a602dd0-5b12-3ed3-97ee-4cafab9122f7 | -20.50546 | -48.1313 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 480a4d6b-b2b0-3a37-901b-edb37dc61d00 | -20.50486 | -48.13679 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4bbc84f4-9c64-35c6-bfc4-e241fa982b4f | -20.50465 | -48.12532 | 2024-10-07 04:55:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4d508771-587a-398f-a3bc-e97ee8d32a5e | -20.50405 | -48.13058 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ba591859-dde1-3412-98d2-12de95528886 | -20.50341 | -48.13604 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 47df14a6-b3c0-3a3c-a7ce-9590050c1da6 | -20.50014 | -48.13603 | 2024-10-07 04:55:00 | NOAA-21 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d83042b5-5429-3f33-a77f-3480c2f36180 | -20.47208 | -47.67444 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d78acbbb-43b6-3078-8db2-dd501da936c1 | -20.46719 | -47.67395 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 523054dd-3832-340d-97de-f86fb005b8ac | -20.46599 | -47.68516 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4131f5b9-9c64-3886-b5f8-c72e3d024ab8 | -20.4623 | -47.67352 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| edaf6463-2c17-3d58-96e6-f68574d3d29b | -20.45683 | -47.67844 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d29dab59-aee2-3c35-a7f8-81c1299b768d | -20.45076 | -47.68912 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 121116c1-9558-3f6e-95d0-c1d78861efc5 | -20.44841 | -47.68265 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 220f8989-12d2-3bd0-bd20-d62ce1013111 | -20.44835 | -47.71188 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b1031233-8cac-3c2c-a2f7-373f51f12c2d | -20.44591 | -47.68831 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d03c5777-75ba-3313-8b83-406758f0f9ae | -20.44583 | -47.70546 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 720717fd-98c7-37a4-a19c-d222acc7c8a5 | -20.44532 | -47.6939 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1b55f5c2-85c5-393b-87bc-8fe1a184ef3c | -20.44292 | -47.68755 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 696bbb15-cce0-3661-ace2-749051fffd8f | -20.43745 | -47.69233 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9c6490d4-eac7-3c54-a3c4-67b303039642 | -20.43681 | -47.698 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7be8a877-142b-3474-912b-195ad205277a | -20.47148 | -47.68001 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a24ff6e2-3206-3751-a90c-b04623e4c0bc | -20.46959 | -47.65152 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1b74a9f-2ed4-3f5a-b325-7ed94f32744e | -20.46779 | -47.66837 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 311d826d-40b7-3168-ae80-4bf6ebac559f | -20.44905 | -47.67698 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4edd9bb-8e15-38a0-bdae-13ea2b40ebbd | -20.44713 | -47.69394 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4d3b1eb1-76de-3dde-a907-cb1b6a8187d9 | -20.4441 | -47.70549 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f83a4f9c-d551-3d55-b116-3a4cf47c0e83 | -20.44106 | -47.68752 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 071eda39-d16c-3a3f-bb79-7f35041cbff2 | -20.44047 | -47.69308 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f03a025c-a696-3dcc-b0e1-c616b1181960 | -19.80643 | -48.02875 | 2024-10-07 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df839f1d-f97d-3f75-a2e3-15454e25d3ff | -20.46839 | -47.66275 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a728672-8752-35ca-b561-94867eb617dd | -20.46537 | -47.69091 | 2024-10-07 04:55:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e8618628-f649-3c62-b0ce-32039c4f1523 | -20.45137 | -47.68341 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39806713-d4b6-3b7f-acc1-6b132c5d6dd2 | -20.44349 | -47.71115 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 35.6 |
| bcbc6167-8834-330e-916b-0cba7f4a9144 | -20.44229 | -47.69312 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 412c8c4f-ee6a-39ea-9285-6a019df24f9b | -20.44164 | -47.69883 | 2024-10-07 04:55:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 191c72ab-4bb7-3e19-9b3b-d6e97fe6dfcb | -21.65526 | -47.72968 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30e8de22-d87e-3804-8e89-d21ba988d11d | -21.65092 | -47.72348 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77aec8fd-f60b-392f-8f63-abed3b53d066 | -21.65031 | -47.72929 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef6f2af6-b43c-354f-a261-0d90d1bd24a6 | -21.64104 | -47.72229 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 290a16b1-4e3e-3aa5-a791-6ea9c80d2369 | -21.60597 | -47.72321 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf627f5d-6003-3920-8def-35b6dd2d6a96 | -21.6016 | -47.71703 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be6b4a60-fada-37b7-ab1f-08e819fc3773 | -21.59925 | -47.72186 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ca1df5a8-8daf-3596-8e3c-14aba79aeb06 | -21.59557 | -47.7097 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e1ca4b4-3601-3cb8-9b3d-f7646cc2e1a2 | -21.59547 | -47.93755 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ede7387d-68b4-3aa0-ab36-ec6292a72ba0 | -21.59246 | -47.73851 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 245d1280-ac61-3478-aa02-f6bbfa9f412a | -21.59224 | -47.71082 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44fbcd87-9fe2-3372-ab5f-b50aac91278c | -21.58928 | -47.7217 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c42b833e-c2b8-300e-baa8-ad76c27ea9c6 | -21.58376 | -47.72657 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4953829-9b53-3f6c-998b-8c0f0fa43c9d | -21.57766 | -47.73691 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4b4dd3c-934a-33e5-87ea-9fa9d5935c80 | -21.57603 | -47.93505 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b3addd3-e602-33dc-bdd4-f6fa7ae3d6f7 | -21.57094 | -47.75304 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f39ad814-924d-3e8c-9836-2bc58cda73e9 | -21.56602 | -47.75243 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e08717bf-4ba2-33ee-bc15-6735d984ffc2 | -21.56467 | -47.71828 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f15be8d-a9b5-3bad-9cad-2605e71ac4e6 | -21.56407 | -47.72395 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f1ede3f-727b-3700-bcfd-0cfa836f82bc | -21.56348 | -47.72948 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e0030d5-6404-3dd8-bceb-8e7b5d115d43 | -21.56289 | -47.73501 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 176b1415-2c6f-3688-9c2c-9508ab2cdd31 | -22.20104 | -48.17067 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b7d992c0-1777-327e-ab69-687e514ae8b4 | -22.20044 | -48.17611 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f837f39f-7ec1-3eb4-a932-e1e4454e02c2 | -22.20022 | -48.17198 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ac627a0-e654-3213-b4e9-48f6fd6ce37c | -22.19966 | -48.1774 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a80e8c6-7ce1-328d-bd6b-d88bd3f6473d | -22.19561 | -48.17564 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c12acb8-064d-3515-b912-4ecf1cfd5798 | -22.19538 | -48.1715 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e779395-1ad4-399e-8373-abb5f2781edd | -22.19483 | -48.17688 | 2024-10-07 04:55:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8b9613d-76fb-391d-9a75-89ab986b5dfe | -21.85664 | -48.44148 | 2024-10-07 04:55:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7e229c8-fc50-3d23-96c0-921d63d06b6b | -21.8548 | -48.44449 | 2024-10-07 04:55:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e92dc0a9-f4fe-38fc-9d25-cde4052c8099 | -21.85138 | -48.44609 | 2024-10-07 04:55:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93d103bd-0c6d-30ed-8666-32625284b8cd | -21.66082 | -47.72434 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f365102a-961f-3e74-871d-3d693ccbf5c3 | -21.66022 | -47.73008 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b68f397-9aec-3f88-b7d7-856cf903fc2a | -21.60425 | -47.72183 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1cdf57f8-1ff1-33b2-96f5-547843c148a2 | -21.601 | -47.72305 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a361b232-e38e-3eae-a681-7aa8a53358ff | -21.5966 | -47.71711 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a04ddd2f-6aa0-3d54-8ebf-d376f9c49f8c | -21.59629 | -47.96227 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 27fd45fb-571b-3bcf-8c54-f6e24e9eaafd | -21.59487 | -47.73423 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ab057890-1e5d-3ff7-b0eb-82a5bccd6b48 | -21.5942 | -47.94894 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 099068df-cd2e-34e4-9b8e-c447ce7d023d | -21.59381 | -47.93879 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4311e7dd-3c01-3f58-ad1e-2e14c33172d9 | -21.59294 | -47.96033 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 487c8725-53e6-3413-9866-931f228d89b5 | -21.59162 | -47.71702 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2c94170a-353f-3261-9345-6eca9fadff94 | -21.59061 | -47.93691 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d1c9f00-3f80-3711-8ea4-2f1f60725b45 | -21.58992 | -47.71575 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b685da6c-e8e7-3d6c-a3de-b593d4361ac8 | -21.58895 | -47.93815 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 895a2a76-eee7-37e8-a3c3-4096f4919dff | -21.58813 | -47.7324 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 488982e8-3a14-343b-8c16-48415f11b900 | -21.58718 | -47.95533 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ce6b655-d281-37da-ad50-0dacd8ef4fd9 | -21.58432 | -47.72136 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1893f7f-398e-3a76-baa2-4b1336253686 | -21.58385 | -47.95351 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff5ce2a4-0250-3743-ba6b-52c95765969a | -21.58198 | -47.74313 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| efcafdb7-e817-3add-ae0a-88054c1a1f21 | -21.57938 | -47.72088 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16ebd839-7668-3f2b-82ef-e481bafab96c | -21.57881 | -47.72619 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5a1689-48ce-3fbe-b36b-6f6f4c7a5016 | -21.57445 | -47.7203 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a52c4c61-1890-3a3b-86f1-e5e5c1fe4275 | -21.57215 | -47.74176 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa11a08e-51bd-3e7b-83b1-e4c076da2511 | -21.57155 | -47.7474 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08066ac9-2e05-3785-bbf6-569195c464c3 | -21.55917 | -47.72302 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3f76062-e789-3d7c-929b-b5fd482f8e5d | -21.55857 | -47.72876 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0a84fb5a-f948-3c8a-b65b-929b3d178690 | -21.31838 | -47.60268 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README90.md)
