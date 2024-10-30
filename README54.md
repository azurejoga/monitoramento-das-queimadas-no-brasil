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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75b06e74-8c8e-3e2a-b987-38fb20cfd55a | -19.6063 | -56.7108 | 2024-10-30 04:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.2 |
| 6706bec0-e2fe-3661-9d9c-60c24ef71fd2 | -19.6264 | -56.7079 | 2024-10-30 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| aa27cae4-7b3e-3878-bf89-6ba24568fb94 | -24.0123 | -54.151 | 2024-10-30 04:37:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.3 |
| 03936c4b-87ac-366b-a6f2-51e8ad1895be | 0.08643 | -49.87458 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a505814-45ec-3fcb-be78-5ddcbf47a8c4 | 0.08589 | -49.87113 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 091a765d-043d-3c1f-a727-8c8ce092adb4 | 0.08534 | -49.86768 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b566015-0b7a-32a2-b5b3-a6cc97aa011e | 0.08257 | -49.87165 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52821c2f-f67e-348f-a3a7-98eb6c6f3716 | 0.08202 | -49.86819 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1267bc7-595c-3351-ac27-696666598f3b | 0.07979 | -49.87561 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aab820a-109f-3567-9fe2-88256756ed70 | -0.2177 | -48.99387 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b074f5-4e71-371a-a3ca-5b313f99d22e | -0.68478 | -49.55436 | 2024-10-30 04:42:00 | NPP-375D | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a6b2f98-72c6-35ff-bdd0-a35e303d6ce0 | 1.6495 | -50.89388 | 2024-10-30 04:42:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea1639d3-ddf3-3e6f-890f-104830409094 | 0.80161 | -51.09752 | 2024-10-30 04:42:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d549f7c6-c2ac-3967-b683-21c633201b4f | 0.43844 | -50.27881 | 2024-10-30 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ab1c507-386b-33e7-ad4f-f359c07728af | 0.42324 | -50.86879 | 2024-10-30 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea89c0bd-e715-3054-86cf-a6867044c06a | 0.12298 | -50.51428 | 2024-10-30 04:42:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fe73a21-6498-309d-969b-6e41ddf520f3 | 0.11963 | -50.5148 | 2024-10-30 04:42:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ec3fee3-68da-34b4-bc98-282bcd744905 | -0.10462 | -51.30647 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1404146-eedf-35a9-b304-16e4611a4d23 | 3.56423 | -51.26777 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51f9078b-0424-3134-b2cf-5903b4648a3a | 3.55718 | -51.26885 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cddadb3-adb1-3161-b1c8-4d413ad071eb | 3.55426 | -51.27332 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9a0df0c-e902-3dee-b2c1-1f758193b36c | 3.55134 | -51.27778 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec2bbcda-4eda-34e8-8724-f5a46d6637aa | 3.55074 | -51.27386 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2d64ab4-9083-36d5-9663-b452ca51ec4a | 3.54901 | -51.28619 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a703d41d-48d4-358c-8248-6741089c3848 | 3.54841 | -51.28225 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02fd4fae-91ae-30c7-9cdc-385f01210dc6 | 3.54781 | -51.27832 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fde3ed32-4199-3ce3-9c44-ee7e31d427ed | 3.54549 | -51.28672 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3d04d9d-7dd5-3322-80d8-7ef422357d01 | 3.54489 | -51.28279 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11024bbc-86da-3f1d-90c4-181eeb9e2dad | 3.48392 | -51.47429 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47e0772e-029f-31ab-bcc3-637bc45cb89f | 3.48331 | -51.47029 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d46053ce-45f9-3221-ac72-1deb57f3b7bf | 3.45165 | -51.2407 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc842ff2-1bdf-3470-8d67-cd636a97a5f0 | 3.44873 | -51.24514 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba1fb0e6-8d0b-319e-a087-5059092af942 | 3.44813 | -51.24124 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fba6b1ea-1e55-3c72-a755-cc0fd9ce7b48 | 3.44522 | -51.24568 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2e0c785-273f-3a55-a077-726fe8777a09 | 3.4423 | -51.25013 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cb97e5f-7fb0-31fe-99f5-248329e89c3d | 3.4417 | -51.24623 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6550ad-4450-36e4-8264-5c1f0607004f | 3.43939 | -51.25458 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6250dfdf-bdd1-3edc-86a9-694e1e9ae0a7 | 3.43879 | -51.25067 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8d85f7-ac5d-308c-bd98-1f7ae320056a | 3.35817 | -51.35811 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 844b6ea1-9c69-3bb7-9dde-333d1ba76705 | 3.31635 | -51.3444 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 908f7f9e-ab60-3b7e-8bb3-66fabd9356ab | 3.31612 | -51.34339 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae0bd8a4-cd6e-321b-b65f-8c2cf5f8bfa3 | 3.31259 | -51.34392 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee2dd391-b845-32ca-8dd8-82666324195b | 3.31092 | -51.35625 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e446cb2-352f-3764-ab48-2e6220a64e6d | 3.30739 | -51.35679 | 2024-10-30 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97257f77-9fec-3156-950d-0d250aaab712 | 1.0113 | -52.21614 | 2024-10-30 04:42:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16c7ed76-78aa-30c4-a793-1bebcd933756 | 1.0077 | -52.21665 | 2024-10-30 04:42:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df97a4c5-1dd9-3cc6-a86a-abc3628e0716 | 0.94448 | -51.92684 | 2024-10-30 04:42:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51468de9-f990-39d0-a7e3-9b9d775ad5b3 | -0.39391 | -52.05993 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a28ae2-d0cf-39cb-9015-013065181071 | -0.39329 | -52.06381 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03d40964-35e5-3e20-b165-7f50d4360455 | -0.16946 | -51.67432 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35366ce9-9163-34b3-8ad2-cd00aa3e7d9b | -0.16887 | -51.67809 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf28487-a77f-3666-b854-f8ba654b14b8 | -0.166 | -51.67378 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2067d08-8fb6-3b77-a307-9639983fd86a | -0.16581 | -51.56223 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e330d6d-30cb-3bca-a3a6-8628e1e9ded2 | -0.16254 | -51.67324 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 383a6d58-e9f5-3dd0-ac9d-5646d8037be9 | -0.16236 | -51.5617 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33c77145-f983-3e60-83b1-f5ceef3c4302 | -0.16195 | -51.677 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e9869d-962f-3f75-9c0e-b12dc5609700 | -0.69527 | -51.6804 | 2024-10-30 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30aef13e-4da3-3ba8-b2df-d59df25a0ee1 | 1.60447 | -55.62545 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d655792-a02a-373b-b4f7-cf23594428c2 | 1.60187 | -55.62391 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e511cb15-10d1-3d4b-9e25-f84a603033a0 | 1.6 | -55.62619 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 391656ed-abcb-3705-9123-617f6fdd3779 | 1.5981 | -55.62906 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24faff9d-e8e2-35fb-ac92-04ddfff5c0b9 | 1.5974 | -55.62465 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43a7ad4f-b322-3ac3-a7b0-d990628f6f28 | 1.59554 | -55.62693 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82d23c52-bfdb-34e9-ad2d-ec8b4c7defb7 | 1.57435 | -55.6236 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd941b34-0795-3f09-826c-175b8692dab3 | 1.79992 | -56.05775 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be94a633-f631-3b1f-ac44-babb285aa947 | 1.74877 | -55.84276 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2becba7e-0349-33bc-a17c-221f2837a0d6 | 1.74852 | -55.84089 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1217de06-d126-3a4f-bfa9-2ee0ded673fd | 1.74805 | -55.83821 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08ef45c8-6f9c-3966-980e-b9f2531a5f2f | 1.72911 | -55.83623 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e229e37-6ea9-37d7-b9b3-e34ea40d0a5b | 1.70115 | -55.83604 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7f3d22f-68fe-3c2f-80e8-815c75102b6c | 1.6966 | -55.83676 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6527753-25cc-33a6-b4ef-7485a677028d | 1.69379 | -55.81849 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d175c8a7-5cbd-3c8f-9314-d04089d495c8 | 1.69308 | -55.81389 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9f32006-682b-39c0-850c-46560338636d | 1.68784 | -55.81001 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd81e58f-815a-353f-8cfd-90159ab50aa7 | 1.6833 | -55.81072 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d320c94f-acaf-345a-8138-aba0d95b41ae | 1.68121 | -55.85779 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c4a03e4a-a0b3-35b4-a730-c79c83678f8c | 1.68051 | -55.85322 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 92f0a3fb-b14e-321c-8e42-9b723b4c0526 | 1.67877 | -55.81144 | 2024-10-30 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fedcda15-19a1-3441-9b50-c19b802f1de5 | 1.67665 | -55.8585 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fd0b78dc-da0c-3deb-be35-31836e76e8c2 | 1.67456 | -55.84478 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e393303c-9131-34e5-8a30-f78036e19b32 | 1.6735 | -55.86837 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5244804e-6f0e-3d4f-bbe4-f72c613db330 | 1.6728 | -55.8638 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b275fd5e-8c57-35fa-865c-de7c0cfd3fe7 | 1.67211 | -55.85923 | 2024-10-30 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 460d2814-e7fa-3d03-bc15-6df1ac08bd2c | 1.129 | -59.44204 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 561e2ecd-c3eb-35e9-bc66-b43dfc0314ce | 1.12888 | -59.44498 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f5f99b8-3de4-3265-bcec-700366bc68b2 | 1.12823 | -59.44089 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 422090e5-8bc8-3fc4-b74c-679d7fe3febf | 1.12324 | -59.44297 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41ce2b6b-639d-3c11-8121-af8043031f88 | 1.12247 | -59.44183 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3db0974-3a6a-3698-93df-148f96a9862c | 0.99499 | -59.45784 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7103347a-37a8-3178-a60b-0778d516c65a | 0.63541 | -59.62252 | 2024-10-30 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03292f9e-b59c-3682-a300-f75e6c051103 | -1.11662 | -46.91315 | 2024-10-30 04:42:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f40bd24-603f-3303-9346-842a4f0159a4 | -1.34869 | -47.75067 | 2024-10-30 04:42:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f89d96a-439e-3f37-b5bc-1706053278c2 | -1.30443 | -47.74003 | 2024-10-30 04:42:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a576a261-6b87-30c5-9807-d4b0218be48c | -1.13183 | -47.59549 | 2024-10-30 04:42:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2800edb0-4441-3105-93c6-b4c898424a72 | -1.05443 | -47.63746 | 2024-10-30 04:42:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ea00345-ded8-338c-89b4-cb3f0d695ff7 | -1.05254 | -47.63796 | 2024-10-30 04:42:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6113bce1-b215-3aab-9e52-07d8634ba002 | -1.04555 | -47.87616 | 2024-10-30 04:42:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35541909-0037-32a6-bb93-e3dc5ac3fc85 | -0.93967 | -47.28207 | 2024-10-30 04:42:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce2e8c6b-3f12-3d75-806d-4449074bd81b | -0.85618 | -47.63503 | 2024-10-30 04:42:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c29268b-78a1-367d-8248-6c720a9fdcff | -2.99661 | -48.9499 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README55.md)
