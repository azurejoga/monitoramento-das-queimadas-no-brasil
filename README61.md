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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20f1c7ef-5096-3453-8b17-aacb064fbf71 | -15.0196 | -54.8112 | 2025-08-19 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f82ed912-acd3-3980-9134-181a3098ff72 | -12.5042 | -45.5788 | 2025-08-19 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| d1449c0b-71a1-3763-aadf-43634a829338 | -7.5899 | -45.4315 | 2025-08-19 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 07872039-b8ce-303f-afb5-8756fc941194 | -12.9971 | -56.8395 | 2025-08-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 0b9489ba-e164-3157-b52c-a699883bdaf6 | -15.0386 | -54.8297 | 2025-08-19 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 73388b13-6be0-3bed-87ad-3b5e32e6a2be | -13.1743 | -54.9542 | 2025-08-19 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ad1cd9a5-4ac3-3300-a7ef-4704a195a75d | -13.2755 | -50.8137 | 2025-08-19 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.2 |
| e3986736-6a1e-31c1-8a17-f0ce8b6e259b | -7.5711 | -45.4333 | 2025-08-19 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 935244a4-0a18-38ac-aee6-d5b57398bc93 | -7.1482 | -44.6065 | 2025-08-19 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 031b4536-dd4d-31c1-bcd8-be66fe89a37a | -12.9778 | -56.8614 | 2025-08-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9c9884ed-0c63-3f78-bb9b-241627f90cb1 | -13.1555 | -54.9357 | 2025-08-19 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 688.0 |
| 85b21b5f-779f-3e9e-a889-8ef025e795bd | -6.9715 | -43.5833 | 2025-08-19 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 24ed8997-7eed-3019-adf3-c9b67487f6c7 | -12.9968 | -56.8597 | 2025-08-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a69667c4-7ba9-344e-9319-92b9b597d1c5 | -6.9712 | -43.6066 | 2025-08-19 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| bafca5ec-ba3b-3a7b-b437-f8a436414113 | -6.0807 | -59.9465 | 2025-08-19 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f0aed2b0-31b4-35d1-8df8-7c83a99e1378 | -6.9715 | -43.5833 | 2025-08-19 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| cbe4d13e-9df7-3e0e-9a6e-94334c288944 | -13.1555 | -54.9357 | 2025-08-19 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 647.5 |
| b7e05064-67da-3f0c-95ed-1ab9c0852b0f | -6.0807 | -59.9465 | 2025-08-19 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 59c1fd48-73c7-34f4-8ebf-7b7fa89d88e6 | -12.5042 | -45.5788 | 2025-08-19 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 89e26a4a-b74a-393a-a073-939ecd6b0a8d | -7.0612 | -59.2358 | 2025-08-19 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ce49a29e-6b4a-300e-80e4-4f4faaa788da | -5.6406 | -43.4153 | 2025-08-19 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3ec4c30a-26fd-30c0-97c9-331d34fdaaf4 | -12.8795 | -46.0707 | 2025-08-19 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0bec80d2-7673-3b63-a3a0-d2c885df6d30 | -5.6408 | -43.392 | 2025-08-19 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 26b2922f-b82b-3867-87f1-e2b66d5edcb4 | -13.2567 | -50.7947 | 2025-08-19 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 322.3 |
| 649fe903-74ec-3dc9-b96b-591d709cda96 | -13.1746 | -54.9337 | 2025-08-19 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 272de212-98cd-38e7-a114-bd144e077c2f | -13.3537 | -54.4213 | 2025-08-19 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 234.3 |
| e1174a72-674c-3ec1-ab53-fa211fb9eac0 | -12.9173 | -46.1106 | 2025-08-19 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| dbe4040d-fd11-3d64-842c-2797406ce280 | -13.1396 | -42.7201 | 2025-08-19 14:40:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 101.9 |
| cceb0e25-e0a5-317c-9c06-a2320bce32e7 | -13.3534 | -54.4419 | 2025-08-19 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| c2e7a219-2e7c-3b99-ac9d-73585bc22e4f | -13.2179 | -50.8211 | 2025-08-19 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 765b28f1-b121-31d2-99c3-eba3a3d87cd4 | -13.257 | -50.7732 | 2025-08-19 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| be38ecc4-bca6-3b45-8059-bc3a29a3dccd | -6.9712 | -43.6066 | 2025-08-19 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| e9e9e220-7380-3b7b-acea-9d2531463a52 | -12.978 | -56.8413 | 2025-08-19 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7e9b0330-e56c-33ce-a1f7-9e20e9aebd98 | -13.1558 | -54.9151 | 2025-08-19 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 207.7 |
| 51cc8161-4281-3c27-ab5e-c832b1811d6e | -6.9527 | -43.585 | 2025-08-19 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| fb32d8fe-31f8-323d-af89-584acda5af41 | -3.982 | -42.516 | 2025-08-19 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 053b8ab1-9892-3d66-861e-d768c3ae9627 | -6.9339 | -43.5868 | 2025-08-19 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| f1c4e965-5f8d-364b-b88c-dc43fb8e1be7 | -11.773 | -51.7365 | 2025-08-19 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 390e56ff-1394-37e2-9434-2fd2cdd0fa25 | -13.1743 | -54.9542 | 2025-08-19 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6040c3b4-cb16-3119-8bb2-052da5ff5784 | -7.1482 | -44.6065 | 2025-08-19 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 550ee2e4-5892-3025-89ab-bab46c45adf5 | -6.5201 | -45.5013 | 2025-08-19 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| c332ae00-c84b-3303-a559-f4af1389800d | -13.1552 | -54.9562 | 2025-08-19 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 52a20e18-101f-3a2f-aacd-401b9d8fdc32 | -12.9968 | -56.8597 | 2025-08-19 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 64a03561-ccc5-33dc-a770-ecaecf6c2c75 | -5.7887 | -43.6134 | 2025-08-19 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| f4ed3b11-0653-3d67-9851-2be5edbd307c | -14.6323 | -54.898 | 2025-08-19 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f76677e4-0d57-3317-bac1-fd05051d085c | -12.9778 | -56.8614 | 2025-08-19 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1361366f-c471-364d-98d1-85046e82c514 | -7.6481 | -45.2673 | 2025-08-19 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 06a4aa30-84b7-326e-b7f5-af68038d7094 | -13.354 | -54.4006 | 2025-08-19 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| ed2d3817-076d-37a8-9f15-8857a3945b3a | -15.0386 | -54.8297 | 2025-08-19 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7992a379-89e7-317e-b9e9-07bbc9498c55 | -13.3729 | -54.4192 | 2025-08-19 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 684951d4-3e18-363f-9d71-05b31c21e311 | -13.2563 | -50.8162 | 2025-08-19 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 9ac88d6a-41dc-3e47-9178-405044d1065d | -15.0196 | -54.8112 | 2025-08-19 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| fc9c2f2e-bfe4-38bb-afa3-08bf61bcf48c | -7.0427 | -59.2366 | 2025-08-19 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 89850b30-fa59-3868-8556-ee033780ae0a | -13.2755 | -50.8137 | 2025-08-19 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 5ec3ca94-aba7-30eb-b8ec-10532858d153 | -12.9971 | -56.8395 | 2025-08-19 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 2a438a06-c593-3e11-88eb-3a152aa2b410 | -10.9916 | -45.6359 | 2025-08-19 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |


