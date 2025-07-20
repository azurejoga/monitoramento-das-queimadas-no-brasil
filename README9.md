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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da75aa9d-ca35-3c08-9b3b-c68b3697fed0 | -7.70687 | -47.28842 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fcbf1d51-a416-343d-bf89-e50c98e36713 | -9.27127 | -48.22628 | 2025-07-20 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7daf1666-d22e-3c80-b284-a01ce99aee2e | -10.97322 | -45.11079 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7b11da6a-b982-3684-8c96-0f2bafdfb848 | -12.68723 | -44.33084 | 2025-07-20 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 629a133e-e9d4-3c85-b814-d4e00244d582 | -7.63134 | -44.2897 | 2025-07-20 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baa74f53-b798-3f67-8207-c2c8cf5d6f24 | -10.88394 | -47.13427 | 2025-07-20 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03f9c810-4f3b-393d-b42b-087eeebb0d62 | -6.36499 | -45.39062 | 2025-07-20 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f751b85-c83f-3cdc-9207-1e0b53a90589 | -11.46696 | -48.16019 | 2025-07-20 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56cf22d6-9e34-32da-aba3-15272a4f0803 | -7.75058 | -42.15931 | 2025-07-20 04:17:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 34186d43-a32a-35dc-b328-8cbe2b9591df | -7.42341 | -44.27873 | 2025-07-20 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58ba6ee4-1cae-3ee8-8476-96272647d4e3 | -7.15416 | -48.20522 | 2025-07-20 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ae6ddb5-82e7-3da6-ba2d-71b4fbe30377 | -9.63695 | -40.60334 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae5d0cb0-4164-360e-ac6b-f234e6c7613e | -7.70153 | -47.29702 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d74e3b4e-3432-3f6f-bcc6-9e5bd59791fa | -12.3535 | -46.42546 | 2025-07-20 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c1f630d-8162-3980-8dd3-f8b0c68e13d0 | -8.35306 | -46.64683 | 2025-07-20 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94adc0a4-524f-3b30-a614-127f9f76cd0f | -10.67089 | -46.79364 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cf528609-f4b4-3b9e-9255-ac384dd4c4af | -9.32847 | -41.51641 | 2025-07-20 04:17:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e9dd724-09cc-3f5a-ac81-1b356a40ccc1 | -9.47132 | -57.83984 | 2025-07-20 04:17:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bca1e38-de7e-3177-80db-6a35e4d0210f | -10.96767 | -45.10253 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ca1b9967-1281-3a95-b0dc-907a6d9581c7 | -10.69591 | -46.81866 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fdae3537-c685-38f8-a6cd-8d59530fedd5 | -10.97044 | -45.10666 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0389ab13-7a30-3f51-9375-ca1646d2aec7 | -9.39957 | -47.94173 | 2025-07-20 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e0fd49c-58a2-34fc-b2f7-9dee4f73f4c3 | -5.34538 | -45.2682 | 2025-07-20 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 117a05ea-8586-334c-b02c-89671bdd4392 | -10.63205 | -45.23217 | 2025-07-20 04:17:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2445413d-9cb0-33fe-8e15-46510440c22d | -9.29301 | -40.36189 | 2025-07-20 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2455b31-9496-37c0-afb5-c86d8618342a | -11.02051 | -43.15671 | 2025-07-20 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 279bb8cd-6c39-3463-a720-cf08c52d46b3 | -9.77093 | -48.74935 | 2025-07-20 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 791374ce-a9bd-3269-a0e1-89e4353979fb | -11.58227 | -47.2214 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b09341c0-8630-3423-a74d-490af7f42e02 | -8.04437 | -42.1562 | 2025-07-20 04:17:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be48f245-2ad7-3467-a320-e9aac53874c4 | -7.27757 | -50.33298 | 2025-07-20 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db0e75ee-2c52-3655-afc9-42ef13f1a3b1 | -10.64982 | -46.81081 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 1d7b1240-a51e-3c4c-bf6f-2928e3907f8d | -10.65892 | -46.7999 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bb549286-fe87-30d8-8501-b9d49a27c003 | -9.61613 | -49.01926 | 2025-07-20 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d2972a3-61fb-3b0f-bfc7-99f675b85b44 | -10.68388 | -49.67332 | 2025-07-20 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95668c89-d20b-3f53-8bb8-d8ad3f166e9a | -7.6991 | -47.28857 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e59f6abe-37f9-30db-92da-aa69042de9a5 | -8.01109 | -43.68641 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af2cf1a7-9b1a-3164-9bcf-6d50670dd87d | -6.73085 | -44.85117 | 2025-07-20 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75be9305-dc90-3189-a214-b31ae63ab1b6 | -11.0062 | -44.47658 | 2025-07-20 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d32ef973-3477-3235-873e-f9d6e891d764 | -10.54569 | -49.49538 | 2025-07-20 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 490841a8-c2b8-3be4-9dd6-01aa34f608c1 | -6.6342 | -48.0799 | 2025-07-20 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d89fba2a-8962-36a1-a196-dfda87dc5d26 | -12.36385 | -46.42697 | 2025-07-20 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ff0f4ab-fa16-3f66-be0f-581b2ac93f8a | -10.70476 | -46.787 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5e51efb-b51e-3ddd-b201-51fbad86de36 | -11.4632 | -48.15948 | 2025-07-20 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10ad4926-d976-34c1-82ec-4858931a2716 | -10.96652 | -45.1097 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 96149385-bd0c-3662-89d2-63a59859b217 | -10.70012 | -46.8152 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e480f8e-5eec-3b31-a02b-44b4b66eeff7 | -11.83062 | -47.50251 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1262006e-c054-3146-b2e3-0729ad21b477 | -10.97437 | -45.10362 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30e9e104-6fad-3363-be74-af9903dc44fd | -9.59182 | -43.85693 | 2025-07-20 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea8d5eaa-bb11-331c-87ce-c46ab08d93cf | -11.36323 | -48.72992 | 2025-07-20 04:17:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b53188-2ece-330e-8014-84309aea2a05 | -11.82629 | -47.50611 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af583811-f2ef-3212-81a6-1296ed1a1999 | -10.99256 | -45.12878 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89473f84-318b-33ee-94fd-d1c97040c232 | -8.35309 | -46.64349 | 2025-07-20 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6101dfba-7d7d-3ec4-8fb2-4f88fedc5c00 | -10.97102 | -45.10308 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| da83b618-5d44-380e-9b50-8d6f03961462 | -7.47191 | -49.4543 | 2025-07-20 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c13395f-f718-3d8b-8951-4a4411608783 | -10.73201 | -52.51883 | 2025-07-20 04:17:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc5f2ba4-a0e0-3ec6-91da-56628b69eece | -10.68883 | -46.81741 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3212c624-9e9d-317d-a3fe-919cadd89da4 | -9.80771 | -48.55982 | 2025-07-20 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64c3afa2-58ae-3a77-b359-d8baf91ac32a | -6.14529 | -42.92085 | 2025-07-20 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72792a48-f392-3323-acd9-cd371604fbc2 | -9.56146 | -40.65791 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47950fef-a49b-3c13-a632-345c0a7943c5 | -6.86314 | -47.82143 | 2025-07-20 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8c6aadd-65d9-3aa6-b19a-de8e3497362b | -7.27676 | -50.3377 | 2025-07-20 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9de37179-448e-342e-8088-b0308c1c94f6 | -5.34601 | -45.26432 | 2025-07-20 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da50c89-d871-3366-8d7b-37b2bbc4b927 | -11.48794 | -47.32083 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84cd902e-d1af-324d-a27c-2c047d96338d | -8.74222 | -47.73203 | 2025-07-20 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85ff60f9-31c6-3b00-893f-8dc4cb6ad259 | -7.4262 | -44.28277 | 2025-07-20 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9134017-f5bf-3ba7-a874-e24fd6a06fed | -10.66247 | -46.80048 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e058abc6-1a20-3313-83c2-5a4cf099aeba | -9.79897 | -48.56338 | 2025-07-20 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45f4f430-17b7-3280-a26e-4027ddda5915 | -10.6864 | -46.78798 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d88a4545-615b-37a1-962e-82a58a748b3b | -9.62019 | -49.02002 | 2025-07-20 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5642187c-130f-3c0d-a723-4f8e0903d01b | -10.68219 | -46.79142 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2da60e7e-67bb-339f-b92f-f7451a3cd567 | -9.63756 | -40.59912 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ae2aa19-6be7-36ac-a2eb-0fe3d7151567 | -11.83134 | -47.4983 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3c173ba-2bf9-3a8a-a7c4-397735794b8d | -10.6751 | -46.79023 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 32f5636e-34ba-3227-bd05-593d36733123 | -10.67347 | -49.6834 | 2025-07-20 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab7fab20-47b7-3029-814f-c7e1d403c676 | -7.99062 | -43.68673 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99b7e284-5d6a-33af-bb54-764a2de5aa2f | -10.00985 | -48.22218 | 2025-07-20 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da5b4cd4-f502-3f38-b2d8-c227c70e7e81 | -12.35631 | -46.42982 | 2025-07-20 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb023677-c6ce-398a-a447-171579afd86a | -10.32305 | -48.52614 | 2025-07-20 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3063c8e4-cbc8-363f-9706-245a8258df62 | -7.29542 | -39.62703 | 2025-07-20 04:17:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9dc678f4-356a-3a58-b274-56dd018260c5 | -9.11387 | -48.11628 | 2025-07-20 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e0ce7b6-95f7-351a-86d3-958289dd4c47 | -11.48697 | -47.32219 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42842f17-74e1-362b-988b-e15f8c650842 | -12.35287 | -46.42928 | 2025-07-20 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28cf50eb-1a8d-328b-9298-bf7ff79d8fee | -9.63393 | -40.59857 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 71e773fa-bd79-3d09-836b-e49449949da2 | -11.55303 | -47.08957 | 2025-07-20 04:17:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 962c0b24-35a2-372a-8bee-214d32147bca | -6.40526 | -41.71823 | 2025-07-20 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 00f06cae-04a9-3a29-b186-14df1bb1b96c | -5.65117 | -44.35205 | 2025-07-20 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aec13f87-4d7d-38f3-bff9-f0ab675aa912 | -7.9873 | -43.6862 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 423e6ee2-6c5c-3e5e-9250-f79924f6d0de | -7.19304 | -43.01888 | 2025-07-20 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12830ea5-d705-31aa-a12d-42fa39062c1e | -7.70287 | -47.28917 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2df358a5-5edf-34d7-8baf-2d07c8da400e | -10.02994 | -46.56291 | 2025-07-20 04:17:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deef9387-1f44-3a06-b2f7-da230278ff96 | -6.81436 | -43.8062 | 2025-07-20 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d92c297e-068c-3956-a376-2c95d08fc310 | -11.48337 | -47.32156 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 029befb7-8225-332f-a524-4c55e30773c0 | -8.57604 | -45.11116 | 2025-07-20 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d0457d6-dda9-3b5f-98ba-b76ad821d7aa | -7.70609 | -47.29303 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0ceff2c4-d1a1-3123-8af6-1a1ace136e0f | -5.80651 | -43.92663 | 2025-07-20 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76e4890b-2e66-3bcc-a0dd-a7a04622ab34 | -11.62597 | -50.73391 | 2025-07-20 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d9dc312-5d84-337d-b06d-8f5c24128c45 | -11.81401 | -47.51266 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36de62cc-55da-352b-a680-529c31e9fd5f | -11.55946 | -47.09483 | 2025-07-20 04:17:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c004cb36-5653-3b7b-9b14-a5c76fd7a23a | -7.69854 | -47.29178 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69206cc3-42cf-339a-abf1-8c142a5b5c05 | -8.01496 | -43.68346 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
