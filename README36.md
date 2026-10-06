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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fadd9c4d-ff7a-3015-a661-85600cae7651 | -2.86867 | -54.13164 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f66a7b0d-a9c7-3509-9fd4-7168899c42db | -2.88851 | -54.1544 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2bfea10-b92c-3dab-bcd4-8da79433ba17 | -2.94451 | -54.15603 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b1f57b19-9546-33eb-af30-e11d6a75730d | -2.94527 | -54.15137 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c138b862-02c0-38fa-8663-40b088e958e3 | -3.3765 | -58.20631 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da0774fe-945a-3567-a9e9-2b42acda1ccb | -3.0555 | -54.16763 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e236d3-280a-3c8a-b1c0-cfe34259bd85 | -3.37795 | -58.19767 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 871f24d1-a29d-333b-857d-500d5aa6ca84 | -3.68294 | -55.96054 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2d1b795-1193-3ac9-aabd-db1e238e17f9 | -3.11691 | -53.76455 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1997c855-256e-3ac3-b64c-e4766b37ae56 | -2.98636 | -54.1295 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43d6b8cb-fe32-3c9c-8ecc-cc48596162e7 | -5.61398 | -44.84269 | 2026-10-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8afd99c5-ff31-3053-8101-311dfa4220cb | -2.95293 | -54.07613 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52ac7516-c062-3a2c-a5c0-acef16da1f8d | -3.09333 | -54.16667 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2044913a-d0eb-3e9d-ae2b-1da2d730fb0d | -3.11735 | -53.70644 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eaf61d4-4e8a-3a3b-8a3a-99650a3cc44a | -2.99468 | -54.10693 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ed4cb6a-b237-3439-a495-24936c4b4a1b | -3.06084 | -54.16372 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6dcc3d25-4756-38be-b9d4-005e368f385a | -3.66546 | -54.54757 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4ee5cbd-5583-3e67-832b-2b5523fb1db1 | -3.07689 | -54.23861 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f997e97-5a61-3188-b49e-2a3f21b8124e | -2.99024 | -54.10903 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c24411c-66b5-373d-bd3a-3e26d2b77aad | -3.04707 | -54.21912 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b3e4855-2801-3e9e-bde1-37f3bb6bf853 | -3.21553 | -53.87836 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e4b0b91-e129-3974-aad3-7d7dc969b17e | -3.07982 | -54.1624 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0cc1e4c-dffb-3aa5-8815-287b50947fd6 | -5.46136 | -45.52352 | 2026-10-06 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 079f5136-0362-341c-98ec-c4d3bafc54e7 | -2.99103 | -54.1044 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f11ae820-2759-3622-954a-d50427a50ecc | -3.07713 | -44.45608 | 2026-10-06 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77e0c29a-a43c-34fc-a81e-6f21caf92b6e | -3.06389 | -54.17379 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3e87514-38bc-3ac3-b8fa-a56eef6ccd68 | -3.50939 | -54.63463 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 361892c5-ff05-338a-a842-4df04063e2ba | -3.08799 | -54.17051 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a83a13b-dbf9-3764-95d5-9e666d252c61 | -3.86723 | -55.81817 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c45dc2-11ed-3b8b-91e6-ab5333414fd8 | -2.98946 | -54.11368 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f80bab0-a7dd-38a9-8a4b-77f55c7e4501 | -1.762 | -55.03681 | 2026-10-06 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc9c456a-6a75-3f32-b4c2-0619dd94ba7e | -3.03622 | -54.25652 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 601d764c-964f-3101-956e-934e195a5cf8 | -4.14555 | -54.03384 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 816e5b78-f468-318b-a864-c5ad3823adab | -3.33002 | -53.39443 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba87ca0-ddb8-30df-a9f5-e10ef3a93f17 | 2.45934 | -50.83327 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d405a5e1-5b46-35c6-a222-97bc30ab1e74 | -2.98178 | -54.12885 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6efb79bf-2619-3546-a2d8-6b151bfa876e | -2.89182 | -54.16177 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 60d4ba6b-f506-31fc-a41e-8c5ac959abcd | -3.15873 | -50.43917 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 08e4c8cf-6cc0-312e-8fe7-79a89db13d4e | -3.0593 | -54.23082 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3cfb29a1-6cd3-3691-978e-6cb8a2de9177 | -3.05396 | -54.20581 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae5a97d3-93f4-3fe9-9bb2-51f181a48c51 | -2.98557 | -54.1054 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27bc632c-a401-3846-ab6e-8020e27a5012 | -3.58166 | -55.40653 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea689ac5-fbc8-3c7e-9278-347c8da2f600 | -2.92551 | -54.12885 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abc12491-33bb-3ccc-af0e-8d92f4857244 | -3.10947 | -53.75434 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0bd023f-e9f5-365a-89d1-4a3d713f4086 | -2.87094 | -54.14669 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d7b6b7a8-3b70-3df3-9d53-6f7735acb40d | -3.17179 | -50.43613 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 151baca4-9dbc-36ed-b1f2-d7ba733ff85b | -3.07147 | -54.15605 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bab26217-6bdd-389a-ab05-bd68972c7bf5 | -2.78714 | -51.6721 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dbefa1f-f51a-336c-818b-b9cd9efaa363 | -2.98246 | -48.59076 | 2026-10-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcff55fd-e517-367b-8402-b88bdf3abfd0 | -3.48584 | -50.089 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e907b19b-4232-304d-a937-bb4744be782c | -3.22045 | -54.30721 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3056b30f-b1c3-330c-ad26-f58315cdc81c | -5.4279 | -43.44503 | 2026-10-06 04:38:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2af6387c-c8ca-3508-a134-33c8fb4dc941 | -3.49046 | -49.90441 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e19276b-f9c3-390f-9729-2509da4ac4b5 | -3.08532 | -54.24486 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c2c075da-278e-3515-8d21-2e3d6fa693b3 | -2.95591 | -54.14373 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1081a2b3-d02a-3cb2-bf16-cf8de7e18588 | 1.71942 | -55.65024 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8796603-2b81-37c7-93cf-c1b7eace5fa2 | -2.87648 | -54.16903 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2434f716-012f-3aaa-8306-ccf3dea54452 | -3.27388 | -50.03304 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9efb1242-9325-3b3b-91b2-66570a2089f8 | -3.46496 | -50.10601 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b95126-77f9-39a5-8d87-b25e1029a205 | -2.9544 | -54.15302 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11f57073-4d20-3ba6-a02d-b3fb1fb23f96 | -5.73436 | -41.62593 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9fb2dac-dcd9-3502-a0be-5ab63a21aef7 | -3.7359 | -48.87757 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eda9461d-0251-30f0-a3f3-adb18daad528 | -2.89261 | -54.15709 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b00b1d6-877a-3cfc-adb0-1e514a890fa8 | -3.03543 | -54.26132 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbaf782c-46ff-3a65-be56-b2ef38658b1e | -4.36208 | -47.77879 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 730f2efa-6319-317a-a91e-881daf48eb22 | -3.47451 | -55.43271 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea037c5c-53a6-3dbf-aa83-2fb43142fe7e | -3.22506 | -54.3079 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c03eebf0-912d-3dc8-b0a2-e2b5606dc77f | 2.45693 | -50.84415 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 80fbfea3-5751-31d0-8a52-a9db2826eb9a | -2.87473 | -54.15236 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 91665d65-af60-32ee-b4bf-bf7482c045f5 | -3.16233 | -50.43977 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 818c9652-55a3-3bc4-a8d7-36331e5d2e28 | 0.31936 | -51.00203 | 2026-10-06 04:38:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45411515-d3b1-38b5-a515-567004934083 | -3.06996 | -54.16534 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70cea3ea-d8a8-3311-9c91-e8609eedcbe5 | -3.10431 | -53.75798 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 07dfa407-82b7-3ef7-bf69-c0c6de34712b | -2.98712 | -54.12482 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2982f138-4e17-363f-bb33-d773bb92aa5c | -2.77117 | -54.09471 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bc08e407-48a5-327e-9898-f4f943aa98dd | -2.47916 | -56.09974 | 2026-10-06 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4274ba26-c6fb-30f3-809b-dccabefda9d9 | -3.841 | -50.31045 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd518155-7dc8-380f-8d39-2a334252e343 | -4.19212 | -44.26196 | 2026-10-06 04:38:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f6ad19d-8eda-30fd-a136-e8cf84a20541 | -2.90048 | -54.07955 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8018ae2-714e-392a-9db6-f7c0be7836b0 | -4.15047 | -53.92262 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29e014ed-5697-333e-a42d-ed161418d27b | -3.58654 | -54.3111 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3221c94e-cccf-35c7-8d9d-7acfd4d06121 | -2.55523 | -53.97761 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f0e9ea11-6862-3388-83e5-b855c2167307 | -3.67941 | -55.95041 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d31e8da-99a8-3ecb-a429-60246ca6a59f | -3.10204 | -53.74414 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a603afc-d8c1-3174-9f72-c91478a7e3b5 | -4.3351 | -43.81233 | 2026-10-06 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6357af48-60b5-3b64-974f-0cf5656f7f64 | -3.35254 | -59.49644 | 2026-10-06 04:38:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5d56b57e-c348-3499-a8df-2ac3df7c7260 | -1.08971 | -54.12087 | 2026-10-06 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4c0654d-2562-3f38-860c-3a59e7ec258b | -3.07529 | -54.24541 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 0ad725eb-6455-34c6-a46d-1a06a7d4ea22 | -5.67017 | -42.58865 | 2026-10-06 04:38:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95c6a6ad-da18-330a-a38e-7a71db432a83 | -3.12991 | -53.71299 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8a9308-1e69-3b85-9b47-2e60503307a6 | -3.0975 | -53.71655 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39c0d394-c5af-3569-a18c-07237a445572 | -3.09514 | -54.18375 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f4dfce39-a6de-35b3-8f15-0929fe1ae0bb | -2.77876 | -54.10726 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da2f7f9b-a83c-3ef6-bee3-bdcd4ba27afd | -3.22591 | -53.87099 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b8c5af6-292b-3465-a4ff-7bcf07e23fcf | -3.33248 | -44.5829 | 2026-10-06 04:38:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 026c97e9-bd07-3bf8-85c2-d19d454793cd | -3.84391 | -50.31495 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac006f3-8570-3cf2-bf54-2ad894bc4ae6 | -3.05703 | -54.15829 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f62b7454-949b-3352-b51d-7883e3ea6652 | -2.90511 | -54.08253 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33abd931-56ea-38fa-a1af-50007163632d | -3.23484 | -53.87245 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e33672e-f3d7-3aef-aa38-7069fc85059e | -3.02132 | -53.9701 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
