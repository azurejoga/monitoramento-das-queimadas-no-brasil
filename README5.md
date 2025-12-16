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
| 3f291a57-6aff-3b8a-93c3-f61feb8e3c1d | -1.67412 | -45.80069 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f641296d-d9ad-336f-b03b-30a140a5325f | -3.4333 | -41.6526 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| aace06c8-2360-3e4c-8ae5-49e1d2d6dd8d | -4.40672 | -42.33603 | 2025-12-16 03:53:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dc306863-0098-3d88-b338-5698b66803e5 | -5.1141 | -43.29168 | 2025-12-16 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c1f8df-9e47-36d1-af03-ae776ff11eda | -3.08622 | -44.88567 | 2025-12-16 03:53:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| baeaa032-6fc7-38f1-8fe8-8cd6c6906911 | -4.08178 | -40.27785 | 2025-12-16 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 573ad102-d469-3f1c-b849-3a82f67727e8 | -4.6628 | -42.40004 | 2025-12-16 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7d2a0262-f10c-3382-afae-0934d10d7e97 | -3.94142 | -47.00419 | 2025-12-16 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6aab2b5-b25c-3966-b12f-94c61c091276 | -3.43029 | -41.64747 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e99df1fe-1c72-35cb-9f33-ef92180861a1 | -3.6525 | -44.25603 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f1bf722-182b-325d-b492-ac4cda8f8e9e | -5.78557 | -35.37361 | 2025-12-16 03:53:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe0015be-ab03-320c-8374-ca646b4aef97 | -3.00545 | -41.87295 | 2025-12-16 03:53:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 48ef7ddb-ba53-3646-b934-8e0dfa646d19 | -3.65269 | -44.26106 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d548519-a350-320a-b000-a39f199db4d5 | -4.66201 | -42.40487 | 2025-12-16 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 336149b3-e396-382b-a0b4-ba35d3d85385 | -5.18818 | -35.86832 | 2025-12-16 03:53:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5142da7c-bde6-3508-a320-a43d919d279b | -3.65134 | -40.74271 | 2025-12-16 03:53:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| df10827b-01fa-3d23-ad56-96410b17582d | -3.65324 | -44.25166 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71012137-d42a-3cb1-a5cb-49c1d8f63031 | -5.43675 | -36.85049 | 2025-12-16 03:53:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 825dfb69-6cc4-3e26-b0fd-20466db98f09 | -3.64966 | -44.25158 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d866ea2b-8727-3ae1-afb4-49c56ee39ac0 | -3.43229 | -42.34422 | 2025-12-16 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 07a70ad5-f92c-3534-8787-ff1b7bfcb695 | -3.64452 | -44.25525 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c5e0325-7355-3d15-bf9c-73229971f55e | -2.50399 | -48.04045 | 2025-12-16 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11da61c0-677e-30ef-b42a-e4452060c654 | -3.42954 | -41.65201 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 5404984b-09c5-39a6-84eb-1fc70c793b07 | -4.65814 | -42.40425 | 2025-12-16 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2d343a55-9157-3046-a000-08a0746badc8 | -3.65176 | -44.26041 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1e5a05b-83be-307a-b533-c4ce360aff9f | -5.78975 | -35.37007 | 2025-12-16 03:53:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf0b0661-fe8b-393e-a082-c2a7e1cff74c | -4.63481 | -40.55721 | 2025-12-16 03:53:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a529935-c956-354c-8cc7-d95257639a7c | -5.11825 | -43.29132 | 2025-12-16 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a93eb668-cc9f-31a1-ad9f-166f00b8eac1 | -1.66902 | -45.7999 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f25a940-d0b6-342d-867a-1cadda75dab9 | -4.62827 | -38.50123 | 2025-12-16 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8378a164-7075-3daa-93c0-acf35157e6f2 | -5.11477 | -43.28706 | 2025-12-16 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8435829a-f997-3ffa-a8f2-ae12969ee0cb | -4.62772 | -38.50468 | 2025-12-16 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2b1521da-77a3-3c4b-a69d-3c928df249fe | -4.40863 | -42.33392 | 2025-12-16 03:53:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7fdca0c5-3e57-31af-be79-b99077d985fc | -5.11418 | -43.29065 | 2025-12-16 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3234c52-1602-34e3-af77-14afafbc4f40 | -4.90812 | -37.43144 | 2025-12-16 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 245172a3-4acf-303a-a070-c04205513f8d | -4.40477 | -42.33329 | 2025-12-16 03:53:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 894a887d-63be-3f4a-b957-a13fc789ddf5 | -8.9897 | -45.94085 | 2025-12-16 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80682b45-4882-313a-a373-8e116f7dff90 | -11.75595 | -44.03172 | 2025-12-16 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73342606-cdbe-3664-8227-0051be3692d7 | -12.34659 | -43.44672 | 2025-12-16 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b040d41b-c7bf-35b6-ae52-54edd2410518 | -4.63405 | -47.94268 | 2025-12-16 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 212a9c28-e3c8-3ab2-99ff-9679b6b2e1e5 | -12.17096 | -44.35724 | 2025-12-16 03:55:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64881915-33b1-345c-8b45-e03d434e0f8c | -8.07023 | -43.14963 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0395669e-2db6-39b1-a916-3ae6d238fef7 | -8.08405 | -35.24426 | 2025-12-16 03:55:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 04c531cd-fd57-370f-9a92-b4cd58cb4f81 | -7.61463 | -47.05281 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7212656-14e7-3e0a-a979-2b3d559fada1 | -7.14768 | -40.16824 | 2025-12-16 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbb1846e-f1f1-33e1-a23b-809ee99f5407 | -8.07729 | -43.14313 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4a51fb85-586a-3a96-bd26-eaa6ebc41bab | -12.57336 | -45.40856 | 2025-12-16 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67aa2626-0484-372f-b301-cd79230e1ce1 | -5.76052 | -40.50192 | 2025-12-16 03:55:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 428f804e-a39e-30ef-9e01-cd12e6be1bfd | -8.422 | -44.03156 | 2025-12-16 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d7547b-53ac-3d53-86d8-7d9af96f3839 | -13.262 | -41.3111 | 2025-12-16 03:55:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24778527-5215-3a69-a1e4-fa09d2d07cba | -10.80609 | -44.50217 | 2025-12-16 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 48d5273b-ac83-32af-80bb-d90ccf45b72b | -8.07261 | -43.14736 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| bfe69d6b-a32f-3cc6-b384-714ab1590dca | -9.46026 | -35.87879 | 2025-12-16 03:55:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 53f301bc-4fb9-37c2-9175-1b761ac0e661 | -8.07408 | -43.15023 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1983862d-f178-36a5-9c5e-19bcec3601c3 | -11.93363 | -44.00024 | 2025-12-16 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12dfad83-6e02-3adc-9f67-87665ea1caf9 | -8.6331 | -36.99977 | 2025-12-16 03:55:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| adb16d3c-3c63-32a0-8d5e-2f70e6be7048 | -7.13599 | -39.80841 | 2025-12-16 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3a1e1e09-ae2e-3b1e-ad63-f7671a09a560 | -7.41525 | -39.46543 | 2025-12-16 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f1b29326-ac2a-3a4c-9e7c-fa08972846c0 | -10.14963 | -36.60241 | 2025-12-16 03:55:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15eab31b-8e63-3687-91a6-16e88367f7e6 | -10.6064 | -44.83295 | 2025-12-16 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69f016b6-8c44-3982-8e05-0ce8d371dd1b | -8.62968 | -36.99925 | 2025-12-16 03:55:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ad1f3aa-6f25-3939-b0d3-72575e8696db | -11.89004 | -43.70706 | 2025-12-16 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b885c2ab-4df7-32f6-b661-465d0278dd6f | -5.27864 | -43.64254 | 2025-12-16 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94c34d38-0bc0-3fe0-9841-5b1303525373 | -8.06875 | -43.14676 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| bf1be3d5-c9d5-398a-a67d-b458d7e6dc6b | -8.41736 | -44.03439 | 2025-12-16 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3f06046-2d93-371d-8f04-3c4343a502e9 | -12.5671 | -45.39561 | 2025-12-16 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc33e2d9-6cca-38e0-92fc-85dcc1c59e76 | -8.38815 | -35.4625 | 2025-12-16 03:55:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 67a9e3a6-a94e-3935-b21d-23f2c6abf46e | -11.00039 | -44.34178 | 2025-12-16 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab31bd4c-29be-39ce-983f-14b51deaabda | -5.76398 | -40.50247 | 2025-12-16 03:55:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d6819890-217b-307f-8d64-bd21f5412c76 | -10.36732 | -44.8843 | 2025-12-16 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2319c673-e95d-3960-b5af-7f00aad0c493 | -8.39115 | -35.46737 | 2025-12-16 03:55:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99e7e797-94d1-3088-8585-f9e6686adc09 | -13.25923 | -41.30689 | 2025-12-16 03:55:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac3acf90-22f6-3815-8adf-e4a866f17138 | -11.58781 | -37.87729 | 2025-12-16 03:55:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07c024af-d64e-35bb-b6d7-b56d3a00925a | -7.1451 | -40.09718 | 2025-12-16 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c85ba3d5-0765-3a08-aff1-78f279cbe237 | -5.39333 | -44.68452 | 2025-12-16 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dca857ff-60e0-3c00-9eaa-650c6a49cd1e | -12.16706 | -44.35659 | 2025-12-16 03:55:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af551786-a79e-3360-8611-f9e4fc75fba1 | -10.36366 | -39.12425 | 2025-12-16 03:55:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1c2ddc72-f665-32d8-9446-fc2cc1829439 | -6.46334 | -39.77839 | 2025-12-16 03:55:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 133349ad-358d-30f4-ad00-1eee5a1bc0c5 | -10.76756 | -44.93792 | 2025-12-16 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03dc8609-c156-35a3-a945-33c9dd1551f7 | -7.18551 | -39.11063 | 2025-12-16 03:55:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c06824ce-a85f-36ad-a7a5-edb913bce9ed | -12.32788 | -40.34344 | 2025-12-16 03:55:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a89e662e-c8f1-3a71-9670-8f95cb7dddc7 | -8.07567 | -43.14057 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bafbc47d-2f1b-3fc6-85fa-3d510a94ae9b | -10.9995 | -44.34698 | 2025-12-16 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af13e9b0-c461-3e7f-949a-7001fc8fea38 | -6.46669 | -39.77897 | 2025-12-16 03:55:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ac623d3-6d77-314d-b154-15cd65d4d205 | -5.19671 | -44.29417 | 2025-12-16 03:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 370613c8-0506-3ae5-b9ae-6113a7693ddc | -8.7483 | -35.8339 | 2025-12-16 03:55:00 | NOAA-21 | JAQUEIRA | PERNAMBUCO | Brasil | 2607950 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6acaa1a-0d06-3526-842e-6d94dcd11b19 | -7.61498 | -47.0481 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 402dd615-b9f8-3b88-89d1-87baf1666026 | -9.55784 | -44.94003 | 2025-12-16 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad15059a-a21f-3932-b519-4b2f68822a24 | -7.85408 | -37.41681 | 2025-12-16 03:55:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50298d9b-d7fe-3d23-a9e7-95dcd5ea3f65 | -12.25562 | -44.42765 | 2025-12-16 03:55:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec4fff5a-6812-3211-8a1a-11a3100bfafa | -7.86328 | -41.94194 | 2025-12-16 03:55:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39d3142c-5edd-3720-9cc2-0fd58617405c | -7.61338 | -47.05693 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 843dd130-432a-3be8-b929-b21d434ea0de | -6.71482 | -39.99971 | 2025-12-16 03:55:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| abbb3852-95c5-3345-a232-2117013cdd9a | -7.61551 | -47.04518 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad688215-1004-3c66-bb9b-e790f5dbf460 | -8.07647 | -43.14795 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8ac9d1ac-91f8-34d0-a598-6f4b96ab1ec0 | -6.07583 | -40.37314 | 2025-12-16 03:55:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad06f002-cf1e-30fa-91d7-3e5e706e2557 | -9.46088 | -35.87455 | 2025-12-16 03:55:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34d9bdd9-72ff-335b-844b-b71cf369c27b | -9.45363 | -35.87351 | 2025-12-16 03:55:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a9960eac-4cf9-37ff-9a3f-8b932770f304 | -11.14893 | -43.33165 | 2025-12-16 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfc1c36d-53a7-3345-bfde-9cc408e2b68c | -10.60229 | -44.83219 | 2025-12-16 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
