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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5a894d-e988-32b9-a613-8dc582afe419 | -19.94526 | -41.64773 | 2025-09-28 03:40:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 05645fd8-1401-31a0-8e32-482a1d9187c1 | -17.18828 | -43.38847 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c87f2eb-da41-3a5f-beea-1fa6324651ef | -21.35482 | -45.78559 | 2025-09-28 03:40:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22f03ded-166c-3318-90d1-7665283f23cf | -17.18116 | -43.37654 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eacc1c12-f538-3dd1-b1fe-81147904c4c0 | -18.06336 | -42.39709 | 2025-09-28 03:40:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5dfa3fc8-46d0-3882-8cd5-aeaf28b3cc30 | -20.12315 | -41.7158 | 2025-09-28 03:40:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2561ae11-ff63-38bb-9a99-77c79cb952a7 | -19.20487 | -43.9776 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8643ddc2-7de6-3ed1-bc23-708cf473c1c5 | -17.71913 | -46.70801 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e584e859-01fe-37f2-8a04-2381797dbe31 | -19.66159 | -45.97651 | 2025-09-28 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4fe96e94-9511-3c5a-a23b-78c26f660401 | -19.98547 | -41.44898 | 2025-09-28 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| fc0e0af5-cd72-30ab-8d69-985624cf9fe3 | -19.32525 | -43.82077 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c16bde9f-4da1-3cd3-8195-de4e718f8368 | -17.18027 | -43.38112 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea78c5d9-8857-330d-94ac-aa23b6e83f3d | -20.16485 | -41.73009 | 2025-09-28 03:40:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1955ac41-8585-3276-b91a-6529efca9ad2 | -17.71827 | -46.71203 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92f788a3-c5db-3b5c-9815-589e3ec18c76 | -20.41081 | -46.46569 | 2025-09-28 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7403a5c3-d730-3f7d-874f-312d50ee90c2 | -19.94427 | -41.65312 | 2025-09-28 03:40:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ec9f27df-475b-3fbe-b463-e8c861598369 | -19.32091 | -43.81911 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbd2643d-f1e5-3c8d-9127-bad1b9e2463a | -19.32846 | -44.16698 | 2025-09-28 03:40:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a1b9c3f-1e00-3119-a88e-e5fe6720b594 | -18.05914 | -42.39644 | 2025-09-28 03:40:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8b5bc495-dcfd-3de8-9b58-e04f34e06d90 | -7.816 | -47.0224 | 2025-09-28 03:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0782b18c-e45d-34be-8705-25f31c5055cb | -5.7583 | -42.8447 | 2025-09-28 03:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| ff7d65a7-2a6e-311a-a59a-bca5c05692c5 | -5.7396 | -42.8461 | 2025-09-28 03:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 7fcde935-a6be-360c-9e8e-d8e79783e15f | -8.1611 | -46.4122 | 2025-09-28 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 69b13bbb-a002-3f7c-aaa7-4663b48879a5 | -9.6512 | -62.8336 | 2025-09-28 03:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 7e8c3dcf-0410-372c-9ff2-cfa3a4579232 | -8.1799 | -46.4104 | 2025-09-28 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| edd56cde-5ee0-31e3-9d80-2c2a546455b5 | -5.8149 | -42.8167 | 2025-09-28 03:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 87bc9875-cf5e-3602-8000-d0b04bf64a74 | -7.8163 | -47.0003 | 2025-09-28 03:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cf18c034-a721-3eff-8c54-8ca092b5d3a8 | -12.9918 | -49.4448 | 2025-09-28 03:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c1decac1-7196-35e1-b683-76ba5edd7338 | -7.7972 | -47.0241 | 2025-09-28 03:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9e417a9b-6018-3d6a-b5ed-cff1368e5244 | -9.6511 | -62.8526 | 2025-09-28 03:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 127.2 |
| a4209b8d-26ad-397a-bcc9-312b9bba877a | -7.7785 | -47.0258 | 2025-09-28 03:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| df1eabbc-97c6-30e0-84da-b53f9cdfc662 | -7.7975 | -47.0019 | 2025-09-28 03:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 16131f2b-53e9-352f-9f57-09027f5c65cb | -16.9667 | -53.6975 | 2025-09-28 03:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| efc384ee-9faa-3739-aaaf-3e9c714fefea | -2.5772 | -48.4146 | 2025-09-28 03:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 56a01f2d-3450-3d57-8539-eb5949207eb1 | -12.9165 | -45.1448 | 2025-09-28 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 78bffccc-a684-3cf6-bdfd-ee7ca14a8108 | -9.6511 | -62.8526 | 2025-09-28 04:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| ab6d1f85-7cb0-3933-91f9-e486e1ab6d03 | -12.9161 | -45.168 | 2025-09-28 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 85b6ada6-f7cd-3982-93b3-f485a89a4ad9 | -9.6512 | -62.8336 | 2025-09-28 04:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c1a9fb45-f9fc-3dc0-be88-d5891d7d6d93 | -9.6324 | -62.8534 | 2025-09-28 04:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 56ec067e-47f9-330b-969e-f0c915e0babb | -11.9846 | -47.8865 | 2025-09-28 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 21346ec8-eed5-3891-a769-e0b5a8270890 | -12.8967 | -45.1711 | 2025-09-28 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| f474a75b-32ad-3072-ba69-d840e192fd12 | -8.1611 | -46.4122 | 2025-09-28 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3d807abe-575f-3ced-8cfc-c0de097b76c7 | -12.8972 | -45.1479 | 2025-09-28 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ed9d7752-64e8-38ee-b924-0a5399a3e611 | -12.9918 | -49.4448 | 2025-09-28 04:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5d2b3832-d6f4-3d12-9175-ee7c3cb041b7 | -3.36728 | -39.19948 | 2025-09-28 04:02:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2dc06855-bf3b-31c2-83c6-aee08a66cd9a | -1.40512 | -48.05423 | 2025-09-28 04:02:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b917c9c1-a6e9-3c30-9f47-97b6b311efc8 | -2.90792 | -40.49179 | 2025-09-28 04:02:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15816f60-fadf-3914-99e0-f96250dfc0e0 | -3.42892 | -39.02494 | 2025-09-28 04:02:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1ea7b81b-2096-399b-b336-53d024bb9714 | 0.275 | -51.41027 | 2025-09-28 04:02:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61df5abf-8caf-3a4e-bca1-09f36e6e337c | -2.90849 | -40.48822 | 2025-09-28 04:02:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9706996a-e22b-309f-9669-9da69c2e5fa0 | 0.2808 | -51.40285 | 2025-09-28 04:02:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ccdb2549-bb32-3ee7-87cd-aab664e79cf0 | 0.27441 | -51.40497 | 2025-09-28 04:02:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0590b72-e1b4-3ac0-b8b6-a4803e200150 | -2.97795 | -39.93096 | 2025-09-28 04:02:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca8583b1-4bb3-31cc-a3e2-1a9c0eaba685 | -2.98025 | -39.93127 | 2025-09-28 04:02:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d013640d-0c70-383f-882f-6ea80619955a | 0.28124 | -51.40378 | 2025-09-28 04:02:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee9a8d48-92f1-38be-a935-92931055ac5b | -9.43974 | -43.70144 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ace4a212-aea7-3cf5-84a3-d395b794ade2 | -7.21103 | -44.5324 | 2025-09-28 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f051895b-f6a4-3beb-ad95-fc35bfe6987b | -5.81526 | -42.81819 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 6c42361d-0c1e-306e-a3fa-46d77e50b808 | -7.77638 | -47.02792 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8782a232-a2d7-39d0-a99f-267868123ff6 | -6.29275 | -39.82379 | 2025-09-28 04:04:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48376a2d-9a55-3d34-be2b-b1f1765f5c49 | -3.32433 | -52.53682 | 2025-09-28 04:04:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5ef109d-0e3d-390d-abbd-30888ae7e8b5 | -7.70321 | -41.29266 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 752c66ae-73e4-369c-a811-5275bd23ef0c | -5.71481 | -42.6564 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b71fbcfb-5f5c-3dc5-a9b7-18aa65667168 | -9.22024 | -46.78274 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f57ab76-3dfb-3085-87c0-4df58fb2b045 | -5.80804 | -42.81715 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aaa6d7e5-c9bd-3826-93fc-008fa0e470ba | -9.97792 | -43.61377 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30f11754-b1e1-37f7-8333-2dbb67465172 | -7.40101 | -44.44726 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddb0ebf6-120c-31f5-9f47-283e2f439723 | -7.42236 | -40.07691 | 2025-09-28 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4ef3f059-7f71-320c-8412-2729737604da | -7.35197 | -42.10732 | 2025-09-28 04:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ccced64-618b-35fa-b8ac-57d4d8829e82 | -6.45322 | -44.2225 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73170613-90e4-3fe7-ae19-c5b92fa30469 | -2.93211 | -48.02055 | 2025-09-28 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97942c88-01ad-38e1-b987-244cfbef9711 | -5.52212 | -42.73615 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e73fa467-6f67-322d-8564-ba6af0dde561 | -3.20925 | -51.27901 | 2025-09-28 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e705fdd-2148-3451-a5a7-9bf2b844ce4a | -9.22099 | -46.77853 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c009e6cc-41f8-324d-9e1d-640cc1bd5d4a | -9.05364 | -46.73034 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f487707-595c-320a-bfff-7bca89cce8ac | -6.61872 | -43.82856 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f2911c9-e1bf-3784-b4ea-372f988dbbc4 | -5.91396 | -42.94331 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0d4ea007-d7b4-3404-a7b8-34bf8e242961 | -4.91579 | -37.48654 | 2025-09-28 04:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b90cb541-9210-325a-8f68-33b0f1b8996b | -7.43624 | -43.03341 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f42f0d2-799f-31af-a338-430bac54645f | -5.80376 | -42.82076 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b0928e5e-ca90-3b8b-b4d4-3d82851c5d12 | -5.89847 | -43.2931 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fff76f3-3f71-34bb-a268-a674838ce9d7 | -7.70378 | -41.28912 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a53ab3da-63db-3cc3-852c-0680c1409253 | -6.69356 | -44.5803 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4016bdd6-44a9-36f0-addc-f7b8d8bd17ad | -5.75511 | -42.83934 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 64c5218f-70c8-3856-83eb-46d2457f8df0 | -6.2558 | -42.46133 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 081af062-36c3-3491-a084-d0da9712e6bf | -6.06793 | -42.44067 | 2025-09-28 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 98992080-71a2-3ea6-8d77-75f435ef97d7 | -2.98289 | -49.54395 | 2025-09-28 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dee2ff0-f457-3831-b6c8-3c48371f074a | -8.83313 | -46.20683 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3ff114d-b68e-3e0c-b856-580126a402ea | -4.15053 | -40.00421 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 227fbed0-ddfc-3914-a9fd-81870eb97ec6 | -6.54683 | -44.14281 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 371f4106-5432-3ec3-b0e0-db754cb778ed | -9.77333 | -47.76312 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2387ad7f-523f-398e-9042-6965d77ef1a8 | -6.38815 | -42.94715 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7522342b-f42e-3e0b-86d6-5fc43163e6e5 | -7.75844 | -45.742 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e969aef-d962-3aa6-85ed-2ea7acec38fd | -5.2383 | -38.48867 | 2025-09-28 04:04:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 468945d7-4aa1-3968-988b-c5703afa912b | -6.00045 | -43.92762 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8fd0f04c-c575-3bff-b9aa-555df99efce4 | -9.32034 | -48.95457 | 2025-09-28 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91b5a03f-34b1-3ca8-a8a7-86e93df16659 | -5.9097 | -43.67941 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bb9b89d-cd82-3a28-958c-52c7cf8f9726 | -9.0062 | -47.84008 | 2025-09-28 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec8c3dfb-1d06-353e-9cad-776db079837f | -9.0457 | -46.72456 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cac2b8e-356e-3b7d-b152-19ebf39f8ff7 | -5.59924 | -43.38208 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README25.md)
