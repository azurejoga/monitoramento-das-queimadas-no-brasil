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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 368a30cc-b883-3370-ad34-fa406776ef54 | -2.30498 | -50.68306 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8fcbdd3-e589-30d1-8324-17d9b917f4ae | -3.39946 | -50.66413 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b9493df-b824-37cf-aecc-35624fd16f2c | -4.17408 | -48.62467 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67d2a25b-fc5c-3c2c-95d1-99293346f207 | -3.09107 | -50.35046 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87b697cd-4dcc-3f92-9146-52a0b73a8106 | -3.05553 | -52.76244 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00448566-d760-3571-a60a-8767267f29f3 | -3.60876 | -50.00025 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae1f7dc6-c0e4-36c3-a812-e4457d6d4bdd | -3.84669 | -52.0213 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3c9f2f7-c570-35cc-8a5b-0692ac8ccb0c | -1.17158 | -51.94463 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1a4ab8-c410-37de-81c7-44674602f7b8 | -1.49351 | -52.43742 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dea97741-c534-3cf2-b886-33ed7d9aad76 | -3.57645 | -50.33098 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc35061d-84b1-3df5-943a-08e00b81efdb | -3.2923 | -53.83132 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0776a2ca-1c5f-3022-b526-f942df8c8fa1 | -3.78635 | -47.72129 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7218fc4c-8953-386c-9b43-27c54c5b6e77 | -3.2167 | -53.62595 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db7566e4-5923-35f4-8366-98e2a4ec149b | -3.4187 | -50.43091 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 265d2f2a-d469-33d9-957b-a8b99cf213f6 | -0.97576 | -53.72621 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98568199-6213-3b7e-b5c1-19a430485224 | -9.10392 | -43.19662 | 2024-11-30 04:40:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2971fbe0-d313-3ff9-a726-bb27d9d25d9f | -3.83901 | -46.52165 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c845da5-1b12-3aad-9674-93dbde4afcfd | -2.71256 | -49.22746 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cac564f7-c4f9-320b-92f0-05171ab2bbec | -4.11264 | -54.41327 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e5421ba-1444-3f90-9a97-103a23fc7c6b | -2.68727 | -46.28302 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dce003c4-c7a3-3d54-a70d-5d8692207bfd | -3.70966 | -47.14459 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f1553a1-18ca-3d57-a6b6-6e0f8bb79afb | -3.7459 | -54.67618 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ccfdde0b-ce3f-3dbd-8617-c05da8416f3f | -2.67801 | -46.60046 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16c5eff4-59c5-3e71-8b8f-c33aad6fb33d | -3.96757 | -46.74351 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85292f02-5a90-32dd-97bd-5b5d426ea7f4 | -2.96907 | -48.03962 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09b00416-1750-30de-bb79-85078841de94 | -2.04122 | -51.1956 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3596d15-045f-3fb2-8782-c26f54b73dec | -4.07154 | -46.82126 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a345782c-ea11-3d5a-a4b4-3731d914fb42 | -4.18764 | -50.68277 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7b2a57d-937f-355a-b83e-ace164ca1bc3 | -1.14407 | -48.33488 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be308c80-01b6-39c3-8035-2861adfe763f | -3.11537 | -53.80965 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab929730-7ea7-3e4c-9a5e-1bc8e310ecd2 | -4.1067 | -46.90768 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29ac13e9-d849-33aa-8202-c2a7732863d6 | -1.20307 | -51.74611 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 448800d7-4614-3675-901b-b0f872d6f612 | -1.8297 | -46.29946 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 783f4581-14fb-3a33-89a8-9483ce8f562a | -1.00363 | -51.72586 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6830a3d0-dc86-3dd2-b255-374ad54f1325 | -1.47514 | -55.383 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa94b4b5-05af-3b5f-bd14-e0c6a1e7112e | -1.55717 | -51.27197 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 235f2576-52cc-3c36-b4ad-bc6d6a8ea4f0 | -3.15226 | -53.82389 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17de7757-a121-3195-a710-c5f459548641 | -1.87689 | -53.6007 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29397b5c-5405-3319-9563-4fe3375e6262 | -3.5742 | -53.75611 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8366458-4a0b-3b63-83dd-993b726b4418 | -1.15166 | -51.68821 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d0ee961-93ae-3f7a-af5e-0ae3a127b360 | -3.0544 | -49.54331 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c2a86ed-8a32-36cc-9863-47393d137289 | -2.46372 | -46.55697 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0999b88b-7ccb-395b-a03d-e3ac86192443 | -3.73047 | -52.33619 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c8bb9f3-bfd2-3686-a0b1-5a1d674604fa | -1.59498 | -52.27986 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aff2e816-c6db-30f4-8fb9-10a44500e752 | -2.56108 | -47.33656 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58f91e57-6cc8-3a02-a003-bd070922dbb3 | -3.26821 | -49.89322 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc637b4e-8b28-3be6-9c83-471b7cf952fd | -2.73832 | -47.99311 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5ddcfed-65a8-3721-b584-fef8ac360927 | -2.19279 | -50.57105 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5399774-7084-3f75-b43b-36fb6da6dd1d | -3.63648 | -54.44253 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fa867674-e1bc-346e-bf5a-5445f714ae99 | -3.61895 | -50.19259 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8d1d24f-f349-33b2-bd61-c0378a72e389 | -1.08156 | -53.63792 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9e4fe263-f896-3aaa-bada-58818029c8ce | -2.88967 | -51.58336 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e6f3dcb-15fe-3615-89a7-dbcc5f8eba5c | -3.83315 | -46.56059 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3af38c88-4d69-31ef-a559-5a55b89c2720 | -4.07411 | -46.68782 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38bd22cd-6c29-396c-94ee-6b6ff3e832b0 | -3.34725 | -46.60548 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbb6ff05-7992-3822-96c3-8f478f539be3 | -3.24558 | -50.77435 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5e42ef8-af8e-3da5-927c-dddaffb34ed7 | -3.44857 | -49.48055 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90d8589b-24d5-3dae-9c8e-613a9147441b | -2.18698 | -47.14346 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e7c83115-4f9b-35fb-9bfa-7721584f5ae3 | -5.22849 | -44.91274 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| deaa9953-4420-3735-ad1c-3361ef124ea8 | -1.31808 | -51.75389 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67e71c5a-99fa-3814-83ed-46132cb2031e | -2.18304 | -47.14655 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f5525bd9-5d3c-3fce-a5e5-9ae1356c4713 | -4.252 | -46.37503 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de98d21c-66c4-313e-b9e5-e5aa247f2d97 | -3.14317 | -53.82947 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f6b166a-4df9-38d7-92b3-fb0ceac01ab7 | -2.50341 | -46.41462 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 478ff8eb-ebd9-3874-804a-850225cc8aec | -1.71833 | -52.6317 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a8402330-751c-3bfd-8e30-e241afd7ccc0 | -3.96526 | -46.73534 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 897a5834-8095-329c-be09-02067dde3b09 | -5.16761 | -46.3095 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d9456bb-0c94-3971-bc73-347dae80897b | -6.59493 | -47.18682 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1562a38e-b774-3d0a-81b8-2a0bdf9c9e9f | -4.18821 | -50.67918 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40c73d91-a223-3538-9b93-c1178e3cb506 | -3.37715 | -50.11122 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a39c363-8902-38ee-b1f0-20c9e89101b8 | -2.23193 | -53.62182 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f996a201-4aab-398a-a1eb-3d84c60790a0 | -2.59544 | -46.56916 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9130d82e-0c52-3506-acb4-4d0518761e50 | -4.03883 | -48.33373 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8074e86-4ead-3aa5-9770-b7e54237428b | -1.04947 | -51.74148 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d019e1c6-a115-3200-a7c4-276d55e5e39b | -3.2916 | -51.49917 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a19b65a-f8fa-3f72-b0d1-0dedaff3e1e6 | -2.59341 | -46.20977 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926d1f70-ffaf-3e47-9ca8-e5de9ba9b546 | -3.25535 | -48.89061 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00901f61-c2e1-3a57-b09a-c10320cd5f42 | -2.73772 | -47.97517 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29efe2d3-b944-3b75-b108-4ea12307b582 | -3.09668 | -50.35866 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d4b1d8-c8c4-3461-8ef4-b0e3f02ea3dd | -2.53623 | -54.04322 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17bec4c5-35a7-3ce9-b9e7-5cc3b89203a5 | -2.65806 | -48.79332 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffc44db2-5c94-3b85-a7d4-83068df754c6 | -4.3461 | -48.12988 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9c67e63-7b46-344c-9afe-72c0db6b9c26 | -3.95267 | -49.75835 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 011be0c8-90f8-3063-a6d3-3ef134b9260b | -2.57395 | -51.84089 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b258dcf0-02b3-3dc6-8bd1-dcf55f1cb0a2 | -3.58147 | -50.34266 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35226877-b91f-3913-afb1-40c01470fae9 | -1.09049 | -53.39511 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e910d83b-2c16-3415-b768-1552c007b49b | -3.69941 | -47.14296 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8b4f3e0-feae-361d-8bda-89358ec3fb13 | -1.93787 | -47.95751 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edf5ecf5-a3cd-3bc1-bb06-95fe8efb25fb | -2.82811 | -54.09637 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7afb918c-5b57-36a5-9b7b-70d611f3d0b4 | -1.60217 | -55.55745 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9fb071f2-3f85-3306-bc68-c49fc94655bf | -2.38226 | -47.87728 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0da734c-ded1-38a0-9bbe-473a6adaa651 | -2.14029 | -51.41505 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0da35f91-bcde-325c-a319-b102998fdb88 | -3.60206 | -49.97769 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bedb6d58-cba9-3090-8890-14976e00be87 | -2.1499 | -46.61454 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b3ff692-0664-3e9d-baf4-86266e7c3fb5 | -3.19503 | -54.33117 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c40bf14-ce86-3beb-9438-4b3bac089571 | -3.3552 | -46.6693 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 923da3fa-9898-3ece-a8b8-bb57d9d8101c | -4.34155 | -50.76989 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5559a471-4571-3b8b-b194-996fcbd2e17f | -2.86772 | -45.33555 | 2024-11-30 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8c2d0c1-062c-3e79-8d96-a2c7685fa1d6 | -2.5637 | -46.56821 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee81d3fd-ffd6-37c1-947c-0747ff197066 | -3.25765 | -53.64742 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README45.md)
