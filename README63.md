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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0650d342-8112-3819-9c67-c54b82606c1f | -10.50674 | -43.44285 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43c4e7bf-64b2-3d4e-bf1e-5564d06a376a | -10.82197 | -43.93425 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66109961-2cee-3bb1-a54d-111198a61cbb | -10.25836 | -44.04343 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07c22c2f-e854-3f73-8b7a-d77232ebf94a | -4.72169 | -46.44577 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32aed15f-8735-3728-87cb-47496f4a0cc7 | -11.13686 | -45.84623 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe137a12-0cf0-326e-94bf-afd56f8dfd9d | -9.30285 | -46.93334 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8048ee90-5034-3112-b94f-230d5d45c650 | -5.69468 | -53.63866 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e3b0de-9288-309d-a8b2-8532cf528c81 | -7.36574 | -46.54682 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78859037-5592-38d4-b397-01bc077817e4 | -8.23715 | -43.32899 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e5c1c572-5bad-3618-bd66-12c210197dba | -7.96729 | -44.08749 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64e2f22f-6698-3c82-b5d9-d8b0344785f5 | -9.70623 | -44.56469 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc9b85c9-f672-3890-b000-7e3bb4d56def | -10.65013 | -45.29943 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 952a1ad9-f037-3adb-bb40-a2c53142071e | -4.29052 | -41.81501 | 2025-10-17 04:19:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26ee6882-ad85-3eae-9195-9fdb6a0a37e2 | -5.314 | -42.94426 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7d5a920-0e39-3343-b582-60e36827f132 | -6.53089 | -42.18929 | 2025-10-17 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0e2ec40-e333-3cdb-8a4a-25d52b45c953 | -7.83822 | -45.46068 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08e84775-5331-3400-b519-87aa2271a7c9 | -5.78741 | -42.46514 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7012adf7-a75a-3c0e-a0a4-eab3fdbde4a2 | -4.25708 | -48.56784 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c07868d9-964c-3bec-8801-9f7e7d21fdca | -6.74631 | -44.36985 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91b507eb-dc23-38dc-8837-c63995fbca1e | -5.14359 | -46.29007 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca54757e-01fe-3f62-8e2f-07ec672c1488 | -7.22079 | -47.86525 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aeb5bf01-37b8-3553-b18b-4cec0be581fc | -5.88614 | -43.90847 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3a353f7-b684-3577-8e7a-ab59a7bebf64 | -8.32241 | -40.38023 | 2025-10-17 04:19:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3a3d877a-59bd-350b-8f30-8df7b95fcde2 | -6.83681 | -42.41507 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1317d370-55f7-3f34-8c99-0612b40e20f1 | -10.27292 | -44.03825 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 259f9f86-4608-3ae7-906b-e4cee4de5f2a | -5.23267 | -42.00791 | 2025-10-17 04:19:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6337b832-0717-36c1-8bd3-3c4d132ffeb0 | -9.9833 | -47.01365 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 544fbd2c-d581-34ce-9d5f-9ebcda9522e6 | -7.95298 | -44.11419 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a333ecf7-4f58-3cf4-8a54-04c8a49ba8a3 | -7.12338 | -44.72279 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 448e2ca8-a689-35a1-a9ac-c1f44cf3443a | -9.07871 | -48.03148 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2de921b-7d7c-356d-b052-ad8a546849a3 | -8.38088 | -46.24501 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 548f3be6-6f4a-3653-9ccd-b3ee5e496622 | -6.43977 | -43.38404 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf23231f-ef81-3c30-8b34-e64dc3776d27 | -10.10193 | -44.62313 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae259894-9960-3a1c-a285-551ea65d1ee4 | -9.22503 | -48.59855 | 2025-10-17 04:19:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4e7b5a1-de80-3267-8680-a90ce384ccbc | -7.28045 | -42.31002 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc1d4d3f-142a-3e1c-b992-acbb44fcfb23 | -5.50464 | -47.30351 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a67ff525-1f67-32b1-a05f-8c5b1fe93f83 | -11.47738 | -44.14277 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 157bb560-2087-3f29-b2aa-ed3ac43ac7c1 | -5.41422 | -40.90316 | 2025-10-17 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b3689ae-ab03-3997-9ee7-75612ed8a899 | -8.45526 | -45.12954 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00823a0a-0d5c-3ac2-a35d-516f6a093969 | -5.91449 | -44.75005 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 76866650-8503-30e6-9edb-0d1bca96f9fd | -10.51757 | -43.39449 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a70088d3-38fa-310d-92c4-fa4cb7254fe2 | -6.96858 | -39.67037 | 2025-10-17 04:19:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc993ff5-10f7-349c-ae8d-1b5dcc31ed16 | -4.42619 | -47.75136 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 558138e7-cef3-35da-91e0-e82ae7857af9 | -5.84602 | -43.88081 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19f4eb92-c9d1-3aed-a9ca-9ce8e55eae83 | -8.21769 | -43.98547 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7fc177b-b53c-3106-827c-5743f6e19ee1 | -4.55667 | -50.60633 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6892e766-980f-364f-870a-8aa7ab4c761b | -6.10701 | -47.03281 | 2025-10-17 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ee7423c-79ca-3473-9f31-227a600448ac | -10.29368 | -44.03771 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| fb1d5e8f-e95d-394c-abab-8bdcafb796be | -5.84325 | -43.87682 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac755def-8897-3e4f-bf63-d597ae1310bc | -10.53047 | -49.54641 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 3d8eb7ec-0a56-3e73-bf21-08926ad814ee | -4.44242 | -49.68878 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb64807d-000d-32d0-ab8d-98f37e2bb4c2 | -11.14456 | -45.86177 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd063314-eff5-33f2-ab19-a95347139d17 | -7.50839 | -44.65712 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba54e1a7-ddff-323b-a9bd-3769af581289 | -8.25691 | -44.03839 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f32f03d-9eaf-38aa-86a7-54e50c6b155c | -6.23272 | -44.15065 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9c64819-3fc2-3682-adaf-1cf4dc83f757 | -9.13229 | -46.63722 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7faf06bb-5a2a-3b44-a35a-f1a3912f8d32 | -8.7306 | -43.87503 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1e209973-f4c2-3f99-b6e9-f6dce615a18e | -4.01826 | -48.96458 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a29eafc-1676-3e86-9abe-b0c155d46a48 | -10.65506 | -45.2895 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7461efaa-c092-3a94-a110-d62c498e63e2 | -7.1342 | -43.77748 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d47500f7-874d-3a8f-90dd-9d6e375ac1e2 | -5.77094 | -46.76007 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1564f09b-94fd-3659-9bf5-d7bd73a5523a | -6.20359 | -41.76758 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 10d91598-fb62-3176-9923-8bf37ef17df7 | -7.33457 | -44.15344 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f05bbcf9-a8c6-33b1-9c07-2dbdcc70f659 | -9.71009 | -44.5617 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13abef0a-3e49-31e9-9e87-862c1f33f8ff | -10.8807 | -47.91424 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b82eaec-74ec-3ebe-a60f-1b5af36bca0b | -10.61681 | -42.31113 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c9f42d62-26d4-37b5-8024-9aa084166d61 | -7.4831 | -44.66314 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a3cc7cc-6a23-3950-8d58-006331b077ac | -5.29167 | -47.92345 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b27ca30-8dfe-3957-9923-64cab7001667 | -7.95236 | -44.09606 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83a50e4b-c08c-3e5f-bba7-542d8629bc54 | -5.24864 | -50.9584 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 076758c8-fe3b-30bc-8159-8cd10285379f | -8.55866 | -45.4872 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6beffc60-a201-3b3f-bbf2-f91214a57744 | -11.41164 | -44.21163 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 00aa581a-749a-3f42-b989-2f69f2db3d38 | -8.18969 | -43.32161 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1d1c8a86-e18c-3892-9297-483957d8ff20 | -4.72165 | -46.15979 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6477ef1e-eec9-3840-91c5-a685d73d90e9 | -5.72355 | -43.83706 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32876f80-e852-3808-9733-a03678616a6c | -6.83969 | -42.41947 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b45f3dab-30a8-3436-930e-c24fa01c7b62 | -8.21565 | -43.31069 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11172387-7e15-3825-8984-eb0a1c857e36 | -11.40104 | -44.23626 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2044640-1812-387b-a936-a345e013c5b3 | -8.28265 | -43.38049 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 30845931-95b8-3d49-bb72-f1814227b26d | -7.41692 | -44.76241 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2aa163c-f5ab-3402-b893-ea3b3eb7d0d4 | -10.15576 | -44.53741 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 043430f4-54db-38c4-92b7-1da6ae8bbfc3 | -10.18573 | -49.50922 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd306ea6-a81a-3ad6-9ff7-56a2c0920d04 | -6.41644 | -43.57993 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f5cc905-f0d3-3136-9bdf-1d7cc15f48cc | -6.75825 | -42.38081 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 81a401ed-f27a-35f0-9b3d-285a0c5813e3 | -4.38182 | -43.3853 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e155204a-5e7b-3a54-ac8f-1b757968f543 | -5.34964 | -45.74255 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3da4721d-6227-34f9-98f5-0d9810518512 | -5.65753 | -46.80904 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da5dd838-7654-3c05-847c-6826c8b4a668 | -10.529 | -49.54829 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 5998d07e-0790-3975-973f-5625d74fcacb | -9.71117 | -44.55466 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4ab3c28-c28d-379c-bb58-fd2531ca19e2 | -5.91066 | -44.75298 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 50dcb05f-71e3-392f-878e-ea0e41d7e48c | -8.08705 | -45.43599 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c133a704-680e-31e6-abed-bd8bf294ebb5 | -7.34195 | -43.86394 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d9cc96f0-a51b-3796-843f-93d9670c4509 | -10.88132 | -47.9104 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e837a615-8f70-3054-a662-05db64f66f4e | -4.57285 | -48.0232 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 282339db-ba92-3e9c-aba6-de3afafc3900 | -8.23277 | -44.02041 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3a9b421-313f-3e61-b575-71b865a21343 | -7.46024 | -42.67452 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4a7f4460-6971-3765-85ad-15e58bbd2996 | -5.05964 | -40.94532 | 2025-10-17 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31fbfaa1-37f5-3de4-ab53-d68cc625d6cc | -7.40864 | -44.7505 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0429209f-58e4-3d56-827d-72b7f726598e | -4.37371 | -46.53215 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54660f1e-5e2b-304d-903c-584cd6b5b792 | -5.90736 | -44.75246 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README64.md)
