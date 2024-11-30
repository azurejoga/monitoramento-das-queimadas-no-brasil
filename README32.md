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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6235b944-e311-3155-9f94-33d8f4fb7f8a | -3.24933 | -50.61811 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e9612d2-2993-3161-b467-f99aa481b819 | -2.70322 | -48.67725 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c130966-8577-338b-a00f-4194389484a8 | -3.79198 | -58.97298 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a29a308-c7cb-3d18-8c38-e27287dd1a6e | -2.97501 | -48.00121 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e869b259-54b5-3474-9e64-fb4fdd921409 | -3.46684 | -48.93043 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af551b0d-91e5-3165-ac1f-ee36fde6df9c | -3.23809 | -48.73666 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b30f4e2a-fb1a-34a7-b655-d63215d4b556 | -2.85134 | -46.68034 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e1e5b56-5511-3557-bc6b-2c71c694c19a | -1.96895 | -53.10341 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd988d4a-469c-39f9-b52d-20ff8d1cad3e | -5.036 | -49.98585 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e652deeb-bfc4-34e8-9386-31d32f045090 | -2.6652 | -48.7909 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a1fab8f-23f5-3e16-a7b8-dddf2481f28c | -1.51746 | -52.03365 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 677e9f7b-7613-3673-aebe-1e4557926647 | -3.7034 | -47.1398 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21ad6df1-e428-3ba6-b119-71bbe46f7f2b | -2.08096 | -48.54465 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15db657-694e-3ef4-8693-38b0f2272e83 | -2.27671 | -46.42857 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fc98ee-614b-349e-ad11-e6adae0cc181 | -3.28548 | -50.60884 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8a72643-be22-3b52-900a-3068630f7314 | -3.05227 | -51.06397 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b75ad621-9c96-3fab-b212-6f225afff697 | -2.93368 | -48.00513 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa15dbf6-c0d9-3bd5-bfd3-9ee22864169c | -3.33276 | -46.60711 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b07027a-f5c0-3b6d-b299-afb1811cc0b3 | -2.01439 | -51.43216 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5abe520-ff87-3874-be33-16dbee94ee72 | -1.78956 | -52.74455 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c13ee990-316f-362b-a2c2-c9c5b7669ad1 | -3.86036 | -46.6644 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1368847c-9190-3818-88c7-b174156fa7a5 | -2.19529 | -53.57045 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b419f60-1390-3450-a147-f4edfa39bfd7 | -3.25713 | -51.2115 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d22eab-2cda-3f92-8008-d90e6b19e2d1 | -2.19846 | -50.57945 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8cc6eb2-e94e-327f-8e9b-3b26061198bb | -3.41983 | -50.35788 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7010736-a52c-3b3f-a369-cfafc0f26f34 | -3.12594 | -53.26745 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 684128fa-39c7-3fb6-abb1-02a25c18d746 | -4.87529 | -41.28966 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 256f51f3-dae1-3be6-9573-1099cee44703 | -2.45893 | -48.54399 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be2a7ee6-00c0-3c37-9269-2d3ea991998b | -3.21047 | -53.8433 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0da1cfe-2e4e-3ed4-b86d-a79646110c0e | -1.85588 | -55.6183 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33b0a22c-3585-3ddb-8e70-18bc74587760 | -2.83379 | -54.03462 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04310070-7a22-3094-93b0-b901dd655287 | -2.45506 | -46.56727 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71dc1dcc-7e7b-3357-8efb-97934d52779d | -4.05213 | -48.33579 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c2ba1a-cf3c-36d3-8b7c-28285e4cc368 | -2.67281 | -46.6113 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afe53d61-e17d-3919-80e8-18fa76d4d29c | -1.74871 | -50.83107 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36d9d2c3-6ba5-3a83-9ff9-3fb896835854 | -4.29017 | -44.10796 | 2024-11-30 04:40:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ced66b0-d461-3f05-8ab0-5c0866f845f0 | -3.11151 | -53.75674 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54333319-f879-34b5-8766-42bdabeb7bcb | -3.98304 | -41.50713 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 22d0168f-249c-315d-92cf-68b0721b2489 | -3.56598 | -46.33798 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f82cbf-1eee-3c31-9c62-3e989d8a73bd | -3.10656 | -49.44871 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 046d6e59-f1fe-3d14-b00d-d0ff1b0b5a01 | -2.446 | -57.88749 | 2024-11-30 04:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca9d1afe-3dce-3cb7-a8d3-f2965b23b8a1 | -1.39494 | -53.6339 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 948e3860-2130-3254-94fb-1bdfd7ddbc17 | -1.07287 | -53.6403 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b3e2cb5-5b2b-3483-a89c-a748d314a97b | -2.84654 | -54.03296 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5480c1aa-ad55-3413-b440-37e31de45728 | -2.86269 | -53.32203 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 233974b4-a52a-30c9-a008-66fc74b512bb | -4.18743 | -48.64795 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 024d95cf-2f0c-358c-bcf0-14d367da3399 | -4.87866 | -41.30143 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c5008faa-696a-3ab7-85b5-d0723d7149aa | -3.51661 | -49.2618 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d99bf024-00cc-305f-b139-55d671e11268 | -3.2231 | -50.44425 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96a57ab1-74ba-37b0-84c5-cfdcee54b979 | -1.36041 | -55.18158 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3aec42fc-a83a-3ee9-8a61-70b74e7cb06e | -2.92121 | -48.58839 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0016a56d-663c-3cc3-98c9-9ef034c6dc2c | -3.16788 | -46.54365 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25054e03-5443-3d9d-8144-fbf196837e48 | -1.41128 | -51.58236 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4610b93f-65ed-381b-bd12-792f80218530 | -1.86136 | -50.80569 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 494c0837-0901-372f-a5ad-7a6bfa02e5e8 | -2.10874 | -48.21444 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa7091e1-fec5-39d8-b3e5-294645779ab3 | -3.24899 | -53.62568 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f6faa09-640e-3dd9-a7bc-3c34f58f646d | -2.33644 | -47.40453 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400f480e-f214-329e-af9d-700b7fca6811 | -1.36958 | -51.97295 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 815d9c03-fc9a-3f2d-8473-dd55c8c85cf8 | -3.88299 | -46.67976 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c198660-7053-324b-9c4c-a27815d7e6eb | -1.26452 | -54.55396 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 01c2c9d7-351f-3ad8-8b0d-6e3ba704cd40 | -3.49537 | -53.84328 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f60c481-1607-3e70-b67d-a7d2fa850b88 | -1.63022 | -53.86185 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0313e832-9195-34e3-9aa5-3cbfb9a942ff | -1.74813 | -50.83484 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d58498-a4c2-3b79-b863-e1b5e73e2c7a | -1.74695 | -47.35052 | 2024-11-30 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85d131d9-f401-3362-88ce-a6ab25427e9a | -2.59728 | -47.03424 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48879422-1ed5-305e-ac1e-3414a49f67a1 | -2.11483 | -50.59698 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcf9a460-fe85-3ccb-9140-5254b25aa72e | -0.85368 | -51.75138 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8b40e4-e08a-3392-ab1e-52ab108821aa | -3.46343 | -48.92635 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8929e88d-4694-3169-8943-425084cb9437 | -3.98293 | -46.64303 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19f4f603-8ab7-3666-8d63-672f15b01bc0 | -3.93566 | -46.7191 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7803b12-b6a1-3147-b16d-be295f868a97 | -3.71121 | -53.75217 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77778c3d-0adf-3d53-b177-72db977fea1b | -4.68679 | -42.37142 | 2024-11-30 04:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82d3c090-4165-3eb2-8ce1-4a37f51c95af | -2.95139 | -49.4417 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ca97b0e-62f6-31b9-b4cf-0800ffc46f33 | -3.49706 | -53.83283 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c5ffb57-814c-39e6-bc51-1b975cc9e6b8 | -1.92288 | -52.88347 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8f6951a-934a-352d-ab47-615510b3e6ae | -2.83263 | -52.94596 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f170a2e3-6d62-3d00-8ba0-738fb8f44f0c | -2.58979 | -48.20425 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36d9ce4b-23bf-32be-b9d9-b1f4b912ea2f | -2.80549 | -51.58741 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8feb1c4b-f048-3278-bbc7-4904d49f653f | -2.46081 | -46.5759 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b5b5227-7a16-3263-aa54-2997d00c7c29 | -2.87191 | -54.00391 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09a1e785-801d-3484-a713-c9aa3524cb57 | -2.10543 | -48.21392 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29d0b1f1-e84d-3536-9b76-8bc43b243709 | -3.54843 | -50.18883 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4425ab55-61b7-3198-85e9-db52f550aa2e | -3.08995 | -50.35762 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa4d715-57e2-324c-8db2-57ff8dc0565d | -2.82381 | -51.95287 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3519380f-4e05-352f-97b1-d38af12ba8d3 | -3.41588 | -50.16481 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d8556f8-8480-3ecf-a8c8-08d117ddd0a7 | -3.67168 | -51.29779 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73763752-206c-3e52-b383-8943811bb815 | -1.30534 | -55.74492 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c53019d-27fc-3ce7-b7ae-9b26e9041402 | -3.60539 | -49.97821 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f211511-1fb8-3fa8-b7ee-e6c800b85406 | -3.00026 | -50.50944 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42338c01-58b6-3523-970a-46a99b839e6e | -2.7225 | -46.24036 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afeb863e-e82f-3e87-96a6-7e364f685c99 | -3.52785 | -50.38543 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34c70334-9b82-35b7-87c7-05ff79d78557 | -2.7505 | -51.66027 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e146b245-77d8-3c9b-9b0e-4e41da1ae1a0 | -3.86031 | -50.15128 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73d4f8ca-3969-309f-95a3-0edcfb6dd573 | -2.32649 | -50.6822 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a699db66-56d5-3ea3-909f-7200719c90dc | -6.22604 | -47.28392 | 2024-11-30 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd941a39-8674-32e9-bcc5-12607420bf9a | -3.82515 | -46.60446 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e44bd25-8580-3890-8d38-3dea5d7988c6 | -2.55795 | -47.03613 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0427529d-9ad5-3854-8235-abbcdb067e6e | -1.05501 | -53.2085 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57022a07-5ca9-3e95-8527-1d25e6608ecb | -2.61224 | -46.55227 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8634841-7f95-3058-ba61-4b0385e8499b | -4.14299 | -47.85965 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README33.md)
