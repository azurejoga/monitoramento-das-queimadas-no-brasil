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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a22edf5d-1f3f-32b9-bdef-723c2dd4af6d | -3.57994 | -54.51488 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e140e6-3d7d-3d57-96f5-ae1907f6c769 | -2.2981 | -46.53827 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dff4a794-2496-3a61-aee2-c3cb21e677e6 | -2.25832 | -51.09069 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2193c2ff-e55b-3706-85f9-25d9ca3f5e84 | -3.67608 | -45.76876 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0aca9d3-8aa4-3bb7-b211-195f8f9ad262 | -2.70954 | -46.28271 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1a8af80-09f2-366f-8427-eef231777970 | -3.39567 | -50.32326 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 13b1b4ff-bfa0-39f4-ac6a-bbd5a0cd773c | -4.2635 | -48.68935 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47aa30d9-24b1-36d1-b1f0-c95615bb5c8e | -2.21012 | -49.86554 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce375700-6c0b-3b0a-a8c2-22be25bac686 | -2.15932 | -50.91833 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2e6cf7a-614e-3639-a19f-fa1ad6282319 | -2.22438 | -50.38773 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe77cb48-61b5-3405-9d1b-fc03adbc1f5f | -3.4893 | -49.91658 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd27354e-c40a-34d5-bd23-19dc2781896c | -1.61631 | -53.31207 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f66967d-2bf0-3e04-93d6-4fca9bdde108 | -2.21867 | -50.62452 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 878a0847-d8e4-364d-9740-f44f689a9c3f | -2.57926 | -51.89003 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 235d6aaa-8283-3829-8e7d-ed514fe5c57b | -1.26213 | -51.7646 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c24364e7-838d-383a-a7bb-701ff1d7d212 | -1.48705 | -51.04217 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 711eab9c-e950-3ddc-ac0e-fa72925acfd2 | -2.6045 | -46.20464 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 824fbf56-154f-35e4-a7bb-02fdca24dc4c | -3.51888 | -53.81341 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bac4913a-736a-3c0d-a644-db9e643952f2 | -1.42102 | -55.27729 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1de9b343-6f93-3de9-96b5-54381bc60bde | -1.60368 | -54.95106 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5597354a-3676-3086-9563-83818969cc0c | -1.24829 | -51.74493 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b3539759-c741-3d74-a47f-53a33071ba49 | -4.70511 | -49.6368 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b863bea4-db70-342b-a5e5-c57c7355b046 | -3.86875 | -51.25391 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33a24eae-d048-320c-aecd-196c08f6d902 | -1.51461 | -54.18618 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 905396c7-0078-3b2e-869c-f9953f32f896 | -3.47265 | -47.68625 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c3e469a-e32e-3252-9854-c20e0870483c | -2.8029 | -46.80795 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 737309e7-50a7-378b-ab18-64327a4e2198 | -3.25133 | -50.11983 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afe80653-7d02-3ce0-b693-e3cbc78ee3a1 | -1.8218 | -46.38868 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b29acbb7-39f7-3527-aed3-0ef93615a87c | -2.45499 | -53.70101 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d67ffd33-ebf8-3905-b899-b2b087c9360d | -2.10886 | -48.82563 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4678a0a1-393d-368c-a6be-b541d9081e3b | -3.68285 | -50.11872 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ddc39649-3a15-35ad-9f89-c0ee4adc7baa | -2.592 | -54.0548 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a0a6419-4499-3609-8b6c-996f1f3d262b | -1.83638 | -46.64156 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c3304ed-be48-34b3-8197-dc02ba3b7204 | -2.07358 | -51.46939 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad2e7829-5e03-313d-97a0-bb8e15850896 | -2.4522 | -49.09489 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6c4056b2-9f06-327a-ae2d-8f33bd9259da | -4.53472 | -42.90561 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52b8ea2-1215-3aeb-9d20-30e39d5c71cb | -3.05327 | -53.42531 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d10ffe8-58ea-3d40-8f55-e5f4653bead1 | -2.19926 | -50.6832 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c4793ba-b64b-3558-8e4f-50581fc82533 | -2.73925 | -54.39449 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21fa8245-779b-3955-bed9-b33d8c0c9db7 | -3.03153 | -49.45028 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e71a4961-a891-3d3a-b5e9-a9e37d2e1ad8 | -2.26792 | -50.80922 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf5ac3f0-6ddd-3fed-988f-e8a425f5a84a | -2.65699 | -46.61003 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b5c4150-43b6-39c2-9ab5-f36bb9ec6414 | -2.83697 | -54.01619 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f92662b-3e0e-3c28-a759-611e7ede517d | -1.24113 | -51.61749 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84bf0a90-978d-3da5-9bfd-c7929ea041fd | -4.62332 | -46.61992 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e3c88f1-5c1d-335a-84e9-c2106981db47 | -3.2559 | -50.1129 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 693f588c-edc5-3962-bf11-a8abce0cc7a5 | -0.92548 | -51.63464 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb6546df-4dd2-3822-b3ed-bad7affd75d9 | -4.40541 | -49.65551 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a977a5ca-27b3-3710-a82f-8da03a484482 | -0.94912 | -51.63476 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7340bced-8d5c-3e2e-aad1-28e29cb196f8 | -3.55147 | -44.98216 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dcb0a2b-722c-3071-a1e5-4b206c6bc88c | -1.36403 | -52.54957 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bc5eeae-e943-3233-a20d-1c570425655b | -2.26381 | -50.46727 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0120ab15-2c6f-315b-9b33-9c58b0ba6540 | -1.49066 | -54.8259 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79919c12-503e-3709-9f19-3444b1297feb | -2.30605 | -51.26552 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c640bba4-8e84-38db-90d0-46bc08de892e | -3.32588 | -53.85442 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 389478c6-05cf-3141-a473-dd2934ed56fa | -2.0405 | -52.09711 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eceb4db0-eb64-394b-9f50-b15f58ca236a | -2.01735 | -51.17455 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 149fcb0e-cc8b-3ebc-a70a-55411b053305 | -2.20059 | -50.54166 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 106266e2-c690-3c7a-979e-d5cfb4901631 | -0.28549 | -51.61518 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7510ae11-8056-34bb-aa91-0b5829f88d12 | -3.67385 | -54.27392 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dd459ae-d919-3fe1-8141-f4eef59dbe5a | -3.13312 | -45.37123 | 2024-11-24 04:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93d8b614-4bb3-3f04-8254-65274f59fcf3 | -2.40089 | -46.98837 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd85f59c-f666-3f24-ac3b-711fcf90b0a5 | -1.20604 | -51.75172 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1015138f-d1c6-3750-98d1-f636777079b3 | -3.51954 | -53.78747 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78ab3d0e-879d-3702-9f9f-dc7381d6267f | -0.05202 | -51.23462 | 2024-11-24 04:53:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe6d66c6-dc06-3af3-9028-b3d1d3e2f25d | -3.25444 | -54.21741 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 677c8d06-0233-3752-9c75-b496f9ba915d | -2.23575 | -50.47029 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dd5e0c6-4491-3063-a9ef-60f48c0dcd5e | -3.47495 | -51.99466 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d625bade-3944-35ed-a187-2c8ccb873d20 | -1.81747 | -52.69562 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92908d5d-489d-39ce-a8f9-d2ad900639c6 | -2.40385 | -53.84725 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d04f3d81-ad00-32af-a823-8e519daebf73 | -2.81889 | -54.08572 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c40ca82c-71f0-3b92-8052-378a0273dd53 | -2.20651 | -48.92271 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad940f35-4c91-39d5-bdf7-c3f89a57a637 | -3.86513 | -44.1837 | 2024-11-24 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b7a4096-d528-3f04-b512-70e462355d9d | -3.49334 | -49.9133 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b5c8af1-5927-3c92-ac73-8074ec81c10b | -2.82232 | -54.08625 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c2d27fc-4c0e-3bfa-8457-de8cf28da73d | -2.08141 | -49.61179 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 020ee990-ab83-3a88-a215-3aed5a602cf0 | -2.09006 | -50.88279 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| defe58a7-1c79-3226-9ba5-dd03987e2efd | -2.56089 | -46.5574 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d0906c6-0c77-34f5-ab11-681937156482 | -3.77773 | -49.93066 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54fb015d-a34b-3d3f-ad67-572ae615f00f | -3.32401 | -49.90004 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfd4bbde-13bf-3871-afb5-8a73ae5dd524 | -1.5181 | -54.18669 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5864770a-068d-3f20-9ed6-110396da5838 | -3.32355 | -54.09095 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26856f4b-8c8e-3455-a370-52d6196698f1 | -3.52214 | -50.48079 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c068189-dc71-3ea0-a3ac-fbf38ddc1b4d | -3.28425 | -53.7807 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0854a891-a60a-37fb-a59d-6b1b066c222e | -4.08207 | -46.82925 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cc5605d-17e7-30fe-a132-8a6beabe4515 | -3.51945 | -53.8098 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| abb8909b-ea87-3334-b603-dcfe6f42e0ff | -5.19538 | -49.15834 | 2024-11-24 04:53:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 429a9e9f-db22-3526-a210-d0ca3fcf6338 | -5.57164 | -50.95021 | 2024-11-24 04:53:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3832ba24-cbd7-3032-a5ae-e23ca0c9b197 | -4.63974 | -48.84663 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea5c31ae-bf78-3b82-a4cd-6fb1801cba66 | -3.48121 | -49.92311 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e058a023-2a06-3c71-9046-cb548f38ac92 | -3.68858 | -49.60559 | 2024-11-24 04:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b24558bd-01b8-3408-820e-d103f601a2fd | -2.78725 | -54.04232 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a22a5839-d27e-3d16-a53f-25f7d3e2ab38 | -1.27953 | -52.24223 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63958dbb-444c-3e18-9d8b-014333bec638 | -1.69852 | -48.46692 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 580a3d49-7431-32b7-bda0-4013e72c5e16 | -2.12553 | -50.18792 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 258b9a0c-2939-3ad5-bd0c-134cb639aeb0 | -3.52159 | -49.93712 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 152a71fc-d2a7-39fc-aa01-e4f09e5cdfce | -3.26064 | -53.71016 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4fda9cd-c003-32c1-a13a-a8dfe6bda856 | -0.9528 | -51.71954 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10849b6c-3b30-3300-b628-3b25cc482a94 | -2.62129 | -51.79811 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e1051b80-ec5f-3814-b05a-9680dfec6950 | -3.55339 | -44.98486 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README43.md)
