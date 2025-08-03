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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e03bdcbc-6712-3681-8fc3-a2568d29813f | -7.994 | -43.1534 | 2025-08-03 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| 22eaeb34-2457-385c-abaa-e04f29aa7fac | -8.0129 | -43.1513 | 2025-08-03 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 255.4 |
| 07f638e7-8d96-341e-8d81-e168d864592c | -7.9937 | -43.1769 | 2025-08-03 05:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 8734bc46-c2a4-33d1-a466-0fcf7db7c63e | -8.0126 | -43.1749 | 2025-08-03 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 189.7 |
| b71f7f8d-1303-3656-b6ea-5f79c2a180ff | -4.5497 | -44.2047 | 2025-08-03 05:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 61137de6-ae2a-3d0a-a668-cb37f3f6eb41 | -2.58543 | -51.92157 | 2025-08-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 251f7f2f-d06b-39fd-817f-695546a759bd | -1.40189 | -54.1241 | 2025-08-03 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6140858b-c89e-3a79-8ac3-73ec46f44351 | -1.62892 | -54.90926 | 2025-08-03 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66defa73-b7d3-37ab-a29a-a0a81bf9cd98 | -6.81661 | -59.27259 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca511863-202f-39dc-a1b6-b42d1f3bca5c | -6.17605 | -58.0723 | 2025-08-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d497070-f5b1-39cc-afde-6bd7d25a264f | -7.88767 | -45.5286 | 2025-08-03 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9ddfb5c-4309-36ad-97cf-0568535aa3b1 | -7.59925 | -55.20156 | 2025-08-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e3a812b-799c-3a24-9105-9a90a12c18ee | -6.63258 | -59.94091 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4ffb0542-6314-36b6-b975-af27a2195646 | -4.31235 | -48.1038 | 2025-08-03 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d1542497-339b-3eb6-bfcf-08787b49edef | -6.81716 | -59.26913 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79b147ee-49fb-33b7-b8ba-dcf009059606 | -6.73585 | -59.18186 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d6eee0c-d82c-39d1-9837-c1f7a81af884 | -6.65168 | -59.11159 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4050949d-169b-33be-8173-a4103fcf6cb3 | -6.82541 | -59.25981 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 601f4714-211a-393c-9766-703a51474616 | -9.46348 | -57.83729 | 2025-08-03 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc675a6b-1644-3e86-968d-af1b791e4699 | -6.61705 | -59.95279 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc8a3eaa-06ab-3db0-8e92-04f154931ae6 | -6.64892 | -59.10762 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e4f5db8c-cfa1-3b74-a03c-32ba24ab0e7e | -8.93885 | -46.74961 | 2025-08-03 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 823e00ad-2728-3c64-bfc7-7c95f11e8d06 | -7.51646 | -61.32011 | 2025-08-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d714a25d-c655-35b2-8da4-22c427638d16 | -6.73473 | -59.16753 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ca1efc2-aa4c-3fb7-a204-056016229ee0 | -6.65001 | -59.1007 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf15adc8-da18-3392-9b37-3f8ea39af226 | -6.62426 | -59.95035 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b01ef67f-2a5b-3503-ba3b-efbba244315a | -6.6287 | -59.94388 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd3b4c11-7065-3890-867b-a4a7a021b834 | -6.65223 | -59.10814 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 9c70e972-b1e2-38b0-89e2-ba51b5b71f90 | -6.82486 | -59.26326 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47aeff3-a480-39a5-99c7-fc1ad7ebbb1a | -6.61317 | -59.95577 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7ba9c63-8c6e-3efe-a618-121181ec8214 | -3.48478 | -51.19075 | 2025-08-03 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc24693e-a9c1-3d96-84f5-d2ef22b9e293 | -10.47708 | -46.97866 | 2025-08-03 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 856b421f-db7c-3c3e-b6ce-157df9e7096a | -4.77214 | -45.33993 | 2025-08-03 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b7597094-ef46-3f7b-95cb-c9d53de448e3 | -6.62259 | -59.96086 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36501196-97a6-34f6-8136-c5327fac04ac | -6.62038 | -59.95332 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 59f71437-cb75-3950-989c-00bda6c3dced | -6.72594 | -59.1803 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eccffd5-5d30-3762-adcc-cc97c3374231 | -6.67711 | -59.16516 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e79c7f20-82b5-3e9a-81f3-92d3e4d9c2b7 | -4.30649 | -48.103 | 2025-08-03 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31781a05-a656-36b7-94ca-df0be60360a0 | -6.62591 | -59.96139 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c180be97-697e-3995-ba42-547433a7195e | -6.68042 | -59.16568 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9fbdb8-d073-37b9-84ad-7d9f4a5b6bce | -6.64838 | -59.11107 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 8db8bf47-402f-3ec2-a3dd-f5cd08f7a476 | -6.64947 | -59.10416 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e29fb25-03f5-3e2f-b4bf-c56ecaa3674c | -6.81385 | -59.26861 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e69a257-c7a5-35c5-8a6b-f90f102d7d21 | -6.61982 | -59.95681 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbd2a8ce-2e07-3bca-9997-a938b5dbfaf1 | -6.73418 | -59.17098 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a945b777-13eb-3149-a8d7-82870e4a58fc | -6.64616 | -59.10364 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b67db11-732c-3b9b-898b-6c48687ac6f6 | -6.62094 | -59.94982 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88f7e2e7-1113-3dfc-aaf9-8c631e8ac952 | -6.83092 | -59.26777 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8a8dcd0-d6cd-303e-9c41-cace9ec2e252 | -4.31175 | -48.10795 | 2025-08-03 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 96a5d353-501a-372c-8b47-e135985fd227 | -7.88291 | -45.5311 | 2025-08-03 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9550541-a999-373c-88bf-adedd4c1c880 | -6.67657 | -59.16862 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29243793-0ed3-3f06-9da3-0feb4aa19d53 | -10.47778 | -46.97271 | 2025-08-03 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 811e8778-5a45-327c-b59f-ba2b2329b38c | -6.68812 | -59.15981 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dbcc4e3-534c-3356-8197-745ebcbc6e0f | -8.4198 | -47.46242 | 2025-08-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 865f2741-adef-3ced-b984-d4605b2921fe | -6.73916 | -59.18239 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3d787da-80a4-3097-8782-a6254c9be02f | -6.73142 | -59.167 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5669a8ab-1de1-3599-b3b7-dbd21957cec6 | -3.81343 | -62.04714 | 2025-08-03 05:16:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bec88467-e9a5-3afb-ba8b-4c5ed8bebd89 | -6.61815 | -59.96733 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9391f4b8-b6f9-304c-848c-4ccfbbc6810f | -6.82101 | -59.2662 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71dbc8aa-704c-3c39-a396-0108f952533c | -6.6705 | -59.16412 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 252ca8ff-beab-34f5-9b00-8e561a723b8e | -2.9105 | -54.15754 | 2025-08-03 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffeac537-646b-33a2-9131-f6df57731df6 | -7.51989 | -61.32067 | 2025-08-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ed63efd-f7a9-3693-a822-2375c338cdd0 | -10.47635 | -46.98487 | 2025-08-03 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a571a8b9-50d6-3373-b5b2-f06ce4a97e02 | -4.77299 | -45.34333 | 2025-08-03 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1d0b2fc7-2f43-3f79-806d-8b7823f22c0e | -6.6749 | -59.15773 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2553d714-a63e-3dbe-958c-ed5ef9fd8138 | -6.8221 | -59.25929 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10896df1-d7c8-3764-a471-8a6366312d4b | -6.83147 | -59.26431 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 002fddb1-1131-3311-9b77-ffea945a40dd | -7.87956 | -45.53496 | 2025-08-03 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f95751a6-c8f7-358f-862e-1c0cbe684d36 | -6.66996 | -59.16757 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0cbd4ec5-761f-386f-8dac-d24b6f12bd8e | -7.52535 | -61.3523 | 2025-08-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b89e39ba-f180-3205-be04-8cc9e8c98f5c | -6.67326 | -59.16809 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7269508-486b-3981-b397-023b639edd63 | -6.67987 | -59.16914 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f70ce76-061e-3ee1-b326-982670f8de73 | -8.42623 | -47.46329 | 2025-08-03 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0364e56f-1e46-3a16-a602-5d5e7d891cb8 | -6.65277 | -59.10468 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81e2475e-c0c0-38d8-b57f-a5e65652a39d | -6.6165 | -59.95629 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a1790190-fc0a-3f0f-8fe5-9916c306a402 | -6.63203 | -59.9444 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41a1ee41-8555-3263-a4a5-c8fc2a5fd92c | -4.10176 | -48.2049 | 2025-08-03 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45e9e2e9-9786-3663-a19b-48adb8999e45 | -6.67272 | -59.17155 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4faa6950-37ad-323d-ad22-81b4dca403e1 | -6.63697 | -59.99914 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 486ec650-1192-32fa-a223-3c1e0fcbe595 | -7.52415 | -61.35983 | 2025-08-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c9b4f68-fa95-3128-977e-8ebe832466e7 | -6.73033 | -59.17391 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa275ad7-d817-39f0-b948-b544ef4622a5 | -9.46006 | -57.83675 | 2025-08-03 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d40d478e-7145-3f56-8cdc-471754100b30 | -6.62371 | -59.95385 | 2025-08-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f52af69-9fb2-3f6a-bbef-5f11238308b8 | -2.49506 | -56.08165 | 2025-08-03 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24a36fb3-b4ff-3251-8846-267b4aef4899 | -6.8177 | -59.26567 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9468f327-4ab0-3898-a0d2-fda7b31a4461 | -6.8144 | -59.26516 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a1ef054-71b4-33b2-9a00-0e9506e925c0 | -6.62203 | -59.96436 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9217d49-2a9d-3432-94b2-9edaa613db75 | -6.73088 | -59.17046 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a7ffaef-85d8-33c0-b497-b76428f52da5 | -6.63535 | -59.94493 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 333e0e8a-5c4d-38dc-8dd0-f19b79e2e319 | -6.62315 | -59.95736 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b82cde93-1f76-3525-b108-9a02945ce55c | -6.81825 | -59.26222 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee61d033-aac9-318d-a9b5-aaac3a8bff5b | -6.63147 | -59.9479 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7909220c-d2c3-34a3-98d4-4f8e42c20ca2 | -6.64671 | -59.10019 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b84628-e1cb-325e-914c-ceda066e9565 | -6.61482 | -59.96681 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb969605-4233-3ba5-b52a-af620559030a | -7.52475 | -61.35608 | 2025-08-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76236668-16a0-3cc0-8ddc-4ecdbb280dd8 | -6.63424 | -59.95195 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a0c34ac-75e7-377c-883a-b27e8b254976 | -6.61594 | -59.9598 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51f24e52-7bf4-33ed-a0c0-d57a38009ec1 | -6.64562 | -59.1071 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 973b28ba-7593-3390-abdf-e181030470c8 | -2.9067 | -54.15696 | 2025-08-03 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ca3e390-2c04-3081-9083-5decfaf13b76 | -6.62759 | -59.95087 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README29.md)
