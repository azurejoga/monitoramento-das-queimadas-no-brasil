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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0383107a-79f7-34cf-bd6d-16ffdfa14c42 | -4.94019 | -45.6692 | 2026-09-08 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e958eb8-a734-36af-b6b1-01a3f1b25a49 | -6.61909 | -44.71872 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1cb56c4e-c535-3950-8b57-8e1976800e86 | -3.24302 | -47.24668 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7d8adf4c-4a11-3fff-8936-55a13538eaf8 | -4.72858 | -48.84312 | 2026-09-08 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1626651-7f97-30be-a206-f2573023833a | -3.77639 | -58.85247 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4f3a9bb-6d45-3242-8976-e1d0e8d4bdab | -3.27173 | -50.0274 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48101a76-fcd3-3c9a-8043-a752487d023a | -1.4785 | -54.84858 | 2026-09-08 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a2a6e69-8f7b-3012-8ce2-c8188a972d96 | -4.34722 | -47.58106 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40b7a70b-88dd-3109-a88e-700db59c06c7 | -3.77014 | -58.85144 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d0ddede-cb4c-3b4e-8ade-143b86ac919e | -3.24634 | -47.2472 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9da33ef-5721-376c-9803-63bb4fb83912 | -2.88016 | -50.45642 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a394d5db-3db8-3dc9-bd11-ef1c4ee3eb0e | -6.61117 | -44.72186 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1f2b4e4-2df2-376b-9759-9830f89a43e3 | -5.91761 | -52.48516 | 2026-09-08 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34588de4-1eec-3df4-96ee-dbc96f72cd95 | -4.98497 | -50.64069 | 2026-09-08 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c0e5e35-65b7-3ea0-b453-f2f36f63d6c5 | -7.3748 | -47.02261 | 2026-09-08 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 896d2f50-c47b-3b4e-a1ef-99b28b9f39df | -2.75113 | -49.47756 | 2026-09-08 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77a8323a-3a44-3553-ab17-461ca934fe16 | -2.97429 | -47.33911 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4d83f38-3dfa-3e44-a4f0-80222616eed8 | -4.72578 | -48.83902 | 2026-09-08 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e4ca02-2558-3ec7-897d-68363ede7da0 | -3.54161 | -48.17994 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c141a0fe-9bec-34b0-b4c6-c192b2a6d557 | -4.82154 | -42.91401 | 2026-09-08 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd08e1d1-7de8-3484-8fca-e6268853c287 | -2.87928 | -50.43885 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4fa9ad-3415-3a0c-9050-2c1f48330d41 | -2.87555 | -50.44382 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40b8272f-0d93-3753-9fef-5b5fd7a5c23b | -4.87286 | -48.90605 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3da28ff7-a9ca-3e2a-832b-1136a21b4450 | -4.34425 | -55.21426 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17089f92-6c06-3b65-aa05-c611e6c471d9 | -4.04733 | -50.87385 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457c10ae-d2a8-3e52-bc56-9b55e6d61d77 | -4.34999 | -47.58504 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9569822-73f1-39f9-8d73-c5941460442d | -3.2397 | -47.24616 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a6c08194-8ad8-3c3e-b123-211a7be9d039 | -6.7632 | -45.48181 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12c47ae6-71f1-3955-afe3-55fd2c2ff6f3 | -2.60547 | -51.2181 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 937a89ee-bd1f-3fc4-b103-25720d1923f8 | -3.26928 | -50.02814 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1fccc15-4df4-371c-881f-79b61e813df8 | -3.94407 | -48.43854 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3002a499-fbec-30e9-b566-0c951d95667c | -4.10975 | -49.06528 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 472ebd03-b9ce-3385-a989-16b64ab8460a | -4.98204 | -50.63596 | 2026-09-08 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69986686-bfcb-3042-bff2-db3c89c6e5bb | -2.86756 | -50.44689 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62cc20a3-1379-3efd-99a8-ccbe6fe9da32 | -7.22648 | -45.10861 | 2026-09-08 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33583c04-a68c-3dfd-b260-21c57506d3b8 | -5.62183 | -44.24945 | 2026-09-08 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdca4b1b-bf76-3b8a-a82b-a79dc6a657de | -7.78178 | -49.6066 | 2026-09-08 04:44:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ad02027-3991-3f2c-b2c8-c9e631d352d7 | -5.84992 | -45.1653 | 2026-09-08 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad112943-3277-3b75-8da9-a8da9df1be86 | -7.66856 | -46.0532 | 2026-09-08 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cbff2224-9494-3a09-9e35-770a2f2d8c22 | -2.87257 | -50.43897 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9eae47dd-82ad-3ecf-9f8d-b6d306e491c2 | -6.336 | -43.35075 | 2026-09-08 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6c3255f6-a30d-384f-8050-e4043abee555 | -3.5338 | -48.18592 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c647b52-13ab-3f2e-ad09-1a9c66bfeb70 | -2.87058 | -50.44616 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4895a7be-a1d0-309f-b67a-8a9015b7c105 | -7.6953 | -44.32179 | 2026-09-08 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b063e19c-7384-363d-b0c1-c429a7ec9afd | -3.36803 | -50.39489 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd72084f-dd08-3557-9957-75a69050e9d7 | -2.87859 | -50.4431 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea98dc0a-f1af-3dde-999a-e0313df30c9b | -3.53436 | -48.1824 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9f97795-85b3-3e0b-bcc8-49c8d2a77faa | -7.56097 | -47.81674 | 2026-09-08 04:44:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a25e81a-cc52-31f3-8684-d542d3b479ad | -6.76259 | -45.48576 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 423d2a73-fab3-3c0d-aa7c-33b32f827c25 | -5.05681 | -44.43851 | 2026-09-08 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2854effd-c2bb-3148-b417-fa6cbfd8cc18 | -5.40878 | -49.11311 | 2026-09-08 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b876631-51ac-39b4-9dc8-8878de418c3a | -3.25123 | -50.82578 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8ddba2ad-1a45-38ff-aeee-d72aaedb0589 | -2.62718 | -46.77507 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2398401-bd5b-33a3-a7f9-077f469396a2 | -7.37254 | -47.01497 | 2026-09-08 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eebc1df4-f380-30c0-871e-798706cbdc27 | -3.55277 | -48.1745 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 530fce2d-f186-3bff-b0d1-7a87d0b15f57 | -3.8906 | -55.82013 | 2026-09-08 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46e17bf1-7fee-31c7-8505-ca75d3081233 | -5.27467 | -49.293 | 2026-09-08 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2f86064-9ea2-31d4-8d33-8501aa993840 | -6.69494 | -47.41734 | 2026-09-08 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a56670df-9bf8-346c-83a7-ef70fc9ec069 | -5.94163 | -51.69782 | 2026-09-08 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fce34b17-2afa-3b47-9eb1-3e2ef43f45ab | -3.24752 | -50.82516 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba0b5bad-e2da-3fd3-92b3-9318053e6b59 | -3.33538 | -53.40598 | 2026-09-08 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4810f576-8e90-345d-b5cb-7c0e553da843 | -5.99595 | -44.37954 | 2026-09-08 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9910ce8-a336-314c-b7a1-583cc96b37d8 | -4.34245 | -55.22512 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20fe1a93-190d-3906-8d8a-af0cc90baed9 | -1.47445 | -54.842 | 2026-09-08 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33fc682f-c431-33b4-8ce7-a2ba6a889946 | -5.62033 | -44.89891 | 2026-09-08 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6539c73-f161-3e4c-9044-0d7c68dce021 | -4.98137 | -50.6401 | 2026-09-08 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ff4a749-380f-32d0-9576-6c4d4764dca9 | -3.46182 | -59.51489 | 2026-09-08 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b484136-ab0c-32cc-9ef8-2e4975993a0f | -3.54887 | -48.17748 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 7346c189-8dfb-3ba8-a7b7-5ebfab120a11 | -6.41497 | -46.60654 | 2026-09-08 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5899ba47-a40a-3bbb-92b4-582dd835062c | -5.27636 | -49.08852 | 2026-09-08 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27cbcceb-a9d7-3983-b62b-61c54472c216 | -6.61545 | -44.71811 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8bf84db-61ec-395e-8cbc-527db320e62d | -2.73601 | -51.3806 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ed5f394-5206-3ad8-8f66-5e8068b4c68d | -4.36353 | -47.77853 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| ccbc989a-0b5f-3bce-adff-3d63399a5508 | -3.85319 | -51.37735 | 2026-09-08 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eccb4bd1-2289-3700-bd0f-675271a0d81e | -3.55221 | -48.178 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 07a64a2c-0b98-3526-8a21-35a0b88664fc | -4.07818 | -48.956 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20a79f5a-2a62-3487-8cad-ea3a14c5d00a | -3.5444 | -48.18398 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| e093c1a9-0247-3867-8a21-0b2d7fc252e1 | -3.32654 | -44.59032 | 2026-09-08 04:44:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| acdf6a01-f52e-3e0d-a9cb-7ab16be144ab | -5.80299 | -49.97941 | 2026-09-08 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3437c5c7-4d63-3ad3-bf1d-88623b45cffb | -1.19517 | -55.7384 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bba5d0cd-9a58-3874-845a-8c78bf4aac8f | -5.84699 | -45.1608 | 2026-09-08 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8dd8b7d-272a-37b7-8b58-f5037e661905 | -5.85121 | -43.83124 | 2026-09-08 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38467ced-70ba-365c-933d-e0ef7fd44f9e | -2.87563 | -50.43826 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8be7cb47-d402-3f44-b748-33e428d48a06 | -2.06631 | -45.98528 | 2026-09-08 04:44:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 657268e5-ddd3-3fe1-96ae-c23e1c70a1ef | -2.87493 | -50.4425 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beeaf023-eb63-3edb-9911-431e6ca043fa | -2.06296 | -45.98475 | 2026-09-08 04:44:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b68b06d-7e71-3d96-947b-ebbb70428ff1 | -3.83374 | -40.10752 | 2026-09-08 04:44:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62b8f29b-53e8-3586-98a0-bf5be22cfd43 | -6.76673 | -45.48231 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61df9136-868d-3c08-ae44-c47d64637ec9 | -7.37591 | -47.0155 | 2026-09-08 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad42fca6-3f2e-335e-8ee1-0ca4da0bf498 | -3.85243 | -51.38202 | 2026-09-08 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74503046-e3ef-3ca1-9e22-9f77345f18a5 | -3.23725 | -50.605 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 109ace92-0126-386e-b8db-04ba649b4d1d | -5.30986 | -56.10498 | 2026-09-08 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 142482a6-663b-3421-8e0e-8f992fa71ce6 | -3.54106 | -48.18345 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 125b7957-a434-34c8-8866-f408cee4967c | -1.19094 | -55.73093 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6d5be69-290b-360e-936c-c0885cd0690b | -3.44873 | -47.27239 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e464c63c-60b3-377e-b12c-b6a4f60f687a | -5.13956 | -55.9691 | 2026-09-08 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e04a69b-8029-3eb2-af50-9954a09fa9db | -7.6732 | -46.04616 | 2026-09-08 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f429ce4-2f40-3097-a9b2-020dbcbc296a | -3.5511 | -48.18504 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd2d68c2-ce63-3020-b7ff-12f6e743e256 | -3.26816 | -50.02683 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1df3c97-d6ff-3f8a-b4fe-cacde7ed7c9a | -2.9798 | -49.26974 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README15.md)
