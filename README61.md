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
| 4471dc5c-d083-36c0-b401-359743f33eeb | -3.82292 | -52.3442 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1722dfb1-6cbb-394b-aad4-a8194288f558 | -5.87247 | -44.21418 | 2025-10-17 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa626128-ff2b-3e11-b03b-43733165fa54 | -10.75411 | -47.28566 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6ee3cda-6e4f-3fa0-a175-b8ecd3094d02 | -10.49806 | -43.40707 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60b44a26-be30-314f-8b8c-a61ae26243da | -9.15169 | -41.06102 | 2025-10-17 04:19:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ee3f117b-14f0-37c9-9ec6-7f5922a6d653 | -11.46536 | -44.03862 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 664767e2-1139-35dc-9d32-d284780f3ce3 | -8.27322 | -48.00314 | 2025-10-17 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c114ec2-33cb-30ba-a260-fd13cddda895 | -7.66965 | -42.56409 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 829daea9-7fee-3a09-98d2-5eb5b4dc74ca | -5.78655 | -43.89284 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73b3b452-f1d9-3ac3-ac76-9f1645903451 | -6.34995 | -41.49702 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e8bf59f9-b471-3e83-9210-c36349a33cfc | -4.07626 | -43.40178 | 2025-10-17 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32170fbc-f8d3-3972-b8af-df80080a7818 | -6.32126 | -44.3242 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8198e3df-5ec5-379e-8d79-bda7d5977bad | -7.72235 | -47.84307 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 975f64ab-e410-3cb3-bb82-86c0cfa88d73 | -6.15262 | -41.79318 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07541201-0224-379f-be16-0c56d8eb32f0 | -10.92538 | -45.41154 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a67dc245-755b-3308-87f1-d6d7555a0c0f | -11.40496 | -44.23312 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61479993-db1e-3eb1-bad0-662459d61684 | -7.68386 | -44.62066 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6229e8a8-7812-3246-b3d1-4199c3c3d215 | -9.25145 | -45.25721 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c1cf0b6-9d84-3fc3-9838-de3f8ec3db58 | -5.64456 | -46.58632 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 671a004c-66e3-3fc2-aec7-b18b9c7c17b5 | -8.1606 | -44.00173 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3525a7f-d884-37dc-837d-0eef77caefce | -6.7084 | -44.37454 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b74d1c48-6cd6-316f-81e5-a923c7360e79 | -10.83733 | -43.99306 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d0eee76-385d-3a17-b702-eb95f9097d78 | -5.88606 | -43.88712 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b63386c-21d0-3010-ba5b-6b25935053b4 | -6.96631 | -42.20836 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f138c5c-09a1-3144-b34f-bea060f801ab | -6.83277 | -42.41837 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e2928991-f7dc-367c-952e-1104e24ac37b | -6.42952 | -44.72229 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 030adf8b-439f-3959-9c28-e46054c77ee6 | -9.67681 | -44.51329 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 742bfe32-602f-329e-bfc3-8742e1713ab7 | -6.7117 | -44.37506 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77d05cc4-9f92-336b-bb38-8e232f0f6dbd | -5.72063 | -44.51107 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1dac28f7-d44f-3905-87ac-16ac88378e9a | -7.19875 | -43.90987 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a368965c-f5d2-3ca9-8050-e371a2696912 | -6.15141 | -42.81152 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3774510b-bd1d-356e-8355-b0746ca6116e | -6.99131 | -39.2283 | 2025-10-17 04:19:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 38c4b1b3-f8a3-3e42-b09c-28e4ceb17a04 | -10.3603 | -47.72008 | 2025-10-17 04:19:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55232a72-a7ab-3444-8686-3436a9e8e6d2 | -7.15991 | -42.52879 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fdf4aac9-315c-3883-82a7-3289d63f0ee7 | -9.39018 | -43.71324 | 2025-10-17 04:19:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a00d5f5-2597-3bc5-a82a-d8cefd6ba996 | -9.71039 | -44.49315 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33bad1bb-14cc-3a5e-b562-94d3cca33058 | -10.81858 | -43.93372 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 510bdf93-d630-3425-97e8-eaea16bfaa0c | -7.60617 | -44.0025 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7983a291-bd04-31fe-9ae7-95532de0bf52 | -10.52791 | -43.36785 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f86d96f7-56c7-382b-9cbc-ac6a4a3987b9 | -10.49633 | -43.39521 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2ed8981-41a7-3a71-8ccf-543b9c414d60 | -8.4004 | -46.22987 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09fcda59-45b2-3c65-8ada-da5f808e95ef | -9.08223 | -48.03209 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3e77b062-6559-306a-922d-03c9a009e54e | -3.65036 | -53.65497 | 2025-10-17 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df33c5b4-6a45-34c7-8016-4b905c1aebf2 | -8.82479 | -47.30536 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bec52b3e-e096-3dcc-8380-64a1add3a48c | -6.35761 | -45.48021 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b18d0f2f-4e09-37ef-bf75-8e5eb67a7b72 | -11.40482 | -44.18802 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4d9e485-8678-31ee-8a14-f4f18a12503e | -11.39279 | -44.1296 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ddf064f-f353-30ec-a98c-26a12eed659a | -4.98241 | -42.79789 | 2025-10-17 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5fe4b41-2700-3caa-b39b-28a8cb7797f0 | -8.30587 | -43.43276 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 807b6008-8a4e-3430-a54f-ce8240c01e4d | -4.93111 | -41.55792 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ea2b60d-978f-32c9-b1e4-8587a05cec63 | -6.32617 | -44.31437 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 515e4bac-b4d9-3bd7-a41d-0c5f98bad005 | -5.34967 | -41.209 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 895bdde8-3250-359e-8d35-56e1d0d1454b | -6.13327 | -41.75337 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5af9694-a54d-33f0-afd8-73b7a635ff77 | -3.78361 | -49.42963 | 2025-10-17 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 97c96eaa-804c-32cf-b283-ac1ea166ba93 | -5.85371 | -43.87491 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5e8a85c-aa21-33e9-83cc-36c36eb6022b | -6.36045 | -41.48933 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bad788c5-5ee8-3291-a37a-b4985e300147 | -8.33596 | -46.23025 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74213936-4c4e-355b-927e-f9e945f023fe | -6.88057 | -44.68833 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 145f9531-97d4-37ce-8ab0-b20abd0f10c7 | -7.30261 | -42.30544 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c75cb743-3f00-30e1-b86b-7c6c59af1682 | -7.3229 | -42.4663 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b4dc8c2-3502-3fdf-8d24-7e26b7936dd0 | -5.5434 | -41.31635 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 538482c1-0645-3765-8ce7-1523ba6441b2 | -8.30643 | -43.4291 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0dca3478-5ad5-3120-b22f-5c1c92a50bd2 | -11.39004 | -44.14805 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660b5a20-2726-37bc-8f5a-7c0e68414a6c | -7.00474 | -43.97684 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c168f77-6057-3df2-855a-51ca08526499 | -11.14621 | -45.8513 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0ed2634-d110-32cb-b007-9ecce91a32d7 | -10.27122 | -44.02676 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f610e6a-428e-373a-a7fb-363ec434ec49 | -8.0843 | -45.43198 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a98d4d7-f225-39c3-a2c3-a3f529277c6a | -8.25924 | -44.0677 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6716e398-feac-39bd-aa14-8fc99c1f5615 | -9.13009 | -46.62947 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9c66f7d-c000-3987-b02c-d99dbf5f7fd7 | -5.74904 | -47.47303 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff27c135-c05f-3c2d-8870-45f4bd5837ff | -8.68366 | -47.00663 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81e673fc-b597-3348-bbf2-0b8b522d12ad | -8.46707 | -44.17612 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 278f51a7-2dd0-3874-9ac1-eef3666ff39d | -8.30419 | -43.44375 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 313c8102-bcd1-316a-b6f1-eb25cc8f4b52 | -9.28194 | -43.73365 | 2025-10-17 04:19:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34926e56-595a-3c40-b41a-529269ec6863 | -6.95478 | -41.56334 | 2025-10-17 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d35ad037-10e7-30b4-9009-be71dc74afc5 | -9.24323 | -45.26657 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f26f5c-5949-3f9e-a28c-40ce8ab8f87f | -7.11793 | -44.73607 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a22f05c-7a72-30a4-bc90-a86803ff5d14 | -8.39537 | -46.23996 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12a1e22b-4c6e-3487-be73-d16fca513fd3 | -9.26985 | -45.2743 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52081c7b-5cdc-31ce-8594-7d670fe516a4 | -10.14632 | -44.53234 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b0d2cb2-b91c-31ee-b526-9d2264a276ad | -10.29878 | -44.04947 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b6c4fe1-71e5-3666-bf09-b8134f7ceac6 | -9.28495 | -46.91536 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c92e4c9e-9299-3da0-bfe8-275aa86e7664 | -11.45664 | -44.21114 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d3c4faa-d159-3f4e-959d-bcec87dbc0e0 | -7.40258 | -44.74602 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0473e61a-cbd4-3044-9238-ce60262d5bf6 | -4.71825 | -46.44523 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e60e70d-0b49-34fe-bc82-93505eb606e4 | -8.06391 | -45.41107 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c00f3be-0317-3e72-85f2-de269a947c3f | -7.0583 | -45.05184 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce6bf58a-ff0c-3bfe-b6bb-6e1304275a82 | -5.90461 | -44.7485 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c7f5647e-d580-3b5a-9a99-46d70bfd82c2 | -5.84547 | -43.88428 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a439bbc0-426c-3524-9d6d-c5e2ff2b81fe | -5.9944 | -44.15251 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f80d8da-9348-3a96-bb83-83b6f3029f71 | -6.14048 | -41.72946 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ad5ad2b8-d051-32b5-8321-4aa5ce2abb44 | -7.11025 | -44.74194 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e643abf-3422-363d-8d24-d8ca7984acc0 | -5.29155 | -43.55191 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 508022bf-a6da-3d59-9d45-ab6bec8e35dc | -7.95352 | -44.11066 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8276d90b-ec5e-3a32-ac7b-07a9960f6379 | -5.24047 | -50.9525 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aed9d95-e7b6-342d-9e3e-a44c322970a5 | -6.69965 | -44.3873 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 359e295b-5e9e-3630-864e-becf61dee857 | -5.27687 | -42.54494 | 2025-10-17 04:19:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 30a8af6a-6fa0-3a09-a489-9691a4600ea0 | -8.22496 | -44.00472 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b400537b-d52e-3262-80ab-8484e332d0ae | -6.99901 | -46.992 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3583042b-01ec-3f2a-8286-a42e079ef58a | -11.39594 | -44.22421 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README62.md)
