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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 460542df-996b-30a0-9eb8-a4ca74221a16 | -5.64524 | -43.71192 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c11bad1c-b5fa-36a1-96cb-81c9527a3fb4 | -5.64144 | -43.7113 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d1e8ddf-5185-36be-a9fa-d5b97c09e24c | -5.91375 | -43.48539 | 2024-12-27 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 01fe9729-d202-3a6b-9a44-2bcbab170c71 | -4.48532 | -45.67642 | 2024-12-27 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1409bdb-a74c-3d82-9854-3ad1dede95ef | -6.90521 | -39.5845 | 2024-12-27 04:33:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6fe0a897-1f2c-342b-8bdd-990da79859e1 | -5.39803 | -42.95501 | 2024-12-27 04:33:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13cb1041-2371-3f40-a487-499c66ddfe5c | -4.50671 | -44.23233 | 2024-12-27 04:33:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f68a1f9f-02c4-34bf-9a89-8bf5fac72add | -5.35933 | -39.34683 | 2024-12-27 04:33:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e89328f6-a79b-387b-a879-33d7943ebd49 | -5.22237 | -41.27639 | 2024-12-27 04:33:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 995894c1-532f-3a56-a566-f32b37a04d62 | -5.31407 | -46.06038 | 2024-12-27 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f0eed0b-41a9-3e92-9fb8-e1615853d3c4 | -5.57543 | -46.13683 | 2024-12-27 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e424706-6727-3643-80ff-1c089a5157a9 | -5.39519 | -46.55554 | 2024-12-27 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14637a9c-86d4-340a-b705-1cd2953170d9 | -5.35953 | -45.20586 | 2024-12-27 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3103de8d-30e8-343f-b462-4fa3c13da13e | -8.63448 | -35.9547 | 2024-12-27 04:33:00 | NOAA-21 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fe069bcd-a43d-3a1e-b9e2-98b1f58a5145 | -5.37383 | -44.84473 | 2024-12-27 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d8ceb84-ff43-3d76-8de3-ffb7a0cc53b1 | -4.07804 | -47.09078 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e7bfcc-8bf1-3fa5-ae96-693dea92fc7c | -4.62576 | -43.91736 | 2024-12-27 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c55340-6a5d-305c-9662-223361037c83 | -11.5633 | -44.82525 | 2024-12-27 04:33:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61331a80-11ed-3c5d-a6b6-7f8ad06c1f63 | -6.21062 | -41.56244 | 2024-12-27 04:33:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1b478f4d-140b-3bba-8742-91595b10b76c | -6.02663 | -39.76825 | 2024-12-27 04:33:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 243cdca2-261d-3c6a-a7ac-5409c6ffe125 | -5.64453 | -43.71658 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6d73ac13-a64f-3d67-a91e-20fc4564e165 | -4.71485 | -43.43569 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97ede28f-19a0-308d-8079-17033b203e97 | -4.08251 | -47.10559 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82ad8e35-d6b8-32b9-b5ee-952478f36db3 | -5.39406 | -42.95438 | 2024-12-27 04:33:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 37036e36-7e2f-3bcb-8052-d9602ad8f59e | -6.46807 | -41.61872 | 2024-12-27 04:33:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f4b20ea3-b0ba-3ec4-a18a-76756ee2896f | -6.90005 | -39.58403 | 2024-12-27 04:33:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8e1b90fc-94df-3fd5-a53e-e176657544e4 | -5.39044 | -40.67142 | 2024-12-27 04:33:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53babb4e-9f56-3397-a337-ffa80f6ac7fc | -7.07723 | -39.68155 | 2024-12-27 04:33:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 22e8222e-3ff4-3a11-acb2-813f8ac93a11 | -6.23536 | -43.31483 | 2024-12-27 04:33:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b74593-0cc3-3a8d-938c-70a6eb4440ec | -5.24434 | -41.40144 | 2024-12-27 04:33:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e803bf66-f26a-33c8-b979-3f3f19a56a92 | -5.6405 | -43.71377 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b00ec367-0207-3f1a-8ed5-99d2e9aff76d | -5.63693 | -43.71536 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0adc70a3-644f-38fc-88e6-5a99f869a08b | -4.43205 | -46.5624 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d8c2bdd-9b94-3f35-a333-ea151c5f37f0 | -5.21299 | -44.90601 | 2024-12-27 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c258d7b2-529c-3d8b-9685-5bbba1b24663 | -4.08358 | -47.09871 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61beeafd-da2a-3d62-85db-b89002f41611 | -4.68877 | -46.52653 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db96de5b-bba1-31fc-b39d-9d6293dedcb9 | -5.64567 | -43.70498 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 586e977a-61a3-314f-9b84-fb022756fcdc | -3.09185 | -53.71912 | 2024-12-27 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68c1fd94-efdb-305d-bcfe-16f0b4c57072 | -4.71558 | -43.43096 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4845602-65c2-35ed-b3a3-479e6fc5e142 | -5.31123 | -46.0562 | 2024-12-27 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c464def-0d2b-3844-a7dd-260bb0127f6b | -4.42926 | -46.55837 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| af99e10b-0a28-3613-9486-2c3f3c6a9519 | -5.39457 | -42.9509 | 2024-12-27 04:33:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| caba8094-2e4b-37b9-a6c0-2b0ec271748f | -4.24894 | -47.58623 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb88089f-5260-39a6-947c-5b31d1537f1b | -4.98087 | -42.59687 | 2024-12-27 04:33:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8998c0d0-4d37-38c2-b879-066db22425b9 | -5.64431 | -43.71439 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e028d647-3c53-37f6-ad3d-67968b42063f | -4.42205 | -46.56088 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 40ef8ff5-f8c3-3939-a022-e42a5f6134e1 | -4.42484 | -46.5649 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d4e69e3f-85fc-3fc9-9761-9fc7f6da5457 | -5.35466 | -39.34307 | 2024-12-27 04:33:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 78d2361f-8f74-3f31-9402-87f96b9e7d30 | -4.07697 | -47.09768 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5e6f20a-8914-3203-b3b7-ec6ada0de13c | -5.63983 | -43.71846 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ae48cf6d-9b27-334a-9535-5d5d9469ac04 | -5.94512 | -44.44698 | 2024-12-27 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d5348b1e-209d-3011-9aed-37b803e3c09e | -5.64811 | -43.715 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cddd6bf-2270-34f1-8688-acf089c97ce7 | -5.63915 | -43.72312 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 574d1d18-1f22-36bf-b22a-fff683661df4 | -5.2201 | -44.90704 | 2024-12-27 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab9611b3-23fd-39f3-8ed4-0467330f2ce6 | -4.56002 | -44.12638 | 2024-12-27 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 489c192f-7a92-3479-bf4f-42ad2e5dd5f8 | -4.34443 | -46.49148 | 2024-12-27 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dbf4e37-b830-3e5d-8b50-846c7034f617 | -5.3589 | -39.34984 | 2024-12-27 04:33:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 26103a0c-6004-39e1-9f10-35d4a5625e22 | -5.90335 | -43.492 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0cd2a06-fb6e-337d-9cb9-f4c271800a27 | -4.42762 | -46.56893 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bbbaa67b-adca-3822-9e8c-52aca29c6cc8 | -4.06705 | -47.09615 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d74d154-553a-3c51-83e0-b0f7baa868f8 | -4.30733 | -47.47208 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73509fa7-0233-300b-ade4-6547eba8c850 | -5.13059 | -43.24181 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2e7f4341-9368-30a3-9484-203d74a6b6c0 | -6.37061 | -43.56832 | 2024-12-27 04:33:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43c3ceaf-48a0-32a2-aeef-83c29054a6b0 | -4.42872 | -46.56189 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 360661f9-dfc0-3131-9c00-6c7171e4574a | -5.91305 | -43.49024 | 2024-12-27 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5286a660-543d-3dfa-ad20-5a3cd94f9041 | -5.64118 | -43.70908 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59a4ca83-c9aa-3d40-a40e-655b0f772cee | -5.35509 | -39.34007 | 2024-12-27 04:33:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 589e9122-f0bc-38a6-97a9-43b9206ef4d7 | -5.91485 | -43.47218 | 2024-12-27 04:36:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8440564e-d612-3c10-8fe6-69e654bf561e | -5.91166 | -43.46675 | 2024-12-27 04:36:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4746968f-f63c-3522-8946-7a4c9e29d4b9 | -12.334 | -43.67935 | 2024-12-27 04:36:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad5098a3-5b53-3327-aeb5-414c241ba087 | -12.33819 | -43.67994 | 2024-12-27 04:36:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 090038b8-5fe0-3443-ae9f-2b6b0a2508ec | -12.45798 | -43.56194 | 2024-12-27 04:36:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 157988b4-5883-3b2b-8fa6-96098061ad81 | -12.33873 | -43.67599 | 2024-12-27 04:36:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 930d9c8d-3061-32be-bc41-9ed7ef5181c8 | -12.34238 | -43.68052 | 2024-12-27 04:36:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bae0498-49bd-37b7-bfd2-594042b6750e | -10.18585 | -36.29553 | 2024-12-27 04:38:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5131f54f-5e29-336e-bd9d-c226d84aeeeb | -10.18896 | -36.27536 | 2024-12-27 04:38:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 803323da-b4c6-3bc1-8d42-5074e3faf342 | -24.24379 | -50.73989 | 2024-12-27 04:38:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3fbe9de9-2719-3ea3-a4a7-2d3fd8660463 | -23.10011 | -52.09633 | 2024-12-27 04:38:00 | NOAA-21 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 65b3d2f2-35cc-31d4-bf5f-dc258617de26 | -22.0068 | -57.30177 | 2024-12-27 04:38:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ac9e749-6b6e-3997-abc3-c4e35b4a2135 | -28.58456 | -49.44222 | 2024-12-27 04:40:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e6b8441-999b-3646-b17d-c4ac53156179 | -28.03833 | -55.20478 | 2024-12-27 04:40:00 | NOAA-21 | PIRAPÓ | RIO GRANDE DO SUL | Brasil | 4314555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcee2218-c638-356e-b470-e70690c947e0 | -29.87504 | -51.14432 | 2024-12-27 04:40:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 1f80409a-fd52-3519-a3b0-bc2aeabf3837 | -28.03904 | -55.20065 | 2024-12-27 04:40:00 | NOAA-21 | PIRAPÓ | RIO GRANDE DO SUL | Brasil | 4314555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe16c5d7-e72f-3031-850c-feb3287fa5b1 | -2.28666 | -45.57326 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc5d5d92-7e39-3a46-9a88-16c7a562c52b | -1.55153 | -53.50283 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 551efc38-6a55-39cb-b519-160e153c0a73 | -1.55763 | -53.50732 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 540cfc4d-ac9f-3639-8f2d-135cb1546dfe | -2.28213 | -45.57911 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c5173bf-c159-3cc1-8abe-b1e27358f4f5 | -2.15528 | -53.72814 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7fa84ee-bdd7-33a2-b136-f33468829465 | -1.8939 | -53.28456 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50736086-6f65-3d52-8802-bfc8adc5ef8a | -1.7984 | -53.22375 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dcf9937-6ec1-303d-aee4-54049ce59d90 | -1.92839 | -53.34644 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6ab5de0-5b5e-333c-9013-9436b29cb7e9 | -3.70373 | -43.41786 | 2024-12-27 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c0079c5-8680-35f0-aa61-84a4adf74f46 | 2.93243 | -60.30052 | 2024-12-27 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 767cf9ab-7b82-303f-9eae-fb6f4ed67de5 | -3.69736 | -43.42094 | 2024-12-27 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ec62276-6716-3ebd-a538-31327ba1591e | -3.22961 | -45.96102 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3feb33fb-959c-37c7-a465-8a996fb036f7 | -1.18973 | -53.58755 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 139daa71-2116-3f08-b20c-0787b5420595 | -2.99748 | -48.05177 | 2024-12-27 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7327edd0-bb36-3734-8bc3-87006869d9c2 | -3.06788 | -41.89574 | 2024-12-27 04:55:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa2b5f8e-63db-3a32-b1a2-2b1bdc3ff019 | -3.0671 | -41.90079 | 2024-12-27 04:55:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5b31ee6-03ef-301f-9b8b-d6c4420346d1 | -3.06962 | -47.77308 | 2024-12-27 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README13.md)
