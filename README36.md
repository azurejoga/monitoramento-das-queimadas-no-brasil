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
| 17a5e3d4-d831-35cb-84d1-b2b196e71610 | -4.59875 | -46.59686 | 2025-09-06 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efee67fa-f741-3f43-9923-b704bb225bc6 | -6.39264 | -43.81678 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08f6210b-73a3-3003-b9b3-574c12e5d862 | -7.59368 | -46.20879 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c7c0ac3-0c01-3df9-a02d-4f8177992473 | -5.87249 | -46.0509 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8218c05d-d542-395d-9683-ee9a2cddbfd1 | -9.82896 | -46.53339 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b663a0c9-90b3-39a0-8027-ea40deb17739 | -8.35435 | -52.52016 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9def6b12-4e01-30b7-846b-de6a8e58cfb5 | -16.92366 | -45.75197 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce6b7a90-edc2-3a7c-94b3-e05ddfa325fa | -8.87789 | -47.91584 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60e27d4e-4700-31c3-add7-9be3a75fa7b2 | -6.49513 | -44.20677 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ef603e9-b129-39f3-9809-e2dda4c30980 | -8.35376 | -52.55333 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3c51ab8-a498-3e8c-bbba-c3b3ea5c1bea | -8.89493 | -45.7589 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5623f06-ff7c-3e3c-b917-b4942c81cfe4 | -7.33952 | -43.94641 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5e0285b-0752-332d-ad80-bc20e0905372 | -13.01947 | -54.83805 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24317ee7-abb1-321f-8547-a418d7f7c1dd | -14.89782 | -49.45439 | 2025-09-06 04:17:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 10fc9c6c-9404-3761-be91-1aad56747efc | -8.09248 | -45.324 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 839794bd-b01d-3bf2-8071-66f71f240d90 | -6.53998 | -49.49823 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1fe5c92-3d06-37ee-b272-9091c6931653 | -7.65288 | -46.72918 | 2025-09-06 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59698a6c-65da-347f-b442-458efa7cbcc4 | -6.11516 | -43.93953 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2dc8fe2-9f4a-3bfe-8ffd-9cbd47cc797e | -4.61021 | -41.54439 | 2025-09-06 04:17:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 031a12bc-cf9d-3ad9-b62f-d3b704c8c598 | -12.95735 | -54.79648 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42627f07-30e1-3587-9d13-b81731b57035 | -13.84331 | -46.272 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0a5c3c9f-5a74-3596-9c4f-6129caf47a42 | -12.63387 | -56.98237 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ee3ee3-672f-3381-b760-e5eb82f35ca8 | -7.21081 | -43.98725 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 345a7ff8-9125-3adc-a393-97589f6e3837 | -8.06934 | -52.37355 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fff28b1-8ffc-3c1c-a677-3ee5aa613d2d | -5.96928 | -45.73072 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 69b1ac19-ffac-3c89-b7d2-32715adcdc08 | -5.98117 | -53.60115 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60f9fd51-91b1-3ae6-9ffa-263603cd4e56 | -7.73038 | -50.32286 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 883cb57e-2e55-36bb-b6f3-208739f835a2 | -7.00234 | -44.93878 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb413b12-60b0-3f12-9e2b-b10f414ff701 | -14.18401 | -53.07449 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4016ed92-ee38-33b0-bed1-2515a46097da | -6.15324 | -43.19328 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f571cba5-d076-32a5-82b4-67794bf18893 | -8.08624 | -45.31905 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89c9fad8-ad69-3f74-b201-4ff22333af2d | -9.0075 | -49.80333 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebff81f9-a57a-3c67-b9e9-261327c71862 | -11.64196 | -54.54053 | 2025-09-06 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 284eff12-6dd6-3bfa-adf2-ef004d9a571f | -7.60238 | -43.87014 | 2025-09-06 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fddeaee-6a5a-3824-bb21-7442904290a6 | -16.30118 | -45.69081 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54730dcd-8086-383d-89db-9e191d980d88 | -8.90915 | -45.78081 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cff722e2-8365-34f4-a725-b74f58a8e64c | -8.08967 | -45.31963 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bd033a6-c13f-3de8-ad67-1e7f53c02f79 | -15.54532 | -48.39406 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac2d781-741d-35a5-99ee-2df143d18564 | -13.73629 | -46.91242 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46a53818-51b0-363f-aa72-8c6a4fd1dbb2 | -6.165 | -53.68373 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d79f4cd-c302-31e9-be1b-1ef3561d436e | -6.39939 | -46.09224 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32488599-484b-38f6-96e2-315ad4113a47 | -7.58532 | -49.28482 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3629071c-a759-3f43-8aa8-054c32f0cc59 | -12.50989 | -53.85245 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c6033f2-86f1-312e-8a58-0951575c2d42 | -2.78889 | -49.62233 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 84e3fb26-2c59-3e94-8ff6-d108cf21a394 | -12.18869 | -53.89755 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f235768e-3305-3d9c-981f-519c5ddaec23 | -5.95413 | -44.74678 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5865467f-904f-37d7-823c-d8851c783308 | -7.16007 | -43.88582 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 864144c9-c7c7-3cd6-874d-e36568a0c4df | -7.5901 | -46.20824 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50be4a8a-516d-338e-9146-b897da4c2d06 | -9.0773 | -47.02949 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 694b38d0-799c-3e2f-9e34-dfc0a02518cd | -6.3979 | -46.09775 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 771ae35b-eaba-36d7-af5c-5ba60ec97df4 | -5.82919 | -46.35728 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f76838b-d3ab-3fe4-becd-67efc52b0315 | -6.1579 | -44.24146 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88e2054a-7d54-3762-be84-a47aa81ba21e | -6.39857 | -46.09357 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e853a45-fb72-3a00-8ca2-73a142add78c | -7.68489 | -44.97063 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44efee8a-ecb6-3a70-9897-08c70d6f4446 | -13.56638 | -48.12188 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4326e1b8-c50f-373c-a899-cc46bf846855 | -9.67839 | -51.08642 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5413d9e7-d6db-3eab-a4f2-0ee84a257fbb | -7.33618 | -43.94587 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25d81d37-1289-3945-bcf2-1869e0f3ee5f | -15.36131 | -46.41039 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3e4a549-7549-3f0e-b53f-b89382125b09 | -6.16377 | -43.19138 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4755e7e3-e1ce-3fdf-8f2e-33ccf11c9e93 | -6.25642 | -42.42991 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cdb83439-1829-32fc-ac6e-9610a9901fa1 | -13.2888 | -46.81475 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 922638b8-e0fe-311b-84d5-bbc8e718931e | -5.95066 | -53.79133 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4315807-8682-3237-b82b-f5b9cdbd78f0 | -10.60117 | -44.32635 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 84359864-77cc-39d9-8769-35d04f2f957a | -5.86778 | -46.10179 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e39f1cfd-2ce9-370b-a8bb-f8d169059e54 | -4.80226 | -47.25874 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66b2ddcc-20e8-3a14-8944-0839c154deec | -14.45235 | -46.43235 | 2025-09-06 04:17:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc32aeed-6e29-3a34-9fa3-99eb854a0bca | -13.47705 | -46.83776 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9303ff-d3ea-305d-89c9-c90db18a67d9 | -13.87728 | -48.02847 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0ca1f6a-ad87-3d1e-b52a-9bdba99a6640 | -7.02288 | -43.23465 | 2025-09-06 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 99e25bf9-2a22-3a31-8bbf-20e208682af4 | -6.55609 | -42.95753 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d816509c-c882-3aae-8bc9-6f234495f148 | -14.57213 | -48.00841 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 113ab7bc-ca09-3fc1-bf88-d100be330eb1 | -7.38224 | -48.17995 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22db2564-e7a1-36d3-b094-08a91cfd821a | -15.84221 | -52.29112 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 312cf9b7-a656-3a6d-929e-895cede08940 | -5.8687 | -46.02892 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04129f08-cbf9-3df6-bcf4-dfbdbd69b8c4 | -12.51123 | -53.84563 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc943fe1-f970-32e9-836a-701dfdf1eacc | -7.29318 | -46.03753 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6deebe7-ee4a-3e27-875a-47710be0a998 | -6.22242 | -43.56776 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8714625a-a6d7-3f87-97b9-556c794e3129 | -11.63552 | -54.54327 | 2025-09-06 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a837e0c-4b55-3e1a-903b-1c3263feba8a | -10.61115 | -44.32798 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 78e72add-1aea-301d-88dd-b1a1de4c5aa6 | -13.55094 | -48.12386 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| caddbb44-e6f9-3078-a207-d1c5887ba7b8 | -6.271 | -53.44963 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c89404b-08d6-30a2-bd3f-694f7b483d52 | -14.57055 | -49.12901 | 2025-09-06 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f33d1632-7308-3019-95f3-17d7567d8a08 | -14.57274 | -48.09159 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34bef87b-66a3-3627-b743-36ac0ab43a25 | -5.73082 | -43.91476 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff31cb50-e16c-398c-89fd-22887712d68d | -8.86606 | -47.24533 | 2025-09-06 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f6da9ca-ddad-3012-bfc8-b6cfdb66995e | -6.07027 | -43.43666 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5266ceb3-1d42-353b-bbe6-af219444f22c | -5.67717 | -45.1708 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71bf6b64-77a0-326a-bc52-f48788b6d3a2 | -6.18117 | -53.25472 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5826a31-b959-367d-9420-9244591e6ed1 | -10.59728 | -44.32933 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 86d2ac04-84c7-3dc6-bec2-400c3963828d | -16.3106 | -45.69613 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9364f7f9-f821-32dd-ab72-5775b6a48f8d | -5.73177 | -45.36945 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a444ed5e-f942-312d-99ba-40f77029df00 | -10.0322 | -48.1291 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 444c849b-08d9-3091-8a41-297191aaedec | -5.7324 | -45.36553 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0920b0d2-53db-344c-8c33-366ef22b40a3 | -3.75338 | -49.06319 | 2025-09-06 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e5ccf1c-4acd-3feb-90a9-925d7756dcfc | -5.83908 | -44.11052 | 2025-09-06 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaa0a3eb-a79d-3f71-92fc-1e169ef0b888 | -7.73127 | -50.31788 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1302cf87-e533-3f80-86a3-79fa5281b3bb | -13.88819 | -48.03027 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7aa9359-a165-334f-8e44-05dc9ea00624 | -6.887 | -45.54486 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 727e701c-564a-33e3-9e0c-0215b4019fb0 | -3.16547 | -48.60618 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3bac355-5616-34fb-b736-1815281188bf | -3.1598 | -49.48067 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README37.md)
