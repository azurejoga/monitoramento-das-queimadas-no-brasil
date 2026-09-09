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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47262bbc-ed3a-3786-9d03-4878bb4726fa | -3.2486 | -47.2438 | 2026-09-09 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f50fbd8f-b55d-3642-b207-4b11bd5c6d1b | -9.6295 | -40.3392 | 2026-09-09 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 3b2841ed-154e-3c9f-a67d-20c43b618f06 | -6.1536 | -44.6675 | 2026-09-09 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0110c664-e604-3080-9cc1-70eadd6ddf4c | -6.1538 | -44.6446 | 2026-09-09 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| eeff2527-060f-3497-87dd-5715f70256af | -5.7758 | -45.0599 | 2026-09-09 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b17cd485-6e47-3535-bf0b-e5837245b8dc | -5.7756 | -45.0826 | 2026-09-09 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| bf138af3-6979-3c23-9ce3-c996fb536544 | -2.9392 | -50.4622 | 2026-09-09 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 04a33257-ddbd-3138-bdd7-22c48daf556f | -5.7758 | -45.0599 | 2026-09-09 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ee79e76f-fc37-3c8c-a33b-2b1e8bae3dbd | -6.1538 | -44.6446 | 2026-09-09 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2af9640d-5532-32b1-b720-39aaa5c949f1 | -5.7756 | -45.0826 | 2026-09-09 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7b57402d-34d3-36d1-9974-857105b5ed2a | -2.9391 | -50.4832 | 2026-09-09 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7c81784e-4215-3c75-a09b-d46df951e986 | -8.84198 | -36.53493 | 2026-09-09 03:04:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 06d76e40-09dd-3b4b-83a8-752de37b09b5 | -8.8429 | -36.53013 | 2026-09-09 03:04:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 85ab7614-c5b8-3a1e-84e6-851b98baa815 | -2.9392 | -50.4622 | 2026-09-09 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| cbf533ec-6f51-303d-8559-fc443ef5c0f8 | -2.9391 | -50.4832 | 2026-09-09 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| eb4721b3-a743-3e3e-ad65-12ab86d4084d | -2.9392 | -50.4622 | 2026-09-09 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 3dc278a4-03bb-3aeb-8346-5265893d99e8 | -2.9391 | -50.4832 | 2026-09-09 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ab821d66-6a40-3e76-81de-6dad8a578214 | -2.9392 | -50.4622 | 2026-09-09 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d2dca36d-525d-30b2-8288-19cc33e17b84 | -2.9391 | -50.4832 | 2026-09-09 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ea0a5286-a19a-3d99-8981-b7ecb81f50e0 | -2.9392 | -50.4622 | 2026-09-09 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 16d13fcc-185b-3768-ba82-696eabc388aa | -2.9391 | -50.4832 | 2026-09-09 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 408692f3-7835-3b9e-a689-75c0583dea1e | -4.29599 | -49.08709 | 2026-09-09 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54292c0f-fc44-3585-be7f-0d9d95358192 | -3.54353 | -48.18272 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 121da911-0a0e-30b6-8c34-f1a29c96a685 | -2.91788 | -41.36541 | 2026-09-09 03:47:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54aeff17-351f-3ed7-a7d9-77b76c5aeefb | -3.96821 | -47.58302 | 2026-09-09 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a93af065-73e7-3226-9295-eac6c4820205 | -3.97056 | -41.51889 | 2026-09-09 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7328afb7-a64d-3cbe-9452-3f86dbce4604 | -3.24391 | -47.24734 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 68e9aa4d-9324-3b5e-9c0c-9ecb0b7b16a7 | -3.24134 | -47.2515 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4dff61fc-8773-3342-afa0-c4fa3bb7a45d | -3.32893 | -42.77417 | 2026-09-09 03:47:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70ad011a-4336-3c9b-8b74-fa28f12514a7 | -3.54897 | -48.18912 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a665ece8-5919-36b5-8975-5f35c87ab3ae | -3.26478 | -50.0882 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 35ffdda2-09f6-324b-b281-cdaba7748385 | -4.30163 | -49.094 | 2026-09-09 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cac9e05-5c80-35f8-bb9b-51b7f25ab74a | -4.86864 | -37.45132 | 2026-09-09 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 76f9b401-82b9-3bc7-9d00-8e406680aea6 | -3.24209 | -47.24694 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9f03f5cd-c12b-3a7b-9119-8434353b16ce | -3.26337 | -50.07334 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39a848d0-6e83-3c60-b040-adf29db99e94 | -3.2672 | -50.07409 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d03be004-9019-324e-8dfd-60b78978b7d2 | -3.98227 | -43.1086 | 2026-09-09 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52c0329a-6324-3116-9a1b-8cf4a11c51bc | -3.71367 | -38.84684 | 2026-09-09 03:47:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ed3f1864-12f9-3529-9c1e-73948ed0500d | -4.49129 | -45.91992 | 2026-09-09 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7719df0-33fe-38cb-9df0-5a5706389bab | -3.54261 | -48.18803 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8972e873-7f24-3b80-b3dd-da933400a359 | -4.29739 | -38.52864 | 2026-09-09 03:47:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ead44239-b7bc-37e2-a0fd-479a917f0015 | -3.26925 | -50.08154 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b6237e6-353a-314f-a2d9-1ab69752f70c | -3.24313 | -47.25189 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 89ef383e-32e8-3e39-a2de-49c6d892afd1 | -4.30263 | -49.08822 | 2026-09-09 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26b5fd8f-e20c-3f8c-a9de-e3ebb598484d | -3.44614 | -47.2716 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d56257-8d5b-3943-b3c4-576885aff658 | -3.97403 | -41.52312 | 2026-09-09 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8386c0b1-2f97-317e-bda7-d6285982f74f | -5.00889 | -38.02789 | 2026-09-09 03:47:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6d91f0f8-0fa5-37e2-82da-ddda2b1686bc | -2.88942 | -40.52378 | 2026-09-09 03:47:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 987e1d05-f910-3f42-87d7-969583dc048d | -3.96741 | -47.58766 | 2026-09-09 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61c60d4a-7ab5-33ab-a50a-e228369933e9 | -3.54991 | -48.18365 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec654970-e638-37d6-ba4a-fcc64393d02a | -3.65541 | -40.34323 | 2026-09-09 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f154bdd1-f2d8-3457-9a48-cdacfedd98c4 | -3.65162 | -40.34261 | 2026-09-09 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0ff1c0b-aecd-31a0-b143-800ac7f7f192 | -3.26087 | -50.08736 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f8f043ea-0e0e-3f05-8aaa-e3eea7d73276 | -4.52208 | -40.55486 | 2026-09-09 03:47:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44e8354e-91a5-3ece-baf1-c81a60a15021 | -4.49192 | -45.91623 | 2026-09-09 03:47:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa51fda1-ee4e-3f18-afcc-e05db9fa4a9c | -3.51956 | -43.25998 | 2026-09-09 03:47:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7de93a9-57c2-3e72-acab-32630edbfb49 | -4.29982 | -49.08899 | 2026-09-09 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5b55412-eb66-301c-afd4-417c163aaa70 | -4.52605 | -37.72579 | 2026-09-09 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 25e2eca3-9325-30d5-9551-356e96a78299 | -3.55081 | -48.17839 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4c398cf-39b0-3575-9c86-bf051e9bbbef | -3.26599 | -50.08113 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 50c96f2d-0214-3d55-a2fc-4ffc0f5d6b26 | -4.46605 | -38.50504 | 2026-09-09 03:47:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c414284b-63d8-3f63-b279-446481c76c0c | -3.268 | -50.08862 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ea1630bb-2e72-31f0-bd76-a9800b5d98b8 | -4.52282 | -40.55022 | 2026-09-09 03:47:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4918d154-fa7b-358f-bc26-e8826c1f553f | -3.26212 | -50.08034 | 2026-09-09 03:47:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0bbd8b9b-48eb-3450-afd3-1340848b3d30 | -3.54443 | -48.17749 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c058fc62-913a-306c-abb6-560fd6c970ed | -3.24813 | -47.24792 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2cc751d2-8149-31dc-995b-2f851b2f080e | -4.46948 | -38.50557 | 2026-09-09 03:47:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 70efb78f-05ba-38c0-9f20-1e2ccf64f67f | -3.24738 | -47.25246 | 2026-09-09 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d38f1db5-d820-34e8-bf77-9f01a68320f8 | -7.13076 | -42.12264 | 2026-09-09 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0d4d5445-3279-38e9-a7f6-7d355cf5b91a | -9.69304 | -43.50617 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c203409c-12ff-3a8a-9913-4bca6b521911 | -5.76577 | -45.07494 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 322f16ca-6afa-3cc5-833f-f9f7833bda79 | -7.19612 | -43.6133 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be0bf715-a447-3ecf-823d-94d7ac8d6a69 | -7.19726 | -43.62693 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dedc8c93-154a-3517-b29c-b7b925df24cd | -6.25513 | -47.3468 | 2026-09-09 03:49:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e3606cf-cbb3-38bd-9344-5977111451f1 | -5.77736 | -45.06771 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2ebcf62a-6f3d-35fd-9799-5722ff13f80a | -11.00445 | -45.08598 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f56b9d17-0561-3120-8c33-c424abefbee7 | -5.71662 | -46.18955 | 2026-09-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df5e946f-1571-35b4-888e-a245fb65a96e | -11.42786 | -47.68668 | 2026-09-09 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 766fd809-3190-3a1e-9192-b2e72f429e45 | -6.8323 | -39.40459 | 2026-09-09 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62483a5c-3384-3163-9a56-bef6639280a6 | -9.7788 | -43.46339 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6d0fd2e-a7f3-3caf-8d58-4bf0b159f136 | -9.16375 | -36.64448 | 2026-09-09 03:49:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83078e99-53e5-31e8-893f-695c3201b921 | -6.83515 | -39.40901 | 2026-09-09 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc20fd84-4c9b-3d24-bffb-bf9699beb2f4 | -7.68531 | -44.31804 | 2026-09-09 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8874e10-0d6b-352e-a28e-45674575ed93 | -7.52309 | -45.92987 | 2026-09-09 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67b02eed-12f9-3698-b4e3-077f06e7d4b0 | -6.83293 | -39.40073 | 2026-09-09 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93dfe055-abea-3a27-b6be-86c38b12fea9 | -9.74812 | -43.51488 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1bbea085-579d-3730-afef-95b821974cdd | -10.74901 | -45.97407 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5dce608d-ab76-38d8-a716-a2f80a70105a | -8.43702 | -36.41952 | 2026-09-09 03:49:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7de02719-3bc5-3524-a601-eb554029ac1c | -8.21336 | -46.00887 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c013c2-69f2-30ec-a78f-272a104d847e | -10.35655 | -40.56073 | 2026-09-09 03:49:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e30dbf6e-b920-3419-b6af-a07f87f6eb2f | -7.68614 | -44.3132 | 2026-09-09 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dc35532-3d35-32e3-b441-49b5098f26c8 | -9.69913 | -43.47055 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d03f8ab-a279-3ba9-b1d3-104adfabca82 | -5.77081 | -45.07566 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a5bd484d-fd8f-3375-a29d-9af538e0148d | -7.19463 | -43.62223 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7a972b9f-d49d-314a-a054-269b780e31fd | -9.70403 | -43.46727 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80a933ef-8db8-3dcc-9c15-1fa86fe488a3 | -6.8647 | -46.01784 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ca57d4e-7d87-3595-8554-e896f377a230 | -9.70335 | -43.47127 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 098ed488-3d35-3a35-b34a-1d5f7a17a263 | -7.52935 | -45.92452 | 2026-09-09 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99edaea4-8566-39cd-a798-a8c18d5b24c8 | -11.4361 | -45.15537 | 2026-09-09 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6ee2da8-5c42-3fa8-b819-46bea3d3af20 | -9.71573 | -43.47676 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
