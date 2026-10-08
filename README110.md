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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c84b8a96-1358-3f0f-b475-5d6287f28861 | -3.48533 | -59.46161 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb18e50a-0062-38e6-a61e-9dd374cf56da | -2.88113 | -54.1767 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15c3c23c-f206-30c0-95be-164981cbf95b | -3.61161 | -55.46804 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d21cf3cc-bc40-328a-b211-2dc1136f606a | -3.52862 | -54.66973 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ba61546-f29d-3592-9beb-8e1fe6d2e5c4 | -3.08488 | -54.2868 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 32afbcbb-e7c1-3795-8e5e-1603bf7f4b9d | -9.2586 | -60.87914 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 748a2463-b7b9-393a-b2c1-18e5c28e53c9 | -4.08489 | -55.38187 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bf308ad-3aa8-310f-928f-2441d20cac31 | -5.18053 | -45.33587 | 2026-10-08 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcc7e70f-1562-3bc5-b99a-1f186618d0ac | -3.26993 | -54.04458 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2247f84f-7ca5-3108-8f8e-ea98a42b8e56 | -6.04212 | -51.73076 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f73f460f-a40d-345f-975b-4ea4544a69e3 | -2.93591 | -54.16702 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10cabc93-bcbc-3f67-ae08-aef7a3f7da94 | -3.9602 | -56.11869 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b18dc727-49bd-3cd8-a121-4c73db592d80 | -3.28403 | -54.00265 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d64962de-545d-3c9b-a878-6b7936ee2163 | -3.04787 | -54.14648 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12516558-0823-3565-95d6-1c51f2af12c7 | -7.38841 | -55.21236 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81bebebc-5155-34f1-a97f-326a8cefed41 | -3.72622 | -54.2156 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c58d253-0cf3-347b-837d-a4c030e9c734 | -7.88867 | -55.0015 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74345af2-872a-3501-84ca-cc32678332a2 | -2.8958 | -54.15623 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b1ffa62-3824-35c7-9d92-2308abe0eaca | -3.10191 | -54.27574 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ce27a620-b5ca-39d6-9a36-5dcffec1c295 | -2.75973 | -54.11336 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7bb0c2c-7d7c-3f8d-bb8f-6feb61a3e8ff | -3.5808 | -55.60537 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c569dd63-7217-375c-9ca6-3d4c2df2bd9b | -5.69089 | -53.48765 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93a94d2f-6757-3e57-a6b1-ebe217d93bff | -3.05466 | -54.21371 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f9f4314-5a9f-38fd-b8ef-e56872444b00 | -3.07669 | -54.29018 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4a1eb6c-38fa-329e-9eb3-7f666e01c5eb | -3.55804 | -59.4767 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8962831-66c5-3f2a-b722-f93d36430b2c | -3.04848 | -53.95063 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 388fbf3d-eb55-3a9f-8cb3-a0e4277e3c01 | -2.99775 | -54.08029 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 7e84dd30-8a06-362c-ab63-2cae99c4d572 | -4.77778 | -55.72288 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65a44b03-2716-315e-8f38-bae24c1c3086 | -3.01942 | -54.11058 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 45fad272-e7b8-3646-93c1-e94cfac06682 | -6.89105 | -43.69155 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c312057b-9543-30f9-b2f0-43eefe5255db | -5.5138 | -42.82327 | 2026-10-08 04:46:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68379f8f-b1d7-3bb5-9dd4-66f1b7cf5827 | -3.0948 | -53.72778 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7441dfb9-04da-337c-a13c-524acc27e7e3 | -3.28462 | -54.04684 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00bb1c3e-e42a-332c-b840-7f093d8b3763 | -2.9404 | -54.10723 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45107ef0-d06d-3b49-970a-a976a20f5ca1 | -4.38194 | -55.16077 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d2f8d800-426f-37bb-8b1d-582394b853d3 | -3.27789 | -54.03994 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8c5fabb-8e8e-30d3-9a23-80b893974a6e | -5.95387 | -55.35572 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5bd88db9-ea91-351c-9063-ff5c42353f34 | -3.04862 | -53.90243 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ef3628d-8003-32f4-b900-3694c854cb44 | -3.28992 | -54.08173 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a6097c9-1fab-362e-9fb5-3a5e0067e525 | -6.97753 | -45.13182 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b14e086-fd08-35f6-9d9e-18c6eb2c37e6 | -7.2271 | -55.17046 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0713d3f8-9f73-3c2e-a351-76cdc5c47138 | -3.26464 | -54.03046 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a0de4c4c-7c51-3da4-ab1d-d44e60ae5a94 | -3.28259 | -54.05981 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90f15664-b230-3b44-859e-a71f982e58e1 | -3.62877 | -55.51303 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbd46170-93ea-3601-bfd5-922372b18ce3 | -3.09184 | -53.72304 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aef1d6c-cad8-3775-984d-3c29902bddf1 | -11.24116 | -44.87958 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 14050137-45a1-3245-a881-3e836bbd8509 | -3.03884 | -54.52677 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7906fd35-3636-3729-87f5-93acb7d3720d | -11.38979 | -46.68779 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12b28db9-38cf-3ccf-b45c-a193f71c8dae | -3.48032 | -54.63139 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e325f4d-3053-3201-8526-a921d0280c41 | -3.1513 | -54.10716 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c320912-d55a-32c8-a146-8fc071b1fef6 | -7.10949 | -55.72585 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fd99f5d-6204-32e8-8dae-a9ce45bd7964 | -7.20594 | -45.35332 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| db082bd5-5a84-3b71-ba23-44bb6e266ad2 | -2.84372 | -54.12553 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 44a92cc7-69b0-3367-8eb5-a0d1ff97458c | -3.3022 | -54.67598 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67779078-4919-3924-a2d4-b525b6d62e56 | -3.57571 | -54.3564 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d7e51aa-d83c-353a-b907-9f1be158b86d | -5.34625 | -50.98168 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6182c41-7e8a-31fd-82f3-54cbe7f1a0b7 | -6.99175 | -59.10605 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec1d8e36-4435-33a4-8f22-25de2de8b868 | -6.06172 | -59.93323 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4e97599-3533-3234-a60a-1d5862cc48e5 | -7.47774 | -42.85389 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8e982c1b-143a-3e69-9342-d9c24c219f8b | -6.99475 | -59.11753 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24fe76da-487e-31af-a8e9-337deaf62f94 | -3.02266 | -54.06627 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7f4d646-2a69-3d74-9ab8-725ac9dd11bc | -5.82761 | -53.53621 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0448946e-79ec-38c1-a68f-8607b970abb5 | -3.03626 | -54.09975 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18ac65f1-993c-387d-88d2-3527a25cc8e3 | -3.47083 | -59.5785 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204cef95-4904-3f58-8ab9-a917b017b53b | -2.47414 | -56.09659 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c62b1bb-d9a0-3e11-9978-3b8491ece144 | -3.29359 | -54.08231 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0bc77bce-609f-3e8f-a726-b696e75d9f31 | -3.0245 | -54.10239 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3ad11c1d-af67-3f1d-a745-f290ffbe437b | -4.80308 | -49.06693 | 2026-10-08 04:46:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00a2c8b2-abe2-304b-9aa4-a69f2a9be02d | -8.08634 | -55.3028 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 879c488d-4eb9-3d79-90a9-c588770a44f3 | -5.14438 | -48.87933 | 2026-10-08 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf0baead-c0b5-37ec-a72f-d001832fb800 | -2.98668 | -54.07858 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 77782ad2-e2b1-34a1-bf4f-fb8329b588d8 | -3.74175 | -51.21133 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb9a1c44-ad8e-345c-bd96-c7cdee28ee69 | -3.21858 | -53.96622 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c6637ff-9b8b-383e-b1e2-6309d50e2699 | -3.65969 | -54.28326 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 501c6f9c-9d41-3717-883f-6873afb05c8a | -3.08257 | -54.27732 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ddc5380-fbfa-3c1c-8d9c-c8bb4acf52ce | -3.26763 | -54.03534 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d3053a8-f80d-3774-bb90-0efdbc5a584d | -5.67797 | -53.50145 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 859d3278-e2b7-3f44-8767-a1d817565daf | -3.55333 | -59.47267 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53e415df-6a01-32ec-b87e-685b1bb00ac4 | -3.54979 | -54.65897 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57580e19-e2f0-3720-bf30-5524ce6507c1 | -6.16198 | -52.65232 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 098ba192-b727-32a6-a738-01913953e2ec | -8.05875 | -44.80589 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f442cd17-6cec-3786-bf10-4f56c651dedd | -3.28016 | -54.04912 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90227c83-5fad-3347-8047-0fdf6a460111 | -3.44114 | -56.93728 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c98a770-08d6-3521-9897-b65fb9604de9 | -5.69029 | -53.49143 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea332964-8d13-3793-bde4-f8b2f3d6b7a7 | -5.11789 | -47.123 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 69610ca9-33eb-332a-9bfb-b87bb08da936 | -3.58238 | -54.67365 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4fa30c3e-7851-3239-8aef-eec16ef46165 | -8.30842 | -54.67068 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f96c1d8-cce6-3074-bcc9-2936b749832e | -3.5687 | -54.66203 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4c544fb-711f-3a27-af8d-70424679cb06 | -6.14572 | -52.6461 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a74b22e3-e0e1-3616-98ba-381b371ec7cd | -4.54841 | -54.96994 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a53b4409-9ab2-3901-acc5-381c195fff03 | -2.50824 | -56.18259 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 966711b7-e91a-3703-961b-6194475bf2e7 | -7.22078 | -55.09224 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e5cf412-facb-3ae0-93b6-91470f495e55 | -4.79534 | -50.78561 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c107991-4190-397d-895f-9b626a896397 | -3.0722 | -54.17573 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38b0c156-88d0-355e-8f4a-5ee49829be42 | -5.04538 | -49.76194 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80738afe-1315-368c-ae85-ffd7003fc802 | -9.31336 | -46.45214 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd792035-9e9c-3c66-b81b-dfda326dd79e | -3.0023 | -57.7501 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b6646b4-ba42-333c-b217-32babab7cd10 | -3.53809 | -59.49976 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2476a0ee-59f5-35a4-a9d2-1e77b2743414 | -3.21248 | -53.86503 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 190687bb-69bb-3b03-8ece-cb2b1640f0ba | -2.50289 | -56.16135 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README111.md)
