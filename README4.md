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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf572d2e-7f6d-3796-8938-cae56a67b614 | -7.5886 | -42.2882 | 2024-09-26 00:09:56 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69372b57-b256-32e5-b594-453fffa6a65d | -7.5905 | -42.297001 | 2024-09-26 00:09:56 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 527a9b2e-d749-3dc6-a266-2af0883210c5 | -7.5788 | -42.290298 | 2024-09-26 00:09:56 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b0130ea6-bf3f-3d64-9bac-280ee442d38a | -7.5807 | -42.299099 | 2024-09-26 00:09:56 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 835a5c87-bea4-3a22-be99-97d23618cf53 | -6.6113 | -39.574299 | 2024-09-26 00:10:02 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ba9215a-e13c-31fa-a5bc-1761850be700 | -6.6129 | -39.581299 | 2024-09-26 00:10:02 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a3ca0a1b-b41f-37f7-81b2-4e5c9111f7e1 | -6.6144 | -39.5882 | 2024-09-26 00:10:02 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 93909490-4199-371f-ad24-6ece14bb8c2b | -7.2125 | -42.444 | 2024-09-26 00:10:03 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ebb262d-3a96-37e7-b850-0cac6de67f90 | -7.2145 | -42.4529 | 2024-09-26 00:10:03 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3869c1b4-c388-3442-b876-befab38f34cb | -7.2028 | -42.492699 | 2024-09-26 00:10:03 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 58b82965-2887-3870-9d7b-4d5d0fb5b233 | -7.2048 | -42.501701 | 2024-09-26 00:10:03 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88603e68-1e1a-36bb-a8a7-390701361561 | -7.193 | -42.494801 | 2024-09-26 00:10:03 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac13031e-1910-3cbc-b855-244719fcbd8e | -7.195 | -42.503799 | 2024-09-26 00:10:03 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3aba2b75-ab21-3dcc-88d9-559bcba3cbf5 | -6.7795 | -41.233799 | 2024-09-26 00:10:06 | METOP-C | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71621efe-fbb2-3850-bf99-9dce79263326 | -6.9502 | -42.463699 | 2024-09-26 00:10:07 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ee094f4-b205-39fc-8d38-a046672eef08 | -6.9521 | -42.472599 | 2024-09-26 00:10:07 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4fb220ab-be20-30f4-9629-61083a7b21a2 | -6.9541 | -42.4814 | 2024-09-26 00:10:07 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46c5ff93-efac-38d5-aab7-4ea660830716 | -7.2098 | -44.777699 | 2024-09-26 00:10:11 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa7cb98e-a231-315b-b367-9aacc0e8aa84 | -7.2125 | -44.7901 | 2024-09-26 00:10:11 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00a26894-dad7-3a3c-aad5-ff9c5ff6ad4b | -7.1175 | -44.823101 | 2024-09-26 00:10:13 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80fdcc79-0d7e-39c2-9acf-9f5c0d0e45ec | -5.8351 | -39.3783 | 2024-09-26 00:10:14 | METOP-C | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a14e26d6-eb49-3b77-849e-5ef21446ca9c | -6.7062 | -43.544399 | 2024-09-26 00:10:15 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8ad2e12-7460-3066-aa58-6bc0d56397b7 | -6.7084 | -43.5546 | 2024-09-26 00:10:15 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 101aace8-c0a7-330b-af1f-df5397b25aee | -6.7106 | -43.564701 | 2024-09-26 00:10:15 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9da7e6e-c0ed-37ce-81bd-367624defe97 | -6.6843 | -43.538502 | 2024-09-26 00:10:15 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3559681-b276-3b7d-a4bf-09ac0c35573d | -6.6724 | -43.530499 | 2024-09-26 00:10:16 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 879ddaa4-947f-3d36-a908-d3d496a003ab | -6.6746 | -43.5406 | 2024-09-26 00:10:16 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cc22b29-2ad2-38d4-825b-dfe5d4a027b5 | -6.6768 | -43.550701 | 2024-09-26 00:10:16 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8be7477-0fab-32f9-8354-aeaedffc3a4c | -6.5395 | -43.019699 | 2024-09-26 00:10:16 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06106f54-c285-3319-a578-20693cc1dc9d | -6.5416 | -43.029099 | 2024-09-26 00:10:16 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad966558-5776-34ab-8ed8-ef578ab955b9 | -6.5297 | -43.0219 | 2024-09-26 00:10:16 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0de76c72-141c-33cb-b26d-7dfb5fbbd8dd | -6.5318 | -43.0313 | 2024-09-26 00:10:16 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 878bed25-148b-3821-89a7-19492694fcc4 | -6.455 | -43.287601 | 2024-09-26 00:10:18 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea2e7c6-9857-3534-99c5-0af870b6385f | -6.4571 | -43.297298 | 2024-09-26 00:10:18 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77ec7ce4-4803-3732-a7d7-219330f6aacb | -6.4593 | -43.306999 | 2024-09-26 00:10:18 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca6e12f5-4cea-3c83-85e8-82148e722c5e | -6.3236 | -42.507801 | 2024-09-26 00:10:18 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cbfc3d42-112c-3dd1-8f0b-b72f2547547f | -6.3118 | -42.501202 | 2024-09-26 00:10:18 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c588d42d-c8b3-3dcd-a944-11668fa237dc | -6.3138 | -42.509899 | 2024-09-26 00:10:18 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fffea10d-d0d8-3ecb-9829-0dd54e6f5728 | -6.7778 | -44.7164 | 2024-09-26 00:10:18 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49331799-2a0c-3c0e-a5c1-ff418b5f16e5 | -6.7804 | -44.7285 | 2024-09-26 00:10:18 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3bcafd9-a8a3-3de4-94b0-7316b438589d | -6.783 | -44.740501 | 2024-09-26 00:10:18 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e60d952-3365-3c1e-ad98-968d962c9e6b | -6.768 | -44.718399 | 2024-09-26 00:10:18 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4977ecce-3264-3566-82d8-d3d5935665b9 | -6.7706 | -44.730499 | 2024-09-26 00:10:18 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d5cabc3-6943-3449-b9df-060e9b76dfe0 | -7.0875 | -46.4403 | 2024-09-26 00:10:19 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69c55deb-7239-3c92-9fca-a97a5f660a39 | -6.3428 | -43.151199 | 2024-09-26 00:10:20 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ba2e104-1800-3254-a566-e6db764cbad4 | -6.6347 | -44.9515 | 2024-09-26 00:10:21 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b146aea6-10d5-3c17-9348-0a2754882c66 | -6.6374 | -44.964001 | 2024-09-26 00:10:21 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff9829cc-bca1-34ed-810a-d09c00c377a1 | -6.2235 | -43.307201 | 2024-09-26 00:10:22 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cdf312f-380a-323a-8bc2-c0d87c7acc9d | -6.2256 | -43.316799 | 2024-09-26 00:10:22 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbab1a00-f025-35d3-9b96-bd14f3e85e3f | -5.9479 | -43.266499 | 2024-09-26 00:10:26 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 660037fd-7410-3e0b-b2c3-4d715476a6b3 | -5.95 | -43.276001 | 2024-09-26 00:10:26 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 612aaf53-a035-329c-9bd1-026cedc24c82 | -4.5341 | -38.0242 | 2024-09-26 00:10:30 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 468d5030-c0a6-38ef-86ac-5833962fd152 | -4.5357 | -38.0312 | 2024-09-26 00:10:30 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1a66ecb9-2b40-3249-ba24-9b7abb8c8edf | -4.5374 | -38.0383 | 2024-09-26 00:10:30 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f05eb091-0076-3696-93b4-d5ceb522a1cb | -4.5259 | -38.033401 | 2024-09-26 00:10:30 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ef67ad85-6312-343c-9a3d-1a15dff3deb7 | -5.9589 | -44.571602 | 2024-09-26 00:10:31 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94e18e2e-77eb-3c81-aeef-112fa15964ee | -5.6263 | -43.6203 | 2024-09-26 00:10:33 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9109cdb-0597-3292-aced-3c7280f08ae0 | -5.6285 | -43.630199 | 2024-09-26 00:10:33 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b3722db-25d9-3818-8d89-65ebd19e15d1 | -5.6166 | -43.622398 | 2024-09-26 00:10:33 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e95de66-378b-3b39-8de5-ae6a2c4cf0a4 | -5.6188 | -43.632301 | 2024-09-26 00:10:33 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a712495-5ad5-3051-bde5-d2b1f75beec0 | -5.5418 | -45.094299 | 2024-09-26 00:10:40 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bfa913f-a583-3bc5-8477-2ebc98b0c3a8 | -5.8657 | -48.087898 | 2024-09-26 00:10:45 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e286c72-cf16-3804-a075-a5e3b8d14541 | -5.8615 | -48.0681 | 2024-09-26 00:10:45 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebe2d0fb-7595-308d-85e8-70c983a55e1b | -5.176 | -45.198299 | 2024-09-26 00:10:46 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d3f45ff-8f0e-3175-9468-7c36669767d5 | -5.1663 | -45.200401 | 2024-09-26 00:10:46 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 088b57d5-f2e3-32e3-828e-b39ecae9f114 | -5.0828 | -45.192699 | 2024-09-26 00:10:47 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e26c2599-0060-3906-bca0-29be26144ad6 | -5.0855 | -45.204899 | 2024-09-26 00:10:47 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2516538d-c05e-3a78-acab-c1dc5f3e3b65 | -5.0882 | -45.217201 | 2024-09-26 00:10:47 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf3222fd-96b5-3609-adc5-4755c192dff6 | -5.205 | -47.942299 | 2024-09-26 00:10:55 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb7926c3-a228-3621-9e31-df800af0ad06 | -5.2092 | -47.9613 | 2024-09-26 00:10:55 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f27e2595-a4fb-30f8-917d-c919302225aa | -3.7937 | -41.589802 | 2024-09-26 00:10:55 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 221eb33a-7004-34af-9f8c-20acdda67516 | -3.7954 | -41.597301 | 2024-09-26 00:10:55 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d1101d12-b161-344f-ae8d-e6db831be97e | -4.5776 | -45.682999 | 2024-09-26 00:10:57 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d85e89a-d5ea-340c-9288-2e513dec660b | -4.5804 | -45.6959 | 2024-09-26 00:10:57 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab6b2a68-6492-30a5-ab4d-573f2557dd3a | -4.5678 | -45.685101 | 2024-09-26 00:10:58 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b52c4e31-bcef-396b-9f41-9c930ca94876 | -4.4884 | -45.880699 | 2024-09-26 00:11:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d67fdc4a-043f-3c4f-9059-3dfe95b6b6df | -4.4913 | -45.894001 | 2024-09-26 00:11:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80d0149a-0ab6-34b2-9c19-11ef3e88e6bb | -4.4943 | -45.907398 | 2024-09-26 00:11:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bae5391-1492-341a-a593-46f943522eec | -4.5697 | -46.295399 | 2024-09-26 00:11:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45844112-72c9-3af0-b568-e2de61db53b6 | -4.5729 | -46.3097 | 2024-09-26 00:11:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34bb6029-2cf3-3c4d-bc81-62fca6e6d643 | -3.9167 | -46.435902 | 2024-09-26 00:11:11 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1a44251-c531-3106-b475-1083b5f3786d | -3.9037 | -46.423698 | 2024-09-26 00:11:11 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62c722c8-3043-3613-9f9e-27064ef337cf | -3.9069 | -46.437901 | 2024-09-26 00:11:11 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 277f09f7-c959-3b46-8e94-e890b1253a48 | -3.9101 | -46.452202 | 2024-09-26 00:11:11 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2812a64-0123-3096-a4f5-a87baa272559 | -3.8972 | -46.439999 | 2024-09-26 00:11:11 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7cd237-0d05-30f3-b19c-5c45d7a0fb1b | -3.9003 | -46.4543 | 2024-09-26 00:11:11 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae28f84-6c47-3b8c-8a69-f78febbaa50d | -3.5407 | -50.341099 | 2024-09-26 00:11:31 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ccbd33-631d-3411-8192-6204b3850e96 | -3.5465 | -50.3675 | 2024-09-26 00:11:31 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 935bb70c-c31b-3201-af80-ca1b5d750ca9 | -2.7208 | -46.754799 | 2024-09-26 00:11:32 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9735e340-c57f-3835-8b6d-3e44fcb7c9d0 | -3.2086 | -50.303101 | 2024-09-26 00:11:37 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70c5025-e349-3c23-b08b-dbf80158c747 | -1.156 | -46.847801 | 2024-09-26 00:11:57 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec14b721-744e-32a3-bf5c-c58498ba5fc9 | -1.0553 | -53.3553 | 2024-09-26 00:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 34d98a3c-b4b8-35c3-bf12-815d56e03711 | -2.6601 | -57.5507 | 2024-09-26 00:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8690fdff-0399-35a0-a5fb-cf1edf528290 | -2.6785 | -57.531 | 2024-09-26 00:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 33971403-1ac6-34d2-8410-243cbe0820c2 | -2.6968 | -57.5307 | 2024-09-26 00:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| bab4a796-ddc9-3754-a07e-82b0ea4c6e4d | -3.3505 | -53.7775 | 2024-09-26 00:15:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 13ee8967-ea35-3702-b7bb-6488ffe40bf0 | -3.7821 | -41.5999 | 2024-09-26 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| dac552b1-2682-35ea-9899-735004aac771 | -3.8008 | -41.5989 | 2024-09-26 00:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 700dcd85-da6c-3023-8f62-8082f7eaa3c6 | -3.801 | -41.575 | 2024-09-26 00:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 421e332f-3a5d-31a9-9b93-fe8dec1520d6 | -3.9208 | -46.4459 | 2024-09-26 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |


[Clique aqui para ver as próximas entradas](README5.md)
