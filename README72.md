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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac8798a2-2efb-3bb2-a044-a8eebf96d717 | -8.77045 | -68.9963 | 2025-09-09 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2e668c3-8724-3ae2-9d2a-5b0ccfaa9e51 | -9.05927 | -62.33788 | 2025-09-09 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b157582f-dbb9-3792-80b6-7bac33d827b1 | -7.55641 | -69.90411 | 2025-09-09 06:14:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af93749d-21db-3c8c-817f-b4bd262e8d1c | -8.98521 | -65.44646 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32e75b24-4145-3208-b0f1-51e797c5bc3e | -5.5032 | -60.13188 | 2025-09-09 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ae04773-c63b-3a6e-ae2e-8f57091cdbec | -9.08099 | -65.41642 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c05ed850-c1ef-3417-833e-196d5deefec3 | -7.40355 | -61.62739 | 2025-09-09 06:14:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 347ed0d9-e1ed-3477-b385-b050e2339d04 | -9.16188 | -60.79635 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699ea8e2-a34d-3876-8045-d1d03ceae7b7 | -9.13687 | -65.96095 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13129948-7e2b-3c98-8c7b-66428e08e3f1 | -8.65644 | -68.74197 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dee1461-dd93-3abd-a570-d1047656ae3d | -9.34677 | -65.44269 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3720f64c-6676-3b81-a6ee-83c11ca80ba2 | -9.20395 | -67.56636 | 2025-09-09 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d3683b0-ea6a-3d1e-a3eb-07e55fade5db | -7.58105 | -70.21945 | 2025-09-09 06:14:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a635f756-2bab-3b64-bb0b-4429253ca500 | -8.53413 | -70.04551 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74da9050-7ab5-313d-9f3d-da669e305289 | -9.44107 | -60.51841 | 2025-09-09 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8eff1629-72c7-3e65-a789-66c6a53771ea | -7.82306 | -63.57927 | 2025-09-09 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c708409-47e6-31a1-a1f6-4f8f69bb8df5 | -8.79816 | -71.04687 | 2025-09-09 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd93a284-97f7-3bc3-9717-f692e429dd2f | -8.87482 | -64.03272 | 2025-09-09 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca157582-e61f-374c-8b11-16aff87feb54 | -8.76334 | -69.35342 | 2025-09-09 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd20efef-8755-3fa0-b085-18915c0c14cd | -7.39649 | -61.6317 | 2025-09-09 06:14:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6951ddb-5b84-3544-9715-ef5533f8225a | -9.0855 | -65.38271 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 631bafdb-05e6-37fb-9099-8b384dad67cf | -9.38935 | -65.94011 | 2025-09-09 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25ad990b-1be6-3840-bf08-1e2d2882d814 | -9.13812 | -60.52905 | 2025-09-09 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f2b1b8b-784d-396b-848d-8291155a4d62 | -9.75482 | -65.01789 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3479b7f3-ff03-3d94-b9ab-65c5c7671668 | -9.44989 | -67.6712 | 2025-09-09 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 355c1205-0e23-352f-987f-e5aa380c292a | -12.87475 | -62.11806 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bc0d70c-3573-3367-8e31-ab34f2bc3d6b | -9.9988 | -68.83418 | 2025-09-09 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30b0b2d-3ceb-3e5e-850f-f8799e83015b | -12.88331 | -62.10125 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8510b3c0-5e7d-3d01-bd3a-d5bc437a94f3 | -9.52793 | -70.42968 | 2025-09-09 06:16:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06160766-d22d-3e21-8988-973f0aa76752 | -12.90584 | -62.08007 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9ff35fc-92fa-3b9e-8d9e-c9dbc9098725 | -9.44346 | -67.55698 | 2025-09-09 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5c83009-1cef-3241-bcc8-776ffbdc5d85 | -9.75395 | -65.0246 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64062084-9c54-3050-9864-7ad6c5ca98e9 | -12.88395 | -62.09538 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b24e0bb9-4509-3c67-a934-0e28304a4076 | -9.8768 | -67.90083 | 2025-09-09 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1d5db9d-2a90-30d3-8ee5-6bcb32c7e23c | -9.98784 | -64.99542 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aa5869e-5e66-38e3-a9f7-f2ce61533b19 | -11.89964 | -64.99483 | 2025-09-09 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6264e54f-d68f-3ee2-9826-d64861732126 | -12.42685 | -63.89285 | 2025-09-09 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c503a1b-544e-3da6-80d8-99298f742302 | -12.89855 | -62.08509 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abdaa291-d941-3e46-9808-ef503dd24803 | -9.74907 | -65.02055 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 762d66b5-1904-33b4-a877-9563e4da6dc9 | -9.4493 | -67.67561 | 2025-09-09 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 097c08fd-e6f5-3505-8a24-b0f4a27088bc | -9.93513 | -65.23678 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 619ccbe8-61c3-3543-852c-f6e89a72003e | -9.98828 | -64.99203 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80e6e9c6-d4cf-3180-966e-0f915b8cc575 | -9.67697 | -65.53621 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7ef9d35-abc3-3d9d-800f-2b80d7d559d4 | -10.00775 | -64.92583 | 2025-09-09 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b2ee98d9-edf2-3616-918d-0b2f1b1edf2d | -9.98741 | -64.99879 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26905075-ff76-3769-91f3-f756e9b204a8 | -12.90299 | -62.08146 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1fc6a55d-c45b-3069-aabf-e5b8d0d09da1 | -9.91901 | -65.23779 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df474b9c-dd9d-3f26-abfc-1c51e78f75aa | -9.93472 | -65.24001 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85b29fbc-abfb-3bde-bd92-b23c25492eae | -9.44522 | -67.6731 | 2025-09-09 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c47cc9a-a416-3f5f-a212-7381fb3db7e4 | -9.75352 | -65.02795 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01b5072a-6512-3e8c-b77e-bd2f8c430273 | -9.91618 | -67.01288 | 2025-09-09 06:16:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 905dfdb6-cfa2-34dc-9ec9-4cdfc30a4e5a | -12.87539 | -62.11223 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9e75a58-3c81-3a81-a59e-9182eddec071 | -9.8922 | -67.8857 | 2025-09-09 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b77128dd-05ad-3208-aa2b-4feb6f8dc9aa | -11.89416 | -64.99423 | 2025-09-09 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f1353a6-56cf-3c69-ae50-16668969ada4 | -9.44549 | -67.67054 | 2025-09-09 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ee59256-ff42-3770-903e-1c15166dac7b | -9.67657 | -65.53926 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1fdb85d-c5f0-3dad-97c7-f85e392341f4 | -12.42735 | -63.88849 | 2025-09-09 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09b0c3e0-0589-3108-86a7-618137b5c15f | -12.42093 | -63.8921 | 2025-09-09 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8210d42c-8451-3a30-8dd1-c6d5ec11e1ee | -12.87603 | -62.10633 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 569a2c06-0045-3627-8133-593abd7a7639 | -9.56178 | -66.73447 | 2025-09-09 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 952eb0f6-3fdc-3d8b-bea9-cedad553e74b | -12.42142 | -63.88773 | 2025-09-09 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f904f6d2-df42-35c6-8870-8a8ec9277623 | -12.42043 | -63.89647 | 2025-09-09 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24b30701-2ba7-3a89-973d-9c59efbdb7c5 | -12.87731 | -62.09457 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6f6ebf9-ba03-3007-ba16-52e74c582012 | -8.85022 | -71.28296 | 2025-09-09 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfc9e986-5486-379d-8395-dc37a2a03e67 | -12.87667 | -62.10045 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeb01652-93d9-3682-b6c7-7965c32e20f6 | -9.91154 | -67.01225 | 2025-09-09 06:16:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13effaa6-8947-3e80-a5dd-eaa2e76efd6f | -10.00819 | -64.92245 | 2025-09-09 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4bdf2d51-181a-3060-bc3c-e8da68ce9fe9 | -12.86939 | -62.1055 | 2025-09-09 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fe63734-8150-38f4-a075-c9ed5943514d | -10.00863 | -64.9191 | 2025-09-09 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dc61c48a-7705-3c29-9c4e-8e1b5660a0dc | -9.75438 | -65.02126 | 2025-09-09 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5d03b4d-8100-3a10-abfb-390745051c4a | -8.85254 | -71.36422 | 2025-09-09 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c34b45-addc-324c-a18d-a33c30344efe | -9.44962 | -67.67376 | 2025-09-09 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d144dbcb-e987-32c9-b85d-9443a710099f | -9.40843 | -68.23676 | 2025-09-09 06:16:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28a70acc-8df9-38f8-a11c-222a0558badc | -12.1991 | -53.8817 | 2025-09-09 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 27e74360-f7f2-3f8e-a38c-c930f5dbd4b4 | -12.1988 | -53.9024 | 2025-09-09 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| aa7da9e9-c1a0-3d6a-95ae-55461c4a6963 | -21.4555 | -48.8455 | 2025-09-09 06:20:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 04eb89e0-eee4-326a-b9df-b6b2906024f5 | -14.3615 | -47.3333 | 2025-09-09 06:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 05e122b6-b05c-300a-981e-32bdf8e2f9de | -14.362 | -47.3107 | 2025-09-09 06:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 740110bb-7b9b-3ac7-8010-504912251e57 | -11.9926 | -51.0126 | 2025-09-09 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 9ac1c273-f259-3984-a8af-4a5c6c5a221a | -12.1991 | -53.8817 | 2025-09-09 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cacece4f-cffb-3d84-b88e-3d9ce8de4bce | -21.4348 | -48.8503 | 2025-09-09 06:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 05f28d53-4698-397f-b3c8-74fd148b75cc | -12.1988 | -53.9024 | 2025-09-09 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 914a4c09-96b9-3ae9-80ef-7d0ef61bc4b0 | -11.9735 | -51.0148 | 2025-09-09 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 25ecd0a5-62ea-31c4-9c7d-fe8997fe3daf | -10.9815 | -45.0874 | 2025-09-09 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 27c87b87-bbb6-3d51-9b55-4477a84fb27d | -10.962 | -45.113 | 2025-09-09 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 6ee9e79b-b3e9-3b92-a3ee-4ddf4231f1fd | -21.4762 | -48.8406 | 2025-09-09 06:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9d6eddbd-133a-3bdb-9ca9-7ad5ea75ec9e | -12.0298 | -51.0722 | 2025-09-09 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| d9b55967-6eb2-3a35-b10d-cb105059352c | -14.3615 | -47.3333 | 2025-09-09 06:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 74772e41-d00b-3e0f-a763-869df716cc98 | -10.9811 | -45.1104 | 2025-09-09 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ce364822-38bd-35ad-b0c1-1cc99c8ab553 | -21.4555 | -48.8455 | 2025-09-09 06:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 234.6 |
| c2312c3c-074c-339e-ad48-06ef4bff9f05 | -12.1991 | -53.8817 | 2025-09-09 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ea1f6366-7061-3540-aae5-d602e6bbbe27 | -12.1988 | -53.9024 | 2025-09-09 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| aaa8012d-020c-391b-a0d4-38b2ce92ac1b | -10.9811 | -45.1104 | 2025-09-09 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b9248031-b0a3-3aba-b40c-d4e48bacb725 | -21.4555 | -48.8455 | 2025-09-09 06:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 10e8eadd-9ef4-3342-a0d9-41af65c1f5e5 | -10.9815 | -45.0874 | 2025-09-09 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 22400198-ac57-350c-a476-082d791180c1 | -11.9926 | -51.0126 | 2025-09-09 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 128eaeab-9d6b-3bb3-91e3-ecad98b6f014 | -11.9739 | -50.9935 | 2025-09-09 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 96c7606e-4c67-3123-8c41-a40f633731d1 | -10.962 | -45.113 | 2025-09-09 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6e171ed1-fba4-308c-aa7b-3ef20426cf6a | -12.1988 | -53.9024 | 2025-09-09 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 002d6a96-d27e-3bd1-b5ec-81987754ff07 | -10.9811 | -45.1104 | 2025-09-09 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |


[Clique aqui para ver as próximas entradas](README73.md)
