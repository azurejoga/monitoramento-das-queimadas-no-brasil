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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68aed125-c362-35bf-85b3-ef8f0a10f45a | -9.5316 | -64.60051 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a34bfd5-654a-3178-ac74-160d3f2c81c8 | -17.56203 | -57.47655 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cdc43d94-e613-33ac-9bb6-842b5f082dbe | -15.08273 | -59.64186 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ba5da8-52bb-3993-b1ed-affe428a05f2 | -17.70971 | -57.58783 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 06d9b6b2-bd18-35ce-a1df-72c787a4723a | -8.64266 | -63.45934 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ab5ce8f-294f-3a9c-b731-f3a835868fe1 | -17.70267 | -57.58966 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d1082e08-7c05-32fb-853b-726f79006637 | -17.64047 | -57.57022 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6914914c-4c69-39de-9c8c-fe9ae32bfb84 | -17.65535 | -57.55271 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9f226b85-2852-31a3-b815-d2debb0a0151 | -17.55289 | -57.51474 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d9b164ae-1a0b-36a6-a09c-1c194adbef22 | -9.01852 | -63.76228 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20c06d2f-ba28-3d41-8010-fbfc452560ef | -17.66213 | -57.56543 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f02fd571-f7b8-3600-8bbb-af23fb4a2404 | -8.63915 | -63.45875 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1127d466-59e7-31fd-b0f9-2c467216fed6 | -17.70558 | -57.58725 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6fa38947-afa4-39b0-bfad-83c0ac4e4b0e | -8.65198 | -63.42471 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6926ee5d-a574-3d66-a4a1-243512c2650d | -17.56619 | -57.47713 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5482ea33-6f68-399a-a68b-7b59141283bc | -9.94063 | -63.58164 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 017f3e7f-4a7d-391c-994f-31a6c381a508 | -17.70507 | -57.59109 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7c295729-f1ba-3bee-ad44-400c6593b948 | -17.63948 | -57.57792 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d2f29157-cb35-33f8-96a3-bb1a29174dec | -17.65914 | -57.58853 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f191d925-be24-3ab2-902e-a0dfe3d274cb | -15.09817 | -59.63576 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f21df43a-5cbf-3173-ae62-1f4efdc59dad | -17.65071 | -57.55598 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 96da3324-2b7a-3c21-b0eb-1780569059dd | -15.09461 | -59.63523 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be2f9914-8af1-34a5-bde5-eb97b1785091 | -9.02206 | -63.76286 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c336e631-2045-354a-90b8-2c84caff2814 | -17.63122 | -57.57674 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ab2fc828-d001-3347-b401-f250c38ca81b | -9.76413 | -62.00024 | 2024-11-29 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9db6da8c-9329-3d81-9983-8b19d701bab2 | -9.88552 | -63.10869 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da61c2ca-ceeb-3609-a44f-58d5e3e2acd4 | -8.46954 | -63.93918 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d248964c-8934-3099-bd24-bb2cfc734e6b | -17.70728 | -57.58639 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e54f9d09-1282-36ff-b1b2-2c082d8f40a4 | -9.64966 | -65.74014 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c316c281-0752-3c93-be3c-8a3f421c66a9 | -9.82431 | -64.7709 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceee4923-dcad-3e3a-8955-9c2cb5a54147 | -9.77603 | -64.77261 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c814ef-3c26-3b2c-8e8d-07ddf283cac5 | -9.28901 | -64.24483 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12403db8-e326-3e8f-8ef7-bb7f4251b027 | -15.0762 | -59.63662 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ededf31-f5f7-3e9c-88a3-5bdb8d719ac9 | -17.64509 | -57.56695 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 931d1a54-65e2-34d7-b286-5573e3e71c02 | -10.13104 | -62.54244 | 2024-11-29 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fddbf09b-49ea-3b02-bb1e-a840b9ee2735 | -9.90385 | -63.21182 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0d2ad3f-4c7b-3980-8906-3b8ef22a0a9c | -17.6446 | -57.5708 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ceb35800-7b8c-3c17-a133-41306731eecf | -2.9844 | -53.2819 | 2024-11-29 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| a9f0289b-a1ef-3249-a6df-31fa830e41a7 | -2.6498 | -48.7986 | 2024-11-29 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| edabed5b-e91f-3f9e-bb22-f056e2a0535b | -2.6683 | -48.7981 | 2024-11-29 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 251e703b-0287-37ca-868e-43d3df630fbb | -2.966 | -53.2824 | 2024-11-29 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2fb3fdf1-46bb-3509-b6d4-799de086b9bc | -2.6684 | -48.7767 | 2024-11-29 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 0f3c8a59-7613-3960-917a-e3fe09fda98e | -1.6997 | -52.4535 | 2024-11-29 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| e1c6e7e6-6187-3e24-a7ec-13eb2c10c6fa | -2.9844 | -53.3022 | 2024-11-29 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 81e2e8cf-cf2c-3de0-ab50-a2a075a01dd9 | -3.259 | -53.6388 | 2024-11-29 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7c1a26c9-25f7-385c-9d04-89ec0643d49f | -1.9541 | -46.4471 | 2024-11-29 05:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 15d86f2c-7aea-374d-a472-606935d679a3 | -2.6499 | -48.7772 | 2024-11-29 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b2c71845-fe37-30c6-b376-4904cec8e92e | -3.2406 | -53.6393 | 2024-11-29 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b8323743-d497-3ff2-be15-c0229f276bb3 | -2.6499 | -48.7772 | 2024-11-29 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| ece37975-9052-39dc-b5c4-ee687f64c6e2 | -2.6684 | -48.7767 | 2024-11-29 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| de7c58c8-dead-3247-8042-24438f89506f | -2.6683 | -48.7981 | 2024-11-29 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d9660308-2b0b-35ac-82b4-54df25f13629 | -2.9844 | -53.2819 | 2024-11-29 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 44d32249-ea00-368e-a0da-73686aca58f9 | -3.259 | -53.6388 | 2024-11-29 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 71ba84d2-6777-3ae3-9638-6dc08fbce750 | -1.9726 | -46.4467 | 2024-11-29 05:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 70925f45-a459-3cb4-a822-f04bc998a361 | -2.9844 | -53.3022 | 2024-11-29 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f0771b30-c4bf-3d09-b9c6-cd358415d007 | -1.6997 | -52.433 | 2024-11-29 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3755ab9d-1af4-330e-9a78-cf413786a766 | -2.966 | -53.3027 | 2024-11-29 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| bef9f919-ceae-3a33-baee-ed0001cd0f9b | -1.6997 | -52.4535 | 2024-11-29 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| ba6a9d0b-5844-3333-83bf-26c2380f3747 | -2.966 | -53.2824 | 2024-11-29 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 3c983d6b-1caf-3af0-9cfa-5596bfa76884 | -2.6498 | -48.7986 | 2024-11-29 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1cb28754-53f4-337a-bc71-0697ca88d547 | -1.58186 | -52.26431 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5b76c50-e6bd-3190-9936-3ea1d661dce6 | -2.33654 | -46.86766 | 2024-11-29 05:42:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 04f48af0-686d-33f7-a932-b939785d1421 | -1.70055 | -52.63772 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 502aab92-716b-3147-a988-3e491131ead1 | -1.31894 | -51.74301 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 17e67ee5-efd4-39c3-a053-8876aef4726d | 0.97722 | -50.12171 | 2024-11-29 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 19.0 |
| dc2802ee-6464-3805-9185-492ba1bac839 | -1.71167 | -52.62873 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| da2012ae-ea37-39ec-aa36-bb035b36bc43 | -1.32035 | -51.73351 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bed11c13-c3bd-3d6b-aa1a-54a3e9f702b5 | -1.78768 | -52.74176 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 85407013-2507-3ce1-a399-a790346ca361 | 0.98959 | -50.26496 | 2024-11-29 05:42:00 | AQUA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 341a0d25-5ce1-383d-9647-c4895ea285af | -2.66617 | -48.78714 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 75e5ccc6-0037-301c-86c2-97a7ea380faf | -2.65567 | -48.79517 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1c2f010c-5f61-3c3e-9014-e5177cb6a1d3 | -1.58975 | -52.27567 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c0e72dde-7109-3d4c-9c12-727dabba13a8 | -1.9699 | -46.4406 | 2024-11-29 05:42:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0958350f-9452-3edf-a483-d9394680070f | -1.92147 | -52.88206 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 022787fc-dd55-3fd7-bbdd-e3081d0bf36f | -1.23538 | -51.79911 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fde4ea95-b519-3e6f-a997-6712ab7b1429 | 1.21521 | -55.95471 | 2024-11-29 05:42:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f2337b35-c211-303b-ad0e-c12456fb6fb7 | -1.53159 | -52.66442 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b70c1bba-abac-3fda-98a0-168e21949712 | -1.69853 | -52.45871 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| d8785ca7-ecc2-3d95-9eb7-248bbbf780ee | -1.64624 | -52.73676 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7a2f91cf-e595-343b-87d2-5a2d87560d42 | -1.509 | -52.55466 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 68b2a00b-9d94-3f3e-bb91-3c1d3dea8fe0 | -1.49438 | -52.43026 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6f3391d0-244e-3db3-83a0-5534271ad7fe | -1.65747 | -52.72764 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fa1c83c7-631b-34d1-ab80-17ec85ad79cd | -2.65846 | -48.77648 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 81caec0e-beae-31ed-b0b5-d77f8f2bc463 | -2.00572 | -51.16867 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9424e09e-2051-37b7-9608-0777e3921c2f | -1.72539 | -52.47304 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c9eb9260-7394-3966-b53f-4dedcc12a5af | -2.10314 | -50.34031 | 2024-11-29 05:42:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 352cd5c1-3560-39cc-90a3-c35629460d7c | -1.61631 | -52.46065 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e2e83b47-3c88-3d16-b1a3-3b749d42e60a | -2.66477 | -48.7965 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a7842b17-5bc0-3e20-98e2-4e14536972e3 | -2.84171 | -46.84954 | 2024-11-29 05:42:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 01808cdb-99ea-392d-b1cf-e6429eb7cdda | -2.33485 | -46.8794 | 2024-11-29 05:42:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1b57fbd5-c784-36e3-aaa4-fa5c1a15d5d7 | -1.59124 | -52.26569 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0f8b89aa-d982-385f-94d6-c7dedf80f6bc | -1.18638 | -51.76572 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 074a429b-50f0-338a-bea4-33e44fb978e8 | 0.73837 | -50.87032 | 2024-11-29 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b79cf0d-05b3-3a2b-923d-970d6ec0b1f4 | -1.19844 | -51.74797 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77fea4e0-71ce-3a92-ada3-9d2704d38ce6 | -1.67333 | -52.4967 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04cbc292-9f6a-367f-a0a0-0bf3652d3382 | -1.72011 | -52.76924 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8fa07395-b08e-370e-ae51-29518d992d69 | -1.72123 | -52.63014 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 67416197-a202-35b8-965c-f0f1859b5d58 | -1.71205 | -52.75725 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 027e4655-2d32-3e66-9ebf-ad603fd777f1 | -1.69061 | -52.44715 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b0f714bc-6eda-33c8-a853-95c942d4b807 | -2.05872 | -51.18313 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README101.md)
