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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a27e8358-4064-3d54-ad31-2c54159d35a7 | -7.74937 | -44.21951 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb1b3031-c141-3ff2-a82f-43208935127c | -13.2943 | -47.12879 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 35c404ac-82f7-3a07-8961-58bd60bfb7da | -7.86698 | -44.48264 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfe93ce3-445f-3b19-86c3-2de01e87c5c4 | -9.40347 | -66.75706 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3aa2f34-e2a0-380b-b0d3-ad18f816d25d | -9.10942 | -45.04862 | 2025-10-11 05:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac8a2393-1634-393a-be21-6d1ecd210d71 | -7.33178 | -43.86599 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cb597d1-1bd9-3333-a29e-5358070b5422 | -8.19483 | -43.32475 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 1cace95f-3345-3fb3-a6a6-87a862cc64b4 | -7.58348 | -47.20961 | 2025-10-11 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbaec7b2-d237-3507-9762-be8229193c62 | -10.55712 | -57.51551 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 894e354b-8145-3996-a551-a4efd0e1a7ce | -13.36283 | -47.63111 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57a6c162-afe1-3463-866a-b7ed8f369bc1 | -12.90142 | -47.05078 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09378037-d5fb-34e9-a00c-e15c7a9b52ae | -13.27998 | -48.0011 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1139e85c-2020-3b5f-985b-31c7eda95187 | -9.92887 | -59.92201 | 2025-10-11 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87fa88f2-b0ad-33cc-90b7-0fd74c963ef9 | -13.51184 | -48.1249 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4eb59b69-17ff-3eca-a530-d169ba8110f6 | -9.81364 | -45.52361 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0499b73-8ed2-3bd2-8cb3-d68fae98c437 | -13.28065 | -47.99586 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 825d3760-cc92-372d-ad04-6769d6830cf4 | -8.14504 | -43.33287 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5127cc8d-17d7-3ae2-aa45-56a1c19376eb | -10.51748 | -47.36148 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 895c4507-d4fb-3613-b48a-c2a82ec50680 | -13.34348 | -48.48094 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| befcaaf0-20ce-3ece-94b5-4a5f8b054934 | -10.37742 | -57.64019 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af91a27e-ca5c-331c-ab2e-e95653b2f6de | -10.05879 | -67.55215 | 2025-10-11 05:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de7eefc4-d759-3c81-9863-657ed4d26085 | -10.1725 | -44.54449 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 43e279f4-1861-38af-b833-de708db98cca | -7.85455 | -44.48851 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7d4dd62-1251-3ed3-ba73-c5ebe857a780 | -10.4228 | -44.99362 | 2025-10-11 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5ed33d6-efae-3566-8112-1c88c9a5553d | -13.45628 | -48.09713 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5ff49f9-637d-384e-bfd6-a623f5a6373c | -7.53835 | -44.60389 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76e53554-6791-3a59-b069-4108334ce2b1 | -7.40919 | -45.92061 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 172209cf-1466-3959-a659-15fddb91911f | -11.88968 | -45.4937 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc26820-33bb-3338-9708-261701731ac2 | -10.50918 | -47.34935 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c5c7fdd-1983-3030-a677-e54c7c89f5eb | -10.51408 | -47.34997 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 418d1674-bc48-3acc-9802-f1d81d07caee | -12.18466 | -48.80586 | 2025-10-11 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8e3090f-4689-37d7-8490-72bbf2d09b0a | -10.73356 | -49.33791 | 2025-10-11 05:01:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89148eae-0b0f-3b8f-90c9-41f2401f07b7 | -7.67322 | -43.98955 | 2025-10-11 05:01:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0707492-cb3d-3170-bf5b-0c6b817cc375 | -7.86075 | -44.48564 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be955f78-1202-3705-b369-87332a7112ee | -12.23894 | -51.13918 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abc82d3e-7a24-3210-901b-332f3841818a | -13.45986 | -47.7023 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 178bff87-141e-3bea-9bfa-cfa4fed17c9a | -13.46033 | -47.70289 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e775b9fd-8bef-361e-856e-26c3ef218ded | -13.2161 | -42.3433 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| f7f1f1e6-ff07-3ece-83cc-986d978f325e | -10.38028 | -57.64475 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2dc658e-e9a7-3da3-a758-8be1fb5491e0 | -6.43974 | -45.82767 | 2025-10-11 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5bfd5f4-8b6d-348c-bb42-06213909595f | -9.40327 | -42.66771 | 2025-10-11 05:01:00 | NPP-375D | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d379c016-ae9d-344c-9ed1-590395e957f9 | -12.89847 | -47.03174 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb860c8d-c4e5-35a7-861b-b7f54e24184a | -7.12215 | -45.92041 | 2025-10-11 05:01:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcd0ad58-6a4c-3340-9e5b-c757c3102c12 | -12.71958 | -44.94079 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 099d26fd-54b0-3649-8bb8-28dea5179ef4 | -13.28287 | -47.13622 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb4064e4-d42a-3881-acba-f4e05826b991 | -7.67587 | -43.9879 | 2025-10-11 05:01:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 965ec984-4fcb-3662-be34-13fab268ceba | -13.28845 | -47.13361 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5f2b314-709f-3910-b66a-a30b1715fb84 | -12.9035 | -47.0337 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1c76074-4a69-3f7e-8d09-a91d11c9716d | -8.15119 | -43.33389 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f969a3a5-90b9-38ed-b662-3fce19424033 | -6.74994 | -42.82007 | 2025-10-11 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 40cba8ab-bf3a-3a60-82b1-45284f841920 | -13.53419 | -48.12502 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfa2ebf8-0998-32e6-9d7b-d2cce2a477cc | -10.05987 | -67.54663 | 2025-10-11 05:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8a281b1-fe77-3328-824e-2c809faae188 | -7.57309 | -45.93502 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5daad81-62a5-3242-a8ea-133f56997b53 | -13.3146 | -47.98003 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbd01bfc-3a8d-33eb-a98e-112511ae8a5d | -7.349 | -43.85818 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 251a03b8-fbfe-3453-a442-13364ee1e6b3 | -12.6928 | -51.19496 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebfb8e61-4168-3671-8a9c-d87c7585de8f | -7.38858 | -45.17184 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f7060c6-04c7-3ca8-a62d-6862d8a4c91d | -11.75927 | -46.35883 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a3efc4-a7d5-3e11-89c2-90be4034b539 | -9.44766 | -45.45798 | 2025-10-11 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 307d32e2-5a56-3792-96c4-8ba169bf1db4 | -11.75433 | -46.35505 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ba4af1e-6524-383e-bd64-1610f44d67ca | -13.21678 | -42.33665 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 9c0e8af7-ed93-3e01-9b65-8136a66e82a0 | -7.67263 | -43.99403 | 2025-10-11 05:01:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3276ce1-340d-3c53-8335-c0d2d90aba88 | -8.17244 | -43.31614 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e10654b2-c52f-3450-8fe1-c66f81321b66 | -10.38391 | -57.64402 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0593bb6-0f11-37ff-8511-e3b797607081 | -13.30453 | -48.48552 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50d3b233-5592-3ec7-bd9a-cbcf2b7c184a | -11.53101 | -49.28275 | 2025-10-11 05:01:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1977edb5-ca8b-364b-8211-2f358e110cb1 | -7.53164 | -44.61092 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed00bb1b-e413-3925-8805-75a7634485be | -9.1728 | -68.18314 | 2025-10-11 05:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e3c7be63-ec32-39e2-a3c9-b28d774fc71d | -10.99769 | -56.91909 | 2025-10-11 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96de03c8-f136-3b3b-bcfc-aec87fab1423 | -11.06277 | -49.56119 | 2025-10-11 05:01:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 054d4a0c-47cf-3622-b2e7-8a3a5f1272ac | -7.06871 | -45.21437 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec1910fd-5598-3e95-a286-dfb5d043df9c | -7.50388 | -45.14257 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 647abc62-7ad7-30f7-8135-315a49d96390 | -13.26384 | -48.0112 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 662f9656-a631-3ac5-9847-ac9d5ba06eac | -13.29657 | -47.98766 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af8f79ce-7cc1-3494-b136-b3eb8dc46227 | -13.33874 | -48.4805 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abb8e1a0-9345-3088-b320-9ca8cf33a254 | -9.40378 | -42.67027 | 2025-10-11 05:01:00 | NPP-375D | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6bfe89fa-7230-34df-9f66-d6e0bbd58645 | -12.90108 | -47.05358 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 483c7704-6984-3032-8511-613abec3cb4c | -6.81239 | -44.63309 | 2025-10-11 05:01:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 036e97cb-17f4-3de1-b126-22e5dcd0b4db | -7.25311 | -44.09467 | 2025-10-11 05:01:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cd402ae-7bb5-38f8-adc0-8308826ecec7 | -13.40637 | -47.26722 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 458a1b69-b619-310d-9942-1c503bbf3ed3 | -7.13008 | -45.08717 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b60dc9f1-c37f-33e3-b1c5-9981e8208cd7 | -6.2492 | -47.22286 | 2025-10-11 05:01:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faf73a48-fb5b-368e-8135-f9dbf7bd4bfd | -8.201 | -43.32569 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6963af00-1b52-3eed-b913-78ccf319275d | -8.20656 | -43.33136 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ef2b5401-a02f-3d3c-8579-298b0f752f4d | -7.74918 | -44.22109 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9c569ff-bf24-3df4-8f5f-0c1afd2cddd5 | -7.38678 | -45.17218 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d145e420-412b-39dc-9728-3ec8ac18ef24 | -12.71366 | -44.94005 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6825b11c-e904-3173-b077-ca61ac2fc121 | -8.1959 | -43.32892 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e6927dcd-69e3-32d4-8f89-c9c89193dea8 | -11.75971 | -46.35529 | 2025-10-11 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25e17307-01f2-32eb-9b1f-595a5bcffe7e | -10.51898 | -47.35053 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c0085c0f-6346-3f50-9a0a-c5c02cafe5d2 | -10.5699 | -44.51031 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6282ae9-bc59-3453-b43f-6e9294cc6dff | -9.40814 | -45.95808 | 2025-10-11 05:01:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bac4fe43-d23e-385c-9a23-b6e34b0c9976 | -7.86803 | -44.4748 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7212fc3-3e48-3e05-ab32-a1138816b21e | -7.53292 | -44.29205 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c1ea43d-7a90-31b0-968d-73c5b76b66b0 | -9.44219 | -45.45725 | 2025-10-11 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74136689-0036-387b-878a-b27ada869a6c | -11.75883 | -46.36235 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ed1fe0-4846-3bf1-b7a7-50c412390d7e | -11.76392 | -43.31559 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea797bb-91cd-3993-975d-0674690cc78a | -12.89699 | -47.031 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43b990ef-62e6-314c-9f35-0042e696c6a2 | -7.34954 | -43.85399 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abf0fb6f-0d9d-36a8-a7d9-33a2732c7b96 | -12.9021 | -47.04523 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README35.md)
