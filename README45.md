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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7eed1a6-2c4b-3783-9c97-45c9d89914ec | -14.4287 | -47.33701 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2a91595-6a09-342c-9b97-e42463be9d18 | -12.68245 | -54.7067 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7b8eea14-348a-3cab-b195-07a6288199a3 | -14.3602 | -52.94024 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99829899-32f6-3ff0-a954-6a2b41997b79 | -15.78037 | -52.22276 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22719e90-1ea3-3ef7-a3f0-d263fd42e6cd | -14.62543 | -52.0365 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00970b84-f1ac-3a94-8221-a76410a6ce9c | -12.6817 | -54.71113 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f99a11d-0936-3b9a-a2b9-c8dc0f15667c | -15.5914 | -54.74273 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce00afad-50c5-3603-863d-a40880464865 | -16.15264 | -49.94313 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c549308-5099-3977-9cda-5c28ec7f71fd | -14.36052 | -52.95941 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37f12bd4-0344-3545-ac67-fb41af1e249d | -14.39198 | -52.91526 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 609d9ad0-9ccd-3f7c-9459-86bf03206665 | -15.1833 | -52.3168 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b8bafd1-7821-3735-afe6-4d4394c7c95c | -12.66642 | -54.66742 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d74ac6d1-ef72-3617-9221-1bb206b2227b | -14.48141 | -53.93062 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0847cd4-1bbd-3ed9-aeb5-22aa2aa05a76 | -15.22487 | -52.82261 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2bfed73-a09c-3f09-ab0c-587559b6f74b | -12.91862 | -54.80074 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2287bf1-5852-3e0c-99e3-e78c4c29a0c2 | -16.86662 | -49.35843 | 2025-09-14 04:42:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c6c7b5f-cd90-39de-a75d-7c093d5973da | -17.99993 | -46.96836 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 742b75c6-0763-309f-920e-95ae2afc6ae3 | -14.42805 | -47.33971 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b486758b-c700-3c23-a279-292cffdc4ab2 | -17.14715 | -53.88891 | 2025-09-14 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49c6a399-e038-38b6-9eb0-292898f90367 | -15.19638 | -52.48932 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7690457e-973e-3a07-82c6-9c8883d178f1 | -14.60322 | -46.33063 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a517df8-535f-30fb-afea-971a22662253 | -12.70019 | -54.69166 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 3d42211e-7b38-3a57-8ece-3a8e51ff0a91 | -13.88859 | -48.24419 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 261381fe-3bc0-3a69-a127-1e282551ced6 | -16.83591 | -40.84498 | 2025-09-14 04:42:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 75819635-97f3-3448-a2df-f24f09328819 | -15.4292 | -58.77987 | 2025-09-14 04:42:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18b0f909-260a-34d8-b0e4-4864875babef | -17.43843 | -49.22127 | 2025-09-14 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa3bbb38-9dbd-3a1f-9cbd-9279d0e6319c | -12.70237 | -54.70119 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6acb45fb-5292-36f8-aa20-722b93d6803b | -12.66198 | -54.67119 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a26eb8bc-46bd-3228-8ec7-db9bab89f66c | -17.14846 | -48.51142 | 2025-09-14 04:42:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95340827-2812-388f-911a-782e459794af | -15.7527 | -49.78077 | 2025-09-14 04:42:00 | NOAA-21 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2b0280a-0681-396e-b6d9-458f347962b3 | -16.33554 | -51.52409 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63b5b0c6-9ce4-3972-a727-299b29ef63c0 | -15.60741 | -47.94622 | 2025-09-14 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 558ec9dd-171a-3d2e-bc55-aea813a12ef9 | -18.14704 | -49.19223 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d0c4bbc7-b912-31fe-9867-88e9bd0a51f2 | -15.57837 | -48.6843 | 2025-09-14 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6df156c-0965-3d27-8768-b9bff9c76f66 | -15.20301 | -52.49049 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| debd9604-16db-3d4e-a93c-1c975bdd1c8c | -14.95886 | -55.95139 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceadfce3-8cdb-3cc8-89e5-85be320760b2 | -14.20441 | -46.17648 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2518824a-f11d-3882-bc3e-5841d4d6d422 | -18.09303 | -42.93504 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| c7d6f418-7190-3b0f-a448-19ad51961d84 | -13.26648 | -51.679 | 2025-09-14 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d6a8f66-8bc0-326e-82b2-40e9f90f6072 | -15.59209 | -54.73867 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9608b0f-4ccc-3d75-8c10-9a6e645949bf | -12.6884 | -54.69408 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| fc46fbd6-e278-3016-b811-7e6e0c3c8258 | -15.67288 | -50.6141 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82daccb0-9efc-3fdb-abd2-e6a0e5a57abe | -15.41143 | -52.97435 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 920b41b4-8e28-3399-80ea-7e523000b04e | -15.76812 | -53.48335 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7dd0292-5612-3b7a-8b69-91e50f631c3d | -17.15212 | -48.51197 | 2025-09-14 04:42:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e57a0e8-4b58-32c9-97df-cbfbd241a1d2 | -16.70794 | -54.9568 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9d1e38f-69c3-3278-ad77-eb6ea7fa4552 | -15.17638 | -52.46708 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42b4b60c-bcd3-3911-8072-5f82013aaf34 | -14.48214 | -47.3405 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 347bcbed-24e7-372d-ab30-5f363fbee605 | -17.43547 | -49.21655 | 2025-09-14 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1627765-9933-3a2f-a193-96fbb498b2d7 | -14.40388 | -52.90591 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dd76613-4110-3e1e-a1c3-b530a6f012c2 | -16.65638 | -49.77957 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cad41407-b8dc-36a0-82e9-8358fe74c22b | -16.5822 | -55.16322 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2a28c0b3-0583-34b6-b584-254c1351bc18 | -15.92731 | -49.97512 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5271e383-feea-320c-99e4-6727c1d9c539 | -14.1579 | -46.24854 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 506e3792-02c5-37c7-a6ca-a957540ffda8 | -17.45026 | -49.24014 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54d90a33-e0ee-3e42-8492-9d174b37cc44 | -12.69208 | -54.69474 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e9118f41-7c36-3825-9537-b2f01a12a380 | -12.9329 | -54.73868 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c7d58165-e8df-3b6f-9af6-96790f02ccea | -12.45545 | -57.78888 | 2025-09-14 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a981644d-cb30-3272-971b-de09327e20ec | -12.93733 | -54.73489 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6dda8564-bf13-3d15-b5c3-05d92a22b8bf | -19.25922 | -51.42868 | 2025-09-14 04:42:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d347d51-162a-3595-9f5d-2e810cd1b4c2 | -17.98969 | -46.95193 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffa069cd-5c3a-3666-b862-afab4e9b0cd3 | -17.99325 | -46.95633 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee8cb9db-725e-34fe-85ea-c5533da54686 | -19.14772 | -44.84141 | 2025-09-14 04:42:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b976b4e-b84a-371b-9a3f-8e54c9f90cf5 | -18.14289 | -49.19572 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ae002b50-50bb-3279-80b3-8c10dd095825 | -15.77375 | -52.22165 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57bb3561-e84b-3f74-9eef-90dc08a8c1e1 | -14.62288 | -46.36739 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 310eeae3-5414-38a5-b232-6c09e82aa475 | -17.25905 | -49.264 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15e0a291-f467-35c1-9c39-224ca6875736 | -17.59193 | -42.73508 | 2025-09-14 04:42:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 062f5015-6194-3e97-9cfc-d10b8b08193c | -15.76258 | -52.24916 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| efd801ad-06ef-31cb-b0c0-0c8076b5411e | -15.76472 | -53.48278 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a64c8c8a-639b-3aea-9f7d-52dab1bb559c | -12.68622 | -54.6846 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8057a6f6-e5a1-3f39-bb6f-3b0ab9b0f36a | -18.00893 | -46.96259 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 005b3754-c995-396c-b58f-8ca0cc708082 | -15.08648 | -52.47417 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ea7d36c-9a9e-3148-9eaf-3c644c6b0489 | -18.15832 | -49.18995 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5bf08eaf-88d1-390d-a7c3-656a9080fae9 | -13.91236 | -48.30759 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 161fca86-7a42-3595-926e-11cf8f6f936a | -15.76875 | -52.23178 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9215311-1c84-3d10-b93b-b50f74b1a2f9 | -12.67745 | -54.66939 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 60216d68-bfb9-3b7e-8ae7-aec16d2ba279 | -12.69058 | -54.70358 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 37d8ca6c-80c3-345f-89f9-ba8dc8460f63 | -16.09234 | -49.96945 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2da43614-4035-3be3-99bb-4790dd5dc0c4 | -18.15657 | -49.20228 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| dea6569a-f183-3fda-962f-d90752b1ae69 | -15.67122 | -52.24509 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1b36998-8d01-31a6-b539-13dc6538e5b8 | -16.33279 | -51.51996 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e672d3e4-1c87-3454-85e2-d3cd2289d0d2 | -16.86254 | -49.36202 | 2025-09-14 04:42:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e75d4324-14ad-31da-aafd-a9949b52bcc0 | -14.02747 | -49.20045 | 2025-09-14 04:42:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e877087a-ad8c-3730-9402-7e23d40826e2 | -18.00801 | -46.96964 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d58ea0-bff3-31bc-bfb5-cddb7eed2c9c | -18.19895 | -47.91767 | 2025-09-14 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51141471-3373-3d59-9689-0bf8c096b280 | -15.69165 | -54.34613 | 2025-09-14 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39228e89-e9a7-3a77-b5e4-35428fc360dd | -18.01845 | -46.95274 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86c34869-060b-3535-a089-e6e27695d716 | -13.88265 | -48.28608 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d914e9a7-ff3b-39ea-bec9-6c2c17142c1c | -12.68982 | -54.70803 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d439f90b-2f88-37f0-99c0-d3b0c9e9e292 | -15.16584 | -52.46898 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0c9eb17-fa4b-32e0-8a9d-8d153ca0632d | -14.50259 | -53.88914 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e604b4b-7242-3618-a002-45a9563a84c9 | -15.69906 | -47.02028 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77acf8ed-af6b-3a77-b4d3-8550ed076e7b | -16.65751 | -49.77192 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4e73ffe-5cd5-3173-884a-e018ce65fd5d | -16.50044 | -55.16483 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 110257d4-e6b3-3b0e-a1a3-5ffe26731259 | -18.02057 | -46.96813 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8631dc9-b1cc-3acd-8166-59e16b71e9bd | -15.86654 | -51.84883 | 2025-09-14 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0041cff5-a317-3ee5-9267-d721552154a6 | -16.50279 | -42.12583 | 2025-09-14 04:42:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f3a117d8-e4d2-3cd8-ae80-0d92196311a3 | -14.62691 | -46.36787 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21434984-a47e-3a42-91db-da2a03e7ee55 | -18.02101 | -46.96474 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README46.md)
