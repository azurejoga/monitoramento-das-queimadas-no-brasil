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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5a2e16-3e32-30ba-ad7c-9d44129d1c34 | -2.82239 | -50.49865 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2da9af1a-f328-37ca-ad64-e78ab402a2fa | -5.80567 | -50.15441 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43a73bf2-31a0-3a89-994d-a747ca53dfa9 | -3.11601 | -53.721 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 865f1a0a-1bfe-3e87-b1ef-2adeca947ee8 | -2.68927 | -54.64074 | 2026-10-04 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8722b301-fad6-3c81-aaa0-6808de0e901c | -0.34755 | -52.05265 | 2026-10-04 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce74d555-552d-3eaf-9659-6c9cb6e45fa0 | -2.75177 | -51.54492 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 546b1710-8ef1-3793-886e-809d044cdc77 | -6.00413 | -53.55284 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fca71ee-1734-371e-9453-55e41746d22e | -6.8171 | -46.65334 | 2026-10-04 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d30371f3-1275-31ec-b571-7a88f034e4fc | -6.81372 | -46.65278 | 2026-10-04 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06d297a5-289e-384e-9c73-33f85a410314 | -3.00557 | -53.87504 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ada148d-2328-3444-ba68-0dee8fb6e50c | -2.44668 | -50.25534 | 2026-10-04 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b52e35d4-b018-3351-a31d-fee2550caced | -4.12195 | -38.34933 | 2026-10-04 04:19:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6c06e2b5-eaa8-3db3-8f75-5b8be027e040 | -5.99607 | -53.52843 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 944f32d0-c294-3a14-bd24-d230d5780485 | -2.75121 | -51.54282 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 269097cf-112c-321e-ba02-3d838ac74508 | -0.49208 | -49.10971 | 2026-10-04 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fa20bd4-1bc9-37a4-a830-310a3548fa9d | -6.50417 | -51.05699 | 2026-10-04 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df08777-e855-32d1-bd9a-8f7ce1744d82 | -3.18019 | -54.08689 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 928d99b1-37c7-3472-8167-dcb9ef95af8b | -3.28491 | -53.83103 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 640dbfc7-4ac4-3c4a-9347-00360b17bcb3 | -3.08082 | -49.54138 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a00017d3-2bb4-39dc-bb21-a9d4b35207d2 | -4.46965 | -50.97405 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c44e186c-c875-375e-abd1-153dd12c1c82 | -6.28023 | -53.15558 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68703558-fc55-30e5-93a2-f1552ee33bca | -2.80907 | -54.10031 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6066117d-8fd0-3394-afb9-38a3d45aaf80 | -6.69562 | -47.93651 | 2026-10-04 04:19:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1368b2-b19a-36d9-99f4-d100f2e30814 | -3.17827 | -50.53348 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a481a68-7339-3eb4-ae76-36dc11998278 | -1.10085 | -54.10569 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bebe08de-684b-36e2-8f73-eb537b424d2d | -6.21429 | -52.80056 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 47207227-b464-342a-a4ef-d9473355e4e2 | -6.28578 | -45.84746 | 2026-10-04 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bfd1a67-cd21-397a-a37f-69145f68f05b | -7.48196 | -47.60605 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5327bfd-10e5-37bb-a54f-08186998e6cd | -5.99757 | -53.52975 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 342b34f1-0472-307e-bd11-5d60020531a2 | -3.08615 | -49.53468 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3bedaf6-268e-3ba4-b94e-3cf1b18a0020 | -3.12149 | -53.72187 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a6a4d05a-3ee8-3849-94d5-ba6b30d79b3c | -4.51281 | -45.89046 | 2026-10-04 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b3a57e4-c928-35a9-bef0-1578e1cd37aa | -6.23477 | -53.15062 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3015ba99-2133-3ee2-bec9-7fb8836118fc | -2.91398 | -48.9972 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddabe0f4-0294-3d3e-8c84-41799ac2390b | -1.62138 | -55.01515 | 2026-10-04 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2251e086-8c24-3eef-aae5-2a0dd4259fb7 | -6.57382 | -44.15759 | 2026-10-04 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec7ab223-c6b6-3881-b555-b863b2f9ad1e | -2.58211 | -51.86336 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c3597e6f-d75c-3e95-b800-aae3cf49f49a | -3.18078 | -54.08327 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57558b2f-8205-3a9f-b129-bf312ed7a659 | -4.26782 | -50.74935 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fdfcfbb-8f26-3e07-8aa7-859ee659b6b2 | -4.26412 | -50.74437 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aa51917-2490-3952-8170-420277c27913 | -2.83123 | -54.2123 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d4553b6-d138-3974-9f3e-f54f7f4582b0 | -2.81973 | -54.10595 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d4f9ea0b-bc0e-3bc5-b5e6-f11f4d03bc8c | -5.55031 | -45.26612 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9b7c515-3bdd-33c3-942a-d42f636172d4 | -7.99487 | -44.48979 | 2026-10-04 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20dc5c69-779c-31de-87c0-5efbdf492c7b | -4.46656 | -54.96668 | 2026-10-04 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c22397f-7644-3214-aee3-9ec8519e40ec | -3.18756 | -54.07708 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5548d47d-3c0b-3011-be3e-0fd3a796f057 | -4.13155 | -54.15546 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be17921c-0b1d-38d4-b061-6f3d07a5048a | -4.14309 | -46.83197 | 2026-10-04 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e954112b-6d73-340b-ab4f-b2084954bd1e | -3.00616 | -53.87144 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 625df039-008b-363c-8f52-34caec2e880f | -6.90214 | -43.68109 | 2026-10-04 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61c87507-12ef-3d8f-bab2-43921d86ba33 | -6.28031 | -53.15565 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b132c5ad-a3fc-36f1-b627-70f01e42b468 | -5.24976 | -42.85659 | 2026-10-04 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b79438f-6740-3f2b-a44f-cfe1a3acde9d | -5.22591 | -48.41117 | 2026-10-04 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c496d82-f658-38ae-b217-0b210f149ebc | -4.81942 | -49.87197 | 2026-10-04 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecc25af7-9d64-3bfc-bf1a-3057b600c0b2 | -2.11206 | -49.00146 | 2026-10-04 04:19:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34e33126-a5c3-31de-b6fb-c860dd10640e | -4.46353 | -49.69864 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3caf00-0443-3a05-b390-9a037a6227cb | -2.58125 | -51.86875 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 965bbc0d-9add-3ba0-9143-2a095b5733ca | -2.81279 | -54.11275 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b77e3168-b241-3895-bd5e-c6d42b6e671d | -3.15374 | -53.0676 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 844942bb-68e8-36f7-b576-eea1e50abbe1 | -4.30715 | -50.78498 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b92bd6a3-404a-305d-992d-18286f024921 | -5.80851 | -50.15553 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a416d9f0-7455-3019-be85-8867c61f9302 | -3.13616 | -53.73536 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3bdbfb19-0da3-360b-a47b-d7bed9cef937 | -4.46589 | -54.97065 | 2026-10-04 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d89c4cd-489d-3024-bf85-8d2032f1ce74 | -3.13068 | -53.73443 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c408ff9-fb1f-399c-84b2-e747db56c7cf | -3.11734 | -53.74701 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3da27d0a-df7f-39a2-8b54-fda85745554a | -2.75828 | -51.55968 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb7901ab-7dcd-32d1-92f7-bdfe272eaceb | -4.27138 | -50.27177 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef238ff4-372c-3d75-9857-4e7c4e0b758b | -2.24359 | -51.92258 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d04b64b-eafd-3125-bebd-83dcd48a74be | -2.81844 | -54.11368 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 57efe5f3-5bcf-38ae-9ffc-c50de6eb1545 | -4.28772 | -50.27842 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c09deb93-dc97-3f71-ad17-dfc14c5c1599 | -2.79777 | -54.09851 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d63a815-fd88-3934-bff6-d0677f950c23 | -4.27604 | -49.97792 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5cfcebf-4616-39fd-9a66-019347f8ce4a | -3.12106 | -53.75865 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d92e0df5-f341-3abd-9425-992cf12ee531 | -5.80441 | -50.15476 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24dcd5e9-046d-3303-b348-0aef6f6cffb9 | -3.04962 | -54.22691 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3551fe93-cad1-3295-acc8-336df247092a | -3.18695 | -54.08078 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9406379a-d29f-3da7-a97b-e2dddbe9c573 | -3.04585 | -54.21443 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eaf28de8-1785-3901-991b-974f74971d7a | -2.58358 | -51.87247 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ede4073d-aaea-3edb-a882-9ff10b6de342 | -3.2955 | -49.1228 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 947ff6d0-aa9e-3f57-bb9f-1aa5a3338e5d | -4.80444 | -48.2187 | 2026-10-04 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0617769d-32d5-335e-84bf-ba54f1bbcfc5 | -4.28281 | -50.28171 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a0675a9-801a-354e-a46f-f87a35f01d8e | -4.0793 | -48.95777 | 2026-10-04 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8210a416-625e-33ea-946e-08956f71ec6d | -4.28186 | -50.26125 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33d7b1ec-f193-3706-83be-6036958131c6 | -4.53027 | -49.69828 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 79ae0b9b-e000-3765-ad97-909bb546f35a | -2.58613 | -51.86952 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 974f2408-1acc-36e5-9ef8-d5f0b43c939b | -3.30516 | -53.84529 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bf9e48a-c53c-3d61-acb2-56ca2c57f8e6 | -3.27401 | -50.02797 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8acd6c32-7dd7-3846-b0de-9c87fc883a56 | -3.07146 | -49.52876 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab6217d3-fb94-3b2c-9e41-a219ba927097 | -3.20577 | -50.74693 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9143cf53-27cf-395a-8909-b95791fb9476 | -3.13186 | -53.72725 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 75c31daf-d038-30a3-b0b0-1961d8c2816b | -4.29127 | -48.56402 | 2026-10-04 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1110bf08-90ad-33c3-921c-e1310fa59eec | -5.74491 | -45.15548 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efca2f94-67cc-3ce0-a702-57d01fc11d1b | -3.77499 | -51.4002 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9c51b2c-7ecf-39bf-88a8-08f0d94af6c1 | -2.58038 | -51.87415 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c47c053b-527a-3880-852d-280bb6f025a1 | -2.0436 | -48.50084 | 2026-10-04 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76903d12-add8-392d-ac66-0189d1b76a4a | -3.18636 | -54.08437 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5101f859-3603-3423-96ed-0325c4111048 | -2.5969 | -51.85266 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 340824c3-9a99-3571-b321-4ce3c3affcd9 | -2.81472 | -54.1012 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea4d7408-4bdb-37ec-b492-ff65995f86ed | -2.81036 | -54.0926 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b589681b-a01b-386e-827f-5ad867ab8878 | -4.262 | -46.36969 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README28.md)
