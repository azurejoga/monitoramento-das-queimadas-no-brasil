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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8872df2a-9634-37a9-a2bf-75a46b472539 | -9.87274 | -65.02998 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1707d10-3d41-3e63-bc37-13b48fa82188 | -8.84838 | -71.31549 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 422d5ecb-635a-3475-88cb-256bda72d71d | -7.58139 | -61.3353 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6934bf-13ed-32e6-b5f2-5b4c09fd375b | -9.25128 | -65.50234 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 704ec69f-9104-389d-bbdc-c1bab5dbbcf6 | -8.99386 | -65.44656 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7ed5ee1-2e18-342c-8178-6158cb62e025 | -10.48386 | -64.49731 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d197a5b8-07c2-3ac6-8d7d-ae67b36bc903 | -7.48723 | -61.40544 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fc34951-32c6-3808-ad6b-1fcbf06e4cce | -10.51032 | -64.306 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bb91dae-32af-3970-9a61-f3ca088f6905 | -8.95068 | -62.38988 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed305958-884b-30c8-9837-8c11a0366a43 | -8.95656 | -62.38469 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64cd2edf-7122-3b73-8f27-57f6e30a936b | -8.94502 | -63.27814 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 326862fe-4727-3d62-8404-bcc6ee964a9f | -10.46592 | -64.49476 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2b84da2-65bf-3093-85a6-71371ed1e223 | -6.92177 | -69.99628 | 2026-08-29 06:14:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f48488c-dc84-3f93-9732-8d71a49f8e23 | -8.95189 | -62.381 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f4731e2-bb5e-3b69-b705-a1ea2d97d59a | -8.60264 | -70.21295 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f26237be-1e34-365a-b300-a23e36cf158a | -10.47041 | -64.49535 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c8cb3a91-9912-3105-9f72-87aa7dd1ffd6 | -11.03172 | -57.2133 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b720bd5e-9078-3019-878e-0d900cd3e382 | -8.94574 | -63.27299 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 308af193-f3ff-347d-87ff-7cc4aa931c0e | -9.4783 | -68.51937 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9566bf8f-a3ef-38c1-9e24-230ea909fe90 | -8.98754 | -65.44246 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 267a0208-081a-3c38-a182-ab5d1676beb4 | -10.46654 | -64.49023 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f2544a6b-9d1b-309b-abab-4fb6bdb3d7c8 | -9.92629 | -60.42602 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11f5cfbf-ba05-35df-82a3-e6da30507a8e | -9.50803 | -65.57935 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00c1371a-1f4d-3747-90e5-ae3908181b15 | -9.49273 | -66.75475 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1bc99e4-7178-35e8-ab4f-15bd0b215841 | -7.57458 | -61.38493 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c09a711-a579-3789-b125-88d83e1b66fe | -10.47937 | -64.49667 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7c6183ed-6ee9-3cf6-8874-21342bb8e50f | -10.50857 | -59.63418 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 502ca76f-8316-3a9b-800a-99f68fba66dc | -10.05629 | -68.84028 | 2026-08-29 06:14:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777189a5-9a3e-3f3e-a2ab-6f89c03ca933 | -8.59709 | -70.21161 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 600a43b2-604f-3edc-a024-777d233e9162 | -8.94825 | -62.40762 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 401ed7b9-1bdd-3ed7-8ab5-fbc2ee8126f8 | -7.59649 | -61.34422 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79eb11cb-a74d-3bb8-87b0-187f11a25a3c | -8.94979 | -63.2788 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 321f4e72-b317-329f-b7d3-8b127f91b91c | -9.00105 | -65.45517 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a45b655-137b-3956-b870-628717f3227f | -8.98808 | -65.43877 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a51f5b34-af48-3ec8-ba0e-5e1645a33a8d | -8.15361 | -64.00197 | 2026-08-29 06:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5958bdcc-d775-31fb-9ab1-a74bded0ca22 | -11.03658 | -57.22243 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0849b887-b7a1-3b62-8047-8e2739bbfbaf | -8.82434 | -70.63444 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 379e1ea5-c7f5-35e6-84ab-99e133e5c031 | -8.99468 | -65.45102 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2066309-66e4-34d0-a1ff-c901f92cf830 | -8.95051 | -63.27367 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 75e54432-2ebe-349d-bb90-0a00536b7758 | -7.56926 | -61.38417 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78f0067b-a1af-3169-93cc-41d1f31cd0da | -7.59161 | -61.34015 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac734121-604a-3b4d-b226-f12a0f24de3c | -5.8894 | -57.7708 | 2026-08-29 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| aac707b1-c318-3238-8277-a4bcd13fca2b | -6.6315 | -43.7533 | 2026-08-29 06:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5247fa0d-41c7-3b9f-a9f1-9c1e0497f7cf | -6.7884 | -55.6635 | 2026-08-29 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 997ec623-5454-3c5b-bf16-5cfbf46f82a5 | -10.4794 | -64.5012 | 2026-08-29 06:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1723d16d-7eba-39ae-bcf7-1ee94a70ac61 | -10.4608 | -64.502 | 2026-08-29 06:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e61424ff-da04-330c-85c4-820891840e3f | -5.8895 | -57.7513 | 2026-08-29 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a0defc4e-e6eb-3e5e-bf1f-9f277800e223 | -6.7699 | -55.6644 | 2026-08-29 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b4f09f3d-8749-381d-aca1-fb17508b52dc | -6.7883 | -55.6834 | 2026-08-29 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f8cdee2a-f3a7-3ecb-b9d7-61271387a3c1 | -6.6317 | -43.73 | 2026-08-29 06:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| fc621b71-da2c-36e0-a5c4-2b40cb5f4369 | 3.11038 | -60.7118 | 2026-08-29 06:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 504fbd3b-968d-355b-a868-95c23aeb18bf | 2.408 | -60.88261 | 2026-08-29 06:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b4906c5-4a82-332f-87c4-794a9ee89ef6 | 2.41507 | -60.88133 | 2026-08-29 06:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 624bf591-27a4-3472-b4a3-fa9e170e67cf | -5.8894 | -57.7708 | 2026-08-29 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 30187e60-df1e-3538-8c08-8a569cddb68e | -6.6129 | -43.7317 | 2026-08-29 06:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 9d84c939-3069-3c14-a11f-8b47785f3e68 | -5.8895 | -57.7513 | 2026-08-29 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| b9f34d8a-b726-3a37-a079-058f2f4b2132 | -6.6317 | -43.73 | 2026-08-29 06:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 7bd3a5da-1957-3be4-ac5f-decf7ba6ea81 | -6.7884 | -55.6635 | 2026-08-29 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1be0b61a-5da7-3e5b-896d-d509f7ac380b | -10.4794 | -64.5012 | 2026-08-29 06:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| abe255dd-6e3a-3a3c-b313-2b962441ca37 | -6.6315 | -43.7533 | 2026-08-29 06:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| e8b50f79-26f2-313c-8979-03d325a454d8 | -6.7699 | -55.6644 | 2026-08-29 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a794f17b-1fcd-3889-90aa-ea6b4178b17e | -8.95018 | -63.28418 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a784cf9-ab29-3917-ad81-cf7cf5fae90e | -9.04229 | -65.43005 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4466677e-0d47-3f8a-9094-3edc32f8851c | -9.06692 | -65.41264 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5a0104a-9db0-3298-a148-7d4756152727 | -9.00054 | -65.45541 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c5c8e56-d204-36b5-b694-51642b799440 | -8.59644 | -70.21149 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50559562-2013-3aca-8471-d6c9d942b439 | -8.98289 | -65.44279 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fffc2a38-83c9-3491-9c54-e940c98855e9 | -8.99551 | -65.4445 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b332f9e8-d3fa-3c2c-a1e1-2fa0c71b85a9 | -8.63771 | -66.53662 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d4e9857-874f-3393-9837-e95fc376bb34 | -8.99488 | -65.44952 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 349fe651-d077-3d67-bfb0-c542d59b7cdd | -8.59579 | -70.21619 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a3616b-9dc3-33d3-97f1-c5abc73e42c3 | -8.14834 | -64.00517 | 2026-08-29 06:31:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fca733c2-e31c-3dc8-b7c0-266bcf0fc0f8 | -7.54587 | -70.00002 | 2026-08-29 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb54236d-ab50-3b18-99d8-04cbf3c3d383 | -8.60559 | -70.21272 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd5e660a-04dc-354b-bbdf-5909e59137be | -8.60036 | -70.21681 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b40aeab1-8228-3b8d-86fc-035119595f2c | -8.9541 | -63.2788 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 282e9567-f026-3cac-9d99-59fba33da3c4 | -8.63131 | -66.54002 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 763c5db7-aba5-3023-8779-2b8adb5a5856 | -8.87521 | -66.8978 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b968b3a-0bc2-34a7-8518-a8983c30109d | -8.34566 | -70.84737 | 2026-08-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53b9643e-3487-34d1-8e22-80695d2a8f9e | -8.94607 | -63.28502 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3572f257-dd72-3ec8-8264-3013b39875d8 | -8.59711 | -70.20678 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bb2322e-8c16-34c5-b405-2427b09e2bce | -6.92386 | -69.9949 | 2026-08-29 06:31:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| badb4ee8-202e-3d8e-b6fe-9ab1cd66ec40 | -8.60493 | -70.21743 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae137dab-7441-37aa-ba16-0b5ca9b48167 | -8.94693 | -63.27792 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ae6ab53-3d8e-30c1-90b1-6d43e26d0163 | -8.9892 | -65.44367 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62899f93-f79e-3d19-acf6-eeb5b3106680 | -7.003 | -71.65961 | 2026-08-29 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2fbc568-25d4-3097-baad-41fc3e892b72 | -8.94391 | -63.27625 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80cf640d-69bf-30b1-a624-1644a44c3121 | -8.34858 | -70.84991 | 2026-08-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d64ef2ce-3a5f-3d7a-8168-09e937f63e24 | -7.00248 | -71.66315 | 2026-08-29 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed26142b-81a0-30ec-a36a-ac1df5649d65 | -8.94779 | -63.27077 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb4392e9-1f06-3569-9f78-93e6a6f16900 | -8.87469 | -66.90187 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ea4f291-e545-3170-950d-eae0c9458a05 | -8.34942 | -70.85226 | 2026-08-29 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3d40ff0-1b4b-32a5-a03e-d8b66a1e30f3 | -8.60102 | -70.21212 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57140660-8028-3256-9c05-0ea269822c3e | -8.24715 | -70.10281 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56d48c26-a489-36e2-90ba-759867e26298 | -9.04796 | -65.4359 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fe7eae2-1be8-36b0-a60a-0b77eac7d7e9 | -8.60625 | -70.20802 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a13b86d-3ab2-3946-8c1d-504c459feb4b | -8.2478 | -70.0981 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ba046db-2ed4-3b8d-a760-8a7b855fcf33 | -7.00705 | -71.66019 | 2026-08-29 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94cb5ec5-99a4-39da-9ca7-1a7b06d896d5 | -9.06258 | -65.42222 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07b8c239-4222-3d1a-a84b-3884a4f325fe | -9.06324 | -65.41712 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README72.md)
