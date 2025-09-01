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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81d94eb3-6271-314d-8904-91df04ff203d | -10.02372 | -48.36516 | 2025-09-01 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d90c306e-ac40-3b96-a7d7-259366b8915f | -11.37049 | -43.59077 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c444a95-c283-301b-a5fb-edacc47d862c | -10.66689 | -46.26467 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2456be40-6fd3-3ee7-8dc3-c57055a3ac43 | -6.2922 | -43.6268 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85884b14-6c29-365e-b6e8-ffaeee34593d | -5.82542 | -51.37788 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 458e8d8f-0928-3085-b5d1-deae90898e26 | -6.46736 | -41.74876 | 2025-09-01 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bab68ceb-7225-3921-a1d5-bee160e3e98f | -11.81231 | -46.41906 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 531fc621-4210-3913-aebb-3a5da9728340 | -7.55119 | -46.11404 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5649fc6a-c17c-31da-ac33-96bc9e7d6317 | -11.36956 | -43.55386 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ced05ac-ed90-3e61-9a56-1db9e4cf255a | -6.09331 | -43.19088 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 937f67b3-a5e0-39cf-85f6-c4f109d15874 | -8.19942 | -42.30392 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c08cfe9-86a4-32a0-a780-5b63ed5dbdfc | -9.15424 | -47.9496 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6078ae4-edd9-35ae-a729-0e09e6013c2e | -11.08798 | -44.61465 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e03b14e9-99b7-3328-8575-3cddf70f141a | -9.28156 | -47.10989 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bd95b96-c27a-3ccc-9d88-2bbd17a9e31d | -11.57136 | -44.65511 | 2025-09-01 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f028355f-00fb-3c87-ab42-b2fae4622200 | -8.19886 | -46.77549 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 938821ed-fc73-3166-a6d3-8e2283010815 | -7.11663 | -44.77526 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51c5f131-3910-3184-964b-70143605db07 | -7.07007 | -44.35034 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49b5bf91-59cc-3eb8-97e4-856abbf46589 | -6.53362 | -44.59959 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 929506d7-4247-37e6-a91d-99c665e3de13 | -10.24257 | -51.11448 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac20d7cb-6429-3d13-bded-4f69b5c0d844 | -6.14905 | -43.32568 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7a1a367-ffde-3299-8400-92747474e80c | -5.32955 | -42.85955 | 2025-09-01 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74c80017-16d2-3b52-bb62-3a1a92a5353c | -11.04245 | -45.15031 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 125f44b6-6ad0-3b3c-a996-2b3a86416690 | -11.03379 | -47.06026 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b097696-a9c2-3f2a-b7c1-aa3618971d15 | -10.60321 | -44.33235 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 7786c71e-05d5-38e4-b619-69c2d90a73d2 | -9.30704 | -41.13626 | 2025-09-01 04:10:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 003c4fbd-40eb-33a5-af1c-c7d380c4551d | -6.42218 | -43.96051 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e89a14da-f9e5-3ca5-af54-8fdce3337e0d | -7.08332 | -44.33611 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f50216f-d298-30d5-ad46-e4fe24077618 | -6.74487 | -43.79314 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b711dff-661f-3cb5-8705-28fcbebc75b4 | -11.80938 | -46.41371 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5e072be-015d-35c6-964d-22c2ade222a8 | -8.82057 | -47.80237 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f3b499-c962-3c22-ba45-f53527c0c176 | -10.66725 | -46.26202 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7241bff1-c38c-31a5-9da6-5f3b9301e543 | -7.24643 | -44.06445 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 814eeef0-b6d8-3641-b309-d12f39b4b57a | -6.33621 | -53.43311 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be96b05a-52e2-36ff-8553-2295bfb2674e | -8.83515 | -47.49644 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0462319f-b5ed-3b87-bee2-48bd0d925c76 | -6.35792 | -43.55882 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de6844da-4906-3fdc-bfa1-68ad5ebf1be6 | -5.8882 | -44.31962 | 2025-09-01 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 244d4b02-f42d-3e6a-a66b-31de3e544c68 | -8.83582 | -47.49264 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a016922b-3eed-3eb0-96a6-05878805bb81 | -11.84696 | -46.78555 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e26a37d1-4548-3f3d-9dc0-0f943e7f7cb2 | -6.85996 | -52.79856 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fefac3f0-9c6c-3b10-9f3a-b27d9cca390c | -9.00985 | -50.12048 | 2025-09-01 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff8c09ec-7311-3a47-9731-6c8b820e17ba | -6.63501 | -44.25047 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99b402c6-cc18-3afd-94e8-90ed5eb92bfc | -7.58182 | -42.71426 | 2025-09-01 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16decc56-2df3-31c7-a121-0aa9e59d3f09 | -7.63124 | -44.02596 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 081cb38b-eff0-351f-af86-01650502b380 | -7.62587 | -44.03693 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8672c01f-e25e-3b51-a61d-cdc2b7ae9054 | -8.01048 | -44.04986 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 611af6f5-886f-34e9-92da-2487ada6d1bc | -11.07514 | -52.06992 | 2025-09-01 04:10:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16577472-4fc8-3ffa-b0c0-b4b29c97233d | -7.11231 | -44.77888 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e546d84-ac3a-370f-987f-f491a570fddc | -11.87206 | -46.70697 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b59cbea-5718-3a54-9481-1cf5b415b208 | -7.69324 | -46.71491 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6411008-bc92-313c-abc1-215d490eb468 | -6.74646 | -43.78836 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84f3dbae-37c5-3e7c-a98a-0aa63024b811 | -6.30612 | -43.62892 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7622ccb-f045-3e78-b509-823d1ddf2b27 | -6.84057 | -43.34314 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04963db8-71e1-3dcf-aa53-df043e315a88 | -8.8428 | -47.50171 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6a9bbbb-c810-33ce-b44b-56f0adf6b2e1 | -6.81185 | -44.31466 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c302a86-d9ec-3ea5-8de7-3a8f101cb5b3 | -9.23634 | -47.08348 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5312bd3-19da-36e2-99f4-cc2e979b0529 | -6.30712 | -43.6448 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a7ab4db-97ce-37a7-a5d7-df5462924c6d | -11.42486 | -46.88264 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2745ffc-8632-378d-a810-e9673615375b | -5.36038 | -41.15482 | 2025-09-01 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b81583e0-254f-3b7d-a93c-4962a1265165 | -6.1685 | -43.3366 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac8a5ea6-abad-3cde-acc4-cd03fa2236d9 | -7.88123 | -46.97861 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| beb3da7b-6d56-3601-b989-f2fa91c9cc5a | -7.29884 | -43.70327 | 2025-09-01 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29ca7d7f-a761-352d-8529-4b12ea60cee4 | -5.55098 | -43.74641 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d456fd39-394b-3804-a728-b167a34917cf | -6.13964 | -44.12432 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d507158f-7269-3979-b95a-821068978c91 | -6.17557 | -44.12141 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8d150f2-b37e-35b8-9b68-bef989b84462 | -7.08564 | -44.33571 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1089369b-97f7-38b3-a0eb-c3b2fc7c7e01 | -9.61304 | -47.82077 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47d1b4e4-b4d4-313c-b64c-9cace6761769 | -9.2729 | -47.11198 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a28a29d-1e10-3bb7-84ec-78dc8db3d075 | -11.90645 | -46.6827 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4870b23-9afc-32c3-b0e2-5bcaab224b23 | -6.28387 | -43.28569 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9750bfda-293f-37d7-ad49-ce1859c42e8d | -9.63799 | -47.80128 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c1c4f15-ae92-392b-bb54-4f8d6068fd17 | -6.8321 | -43.33041 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| bed7cf60-4da7-3c00-9ab5-dcbc3df61b95 | -7.5846 | -42.71834 | 2025-09-01 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52d6d9ad-f989-32dd-9e8f-eb4fe6750777 | -6.79516 | -52.80883 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 751ce94b-1850-3dfb-ba72-438c2f89c074 | -6.83019 | -52.82296 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0001232b-5ef0-39ea-b1d0-9f7b607f1a99 | -6.16057 | -43.31992 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90d813c7-aaa6-3830-b668-3b06a7e31c13 | -6.30264 | -43.62836 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7b96c59-cd26-31f9-a358-4bedbf7bc885 | -6.27579 | -43.53047 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d06b353-401e-3601-b821-e9492d78ec7e | -7.28474 | -43.68979 | 2025-09-01 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 736ac474-7916-3be0-be12-bf88ea252566 | -6.32279 | -43.56959 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b163b5b-751c-3d0f-ba4a-6a068c9542a0 | -10.03956 | -48.10172 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdd5b697-7fe8-32dd-bd7c-5cabd03eca7b | -7.30019 | -43.70396 | 2025-09-01 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc40e37c-6ae5-3c8b-9d2e-a7e2b5fb3dae | -8.87808 | -45.09689 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| becc2e8e-0aac-3a7b-80d6-d50eea1ddbcb | -11.78969 | -46.46184 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b3d7eed-16fe-3454-baf8-7731895d4dfb | -7.04035 | -42.35986 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38bb06ef-4027-3b65-9699-235cc232e42d | -7.07586 | -44.3597 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2dc51666-532b-3f66-8f96-44fadf12f7a7 | -6.31368 | -43.62625 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec37be51-6ed1-336f-9acd-403c34601071 | -5.73125 | -45.54475 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50a2c4f5-36a5-3f97-a24e-1e94765bfe89 | -11.08735 | -44.61846 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40818e9b-0285-33cf-a61f-b7ad67c678ee | -11.80618 | -44.94153 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20f7ee86-9632-33e6-a753-8f4f631f1af9 | -5.65842 | -43.66297 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09a5c468-576d-32ee-aaa1-a5113f9ca3c4 | -11.03114 | -47.02888 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 67012317-0a80-3962-a8d6-2f254874e403 | -6.78386 | -44.62054 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d58f64-12c3-38ae-a225-5aef237bf9d7 | -11.95494 | -45.84047 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7f3e996-7d8e-330f-b4ca-cfd106b1bca1 | -6.5327 | -42.95605 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adf5892f-b6a7-3118-8989-01e7f0f2c806 | -6.824 | -52.8243 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a9120fc-968b-3ed6-8032-8a2e500da7cd | -10.59978 | -44.33177 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 950880f2-6cde-3e4c-97e4-c7935b549360 | -7.07297 | -44.355 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e246abb5-5464-3793-99e0-cd351fae3422 | -8.84413 | -47.49413 | 2025-09-01 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5dbbfbf-12b9-34b0-825a-5e848ea7f286 | -7.20929 | -44.22477 | 2025-09-01 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README34.md)
