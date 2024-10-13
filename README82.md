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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0fb8358-00be-3f3e-8859-9d42f24d72ee | -8.05206 | -44.81368 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 918e5da7-2a70-3031-ba7c-c8e77f093997 | -8.05132 | -44.8194 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2f59f8a-3834-30dc-a506-55f2ce0b8c64 | -8.05062 | -44.82467 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 398c3c9f-9c29-39f8-b22d-2d2559c826b3 | -8.04996 | -44.82969 | 2024-10-13 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ff0efcd-0b75-3fcc-b5e3-9baadc5b1d47 | -9.44316 | -45.50717 | 2024-10-13 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| abf99641-429b-3634-a0b1-54ef36f52ce8 | -9.44266 | -45.51108 | 2024-10-13 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8bd98cbb-0f67-3d5b-9fa9-653d6293d70a | -9.44213 | -45.51519 | 2024-10-13 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 69ed2aee-7b34-314f-93de-25fe4fbc52be | -10.9247 | -44.67662 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d312ea9b-f425-3a52-890f-eca47014744b | -11.93207 | -45.78891 | 2024-10-13 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb5391e5-2f8b-3e55-b60a-a1b6d9467d0d | -11.93153 | -45.7935 | 2024-10-13 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39398180-05ee-32ff-be5b-9e32c90e7772 | -10.94592 | -44.6628 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe069cde-5142-3960-a144-93cf9bdd8dd3 | -10.94588 | -44.66608 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a82b600-2acd-3913-9a87-59eba51132be | -10.94527 | -44.66814 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e82f337-fa79-392d-9dbf-2b835640ddb0 | -10.94006 | -44.66002 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d14eb3f2-1ae1-36e0-92c6-4c32fb1005b5 | -10.93948 | -44.66209 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f4f7093-b4d9-3b55-87b2-e5af9f39fe23 | -10.93945 | -44.66534 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5c497b9-7754-37ee-aa1f-643753d554d2 | -10.93884 | -44.6674 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a752716f-5bb1-37d3-9bee-b78a44b37882 | -10.93113 | -44.67731 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c2fdf5d-fe4a-3cfd-a2bc-083c42ac197e | -10.93049 | -44.68262 | 2024-10-13 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd130cea-c43b-3c60-b0c4-e6f16a973ac0 | -7.52263 | -46.59361 | 2024-10-13 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1deb65ef-f606-3e71-a9b2-7ee2946dc71c | -7.51721 | -46.59283 | 2024-10-13 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 331be594-7270-3615-9b8e-7480dbaacd38 | -7.39105 | -45.62367 | 2024-10-13 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3e0d76b-93e8-3904-a700-66c583df5331 | -7.39054 | -45.62755 | 2024-10-13 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46d254fd-b814-332d-b3a9-f2874fe0d7c9 | -7.24703 | -45.38313 | 2024-10-13 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6c8b869-f97c-376a-87a6-f294d9d13040 | -7.24646 | -45.38728 | 2024-10-13 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc33cebf-626e-3149-bb41-98f7ed547a76 | -9.22919 | -46.68232 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 203b483c-91c9-39d3-b1bf-7b05a9d84a9f | -9.22512 | -46.67746 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea4af1af-952f-3251-a57b-55a84514c822 | -9.22465 | -46.68101 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4c2e2a8f-2da0-304f-afd5-0ba4b4661f15 | -9.22456 | -46.67455 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95a0a232-e23f-39ab-b469-5e85bca878c5 | -9.22412 | -46.67809 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 322e3b26-1bd6-3b23-afcd-f0275f6b46ea | -9.22367 | -46.68164 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5fdf680-4ed3-312a-929c-f52ef465305b | -8.70301 | -46.60414 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bd41307-da52-3cb6-85b9-cf8c7ea4867d | -8.70275 | -46.6072 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26e1cfab-1914-3ac3-b6b1-e0f4e6ea61a6 | -8.70249 | -46.60793 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 895aa10e-a2bb-39b5-bbc7-aa3ca4892583 | -8.69866 | -46.59531 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb2e939a-0a56-350d-98d6-344165a88050 | -8.69849 | -46.59606 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e4c8773-a63f-3cd7-881d-94dfec6d6300 | -8.69819 | -46.59895 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab1b1e7c-0572-3e68-bec3-c7e9ea85cfc2 | -8.69701 | -46.60702 | 2024-10-13 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9e07b44-1fce-33b6-b46f-70a8385856d0 | -9.95279 | -47.27231 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 279778d4-62e6-3252-bd3e-cc9ca1f0c6c8 | -9.95236 | -47.27565 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afb1613a-1dd4-3e87-8aff-cc2366af3224 | -9.9483 | -47.26489 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd7d6a9b-a16f-364d-89b9-1bd750c6b973 | -9.94787 | -47.26823 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45eb4b6b-0752-34d5-9e37-63227c5b4d31 | -9.94699 | -47.27501 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec6c5c1f-505c-359b-b576-f43294e7a957 | -9.94654 | -47.27844 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0173f8e-45ec-342e-9ec4-19aeb48ec95c | -9.94293 | -47.26419 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7db060c-2a22-3169-b58f-7c44bd11694a | -9.9425 | -47.26754 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2835ce58-93cf-345d-ab23-6a420077e413 | -9.94162 | -47.27431 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35b07c46-3ff2-39e5-9003-7ba8f956200c | -9.94118 | -47.27774 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9176d40d-81bd-3f6a-a914-3d0f62ffb32a | -9.93582 | -47.27705 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2695c576-36bb-3da1-9ddf-f1c5c419eee0 | -10.17292 | -46.29148 | 2024-10-13 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1c9ab16-7bf0-3d9f-bef9-61d2b252b7d4 | -10.17243 | -46.29536 | 2024-10-13 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b159886-ca52-35d2-b75b-aee0e25abee9 | -9.83769 | -46.992 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4498d84-6ef5-3812-a4c5-dd63e2eae4d1 | -9.73856 | -46.94281 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fb6b039-21ed-3abf-ace2-513c32bd2a39 | -9.73771 | -46.94165 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57def611-236b-3c41-90a5-b57747e1a945 | -9.73724 | -46.94512 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4d69f6-cb8b-31af-98e1-7888ac99864c | -9.73674 | -46.95718 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16dc47a5-f0ca-3441-9686-44c9cf5e0d89 | -9.7363 | -46.96069 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc032cdb-0dda-3e98-a276-de673f045e97 | -9.73627 | -46.95237 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3979dd6-fb1a-3440-8006-0a7829dde05d | -9.73532 | -46.95943 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe9dacf1-7cb4-3564-8956-3a09c0d2c9a4 | -9.73264 | -46.94569 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 831663e2-d485-3558-9b86-62f6dacee5ba | -9.73219 | -46.94923 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35cb0bd4-2bb8-3f8f-920b-a96200bc359e | -9.73176 | -46.94451 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89eeb189-d763-3538-b2c5-a98084d70910 | -9.73174 | -46.95279 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7324347-0d97-351b-9a24-15290fe23f6c | -9.73082 | -46.95155 | 2024-10-13 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 000920b1-62ee-3191-b20e-3254aac3a231 | -12.26405 | -47.15336 | 2024-10-13 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82005c0a-727c-383b-b322-3fac2f494f14 | -12.17844 | -46.73309 | 2024-10-13 05:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5cc5a2e-4bc3-3f6c-9f07-8fca3194b882 | -12.17798 | -46.73708 | 2024-10-13 05:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a76c190-d3aa-31c7-940e-3c94de63a09b | -12.17787 | -46.7313 | 2024-10-13 05:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2ab4a75-08ee-33d0-ab3a-1c099f3515a6 | -12.17738 | -46.73528 | 2024-10-13 05:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 679d0de2-8422-36fe-b667-a487527bba88 | -12.17689 | -46.73927 | 2024-10-13 05:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c1841f5-55d8-3276-aefd-5b28a00c6043 | -12.17164 | -46.73468 | 2024-10-13 05:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 016f5606-0b15-30b7-95fc-4810a58fba1b | -12.15693 | -47.52715 | 2024-10-13 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 557571a2-f03f-3823-8b69-6a9ff7279297 | -12.15648 | -47.53077 | 2024-10-13 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13883617-40da-3eb5-8d3c-259b1c31cce3 | -12.52714 | -46.81768 | 2024-10-13 05:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e5c61ad-fd89-36cc-97cf-31451a0e45fb | -12.52668 | -46.82161 | 2024-10-13 05:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dcec133-eafd-38bf-94e3-697c3bf19852 | -12.52097 | -46.82082 | 2024-10-13 05:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f54e83d-6fa1-347e-9d90-40d6cc644061 | -12.38378 | -47.31748 | 2024-10-13 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3eb100f-3a0f-3075-9f74-37324bc6b883 | -12.38333 | -47.32118 | 2024-10-13 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a46db8e5-714d-3859-92cb-97ec54d71306 | -12.28635 | -47.65253 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965ed54c-9bf0-308e-b4cb-7bd60fc2f138 | -12.28548 | -47.65944 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07f364c3-9bbe-342d-8e00-6ac7054004f0 | -12.28266 | -47.65135 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d29b76fb-40a3-3254-882f-6f7dc5c94a3e | -12.28224 | -47.65484 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72921fc3-eb77-341e-9d70-ab5c3e796719 | -12.28184 | -47.65821 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 862af640-cabb-3274-b5df-b9398d75167e | -12.28144 | -47.66158 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 596ee5dc-bf2c-394f-b45d-2747e59fc274 | -12.28094 | -47.65194 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4035604-cf5f-382b-9977-28e34a70e2ff | -12.28051 | -47.6554 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a39382fe-f7c8-3dcf-93d9-2ea8e44ace94 | -12.28008 | -47.65874 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50abed9c-1e92-3813-a087-49ca567208bb | -12.27966 | -47.66208 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba549a06-7327-3a24-bc96-cc8621ad542d | -12.27598 | -47.64783 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59cf689d-d0be-330b-bb62-dd9163883ed4 | -12.27554 | -47.65131 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4a0fb1a-4f7f-3da9-93bf-c08efc391d46 | -12.27511 | -47.65474 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bff7295-034e-33b4-a225-c3f8bf46fe8c | -12.27468 | -47.65811 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96acfe22-17a3-3e10-be5a-750d7ef3820a | -12.27099 | -47.64381 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f57906c5-c106-3e8b-9c38-cac0a1f7ad16 | -12.27056 | -47.64728 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58dac16c-ab3f-359d-83f4-168c31991113 | -12.27013 | -47.65066 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a49ba27b-7d9b-3607-846b-b9764d8d1dc3 | -12.26971 | -47.65403 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a73290f4-4708-38f5-82bd-ebf2d9c827cd | -12.26559 | -47.64317 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2172fb3b-9bef-34b0-899c-6c7e6f4644d9 | -12.26515 | -47.64664 | 2024-10-13 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 373ac782-3dec-3371-8061-f08cda6bcf01 | -7.02195 | -46.81771 | 2024-10-13 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e27da12-540d-334f-a0a6-8a6bd77027e2 | -7.02149 | -46.82101 | 2024-10-13 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README83.md)
