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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2db9de92-691c-31e0-9c4a-520444112da5 | -2.7216 | -47.971 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bffbf228-442c-3993-874c-57e57e296fbe | -3.23645 | -51.29854 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcf15499-2622-3b81-b175-4950ba423735 | -1.21486 | -51.78897 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 609d389c-2a86-36f4-8e7e-be417f43516c | -2.84931 | -46.61895 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c524055-7588-3b60-a49f-ca3ddb44bb32 | -2.20015 | -50.53852 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f4e937b-d2a4-3876-a864-6873a8dde4c5 | -2.88794 | -50.41953 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30c4266d-c5c6-33b7-aa92-2c8dac34a75a | -3.8079 | -47.79591 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e1af9fd7-a5bb-352d-857f-4cb116cb269c | -3.46154 | -50.83199 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31ee14d1-e495-3172-bc34-99d5997560c5 | -0.83329 | -52.55956 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecc71ad9-7019-392b-bebd-bc702c66859d | -1.62281 | -52.58883 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb364b54-11ca-33b3-bcd3-ff6a7566a51d | -1.78765 | -53.61284 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5ff7a50-2087-36cb-934c-61ea27dd374c | -3.06238 | -44.34054 | 2024-11-21 04:29:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf0a5c3-95cb-3baa-8f18-709ca37ecc35 | -1.19721 | -51.76743 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6ad852a-a653-3b66-87ef-0092e6215efe | -2.90475 | -48.31987 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b7b5468-e806-3935-8b80-0190d9e5536e | -2.67236 | -48.28444 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d366e521-087c-3555-9b17-78cceaf4337c | -1.24225 | -51.74852 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5334491c-cc0c-39e8-86e8-db82fc3b5daf | -1.65099 | -52.67181 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4adac35b-e43e-3cea-959b-04ecb5261714 | -2.68113 | -46.24497 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7917a83f-22a8-3e37-ba51-c4c3e821a190 | -3.18245 | -46.54306 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1acafd4-6d06-3f21-a9c2-82a712459c47 | -2.39787 | -49.04752 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 080acf12-8947-36a8-9103-5df714ed145c | -1.10675 | -53.12524 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92140270-eb07-3ffa-97bb-bc76dedaff9b | -1.12956 | -48.3485 | 2024-11-21 04:29:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a439227-7eb0-3c73-a208-6c984a0d8223 | -1.45797 | -52.66915 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c307677c-b31c-30d9-9fe0-67a17a717f64 | -0.27319 | -51.39051 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fcc9989-1e31-3320-90be-5791e7dc8bd8 | -2.36919 | -49.00404 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42325df1-8015-32d6-855e-6e0e49dfde0c | -1.26878 | -51.60545 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b1ac8e7-fb0c-3835-a0c2-8172fc165ef9 | -2.6882 | -46.19979 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c71f5780-a149-3d6c-8be3-b3016979f8e6 | -2.7466 | -54.01155 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cef2152-1f4b-3b8d-9645-18e23242eb19 | -0.42452 | -51.56895 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45841822-bff9-3058-91e1-3c2f022d5bd6 | -2.92035 | -53.06887 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ad0e717-6f8e-3d00-bd8a-8088ce88ef13 | -1.78228 | -53.61684 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83e7a135-b740-3f68-a91d-89b6e4a07f3a | -2.6618 | -46.60698 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5729afae-b9e6-38b8-bf05-77bcde611688 | -2.90532 | -48.31628 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af5915b2-1dfd-3245-92fc-7c881205e390 | -2.26318 | -48.42071 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 564b3d52-b87b-3974-9090-89ba03fff0b3 | -2.01039 | -48.76027 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98ff9c49-97ca-30c6-860e-2a6f706a13c2 | -2.26376 | -48.41707 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c95a57f3-c1c2-3a82-a328-989a846d94cd | -2.66051 | -46.55022 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5fab3a8-93d1-354a-998d-17fd09eb7ea7 | -2.70035 | -47.97493 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 932233a8-cbb9-3f94-aa56-8423beb66e58 | -2.9173 | -46.8308 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5ba06bd-2db6-316c-b5cf-becf13796b50 | -2.61866 | -51.80926 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 590da98a-644d-3ea4-a62d-e5734f7eb4d8 | -2.30392 | -48.49441 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d7dd7a-a5a0-3bbc-a531-f976507819ec | -2.66232 | -46.23851 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb8b93bf-5af8-302a-b05c-7285c2e02042 | -2.2405 | -49.20005 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d65c00e7-2725-342f-8750-1441bb6ac308 | -3.59031 | -43.63461 | 2024-11-21 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0195c5e-13d4-3c54-b9df-27e61499efc8 | -2.40168 | -48.60713 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b0b8874-4227-3cd0-ad12-f9909431eae8 | -1.71332 | -48.63076 | 2024-11-21 04:29:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22c4c2fe-7184-3a5a-a5c3-b354db47bba5 | -1.72807 | -52.38757 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a57b9f9b-19f2-3913-90ea-b90e3139125a | -2.63369 | -48.06974 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 800403e8-2ecb-3af5-ae39-b1474d119f4b | -2.19771 | -49.26497 | 2024-11-21 04:29:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daf367d5-7bbe-370d-a2b8-f0996d6aea24 | -2.51895 | -48.34921 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f413ab10-7fa2-3ba3-acd6-6e861bc0e520 | -0.77561 | -51.75844 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bb0afb6-3f29-3c39-97d1-74dee1ae45b6 | -2.58231 | -46.55215 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c98956f-9788-3f7b-bd85-5fc58919d6d9 | -3.94129 | -46.71133 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a7f02be-4eab-3972-aaa7-0a4e443b8128 | -4.06713 | -46.83712 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61477a2d-61d3-3f60-bdcc-7e0300b8cfee | -3.10431 | -53.09967 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fed0484-ac20-3dc9-ab1e-6de3cf651d6b | -4.07045 | -46.83763 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13cb2e6c-11c0-3b28-a51a-7220d2a74da6 | -1.23053 | -51.74292 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afdcd269-1c04-3989-9f3c-d9980a1c37f3 | -4.00484 | -43.2483 | 2024-11-21 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c1e4682-c301-3d90-ae6c-1e381975dd22 | -2.14895 | -48.91577 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c871fcef-b2b7-3370-bf1e-818ef13337bd | -1.23405 | -51.7472 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82ce8ef4-6e83-3a51-be92-8f81b9f101b2 | -2.69311 | -46.08641 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a405d5e-f6f0-3197-9559-efce4e46b4c3 | -4.06768 | -46.83365 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f552ab4-a57c-32c9-8124-f95d1b5c215c | -3.28974 | -49.18677 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35aa1703-ceb5-344c-9173-cb9376c3125a | -2.1568 | -50.49235 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08084ddd-856c-32e6-bc8f-e5bc082dff36 | -3.08386 | -45.96394 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 376ad128-6842-3c04-9d64-150a0dd49d43 | -2.94699 | -48.33754 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02c66db1-e5da-3f3f-947b-0ab03cfc0126 | -1.486 | -51.13349 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c0953ab-b7a3-3247-8dce-32927cbfa01b | -2.67247 | -48.28773 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 941bf1b9-00fc-31cf-903f-2fa298470b36 | -2.94229 | -45.19423 | 2024-11-21 04:29:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf90b114-a2a5-35cf-84de-500f0900270e | -3.16179 | -50.58097 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb0f1bc0-7776-3bed-9269-b43accd7a620 | -3.10947 | -50.20351 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0df6c70b-69b2-39ed-a179-0b6a4701524c | -2.15221 | -50.91471 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f0c859e-ee94-30b5-8f9d-76411efbe497 | -3.94173 | -48.14674 | 2024-11-21 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b88280c-8156-3a2a-b299-87d98dd0ed61 | -1.6185 | -55.4077 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb007737-8d72-338f-9e18-71c7940db5f5 | -1.49575 | -52.54502 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc3d572a-669c-36d9-8e6a-5b54df370d38 | -1.13298 | -48.34903 | 2024-11-21 04:29:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc7872c-0139-365c-ae93-6bc5680e0737 | -2.55782 | -47.41815 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fc4d7e6-4d9d-3c9f-833f-472aadd9e2d8 | -2.04433 | -46.3799 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aec004a-5247-38ef-843e-e752820669a2 | -2.45707 | -53.69982 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2651f66d-76a9-318b-a19f-875fd81550a7 | -3.48352 | -50.31336 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fb6ddf2-f493-3c59-a3b4-4b9d3e5036d7 | -3.33897 | -51.16109 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8024dc6d-7ce8-315b-ba19-f1bdeaf50e53 | -2.02108 | -54.52637 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0e5cd58-1aeb-3924-8744-f05827283a0c | -1.64611 | -52.6093 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88c0a53d-75c4-35f0-ba54-250011d0bd25 | -2.64056 | -45.76559 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad19c289-facb-3d47-b67f-f66a78c13b83 | -2.55802 | -48.16757 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73226559-e1bf-32da-97f5-6bac63e29641 | -2.78876 | -45.95069 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd60c31-a260-3f7c-a3eb-630af347537e | -0.17208 | -51.50785 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 860ff943-ef17-3a62-8102-0b8861ec2798 | -3.09791 | -53.2199 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c70a5b4e-a022-3e12-90ed-cc197391ffd2 | -2.54564 | -48.18029 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 195b56f0-5e2a-3e29-bd8f-d5b006bdd886 | -4.03832 | -46.22279 | 2024-11-21 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b5781b-7938-3431-a4d0-b51737911435 | -2.83601 | -49.53797 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bf39c78-5d4e-35ab-ab37-57e1c99f9424 | -1.21299 | -51.74757 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9182595c-5811-3730-b190-306a226c23f8 | -3.32184 | -51.56466 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85506009-193d-3a02-882b-416d09d97d5e | -1.3914 | -53.5775 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2acd6e98-bcd5-309c-b3d2-99e714e27ea2 | -3.25468 | -46.43007 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fdd2bae-a29b-361e-bddd-8025f5840438 | -2.72868 | -47.97905 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c68ae1f-9695-353a-a05f-0aff57ab21a2 | -2.15181 | -48.92009 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 468e08b3-0b33-32a2-8629-d609829c791c | -2.76944 | -52.11124 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f18fa88-f23d-3070-bf6a-ced8062538bd | -3.46179 | -50.83458 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b86e33a-4011-3876-8808-2bf6d0ed55f2 | -1.18902 | -53.72087 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README37.md)
