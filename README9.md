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
| 9b77407c-8a81-3afd-b90d-82983db894d9 | -11.0381 | -45.1256 | 2025-09-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b59537ff-9f8a-36e9-ac27-3f8af57f74be | -6.8466 | -52.8132 | 2025-09-01 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6d264569-9d53-3572-a291-f65f5ce53e57 | -8.6468 | -67.2515 | 2025-09-01 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d4a80621-0864-311b-8f9e-7ac0be45e216 | -15.7112 | -48.9032 | 2025-09-01 02:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0654f5e5-b22a-3e18-a2a3-af18f181c0b3 | -12.9004 | -56.9689 | 2025-09-01 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2948a24f-358a-3444-ac3c-a9335beec538 | -6.4793 | -43.9516 | 2025-09-01 02:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ca7a1cf6-76c2-3900-963b-08ba67bb273f | -7.076 | -44.3376 | 2025-09-01 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 6ba77759-68b7-33a6-b469-20a64b28befa | -15.6058 | -48.3402 | 2025-09-01 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 57694f0b-55e5-35d6-9600-8c899e2afbf5 | -10.6128 | -44.3284 | 2025-09-01 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d24dbeed-721e-326c-bdb1-30c4b86cf338 | -10.23 | -51.1147 | 2025-09-01 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 661b20ba-0bee-3586-970b-5ef46a8ad0b1 | -12.9194 | -56.9672 | 2025-09-01 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 265.8 |
| 8f83b7cd-5748-3c66-bcd6-44c82cf1a3fd | -7.0757 | -44.3606 | 2025-09-01 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c011fc95-5926-3e6f-b973-2bdcf2d71cb4 | -15.5867 | -48.321 | 2025-09-01 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 35d9c4c7-ca7d-3e05-85d0-aa92f1bb5622 | -13.1644 | -45.2897 | 2025-09-01 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6443836e-ead9-393c-9c32-c6cd8d2b01a6 | -7.0965 | -63.0437 | 2025-09-01 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 17200779-2b33-38d9-bafc-543899879778 | -7.0948 | -44.3358 | 2025-09-01 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 6d6594d0-ef7d-36c9-974b-b06606aed073 | -13.1648 | -45.2665 | 2025-09-01 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ef3abbfc-2095-35b8-b690-61a35e4538c2 | -12.9197 | -56.9471 | 2025-09-01 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 404.0 |
| 46e6911a-71a6-31ee-9b17-d3cfeb03b7a5 | -7.6783 | -61.0908 | 2025-09-01 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e928664b-e8c3-3432-ad2a-c665497f4a6c | -9.1337 | -65.844 | 2025-09-01 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 69dcfc38-32bf-3d0f-9063-4ffb046d45cc | -10.2488 | -51.1128 | 2025-09-01 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e1d7026b-11e6-35b3-bb6a-5fa6d18044d2 | -15.6916 | -48.9065 | 2025-09-01 02:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 17454004-0039-340a-9802-b06423a047c2 | -23.1126 | -52.5288 | 2025-09-01 02:20:00 | GOES-19 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 101.2 |
| 42cc02d7-9867-3674-a40c-ddda9adac278 | -7.0948 | -44.3358 | 2025-09-01 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 563f059b-1c91-3e4a-b8da-f9fecaa65041 | -13.1837 | -45.2865 | 2025-09-01 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 54a8519b-2b75-3d89-97ab-00332d34a965 | -12.5914 | -48.2032 | 2025-09-01 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 569d5db5-5000-3dd7-b6fd-e1b0f3f164d1 | -12.9385 | -56.9655 | 2025-09-01 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.8 |
| 253d5689-d0f9-34c8-b379-2a0a4c70073e | -8.6468 | -67.2515 | 2025-09-01 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 4d32beec-11f5-3145-b12b-4516b9c43676 | -12.9194 | -56.9672 | 2025-09-01 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 317.8 |
| 562426aa-2189-37b6-8208-1375d3fe6a84 | -23.112 | -52.5513 | 2025-09-01 02:20:00 | GOES-19 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 142.7 |
| 02838f67-1ddd-3bac-91db-860c6e96c36d | -11.0377 | -45.1487 | 2025-09-01 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| fc9debb9-51d6-350a-a127-53ca7d8fc492 | -11.4232 | -63.2634 | 2025-09-01 02:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ec8a72b4-e898-3669-81f5-d6b090c927d2 | -12.9387 | -56.9454 | 2025-09-01 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 309.9 |
| 89af5bce-56e2-35ed-857b-165d03f62a1b | -7.0757 | -44.3606 | 2025-09-01 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 22e2713a-dae5-305d-bd4c-8b2a1a36edbb | -18.6704 | -52.5973 | 2025-09-01 02:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 55f9f0d3-5fd5-3dbb-8ab7-76ea9bd3ab32 | -11.045 | -47.0514 | 2025-09-01 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fbc85da1-10bb-3302-aeec-19b2b143e856 | -11.0568 | -45.146 | 2025-09-01 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 17803444-2f2d-33bf-a655-900fb3404b0b | -10.6128 | -44.3284 | 2025-09-01 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 2e82303e-1109-32a4-93a0-6cbf066dfe29 | -11.026 | -47.0538 | 2025-09-01 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 613d14cd-6546-3fb2-b6a1-a286f345a0ed | -6.8466 | -52.8132 | 2025-09-01 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cf4c5f1b-2dc0-393d-b18e-28c09a1ebda8 | -8.7684 | -61.4261 | 2025-09-01 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f714b3c1-f89f-3764-b58f-312e3a414f8f | -13.1644 | -45.2897 | 2025-09-01 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c5c1a58b-25b7-3bf7-8bec-9c734295b263 | -11.4044 | -63.2644 | 2025-09-01 02:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 376a54e1-545f-31b3-965f-b2b4b7c656e0 | -6.4605 | -43.9532 | 2025-09-01 02:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 9bcfc512-e4c8-336f-b85c-a87f9c6bf5cf | -12.9004 | -56.9689 | 2025-09-01 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a66d6998-7700-37e4-b73a-0bbd66c827ca | -7.0946 | -44.3589 | 2025-09-01 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d8990cfd-7786-3a28-a973-bc0d1f94c504 | -7.076 | -44.3376 | 2025-09-01 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 53a60f07-f6a3-3a2f-a8e1-2c7ea9c96448 | -15.7112 | -48.9032 | 2025-09-01 02:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5f25efb0-45f3-3264-a4f7-7925d1a499d6 | -13.1648 | -45.2665 | 2025-09-01 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9668dda8-b076-347d-aba4-896af27bfdb6 | -10.0434 | -48.0998 | 2025-09-01 02:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e2e565e9-7dd9-336e-a9c7-06922f742848 | -9.135 | -65.5453 | 2025-09-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 146ec936-f802-3627-86ae-361172b95ddd | -10.23 | -51.1147 | 2025-09-01 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| bfe5c0db-4279-38ff-80f1-2c348d8afe47 | -12.5722 | -48.2059 | 2025-09-01 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2da32bdc-829b-3a24-aba9-7e35375cf438 | -6.8095 | -52.8154 | 2025-09-01 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 682900e1-3301-3ea3-935a-dadca6a6dad5 | -6.8281 | -52.8143 | 2025-09-01 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1878f3b9-5291-3c6f-968c-387cc8f7aea7 | -9.1165 | -65.5459 | 2025-09-01 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3f76f3bb-8353-3ea2-bca3-df76a2b63392 | -6.4602 | -43.9764 | 2025-09-01 02:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5420143c-2d0d-3aef-b0ef-efa95cda1184 | -11.423 | -63.2825 | 2025-09-01 02:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c6674ae3-1c46-3734-8ad0-92266dea4d2c | -10.5937 | -44.331 | 2025-09-01 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 88fa89a4-b4b1-3907-ba8b-25aa3b38e71d | -15.6058 | -48.3402 | 2025-09-01 02:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 31486a9d-c279-3c36-a0b7-18abe3ae6a07 | -15.5862 | -48.3435 | 2025-09-01 02:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 96552639-d34e-3a8b-a9c6-f6187f07fb89 | -11.8185 | -46.4087 | 2025-09-01 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d92289a3-195d-3100-97bb-8e4a02082e1e | -10.2491 | -51.0917 | 2025-09-01 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| a2ad4b73-06e1-3a0f-a112-90ee4ca42841 | -12.9197 | -56.9471 | 2025-09-01 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 450.1 |
| 06ada068-f84b-3dc7-b417-f177eb0db7c7 | -6.8279 | -52.8348 | 2025-09-01 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d94a842a-45c6-368f-b769-23827e0bcc86 | -6.4793 | -43.9516 | 2025-09-01 02:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8677b34d-2dce-3b61-8b00-da07a249e2d6 | -12.9006 | -56.9488 | 2025-09-01 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 2e84df43-270b-39fa-9ef1-70af06a98bf5 | -11.0381 | -45.1256 | 2025-09-01 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| fcb63653-1f9a-3cc3-83d2-8f27092bb5fc | -12.9387 | -56.9454 | 2025-09-01 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6641e8ec-c0c1-36fe-a513-12bfd09c8d7e | -18.6704 | -52.5973 | 2025-09-01 02:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| c2b79ac7-d109-35a4-a1d8-949de4570bb0 | -7.0948 | -44.3358 | 2025-09-01 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 15298c50-fc61-311f-890c-03388d35422b | -15.7112 | -48.9032 | 2025-09-01 02:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| fc646dfe-c160-3cc3-b9a8-85ea71b413b6 | -10.23 | -51.1147 | 2025-09-01 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 0cd8459b-a370-3bba-8ee4-13b8da139fab | -13.1648 | -45.2665 | 2025-09-01 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a3256f3d-f155-3b4b-b2e5-946aab1b8969 | -12.9385 | -56.9655 | 2025-09-01 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4f7baaf8-106d-3c3e-8326-c08a71abe3b0 | -6.8095 | -52.8154 | 2025-09-01 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| daae9d2e-f825-39ad-82af-68d5a0111373 | -6.8466 | -52.8132 | 2025-09-01 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4633ea9a-6498-384c-b284-c3498f8b913c | -13.1837 | -45.2865 | 2025-09-01 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 00fe42ad-99e0-3f92-878d-6708a3323395 | -6.4605 | -43.9532 | 2025-09-01 02:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 71da12fe-2a45-3189-a476-6ac7f190972c | -10.0434 | -48.0998 | 2025-09-01 02:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c10e9ad3-b564-39c9-b5ce-939f9245f793 | -4.8388 | -43.0282 | 2025-09-01 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 29bfca42-7a97-3b14-b49e-d71c07f26d1d | -10.2302 | -51.0935 | 2025-09-01 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| dcba54e7-2898-3eb5-a782-f74a7d84a611 | -7.076 | -44.3376 | 2025-09-01 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| fe607ba4-4e0e-3065-a45f-2b02b5de4b85 | -10.6128 | -44.3284 | 2025-09-01 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 43fbb548-344d-3522-bbef-28af88a562af | -11.0377 | -45.1487 | 2025-09-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 28babc83-0cf2-3ad5-aa02-6bfc8cfd04fd | -15.6058 | -48.3402 | 2025-09-01 02:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 122.4 |
| cbe773b9-91a9-3aba-a90d-841484d5fff0 | -7.0946 | -44.3589 | 2025-09-01 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| e5a423e0-e3a0-3516-8935-2b31bc6a4554 | -13.1644 | -45.2897 | 2025-09-01 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 016df5ab-efb7-3024-a867-9945e5d87f09 | -10.2488 | -51.1128 | 2025-09-01 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 496003b7-39f4-3502-928a-85dbf5891df6 | -11.0381 | -45.1256 | 2025-09-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7ee7d800-4ea7-38f0-a857-e623e8b19ca9 | -10.5937 | -44.331 | 2025-09-01 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b7f13896-ec3d-3d78-82b0-e4cb683994a9 | -6.8281 | -52.8143 | 2025-09-01 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e4f3722b-2af3-34cb-b7bb-ca69951b17d7 | -12.9197 | -56.9471 | 2025-09-01 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 7a406141-cbbf-36da-a45d-ef9002d6f448 | -10.2491 | -51.0917 | 2025-09-01 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 2eeb98e7-ef05-37e1-8466-9800b4d9e89b | -7.6783 | -61.0908 | 2025-09-01 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c8e0c61a-a888-3bbe-90f0-a7a6feb93914 | -8.7684 | -61.4261 | 2025-09-01 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a386cc89-c2a6-31a7-8a8b-c4261acfc710 | -15.5862 | -48.3435 | 2025-09-01 02:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cbad741d-8aed-301a-89f0-955d000194c7 | -11.0572 | -45.123 | 2025-09-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 90a3c6e6-39e1-3e7c-a6a6-cb63546ed369 | -15.7116 | -48.8809 | 2025-09-01 02:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1ecd6240-2750-30d0-9a80-399f074ac5d5 | -9.135 | -65.5453 | 2025-09-01 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |


[Clique aqui para ver as próximas entradas](README10.md)
