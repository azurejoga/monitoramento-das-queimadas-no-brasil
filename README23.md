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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef839b2-41e3-3c89-9f43-6928e8d751ae | -11.33202 | -46.22865 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83c775bc-5bf4-3fc8-8e10-a1c41f4599f0 | -13.23865 | -54.24877 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd45d401-48b3-31d4-befe-ac3a25d16349 | -14.94327 | -46.62952 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7183c9c2-dba9-3b08-bdc8-56493a47e071 | -14.93644 | -46.62859 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a174a068-766a-3307-a745-04752467a7a6 | -13.8357 | -44.06109 | 2026-08-14 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b65714d5-b713-37e6-95b3-20475d39956b | -12.34903 | -53.14025 | 2026-08-14 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c84b5add-0cea-3513-9461-63b91a8b5535 | -14.95692 | -46.60851 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcc05c19-1c19-3ce8-b3eb-b880875b5a00 | -14.65997 | -52.36697 | 2026-08-14 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf012a33-25ad-388d-bff5-c55abc4e650f | -10.97044 | -50.54179 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b3b636f-737f-3900-8011-7c368d18ab71 | -16.87637 | -54.13067 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6946eb55-8df5-3bfd-b083-84b910c6374f | -14.09543 | -53.64526 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6356867d-39d1-3669-afea-77ffc07e9248 | -14.95753 | -46.60453 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2325e14-6936-353a-b2ee-66d04b0388a7 | -9.983 | -53.95514 | 2026-08-14 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c527cede-f53b-340e-91f7-fba65bed2e8c | -12.0313 | -47.81215 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6d43b71-7d1e-3350-827a-66aa64da2ee0 | -14.04657 | -53.58941 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f459edf0-4041-3374-bd45-cc47814fe092 | -14.28617 | -51.96696 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2a59877d-08c8-3967-8630-84b4fc242afe | -13.90317 | -53.77767 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4322cbe-3fd6-3eea-a694-dc7e220f658b | -13.75609 | -53.41461 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86d816f0-e059-3fad-acf3-d6b1d0d11699 | -11.49414 | -54.62781 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d0eaa84e-1149-374d-a76b-08e6ef268e0d | -18.48762 | -43.40152 | 2026-08-14 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f658566e-445d-3d69-9762-6aa4ba39a9fa | -11.49133 | -54.61748 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0c5d346f-e9bf-36b5-8b20-daf3bb606c5c | -14.72992 | -48.22993 | 2026-08-14 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82fec3b0-acaa-33eb-b088-2af43a74003c | -13.55871 | -46.25249 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d844f9f-011c-30e0-a15e-c000be7951a1 | -11.2032 | -54.83073 | 2026-08-14 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd8ec3a7-da07-3ff7-8970-6d89e2ed9115 | -15.00719 | -41.95108 | 2026-08-14 04:34:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b857bca9-5da7-3588-84a1-92dd4ef2db1a | -14.71707 | -52.89769 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ba962b1-a42a-3db2-a5d1-31e203374a37 | -14.29354 | -45.26984 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e985dd54-35ac-3836-8ca9-efc0b8b32893 | -14.45454 | -45.69685 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7648bed7-c559-3451-9b4d-0b3a77334c80 | -14.9723 | -46.59919 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c61918bf-4e81-3bf2-becc-24c02b3d41e8 | -18.41381 | -45.19675 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3835cfb5-47e1-3d06-9259-697f14ab46aa | -14.94096 | -46.62174 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a69f606d-0a07-3064-a798-f6a45da35231 | -18.49243 | -43.39735 | 2026-08-14 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad8fe49e-e0fa-371c-9267-a8ae85c95418 | -14.07501 | -53.61822 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cd5ac97-37ca-39b0-9510-1f9557997961 | -13.68066 | -46.25629 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 522024ee-3f1f-3d65-8566-934325cecaa7 | -14.98845 | -46.6087 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db8f9af7-da61-35f5-b586-c9213fd1dfad | -11.06431 | -50.94732 | 2026-08-14 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bd1ab36d-d172-3d16-b274-e2a694879b85 | -14.94555 | -46.61449 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 277a8fbf-358a-318f-9da7-fd801d40a84f | -13.92102 | -53.96204 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6697215-536d-3cad-92c1-d52fe85d9e99 | -15.50803 | -53.02728 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75cdc619-f6ac-3532-8e45-ab5802048864 | -12.01024 | -46.40078 | 2026-08-14 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26b49ef2-1574-39ce-9f70-13b570115328 | -13.92173 | -53.95811 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba822c98-0914-388e-be4a-5b32732bfb18 | -11.87274 | -51.94413 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fdb4be3-6e08-3173-89d6-5c0db5dd3016 | -10.59284 | -55.59005 | 2026-08-14 04:34:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2da91bb-34af-3bfa-a907-3dae28417d15 | -18.41446 | -45.19188 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e629335f-1b3f-34d3-b3c6-7b2bb645c8b8 | -9.97853 | -53.95435 | 2026-08-14 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3c71ba7c-0d6a-313b-aaae-87e474cc2759 | -14.05544 | -53.65622 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2afda1d-1521-3600-87d0-e6109e69ae29 | -16.90567 | -54.1521 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b778b76-bf65-3bbd-96ac-dda455d8c956 | -16.24887 | -53.70896 | 2026-08-14 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1d2de67-fb04-328c-b527-f3a2982d5df6 | -14.21494 | -53.35512 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5afad26-8a03-3df9-a6bd-d6da7e88b7ca | -16.919 | -54.14755 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5ca3448-1f94-3e81-ae98-c9461713e787 | -14.07236 | -53.63284 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5951b3fd-cf34-3196-ac86-6b444415838a | -13.27895 | -54.23326 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f80cfb55-5603-3fbf-8195-e8874fbbf0b4 | -15.33519 | -48.00777 | 2026-08-14 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24dd3957-0d34-33ed-aae1-7cc0862d0f43 | -11.45302 | -44.5546 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9a668e2-a7fd-39e5-818e-79455f8a0ad5 | -13.24723 | -54.25053 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d664c9-6485-3c4a-b48e-90198aa68d20 | -16.71865 | -46.40336 | 2026-08-14 04:34:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae545e00-1db9-3d40-822d-2a0ff52a61a1 | -12.712 | -48.44506 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c877de7-c384-3a78-85cf-b2997ed1c32b | -14.44992 | -51.86403 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 322f688e-5b1f-332c-bf01-c69a8e596526 | -9.97933 | -53.94988 | 2026-08-14 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3e3c48f5-f437-31b9-935f-701cebbf0a55 | -14.07306 | -53.65225 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74ca5019-b318-307f-a264-0f73d7e4b640 | -14.05275 | -53.64784 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52fd669a-c269-3778-a703-c77ac17a8dab | -14.43842 | -51.86805 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8090eaf7-defa-30f7-a5fc-d6b653450e0e | -11.86645 | -51.95774 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eb21a62-d69d-3e76-a639-192239776a5f | -13.28555 | -54.22165 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea475690-cd59-34f6-9b90-90930bb72da8 | -10.70474 | -50.47752 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a27c54e2-829c-3683-9fae-97a7b86dbabb | -14.99187 | -46.60915 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b98d3bc-b3d5-3193-aaf2-50e7b69ebb62 | -14.02962 | -53.58998 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c06380dd-aef4-34e2-a7df-1f389079c2d5 | -12.51271 | -55.78686 | 2026-08-14 04:34:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56558208-aeba-3a9d-9267-a8616a1bd2e1 | -13.83074 | -53.78836 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63289209-3673-3154-9e44-6eff2a5d828d | -10.97538 | -50.53412 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 650913ec-050f-3bb9-ae3f-a494235e8dbc | -14.43552 | -51.86293 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a4311cd-50fd-39a1-b9c0-d8db9965dec7 | -14.96204 | -46.62078 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e4bcb03-40dd-3060-9db2-4bb3f0184080 | -18.28801 | -46.08409 | 2026-08-14 04:34:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20538bbf-226d-373e-98a0-eb71a318876b | -11.48433 | -45.09412 | 2026-08-14 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d73f3026-7d38-3623-9b6f-62e2aa216fc2 | -15.09667 | -50.43715 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 387b51df-9ccd-3cda-a11f-7585d6f71a73 | -14.39551 | -53.16103 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0fdda44f-df72-324e-a2d6-85f1cca64042 | -13.38843 | -42.38871 | 2026-08-14 04:34:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e2db27dc-44fe-3ef0-b9cb-3dd2f3946c85 | -14.71501 | -52.88702 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 807b6d52-0e74-32d5-b4cf-36a3a4be2600 | -13.38789 | -42.39264 | 2026-08-14 04:34:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 000ddff7-d3c4-3efb-82db-998f0b2ad6ff | -10.80795 | -48.57621 | 2026-08-14 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f18f217-82a2-3d85-8f4d-93f8227a20bd | -15.35285 | -49.667 | 2026-08-14 04:34:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 125e9883-e61c-3631-93a4-7689e6a6991c | -11.32148 | -45.21841 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76f8df12-0373-3844-ba29-991d3ca91395 | -11.49586 | -54.6184 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7bf5302a-9569-3b18-87b7-bb05d027f1c6 | -10.97411 | -50.53286 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 827ea388-a30a-34c9-9d14-c2c2aa06359d | -14.05128 | -53.58663 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| beb9b2bf-e88e-3653-b62e-c90732b8cb13 | -13.90335 | -53.84657 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78ec9705-f0d1-3607-b823-a23701580de9 | -17.56882 | -47.50433 | 2026-08-14 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ee68cc4-c55a-3a80-8c9c-3b17b930aa04 | -14.09135 | -53.64445 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4ae43a3-b2e0-3819-a75f-27ebab26c25e | -16.91035 | -54.14935 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac3dd88d-40b5-3ddf-bf5b-689188390060 | -14.22303 | -45.40304 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62f7e7df-5099-354f-ac9e-a46554156560 | -13.27466 | -54.23244 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4df9c91c-2999-3751-b56e-7460d60fe830 | -11.07525 | -50.94922 | 2026-08-14 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f001285d-bee1-3253-ab18-c0d96166cb31 | -14.72787 | -47.15008 | 2026-08-14 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9913700a-4d5f-300e-9ba3-5579ee73d10c | -14.71204 | -52.88138 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad6a9c2a-649e-37c8-a30c-b6824ce31c04 | -14.4639 | -45.6818 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd1cae1c-dc7a-3d47-8af1-a903f65d488d | -12.32698 | -50.86469 | 2026-08-14 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c94ea80c-3acc-306d-885a-6c14b45d2e59 | -14.33367 | -51.99113 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0adc23a7-5059-317c-b516-9a9c69af7476 | -16.91307 | -54.13464 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86a1254f-ed1e-367e-bd25-c8f518375eb7 | -13.3926 | -42.38935 | 2026-08-14 04:34:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da449863-e64f-3a43-8913-5ecdad2d0cb8 | -15.16109 | -52.80845 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README24.md)
