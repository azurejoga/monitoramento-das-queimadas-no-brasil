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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1261bde9-759e-399a-9585-00dd3c26f223 | -11.1363 | -55.54015 | 2024-10-29 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2d525c8e-2d0e-3127-9e1e-f9e6c3e8f085 | -11.12575 | -56.29475 | 2024-10-29 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdbccdd5-2027-3669-bc49-ebe8fbc2c1b7 | -3.64904 | -55.50256 | 2024-10-29 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee277295-86e3-3b89-a93d-fad1ea3a7c93 | -4.24014 | -55.9655 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de1bafe8-5b1d-318b-b60c-213fe9c3ff73 | -4.20272 | -56.31223 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd6c168-c6f1-3c10-98c4-f27e98ed7572 | -4.12906 | -56.2225 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b23e2a4-aff1-30dc-b7f7-3b3c68fbf1e5 | -4.1158 | -56.19761 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85fd5623-dc85-3f0f-88a8-c3b9a73a9604 | -4.08628 | -56.31931 | 2024-10-29 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75431c8a-3f05-3a6e-81ce-16593e73ebfe | -3.91845 | -55.3861 | 2024-10-29 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf521b2a-a68d-3c2a-b333-b6725979ffb7 | -3.84543 | -55.71841 | 2024-10-29 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58a9621d-cc36-3324-b7eb-a907c5d37477 | -5.07628 | -56.24548 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8dc1aa3-baf9-37b1-a6d5-1d434d1a7e2d | -4.96206 | -56.93582 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f2a0fd5-0af6-3106-9196-765ebf52745f | -4.85609 | -55.89141 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fe3a4b8-7a1c-354e-9476-eb6fabb44fb0 | -4.73295 | -56.05124 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeb8284b-c6f5-39de-a897-cf5a943e092f | -4.73237 | -56.05513 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4a5052c-3248-3efa-9aaa-5e87758c83be | -4.72441 | -56.13735 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90677c89-ea68-3edf-84ff-ca44e3cf8117 | -4.60808 | -55.87239 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 478fc3d3-1927-3d9f-b9e6-9a4faa3837e3 | -4.53546 | -56.12738 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46b420b4-9f39-3035-8eae-2b5b80ae439f | -6.26584 | -56.52697 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53fc9acb-5f05-3042-a863-1bc6f8f69ebc | -5.30932 | -55.83563 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02f3d86b-939f-351f-894a-8b9980f6a3c3 | -5.3062 | -55.82689 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 364a9f23-4e71-368c-b075-6eb5e7c9f9fe | -5.30559 | -55.83101 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d7cbb5b-8b9a-36c7-ba1d-09ef816be6d1 | -5.30498 | -55.8351 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbeecb3f-38d6-39b9-a2ca-dc4df99e5fe2 | -5.30438 | -55.83918 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc6044ae-df97-3873-9556-817bbd343859 | -5.30186 | -55.8263 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1d34472-f36d-39cf-9eee-b715c359b87b | -5.30126 | -55.83042 | 2024-10-29 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ce9b825-cd88-3d3d-954b-92bfc556c7cd | -9.36706 | -56.83554 | 2024-10-29 05:27:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc1e0862-342a-378d-a0a2-bfc00b1f0c25 | -10.5967 | -57.7971 | 2024-10-29 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34010764-3964-3b43-b600-022f70230603 | -10.59619 | -57.80079 | 2024-10-29 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d26440f-3af2-39c4-be4c-8a1b80509670 | -10.59211 | -57.80016 | 2024-10-29 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 363a12d2-ef80-3e15-a8f6-b392dc681e7e | -10.12085 | -58.20352 | 2024-10-29 05:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82c17486-0a99-3195-9109-0d6ab0f4587c | -9.7431 | -56.98001 | 2024-10-29 05:27:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4251691f-9431-3755-9ada-72fe1a30df17 | -9.73884 | -56.97939 | 2024-10-29 05:27:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aba2917-9ad6-3d52-bc0c-1118e98110c6 | -10.84989 | -56.92043 | 2024-10-29 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e34ad82-ddb7-3b9e-872d-72db937225cb | -10.8461 | -56.91562 | 2024-10-29 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8588f21c-7e5d-32c1-ba45-e983e2652a04 | -10.84553 | -56.91985 | 2024-10-29 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85a156e7-8961-3f19-9b91-5b703bdc45c2 | -10.2616 | -56.75996 | 2024-10-29 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111fca38-7af1-3650-a078-e11765ab78c4 | -10.254 | -59.21452 | 2024-10-29 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847233a3-08d9-38f9-914e-2b4e8c4679aa | -10.06054 | -59.35592 | 2024-10-29 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b0ad7d0-34dd-3a8b-a5f3-08aae034eef5 | -3.56964 | -58.724 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40e6ceaf-38ee-3711-b346-8ca4fe1dc856 | -3.5633 | -58.69446 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 814e204d-4343-3cdf-8e7f-b8d8ee6a4436 | -3.56269 | -58.69846 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bda95683-a272-323e-9571-8f21dad280be | -3.55976 | -58.6939 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a16b1a7-9849-3e2f-aafc-7dab63e1bfa8 | -3.55915 | -58.6979 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 67add128-2864-37fc-9c7a-f421b233f657 | -3.55096 | -58.68027 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 857690f7-05b5-3e68-93dd-417113c80f06 | -3.55034 | -58.68427 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fff9a2a-add6-35e2-a71f-73d31bca266c | -3.54741 | -58.67972 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afda2c31-d6ca-3d5b-9f4a-27912cb7ab7b | -3.5468 | -58.68373 | 2024-10-29 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7593af62-4286-38cd-a088-172ef29e7d19 | -3.50726 | -59.53476 | 2024-10-29 05:27:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ab32d7c-0bb0-337f-9f6b-ba157a3f808a | -3.459 | -59.73124 | 2024-10-29 05:27:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfb5b569-b87c-37f9-9419-793211d9a916 | -3.43848 | -59.25247 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb37c7a8-b9ff-3beb-bd56-429bd81ecacc | -3.4379 | -59.25626 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68185ab4-9809-3d87-b6d6-3cefe4540a94 | -3.43444 | -59.25573 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 608ea7ea-1c0b-3301-8d86-fccf349df481 | -3.38922 | -59.52856 | 2024-10-29 05:27:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 811d86ca-942a-352a-b46d-5605a173d9a1 | -3.38902 | -59.52862 | 2024-10-29 05:27:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6efe3090-cbda-3824-bb57-4e09a91be415 | -3.11753 | -59.42684 | 2024-10-29 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69a6879a-3f3b-343a-9fc3-9ad722b2a1bd | -3.11696 | -59.43055 | 2024-10-29 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7acaec7-b4d5-38f4-8a32-c76fb4473b5f | -3.9619 | -59.18114 | 2024-10-29 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c67373fd-7ced-3bbc-bb02-7594379d9f5d | -3.91604 | -59.58843 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dae7ed5-6340-3adf-b531-f6e4629b867c | -3.85365 | -58.82901 | 2024-10-29 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6c15f00-00fd-3fd8-aa4c-1bd1a99a1eee | -3.76612 | -59.33139 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0cf6e10-3267-3781-b3ad-1926739ec9d8 | -3.74191 | -59.44343 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb29a3a1-3250-3f84-b298-a7cd6effe53f | -3.73847 | -59.4429 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14a107a6-7065-3aab-9504-99ef739e029e | -3.73099 | -58.99255 | 2024-10-29 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fba0530-8aaa-3880-a2a8-20706387cdb9 | -3.73039 | -58.99646 | 2024-10-29 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c356cf9-60ac-3b46-9d91-b589e977a6a4 | -3.70657 | -59.6739 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c22477b-7e32-32c3-a9df-53be33081756 | -3.55033 | -59.77476 | 2024-10-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d5ee3dd-9e47-320f-a775-72dd1230afd2 | -5.24571 | -59.98339 | 2024-10-29 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f3e9b9c-8273-37ac-9ab6-f888ddd6bf5c | -3.42321 | -59.9594 | 2024-10-29 05:27:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1448ca56-e007-39c4-a039-ebcc7aea2d72 | -2.95537 | -60.01646 | 2024-10-29 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d850806-3cdc-3015-bc65-0e1774b2c1a4 | -7.93165 | -61.557 | 2024-10-29 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14133367-ca44-3d95-a0be-6fc4a3e0f1d2 | -7.92832 | -61.55648 | 2024-10-29 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80d6de5e-c917-3549-b6a8-de591b83ca93 | -7.92498 | -61.55596 | 2024-10-29 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab2db936-94f9-30a4-8f41-e321e73624ad | -7.89978 | -61.47615 | 2024-10-29 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b37fa67e-48aa-3b56-b14a-b9634dc686f0 | -7.89936 | -61.52311 | 2024-10-29 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83aa21b8-7ce5-3783-b6ad-a05c5de7651f | -7.89311 | -61.47512 | 2024-10-29 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89511359-4925-3fc3-9e5a-effb70806357 | -9.4908 | -62.57961 | 2024-10-29 05:27:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990a1f95-15a8-3f6b-be11-12e1e297bc6c | -7.66093 | -63.45297 | 2024-10-29 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 692651a0-8397-3211-be14-5b1da93f789f | -7.65981 | -63.46004 | 2024-10-29 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35e7aade-02c1-3b2c-abda-7cbd1aa06a70 | -7.6576 | -63.45243 | 2024-10-29 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c821beb1-0fe4-353c-b036-eaae8f0cd7e5 | -7.65704 | -63.45597 | 2024-10-29 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 539802f5-10bf-3df7-afc1-106f0e5879e4 | -7.65648 | -63.45951 | 2024-10-29 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e27ed34-2bb3-38a5-a200-c5a79d767001 | -8.60935 | -64.06636 | 2024-10-29 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9157d1f0-7578-3e51-bd00-b2339c5e6d8c | -8.58691 | -63.24808 | 2024-10-29 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cce4158a-29a1-3e4e-95ce-2f5d3abbc910 | -9.5026 | -64.42588 | 2024-10-29 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d0e1a6d-ef1c-3135-9de6-be4473826b40 | -9.64927 | -65.74245 | 2024-10-29 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba0bd4ca-2ea7-3312-8dbc-a26b9ff9744b | -4.11212 | -54.29047 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ddd24f7-841c-34ba-ad93-9f0caf67904e | -4.05377 | -54.284 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a09f88f0-0264-31eb-bc1c-1c2b9ec7a5a9 | -4.01495 | -54.82472 | 2024-10-29 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 031d058a-eecc-37cd-960b-6a7f412e0592 | -3.96432 | -55.38287 | 2024-10-29 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c57912-3a3e-33d5-8d68-1eb0a6ca9ef7 | -3.92566 | -54.51244 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09df734f-9ad5-3bf3-8da7-5f9648d9639c | -3.92488 | -54.51017 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09d9497a-9f9b-3f83-b262-d86593471c1a | -3.91942 | -55.38473 | 2024-10-29 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36c65d93-3b9c-3249-8e0e-60f2fba9c87d | -4.90841 | -48.64521 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 958f2542-0e5e-34aa-9a0b-0f0b1b9b39bf | -4.90835 | -48.64566 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1eee3ff-d354-3ff0-9c7e-7bf98c030f21 | -4.90751 | -48.65147 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4435f450-3fa4-3dfe-9162-ac502296fd93 | -4.90749 | -48.65194 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17b2f1db-0f89-36c6-a1e3-8fd4fe755e5d | -4.89107 | -48.66928 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ecf093-0ef5-3254-a625-0cb422528d95 | -4.89096 | -48.66883 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b7672c6-4b34-32dc-8954-2fcad0600cb6 | -4.88419 | -48.66832 | 2024-10-29 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README104.md)
