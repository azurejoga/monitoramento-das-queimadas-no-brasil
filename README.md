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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9714a95c-b97a-3450-a3b2-5e66da2f0666 | -13.4901 | -52.9715 | 2025-05-11 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 620cd0b4-d840-3d37-87d5-994231b38488 | -6.7053 | -42.1234 | 2025-05-11 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 33991ff2-f7cf-3fd6-a593-14f510f305df | -10.6296 | -46.370201 | 2025-05-11 00:08:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 806faab2-df8d-3f26-8727-c93c3ea08c08 | -9.0283 | -36.662899 | 2025-05-11 00:08:00 | METOP-C | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87f9eef1-0f2b-3574-8966-ba0599e09056 | -14.6707 | -45.129601 | 2025-05-11 00:08:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0258484-8d7d-3168-9ac4-f52d76017444 | -9.0302 | -36.6707 | 2025-05-11 00:08:00 | METOP-C | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfd90617-bbc0-32d1-bd5c-bb9fc8b9bdde | -14.6512 | -45.133499 | 2025-05-11 00:08:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3aeac75a-c555-3aa3-8085-63248088999c | -20.164 | -46.831699 | 2025-05-11 00:08:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88fd05ba-ce53-356a-a556-4650a6b6ea2e | -10.4992 | -42.398499 | 2025-05-11 00:08:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 73715605-58ab-3233-8805-2e31998e31a4 | -14.661 | -45.131599 | 2025-05-11 00:08:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 587be10f-af80-364c-bc87-23b798f15e91 | -14.6639 | -45.1464 | 2025-05-11 00:08:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0cf3339c-2e0f-3533-bad9-93628bf744d7 | -13.471 | -52.9737 | 2025-05-11 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6458d180-4d20-36bf-ab59-b71190fab8fa | -6.7053 | -42.1234 | 2025-05-11 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 7e774c8a-c00c-3031-852e-bcb6d0a1771c | -13.4901 | -52.9715 | 2025-05-11 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d3eb033c-9696-3c33-80a6-d473400ac761 | -13.4901 | -52.9715 | 2025-05-11 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 81a4d82d-a04e-3888-ad81-51f2accd58c5 | -6.7053 | -42.1234 | 2025-05-11 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 6868a1b5-1c06-3c41-a415-ec141bab695e | -13.4901 | -52.9715 | 2025-05-11 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| df947c1f-16b1-39bb-bff9-8faea89ae0be | -20.17566 | -46.82295 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8f96f89f-123e-3703-afdf-8553b5104b29 | -16.49235 | -43.13818 | 2025-05-11 00:33:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eadbcdcc-26b3-3ec8-8141-7c509ad928ef | -14.65486 | -45.13015 | 2025-05-11 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c1900c80-76bd-38d8-bcb6-e2f087646aeb | -20.19235 | -46.71381 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 729db16a-0b17-3064-a0e7-2a0f18a940b9 | -20.17422 | -46.81094 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 69735e6a-4b64-33e1-90e3-0a6f7af9a02d | -20.16716 | -46.83557 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| df98b24f-27eb-3ffe-ba8b-c084ffa5b0f3 | -20.16569 | -46.82331 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1e742148-7a4a-3d56-9779-65edd1fb24b9 | -20.15581 | -46.82435 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d93ccceb-cd12-38ee-84f1-7186afba42ec | -20.15723 | -46.83628 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1a695513-fbb6-3f2d-8a4f-7303b41b810b | -14.66369 | -45.12883 | 2025-05-11 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dea8ec33-acbc-3169-b61e-c96f7c5d353b | -20.1215 | -46.88417 | 2025-05-11 00:33:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0bea9255-376b-3b0f-94b8-9862c0090a3b | -14.66495 | -45.13791 | 2025-05-11 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b373eb3f-36d5-3a1b-ad95-57b4776b2780 | -20.37646 | -48.07924 | 2025-05-11 00:33:00 | TERRA_M-M | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 690d636a-bfe1-3ca0-b98f-6ecaadd8b84d | -20.15503 | -46.83093 | 2025-05-11 00:33:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 998a55f4-3471-3932-8c11-4c3c146afd71 | -14.67253 | -45.12752 | 2025-05-11 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9474488c-bac5-3d11-8251-34c39220e9e4 | -20.17891 | -41.50953 | 2025-05-11 00:33:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 278fcf49-400d-3c7c-a25a-554e8dfa5aea | -14.67378 | -45.1366 | 2025-05-11 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27eaec2f-c66d-3376-a687-e76f6c3ec758 | -17.46121 | -44.71594 | 2025-05-11 00:33:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4f2d9c6d-849a-32e1-bb8a-bfb28169c889 | -14.65611 | -45.13923 | 2025-05-11 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2227d1a9-0aab-305a-a599-7d8aa957c994 | -20.13133 | -46.88252 | 2025-05-11 00:33:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 849ba756-ce22-394e-928d-c888342fb754 | -12.11222 | -47.98146 | 2025-05-11 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| bc468c52-5cee-357b-9f70-67cdbd0bfd91 | -13.47812 | -52.98399 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e0835e0e-708f-3ba9-8515-b69f66d798c4 | -7.65937 | -46.1017 | 2025-05-11 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a4077c9-143c-33f3-af01-428518d75e8c | -7.5881 | -45.86382 | 2025-05-11 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9596e56-873f-3a7e-8c07-8a2c766bfb00 | -10.62461 | -46.3673 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e59a2efa-ddfb-3491-a0c1-14c3f1b86292 | -10.50099 | -42.39769 | 2025-05-11 00:35:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d7acf243-bf75-3421-af87-6dd9651b0c27 | -11.60751 | -48.00687 | 2025-05-11 00:35:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9da0e6e5-0631-3ec3-8bd2-9becec79054f | -10.49775 | -46.1812 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d0b0727d-337f-3d5f-8b93-53e61fcc1cf9 | -10.48768 | -46.17353 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb9af1aa-b8ad-3a82-8fb1-dac5837c2633 | -9.67699 | -49.72826 | 2025-05-11 00:35:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3710e338-9cea-3582-9157-ec760b723e98 | -13.04345 | -53.7275 | 2025-05-11 00:35:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9042f30c-9510-32a5-84da-db8276ac078f | -10.77209 | -46.29723 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f7ec051d-48c1-3a45-a93a-3798075c6971 | -13.48563 | -52.96279 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 9995582c-41b1-3385-8e56-5692b12c9402 | -7.58686 | -45.8549 | 2025-05-11 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a77243c-1c9d-378d-9a5e-376ec2112529 | -10.49651 | -46.17226 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1dfd5bf9-fd5c-3513-8272-44e2ba132f7f | -10.48891 | -46.18247 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a95cd7c5-ef39-3176-bf77-2c7cdbdb1c27 | -13.49236 | -52.98239 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 39edc582-7681-3aef-aaca-9c881ca6770d | -10.62585 | -46.3763 | 2025-05-11 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 56f1b850-9a3e-308b-99c6-c7b6d87b9801 | -13.4754 | -52.95871 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 6e425ea4-d1ef-3e31-b7cb-e2ccd33c5f7a | -12.11357 | -47.99178 | 2025-05-11 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0712aff8-42b6-3c30-9571-7c50a8b5c147 | -6.70789 | -42.13451 | 2025-05-11 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 2c0d15dd-b2cf-36aa-ad7e-9ef77ba16e21 | -6.70948 | -42.12847 | 2025-05-11 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 9b8318c8-a0f3-3658-a4c8-64860efbfd6d | -13.47433 | -52.9898 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| cdd36e78-d030-322e-8774-0ff34435a866 | -13.48856 | -52.9881 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 32bb5acd-e2d5-3abd-9566-e29328b4bc1d | -13.47143 | -52.96452 | 2025-05-11 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 20070648-8a1d-3c49-b107-d8fcd944d9ad | -6.70584 | -42.12037 | 2025-05-11 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| fb242368-1414-38ef-b653-ad0955b0d4ad | -13.4901 | -52.9715 | 2025-05-11 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2a852a96-1614-38a6-a099-2d36c2057fdf | -13.4901 | -52.9715 | 2025-05-11 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a710a0ca-6ed6-3dc6-9fd9-184a1de83091 | -13.4863 | -52.967602 | 2025-05-11 00:54:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 114abd92-6994-3e0f-ad24-e1c1176a110c | -13.4843 | -52.959099 | 2025-05-11 00:54:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed657722-495d-31a4-97c7-30ab26682d43 | -12.6934 | -58.146599 | 2025-05-11 00:54:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2458f1b-45c7-3545-b763-783ab2273b14 | -13.0523 | -53.7174 | 2025-05-11 00:54:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7dabff-c2fb-3bc7-9cb4-23db512301f5 | 0.5574 | -60.834801 | 2025-05-11 00:54:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4742611c-e830-37c8-a799-5ba53767e67f | -13.0425 | -53.7197 | 2025-05-11 00:54:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc6173cf-be13-3b74-bdeb-1c12659d8820 | -12.6918 | -58.139198 | 2025-05-11 00:54:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e410c662-3b25-3c8a-8d04-d95b3c7b822e | -11.4037 | -52.939201 | 2025-05-11 00:54:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 720806b4-4bc8-345a-a7e3-095d0dc2d264 | -13.0541 | -53.7253 | 2025-05-11 00:54:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1f7e31-cd49-3a40-83bc-0283a43997d0 | -20.160601 | -46.813999 | 2025-05-11 00:54:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4309ed9f-35bf-35bf-8737-d87b53f1cbae | -13.0504 | -53.7094 | 2025-05-11 00:54:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3914a0f8-e236-3a9d-adda-459092b70d31 | -13.4883 | -52.976101 | 2025-05-11 00:54:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 441ef06a-3716-3073-9dc3-0deeaaf2d8b0 | -12.6573 | -54.061798 | 2025-05-11 00:54:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6b5120e-a48d-3edb-b57b-925960f8277c | -13.4786 | -52.9785 | 2025-05-11 00:54:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65192b66-88f8-3e10-b32e-86812b538a3f | -13.9852 | -56.805 | 2025-05-11 00:54:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6d1863-e449-32b1-bf95-b7cafa251a58 | -13.4766 | -52.970001 | 2025-05-11 00:54:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a874b80-2dce-311d-bfb4-f9e820bc647a | -14.8735 | -51.974701 | 2025-05-11 00:54:00 | METOP-B | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be3de193-d2ed-35ef-a829-a03728e2343e | -13.4901 | -52.9715 | 2025-05-11 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 93a81335-f03a-3555-85e6-47821854db0d | -13.4901 | -52.9715 | 2025-05-11 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2918c028-2563-3a2f-9dbb-0e7dc07fa9cc | -13.4901 | -52.9715 | 2025-05-11 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3820dcce-bb6d-3f52-a016-3f7ec1b63d3e | -13.471 | -52.9737 | 2025-05-11 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7d50eed6-4c6c-348a-94d9-4b41f3e32fe2 | -13.4901 | -52.9715 | 2025-05-11 01:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 23aa373a-5eb8-3296-b3fd-e80e74a39899 | -13.4901 | -52.9715 | 2025-05-11 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d96ac33a-6f38-3773-b8f1-5ba558219224 | -9.02806 | -36.66806 | 2025-05-11 03:10:00 | NOAA-20 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b5d57b11-91be-3ad1-a5ca-817a52d25b4d | -9.02749 | -36.67124 | 2025-05-11 03:10:00 | NOAA-20 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 779e794d-9b70-3f02-963d-c7786e260b40 | -16.4932 | -43.14165 | 2025-05-11 03:13:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d276370a-2844-3f3c-845c-d068e656f74f | -14.27826 | -42.69426 | 2025-05-11 03:13:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d8a25f4f-9b61-3108-a1b5-ef0aaa29618d | -16.49195 | -43.13885 | 2025-05-11 03:13:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1bf73c05-2b8e-3ebf-a462-1485fb9b68f1 | -16.49481 | -43.13465 | 2025-05-11 03:13:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55c2ca7b-72fe-35bb-94c6-2254b3bf348d | -5.06893 | -37.71662 | 2025-05-11 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0235fcd2-2074-3298-9737-251d16739b59 | -7.84597 | -36.85047 | 2025-05-11 04:00:00 | NOAA-21 | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4bf67008-8929-3526-b594-5b3680a8979a | -8.07384 | -34.97666 | 2025-05-11 04:00:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfe483e7-7eb4-3561-a64d-0c887b102b47 | -5.67327 | -37.22039 | 2025-05-11 04:00:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 777282b1-5b3f-37ba-abe1-74db9d845d13 | -14.64979 | -45.1296 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7acae504-d24d-380b-9243-78b28c30de11 | -14.6534 | -45.13024 | 2025-05-11 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
