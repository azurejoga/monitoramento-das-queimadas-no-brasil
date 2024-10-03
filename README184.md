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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb13613e-c4da-3dd9-9d22-fbaa14ce2a4b | -9.30573 | -65.37311 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4aca7b12-5031-31ce-bc1f-0379123beff7 | -9.30599 | -65.37589 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56273d87-d070-35e1-aea2-368abb7b730a | -9.30639 | -65.36843 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41436e01-ede0-3dd8-88ea-3b131d531b41 | -9.30661 | -65.37123 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe466a30-8868-3b21-81c3-9553a34c3c08 | -9.30705 | -65.36372 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53eb17d3-00c5-32f0-a60f-0662e34415f0 | -9.30724 | -65.36652 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 671b3af2-0668-316c-95b1-25ad436b676d | -9.3077 | -65.35911 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01f54b5b-5d3d-38e2-ba56-5d059207af7b | -9.30786 | -65.3618 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c82e978d-5349-3ade-aa07-3677efdc8803 | -9.30848 | -65.35722 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3b81fcf-e7a3-3926-ad24-357a6d8b8a04 | -9.31027 | -65.37391 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 332cab71-bdff-31fa-a572-3eaa6ca58de1 | -9.31054 | -65.37666 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 992b372b-933a-3530-bc23-f5b21f960c67 | -9.31093 | -65.36927 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5e73ffa-3748-32bc-830e-eabad1c1ada6 | -9.31116 | -65.37206 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e75d19be-08dc-31f3-8b99-ea20d0e554f8 | -9.31159 | -65.36455 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2eaf2869-624e-3a84-9fd8-967b63d4c106 | -9.31178 | -65.36738 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19048d20-35dc-344c-a43b-ed304744447b | -9.31241 | -65.36264 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fbe20b3-26b5-396e-99ef-4381c0b02fc8 | -9.31353 | -65.38381 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 541dc7fc-6427-3ce1-bbe3-3225d87c7b93 | -9.31416 | -65.37933 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79fd8ceb-625e-350d-9f2c-eb8f54efc5b4 | -9.31447 | -65.38206 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2472d1ad-da92-3734-953a-fa046fe80af1 | -9.42946 | -64.54894 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2f0d22e-8112-3c04-9f9c-135d2def0d5f | -9.43016 | -64.54359 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bbd2e16-d004-3209-9f29-1f6e64de366b | -9.43082 | -64.54701 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 128822ac-c668-30be-973a-2efa0ab66861 | -9.43155 | -64.54178 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96b2a489-3860-301f-803f-6bb8039e33fb | -9.43499 | -64.54439 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1b24c3ba-4cf4-3557-b305-db174058975c | -9.43983 | -64.54507 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c8b86460-3743-3a95-8513-39cd556a2d51 | -9.44469 | -64.54562 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 882b855a-df67-3b0b-aa90-24581322940b | -8.74002 | -64.19179 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd613c31-0beb-3e2d-8fbf-4cae57e36022 | -8.74076 | -64.18623 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4dfa42a6-2ae5-3996-b155-905ac68ebbde | -8.94147 | -64.19991 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ffa5555-52ad-31d1-9780-eff538f3e137 | -8.95168 | -64.36434 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d7470bf-d341-32d3-a604-fbf30a5aa6f9 | -8.95241 | -64.35889 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50e80ccb-29a6-33a2-8bbd-e0ff22210a29 | -9.02515 | -64.46931 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ce566f3f-90cc-34a4-8c35-e367f23e68d3 | -9.04326 | -64.44451 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed131578-df4a-35ba-8e93-c50e3ad9d15f | -9.04811 | -64.44521 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1814d8a-57a8-3e02-9070-4de12d51ca56 | -9.17739 | -65.5506 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4cd4c77-9cea-3804-8d4a-a6e90a880b78 | -7.28865 | -64.65501 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03dd6e20-08fd-3294-a712-3a543eaf2e97 | -7.29261 | -64.6606 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1e6147f-ff5a-388d-a776-e93a28bf9bd4 | -7.38345 | -64.68011 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5edb2136-0c6a-3a7d-af04-9da3e755cbcb | -7.3881 | -64.68079 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c99c81b9-e321-3ac4-a54e-61900cb7273a | -7.4543 | -64.44636 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aa70a02-7756-380c-9179-48ee48e0a0a7 | -7.45501 | -64.44125 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eeef76f9-a766-3a5f-9966-9f0a8a9f8102 | -7.45903 | -64.44702 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e6bd4e2-c751-37ec-a38d-cee927b4621f | -7.45975 | -64.44191 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31e60a49-53d6-3595-8d1c-7976d6b8eb1b | -7.46723 | -64.68006 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 517c94c0-543a-30f2-8c5d-c5a13dc0a918 | -7.46858 | -64.68257 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 969ea718-12f8-3c48-89e5-40b85052b8e5 | -7.46929 | -64.67767 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84f2a22e-9e72-31ec-a025-2d3d97232cc5 | -7.48347 | -63.98788 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd180cab-d814-34e3-b02d-8ef4c4320423 | -7.48911 | -63.98312 | 2024-10-03 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a60a881-fcd0-3c83-a92e-eecb00c02f30 | -10.10991 | -64.42195 | 2024-10-03 06:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af0dba22-d67b-36df-9c18-e2bd9f25dfeb | -10.11065 | -64.4162 | 2024-10-03 06:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5fc270d-9329-324b-8c52-d6ed102b2d74 | -9.75229 | -64.29804 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9dd9b89e-495c-3121-8f01-4e385ba1ced6 | -9.75305 | -64.29243 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ff2e523c-9247-3956-815f-928513cfb92a | -9.758 | -64.29311 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 798c80ec-7d7a-3675-a589-cf18c6bda4c4 | -9.7594 | -64.29474 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30724862-faee-39ab-810c-0e2a49382837 | -9.76012 | -64.28907 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 273de70f-2616-3355-9085-fd8e2ab4fb87 | -9.76295 | -64.29381 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cd84147-3559-3bf7-9996-3352a3d0cb5e | -9.76371 | -64.28815 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca3aa903-81b3-3b9f-b350-93fa8c57e5df | -9.76435 | -64.29543 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03903f3c-4bea-32a6-bdcf-b61f3ade7586 | -9.76507 | -64.28976 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66d529c9-305f-32c0-896a-9c8bb3da2c48 | -9.76867 | -64.28882 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d582b69-9ad1-3a4e-b52d-0ce514e1c6c1 | -9.77002 | -64.29044 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64d2ffa4-0c2b-32d9-b679-2f3328a553c7 | -10.26026 | -63.33354 | 2024-10-03 06:08:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e230118c-71b6-38a5-9313-793b9c74f47d | -10.2607 | -63.33012 | 2024-10-03 06:08:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08fc9e98-0368-3390-9640-579ca3f58619 | -10.26472 | -63.34106 | 2024-10-03 06:08:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e51f5ade-354d-3582-904c-8ee76b67b819 | -10.26514 | -63.33771 | 2024-10-03 06:08:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60a4b4e8-d488-30bd-9ca7-9aabaa0613f5 | -10.26558 | -63.33431 | 2024-10-03 06:08:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 434d6391-037a-3458-87cc-06a1d9e8451e | -10.26601 | -63.33091 | 2024-10-03 06:08:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b42c8286-6be7-36b2-ab10-5e81dc8e6655 | -9.51204 | -62.92643 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bf285b2-2c8e-3636-9eb6-18ed9f14da78 | -9.51416 | -62.92856 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21bce550-3664-3fca-9168-69ecd4e9f14c | -9.51459 | -62.92509 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 568aab79-11e6-3d46-b27c-14de7067c192 | -9.52216 | -63.61567 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 160d2fae-7eb4-30e8-9b62-35ea8db30c82 | -9.52257 | -63.61263 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 812a422e-d645-3302-8ca7-25165aeb5dcd | -9.52734 | -63.61626 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ecf6d30-7b08-31d4-9fe4-3e86f6b4f872 | -9.54416 | -62.80947 | 2024-10-03 06:08:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c115d03-9933-346c-b1f6-bdc889d9b6c6 | -9.54617 | -63.14944 | 2024-10-03 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41aea787-27ce-3cab-8088-bb3f91ba044a | -9.54661 | -63.14603 | 2024-10-03 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 586a72ce-3e2c-32d2-a4d4-0a942c8f16bf | -9.77394 | -63.94461 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a24e134-507b-31bf-9467-fe3852a3d936 | -9.77433 | -63.94161 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 90202a13-87a0-35d9-af94-a7926701996c | -9.77939 | -63.94241 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 002ac63a-75dd-3f64-9ab2-8b542ed473ea | -9.77979 | -63.93936 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07262998-2ef6-3858-9e9e-18de2697b2e6 | -8.17399 | -62.8387 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0789b17e-3d02-3edf-bd0e-5a9c5cec9a02 | -8.17933 | -62.83948 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e714c32c-3e74-325b-97ed-8e52c845bf41 | -8.23208 | -62.96483 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f92349d-69d3-31e5-b8f0-da351de2b033 | -8.2325 | -62.96159 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f7a7907-9113-3a72-899c-0705e92ffdcf | -8.23317 | -62.96283 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ab3de86-93a7-37d0-b92b-5f1224d37781 | -8.38784 | -63.35889 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1036092-100b-3c74-a097-ed2014827ed2 | -8.38827 | -63.35578 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 792a3928-564e-30f2-b0f6-9ead4e5a9bd7 | -8.38984 | -63.3583 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 894b26e0-0eef-3e91-8aa1-d5f3ab906fc2 | -8.39024 | -63.35518 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f82d01c-1874-3fbe-b1f4-88fdfae81d42 | -8.39301 | -63.35959 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b51c83b-0d1f-37d2-be6b-79c78dd60b34 | -8.39344 | -63.35649 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e928c61e-54ee-3178-a48d-e05a7e7ebe87 | -8.39501 | -63.359 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3a41c34-2e74-38ef-beb5-fb693b042545 | -8.39542 | -63.3559 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3dd4c4b-0a9b-3206-927e-c51d96209fd0 | -8.39819 | -63.36028 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 251a08bd-a7cc-301c-b0ca-6009966753d3 | -8.39862 | -63.35718 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ca286eb-e346-3a6a-b612-70e6d6414e5e | -8.40019 | -63.3597 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 031a62e6-f52d-301e-b4ad-6be2b55c539a | -8.4006 | -63.35658 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 492a52f9-1494-382f-9240-63acaed88835 | -8.46043 | -62.66516 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64728263-4b1c-32d7-87cf-6487cc20ef62 | -8.4609 | -62.66166 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f7e88fe-b1f9-310e-a2e0-5d27748487d1 | -8.46136 | -62.65818 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README185.md)
