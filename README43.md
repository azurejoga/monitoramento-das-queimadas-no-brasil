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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e244813-a67a-3c6f-a6e6-1bf6b090d13e | -11.05533 | -45.15322 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bd671f51-0082-3932-a825-8952d9716db3 | -6.30111 | -43.7942 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 742ba3e7-5397-39f9-b961-8521103d156f | -8.40891 | -40.45487 | 2025-11-16 04:08:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 34d454c3-1225-3be0-8998-424819b3b69b | -8.4558 | -45.59103 | 2025-11-16 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd693432-5b83-3dec-986a-9bcc6b1efc5d | -7.37568 | -43.31609 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12d23a6b-6a10-3d66-8f87-00be67eb5b6e | -10.52753 | -44.8385 | 2025-11-16 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9337289b-5353-37a3-82c4-d01632f95f62 | -6.54052 | -43.40106 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecf03497-3694-38dc-8b61-0b41e66a8a26 | -4.66819 | -50.36969 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61c557de-1bf5-31b8-a028-bf0ff964b0a4 | -8.05638 | -43.10046 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| cb0c1b5e-4f4e-3d18-8d13-dac517aac6b2 | -9.11314 | -40.45626 | 2025-11-16 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b9be3d43-7b86-350f-8a17-2b6323805319 | -7.26635 | -48.03173 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c22d9f9d-a259-3eb0-bc03-792c5c3c266b | -6.53933 | -43.40849 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2222ad54-b3a4-30a0-858b-5dde15308812 | -10.17951 | -44.50203 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0840bb5-e8c2-356d-9db1-30ce7d0e46d1 | -12.39823 | -47.56384 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9745bcf4-2c25-3f8a-8928-416da005195e | -6.90602 | -38.88301 | 2025-11-16 04:08:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cab2f065-417c-3fcd-a0f9-d62e8d401a9e | -5.75875 | -42.50744 | 2025-11-16 04:08:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c6d99a9b-37a7-3021-a6e7-961680429952 | -6.74503 | -48.19486 | 2025-11-16 04:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36e0783-821f-3350-afb1-40635b8a3df7 | -8.20507 | -43.56799 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6a6609-ae87-34bb-86ee-6512b066448d | -11.70795 | -48.39584 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 418fafcc-5940-37dd-841f-ec686398130c | -6.6974 | -40.80597 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e7c51ba-a0f9-3b54-b0b2-f89c23157188 | -10.54221 | -47.92551 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2676de9-a9b0-3a6c-a4ed-377a87808dea | -9.57377 | -49.10492 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a9a1999-bd15-3697-96de-4f693d2a0d43 | -6.94655 | -41.53458 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d95d00d7-8716-3588-8d35-124d14c10af3 | -12.20031 | -49.61736 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d4cea5b-6fdd-3962-8f99-c05e7b5e09e5 | -5.72253 | -42.3753 | 2025-11-16 04:08:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d51d9def-b144-36ee-b601-6f9851734418 | -6.94325 | -41.53405 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67544b2d-a29a-33c3-ae76-72c0a4a177b2 | -6.72573 | -42.94631 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5b9c5f50-dc69-39b6-a50a-94f5ddf66ad4 | -10.6217 | -44.58425 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a8bccc6-a66f-381a-bb24-df105f837529 | -9.00688 | -44.44296 | 2025-11-16 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba5e51bd-d8b5-3df6-8645-03237d52be0a | -6.32147 | -41.83513 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecbeb715-17fe-36ae-812e-9a4c4ed068f1 | -5.69331 | -45.992 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac4ba574-1311-34b8-a384-046406eabaab | -12.00735 | -49.28385 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3f43930a-45d4-3429-b99d-46268689b195 | -6.88092 | -39.66386 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 912c19c0-b74c-387a-acb8-8d485371bad9 | -7.18918 | -39.2067 | 2025-11-16 04:08:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f8428d5-4559-3741-ac8d-70a92ad34a41 | -11.79231 | -45.54245 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5b52dd5-56f4-3c01-b45d-f81f00674599 | -7.05129 | -42.24699 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 20a9cab5-f984-31c1-9af6-3d5dd352c610 | -7.57569 | -46.30651 | 2025-11-16 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38fd94b1-2202-32be-b541-a2cf87b7e1e2 | -12.0674 | -48.21496 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 03662e38-f196-386f-9490-92f16b2f342c | -6.09985 | -41.71164 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 00641910-678c-3682-8e2f-040a8a8cfe8b | -7.52535 | -42.62013 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b94bbe81-8701-3ffd-be84-3dcc36e33b95 | -12.06129 | -48.20624 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49cb6c6e-854b-338a-8468-49024c7e47b7 | -10.32667 | -44.60793 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95796f6e-c018-39e6-9f46-e7829ff396c2 | -9.57294 | -49.10955 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11cf75c0-c05c-3f0e-b4ce-ec08efbf4d5e | -10.11972 | -43.90069 | 2025-11-16 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cde12db-c956-3320-a587-1878ffdaa019 | -12.06065 | -48.20993 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16683e48-07f2-353f-a188-bdeef1600bbd | -8.73858 | -45.64677 | 2025-11-16 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d08387d0-2f6f-3ca6-a397-c730905bf38c | -5.70411 | -42.86843 | 2025-11-16 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56c68737-4620-375a-a40f-7d9fc9c98144 | -12.408 | -47.55269 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55b7e7f0-4287-3b31-8c2b-e03181da90e4 | -7.91799 | -47.10318 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f1381a1-6c57-3a4b-9c78-1c3f921408e6 | -10.25459 | -45.06359 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3acf72b7-18cb-3f1e-bcfa-49d6bc50e740 | -10.0061 | -44.76609 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee67e787-1c4e-36d4-bd62-f5a3dc091881 | -7.09975 | -42.7326 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e97a9c2-831a-347b-88b1-9b1b46ba513b | -10.94483 | -48.69752 | 2025-11-16 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f12ee625-e9f5-3339-8cb0-a1d84996a3fb | -11.95789 | -44.95661 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fb27878-69f6-3004-b39e-ce39f5c3bd3e | -11.7057 | -48.86958 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dcaac239-b2b1-3a10-a4fa-0b96a001c3b7 | -7.15234 | -41.75882 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 28d0d147-edb1-3ced-9ed4-72bc02e73b00 | -9.84299 | -44.17682 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57774831-642b-3d48-9b0b-610cb798b7f4 | -12.06019 | -46.97219 | 2025-11-16 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dbe35e8-5290-39dd-824d-375142e05ab7 | -11.90555 | -46.20002 | 2025-11-16 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4b52c6-8ce3-33dc-9d77-eeeb9ff42bd8 | -9.68083 | -46.0232 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee746e35-1c2b-3688-84c9-86f3efd7b1b6 | -10.54283 | -47.92199 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ba2bc3d-5f03-35b3-ad19-5220aa76a246 | -8.90277 | -50.23083 | 2025-11-16 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8fc6d13-43d8-388c-ae91-25130930086d | -7.12181 | -46.15991 | 2025-11-16 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d0e38d0-ea62-3c6a-b6fe-a74a5dd1bbdc | -9.71385 | -48.90094 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f72b8c2-fe27-33bc-9bb0-ef13afa91bf8 | -7.15179 | -41.76227 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| be6fdb13-ec1d-39e8-86ad-95dbaa5022fc | -6.16226 | -44.70235 | 2025-11-16 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb4007ce-6b1c-3aae-b7d1-7d425f3123e1 | -7.10365 | -42.72962 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb91e790-bad4-366a-b500-4d51b14b6e4d | -9.73832 | -43.95466 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df4fc4b8-fe09-3f75-8087-17c4bfcfffeb | -11.10248 | -44.80114 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a36c39e2-b5f0-3168-9ebe-c6d7521fd68b | -5.79652 | -42.57137 | 2025-11-16 04:08:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5615da7e-7e91-31b2-b01c-e2d10c12b23f | -7.14958 | -41.75484 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 21586669-8078-3bf0-8444-eab5f167e1fe | -12.69367 | -46.79162 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 615da45f-4869-3d49-937a-9e58ecc9160d | -9.71307 | -48.90532 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51eb7b28-46f3-3068-bf41-0347147de48c | -6.24997 | -41.70753 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 700eb271-070d-34ec-870e-08c2ddfa892c | -9.50567 | -47.27205 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90333529-1b17-3bb8-a607-ac200a12d19e | -9.33055 | -46.57455 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f281f803-19d6-3c57-8a74-829fac237d3a | -5.48249 | -44.84486 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2009dcf3-d8a2-31e8-92a0-6383a0479fdd | -9.74509 | -43.9558 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab028f2f-03ac-3a4b-af15-6ef9f061230b | -5.96628 | -43.74701 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0b861a9-4b0d-3255-ac4c-ca87ed339e39 | -5.5788 | -46.14468 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3629501-66eb-3889-9248-bf0c7dc7fb28 | -10.8062 | -47.99016 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8598cb93-ad65-38a7-9903-ef157603bfc9 | -7.27244 | -39.3492 | 2025-11-16 04:08:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7333b02-99e2-394d-b0d3-0bebfdfd4cb7 | -5.75185 | -45.10664 | 2025-11-16 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7630b3d3-6441-3c65-86a2-e0c74a582851 | -10.07286 | -45.52061 | 2025-11-16 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44933a98-82d5-3280-8b89-23135dc7976f | -11.78946 | -45.53781 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 615cff88-53e8-30cd-bb3b-d80be9c4ac1b | -12.69446 | -46.78706 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bae527a-d7df-3ce8-8de3-db9381a84d4d | -7.06196 | -48.32224 | 2025-11-16 04:08:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ac31a6c-d3e9-3289-9371-e05f13ebc90e | -9.51368 | -47.27348 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a5c643-191c-383b-a442-4ea5abe83eec | -7.7136 | -47.29691 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f415dbcc-069f-3761-960c-0a6165aae71a | -10.66643 | -44.26921 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6a07f50-5129-3091-89ed-aabb941a7ad8 | -8.6723 | -41.03429 | 2025-11-16 04:08:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 598e73b7-bdd1-3642-a97e-caaebc67f489 | -6.94923 | -39.56256 | 2025-11-16 04:08:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81456057-7dda-3ef9-a7d6-bc3a023e3c07 | -7.05464 | -39.62885 | 2025-11-16 04:08:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dcfc83fa-2000-3ca9-ac14-b782d7c4cc6c | -10.66383 | -49.36493 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a377013d-b9e6-3609-9926-5b70ee554643 | -7.58478 | -42.33228 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62e9a1d8-55d2-3f5b-a5da-fcf6d3fb8202 | -12.65415 | -46.7448 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d9b0e3d-8442-324b-9472-f2e798ef7af3 | -9.05918 | -44.7466 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 17b405eb-3e43-33cc-b630-4bea22705e0d | -6.14302 | -48.04691 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1c9dc18-92c9-398a-a202-7ad264a4c41a | -11.03172 | -45.29647 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 728ec5b7-dfbb-3444-b129-124d3dd719eb | -9.34729 | -46.5925 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README44.md)
