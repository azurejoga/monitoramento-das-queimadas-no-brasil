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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a662249e-34ce-3331-be3e-a12272bddfea | -11.32111 | -63.2723 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed7448b0-c341-3d23-9ea1-1cc4f75cce50 | -8.75074 | -62.38898 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd36ef37-097d-31b1-98af-c71d203d774b | -11.28191 | -63.23584 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94c170b2-44f2-3339-b258-371b39563926 | -10.30755 | -68.2663 | 2025-08-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec25485-a06b-33cb-9cf1-ea2c31faf071 | -9.46519 | -62.338 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c6de2ed-784d-3eb5-b29f-f55ecace54c6 | -10.75432 | -59.82703 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76224980-3e61-37ed-9483-d94a9bdcec4b | -9.27614 | -67.64912 | 2025-08-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c3b4309-c210-30bb-8da7-068b05f68dfd | -9.45332 | -62.34089 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5a6dbe60-d02a-3baa-8918-55c48072db04 | -8.09888 | -71.24708 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a90e6d-8501-3aff-9e26-c5e2694ef9e1 | -9.43029 | -62.34198 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1f9cba0-cc79-39c3-882e-2d3ff376000b | -8.86541 | -63.02602 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114a6e04-8b87-3cdd-bd95-71cc73adff9a | -9.06961 | -65.42136 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 686d038d-dcdc-3137-b57c-69a9dcb2a029 | -7.68196 | -61.08479 | 2025-08-31 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3fe5d4be-88c8-3ad7-9bf2-e33daa944059 | -8.8523 | -70.62135 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c2a8bee-dca6-32da-87be-aead2001c5fa | -8.76143 | -71.06643 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9528351-da74-3ffc-b098-df4f8bcfffd9 | -8.63795 | -61.93394 | 2025-08-31 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d152685-eccf-3032-9052-09a9f0eb9e3e | -7.89772 | -63.00908 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 935b8efb-f5f7-38c5-9d06-36144d32075a | -15.23044 | -56.07566 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f0f5354-f960-3809-8ecf-ef3c01780f9d | -9.11276 | -61.19872 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97997ad2-b74d-3aa1-8b64-b24057d98df5 | -9.45641 | -62.34592 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fde350ed-2b6c-3eba-88ae-b35dfb29f2a6 | -9.76344 | -67.54219 | 2025-08-31 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adedd8d1-c7eb-3bd4-8846-3531a3c34188 | -9.43638 | -60.54066 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be4c1aa2-ed3f-3ad4-bcd6-b05670eeabc6 | -8.34257 | -62.93478 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb78f014-0071-3e5c-ad15-c89a7d60caea | -9.07239 | -65.42538 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85a12e4f-4470-399d-a52b-8b892b506ab1 | -10.75043 | -59.82201 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de4c3e8-bcd1-335a-894a-68f3d5fd5374 | -10.31226 | -59.21138 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86e6af77-5fb4-3927-bb13-f4c0ed79d716 | -9.43807 | -60.53937 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65756465-14e2-3560-b2d7-fdaf0c31451c | -8.73597 | -62.38673 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 820d105b-cbcd-3183-9882-a8f7d0c66f44 | -7.83065 | -71.94548 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2399009-3f2a-3cc5-8606-cb8ef44e95ce | -9.43702 | -60.5471 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e751c6-f458-3450-9bdb-c5a3e0c827ee | -8.38435 | -70.83182 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1477a215-a98e-3fc3-ae19-bed720f6f006 | -15.79412 | -56.40089 | 2025-08-31 05:46:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d571a35-8f8c-35fb-8f95-2cba41c8bf1c | -20.69198 | -54.58974 | 2025-08-31 05:46:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cec1b7ec-c859-315e-8590-a625eb131eb8 | -20.68697 | -54.58583 | 2025-08-31 05:46:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bf396521-60a6-33dd-a1e4-98bf94da11cb | -15.79461 | -56.39622 | 2025-08-31 05:46:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0181e238-46ab-3626-be30-3d46da3bb238 | -20.68645 | -54.59285 | 2025-08-31 05:46:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4715b7c8-156a-3098-be3c-e35a0df9d7a8 | -28.71387 | -55.64455 | 2025-08-31 05:48:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| d2276dbb-2444-3ae1-8948-82b5bc1a01f7 | -28.71419 | -55.63704 | 2025-08-31 05:48:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.7 |
| a9c38654-b245-347c-9056-20f821ca1f8e | -28.71355 | -55.65203 | 2025-08-31 05:48:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 6b9032cc-0a6c-31ac-bc4e-d310333fe7fa | -11.8181 | -46.4314 | 2025-08-31 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7e80a39a-1403-3ed9-9509-b908edf11829 | -9.4497 | -62.3485 | 2025-08-31 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 36fafd83-d468-3860-80ad-a1003ad8b48d | -11.8177 | -46.4541 | 2025-08-31 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ba5ab0a0-418f-3013-82c0-436e08b0056c | -7.9265 | -63.0158 | 2025-08-31 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 9dbac8bc-039f-345f-bbd3-274f3170b9a3 | -9.4683 | -62.3476 | 2025-08-31 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f8f64892-a5d8-3a30-a333-b9fc3a7073a7 | -6.5758 | -43.6885 | 2025-08-31 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 04c72db3-ed69-3e31-a3e7-6f03c7b8fd92 | -11.8373 | -46.4287 | 2025-08-31 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ea5566e6-0db6-371e-8067-15ab2b090c70 | -9.4432 | -60.5692 | 2025-08-31 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f228ebb9-73eb-396e-98b7-3f5880e9f22d | -10.0434 | -48.0998 | 2025-08-31 06:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| d0b4b3d8-22c7-3095-ab35-e58f598ee61c | -9.4497 | -62.3485 | 2025-08-31 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 3a185e22-2f45-3f76-9109-a93d7bcb2886 | -16.2217 | -52.6992 | 2025-08-31 06:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 71e71c87-e320-32b7-8842-681b60d3916a | -11.8373 | -46.4287 | 2025-08-31 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 4986528e-9626-3607-a834-ddfb9beb6f6c | -9.4432 | -60.5692 | 2025-08-31 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 431d7238-0d41-3703-bbff-8d33df915a9d | -7.9265 | -63.0158 | 2025-08-31 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 53442845-8d42-3566-bad4-86cf17c9acad | -11.3293 | -63.2681 | 2025-08-31 06:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 15945013-5902-36a2-9d70-671ea1b67c35 | -11.3504 | -43.637 | 2025-08-31 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c3375d60-ce2a-3887-a333-1990720aa081 | -11.3106 | -63.2691 | 2025-08-31 06:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c6631d49-17d1-3ec0-aa34-7b01ffc670ed | -11.8181 | -46.4314 | 2025-08-31 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bd1a58e5-e86e-3a88-a07d-19e1000728a9 | -9.4683 | -62.3476 | 2025-08-31 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3d4bc60a-24e3-3a3b-939f-a69f05ba1c00 | -9.4495 | -62.3675 | 2025-08-31 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 40509d74-2ca4-36e6-8c53-2708970ca78a | -11.4045 | -63.2453 | 2025-08-31 06:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 09114ddb-6b03-3edb-b9c0-f464fc378b03 | -9.4432 | -60.5692 | 2025-08-31 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 55fe90cd-ccc4-3c15-9897-4b9084eb8f23 | -15.7298 | -48.9446 | 2025-08-31 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 195c9ac2-e3a8-3c58-8115-8de5e1f20063 | -15.7294 | -48.9669 | 2025-08-31 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3b548e28-1491-3a3a-a8e2-c18947a7bfe7 | -9.4683 | -62.3476 | 2025-08-31 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5b2cb628-7539-31ad-b678-9eddadffbfc1 | -11.8181 | -46.4314 | 2025-08-31 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6258d5fa-a978-3ff4-ba55-11e46c9c8514 | -9.4497 | -62.3485 | 2025-08-31 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4e24a4a7-dfae-329d-baa9-a6479df29ef8 | -15.7102 | -48.9479 | 2025-08-31 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 94274192-011f-369f-a1e3-3bc05668f70c | -16.2225 | -52.6565 | 2025-08-31 06:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| b0574225-ff0a-33eb-a9cf-040df7025a1c | -11.4233 | -63.2444 | 2025-08-31 06:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 97.4 |
| cf9edfa2-2613-3e03-9abb-8c92dd4149d2 | -7.9265 | -63.0158 | 2025-08-31 06:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9965d7c2-644f-33df-9776-73fd3d9032de | -6.5758 | -43.6885 | 2025-08-31 06:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f20e80f6-ea4b-3607-8a65-78dde9c2f994 | -15.7098 | -48.9702 | 2025-08-31 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 38379ecc-4e37-3007-8b9a-b85a5e44403d | -9.4495 | -62.3675 | 2025-08-31 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5794025a-1fa1-3c26-b533-2e432886487e | -8.235 | -72.81136 | 2025-08-31 06:10:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5e23d10-88f0-3441-b71e-a7280fb6196e | -9.45869 | -62.33625 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccd6ec96-2b0b-366b-95ef-15d926ec7bc1 | -9.42958 | -62.33987 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e99efd0c-20d7-3759-9043-6a48ede9afea | -8.60382 | -70.90533 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a880142-b0bf-3928-8000-0f616c2fa494 | -8.67117 | -62.42378 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 900577a1-c843-3b75-8c4e-ff28d637b719 | -9.46336 | -62.34444 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f0c06d5-9d4b-3158-889b-34296a815378 | -8.88679 | -62.3884 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f494f8f-7d19-3da8-a0c8-7e9d61874ab6 | -9.57308 | -66.6896 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 168e5bf7-3bcb-3ba0-907c-fae69dc42735 | -11.41671 | -63.23994 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f024498b-e0af-37d5-8b42-4a7802bd60f7 | -9.44229 | -62.33 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa2ff6df-5e08-31c7-99a2-583f495267db | -8.24565 | -70.83514 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1821423-3275-316e-88ba-3db92bcf99b6 | -8.73736 | -62.38332 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa040854-7fd3-379e-a9a3-dd43a2c4d54c | -8.38808 | -70.83486 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1b18c73-28e6-3adb-8bfe-f1f9fdfb50bd | -7.90252 | -63.00996 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcb549ad-f1b2-3916-839a-637e51bf098d | -8.66001 | -70.03829 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24702826-9089-37a2-9428-b321a2094bd5 | -9.43793 | -62.36411 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5e61cdd-cd14-3678-9f06-7b57a6a2a641 | -9.69812 | -61.28206 | 2025-08-31 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3bddddc-b1ad-3ad2-a82f-e5bdfa5a135e | -9.95478 | -66.8754 | 2025-08-31 06:10:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f22ce9e8-65b2-37c0-ab0c-2b6f5007decb | -11.41585 | -63.24702 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bd4523c5-8b33-3baa-a391-61b9b5162197 | -9.4471 | -60.57827 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce626e24-13d5-3eb3-9224-fef5c246a874 | -11.28172 | -63.2418 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e80eee96-4fce-3128-b822-b02faa393ba4 | -9.27706 | -67.64613 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b843adc2-3093-3a4a-a644-2e314c095a1b | -8.53764 | -70.74764 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34e6c8bb-3a9e-38f3-889f-943b6c14c722 | -8.97781 | -70.74483 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f6b5608-89d7-393a-8e9b-09f20f301dc2 | -8.6769 | -66.93417 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bc68762-0024-3253-9d99-006cf4773dac | -9.44598 | -62.34599 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94c5e3b0-1826-3321-bd67-91c21e393a7e | -8.73589 | -62.39439 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README79.md)
