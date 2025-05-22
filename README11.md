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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 776d2068-bb1d-3bf5-b5d5-4895c967eb0d | -7.80319 | -46.21396 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b3e5759-2f3c-317d-b876-be66ea4dcb71 | -10.09439 | -47.09975 | 2025-05-22 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca5cfe0e-e521-33a8-8644-3aa64546865e | -11.5784 | -54.57199 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90e4db35-9a30-3857-b9c8-c0f7219c38af | -11.64232 | -48.10411 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 13a5573b-0d2d-3b1c-a298-68096b03f08a | -11.2968 | -53.98597 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1f87d8f1-44e0-3797-8467-17b297136b7a | -13.53243 | -43.67907 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 105e919f-8bed-3044-b59a-1616a205ec7c | -9.67692 | -50.95558 | 2025-05-22 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5bacdbd-d04c-3ea3-9a3d-d9635f175ae4 | -12.84098 | -47.39647 | 2025-05-22 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 410da5f9-941a-34d5-87fc-c7c427d432f8 | -8.47761 | -49.60352 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2096d99a-7dc7-3b96-901a-65b8c6f5f780 | -12.33809 | -49.9761 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc2b8b4e-7da0-372e-b764-04c5d3171ac9 | -12.34591 | -49.97484 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fde7166c-c415-3d3a-825d-77faf6421bdf | -10.65687 | -49.44625 | 2025-05-22 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b5f226d-4b08-3385-99df-63a75170e1c8 | -11.88081 | -47.05218 | 2025-05-22 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16e17909-ac44-3575-bdc6-87dab1a03f97 | -10.65717 | -44.49358 | 2025-05-22 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4a38494-1097-38ee-81a2-f145425d37a5 | -11.57205 | -48.37686 | 2025-05-22 04:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2946ae7-8fba-3e29-a136-f39e8838623b | -11.5609 | -47.44901 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4d352e7b-cb2b-324c-bc51-f9f4448a7ba5 | -9.37134 | -48.40513 | 2025-05-22 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e94e2b61-08c6-3cdb-8a76-e1f38c1a4e54 | -11.5535 | -47.45155 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d49632b9-8d4c-3295-9769-b55707c164b3 | -8.7457 | -49.74746 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 54a86278-39e6-331e-b829-19a185d8fe75 | -9.79709 | -48.26277 | 2025-05-22 04:21:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a44dc66-79d4-3cec-b47e-a5418dab7a0f | -10.35384 | -47.81889 | 2025-05-22 04:21:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a39b215b-2f24-3d25-b0c7-74ee9f9fae8c | -11.57388 | -54.56785 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ea86f5c-3463-3bbb-a6c9-1b586bf7b75e | -10.82365 | -56.9636 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec8c3dff-69e2-39b0-bc34-a346dd975aa7 | -10.67885 | -57.60365 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3e87e3d-d272-368b-ad1d-03d08a422401 | -10.33045 | -47.02187 | 2025-05-22 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5239b5c-c54a-322c-a1e7-7a2300381778 | -11.89269 | -49.20205 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb678bf7-cdc0-3964-8d25-9d53581176c9 | -11.29443 | -53.97644 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f0dcdf0-b0fe-3821-8b1a-2ebc5f2f4139 | -10.03157 | -48.69744 | 2025-05-22 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a5619a74-5692-3279-b102-0d3eaf1b02a6 | -11.5699 | -47.45808 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 77196dcc-f941-3d80-81ed-15d76d6b4d32 | -10.3673 | -47.97587 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1833eed4-4ead-31e1-898f-704d995f0a60 | -10.37777 | -47.97763 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5c74e7e-f744-3037-adfe-be7254ab2c12 | -12.35557 | -49.98599 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e7583e1-c45a-361d-a5fd-b62b619dd896 | -10.65764 | -49.44173 | 2025-05-22 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be18c15d-f214-3100-a7af-4384048563ea | -11.5603 | -47.45269 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 628ec267-8bf6-3137-b16c-eee449df3db0 | -9.01645 | -47.74037 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a782531-4d2d-3eb9-8a3b-466b739963b3 | -12.08196 | -47.33897 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| effe67d7-2f56-3807-aa97-ab23e14d0e82 | -9.72454 | -48.32542 | 2025-05-22 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f4697e3-aadd-37f1-871f-119a2a51857b | -11.79799 | -49.33989 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4087850d-9e99-39e6-b056-7def3e8b2dd3 | -12.94401 | -46.54112 | 2025-05-22 04:21:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d7421fc-91cb-3064-a960-e928c0657aab | -11.86004 | -52.27823 | 2025-05-22 04:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8e0403f-9ddf-3fa5-9721-841037d6a12c | -7.96976 | -49.69096 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b85517c-ae53-31d7-8e30-908a868d3273 | -11.64643 | -48.10084 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8580be5e-611e-333f-8596-b21c9df1541e | -11.29785 | -53.98021 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 421cf6b6-b3b9-3f20-89ba-aec714e8d761 | -9.03927 | -47.75569 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c9adbb8-4d4a-336b-b159-bf8e3713025f | -9.04056 | -47.74791 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eab6bd44-c467-36bf-9060-f8284cd20923 | -10.35038 | -47.81828 | 2025-05-22 04:21:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72c8c063-2fd4-36cc-af7e-66e5c3215b04 | -11.70511 | -47.78608 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12c164fc-5dc8-380c-b8e8-bedafb2f45ee | -10.09837 | -47.09665 | 2025-05-22 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f68f2bc5-2f02-3746-9678-09d479531cb6 | -10.36381 | -47.97529 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b16c98ee-7c43-3128-8d2f-8d03085147c3 | -10.62064 | -51.79419 | 2025-05-22 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4339af3a-1ee4-3f76-b029-68119eb5730a | -13.5194 | -43.69369 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa5b8479-353e-3682-8b0a-898c8ca750ef | -11.56935 | -54.56381 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b5b41a0-a8ec-3696-8eda-b671f8d75cf8 | -12.34887 | -49.98006 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52a72c6f-bb4a-3fd0-a45f-90944bee91a5 | -10.87864 | -45.0737 | 2025-05-22 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc977a8a-3f03-37a6-ab04-fb4dcec580c0 | -7.94896 | -49.76503 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 274e5f43-5745-33d0-b658-47c4e5c57454 | -11.11922 | -54.6629 | 2025-05-22 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fec36fac-a120-3390-8d87-2f20a4966043 | -9.01932 | -47.74483 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc39ff6f-0b0f-34c7-9fee-a2ee54fb7ae5 | -8.75349 | -49.74883 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8deb86e-5b9c-38be-be3c-975aa32bc903 | -11.57085 | -47.45408 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 74e6337c-2c82-3838-abbc-1c5077b2eab0 | -7.94983 | -49.75996 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c26bb4af-ff03-3519-9415-f3221709de84 | -11.79578 | -49.33691 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2922bff-6321-34aa-b428-831f30d729ea | -8.06397 | -47.12384 | 2025-05-22 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13d8fee8-ec25-3fe6-b5a7-a7cd8b5f5b64 | -9.96573 | -49.80833 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 428bb122-bc44-3692-b541-d81269c1f578 | -13.53183 | -43.68314 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33579eba-3993-37ea-9827-f2f4a7749d24 | -11.57025 | -47.45773 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ca5a86e4-b377-3b84-b68b-5b05c0986bd8 | -10.82323 | -56.96222 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1da0d07f-b823-3903-bc00-6635c9ab988d | -10.712 | -48.80871 | 2025-05-22 04:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d8dfd90-04f0-3e77-91f4-f8ee692f6173 | -11.2929 | -53.97932 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc50e3c4-effd-3837-925d-fea7f7c70fa0 | -11.5637 | -47.45327 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1a2b7cb5-c54d-3590-a216-48ac782043fd | -13.52294 | -43.69423 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e7a7ed-3bd9-32d5-b0d4-47d39808c477 | -11.56489 | -47.4459 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cd919c6f-7d16-396b-8266-61272d52c987 | -13.52889 | -43.67853 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7506702-e5df-3f23-8fc2-1139f227826a | -12.11183 | -49.29828 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7e7e05e-d510-378d-a44c-02a5241f39cb | -7.20708 | -45.35237 | 2025-05-22 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f11ffc5e-f323-3ff6-aae7-3c063b43a283 | -11.29335 | -53.98215 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fd0fd786-d7e2-372f-9f68-ed2eaee74151 | -8.60463 | -49.51326 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aebba1a-3351-36f1-b624-3111cd93a21b | -8.91112 | -50.02232 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4eb704f-3520-3984-945a-b36f791cd94b | -12.08415 | -47.34684 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d07cf71-112a-3455-9892-49ed864411a3 | -12.34262 | -49.97216 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 121f9dfa-1502-354c-9952-81b44f48459d | -10.82928 | -56.96331 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42ca7e08-e754-3ba0-bd45-de4a4d96ab18 | -9.04613 | -47.01638 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b9f237f-4c4f-3998-8c79-65f598c22b86 | -11.6026 | -47.62308 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55e417ac-aaaf-35a6-ab50-ecf7302379d9 | -11.57545 | -47.4473 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb1d56e7-7e36-3893-b045-62fedce78290 | -10.93501 | -55.31034 | 2025-05-22 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| f061522d-35dc-3ff6-b3dd-6b94cddb3699 | -11.67046 | -54.94071 | 2025-05-22 04:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31f09e69-4ca8-32b5-a1f7-0237d8732fde | -11.57365 | -47.45829 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ad1ea66e-22f0-3105-99fb-c7c510955e1f | -11.29186 | -53.98504 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f148febd-e4ac-3d26-b8fd-63f9a038fc47 | -6.63609 | -55.01363 | 2025-05-22 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c85554a-87d1-38ac-a03e-0f15e630c06a | -12.34807 | -49.98463 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fee7ef45-7fd1-3ecc-a3a0-1d776c628fab | -8.79094 | -49.0685 | 2025-05-22 04:21:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23403df8-0142-32eb-900e-f9996e8fccfc | -7.80262 | -46.21754 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f704a567-f88d-3e08-ba19-506a5d900a14 | -11.57049 | -47.45443 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4d4c9e61-cbfd-3b2e-a1e1-d9a958c68efc | -7.94664 | -49.76282 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4f72ec8-5deb-35f9-b751-6c87e6afeefc | -9.28013 | -50.68741 | 2025-05-22 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b18125c-8e0f-3e9c-86a5-f428414dcf49 | -7.23746 | -44.71145 | 2025-05-22 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fa811c7-d5d1-3f50-9a0b-898a9a2969cc | -10.93898 | -55.31542 | 2025-05-22 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f00c8ee1-f81d-35a4-949d-5f37dd235499 | -11.57145 | -47.45041 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41abf735-f251-33a4-b022-d13be2ff03cf | -7.46713 | -47.06095 | 2025-05-22 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 669c1e7e-32b4-3770-ba93-bcff6300b298 | -11.24468 | -49.49603 | 2025-05-22 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53b4872a-9a53-34dc-b461-3c80cbd00f81 | -12.34215 | -49.9742 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
