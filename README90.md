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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee887a1-61ba-30eb-91e0-88b8a2c8b87c | -14.48624 | -40.82528 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 03ee7308-329b-394c-82c7-c2659833e419 | -12.35081 | -44.27251 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e85b152c-4324-312d-a2a5-305c72cb2fdc | -8.69282 | -39.6041 | 2026-09-29 15:46:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c7ff056-74fe-31b1-a104-97c9d2195cdf | -10.11405 | -43.92778 | 2026-09-29 15:46:00 | NPP-375 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e92c1d6e-f043-3b2e-8a79-35e4bfa965e3 | -11.44121 | -43.44776 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 13409b2f-4bad-35ea-b068-87e6f4fb177d | -11.44043 | -43.43337 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f3030ce4-d7f4-3b83-a6a8-9f862e89a6dd | -11.32277 | -40.34627 | 2026-09-29 15:46:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6de59f31-9d9d-3101-9518-90d735299fa0 | -10.11329 | -43.92111 | 2026-09-29 15:46:00 | NPP-375 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d8531c81-cd84-3df9-bc61-98839d4ee5c1 | -11.2642 | -43.54251 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5fcb0f26-1339-3d70-92e8-c757334163e3 | -12.34234 | -44.27696 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cd0478b6-e83d-37db-9546-a136bd49a892 | -14.49105 | -40.82381 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 36a36459-8614-358c-b245-acd3bc4fb3f6 | -11.09833 | -43.31065 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9e3b0653-1414-341b-85db-07cfab9eb725 | -11.41159 | -43.42387 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| c55be246-e00c-30af-aeb6-718b618f08d4 | -14.97275 | -41.53627 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| c5f21b4d-a5ed-30fc-8937-84b56907d429 | -11.41224 | -43.43802 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 284b3a79-eb8c-38b0-aefe-fc4536eb9d47 | -13.16155 | -41.02221 | 2026-09-29 15:46:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 56becd1f-3211-365e-8d2d-233b130f86b7 | -12.42426 | -39.34396 | 2026-09-29 15:46:00 | NPP-375 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7090744c-551c-3077-98d2-60e65a5287a3 | -13.22132 | -42.53563 | 2026-09-29 15:46:00 | NPP-375 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 46237ccb-7a8e-31b3-ae93-b2bfae3361e5 | -9.44411 | -41.81978 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 3da23820-99e0-3877-af87-1c3c71f9574a | -11.65871 | -43.51543 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a9bdf74e-28f0-300f-9a7e-46de6719ebcb | -9.10892 | -37.74568 | 2026-09-29 15:46:00 | NPP-375 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e18c3978-0154-3a57-8b20-29c29bc30198 | -13.30703 | -43.96511 | 2026-09-29 15:46:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 65fbeafe-da7d-31cf-a9da-f162bf97cce8 | -14.23978 | -41.3091 | 2026-09-29 15:46:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 0fc8de85-098e-33e3-acb0-a3f718d7e041 | -14.75828 | -39.81421 | 2026-09-29 15:46:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e275ae7c-b54a-3943-a2aa-1c12dfc150c5 | -15.20772 | -39.78039 | 2026-09-29 15:46:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 48f39b03-6148-383b-b473-73ffb90bc4f0 | -11.62966 | -43.5057 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 44acd6c6-a517-3ca9-b7ed-4c56bde0541e | -13.3766 | -44.00113 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7e706f16-3dc6-3449-8916-a265e7b9b09f | -13.32638 | -43.94048 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 231.7 |
| f4632f4a-d779-3738-97e8-1f42ecfec10f | -15.45089 | -40.52606 | 2026-09-29 15:46:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d3efc07c-4c40-3463-8554-b7ff57ebe91f | -11.71406 | -43.4524 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 3af8a533-3345-36c2-aba2-b984e3f92fe4 | -9.79834 | -44.82612 | 2026-09-29 15:46:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 358422b5-d428-3d91-9bff-479462a8263e | -12.75769 | -42.0041 | 2026-09-29 15:46:00 | NPP-375 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b304b178-bccb-3f61-875c-77fce09cc23e | -15.01088 | -41.78923 | 2026-09-29 15:46:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fd9d5784-c6ef-3223-ab01-dbccd283d676 | -11.66846 | -43.54041 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| d5e76560-8ebb-35ed-ac97-22f94eeac38f | -11.6141 | -44.13714 | 2026-09-29 15:46:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d49ad54f-97de-3b14-ad59-f6650645d625 | -15.83736 | -42.56556 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| e1235253-3eb5-3609-b32e-6619cc1a9e31 | -9.06624 | -44.99845 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a7e096a3-9874-3343-a853-a7c7fd22e65f | -13.36102 | -40.97537 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 612ba7ae-ef9e-32ec-b6b2-b397a0602e70 | -9.44471 | -41.82437 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 5d11c00b-08cc-3cc6-a9c7-45648354bdf6 | -14.60362 | -40.76934 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 2d315899-4781-3edf-bcc9-fc6c6417c153 | -13.76001 | -42.89028 | 2026-09-29 15:46:00 | NPP-375 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e43d5ed7-47ff-3bd4-86ea-c4fc030c226b | -9.43802 | -41.81654 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 176.9 |
| 918d8541-7b95-3bb2-ab14-63bb031d9814 | -14.07312 | -41.36214 | 2026-09-29 15:46:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2f81bb5d-2bbd-3788-9024-592e5c67f10a | -9.45074 | -41.81968 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d115c22d-64bc-3606-a6b0-5ee7cc789a6a | -13.32874 | -43.93929 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 153e4798-3173-3f87-83c4-22f15a740fb4 | -11.42326 | -43.46703 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 1f736a44-9849-30bf-b26e-eb2e23045985 | -9.43858 | -41.82111 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 176.9 |
| 6d848d96-f763-3a74-aa21-86068e6e460c | -14.67525 | -42.84832 | 2026-09-29 15:46:00 | NPP-375 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| dd6ef007-fe8e-3cfb-8922-0d145dcad5aa | -14.66109 | -41.82829 | 2026-09-29 15:46:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a635ad7d-5984-39a5-b4f2-67d5cd5d0c22 | -11.72096 | -43.4516 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 38a038d7-15d0-368d-9a7a-0c5c3f4f892e | -14.62702 | -40.70168 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 7b1c4a0c-d585-397f-83d4-72f0b48a99ce | -11.44047 | -43.44148 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 81a805e7-995b-34e9-a58f-c4d0195a3061 | -11.3945 | -43.46524 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 62d56542-6e00-3a6c-a8f9-de5f21763c17 | -12.17388 | -38.59752 | 2026-09-29 15:46:00 | NPP-375 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 66f17a23-7298-3b15-841c-41c071d8261b | -11.23256 | -40.2003 | 2026-09-29 15:46:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fb395348-16e3-3cd2-b1c3-cea47b82cd7a | -12.5724 | -43.07202 | 2026-09-29 15:46:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| cfa9029c-a6af-36e9-b532-e90efe37c3bc | -9.05978 | -45.01517 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ef53bb26-807e-3603-85e8-66d3cd0c6198 | -9.17249 | -40.47592 | 2026-09-29 15:46:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d661a78-b922-32cb-a31e-a540ead6dea1 | -13.36935 | -44.00184 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 5fd1327b-585d-39a4-b87c-9657bdc100f3 | -15.31122 | -41.77711 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| c9f7a464-0ed6-3483-9fce-28c36280c505 | -11.25731 | -43.54332 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 37bce8af-aae3-3abc-aefd-3aa4e93fc372 | -11.75862 | -37.55335 | 2026-09-29 15:46:00 | NPP-375 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 44ff2be2-694c-30ff-983b-d3cc1e6a999b | -11.26349 | -43.53616 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 899efa88-3082-3208-853b-3fd170c21dc8 | -13.76952 | -40.62729 | 2026-09-29 15:46:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ddda53d7-5578-3490-a840-59a7df6d0245 | -10.95205 | -43.87721 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| df4ef00e-4079-324e-93b8-61136bdc1899 | -11.41914 | -43.42937 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| abb45e2d-61a6-3f28-90eb-075492a14844 | -7.936 | -37.21701 | 2026-09-29 15:46:00 | NPP-375 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| eb6a26df-1ee2-3b4e-ac67-1068309d6a8b | -13.02895 | -41.04232 | 2026-09-29 15:46:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c1729534-9e29-321f-afd2-a7ce9c53396c | -14.3809 | -41.67058 | 2026-09-29 15:46:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c5594801-b08c-3ebf-906c-3d327f837f19 | -8.79429 | -41.08653 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| faade908-4724-3903-9f63-62afc6dd2ed5 | -14.65917 | -41.32959 | 2026-09-29 15:46:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 42.7 |
| e34e68c7-2c2c-337b-8909-f770dc718db6 | -8.30642 | -39.38303 | 2026-09-29 15:46:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 50b51848-8a8a-3242-b0f1-2784ffebedda | -11.63104 | -43.51846 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| ab3a6846-a83f-3c98-8629-e40cc8fe393c | -14.19835 | -42.04433 | 2026-09-29 15:46:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a07fefce-f4a9-3e18-bf8d-2353da30bc82 | -15.31293 | -40.97866 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 41465d78-e956-361b-ad8d-bf753cf7dc00 | -11.40404 | -43.41834 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 17c1d4bf-5aef-3306-8f15-264e5216a3d2 | -15.50477 | -42.86917 | 2026-09-29 15:46:00 | NPP-375 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f427bf54-410c-3d2f-80b7-6495fd9b3a85 | -12.43448 | -44.14985 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| b128b744-2628-35b1-a385-6dffbc883787 | -9.48377 | -39.06252 | 2026-09-29 15:46:00 | NPP-375 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 011611ab-5eca-3f0a-b3d0-51b632fdf8bc | -15.19515 | -41.43013 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 8b63b2bf-e00a-31c8-8a78-9bd3d6b5b700 | -14.38669 | -40.93866 | 2026-09-29 15:46:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d7d8d68c-c2d5-3115-9c19-85dcebd08504 | -9.06537 | -45.00013 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 2662c2c1-4e1c-3628-bef5-f1103e4e626b | -11.62897 | -43.49933 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| f9aa9d9d-f570-32c4-aa3e-66fac1c82cf9 | -9.24257 | -37.06951 | 2026-09-29 15:46:00 | NPP-375 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d72261d8-6d0d-31cc-910e-e6e3098adac1 | -11.307 | -43.55017 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f2973649-c1ed-3470-86e1-90905c03e764 | -9.77173 | -44.85281 | 2026-09-29 15:46:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 82a613c5-31cd-398f-a51d-c30438d14dcc | -15.75473 | -42.28722 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 31999a39-8e34-37c6-9c83-537e2dd3ef10 | -12.21902 | -42.02064 | 2026-09-29 15:46:00 | NPP-375 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| cc9d1868-34d6-3df4-a6a8-0f72a8830f25 | -9.45079 | -41.82367 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e9dd4087-60c1-3585-8a31-d4d378065159 | -11.66011 | -43.52823 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ad4b103c-49bf-3210-bef5-d98beae8c49f | -8.61063 | -36.49126 | 2026-09-29 15:46:00 | NPP-375 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 16991479-216f-37c7-be52-a3921327262c | -10.28267 | -44.62306 | 2026-09-29 15:46:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b6da92a8-fd44-3111-b56d-40fcae552f0a | -15.08229 | -41.41307 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 872dc9a4-887e-3853-b285-7537f300a0b7 | -14.34983 | -40.82854 | 2026-09-29 15:46:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ae5ca1d8-a7c3-3a33-83a1-76c355055d46 | -11.65958 | -43.52328 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2aac908e-5dca-37b7-930d-1dbaeae5f424 | -13.37396 | -40.86378 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 323c6c8f-588d-3b46-b240-f6809e460184 | -11.45151 | -43.47047 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6961b9ee-9542-32c9-9dfd-b63fba7132d5 | -14.38643 | -40.94 | 2026-09-29 15:46:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c93c107b-7973-3901-a592-65944fe05d36 | -9.61263 | -42.31234 | 2026-09-29 15:46:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4b8b4094-a1b0-3b1b-a858-18656c796ffe | -15.48651 | -42.59882 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |


[Clique aqui para ver as próximas entradas](README91.md)
