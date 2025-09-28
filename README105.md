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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a8831e0-d8c5-3481-a639-d7b306ce2e56 | -12.2825 | -44.0804 | 2025-09-28 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| affb05f0-a589-325c-b89a-14bce0611c7c | -13.6122 | -48.0787 | 2025-09-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a2c9bc41-f539-3023-8933-534a5843658a | -5.1885 | -43.7495 | 2025-09-28 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 692d4b39-230f-3c70-bd14-436cd2d83e8b | -11.4413 | -44.9998 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| dff0e1ee-beaa-3bef-add3-d5eaa7cc7575 | -12.9717 | -46.2846 | 2025-09-28 14:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f84cbd22-2ebe-3c3f-9a8b-12af2d68b8c8 | -11.979 | -47.0847 | 2025-09-28 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 206.8 |
| b2afaa2b-1268-3185-a149-f15e4cca74d9 | -6.6192 | -44.9493 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 68b676cb-3fac-3b06-840b-704a8817ab56 | -6.3 | -45.0205 | 2025-09-28 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 28d7595e-f4c4-3471-a808-523482587f08 | -11.4217 | -45.0257 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| b647005a-491e-381f-9c4a-4d0715957b61 | -7.3849 | -47.0157 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| f053a55c-9208-3ddd-b86a-745f87ec9063 | -5.7001 | -43.0604 | 2025-09-28 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| a654b8d2-2f8e-3208-9590-f86f4fabce71 | -8.9185 | -46.0889 | 2025-09-28 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| bb8a07b9-f5bf-3a4d-8d3a-65579f9397b4 | -5.3057 | -43.1599 | 2025-09-28 14:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 021b520e-ed90-3a28-8aee-db99a0085ef5 | -7.8823 | -44.5594 | 2025-09-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 00da42fb-cddf-34f9-972f-604499f46185 | -6.6178 | -45.0859 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 6eaaa594-bba5-3f62-94f6-5c5b7a301b3f | -9.106 | -47.6275 | 2025-09-28 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 14405f6e-67ae-3241-ae1c-7c8131fe535f | -11.4083 | -46.9597 | 2025-09-28 14:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| d40d79f9-5c09-3951-a82a-6c4074085388 | -9.4194 | -54.697 | 2025-09-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 60c1b178-2054-37df-bce4-9c975387cb07 | -8.6798 | -47.0738 | 2025-09-28 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5d39ef5f-9cbf-35e6-bdec-1ec1c23ce91a | -14.885 | -45.5708 | 2025-09-28 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| bcf8019a-3b6b-3e6e-af07-de544b6b62cd | -8.8759 | -45.0274 | 2025-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 492.8 |
| 30e114b9-eaa5-3f13-ba69-3899133c1052 | -6.3154 | -43.4548 | 2025-09-28 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4772a470-bafb-348f-a7c5-c8e7621a48e3 | -6.6005 | -44.9509 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 92f9ed5d-6114-387b-afc6-5707c2ed7e8a | -5.6273 | -44.9343 | 2025-09-28 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 66c6eeb0-8a7b-324d-957c-125e9cc85c23 | -5.2869 | -43.1613 | 2025-09-28 14:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1f182c88-0642-38b9-8de3-ee4308df799e | -11.9456 | -47.936 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 977f799f-206e-32c1-b8a3-67901494c0d1 | -12.9543 | -45.185 | 2025-09-28 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2f604218-4ed9-3b0f-a95c-bf3011b06b14 | -6.5991 | -45.0874 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 98898cbe-fced-36cf-b7c3-d4d84088257a | -8.8393 | -44.9399 | 2025-09-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3b35fbce-2808-3172-b4aa-042e521e361f | -14.885 | -45.5708 | 2025-09-28 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 2411baff-2005-399a-8658-5bc0ac23bafb | -12.0222 | -47.9259 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 556cfec9-296e-3497-a8b0-fb0b2cdad86c | -7.1571 | -45.5158 | 2025-09-28 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6d0be1da-5b14-3ac4-ac48-20043623f805 | -8.2668 | -45.4564 | 2025-09-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 21b10233-ada5-3015-8ed8-dac41e836410 | -13.6122 | -48.0787 | 2025-09-28 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9f5ac026-56a8-3559-aae7-72a46fa2a90c | -10.8627 | -47.7852 | 2025-09-28 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 64332e34-23f3-30f4-95e9-6e73a02a6902 | -6.6005 | -44.9509 | 2025-09-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| ad42133d-ec7c-39fe-a6bd-d7b89c5cf084 | -9.0874 | -47.6074 | 2025-09-28 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 67d2b94f-f9f1-3e9c-8f8f-7d3ffdc6fefd | -15.9076 | -46.2139 | 2025-09-28 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4596d12e-f995-39a4-a966-3d1d81b6a7b4 | -9.1099 | -45.8879 | 2025-09-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 839a60b8-127a-38af-b98c-5b4c2374e4c2 | -6.6983 | -42.7646 | 2025-09-28 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 361994f6-1e84-37f3-bb58-85041b137012 | -12.7637 | -50.4921 | 2025-09-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 70fb4943-fd95-360b-9770-eccc57fde216 | -11.9648 | -47.9335 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 7c143c13-1965-3f17-934c-33bca7860999 | -9.3013 | -45.7082 | 2025-09-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 272152b8-aeac-3243-981e-bd54bd144018 | -9.106 | -47.6275 | 2025-09-28 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 6317c192-99a2-3902-a744-f93f3098641f | -13.2777 | -50.6846 | 2025-09-28 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 31659eac-9e07-3a63-aa3d-9dfb5eb18f21 | -9.1102 | -45.8653 | 2025-09-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 89b9f2f3-b401-3adb-ba8c-c3c034810a02 | -3.8458 | -40.4342 | 2025-09-28 14:20:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 6fcbc0e7-4cfe-33e0-885e-cba1da84fcab | -7.3661 | -47.0173 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9350dee9-43b5-3d07-a7fd-d84ed1e7f022 | -6.3351 | -43.3598 | 2025-09-28 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 788b3fab-684b-33d2-8f33-40598bc4be10 | -11.9637 | -48.0001 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9a0ead04-1053-364e-bfbf-db8d4b533fda | -11.9456 | -47.936 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 267.1 |
| fcabf974-8c11-3b32-9a16-6b44744c85af | -5.6273 | -44.9343 | 2025-09-28 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| f0298e84-419f-321a-9368-e002e01bbfe4 | -5.3057 | -43.1599 | 2025-09-28 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 17f76b62-ec4d-38e8-8cfa-10e293ef6851 | -13.6267 | -47.3152 | 2025-09-28 14:20:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b0f7a1a5-0693-3b54-bb1a-fcc83608df49 | -10.0373 | -48.5381 | 2025-09-28 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6c7cf8ae-2f44-3126-87df-14e1ef115663 | -11.964 | -47.9779 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 70bc0c73-d7c7-33b5-b3cf-77d8a802bade | -5.1885 | -43.7495 | 2025-09-28 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 82d3de0b-a988-321c-9ec1-bd4136936661 | -6.3105 | -45.8999 | 2025-09-28 14:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| eaac7192-2d39-3608-9cf2-c71e712064f2 | -8.2419 | -47.5352 | 2025-09-28 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 180136dc-466f-3ed2-98f0-2cb0480cc699 | -9.3331 | -47.56 | 2025-09-28 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 46e5c6c1-66ed-31d4-b491-201e37a2b2d8 | -13.7889 | -47.9181 | 2025-09-28 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 655d2bb8-6105-3b4e-8e12-2221c7838bd2 | -8.8759 | -45.0274 | 2025-09-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 391.5 |
| 1586aa00-5c66-30cd-a8f7-10847f2e8eb1 | -5.9076 | -42.9268 | 2025-09-28 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 5eafd024-fcff-3c6a-8368-daaf20801806 | -8.2859 | -45.4317 | 2025-09-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9b8b1d44-e9b0-3d3d-b46c-465d33ada14f | -9.7643 | -47.7786 | 2025-09-28 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b06e6117-c529-3d30-8bf3-38d5ed16941c | -11.946 | -47.9138 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| edae62ba-2b97-36a2-aee8-11e4b6a25a1b | -14.576 | -48.2417 | 2025-09-28 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 882bf93f-9611-3326-bef4-1cd8e756c523 | -11.9824 | -48.0197 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 51a949ce-62c4-3e57-a5ba-d437bd2e401c | -15.8879 | -46.2177 | 2025-09-28 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| feb52e75-02f0-34ad-837d-d53f8463a468 | -6.5065 | -44.9813 | 2025-09-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e8b68b91-b28c-359f-bdef-51b8a4000201 | -12.9363 | -45.1184 | 2025-09-28 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0a296353-db8a-327c-8ed3-0718be4f797b | -7.5447 | -46.1115 | 2025-09-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| eb5dce4e-d1b2-3578-b84c-2f564f78d6ca | -10.9137 | -45.7375 | 2025-09-28 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 7922c157-fe68-3660-b2c1-a4910feb385a | -5.6275 | -44.9115 | 2025-09-28 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 22a8d38d-52d2-36ad-bd57-a5142447661c | -11.3842 | -44.9849 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 2ca76fb3-8fd5-3c05-b542-e5978ff2cd7c | -11.3846 | -44.9618 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 039b235c-ef3a-3748-a8b3-1de53a44fcdf | -13.7704 | -47.8763 | 2025-09-28 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f14bc829-0ade-3a42-8a55-8e3433183ff6 | -11.3658 | -44.9413 | 2025-09-28 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 290642ec-bc15-3402-91b2-0ec7f1be2234 | -4.4013 | -44.0755 | 2025-09-28 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 311.3 |
| 77840c31-0f3c-3ea8-8e63-edef876c9634 | -14.8845 | -45.5941 | 2025-09-28 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| d693590b-0e2d-3ddf-b8a5-646cef99e6c1 | -12.0177 | -47.0569 | 2025-09-28 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e2fe30ec-5166-3f7f-b17a-564c5c656df4 | -11.9986 | -47.0596 | 2025-09-28 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a00dcaa9-9bd8-399d-9106-6b803d28cfc1 | -11.9464 | -47.8916 | 2025-09-28 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| cfbf339d-2c1a-33de-8b33-d777cb18d2f9 | -9.3016 | -45.6855 | 2025-09-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ea7150ef-f64c-350a-87aa-dcdc0bbd09eb | -12.8972 | -45.1479 | 2025-09-28 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8152019c-9ebc-353f-8b72-e9a9d88c3729 | -14.7851 | -45.6818 | 2025-09-28 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 218.0 |
| c3330edc-5be9-3196-9f1a-f9f207156f54 | -9.2824 | -45.7104 | 2025-09-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d550376b-6f4a-3b76-bab8-e8513679c10f | -9.9585 | -43.5752 | 2025-09-28 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| fa891525-8716-3b18-bf04-f0320e148d09 | -5.2869 | -43.1613 | 2025-09-28 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7d0d37d0-d733-3c47-9860-6788f3921be3 | -12.6917 | -46.8708 | 2025-09-28 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 488bc249-4033-3944-b65f-f59d98e50a2d | -18.1778 | -53.3239 | 2025-09-28 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 75395937-ea01-3a7c-bd1d-700feb663611 | -9.9581 | -43.5987 | 2025-09-28 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 71150cd7-d9d1-3269-b74f-54add479b479 | -12.6495 | -51.6797 | 2025-09-28 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d56c97e4-ce14-3b7e-b672-409feb5ec4f4 | -5.9074 | -42.9503 | 2025-09-28 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| edcc1d6a-73f1-3ed0-8e66-865327b4ee95 | -8.6442 | -43.9931 | 2025-09-28 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b90aee9f-02fc-3de1-b403-bac4fd3272e5 | -14.7846 | -45.7051 | 2025-09-28 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 495.4 |
| 610ab487-c63a-3084-9869-010d0fa15c92 | -5.6462 | -44.9102 | 2025-09-28 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 7f091264-3039-32b9-9f86-349dd18c45b3 | -7.1574 | -45.4932 | 2025-09-28 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e234ca15-072e-3f82-a7dd-b5bece8a338c | -9.4196 | -54.6767 | 2025-09-28 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 224.3 |
| 6e50104e-a1cc-3590-bd48-3b60db70249d | -5.9006 | -43.6744 | 2025-09-28 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |


[Clique aqui para ver as próximas entradas](README106.md)
