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
| 6c0266e1-a523-3e1e-bd76-d0858dcf207d | -11.3156 | -50.899601 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf15c1d4-1e13-3116-9973-7a8be24b04f5 | -11.3181 | -50.912102 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6ae6062-712c-3fe1-ab34-3c6f14b2a277 | -11.3032 | -50.889099 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e46a1da-2596-322d-9c1b-dd42d99015b8 | -11.3058 | -50.9016 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20ce7556-d5d5-31b4-8dc4-a341a670e90e | -8.7834 | -40.347301 | 2024-10-12 00:23:20 | METOP-B | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| c6cb1354-cb42-3c9f-bef5-d2f984a07e8a | -10.4826 | -47.6474 | 2024-10-12 00:23:20 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b657e6b-e091-3b69-983d-a92dbb1b663d | -10.4843 | -47.6553 | 2024-10-12 00:23:20 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23e53fc7-42d8-3f10-be10-fa8cca1c27c8 | -10.486 | -47.6633 | 2024-10-12 00:23:20 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84cfc3cc-3856-3086-b596-20cce9d43f2e | -10.8804 | -49.723499 | 2024-10-12 00:23:20 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d28160b-fdae-3ff0-baf5-27cbcae205b0 | -10.8706 | -49.725498 | 2024-10-12 00:23:20 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c751a31-54c2-3ac7-8740-326159b8cb1f | -9.2684 | -43.1647 | 2024-10-12 00:23:23 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c0064b10-0a25-353b-b550-289f006704f9 | -9.2701 | -43.172199 | 2024-10-12 00:23:23 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6666ce1-15c8-3d99-844a-3b375c5d1ceb | -9.5619 | -44.452301 | 2024-10-12 00:23:23 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 874ec2d1-6746-3d0d-9f1c-c1f829b34c38 | -9.2698 | -43.530701 | 2024-10-12 00:23:24 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66b8fc5a-39b8-3077-9bc5-402ac6c0e0cc | -10.5423 | -49.084202 | 2024-10-12 00:23:24 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a4ab5c9-9568-3723-afed-c345c8e253cf | -10.5443 | -49.093601 | 2024-10-12 00:23:24 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d926b5b1-f4a1-3ed6-b268-5d2cc211424f | -10.5463 | -49.1031 | 2024-10-12 00:23:24 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9598e1b-eadd-3459-9e3b-484adb387ced | -10.5345 | -49.095699 | 2024-10-12 00:23:24 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2417d1-58e3-33c4-bd5d-7d781fac3e4e | -10.5365 | -49.105202 | 2024-10-12 00:23:24 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4dd51d-3d3c-366e-8a96-ebbd711915bd | -9.2583 | -43.5256 | 2024-10-12 00:23:25 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d39a85e-01e1-398e-bfdd-542d800fdbb5 | -9.2546 | -44.551701 | 2024-10-12 00:23:28 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ef2ff29-7198-3aec-9c6c-3ff1492508df | -9.2562 | -44.558701 | 2024-10-12 00:23:28 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b706929-76ca-32aa-83be-8ffe80c19de5 | -8.383 | -41.006699 | 2024-10-12 00:23:29 | METOP-B | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4649700-90c1-3cba-93e1-36ece4558dab | -9.5366 | -46.136299 | 2024-10-12 00:23:30 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62b248f7-6b3c-37ab-8dcb-6816aaba7fba | -8.2427 | -41.111301 | 2024-10-12 00:23:32 | METOP-B | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b70cf41a-67d3-3b21-baaa-9707f77c322e | -8.2538 | -41.377201 | 2024-10-12 00:23:33 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63849f5a-413e-312a-86db-6dddea9962af | -8.3864 | -42.162998 | 2024-10-12 00:23:34 | METOP-B | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48994536-5b44-3bc2-9a13-ac5a83d9163f | -8.3884 | -42.171398 | 2024-10-12 00:23:34 | METOP-B | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0ec1c90-dfce-3687-abe7-ef0f1d961334 | -8.0878 | -41.066799 | 2024-10-12 00:23:34 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9456379b-7139-3727-9cc4-2889a1ca7bea | -8.0901 | -41.0765 | 2024-10-12 00:23:34 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 088658f4-c6ef-3463-8504-2b1a08bf931f | -8.0637 | -41.051998 | 2024-10-12 00:23:35 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4fa2765e-fb0c-31a7-bd91-e7210cce85bf | -8.9355 | -45.010601 | 2024-10-12 00:23:35 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1713c811-4495-3a58-98b4-135d7c32c20d | -7.4711 | -40.2062 | 2024-10-12 00:23:41 | METOP-B | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d5fa1f86-b489-3d04-b5be-a88f282a64c6 | -7.4737 | -40.2173 | 2024-10-12 00:23:41 | METOP-B | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 20bf1ab6-df2e-33ff-a367-33e4174aa9b0 | -7.4614 | -40.2085 | 2024-10-12 00:23:41 | METOP-B | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 989d7a3a-92be-3093-aafe-0d5e7ef85b1e | -8.9245 | -47.046398 | 2024-10-12 00:23:43 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8caf21fc-feaa-32b2-962d-202859cb987a | -9.1917 | -48.9431 | 2024-10-12 00:23:45 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6fdf38b-00de-3549-aa46-dad05e81f932 | -7.1371 | -40.058701 | 2024-10-12 00:23:46 | METOP-B | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 37814239-d98c-3631-98ed-41b0d29dd7ef | -7.1398 | -40.070202 | 2024-10-12 00:23:46 | METOP-B | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e8435741-b394-3948-b135-2bacc56d15cc | -7.0843 | -39.923698 | 2024-10-12 00:23:46 | METOP-B | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e90ba929-ba66-3f5d-8833-a5c2212a10cf | -8.1396 | -44.452499 | 2024-10-12 00:23:46 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed56106-4118-3887-9390-1b2a90a7d998 | -8.1412 | -44.459499 | 2024-10-12 00:23:46 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48af0fa5-0106-3383-bf21-ba51d91f5f5f | -8.8849 | -47.8055 | 2024-10-12 00:23:46 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e05231b-f521-35ff-86cb-d1382c154640 | -8.8866 | -47.813301 | 2024-10-12 00:23:46 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c72bef9-7503-3b64-a695-d593f2ab8600 | -8.863 | -47.941502 | 2024-10-12 00:23:47 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de4722de-26d1-3b35-88ae-205f94d6ae2d | -8.8647 | -47.949299 | 2024-10-12 00:23:47 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce88941e-4192-38e5-98fa-291965881fbd | -8.8532 | -47.9436 | 2024-10-12 00:23:47 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4a5d109-5163-3397-ab95-6ffca5b0722a | -8.8549 | -47.9515 | 2024-10-12 00:23:47 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6841b0c-cf4a-3fb3-862a-8c24685b70b9 | -9.0384 | -48.801701 | 2024-10-12 00:23:47 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d6fd09b1-321e-381d-8b4a-216e2ffe704b | -8.6807 | -47.200199 | 2024-10-12 00:23:47 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be191637-3663-357b-a046-0c577b01f40c | -8.6823 | -47.2076 | 2024-10-12 00:23:47 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f411d7b-7d8e-308f-8441-f54af0017599 | -8.4487 | -47.220299 | 2024-10-12 00:23:51 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3851ba6e-5a67-35b8-a6e3-e13efcace079 | -8.4503 | -47.227699 | 2024-10-12 00:23:51 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d79e9b9-2085-35d4-b309-a7857a13c23e | -8.4389 | -47.222401 | 2024-10-12 00:23:51 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9d4d0d4-707a-3772-9541-ab7f85549b4c | -8.4405 | -47.229801 | 2024-10-12 00:23:51 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0f63e69-5b7e-3ba5-971b-faa2e91bae0d | -6.4453 | -38.805199 | 2024-10-12 00:23:52 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e6e5b786-3a5a-32f8-98f6-83c53cba7a23 | -6.4487 | -38.819401 | 2024-10-12 00:23:52 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 921457fc-fb03-3f31-8596-3d0103ce58e2 | -7.8425 | -45.2356 | 2024-10-12 00:23:54 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54f4002c-3593-3b3d-bb33-36337d00b010 | -7.3085 | -43.522499 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9af6de8-beae-3a1a-a04b-104b0ff3e799 | -7.2987 | -43.524799 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17849e8d-085a-39cd-984f-047b4726d594 | -7.3004 | -43.532398 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 946f2f94-4608-38da-84ad-65aed8eb30a2 | -7.3021 | -43.539902 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 533d7af3-687c-31a1-b5fb-0d022509a7f5 | -7.3102 | -43.530102 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f8c12fb-97e8-3de9-8fba-5f7a5c7e318a | -7.3119 | -43.537601 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d434efca-2a0c-30c8-8df2-b69d792f0418 | -7.297 | -43.5173 | 2024-10-12 00:23:56 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44f927d4-355b-3556-b507-82bc430a522b | -7.1611 | -43.8689 | 2024-10-12 00:24:00 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bac92529-571a-34ee-8be6-db9bfe33cb48 | -7.2209 | -44.130699 | 2024-10-12 00:24:00 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 30e8c1fc-57f7-342d-b42f-a528bd913bea | -7.2226 | -44.137901 | 2024-10-12 00:24:00 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b54454aa-4edf-3257-a285-5a99cb1ae88b | -6.5892 | -42.240501 | 2024-10-12 00:24:03 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4da90bed-41ad-3360-8443-672f4d54ba7d | -6.7015 | -43.036301 | 2024-10-12 00:24:04 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2fda14a-bc7c-3f87-90f9-22fbc99b0b41 | -6.7034 | -43.0443 | 2024-10-12 00:24:04 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d04778e-1df5-3534-9e7d-3ead57bf2701 | -7.9452 | -49.2943 | 2024-10-12 00:24:07 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c480382-ab44-30a5-b256-75fc8ce3fd38 | -7.0016 | -45.2076 | 2024-10-12 00:24:07 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77e73315-9f4b-39de-b42c-20cfc2db4e84 | -6.6408 | -43.848202 | 2024-10-12 00:24:08 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9de9900-a1cb-3850-9b4f-859d4bdc5f4d | -6.6425 | -43.855598 | 2024-10-12 00:24:08 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfb3f411-683d-3430-87f8-94b29068ad80 | -6.631 | -43.850399 | 2024-10-12 00:24:08 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0bbc1fa-22aa-3302-bf42-051ae52caae8 | -6.4903 | -43.686298 | 2024-10-12 00:24:10 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5a81d3-4d1c-3103-8384-087fa913b337 | -6.4827 | -43.743301 | 2024-10-12 00:24:10 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d04bf1a6-9626-349f-ad6d-03f02173fb3e | -6.4904 | -43.866901 | 2024-10-12 00:24:11 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd2767cb-1332-39c4-927a-d7a7e2a89aca | -6.4921 | -43.874298 | 2024-10-12 00:24:11 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbdc1e19-fad7-3540-912f-60c30b49d0c4 | -6.1673 | -42.688099 | 2024-10-12 00:24:11 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e6a63f6-19a7-324d-ab05-90bc8ace1289 | -6.1693 | -42.6964 | 2024-10-12 00:24:11 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| edbecd0e-4821-3cc6-b009-82af1e26bb3a | -6.5018 | -44.1422 | 2024-10-12 00:24:11 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e1dcba3-12eb-3896-ae6e-3b58f4c81970 | -6.5035 | -44.149502 | 2024-10-12 00:24:11 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3815019-5f65-3bb7-80d6-fbcd80742488 | -5.638 | -40.687599 | 2024-10-12 00:24:12 | METOP-B | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f6d0f0b1-f1c2-32fc-bb18-ad0e73479f7f | -5.6406 | -40.698601 | 2024-10-12 00:24:12 | METOP-B | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8c1b39e3-6fed-3743-8e38-a01286c58632 | -6.1576 | -42.690399 | 2024-10-12 00:24:12 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33dfbfe1-4ba5-308e-b907-fb488c023110 | -6.2977 | -43.746101 | 2024-10-12 00:24:13 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e22b354c-db43-34f2-9f99-0aa227546c3b | -6.2995 | -43.753601 | 2024-10-12 00:24:13 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd1767e1-f7ef-3f6b-b961-099ec50652f7 | -6.4564 | -44.259201 | 2024-10-12 00:24:13 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0dac1a4-07a7-3ea7-820f-9a0452bd1b59 | -6.3732 | -44.391399 | 2024-10-12 00:24:14 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84d102a8-a0e0-371a-99a5-db5c2348f35d | -6.3748 | -44.398602 | 2024-10-12 00:24:14 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d641b99-cdde-383c-8dc3-113dc85ba005 | -6.7156 | -46.4561 | 2024-10-12 00:24:16 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1100c3d3-5f40-3a54-9444-ff51921706a6 | -7.1162 | -48.313301 | 2024-10-12 00:24:17 | METOP-B | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a1ae2a93-a1dc-39b3-96e3-fb13ef2ea197 | -7.118 | -48.321098 | 2024-10-12 00:24:17 | METOP-B | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a759d6dd-6b16-321a-8015-4ec71e5b504e | -5.9339 | -43.328999 | 2024-10-12 00:24:18 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e92d227b-b80d-3ea2-b488-813aa442b33f | -5.9357 | -43.3368 | 2024-10-12 00:24:18 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4a40f61-7184-3580-ad53-e2f6de13a0aa | -5.8604 | -43.726898 | 2024-10-12 00:24:20 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 341cadbe-ffe4-3fc7-911d-80723a511e72 | -5.8621 | -43.734402 | 2024-10-12 00:24:20 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8229c0e9-f112-32a1-b219-d9e39cf8c8e1 | -6.0854 | -44.621601 | 2024-10-12 00:24:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
