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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c04f2432-88b4-3594-b0b9-1fdfc46a659f | -12.6636 | -45.2776 | 2025-07-04 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 0c99056f-248b-3aba-a117-bf920593689a | -12.427 | -50.0387 | 2025-07-04 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 408.1 |
| c438119d-8ff4-389c-9b42-e842bc00fb0f | -6.0239 | -44.5174 | 2025-07-04 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 2edb99e4-01d3-33de-8c8a-849b58da1ba4 | -12.6636 | -45.2776 | 2025-07-04 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| f645fe62-6a39-3bd3-ab0c-7cc2bd347df7 | -6.0239 | -44.5174 | 2025-07-04 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 240691dd-a932-3967-9917-98bdf9110969 | -12.4274 | -50.0171 | 2025-07-04 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 252.8 |
| 858de47b-2428-3d28-aa25-a84229780a26 | -6.0237 | -44.5403 | 2025-07-04 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| db1d15a6-e6fa-3a87-943d-5b8c11978dec | -12.427 | -50.0387 | 2025-07-04 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 461.4 |
| 9c23c447-e79f-3742-9fd9-dc5015fbfd68 | -6.0052 | -44.5189 | 2025-07-04 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e08f46cf-76f3-3738-84d4-17aa4a11ee4e | -6.0237 | -44.5403 | 2025-07-04 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 70a4933c-7915-30e7-a113-b6f8ad135759 | -12.427 | -50.0387 | 2025-07-04 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 392.1 |
| 1b97a17d-e380-3386-a490-da02b95c7333 | -7.8962 | -46.571 | 2025-07-04 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7ca656b5-7014-3ac1-8178-e9fb74e824cc | -12.6636 | -45.2776 | 2025-07-04 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 54cf2908-3f88-36f0-b9b1-0520c41b21e2 | -12.4274 | -50.0171 | 2025-07-04 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 230.4 |
| fcea97f1-ce33-3707-9fe4-84e665baafb7 | -6.0239 | -44.5174 | 2025-07-04 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 6f82aaf1-5865-3b12-9f69-29d1f5f3f1b9 | -6.0052 | -44.5189 | 2025-07-04 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 21b1ce4e-b9e0-3737-b47c-76a9e92d6a4e | -12.6636 | -45.2776 | 2025-07-04 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 9c97a78c-0da2-31be-bc6c-e8d34591a909 | -12.4274 | -50.0171 | 2025-07-04 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 9d127245-ca48-3f4a-bfcd-ef0d14cbd565 | -6.005 | -44.5418 | 2025-07-04 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e9cef913-894e-3e9e-b7d2-39c16b62b469 | -6.0239 | -44.5174 | 2025-07-04 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| ff9cfff7-e109-3aef-81e1-d1675ce8c665 | -12.427 | -50.0387 | 2025-07-04 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 501f2879-f546-3a4a-88ad-465e7bffd8f1 | -6.0052 | -44.5189 | 2025-07-04 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 23e1a283-42b8-3bbe-b878-65f6b264e998 | -6.0237 | -44.5403 | 2025-07-04 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e273eead-c8d8-3c10-85b0-121404fd313f | -6.0052 | -44.5189 | 2025-07-04 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5c538c09-e1fc-3e82-b9c2-cd746f3a8cda | -12.6636 | -45.2776 | 2025-07-04 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| ab103e56-cc1e-3c3a-9f67-ea4fc2d10ab1 | -6.0237 | -44.5403 | 2025-07-04 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 88de1016-e762-3b0c-8694-2c9b19f0ba11 | -12.427 | -50.0387 | 2025-07-04 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 257.5 |
| d8912b41-3036-3f0f-9329-f1aea9cdd1ac | -12.4274 | -50.0171 | 2025-07-04 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| b8cbd54a-717b-3dfb-b170-c2083ac91f01 | -6.0239 | -44.5174 | 2025-07-04 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 7c249a24-0d67-3977-91cc-e478870eee66 | -5.1398 | -45.171 | 2025-07-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 96b934f4-6a83-3bd8-8474-eb4b48412045 | -12.6632 | -45.3008 | 2025-07-04 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| eed09076-599d-3142-9c88-dce74210d703 | -6.005 | -44.5418 | 2025-07-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 65ac1f3a-6ca0-3540-820e-2c2a57bd8f60 | -6.0052 | -44.5189 | 2025-07-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 833b2aaf-921a-3316-b748-e178a32301ee | -11.1022 | -47.0441 | 2025-07-04 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6ded6044-8fc4-3a00-aac9-0b31ef13ed70 | -12.4274 | -50.0171 | 2025-07-04 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| a12ca109-f84f-378f-9a0a-9a7e4f67b95f | -12.4079 | -50.0411 | 2025-07-04 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 155b57e9-8d76-3261-81aa-77c1f8ae0269 | -12.6636 | -45.2776 | 2025-07-04 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 344d1bb1-767d-3082-976f-0ffdd9b6136f | -6.6564 | -43.1681 | 2025-07-04 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 32231c75-d4a8-3f1f-ae80-1881d2ce9432 | -12.427 | -50.0387 | 2025-07-04 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 286.9 |
| 04f7dd7e-7a0a-3281-93d5-9d2615ea17b3 | -11.1217 | -47.0193 | 2025-07-04 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 496665b6-6590-3f19-b45c-074b15284300 | -6.0239 | -44.5174 | 2025-07-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 14ee4aab-b945-3906-abdb-2193fb382de9 | -12.2031 | -50.9456 | 2025-07-04 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5b27a103-5375-3a78-a374-ece7f06d140d | -4.0148 | -43.2408 | 2025-07-04 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 2ce812c9-e036-307c-8993-960691a71d55 | -6.0237 | -44.5403 | 2025-07-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d07b883d-227e-32cb-afa4-d59d6d07236b | -3.9961 | -43.2418 | 2025-07-04 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e21a49c6-1db2-3f59-9f03-03655d81e5ba | -12.427 | -50.0387 | 2025-07-04 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 240.2 |
| e9542734-8bd4-344b-925c-df90c054bee2 | -12.6636 | -45.2776 | 2025-07-04 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 1bb0fda8-f754-38cf-b5a6-c8424bffbe74 | -11.4584 | -45.1126 | 2025-07-04 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 18ec9350-9405-32c5-83bc-5ecea2bd54bf | -6.0052 | -44.5189 | 2025-07-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8722dc63-3f0b-3b07-adbc-881cf6320a62 | -3.9961 | -43.2418 | 2025-07-04 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 66a875b1-5712-3c52-b481-6aa92a6f35f7 | -6.0237 | -44.5403 | 2025-07-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ab7737f8-137a-3390-acd1-289075fba6c2 | -9.2255 | -48.6 | 2025-07-04 14:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2d06489c-de5b-3a33-8aa9-9f7f720a1bb4 | -11.1026 | -47.0217 | 2025-07-04 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a37e4d9a-67e5-3265-919d-f8e0183ca323 | -11.1022 | -47.0441 | 2025-07-04 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c62db941-a1c1-3900-bff8-cac7f183fff3 | -12.4274 | -50.0171 | 2025-07-04 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 186.2 |
| c470ec83-cf37-3982-9b2e-5fc16b2873cd | -6.2757 | -43.6675 | 2025-07-04 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 70b6cff7-ea4f-3f45-98fb-1e9633768715 | -6.005 | -44.5418 | 2025-07-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 67eb73a7-b6ec-3203-b800-e6b92f364b75 | -6.6564 | -43.1681 | 2025-07-04 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 311.9 |
| 1fce1daf-3787-3a1b-9092-20d5d8f2807f | -4.0148 | -43.2408 | 2025-07-04 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 28b91558-7816-38b0-bda6-449eaa73aed9 | -11.1217 | -47.0193 | 2025-07-04 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 796c1fe7-4c7d-3aed-bd95-4776bd450bdb | -12.4079 | -50.0411 | 2025-07-04 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9e691a7f-2a3d-38c4-b5e1-35bb58824f2b | -5.1398 | -45.171 | 2025-07-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 14ba6730-e949-3af1-b140-420b53160fdd | -6.0239 | -44.5174 | 2025-07-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 6c400cc0-e91f-3d6b-afe2-01e2787ad3c6 | -7.64 | -44.3534 | 2025-07-04 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| c163fd86-bfeb-3375-84ad-8162e9354c19 | -12.4274 | -50.0171 | 2025-07-04 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 39855916-c24d-3a98-af0f-7a2062df12be | -3.9961 | -43.2418 | 2025-07-04 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9bb6987b-8bac-3bbc-aa1f-c4644778ac07 | -6.6564 | -43.1681 | 2025-07-04 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 78b6ea61-fd36-3688-a53a-255ba5a9739e | -6.0052 | -44.5189 | 2025-07-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 0c0db23f-a538-3557-80ff-951e882d579d | -12.427 | -50.0387 | 2025-07-04 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 4cccd3e8-b09b-336c-bcdb-1d8f4208d1b7 | -6.005 | -44.5418 | 2025-07-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c9426ace-8a59-355f-8d52-cf8016f6db8e | -4.0148 | -43.2408 | 2025-07-04 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 178.7 |
| e15424b5-75d8-3fbd-8cb4-97d475fe28f7 | -12.6636 | -45.2776 | 2025-07-04 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 4225cbb3-6547-3777-a183-17006bae8538 | -11.1026 | -47.0217 | 2025-07-04 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c9e31071-89ab-3d2d-b06d-ba290fb30fb7 | -12.4079 | -50.0411 | 2025-07-04 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d4ffe39f-3f3b-33e0-a79f-fabe900170b6 | -6.2757 | -43.6675 | 2025-07-04 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 50e3343f-f37c-3a60-ab07-5fffb8c0271c | -6.0237 | -44.5403 | 2025-07-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ae089a40-1596-3f7d-bab2-269dbb77e341 | -6.8815 | -43.2179 | 2025-07-04 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 2927dbd2-ce3d-363c-8c2f-12f327b19dc8 | -7.6588 | -44.3515 | 2025-07-04 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ac280091-c149-393e-94f1-8d53bb272f09 | -6.2755 | -43.6907 | 2025-07-04 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9b95c0e7-b540-3a33-a405-14e2f19697b6 | -6.0239 | -44.5174 | 2025-07-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 4953c87f-a292-3812-9e34-a7c0c3cddf46 | -11.1022 | -47.0441 | 2025-07-04 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1d6c7af5-651f-31ae-be47-4d0424883a08 | -3.9961 | -43.2418 | 2025-07-04 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f9b3947f-f58e-30e2-a2f8-c8071ffec325 | -10.1961 | -47.995 | 2025-07-04 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 638c9502-d521-3bb0-b136-a63a5ea6061c | -7.64 | -44.3534 | 2025-07-04 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2148679f-faaf-361b-86ff-49efc37a4549 | -6.2757 | -43.6675 | 2025-07-04 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| c6746c2f-6541-38c1-a43b-fc7a2fc27d15 | -3.3994 | -43.1316 | 2025-07-04 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e906c354-7c6d-332d-a914-d4962de943e6 | -6.6564 | -43.1681 | 2025-07-04 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 74a24f16-8a80-364b-a6f2-797101cc8c5e | -12.427 | -50.0387 | 2025-07-04 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 520bfbbf-059c-3a49-b85f-9dbb486713a3 | -12.4274 | -50.0171 | 2025-07-04 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 40e0ea67-bf70-3e7a-94c9-64f17084e632 | -6.005 | -44.5418 | 2025-07-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4d558b28-3a44-36f6-9226-e458a4d4e9ec | -12.4079 | -50.0411 | 2025-07-04 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 7ed059f9-4fbd-3d27-9b51-397625225a96 | -6.2755 | -43.6907 | 2025-07-04 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d624cd88-f7a7-317c-98f8-40c3a0723986 | -10.8161 | -54.0334 | 2025-07-04 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 385764bf-6826-3e3c-8a9f-1403d55a593e | -11.1026 | -47.0217 | 2025-07-04 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b62066ee-14d3-3367-bc1a-274fd0f93138 | -12.6636 | -45.2776 | 2025-07-04 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 65f672ec-1371-357d-aeb2-458f5a9bd97d | -6.0239 | -44.5174 | 2025-07-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d43778b2-3fdb-3cf7-bf56-dbec22aa94f1 | -11.1022 | -47.0441 | 2025-07-04 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 63987c72-bcec-373b-af2f-bc0ff6a1cfcb | -6.0237 | -44.5403 | 2025-07-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 396164bf-d5e3-3d32-989d-b6b5583728e0 | -6.0052 | -44.5189 | 2025-07-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 85d1df47-ce3d-345e-9b7f-61b042799693 | -4.0148 | -43.2408 | 2025-07-04 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |


[Clique aqui para ver as próximas entradas](README25.md)
