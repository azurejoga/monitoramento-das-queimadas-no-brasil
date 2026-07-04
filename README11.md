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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 652213c4-70f5-39bf-a921-3dce0825fad8 | -18.71742 | -47.53356 | 2026-07-04 04:02:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a10e5aae-20be-3b69-9be8-46bad621752e | -18.12782 | -46.46301 | 2026-07-04 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76af79ac-a5c3-3f91-902f-a29b1a59d7b1 | -19.83815 | -49.06893 | 2026-07-04 04:02:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc7985bb-4c91-3fd0-ad4a-c66a730a5db9 | -13.25219 | -54.34524 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9955a4d1-aa0f-3681-8830-128c7cfd74c6 | -12.67715 | -48.21592 | 2026-07-04 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eebcfe4a-9b99-3583-894e-d55f73991a99 | -13.22966 | -54.39485 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abe2e1be-1ea4-3047-9d66-0e4130603947 | -13.25675 | -54.34012 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 316fc3fe-895b-39e6-9cc9-567ff3fb3e84 | -20.4418 | -44.8583 | 2026-07-04 04:02:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b537a424-1b7a-3ec0-843b-8cb56b6645c3 | -19.86333 | -43.87265 | 2026-07-04 04:02:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a5ea4341-64b6-3154-9e80-c6b3a09d8921 | -18.77399 | -47.62257 | 2026-07-04 04:02:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 894e5bf0-a4d4-340a-b7ab-2d550ae6f01b | -16.49567 | -43.50232 | 2026-07-04 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fe77a5d-9481-31d2-b5be-825bcf198360 | -20.23991 | -40.37874 | 2026-07-04 04:02:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f9c11fe6-687a-32c5-a242-d884166beca4 | -13.22472 | -54.36908 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c04acac9-065d-3084-bcc4-ea3a0f22fc50 | -13.2302 | -54.37814 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 882c28a1-ff0d-333d-9a3e-f096314ecc02 | -17.69138 | -48.64054 | 2026-07-04 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b31dcbc-2d6f-3f7e-b568-cc7ba947424e | -13.23295 | -54.38013 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2852d73f-2dc3-3e86-8d9f-1fe189a906e8 | -12.50908 | -48.25611 | 2026-07-04 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0d11d2f-623b-3898-9ac4-9c5ef7a64dee | -13.23842 | -54.38903 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4785de1-e639-3d82-b05a-5975cce033b2 | -13.24661 | -54.33667 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cc352e93-b016-3bfb-b781-82f82840f960 | -13.24096 | -54.34422 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d8ff7811-0524-3c1c-a85b-331e9b753eb4 | -18.99857 | -49.76621 | 2026-07-04 04:02:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 970d1d04-ddaa-30c1-b3c3-d58b138cb5f1 | -13.24006 | -54.38166 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e23a50-6227-346b-ab9f-4a44955aa767 | -13.23798 | -54.34225 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1e635081-c4db-3b47-9c29-c9982fd75470 | -20.39375 | -46.56038 | 2026-07-04 04:02:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b43bc92-602a-3f55-86bb-f94232d4ba96 | -13.23388 | -54.34263 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a1800e48-4336-34c8-9501-144c1c3be54b | -13.23648 | -54.34915 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7a1d976e-f77a-32cf-91b0-bc8e9dbff62b | -13.25372 | -54.33813 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7330cb38-4658-3e56-862f-52947ab1be29 | -13.23942 | -54.35115 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| db1796d4-763f-3386-8fca-3ef08a7092d3 | -13.23572 | -54.38703 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83adb267-63b0-39c5-9440-1ecae0302edd | -13.24167 | -54.37445 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92a9a2ef-470e-3627-b3f7-60a5bc413215 | -13.23178 | -54.37083 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e174f0c8-00dd-365f-8e32-20afb2742439 | -12.50852 | -48.25908 | 2026-07-04 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32b1a42d-e6f8-3e78-b5c8-32bbce792c02 | -13.24965 | -54.33864 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| bee91a89-83ad-322f-bc09-32802086bb84 | -18.76974 | -47.62163 | 2026-07-04 04:02:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f115aa-b980-3ca3-afcd-6d9bf535f534 | -14.22759 | -45.44592 | 2026-07-04 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb477a6c-3aa5-3db9-8589-5324aad74866 | -20.55752 | -42.09668 | 2026-07-04 04:02:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b1b744a9-1e0e-345f-892f-7d6423f5af1d | -14.1934 | -45.42812 | 2026-07-04 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7efb2c7-0bb0-3362-af31-3c4994d35420 | -13.24442 | -54.38121 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21f02318-cd5d-3650-b42d-114b3b2bf39a | -12.67604 | -48.22165 | 2026-07-04 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 198db493-ce29-31bf-a086-95350208b0d6 | -21.20165 | -48.60118 | 2026-07-04 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6b1e456d-f48c-3c1f-b32b-200de8615472 | -21.89872 | -48.48595 | 2026-07-04 04:04:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 563ab399-314e-311f-91ae-1a38ca3f8df0 | -22.79513 | -49.34716 | 2026-07-04 04:04:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f74f6c-c410-32ba-b447-0e3bb3669fba | -22.78734 | -49.34029 | 2026-07-04 04:04:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e8e072d-45e5-3fe0-9822-8bd476535520 | -21.42957 | -48.64503 | 2026-07-04 04:04:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6f4c680-c31f-3446-a5c7-1dca7b5740d1 | -21.20599 | -48.60212 | 2026-07-04 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8e4afea-a197-3d27-84b4-78c019783a33 | -20.7117 | -50.52975 | 2026-07-04 04:04:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 33cf420a-35c1-394c-802a-a0dbc140474d | -21.90185 | -49.45091 | 2026-07-04 04:04:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6e6fd7c1-b616-392e-b728-a7e68a636f1f | -21.1117 | -48.99837 | 2026-07-04 04:04:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83209527-ba87-3e76-a89b-b334ed20baa3 | -21.20254 | -48.59679 | 2026-07-04 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 63d8b2db-130b-3fce-89a8-2cb47e53b057 | -21.20058 | -48.60251 | 2026-07-04 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d4dd6b65-7ede-39e1-a4e7-f86e2f1a6bf1 | -22.78637 | -49.34496 | 2026-07-04 04:04:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ecfc887-e7a6-3b2d-a401-dabe82b64c05 | -22.79117 | -49.34938 | 2026-07-04 04:04:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d07ce8af-c25d-34cc-b5a6-15a80dfc6308 | -22.03688 | -42.49368 | 2026-07-04 04:04:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5de98264-c834-3361-9d81-cc5c609dd0f7 | -22.1807 | -43.09749 | 2026-07-04 04:04:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 37c048b2-ef9c-3f9a-bc23-6bef1bd996a8 | -20.76628 | -48.56841 | 2026-07-04 04:04:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb861090-a764-3b9f-b64c-56fe236e87d2 | -22.78773 | -49.34355 | 2026-07-04 04:04:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4428d91a-27d9-34b5-84dc-5a0eca94c0a8 | -21.10896 | -48.99982 | 2026-07-04 04:04:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7c48210a-1e5b-369e-b354-fa5a86410bc4 | -20.70679 | -50.52847 | 2026-07-04 04:04:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a5f6652-1b36-33ff-9c50-5ef0f5fb1334 | -22.79554 | -49.35054 | 2026-07-04 04:04:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 122618fd-f779-3a7f-941b-3dcf1611a373 | -21.20144 | -48.59812 | 2026-07-04 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 076a3b14-fd47-316e-af4d-11fc7e910f1c | -20.76605 | -48.57026 | 2026-07-04 04:04:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a9c8c59-2460-3752-b7c8-72bce2cd7978 | -12.7741 | -44.5396 | 2026-07-04 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| b5d9ca6b-727a-3e00-ba61-3d36583e967c | -13.2592 | -54.3489 | 2026-07-04 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b83e7372-9415-35b7-a43c-346d0735bb5a | -12.7553 | -44.5194 | 2026-07-04 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| bb11d46c-fb05-361a-8a81-a29614c5255c | -10.9397 | -43.0593 | 2026-07-04 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| d451ecd8-892a-3bcd-b346-98c47c8cfc69 | -13.2595 | -54.3283 | 2026-07-04 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6e2a7567-92a3-3a24-8add-5234a6e6225f | -10.9401 | -43.0355 | 2026-07-04 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| a0830df8-981f-3580-b634-ed2e105800a8 | -10.9209 | -43.0384 | 2026-07-04 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 24eb4970-1fe7-3eb7-af88-faf383e2c7f2 | -10.9205 | -43.0622 | 2026-07-04 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 57a280d5-be07-3709-95e4-95185da1de52 | -12.7548 | -44.5428 | 2026-07-04 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 6994dc4f-411e-3b97-8932-6a67ab7c76c2 | -13.2401 | -54.351 | 2026-07-04 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6fa9551c-78a4-30bf-85aa-f1ba947b0032 | -10.9401 | -43.0355 | 2026-07-04 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| b32f6995-2854-30c0-a87c-c3c54280d185 | -12.7553 | -44.5194 | 2026-07-04 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7102bed8-5745-3b13-8a74-77f9819c281d | -13.2404 | -54.3303 | 2026-07-04 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 95ab0e1e-20f5-39e6-8d3c-ec97ea34f847 | -10.9397 | -43.0593 | 2026-07-04 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 8010c358-c983-3362-b4b4-1c455350ee77 | -13.2401 | -54.351 | 2026-07-04 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d637c642-c18a-3b8e-b05a-9ddd9b64fc6a | -10.9205 | -43.0622 | 2026-07-04 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 8d0dc206-9c57-3859-91b8-53e2679258f8 | -13.2595 | -54.3283 | 2026-07-04 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| adaf1d8f-c474-3165-9b46-1ea7699c401a | -10.9209 | -43.0384 | 2026-07-04 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 93ad7505-ce69-3208-919f-6864e1576b87 | -12.7548 | -44.5428 | 2026-07-04 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| f5549506-7c69-32f5-a4be-8878d889773b | -12.7741 | -44.5396 | 2026-07-04 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 086f43ba-a17a-36b9-bcd2-11d26b4d69e0 | -13.2592 | -54.3489 | 2026-07-04 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5490c7f7-24f5-3d94-8986-61621b4e2211 | -13.2592 | -54.3489 | 2026-07-04 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| a56b52b5-cf45-3a33-97c7-253ce2e78fdd | -10.9205 | -43.0622 | 2026-07-04 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 3fcfb7ad-884b-3b27-9557-c7d153b3e45c | -13.2404 | -54.3303 | 2026-07-04 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| ccc686fb-90d6-3a9e-b16c-2d8a39cf3ad7 | -12.7553 | -44.5194 | 2026-07-04 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| d451504b-b55b-3f43-aba4-e600facbfabb | -13.2401 | -54.351 | 2026-07-04 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 2e30d7d4-8527-32b6-84ea-14aab0799b0d | -10.9209 | -43.0384 | 2026-07-04 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 1074fe7f-03e1-37a6-90f9-52484ec565be | -12.7741 | -44.5396 | 2026-07-04 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| e41961d7-99f8-3c54-880f-1c5a0386e915 | -13.2595 | -54.3283 | 2026-07-04 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fead33f7-1522-33fa-887f-58a35b1ac316 | -10.9401 | -43.0355 | 2026-07-04 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.9 |
| ff3f723e-1bf2-3338-994d-8066429326a6 | -12.7548 | -44.5428 | 2026-07-04 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 4b016f33-1aa6-37b2-b489-19d2d003bf44 | -10.9397 | -43.0593 | 2026-07-04 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| ddf43d7b-0705-310c-98a1-9ec0df7fbb85 | -10.9209 | -43.0384 | 2026-07-04 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| edfc03ed-3304-355d-9041-d5eab384d338 | -12.7553 | -44.5194 | 2026-07-04 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| c5777f17-5140-383b-a37b-afb89a48d7ef | -13.2592 | -54.3489 | 2026-07-04 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ab06cdf8-5110-3e73-8255-1c8c6394fb0a | -13.2401 | -54.351 | 2026-07-04 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 1077d731-9aa5-379e-8427-75d3a837dc26 | -10.9397 | -43.0593 | 2026-07-04 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 26ddf443-baa8-3a1c-9789-5ff3deaaddb1 | -13.2404 | -54.3303 | 2026-07-04 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 65adc640-b5d8-36fe-a342-310d4674d94f | -13.2595 | -54.3283 | 2026-07-04 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |


[Clique aqui para ver as próximas entradas](README12.md)
