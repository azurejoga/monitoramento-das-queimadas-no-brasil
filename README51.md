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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 394389cf-ce53-349f-97c4-6b0683c186be | -4.88818 | -45.75276 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd4fe5cb-c630-32e6-b0a4-01496d9a4008 | -4.88265 | -45.76475 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7170e00-8445-3130-b196-7426534cb998 | -4.879 | -45.76428 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd30efe6-6881-3c5a-9957-01f8eab029d4 | -4.87836 | -45.76856 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c837baaa-60ce-3fba-9f0d-8d8aafef5d4d | -4.87471 | -45.76815 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d27c87f2-97c1-3d9d-8e5b-082135f062c1 | -4.86728 | -45.04186 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2cf414ad-7d6f-3848-9c5a-5cada8fe7d3f | -4.86417 | -45.03671 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1df0f01b-5496-3290-a769-23536ee5eab0 | -4.86349 | -45.04132 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 75adc9e6-243c-36ae-b82f-1591f6a56411 | -4.86338 | -45.74454 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 039ef590-ad36-3d7e-b69d-f5f1f7ef72a4 | -4.85975 | -45.74396 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2cc6f16d-1ef4-397d-86a7-66317ed1f148 | -4.85971 | -45.04073 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f9909a7-2c98-37ce-b14a-4b1c612b7e50 | -4.85701 | -45.78706 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfd56d70-a8b1-3268-aa33-26782d97e10c | -4.85417 | -45.85532 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bc5df5d-3eed-309d-be8b-8ca2d88d7605 | -4.85215 | -45.03951 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca9fa6ea-eaba-3bd0-85d7-57d73450119e | -4.85055 | -45.85481 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60a9d1d1-75fc-3189-aa3c-4d03694b66fd | -4.84992 | -45.85896 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98b95bb0-b755-38df-bff6-9bbc85aad643 | -4.84905 | -45.03427 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d956231a-2283-34dd-8f1d-e6e9373b5781 | -4.84837 | -45.03893 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c001e6ea-b356-3105-bbad-bf642095d7d3 | -4.84306 | -45.67791 | 2024-10-13 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bb21928-cbcd-3350-a1af-6475fc072652 | -4.837 | -45.79685 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1da1817-590d-3577-b23e-678a3d2e6d5e | -4.83557 | -45.79864 | 2024-10-13 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83cbb321-c1f6-326c-815a-ca6d169a345e | -4.83258 | -45.40133 | 2024-10-13 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31e5a678-52ae-3a06-af53-848883fd46cb | -4.83191 | -45.40573 | 2024-10-13 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b110924-b469-3d80-8854-7260493ce2e3 | -4.8248 | -45.67533 | 2024-10-13 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de71442-1776-3def-834d-64d51caf940d | -4.59209 | -45.62986 | 2024-10-13 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd6627aa-9e7a-3d60-98a3-c028b05a1058 | -4.38329 | -45.69626 | 2024-10-13 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d600c5-0bb4-35eb-b905-291dd0cd4cee | -4.34847 | -45.58275 | 2024-10-13 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56052d40-dca5-3607-abe1-4026afd4628b | -4.34782 | -45.58707 | 2024-10-13 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88f52bfe-38c2-3fcd-907e-6e8e6c98f7d2 | -4.30592 | -45.36968 | 2024-10-13 04:38:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d0e6da8-0659-3e45-9e09-85a6fc7c678d | -5.05053 | -44.85556 | 2024-10-13 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40ff81ad-d657-3755-a319-de2a841ca875 | -5.04669 | -44.855 | 2024-10-13 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aced3a64-da40-3736-bbe0-b55129ca5f91 | -5.04598 | -44.85971 | 2024-10-13 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4af20526-c8d6-31af-b62e-109a4486b041 | -4.16044 | -45.77992 | 2024-10-13 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de0fbf47-7b08-304c-a0ba-76a8d8d80148 | -4.15685 | -45.77933 | 2024-10-13 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ac66e3c-9531-3b8c-8cda-7e25bd2261ce | -4.07981 | -45.55037 | 2024-10-13 04:38:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 834abc3e-4ba4-38db-ad44-5fa7fd0b08d4 | -3.73478 | -44.66275 | 2024-10-13 04:38:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2a4901c-0adf-37ed-817a-f77da1c173f2 | -3.73408 | -44.66744 | 2024-10-13 04:38:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba429bd-12c3-3f91-937f-67e137ac9212 | -2.23917 | -45.87871 | 2024-10-13 04:38:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1a0994b-d254-385e-b387-8398bd0f8d1e | -2.05659 | -46.53838 | 2024-10-13 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2defb7eb-aa78-3011-aec5-7e1f9742cd34 | -2.0492 | -46.541 | 2024-10-13 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe01a7a0-3e13-3329-beb8-777b7e009d6c | -2.74798 | -46.74474 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 564d4e35-38ef-3d75-9bc8-7fac191d1154 | -2.61178 | -47.34284 | 2024-10-13 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| edcaf64b-384b-3eac-9ad9-b0b3b4837da6 | -2.53112 | -47.27259 | 2024-10-13 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8443d02-69a7-3fcd-a83e-88aac08b9bf4 | -2.53057 | -47.27613 | 2024-10-13 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8e93b3d-65c2-3cf7-98a1-64d8e9d4d225 | -2.52889 | -47.26497 | 2024-10-13 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ac0bc3a-5e1c-3477-bc78-1d5ab71c4d3c | -2.52833 | -47.26852 | 2024-10-13 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c739a9a4-c5cb-3b3c-8ddb-9575d9172012 | -2.52777 | -47.27207 | 2024-10-13 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b1c5bd1-2891-3061-a693-925d8cd5fb75 | -2.31369 | -46.55483 | 2024-10-13 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aa2a9ad-8204-3c8b-a692-54e95ce6e2b4 | -3.6118 | -47.51506 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75d26c1f-13ed-3155-99f2-e048ef8c3679 | -2.27659 | -45.98419 | 2024-10-13 04:38:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31a52e1b-5423-3ce8-ad78-88de8240201a | -2.24754 | -46.73262 | 2024-10-13 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65f40f95-e5a3-3ad7-9cb5-a68050451c1e | -2.24697 | -46.73628 | 2024-10-13 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47a484d1-bea6-388f-8686-6043ca54c485 | -2.24414 | -46.73209 | 2024-10-13 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5877dca1-35e6-3614-8dd1-cdafbdaa2a7c | -2.24357 | -46.73575 | 2024-10-13 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 635e162c-aa01-377e-87af-d6428919ce1a | -2.24301 | -46.7394 | 2024-10-13 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77ab3c0c-3224-3bea-9849-fc20029828c3 | -3.35353 | -47.31903 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5690412a-7b4e-3356-ad65-67b17ab1f312 | -3.35128 | -47.31139 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d5d9399-2450-34ca-b6c5-cd5b95512d89 | -3.35072 | -47.31496 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| da8084cf-7176-3dab-a2f2-bdeabeea2b26 | -3.35017 | -47.31854 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ee50366c-b780-325e-87a5-9ff5342d3553 | -3.34736 | -47.31447 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de63f08d-52e0-33d7-b854-589b430a1a97 | -3.3468 | -47.31805 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 528526b3-704d-3b96-9247-b8b19b658d44 | -3.34625 | -47.32163 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2fcb334c-00d6-3247-8778-d05614fe2ca8 | -3.06952 | -45.94641 | 2024-10-13 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ec817ba-c084-37e3-b0b9-725a1796bf6d | -3.05769 | -45.94992 | 2024-10-13 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb90a994-eb7c-3a56-b6fb-907266734903 | -2.96099 | -47.3681 | 2024-10-13 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9e2c1bd-538f-3e01-8ea2-71f38b630001 | -4.69016 | -46.75124 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ac65a41-a9ff-3e5b-9a55-cc1b949d477f | -4.68959 | -46.75503 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd58c5dd-a811-356d-978f-7735518639a5 | -4.68754 | -46.75182 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb825f5c-89ba-37fe-82ed-504efd60af4e | -4.65909 | -46.79824 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ebb0a1c-a5de-31e5-867f-7dea4b60da57 | -4.53719 | -46.56094 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| da7210d4-d441-3f1d-a8d0-a4ccde76cff9 | -4.53489 | -46.55263 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e2a7bd5-d1ce-343a-84f0-43744825ba25 | -4.5343 | -46.55651 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6f17c230-e147-3c32-9567-a5afd9e0b71c | -4.53371 | -46.56038 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 29bffdca-40c1-32ac-8e73-7a27d7bd432d | -4.53141 | -46.55208 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3bafafd-d507-377f-8942-d8056d289920 | -4.53082 | -46.55595 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 40611f10-ac71-3bf9-a1b2-0e45de75b66e | -4.52608 | -46.61048 | 2024-10-13 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 513d20ac-a9a8-389d-bc41-7a86acff5f80 | -4.35746 | -46.75315 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9f6c6d1-bc8a-3e09-9711-ce1a77ba30d5 | -4.33276 | -46.73014 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23b6b47-5b10-3e94-950a-d8e742901819 | -4.33218 | -46.73392 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff6b319-be03-3903-8bb6-81806a0d7e83 | -4.60871 | -47.33282 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33272e9c-32f8-32fe-8a34-8a09b06857d0 | -4.34951 | -47.27888 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06c3a834-8fe9-3b79-804a-376131b45ca4 | -4.3247 | -47.30481 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3769ca27-93df-3a70-9b33-e63db067f2e7 | -4.32076 | -47.30791 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 072cbfe8-fe61-340f-b6da-a2518bb44a50 | -4.3202 | -47.31156 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0399eb41-5910-3712-a165-9d775ecc44c1 | -4.28805 | -47.29531 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6027562e-2652-30ff-9e79-b3c91bcfba44 | -4.2875 | -47.29896 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| efb104a9-4593-324a-874e-65345f34b312 | -4.28694 | -47.30261 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 25b0ec89-2a87-34b7-a920-69ad755170c3 | -4.28467 | -47.29478 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99e5c792-4d74-3857-987b-9d5eaf349443 | -4.28411 | -47.29843 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e78eed7b-798f-3c0e-a1d9-98a3095d2a7e | -4.28129 | -47.29426 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82dd8e5b-c307-3824-9cd5-73b4d17c5b7a | -4.14546 | -46.69442 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd1ca0bc-359d-3f0a-95d1-25751512b9f0 | -4.07707 | -47.25255 | 2024-10-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae07fe72-e799-3290-aebd-a18d41666ffb | -4.0515 | -47.6196 | 2024-10-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87b1fd77-72a9-3f6a-b356-08321b415a78 | -3.9428 | -46.43867 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a9f562-d28e-3197-ad23-78a1ccc088ba | -3.9422 | -46.44253 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3e04ee7-ec1d-3e2c-86aa-f6370ca63889 | -3.93992 | -46.43428 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa0cfabe-107f-3f86-a99c-e2c954a1fbc3 | -3.93932 | -46.43813 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 507feb59-f20c-3fa2-bea7-790684975a6e | -3.93872 | -46.44199 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea11845-fa23-3b8a-ad6a-5253344065e8 | -3.93703 | -46.42988 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 152ff761-ff71-323c-8183-96e82acf83ba | -3.93644 | -46.43373 | 2024-10-13 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README52.md)
