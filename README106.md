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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e82e3284-fd0a-3b6b-9ab1-e3487b4848c6 | -3.45891 | -59.46362 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a441f64-466f-38f8-b780-9e2bd810d4e0 | -3.21591 | -58.93901 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13c922a6-9282-3fda-9a1b-83212929a26b | -3.21257 | -58.9385 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01d8e701-ffba-3c17-8da3-b35c0605831f | -3.1829 | -58.96202 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1976469-fc6f-3f09-ab72-6658b0647634 | -3.14782 | -59.14177 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97f298c8-8eea-3c24-a4a2-e6fcca03ac87 | -3.09644 | -59.38198 | 2024-10-12 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b0449df-d166-3104-91f9-2f5420c5fa9f | -3.09311 | -59.38146 | 2024-10-12 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ec5fa0e-05a5-32df-9a47-d349abf76dfd | -3.05209 | -59.36093 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a3d9922-5e58-3809-b813-26261eebc733 | -3.04931 | -59.35695 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3185af37-6e4a-3a06-b1d8-bc0ed1fb77cd | -3.04877 | -59.36041 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb32b6cf-a954-3d90-83fa-374288cd3d7f | -3.01859 | -59.10044 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f8a77c-7fc3-32fd-9c90-c328261e24af | -2.96441 | -59.31543 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abc376df-012f-3b7d-bf4f-3763e6ef1049 | -2.93982 | -58.93548 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebf1f76d-4fe2-379e-9c34-ae6ca2cbbaf5 | -2.87624 | -59.18864 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eaeb3b0-8378-3820-a4c0-ad885ff25b95 | -2.66505 | -59.39259 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eddd1ef0-cae9-3386-bb73-ad6b4ac79e16 | -2.5882 | -59.40537 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25b48d70-bfa8-3a03-9088-aa4f52f7d69a | -3.28546 | -59.79021 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a31ef59-53c9-340e-80d7-bd5b9627b8f0 | -3.28282 | -59.78988 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb2dbdd1-cf88-37ee-9201-36b314285046 | -3.54089 | -59.48346 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e791524-d5c6-335f-846b-7ab946de94cb | -3.52543 | -59.49521 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d408df5e-db1d-314c-ac38-a6c0e99bfa19 | -3.49307 | -59.59278 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acc16a87-a4ca-386f-afd5-717608d1997d | -3.47674 | -59.50179 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1172175b-548f-3a00-b83b-acc3de492f09 | -3.44556 | -59.61368 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0115a065-fdd1-3fa9-99a3-50e624c083b1 | -3.44502 | -59.61713 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c12ed606-0be4-380e-b54d-1657ab6ccb21 | -3.44447 | -59.62058 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6693f9c5-df66-35ac-abe0-320ee5b39601 | -3.44393 | -59.62403 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a19714d5-db2d-30c7-a80c-a9503372f842 | -3.44224 | -59.61316 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77dafa33-dc15-31dd-b186-b1b1d513c606 | -3.4417 | -59.61661 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef9173d4-230c-3964-95ed-a0088aeeb35b | -3.44115 | -59.62006 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a283ce6-292e-3bcb-af8d-f9a24dadee66 | -3.44061 | -59.62352 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81111483-cf1d-3ff5-9248-67ba9b30726f | -3.43892 | -59.61264 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f8ddc0c-cc58-3480-9b05-1babba833f07 | -3.43837 | -59.6161 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87717fad-1d9c-3817-b304-b90d9fe9d279 | -3.43798 | -59.85645 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9809063a-1c54-3d2b-b147-f8ff26953572 | -3.26511 | -59.59979 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1abed4-4b78-36d6-9630-ef86aeef9816 | -3.26179 | -59.59927 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc966edd-e624-3891-b909-406df49ddae2 | -2.86469 | -59.56532 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09295563-b207-3f57-87e5-ecdb5fa1aff0 | -2.86191 | -59.56136 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b4bc81c-2ded-3c24-9dcd-ffc24aeee876 | -2.85913 | -59.55739 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a600a253-8ead-3302-8c26-b4281dddaf6a | -2.85859 | -59.56084 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dfff2f2-d129-3bea-8a8f-d3f420b6f18f | -2.77381 | -59.58298 | 2024-10-12 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b45f572f-ecb7-3f2d-a7d5-0e211612e639 | -4.11849 | -58.74641 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f5381cb-afc2-39f2-a0ed-5092ded75080 | -4.11568 | -58.74234 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349c693f-8a3f-30de-87fc-adf5610c2a32 | -3.98877 | -59.01894 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906fd62e-3090-3023-bcf4-d4f96605a49e | -3.96461 | -58.89671 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97966518-c6ca-3717-a757-b744c5fc0c56 | -3.96405 | -58.90023 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c6ba2d-d0fd-3899-a313-7235fd7a3e6f | -3.95048 | -58.50209 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 377f5bef-4d76-3ce3-bb36-0b9140bf0bd5 | -3.93179 | -59.12114 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb1c0fe2-165e-36de-a770-f4a67a1313f9 | -3.92937 | -59.12085 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e3275ec-0f5c-31d5-979b-340c38760319 | -3.90586 | -58.63409 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85f28bdd-7a59-3bf1-bf97-bc410c3c7062 | -3.88028 | -59.06317 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9ad6d65-7cef-3f31-8403-fdd736dcf9a1 | -3.86843 | -59.0076 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02067aa0-7ebe-37a4-b321-dc7d6cd54200 | -3.7729 | -59.36387 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67dca637-ea37-38de-8de9-1ed972eb5f28 | -3.72789 | -58.47521 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96543b20-e1da-301f-8d95-7308f2f7568f | -3.72507 | -58.47111 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cd8a805-7356-3779-84a1-f48008dbd34b | -3.72452 | -58.47469 | 2024-10-12 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b7668f2-488a-3538-b7d1-1af5ab078a9d | -3.68385 | -58.78101 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1be65ec-0111-3b4a-8d55-33b8e2f4a939 | -3.6833 | -58.78453 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e0f6628-d438-3975-ada0-afbd94975570 | -3.66941 | -58.80764 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bed51242-677d-3b88-b295-000dabadee8d | -3.6319 | -59.09232 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc120396-d787-3204-8a75-4d5405166a43 | -4.26827 | -59.99741 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05b12f81-f7d8-3ac4-a5c6-0b53ff9d58a6 | -4.2655 | -59.99343 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc040ae3-338a-3dec-b7a3-1be8a2000398 | -4.26495 | -59.99689 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abbc281b-f47f-3ca4-8b50-fcc5eea5d6c5 | -4.26441 | -60.00034 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f44f1e2-e2cf-393a-943e-c4a91f929ba1 | -4.26218 | -59.99291 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90a8f333-c493-3366-8267-8a7e35bbb6fc | -4.26109 | -59.99982 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7653fa6-cace-369d-8587-0ea9d0455494 | -4.25886 | -59.9924 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 085ddd1a-ab68-3696-92c1-b0375fd07db1 | -4.25777 | -59.99931 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 847941bf-2394-3eb3-9a3c-e0dd8be1bced | -4.24751 | -59.89153 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 234d9751-76fa-399f-9cc3-483dc136024f | -4.23285 | -59.85736 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89f199e3-420a-3333-ac10-c5fc03311ea4 | -4.23231 | -59.86082 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33da617d-939c-3d9e-96ea-6ce6a973c90f | -4.22736 | -59.87066 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 427c7064-16b1-3c1d-9711-409aa89fefc8 | -4.22095 | -59.95459 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc174824-5dee-36bf-9016-5bbab0fe550b | -4.22041 | -59.95805 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1617326-1c64-38ea-a4c4-1ca1ae709739 | -4.21431 | -59.95356 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9b66cdc-9072-389c-af71-b9e838be7ecc | -4.18998 | -59.95684 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ab14ab-7f74-3599-a8e9-86ab41bf2124 | -4.28989 | -60.0114 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 057a985c-2ce4-335d-a700-dbad37171db0 | -4.28657 | -60.01088 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5abd54ea-4286-3515-b53b-f88d22772ceb | -4.28564 | -59.69212 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e57cb82-527f-3e1b-a9bf-b15e35e43382 | -4.27317 | -59.96632 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6519949b-2c36-331d-8c4e-7c186f74ba67 | -4.26985 | -59.9658 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fdb667a-8f63-3145-aeeb-f042623aa3c8 | -4.26163 | -59.99637 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f0f4fdb-888c-3b8a-ad09-6326d7719979 | -4.25608 | -59.98843 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 351cbae8-8cd4-3a16-92a9-5d230dcff509 | -4.25553 | -59.99188 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e500fd7b-5b3b-3dde-9875-1705fef5296b | -4.23658 | -59.93937 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afdab744-d4d1-3694-bb9b-11282d82dca6 | -4.23563 | -59.86134 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15e302f8-ccda-3891-b2e2-32d3f10e531f | -4.21763 | -59.95407 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c36f91f-f7b4-390e-b3f4-e8061c2aa996 | -4.20725 | -59.99847 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda699c9-5ef0-3db1-b011-9fb25b7744bb | -4.1872 | -59.95286 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2aaf8381-32e8-324e-beca-d7adb26d74a1 | -4.18334 | -59.9558 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c086c62-3fc1-3b57-bcc6-34603079ba4a | -3.90237 | -59.61421 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae7087d-cc16-30e2-a05e-8bbe72f9abc4 | -3.89483 | -59.68384 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fad8d699-831b-3e04-8b33-0e3d4aa715b6 | -3.89429 | -59.68729 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e1153f-09de-3ca9-a89e-a5254aa23b97 | -3.8911 | -59.72925 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb01808a-e57d-34bf-ac98-5e912fa51021 | -3.87286 | -59.73703 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94904826-3119-3aac-ad6f-8b0c419e4815 | -3.86954 | -59.73651 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf75e22-80d0-34d1-a560-cb2e867a5330 | -3.869 | -59.73996 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774a8dbc-7350-359d-8d98-d648781ad027 | -5.57432 | -60.17052 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f4d65e7-c27d-3207-bc10-8e8b57cd9b51 | -5.57377 | -60.17398 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60cf7f28-eb5c-3f1a-babc-96c900db3a4f | -5.57099 | -60.17 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f047c828-1a0c-380e-836f-94782a5f1600 | -5.57045 | -60.17345 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README107.md)
