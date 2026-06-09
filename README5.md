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
| 8f3e81f5-44d4-3624-9509-d183500171f9 | -6.11695 | -53.08372 | 2026-06-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a56f7be-45ad-3404-b957-a2c12b74f9d4 | -8.97195 | -47.98176 | 2026-06-09 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e4f813f-2c4d-38f7-b077-4f4f0538a51d | -3.49335 | -48.03967 | 2026-06-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64c67885-811d-39b0-a545-b583b52e5001 | -5.29131 | -43.95971 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 63cf5ba7-73f2-373e-a430-67fe9f8a267f | -5.80992 | -45.11365 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68ba1ed0-2029-39bc-a62e-354348875fec | -6.57525 | -47.91256 | 2026-06-09 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53bcdbac-7a03-362b-8aae-340a36a08f31 | -3.50244 | -48.03682 | 2026-06-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 580bb377-7d22-3117-b3a7-5a0b89bd3e5e | -6.65336 | -47.46711 | 2026-06-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6417a4b3-cd48-3fe7-960a-d07b34bb28ef | -7.09873 | -46.51073 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 830fef5b-ab91-3c3d-8eeb-b8dea8247a02 | -9.31633 | -45.4867 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae425b9f-be05-38cd-bfe0-63515564e104 | -8.60388 | -45.98118 | 2026-06-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb8d23a0-d95d-3d64-a704-e688d6be10f8 | -4.66736 | -41.87926 | 2026-06-09 04:14:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 41f8e8a8-e60c-3568-8092-a52a21ab2a9d | -6.57466 | -47.91614 | 2026-06-09 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a6172b8-a691-3a9e-8c08-8e95577ede1b | -3.49399 | -48.03571 | 2026-06-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e1487c72-3d09-3668-9b21-f7f32a85e0f2 | -5.79957 | -45.11193 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd4c4b74-675f-36f3-93a8-c70fcd532ac4 | -5.80302 | -45.1125 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87eee804-c595-3497-9c88-931e50d21499 | -6.72604 | -44.37634 | 2026-06-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 22aa1cb8-d209-394b-acbe-444a7ebf41d9 | -5.80525 | -45.1207 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c60794fd-bb86-3c17-8142-181fa3d1e24b | -5.04695 | -43.26555 | 2026-06-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ec0f586-7a4e-3d95-af73-4f262d1d4cb2 | -9.29774 | -45.47224 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 479adcd4-daa3-3750-99f7-56e769b73e21 | -4.84516 | -42.92249 | 2026-06-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e038aae2-fef7-385e-9f17-056ec497c270 | -7.89305 | -47.09553 | 2026-06-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a576267-ff49-3a2a-94be-0786af25a1f2 | -5.80241 | -45.11631 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8144b857-6441-3800-b78e-cc9dbcc763dc | -5.79896 | -45.11574 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ad49f9c-7ad7-33e3-90f1-a1731f405e59 | -5.2768 | -43.96471 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8031b84-5bbf-3be9-bbb6-28224e4ac64c | -5.8018 | -45.12013 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6856a4c7-5579-3a51-9a08-2eb61a0934ba | -7.59723 | -46.47378 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 845a7d7b-182a-3b79-81ea-fa959cc2049e | -5.79835 | -45.11956 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f92e4b93-f86d-3968-8480-0fab8b83d748 | -4.4812 | -44.21487 | 2026-06-09 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e02253b2-2f5c-3ed8-9964-ad3503766043 | -6.85641 | -45.0073 | 2026-06-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdef0faf-ab2f-371e-9b21-23b6ec7485cc | -7.15709 | -44.0643 | 2026-06-09 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178e9380-7b50-30e6-9704-4f011cf52b89 | -5.28796 | -43.95918 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d45d782-eb3e-36b7-851b-98fa494a90bd | -5.80017 | -45.10814 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05a97b82-5c38-3876-8c6a-4c2f067d94c5 | -7.90194 | -47.08782 | 2026-06-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 151680ba-4f05-3c34-88c1-35c9239802b9 | -9.29714 | -45.47594 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fb8e24df-83fd-3fce-bfea-74604abfae1f | -8.60675 | -45.98561 | 2026-06-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3c5e60e-71c8-345d-998b-30f1917d4b73 | -4.63747 | -43.05236 | 2026-06-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0697e9d-02fa-33ef-911c-44586f99a7dc | -8.74228 | -49.46874 | 2026-06-09 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7ff3949-5a16-32dd-a97e-fc9d763e1409 | -7.106 | -46.51187 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a1962612-bace-32bb-a461-bf06de77b3b8 | -8.61023 | -45.98617 | 2026-06-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cb0cf2a-5fbd-33e2-9bb4-4b5e3b81b335 | -7.89678 | -47.09609 | 2026-06-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bcf0aaf-a6b8-3aac-8433-20134fb6937d | -5.84175 | -43.49105 | 2026-06-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a59352d-fed7-3559-9ec2-d22ce415b4f5 | -7.90638 | -47.08393 | 2026-06-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af2914e4-1960-3919-84d5-2b31f1d72968 | -9.31293 | -45.48614 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 088f7edf-d442-35c4-99f0-252a22b8b227 | -9.30394 | -45.47706 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6ae48356-a60a-3a55-98c3-588689bc128f | -8.72418 | -48.07428 | 2026-06-09 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ba86260-c8ea-3f78-afb1-53db6316de79 | -5.80647 | -45.11308 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 857478df-bea5-331b-8a7c-07d8bc274826 | -3.49821 | -48.03626 | 2026-06-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 230157da-b54f-31be-8d66-15692f9f3865 | -5.81052 | -45.10986 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c61c70f-61b2-3cf6-b86d-2c1ec6d6dabe | -5.92187 | -42.47537 | 2026-06-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48ca11e3-cbb4-3d5e-8f00-367b8ca245e0 | -4.99631 | -42.7813 | 2026-06-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ed3846a-6298-34ad-97a4-ccc61ec01bab | -8.74654 | -49.46943 | 2026-06-09 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf85795-7f0a-3ac1-89a6-bf30b0681eeb | -5.04323 | -43.26495 | 2026-06-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fff75ff0-2ca9-35c1-8ad6-52a45b518a3c | -5.28406 | -43.9622 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f648fe7-9a23-3227-9354-b538034f585f | -4.45766 | -46.13371 | 2026-06-09 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb1cda0d-5234-3598-b676-21f8f7a0f6b7 | -5.73014 | -49.09917 | 2026-06-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e1b05c9-981d-3181-8d1d-a3b18be8cdd7 | -9.29375 | -45.47538 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cada60b3-cb01-31fc-8684-98ffe807c4ea | -8.43565 | -47.88807 | 2026-06-09 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e9e725e-edb6-3881-b32a-f7fd230d7356 | -5.93139 | -43.48369 | 2026-06-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b537333c-03a5-31c8-bf30-72181150e601 | -6.98457 | -42.88683 | 2026-06-09 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7105cac-06e6-355e-9ce9-76ed71225e14 | -4.64131 | -43.04942 | 2026-06-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d74cba-0d10-35e3-a2fe-024824697354 | -5.84284 | -43.4841 | 2026-06-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f78a4a0-15b1-3f55-862a-798a21a1aa4e | -5.52321 | -37.48681 | 2026-06-09 04:14:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 788fb598-640c-32da-baf9-8c9089027ab0 | -7.60153 | -46.47019 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3e409b3c-c2cc-3118-ac72-8546ece0c3fb | -3.49758 | -48.04024 | 2026-06-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9523855a-61ae-369b-9b94-df5642e679ff | -5.73083 | -49.09495 | 2026-06-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a7bd1c8-f712-3414-bd4d-6d4f353712cd | -9.29994 | -45.4802 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e247f1d-ae5b-363e-88ac-bc04ebcc3439 | -5.93193 | -43.48022 | 2026-06-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 92a503cd-846e-3d80-9ca7-77ba5c98e6ef | -9.30953 | -45.48558 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 798632cc-0c62-3cf2-b7d4-fc714eb7d46e | -8.97815 | -47.98 | 2026-06-09 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fea0b34-c11b-3190-a67a-2e8f61148dd8 | -11.57798 | -54.58382 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bd7aa5ee-4271-3e55-b938-4c6c030236b6 | -11.55851 | -52.78259 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 073e9ea5-6e07-341e-af04-3e6ed3f5574e | -12.36074 | -47.89607 | 2026-06-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5946589-c034-3a98-abd5-3f55d8ec85b6 | -22.80154 | -49.34405 | 2026-06-09 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0a6fbd2-5800-3c3c-ad05-c30421242ffe | -10.6495 | -49.38531 | 2026-06-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 955faeca-c32a-3645-9a13-0a33182cd82a | -11.65191 | -52.86434 | 2026-06-09 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e99dcaf-f780-36f1-8db9-d359667e75f2 | -11.78528 | -47.33347 | 2026-06-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67095523-f582-3934-8046-a9766ce1c678 | -10.90652 | -49.35022 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f53b71c-9001-3001-b8be-8b2b096e6a6b | -10.4561 | -46.47337 | 2026-06-09 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53fb75f6-fd03-3e89-b6f4-cca3dc777e61 | -11.34849 | -45.61663 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0167a454-212f-3de2-8f2d-e5aab190ed01 | -12.31901 | -46.73699 | 2026-06-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7abf2d92-a445-3e2c-a54c-b853e9441631 | -9.07788 | -50.59809 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| bdc03e95-05ef-3dc0-8670-a4291a1a7f49 | -9.62272 | -49.02679 | 2026-06-09 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7655753e-245c-3108-8206-22016b8298fc | -12.10464 | -45.82801 | 2026-06-09 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b0770a4-17ba-33ba-a039-d6d053a2c1b6 | -23.28507 | -47.31954 | 2026-06-09 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f95a57c9-e0c7-39f8-8cbe-958670319087 | -10.42962 | -49.44742 | 2026-06-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b60c3c56-3757-387f-8179-fd5b65d5d190 | -16.72558 | -43.366 | 2026-06-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da89ba8f-da0b-3c2d-92c7-8d5bcd243c17 | -10.58386 | -49.64075 | 2026-06-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9bb3cb2-4e4e-33cb-90b5-785c483ffba9 | -20.69657 | -44.27536 | 2026-06-09 04:17:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 804533fe-7f2e-3b36-a1d7-25e6a3a4dc5a | -22.80499 | -49.34476 | 2026-06-09 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ba1dc47-190d-3451-8f60-6a49318a470a | -11.95809 | -48.53331 | 2026-06-09 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e37b5069-5579-36fc-836e-5ffe9c4f9910 | -13.25464 | -44.39536 | 2026-06-09 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f81d7dcf-8752-3f4e-b1ef-51c8acf5c419 | -19.90807 | -47.97444 | 2026-06-09 04:17:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caae0e92-957e-306f-a67d-050b9aadaab6 | -12.05217 | -49.76669 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df84d3ec-8981-3870-aa95-8a9bcf02404d | -12.05351 | -49.75917 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 974450c7-1299-3d2e-80a1-58695885e464 | -22.70037 | -43.36282 | 2026-06-09 04:17:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f677c029-f045-327d-8715-a080a567eb40 | -23.50201 | -46.82393 | 2026-06-09 04:17:00 | NOAA-21 | BARUERI | SÃO PAULO | Brasil | 3505708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bda1a0ff-e497-34fc-8c30-acf777969f1b | -15.45027 | -41.37218 | 2026-06-09 04:17:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 640f592e-753f-31d2-90bf-3e21fc8eb99e | -16.72843 | -43.37043 | 2026-06-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69038bb5-30a5-35db-83ae-89de966156e0 | -9.0816 | -50.60364 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |


[Clique aqui para ver as próximas entradas](README6.md)
