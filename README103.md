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
| bbdd2cde-5aa7-3ba3-9592-a322ab2a2168 | -11.54325 | -60.15336 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6986927-2206-38ca-a8d3-f16b486cd3ec | -11.54185 | -60.28923 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa7f7b7c-86e7-3714-9961-629c87129640 | -11.50556 | -60.24722 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0059fd16-0482-3c62-ac01-b8940da5fa2c | -11.50495 | -60.25135 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dbbfdde-27f4-31db-a7d0-bf090668afa7 | -11.50261 | -60.24251 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f482ece-f643-31d9-8482-d53c24a0da26 | -11.50198 | -60.2467 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c58d887e-c749-358b-85bf-767e8c854df9 | -11.49904 | -60.24192 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe29c82-ab64-3ca0-a686-638f5a8cc291 | -11.49841 | -60.24615 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9b4a980-52ce-3e24-9937-37933befc105 | -11.29626 | -60.33841 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eacac990-6804-3b63-b6ca-9fa85c405c5b | -11.29566 | -60.34253 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667a4d66-a4a0-324f-a21f-96ddcfc5a4c8 | -11.29211 | -60.34192 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f3f5fee-0df9-3356-bcce-39c5ecbcb10a | -11.27468 | -60.36612 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5fe2f6cf-3fdc-3240-81a4-27aed286f0ca | -11.27112 | -60.36568 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d42dd83-f8ea-3882-b6d6-c0138fe3713a | -11.26817 | -60.3611 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7edf53a4-f648-31ab-83c0-f325e3b87a37 | -11.26756 | -60.36517 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b33df5f-674e-31fa-840c-d04faecbef08 | -11.26402 | -60.36463 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbb814b8-13c8-3f6c-b7ed-301edcc62aa9 | -11.26047 | -60.36407 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07f0eb68-021c-33bb-9a1a-6fdf79812b13 | -11.42788 | -60.42776 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccec28ea-00d8-3edb-ab5c-2405872c9873 | -11.42729 | -60.43174 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| effd2e09-873e-3030-94cb-e5313cf2dd40 | -11.42671 | -60.43572 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78de31bb-3ceb-320c-9221-74e89db06c93 | -11.42375 | -60.43116 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72484c48-c772-3fe4-b3b2-9e5bd9afc474 | -11.41726 | -60.42602 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc7b278c-17bb-37a0-a5a4-2e7f16af16b8 | -11.41372 | -60.40074 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf07b6c-06b9-3515-aa64-9ba237c8cfe9 | -11.41313 | -60.42948 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add7a780-7f3c-329f-8ccd-039615addf7c | -11.41312 | -60.40481 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1a55e0d-31d2-371f-9fa4-2bf7b0def742 | -11.41253 | -60.40883 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 395bda38-79e0-3e5d-bc7a-9694f91d8da8 | -11.4125 | -60.45848 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc72f1b1-48c1-386d-b51f-120f538e0237 | -11.40956 | -60.4539 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8430fb8e-7d17-31fb-a6bf-b4dcc1bf8f62 | -11.40899 | -60.4083 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce96ec0-c74d-3777-aa31-0f92bad672dd | -11.40897 | -60.45791 | 2024-10-13 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d96fdd5-6f2b-375e-ab1d-767d3424f9b1 | -11.4084 | -60.41229 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df9ae6e1-44d4-3a91-96ba-66ed1949dcf4 | -11.40722 | -60.42038 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b013584-78ec-3fb6-b4df-944375f31cd8 | -11.40426 | -60.39095 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd8c890-ad47-3143-b7a0-cf3b3d90d86f | -11.40367 | -60.41987 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8856b0c4-b3fe-3230-86e8-6f780ca7597b | -11.40366 | -60.39507 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e121c062-2745-3d56-aa11-f8c5a3b096bf | -11.40308 | -60.4239 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a5bf51d-ffec-3f5c-b570-da2fe1fb59a5 | -11.40012 | -60.39448 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a00cb86c-6492-397e-89ab-64502f745add | -11.30806 | -60.43127 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cb76434-1295-3cc7-b321-6fc14bc4061f | -11.30748 | -60.4352 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 363530a3-7174-32ce-9b15-89cd107eeb9b | -11.3069 | -60.43918 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0964e1ec-05b5-389b-a2a6-1aabff72239f | -11.30453 | -60.43071 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb5573b1-f95a-3e23-a8d0-48cf42e88de8 | -11.301 | -60.43008 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cffa9e09-6a43-3e9e-b1f2-7acafe5945c2 | -11.2874 | -60.47359 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89039d27-7605-3616-a17a-61aa93144018 | -11.28682 | -60.47756 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df13cc65-8f45-3b9a-8f8b-353d2373fc65 | -11.28386 | -60.44842 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c9157fa-bbc8-3019-8d08-636484413618 | -11.28091 | -60.46864 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 368f741b-69fc-3041-8f43-457568c668ad | -11.28032 | -60.47266 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56b46966-4438-3b63-8bd7-bc9dbdfc3d51 | -11.28032 | -60.44793 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c75392e-bb13-377b-a7dc-63bab9b6f409 | -11.27973 | -60.47667 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 285368ce-a251-3ce5-8c54-f09b68fe47b3 | -11.27973 | -60.45198 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 40c85a0d-641c-345f-8e63-dbc7ceee4458 | -11.27738 | -60.46803 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5549b064-d20b-3eb3-9a4f-06940f1f9dff | -11.2768 | -60.47202 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14fc0d7a-eed3-3b72-8d9b-4d3ccf5e3154 | -11.2768 | -60.44726 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e2ad27c-362e-3303-b52f-419aca9fcb4a | -11.27622 | -60.47602 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfdbcf07-7a14-3032-b695-9cf90ff99ab9 | -11.27621 | -60.45128 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4b33cd1d-f57d-3fdd-8662-9123c343dc17 | -11.2733 | -60.47128 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 936ec886-c4ea-3ed2-8fe1-0047e01a14d9 | -11.27329 | -60.44649 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9b080b8-0de0-3450-b9cd-4e3b878b9196 | -11.27271 | -60.47531 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12a052d7-bd92-30e1-9489-22790c473d9b | -11.27271 | -60.45052 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d412db55-70a4-320c-af65-9b7b0b1b6593 | -11.27212 | -60.47936 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5c51944-6dfe-3b1e-9b0a-174c9db3d40f | -11.27037 | -60.41903 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afc197dd-e3ee-3335-b25e-1aafd727186b | -11.27032 | -60.4172 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dddbf4f6-3559-3e3c-881c-75148ce6a896 | -11.26684 | -60.41844 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1454d8f9-ab1c-3b56-a6db-f88ba5338ec7 | -11.26679 | -60.41658 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1347e442-6b80-3768-9fbf-87c7c5a2da37 | -11.26331 | -60.41783 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4be23fd-bfdc-3216-9aa8-60107b5ef42f | -11.25978 | -60.41723 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 836c5daa-fb37-350d-8dad-ec58d5f406b5 | -11.24496 | -60.44383 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30129713-bfaf-3c5a-9740-416c5ffaaca4 | -11.24202 | -60.43928 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b0febbe-fa7a-373d-ade6-7fe3e2441cbd | -11.24142 | -60.4433 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b06831d9-5135-3e25-a203-d1f1f2759451 | -11.23614 | -60.43019 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d3e09d-25d7-3882-8ab1-68ce37ab8e39 | -11.19841 | -60.4409 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01e9cc0f-7e6d-36fa-8869-fcc264244503 | -11.17074 | -60.45725 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ff9674d-41e1-313b-b16a-1dd0d49ecf2e | -11.17015 | -60.46125 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ad1e827-1341-3a62-a061-271c96070229 | -11.08342 | -60.4118 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02d391e5-be9d-3bad-9177-70978e0e3748 | -11.06163 | -60.43728 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c09b0c8-e5f9-3ac2-a461-7144aeb89d6b | -11.0581 | -60.43673 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bb13b9c-e8fd-326f-98f1-c8d306ec198b | -11.2329 | -61.22114 | 2024-10-13 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cd31318-068e-33f6-b49e-d24ff4b72b86 | -11.22948 | -61.22061 | 2024-10-13 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 591a8b82-7e8b-3b1f-ac41-07b656c7253f | -11.22548 | -61.22386 | 2024-10-13 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7967a08b-51c3-3f5c-983e-f1f3be14e482 | -11.18505 | -61.28303 | 2024-10-13 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1099080f-ea99-34c9-a0be-46e8e34c94fc | -11.10462 | -61.37507 | 2024-10-13 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059fdb26-4afa-3455-8ede-2a5b8cd1569d | -10.97596 | -61.09036 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c76a8b8-c6f4-3225-8b67-73be75878fe9 | -10.97545 | -61.1173 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d6dfbb-0d2f-384b-859c-4b8dc6470d71 | -10.9754 | -61.0941 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2456ebad-fa2e-32fa-b51b-69c0658aa3ba | -10.97309 | -61.08606 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ada37969-c22d-398c-9ae9-e537b4561563 | -10.96965 | -61.08554 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e60c842-072d-3d02-9317-0f0ce37a082f | -10.96622 | -61.08498 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c20a7fc2-f8ad-39ff-9b59-846d4d0ac9e6 | -10.96279 | -61.08443 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c960ef8-a1b2-3cf8-be3c-b85c405f2e3c | -10.96222 | -61.08823 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ba876f1-1cd5-3feb-8ec5-e2b27ae43012 | -10.95998 | -61.10334 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71754074-c87a-3156-bf6f-e501420d2f92 | -10.95654 | -61.10287 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c5e58ae-6eab-31ac-a183-dbf0cf61ebd6 | -10.9531 | -61.10238 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c703988-c544-3963-8282-6a9d80ead559 | -10.94917 | -61.12883 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d1333af-647c-33dc-bb98-817efe3aa5e8 | -10.94861 | -61.13258 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 282bb00e-9014-3922-a425-acf899d32932 | -10.94661 | -61.10209 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c298a1ab-e489-329b-b525-7d00436cf9b3 | -10.94604 | -61.10585 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9fb0aa-b781-3157-a860-98a36901bcf8 | -10.94603 | -61.12898 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e290a80-808e-3754-9780-2f02b9b8f329 | -10.94574 | -61.1283 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5628f330-a452-3eb8-a661-b8281a53c0e5 | -10.94546 | -61.13273 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52769005-4400-315c-8bc0-20c36a470892 | -10.94518 | -61.13206 | 2024-10-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README104.md)
