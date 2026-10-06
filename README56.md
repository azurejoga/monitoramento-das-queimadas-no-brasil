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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c16d488-6a1f-32d3-8016-7aa55a4c3810 | -3.24231 | -57.86961 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e3515b-3762-31a5-bc1f-ca4b6d83daba | -3.67589 | -55.9403 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 297a1fad-d96a-3cd5-a47b-9f26ade1d63c | -2.94985 | -54.14191 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 957c333f-2362-3da0-bb63-7b8a2f921c27 | -2.99128 | -54.03609 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 511b13e7-4538-3b3c-b949-b724a2b43ed9 | -3.06035 | -54.21236 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8595a412-00ff-33b4-8287-70dc5ae6b54d | -3.46646 | -54.59634 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b41fad19-ba2d-3649-8e49-9fdde4b06591 | -3.10131 | -53.74465 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 29231fc5-2ddf-3650-b261-a7a6515b1d4d | -2.78384 | -57.65482 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad44f0b8-e023-3c1f-9449-ad174aea8aa2 | -3.3502 | -59.4954 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4030c386-7e36-38e2-80cf-f9622bde3cf3 | -3.13663 | -53.72194 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 001d5b75-9ed1-3839-b7a6-cf8d6506e794 | -1.72712 | -57.26864 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02e2766c-f41f-3a55-a03a-34322e1f1d86 | -3.06634 | -54.14584 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4186e0a-cb6f-3308-9e29-2963bbf9ddf3 | -3.04629 | -54.21966 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 945b8f65-52ff-3b8c-863e-9bcaf4c0dffb | -4.25686 | -50.7963 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6408be0d-74bc-3a96-a188-fc3a45f2e2f7 | -3.11671 | -53.76654 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 072d7b0e-4123-3d27-bda9-ae09b5945aee | -3.67096 | -54.53273 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a8e87e-f7d0-3193-a1db-4547be0f9699 | -3.49568 | -54.6277 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff38f6a3-a066-31dc-b6fa-9de3bc17588b | -3.63047 | -58.93952 | 2026-10-06 05:23:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d41a437-36d8-3b44-943d-03690f131f47 | -3.68906 | -55.95668 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bd98e19-cef1-33f3-8245-639199dc5bf0 | -3.08611 | -54.15522 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c905c2be-4e98-3250-a3bc-033e9712257f | -2.92193 | -54.12559 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 05e66c11-de8f-3b6e-9576-a4714c0596ad | -3.05861 | -54.22419 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3064ae51-5096-3de8-b986-1789ae522df0 | -3.11732 | -53.76233 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09042c49-347d-380e-9100-476528d3d07a | -3.37754 | -58.198 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22196787-edf7-3ea3-a009-5282588afc16 | -3.10311 | -53.7622 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 902701a6-cb6b-369e-8a84-9a793ab67176 | -2.93892 | -54.12815 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8aca4d13-4aea-3da4-9c0d-ebaea9039039 | -8.59893 | -66.81431 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fec257d-9e05-33e9-bc72-af2e8a3b3290 | -3.48221 | -55.43289 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3b68915-1a1b-3f62-989c-720e9296e041 | 0.31608 | -60.4413 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 078d298d-3bf3-3ff7-99a8-a5e02f95e693 | -3.06674 | -54.1688 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 584d2c46-1b00-3c4d-9fa2-57b4b5330f03 | -2.99883 | -54.1029 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41314304-5937-35a4-b54e-fde301d64bf7 | -2.95835 | -54.14309 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6a90e12-e7e4-34c9-b408-fe1c6ccff427 | -3.46701 | -54.59259 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6155f1d9-24b5-3bde-8975-048d79be7830 | -3.50922 | -54.62225 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f27b76c-d0ca-382d-868c-21517c7f05e5 | 0.44661 | -60.53671 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f20accde-31c3-3dfb-b76a-be3e9462c404 | -2.95046 | -54.13794 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f40f72e2-fa9b-3171-ad64-6e0a4d0c1f3e | -3.00377 | -54.12819 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 13e15d2a-4688-316f-8cc5-b704675cb819 | 3.0745 | -60.57277 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3a40043-dbc8-3294-8acc-046b8c8f4710 | -4.45815 | -47.92094 | 2026-10-06 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| d7968e46-6b92-3382-a280-c1e61cc7b3d8 | -3.07743 | -54.24313 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ae3db64b-12d2-3006-95bf-164771bad665 | -3.05746 | -54.23205 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45a6fd94-04fc-3091-a632-e17a0b1001b9 | 3.56488 | -61.3399 | 2026-10-06 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a662a9e1-70e5-3f05-9b4b-6b1c2c410903 | -2.89476 | -54.16181 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d028625f-51c3-38af-8ce0-d409e7586b30 | -3.16817 | -50.60185 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81819e9e-8c1b-3d35-beff-b6ada7fed713 | -3.26922 | -54.00581 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd69ddb4-a318-34ca-879a-64801ed2ab40 | -3.3975 | -59.21178 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99cb8192-16be-3e0f-87a4-353b3cd32cdf | -2.89112 | -54.15717 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d5d220a-a3cf-3836-a8e5-8bd8cef49c2f | -3.72691 | -57.14872 | 2026-10-06 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15972a2c-df66-3fc5-a5fa-c01f7d07465e | -2.07214 | -56.86039 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66298bf4-1f38-3ee6-a8ea-bf03495a667a | -3.08282 | -54.23591 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7220633b-2a76-3396-ae01-b8c5705c322c | -3.01321 | -57.7389 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec40d9ac-5664-34c6-bf22-420190ea87fb | -3.28164 | -54.17832 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34dc9e5b-d55d-38e6-9445-7ea9602c0d18 | -2.93771 | -54.13608 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53d2b7be-a353-3e3d-9cf2-aaed437a4ede | -3.1321 | -53.71902 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b93d44f-545c-337e-ae6e-b790094962a6 | -2.95713 | -54.15104 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c04831c-123c-3e3c-8b92-8d837c03bcfd | -2.76538 | -57.68305 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36e48130-1dff-311a-a1c9-e48ae3828cda | -3.80453 | -51.03271 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb3f4137-a1de-30c1-b1c4-d176df0dc732 | -2.77488 | -54.09523 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 21a53622-9099-3ff1-8c33-510c58039201 | -3.59117 | -53.47267 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9045636f-5e40-3ff2-a4a8-3038faeb5b27 | -2.96244 | -54.11346 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f95724e4-59dc-3d9d-a7ab-dfb920750688 | -3.6745 | -55.94968 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f046708d-60ce-390f-802c-b9d886eacf39 | -2.02039 | -56.88945 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae29c242-a0b5-356d-a77d-ab4bd693fc99 | -1.76311 | -54.95454 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79778fb5-c6a7-3999-90d5-93cec7644e27 | -3.67342 | -54.54514 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ea43ac2-6c96-32b3-88de-e190f0ba885e | -2.83836 | -59.24256 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2bad7964-e059-3df2-83af-b022c310cc4b | -3.07801 | -54.23922 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c29182dc-0d07-35d7-87c1-5446debc1880 | -4.13178 | -54.91413 | 2026-10-06 05:23:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53840495-eb09-34ef-8e2a-0790989ed7bd | -3.84618 | -50.31461 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4261d7cd-dbb4-3efe-80c3-a396997d2967 | 0.67109 | -59.98842 | 2026-10-06 05:23:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5dcb1f8-bf7d-338a-beb9-2596fc918a15 | -3.33069 | -50.05426 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5b5b909-4980-3db1-b065-493c3d059874 | -3.16676 | -58.6357 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca0d8f3b-fdae-3dd5-bd67-bf0244850cab | -3.27777 | -54.17945 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf37fa93-efee-3df5-9c31-20dfdb724bef | 0.44216 | -60.53011 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5dd696b-d235-3df6-9265-5911746dbba6 | -3.0645 | -54.15775 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 255d3950-2369-319f-9491-0d1d89955985 | -3.09334 | -53.70858 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a881bf7-a869-38aa-bed6-ceb090a99ce9 | -3.06573 | -54.14981 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fc2e27d-83fa-3d51-a958-121e94c895dd | -3.67832 | -55.95026 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 79b94a33-b030-3e4b-b41b-b1d690eea5ce | -3.10324 | -53.73196 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d16416d-b9c0-3c2c-bb1d-bb385c66b16d | -3.67971 | -55.9409 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3080856e-3d2d-365d-9c8b-5285a9bb20cd | -3.38436 | -58.19904 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 48e0d7a0-1b98-3df8-ac2c-ed739f0d8298 | -3.11685 | -53.76002 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 088ec94d-2a1c-30d7-9f6c-351629d519ee | -2.87827 | -54.12701 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33dcded3-71ec-38a4-a115-76ef7f621278 | -3.49868 | -54.63585 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ce36efb-372a-3efa-a200-3119e060c63f | -3.1094 | -53.75023 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ded8045d-b42a-32e5-929d-b0763ca7dbc7 | -3.06025 | -54.15714 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 452e868c-42c4-37d0-8b38-25f0059edc15 | 3.0688 | -60.5812 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 70ecbc18-1ab0-315b-85bb-bd4e35cfa547 | -3.02088 | -54.18757 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23986539-9e05-36f5-92f2-1088fe921e8c | -3.11215 | -53.70287 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bede51d7-898c-3063-84b8-ec6f999ad7c5 | -3.08372 | -54.17139 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd2ffada-a9f0-3481-9fbc-731e8ef9fb12 | -3.51101 | -59.51009 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a9cb319-021a-399d-af01-72ff3179b825 | -3.22593 | -53.88094 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fb36362-db37-3940-9d15-2d38e369469b | -3.66868 | -54.54834 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aca763f3-68d4-354e-8bb7-e3abd2f25ca1 | -3.27291 | -54.01057 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c906d220-954c-3502-9b72-673d48adf725 | -3.02532 | -53.89532 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e52af367-db84-31f2-acfa-880e9062aa9f | -2.87286 | -54.13425 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcce67db-e72b-33d8-b62c-82b4f50b01ab | -3.52049 | -54.63172 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba95212f-6502-34d7-a7b2-d91907d65a96 | -9.16651 | -61.40638 | 2026-10-06 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 16ddb6a2-40bd-346b-b35f-2b5538050f3c | -3.4623 | -54.59577 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2864bcab-dcac-39d3-8b2b-2c46b0dfa4cf | -3.67901 | -55.94557 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7afac605-8bab-318a-9734-b19a1e839d7f | -2.87593 | -54.14277 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README57.md)
