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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b71e5d7c-4a9a-3a02-8510-ec8173fbf246 | -12.07557 | -44.81127 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dd57f8e-3e0a-3ad9-9512-e78c05fec952 | -5.6947 | -51.7515 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 08082639-cf3f-31aa-9d0c-64de3c56818c | -9.06127 | -47.01217 | 2025-09-21 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31f8dd9e-76bd-3f0c-a61c-2276fb8288fc | -10.23324 | -48.07153 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22513f1f-3a20-3f53-9db4-dfdbebf43dfc | -10.0371 | -46.26664 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e9f770-6b37-3dcb-8153-d7ef37f785f7 | -6.48106 | -45.99072 | 2025-09-21 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a31295f-584f-3659-bca8-9c7d27178179 | -7.42498 | -44.54227 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 870904de-dc2e-36b2-9ff7-3c40f72d26dc | -11.29782 | -47.40951 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ecf01e3e-278b-355c-af0b-7f5a5c52bcf7 | -9.01719 | -44.96355 | 2025-09-21 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7ddac87-673a-3a45-880b-c4e3f1a63e09 | -7.18109 | -42.24302 | 2025-09-21 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2093c50-5318-3acc-a751-72d0b63e55d4 | -8.60447 | -45.33691 | 2025-09-21 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41e5884b-a0d7-3e50-9ae8-e6fa544d9a28 | -10.35485 | -47.89745 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85e7e17a-ae73-337d-8fa8-36d3ce783d15 | -7.93014 | -44.09436 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f52b1069-2c47-34c3-a2b0-4c879c5f6e02 | -6.44572 | -44.35887 | 2025-09-21 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4d22ead-2675-3bc7-a6a5-7e421eeec730 | -8.92525 | -46.24007 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caea0c41-90ae-3f33-a0b1-06dc2036b198 | -9.65793 | -43.86092 | 2025-09-21 04:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c04764d-8562-3383-83d1-8a9e659e80a7 | -11.2985 | -47.4966 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99c27e4d-3809-3a9d-afc3-a84ab3a5fc8a | -11.42927 | -47.32254 | 2025-09-21 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b66f073-b379-360f-b5b8-785c04d08d16 | -10.35875 | -47.89439 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c24de3d4-b745-388e-a879-4853c8de12bf | -5.52712 | -51.45081 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b2268a-cd44-3390-adea-62119ef97989 | -12.07281 | -44.83034 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25fcf00b-00f8-3c86-8a7e-1d9d49d89d42 | -10.28751 | -46.08099 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c919a0cd-a6e0-32a9-9477-c7355fd5656f | -9.00535 | -45.06776 | 2025-09-21 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5966ef80-0666-3633-8147-9b8eaed5a7a4 | -9.51569 | -43.06238 | 2025-09-21 04:36:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e06653f3-83bc-3a20-80b9-22d7df4fd195 | -11.43438 | -47.31189 | 2025-09-21 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0540a260-fc8a-35c7-9afa-df5d4564914e | -12.08266 | -44.85345 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cab3db71-a556-334d-a465-0bfecb7ad4cd | -8.60025 | -45.34048 | 2025-09-21 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e778bc2-a6cb-37ef-8040-993c878e52cc | -7.60429 | -44.49501 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6c8790c-4c00-3f48-acbd-407335a774b8 | -10.29342 | -46.09004 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ada9f1d3-141c-3133-93bb-1b55a15b8299 | -7.91345 | -44.10156 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 773fab70-366c-3a9b-b92d-7a793c6a991f | -9.08396 | -49.63988 | 2025-09-21 04:36:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206e4818-783b-3c79-bd79-545298dae8f7 | -7.72441 | -44.46632 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3c526325-276e-3f3d-b43d-4bf82654a724 | -7.93639 | -44.10501 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3844466e-9e8d-3b0d-b746-428bd9c80beb | -7.44874 | -42.61977 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5b2d917-031f-31f3-860a-a4ef81fc810a | -12.28181 | -45.27068 | 2025-09-21 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d72c143-14d0-3878-b597-31f9c53b5501 | -9.4289 | -44.70675 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e1c1d707-1e49-3fbf-9f2f-493d5be1dfa6 | -7.93569 | -44.10974 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d6a7ae0-a5d8-3258-a4e9-6765ba6f852e | -7.73415 | -44.45633 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a495f672-66aa-3120-8c03-7fd3d822e4b6 | -7.93256 | -44.10444 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 375d2fc1-ff07-3de7-8249-a75a675053e4 | -10.42014 | -47.85297 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eaa5c41-e55f-32f2-a57c-cd78d0e6fea3 | -10.34867 | -45.23362 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adb8f5b9-59d2-3c05-b5eb-b353298e157e | -9.17199 | -44.62423 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4874d760-d29b-32b0-91b5-e5cbbca399af | -12.07349 | -44.82561 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee631edc-0d98-301f-9a81-78f5289c710b | -7.91727 | -44.10213 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c4112c2-a45e-36c6-b300-a0f0850f3b35 | -6.39173 | -44.63601 | 2025-09-21 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88798279-db9a-3644-af70-3d4eaa156e90 | -5.82838 | -49.91659 | 2025-09-21 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 843580e9-4848-35e9-838b-d0a2acd3a38b | -8.98232 | -48.94724 | 2025-09-21 04:36:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20471e7e-e36d-36c6-a2aa-2d9756ec3fe0 | -10.3649 | -47.89902 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14f6b415-4859-3108-9713-537ffe3e477e | -12.09105 | -44.81355 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fe3174c-3e1c-3ad9-8eee-f4bc47f6262b | -7.92179 | -44.09797 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a680c573-8a5c-3e99-b64a-ad44991a73a6 | -9.62697 | -47.21069 | 2025-09-21 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13b83cb7-cc6c-34d1-8354-806ab3fc2928 | -11.2872 | -47.5023 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ce8a53b-f9a4-3dea-abad-2ca167f46824 | -7.0374 | -42.00867 | 2025-09-21 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 966f4106-093a-3e79-b741-080d78bae14b | -9.99822 | -46.23821 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a7f2247-ec51-39e4-a4fe-abe195e4b085 | -11.43382 | -47.31562 | 2025-09-21 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29bdb0b5-84e2-3dc7-9542-ec0301c011ba | -10.33919 | -47.88763 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 043daace-a575-37be-8e59-8cc64b5784c3 | -10.2855 | -46.07728 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 51673503-6a3c-3d7c-bd59-3491581751d1 | -11.27022 | -47.40581 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 281dc64a-7b9d-37e2-a2b5-099a7d9b53e6 | -11.27455 | -47.40212 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 871c8426-cbcb-37a8-b65e-46f73776c0d9 | -9.42514 | -44.70617 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a948ba18-93e6-34d5-924a-5e10856bd297 | -10.21933 | -48.07294 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84e5b6b8-68fa-3d2b-892c-a72cdc6f9e69 | -11.26094 | -40.96394 | 2025-09-21 04:36:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1065e869-c657-33ca-ad09-d2d940aa2d68 | -10.3582 | -47.89797 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d817bcf8-0394-3f70-a736-6264dbe1fa1d | -9.4238 | -44.71543 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2d51d1a-684f-3754-919d-14662eb8194f | -10.36155 | -47.8985 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5335199d-d9ac-3cb4-a724-d7f7db4f4941 | -10.33168 | -48.69321 | 2025-09-21 04:36:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a0f24df-cf7a-36e6-9685-6f72d8f4f332 | -10.0406 | -46.2672 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8474dca2-76d2-3df3-910a-4925b8fc3924 | -10.29106 | -46.08152 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fd6ae6d0-da0a-3f40-8af5-c70bed2d0478 | -10.85444 | -44.35245 | 2025-09-21 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77ec57f2-1906-39ab-a7a6-60872560c720 | -9.42824 | -44.7113 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09909257-59e8-30ff-89f0-bbad7942fb0c | -6.67615 | -42.43013 | 2025-09-21 04:36:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 819110a6-0d05-3a5d-8dbe-43d8eda1251b | -7.9204 | -44.10743 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3146f7f2-7c3f-3f50-99d6-796cc4c63c6f | -11.29287 | -47.51073 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e0fb76d-10f1-313c-b965-ef1a572c21ef | -8.83619 | -43.03889 | 2025-09-21 04:36:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6f2accd-f328-3fc0-b4a8-7f2b66903758 | -11.49496 | -43.58462 | 2025-09-21 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3ea67db-ca8d-3e9c-84eb-04bc81ea319f | -7.91702 | -43.88037 | 2025-09-21 04:36:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6333b43-6ac3-3bdd-ac2e-348842f448bf | -7.92735 | -44.11331 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 253ef47b-cb93-3a23-8583-e0266ca0e173 | -11.3036 | -47.5087 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30928d30-e9ee-339e-9c40-5bb1ffa82c8f | -10.2714 | -46.05066 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bf47d4b-abe5-385e-b8c2-e263716374eb | -12.28558 | -45.27126 | 2025-09-21 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bbb03f9-0abe-33c6-a376-acd76d406f4d | -10.25718 | -48.07161 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d1685d4-9c71-3d33-bd76-afab8caa5068 | -10.2881 | -46.07699 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e5461bb8-013a-3305-ae2a-aab045d0a944 | -11.30416 | -47.50508 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22a57ec3-f946-30e3-84f4-b8c620673dac | -5.69012 | -51.75559 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d7d160c-e13b-3c7d-9735-377832661d75 | -7.94404 | -44.10616 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ade555d3-1d48-3cba-85f3-952e1a52d40c | -7.34971 | -44.55072 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1ee24a9-6c63-3a2e-aa87-2d98b5312385 | -10.27019 | -46.05867 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203d9f40-69f6-3692-abfe-aacdecff157b | -9.86443 | -46.12115 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5dd12d60-6da9-3b73-82cc-3b1d1a20f81f | -9.4207 | -44.71024 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f94c71e4-1224-3bbf-8b48-a453c2f604ca | -5.69699 | -51.76152 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f369b93d-e37f-316c-8446-ba94118d05e9 | -7.95578 | -43.8932 | 2025-09-21 04:36:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2237bde9-89d6-38c6-a3e9-8118b18f66e3 | -10.33639 | -47.88353 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d842df0-1fd0-37de-bc4a-02f8ded6fc6e | -6.4148 | -43.85659 | 2025-09-21 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bebd8b16-aa98-385b-8fc3-44d72bc0ac85 | -10.36714 | -47.90671 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ad8382bb-0f1e-36da-ab29-7e25e0d6e552 | -10.85097 | -44.35034 | 2025-09-21 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f741ee7-24f9-32f1-91e6-299c48149870 | -9.93101 | -45.59544 | 2025-09-21 04:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0a36df3-c5c2-3480-9dc0-bb5b2d654dd1 | -10.3459 | -47.88871 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96fbf70f-8119-32b8-b213-5e22f453da0a | -5.69972 | -51.75927 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4924a64c-c7ce-3bc4-b00c-4e11751c9397 | -7.72099 | -44.468 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ac76184-fa81-311d-812d-97237a665419 | -6.55303 | -43.53075 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README27.md)
