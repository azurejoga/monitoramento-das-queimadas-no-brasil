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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cc63efb-e52e-330c-aa1b-2c80a46463a0 | -5.65827 | -43.89857 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00766251-30ac-36b4-ba3d-6173472981a3 | -4.33157 | -48.39362 | 2025-09-11 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b9535c-697c-3df3-adf8-24e0e50ee3aa | -4.89454 | -45.19409 | 2025-09-11 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88274ee1-d692-3880-a042-b32957d95180 | -5.35553 | -43.40475 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d8a4f9d-ea49-3b83-9d8b-4fd7b850d678 | -5.52522 | -44.35136 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d957338-fb05-332a-8fd3-92f8f1f927e7 | -5.1996 | -45.72248 | 2025-09-11 03:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18e2e93f-539b-38ca-972b-e36aeb70045f | -3.63466 | -49.20345 | 2025-09-11 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8734d5ec-c401-3d5f-b6e9-6c4a5fc076e1 | -3.79535 | -51.16008 | 2025-09-11 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 70984bd0-2086-3d27-86fd-020683285077 | -3.60575 | -42.85886 | 2025-09-11 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fe1eb60-2a4e-37aa-9b74-fdd1732b498a | -3.79613 | -51.15736 | 2025-09-11 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| df2fe070-bfc1-3d5b-8f7b-1ea872f2ae09 | -5.24163 | -45.46172 | 2025-09-11 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22d9bcf6-50d1-3671-a926-1e1df76e8183 | -3.05783 | -41.22324 | 2025-09-11 03:53:00 | NOAA-21 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c0c43e8-19cd-365a-bf0e-b0aa1aaa158a | -2.43885 | -47.33263 | 2025-09-11 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 040afd35-e69b-3e3a-8fbd-162121a33a2a | -2.44004 | -47.32926 | 2025-09-11 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f3274b-38ab-361f-b426-40e6bc345340 | -5.66788 | -43.89226 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8068b1d-7419-30c3-bfa6-e5d6d529f817 | -4.94789 | -37.63583 | 2025-09-11 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f4d03d9a-c87e-3222-aced-ce07dd811fd5 | -4.71114 | -47.23417 | 2025-09-11 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a934bdd9-1c7f-3d87-b096-224929eb107d | -3.35269 | -39.27815 | 2025-09-11 03:53:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d9e0a4e2-f27a-357d-97a6-b40699409977 | -3.24797 | -50.79895 | 2025-09-11 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 477eb257-5b0a-3e58-a191-2a0d85869de8 | -5.52952 | -44.35209 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e71f4e5-0d67-3383-ac69-0d344814c0fe | -5.67269 | -43.88905 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 051e8943-d187-31f3-9afd-6c5ec7b7d1f0 | -4.11453 | -38.33309 | 2025-09-11 03:53:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c87d5c0-5818-330b-b228-738ff9128e71 | -3.24583 | -50.80099 | 2025-09-11 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9932d5b2-9063-3c59-8b42-3264a3c19da4 | -4.56357 | -43.74293 | 2025-09-11 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e8dc882-9fd8-3c51-ad84-c78456108209 | -5.22753 | -43.69674 | 2025-09-11 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b15364fa-b5f3-3ced-b448-f8bccf45b9cc | -5.47561 | -43.43901 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd27241e-40e1-393d-8a1a-f33bb283e0ed | -5.48927 | -42.6494 | 2025-09-11 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 35891f0e-1e28-389e-9c80-34f3ae6562cd | -2.43944 | -47.33297 | 2025-09-11 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73972876-ea6d-3bdd-aeb3-469933d99bd6 | -5.45681 | -44.34958 | 2025-09-11 03:53:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f66d5ae-e7aa-3025-b942-0c4b8743b3cd | -3.73754 | -49.04343 | 2025-09-11 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79aeacdf-4b2e-37ff-b7d8-9e3843090341 | -5.35957 | -43.40548 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21934e48-2ed8-3c71-a3ec-dc31c0fdab58 | -5.6541 | -43.89793 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbbbe06c-0b25-3ba8-9645-a10185d21e78 | -5.80351 | -35.54424 | 2025-09-11 03:53:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b92f874-bf5c-38e5-96b1-6928e163fd50 | -3.79639 | -51.15411 | 2025-09-11 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4c69a490-74bc-39ea-8a94-5bccbcbe8d2e | -5.54515 | -43.04909 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ace8d4bc-9d8b-3ae1-9e2a-923a9fa936a5 | -5.56092 | -43.05182 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20b923d3-e7a2-3943-9b88-71e4b395d4dd | -5.08353 | -44.24977 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dfde433-ad81-3753-9710-6aac89889962 | -5.52844 | -44.34448 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06705e09-b580-3a7d-bdda-0c32d6ea17dd | -5.47501 | -43.44262 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56468e73-bea0-382f-bb89-9bb07682b8a5 | -3.96402 | -38.87756 | 2025-09-11 03:53:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4025d2fa-0e8f-3c68-83e6-4b7180919ad1 | -4.33086 | -48.39767 | 2025-09-11 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 832dfdbd-cbc1-38ed-bfda-32d0d9d01861 | -4.55872 | -43.74611 | 2025-09-11 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e7dfa1d-1232-3a50-a603-bac10b03596e | -5.359 | -43.40902 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5e42110-4906-323c-96b9-1553a2fcb4bc | -5.28289 | -44.19683 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd7807d1-2167-3384-a95a-fe81edf5151f | -5.57122 | -43.43953 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33f74a25-8092-3722-9c62-c9868b76b5b0 | -5.19847 | -45.7243 | 2025-09-11 03:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2fdb852-d91a-322f-b0ef-2cd51c4f8774 | -4.96403 | -43.22359 | 2025-09-11 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef09734f-87c1-373b-bfb9-e8b28c5098d0 | -5.23532 | -45.45938 | 2025-09-11 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9080394-3217-3dae-be42-bb20671606db | -3.66525 | -43.08871 | 2025-09-11 03:53:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c88045da-6c5c-3ef1-a112-1ad8e0fb7998 | -3.6807 | -47.49815 | 2025-09-11 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b122d8-26bc-3b8a-922c-b093f806b67f | -5.55697 | -43.05114 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831ab200-7c53-3f1f-940d-b7a27cc8d0cd | -3.6813 | -47.49454 | 2025-09-11 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16079dde-88ae-3ab1-b326-efa10985289c | -5.12666 | -44.67341 | 2025-09-11 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 625a8a6d-56fe-31d6-811e-965408826c6a | -12.02041 | -47.57801 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d3b5091-a46e-3427-8977-70750f497230 | -9.80849 | -47.75759 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b87b9647-53fd-3fb5-a2c1-a48fbedd1f9e | -13.16239 | -45.27891 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37ec5540-74fb-3fcf-b5ff-58c08507389c | -8.07858 | -50.18311 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8678d038-96d0-3478-8503-2b25d05ade9a | -6.90856 | -44.55544 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5be49f8a-7277-3aa7-83ac-0bdade4091b5 | -9.29795 | -48.42331 | 2025-09-11 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 875ca434-2f2c-393a-8079-117561ff40af | -7.53513 | -44.67335 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d77a6472-c76a-3b85-9305-9fff1ea6d382 | -11.38081 | -43.51903 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23499467-23dd-3af3-9a8f-c573fca4283c | -12.56818 | -44.63873 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 13b06d09-452d-336a-8103-cb66014ce552 | -11.02356 | -44.65068 | 2025-09-11 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5f0b84c-9b50-31f7-ba59-243118c41050 | -11.46035 | -43.60176 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8e8b09df-3104-351f-97ca-9fd5b724222c | -7.18994 | -44.96154 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7f7545d-eae3-3e84-a0d2-b64de09f4ac3 | -6.36898 | -45.16579 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5386d30-2313-31dd-a2fd-a1ca1c6bb381 | -7.91908 | -44.87339 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4dd5040-a3fd-3771-9852-e257884fc09a | -11.1613 | -52.03825 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b3ea304-05bb-357f-b372-1bf2c90284e0 | -8.16475 | -46.09005 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e557ca32-4c16-3824-bcc8-dbe7c83430d1 | -7.29743 | -45.17888 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15ff006-5299-38e8-a331-27c463f7f26b | -7.46966 | -45.28102 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78e848af-c1dc-31e2-bcae-16c0bc488bc0 | -12.55331 | -44.65489 | 2025-09-11 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0da29b5d-e23e-3a21-9f99-7157d2ac4748 | -10.39065 | -50.52371 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf735cb6-6fd4-396b-97f5-991fb12750ae | -10.38865 | -50.51694 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4d555515-1928-35e4-9aee-d409fca56ef7 | -11.72354 | -50.63632 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 99d64bde-74d9-3ca5-b6a2-029222a0245e | -7.3926 | -47.37159 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe755e19-82c2-3c06-b7a9-3714fd7a7ddb | -9.07167 | -47.04346 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 273f42f5-a290-324c-ac73-eb659f63bdd8 | -8.65596 | -45.72741 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77a61fc2-2ce1-3a94-9ae3-2cd3fa89952e | -11.41479 | -43.61438 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 056d5695-2a84-33d1-a872-2f69cdccbb90 | -11.45819 | -43.59188 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ed64a8f-9dc0-35e8-8fe4-853ea6b302e8 | -11.10753 | -48.42883 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86dbedf9-d547-36ea-a075-99e276a089f1 | -6.21378 | -43.36937 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9c7826d-9af6-3ac2-8bb1-344de4cdd441 | -8.02093 | -48.64885 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 065e2ac8-368a-3e45-acd3-308e527f4385 | -9.34216 | -48.94929 | 2025-09-11 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a7a9108-cecc-3aad-83ef-74240b0a4dd8 | -11.03682 | -46.03804 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46cd4c29-e80b-3e4a-9354-fe006856afe3 | -11.69808 | -48.26266 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 695dbc88-5ba1-3af8-80a8-12f7bf8de07a | -9.90652 | -49.91098 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42ec7793-e5a3-3581-8493-9cbc5312ace3 | -5.85088 | -44.17628 | 2025-09-11 03:55:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8f25bc8-0f37-39ce-b8b0-a79210b2d73e | -9.02541 | -49.78037 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ccced02f-5208-3ff5-b54a-9ceda5e777cc | -9.12224 | -46.19641 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f0a9177-551e-373f-b0aa-32bb57355160 | -10.38554 | -50.51806 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16ad99da-f1ca-3695-863f-f07f43db967b | -6.83527 | -45.59167 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1757ea0f-2a3e-3255-90de-f105cc6c8b3f | -11.38673 | -43.52945 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52e4bff6-0df7-3157-ab65-129b3da0930e | -9.02701 | -49.77196 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4fea3482-694e-37d7-8bb9-a67b21a57e66 | -11.10297 | -48.44437 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 613d9fec-4175-3c25-94e3-db19aabf9b79 | -11.33973 | -46.47653 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f387a560-8edb-3425-a13f-b40507ba267d | -7.36855 | -47.41851 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 299d28e4-c995-3d44-8265-e9c9c3e89629 | -8.66051 | -45.72781 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0defbb04-f7a7-32ca-b918-c1c945cd5691 | -6.41309 | -44.39704 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8cdff23-d8ec-3c17-8f63-05f6bb75f7b3 | -5.81151 | -45.68112 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README14.md)
