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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da86aec9-81c6-31b8-9423-cd9a754cd866 | -9.5339 | -40.3531 | 2025-07-31 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 131.9 |
| 65a14644-40d8-3c7b-9497-f5050a1ea859 | -9.5147 | -40.3558 | 2025-07-31 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 177.0 |
| ea2b5990-8a5d-302a-ad00-e0125ffa8fb7 | -9.5343 | -40.3282 | 2025-07-31 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 52e45fda-9b50-332c-8d8b-914dc622bb87 | -6.5258 | -56.2121 | 2025-07-31 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 608a0c3d-4e60-3706-ae66-4e76696a84a0 | -6.526 | -56.1923 | 2025-07-31 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2e323061-3723-390c-a88a-239fef76eb15 | -9.5152 | -40.331 | 2025-07-31 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 3d33a227-7792-3e22-b3e5-2474e9c136e4 | -6.6725 | -56.4029 | 2025-07-31 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 7f18ca0e-54d0-3505-acf5-344164282d4e | -6.526 | -56.1923 | 2025-07-31 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f6f0911e-e58d-35d5-a6ce-a00077b195bc | -6.5075 | -56.1932 | 2025-07-31 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 8bc959bb-6acf-3748-b64f-2a5a2a7936c2 | -12.6317 | -48.0869 | 2025-07-31 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0d3a67e9-d79f-3380-98b0-f6f1d8d78349 | -15.8955 | -43.4523 | 2025-07-31 03:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f4bf2f24-5813-3754-a71e-17148a9859e6 | -6.5075 | -56.1932 | 2025-07-31 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3c621d8e-1231-34ec-936e-c9028beb186c | -10.0843 | -53.8712 | 2025-07-31 03:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5809f206-4fa8-3302-9588-26c7e670264a | -6.6725 | -56.4029 | 2025-07-31 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 77a7ca44-84a5-3bcd-80e7-9e68344d0a19 | -6.526 | -56.1923 | 2025-07-31 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 30102b46-8a86-3804-a0cc-1f684a171e86 | -6.5258 | -56.2121 | 2025-07-31 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 07e9fc87-66ea-3857-943d-2680bb7354fd | -6.526 | -56.1923 | 2025-07-31 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f68446b9-f320-3435-a8a6-955bf88bb454 | -8.0513 | -43.1001 | 2025-07-31 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| e252db27-7ba5-3e95-be46-0c82c2c90c24 | -6.6725 | -56.4029 | 2025-07-31 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ad2eec2c-1ab7-399e-8ad0-2043540065be | -6.5258 | -56.2121 | 2025-07-31 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 295e7454-2869-39f0-ae0a-ee2efe129a43 | -12.6317 | -48.0869 | 2025-07-31 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e9baa172-1fed-3421-bb27-ad6b98724761 | -4.19541 | -38.365 | 2025-07-31 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d20e7d9d-62cb-3784-8cf8-2327211abad1 | -6.23265 | -37.42768 | 2025-07-31 03:42:00 | NOAA-21 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 93f04b15-5873-3777-8b73-dd9cc40b17eb | -5.07092 | -37.71791 | 2025-07-31 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ea8a5687-f809-30b6-bb4e-39633ded1b11 | -6.46227 | -44.56979 | 2025-07-31 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2d448ac-4dfa-3abf-b781-b17305344e8a | -6.64531 | -35.4818 | 2025-07-31 03:42:00 | NOAA-21 | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4cda9a12-b5bb-36e7-98a3-adea7ef792ce | -4.19174 | -38.36442 | 2025-07-31 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c2e3202-05f6-3dfb-8c48-19612be3b180 | -11.54165 | -44.24311 | 2025-07-31 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c5d0872-b24a-38bf-bde6-529e9760199c | -9.39312 | -45.49878 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 14bf53f6-cbe5-36c9-afe2-59904f93dc29 | -9.59119 | -43.84742 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7e648a0-355c-3da9-806e-27c05b745e85 | -12.48686 | -44.75922 | 2025-07-31 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6666b13-dc6d-3f67-af4a-7902ad75292f | -10.6484 | -45.23558 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9cdfca1a-e417-38ec-9647-8757399a32c6 | -8.87797 | -44.79325 | 2025-07-31 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 13676178-d69f-355b-bb5b-a9742c2a5940 | -10.6364 | -45.23592 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f019d0f-ad0b-3824-8991-519bcf7076c4 | -9.3972 | -45.48941 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3677b994-bed3-37de-ba0e-319f537a58e4 | -10.63801 | -45.23381 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b23ad05-50c3-34f3-963e-3552284c0203 | -10.64678 | -45.23774 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c237ef39-8b17-3296-a2a1-0d44542cd218 | -14.3912 | -44.37453 | 2025-07-31 03:45:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59706761-6bb7-3582-9128-95ed0b49801e | -13.36874 | -44.77544 | 2025-07-31 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4592942-da0b-324e-9b67-fda9f1784f66 | -11.54444 | -44.28182 | 2025-07-31 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0be834ac-73fd-3a7c-8e7f-de7f15c8aeab | -7.48743 | -43.93577 | 2025-07-31 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43bda0b5-92e3-39f6-aa64-b8b9af4454b7 | -11.96079 | -46.68061 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d91edcbd-41d9-3869-abe0-be52dd4f1dab | -10.21284 | -48.21839 | 2025-07-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b88b879-3a9c-306c-9003-0dfe5015319a | -12.15401 | -44.6182 | 2025-07-31 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 786151f9-61dd-322f-87d6-dc4771e86b63 | -10.22589 | -47.9895 | 2025-07-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6aac953e-63b4-3060-be1a-faa6f28976f5 | -8.958 | -46.751 | 2025-07-31 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44ae97ab-29a5-3516-977a-b67172dd9bf5 | -9.39376 | -45.49529 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3a50edbc-563d-3fd3-bf62-b37a91ebdc06 | -12.63049 | -48.09663 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e3dc96d7-8fc9-351d-87a6-9ea153494ed9 | -7.58655 | -44.80949 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d52733b8-1029-3429-81ba-79350634b16d | -9.64009 | -43.84766 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| db8b86ae-82d0-3af7-aee3-f26a7b00cda9 | -9.5709 | -43.87782 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5d79b33d-73af-37fb-8b21-7736e700248e | -10.5249 | -42.54708 | 2025-07-31 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 02148980-2b3c-3feb-95d3-c95152aaa5d3 | -7.59286 | -44.81353 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1138b24-f6fd-32a3-bcc5-9558bae7cf20 | -10.9306 | -44.50385 | 2025-07-31 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0644097-4d99-365e-a436-be409b1b8f95 | -10.61911 | -45.2425 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67898a5f-44a3-30e9-bb2f-5cbb846e162b | -13.54424 | -44.14737 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfefae0a-91b4-37bf-926c-0751ec348f8f | -7.12949 | -44.89921 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92a7eb46-3d66-346b-ba83-1ceebc06ce89 | -9.22337 | -48.59664 | 2025-07-31 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf75e427-5271-3c2b-980b-bc4461d16372 | -7.12568 | -44.90302 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f29a96a-5cb5-332c-bf80-41d6733dc7f4 | -10.61971 | -45.23924 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 389f34d0-69fb-3993-80c7-2854d2a7c720 | -9.64387 | -43.85416 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 389388f6-5a8f-3156-ab32-64ab5be5d7d3 | -8.95297 | -46.74551 | 2025-07-31 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398ad936-f2ac-361a-aa53-9641809bc00e | -10.62075 | -45.26273 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 756b75fe-d0d4-3db2-8570-3e0eeb8be04c | -9.59596 | -43.84467 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 160c6960-1adf-3a3c-805d-80b4ca82264b | -10.63697 | -45.2328 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b86f5dbc-e616-3efd-a25c-67f80646be5d | -10.64274 | -45.23054 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff95cb9d-1ad7-3717-b472-107673161876 | -12.62348 | -48.10047 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e188a41a-5fa1-3c96-8f2a-ebb8e59f2778 | -13.51174 | -45.64605 | 2025-07-31 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a2a1179-7e0e-372f-8964-9753cd5fad1d | -7.12405 | -44.89855 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc812b59-7909-3d59-8510-60ef1c1ba1b2 | -13.50614 | -45.64789 | 2025-07-31 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa00ea83-6a1c-3681-ad38-d13b82654c83 | -7.59341 | -44.81034 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93109e0a-a736-342e-b117-5c18247b6e5c | -7.12347 | -44.90191 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 416e248f-7c27-35d2-9b63-cc47d8b88702 | -10.60566 | -43.31103 | 2025-07-31 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c00fca76-c620-3d27-98be-22899bd3f836 | -12.76485 | -44.41425 | 2025-07-31 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6ca1db01-c4b2-3ad5-b46f-4cdc78175c14 | -8.88238 | -44.79287 | 2025-07-31 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ad6f320-2cd3-3a1d-91e5-dc00bbe27bc2 | -7.48693 | -43.93863 | 2025-07-31 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c3ab6c3-92e5-3060-87fb-68b96fa83143 | -10.22684 | -47.98471 | 2025-07-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d194ef3-5267-38a3-a4bb-0b3aac8807ab | -11.7486 | -48.18429 | 2025-07-31 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 76af9d18-8842-3943-a7bf-6b7ff5eeb5d0 | -7.57883 | -44.82175 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ae82af2f-45b6-3c9c-91fb-42bb279c6f9f | -12.62662 | -48.08497 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b1d3a48-ceee-3dfc-95f2-a148d16c6056 | -9.22992 | -48.59787 | 2025-07-31 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 176717c5-e932-3598-a0f1-bba46ac32e5e | -7.33083 | -44.67104 | 2025-07-31 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2824765f-1222-3022-8518-aa54494ef2c1 | -11.54068 | -44.24837 | 2025-07-31 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 448d1062-07aa-3458-aa9d-8a3202581b9e | -11.98867 | -46.67904 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7013cc6-6ee4-35ac-8553-ad0a389b03d8 | -10.61272 | -45.24809 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8706ada-721d-35ed-9603-5ebc0e1c2dcf | -8.87716 | -44.79211 | 2025-07-31 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81b51610-f38e-3be5-9a06-30fa89793853 | -7.58536 | -44.81601 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e50b5050-657c-3da2-8d15-91739a8ea6a9 | -12.55818 | -44.727 | 2025-07-31 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26c3dea9-0fcc-3af2-96fa-d994ed118600 | -10.61036 | -45.26084 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b326d8-fb0c-3641-8c17-165dca0e4292 | -10.2282 | -47.98738 | 2025-07-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c21fbae0-e238-392b-a601-33917d31b394 | -8.17168 | -45.01881 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f90403de-accd-3580-a857-9b0ac471cfb0 | -11.96629 | -46.68198 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd0ccbb9-31ba-3f70-8efc-4afdb67e3d0f | -10.61331 | -45.24487 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64940a25-0955-3ecf-b922-81bc21901e9d | -12.22695 | -43.9825 | 2025-07-31 03:45:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dc9f754-6efc-3cb9-9c93-7d0b6faf0f2f | -10.64159 | -45.23684 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36a87dcd-dcf3-344a-ab88-79ba2dae0f3f | -8.0557 | -43.10748 | 2025-07-31 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 6ab7699f-9b54-39a1-bd6b-92efbaeb2c01 | -10.60812 | -45.24391 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b98d775-1219-301a-b744-535aebf17322 | -7.58643 | -44.81898 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41ae3a74-328d-33fa-9b6b-7a313862cbc1 | -7.3314 | -44.66788 | 2025-07-31 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2e848c2-b2ed-38ef-91d6-f9efadf6a905 | -10.10444 | -43.95415 | 2025-07-31 03:45:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
