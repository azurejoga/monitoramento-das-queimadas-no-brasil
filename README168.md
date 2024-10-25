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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3e21a67-3c84-34f5-a8ed-64f9a331c6b4 | -7.4942 | -42.9223 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6947004b-1e1e-3538-bd63-49bf535d82e7 | -7.45136 | -43.02311 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f2a20cbe-7e4a-34c1-86cf-d0371b3a8b0a | -7.42732 | -42.31993 | 2024-10-25 16:52:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 2b56b086-3514-3e93-a689-910e6a70c360 | -7.42536 | -42.90103 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c6c85ac6-8ea4-3296-a5bf-61b5154f82bf | -7.42361 | -42.89091 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 14539a2d-6d1a-39e2-a284-f073bf4bfe18 | -7.37157 | -43.04975 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 114cc237-5c47-3766-a662-dbcc92ce3a9f | -7.32018 | -42.5484 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| c2c36ca9-2e88-36b1-8472-78c09685085f | -7.31982 | -42.55165 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| c4d6dfbd-3d65-3e8f-8c38-582d665cdf84 | -7.31887 | -42.5463 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 274d6f28-9960-3c05-bace-def92bc73d8e | -7.30735 | -42.92888 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 6f25860a-8d53-3e57-a9c3-93d90f3282df | -7.25565 | -42.54851 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 0b07298f-5f1e-30bd-b417-940a3f7d2f4c | -7.18868 | -42.90701 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 137244e1-de58-36b5-8fb5-919e120df707 | -7.18783 | -42.90189 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| c5e3a472-c6ee-3081-84d3-072522337b7d | -7.18496 | -42.90472 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d5b51e87-4eee-3d6a-8709-03071566936d | -7.18407 | -42.89963 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 344a7f38-eb9c-3f4b-8089-c7935a41da6b | -7.14457 | -43.07385 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 768e82b5-e483-33ef-a3f8-47747c6e94ca | -7.01929 | -43.03215 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| f65a5bf6-e23b-3771-9718-1306aee55de2 | -6.92637 | -42.14132 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| add34a93-9eeb-3622-9589-a550fdc1db4c | -6.92138 | -42.14217 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 9d46707e-d4da-3f7a-915a-ac99f3be4658 | -6.90189 | -42.63437 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c08f8c6-82d3-34ef-8bda-0adedd890c52 | -6.9007 | -42.63366 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43fc4fe0-0477-3e17-af38-c5c8035e8102 | -6.86093 | -42.68506 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 6accfdd0-aef9-365d-bcf0-8919f379ef97 | -6.86003 | -42.67985 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| a6c244a8-de99-3929-8ebc-0dad346cd6e0 | -6.84645 | -43.28839 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee54288a-86fd-399a-a8a0-179eb7de7042 | -6.82546 | -43.27692 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d8250637-751c-3b2d-b148-1d0b77fad8a3 | -6.82165 | -43.28245 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9be87382-638c-37f2-a5bb-636029b69ab1 | -6.82082 | -43.27767 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 52f6e341-c796-39cd-87fc-35c08a2a59bb | -6.80604 | -42.79607 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 60a75f02-3b5b-3e62-8a0d-2ba89997bd3f | -6.80127 | -42.79698 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 8b795b16-3a7f-39a8-9b4e-3fde31546b35 | -6.76535 | -42.33773 | 2024-10-25 16:52:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 8d3d2a1b-be1c-3e57-beba-da889ce505e9 | -6.76419 | -42.34059 | 2024-10-25 16:52:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 03e30dc8-d8a4-3f73-85e1-fe4011d25f43 | -6.73673 | -42.32847 | 2024-10-25 16:52:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 78780d3b-c448-3fa5-8ef1-ca66b08bda58 | -6.71529 | -42.69404 | 2024-10-25 16:52:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 917b9c9a-32cd-3cb0-8398-50567d81ae58 | -6.71487 | -42.69709 | 2024-10-25 16:52:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 2d156dab-71c5-3aee-a320-c9650d30ad92 | -6.70811 | -42.09931 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| aa80704e-e27d-352e-85df-18c7f3c5c378 | -6.70796 | -42.09986 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c16bd7e9-55bb-3be3-ae3d-ba954379b665 | -6.65708 | -42.64374 | 2024-10-25 16:52:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| d7c11c3a-9413-3a7b-a963-80f502d8487d | -6.67646 | -43.04226 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0e649e25-fb8f-3e23-934b-3c6dcfe54dd6 | -6.67174 | -43.04303 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2a9cf95f-8ffe-3f4c-a4bd-3db7d0d38716 | -6.6703 | -43.04478 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9b958b9e-537b-3cc1-865e-7957d9ed95a3 | -6.6636 | -43.00437 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c61d4bfa-e743-37a8-bb72-fd160e4b2abc | -6.66001 | -43.00352 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b457509b-d0fa-368e-9f4d-b053c97fe9ff | -7.42558 | -43.70832 | 2024-10-25 16:52:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f2d44356-7b07-3975-87de-4cffd2de26b0 | -7.42397 | -43.70623 | 2024-10-25 16:52:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6839c09e-77f3-3413-87d3-3a9c35531b1e | -7.28591 | -43.65787 | 2024-10-25 16:52:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3b50104e-1ab9-3937-9e85-021b06197723 | -7.04884 | -43.36821 | 2024-10-25 16:52:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 0d752f1c-e82f-34b7-9e91-d5be55a69689 | -6.92902 | -43.38418 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dcaa9cbe-ffe2-3222-8569-00c3026312ae | -6.92868 | -43.38281 | 2024-10-25 16:52:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7e58e3db-5e97-3ac3-918d-0839f07ac321 | -7.58271 | -43.62541 | 2024-10-25 16:52:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d4d1bb91-dfdf-30a0-a481-dcd201c99199 | -7.43847 | -43.49618 | 2024-10-25 16:52:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b9789c7d-b47a-3c01-8a55-a1dd223b113f | -7.28666 | -43.66239 | 2024-10-25 16:52:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2f41f328-b4aa-31b5-94a2-e9531ed674a2 | -7.28143 | -43.65862 | 2024-10-25 16:52:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9c0f2f2b-929e-3bb5-8572-6e071d47af2c | -7.15236 | -43.5911 | 2024-10-25 16:52:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7bf0f536-70c2-3f39-aebf-b9b2ae9c53ff | -7.14853 | -43.56839 | 2024-10-25 16:52:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f5fd5c73-f7d7-3cad-91ac-c263fb29e0ea | -7.08055 | -43.64371 | 2024-10-25 16:52:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a66b591f-cbfe-348e-863e-e19bcaf68738 | -6.85935 | -43.50047 | 2024-10-25 16:52:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5aca06ef-c111-32ed-805f-ba6074a423e0 | -6.85854 | -43.49575 | 2024-10-25 16:52:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b6d22d2-99f6-324f-93c6-5e043e9a8588 | -6.79724 | -43.5524 | 2024-10-25 16:52:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4f152035-7a7b-33b5-a619-042ef6c592d3 | -6.79644 | -43.54768 | 2024-10-25 16:52:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f33d80d9-bec5-3ec7-be80-9e418610c6a4 | -6.79189 | -43.54841 | 2024-10-25 16:52:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f85d177-a92e-3100-ad98-45f239e2c3d7 | -6.6919 | -43.40379 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bbc7013-d68b-39ec-a9ac-ad8c3c876716 | -8.34715 | -43.94013 | 2024-10-25 16:52:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d2e5edfb-d8ba-3d3b-a3cd-16b91c142e56 | -8.34356 | -43.94499 | 2024-10-25 16:52:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a80af512-d733-313a-aa21-a6eb44480100 | -8.33972 | -42.81115 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0f008548-0a42-3ebe-a020-1e05d7834ecc | -8.33043 | -42.81283 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| dcfa6e7f-7fca-3af0-9b64-17773dd87c5b | -8.32958 | -42.8079 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fe166a66-1ae0-3f17-aa4b-2b06b8ea6b6d | -8.13946 | -42.79555 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 34339075-bcdf-39d9-b5ff-f95e7f7b7aa4 | -8.13769 | -42.79775 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5667fcbb-101f-3edd-91cd-481d21163c86 | -8.10412 | -43.14285 | 2024-10-25 16:52:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c3eeabb5-9bb2-38ab-8c7b-bfaa8132c013 | -8.09024 | -42.78935 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| d617c708-7ecd-3925-86c5-6838e9c05e51 | -8.02214 | -42.9953 | 2024-10-25 16:52:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 25efd10e-8852-33be-8b32-3e3bd185bfb5 | -3.25277 | -43.16213 | 2024-10-25 16:52:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d737bb6f-9af0-3d11-8672-d7d425f4a81c | -3.58701 | -43.69994 | 2024-10-25 16:52:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c3c3bfe0-bc6f-36cb-aa75-f95e27f0f0d3 | -3.58226 | -43.70067 | 2024-10-25 16:52:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3f504eaf-4165-3b05-b338-4581991e0f15 | -3.51941 | -43.61847 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6438ac58-123d-32b3-9f57-438df6406765 | -3.45471 | -43.95183 | 2024-10-25 16:52:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f7d50f3a-b7c0-3575-850c-ccf1c90fe681 | -4.80195 | -43.87901 | 2024-10-25 16:52:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| a7d88555-5594-3603-93f9-42ed1d4ce707 | -3.45297 | -43.95426 | 2024-10-25 16:52:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 72cab57d-e214-3e29-914f-046856d2fa1a | -3.30539 | -43.51125 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| baf8e0db-0f68-3225-9ac9-94f7b380c91a | -3.2537 | -43.16772 | 2024-10-25 16:52:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e28528b8-d5c0-3c31-a49e-8d43f0a63a64 | -3.25072 | -43.9533 | 2024-10-25 16:52:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 9abd367e-18c0-3665-86fa-f5b0e364f4ac | -2.96899 | -43.52934 | 2024-10-25 16:52:00 | NOAA-21 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ca409f1-65f3-3e2d-b601-ac052cbfe83b | -3.30267 | -44.09465 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 0d130539-bb57-3cd7-84a6-02d2aa919243 | -3.29804 | -44.0954 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 751510b2-0bc3-355d-9df3-b6ecfd367315 | -3.2324 | -44.21114 | 2024-10-25 16:52:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b057d4de-a99a-308d-a3f5-7ee368a97c3a | -3.12039 | -44.09963 | 2024-10-25 16:52:00 | NOAA-21 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9e9f9ec2-5427-3744-8d41-784c05cad470 | -2.87401 | -44.17892 | 2024-10-25 16:52:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 18dc986c-d84f-31fe-8d24-1d7fefade4c1 | -3.61116 | -43.15516 | 2024-10-25 16:52:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 47cf8d71-b3e4-3177-8c2b-bbf3019345b3 | -3.51448 | -43.06193 | 2024-10-25 16:52:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1a82be8d-dd05-3300-ba68-a611dc43e4db | -3.51384 | -43.06411 | 2024-10-25 16:52:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 84f1b526-4caf-34ff-ba51-5dd7623ea8a7 | -3.09241 | -42.87679 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2c1c069a-a4db-3533-a813-29ef7e9faec6 | -3.09192 | -42.87383 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b0e70c8c-aa54-3d59-bca5-6e81e1a0819a | -3.45074 | -44.42342 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e76e6c8c-155f-36bf-943b-a2e518b5e38e | -3.2896 | -44.32996 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 26672ea3-7ef1-3fab-9284-264f1170252a | -3.2894 | -44.33211 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 86de97dc-fc37-3c0b-b3d8-78687e310cf3 | -3.27498 | -44.32973 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4e6e60d3-423a-35d3-912b-021d7a8edf73 | -3.27423 | -44.32503 | 2024-10-25 16:52:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2f97a366-32fc-31f4-bc0b-03fbc245c3da | -5.0891 | -43.76459 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 752d2e24-ec08-356d-b8d5-1c144fcf0799 | -5.0873 | -43.72546 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 727124b0-4a58-3fd7-89cc-de643c123b34 | -5.0845 | -43.7654 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |


[Clique aqui para ver as próximas entradas](README169.md)
