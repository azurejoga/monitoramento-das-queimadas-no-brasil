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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af70edd0-7eca-31f7-92fb-68d6c65924a8 | -11.73971 | -50.62265 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| d87b3796-e261-30b7-80ec-4f7f0ef21645 | -12.06758 | -64.16965 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 39b3f976-52ce-3f87-8fb6-c04824f51d5e | -11.87672 | -58.82318 | 2025-09-11 01:09:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f50b6141-c874-3640-860a-1e1cb95acc66 | -13.01473 | -48.70691 | 2025-09-11 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 21631451-e64e-3ae8-97f5-bdde7d3e9e04 | -11.73019 | -50.64504 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6ae606f6-52b4-3c37-bb27-bc3d7533ae50 | -14.27996 | -53.08998 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 54905d86-6732-323f-8a16-cd2bf02f0db2 | -17.83238 | -46.74385 | 2025-09-11 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 37b96046-85b5-3fca-87ab-92dbd0dd8322 | -9.01384 | -49.77594 | 2025-09-11 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 399865ea-23b8-383a-8966-d0eea98c9c10 | -11.35879 | -46.5376 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 667ebcdd-97c9-32f2-82ce-bf799ab8c76f | -12.96728 | -54.76261 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7874e25b-d727-37c3-b702-7c2ab9cba9a1 | -8.78502 | -48.082 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| e7b973c4-cb03-379f-9023-ee42275399d6 | -9.79357 | -61.51671 | 2025-09-11 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 46104383-df4e-33da-b743-882a714c37a6 | -13.13896 | -54.91495 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 46af72c7-9ee1-3045-96fe-9fed604f121b | -15.66329 | -53.8927 | 2025-09-11 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7a4720c8-e2cd-328e-8a1f-b40f8a91c0e7 | -12.40398 | -63.81931 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 47956ff3-0d70-3283-9501-992a35f00a74 | -12.92916 | -54.80598 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 95bff692-cf0f-3854-b353-b673aa51b879 | -10.3835 | -50.51698 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 61cba0c7-798d-340c-937d-cc94d666d39f | -11.37664 | -46.53619 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 41fba5d5-8ece-3db2-819a-1af547ed955d | -15.56922 | -54.75832 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9f1ad427-1002-3c77-962d-2da0a1b7af7f | -12.92321 | -54.76551 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 65ca1696-cbbe-3272-a89a-76ecc3e64541 | -15.12688 | -52.40628 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 472dad3d-e470-39f2-9f0f-0bfea7c88a84 | -11.99173 | -47.59854 | 2025-09-11 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 8eaf7d25-4bf1-39e4-a0e9-e54f13a60a4d | -15.14556 | -52.45653 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| dc143453-b5f3-31cc-923d-47181f564f45 | -15.14157 | -52.43129 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 0f0bc41d-d75a-3d6c-ab98-0a51431182c0 | -15.55869 | -54.75 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5efe73a3-7047-3698-800e-3bd8afb6d06e | -12.07022 | -64.19197 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5c753aee-bf91-364f-991e-11fe60de1782 | -16.62116 | -49.42084 | 2025-09-11 01:09:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 60208e81-5837-3139-9042-d548c6528f68 | -15.87078 | -54.92818 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a79812b1-01c4-3936-b91d-f46f1fd6e60f | -12.6004 | -56.96271 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d2e3467d-eb5c-3918-b1ca-d76f2fbee058 | -12.93994 | -54.81461 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1e2c5929-c5ed-39ec-a634-cca8c2cf0e6a | -14.89073 | -55.87114 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8cdb6434-5eae-3a50-bc2c-d35d362de4af | -11.16693 | -52.02529 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 35cbed8a-a713-389d-883f-3df1f5c179e3 | -9.5224 | -54.64167 | 2025-09-11 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 2fdbca5d-77aa-31d0-81bc-401567d80fe4 | -14.28016 | -53.08338 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 31ba90aa-d934-35fd-ab92-522beef98691 | -8.02386 | -49.03427 | 2025-09-11 01:09:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 35bbd314-1c07-3c05-8ce5-78c3efb8ee15 | -8.02403 | -49.05931 | 2025-09-11 01:09:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 01180b85-1681-32a0-b6d5-9b2785390c0f | -12.09304 | -51.01999 | 2025-09-11 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 06ea4379-04ed-30a9-86f7-423aff12517d | -12.00028 | -47.60349 | 2025-09-11 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 62e5961d-cde0-3b2f-905b-609174f7be1a | -15.1605 | -52.4152 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 003dbc83-8224-356a-8ac0-9c0dd1a8ae7d | -12.92471 | -54.77567 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c889356e-dc68-312e-b25e-f8f10c3d79a2 | -10.05946 | -50.38632 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 489c6857-b8d9-391d-8450-2cdfd00d47cb | -11.21339 | -54.99146 | 2025-09-11 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a4f21f66-98df-3a77-826c-c8bc6548f6c4 | -17.83616 | -46.74846 | 2025-09-11 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 96e61478-3749-3ddf-8d33-0c12505361ec | -14.73856 | -60.24223 | 2025-09-11 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| eeeb1091-ac48-3f80-93ee-5e737d63aa4d | -16.51091 | -55.14878 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| beaad3ca-26f2-3d9d-8bf1-3bd2fa949523 | -12.93847 | -54.80455 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e9dc6568-60b2-3fdd-8a11-08d8ee5c885d | -12.92619 | -54.7858 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4d3e2cff-2304-30ca-9e4f-14f6696487bf | -12.96576 | -54.75246 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e5625f27-42c5-3e0c-8973-d9ba08f6e2f3 | -14.7607 | -60.25251 | 2025-09-11 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f69714cf-bda2-3155-8c68-0f7348b0aacf | -8.19367 | -50.11007 | 2025-09-11 01:09:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 4624f22d-9690-3f30-a288-6fc992540b34 | -10.39606 | -50.53147 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| ee500d61-8509-35e1-afba-93b154311b32 | -10.38282 | -50.53371 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 49a03cd3-0c0d-3e72-86a6-8cbdb527908b | -12.03379 | -47.55484 | 2025-09-11 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 3b2d329e-e7f3-3c85-8475-328d81ace7ff | -10.02585 | -51.7349 | 2025-09-11 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9e35e6a4-eefd-3599-8d54-e05c0acdf01e | -11.74298 | -50.64281 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a7104a36-763c-3964-aa12-37dfe21b96d7 | -8.43311 | -49.12366 | 2025-09-11 01:09:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5b7c6490-4d74-38ad-8927-dd03f587702e | -14.5647 | -48.76571 | 2025-09-11 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 2c2d3c3e-71ce-38b1-bc98-6e1761df0557 | -12.47648 | -53.82848 | 2025-09-11 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 22be6fa5-1c49-3a13-b946-e214cd69bfba | -9.79521 | -61.52948 | 2025-09-11 01:09:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 76b496bd-17c4-3f19-92ac-024a877ec6c0 | -14.57437 | -48.77034 | 2025-09-11 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 07e33587-7a22-3f18-a5c4-41c0b4285796 | -9.99879 | -51.7213 | 2025-09-11 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d16b9a98-6ab9-3a56-9b26-66ad1deb20fe | -12.21874 | -53.88829 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7e5d5f7b-88ac-3fb2-9725-203ac3d1f1e0 | -16.62006 | -49.41536 | 2025-09-11 01:09:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 5236b7df-b9cd-36a1-bc8e-ba1928f2f575 | -15.79331 | -52.26173 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 93a81251-2429-3869-9753-ef234959833f | -12.94972 | -54.75094 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 39e495f1-52f9-3bf2-9488-6604c94aaf13 | -14.73358 | -55.61552 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b879ca30-a071-3687-a73a-44652bf9c8a1 | -10.01374 | -51.73684 | 2025-09-11 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| a29f4fc8-a54f-3db6-9c10-f39d1fa4e672 | -12.60921 | -56.96141 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7363a5e5-4d08-352b-8718-b4e33def7772 | -11.16504 | -57.17949 | 2025-09-11 01:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfdfcd3c-0721-3332-b037-ac0937e29e5c | -13.13117 | -54.92631 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e303ab2c-7387-3086-98e9-3dcc6113e994 | -10.32476 | -48.82253 | 2025-09-11 01:09:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5bd785d9-7ea5-3b64-a526-dedbdc162454 | -15.80576 | -52.27272 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 2e8f7ab8-7d33-348d-b701-206b070995e4 | -11.15914 | -52.03226 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| c7701718-61d7-32f6-9a80-de26d538250b | -15.80182 | -52.24742 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c999c6c9-6590-3908-b059-a37327c9b6aa | -14.89569 | -55.84229 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fefd906e-1ce1-308b-a573-7ffcaf563be4 | -11.15798 | -52.04335 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 189.5 |
| ffb30cce-c401-34d4-9e7f-37aab9588b87 | -14.46094 | -53.26253 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 392f50fb-6256-34df-a27f-71f5dff7dcee | -16.27879 | -48.50659 | 2025-09-11 01:09:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a1b2b87a-a0f1-390e-9dfa-4bf8f52ab65d | -12.40132 | -63.8142 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 136.6 |
| f53bfb4d-e9d8-32db-ba16-ceedf58cebd0 | -15.14363 | -52.44434 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b4fdd569-65b1-3ed0-ac3a-3c5dd063a1de | -15.81318 | -52.27913 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7c73e55f-0af3-3c4e-9b07-06b957d50666 | -15.80776 | -52.28558 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 777a4ef4-a061-34f8-87ea-0a148af8db3c | -8.79671 | -48.10944 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 5f0a5ac4-cf6d-3076-9de6-9c3af88c3a06 | -15.12471 | -52.39265 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 70612af4-b2c0-3837-b6c7-1a7dd134af61 | -16.62494 | -51.82108 | 2025-09-11 01:09:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| afc12b61-4c13-3f4c-8b0d-197448864ba3 | -11.06488 | -51.34477 | 2025-09-11 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 65b50f6a-96c0-3f9f-a56d-22807fe02ce9 | -11.37646 | -46.5409 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c226e63f-85db-33d2-a791-57e09fce2e2c | -14.30498 | -54.75312 | 2025-09-11 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8443b4e2-f473-3183-ae49-e9b49c398322 | -15.13096 | -52.43204 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 94d50ee9-10ea-352a-8a8a-5587aa8a1fe0 | -16.48778 | -51.98293 | 2025-09-11 01:09:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7a9bb271-40eb-366e-8d58-53e2d3af548d | -15.1371 | -52.4252 | 2025-09-11 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0961b4f0-60dc-38b9-a2f7-f4c0ad309413 | -11.1624 | -52.032 | 2025-09-11 01:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 09c97942-9977-3faf-ad4d-00e60b24d280 | -19.2421 | -47.9802 | 2025-09-11 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e221f4a4-94be-3d77-8109-b137e973868a | -12.3976 | -63.8048 | 2025-09-11 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 889be2ea-f3a2-37c6-9273-096a4d56056b | -10.7369 | -46.0785 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 8ca14110-c34a-3316-bb58-4626eed8a3c7 | -12.4165 | -63.8038 | 2025-09-11 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ba959f09-b1e2-3381-936c-8731f00c879f | -22.5894 | -51.8759 | 2025-09-11 01:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.0 |
| fadc1977-66c8-3c87-b925-97aef2c2625f | -11.358 | -46.5393 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 47beed88-7c36-3b1e-9186-bf2792a6a752 | -10.3885 | -50.5264 | 2025-09-11 01:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e7695032-49c3-3f7f-94d8-d1538e4535cd | -19.2016 | -47.9889 | 2025-09-11 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |


[Clique aqui para ver as próximas entradas](README7.md)
