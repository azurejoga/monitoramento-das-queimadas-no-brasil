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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c088a5c-803f-33b3-aa0f-381ae97c3440 | -11.64633 | -46.20925 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b270d310-62f5-3618-8772-eeef7e376eb5 | -11.14875 | -44.79442 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ca1c181-3f1b-3739-bacc-e1eef4dcda72 | -15.05467 | -48.51494 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7228c12-edb0-3016-903c-832cb0092555 | -20.39134 | -46.73156 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8291768d-3480-3d85-9400-144d3f8baf47 | -14.27534 | -58.61587 | 2025-08-25 04:17:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97bb18d2-629b-3ee8-8bcd-390bcde5393a | -12.75282 | -48.13113 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75657269-c13d-3c3c-9380-a5baf2f77b72 | -11.16885 | -55.02841 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ce14e9f-d9db-36fd-b402-9f03a06015ef | -13.51017 | -46.90929 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36d36293-a306-304b-9f3e-755dfc0b76f4 | -15.17989 | -48.19977 | 2025-08-25 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bde4de59-f81a-3d5b-bc4e-5df27407b945 | -13.46106 | -47.0142 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dcfb1a9-d417-3076-b974-1817807745ee | -12.74923 | -48.13025 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8daf9e09-00ba-3b0f-89b8-c2da50ef069f | -13.34291 | -54.38632 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b75405d8-aa90-3eb5-baa1-4b6dc1367501 | -15.98619 | -48.07136 | 2025-08-25 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0ecffb0-b11a-3e3c-8161-1b5650e07556 | -9.86784 | -47.84005 | 2025-08-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b97fb37d-4e4f-3706-9fd1-5d4b625d0840 | -11.15707 | -44.69867 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a58704a8-83fc-31f2-855a-24a4ee2897fe | -13.43189 | -46.91504 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b642820-d96d-3070-8b8e-75e7b6cf8f86 | -14.16463 | -43.66859 | 2025-08-25 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c57ffdfc-284f-3565-8636-6103812fedde | -10.46683 | -48.32267 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4d7a8d8-cdbc-3350-83dc-42399ca0a900 | -14.92553 | -45.54358 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3449d686-444f-3549-bee8-ee86ee615643 | -15.1263 | -48.64782 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32b94068-5bf3-34d9-b158-93457d792f6e | -11.86605 | -45.12089 | 2025-08-25 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d7a6953-b9f3-35de-876b-07a957cd39ff | -13.65816 | -47.97897 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60c35237-5311-31c0-92b7-88827845f0e4 | -9.71352 | -54.98693 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68b0cf5c-cebd-31ad-bc0a-79512a5abebe | -22.3109 | -49.05134 | 2025-08-25 04:17:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4519e1f9-81bf-3aad-a17d-06436e6f8945 | -11.18785 | -55.02332 | 2025-08-25 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25df3b5a-820d-30d9-832b-332355ac1540 | -11.62387 | -46.23991 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e948b455-0d72-3234-a4a1-cdcbdb22b441 | -14.7642 | -47.51203 | 2025-08-25 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b668cff-06d4-3982-871e-63dcc73e87fa | -20.38532 | -46.7267 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e49931-02e3-3c49-96d6-d55ab66aa388 | -13.65791 | -46.88678 | 2025-08-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8823617-3a7d-3ed8-83a3-88359d2f5006 | -9.86859 | -47.83556 | 2025-08-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a53e5679-edd3-3ba3-82d7-756b2b8c6805 | -10.4325 | -47.18033 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 119bb426-010a-30a5-9996-9dc340fed1e8 | -13.51359 | -46.9099 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e146cb7-024d-3c5e-9bd0-441cb5deb2a9 | -15.07225 | -48.72351 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f75384d9-b3f2-3827-aee0-4d583766c8d0 | -10.78485 | -46.42723 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b76fa7b-5dbc-3297-b9b4-27bb761182c3 | -9.57831 | -55.36804 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c67980c0-052e-3262-b6fa-9455b25adb0c | -10.49262 | -46.88199 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a5fd02f-d7fa-3e31-b122-8ad4dc26406f | -11.27868 | -44.96303 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 669df37a-c595-3695-9a30-b3b8a3329720 | -9.47094 | -57.8239 | 2025-08-25 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da69ab3a-1050-308e-871d-44745faf360f | -10.71715 | -48.31358 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef665502-23ca-3132-ad14-186bda89f665 | -13.37504 | -54.3923 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e18055ec-7411-3cd8-b414-82725e775940 | -16.41927 | -49.9342 | 2025-08-25 04:17:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206aaa38-ed5d-3a44-87ce-da2031ddc06c | -13.45425 | -46.90742 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb50daee-ff89-3631-89fc-8ea5d5ca89fc | -15.13729 | -48.15004 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e108e6bf-35e0-307f-a319-f287303f45b3 | -19.93635 | -47.48936 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82ebc698-e5e2-3c70-94e2-351c68b45d4c | -13.46237 | -47.00632 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df9459c9-cf13-39df-bf48-18fc23a28d14 | -13.50182 | -46.89596 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 207c3c2c-ea75-3f09-baf1-33be734a0159 | -15.1198 | -48.64215 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc4bc7a-9c0f-3a45-8f6a-5002afe2492c | -20.98631 | -45.48438 | 2025-08-25 04:17:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 513d8f07-9ed7-317f-8aca-1c512b7a9683 | -20.35946 | -46.71802 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b0b3c53-2361-3182-aa13-ab6fe758f8ac | -13.13406 | -46.88906 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99ec9dbd-c8f5-3b92-b692-6ee8c8d27b9a | -15.143 | -48.63728 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9b68a43-8d7b-3145-b433-27554f5cbf92 | -11.27417 | -44.96959 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de8d9be9-0cb0-3225-a595-a7d463efc525 | -10.10413 | -57.76352 | 2025-08-25 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3a34fb4-ea02-3fac-8958-c6265994b87f | -13.81316 | -45.88481 | 2025-08-25 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 195283c3-b67c-3e54-a44e-f2c907605425 | -17.50355 | -44.78798 | 2025-08-25 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f402a13-4343-3d17-9835-c9f2365ec7d7 | -13.63381 | -48.16589 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9996126a-ca58-37c7-a7e4-89394d10c7a4 | -11.90959 | -47.11614 | 2025-08-25 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d0e06b3-7f8c-3ce4-80ba-4aef74344475 | -11.60599 | -46.34851 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ce4b3b4-ff92-3eb5-906b-ad8d043a845e | -13.46642 | -47.00319 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f92da1cc-fb73-3b1b-aa73-0939cd53ac9b | -14.39031 | -51.9498 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e4bf109-fa3d-33b6-a1f4-92e2926cbe12 | -13.44297 | -46.89039 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9cbe381-028c-35cd-a847-32be1e3cba53 | -10.88478 | -55.7907 | 2025-08-25 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fd9f9fe-c489-3d23-a1ef-cf0a8439d553 | -13.40078 | -47.52353 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e1f0477-7452-3aa1-8db9-27d37d574581 | -10.71101 | -48.32709 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5176fe7-dfb9-3f12-ac1e-68d2736889c5 | -14.10429 | -53.99553 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57499adf-2735-30c4-b732-04b47be2819d | -23.32826 | -47.84146 | 2025-08-25 04:17:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 32484546-2e7a-3511-afc6-9987e2be30d6 | -14.81656 | -47.91777 | 2025-08-25 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7809180a-7f86-374a-b4aa-7391187c525e | -15.94283 | -47.76168 | 2025-08-25 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50591262-5c6d-3da3-8195-315dc13982f0 | -13.61727 | -48.17587 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63a827f0-81b0-3ed5-a4bd-bc2183ebac8e | -11.60167 | -46.33228 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 162f983a-cb4d-327c-9757-096ce2b173a5 | -11.39755 | -50.68209 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23139280-4014-3722-b238-872e46bc340b | -13.43891 | -47.023 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bc574da-e882-3f2b-a4c0-9f6bbd6bd1ae | -11.26807 | -44.98669 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c8106ba-5a18-3dcb-a31c-495e908d7cba | -14.10369 | -53.99858 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8c6a0d6f-2ba0-3dc5-89ca-0cc128cce3d0 | -14.258 | -48.04538 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5c9bddf0-6be8-3975-8769-eda5a3e37716 | -10.7118 | -47.13618 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2202179b-0dc1-35a3-8e03-684c7448cbe1 | -11.61561 | -46.24279 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27378e20-d316-3bb4-aa00-a384598f70eb | -20.11363 | -47.25735 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb29bfb4-f996-3440-9385-43e5f2b3d1a9 | -11.91023 | -47.11218 | 2025-08-25 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b98014ba-bbf2-3b43-a576-ede2065fe927 | -13.42816 | -46.24772 | 2025-08-25 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec8d188f-2e79-3d78-bd30-0aabbafeea09 | -11.10627 | -44.78398 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03654877-3996-3f97-98ce-0c1fb93310b6 | -10.79235 | -46.42456 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27c0c2ba-c320-3e85-9fef-58c383e0834b | -13.43745 | -46.92406 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7345106-04c2-3129-a4fa-7e305e923ba9 | -9.54889 | -48.14064 | 2025-08-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53006738-ec62-3854-b848-34138d090ae6 | -10.60164 | -44.33607 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3c54f2e0-45bf-3200-8a29-12f4c3a1dded | -11.46709 | -55.47195 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 199e2c0e-7506-3e03-a455-f6c626a44fee | -13.49281 | -46.88668 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a10b59d0-effb-3595-b3df-75bde7550a92 | -11.62788 | -46.23675 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 74f61231-86bd-33e6-8653-3b2b2bf49aaa | -13.43132 | -47.02618 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 570cb7bc-6e63-30bc-b8cd-b0e0e020c00c | -11.60258 | -46.34797 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36b23db3-c361-3607-a4c3-5da6db352376 | -15.04096 | -48.5083 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cc50e62-12d2-318c-9931-d27d96597f8e | -13.44495 | -46.92125 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd2a45f5-93e3-399d-81af-da99f94d0755 | -17.58167 | -45.38697 | 2025-08-25 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cedda3c-6c22-3def-8e46-f71a4d80b3e0 | -11.17959 | -55.03488 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e154a6a5-c2de-3dd7-aa7f-1323fe9fd430 | -11.17547 | -55.02527 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2e13e2d-bfd7-36e0-a2a0-df400857a5e7 | -10.6176 | -55.05216 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e866ff03-d771-3c56-ba1e-bd9b771c0739 | -14.25732 | -48.04401 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| db16b66b-d8fc-3c6e-937c-ebe0ddfca168 | -15.03877 | -48.52126 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 967fbd3a-f409-36f6-a7ad-aca38fdcf487 | -13.43678 | -46.9282 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1644ca1-b0e2-34f6-9b3e-a80476d5cffc | -15.0761 | -48.67936 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README33.md)
