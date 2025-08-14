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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2320fed-e973-3f19-980b-c4ac15369453 | -10.3362 | -64.457001 | 2025-08-14 01:31:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4151734d-a70c-3a98-acc7-c58a233d73d7 | -9.6911 | -65.684196 | 2025-08-14 01:31:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d794c4a4-7f9e-3f0e-b89e-a985ea81a30b | -9.1539 | -59.675201 | 2025-08-14 01:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 742ab7fc-5e3d-3630-b015-40bf9abd1d6e | -7.6067 | -63.5047 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 940890ca-886f-3742-ac29-87bb05b91257 | -6.8948 | -59.144199 | 2025-08-14 01:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb1e490b-b982-3eae-8b43-e2caedf97b48 | -7.6187 | -63.512199 | 2025-08-14 01:31:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 657023f7-ac63-3132-8d60-82a4fd1823bb | -9.5721 | -40.3475 | 2025-08-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 7b8e7055-266b-3d15-afdd-3cd2d0e1b9f5 | -5.9899 | -44.1528 | 2025-08-14 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8e2a0853-500c-37e5-8001-292f064664d9 | -6.0807 | -59.9465 | 2025-08-14 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| afa978e3-b667-35b9-9d0a-4cdc0f3806bf | -9.553 | -40.3503 | 2025-08-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 159.1 |
| 1a7224fa-df63-3eb1-8cfc-2a66afd075bb | -9.1522 | -59.6578 | 2025-08-14 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a8cac9e1-fbf6-3770-9d0d-970a9b246372 | -8.5208 | -43.3298 | 2025-08-14 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| b39aa651-bd85-39dc-ba1e-16ad8c4f94ab | -6.0992 | -59.9267 | 2025-08-14 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| da49d94a-3f06-35b2-bc3d-86fec5be3eaa | -7.8775 | -61.8063 | 2025-08-14 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3cd7a7f7-7d9a-3e6f-9719-74d14e471ef5 | -8.5211 | -43.3063 | 2025-08-14 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 62b34ae5-dd86-3fbb-818f-8b2d4874fc66 | -22.6767 | -47.4647 | 2025-08-14 01:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 847752f3-910b-3b71-a3c6-6a99e4d8c9d4 | -7.8774 | -61.8253 | 2025-08-14 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f31df4aa-26b4-3372-b4de-34f208550aa5 | -8.1877 | -49.0202 | 2025-08-14 01:40:00 | GOES-19 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 16914371-30e8-3e9c-be3a-494571161edb | -6.0991 | -59.9459 | 2025-08-14 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e12d1a2f-c02e-3efa-9b92-2bb76c0ad2ae | -7.6287 | -63.5154 | 2025-08-14 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 60037890-0482-3aad-8255-0186792a24d0 | -7.6103 | -63.516 | 2025-08-14 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| eba36fcc-6af7-3c23-83ec-3f963dbdb536 | -8.5211 | -43.3063 | 2025-08-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 378083c8-77b6-3db3-a54a-e313a9af44ec | -9.5534 | -40.3254 | 2025-08-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 5944e86c-7a9f-38b9-aead-feccbb12412e | -6.0807 | -59.9465 | 2025-08-14 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d448cfef-adbb-381c-ba5d-72fe5965f538 | -7.8774 | -61.8253 | 2025-08-14 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ba6dfe11-245a-39a0-bd0e-1bf053af2ed1 | -7.8775 | -61.8063 | 2025-08-14 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 474377fb-84f6-3898-bd2e-eaa53b014efe | -9.1522 | -59.6578 | 2025-08-14 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1179c03f-bfe7-36f9-8af5-655372a53549 | -9.553 | -40.3503 | 2025-08-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 355.7 |
| d7906c95-6542-3c03-827e-9f182a3b8695 | -22.6774 | -47.4407 | 2025-08-14 01:50:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6718b88a-580b-3a52-b3b4-2264a17a2803 | -8.1877 | -49.0202 | 2025-08-14 01:50:00 | GOES-19 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 97aa617c-48b1-363f-8af8-efa8503efd1c | -6.0991 | -59.9459 | 2025-08-14 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 6c268efa-fd18-3a0a-9e26-d34726bb51cb | -7.6103 | -63.516 | 2025-08-14 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9b772772-cac8-3280-83dd-c389166c63e5 | -9.5721 | -40.3475 | 2025-08-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 163.6 |
| 4173b5fc-51d8-3bea-90c5-26917e2bf12a | -9.5526 | -40.3752 | 2025-08-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 9a6a00c3-0d63-3d6e-9c65-3fa77b11b852 | -6.0807 | -59.9465 | 2025-08-14 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 06caad10-4d56-3b87-93a2-1073ef8cc806 | -15.1066 | -55.4209 | 2025-08-14 02:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1e52ac49-159a-39e9-8cdd-ee1dda912d34 | -8.1877 | -49.0202 | 2025-08-14 02:00:00 | GOES-19 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 82ba4584-8695-3b53-bfae-8e74a4cdce17 | -7.6103 | -63.516 | 2025-08-14 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9b869d42-b9f1-3e34-aa8c-001fedb51fb9 | -15.1063 | -55.4415 | 2025-08-14 02:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| cdff413f-2315-3482-a3a2-9fd9834ec3d1 | -9.5721 | -40.3475 | 2025-08-14 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.5 |
| f5a52464-2b29-3230-a91b-83a82d2bfa97 | -17.0634 | -51.7767 | 2025-08-14 02:00:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 64d69e68-df1c-3df5-a523-d8a43e2cd29a | -7.8774 | -61.8253 | 2025-08-14 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b0be7546-9f95-385b-a227-ea5077542a60 | -22.6767 | -47.4647 | 2025-08-14 02:00:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 52.1 |
| b661fe54-5cdb-3f21-a323-4845be75a7f1 | -15.087 | -55.4438 | 2025-08-14 02:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 761e5c6c-3b10-34fb-9f7c-fafa1e1b9404 | -7.8775 | -61.8063 | 2025-08-14 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9c9be38d-191a-3521-81f9-cc5d5502e9b8 | -6.0991 | -59.9459 | 2025-08-14 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2b223ee7-27ef-3588-8e7b-c807f15784a0 | -15.0676 | -55.446 | 2025-08-14 02:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 69f92030-3ceb-326d-9463-854d35c73f78 | -7.6287 | -63.5154 | 2025-08-14 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 27f904df-5e67-36cc-8c68-93d9e16411e5 | -15.0873 | -55.4231 | 2025-08-14 02:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 216.7 |
| 40ea6c0c-19fc-3641-acf7-75029dc630f0 | -9.553 | -40.3503 | 2025-08-14 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.6 |
| b8b122bd-4035-3c41-ad4e-2a08a43ae158 | -8.1028 | -61.2069 | 2025-08-14 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ba05c2d1-aa23-3c75-9658-0679bae161d7 | -8.5211 | -43.3063 | 2025-08-14 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8b3d00c2-0e8f-356b-8a35-6feaa0c3e67a | -15.0679 | -55.4254 | 2025-08-14 02:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| a2ed4d73-519d-3b09-b864-b0875ee602be | -8.5208 | -43.3298 | 2025-08-14 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| ca45fba8-2f31-3277-bbc9-109bd19cb61a | -9.1522 | -59.6578 | 2025-08-14 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c933cd84-1dde-34b1-9050-487a5f6bbe6e | -17.0629 | -51.7984 | 2025-08-14 02:00:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 7a8f6a51-7278-38e9-ae4a-a5cbc6d3526a | -7.8775 | -61.8063 | 2025-08-14 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5333f691-89d9-3de8-a390-7ce88695d1ec | -7.6103 | -63.516 | 2025-08-14 02:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0ab7087e-03fe-3aa7-9d02-18e0d22ca184 | -17.0629 | -51.7984 | 2025-08-14 02:10:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 330a537f-a082-3b44-bf40-2f6b67d6d51e | -9.1336 | -59.6588 | 2025-08-14 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| cd0cadc8-5a28-36a6-b21c-7b3910ca9f85 | -8.5208 | -43.3298 | 2025-08-14 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| e676addb-eaf5-3c5f-bace-b59028707558 | -16.3153 | -52.9201 | 2025-08-14 02:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| efe80360-7c65-3d06-8547-ccc44dddfdea | -8.1877 | -49.0202 | 2025-08-14 02:10:00 | GOES-19 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 3ea8b471-0808-3723-90e4-2b3bd12133e0 | -6.0807 | -59.9465 | 2025-08-14 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0f635c28-c9fb-3480-8c12-ac12f096ba1a | -8.1028 | -61.2069 | 2025-08-14 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| cbc0451d-3a1a-3d9e-92d7-d1a95eb738e7 | -8.1689 | -49.0218 | 2025-08-14 02:10:00 | GOES-19 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 88ac602b-b335-36bd-9683-c44da990ae43 | -6.0991 | -59.9459 | 2025-08-14 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2539aee6-e928-34a6-ab90-016a900b715f | -9.1522 | -59.6578 | 2025-08-14 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f46ca623-82c6-3b30-87b5-2532d0b52484 | -17.0634 | -51.7767 | 2025-08-14 02:10:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 720da481-b02a-36cc-982e-959025573971 | -2.9106 | -48.2971 | 2025-08-14 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| eafd63de-d3d3-3f36-887e-e0f01f5792d4 | -8.5211 | -43.3063 | 2025-08-14 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 33160ba4-8842-32b1-9152-6e33e044a8be | -7.8774 | -61.8253 | 2025-08-14 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b5490e01-f0f0-3361-b88c-5068342e5039 | -17.0629 | -51.7984 | 2025-08-14 02:20:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 279e2134-99f4-3ca3-8756-a56806d3027e | -8.5211 | -43.3063 | 2025-08-14 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 58e121c2-4239-337b-9e6a-0ef83dcbb44f | -6.0807 | -59.9465 | 2025-08-14 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7ef34680-3b50-31a6-afd9-d69740644976 | -7.8775 | -61.8063 | 2025-08-14 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f22f4020-00a3-3bb3-9cd9-242fd2a14d2b | -9.1336 | -59.6588 | 2025-08-14 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1854e3a1-f687-3090-b22e-405bf38078bf | -17.0432 | -51.8016 | 2025-08-14 02:20:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 605e50bf-4b95-3eb3-bd83-f2e45ddf157b | -6.0991 | -59.9459 | 2025-08-14 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 544be872-c032-37e9-9776-c68d75b1870c | -9.1522 | -59.6578 | 2025-08-14 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8d5da707-c8bb-34aa-8829-9d0912b7ddc6 | -22.6767 | -47.4647 | 2025-08-14 02:20:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 24a7c44d-f4b9-341f-a052-76685d389aaa | -7.6103 | -63.516 | 2025-08-14 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9ab23fa9-8174-3172-9769-b20a8b200171 | -7.8774 | -61.8253 | 2025-08-14 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3d2188c3-3875-312f-866f-4cfb2d6fe537 | -22.6774 | -47.4407 | 2025-08-14 02:20:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f77922fe-1968-36c6-89e1-773c4a73d38e | -7.8259 | -61.855301 | 2025-08-14 02:21:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f00856d-1d06-37f6-8ff5-b25981563b2b | -7.5542 | -63.5397 | 2025-08-14 02:21:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97b99e30-736e-3302-92d3-139b35c5ec9b | -7.8182 | -61.826099 | 2025-08-14 02:21:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b764b66a-3197-3e21-a732-0813e6e34e01 | -8.0628 | -61.238602 | 2025-08-14 02:21:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e313bae7-097b-3e97-a30f-89fe76661382 | -7.5638 | -63.537201 | 2025-08-14 02:21:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa8e7630-a80a-365d-ab6d-72c30f5715e7 | -7.8278 | -61.823502 | 2025-08-14 02:21:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c01a2917-698e-3b8b-aeda-a2cd056b5070 | -7.8354 | -61.852798 | 2025-08-14 02:21:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 980c0f87-e4ef-3bd8-bca4-4c491ceb867d | -8.0543 | -61.206699 | 2025-08-14 02:21:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 814c6e75-83d8-3def-82d3-9995f0013e67 | -7.5734 | -63.534801 | 2025-08-14 02:21:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6022fc-e493-3778-8931-0ab8d09a91f8 | -6.0807 | -59.9465 | 2025-08-14 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3bd94ebc-5093-325e-b3bb-2eeb62baa8b6 | -17.0629 | -51.7984 | 2025-08-14 02:30:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8b4efcad-702b-38f5-992b-14f4518ad314 | -16.3153 | -52.9201 | 2025-08-14 02:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| db8a7a22-a555-3bd7-a5b2-9e4e5257669a | -7.6103 | -63.516 | 2025-08-14 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3434702a-0fe0-360b-b118-0e330946162a | -7.8774 | -61.8253 | 2025-08-14 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ee0ca307-a9f7-34b1-bc72-f5947093158f | -17.0634 | -51.7767 | 2025-08-14 02:30:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 1add8184-43d7-30e8-94a3-6694a76dd167 | -8.5208 | -43.3298 | 2025-08-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |


[Clique aqui para ver as próximas entradas](README8.md)
