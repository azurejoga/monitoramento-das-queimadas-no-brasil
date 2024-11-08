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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d7cf88c-a52c-3eb9-a919-46362a85f723 | -1.5348 | -52.1489 | 2024-11-08 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c44c8156-f3e3-31d1-a7a9-1c20a7963454 | -4.1379 | -44.4109 | 2024-11-08 13:50:00 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 149533ca-194e-36d1-a48c-efa173b5b81f | -1.7366 | -52.3712 | 2024-11-08 13:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1694897a-5dc5-3594-ba21-537d190e1477 | -1.7366 | -52.3507 | 2024-11-08 13:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f2669d40-8fe3-3df5-8d46-5dd8588de649 | -1.7183 | -52.351 | 2024-11-08 13:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4f5fea4e-4cb5-3e6b-9258-3c9fb9ccdb9a | -2.1765 | -46.4417 | 2024-11-08 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 11ce694b-60e0-33f4-9b18-e31e3913d577 | -6.9591 | -41.3539 | 2024-11-08 13:50:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 09044e6b-a1ce-3a05-a424-87d276a6ceb5 | -6.9591 | -41.3539 | 2024-11-08 14:00:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 45cca81c-d21b-33a0-8050-ae0557694f17 | -3.0865 | -50.5625 | 2024-11-08 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 243.0 |
| bbb6a47e-a606-3bc1-a33d-3386eb41397e | -3.1021 | -51.291 | 2024-11-08 14:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 15063b57-602e-3101-a243-a1d273dde63a | -1.5347 | -52.1694 | 2024-11-08 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 8829e710-d75f-39d8-8139-7dc9ae79ba2f | -5.9384 | -43.6482 | 2024-11-08 14:00:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0ef786be-05d7-325e-a952-2ad4a5ce24aa | -1.6543 | -47.8315 | 2024-11-08 14:00:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1bb82911-599f-38b0-9307-256a3d403c5a | -2.3061 | -46.5046 | 2024-11-08 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e48ad23c-3764-37f6-a545-2a53e7b53abe | -2.3061 | -46.4825 | 2024-11-08 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 6a266178-e42e-34f5-b129-84bd7ad8e004 | -1.6534 | -48.2204 | 2024-11-08 14:00:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7fdaf230-4ad9-3e33-b718-ab896038353a | -2.2876 | -46.483 | 2024-11-08 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 177840dd-390a-3723-94a1-777832150d7a | -5.4359 | -43.2673 | 2024-11-08 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| dcc287f1-ff4d-344f-9520-c08fd170423a | -2.0805 | -54.7076 | 2024-11-08 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 03136bea-5dd1-3ecf-a603-faab39e878c2 | -4.4417 | -43.6348 | 2024-11-08 14:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 29b045ce-b300-3b13-8c39-440ee8c9e864 | -6.9974 | -41.3016 | 2024-11-08 14:00:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 64c9106d-c14d-312c-a66e-9c95160d30a4 | -2.4365 | -46.3019 | 2024-11-08 14:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c898b040-0dbe-3d2b-8092-ed6ca6998054 | -1.5164 | -52.1491 | 2024-11-08 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 94e3960e-0a7b-3379-9620-c30d450e023a | -10.2243 | -42.4476 | 2024-11-08 14:00:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 27b9367d-a881-3400-9a47-04e805892d4b | -8.9516 | -41.0493 | 2024-11-08 14:00:00 | GOES-16 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 1c6c537b-db6e-3053-b415-f1cbfb2da3ef | -8.9706 | -41.0467 | 2024-11-08 14:00:00 | GOES-16 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 83.7 |
| f834e358-9f4c-3010-85e8-a916b1359dbd | -7.1077 | -41.5562 | 2024-11-08 14:00:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| fe6ab83b-7f7b-39fa-b6ca-38e4d42799d7 | -2.8659 | -50.3176 | 2024-11-08 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 773f06db-1bc6-3b58-8cf2-4c442006e1e8 | -2.4382 | -45.8349 | 2024-11-08 14:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 595db241-54bc-305f-a02f-ba56fd011e6b | -2.1765 | -46.4417 | 2024-11-08 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 899887fb-1c78-30ff-b9a1-97e632bc2d54 | -4.7224 | -48.9751 | 2024-11-08 14:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 28e7e8ea-ebd7-3ddd-9019-c04fa19c3251 | -6.9591 | -41.3539 | 2024-11-08 14:10:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| f4fb828d-bd3d-3d4e-b844-91b48390f535 | -5.8679 | -43.1644 | 2024-11-08 14:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 29ceeacc-d0fa-34f3-a294-07b4f1c28a14 | -4.4417 | -43.6348 | 2024-11-08 14:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1bb45e75-4f5c-3c4f-bb2a-37cc50438792 | -5.4359 | -43.2673 | 2024-11-08 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 3123d892-93d7-31e7-92ea-96d3b582cb64 | -1.6534 | -48.2204 | 2024-11-08 14:10:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e2911b6e-7e45-3dca-b923-b10377c29805 | -6.9974 | -41.3016 | 2024-11-08 14:10:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| c7a3960f-14d1-38d5-b852-5ad432115492 | -5.5439 | -41.6741 | 2024-11-08 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 0ce01116-42e4-35f6-8def-7584181540c2 | -2.4365 | -46.3019 | 2024-11-08 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 989f3383-0594-32d8-bf62-e64b9ceabf12 | -3.0865 | -50.5625 | 2024-11-08 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 218.6 |
| b3fc417c-b6eb-3295-bb8f-b2e716f63db4 | -1.7183 | -52.351 | 2024-11-08 14:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| fc8f9aff-1b7a-3312-802d-f16bd105bc43 | -7.1077 | -41.5562 | 2024-11-08 14:10:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 955367f6-af94-3ac6-89d9-a5d2ea464c56 | -1.5164 | -52.1491 | 2024-11-08 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 549b6821-ca10-30df-8188-4e3e077931ee | -3.106 | -50.2896 | 2024-11-08 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0b53c33e-9e3f-3167-9c22-718e827b4d17 | -0.6712 | -51.7055 | 2024-11-08 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 581b5236-2539-31e0-879a-aded91cda667 | -2.925 | -49.3449 | 2024-11-08 14:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 761acc04-3d3f-3b08-9511-b919d3dc5436 | -1.535 | -52.0053 | 2024-11-08 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a974a31d-c7da-3f58-a510-bbe47d02f7b0 | -6.9424 | -42.8126 | 2024-11-08 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 0044d08b-aac7-3d46-9c63-3a99ec86a163 | -10.2243 | -42.4476 | 2024-11-08 14:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 85.6 |
| f049fd64-ac97-3c75-b486-fa360f22bd02 | -5.7473 | -42.0166 | 2024-11-08 14:10:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 8bfd3ec2-fe29-3e14-b3fb-c457513ef627 | -0.9102 | -51.7655 | 2024-11-08 14:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 12fed085-fe28-3418-9e3c-43ca854c0275 | -2.1765 | -46.4417 | 2024-11-08 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1e60b50b-a0eb-3b2a-98b7-a223c152c11c | -5.5437 | -41.6981 | 2024-11-08 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 2f0745be-9268-3c21-ab81-cddb43363536 | -1.4707 | -47.2257 | 2024-11-08 14:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f8dd4056-4d6b-3e79-be86-38869228a91a | -0.6711 | -51.7261 | 2024-11-08 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 05327af5-eb14-35e2-9ccd-9be32415d01a | -2.2864 | -46.8357 | 2024-11-08 14:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0e54bce1-5824-32b7-8fbb-701af24fbbf1 | -2.4382 | -45.8349 | 2024-11-08 14:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 923da55f-accf-348b-a7d1-081ef82d9b4e | -3.068 | -50.5631 | 2024-11-08 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 1c1dfd2c-9ba8-31a0-9daf-26118c2b923c | -1.5352 | -51.9436 | 2024-11-08 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c4441630-9321-3bfe-afcf-89ca892a8d78 | -5.7473 | -42.0166 | 2024-11-08 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| a6df4e36-400f-3140-87df-2c744df9e36c | -1.5164 | -52.1491 | 2024-11-08 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| dd657b90-f49e-33ae-97d9-e9dac0b90056 | -1.6543 | -47.8315 | 2024-11-08 14:20:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 701e1d9a-7787-3452-bbbe-04b9dcfbe8b8 | -2.2864 | -46.8357 | 2024-11-08 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1685ccac-b67e-3af8-aafc-ea02e85b29dd | -3.9485 | -48.1508 | 2024-11-08 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| cc6f5ea9-9d71-3faf-96bd-5638d007a916 | -5.5439 | -41.6741 | 2024-11-08 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 87e15e3e-0f4c-343d-be70-5a3954e2e424 | -5.4359 | -43.2673 | 2024-11-08 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 4330e5ae-2078-3010-9afe-cb7d6987107a | -3.0865 | -50.5625 | 2024-11-08 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 248.1 |
| c3236c43-26bb-377e-a1d5-b3091cc0f904 | -6.9424 | -42.8126 | 2024-11-08 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 334fee6a-c0b5-3886-a71a-3cd6d7bc628f | -3.5875 | -42.8655 | 2024-11-08 14:20:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 10ec7d82-0f52-3c64-ba2d-959d593c576c | -2.3052 | -46.7472 | 2024-11-08 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cc5b1363-8fae-3608-8fc2-6d78fb3c34db | -10.2239 | -42.4717 | 2024-11-08 14:20:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 3695ddaa-d2fa-3164-966a-93a115169f5e | -0.6712 | -51.7055 | 2024-11-08 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a9b6c86c-79a7-3591-8212-fd21fef2b484 | -3.106 | -50.2896 | 2024-11-08 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 60540d76-2e26-3348-ac9c-68893beb6d67 | -2.2505 | -46.484 | 2024-11-08 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 8f85fa78-1449-3b40-87ce-c72dad52b59c | -6.9974 | -41.3016 | 2024-11-08 14:20:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| d76bf4a4-f024-3177-bc04-64bf00d86f44 | -5.59 | -42.7871 | 2024-11-08 14:20:00 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 78759d3c-0c8b-3a80-aaaf-4ec7e54c2b5a | -0.6711 | -51.7261 | 2024-11-08 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 95.5 |
| a4ccfd70-97df-3f90-8870-c45caf614a82 | -7.1187 | -40.6309 | 2024-11-08 14:20:00 | GOES-16 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 7bd7786a-a960-3326-9648-565cd6bebfc3 | -2.4365 | -46.3019 | 2024-11-08 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 847171ab-0697-39ab-a5b4-f37ec017092f | -1.535 | -52.0053 | 2024-11-08 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5718f343-7a3b-3125-b4fb-ffa24d7e5113 | -6.9591 | -41.3539 | 2024-11-08 14:20:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 796bbc61-e502-3377-9555-8697f73bf22f | -2.1765 | -46.4417 | 2024-11-08 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 8c873b90-da61-3226-8d24-374de1c20294 | -2.2691 | -46.4614 | 2024-11-08 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5d124ada-8a76-38fe-a9e8-cb5ac7fba23b | -6.9196 | -41.5028 | 2024-11-08 14:20:00 | GOES-16 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 440f9294-3847-3e18-ba4f-0f32ff71f6b5 | -2.3053 | -46.7252 | 2024-11-08 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e40d4824-11ff-39b0-9a1a-480568937ad2 | -2.3061 | -46.5046 | 2024-11-08 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 06a7eee2-4aee-3f45-b9b8-3286c0b34109 | -10.2243 | -42.4476 | 2024-11-08 14:20:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 8f0f9925-fa96-36a7-a695-a9c043c6210d | -6.9007 | -41.5047 | 2024-11-08 14:20:00 | GOES-16 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 1ae98492-64bd-3123-80a1-44cf11e78f40 | -3.068 | -50.5631 | 2024-11-08 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| b5504e22-e289-3aa8-a2f9-1b9c0c9667f0 | -1.8569 | -48.1519 | 2024-11-08 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| eaff2487-ab0f-33b0-b272-16956af5ae0d | -6.2208 | -41.6651 | 2024-11-08 14:20:00 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 5a67defe-6cb3-3c35-8cd5-b6282c8d236e | -5.5437 | -41.6981 | 2024-11-08 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| fa27c53a-c217-3042-a4c4-84234de32a7c | -6.7975 | -42.3053 | 2024-11-08 14:30:00 | GOES-16 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 6161a603-8f84-3a72-abfe-beeaa905a05c | -1.857 | -48.1303 | 2024-11-08 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| fd2fbf1b-fdab-3188-b764-1668aafb3aa3 | -2.4382 | -45.8349 | 2024-11-08 14:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a7d26ca4-ef0d-301d-8d5a-47b7be2df4da | -3.5875 | -42.8655 | 2024-11-08 14:30:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c00f87f8-31f4-39a4-b915-808785dc9bfb | -2.3053 | -46.7252 | 2024-11-08 14:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| dfb2bbd6-1bbc-36d3-b13d-3abcb21c0daf | -0.6712 | -51.7055 | 2024-11-08 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 084a2a9e-6ab2-34c9-a9a8-8d275e27eeac | -7.1077 | -41.5562 | 2024-11-08 14:30:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 10baf912-8761-335e-9fc2-4c1442cccc12 | -1.5352 | -51.9436 | 2024-11-08 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |


[Clique aqui para ver as próximas entradas](README42.md)
