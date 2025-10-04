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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f18c37c4-1fbd-33a9-84d3-558b6e83a778 | -12.535 | -45.9864 | 2025-10-04 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1258.8 |
| 21e270bd-b6a3-399c-a190-59db159b1a22 | -14.2325 | -46.0563 | 2025-10-04 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ef3dde6e-b0ff-3a4b-8dce-e650657640da | -11.5069 | -46.7671 | 2025-10-04 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d9630e82-1ff0-37f2-8187-0ab2fe973ffc | -12.5162 | -45.9664 | 2025-10-04 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 6ed63dd2-7460-3666-8418-48e4d7be6a52 | -14.2131 | -46.0596 | 2025-10-04 11:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 9ce7bf3f-1f8c-3567-a82a-05d10b94829f | -14.2126 | -46.0827 | 2025-10-04 11:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 2b5a683a-01af-36a3-be4c-49a5ff7110cb | -12.0314 | -45.1901 | 2025-10-04 11:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| a41e6862-bfae-390e-9ba5-cb16751150d0 | -13.1966 | -50.9525 | 2025-10-04 11:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 176.4 |
| a3f19d26-2730-3147-9c9c-e15c996c824c | -13.2938 | -47.5905 | 2025-10-04 11:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3a014b30-2cfd-3e58-a56d-f357b864546d | -8.9664 | -46.7557 | 2025-10-04 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 98c1e2d0-e0ac-3e68-954a-86ade7fb88ce | -13.1962 | -50.9739 | 2025-10-04 11:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 252.6 |
| 6dd536fe-4fe6-3733-84d3-6a1808db3e9f | -11.1268 | -47.9077 | 2025-10-04 11:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| f1aa81d9-fcf3-3353-8474-53831eee7bfc | -11.1458 | -47.9054 | 2025-10-04 11:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 77c4f52a-0628-34ef-a753-a09feedc56c5 | -13.1774 | -50.9549 | 2025-10-04 11:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 997ddb15-3041-39b2-9906-aa11e3bcad2a | -11.1271 | -47.8856 | 2025-10-04 11:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 001a8d5a-a7f3-3161-b0d2-1db2783ac017 | -12.0122 | -45.1929 | 2025-10-04 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 984cccef-310f-3f5e-b686-fe6663c638ad | -14.3899 | -45.9601 | 2025-10-04 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 18dd8d0a-faa7-3a97-8ee4-e2af1c98cbb5 | -8.8534 | -46.7451 | 2025-10-04 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 4690ad18-3e15-382c-9928-6ac6a6aa3bda | -13.114 | -47.9518 | 2025-10-04 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8d2d7415-f6b0-36ef-b076-511e3b2eec2e | -12.0314 | -45.1901 | 2025-10-04 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| ebd4aa2b-b76a-3736-8fb1-ec2a1c82dfbe | -13.1164 | -47.8178 | 2025-10-04 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a2f43af9-7b46-3728-8c27-d2227f21a644 | -13.1168 | -47.7954 | 2025-10-04 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 16969209-1170-3ceb-b006-a4a4085798c7 | -14.2321 | -46.0794 | 2025-10-04 11:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 4875414b-2ffe-3479-9453-e076a02e32a3 | -14.2126 | -46.0827 | 2025-10-04 11:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 206.1 |
| cc86d673-b5b4-3862-983d-d9de356fbaa8 | -13.116 | -47.8401 | 2025-10-04 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 23349108-5b77-3436-947e-ea6d82d61a00 | -13.1357 | -47.8149 | 2025-10-04 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 87bb0376-c63b-3531-b755-743d1582a6a2 | -13.1962 | -50.9739 | 2025-10-04 11:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 8f50ddf9-d708-3f76-bbb3-058fc7970172 | -12.5158 | -45.9893 | 2025-10-04 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 6f6511bf-1787-3256-9308-61c2a8ad57fd | -12.535 | -45.9864 | 2025-10-04 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 871.6 |
| aad07d72-da98-35fb-b8f4-87981c7aaf49 | -11.1458 | -47.9054 | 2025-10-04 11:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 6f09beec-0a20-3bd2-9bf3-b8d8c6a36145 | -14.2325 | -46.0563 | 2025-10-04 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| efde85c6-fc44-31db-b35c-c66b9420b4cc | -12.031 | -45.2132 | 2025-10-04 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| ba282fb0-6682-3d3b-b554-abd536642aa6 | -13.1966 | -50.9525 | 2025-10-04 11:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c01ea29b-62a4-31a6-a844-0fc8cbeb28ae | -12.5355 | -45.9635 | 2025-10-04 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 5ef595af-e7e0-3cdf-9abd-2ab1ed07f19f | -11.1268 | -47.9077 | 2025-10-04 11:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 77d5d355-6876-3b7a-8815-f20cb6a5e7c9 | -14.2131 | -46.0596 | 2025-10-04 11:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 324.3 |
| 3c1dd2b4-eaa3-32bd-b9fa-4a4cd6217b8f | -13.1774 | -50.9549 | 2025-10-04 11:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 75f5f7ae-7267-370c-a836-1ef08608fc32 | -11.1271 | -47.8856 | 2025-10-04 11:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 622d5c77-e6ff-39ae-8747-81c2b0dfd2f5 | -12.535 | -45.9864 | 2025-10-04 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 945.7 |
| a127e83e-8e38-3bcf-b578-60fe31102eab | -12.7194 | -48.5611 | 2025-10-04 11:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4206c8dc-5e8b-3a8f-acbc-9386e1e73a04 | -15.5408 | -46.8344 | 2025-10-04 11:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e2212006-12ab-3fe3-81b9-db5f0ce0af4a | -8.5458 | -47.264 | 2025-10-04 11:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 04cbc0db-a857-3eac-a0e5-5835c3bce0a6 | -14.2131 | -46.0596 | 2025-10-04 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 176.7 |
| d243e1b7-730e-3a97-884e-1d9c889bbab9 | -14.2321 | -46.0794 | 2025-10-04 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| f72c6feb-2637-3851-8a18-fa678aec84c1 | -13.1962 | -50.9739 | 2025-10-04 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 7574b694-1b52-373a-ad13-4a8eabc3a646 | -8.2316 | -46.8066 | 2025-10-04 11:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5db6c528-e9ae-3927-929f-82998d6d7eb1 | -13.116 | -47.8401 | 2025-10-04 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| aab13890-2f0e-3e03-b196-f7f22f5aa679 | -12.5355 | -45.9635 | 2025-10-04 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 8dc07c88-111c-31a9-933e-35aec792b7c5 | -14.2126 | -46.0827 | 2025-10-04 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 145.9 |
| b4f1ba04-1792-3b32-8ef2-94c12dcf248d | -13.9383 | -48.1852 | 2025-10-04 11:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9431a048-70a2-376e-a596-758e45fbf55b | -12.0314 | -45.1901 | 2025-10-04 11:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 4cbe8dd2-1524-32a8-b6c6-4690534baeb8 | -12.6512 | -46.9894 | 2025-10-04 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f379da62-9d63-3a43-a2f2-cf1827766630 | -14.2325 | -46.0563 | 2025-10-04 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 5f17657e-9097-314a-9adc-d12d49222951 | -13.2938 | -47.5905 | 2025-10-04 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5f3040fb-b4b3-3014-bc6e-4b922ce5a444 | -11.5069 | -46.7671 | 2025-10-04 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2ebde53f-1e64-32a3-8e39-1195e6f1af03 | -10.9314 | -47.021 | 2025-10-04 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 54d2e503-b2cd-3546-80ac-54254425f102 | -11.1462 | -47.8832 | 2025-10-04 11:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 552a93c6-3d8f-3e7c-9fd1-8a2ecb696b94 | -12.031 | -45.2132 | 2025-10-04 11:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| e3e88a68-fcdf-3603-a5e1-14d4e2b534e4 | -11.1458 | -47.9054 | 2025-10-04 11:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e4934d20-a9f7-3355-8653-f3541bd4defd | -13.1774 | -50.9549 | 2025-10-04 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9e09a1ff-b2b5-3167-9bf7-b710021f421f | -11.8818 | -44.9815 | 2025-10-04 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5694a51a-7843-3547-bf7c-ccade90f7633 | -9.3382 | -45.772 | 2025-10-04 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 9e0fe284-a112-33fc-982f-1eb27b3a7a98 | -11.1458 | -47.9054 | 2025-10-04 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 7a0dc013-1525-3b72-9432-70a533c6b755 | -13.3127 | -47.61 | 2025-10-04 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 49b70425-e1d9-35a1-ba91-e551f82cbfc4 | -11.9143 | -46.3953 | 2025-10-04 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 255b863a-05bf-3e52-844b-083aa856fcbc | -11.1462 | -47.8832 | 2025-10-04 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6643c0c6-3a38-35ac-af64-96ee944ccfc3 | -12.0507 | -45.1872 | 2025-10-04 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6b01465e-3e7a-3d64-916b-10832feaf24c | -13.1962 | -50.9739 | 2025-10-04 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 93f17a49-ac9f-3244-8a61-8152768bdefc | -11.9335 | -46.3926 | 2025-10-04 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 27ec38ca-adc6-39d5-bcca-c367f8ad3f6a | -12.0891 | -45.1814 | 2025-10-04 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| d44bf45e-b56f-3753-a5e4-d0e8f0128dbe | -14.3171 | -52.9131 | 2025-10-04 11:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 146ac4e9-7837-32df-ac00-3f852b4c337d | -12.0118 | -45.2161 | 2025-10-04 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6f011c68-c3f7-3939-9934-e9b6930833d8 | -17.4591 | -49.8903 | 2025-10-04 11:50:00 | GOES-19 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 125.5 |
| badd7567-7551-3e70-9049-f4163423ffff | -15.5408 | -46.8344 | 2025-10-04 11:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 169.5 |
| c27c7c8e-220d-3a0e-b1d5-20d569133191 | -11.1268 | -47.9077 | 2025-10-04 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| e0fe5b93-4b32-3333-90a2-a2a4e525d7b6 | -10.3343 | -50.3402 | 2025-10-04 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e09ef2e0-2cc1-3e78-b4bf-5f5a7ce64b86 | -12.5355 | -45.9635 | 2025-10-04 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 4ef04d14-9d21-34e2-b262-8c4f1fbfcfff | -14.0509 | -53.9289 | 2025-10-04 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 977a6e8c-89f2-3fc8-bea1-41c5e4c76ebf | -11.5069 | -46.7671 | 2025-10-04 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 1037eeaa-c409-3a6b-b5d7-9cfbbd6d4838 | -12.031 | -45.2132 | 2025-10-04 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| e10a5788-1f42-3bb3-8161-eef921dd25a6 | -11.1271 | -47.8856 | 2025-10-04 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8fe2836d-6c0a-325f-b625-4b227221b689 | -9.3379 | -45.7947 | 2025-10-04 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.4 |
| ad314ea1-d62e-3e4f-8f2e-69cb31d3fe15 | -14.251 | -46.0991 | 2025-10-04 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 420d442a-5964-36de-8d03-557b52fe1068 | -8.8534 | -46.7451 | 2025-10-04 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 18ce59b6-a723-3f8f-a4ee-1cd458457862 | -13.116 | -47.8401 | 2025-10-04 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f79ede3c-fcef-339b-b4ba-d244e5dd95e2 | -12.0314 | -45.1901 | 2025-10-04 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 307.6 |
| bdb87b86-9ec3-3930-8967-d4cb5155d0cc | -14.2126 | -46.0827 | 2025-10-04 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| f9174594-9ea8-37f8-9c95-2d496ab00ddc | -12.0122 | -45.1929 | 2025-10-04 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 323b877c-a04d-3733-a15f-46571085a653 | -9.3382 | -45.772 | 2025-10-04 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6dac59ff-6b55-3807-88c3-a44d30cde1d9 | -13.3081 | -47.8565 | 2025-10-04 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| efe8d1b3-951b-3dcc-876d-b2731e463ca0 | -14.672 | -48.2933 | 2025-10-04 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e560fa18-2289-3eaf-8ff4-31858c93baca | -14.2131 | -46.0596 | 2025-10-04 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 7072f032-bd9d-3bf9-9583-823760051864 | -14.2325 | -46.0563 | 2025-10-04 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 92e0a97e-0311-332b-b255-faedfc941e35 | -11.1458 | -47.9054 | 2025-10-04 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 213.7 |
| c5de1a83-a24d-344f-9cca-5049f1cfa86f | -14.2325 | -46.0563 | 2025-10-04 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 678da491-9ed5-34bf-926b-359956329e78 | -12.0314 | -45.1901 | 2025-10-04 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 810550c8-4763-322c-a35e-db8c3567271e | -11.9335 | -46.3926 | 2025-10-04 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 8dbb11d4-bc0d-3f1b-a317-6f5cca154c4a | -9.3382 | -45.772 | 2025-10-04 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4d73779d-39b1-3dd0-a664-047a869b9b68 | -14.6725 | -48.2709 | 2025-10-04 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f3d84ea5-4e7e-38d5-a289-0637ddf77b45 | -10.3343 | -50.3402 | 2025-10-04 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |


[Clique aqui para ver as próximas entradas](README136.md)
