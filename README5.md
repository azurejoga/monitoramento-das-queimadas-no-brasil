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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4cf5172-81e1-376e-a7d4-c3bbd28c238d | -8.2413 | -44.8582 | 2024-10-15 00:17:02 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48499872-99b6-335b-9427-e90c204ba82c | -8.9176 | -47.897999 | 2024-10-15 00:17:02 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 610e100a-ba8c-3a56-a0f8-813fcb1932cb | -8.921 | -47.914299 | 2024-10-15 00:17:02 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 502f4592-82c5-3297-b280-3b7482e50b5f | -8.9078 | -47.900002 | 2024-10-15 00:17:02 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04f8fe70-f6a2-3fbe-8985-a9b6a7bc0256 | -8.9112 | -47.916302 | 2024-10-15 00:17:02 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c75ee7d1-f9ef-3458-aa96-1d35f8dd8411 | -8.8981 | -47.902 | 2024-10-15 00:17:02 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37f38b02-24c8-3757-97cb-a082cb802f77 | -8.9015 | -47.918301 | 2024-10-15 00:17:02 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6adc1508-4ad4-3878-a60c-f766ace67fc1 | -6.2649 | -43.892601 | 2024-10-15 00:17:02 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8d7541-d1e3-3bee-82a5-b835ad4b9b35 | -6.2667 | -43.901001 | 2024-10-15 00:17:02 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4dd38732-8953-321a-bf10-91634eee8e09 | -5.6581 | -41.246201 | 2024-10-15 00:17:02 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19f90343-d437-3a83-afe5-653a95f663b7 | -7.0338 | -47.3605 | 2024-10-15 00:17:02 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68fc15bd-a799-3d00-8229-07cfc03bbf7e | -6.4099 | -44.5924 | 2024-10-15 00:17:02 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7df4f2-17ed-33af-9033-c1a8e1340da5 | -6.4119 | -44.601501 | 2024-10-15 00:17:02 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ead0d10-604d-3f7a-a8de-145846a13b3f | -7.7231 | -43.195999 | 2024-10-15 00:17:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79d31bfc-a453-3efa-974b-c53d18296cf5 | -7.7249 | -43.204102 | 2024-10-15 00:17:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dfc4dfc1-1935-33cb-9970-81cd07c2de72 | -7.7267 | -43.2122 | 2024-10-15 00:17:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03229dc8-d494-3454-8a24-8da2fdd89204 | -7.7142 | -43.248798 | 2024-10-15 00:17:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab9bba11-455b-38f1-a7ab-d8a92e6ef3ca | -7.6893 | -43.228802 | 2024-10-15 00:17:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29bc2e1a-9a34-3e96-bd84-61a2036b8153 | -5.529 | -41.448601 | 2024-10-15 00:17:05 | METOP-C | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc1b0da9-2d53-3267-b7b8-5fc18f7fe55b | -5.5306 | -41.455502 | 2024-10-15 00:17:05 | METOP-C | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3268f36e-8a2e-37ef-a488-b925434800b9 | -6.1337 | -44.1339 | 2024-10-15 00:17:05 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97a35604-ae5a-301f-b791-02fda54f5051 | -7.7747 | -43.894901 | 2024-10-15 00:17:06 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b19d3fcd-573d-34a3-b401-40e8a1c51291 | -7.9434 | -44.5243 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e430cb74-e241-3ced-8c16-b8cb90f748b8 | -7.9454 | -44.533798 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 163a843f-b348-30d3-ae95-6067094d3787 | -8.0023 | -44.794998 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1634880-bbbb-3de2-b0f8-a5a5cfdc3795 | -8.0045 | -44.804901 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1051d21-f1ca-3cb6-8d68-f8c8612db5c1 | -8.0066 | -44.814701 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 964c5c57-313f-3366-bd9d-27ccc7fbbe3d | -7.9315 | -44.516998 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb3ca39a-3762-36ab-8c1c-665d50f5ede6 | -7.9336 | -44.526402 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 097f0e70-0f48-3408-8e65-95709fbf9884 | -7.9356 | -44.5359 | 2024-10-15 00:17:06 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9de5d67d-1feb-3793-9092-54889ce4088a | -7.8846 | -44.5369 | 2024-10-15 00:17:07 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c697b62-ad86-3e2d-a356-cc8a3e14690a | -7.3214 | -42.2243 | 2024-10-15 00:17:08 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4026c49c-0096-3213-891e-66dac7326454 | -7.2036 | -42.158298 | 2024-10-15 00:17:09 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9243a830-bac3-3e24-898b-47d830b5bc05 | -7.4297 | -42.985699 | 2024-10-15 00:17:09 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c12d1e1f-9b46-3510-9747-0584da1f9fe7 | -7.4349 | -43.009201 | 2024-10-15 00:17:09 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0ef768a-4459-33b7-9eb7-fcaec200f073 | -7.4153 | -43.0135 | 2024-10-15 00:17:09 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40c09381-5c15-3a16-8423-1c1aab15262f | -8.4587 | -47.791801 | 2024-10-15 00:17:09 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a560e45-4cb7-3dfe-a1f4-e2b19205b697 | -8.462 | -47.807499 | 2024-10-15 00:17:09 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c749e53-8536-316e-ac4d-09ff103b1e2c | -8.4456 | -47.778 | 2024-10-15 00:17:09 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2f0d680-5c1c-3481-8e34-d04217386b2c | -8.4489 | -47.7938 | 2024-10-15 00:17:09 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e3f6109-5894-3494-b0c2-7969e6e94b41 | -8.4522 | -47.809502 | 2024-10-15 00:17:09 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a90646f3-3e35-3a20-a8de-c8267e1ed05c | -5.0515 | -40.892799 | 2024-10-15 00:17:10 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 035a0b41-9124-31d4-86b6-6a1ee757f936 | -7.1741 | -42.6231 | 2024-10-15 00:17:11 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 038b0ee5-f39d-3a58-9d7d-db005f47d26a | -7.1757 | -42.630699 | 2024-10-15 00:17:11 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67c6ec98-e703-3018-b775-b2b50c69a471 | -7.1774 | -42.638199 | 2024-10-15 00:17:11 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a28fae2-353b-3cc4-9577-dca393c0d697 | -5.0417 | -40.895 | 2024-10-15 00:17:11 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9afadf0b-3c9f-3220-9c77-3e9b72523e81 | -4.7829 | -39.7701 | 2024-10-15 00:17:11 | METOP-C | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6ef95fdd-f6aa-3a03-a33f-cb6fe9cd38ce | -4.7846 | -39.7771 | 2024-10-15 00:17:11 | METOP-C | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 343f3068-489b-3534-beb6-839be27d61e6 | -7.0435 | -42.0872 | 2024-10-15 00:17:12 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7852bb6-a300-3ed0-9826-d6e849ebd958 | -7.1693 | -42.647999 | 2024-10-15 00:17:12 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e365089-350d-347a-abd3-01cd649b3058 | -7.3799 | -43.6408 | 2024-10-15 00:17:12 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5274d664-f2f5-3df0-be41-28603614ec03 | -7.5936 | -44.659401 | 2024-10-15 00:17:12 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d867bbb-e2e0-35b9-9ed4-59a81bcc15bb | -8.2761 | -48.132301 | 2024-10-15 00:17:13 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c1542ee-8021-3bb6-a2e3-3cfc83baa445 | -7.0762 | -43.014099 | 2024-10-15 00:17:14 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 706346cb-abff-347f-b5e7-0b41c2db5b91 | -7.078 | -43.0219 | 2024-10-15 00:17:14 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c015e8eb-1027-32ed-a817-03bfe8f5a3e8 | -7.0797 | -43.029701 | 2024-10-15 00:17:14 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 13a13321-240f-3a16-8029-d1ad9f096f91 | -7.0699 | -43.031898 | 2024-10-15 00:17:15 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9aae57ad-b02b-3d14-b2f3-1f286e606e46 | -7.0717 | -43.0397 | 2024-10-15 00:17:15 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f22abeb-2c4d-3d7b-a28e-87d2f2a0df48 | -6.0387 | -46.5853 | 2024-10-15 00:17:15 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37de948c-9662-3724-99ba-36231307c361 | -6.0413 | -46.597198 | 2024-10-15 00:17:15 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0843b502-3a94-31e1-b24c-c8ee44a8ee8b | -6.0439 | -46.6092 | 2024-10-15 00:17:15 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02fc49b9-16b9-3cdb-8de6-9dc04442e20d | -6.0316 | -46.5993 | 2024-10-15 00:17:15 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d38c7cc1-016d-379c-a665-f6e928a06df1 | -5.8986 | -46.226101 | 2024-10-15 00:17:16 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac7911b6-f2d4-3d5e-8ec1-7d33fb25b9a3 | -5.5439 | -44.713699 | 2024-10-15 00:17:16 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3624d975-c682-3a3c-adba-36518fb73975 | -5.5459 | -44.722801 | 2024-10-15 00:17:16 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f865bfc-7eba-37c5-a136-25172b87b1af | -5.5479 | -44.7318 | 2024-10-15 00:17:16 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18c938d8-d3f2-3bb7-b102-b33138d615ac | -5.5804 | -44.878101 | 2024-10-15 00:17:16 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00fb8cef-7c5d-3dc2-bf2c-2a5e2f338f22 | -7.3915 | -45.188301 | 2024-10-15 00:17:17 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73e478c6-6fe8-33e5-b04a-6b329c52254c | -5.217 | -43.7113 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b576997d-638f-3e5a-9bf5-05b4a780545d | -5.2188 | -43.7192 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 981ce80c-a87b-3083-9e8a-259464cbac78 | -5.2206 | -43.7272 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdaa2a32-5c61-3539-90b0-d3a9e98a84ee | -5.2224 | -43.735199 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 320caa30-db8f-3285-8139-e06e56a11c47 | -5.2072 | -43.713501 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63148d1c-e3b2-3011-8699-bc6447c1407f | -5.209 | -43.721401 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfd936a0-89e3-349a-8924-fc66c2bd0a70 | -5.2108 | -43.729401 | 2024-10-15 00:17:18 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab5c5c7d-f9b8-32dc-a977-06ff9e65223b | -6.3892 | -41.606499 | 2024-10-15 00:17:20 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3cfc7f87-a7f8-3975-87f0-b1f8de3f98fa | -6.3908 | -41.613499 | 2024-10-15 00:17:20 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 194490b8-7f06-3c54-b49e-095a59e56dc3 | -6.3924 | -41.620499 | 2024-10-15 00:17:20 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 97ce9471-f2e6-37ae-b492-c1593d96b4fe | -6.4013 | -49.586102 | 2024-10-15 00:17:20 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cff1450a-9a83-35ce-b76e-1aa8e1d88764 | -6.7033 | -43.047199 | 2024-10-15 00:17:21 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92d855af-2aad-394d-b18c-a674d6524f92 | -4.2223 | -40.380199 | 2024-10-15 00:17:22 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e66e72e8-e499-320d-b924-a42a1fef262e | -4.2239 | -40.387001 | 2024-10-15 00:17:22 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6c139510-7cbf-3eab-b43e-4c80c103be18 | -5.1951 | -44.761299 | 2024-10-15 00:17:22 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83cb1984-37e1-37d4-96b4-8f0ae1b31544 | -5.2112 | -44.833599 | 2024-10-15 00:17:22 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2e7564d-71a6-355e-85f2-98081ace621f | -5.2133 | -44.842701 | 2024-10-15 00:17:22 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a93fe97-2fb7-3c65-aa1e-2c8979840233 | -5.2153 | -44.851799 | 2024-10-15 00:17:22 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 398c6d57-32e5-3b36-bcdb-f4eac6fd014f | -5.2014 | -44.835701 | 2024-10-15 00:17:22 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a854438-9c28-3687-acc0-06c0fd608fe7 | -5.2035 | -44.844799 | 2024-10-15 00:17:22 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be91f6e5-ecaf-3a6c-b596-477167726d36 | -5.2055 | -44.853901 | 2024-10-15 00:17:22 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f11e376-6ae8-3ddf-a8dd-7715990098bd | -5.4806 | -46.233799 | 2024-10-15 00:17:23 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16efac72-60fc-3603-acf6-4bb2b746e222 | -5.4831 | -46.2449 | 2024-10-15 00:17:23 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97d3f23d-760e-3dbb-885b-f5f75ecfc907 | -5.3257 | -45.5798 | 2024-10-15 00:17:23 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f02e9509-6d00-3202-abaa-bf0dbafd9ba1 | -6.8677 | -45.462399 | 2024-10-15 00:17:27 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0a04b0-7c2c-356e-a674-c8365b470f21 | -6.0483 | -42.375999 | 2024-10-15 00:17:29 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 256c0b82-1944-3f8d-8e27-8b7b123a0136 | -6.0499 | -42.383301 | 2024-10-15 00:17:29 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 464e7f47-fda8-3dc4-916e-ad41735abb57 | -5.2358 | -46.7948 | 2024-10-15 00:17:29 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecf15f9-6305-3e7f-8b39-120bb73e313d | -6.3669 | -44.630402 | 2024-10-15 00:17:32 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20841e9a-f5a2-3bde-a05d-24c2a14a1caf | -6.3689 | -44.639599 | 2024-10-15 00:17:32 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70add77c-a128-37ee-b1d0-f62fa9c3d0fa | -6.1987 | -44.057201 | 2024-10-15 00:17:32 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81278afa-236f-30e0-abd9-940d91e6ba8e | -6.9409 | -47.498001 | 2024-10-15 00:17:33 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
