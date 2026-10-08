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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f64b62fd-2827-3267-b629-3b12c50e5d5c | -2.572 | -56.1842 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1d4bd2e5-3840-37b3-9b25-9a4711c7046b | -8.537 | -66.9764 | 2026-10-08 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3f99d172-7488-362e-91b4-3bd328220005 | -2.517 | -56.1656 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a78090a0-3ee0-3195-8bcd-147bde4b6a6d | -2.7796 | -54.0937 | 2026-10-08 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 35be873a-c822-30fb-84d8-4e65950e9375 | -3.8383 | -55.9774 | 2026-10-08 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 8472febb-f1c3-3d33-913d-7fba39559000 | -2.7797 | -54.0736 | 2026-10-08 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 5a67b8f0-592e-357f-a788-987528e9088c | -3.11 | -54.1862 | 2026-10-08 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 2f32fa20-d6f8-3981-a0f1-92063c550dc3 | -7.0065 | -59.1223 | 2026-10-08 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 5f5eb1f7-7e5c-3113-8f49-451bced725ae | -9.4935 | -64.3706 | 2026-10-08 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 5f2e83c0-f4a1-31d4-b4fc-3dd7f39d332a | -3.1114 | -53.7839 | 2026-10-08 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b045c135-d2b4-3010-bb0a-7de2ee2de129 | -6.6317 | -43.73 | 2026-10-08 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 442.4 |
| 79407b92-a090-34e1-bbdb-ca68b852adc6 | -6.1617 | -47.9201 | 2026-10-08 02:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 5a139c15-f4ec-3c14-b817-53457507a3b6 | -5.6932 | -53.487 | 2026-10-08 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| d58a41ad-4e97-326a-bc08-e695b1d820d3 | -4.1176 | -59.8888 | 2026-10-08 02:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c2933599-5cdf-35ad-9f01-f6ce276bb3ba | -6.1431 | -47.9214 | 2026-10-08 02:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 0425005d-21f1-3129-879d-47303b76f5aa | -3.1792 | -50.4551 | 2026-10-08 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 2c7ac93e-99f9-3d0d-8cad-c494102d56c7 | -3.1786 | -50.6016 | 2026-10-08 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 9500d32e-59f8-35e4-88fc-086f7745ae95 | -5.7117 | -53.4862 | 2026-10-08 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 55a43b14-7589-3289-b100-0db34289650f | -2.572 | -56.1646 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d6b92dfe-70b0-3ba4-9189-d3408687a820 | -1.5306 | -54.5558 | 2026-10-08 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 76f0fcb8-e173-3247-8301-9d125fcc58e3 | -9.0591 | -65.9396 | 2026-10-08 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2d8b53bc-823a-36ac-8429-7d7bf822ec33 | -3.478 | -59.5779 | 2026-10-08 02:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 945a4df9-310d-328b-95bf-06f952f28f43 | -3.531 | -54.6557 | 2026-10-08 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| c81273f4-b576-38d1-ba2f-75e38970cbc1 | -4.3471 | -43.8021 | 2026-10-08 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 298cc679-b777-33fd-94f6-bc3691fbeda7 | -3.0374 | -53.9268 | 2026-10-08 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| a4aaa872-5056-39e9-aa9d-008cc87f0930 | -3.0913 | -54.287 | 2026-10-08 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 62d3ac20-9cf1-3858-ba69-ae0c27bad04c | -3.1114 | -53.8041 | 2026-10-08 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 0286dd4e-720e-3a99-a0e4-abbc7a278d8c | -2.4031 | -57.9041 | 2026-10-08 02:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| a2e8c3f3-2538-3825-9115-91dd658f0335 | -3.5861 | -54.6741 | 2026-10-08 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 0b738678-e578-3289-ae1c-c74fd836e6e2 | -3.0374 | -53.9268 | 2026-10-08 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 25183a4e-6803-3c31-8d26-620d6527a081 | -8.742 | -45.1563 | 2026-10-08 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 843a06ea-6fa7-364a-b938-972fcac7525f | -2.4987 | -56.1659 | 2026-10-08 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7bcb285d-2ed3-3534-a725-c7f2e07598a3 | -3.531 | -54.6557 | 2026-10-08 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f0e1bf45-b214-3a0d-8d33-f086c591f218 | -3.1114 | -53.7839 | 2026-10-08 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 2c537eeb-bfd5-3c7c-ae7e-a1a0845ab0e4 | -2.572 | -56.1646 | 2026-10-08 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 330bca7f-4106-37db-9e3a-d9cb9bee79ed | -9.475 | -64.3525 | 2026-10-08 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7aeb6bfd-90c7-33ac-9c23-0cab270480fb | -2.4031 | -57.9041 | 2026-10-08 02:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a04f6b28-e2b0-3843-9e76-5a9ed22c8714 | -5.6931 | -53.5073 | 2026-10-08 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 93545174-8d5c-35ac-84fc-fb78ebc5c713 | -8.7561 | -67.7115 | 2026-10-08 02:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e1883b39-381c-3cfc-a839-c71bc6ab2d53 | -2.7796 | -54.0937 | 2026-10-08 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 495ac296-8560-333a-9c78-a08f4b01fe02 | -3.5515 | -59.4807 | 2026-10-08 02:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| dda8d131-15e6-379f-bc79-0cb033c6c8f6 | -3.073 | -54.2874 | 2026-10-08 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6a106f1e-8cda-31aa-86cf-c7fd7cdfd167 | -4.3471 | -43.8021 | 2026-10-08 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8266eed3-2867-3ed0-b9d7-e2b2859475a2 | -5.7117 | -53.4862 | 2026-10-08 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a60ae6b0-2b10-3ece-bbd7-d389ef6ab748 | -2.4032 | -57.8848 | 2026-10-08 02:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 0b4a14e3-97cf-3c1c-a0a9-230c9a8a1558 | -3.478 | -59.5779 | 2026-10-08 02:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 3d1b7315-1549-3d89-bcf5-7daf5bc92264 | -5.6932 | -53.487 | 2026-10-08 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a7e20964-6278-3f93-a011-4269d528f2d1 | -3.1972 | -50.5592 | 2026-10-08 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b8ad76a6-b4e8-32b0-9e0b-c8405cf80089 | -2.4805 | -56.1072 | 2026-10-08 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c5dbbae2-8c47-3b74-a10e-1e82cebfbe8e | -1.5306 | -54.5558 | 2026-10-08 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 4619130e-af1f-354a-af90-a673e29fdb26 | -3.1101 | -54.1661 | 2026-10-08 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| c95624d3-1447-3d04-bc77-7b63432d3cad | -9.0592 | -65.9209 | 2026-10-08 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| bfe7b32f-e938-3db2-808a-d4e977562d4a | -2.7797 | -54.0736 | 2026-10-08 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 004031b5-f344-3b64-b4a9-a6aaf66fa7af | -3.5493 | -54.6752 | 2026-10-08 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 182ae3ed-5649-3d99-9c47-a8126e989459 | -2.4805 | -56.1269 | 2026-10-08 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7a900172-80c6-3047-9a94-6f1ba14b6ec1 | -3.6049 | -54.5736 | 2026-10-08 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 96e312f5-8904-3239-aa27-388ffb61e5dc | -3.5865 | -54.5742 | 2026-10-08 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2f1a4845-558f-3211-b689-06b5378d6b2a | -3.8383 | -55.9774 | 2026-10-08 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 54a7c2b7-d8bf-3fff-ab66-c662ca858fda | -4.1176 | -59.8888 | 2026-10-08 02:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e9bc8bbc-39a2-3f46-80ab-506c5e62996f | -3.1115 | -53.7637 | 2026-10-08 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 380e521e-d4d0-355a-9e01-b86d78473e67 | -8.7417 | -45.1791 | 2026-10-08 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 497428c0-611d-3866-815e-62d66c10a68e | -3.531 | -54.6757 | 2026-10-08 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ec15ac33-e51a-3281-845b-0593481d4cc1 | -9.4936 | -64.3518 | 2026-10-08 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 58b2c57e-e19c-317e-b1ab-1cab21728d40 | -9.4749 | -64.3713 | 2026-10-08 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 483a024f-81fe-358a-ae67-1eaa9a08a537 | -6.1431 | -47.9214 | 2026-10-08 02:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| bd1394d2-22b0-353c-8936-303d89f34467 | -3.1114 | -53.8041 | 2026-10-08 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f7057e75-af4c-3c78-82fa-2b8db56681c2 | -2.572 | -56.1842 | 2026-10-08 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 9c30bc26-9955-38e4-896c-2e44431df4ad | -2.499 | -56.0675 | 2026-10-08 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0a65b37a-d56a-3745-af49-e5a93216136f | -3.1697 | -58.6437 | 2026-10-08 02:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 97b5477c-b8f3-3826-be52-1718aa111ea6 | -3.8567 | -55.9769 | 2026-10-08 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| c90b228e-2741-372c-bd46-88f2d6f7f167 | -6.1429 | -47.9432 | 2026-10-08 02:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 6af230fd-27fd-319f-bf7b-e197fd69da38 | -8.7228 | -45.1812 | 2026-10-08 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 78a3c7fb-9ae1-37f1-bdfb-2fa444b89636 | -6.1617 | -47.9201 | 2026-10-08 02:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f43b5824-c65b-3e08-b247-e0132cf7e3f3 | -5.7376 | -45.1533 | 2026-10-08 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| cdab3a02-ff6c-33c7-941e-c301e726fe26 | -3.11 | -54.1862 | 2026-10-08 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d574be26-f91a-3921-93cc-ce356002f950 | -3.0913 | -54.287 | 2026-10-08 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8340053c-483f-383c-a301-862916e6bd5f | -7.0065 | -59.1223 | 2026-10-08 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6d7c4861-aea4-3897-9040-533efd7955f1 | -8.7231 | -45.1583 | 2026-10-08 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 87d2b429-b133-3925-a555-b8e7df340ab4 | -8.7423 | -45.1334 | 2026-10-08 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 38964831-e0ee-3492-ac5c-1f09eab123c7 | -3.2157 | -50.5586 | 2026-10-08 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1b31366d-c1f6-321d-bcc4-d4be4243c9b1 | -2.4805 | -56.1072 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| df32efe4-d9b4-31b9-809d-2d83da05f593 | -2.4805 | -56.1269 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f06f4a12-bf2d-30ee-8cae-82bee0556dce | -6.1431 | -47.9214 | 2026-10-08 03:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 43826832-6924-3f94-8d45-593ee72c8277 | -4.3471 | -43.8021 | 2026-10-08 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 690aa9d4-721a-315b-8846-b84f386e0381 | -8.7423 | -45.1334 | 2026-10-08 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 9f4dc9e6-45f9-302a-839a-4006d939219e | -2.4987 | -56.1659 | 2026-10-08 03:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b234ee44-a9c8-33b0-b442-9bc37f801235 | -9.475 | -64.3525 | 2026-10-08 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| de75e895-4d08-3dcd-81a8-b7d94211bc06 | -3.1973 | -50.5382 | 2026-10-08 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| dfde08dd-d3ed-3a74-a275-cc1ce1464136 | -3.1601 | -50.6021 | 2026-10-08 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fe119318-6335-3468-a497-44ae19cfd620 | -6.1429 | -47.9432 | 2026-10-08 03:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 51ac1396-cbda-32a1-9dd9-9137820ea03b | -3.073 | -54.2874 | 2026-10-08 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a8147e1a-a624-3c4b-b1b4-5618e2241845 | -2.9448 | -54.1501 | 2026-10-08 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| fd4264ef-e0e5-327a-b079-7851edb9490b | -3.1115 | -53.7637 | 2026-10-08 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 48bd1105-b0a0-3823-b0ab-3adb4266458a | -3.0374 | -53.9268 | 2026-10-08 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a9006b65-f713-3b01-851b-a0530fcbbf3f | -3.5865 | -54.5742 | 2026-10-08 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3dfb56d5-004a-3629-bff9-636b63723990 | -3.6049 | -54.5736 | 2026-10-08 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d6296a03-b990-3e05-a426-054036d11530 | -5.1916 | -48.2189 | 2026-10-08 03:00:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 39a5156b-dfd5-3e94-ae9f-b5822e81c6c5 | -5.6932 | -53.487 | 2026-10-08 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 13e93837-774a-3854-a6c8-bd6be520950d | -3.5515 | -59.4807 | 2026-10-08 03:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 2c870034-d2aa-3f57-86fd-65352af93a03 | -2.4031 | -57.9041 | 2026-10-08 03:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |


[Clique aqui para ver as próximas entradas](README53.md)
