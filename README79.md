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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af64c726-3e03-3cb1-b6af-9ff5cd2aa6fc | -2.99505 | -53.36378 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a9d8760-013c-3afc-b40e-3cf194b20325 | -3.10887 | -53.10364 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 763cedf2-f03e-39ac-9a72-8290021e7c8a | -3.12533 | -53.26389 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65b0c8cc-a667-3524-b23e-e36ea20249db | -1.59952 | -55.5565 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e7b51fa-b43b-34a8-9733-ad8cb589a0c0 | -1.49663 | -52.96558 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aceb79e5-63d6-3e75-968e-6c03634358c7 | -3.48517 | -53.8027 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 33bf09ef-25bf-3ebb-846a-cf7b9d1e9e37 | -1.14848 | -54.06184 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f103476-58c3-3850-b54d-5f9b73424815 | -1.21901 | -51.74429 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ce397d8-b7e9-303f-8b5c-794730f5f34e | -2.9653 | -53.73408 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e337be4c-e802-37d1-9aee-dbbcb2bd2ed8 | -1.0941 | -53.3739 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08a7b9bf-7ee2-3168-ae15-b878858bf2dc | -2.4637 | -53.70049 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c4c5721-e7c8-3630-ad40-38a2233bbf99 | -1.11416 | -53.22419 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a23e16a-c6fc-33b4-8803-a8f025773047 | -1.33209 | -52.38587 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2d9b681-81a3-30e6-a494-fc5a3fe94d4e | -1.10359 | -52.22851 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bd64e4e-22af-36ca-ade5-366d07006a85 | -2.84932 | -54.02332 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14244aa9-e3f7-33de-a71c-7b4fee5bdcf6 | -3.10282 | -53.80943 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5ba87c-9fd0-380e-95a2-17adf1149cd7 | -3.40779 | -50.66331 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8234b6dd-6a1c-30be-bc96-1abf60144638 | -2.15366 | -46.49311 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8433c6f-39a8-3407-b08e-6afd54aaf1d2 | -2.46463 | -46.55851 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96260365-ae84-33d6-ade9-b4c8c1991e83 | -0.58061 | -51.70057 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9f5a9fb-f767-35cc-b58b-3e4036fd9af9 | -2.79315 | -54.05408 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ace0672-37d1-3a5e-9afa-65d278fef057 | -1.08069 | -53.39364 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19af6d97-c044-341f-9d40-d53cf9dae3e0 | -2.7447 | -54.13258 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d66cfabd-583e-388a-bf2d-2f69b0024626 | -2.45905 | -53.94828 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e7734d-1d6a-3c93-9976-55fc68940be4 | -3.46294 | -53.87922 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1296b0f9-66a7-3b4c-acf8-60d30344fbd2 | -1.09468 | -53.39217 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 768923eb-eaff-3d8d-a955-118b69e9827e | -3.28868 | -53.67421 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08738dc4-9aaf-37b0-9594-6881eef8b03b | -3.05516 | -54.04771 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8381f841-cc1b-3851-b532-8450ea4b1ee4 | -1.15685 | -54.20109 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4df6e1-e157-3557-ba8b-072526bb0770 | -3.14987 | -53.82798 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a72819b-39bd-3453-ad83-fa57cba0129a | -2.84222 | -54.09034 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38d1fb41-36a7-37e8-91ac-f53e83f89b36 | -1.82914 | -54.5324 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6736f06e-b2c3-3797-9963-e2779bacc549 | -2.46375 | -46.56439 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf939025-f5c7-3381-a21e-a0400b434d7e | -1.27929 | -54.5416 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d95c82cd-0779-31b3-8cb7-c5e6258b797e | -1.53368 | -52.66228 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0afa77bc-9634-3387-96e6-27f07d875e34 | -3.8734 | -49.98745 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61065bab-1833-3d10-ab36-01fee5ed120b | -3.24817 | -53.86848 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a95a17a0-ce0d-3012-8013-4d2279784ce9 | -1.21599 | -54.19265 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec8f4393-9996-3739-b4e6-c9a897ffcb25 | -2.76878 | -55.31174 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0c1b069-cde0-3a2d-a6ed-027e7a7135a9 | -3.27327 | -53.41374 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e025d702-8034-33a0-8de1-4b0898e4a774 | -1.35245 | -51.39038 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 092752f2-f609-39ee-8741-e3751517022b | -1.91751 | -52.65855 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd3deb6-d2b0-32fb-b4b4-1d8ce2a5bfc4 | -1.38616 | -53.6465 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4c3c71d-09a6-3aa1-9513-f5171e29c70e | -2.67874 | -46.09851 | 2024-11-30 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fa4e354-d5a6-32f5-a2f0-a8d6e4f2cbc9 | -2.80305 | -53.04993 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec09a118-2c99-3e12-9c0f-c0846d904701 | -3.02908 | -53.41347 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47cf61ff-6b33-34fd-8ffb-3ab505f5688c | -3.22057 | -54.17765 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e629f898-f3cf-387c-af37-91d0ffe19a44 | -4.59288 | -44.70385 | 2024-11-30 05:01:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 972f900c-2b57-393f-9253-e3d519706f5a | -2.87883 | -54.00996 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17594ff3-adce-3647-addf-91bfdf451efc | -2.53164 | -54.02398 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb93fa7-4a7c-3eff-b9e7-7fc59de636a4 | -1.65163 | -52.48792 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 447617a5-1ec4-3250-b68f-a11797c3c18d | -3.25963 | -53.63352 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 18e3d433-bcf5-3f17-bb02-8c62495bdbe1 | -1.70174 | -55.01734 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b80160bd-b7cc-3052-8690-d3732638b78e | -2.57462 | -53.9804 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aec3476-de65-335b-b40d-6eff7450f3cd | -1.99964 | -56.49008 | 2024-11-30 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1640cd6a-1211-35eb-b50b-24846af7217e | -2.3757 | -47.88776 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36c5e660-bc56-3d3b-8258-5b2ebeb8f235 | -3.33489 | -53.22128 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85ec4bd9-d8f2-303e-a3ff-be177cc161e6 | -2.51819 | -48.48223 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac1ff66d-6f8a-3c17-b350-24b96e3012e9 | -3.11276 | -53.7019 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3136206d-6307-33fa-a1d3-c583bdce8a83 | -1.71907 | -55.0802 | 2024-11-30 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fe2f779-8c73-375d-a2b6-61f79514841a | -3.29342 | -54.12789 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73974847-d764-34e8-b5c2-bfc88371dfbd | -3.50816 | -53.78801 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0353cb06-3b79-3c3e-9ecd-e0160c909ce5 | -4.00535 | -54.3345 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee445f2-5832-30dc-a70d-ebecf1a9e69c | -3.12391 | -46.05469 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f85a8de2-991d-3acb-92bb-9e012070f738 | -3.24017 | -50.25113 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f56a4f21-6391-3e74-b7f0-d16ff4f2a37b | -2.23147 | -51.79861 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6519b0a0-f93e-30d5-9ae9-484ed4f73278 | -2.86814 | -53.94715 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e4367d0-46cf-3fab-90c4-a87ee7227adb | -1.1362 | -53.79357 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f3443fa-fac4-3900-a1e8-89dcd4ed8cf5 | 0.83518 | -52.05442 | 2024-11-30 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd0b7725-ba3a-38d5-8a6e-ff1c5355b309 | -3.25344 | -53.62886 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 19b081b4-aca8-3822-a03c-d5d6747d1440 | -3.29232 | -53.82813 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b44af11d-c0ca-3618-bee7-edefadd312bf | -2.04104 | -51.19802 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b469cb41-5e8f-337e-ae07-576a23b438eb | -3.02734 | -52.37973 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1bce190-7f45-3e82-8eba-8a09b8352cf8 | -2.73917 | -54.14601 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4050fff2-8d59-3500-976c-c6637934ca5b | -0.96114 | -51.71587 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25111bc2-6300-3286-8475-a0dac307eb75 | -1.68333 | -45.77992 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0b3d764-3ffe-3a44-9290-63c99fea79a5 | -3.49637 | -53.7972 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 57d091c1-2905-3353-8423-b0af7c43829c | -2.43497 | -53.88354 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3b9ab30-fa7e-3778-add8-83e2cc05c722 | -2.88343 | -54.21458 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 824061a1-a6ec-3c3a-8f04-e57a176bd21b | -2.8098 | -54.03514 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da533a8b-7cf8-3f68-9791-a8aaa378e8bf | -3.11346 | -53.80747 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| edab55e7-8908-3380-b2a9-0eba915ae513 | -3.4993 | -53.84487 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c035dd45-1567-3a3e-8cb6-1deed95010da | -1.19001 | -54.01175 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05b931f9-5a53-3beb-bbf0-38632788a563 | -1.06943 | -51.7599 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16dceaa4-dc5e-3155-8270-1219edddb4e6 | -1.16701 | -51.93957 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e052518-f3d8-38bd-b2a0-9b58f4b44201 | -3.25462 | -54.22229 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 153abe8c-c7d4-3352-a325-7421fd9fb23d | -1.41936 | -54.94096 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d73dc67f-ba57-328e-8fbf-9764c0fe8472 | -2.60085 | -51.82485 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a433d1e-b563-3e9b-9973-f586c14af007 | -2.86321 | -54.00034 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8adf79d-a268-3b79-a716-781b923fb1a9 | -0.09401 | -51.74715 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c854326-a645-33c9-8061-48a43ac992b1 | -1.41621 | -55.25961 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55bbc291-a72f-3c2b-835d-10f1b747bd52 | -3.53844 | -50.17653 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc0f2909-5c90-3c54-b369-91e3ee4c06f3 | -1.22382 | -51.7368 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16306169-364b-3181-a86a-927ef0eabbed | -4.18829 | -54.75921 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08494a6b-18bf-304b-885d-d136417acf8d | -1.57951 | -53.83726 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b3af4cd-dacd-3e15-8ae5-29ae3d58904d | -1.3074 | -51.91986 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4280c745-fad5-31b5-82ad-0cd8efaadf20 | -1.69511 | -52.45975 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 958c7b36-b66d-3783-8e76-af110e464715 | -3.40855 | -50.65847 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 66ebb4c4-367e-3365-b063-fe1d44732ea6 | -3.07665 | -53.91056 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52b2677f-2c03-3e0b-b2ae-f71c2b737c3d | -1.58285 | -53.83777 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README80.md)
