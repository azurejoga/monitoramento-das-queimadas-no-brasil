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
| 5b03e827-7802-339a-8af3-7a6839be0d9e | -9.0036 | -65.9412 | 2025-10-22 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 6956d5e3-ea66-34fa-93d0-14b594daa30b | -7.9403 | -46.0076 | 2025-10-22 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e7844f76-ce50-3f66-afb5-f906448e3a9c | -8.9851 | -65.9232 | 2025-10-22 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c7d0f042-4b04-3d8d-8d90-e2679c588b60 | -2.2527 | -51.9108 | 2025-10-22 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 9004bd91-6677-37ad-b719-a29267ea0018 | -2.2343 | -51.9317 | 2025-10-22 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ed6e4af7-7c12-344b-a36c-af7715600f83 | -9.0221 | -65.9407 | 2025-10-22 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| cc45ca48-664e-3f61-9ca8-84fdd701254d | -3.824 | -50.7678 | 2025-10-22 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 99658f7e-1976-3fa1-9571-0d641be0e3a4 | -9.0036 | -65.9226 | 2025-10-22 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 84844a8e-0e06-39ca-82c1-66dbaffae1c3 | -3.5346 | -49.4521 | 2025-10-22 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d82df6b3-90af-3c2b-ad55-b2beea79b70e | -4.4806 | -49.0936 | 2025-10-22 00:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 4d265a03-acf0-3bd9-9a48-fefcf5a3c9b7 | -12.8139 | -48.6362 | 2025-10-22 00:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| a26003f9-d8db-332f-b399-4874d20efd9b | -9.0037 | -65.904 | 2025-10-22 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 840faf08-aea7-32aa-bee9-3ea8029892f5 | -3.5161 | -49.4528 | 2025-10-22 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8225aa69-cb9e-3c20-9303-3696e32045a7 | -2.2527 | -51.9313 | 2025-10-22 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 965b5db8-03fb-3c2d-9369-f4466e7058c2 | -3.4438 | -41.8564 | 2025-10-22 00:00:00 | GOES-19 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| c4fe56d7-2e63-30db-870d-15fdd79c210e | -9.0222 | -65.922 | 2025-10-22 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| be8a3bc6-c117-33f9-b44c-380179f2a5eb | -12.8331 | -48.6336 | 2025-10-22 00:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 0cad743a-b495-3582-8ec6-d625895c7171 | -21.60697 | -46.0571 | 2025-10-22 00:09:00 | TERRA_M-M | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| d559dae6-1186-3b98-8dd5-ab5335e2fc07 | -21.90123 | -50.67639 | 2025-10-22 00:09:00 | TERRA_M-M | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| af13fde1-0c6f-3491-bb4d-d625ff6248cd | -20.98283 | -47.19828 | 2025-10-22 00:09:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 68759fb7-83fa-3d90-b82a-931323781f1d | -20.98473 | -47.21558 | 2025-10-22 00:09:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 68566d89-d0c2-304e-9b80-366e4fb8afe7 | -20.57043 | -45.88945 | 2025-10-22 00:09:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 47c0e395-8d35-39f6-a7f8-5e5b127f6d87 | -20.61028 | -45.81222 | 2025-10-22 00:09:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3cbc4070-bc45-3e5a-bfc1-a3e47eac6c47 | -20.97298 | -47.21627 | 2025-10-22 00:09:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 54df890a-0176-3a91-af77-5a1de70cafb1 | -20.61179 | -45.82536 | 2025-10-22 00:09:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1d75f56c-7824-32b3-83b2-843060bb28ca | -21.61157 | -46.06494 | 2025-10-22 00:09:00 | TERRA_M-M | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 85561a29-f42c-3b9e-8ad2-6792b7710cd2 | -4.4806 | -49.0936 | 2025-10-22 00:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4098cb2d-2b6b-344b-b866-702fc1f54bc1 | -2.2527 | -51.9108 | 2025-10-22 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 5e8ebc37-63ed-37b0-9d84-6404a9577c7d | -9.0221 | -65.9407 | 2025-10-22 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 549f803f-184e-3cf7-820c-f464a8fced38 | -9.0036 | -65.9226 | 2025-10-22 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 224.5 |
| 1d33a59f-31f4-3c67-8317-529a6bea566f | -8.9851 | -65.9232 | 2025-10-22 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7d6fc7e6-0794-35f2-9637-29e35ecbb571 | -3.8056 | -50.7685 | 2025-10-22 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 694475dd-24da-3a0c-bb49-d08c8c709ffa | -3.824 | -50.7678 | 2025-10-22 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 14c5aaa8-6ac5-3822-8399-61f3da04dbb2 | -9.0036 | -65.9412 | 2025-10-22 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 96f888ce-613d-35d8-b13b-52070417049f | -2.2711 | -51.9309 | 2025-10-22 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2d1eef13-395b-3ff1-9ad3-bd424d0f5d5f | -4.4621 | -49.0945 | 2025-10-22 00:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 18e9dbfc-2584-3ca8-94a9-9b71d7af2b82 | -9.0037 | -65.904 | 2025-10-22 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 48e89883-f0e8-30f6-8638-288526e2b384 | -3.5161 | -49.4528 | 2025-10-22 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ecb47250-1e62-321a-97bb-f989c09ea2ac | -2.2527 | -51.9313 | 2025-10-22 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| fdcad5b3-dc9c-3aa0-8cf9-d75f034e1652 | -9.0222 | -65.922 | 2025-10-22 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 841802a3-fc9a-3bcb-bd6e-03c3bd55b1f2 | -12.31782 | -47.84174 | 2025-10-22 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0c5a3145-9589-399f-93a2-e92ffd4127bc | -12.31616 | -47.82817 | 2025-10-22 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4afed314-8d72-3b8b-a6b5-b13ca3b2cc40 | -12.81547 | -48.64568 | 2025-10-22 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 82f986f3-06dd-3264-9e13-695116c91b26 | -18.15132 | -52.98653 | 2025-10-22 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 41b52a30-c188-3da9-a28e-5b9e90b2502c | -18.15334 | -52.97929 | 2025-10-22 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| ed562a7b-f639-31c4-a2da-9dc8261d7149 | -12.50959 | -48.57699 | 2025-10-22 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f4fe124c-3881-3717-8463-e7205a24dcee | -12.53364 | -51.32619 | 2025-10-22 00:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 88f0f999-f96c-3847-ab48-3edaea7777fd | -13.4646 | -48.82225 | 2025-10-22 00:11:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 4d81c8ab-e0cd-359e-a8e1-6759d60a56ea | -18.64883 | -49.08471 | 2025-10-22 00:11:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| db1551a8-3dac-306b-ba76-d2635eded447 | -12.53431 | -48.58992 | 2025-10-22 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6cdc5e13-672d-38e2-9bb5-a50cd26eeba9 | -13.4666 | -48.83918 | 2025-10-22 00:11:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b8acd62b-6b76-310f-a5ce-f1d8d9b6acfd | -18.65103 | -49.09093 | 2025-10-22 00:11:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 963cfa6f-45cd-3c0a-a073-4769f97ef6a2 | -19.16063 | -49.1289 | 2025-10-22 00:11:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d413be01-61ae-3ad1-9f6f-89d7e24bdf87 | -6.64225 | -43.61425 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 54fd99ca-5c2c-3c52-b9ad-fbc3c44364d8 | -4.387 | -43.30589 | 2025-10-22 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 319322f0-2aa6-3abf-b228-56ec516aa7ae | -5.65834 | -38.3025 | 2025-10-22 00:13:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| ebf79105-704f-3b6c-9620-e7524fb4aa88 | -4.93006 | -40.88515 | 2025-10-22 00:13:00 | TERRA_M-M | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8e1b43b2-9742-3fde-bfd3-382a24e0f8d4 | -7.49067 | -47.03712 | 2025-10-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 36061e75-6116-3259-8307-6f6ec3f0a6ca | -7.88637 | -44.54026 | 2025-10-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c5e45f2-a05b-37bb-b1e1-360d11a476a9 | -5.91889 | -42.68009 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 05b0b801-45c3-3942-b9e6-c7dc726f8fa3 | -8.21379 | -45.78408 | 2025-10-22 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf7e6fe6-ebeb-3781-a9be-3d3bb7a908cd | -7.48928 | -47.02677 | 2025-10-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 739e7ff8-9b3d-3769-b651-36dc584709f3 | -7.94686 | -44.84776 | 2025-10-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 76aefcf3-1408-3ee9-a375-de0c16933b68 | -8.21505 | -45.7934 | 2025-10-22 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5bc9b7a3-e57b-3309-b1b8-424a355ed9ab | -7.35624 | -44.7696 | 2025-10-22 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9cb3a1e2-28f8-35f0-98b4-4f4561728544 | -8.22534 | -45.80145 | 2025-10-22 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6f5c9faa-bd59-3d80-9ade-5f54bacc768c | -4.38837 | -43.31565 | 2025-10-22 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b5206882-8ac5-3ef3-84ab-4509d7a5b068 | -7.15864 | -44.99922 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70b446fa-3d82-3cbc-870f-9600b4429394 | -7.88515 | -44.53141 | 2025-10-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d913344-efd3-3820-91af-2bf7720dcc8b | -6.67297 | -43.76819 | 2025-10-22 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f27609a-1e65-32b8-b15e-a63d5d17c95f | -5.06552 | -40.47906 | 2025-10-22 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 08ecfccc-931b-34c2-ba30-e968add6fb93 | -4.8331 | -42.11498 | 2025-10-22 00:13:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 58954150-b22f-34a7-98e3-da99ce216b41 | -8.02373 | -40.82021 | 2025-10-22 00:13:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| fd6a1598-5021-3ff5-ba76-65fa788eff23 | -5.66157 | -38.32359 | 2025-10-22 00:13:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 4aa49785-8420-3029-b04a-1b7eb58cf095 | -5.3565 | -48.1138 | 2025-10-22 00:13:00 | TERRA_M-M | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76f36dd4-7cc9-3ca2-8ba7-a4788e5fdd1e | -4.86152 | -42.88605 | 2025-10-22 00:13:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7a316960-dba0-33a2-abae-0068f162ae5e | -6.65123 | -43.61294 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6b28594b-83fc-341c-8917-a217a73f459c | -6.64995 | -43.60381 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d52ada13-d16a-3429-97a9-a21ce4ff5422 | -8.02229 | -40.82661 | 2025-10-22 00:13:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 0543ac14-1b28-3ed2-ba4a-b8484956c225 | -7.15742 | -44.99036 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c459e45-dac9-3f1c-bf3e-f9a359423448 | -8.22807 | -45.75377 | 2025-10-22 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ba13eb7-0039-3343-b660-298cfa8605cb | -4.451 | -43.24081 | 2025-10-22 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 57444ab8-7fe8-3226-8288-b2103b7d0278 | -5.44155 | -47.60594 | 2025-10-22 00:13:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 103377f7-5f76-3131-880f-1559aad57434 | -8.02549 | -40.83241 | 2025-10-22 00:13:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4948cf7c-6716-3a77-b4f3-b65724994b64 | -7.93803 | -44.84901 | 2025-10-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e3ce8b30-c514-343f-9e19-aff318052415 | -4.39627 | -43.30457 | 2025-10-22 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| cb5ac977-3b31-30ad-826c-15b2aa895393 | -8.2266 | -45.81076 | 2025-10-22 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ce277f32-6e91-3053-9e02-156c7de89a4d | -7.84676 | -45.25012 | 2025-10-22 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0e337ee-e5b9-3496-93d7-c0e2de1b56ec | -6.55278 | -44.02222 | 2025-10-22 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d29ce696-e333-3ccd-9d23-29a388354b96 | -7.94563 | -44.8389 | 2025-10-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 69a096f9-6aaa-3e8d-9de2-22a6f08787fd | -4.86008 | -42.87596 | 2025-10-22 00:13:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b1bc1ee1-6969-3fec-baed-fb861022d3ce | -6.64096 | -43.6051 | 2025-10-22 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c2be2094-3b79-3810-a28c-22275efab656 | -7.9368 | -44.84014 | 2025-10-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 08a6270a-6d06-3f45-b235-ba2036db97d9 | -4.28412 | -48.25818 | 2025-10-22 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7a094bf9-01cb-3699-8053-aea5a039150b | -3.5171 | -49.44873 | 2025-10-22 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 5e40b041-0803-3e2a-abd7-352d8b358e8e | -4.70329 | -48.1204 | 2025-10-22 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d08d5442-faad-307e-a5d5-b772cfde37a7 | -2.92876 | -48.29322 | 2025-10-22 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5dd1d9ee-3328-3b37-a1f0-f6f1c79af4d3 | -3.71566 | -47.63451 | 2025-10-22 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 8ab32216-0c9d-359f-948f-9779de6c5ff2 | -4.21434 | -48.80606 | 2025-10-22 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ee1bf3ed-75f5-3777-84e3-fb3ca775f394 | -2.25118 | -51.92464 | 2025-10-22 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |


[Clique aqui para ver as próximas entradas](README2.md)
