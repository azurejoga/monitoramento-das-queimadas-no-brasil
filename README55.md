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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b1d15e8-a880-3bfe-acaa-ad0e7844767b | -13.95241 | -44.62112 | 2024-10-08 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7fafa2a-d154-3fa5-bc65-29aebe351e37 | -13.94938 | -44.61353 | 2024-10-08 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dae0b16-bbd5-331e-b616-ecc9e4ce1f22 | -13.9489 | -44.61707 | 2024-10-08 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1026ad62-90ca-3658-a120-b4606e4d78db | -13.93843 | -44.63433 | 2024-10-08 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aedc007b-9d01-39c8-9c9e-066be10eb1be | -13.93838 | -44.60481 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1845049-cf77-350f-b626-4aa8592bd30f | -13.9269 | -44.59954 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d38ee19-1608-3916-965c-701f4db531d6 | -13.9229 | -44.59899 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 897280d9-90c4-327e-9d6e-83908808f3c7 | -13.9225 | -44.6321 | 2024-10-08 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d0943d9-8505-3ae4-8873-97025e18ad91 | -13.91958 | -44.62371 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acf079e6-6e32-3334-bb68-43591a3e6e31 | -13.91911 | -44.62719 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8139eb57-bcf3-307b-94a4-9f0c6f4d49a6 | -13.91606 | -44.61968 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18e91802-05c0-3302-a811-53836f684733 | -13.91208 | -44.61911 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93657b5d-7b44-3ecd-bb21-ad112b65ddb4 | -13.88886 | -44.57991 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55a51596-1fbf-3de2-b6e5-86a23f52ea15 | -13.88839 | -44.58346 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0668c992-0968-35d3-bf05-79e8dafcf61e | -13.88659 | -44.57954 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b9aabe4-12ae-3a72-b584-a74d1f4bbdb2 | -13.8861 | -44.58309 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47d0d846-6117-3f90-84a5-4d9c5939ea5f | -13.84322 | -43.89525 | 2024-10-08 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74569d9b-39e6-392a-a879-4ff87dd802a6 | -13.81932 | -44.62583 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 089804b1-60af-3718-ad30-8a36bf570316 | -7.28886 | -44.97883 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded1409a-d345-3b93-a712-8944a2f45987 | -7.27935 | -44.96893 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78ca438b-3661-3bda-83fa-8d8c57dbab3c | -7.27576 | -44.96838 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3871036a-17c2-356d-b9f4-0961a6213603 | -7.27218 | -44.96783 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7a6826ae-dc02-33b6-ab02-459f6501dc1b | -7.2692 | -44.9632 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d561ade0-acb9-3734-af09-6fce92393ee2 | -7.26859 | -44.96727 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 70b1f03a-fd42-39b1-9c93-d51d8a79420e | -7.10185 | -44.57858 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b7cd0e4-7576-34ed-b3f6-bd1915a66a33 | -7.10121 | -44.58292 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4359bb3-3d1d-3af1-819c-8a484888ba5e | -7.10069 | -44.45927 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 357a65d4-597c-3c3e-8ba7-086074579414 | -7.10005 | -44.46361 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca8bb311-cc7a-3ef9-b01c-bc38d6111412 | -7.0982 | -44.57799 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65d08621-8423-35bd-a55e-1e12495789a6 | -7.09455 | -44.5774 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01768f5e-d917-3bd4-b02a-2fa059e9b368 | -7.0909 | -44.57684 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a0693c0-1e23-3d56-9835-fbe0a3057eb3 | -7.08725 | -44.57627 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fb3e218-cb77-3f66-b0ae-64b8a4057d1e | -7.08599 | -44.58483 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eacab24a-2e34-3853-b88e-36ed91db8f30 | -7.08297 | -44.57998 | 2024-10-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d7be199-907a-34f1-8598-783fe4311113 | -6.94164 | -44.64576 | 2024-10-08 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28fdc344-c8ad-385f-b2c8-6c2c1e22c2a5 | -6.69933 | -44.14706 | 2024-10-08 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc3dc7b8-0c20-3f34-aaaa-8ffec3c2a621 | -6.684 | -44.64362 | 2024-10-08 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e708eea-878c-34ad-a71c-cc728b0ab6cf | -6.61887 | -44.47908 | 2024-10-08 04:34:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aab88bbd-b235-3109-a023-2d3292778b19 | -6.61822 | -44.48339 | 2024-10-08 04:34:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4432bca-de2d-37d2-a836-12d476feeb4b | -6.58227 | -44.17738 | 2024-10-08 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 162f9309-fa5b-3ce4-ac5d-02bee4335be7 | -6.58161 | -44.18178 | 2024-10-08 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96bcba16-0d6e-3686-82e7-8f8896c70d65 | -6.58048 | -44.17998 | 2024-10-08 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e1fb757-34cc-3f93-accc-8b74fb1a950a | -6.57855 | -44.17692 | 2024-10-08 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61806131-1bbd-3f59-9058-9ccb43d5e837 | -9.12472 | -45.5282 | 2024-10-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05865827-bbdc-3133-aa0c-e709d2e9191f | -8.30977 | -44.10534 | 2024-10-08 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f51cb50e-e046-3154-8c04-92e999ad1cc1 | -8.30597 | -44.10472 | 2024-10-08 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a1f95ac-cce6-30c6-bacc-6bcefdeb3097 | -8.28377 | -44.09686 | 2024-10-08 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad848f50-58ab-31e5-8dd3-9ab966afc10e | -8.14049 | -44.4129 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed00f7f6-66fb-317a-90f3-33af9ff3c013 | -8.13982 | -44.41739 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0912756b-04be-37ed-a674-0f9e9f1ae541 | -8.13916 | -44.42188 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 796040ba-14d8-3b77-b38c-2e4086f248ff | -8.13676 | -44.41234 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b424e2b-0e33-35c4-8263-ace4c8dd0c92 | -8.13609 | -44.41684 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 943c4ea3-d8a1-3240-9e29-74114cb1f19f | -8.00738 | -44.37257 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dc5e36c-bdc6-3ad0-9664-00d06470859c | -8.00672 | -44.37708 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a7bc183-d108-397d-86c9-f3fdbc987984 | -9.64719 | -44.61969 | 2024-10-08 04:34:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 685a4f4e-37c1-325a-a954-2090c5b2a167 | -10.0669 | -45.27343 | 2024-10-08 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 460d44da-544d-3ef5-89f6-16aa9271c586 | -10.06627 | -45.27769 | 2024-10-08 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3a0c8654-e9f6-38a4-9182-a42aa21f8345 | -11.91543 | -45.70137 | 2024-10-08 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa547012-86cd-3143-848a-69f6e49719fb | -13.23111 | -45.53276 | 2024-10-08 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 347fcb8a-145c-3890-9254-02828bffa9e0 | -13.09149 | -46.32638 | 2024-10-08 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95ae2ee1-7cf1-33a5-a1bf-409addbb79e2 | -13.0909 | -46.33042 | 2024-10-08 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d28e8377-70f3-3cf2-acc4-1b15f5ef53ca | -13.08797 | -46.3255 | 2024-10-08 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a42973d-56f5-3907-b201-f96d4ea0e503 | -13.08497 | -46.34599 | 2024-10-08 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad2a1c03-b177-3941-b083-38514c31c67a | -13.08436 | -46.35014 | 2024-10-08 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24cf597b-9dd7-30d0-89c9-aca31362496b | -6.39372 | -46.2576 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 006eed51-10ce-32e3-a8cb-b156f479d412 | -6.38317 | -46.50627 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b323cff-a3f0-376e-8a86-8e29c42d88eb | -6.38262 | -46.50986 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed87f54e-e9b1-36a0-80d7-ceb00e1f2c35 | -6.36873 | -45.72954 | 2024-10-08 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fae5476-d184-3664-b404-b332f493fd30 | -6.33744 | -45.72846 | 2024-10-08 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31bc3b81-9cb5-378a-a56f-5204fd4d3af4 | -6.33686 | -45.7322 | 2024-10-08 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e47e04a4-250a-37fd-8c67-ab3bbced0e4e | -6.33517 | -45.7204 | 2024-10-08 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ff1b36f-e496-3438-9adf-33755524591b | -6.33459 | -45.72416 | 2024-10-08 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcc4c5d7-6cf5-3976-aac8-7d9136b11f35 | -6.33401 | -45.72792 | 2024-10-08 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdb4ddc0-0b3e-3ed2-9c3f-001da8e93e01 | -7.65119 | -46.66022 | 2024-10-08 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 056c7724-7c16-3d36-be38-76e38158f198 | -7.52525 | -46.59247 | 2024-10-08 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8913b87-0753-3951-86be-77e46ec5821e | -7.5233 | -46.59268 | 2024-10-08 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7604961-8dae-31ad-9580-a882f747778e | -7.46009 | -46.68982 | 2024-10-08 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96d4f166-94ae-3689-9a63-f172e4dca4a8 | -7.42916 | -45.99772 | 2024-10-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f3afd86-bb0a-3626-b59b-410ca4fd0f3d | -7.17983 | -46.61402 | 2024-10-08 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56d3475f-4e10-3a39-9ced-7cd4405339fc | -7.08162 | -46.38858 | 2024-10-08 04:34:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12491cf8-aabb-33d7-8470-7619386b6b25 | -7.01536 | -45.3755 | 2024-10-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b726843-f4f4-3254-8b88-56b2d32b4a9a | -6.96242 | -45.72372 | 2024-10-08 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9353093-7108-36dc-bfc7-4360d82b6aa0 | -6.94227 | -46.40807 | 2024-10-08 04:34:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0837cc04-980b-3427-9aa8-0e14f2546b7e | -6.93812 | -45.23988 | 2024-10-08 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84278f94-c9d1-3a2f-b89e-35f964b5771b | -6.93753 | -45.24377 | 2024-10-08 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22fb7979-e83d-3651-ba4c-5e58eac90128 | -6.93459 | -45.23938 | 2024-10-08 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4934f2e7-a6d4-36f0-b9e3-63325086834c | -6.89991 | -46.08717 | 2024-10-08 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6f1e98a-cbe3-3ef8-98d5-a2fa2047115e | -6.89708 | -46.08287 | 2024-10-08 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a8a7131-15b7-3427-be38-b2fdbd23c844 | -6.89651 | -46.08658 | 2024-10-08 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4f53c77-7578-3a5d-8240-fc1a4a6020ae | -6.77355 | -46.40449 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c5af928-7617-35b9-9f59-c9887c38fb8a | -6.68346 | -46.4975 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8587e930-cfa1-3e0d-b939-fae07f7635f0 | -6.68236 | -46.50466 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd214dc1-2aff-3ecd-a410-a6c0f3b8387e | -9.31945 | -46.73502 | 2024-10-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bce44723-9eb3-3161-85b1-2cc81b0f4ab0 | -9.30094 | -46.48805 | 2024-10-08 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a413190f-800e-351b-8d5b-97d3081ad0ee | -8.53474 | -46.59325 | 2024-10-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e28b756d-96ce-3d3f-bf77-8962070d173a | -8.53135 | -46.59273 | 2024-10-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60fb16ac-42a3-3d00-9405-9258408b0482 | -8.51216 | -46.60484 | 2024-10-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c34f5ccf-acd1-337f-816d-752a77a5b766 | -8.26892 | -46.86565 | 2024-10-08 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a72783bc-9898-381d-8452-5687f9fdce39 | -12.23782 | -47.28494 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7ac0d36-47cd-31ee-88ea-08d704c1fe1b | -12.23441 | -47.2844 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README56.md)
