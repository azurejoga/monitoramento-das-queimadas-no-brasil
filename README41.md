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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be660a3a-14e1-3751-8749-2a53f6658ae0 | -7.4638 | -46.06295 | 2024-10-06 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44ba7e60-a0b5-32a7-9bee-5f6cd1845b9a | -5.81653 | -44.13324 | 2024-10-06 03:30:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d57e854d-5c27-3d6e-bf14-aa664e198a90 | -5.81753 | -44.12783 | 2024-10-06 03:30:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bb86a78b-931e-3879-838c-04c858e2985c | -5.82301 | -44.13432 | 2024-10-06 03:30:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2b61da85-65bf-3566-a068-36aeed31b40c | -5.824 | -44.12894 | 2024-10-06 03:30:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 779b87f9-ef2d-3fc4-a0a8-c1e9b18eb5c9 | -6.34164 | -45.71135 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dd5a1916-7ed3-3a5a-8590-64f4305ad67b | -8.76742 | -40.58417 | 2024-10-06 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 11c8733a-add6-3bfc-94c0-6cfac514aecc | -8.49387 | -40.58034 | 2024-10-06 03:30:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6efe31b5-5126-31dd-b2aa-2f7905766b4a | -8.48469 | -40.69591 | 2024-10-06 03:30:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6dad8f4-545f-33e9-b1aa-f0e548b908c1 | -8.41345 | -40.46289 | 2024-10-06 03:30:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07c653a0-bf96-32bd-b01d-6dd7cbcc72fe | -8.41125 | -40.46087 | 2024-10-06 03:30:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87413d09-3798-3137-9ddd-1924a5fac897 | -5.56951 | -44.8826 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5b4d49ce-fbd7-3961-97b4-3cd06f835a19 | -8.33659 | -40.62621 | 2024-10-06 03:30:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 450c3941-c8d3-3486-ac4b-314c4b02e6f7 | -8.20563 | -40.72558 | 2024-10-06 03:30:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6289954d-5ff5-30da-b075-0a19ab67eb44 | -8.20062 | -40.72477 | 2024-10-06 03:30:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db610cd7-3fc3-3b24-bd4f-bb133a27cd6c | -8.19269 | -43.73152 | 2024-10-06 03:30:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75c2e2e1-b008-3f33-8560-750a0d1d0965 | -8.18752 | -43.72558 | 2024-10-06 03:30:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3bfd1979-acc3-3697-96b6-eb05773ebbec | -8.18145 | -43.72444 | 2024-10-06 03:30:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ef13f81-ec2f-367e-ab97-d9c9f2e04d1e | -8.15431 | -44.40475 | 2024-10-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c474836c-70a2-3f25-9efe-c1a5f0c22164 | -8.15331 | -44.41005 | 2024-10-06 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9e36c59-4913-37c6-bc07-6448268138d9 | -8.07357 | -34.97743 | 2024-10-06 03:30:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3c31cfd-855b-3787-8b5d-f311214c9842 | -8.0333 | -35.37859 | 2024-10-06 03:30:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 44e1a314-436d-3c80-b0bc-1ecb6c5ee8ce | -8.00253 | -40.59122 | 2024-10-06 03:30:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 61388b1a-1ddd-3afd-8fce-92c76d41ec11 | -7.76964 | -43.07577 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 54604cbc-4ff1-37b3-a6b3-4ad455b8aa63 | -7.76879 | -43.08037 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85cfe31f-6fbe-38c8-a0a4-cb00c966d96d | -7.74438 | -43.04836 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 13adb006-53af-3c97-abf2-d3734e8252cc | -7.74358 | -43.05266 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d0de3a81-1dde-3ffb-aefb-f29dd643d410 | -7.74154 | -37.97416 | 2024-10-06 03:30:00 | NOAA-21 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 787e899c-cc11-337b-8563-614142832694 | -7.74034 | -37.97359 | 2024-10-06 03:30:00 | NOAA-21 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 813bb835-61e1-33b6-a38d-1d8cf81f0f3c | -7.73771 | -43.05164 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dd565460-c1f2-3ca3-9de3-62a128b21ea3 | -7.7369 | -43.05598 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cfaea246-826c-31bb-a8bb-2be8b5654684 | -7.73608 | -43.06039 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d1e7dc13-9e79-3931-90dd-12cbbaf8de25 | -7.73521 | -43.06502 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 705c3cfe-a316-3afb-bb16-2162546c6400 | -7.73431 | -43.06983 | 2024-10-06 03:30:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ce7d8338-3d03-34a4-82cb-d8dd7bbc9c81 | -7.69821 | -42.97621 | 2024-10-06 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| b5add0a1-0274-35f0-a747-9095933880f9 | -7.69747 | -42.98031 | 2024-10-06 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 7428b44e-5513-3441-b156-3f7a62c43715 | -7.6967 | -42.98452 | 2024-10-06 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a3afbcb0-467e-3caf-af67-13e0859f382a | -7.69085 | -42.98347 | 2024-10-06 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e5960206-4d25-37e9-957d-28672ac87cc4 | -7.69007 | -42.98774 | 2024-10-06 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 93208c5c-d056-3d45-9403-0750cf0ce63f | -7.63933 | -42.41798 | 2024-10-06 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2aee02c-c6fa-3ba4-926e-e68d0a7c2bbe | -7.63781 | -42.48977 | 2024-10-06 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 55b7e0be-aac0-30db-885e-4953b8123f84 | -7.63709 | -42.49368 | 2024-10-06 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9b74b412-1488-324e-b76f-8975c70b690d | -7.63637 | -42.49762 | 2024-10-06 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a62246e9-5800-3978-b84e-d845b452fa93 | -7.63564 | -42.50157 | 2024-10-06 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b3ae121c-fbe8-3d7a-8c35-80d9706bd37f | -7.63297 | -42.42081 | 2024-10-06 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 451565f3-7232-3512-a7a6-bd4ac11b95d4 | -7.63069 | -42.49665 | 2024-10-06 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 48c62d59-5547-34eb-b39b-f73a70291a98 | -7.61768 | -42.4571 | 2024-10-06 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f7bf8b66-5f82-3d6c-a347-8a6d66dddff8 | -7.61517 | -42.4539 | 2024-10-06 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1916d7bb-1f7a-34be-bdbb-589870dc3ea3 | -7.54319 | -35.22384 | 2024-10-06 03:30:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b9c3997-d1a2-32c5-ac1d-3b514aa06091 | -7.50346 | -37.31396 | 2024-10-06 03:30:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da4cb3b7-ffe8-389d-83b0-a62ee3a6d7fb | -7.47773 | -34.84345 | 2024-10-06 03:30:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af664d6c-418f-3037-8857-7e2311ef16c8 | -7.47738 | -40.18321 | 2024-10-06 03:30:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f8e9fd9-c8b5-3bce-8487-9f4d335b7b72 | -7.47508 | -40.18082 | 2024-10-06 03:30:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e32238a4-d8e4-3dc7-b925-5fc301a1ad90 | -7.36816 | -39.17847 | 2024-10-06 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d228f76e-54a5-3093-8ea2-0ea6a46281bf | -7.3507 | -41.9449 | 2024-10-06 03:30:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 80588500-0cad-3275-a69e-f1f4ba40c2f4 | -7.34781 | -39.16046 | 2024-10-06 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7713762c-1fe6-3dcc-8480-5631b99803f1 | -7.34697 | -39.1652 | 2024-10-06 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cdc539d6-0710-3ce5-a770-74bbd35d2eab | -7.34322 | -39.15979 | 2024-10-06 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9135fc9f-a0b6-3297-8794-4e974cb43e73 | -7.24261 | -38.54372 | 2024-10-06 03:30:00 | NOAA-21 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5a9cfeb4-15e2-3bba-9210-47a67164ae6e | -7.23894 | -38.5389 | 2024-10-06 03:30:00 | NOAA-21 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 31d32124-495b-36a9-9b4a-1cbad73af2af | -16.29405 | -43.69388 | 2024-10-06 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b4ef208-3907-365c-b26e-0f5d1f120c01 | -15.38885 | -47.41335 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 30828fd6-9b4a-32e8-ba53-c03f0b5bd569 | -15.18699 | -47.50694 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 68585fb0-4d68-3c00-bf09-3dc6e4d6f03d | -15.18592 | -47.51176 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf52b834-10e6-31a8-bf59-fa9e3f2b27b2 | -15.16162 | -48.04101 | 2024-10-06 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d4127ba-55db-3fc2-8112-cdfd042c55ea | -15.15308 | -48.04668 | 2024-10-06 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 706a2d4a-d404-33ae-ac40-4af20daa7e80 | -15.12545 | -47.08577 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 272d8d25-d802-3989-8a15-257a88af6cd4 | -15.12345 | -47.08619 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f7271af4-1270-31cf-a825-1cc9b2016cb8 | -15.11757 | -47.0904 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d05bf12-0d2b-3d10-a3f7-0aa38233e099 | -15.1155 | -47.09096 | 2024-10-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f7020c5-0d4c-38a2-b00d-f84cf2735de6 | -15.05683 | -44.11584 | 2024-10-06 03:32:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d84b2d0-88ac-3435-8ff8-8d15f6bbfd6f | -15.05132 | -44.11467 | 2024-10-06 03:32:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c2d409d-c51a-3a26-9bb7-3a41336f751f | -14.70439 | -45.12967 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc0a8e2c-4749-36d6-a25b-bf3f1fd7a7ee | -14.70343 | -45.13423 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b16dc74c-a7db-3cbc-b1ea-a4ef65faeddf | -14.69855 | -45.12811 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc64be10-5663-3314-90bf-9a7dc85d9822 | -14.69756 | -45.13284 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d1f7ee0-8ac6-3ed2-af27-f5a802f96b2a | -14.69657 | -45.13757 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b13ed280-3540-312d-8640-5d41c93a08e2 | -14.65895 | -41.96277 | 2024-10-06 03:32:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e920761a-4c79-32f7-ba13-f593f9ce84f2 | -14.4874 | -44.96236 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1bc07c0-54d3-3bc8-b233-c9e60c27c5a1 | -14.48604 | -44.96041 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3212fa4-634a-34fc-a9c7-f91df5da21cc | -14.48513 | -44.96474 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68d688b2-c894-30cd-b666-4b5928718e26 | -14.42606 | -43.78658 | 2024-10-06 03:32:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04436d7d-52dc-38bb-b8e3-4f482b05918e | -14.29766 | -44.64988 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cb13e7d-f4f6-3870-a5a2-4860fc9a11a9 | -14.29678 | -44.65421 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5724e4db-eec8-362d-b90f-a234b4ad6481 | -14.12027 | -41.67936 | 2024-10-06 03:32:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94241c59-1b1b-3b5d-8441-c7a8a8bca4ff | -14.08604 | -45.49497 | 2024-10-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f92a32d-8c16-33d8-adfb-9dbee027cd1e | -14.08501 | -45.49989 | 2024-10-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52552628-cc7a-3179-b6ca-7ee5a93d7bb9 | -14.08095 | -45.48888 | 2024-10-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d771351d-940d-361c-966f-c6c384215977 | -14.08018 | -44.47658 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49426269-3d42-3909-b8f8-6a7e518896e2 | -14.07934 | -44.48069 | 2024-10-06 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92d347e4-f4e5-339c-ae59-957ea2f41c9f | -13.89736 | -44.60559 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a30ee2a-3705-3d08-8c80-9925bef70782 | -13.8973 | -44.60423 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 329ef15a-dda7-3593-8b9a-841794b2295e | -13.8965 | -44.60988 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a21ec35-2f16-3adb-88f6-0f1ed8765e7e | -13.89641 | -44.6085 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 511c1bec-a0d7-38f9-9515-17b222a5be9d | -13.89563 | -44.61421 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46788456-4213-32a1-abb6-0ac14bb86ae1 | -13.89552 | -44.61281 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a49f2856-191b-3ede-a07c-3c44ac577637 | -13.89329 | -44.59575 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35d1e3ad-b463-321a-98e4-cc4e8b4c89e9 | -13.89243 | -44.60006 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4220314-2ed8-32ef-821d-25057f0c5502 | -13.8924 | -44.59872 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34fe05cb-20fc-3209-a133-9130933c7eab | -13.89155 | -44.60439 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README42.md)
