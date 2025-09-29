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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b74a81c-8bc2-3744-9006-de7df5397776 | -15.34031 | -47.91535 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2ec26d3-eaae-3b0f-a17e-905abee797fe | -13.62662 | -47.33429 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c86f2eb-e712-363f-ae97-7609d924fd88 | -15.16891 | -50.08887 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49bd73f6-f3b1-33a8-90e0-2d1c5758e20d | -12.94044 | -46.77551 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41f0713f-e6f3-3ca3-8871-c22db2d6d681 | -17.08359 | -48.56532 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6a8d4c9-6cfe-3769-b31c-5689d44d4c6b | -11.99903 | -47.09682 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db64b857-b001-3da1-8b7e-7769189b5287 | -13.60221 | -48.05803 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a4f79134-8ea5-3262-ac07-4b10b44cf089 | -14.51994 | -48.39713 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 26992d64-873b-3e18-9758-946d1ccce895 | -13.39023 | -48.15168 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 0b18c6ac-56e9-342f-b4ce-bcc1b50be354 | -13.80163 | -47.90319 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3dc1ca9f-4523-34b1-bf9d-b6ea754a714e | -13.83179 | -47.49297 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e0f86a2-2337-355e-90f5-a226380d1383 | -12.85142 | -46.97339 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f390fced-fccb-336c-8a82-d170ca026b72 | -15.08319 | -48.32883 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9295137a-7721-36b4-b2b1-8ebbdf640478 | -12.9311 | -46.76479 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2c08520-1312-39ba-8610-6c362f93263a | -13.01686 | -49.44948 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0f6da00-9942-3d87-81b0-68140da51bb7 | -15.17565 | -50.08771 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55062b28-3e62-3052-baef-f3cb7f0b336d | -15.53796 | -47.87908 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c50f598-ff7a-33bd-9422-d693dbb87137 | -13.00056 | -49.43797 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5ff0f25-d540-3fdc-949d-6cb3a7ba8d3d | -15.04233 | -46.96528 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 497ddfe4-c393-3316-a6a5-01a5a7c429e2 | -11.93242 | -48.06663 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 66a8decd-34f7-326a-ab2b-12b239d9faf0 | -14.5241 | -48.4032 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b6c0146-f963-366f-8a3b-54b8ac22a13e | -13.83495 | -47.97847 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c83dc33-9336-3b3d-be2f-085381adbeed | -11.4345 | -46.63441 | 2025-09-29 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29188e3a-6264-3342-a959-0157d5bf108a | -14.56564 | -48.26 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 858198e2-411c-3228-9c9c-0956af6f4aa2 | -11.80767 | -51.80444 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d4d6c0-9f94-3f1b-8bb2-fa2020c15970 | -10.71988 | -53.79165 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e2db20f-f7c6-3cc4-a524-b91af846e78b | -12.21156 | -43.74969 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de8bb4dd-d322-3f18-a34b-7cb1e02933c6 | -13.57899 | -47.29997 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f248afc2-ff69-34ff-978e-4566bd1d527f | -13.60956 | -48.03918 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d54de91f-e404-3485-b928-528fd66b099f | -15.60953 | -46.25218 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cbb8c70-39cc-3a20-9d2b-b10d456c3bea | -11.65431 | -45.33348 | 2025-09-29 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e199030-b5d6-39b7-bdde-253b35b1e501 | -11.94124 | -48.07276 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8d69019-75a6-353a-94df-378903b04279 | -13.38545 | -48.15094 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4ea65c94-c041-3f3c-a597-c885ee4d5541 | -15.33564 | -47.91183 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 351fa158-ff66-3c54-8341-646057347a8a | -15.04768 | -46.96563 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74a15be2-73cc-3c8b-bc52-92d797745c09 | -12.85583 | -46.9801 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a05d366-5d36-3214-85b3-e6105e6e29b9 | -12.20536 | -43.74811 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78dc7144-d7ad-3e5f-bcce-911e2d9cf294 | -16.48937 | -46.03458 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd5cdb83-9cc8-3784-9f7c-072e497948da | -11.81445 | -51.80996 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d1033ba-14b2-31b6-8a93-4bbd10e8566f | -14.75252 | -48.37119 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea260342-9579-3036-a989-7f71d71c0742 | -15.28718 | -49.49729 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6c84f1c-2cca-38ab-8bb2-3cfbd4a8a64f | -12.90038 | -47.10664 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f45f5ff-0cd2-3d3b-bb69-f90f36caa976 | -11.83078 | -55.2116 | 2025-09-29 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 147329e8-9d2c-3826-aeac-e04c87beef72 | -13.3559 | -47.30424 | 2025-09-29 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6cd103d-1d47-3f28-88e5-611da25a74b1 | -12.90112 | -47.10054 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d239b61a-503a-3523-beb6-49d2eecc62ab | -12.87052 | -46.96373 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0df750e4-833e-3b1f-88aa-f32641e54a7c | -15.28998 | -49.51148 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 27d321ee-073e-3fc8-97ed-7123f1ecb9b3 | -15.47011 | -47.93583 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 445414a5-7cf0-3707-949c-70923aad926a | -11.74569 | -46.8399 | 2025-09-29 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f633f2a-ba21-3dce-b29e-7943818b13dc | -17.40068 | -47.1264 | 2025-09-29 04:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c107d6b6-20a6-32c9-b30a-5e1d636dac10 | -12.97993 | -45.22421 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af7e293d-c2e4-3cd2-812b-efcb236d4ca3 | -13.59754 | -48.04861 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92ec99bb-083b-3ccf-8e36-9f61b9531430 | -13.63706 | -48.04749 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65b8c134-e159-3da7-9ed2-4a17f037a48d | -13.59285 | -47.28658 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c37720f6-717e-3a8e-95e5-94f696717149 | -13.82981 | -47.93828 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3f9ed09-cf17-3266-8a4d-cbb247b595b4 | -12.76998 | -46.85326 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9151e60b-3db4-355b-bd83-a5ef5daaf1ab | -13.72105 | -48.65544 | 2025-09-29 04:59:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41fdf86d-0d80-3b8d-a33f-04ceeb0d00d4 | -11.99981 | -47.09717 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1549773-6b91-3f28-abc2-506e78fa590d | -15.54845 | -47.87421 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d45d5754-c7d8-3828-95e8-a06d04fbdbbe | -13.79037 | -47.87317 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f62afff-91d2-323a-9e93-ee43f06dda6f | -17.39536 | -47.12484 | 2025-09-29 04:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e805d3c0-9b06-309d-9fef-18bc01d0c199 | -13.16474 | -47.44476 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d21e90-3849-308c-9767-162a175bf20a | -15.32545 | -47.90901 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99f71831-706f-373e-8dd8-3a985162a411 | -15.29112 | -49.50237 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c2e1230f-7086-3d9e-9b26-152f9e31dc49 | -12.93556 | -46.77193 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77fc49b5-f2c0-343d-99fc-67b3c8c6ab39 | -15.78501 | -43.85854 | 2025-09-29 04:59:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ac73804-e030-3b1a-a2ad-b3fcaca75059 | -10.7238 | -53.78851 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed460f29-8106-3c08-bb67-013ff6ad8f3c | -12.65348 | -46.9282 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9015c5b6-8b6e-3037-9e9b-defc11fc087d | -13.74345 | -47.88976 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a69b59e9-c4c8-3e4d-8920-b9fcb5ae03e2 | -13.38479 | -48.15636 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| f5ab2add-be68-3ba3-a165-0d39af73ee44 | -12.65485 | -51.65773 | 2025-09-29 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b42c27a-3a2a-388e-ae62-2c408aa9d857 | -15.26982 | -48.76456 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c22a8b9-8750-36b4-9ffe-656684ee66ee | -11.92635 | -48.03887 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eaae5401-7e19-3cd4-90bc-3a57843950b1 | -12.89635 | -47.09707 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f6bccd9-80ab-39ad-a095-94a6e34c1afc | -15.28946 | -49.51569 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 979898aa-ca07-370c-afac-5b2987d0e55f | -12.86852 | -46.96245 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f2faead5-770b-3faa-9c5d-005cf0b4fac7 | -12.96015 | -47.20937 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e500026-a633-3eeb-aacf-d5ee983a4f30 | -14.59336 | -44.99564 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 693875ec-426b-3582-ad40-eb597a389bd3 | -12.94794 | -47.18324 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9822602d-8230-3863-a117-7e3e5f2f56e7 | -11.98124 | -47.12185 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13876a1e-0406-32be-a9e0-05b6072f392a | -11.92163 | -48.03812 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e5090aa8-578f-3f38-8e87-a577096cc525 | -14.53522 | -48.43222 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b55894b2-9e74-35be-b264-f9cfd7c2f7a0 | -13.78413 | -47.92376 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c20c97c-db5f-3b44-bfb9-48f7234e6a70 | -13.57633 | -47.29441 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4ad61bac-55ec-3d53-ad57-10e960b0216a | -14.42399 | -52.24686 | 2025-09-29 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd242f33-506b-3779-ae5e-970dcfdac7f5 | -15.87366 | -46.83751 | 2025-09-29 04:59:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09748636-4ade-3edc-a51f-258ee53aa996 | -11.98052 | -46.58302 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb8faa65-d234-3e3f-9cfa-84eef3b3b641 | -16.49089 | -46.03178 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad5276c9-26d6-3dac-a896-5a05870df334 | -11.62217 | -52.84838 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5edab958-1531-3064-8263-8da95bcde598 | -13.59789 | -48.05334 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 10f465c1-84c4-3160-89ed-9b5c9a8739c9 | -14.84197 | -45.56535 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8a7010f-954d-3860-91f6-e02803d2cf01 | -14.57872 | -48.23302 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b038e862-9d30-3b44-8a5e-7fe7213126e7 | -14.59236 | -45.00455 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c2e5fd9-c157-32ca-bcc9-4d691aa8d089 | -14.59184 | -45.00924 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8aed02ec-5bfa-328b-9409-a62854b2515f | -15.27989 | -49.25584 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a4cd52a-cd19-39b6-9765-fb3d5aced8d1 | -11.46811 | -54.87657 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 905fa088-081e-3235-af1d-c6f26b9736e0 | -12.70143 | -46.89693 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 588afbd8-db58-30b8-8bb4-37c5d432d633 | -10.73905 | -51.98732 | 2025-09-29 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2ce140b-2dfa-3e92-9774-0c2fdc88ef4b | -13.75199 | -47.90147 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5d0e876b-44cd-3eb9-9a97-128f3c069fe9 | -12.84905 | -46.90776 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README67.md)
