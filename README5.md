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
| a5781ef5-c4dc-3561-9340-cf702d5ef09f | -11.93348 | -38.14363 | 2025-05-27 04:02:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aaa1d0b7-89e4-3ea1-8326-32331eabf479 | -6.65153 | -43.20018 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd5bea21-6bf5-3336-82e6-6d646bb19508 | -8.43229 | -46.65596 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce3f130e-9bbb-3968-a44a-7e4a5755e3ce | -8.72371 | -49.38611 | 2025-05-27 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fcd0364-5f50-3f7b-9684-3a8cec655fa5 | -12.82554 | -47.38134 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 603c16ef-a15a-360c-94c6-032d0a1836f6 | -9.71921 | -48.32212 | 2025-05-27 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40e68e67-b512-347e-ad1e-22271d1c1172 | -10.74282 | -49.28711 | 2025-05-27 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce93c810-f10f-30c2-8c78-d2468428ebce | -8.38814 | -49.65773 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5ea69ce-09e5-339c-8b5d-1ab88696b355 | -7.15565 | -47.14582 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e3e62368-2311-3458-926c-4aeb8037e39f | -7.22914 | -43.11182 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 46cc6da0-a571-3138-a19f-fb63204559cc | -7.20354 | -43.11195 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| aed2d0f8-db49-358a-8338-28e6a68dc990 | -7.54448 | -43.18124 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca635324-a522-3e4e-8640-665158c28d15 | -10.65476 | -44.49761 | 2025-05-27 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a4e79a4-c08e-36b5-831b-5f18f03449e7 | -8.75073 | -49.75111 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 687a3103-1fc1-3a49-96dc-1c0e6eba94f1 | -6.21574 | -43.33763 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ff1c21ca-95ad-3138-8371-60b9cb0e3d7b | -11.80245 | -44.27098 | 2025-05-27 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 999468c6-c135-32f8-b748-19ff7b8f7572 | -9.60712 | -49.02755 | 2025-05-27 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 323e235d-6754-35e6-b4ae-6b62e26ca752 | -8.75375 | -49.75587 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 602c79ec-f6d0-3096-b968-8fda6e3646ea | -7.19641 | -43.11081 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 50367d94-1dc3-30ba-9962-01c848ec59fa | -7.22624 | -43.1072 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 7cac3c8f-fdfa-306f-9f3a-389be9b99a46 | -8.38752 | -49.66115 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 873dedcb-923a-3e40-9cd1-dd8979458828 | -9.15804 | -49.65164 | 2025-05-27 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 190d7af3-32eb-3c56-b9ba-a914ccf9f80a | -9.03711 | -47.75054 | 2025-05-27 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aae58a90-df91-3605-b147-13209d57799d | -10.49747 | -42.42365 | 2025-05-27 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93aabff5-b4f0-3e08-ae87-82f974af1945 | -9.92971 | -44.1819 | 2025-05-27 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddaeb6ce-e51c-3bbd-aeb8-d5ce2d6b3f76 | -8.16968 | -43.39943 | 2025-05-27 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 225328cb-7ecf-3b70-8ce5-40f879e12867 | -7.60206 | -43.40472 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6107a18e-ff0d-3d76-999a-11d77044b6f7 | -7.22491 | -43.11534 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b10396ef-20af-31f9-9cbd-4bec78ecebb2 | -8.43474 | -46.65092 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70682c4f-bead-31e9-a925-96e6ecacd513 | -6.05648 | -44.05059 | 2025-05-27 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66d7b844-3e30-3464-bea8-3036e714d14c | -7.20643 | -43.11658 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 3ea4586c-dbf3-392e-95b7-26d0495ed32a | -6.1675 | -48.05683 | 2025-05-27 04:02:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 03185aa8-dac7-3b05-926c-f39c018e1647 | -6.32361 | -43.36688 | 2025-05-27 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f792e0b7-985d-38b5-9130-0b169a1ba570 | -11.57462 | -47.62636 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6519db92-25b0-3678-9633-4b79f294b6bd | -7.24072 | -43.50055 | 2025-05-27 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aca58170-4db1-3cc4-adc5-f8b6ff2349db | -10.36272 | -47.97451 | 2025-05-27 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2de6bb34-9598-3c98-9f88-43e20fe3d2f0 | -7.65997 | -46.10674 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d9e98df3-b994-3831-9cf3-4109f66b1a50 | -12.42167 | -49.9839 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a85822b-fd50-301d-8ea1-7196d458d7fb | -7.1515 | -47.14392 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 36e9ee6b-abc4-305e-afc5-c4e7cd50bc3b | -11.40191 | -52.94855 | 2025-05-27 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2c4f958-fc17-3e98-9dbe-b4da6bc76bf9 | -6.22599 | -43.3436 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0caee091-a15e-31fc-8fbb-daec3f7a77ee | -12.35605 | -49.92298 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad1093f8-d49f-3890-9a5c-da99ef7b88f3 | -8.49471 | -43.88911 | 2025-05-27 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d6986ed-b13e-365b-82f9-2a5f588b3e26 | -7.56289 | -43.36119 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79dc8e18-0387-363e-bfd5-273ff4d6d92c | -12.82687 | -47.3982 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 15dc7646-470e-3f5c-a193-f762cbfe5e4d | -6.23259 | -43.34901 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 757cda93-6619-37df-9544-561e0b9ea057 | -11.13665 | -53.91975 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c84ec85f-61a6-36bf-a375-73cb4e6f6134 | -6.22826 | -43.35262 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f695425f-b37b-3e2e-a6fd-60fb0b07027c | -6.8384 | -42.79137 | 2025-05-27 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc886a0b-c1e3-392c-8fa9-919a8d051371 | -10.6351 | -48.08851 | 2025-05-27 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7619c3f9-755c-31a2-b2c0-2815e9fb7503 | -7.15108 | -47.14502 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ec0eb94-b26c-36e8-842a-575ed2cc6e61 | -8.02129 | -49.69143 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7590e0b-cf78-3e77-a918-743b731c514e | -8.755 | -49.74918 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7087114f-aa2f-3405-9455-ad11b49e6ced | -7.15879 | -43.31595 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bbc9fe33-df52-3f89-98c2-27a169fce2ed | -10.36817 | -47.97042 | 2025-05-27 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8048b48a-435a-32b8-87ee-a63909040de2 | -12.27384 | -44.58831 | 2025-05-27 04:02:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12ae6fdc-e87c-3803-b85d-ff0000fbdf46 | -8.75664 | -49.74872 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69d21a77-2753-3301-8379-4018f34ce582 | -7.46329 | -47.0585 | 2025-05-27 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88dae298-048f-32d7-96cd-c094a477eddf | -7.65732 | -46.0977 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76557bd9-083a-350d-a73f-7c46ea2665ab | -6.0562 | -44.04899 | 2025-05-27 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9812dab8-92ef-3bc3-8f7d-a1f6902984b3 | -7.57139 | -43.35421 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83019f61-6349-396e-baf8-68d5cd79189a | -9.03797 | -47.74577 | 2025-05-27 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17c2ad4a-8a94-334d-b087-83085964a0c6 | -12.46627 | -44.3014 | 2025-05-27 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fef0acf9-ac41-3791-a051-d705105053d9 | -9.84392 | -44.70054 | 2025-05-27 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7072d0b6-7fd2-3b5c-87c5-dfae748aefcb | -8.43547 | -46.64678 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da3dadfb-f0c1-301f-9c59-2395c3492c25 | -8.78328 | -47.9552 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2a38bb0-0824-333d-8531-a2855011a73c | -8.74662 | -49.74343 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df1888c6-22fe-358c-8c4c-7baad127f289 | -13.37165 | -43.64055 | 2025-05-27 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8afc6c5a-0ac7-30e9-ba4b-c25fb1dd28e8 | -10.23223 | -47.42882 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04a0ce2d-49b0-3039-a524-0aab7e155488 | -8.01973 | -43.18431 | 2025-05-27 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4b34fdcc-730f-3656-be6b-719ac7393f86 | -11.8663 | -52.25599 | 2025-05-27 04:02:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e68c70c5-a45e-39a6-be11-8e988fb72c8b | -6.2253 | -43.34782 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9aa1445-9caf-375b-a75d-c12ed75fff1a | -6.63369 | -43.2187 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0e7e3ea7-1340-3d2a-b586-f79e05aae6b9 | -12.0777 | -47.34882 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a57582af-07ca-3a83-a9ae-ff52a4e9aa49 | -8.01592 | -49.6905 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9142a519-3264-335f-a8ea-85e48f2ab36f | -7.60536 | -46.65051 | 2025-05-27 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 301f0f48-25c1-3bee-b481-315aabf1284b | -8.43327 | -46.65923 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f2091a4-6574-3cfb-a93d-549afc0d0c07 | -10.64464 | -47.47852 | 2025-05-27 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64714b9c-d2b9-3722-b2d1-da3905ecd2de | -9.1522 | -49.65399 | 2025-05-27 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f294e19-d485-3905-9abb-194aecf7078a | -7.59764 | -43.29792 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0b47a24-2863-322f-afc0-258e03836376 | -6.16254 | -48.05606 | 2025-05-27 04:02:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b777628-8e1b-3041-9d2b-c57433addd01 | -9.15744 | -49.6549 | 2025-05-27 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59612197-9821-3661-a897-1ee2c7ca8f78 | -11.57149 | -47.44493 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f8eb807-2404-345c-8283-0abe5c1b3181 | -8.05578 | -43.16428 | 2025-05-27 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6fc1a392-fc6a-3292-ac2b-75d22d46eda7 | -7.22135 | -43.11478 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfcf7ea2-37aa-36f0-a358-0a999c5b10ee | -7.56714 | -43.35771 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 477ae361-2d0e-3fd9-855e-dc54a237c675 | -7.20859 | -45.35191 | 2025-05-27 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5120dd3-9f07-3964-a363-b7f6b775ec08 | -12.35101 | -49.92205 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c48f651-457e-3673-9498-3e5fb240189d | -8.01653 | -49.68706 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a42a280-c7be-396b-94f9-06d393dd7459 | -10.82479 | -54.01978 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5096e1ff-6ddf-3ff0-bf74-5b87a41ba5fe | -12.42285 | -49.97778 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21955155-5fec-3b73-9181-5b04f2a4017a | -7.47213 | -43.36382 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b987f742-d6e0-3a5a-8a35-6d220881ca1f | -7.60567 | -43.31601 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba28524c-ab14-3fec-8f2d-023acc37a0ce | -8.01386 | -49.68861 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51da778e-3c1e-3902-8c0f-474eaea353e1 | -11.5585 | -47.44255 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33ce27fc-c90d-3b57-ae03-ce5691f86e2d | -10.82351 | -54.02592 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18f09133-fe2e-38df-a56e-43d59f444c75 | -7.66912 | -46.10423 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deeadc75-391b-3a14-b3c4-66cbcb2a1aa6 | -6.65115 | -41.99432 | 2025-05-27 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20b154ae-7587-302a-9ac9-9b01145fa556 | -11.14209 | -53.92676 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4afa3f20-8987-3ba6-9cfb-da01c3b219fa | -7.20576 | -43.12064 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |


[Clique aqui para ver as próximas entradas](README6.md)
