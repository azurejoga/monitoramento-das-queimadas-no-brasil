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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a85be3ca-7c0e-38e0-8d0e-8a41d125d1c8 | -18.8115 | -57.6286 | 2026-03-03 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 839a94fc-8a64-385a-907c-62e95fbef6f4 | 1.5047 | -59.9116 | 2026-03-03 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 881feb39-fccf-3a7d-a3fe-f420f3fb83da | -18.8111 | -57.6493 | 2026-03-03 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| c8f2cc33-71a5-3350-bfab-61533fc9ed44 | -18.7915 | -57.6312 | 2026-03-03 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 0040b020-17b7-3635-a58f-b00bec39085b | -18.7915 | -57.6312 | 2026-03-03 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 1e949f64-95ff-39d2-a9ab-9935aaa98f79 | 1.5047 | -59.9116 | 2026-03-03 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a5c4fc86-83d1-3ab3-a7d0-52d6433322e4 | 1.5047 | -59.9116 | 2026-03-03 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3371a35d-099f-392f-a85c-3abea7d6dcfd | 2.86838 | -60.81443 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a31cab-732c-376a-97b6-81a96f4a92d9 | 3.12565 | -60.48072 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e57f72d9-6181-38b7-9c47-768dc17c4b60 | 1.95241 | -60.51707 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c775693-d3c5-30f3-9468-fc8c554b6a9b | 3.15603 | -60.70475 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f0ee082-269b-3039-8fdf-33bb7be979f0 | 2.89509 | -60.62777 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 561628dc-5902-3e6f-bfe2-10aeb289eec5 | 1.95796 | -60.51632 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff8a749a-dac4-3fb4-9e18-13ff0a57d201 | 3.14934 | -60.68567 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3449578-840b-3ec5-95f0-f304c12e21a3 | 3.15672 | -60.69645 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf45676-8bb6-384a-8cdb-874b19ab7f77 | 2.86412 | -60.8121 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 404b387a-5c00-391e-9ea5-6b73fb28487d | 3.12158 | -60.47723 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6253a56b-a80a-3aa4-945b-c8ef355ccb84 | 3.15298 | -60.68465 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc6af30-c82e-38c8-b109-d5323de717f7 | 1.86077 | -60.39754 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8008a6-1132-3b6e-b7cd-213a4c1e666b | 2.86777 | -60.81046 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4680b3d-0eb4-345d-9fa5-75e34cefbda2 | 1.72038 | -60.30042 | 2026-03-03 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77a88295-db11-3424-a673-5b19003afb78 | 3.15539 | -60.70055 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85bbadc9-1480-35cf-8cfe-c50d7596797d | 3.04991 | -60.65644 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eca69c3c-de7b-3415-a831-c62d0f92fe58 | 3.15106 | -60.69762 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 674187b2-65c9-35dc-b51d-12b4f79b98be | 2.31793 | -59.8654 | 2026-03-03 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12527746-d78d-3ddc-aa06-23a5778905f1 | 3.02524 | -60.66502 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 000da28f-20ac-3807-9658-d5ba9ebcd310 | 4.64799 | -60.69734 | 2026-03-03 04:50:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2cd3bab-eb84-3063-b4c7-94036212de03 | 3.12456 | -60.47316 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0651addd-022c-30e4-b5b0-96be0d657b03 | 3.04422 | -60.65727 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bdabc16-0c5a-3e4c-a253-b9dd0fee6cfe | 3.14882 | -60.68201 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b838f21e-9f9f-3693-bb0a-cbedd5122c44 | 1.86734 | -60.40389 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bdd8753-4c0e-384d-a70c-839c9273d8b2 | 3.03853 | -60.65809 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ae2d365-6758-397f-844e-2cebd64d2a70 | 2.31843 | -59.86873 | 2026-03-03 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dee233d8-d2ea-3136-bc91-b19b91581857 | 2.88942 | -60.62859 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15f90876-24dd-3a03-807d-52e67a690573 | 3.15476 | -60.69637 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0703eb7-36a3-3e6c-97f2-d06a6f556981 | 2.89 | -60.63243 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e369079-3b5e-3f63-bbb9-32a0db99a09d | 4.64302 | -60.70404 | 2026-03-03 04:50:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6f09186-b0c0-3ca9-9392-373377df952d | 1.65038 | -60.24321 | 2026-03-03 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7568335c-7498-3f1e-bdcd-3f7939393d17 | 1.95217 | -60.51748 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd64e2dd-d505-32e6-9cf3-4c837720e7d4 | 2.90467 | -60.61456 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d5ede33-1890-3fe4-afaf-9f7584d77438 | 1.86131 | -60.40112 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5de9ba7-a1c5-3227-b778-3178496089c8 | 2.67784 | -60.42078 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9433e45a-07bb-31a6-8535-4f84820698e4 | 3.12511 | -60.47693 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f254b196-664d-3f5d-88af-26c84ecef742 | 2.68687 | -60.06785 | 2026-03-03 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 701da7eb-b7a5-374d-87b8-6d7366b7bf94 | 1.64985 | -60.23973 | 2026-03-03 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ef43fcf-bc07-3b13-b957-10d4bfabb846 | 1.82748 | -60.85009 | 2026-03-03 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24c9bcd2-7080-3975-ae12-02ddbcaf4f7e | 3.12215 | -60.481 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f4cf24c7-4cfa-3498-92b8-93a1d03b03a6 | 3.12663 | -60.47265 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4820a1ed-e89f-3865-b748-318b0ea69798 | 3.15244 | -60.68102 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1238b86-5954-343d-82ac-f69ba65a768a | 3.11948 | -60.47775 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53893565-78ef-3340-8b8f-0f455733a89f | 1.95714 | -60.51274 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 915cb033-2c9e-34ec-ab0e-79162a0d8caf | 3.14729 | -60.68557 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11821e98-4237-3497-8a96-ce87d7972c6c | 2.8647 | -60.81606 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99bcdfbf-5778-3b3d-a2e1-4648d32eee33 | 2.86354 | -60.80814 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ef3f840-b3b5-3dc3-8460-0ebcbdfebf4c | 1.64932 | -60.23626 | 2026-03-03 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8168663-5985-30e9-9d57-8e16cb720a7d | 2.68195 | -60.07211 | 2026-03-03 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1e424d0-4752-3dd5-b702-3a8d37836785 | 1.83255 | -60.8454 | 2026-03-03 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5371c83e-5995-3957-8306-7b14b3ada19e | 3.5687 | -61.73394 | 2026-03-03 04:50:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92eb69f8-7e4f-3dbb-aae4-604e8ce83eb3 | 2.31894 | -59.87214 | 2026-03-03 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c44035b-1705-3649-8556-0156e8da0006 | 2.90525 | -60.61841 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4489dfc8-9883-30c0-b135-9c3dc37323e5 | 1.95772 | -60.5167 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70e0400b-0eba-3740-8f85-20c01bdf2098 | 2.90699 | -60.62998 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 604e4312-fedd-3c32-a602-8d2a72dada1d | 4.64935 | -60.62548 | 2026-03-03 04:50:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cf81624-8d14-3c0c-857a-878b2430fb39 | 0.71354 | -51.3707 | 2026-03-03 04:50:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cee5669-a7f7-3997-949b-db220ff43a26 | 3.9571 | -60.22448 | 2026-03-03 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a7bbdce-f1e8-3114-80d2-760a52fcf474 | 1.8668 | -60.40031 | 2026-03-03 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf27604-8796-3763-8dda-e180b206337c | 2.31945 | -59.87558 | 2026-03-03 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b40d4716-7798-375a-9353-c2ce61cb5af8 | 3.12003 | -60.48154 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72af9901-3f5c-3063-a1da-15395b1ca660 | 2.90583 | -60.62226 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9392e8d4-78d6-385f-9879-f4145dd31ed5 | 3.15733 | -60.70071 | 2026-03-03 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1cfc177-0b5b-3dbb-84bd-15ae27ef51ae | -9.51359 | -60.19019 | 2026-03-03 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7632cab0-5282-3803-983c-254fea1411a3 | -9.5144 | -60.18558 | 2026-03-03 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6688640-ab32-3cae-991e-40acc004c4e6 | -12.00902 | -53.94437 | 2026-03-03 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 709ff6a7-7d2e-3cc0-84e4-ae58ae5c5d2f | 0.49804 | -60.50962 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6da2e515-d5de-3477-870a-12308eff1362 | 1.35431 | -60.03462 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1029d20-7ac0-3897-9f0a-3942e9b56258 | 1.51563 | -59.92453 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b86845a6-d1ff-3744-9397-ac1a0def9a60 | 1.12691 | -60.5144 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbdbcd6e-61c8-3a9a-b3e4-b7e152ba74ae | 1.11483 | -59.19728 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67bb79a6-b379-34ce-a5d7-c8711b6cdc02 | 0.31139 | -60.4454 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edcec92c-01cc-3554-af9c-d4726d5e6f38 | 1.4829 | -59.92274 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1345080f-06f3-36e3-99be-a1be2247dc34 | 1.35917 | -60.05678 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14d40aa2-a4a4-3b1c-8220-7e60d5b968c2 | 0.87206 | -60.47165 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4efee0a6-0e39-371a-927f-219981017c37 | 0.06461 | -60.99302 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ca308ee-6846-3c4b-a666-7937084a5e6c | 1.36129 | -60.07016 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffdfb7a2-89cf-3213-9a34-a029fb275183 | 1.45651 | -60.07159 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 579fa7f0-41d3-37bf-a990-90d8a609eada | 0.92463 | -59.5555 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997bf2f4-bb26-314a-abee-6afa2b982fec | 0.87019 | -60.4719 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d35e0e04-dd81-3ae2-b753-58f6b5e4fe73 | 1.5167 | -59.93141 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8226efe4-cefd-31c9-8e09-ff81158ba7e7 | 1.51617 | -59.92801 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 263b759b-c271-310a-a1ab-ab7ec7786290 | 0.9414 | -60.18367 | 2026-03-03 04:53:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c38107a-af28-31c0-8aa0-02fdefb694f9 | 0.31031 | -60.43858 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23fb4022-bfdb-358c-a232-97b543b65b6f | -1.512 | -54.52461 | 2026-03-03 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b64fc89b-4724-3ab8-a5cc-79fd28e8d2f9 | 1.48821 | -59.9221 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71b50014-ee99-3b2f-a310-d76a6c5bdb9a | 1.11545 | -59.19865 | 2026-03-03 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ff5be1-1f4b-3820-ab42-15d0759961c8 | 1.12198 | -60.51881 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80976998-48bd-38b6-83a7-f30cfe0bffb9 | 0.17507 | -59.42696 | 2026-03-03 04:53:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d982d1-9e6f-3e70-b741-dc40e04f31c0 | 0.23372 | -60.51332 | 2026-03-03 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 831ac64e-6868-38e7-8cfe-d9133ed4450d | 1.33889 | -60.06644 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d3a7ba-ecb6-38a7-adb3-f5cdb5b48270 | 1.48339 | -59.92595 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0b4d396-eed5-33d0-b851-137e36b1490c | 1.47809 | -59.92672 | 2026-03-03 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
