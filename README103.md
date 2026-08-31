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
| e6ce9d35-51ea-326d-8803-dbec9d66f7a4 | -9.694 | -65.0958 | 2026-08-31 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 4deec964-57ee-3c53-8b0a-4a066893f50f | -9.1103 | -60.2973 | 2026-08-31 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 84141ad1-53ae-3549-b629-d357d92dc009 | -11.3619 | -45.1724 | 2026-08-31 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 4d802ace-098c-3adb-a54b-976f95d8912f | -3.4185 | -61.3461 | 2026-08-31 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5b8992aa-a848-374c-8bb3-57a594bc00b3 | -6.2471 | -53.6623 | 2026-08-31 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6f780226-3480-3361-8bb1-de40f1f7e47b | -10.7457 | -50.6599 | 2026-08-31 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| af4456a8-c4eb-3468-b3df-775c32fc7a6d | -10.7428 | -50.8727 | 2026-08-31 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6fe6baa4-87fb-35f5-9082-b1ccae89afad | -10.1531 | -45.7438 | 2026-08-31 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3958a965-b391-3a22-8205-2aa7ec4d098b | -9.6939 | -65.1145 | 2026-08-31 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 348.6 |
| 0f6a7ad4-c510-38b2-86c9-4ca8435fef29 | -12.3615 | -50.5632 | 2026-08-31 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 842c975f-453f-3063-963b-36f301979210 | -7.9236 | -44.2558 | 2026-08-31 15:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3ec4ac16-8a39-3935-af92-96a201da3643 | -9.4345 | -45.6477 | 2026-08-31 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 6eaa89dd-7b66-37f0-83d9-f213b638b152 | -6.1109 | -57.684 | 2026-08-31 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 281.7 |
| 6cb27718-ff56-343b-9b64-139e8c2c9afd | -4.9788 | -55.8417 | 2026-08-31 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2ece0b02-7662-3155-8f64-b175e6ab8750 | -8.9428 | -63.2797 | 2026-08-31 15:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 776597cb-aa88-3b34-9e34-5fbae907be39 | -6.8358 | -59.9379 | 2026-08-31 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 302285ff-b3cc-31c4-b2ad-6417e6d1304e | -10.8046 | -50.5046 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 5e8c9baa-c671-3fe3-8601-dbdfd8e460b2 | -10.1528 | -45.7665 | 2026-08-31 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| e0e9a2fa-616f-320e-9fa5-af0f42f9e64b | -13.4519 | -57.039 | 2026-08-31 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5bf9342c-91f4-3b10-9af0-4daa39010d26 | -11.2128 | -53.9976 | 2026-08-31 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 2ed76ab7-586b-34dd-a575-168205c8d67c | -3.9707 | -60.0258 | 2026-08-31 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8b49da78-ffd0-330d-bf7e-e208a67b0349 | -13.9667 | -54.4157 | 2026-08-31 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 168.9 |
| e1aabdf9-94d7-3efb-bd5d-259eb5735134 | -8.7442 | -46.4437 | 2026-08-31 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ab4e514a-2f62-341e-940a-7465104680a5 | -9.806 | -59.4468 | 2026-08-31 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| afacbbfe-a772-3e58-a23e-02fa074553f2 | -12.1714 | -50.5217 | 2026-08-31 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 871d69dd-4fae-3678-93c7-8fbcfffacbc6 | -10.1535 | -45.721 | 2026-08-31 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 057eaf6d-e14d-3e5f-acb7-0c25bd05893b | -10.8617 | -50.4772 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0f6a0205-14df-3f2b-8fd0-7ef51ce97232 | -11.1824 | -50.5706 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 25e8eb32-0b58-323b-ad93-7f46580363ab | -4.1516 | -60.6878 | 2026-08-31 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 8a9e2bc3-165d-3971-93de-8335346665e2 | -9.7873 | -59.4479 | 2026-08-31 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 3c052fc7-2e5e-3ad2-8ef8-159e9608baec | -10.5793 | -50.3789 | 2026-08-31 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 2fc8f639-6dd2-3879-b702-7af2e4b782ba | -11.1821 | -50.592 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 60290c71-7aaa-326a-b382-57cdd60bf554 | -11.0244 | -49.6872 | 2026-08-31 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b10ff24c-1c3a-3a70-a3b2-587fde8e3181 | -13.4379 | -51.4348 | 2026-08-31 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 79b3c528-d457-3f7f-9321-45df84c39f67 | 0.1914 | -60.4878 | 2026-08-31 15:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 102.9 |
| caa869c5-090c-3ede-9f9b-44b393cb474a | -10.7405 | -54.0606 | 2026-08-31 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 7c4a6ea0-7a4d-3a16-9c88-78567e82b8bd | -8.7439 | -46.4661 | 2026-08-31 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 274.4 |
| 9dfb403d-0c79-3944-989d-fa32aa65bcc7 | -13.471 | -57.0373 | 2026-08-31 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 379.6 |
| 479cfe6f-0190-3480-82ee-926dc585d5a4 | -6.1295 | -57.6637 | 2026-08-31 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 94a2ce91-caa6-373a-a381-e3cd2bc4d174 | -11.0569 | -51.4328 | 2026-08-31 15:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a62ba8f7-0776-31a6-92e4-38eaec092009 | -5.5647 | -60.2312 | 2026-08-31 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2e039a18-8731-3cdf-85d4-3daecfd2ea47 | -11.3806 | -45.1928 | 2026-08-31 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| eb426941-4e8f-3269-8886-05ddbef33267 | -7.0982 | -45.7689 | 2026-08-31 15:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 842c4126-a445-358b-8a8c-81dd4e4dfe84 | -5.2548 | -55.8907 | 2026-08-31 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 666632b9-24d8-365e-a2bb-74aad24c9280 | -12.1902 | -50.5409 | 2026-08-31 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5fa5928e-6575-3fe9-8c86-d0ba6813d248 | -15.6139 | -56.4103 | 2026-08-31 15:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 703a804c-92b5-38a5-a7cc-4656ab07135f | -10.1084 | -50.299 | 2026-08-31 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| c9ebd685-cff2-3067-97f4-2902c21e0883 | -9.6942 | -65.0582 | 2026-08-31 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| f2f1b08c-bd3a-3594-96f7-381ee2b8934d | -9.4156 | -45.6499 | 2026-08-31 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a375de4f-e2c8-371e-93c2-d843a9c9b15c | -3.6076 | -59.0769 | 2026-08-31 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| c86189d8-b32a-3499-8baf-a2d4a91701e3 | -7.5662 | -61.3049 | 2026-08-31 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a27296c7-b777-352f-af1e-65e23a1b1d9d | -9.4342 | -45.6704 | 2026-08-31 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 230.9 |
| c6b6c675-2607-318a-8b3a-37b5dbafb305 | -11.6786 | -54.5484 | 2026-08-31 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| c0fbc453-ec7e-3578-8e47-af8559d7b055 | -10.3205 | -49.9567 | 2026-08-31 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 77e991e6-d03b-3738-82fe-20bef08c3fed | -10.8804 | -50.4965 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8de8f8d7-3bc3-353e-9880-2cf59254c722 | -11.6975 | -54.5467 | 2026-08-31 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 03d90ad3-9202-3bf8-9ad6-f121a61ced13 | -5.2362 | -55.9112 | 2026-08-31 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 0abe0717-64fa-3668-b829-a489e23c5bc8 | -11.3615 | -45.1955 | 2026-08-31 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6b98e69c-6d4a-3620-936f-73013ff3c1af | -12.1711 | -50.5432 | 2026-08-31 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 09eabf07-3029-32d2-a610-fae8eec85f40 | -8.2043 | -54.9423 | 2026-08-31 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 527e33a2-fc69-34d9-adc4-f2685d20b83e | -10.7409 | -54.0196 | 2026-08-31 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d3a5cc57-4984-38c3-9ef7-f2c63d83ec2c | -6.7514 | -55.6654 | 2026-08-31 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 049afec0-3437-3954-b16d-4b04b3ba6f99 | -10.1538 | -45.6982 | 2026-08-31 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 397ef098-34dc-33ed-8ac5-2eaa324d7ba1 | -2.6741 | -59.382 | 2026-08-31 15:50:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7e3c1508-2dc1-3f32-82f3-5a926ade1be2 | -10.8463 | -50.2224 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 7ffeefc9-d32b-36a2-8f81-8840b8213ae8 | -8.7631 | -46.4418 | 2026-08-31 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 191.8 |
| dbde6cb7-1418-384c-95ab-0d2f67a40c1c | -9.0717 | -60.4918 | 2026-08-31 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0a637a21-cfc8-328b-9cea-35fdf9d6e44f | -6.8751 | -56.5116 | 2026-08-31 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5243f2ff-dc7d-3d9d-9678-7cfe82cf7406 | -5.4876 | -57.1416 | 2026-08-31 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 13c2a6f0-70af-33f5-9395-7e681176ab7e | -13.9474 | -54.4179 | 2026-08-31 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 173.8 |
| daf9f699-e2d9-3883-befa-dc7e363c77f8 | -5.5832 | -60.2116 | 2026-08-31 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 53e04737-d67f-36e0-a08f-182c49dff822 | -3.1998 | -61.161 | 2026-08-31 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5649b028-1845-3499-86a5-103546e0c47d | -13.967 | -54.395 | 2026-08-31 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 337939b4-949b-3724-ad98-0cd76e75cfb4 | -9.4339 | -45.6931 | 2026-08-31 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 84e2dc10-128f-3a5e-9526-287d2980153f | -3.6216 | -60.547 | 2026-08-31 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| b9f624ef-e453-36b4-9589-ea453a1e9299 | -10.7407 | -54.0401 | 2026-08-31 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 253.3 |
| f30e9a2f-e4a7-324e-8701-601d1fcfeac8 | -8.6156 | -54.7743 | 2026-08-31 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 14cea6f1-4033-3c48-a8e0-ae0a9512f59c | -10.7641 | -50.7005 | 2026-08-31 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9b9225ba-1440-3bcd-a853-790ccd05186e | -9.5964 | -47.6204 | 2026-08-31 15:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 892ccaa8-2078-3630-8f45-9921c4f5397d | -13.4707 | -57.0574 | 2026-08-31 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f396fe3c-a7b5-337b-ac8e-84f77494c022 | -12.3803 | -50.5823 | 2026-08-31 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| cae5c968-c1f3-3f0d-abb0-11cb20218dcd | -5.8537 | -57.5576 | 2026-08-31 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 83d0a2f7-6cbc-397c-9558-bc4cbce222d1 | -5.9636 | -57.6704 | 2026-08-31 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d3cc59f4-6dc6-3d35-9b61-5dce6e6f4077 | -7.5845 | -61.3423 | 2026-08-31 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| a2dcda0a-176c-3294-ae21-a6875047dcb4 | -5.5831 | -60.2307 | 2026-08-31 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 6f8b1f5d-73f3-3707-95b5-15ea35d47a46 | -10.7647 | -50.6579 | 2026-08-31 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 10afbe89-a9c9-36f0-9749-a9647a1fd753 | -6.8203 | -59.4001 | 2026-08-31 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8db68758-2eaa-3c18-b18a-cacd28e93ede | -9.6676 | -47.9429 | 2026-08-31 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 228.3 |
| e00ceed0-0828-3ca1-ba2d-3b2a1e113498 | -7.3476 | -55.1945 | 2026-08-31 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 801e5cf9-b7c3-3a4e-b4a8-25e6b70a943c | -10.8235 | -50.5026 | 2026-08-31 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 5c0693d9-7250-3932-a762-481ba3f70fc2 | -7.4735 | -61.3846 | 2026-08-31 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 22bde2cd-d3e8-348d-95e9-d08f617dd039 | -10.746 | -50.6386 | 2026-08-31 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f34260b8-227f-3312-bc7a-53308a7c9d66 | -10.8212 | -50.6732 | 2026-08-31 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 71881e3d-4a6b-3f07-a6e2-9a40184d2bd4 | -10.5796 | -50.3575 | 2026-08-31 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b8efa266-659b-3296-8975-60c647a0721c | -9.7875 | -59.4285 | 2026-08-31 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| a8154d02-2481-3733-b979-7ff918a6181a | -3.6215 | -60.566 | 2026-08-31 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 0104905e-7b81-3ee0-9efb-2c7678546bf0 | -10.7428 | -50.8727 | 2026-08-31 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4b8cdcbd-4a8b-395f-9ba8-f78490009f79 | -7.0242 | -59.2374 | 2026-08-31 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1cf630e5-968d-3e61-890c-fb37ef3e84d1 | -11.1807 | -55.1024 | 2026-08-31 16:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6e573117-0f0e-31c5-8546-f3d954613985 | -19.0944 | -57.3849 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 277.2 |


[Clique aqui para ver as próximas entradas](README104.md)
