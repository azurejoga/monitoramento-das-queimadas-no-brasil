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
| bfb2d5dd-feed-3af9-bd21-f314e39513fb | -6.35127 | -43.45501 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b0c8513-3a36-32f5-91d5-f0f1d8cd4a6d | -7.7277 | -46.29913 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5f12ac8-4717-3aa1-803c-d0d662c60336 | -10.27829 | -44.34422 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff030b1f-ebbb-39fd-84b0-8ec72cb37f1d | -6.44095 | -44.80394 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5885d09-c9ac-3a66-8b48-d6d9e2985277 | -6.24681 | -45.35244 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ecae3b6-1bee-3a49-8a1b-78e128b6f642 | -7.72126 | -42.5872 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 13468e10-6007-3ed2-9924-45e8ff2ed32d | -5.69308 | -42.84098 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9cac4ebf-e68a-3f84-95e5-9bc47aacf119 | -5.70946 | -42.63441 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dcf83d40-4b05-31e6-b1ba-4f3d8ed84cbd | -5.45732 | -43.16665 | 2025-10-04 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81f63a1f-8065-323e-a6de-46bf655f5d75 | -9.10546 | -44.39726 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c5474a6-7544-3231-ba61-2ea8385940d0 | -8.17815 | -44.14154 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6acc8202-8df7-3e02-8d3a-5db6163e2c33 | -6.29824 | -42.44223 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60b30e06-7023-32a2-863b-57ea3ae73c2c | -5.48751 | -44.10851 | 2025-10-04 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7994dc1e-76b0-3faa-a203-a7cdb44b2da0 | -4.88831 | -45.0659 | 2025-10-04 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37f16bd7-cd50-3796-b24e-edd688f432b2 | -5.40961 | -41.33881 | 2025-10-04 03:51:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 95c3d986-1353-3268-a143-ea168a190a1c | -4.6069 | -43.14844 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ab703fef-9604-39d0-bce5-e54f4128068c | -7.72693 | -42.6041 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e409918-6e90-3f29-849f-a36fcdf1cabb | -8.05565 | -44.80064 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35e2b6aa-2fb3-37f4-b230-c74e448222a0 | -5.25792 | -37.92732 | 2025-10-04 03:51:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f25c288f-cd5d-3388-b76a-d8e39abdf37f | -10.34037 | -48.16884 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe7792cf-eb52-38e5-870c-4fc70418930a | -7.72138 | -46.24292 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18a9a97e-32c7-3e80-9a93-62e90189b968 | -6.87294 | -44.50328 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d4bf760c-04a1-35ad-99ed-8356d4a5a4a7 | -4.61068 | -43.15381 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d6e42958-2a08-327f-87fc-1f0887ed3553 | -6.38419 | -46.5082 | 2025-10-04 03:51:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5a5554f-6cab-3eee-a4dc-072a73cd7973 | -8.71165 | -47.98378 | 2025-10-04 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ab18437-a28c-3163-b205-aff71884b5ef | -11.1288 | -47.85331 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c76e327-646c-3c10-b8bf-4c66d6f03c74 | -5.94274 | -43.29538 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 03d656c6-0d8e-30cb-b377-4d104c362f04 | -5.14551 | -44.80735 | 2025-10-04 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01786307-9ecb-31df-8783-c0a05bdb037b | -6.06128 | -42.51692 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ea4eca4-0705-3a1a-8484-f3ef0cfd22fa | -6.3645 | -42.8857 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9a02684c-f11e-3ecb-b70e-5919f840ccd5 | -10.32737 | -50.35453 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fc5053d8-139c-346b-9701-510601955c3e | -8.95717 | -48.68476 | 2025-10-04 03:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9846f88-df29-3d24-b43f-fae748ee94ef | -6.67767 | -45.92881 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc909431-74c6-38e2-a9c4-f53ac6bb9288 | -5.97927 | -43.48892 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f3958f7b-86dc-3215-a493-e5368bc84c21 | -9.34153 | -45.76834 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7147feeb-6c78-3239-b50a-4b8861a38249 | -7.04981 | -42.77166 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f495d36-1e94-3a52-b803-3e2872389e3b | -9.93465 | -50.23457 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 719f85a2-977a-352c-a89a-50e42676a1e3 | -7.73728 | -46.27657 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86f6f094-24ba-301a-bb72-ccfa0d683186 | -11.44677 | -45.13988 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34d3aa8e-9931-340f-a0d6-586a9cb21ced | -11.49593 | -44.994 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73a1837e-9aeb-30fe-88d9-c40d6d819085 | -8.97834 | -46.73027 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d210ebb0-268a-34ed-8e10-ff8a2cc1d289 | -6.72391 | -44.14845 | 2025-10-04 03:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0a72142-b450-3ca5-9e26-cc308f6eb388 | -6.6676 | -42.82838 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3058f4a8-288f-3f87-8174-0a0c4583712a | -9.94121 | -50.23593 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b824cbfb-0c36-30ff-88de-1e8ec58ad1db | -5.73778 | -42.92077 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f75e7c37-0a24-3bbf-8e99-a22d3318b227 | -7.80369 | -42.53878 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e83d6208-5bda-3ee6-bb57-56c671b93aca | -6.18608 | -43.59579 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5c09e664-138d-34d8-9d00-660de2de679b | -5.48156 | -44.10892 | 2025-10-04 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 81674a30-9033-33c4-bd1a-96872aec11d9 | -4.25272 | -48.568 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17887a84-1997-37fb-a132-3f0918b00fc3 | -11.47415 | -45.03458 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4e53ddb-9e56-3e37-9157-faa646b931ad | -6.87859 | -47.2336 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0e2065f1-b56e-324d-96b2-d7275b83d867 | -11.4994 | -43.49706 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbcd9c16-e2fa-39bf-9fdc-0904095a9ecc | -11.47676 | -45.02054 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6b00eea-7b61-3219-b544-f81b7257f14e | -5.40165 | -41.35027 | 2025-10-04 03:51:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38733924-845d-37cb-a139-841abef7ab9f | -8.06045 | -44.80154 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9cfc0bc-0625-3762-8dbc-3ccda05c179e | -4.71373 | -46.13211 | 2025-10-04 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50442a36-70a7-310c-a2cf-e0ff74d7084e | -6.69277 | -42.83647 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99c284a6-044a-3e88-b04e-73fdf32820ed | -7.79171 | -42.49922 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c82872bf-f996-3a71-bec5-e971e3570f14 | -10.06813 | -48.18794 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8082ebd0-b270-37f0-9987-f58621f12313 | -5.64782 | -41.23957 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 29574aa2-37e9-3c71-bc1e-9948529a91b5 | -7.72736 | -42.57659 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31a7f74a-75b0-3aff-a059-27f5e00f2a32 | -6.17511 | -43.92543 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02487b2c-d528-3df7-8cb0-8d699f936504 | -11.13365 | -47.8582 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43943f2b-dcbd-3f15-a8b1-2522b5db896e | -7.34487 | -44.35368 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5536ec5-478f-3692-90aa-37ac087b92d7 | -5.83932 | -42.85334 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 357d8c68-b13b-36b5-94a8-4c073ef531d5 | -11.13985 | -47.85598 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad866252-a2c3-38c3-bc50-597ddfb7559e | -10.04648 | -49.20888 | 2025-10-04 03:51:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e6a08b-9926-3700-b48c-97ef1769deef | -6.26973 | -42.4571 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d6823f1c-249d-352c-9158-1e3bfaf58c5a | -10.33714 | -50.32681 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9e3fdbb-0681-3237-81d1-3e05793cbcdf | -7.74946 | -42.52241 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 77082dbe-0fc7-3849-bb19-2ee86e5c3366 | -9.94663 | -50.24296 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ce2f01f-3ce8-350e-8475-42d4f51e9857 | -10.25205 | -44.9404 | 2025-10-04 03:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ca17076-7bdd-30fe-920e-1b86b6a74b85 | -8.22414 | -46.80433 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29116269-90c0-3f90-815a-78a251012384 | -6.19847 | -44.63847 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c042348-b708-3e34-b51a-e551bacbd5aa | -11.41472 | -43.48645 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbe94366-320e-3046-95a3-9b4ebd02b950 | -7.0563 | -42.78498 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4b7774c5-3c48-319f-a574-e56c12742ca6 | -5.14503 | -44.81023 | 2025-10-04 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af4c8f3-47e8-380f-b0ab-25e8c8a6aaa5 | -6.66044 | -42.83332 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0cbe53f3-307b-33c7-aca0-3993becc17f8 | -7.74374 | -46.30189 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8aed2d85-3388-31ae-9020-3884f91b9d79 | -9.95232 | -43.76239 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f56703c-5176-396a-b9b2-1e9d86c3d79f | -11.62092 | -45.03003 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e3e0fe9-65e5-3105-a521-fd0379d24a12 | -6.28992 | -44.05321 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ae0b4a4-425a-3d54-b39b-6d317b45815e | -5.94116 | -43.30442 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa1d87f8-df0d-3b39-ba4e-407f3eda2bd4 | -7.35523 | -44.34996 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62486907-569e-37b6-8460-3eb9570b8774 | -6.12641 | -45.93343 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51ad29e4-31f6-3c84-b566-4675caf1c16b | -7.50893 | -47.56418 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dd94a52-b465-3de8-a19d-f263eb067072 | -9.94218 | -50.24499 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5ad1fd8-864b-3415-b162-bc6078d18eb7 | -6.6655 | -42.82947 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 507475bc-3c45-39b7-9c83-4a1875db8eae | -9.90401 | -43.73215 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c45a6958-a956-34a4-98a8-9aeb71f84aa5 | -11.17109 | -47.75177 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 574ac27d-fb5c-3995-be8b-eee62ad02a90 | -5.41037 | -41.34698 | 2025-10-04 03:51:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fccf7e1c-1b9c-3a5b-9a25-7d85801b2c2d | -6.17042 | -43.92473 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd9419b3-0843-3026-bd20-f7c76d5d20ed | -7.79604 | -42.54959 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8dc9520-721d-3696-8bdf-dcbda83648c3 | -6.24345 | -44.23656 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b9ac60a-faff-3786-85ed-52b2f608b56b | -11.41888 | -43.48721 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e686bddd-cfe6-3028-881d-531e548df977 | -7.78746 | -42.57532 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 90a57de8-73da-3c9c-92cb-dc05cb18436d | -5.74071 | -42.9302 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 03d8140f-d235-3a81-bf3b-c198b8c17d35 | -8.81616 | -44.82248 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 505b6654-074c-3c8a-ae3b-978d6c17120e | -7.88713 | -42.60008 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62ce167c-1db7-3d5e-b7ed-ae985df40ba9 | -10.2746 | -44.33887 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
