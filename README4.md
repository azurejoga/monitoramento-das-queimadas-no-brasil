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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ede1771a-90eb-33f4-ba3a-856cb5fdf46b | 2.24839 | -60.29243 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00b9670b-27ee-364b-a41b-33a074defaef | 1.17601 | -59.14912 | 2026-03-19 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c06f168-bd47-3f93-84ac-df424ebff52b | 3.41674 | -60.16685 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee7684aa-d883-32c0-958a-a2317efad3fe | 3.38193 | -60.19213 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 874633a4-a04f-3516-858b-cf00053fc951 | 3.21361 | -60.1425 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 022193bb-cd5e-3dfc-bdba-8569ab655ca7 | 3.4216 | -60.16479 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33f8fe14-4a52-30e7-bf16-6a49db69a4df | 2.25132 | -60.28774 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05b8c1f3-759c-3fb6-b561-57f3044f5107 | 1.98923 | -60.88668 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8a239a5-de7d-3302-ad58-382fc5fb5087 | 3.41738 | -60.16128 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81706a4f-8663-3c4c-aecf-600713cba6f9 | 2.24772 | -60.28833 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d59e548b-04cd-3da6-8206-0ca7cb5c637b | 1.88484 | -61.31715 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee4d610e-cd93-3343-a20a-80ecc02a0037 | 1.51359 | -59.91544 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9264373b-9a02-3c6a-88e2-360172b43734 | 3.21495 | -60.15075 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6837d0e7-bc79-30c7-a0f4-059cc7ae360b | 3.39655 | -60.16883 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de8ebbc7-6580-3cf3-96c6-e0c584a5e8dc | 3.42032 | -60.16628 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a85460b-cf6b-340d-ae19-349acf23626a | 2.49842 | -60.01032 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f68c6d6-2191-358c-91d0-914775cc1d58 | 1.98985 | -60.8906 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c2c3cd5-8236-380d-907f-3a7195a12024 | 1.64537 | -60.29787 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d670dbca-cf04-34e4-ab96-04e55cbae17f | 1.98599 | -61.39774 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6a09889-cbb0-3671-a8eb-78e9837119cd | 3.38485 | -60.18746 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56285fc-8757-38fa-b300-18d5278ae741 | 4.09233 | -60.77415 | 2026-03-19 05:42:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2108cd64-b20a-3e2a-80c0-f52abe361e69 | 2.32161 | -60.49503 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef246e7-7278-3358-8528-51b76775773b | 1.98554 | -61.39796 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3bcd80c-33b4-3ed5-a580-c5e1a47d5091 | 2.06823 | -60.67695 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f37764c8-7199-31e5-aadc-503c90dcb3b6 | 1.96371 | -60.5635 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6f365d9-98c2-3581-8cec-70d16118f677 | 3.37901 | -60.19678 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a128576b-3a22-39a0-bc40-1c1fd0c7e5d5 | 1.56089 | -60.5191 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b696c850-2215-3252-abf8-ad955e644170 | 1.20565 | -60.62461 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1470e14-590d-39cf-8293-63e1e8d2f642 | 3.41965 | -60.1622 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3cfb623-2863-3f5e-b999-1c9246b69d35 | 3.21428 | -60.14663 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 284f235a-e7ae-30eb-8b80-632b09bac2f7 | 1.98634 | -60.89115 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4995edb8-1434-3e1f-9898-b554a3de315c | 3.42814 | -60.16921 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b5831ec-e855-38b0-9f0a-14b2085cb996 | 2.24609 | -60.28767 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8c83de9-f75b-310d-a7f8-7cdae135af5f | 2.25199 | -60.29185 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bb96949-3dc9-3fe2-a33d-f47a7608bdba | 3.40013 | -60.16825 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44362eac-9249-3d7b-9177-0defeab80558 | 1.96284 | -60.56554 | 2026-03-19 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a368eea-e0c0-3f0a-9d41-4390555727bc | 3.4138 | -60.16186 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 719b477f-2970-3e86-aee9-ae6bb1974743 | 1.41436 | -60.75643 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38307a2e-acff-39e4-a088-375b1e08a84e | 3.4254 | -60.16028 | 2026-03-19 06:54:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 50747bcc-649c-3b31-bd0b-d93aebd1854e | 3.3795 | -60.18432 | 2026-03-19 12:44:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7154e4db-8e4e-3b61-903d-4bf139ca1e0a | 3.41423 | -60.1604 | 2026-03-19 12:44:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 27a0f333-a703-353e-a718-63165fc7942b | 2.6543 | -60.1075 | 2026-03-19 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 97.1 |


