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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2092b236-767b-3f6e-b06d-00c8ce26cf25 | -12.36214 | -50.02951 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 655f2221-7695-3dd9-891e-857ebb0b7c9a | -14.05888 | -53.39896 | 2026-05-04 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 400aea8c-edc2-3aab-8d6f-11da6a0ca366 | -11.85232 | -55.01223 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a6a1269-dd2c-3516-adbe-4801d818cfb1 | -12.36159 | -50.03307 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1bb8accc-0fdf-361d-96ea-89359cf04d65 | -17.40513 | -42.62238 | 2026-05-04 04:44:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16d9c0ec-1f2d-3891-8cd3-6aa5cd8bdf29 | -12.36547 | -50.03004 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d3a541f-e25b-3d1f-84ce-e8468980e4d6 | -12.22772 | -54.37653 | 2026-05-04 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90d7dcdb-d5dc-383e-83c3-9b863d41a80d | -14.53448 | -48.55464 | 2026-05-04 04:44:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e0251bd-a7c2-3656-8140-7dfa1874061e | -11.91831 | -54.81649 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3452edc-bb27-3683-ab4a-91b229f1d343 | -18.0803 | -52.97166 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd35ff42-e0ff-3b36-90d4-5216550b53ef | -12.35494 | -50.032 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db52933c-928a-3ff4-8fa8-8cb3649ccc0a | -12.35439 | -50.03555 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8bfb5fe-3415-3dd6-a5a4-d6213d695c89 | -17.40475 | -42.62575 | 2026-05-04 04:44:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c0150c-66cf-3da5-9be6-4d1ed6e910ce | -18.0013 | -52.97267 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57d497d3-8116-39a6-ad44-c5e88cab7a62 | -12.44363 | -54.21181 | 2026-05-04 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9df1ea60-2df3-3d45-80cc-6c532e808d77 | -11.91914 | -54.81175 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbbce2fa-5944-3d36-8c9e-f2bdace82c28 | -11.84251 | -55.01339 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06f8dccd-965d-3b76-a1b4-f7c673ef9967 | -14.31428 | -57.7347 | 2026-05-04 04:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec541236-20f7-334a-ac1d-568f8eb33073 | -12.35826 | -50.03253 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d455129f-b088-3795-b765-5068f2bcfb34 | -18.04949 | -52.99259 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0abf521a-76a8-3329-ad0f-3a22aa46082d | -12.38987 | -50.02668 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6bc26930-8e16-36c8-b769-36ee21ea8de1 | -18.00404 | -52.97693 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 414aa212-4e22-32cb-91b5-e2f255f42f97 | -13.95415 | -47.25331 | 2026-05-04 04:44:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e74456e-571f-3f93-9518-678dfb0608fd | -14.31358 | -57.73783 | 2026-05-04 04:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10085096-984d-3b89-b026-c10d2398919f | -12.35881 | -50.02898 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bbae20c-d6a5-3482-9ecc-cf48c4573730 | -17.95215 | -52.96396 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c65503a-5847-3815-a209-c12551797a41 | -18.90969 | -48.33429 | 2026-05-04 04:44:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ce7b4a7-f438-31fe-9eae-75a7c9387333 | -14.32317 | -57.73514 | 2026-05-04 04:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68998e60-3a6a-3887-b547-e2bf3adae2fd | -11.84636 | -55.01407 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a16e0d54-1a2e-3f64-8fca-52a1babbe828 | -18.25165 | -51.25977 | 2026-05-04 04:44:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 234df885-a20c-3a13-954b-687cb323efa4 | -11.8502 | -55.01477 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9db559ee-d19e-32cd-823f-470f60ec576c | -18.00464 | -52.97327 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f2cd1a6-2e65-3cad-b59a-41a5127670c6 | -13.95719 | -47.25139 | 2026-05-04 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab588ef6-7f6b-32d3-8044-67da7c686aa6 | -12.36104 | -50.03663 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7cb72673-7722-3377-a50f-fb4b4a63e083 | -18.07697 | -52.97107 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d67c0e7-e1e3-394a-b8de-a2327599d779 | -13.94906 | -47.25481 | 2026-05-04 04:44:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9400ccfd-0464-36cf-b111-8c96f327683b | -14.31443 | -57.73338 | 2026-05-04 04:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06bfc3b6-8d63-35fc-a4c6-6e2d677d589f | -14.02134 | -53.36834 | 2026-05-04 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1d1078d-46d0-3957-9edc-7d06ec4e24c9 | -14.31347 | -57.73918 | 2026-05-04 04:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a88072af-7e13-354c-9d9a-2296a74b535d | -16.59534 | -58.23966 | 2026-05-04 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e65db36c-fd60-3e0d-a7c6-7e3af0adb70c | -12.36437 | -50.03716 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 879bf948-54ba-300a-b25b-fb5e7a5fc0ac | -11.85103 | -55.00992 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f45d6db1-56ef-3722-b6e6-6aa1edaea985 | -14.31796 | -57.73872 | 2026-05-04 04:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11d0f002-e5a1-394a-bd40-aec6e6d7a2b8 | -13.95347 | -47.25076 | 2026-05-04 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff08e098-9629-3f29-b862-0da1ba382eda | -11.91369 | -54.82055 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b9432de-b55a-30e9-ad39-3639734a951f | -11.91285 | -54.82533 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b3c3fb7-5936-3abf-b3aa-4001c627656c | -12.38599 | -50.0297 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 594e3464-2eec-3e3a-8de1-6ecce14a8c5d | -18.05008 | -52.98892 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c9aa7d0-7c51-385f-9fbf-5ea7bb23aa38 | -14.06234 | -53.39958 | 2026-05-04 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b9dc537-53bb-32bd-83b7-8c3f14ae63de | -13.16109 | -53.26334 | 2026-05-04 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4da6a4a-0f86-3fcf-9939-1d3db1756292 | -11.90989 | -54.81988 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5488e28-1d5b-312a-b2bc-1703e8fd2f09 | -12.36492 | -50.0336 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf11753d-77d7-3779-b922-3df134cd9298 | -18.07756 | -52.9674 | 2026-05-04 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f143549-ae1b-3a5f-857e-9e64b3e38e03 | -18.25499 | -51.26033 | 2026-05-04 04:44:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cbb7262-b60e-3177-a372-a8e565908fe7 | -18.25109 | -51.26345 | 2026-05-04 04:44:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcf1942e-a52f-3ab8-af7b-760aa7c153aa | -12.35771 | -50.03609 | 2026-05-04 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 576cca7b-beb7-3517-b072-7f3060646d18 | -11.85702 | -55.00811 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e844feb0-b60c-30c6-b42e-ba4675eaa9c6 | -11.85487 | -55.01062 | 2026-05-04 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70debbca-53e6-3cab-be80-52052a19030a | -22.36113 | -47.31787 | 2026-05-04 04:46:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 120848b0-62f8-3c2c-a3ff-19de13d5b63b | -21.50101 | -51.76878 | 2026-05-04 04:46:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70601c44-a805-3250-91f7-ee6589a5cb35 | -23.35708 | -49.48735 | 2026-05-04 04:46:00 | NOAA-20 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 46cf66eb-2a10-37da-8cea-0ca6a9c4615a | -21.51868 | -49.86447 | 2026-05-04 04:46:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bb1117c3-a036-30f0-8992-9e3b898b8bb6 | -23.15837 | -48.35868 | 2026-05-04 04:46:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 002d9f89-1c5b-397d-9ea3-634a6c2754d6 | -21.49708 | -51.77201 | 2026-05-04 04:46:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1eec63dd-8758-3e36-844b-dad4f91a1ba3 | -21.49766 | -51.76821 | 2026-05-04 04:46:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81167fe8-bac9-38f7-8f07-74ba627a3922 | -12.36198 | -50.03575 | 2026-05-04 05:31:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9d08037d-b814-3cd7-bf40-cf90c392e4a8 | -11.84703 | -55.01487 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acea1f1d-6ecb-319f-902b-b0cf10f4bd89 | -12.3616 | -50.0345 | 2026-05-04 05:31:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ae498cc-95d8-3bf0-bbe5-701210967d85 | -14.00241 | -56.62799 | 2026-05-04 05:31:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c565fa94-a0ac-3a82-9d78-0fdd4a70b57f | -15.22008 | -57.65538 | 2026-05-04 05:31:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39e6d56c-15ef-3e20-95ac-2545d544d52b | -11.91838 | -54.81693 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5912207d-22d8-33fa-a50f-4d12c72f7cc1 | -12.36887 | -50.03659 | 2026-05-04 05:31:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3013621e-83de-36c1-b1ae-97706a599d75 | -12.36848 | -50.03532 | 2026-05-04 05:31:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a99ff0f-8255-31b2-92c6-ac65ad629391 | -13.66451 | -56.96338 | 2026-05-04 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f351979b-171e-33f6-8074-33460c13d41b | -11.918 | -54.8199 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0baa1b7f-8b59-360d-84db-0306ab9bf14c | -14.31656 | -57.73552 | 2026-05-04 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 785a5896-3cfd-30a7-80c3-4467f38c147c | -14.06302 | -53.39929 | 2026-05-04 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 164aee55-8c05-33d7-a153-28a72c3f3daf | -11.91736 | -54.81656 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db25eb77-c14f-3a39-9198-6d156cf8fb85 | -14.32515 | -57.73668 | 2026-05-04 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c98de4a-93e4-3462-9923-064ee1ea9f5e | -11.917 | -54.81955 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d9f8cc2-c03c-3ee7-8f24-76a362affd18 | -14.32569 | -57.7326 | 2026-05-04 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3b35478-a689-370f-a55c-e22ad76b4c56 | -11.92278 | -54.81432 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 499deae8-38a8-3e17-8e73-aa7c5a141aa8 | -11.85275 | -55.00974 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5502b567-6f62-302f-9ebf-8dfcb0c3d481 | -11.91664 | -54.82249 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5452a9ad-5d8b-3030-a2c8-f359cce38f1b | -14.31602 | -57.73958 | 2026-05-04 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03a057ca-8421-3909-9f6e-f9244226dda9 | -11.91877 | -54.81396 | 2026-05-04 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ccbd251-92ce-3c89-aee0-6e606cde9f4c | -16.59735 | -58.24117 | 2026-05-04 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fb4337d7-8b47-343e-abc3-6d3b39365393 | -21.50184 | -51.76734 | 2026-05-04 05:33:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7e365dbe-7e83-300e-b50c-77bb6c0f934c | -18.0481 | -52.99322 | 2026-05-04 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 802e9638-2277-3af9-bb92-d1b8f4f74ea4 | -18.07545 | -52.97095 | 2026-05-04 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5342801-6445-3704-b7e1-42abc90f4788 | -18.0816 | -52.97173 | 2026-05-04 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38e3acc5-de27-381f-b0da-8c1afc413dd9 | -16.59306 | -58.24055 | 2026-05-04 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 24da5b70-7c42-3a4a-8790-fe57026f5233 | -18.04844 | -52.99278 | 2026-05-04 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 818dee8c-8dd6-3dce-bb8c-dac20f8ec46b | -21.50137 | -51.77427 | 2026-05-04 05:33:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 93b253ce-5484-3e3f-820d-aa6b0542c722 | -21.50049 | -51.77261 | 2026-05-04 05:33:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 16a808c6-6d39-3f00-9f74-86cec3234311 | -12.35562 | -50.03268 | 2026-05-04 06:44:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b09bc122-9735-3f60-84ca-fe70815e8e52 | -7.92423 | -55.43953 | 2026-05-04 06:44:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 12e0db85-3b59-3ece-a8ce-2f70ccf8844e | -12.50592 | -41.92836 | 2026-05-04 11:42:00 | TERRA_M-M | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 148410a3-42d5-3bba-a3d6-4b8e59b9b84b | -18.24483 | -47.0147 | 2026-05-04 11:42:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3230934e-836c-3d26-b667-f176e7a546b2 | -10.98635 | -45.09168 | 2026-05-04 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README4.md)
