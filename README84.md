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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8e82557-7173-3308-b734-95a3441b9524 | -6.28552 | -44.01209 | 2025-10-16 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7d3ead52-82f4-35d3-8fee-7260861a4c16 | -5.88251 | -42.78568 | 2025-10-16 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9f0df104-962f-3b51-8411-20532d685d6c | -5.62914 | -45.83614 | 2025-10-16 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 93773620-ba35-3e58-9d76-388f110e173b | -5.47448 | -42.92981 | 2025-10-16 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 230.6 |
| 88f7ebc2-1b57-3070-9008-7111f523bb42 | -5.67705 | -45.1104 | 2025-10-16 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6fbfa8c6-2874-36a6-9ceb-b92c69401863 | -6.052 | -41.93461 | 2025-10-16 11:57:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 3434af6d-7029-3fb3-8272-9b173c2811d3 | -3.33245 | -42.55173 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56a44c63-4836-327a-8822-5b33426c2eb0 | -4.0024 | -43.27756 | 2025-10-16 11:57:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 53d9b5fe-be79-3bec-b971-e5dd67ac6a67 | -5.53798 | -41.32861 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3948c281-c806-3e56-b5f8-cc6e49d847d7 | -5.47318 | -42.93872 | 2025-10-16 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| c8e581c1-e0ec-3bd3-a6b9-078695462c6b | -3.33407 | -42.92517 | 2025-10-16 11:57:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9d78a204-20f6-3af7-ad7b-70a6f3dca6ef | -4.38408 | -43.38181 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f74ecb10-77a5-3b2c-93e5-873c290447da | -6.22715 | -42.50205 | 2025-10-16 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d9d64c59-4c1b-386c-8f9a-f1791361fd8c | -5.48335 | -42.93108 | 2025-10-16 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| e67cc7d4-d42c-3249-ad96-7318d7981c4a | -6.39488 | -42.55602 | 2025-10-16 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6a4c7eac-3f7a-3480-afa4-1f273e2a3b68 | -5.63092 | -45.82412 | 2025-10-16 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cf18789c-bbb4-3d58-89a9-c26e3027f462 | -5.87357 | -43.86094 | 2025-10-16 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d719c739-8a1d-385e-af81-75d3c38de689 | -3.74811 | -41.71256 | 2025-10-16 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2cddaecc-d2a2-3635-823d-d74ff5be8380 | -6.19767 | -43.28301 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 751bfc4c-9abc-349e-8c09-19b8d9b887d0 | -3.36201 | -41.45505 | 2025-10-16 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 3bee7353-f082-3685-a60c-9f326fe4b6fc | -4.66699 | -44.09711 | 2025-10-16 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 08819e0e-9e72-3715-9d92-a1fbaff47164 | -4.87184 | -44.58648 | 2025-10-16 11:57:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 632c65a4-5ab0-308e-8c09-58fd97fd05f2 | -3.31711 | -42.59507 | 2025-10-16 11:57:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c10c1983-d7a5-3d96-b7ba-8a55945161b1 | -3.55491 | -43.75813 | 2025-10-16 11:57:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 294ac984-5777-37a6-9657-7528657c70c1 | -3.31582 | -42.604 | 2025-10-16 11:57:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 138b865b-5381-300c-a893-2cd8119dd44d | -5.83507 | -42.22471 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 234769c7-f694-3d0c-ab24-65cba31f95a2 | -4.39176 | -43.39234 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 96d9b41f-8d3f-3098-b787-0b334ae8e9fb | -4.40079 | -43.39363 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f86ddf79-1350-3d9d-8566-db5db72b04f5 | -6.37201 | -41.49108 | 2025-10-16 11:57:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 823133e8-5d48-3a2b-b2fd-3481b75c91ad | -5.73508 | -44.98712 | 2025-10-16 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4141e602-dbfb-31f2-99a2-b5da84f14a29 | -5.87496 | -43.85153 | 2025-10-16 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 824b738e-78d1-3731-9809-9381e6ab6a05 | -6.39995 | -42.52079 | 2025-10-16 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 13eb5d65-8f67-3da1-96fa-f902c6a6d4d8 | -5.46561 | -42.92855 | 2025-10-16 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 81b924e6-9dc0-3737-b9bc-65d6548ce3ac | -6.70248 | -37.99593 | 2025-10-16 11:57:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 5adf3e57-ef53-31ff-9991-8be9c341c0cb | -6.37626 | -38.21477 | 2025-10-16 11:57:00 | TERRA_M-M | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 04bccf25-d761-3e85-a2e6-ca019da6db2a | -6.37073 | -41.50007 | 2025-10-16 11:57:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8244c234-ade5-3972-a4ae-d0acbe8b0570 | -6.53013 | -42.19451 | 2025-10-16 11:57:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c1914bac-c16b-38a0-b625-76e98d4f79b8 | -4.11163 | -42.20583 | 2025-10-16 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 9191f86c-db2f-3b24-ac7e-24e9e3ec734b | -5.30062 | -43.87069 | 2025-10-16 11:57:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8617b702-4290-34f1-9162-f66b7cfb7cb8 | -5.8338 | -42.23351 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| b531ff18-d6ac-332a-b541-4f080ef7a810 | -3.33937 | -42.19166 | 2025-10-16 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1c5531ae-3848-341b-b1fe-4a8c816c71e4 | -5.35478 | -43.74953 | 2025-10-16 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2e627e9b-520f-3407-9a9c-d402023c0165 | -6.03714 | -44.12919 | 2025-10-16 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7750511d-1d17-3e0f-81e0-f58d58256387 | -5.88378 | -42.77684 | 2025-10-16 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 7531277a-6cc1-3cae-bca6-21217a035616 | -6.29234 | -40.55594 | 2025-10-16 11:57:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 487ff452-60eb-31ef-b3bd-ec37f967778f | -6.46331 | -41.8268 | 2025-10-16 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b52f2f44-4d7d-3c37-9157-5eb1ae779979 | -4.01949 | -44.17361 | 2025-10-16 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2587d101-90a4-39d4-a8ac-95e37384c14e | -4.64156 | -42.82016 | 2025-10-16 11:57:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b8f00c5f-5592-3028-8f87-be86fd3b41b1 | -4.91174 | -39.01274 | 2025-10-16 11:57:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 88862bc3-4834-35f0-96bc-708e5706bdc7 | -4.64026 | -42.82909 | 2025-10-16 11:57:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| aa56297c-671c-316f-bc2b-9fab70d8b0cf | -5.86983 | -42.81096 | 2025-10-16 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 25c224d7-2a73-3e7f-8583-9b1148e91cec | -5.49059 | -43.06875 | 2025-10-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dd82bb5b-68e2-3a0f-9b19-92ca728d1037 | -5.87867 | -42.81223 | 2025-10-16 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 27cd6f64-80f0-3f28-82d6-89ff0520c5ef | -5.2726 | -43.23685 | 2025-10-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 66ea4bde-d9d2-3b5a-ad2a-239468558171 | -3.36075 | -41.46383 | 2025-10-16 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 2c05b8b7-ca2c-35aa-80e3-cd5d535e5b44 | -4.38136 | -43.40034 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 999fd4f2-2f4c-3175-8f86-876ae8cac4be | -6.5213 | -42.19331 | 2025-10-16 11:57:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1f5f1217-7a58-3142-b618-4652fe555c9e | -3.85042 | -41.58053 | 2025-10-16 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 01a5f07e-d3d9-3b96-ab99-0198accfc11f | -4.16967 | -40.50846 | 2025-10-16 11:57:00 | TERRA_M-M | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b73c10f2-eaa6-3cc2-8fbd-acce876a1d50 | -2.9073 | -40.4358 | 2025-10-16 11:57:00 | TERRA_M-M | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0c0f2128-c133-3226-8df4-5f405f541990 | -5.67501 | -45.10392 | 2025-10-16 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 3d41fd72-5f2a-3c99-8849-5e135f1794bf | -4.91019 | -39.02407 | 2025-10-16 11:57:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3731a8cd-8fe5-311e-9af5-f615e382aa35 | -3.55757 | -41.37785 | 2025-10-16 11:57:00 | TERRA_M-M | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6ccc968e-fb5e-3e42-a348-8002edd947e7 | -6.40496 | -42.54844 | 2025-10-16 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 038bcc4d-49b9-36df-8236-5220d0473b43 | -5.8199 | -42.33027 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f1ea0109-1277-3ce8-a48b-149c32dc201c | -6.06715 | -41.89159 | 2025-10-16 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| cd3006ca-6745-356f-a8d8-ede8b56934ea | -4.41677 | -43.53829 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 84cfd46f-80d7-369e-a528-9f8bd92ac448 | -5.68677 | -45.11174 | 2025-10-16 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4f167c50-af11-3ff0-b116-9f54095ee195 | -4.30328 | -41.82719 | 2025-10-16 11:57:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 28808bf7-eff1-3f0f-9ec3-d19d2f313eec | -4.58294 | -43.34713 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 20c0dc0e-80f9-3637-b74e-611fe43300af | -4.37504 | -43.38054 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8968cccd-bb1d-399c-b1df-823222bbff41 | -6.06084 | -41.93585 | 2025-10-16 11:57:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 5b23c504-1a04-3667-b1bd-636100cf271d | -11.5724 | -44.0736 | 2025-10-16 12:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 69489d17-ae27-33e5-a169-fd1ba7ec9f9e | -12.9905 | -47.3442 | 2025-10-16 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 8e03809f-8e2d-3070-9a2d-6cdf038d0d49 | -13.9127 | -45.5808 | 2025-10-16 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 239.2 |
| e2fd9d8d-04fa-3cbe-badf-234359428055 | -13.8933 | -45.5842 | 2025-10-16 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fe2ae9c7-333a-3ea7-af8e-454f1b3cc870 | -10.6024 | -47.4178 | 2025-10-16 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a373f1fe-da60-3eb2-af6b-c25fbad0e156 | -12.9909 | -47.3217 | 2025-10-16 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 15f60365-a240-3cc3-951e-d6a96241d1fe | -13.0165 | -43.0547 | 2025-10-16 12:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 00cf0ae7-6aa3-3243-b36c-dbfecb49402b | -13.90618 | -45.58677 | 2025-10-16 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| b6d42f71-a069-328d-b95c-cfe3071ce66a | -13.44301 | -47.9548 | 2025-10-16 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cdbfc9d9-13aa-3ae9-9ce7-a56fb77220cb | -12.30095 | -45.64217 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 372066f0-2838-3429-8b21-77c938d317e0 | -8.18604 | -43.31974 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 5d1f59c5-1244-372f-a5bb-6ae76a3480ed | -13.6391 | -47.88149 | 2025-10-16 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b0e3360f-cf3b-3558-b56b-bb9c6114fe05 | -8.29425 | -43.39619 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 6dd7af71-824b-3a3a-a87c-2ac92fadb254 | -11.94692 | -45.35302 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e9513258-9ba2-3a69-9bea-90a97c583dfd | -7.53662 | -44.28946 | 2025-10-16 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b54210a-abe6-3e10-a69c-54e8cb5bd3b2 | -7.9549 | -44.1417 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 743ccdbf-68c5-3513-9e23-70e387940b3b | -7.35185 | -43.85058 | 2025-10-16 12:00:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dae2799f-fb08-34dd-a32a-9e516dfbfd2f | -12.67984 | -38.28141 | 2025-10-16 12:00:00 | TERRA_M-T | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 7ae88674-1c74-3e65-8f5d-7de9f8c2168d | -7.16702 | -42.52258 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| f1cf32c0-70b8-3aa7-a9f1-97d8abb44e16 | -7.16956 | -42.50494 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b9d624ff-8515-334e-9c7e-91af92369894 | -10.05422 | -39.65928 | 2025-10-16 12:00:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 1cf63fa6-2dba-32e2-82f0-0f3954648e6f | -11.31554 | -45.25324 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e36143ef-a6ac-30af-bdeb-0521d7e1be55 | -10.61838 | -45.2284 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9926d077-cab5-30c7-b1c2-eec7c914be4a | -13.77946 | -43.61127 | 2025-10-16 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 61b7e591-4c7f-3759-b399-efc98e87822c | -10.66839 | -45.32227 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c0fb4472-6b9d-3567-9958-a459d8ad2934 | -8.22268 | -44.01347 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 349e40c8-cdba-3a6c-a8dc-baa05dc62f1d | -7.65396 | -37.64162 | 2025-10-16 12:00:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 6b1610a2-7fca-34b9-84e5-cac9c065cf25 | -9.23825 | -46.90033 | 2025-10-16 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |


[Clique aqui para ver as próximas entradas](README85.md)
