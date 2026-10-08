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

## Dados Diários - Página 346

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0edf0f51-9e47-30c1-9542-538751590a49 | -3.46321 | -44.93744 | 2026-10-08 16:39:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e96adddb-636b-318e-b349-9f26f1f0d1f5 | -5.9523 | -44.26896 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| ab9dd9fa-aa13-34d8-9f50-81020477dd7a | -5.53228 | -48.17364 | 2026-10-08 16:39:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 0a2b0dc2-5c3e-3060-a0ab-8630851b7e9b | -1.37752 | -55.45013 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 53be5aeb-e0e5-357b-8ce7-ba722c4fb87b | -6.20527 | -52.86691 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8649b820-1abb-386a-8b5b-8ee139225f54 | -1.62235 | -55.10905 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 624c252b-07cd-3160-a80e-f84994a0283c | -3.04204 | -54.27454 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| bbca217e-5cde-3f39-84d2-1fdcd6894482 | -3.77688 | -52.62397 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7a1b51af-4723-3352-b6dd-5315aede1d7c | -4.57616 | -54.95747 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80b1997a-5301-3564-b366-2a669df5baf0 | -7.23776 | -55.09966 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13908e81-16b1-3a8b-accf-75b80d9f16c3 | -3.65216 | -40.9295 | 2026-10-08 16:39:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 54c4ac33-00ee-3d09-b3ee-62b98e5bfb11 | -3.17509 | -50.44342 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 21c37be9-d760-3dc4-9584-f8ff7c9ea18a | -7.22842 | -55.16602 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 038f65cb-0b22-3dcf-86ff-b02bc4c449df | -3.3015 | -54.01143 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eeb7d8d9-75aa-347d-8a7e-bbcd84197fe2 | -3.00366 | -54.07487 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 140db0ef-b2dc-3e4b-a66c-80d82f0adcdd | -3.29296 | -53.70099 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b41271c7-8392-3b81-9494-b20a23aaa61e | -3.90747 | -44.3874 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a7abfaff-4dcd-3209-8f30-a057e23b9b80 | -2.23973 | -45.99253 | 2026-10-08 16:39:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b81e3e6d-8fa4-3163-9e61-4cb96c6bcfc3 | -5.28385 | -47.91574 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| a7f9f2bd-ee03-3c7b-babb-e9437dca2cfc | -2.04601 | -56.19504 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd2059c3-0fd7-3cb7-b976-3d9cff1b8bf6 | -2.50442 | -56.1198 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 585e6aad-447a-3231-8da3-9ea3974bfa3d | -3.39644 | -43.00669 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b3122f2f-1c3d-3fbd-a283-243ea1524df5 | -6.44548 | -55.03728 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 333a017c-cb4d-3a98-910a-c0d7fb62097d | -2.94157 | -54.15391 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 761700f9-b5f8-3954-bdbb-b186e069997a | -2.61509 | -52.04417 | 2026-10-08 16:39:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 186b67fe-4abc-33e4-b7ae-0b3176c9d9b0 | -7.10332 | -55.72682 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c3f69c0e-b278-30f3-ac6e-270b498505e5 | -2.08916 | -56.62252 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d841bfe-156a-3510-87e7-19d7aa5c0819 | -1.48395 | -54.55307 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dd95cd3f-b533-3743-a535-39c3a2c42a8d | -4.35949 | -43.80227 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d1dd67d-a0de-34af-a01b-8d0d3a24432a | -5.44016 | -45.679 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f07a53b3-895d-35ef-9879-13d4c10d816c | -3.78145 | -59.25257 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e8abfc5-6ea7-330c-9202-51d9769e6ecd | -2.98382 | -54.11134 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1e41c72d-8236-3607-a579-4aade94c1fcf | -6.23821 | -52.67447 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7cbbfbe0-a5ee-30bd-ac5e-7f7eceaf9624 | -2.03455 | -55.63169 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b51e52b8-b113-351b-bdb5-e9aacdb511ca | -3.89719 | -59.45089 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 16a82471-4820-33a3-bade-d79e6edbe310 | -7.08667 | -52.68289 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 473daf39-efe2-308e-bfd3-dee46933cbf4 | -1.77344 | -55.06182 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| db9c93fc-e003-3d9b-b94c-14af512c0207 | -5.68208 | -53.49659 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 25497ac0-7da4-3233-8d6f-86b3b2d9b2fd | -2.74496 | -54.11596 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 470bdc63-5013-391e-a107-3535f10dfd3d | -1.20841 | -55.69835 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21011233-9d60-3a38-b0e7-b565787fb7b4 | -2.55588 | -57.43579 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e627551f-e1e4-3328-9eef-1861a3693c96 | -2.04649 | -56.37936 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec24c3dc-878a-3638-a080-3cce8d01bad7 | -5.39246 | -42.96145 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d1da888d-c24a-36bf-8bfa-81d1b4ae77da | -3.10102 | -50.26813 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5a3c7565-f7e7-3429-82ea-1a2a8bb453aa | -5.61772 | -51.37762 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| adf049e4-739c-333f-bab6-fe9d86a772c2 | -2.87398 | -45.74584 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9227e3f8-9829-3319-8da0-d4550d395928 | -6.15907 | -53.30786 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d66c48a6-fe7b-37b2-a797-cfd3fc48143c | -2.09129 | -46.57382 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0c1a10b0-1d06-3d49-9544-e7bb80368d82 | -2.44328 | -56.54418 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 59f2cd96-dcd4-3a1e-8a4b-6811c5f91126 | -4.61418 | -43.48644 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1782a9ce-7bb4-3512-84d3-3ac5f19928ab | -3.17043 | -58.6245 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 61a90605-140c-3d31-8c61-1d19db09ce39 | -6.02705 | -51.72295 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5b8ee96-a2a2-3773-adc8-4ef3ffefd913 | -2.07978 | -46.56498 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5026da96-4f13-3b0a-82f6-81225cba14f5 | -2.08903 | -46.5812 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 16d0b256-57e4-34ac-b430-2db6906c4c95 | -3.82785 | -57.17248 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c021cf22-8190-3650-b771-1934f5d8c36c | -4.46277 | -55.40146 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 31a65e57-28e4-36dc-9a3a-a8dd08b8e978 | -2.90404 | -57.50616 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f80d82e7-8421-3eca-bb4e-855c26dcaacf | -5.69616 | -53.49363 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e941d13b-8d36-376a-8d3c-098f63406f3b | -6.19813 | -52.78263 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67e5916a-a05f-37bc-b066-295302e98234 | -6.02283 | -51.72355 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c58ded70-f260-3b26-a065-240a74141a91 | -6.39489 | -52.71718 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 72591552-6f6f-361e-b379-0a1ee8c7c66d | -2.50897 | -56.15054 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f496fb67-f0ca-387e-8201-7046cc07ba88 | -3.7587 | -58.51262 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| c8f3a197-0c09-3e17-b5ea-f5445939b100 | -6.19153 | -52.86867 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 89f6a653-d923-3d1d-be39-4bcf5f713c93 | -5.43176 | -42.64555 | 2026-10-08 16:39:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1cc79971-1aec-3802-91f5-23328bc9a9b2 | -5.09448 | -46.21385 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 97f4a332-ced8-3f46-8195-5c79b640ccbb | -1.72696 | -45.81102 | 2026-10-08 16:39:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d27b3db0-277e-3235-81d7-5190b19fab79 | -4.7241 | -56.15667 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 63a4ef0a-5a62-3354-ad27-d6e84fc7292f | -3.08185 | -53.95103 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f4b94ef5-6da1-396f-bec8-394c75f231a9 | -5.18276 | -48.3373 | 2026-10-08 16:39:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a025917b-697a-315a-b8e2-120f25a41be0 | -1.20701 | -55.68886 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 459d8d99-5ea0-3b65-a9d4-8c8c39140cf1 | -4.08661 | -44.11891 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e7e2ce4b-7e72-3285-af7d-7709c4421e0b | -3.26434 | -54.02186 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| b8c14564-052c-391d-80f5-ab8f9b8b05e6 | -2.51611 | -57.24288 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3fe2246a-8d09-3ad9-bc5b-8ff39cba6534 | -4.36829 | -43.9049 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3e6ddf8a-71f7-322f-86c2-251992174ee5 | -1.75418 | -56.19346 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 44ea4029-74d1-3c6c-b59f-349d99177a91 | -2.22338 | -46.14955 | 2026-10-08 16:39:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7dd1aac-73a4-36a9-99df-559dad77ed81 | -2.93906 | -57.92047 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4cc5e284-4251-3b11-929e-d4c6cf9345e3 | -2.58605 | -56.17138 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 898de3ee-ec4c-3ab9-af11-465eba926277 | -3.00754 | -51.12354 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4feab320-6e4d-344c-8bbc-7b35bc35946c | -3.45127 | -60.27589 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 31a0f8a4-8d06-3ef0-aa26-3b69f40a08d4 | -2.07858 | -46.57926 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 71494f32-c38f-3992-92d4-1fc63bdf1dd9 | -3.02071 | -57.92286 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a6ed6070-ed79-378e-99ed-dec2dc582aa1 | -6.04586 | -53.48055 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c849c826-655c-3571-8971-06c6a7173261 | -3.91092 | -44.38687 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2e3c6c8-412e-37e2-9d1f-f08a79bba494 | -1.40986 | -52.72491 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 508775a0-3d48-3599-b623-3c567b7d279d | -2.99197 | -54.06882 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 16b00db9-6a0f-309c-9ebe-a523968be8ce | -4.09296 | -44.11393 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| b36a38c9-bda6-38bc-a828-596115d9aae8 | -1.18953 | -48.92323 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72d53864-33b1-381f-9a1e-3732b03a3a98 | -3.14699 | -43.033 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6eccf1b4-e153-31c2-93f8-fd92420ad053 | -3.01022 | -54.05328 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| caead914-7ebf-3201-b9dd-da0c042a981c | -2.07091 | -46.57337 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1fdc60cd-ecad-31b0-addb-e0056089bb4c | -4.86515 | -47.41018 | 2026-10-08 16:39:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a7102a93-d46a-3f82-aebe-68b0f7375a33 | -3.25115 | -57.87114 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 32d9563b-8509-3643-b11b-ba770188009f | -7.2221 | -55.16027 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e3e301b6-0272-3e63-acca-23bde8457664 | -3.32686 | -57.91606 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5fd7e0d1-c7d3-3b5d-9692-9b1288631d23 | -4.87917 | -49.10735 | 2026-10-08 16:39:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b7264976-d42e-3fe7-9ad3-b9851ebd5bb5 | -1.28456 | -55.41802 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe687b56-260d-3cbe-af49-f161a442a731 | -3.77299 | -44.35766 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ee5229a2-98d0-39d2-bb5b-9d7672321d26 | -0.90449 | -49.50929 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |


[Clique aqui para ver as próximas entradas](README347.md)
