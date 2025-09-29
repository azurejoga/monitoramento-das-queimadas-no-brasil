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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4499493e-42ef-35f1-b9ae-cf06a8b6db1b | -4.90606 | -47.14238 | 2025-09-29 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 275b3918-40a1-3c91-bd7f-63e1152fbfa2 | -3.10538 | -47.00988 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 45b8ae95-21bd-3213-a0b2-8e32f9c31159 | -7.44307 | -46.98551 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23269172-70e1-38a9-bdc9-7ecdcffe947c | -6.11794 | -41.8168 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 682e6091-39f8-3afd-8dd7-f108429fde4f | -5.42504 | -42.2621 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 289bbc38-7e8c-3211-bbd6-80dc3a0b3785 | -7.2252 | -44.77739 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| dac0a374-7212-3d10-be2f-46b0766ba9a7 | -5.5992 | -46.40754 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9560476-95f7-31d7-9e95-d2b8212de094 | -3.61432 | -42.76649 | 2025-09-29 04:06:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f3617ea-53d3-3f12-b9f2-643e98ea5fe8 | -7.45652 | -46.30496 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90e169e9-579a-31e8-b78b-c6fbb49751e1 | -8.64986 | -43.98672 | 2025-09-29 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54999b71-98aa-3ed4-9065-5b38cfad0106 | -7.50481 | -44.29155 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52fdc694-2f43-341f-938e-429e087db54c | -8.28232 | -45.47318 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31578aed-458d-3b0c-b7aa-c139ce57529a | -5.48326 | -42.87676 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b01b444-2e6e-35dc-8817-807e69ca4e26 | -5.16643 | -41.26175 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63deb178-40a9-35d0-a142-385b5827061f | -5.24606 | -45.35822 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fd00c1f-aa45-39e4-937f-23edcc8d7751 | -4.50335 | -40.72663 | 2025-09-29 04:06:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4ccc39d-7c38-37f1-bd3b-77a4a297a8cf | -7.89278 | -44.59762 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c77ff45f-7d2a-3df9-b00f-005f0bbde740 | -6.6184 | -44.9539 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed344b56-3d4e-3cdc-a167-d992545b3a89 | -7.82299 | -44.80611 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f88e6b7d-aa5a-3ea7-bded-4381a35317d7 | -5.9808 | -42.35733 | 2025-09-29 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9dd3ef4-f03d-3492-9934-1b9e41e85f75 | -6.71643 | -44.58834 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b0ca20c-e4ad-3d11-85b1-670817bbc899 | -5.74327 | -42.65449 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a3e2bdb-5139-3865-8359-9a054ef425a1 | -6.98323 | -41.19845 | 2025-09-29 04:06:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c5a73ba5-676b-3d7a-8196-bdb52996b690 | -5.81682 | -42.78819 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1600012e-2ab9-34e0-961c-11094469a8e2 | -5.74037 | -42.82423 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 149519f5-906b-3c9f-b89f-6648e70f2077 | -6.084 | -42.45672 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e25a220-472f-372f-8e73-a9691c952a80 | -8.16175 | -46.39227 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 622e6f62-944b-33cf-a0dd-828b5e2699e1 | -6.18992 | -43.84222 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a943aa94-914b-358c-85fc-6647064b3083 | -7.82459 | -45.1412 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9e259d1-5c2d-3d75-96a9-1218d8f0e1b9 | -7.86366 | -41.06265 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c0c5e39-5c26-310f-a34e-715ebd555ec5 | -5.5999 | -44.93025 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 496c9518-cd81-33d8-9163-2fc392d7be48 | -6.57343 | -43.40329 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 91776754-1b4a-3311-9e71-b8dd47435a6d | -6.11363 | -43.46907 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b79d6b47-291b-3f55-a518-25eab85287e0 | -5.54092 | -42.7333 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 663de930-675f-33e2-8ab8-a56a51d14422 | -7.73316 | -46.99693 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bab3cbdf-474c-3411-8d56-eba797cb5b76 | -5.71881 | -42.85053 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f013cc40-0c06-36e1-9ddc-bd778a09264b | -6.39681 | -42.90628 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cdd0778d-8f59-3331-927a-bdb2b9cdd6fb | -5.74432 | -42.82116 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 98ab16ee-50e4-3021-b620-ee4547ac12e1 | -8.00625 | -47.0347 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 815c5d57-e18e-32e1-945b-23ac11c228ec | -6.62431 | -44.96362 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 658cf543-ed0d-38fa-b352-5e7bd16899d1 | -6.85555 | -47.35922 | 2025-09-29 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a404ba80-adc6-3a88-af31-5b9b924e2b9f | -5.77426 | -42.83717 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 46267f63-7d37-3098-adbc-721e9bf286c7 | -5.59916 | -44.93476 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b17153a-610d-3da2-a697-3856959a0892 | -6.16321 | -44.16211 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dafc10e-9672-3bc6-8b07-75e977aa0a6a | -5.74317 | -42.82838 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6aa53d4c-9a1d-3652-9e9b-2688d81432a3 | -7.25318 | -44.76491 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c229cde3-dd1c-32cc-8c14-2724f89254c2 | -6.85981 | -47.35981 | 2025-09-29 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 014b5f8f-fd38-3fd8-95db-47827bb79052 | -7.85471 | -44.58857 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fbc3789-f180-3c19-a958-ffd773b2c1f2 | -6.17677 | -43.47182 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34e02d8c-8cca-359a-8245-a3aadb26fcfc | -6.27992 | -42.48419 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86795e6e-1d11-347c-bf40-40892ba6cc73 | -5.68892 | -42.63885 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b74b1a18-8973-3559-a88c-1439ccac5999 | -6.216 | -44.2151 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e9838e39-9c5c-3922-8a26-0002f31ce131 | -6.42661 | -43.50662 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a214b7b3-5347-3010-ac1a-0885899acbf0 | -7.76595 | -45.74785 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3d23829-44b2-3bfd-9d82-c82deeb0959a | -2.57513 | -48.40928 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dc0d67ab-1b0b-3044-a7f5-0c6443471bd1 | -7.88684 | -44.5676 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59e06dc8-731c-31db-9e94-8322fee436d1 | -5.38406 | -42.30967 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ddb098db-4175-3a79-9f1e-3b1850fa7497 | -6.26306 | -43.63259 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 566e4636-35ba-31a9-8ba8-8489154acb1f | -4.5039 | -40.72318 | 2025-09-29 04:06:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4781f49-630b-3b1b-92a2-d26e8ff49680 | -4.15347 | -40.01114 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 648f1ef7-6df7-3d40-a552-038da77c2485 | -5.28144 | -43.15158 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dd00952-ab50-3efd-9646-b5f20a805a04 | -7.24852 | -42.99716 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af716132-c252-37ce-baad-f8a843fefe64 | -6.12125 | -41.81732 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5bb91677-a5fd-306f-b05e-66696f1a91a8 | -7.32503 | -44.71912 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 818c4ac3-0521-3812-831b-c6aa8c6b1c0c | -7.75297 | -47.00396 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf1bdedc-3c34-37da-b655-6a0904d3ca2c | -7.28543 | -42.83041 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4791b778-de47-3be9-b9ae-1113ebd94f5c | -5.70901 | -42.65285 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b074b571-3544-3cda-9354-673039586d11 | -8.29934 | -45.46232 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56991ecd-da68-36fc-917a-a1f6ded28760 | -5.14708 | -46.41759 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2bdd8bb-3fed-35f9-bfaa-a70c5ca35352 | -6.62205 | -44.95459 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fd1cceb5-869e-31a7-9647-f8e82fa71639 | -6.24516 | -42.47138 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 500f94a8-97bf-3f67-b454-60ae53dd7b01 | -4.71251 | -41.97937 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4c29e1ce-07cd-3f32-8797-2ad25a31b2dd | -7.89567 | -44.60215 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9deec0c-1937-3e2c-bcfb-b0dd2d75de27 | -5.35975 | -42.83942 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9639d639-8ceb-3581-b239-fae5e7972536 | -8.15223 | -46.40103 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2416f404-6179-399e-bce6-49dd3d729f5e | -6.73158 | -43.37932 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 721ca341-f5b2-3429-82e0-95c9bf0649e3 | -7.58277 | -44.81052 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf8b98c-4050-30ed-91ee-f6df82f46c99 | -7.22673 | -44.7905 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2c2395c1-32f6-3516-b75f-32a0dd22b35a | -5.76293 | -41.74239 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0507bd24-b932-32e4-a9d3-22229ea75cd9 | -6.13681 | -42.65466 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db5366c3-0f59-3e8d-adb4-12129043e461 | -4.71417 | -41.99043 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 061d9459-7571-31ec-b392-5df7b5b48e48 | -7.74826 | -47.00693 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e9b849e4-0f37-3e17-afb8-29cfc511563a | -5.81343 | -42.7877 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94f93690-bf6e-3682-873c-46b96a0fdb6c | -5.24319 | -45.36044 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edd904fb-2ee8-37c5-8f66-ee6efe96681f | -6.48783 | -44.26118 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c587effe-6603-3fe0-93cd-4cf2ea6bee53 | -7.29762 | -42.83253 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c22b3aba-7e99-37cc-a632-6ad26d26b82b | -3.10469 | -47.01416 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| b2581fb1-a971-3b1d-8817-76d310ceed02 | -5.74192 | -42.85801 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| af156950-5963-36c3-81ce-ebbbc6a9fa7c | -4.71529 | -41.9834 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec031f7d-73f2-3798-91ac-b3bfb8825575 | -3.83446 | -40.46596 | 2025-09-29 04:06:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb65a637-fa8a-325d-89e4-af85b5ec0467 | -6.14741 | -42.80335 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de5c1162-6cfe-35fa-9c21-1e4128c9110f | -6.11584 | -43.47717 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab9771c7-41f7-3070-864c-445d694936fe | -6.46374 | -43.64833 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 307cf6fa-97a0-314f-9656-be4d71bda039 | -6.25959 | -43.63211 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fc2fac5c-7637-3806-b929-36c05740ba98 | -5.74588 | -42.8549 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0d934db-a697-366d-823f-b6d92c35da9c | -4.71473 | -41.98691 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5a0c6172-ff09-33ea-842a-e25dfbae2612 | -6.71396 | -42.76854 | 2025-09-29 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 117bb5cd-b535-3d6a-8765-a3d1938ba6cc | -7.54965 | -46.10974 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd61c568-68e2-3524-905e-6d8ad465f3fa | -4.14021 | -40.01262 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0a5fe374-fc54-3cf8-90d1-4854f57b2e60 | -2.701 | -48.83881 | 2025-09-29 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README30.md)
