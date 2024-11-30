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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa4fa56f-318b-3fd2-b5c3-189779e8269e | -4.5896 | -44.70305 | 2024-11-30 04:40:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b215ebab-e379-3984-bd5d-7cfe7eb1b92b | -2.06829 | -50.29491 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6accefe-c2fa-3057-a4f7-833f8f612762 | -3.20161 | -46.56818 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 889858b9-07dd-3f4a-8fe0-0c0df2a224bc | -3.86196 | -50.11914 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db5346e3-fbb8-3fae-a3ad-65177dafd87f | -3.14705 | -49.21157 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9378e855-b734-3a84-8f54-32763939ecba | -2.63133 | -51.74888 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b9414b8d-56cb-3423-bdf5-a649d3a50c24 | -2.12428 | -46.38974 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7850cd2f-d802-3032-8e10-08a6c0fba8e4 | -3.22063 | -53.83073 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34c1fc12-ff39-3410-b228-a2926f5e3b4d | -3.59654 | -49.99117 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b47646bc-27f4-39a6-b66e-4cde811daaee | -1.68412 | -52.50256 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee4f48ba-8a95-377a-bcca-822460d355dd | -2.37347 | -54.33423 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5659bad6-0e37-30c0-b8cd-958be67cc2e6 | -2.90191 | -54.77319 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 535ec6e9-ccf4-3d02-bbc1-a52c3440e8b0 | -2.37884 | -54.32728 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18fa3e49-9195-3d67-ae3e-c7465461d3d4 | -3.30494 | -46.15053 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94813ddb-c9eb-35bd-8090-4b09ef1df0f9 | -2.8253 | -52.96652 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61ab847e-ebbb-38fb-9d60-a2fcabf9b6ec | -3.18478 | -46.56168 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9f6abea-419d-387a-901f-db5a53d895b4 | -6.91509 | -43.54826 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 90666faf-3702-3cdd-b95e-cd1926b253df | -3.51387 | -50.25592 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9888d611-79b5-310f-aee3-1896e836bdc7 | -3.09574 | -53.72807 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c374054f-615a-3461-b681-0bc4554f1e4a | -2.99416 | -49.5368 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d421077a-4b1e-3ddc-8f48-8cc2aaf7750e | -3.44205 | -54.07053 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 593d1b13-640a-3cf8-8f0b-d56177fc9150 | -2.96628 | -48.03562 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f8c2a91-fc49-3cac-a94b-77f0476a28f4 | -3.38745 | -50.14956 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9777434-4d3d-3335-a6b0-0c1f7cf6abeb | -1.59445 | -52.04417 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2123f00d-74f0-3dae-8f09-a57347ba2b18 | -2.77645 | -48.57958 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f83ec1ff-fa1e-3568-a5d6-4fc6c2bc8752 | -1.20119 | -52.56503 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72ada3dd-3f2e-33e7-a685-0efc4f89942f | -1.4398 | -55.2475 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f3d29e5-e873-32f6-9a68-cb47c5825d48 | -2.63656 | -49.90914 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f29ab245-0599-3f95-97df-cd94444ec700 | -2.85868 | -48.09342 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8820491-d24f-359f-8b76-4f9c2c4a63aa | -2.62955 | -49.49744 | 2024-11-30 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6611fcd-f063-3fa3-a5f1-6471c2060bf0 | -3.04712 | -49.37166 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e72c07ec-cd7b-3c95-bbc9-a68dcbe1e73d | -8.38266 | -44.47236 | 2024-11-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc337a0a-29dd-3e2a-8b34-12100bf1bfb1 | -5.35391 | -44.77001 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef7be228-e4ff-3e43-b8d5-6ced96356c9e | -3.10285 | -50.36327 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f950f85c-bc5c-3573-9f52-68cb2b3f17e8 | -4.83176 | -43.64704 | 2024-11-30 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f290fdf-cafb-3b3e-98cc-ae779b958547 | -5.03928 | -45.24478 | 2024-11-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0bdf311-d6ab-329d-95c2-47ef44042f39 | -3.0246 | -54.01701 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39357a0-4954-338d-b6be-585896bfcf87 | -2.18599 | -48.41683 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87c8ff03-afa4-3430-a2b9-615a816de737 | -3.26488 | -49.8927 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dd229ea-944f-37ea-87fe-1083f271339a | -1.21591 | -51.73525 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcaa16bb-14e6-3dd2-b12a-9d0b93e8a83e | -3.04994 | -48.96367 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e515882b-831f-3588-ab86-a1cac3b601ce | -3.57184 | -46.34696 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88d2a218-af4b-36a1-90e8-facead8a4b00 | -5.18707 | -60.26156 | 2024-11-30 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 086b9109-4451-3528-92f6-87b5989f5298 | -3.89346 | -46.68129 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2111b6c-1226-3ee8-aa6b-3ee9b5b8a2b4 | -2.54885 | -48.18379 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8da00ac0-8576-393e-908b-5e25b834478e | -1.53167 | -51.61613 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd994a9e-2ccd-391d-89ef-7cc311c1ec86 | -3.99514 | -46.65674 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae4a5fc7-620e-3a74-b957-98ef3ae794b5 | -4.01829 | -49.01358 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f82c5243-a694-33da-a457-dcd935188834 | -1.62234 | -52.4561 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b64db2f-60bf-366e-8561-eecb37725d74 | -3.25057 | -53.64117 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b31b6dea-3234-3886-9bf4-0b09d6c6aa70 | -3.10739 | -53.80849 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 482bc604-9216-3495-bc80-64dd4d4ea836 | -4.4825 | -48.19067 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32b453af-4aae-3851-bc7b-adc09dfbdb2c | -3.75115 | -49.93705 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e777c924-017d-3880-91bd-5043aa144155 | -0.58457 | -51.69629 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7d5ea8d9-31e8-3842-a4e0-363831bdabcb | -1.54906 | -52.28181 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 551afb04-70ed-3c1c-a9db-02b9a9fb7897 | -1.78906 | -46.25087 | 2024-11-30 04:40:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd71c9b3-22c1-30f0-a65e-009aa8fc2df9 | -2.735 | -47.9926 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029d2842-7570-3234-a609-bf0c5ebb37a4 | -2.16713 | -48.38577 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18806b01-8a2d-3e04-8e34-7593acfb8031 | -2.69663 | -46.86753 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| daa6769c-d583-3d69-a97d-a2b322a692a6 | -3.24206 | -46.42001 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc13d34d-7090-3921-bed4-c221729c5000 | -1.35552 | -51.37928 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6f023d0-70ba-3b92-bd5f-0fcc4cb06466 | -2.67591 | -46.14178 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c2d252b-538c-3867-8c1e-ad1c84e09f0e | -3.26142 | -48.89507 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11ad56ae-b202-3638-a0e8-10952beeee10 | -1.51436 | -45.89663 | 2024-11-30 04:40:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcb0faaa-03ad-3cfc-8cde-bbe0978f40e9 | -1.04649 | -51.73672 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9059f9b8-a0c7-3eca-bfff-f232a8fece69 | -3.69594 | -51.80499 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5ecddca4-be11-3762-976b-12e3e5bb5b50 | -2.02475 | -50.76919 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| febc6203-0cd9-39e2-8629-76e082a0f9b7 | -2.64952 | -46.12555 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4eaf2b9-f5a1-39a8-a07f-c25fed79a82b | -2.45111 | -54.00043 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bddd824-3039-383a-a8c2-c5fbdef836ab | -1.20176 | -53.87996 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6070d944-2fae-3986-899a-216e044179fc | -2.88026 | -54.21262 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fbd0121-dcd1-3392-81fc-5c29b8c30a4c | -2.98731 | -53.29518 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e136d85-eb79-3bd1-8f73-60b534631dd8 | -3.05434 | -49.52204 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad538c91-9ab9-3c5b-95f0-51e721992d54 | -2.22407 | -46.40096 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c0963c2-534a-3d6b-81e7-651b2e1ba01f | -1.96919 | -48.6714 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11d287ed-9e8b-307c-ba89-784965052267 | -4.11325 | -54.40963 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8336b45-d203-39cd-a26f-bb8523d4d4ea | -3.61369 | -49.96876 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9cc2d41f-6e26-3375-a048-01445ede79ab | -2.72295 | -48.65919 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b98e4249-c7b4-3d32-81c3-d4df5a157428 | -4.61549 | -47.00289 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb7f09e-b58b-34c9-835a-64ad1cea3095 | -4.09094 | -51.11285 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2b86f73-b631-34a7-a2bb-98e4b000be15 | -3.32058 | -54.17522 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e879f30a-d868-3d68-bbb2-97225d80a96f | -2.26086 | -50.35773 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49cda347-1d49-3c7b-916b-3cc5cf15b184 | -1.28497 | -51.64819 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb32424c-e5b7-3972-bac6-88dccd0ae037 | -3.07033 | -50.32897 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70979259-9fa7-3088-b21d-0db4ffee775d | -3.31998 | -54.17894 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| db5d586a-4555-36bc-b154-af1759b9d566 | -2.19939 | -48.33084 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dfc9493-399a-3c77-a1ac-430dcb11b206 | -2.51385 | -46.41623 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4912ccac-02aa-3f1f-ae4d-48b08972a8ef | -6.6391 | -47.9152 | 2024-11-30 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b22a19aa-a6b3-3d53-8b8f-dbe180a4467d | -2.64422 | -46.2535 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b778591b-95ee-3848-949c-5d4e1ec25a13 | -1.06528 | -53.63561 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63e32781-606e-3000-b4d2-d9270d07c746 | -2.60295 | -46.56644 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9237c1e2-d3f3-3795-9e8b-61e05e86c16d | -2.85096 | -48.09935 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53f19419-2494-348e-ae9d-2bf3dc3d8217 | -3.69314 | -47.13819 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e91e2076-70fa-3612-8302-9134fb66ece4 | -4.04548 | -48.33477 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c38f9e65-784c-342f-b05a-126f0b5f4503 | -1.44044 | -55.12804 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d952cd9b-45d4-3258-8eb6-2575d8943a41 | -2.60177 | -46.57404 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dfec6eb8-2b22-3c05-a4d7-b4fbfcb00119 | -2.83047 | -49.84278 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b0aa46e-1de2-3200-b305-7f698024fabd | -2.47725 | -50.36551 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67f3c2d8-e7d4-3441-8cd0-e1ecd86895cb | -3.30188 | -50.75351 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ef2a09a-4560-3adb-8b8e-250fb05b68aa | -1.28296 | -51.73278 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README54.md)
