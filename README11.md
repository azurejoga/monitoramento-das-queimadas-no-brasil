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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eb83df8-bcae-3b44-879e-fa31c531fdfc | -3.24777 | -47.24869 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbe63432-a50f-3a90-a11a-5eb70f598d38 | -4.36487 | -47.77272 | 2026-09-04 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 700b0781-4cf4-316a-aff9-72e774daba23 | -3.44713 | -39.63988 | 2026-09-04 04:17:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e89322a-9178-3791-972c-9f1728651c97 | -2.98578 | -49.27236 | 2026-09-04 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f08e044-d8df-3266-9ac6-4ecf0055540f | -4.90255 | -43.47145 | 2026-09-04 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| be447092-f978-3df7-a6c0-9ff4f8668d90 | -1.39149 | -47.576 | 2026-09-04 04:17:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f7c16c5-0dca-3ac9-8db4-0420b03dbc61 | -2.26425 | -47.00714 | 2026-09-04 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bcf1163-887c-355d-9b42-c9adab365765 | -4.8193 | -42.68055 | 2026-09-04 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1315ac8e-2945-3847-87ce-420b78cf322c | -2.75815 | -49.4728 | 2026-09-04 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c50efcc-48b6-3f8b-bcd2-ac3dcb5baee2 | -3.89706 | -52.04505 | 2026-09-04 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ce98ace-a0c9-3590-90cc-07b3c0bad9c4 | -2.76282 | -49.47681 | 2026-09-04 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb9f4b69-2daf-3a0f-9f0a-09dd3695446c | -5.3848 | -42.85875 | 2026-09-04 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7beecbca-8eaf-3066-b0d4-ffd58cacaed3 | -3.42985 | -43.20514 | 2026-09-04 04:17:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e16b3704-0cfa-375f-a453-c3c18929f862 | -2.98386 | -49.27162 | 2026-09-04 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c5588e-869a-37ec-bc75-e28ac50a5956 | -2.98898 | -49.27248 | 2026-09-04 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae058a2a-ded2-3aea-bbfe-f1155b09529a | -3.24262 | -47.2523 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9af4be3b-1bc3-37f0-bb65-0685a3324c10 | -3.89629 | -52.04959 | 2026-09-04 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8ca4c5f0-48b5-37ae-a331-ecf134d30e06 | -4.34617 | -44.33868 | 2026-09-04 04:17:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3835603c-cecc-3bf5-ac72-0315cd797097 | -6.20942 | -38.24388 | 2026-09-04 04:17:00 | NPP-375D | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c279e725-efb8-3d9e-a5c5-187639ed56db | -4.91524 | -40.6678 | 2026-09-04 04:17:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4588120a-fe54-3ac8-b5de-572811dd02be | -5.29933 | -43.06611 | 2026-09-04 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c37e6988-0c81-3363-8463-385be1694ade | -1.249 | -54.53012 | 2026-09-04 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 745821c5-0aa4-3aeb-ab48-a072163fd64d | -3.73134 | -44.6608 | 2026-09-04 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21de2b89-5221-30f8-affb-d3cd05b670b4 | -6.21307 | -38.24443 | 2026-09-04 04:17:00 | NPP-375D | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fb3b708-a4ae-343a-84a7-c208d15c14e9 | -4.24782 | -46.63525 | 2026-09-04 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d75ac68-5d61-31c8-8211-c19c1723b6cc | -4.36864 | -47.77795 | 2026-09-04 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| de813851-14d3-3783-a426-e8edcc97dd6f | -3.90233 | -52.0507 | 2026-09-04 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d486d537-98db-347e-a726-ad89b6d13dd5 | -4.36412 | -47.77721 | 2026-09-04 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 339a15de-2dc6-333d-a585-46950923e46d | -2.76229 | -49.47996 | 2026-09-04 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0b641f0-bf62-32ff-aa01-a8cd50a67e6d | -3.72034 | -38.6693 | 2026-09-04 04:17:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2d9be24-ef59-3d3a-b801-92b6aeb672e2 | -5.10377 | -40.60837 | 2026-09-04 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5718a9bf-c3a8-3c05-9b06-564833af1598 | -2.94218 | -48.74039 | 2026-09-04 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c057a3b9-fe05-3a59-a3c7-94ee84dce6d4 | -4.90603 | -43.472 | 2026-09-04 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c9a2b8-b320-3576-9f3c-b52cbdd13dd7 | -4.497 | -42.55592 | 2026-09-04 04:17:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc438bbe-5efb-30bc-bd79-d3cb968a055d | -4.03232 | -38.2336 | 2026-09-04 04:17:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 135b4a42-eebd-351c-863b-eb26a25d6640 | -2.98628 | -49.26938 | 2026-09-04 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2f765ef-7c11-3b03-852d-9454409d886a | -4.2961 | -38.53121 | 2026-09-04 04:17:00 | NPP-375D | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f02d4cd-9877-3c83-8b2f-cc1d912223c0 | -3.89789 | -52.04727 | 2026-09-04 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a37e9148-527a-30fa-8493-4d7837203d2e | -3.59604 | -43.00869 | 2026-09-04 04:17:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3fda92d0-8bf2-34ed-9a09-df298d41339e | -5.11044 | -40.6094 | 2026-09-04 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7fd4982f-fd1f-3ed6-aa0a-2e38f1962e17 | -4.50039 | -42.55646 | 2026-09-04 04:17:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60c5bb68-4797-39fd-bdb7-f0caa30ab3d0 | -3.77388 | -47.54804 | 2026-09-04 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97997446-0e5b-34f2-9535-cf535fe91e08 | -3.67678 | -53.75594 | 2026-09-04 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8f9e13d0-8ec8-399d-ac5e-784ccc84f560 | -5.2108 | -38.02956 | 2026-09-04 04:17:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91e6f7f8-d8e5-3809-8493-2890b31ba1dc | -3.71902 | -38.66989 | 2026-09-04 04:17:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa9b9bac-50bc-3d7a-957a-414534402e5e | -1.71731 | -47.08915 | 2026-09-04 04:17:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d4fdcc2-4f45-3682-88c9-7cd6520f675c | -5.38082 | -42.86184 | 2026-09-04 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e76c0ea0-213c-3340-a98e-3e1591fb63fc | -3.43045 | -43.20132 | 2026-09-04 04:17:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b80d0534-ba37-3fa8-abf6-a753019a0302 | -3.93825 | -42.98936 | 2026-09-04 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3369a883-bf43-33b2-bf61-0d6ad26df69f | -4.55444 | -47.76296 | 2026-09-04 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a38d628-70e3-377e-97e2-31afaade5276 | -5.29896 | -43.06541 | 2026-09-04 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b09383e4-737f-3677-807c-04805c766234 | -4.91579 | -40.66432 | 2026-09-04 04:17:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ad7b6da-6eaf-368d-842b-88fe11f2ad49 | -4.56512 | -41.95634 | 2026-09-04 04:17:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94172b81-9798-306d-a5da-e284f77c94fc | -3.24334 | -47.24796 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55998fc5-f3b9-39be-ac6b-cf6e6b169112 | -2.32709 | -47.19941 | 2026-09-04 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2655fd61-be52-3527-b268-26629da15997 | -3.33674 | -39.77189 | 2026-09-04 04:17:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec5a8021-62c6-353c-92e3-4048f0f69d5f | -3.77316 | -47.55243 | 2026-09-04 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 07d3fd1f-b2f0-35e5-9d0c-e98a94a32b6e | -5.1071 | -40.60889 | 2026-09-04 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 749a7814-fb31-3825-88d6-c654c7669b32 | -4.49362 | -42.55539 | 2026-09-04 04:17:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c6b4c645-e7c9-3f5d-867d-817fd51ffbcf | -4.36866 | -39.55285 | 2026-09-04 04:17:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d2513cb-2554-3bf4-acb4-437092f5fa66 | -6.94126 | -45.19403 | 2026-09-04 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59b3ad48-b25f-382d-b3fc-e094eae928dd | -10.64416 | -50.39354 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 06d548f0-3b56-31bd-b9d6-7b3bb20309c7 | -5.80504 | -43.63138 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 881f9467-5322-306d-9b2d-d8fd11b66ab0 | -11.59365 | -50.48232 | 2026-09-04 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d209209-60fa-3df3-ac17-fd6c7bcc7dfc | -10.65453 | -50.40825 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c9df27e-82d5-3792-9506-3baa7b40d538 | -10.649 | -50.39447 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| de947bd6-5413-3166-a1f2-ce75db25676e | -9.01538 | -41.00048 | 2026-09-04 04:19:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bb6c54cc-6a53-331a-b156-7d1d99f1035c | -9.5772 | -40.34189 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 2db5d2dc-bd7d-3ff0-9d5c-a8c94e6a8e69 | -11.595 | -50.48159 | 2026-09-04 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 099d51cb-e022-3624-b859-2c56348fba92 | -8.11344 | -54.7825 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4443aae4-e9af-3179-a4e4-0e5a3a1f63ba | -8.50543 | -54.6602 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 166809de-3252-305c-9288-f16cb7835b8a | -6.94196 | -45.18983 | 2026-09-04 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28956a8a-bbc9-3338-9475-03e4649cab5d | -7.25072 | -42.77073 | 2026-09-04 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a879b2b2-24f8-3d71-8bca-891088967489 | -6.77756 | -41.17485 | 2026-09-04 04:19:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf3c80fc-2da9-36dd-bb2c-111c2d803703 | -10.5011 | -51.33408 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d17ffe2-2272-3f83-96ee-a40907366ebd | -5.55175 | -43.42888 | 2026-09-04 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af2db0e8-bfe1-352a-bec2-887deb3f6d76 | -9.15217 | -49.98637 | 2026-09-04 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2809619d-8959-37fb-8028-f82c800058e3 | -7.24737 | -42.77019 | 2026-09-04 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 93e7679d-c76b-371c-a4ce-fa1928eca2d4 | -10.64868 | -50.41272 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c39776a8-27bf-3638-845c-14779eed1e7f | -10.64514 | -50.38813 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 3cb209af-ecc6-3987-99b9-4dae1ee6d6ff | -6.09696 | -44.14568 | 2026-09-04 04:19:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20e2b066-a4cf-3aa7-bc4f-9f1ec97b2c46 | -9.58007 | -40.34619 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 3eb427df-57ba-3b7d-8289-e2d271089d18 | -6.51457 | -45.87636 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5807af04-7e41-3a48-94ed-0d74ad0e9111 | -10.63719 | -50.3938 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3171d38f-45fe-3c07-92ee-580fb242f919 | -8.44242 | -54.68293 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81f26563-6de9-3c96-978e-7878a61762e3 | -9.15313 | -49.98103 | 2026-09-04 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2daa68b1-614d-3bfc-923a-5152486cc8d1 | -10.64997 | -50.38906 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| d9323bd0-fa2c-3109-96b6-7b633ac3c154 | -8.11118 | -54.79405 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d4df7652-493f-30a0-a954-0fe555aba8ed | -0.92916 | -47.19241 | 2026-09-04 04:19:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b921ce5-8628-3d68-9582-d6eb33f5e28b | -10.50039 | -51.33785 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c107aec-252e-336d-9e8e-2f5b43c5a91b | -9.01594 | -40.99689 | 2026-09-04 04:19:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5d99b637-30bd-374f-afe2-1fe1b3b674f0 | -11.26908 | -45.72046 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b9fa0bc-2e30-3ac8-82d4-9822c3562cde | -10.25561 | -50.04369 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3834f7-8bae-3c59-80c8-11ef9e356360 | -11.27414 | -45.7341 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c36f800-cc3a-33af-99cf-920a6cba5691 | -5.82647 | -47.03951 | 2026-09-04 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16377ec3-a5e1-38ac-a0bd-6738c2e082cc | -10.86532 | -45.33226 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc1eff20-d709-3ca8-a7e4-2f3d4e02acdf | -6.30737 | -46.08829 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f60a3009-ea0d-389b-8aa5-1e9fac7b52ec | -9.57376 | -40.34135 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 7f8b0935-48da-3b94-8977-e2935b7d3483 | -10.26673 | -50.03706 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8ba2ca4d-246e-3571-8b0c-445e9a5d6fc0 | -7.3509 | -45.47268 | 2026-09-04 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
