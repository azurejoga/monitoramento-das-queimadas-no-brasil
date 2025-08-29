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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a41e9b3-48c4-31ca-b32b-7c43d2c3dba6 | -8.44855 | -43.71519 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e4055f-770b-3d3b-ad34-2a2cf8d4f334 | -5.83772 | -45.30764 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 085d31c8-3e16-37ef-8dea-92cf96eab618 | -7.56292 | -47.49705 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbee8a37-3b84-371c-8be1-991393d6916c | -9.6 | -40.35914 | 2025-08-29 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7e965463-c4ea-3094-835f-8f00fb30265e | -7.22163 | -45.44723 | 2025-08-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 775052d9-41a5-3889-978b-4ad71fe69353 | -8.70249 | -49.93712 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bec7a99-ff1b-33af-bf8d-053578473936 | -10.9543 | -46.89227 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9609b60b-c679-3d32-a370-eaee87d376f2 | -7.04807 | -44.36994 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93e399b3-0d4b-39ba-993f-6f70dc707c28 | -6.51371 | -43.00115 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2149df5-ea6c-3274-b5f1-c411269b96a7 | -9.42899 | -47.64978 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae592f52-88ae-3004-9410-5aa9a358cdc6 | -10.94462 | -46.85406 | 2025-08-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d225580-3cb2-32db-9774-0e41bcf6b604 | -7.73036 | -50.30062 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7986c36-5e05-3e44-a629-a8e163e562c1 | -6.14502 | -44.43314 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94e0c478-df4c-3e66-b98e-3d40e5f0fee7 | -9.46176 | -60.31242 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a4dc987-d068-3266-88d8-ff5dc02cf4ef | -10.02318 | -48.0803 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61c45ac0-983e-3f7f-9bed-c09cc2dc7ddf | -8.0972 | -44.99726 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bc75315-d112-33ca-9f21-7302ad7950a0 | -12.91649 | -48.1328 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba0bdc86-f373-3084-bcc1-ade62573463f | -11.64165 | -46.38221 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ce457ce-edc5-3b8e-9d5c-dd270f2a1b05 | -9.81984 | -44.90214 | 2025-08-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0aa681e-d9ac-3030-a868-9f0e9280a20e | -7.19683 | -44.05236 | 2025-08-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30c16d4c-0f7a-30c7-b283-78ae1ff837bc | -8.10509 | -45.02725 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6269fdfe-4975-33d2-ad47-5ee25d56ed46 | -6.16176 | -44.17608 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e73e4e27-415f-3ea7-882a-02fe999578ad | -11.90793 | -46.71512 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3287e2d-e0c8-3922-8bc5-a17242514a13 | -6.8814 | -43.60293 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05b57997-2f9b-32a0-87e9-20ea67b1a9e1 | -7.02506 | -44.67497 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a84d6b9b-6ff5-3780-96b2-63fb67dbae0b | -6.3866 | -45.23144 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 0cc36ebd-7ec5-3a2b-b624-7c94c6e9d1fa | -9.15516 | -59.57414 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12bd9b80-99d2-33cc-9fa8-28f2836ddaa8 | -12.8595 | -48.14936 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 614da40b-b720-37ad-a5e7-1e71f0466df6 | -7.54788 | -47.5025 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79c2422e-b486-3e48-995b-6d07e3a86e82 | -6.49511 | -43.5313 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cebbde55-45c8-3881-bece-2a1310da1714 | -5.84331 | -45.16294 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d7a933d-9367-3b5c-8301-994b6d4f8e2c | -12.90877 | -48.13579 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d9f9c33-599f-39a6-ac41-6458a475ae88 | -11.08033 | -44.77778 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a35d2a2-1702-31f7-bd94-0b1b3a640b88 | -9.52059 | -46.54103 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd55237f-89d9-36e4-b013-52fee71c27e5 | -12.15861 | -47.18756 | 2025-08-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efed98e7-b11f-330b-ba79-dfa769d5b253 | -9.55342 | -45.84791 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2671ddfa-bc1e-3df4-961d-92236c621619 | -11.32428 | -43.56421 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3cdf16e-1ed3-37cd-a0b4-382d61c13eea | -10.02553 | -48.06464 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad9d7850-021e-3735-aa50-631abebb23c2 | -11.12329 | -45.12072 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 002fd25a-0a4d-3a93-aec6-adbdf2ae490f | -7.5693 | -47.50195 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a960767-fa56-3fc6-b9ba-4b0daeda0535 | -11.34285 | -43.53166 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9611ad19-9b3a-3f02-832d-a0065c290c1c | -10.02436 | -48.07246 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25613456-ea92-3633-8a04-d720839a108f | -8.69633 | -50.3878 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e0d9d3f-ef46-35b7-b5bd-98d8b61d75e8 | -11.57609 | -44.65398 | 2025-08-29 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e8fa778-917d-3e8f-b962-ffcee6cd904c | -12.40254 | -46.4963 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a41c8fe-4e8f-3fbf-a801-59e45e404c1b | -6.10544 | -43.31131 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20c28646-15cc-3d9d-86ae-9403f747acae | -11.07928 | -44.75319 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23163052-76d1-33a4-b806-978ccec31489 | -7.1622 | -44.1461 | 2025-08-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18e549ad-3f2c-3d4f-9c84-1cb819ca33f2 | -12.69736 | -48.19847 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f2ca662d-4e1b-3559-b472-21f07bbae44a | -12.86831 | -48.13871 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a44d33f1-1343-3a67-a3ae-cbfc5e95ea52 | -6.13821 | -44.41852 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 054fee46-2bd0-3a0d-8637-10eaf3fe2647 | -6.55036 | -43.9197 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 64d4fe61-cb42-3992-aa99-f534c0cc5a50 | -5.91853 | -44.9752 | 2025-08-29 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f4f6845-26b4-388c-8529-a085a6e3f921 | -6.77525 | -55.48803 | 2025-08-29 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14ac6271-39d3-33b0-a09f-2160be433cf9 | -10.86357 | -60.8117 | 2025-08-29 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3152905b-fec7-36ee-bcbf-5be4dc093928 | -7.73032 | -50.27927 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc6b5608-6710-3269-b314-74519446d8fa | -12.67315 | -48.19044 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2783df9-9e58-34cc-a29c-8b2e32df2b54 | -9.45037 | -60.56077 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e44041ea-7417-3c54-bab4-4d1346b55e18 | -7.08004 | -44.29396 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68584fda-ad53-3124-a788-e946c83f37a7 | -11.32098 | -43.55362 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4a1a637-82a6-3b51-bdcc-3247e4a34eef | -10.62243 | -54.90928 | 2025-08-29 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84fecbcb-f615-3edd-a4e0-2bc7d433ea6f | -11.29319 | -43.54956 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51949a1d-1d2e-303b-ae14-7ec6a51fdbd0 | -11.32824 | -43.56981 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a48be0-f645-3281-b0f0-ccfb46e5e1f4 | -12.82381 | -48.10019 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2bdc4858-f8d3-300f-afe7-95750d6bf7da | -6.50542 | -42.93016 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d8b59da-2ec5-3980-a2a5-ef31254b5233 | -6.72435 | -43.57597 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36d980ae-30c8-3da7-a7d7-a8cd1752c21b | -10.02842 | -48.06907 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5437fa55-ed47-3a32-af1a-be8ecef899cf | -12.85597 | -48.12944 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 803880f8-9600-3bf7-9b3f-69284cf249a1 | -11.31466 | -55.22412 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4de6ba85-2a65-38f5-8662-96c711116e6d | -6.08881 | -43.99629 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ac5257f-52c7-3467-ac11-72e8f2c9c767 | -12.81022 | -48.16864 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9aa21f80-e07d-3029-9efb-22cdb3bfc9b8 | -12.09185 | -44.72593 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 461ea5b9-aeaf-3c2e-812d-cc18eeabd753 | -6.19514 | -44.00813 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c607ec95-cc80-3acf-be0e-7c302c1d90ab | -8.47974 | -43.68477 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7102cf63-e5e9-338e-976d-44036a9c3950 | -12.89329 | -48.14219 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c640b637-cbd3-3170-ab22-9701c7137cc0 | -9.24699 | -59.78249 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f4a00cc-6f76-3865-a714-37c29ca6d45f | -9.1525 | -59.58852 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 140a0100-e3e3-304e-a257-2a9b50ca6a98 | -11.06401 | -44.77328 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0850d8bc-1158-3e7a-bb7c-1e911ef89910 | -7.2178 | -45.44646 | 2025-08-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae9cd236-0626-3df0-bd9b-f91f7c1bd5f2 | -8.12493 | -61.21429 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4f08343-68f3-30fe-816f-7b155039bc1b | -11.94346 | -46.71085 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9458638-71f2-3ac2-93e8-8af5e011a806 | -6.34399 | -58.18577 | 2025-08-29 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70144120-518d-382c-b5ba-3e9dc4396b7f | -11.35145 | -43.56444 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8772d69-158a-3b47-b4df-0a15593a33fd | -8.13782 | -61.2121 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5eaecc6-115b-3284-bcee-d1cb570a1364 | -10.9877 | -46.85839 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33b779a9-7376-3ad6-8349-5cfb0643929d | -6.86685 | -44.38905 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fab1150-7bb1-367a-a40b-150a4c2e3061 | -11.61903 | -47.30743 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e98b908-48bc-3b39-944e-76f4396a7a5c | -6.49078 | -43.53069 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 371d7488-91a9-32f6-814e-e849c2d2cbc7 | -9.15312 | -60.93401 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2c9a017-c95a-39b0-b046-2759f69c83c0 | -8.29193 | -61.40557 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 705c18ae-2321-3c9a-837b-3b1515933d18 | -10.4566 | -57.95577 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73972bef-9a84-3b64-bcce-922fa3d30433 | -10.45925 | -57.941 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d57995aa-8a15-38fa-a691-7b3311d2c42d | -13.07094 | -46.35351 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e5d4527-ece3-314a-b61b-9f52fd7abb36 | -10.37986 | -48.33981 | 2025-08-29 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44899af4-b4a8-39e3-be9b-44e141c09d46 | -6.34129 | -58.18446 | 2025-08-29 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfc82982-6255-3972-a089-7674e0868d0e | -13.18219 | -45.27835 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b714d115-b84b-3c11-972d-279ed180027c | -9.46409 | -60.5631 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d5960ce2-741a-3514-98aa-353cbec354ba | -9.68338 | -48.31187 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd3cb273-4b5a-3471-82a2-fb1c02c29a27 | -12.69973 | -48.15721 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac034262-42d4-33d0-a7a4-e4abe04de042 | -8.56334 | -51.31694 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
