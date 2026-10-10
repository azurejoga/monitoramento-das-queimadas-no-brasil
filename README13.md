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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b50a6d1a-75d5-3559-afd2-cfe1b1fa423c | -6.441 | -55.0624 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 62be587a-ef36-3a5e-9644-b7c0f20ac511 | -4.4025 | -49.7774 | 2026-10-10 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 3fe9e93b-9c4e-3aa6-9f1c-2eec6c0e67b4 | -3.2031 | -53.8621 | 2026-10-10 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 11a0c1b7-23e1-3769-8c76-ea8291da52d0 | -3.2204 | -49.4205 | 2026-10-10 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| aa6a596c-875a-3c3c-9ce0-f7e64164bad8 | -7.1825 | -52.6283 | 2026-10-10 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 6e7bc245-1dbc-39be-9e45-dc7da7335e1c | -6.9319 | -59.2412 | 2026-10-10 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4f33fcc3-4209-3b3c-bcbf-5a9549cb47b5 | -9.0153 | -45.8982 | 2026-10-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.5 |
| fa255729-ac61-336a-8b6d-4524fee36b68 | -4.5929 | -55.7168 | 2026-10-10 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d83ba5cc-6e86-34d6-a7a5-ff5d6949c4da | -3.1285 | -54.1657 | 2026-10-10 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6ae3d2cc-bd35-3ba7-9ffc-b1da106eca76 | -7.2187 | -55.0815 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| c6752f17-a8aa-3a89-aeff-826ed5d3e3c6 | -8.9967 | -45.8776 | 2026-10-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 234.1 |
| abb3667e-2c85-34c0-8f7e-2c8a210a7496 | -8.9964 | -45.9002 | 2026-10-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0823d122-cb5b-3beb-a83e-cadb23e0e524 | -1.2723 | -55.7494 | 2026-10-10 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 25411d2c-c520-37f5-959f-8b2bffaeba43 | -3.5676 | -54.6946 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b510186a-3a24-3ebd-b2ad-20f2bc0dfeba | -7.5347 | -45.3233 | 2026-10-10 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 54e0a658-6dd9-35d7-99e3-0590549d2bfd | -7.5161 | -55.0044 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f6af2902-1548-3aa9-b930-434a0f44f23b | -3.9911 | -59.3752 | 2026-10-10 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 53cb233a-0f56-369d-986c-7ef67b9de38f | -6.4566 | -55.5008 | 2026-10-10 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 1841b2d0-d701-332f-b200-b3974c8e4718 | -12.1015 | -57.1583 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d9b5505c-d429-363b-98ff-2cc9d423ea9e | -3.1284 | -54.1857 | 2026-10-10 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7436593f-17eb-347c-b177-6a92e2ba5aa3 | -6.4751 | -55.4999 | 2026-10-10 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| bb58f33d-f385-3014-997e-d83663a52aa6 | -12.2154 | -57.1287 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 858edd88-2ff9-386c-b07f-ebe6726755be | -10.6201 | -60.4658 | 2026-10-10 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4d12e1cf-31d9-30b4-b6d8-8c7d8339e0ed | -22.0903 | -48.9972 | 2026-10-10 00:40:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6ddece91-961f-30c7-9b68-973c1bbdd24a | -3.3139 | -59.4089 | 2026-10-10 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 491e5319-88c4-3d3b-ba1c-d4003726d695 | -12.2158 | -57.0887 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6d073375-b29c-34da-938c-5243e6ddd4c7 | -5.7059 | -49.05 | 2026-10-10 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 3a2ac31a-0951-3c96-8425-81d004835398 | -4.4506 | -47.9329 | 2026-10-10 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d1e8253a-97d7-3068-8ff1-69e35d561978 | -11.0933 | -44.1209 | 2026-10-10 00:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| cdc44774-d444-3f20-a8ac-d6c33aaf5e71 | -1.6225 | -54.4348 | 2026-10-10 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1dd945fd-d031-3696-8286-0ac30c406fb8 | -4.4507 | -47.9112 | 2026-10-10 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6e312de5-6637-3f62-88d3-a7c0799f2b60 | -12.2156 | -57.1087 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c2395a11-1732-3aac-b1d1-871eb4acc6bb | -5.7378 | -45.1307 | 2026-10-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0c885312-3acb-37fd-ab3e-b6df4e6cb4bf | -10.6199 | -60.4852 | 2026-10-10 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b64c1c7b-936a-37dc-bd8c-fc74ad615efe | -7.9086 | -54.7194 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| ef7050c0-e0b7-38e4-93fd-535985d08b63 | -7.4975 | -55.0055 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b3a25a55-9b2f-3522-b12e-2de83b2d9bd0 | -5.9587 | -55.3448 | 2026-10-10 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bd8cf804-33f2-3319-8c91-fa90356dd4e0 | -7.927 | -54.7384 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| d36ef442-60ec-34cc-9bb4-80831bd1e21c | -12.2343 | -57.1271 | 2026-10-10 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 31516235-11e4-344c-943f-9bfe8b633cd3 | -12.3066 | -63.3701 | 2026-10-10 00:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| bafe001b-3c05-33c2-827c-059eaacd7fff | -9.2976 | -47.3871 | 2026-10-10 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 52e69747-84ee-369c-9fed-e75f7df20abd | -9.6364 | -48.8845 | 2026-10-10 00:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 39570b61-3f18-39ce-9de9-4860b1a6810d | -6.9318 | -59.2605 | 2026-10-10 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bc653b35-2255-3153-9e35-aebc2e2faeb1 | -10.6013 | -60.4669 | 2026-10-10 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 60f52a16-de5b-31fd-a73a-717885735a66 | -7.1825 | -52.6283 | 2026-10-10 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d684bdc1-5424-37cf-b8d2-cc8860361eef | -5.7059 | -49.05 | 2026-10-10 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c5b5c1f9-dfee-321e-8f57-5a44aa38f7d6 | -22.0701 | -48.9788 | 2026-10-10 00:50:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 39cf7f70-8246-3867-8d06-f341a46f1a01 | -7.4977 | -54.9854 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| b6541f32-a4b4-3c29-a526-b799471729de | -3.8391 | -55.7799 | 2026-10-10 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 41ac9357-73f3-3ce0-bb65-85f779434f44 | -4.4344 | -47.5421 | 2026-10-10 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5ab86e2a-31cb-3044-8c43-c906a37a2626 | -3.6047 | -54.6136 | 2026-10-10 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1f420671-ada5-3a1c-b90a-165389a26828 | -7.4975 | -55.0055 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| dde0d84c-bc0a-37a7-a852-2e48c91003a6 | -8.9778 | -45.8797 | 2026-10-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| eb06df7d-f42e-3a81-be51-75656b85f5dd | -13.386 | -43.8945 | 2026-10-10 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a994f9b8-3915-3426-8b74-6641228e00ef | -12.2156 | -57.1087 | 2026-10-10 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fca10158-ea9b-305f-a2ea-90e3c2212aaa | -7.923 | -63.7123 | 2026-10-10 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5066336b-6ca0-3c82-ac91-ad189d80460f | -3.7494 | -60.6014 | 2026-10-10 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 153.5 |
| aad11cd1-105a-3b2f-a8f6-0cad156a430f | -3.5863 | -54.6142 | 2026-10-10 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 68575fe9-1651-3c3c-a927-09dbb08f5e84 | -10.6199 | -60.4852 | 2026-10-10 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 233ec3ee-a0e9-3fe0-9772-e6561da9d850 | -3.6048 | -54.5936 | 2026-10-10 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 8e50e428-c6dd-317b-99f1-37302373dc0f | -3.1285 | -54.1657 | 2026-10-10 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 459daa0a-f080-3a48-a11a-96e6370aa3d3 | -6.633 | -59.9457 | 2026-10-10 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| f8ffb15a-11b4-3da1-8e82-e068eb930a26 | -14.4535 | -43.9359 | 2026-10-10 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| bd07ffe2-5560-3a76-9927-33a289d5b91d | -7.5161 | -55.0044 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 9189d1ba-737e-3643-9a13-7c52e92630bf | -5.7378 | -45.1307 | 2026-10-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 675ad371-afec-3644-a3d5-7cce9e57059b | -3.9911 | -59.3752 | 2026-10-10 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c4ee9c5a-e811-3e23-a380-cf99b03484d3 | -6.4566 | -55.5008 | 2026-10-10 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 6277db51-ecef-3d20-ad11-58456a3ef9cc | -5.7565 | -45.1293 | 2026-10-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5f29edf2-3eba-3b3f-95e9-1c798fb97ae7 | -8.997 | -45.855 | 2026-10-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 7e53a6d9-de0a-3c39-98ae-6f39d00cfb70 | -3.7312 | -60.5828 | 2026-10-10 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e3d90037-3e64-3f1d-9f36-742d3901f13d | -12.2154 | -57.1287 | 2026-10-10 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a1dd5b3f-2519-3960-a3ef-b86cfab73ecf | -9.6175 | -48.8864 | 2026-10-10 00:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 673505dd-0601-3782-b70f-0a9d8144264b | -3.5676 | -54.6946 | 2026-10-10 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ed669b60-2103-389e-baa6-a0bd3108cc4f | -3.9912 | -59.356 | 2026-10-10 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| b2261155-16b2-38a8-82ce-a31982cd4b59 | -3.839 | -55.7997 | 2026-10-10 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| e6c39187-7a37-32e5-b822-5b84a41ab091 | -4.5929 | -55.7168 | 2026-10-10 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| e0248040-17fe-395d-9bc3-2466d71effbf | -6.4411 | -55.0424 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7f947799-9b3c-3ede-82ac-a1fcb6b43b5a | -6.5519 | -61.4177 | 2026-10-10 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| bc52886b-a496-355b-abf3-fc78ea3c7c19 | -1.2723 | -55.7494 | 2026-10-10 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9c8fe5ab-a974-38cf-ad71-38aeca4727ce | -14.4726 | -43.956 | 2026-10-10 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fce10356-d9d5-3f24-b8fb-390dc51f8581 | -12.2158 | -57.0887 | 2026-10-10 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ede3f133-6b94-3559-a5c1-bd1f9f447964 | -11.0745 | -44.1003 | 2026-10-10 00:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8cacaf64-733d-31ed-9283-7825d29e400f | -7.5347 | -45.3233 | 2026-10-10 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| e67f7e85-9410-3e2b-8e61-692be8b4993c | -7.5162 | -45.3024 | 2026-10-10 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 86880c1d-e3ea-34bf-af07-12838c6dedb3 | -3.1114 | -53.7839 | 2026-10-10 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 72a8d660-77f0-3582-a056-57dc92eb0991 | -12.2859 | -47.0419 | 2026-10-10 00:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| fdd7f334-2361-3875-aa25-39a48400485b | -10.6201 | -60.4658 | 2026-10-10 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| fc7f02c3-fd5f-3392-9184-c8a67be560a1 | -6.9319 | -59.2412 | 2026-10-10 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 609ba308-c842-30c7-9127-f3f3ebef8bbf | -12.2877 | -63.3711 | 2026-10-10 00:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| dfa35b66-e3be-3976-a047-0f96d1e6e2b7 | -9.0156 | -45.8756 | 2026-10-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| aed8bc6e-0929-3d34-a1a1-e897df80f077 | -3.1284 | -54.1857 | 2026-10-10 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d144b6c9-cabf-3f83-85db-a605c5bf78ed | -9.3165 | -47.3851 | 2026-10-10 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 992caf62-40e6-3d39-b1fb-c93aa6712f3b | -7.2011 | -52.6272 | 2026-10-10 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 15f159eb-51b7-3d53-a52e-5d6a6cbaea13 | -7.9084 | -54.7396 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 06bd7e85-d2af-302a-b842-d5d340ea8546 | -14.453 | -43.9598 | 2026-10-10 00:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 59f9fbe9-39a2-3a75-b742-0af0c892a8f4 | -3.2553 | -54.683 | 2026-10-10 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 16f87ffd-9515-3a53-9b09-988e80ad3249 | -7.927 | -54.7384 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f1edb3af-a238-35a9-bce2-9694b7463129 | -6.6145 | -59.9464 | 2026-10-10 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| fe87a471-bc41-3029-9c70-76e3bab37400 | -3.7311 | -60.6018 | 2026-10-10 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e25c5f6d-3f64-3f58-8af4-b4e3d934ee22 | -11.0937 | -44.0975 | 2026-10-10 00:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |


[Clique aqui para ver as próximas entradas](README14.md)
