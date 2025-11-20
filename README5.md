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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3fe45fe-eba6-3d89-87a1-0759707167c7 | -2.94005 | -40.28596 | 2025-11-20 04:10:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0597a5d-e6c8-397e-8ab4-414396a350e4 | -4.13142 | -43.83326 | 2025-11-20 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 582b667d-3396-3fe7-9c00-8789fc347e1a | -7.27031 | -35.1185 | 2025-11-20 04:10:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2682fdbd-0503-3338-97a4-cae5d3aa8417 | -4.66617 | -43.22433 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63f775f7-9eb0-34ab-90a1-0a7a765bc395 | -3.57476 | -39.78098 | 2025-11-20 04:10:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8e900537-f3e4-3ade-b018-cb7a6d442e57 | -6.81459 | -39.50904 | 2025-11-20 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0840c6b1-7874-377c-ad92-34199c2a8f49 | -3.00258 | -44.38454 | 2025-11-20 04:10:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2e01dc9-bc45-3792-b8ca-f5720638efe6 | -5.90975 | -39.23971 | 2025-11-20 04:10:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45c90a0f-6d6e-3e79-98af-009de0f42992 | -5.33476 | -43.42897 | 2025-11-20 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4fa3f2a-3c7e-3768-b355-4e3278375659 | -5.03817 | -43.60296 | 2025-11-20 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54281b3d-656b-355f-be2a-68b03bfc4dd6 | -4.06277 | -46.25103 | 2025-11-20 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c0e627-c66e-36a0-8b70-82cc815b02aa | -4.67308 | -43.22545 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad081a9f-41a5-3df5-9e12-9d44e61f6cc1 | -3.67813 | -50.16073 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d3079a8-1ed9-350c-9617-afcd6f14e89e | -3.68186 | -50.1718 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5de68df7-daee-3456-9779-7e61c9868cfa | -4.66962 | -43.22489 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e0b81d2-6589-33a2-9251-988b225c74ec | -3.23315 | -44.85258 | 2025-11-20 04:10:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b685568-78d5-3531-990c-da659b763fe6 | -2.30126 | -46.30386 | 2025-11-20 04:10:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa0f6d83-cf3c-3423-998c-26d67bea5931 | -4.32969 | -43.65472 | 2025-11-20 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 649af747-5c05-39d5-b4a7-010aedac264e | -7.0273 | -35.19167 | 2025-11-20 04:10:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 57654c8e-719f-38c1-b711-7a0af2d12c76 | -5.61434 | -37.46882 | 2025-11-20 04:10:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d36c8a8-775a-3240-be3e-70c26cf3f19d | -4.67429 | -43.21791 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 045d5068-5100-3b79-bc10-5f38baa78ca7 | -6.85043 | -35.18242 | 2025-11-20 04:10:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e5c52e14-0b78-3ccc-b125-a2ad03b523fe | -2.85631 | -45.0073 | 2025-11-20 04:10:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5007afb6-ef85-3976-9653-a64e6c2e4dca | -4.1463 | -43.69586 | 2025-11-20 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5f4baca-fe69-3156-936c-7e00b1698292 | -2.48045 | -49.32582 | 2025-11-20 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d58110b-964a-3821-ae20-9b43b3f1579e | -3.67381 | -50.16125 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ffd1f8e-9a0c-3583-896d-dfeb0fe76115 | -3.25372 | -42.5555 | 2025-11-20 04:10:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68e54289-e5f4-3d43-be34-8672c017fc39 | -4.6806 | -43.2228 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b58d2774-addb-3c72-8094-823f92cf45d9 | -2.5114 | -47.82503 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11983754-e51c-35b0-837d-109d0eb0de03 | -3.67978 | -50.15885 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f5b379-b62c-302c-b08c-799bb28750f8 | -2.92972 | -45.05095 | 2025-11-20 04:10:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a71c5b5e-ff8d-3de0-be97-e388bea56845 | -4.14179 | -43.67882 | 2025-11-20 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40617cfc-6c19-3f9f-8051-fb06c35c159a | -2.50993 | -47.80454 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f670bba4-2785-3c7d-8066-246567f04054 | -1.87829 | -47.0508 | 2025-11-20 04:10:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7ce35ff-b790-35f1-a49b-7289e47ffc50 | -3.68343 | -50.16991 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e612c10-6ddb-3bb9-959b-377c7cfb44b6 | -6.81343 | -39.50887 | 2025-11-20 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf41c618-f02a-30ac-9a0f-954d3f8c0217 | -3.65917 | -40.90085 | 2025-11-20 04:10:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eee922c9-79ee-37e4-b17a-7dc2df5bb9f8 | -3.2324 | -44.85723 | 2025-11-20 04:10:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0df2807b-7841-3db8-bcc1-6f68a250a23f | -4.05864 | -46.25043 | 2025-11-20 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81ae8312-55d7-30f4-beac-89af36a9b098 | -4.06687 | -46.25175 | 2025-11-20 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a200faa-269c-34d5-b2fb-f0115e71bb28 | -3.4541 | -40.50492 | 2025-11-20 04:10:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 82a0c95b-685a-3f5f-9cfc-af75ec501031 | -4.67714 | -43.22224 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bfdb62d-c208-34c1-bdcd-39b43d164ec1 | -3.67757 | -50.16412 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d3a1cc6-0e57-30df-a77e-4d75b856a0d5 | -2.51222 | -47.82003 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6852caaa-82cb-3d5a-8a7d-4f9104105c63 | -4.38986 | -44.08478 | 2025-11-20 04:10:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe1ff822-fd14-3d31-ab59-b6950bbc2275 | -3.01133 | -44.45673 | 2025-11-20 04:10:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f7175c-1e05-37a0-9e58-c12f4b86b999 | -3.68032 | -50.48452 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce854622-c9ee-3380-b155-e24184d4cb50 | -3.29883 | -40.00734 | 2025-11-20 04:10:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fda9dcfd-03f7-3606-aa89-a80e8492394f | -3.67744 | -50.1724 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e909dc16-6691-3686-b2cf-5ef513f2b892 | -2.51383 | -47.81014 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6a19d993-93d1-3174-a50e-e60532cedc56 | -6.01819 | -43.66065 | 2025-11-20 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 823e78e0-1c1c-35ce-9cd0-9fa5bbfa78af | -2.23407 | -46.54015 | 2025-11-20 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6bf8cfe-2892-3dd0-a962-a21454c029b1 | -4.14533 | -43.67938 | 2025-11-20 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc334f02-2255-3c31-8296-fcd75bfc9126 | -3.8481 | -43.94919 | 2025-11-20 04:10:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da829e62-4688-366c-9641-e39965434c9e | -6.8555 | -35.17876 | 2025-11-20 04:10:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 28a87c77-2bc7-3a9c-9865-2a73f20b3722 | -4.85754 | -43.98448 | 2025-11-20 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eeb7d4c-4b9f-3701-a96f-313f697e039f | -3.68298 | -50.16503 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27b1c815-f2f6-300f-b29d-9a253ec96f70 | -3.5908 | -40.96783 | 2025-11-20 04:10:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32f0cf70-1143-3a97-bbff-f819b891d2db | -2.5161 | -47.82578 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fcbca04-0d4a-3dcc-818c-528ba6791a5a | -3.67911 | -50.49168 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0240a5c1-0da1-307b-8620-45dc315ea9ee | -2.51541 | -47.80044 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1414aba6-fcbc-3ac1-a86e-4564b088d815 | -3.67646 | -50.17089 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b71b6bc5-5281-3b8f-84a8-7efe2a49bbd0 | -3.01507 | -44.45732 | 2025-11-20 04:10:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 744185e7-00f7-3c2a-bc50-304ac71ffc68 | -4.67083 | -43.21737 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e3ffcae-9f33-3bfc-a2d7-6dc2646cab7f | -6.85169 | -35.17367 | 2025-11-20 04:10:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3ee9d392-2680-3df6-bc31-bf00f63258af | -6.68816 | -38.06388 | 2025-11-20 04:10:00 | NPP-375D | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8728dc24-b4e2-3233-aea5-78d9fb5de312 | -3.67321 | -50.16468 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b2ee43-f192-3bfa-a286-f1254e0f3c9a | -6.16114 | -46.10223 | 2025-11-20 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7626909-3726-3b47-b7b0-8964f10ba62a | -4.66902 | -43.22867 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b2846c6-5493-3540-b980-a28a4005478c | -5.48408 | -39.51259 | 2025-11-20 04:10:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 90ae20a2-a55a-3df8-a280-8083bf6d8308 | -3.68401 | -50.16653 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8fac15b-1745-3b8c-8adf-3bd2f062dae2 | -6.84662 | -35.17737 | 2025-11-20 04:10:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 21151009-b0bb-302b-9a86-440f7a7a70e5 | -3.67361 | -50.49061 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54a0162a-921c-34cc-909c-d670a9ef6e5d | -3.67972 | -50.48807 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 221e75de-04ca-3712-8c05-19b7a0b8dadb | -6.85106 | -35.17806 | 2025-11-20 04:10:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 918e6ea4-8f97-31f9-a7ca-71edd64257e1 | -3.23464 | -44.84327 | 2025-11-20 04:10:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 049fec1b-77fc-3103-b8b1-34c203e53e8b | -3.3462 | -44.50935 | 2025-11-20 04:10:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e8071e6-0ba4-3175-808c-aa80dfc58f00 | -2.9588 | -41.55727 | 2025-11-20 04:10:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd55a42-e9fa-33a7-82bc-57639f699d32 | -4.69912 | -38.64977 | 2025-11-20 04:10:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2195fc0b-2e91-3646-8160-e47821b96c15 | -2.92469 | -40.34023 | 2025-11-20 04:10:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4858decd-9843-38a4-999c-ac69aa64182e | -3.67702 | -50.16749 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d43edfe0-06f8-35e6-98fd-8b15ea1bd0d3 | -3.67919 | -50.16228 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34e033db-0abf-3204-b699-c7fbdb1cf9a3 | -4.67023 | -43.22112 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71da274a-64e7-3b13-a199-ff63167b5589 | -2.9395 | -40.28942 | 2025-11-20 04:10:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd676d4c-761c-36f1-9983-c108f13ef048 | -3.66249 | -40.90137 | 2025-11-20 04:10:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ea5fcca-7fe7-329b-81d8-826ef96696aa | -4.67247 | -43.22923 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c440ce6e-26ac-359d-83c0-69eb1f44051b | -2.85708 | -45.00249 | 2025-11-20 04:10:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31e78551-81a9-3af8-bba2-244b29f58a1d | -4.10155 | -50.06128 | 2025-11-20 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e169295-c60b-33ad-8e48-ae75160143b6 | -4.10632 | -50.06558 | 2025-11-20 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8604d125-895f-32a0-930b-361b847d528a | -2.08316 | -45.6512 | 2025-11-20 04:10:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abc62f89-3c4f-37dd-b509-e862faa70137 | -3.49789 | -40.29185 | 2025-11-20 04:10:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97e9d6f0-564a-380a-8e31-68300340d8ed | -2.12972 | -46.19018 | 2025-11-20 04:10:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1791140f-d5ba-373a-bab2-4aeae77ef15c | -3.67861 | -50.16565 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 968af179-2b9c-3c36-8877-e4fd81f6abb6 | -7.03175 | -35.1923 | 2025-11-20 04:10:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 31aa0e1d-150c-3632-a0b3-cf49a237446f | -2.23191 | -46.53862 | 2025-11-20 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 914cc39e-c2c9-3b0d-8238-4e0dec877605 | -2.83086 | -40.35757 | 2025-11-20 04:10:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e31fd0a-225e-31ac-8886-428bb36f8475 | -3.84743 | -43.95332 | 2025-11-20 04:10:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb5c0382-6ac0-3b2e-b405-d201995eb3b8 | -7.02908 | -35.18971 | 2025-11-20 04:10:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f3e3af34-c3a5-3f73-8198-0c80b2098790 | -5.49886 | -39.16724 | 2025-11-20 04:10:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f696d8f-475e-3952-b355-978b1e974803 | -4.85688 | -43.98849 | 2025-11-20 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README6.md)
