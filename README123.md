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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a22db2f-d508-3f2f-8cb4-5b30f0779883 | -4.45855 | -47.95955 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a29cca8-4e88-3615-a361-18817acb649b | -4.458 | -47.96305 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cae52240-e2f2-39f5-b233-b84e9043cc86 | -4.4092 | -50.8339 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e2d76f8-dc90-30c3-a325-56d8da46ef3f | -4.408 | -50.75353 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccab2b5e-cec9-3c5b-bb56-36aed1a339d5 | -4.39988 | -48.63153 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ce8822e-c877-32f1-b867-103332489a3a | -4.39323 | -48.6305 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34e614bc-e8ce-34b3-bc2c-4b44ac5a6a85 | -4.39269 | -48.63396 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b7aa938-c2cb-3391-bf47-23229e354413 | -4.39126 | -48.70811 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 586d7093-da2e-34c5-914c-8b4895aeef23 | -4.38794 | -48.7076 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b19e205c-ef5d-38aa-a6cf-07eac7c2b8be | -4.38407 | -48.71054 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59e4a174-b962-3f11-9d92-fc8a5abb7605 | -4.38359 | -49.78917 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7978beba-7115-33a6-a462-45098592bf89 | -4.38129 | -48.70656 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 260ed95c-c002-383b-aba5-f2d4fb7be53b | -4.3808 | -49.78511 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79157adf-b904-37c5-9cb6-bdc284cd2e0b | -4.38075 | -48.71002 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fb2f983-7d28-3f81-a199-1c4291949163 | -4.38024 | -49.78864 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f04d5fb6-4323-3103-a6d5-bd9ca10a25c6 | -4.38007 | -48.69878 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 443184c7-986a-316b-ba41-35e278aa7078 | -4.37968 | -49.79216 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f287c235-7b97-3c24-bbc2-bbdc560daa64 | -4.37953 | -48.70224 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82aa57e2-cfa1-3b54-bfbe-e8d4f557f934 | -4.37899 | -48.70569 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bc0f9e9-bfab-38e0-9836-c77aa9cd9820 | -4.37844 | -48.70915 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1b555ec7-dd8e-35f4-9ab7-b031c7095507 | -4.37675 | -48.69827 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ae9be53-49a9-3407-9e94-f0e3eeb54c0b | -4.31987 | -47.70351 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33b73b54-c5aa-348e-9f41-6f7445273ea6 | -4.31931 | -47.70706 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc20cd19-8c6b-3cb1-9a88-3357896fc8ad | -4.3165 | -47.70301 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc535f2c-7c4a-359a-9a49-1fd18ebbfe17 | -4.31594 | -47.70656 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd611530-78a6-362a-a649-40e6337135c2 | -4.29614 | -60.02158 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447afe39-5415-3bdc-8ac5-da4f565da75f | -4.29082 | -60.01588 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf8d2907-3203-334f-89ad-321f33ebde30 | -4.29002 | -60.02049 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d741757e-525d-39de-84a6-3a137b1a4a91 | -4.28801 | -48.63484 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0299fd4d-233d-3865-874b-8e4e10c95ee4 | -4.28747 | -48.6383 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a9da605-f584-376d-a1fd-c9f906d2d5b6 | -4.28481 | -49.46871 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c873c6c-81b8-3294-866b-7f50361312bd | -4.28471 | -60.01482 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38885b7e-2ec1-33f1-b96b-848a57f5ef18 | -4.28469 | -48.63432 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e07c5f-411a-3108-99a2-9927ba6d9b0a | -4.28445 | -44.39636 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f965ab2-91cf-32ad-80e7-9ce487660dce | -4.28437 | -44.39442 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2f24a65-79a7-3de1-8a4d-8e84543234a3 | -4.28344 | -48.62341 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1292c99-74d4-3d56-87a5-bb67a3352d4a | -4.28066 | -48.61944 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d717a0c0-016d-35bf-a829-bb1c8e5db6de | -4.28055 | -44.39576 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89473fbd-2334-364d-9518-ffd45d3d2dc8 | -4.28047 | -44.39383 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7801ee5f-a33e-3046-ad7c-9e6fe7c9c7fc | -4.28011 | -48.62289 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75bbc61d-461a-31a0-8a6d-0ec61abea23f | -4.27983 | -44.40062 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d3193ac-9050-399f-b87d-0555ed36980a | -4.27972 | -44.39869 | 2024-10-09 04:38:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 326b7719-75e3-3e92-a208-4281cddd59e7 | -4.22796 | -44.26525 | 2024-10-09 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98e85f81-eacf-3463-92da-92ed8262ce6b | -4.22723 | -44.27017 | 2024-10-09 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b65ec1e-efea-3447-903f-e780ff1c61aa | -4.22404 | -44.26464 | 2024-10-09 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 396457d5-75fa-34ef-8e98-7517c3c3ce78 | -4.2233 | -44.26957 | 2024-10-09 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a50672d8-550b-36ef-9427-5c1820753287 | -4.20996 | -46.84499 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a006b44-2749-3653-9238-6df7160e8cc9 | -4.20938 | -46.84871 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54aa1d7b-2248-3de2-ace5-207a2f81ba4c | -4.20646 | -48.1427 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4f8f2be-dd2e-3dbe-86dc-afb62c2a11cc | -4.20367 | -48.13869 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 946fbc83-7ec2-3545-8120-4cefad9ebfe8 | -4.20313 | -48.14218 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f887f89-f534-340d-babf-9d9ba37992d0 | -4.20034 | -48.13818 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08096097-dcc2-3f9a-9009-2c823ea92334 | -4.19755 | -48.13417 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5c13105-100d-35fd-a896-82789754030e | -4.18504 | -49.39545 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32660e09-eb52-384b-8d2c-c94737dffe26 | -4.18449 | -49.39893 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 980dca5f-7a40-3ec9-801b-b8613c563fc3 | -4.18171 | -49.39493 | 2024-10-09 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f130ec7c-afa8-3be6-9326-abeef3938c00 | -4.15914 | -51.04357 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78753a4e-ddc1-359c-afbd-0b224a1486e2 | -4.15908 | -48.61827 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 841339ac-b1a9-329a-96ea-58b35404b0d7 | -4.15853 | -51.04736 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31ef666b-203a-31e8-b062-2e7d6022255f | -4.15567 | -51.04295 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e902086a-0433-3dfe-ac75-3a73afd2dabf | -4.15506 | -51.04672 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72879bec-4bde-35e8-bf49-c12e561fbb8a | -4.15445 | -51.05055 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c569c7ab-82fc-3ed3-b20b-9c4616e8afb2 | -4.15158 | -51.04616 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fcd3e1e-cd65-34a6-85fa-2a656dc53c6f | -4.14056 | -47.87094 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6913b2f0-6882-34fa-9379-a9a82a582125 | -4.10702 | -59.88045 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e561ef0-a00a-3c02-9c34-076e5bb27dcb | -4.10623 | -59.88503 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a143c800-537f-39ac-b95c-f9522e831e46 | -4.10096 | -48.25457 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 941c4c20-3161-3f3d-9600-0a15a552b6b7 | -4.10093 | -59.87945 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84061b32-b55d-33bc-bbf3-c91ee07370b9 | -4.10041 | -48.25803 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ff5d3c7-5d5d-352c-818f-32b848065ddc | -4.10014 | -59.88407 | 2024-10-09 04:38:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d87f1ca4-b088-3507-9a82-0617c89e010f | -4.09987 | -48.2615 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a3085a1a-5f59-32c9-9579-ba3313afd7dc | -4.09932 | -48.26497 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e8753692-1fb1-3377-b3a7-15b2aadffd2a | -4.09878 | -48.26843 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 115e6688-1543-39ae-93d6-ac361b0140ee | -4.09817 | -48.25057 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91fc8ccc-9b3e-3b9b-8ce9-2899dcc04235 | -4.09779 | -48.48833 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5e32019-a7d7-3181-af0b-8544be1488c5 | -4.09763 | -48.25405 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b6df9e3-90e6-390a-9228-3d355f44d0c7 | -4.09708 | -48.25751 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2eb473ac-d1d5-3042-9383-02fd6be00378 | -4.09654 | -48.26099 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f3d3929b-e0c3-36e4-b571-954900f0b13c | -4.09599 | -48.26446 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d6ccb74-aa71-3672-a05d-95d224feb96e | -4.09545 | -48.26793 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e19fe1ff-36e4-304f-8f83-11f59c73f82f | -4.09485 | -48.25005 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5800305-eca4-3f17-8409-ba536a884d6a | -4.09455 | -54.43891 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5df02945-1b49-3e5a-ad1d-d02a0270b37f | -4.0943 | -48.25353 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e8d6736-cc0d-3b68-bbed-aa49e069dd19 | -4.09375 | -48.257 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53a9e563-8bd1-3a04-81a2-2e7526b30529 | -4.09321 | -48.26048 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a65d008-0df5-319b-93b4-75e802f43f4a | -4.09267 | -48.26394 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 20c8afa8-0d2c-3764-8b46-c1427ac27bb5 | -4.09212 | -48.26741 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c2916ba-e6f3-30d3-8ef8-de40ef96db0d | -4.09156 | -51.03358 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 600085e5-a7a8-3d85-b6d3-6b0e6164cbea | -4.08716 | -48.27729 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84f2e560-9517-3de0-928e-d58133885d24 | -4.08662 | -48.28076 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ad6b8ed-7892-3a7e-a8d4-aae129dd36ca | -4.08383 | -48.27677 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 668077a1-b598-3e9f-a919-cfde126cbb67 | -4.08153 | -48.24798 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a1efe65-e9d7-3524-b539-014cf1c896ec | -4.07395 | -54.79244 | 2024-10-09 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0fdd902-ee9d-3cf8-a4ca-3e828a15ec15 | -4.06356 | -51.11953 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b098ae17-f1aa-39b0-94b4-29ef514d5281 | -4.06008 | -51.11893 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56dbde26-3d6c-3581-b916-edc4c2fb8c22 | -4.05659 | -51.11835 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ee608f9-1b80-3ea1-a232-1a45715990b6 | -4.05248 | -51.1216 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3425f0cf-55e4-3f01-acce-fbab3963dbf2 | -4.04961 | -51.1172 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 572260ab-ee0f-3ad7-8cb2-2adec791848e | -4.04673 | -51.11281 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b817bd6-ae2f-3155-8604-89692e2b1c76 | -4.01238 | -46.542 | 2024-10-09 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README124.md)
