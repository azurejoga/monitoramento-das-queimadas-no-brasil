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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a40b6ed-5b6d-3a9d-b9b8-c749251da935 | -14.1932 | -45.1606 | 2026-09-18 16:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 75aa23eb-7c8e-3801-bd7e-afab423d5a76 | -14.1542 | -45.1675 | 2026-09-18 16:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 653.0 |
| 283fdb37-3977-3b8a-9a05-c4d76f106141 | -11.064 | -48.2898 | 2026-09-18 16:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| d9c67be9-8ae6-3ce6-b026-0cb80788fefe | -12.126 | -44.2225 | 2026-09-18 16:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8e4f9d3b-be8f-3d6f-8c81-63a9400d426d | -0.803 | -48.6825 | 2026-09-18 16:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d97fe692-89da-38fd-a24f-d7b947042191 | -0.803 | -48.6611 | 2026-09-18 16:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8ed023a0-261d-36e8-9ed4-c063482c3f2b | -11.3437 | -44.0141 | 2026-09-18 16:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 4ecd3dd8-5e61-3bc9-848f-4c782caccebc | -11.3442 | -43.9906 | 2026-09-18 16:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 80bd370b-2f56-37e3-ab02-8175c2872e00 | -11.3809 | -44.0788 | 2026-09-18 16:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 331.7 |
| 44fa69bf-a259-3928-9536-885ba4f1aa20 | 1.2794 | -50.8718 | 2026-09-18 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 910fb51b-b197-38f8-b7a5-3562d7b50308 | -14.1742 | -45.1407 | 2026-09-18 16:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 8b553b1b-88ba-3678-bdd6-1cc01498a9a4 | -7.8036 | -44.8422 | 2026-09-18 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e10678f7-a07a-358c-8227-469223d97220 | -9.9512 | -45.2902 | 2026-09-18 16:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 4af11b00-7b31-3ebf-9fff-0d31e0b74db2 | -7.85 | -45.18 | 2026-09-18 16:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89ecfb95-4cfb-3762-9cb1-2ed5e2565666 | -10.82 | -50.2 | 2026-09-18 16:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c985b103-59d9-385f-81a8-a153ddbef3d4 | -10.9 | -50.83 | 2026-09-18 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c852dfa-0cfc-3ca7-a3ee-f497c6dd3b50 | -8.6377 | -44.4798 | 2026-09-18 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ce7ddffa-d3f2-3477-8046-ddf60ff31cfa | -11.3809 | -44.0788 | 2026-09-18 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| f1e6fd5c-5840-31b6-bfd8-a07bb64c1818 | -7.8033 | -44.8651 | 2026-09-18 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 0a123af6-06e3-33a2-90f9-b70caaebb0bb | -11.3442 | -43.9906 | 2026-09-18 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 5d2c3736-2fcc-3bf2-b47c-da22439301f2 | -7.803 | -44.888 | 2026-09-18 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a3827fe7-2022-3e19-81a1-63866d4b97f7 | -0.803 | -48.6611 | 2026-09-18 16:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b6cdbef9-edc5-3bed-8ce9-9d46c8b808e5 | 1.2794 | -50.8718 | 2026-09-18 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 3a5a43cc-f68b-3709-b8df-e200b7118213 | -14.1737 | -45.1641 | 2026-09-18 16:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 228.0 |
| 18bd2a9b-d73c-3661-9268-bcaba6a1a08e | -15.2859 | -53.9037 | 2026-09-18 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fbf320da-d21b-3721-af82-1fb3230c6b49 | -0.803 | -48.6825 | 2026-09-18 16:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ca71e157-48fc-3b74-8e70-1bb6d557140b | -11.3433 | -44.0376 | 2026-09-18 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 376.2 |
| 8fe125f0-2d71-3c70-b746-96c4c65b409e | -11.3437 | -44.0141 | 2026-09-18 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 5f67b0b9-9607-3c0f-9a17-68c1d0f4d343 | -11.064 | -48.2898 | 2026-09-18 16:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4a60d30e-a96b-3f97-bd1d-a7dbcef6177b | -14.1742 | -45.1407 | 2026-09-18 16:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| ce6f9956-1539-3c85-b3ef-5600d5650dd2 | -10.1168 | -45.6346 | 2026-09-18 16:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9dffaf13-473d-3f31-aedb-9754c711548e | 2.2003 | -50.8773 | 2026-09-18 16:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 18c48ac5-e170-3edb-9e21-cf26228fa932 | -11.3437 | -44.0141 | 2026-09-18 16:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 417.9 |
| 43d3dc74-dd0d-3bbf-99ac-bea10625c9d4 | -0.803 | -48.6611 | 2026-09-18 16:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| ec54032e-8323-3093-8843-03152c2500a0 | 1.4082 | -50.8909 | 2026-09-18 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1fa3802a-b46d-3c01-8b86-cb0daf7bdabb | -0.803 | -48.6825 | 2026-09-18 16:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d6f587ad-bd20-3239-b208-c08fee85503b | 1.2611 | -50.7679 | 2026-09-18 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.9 |
| a01d98c4-74e6-3721-91e1-2e562e89570c | -14.1742 | -45.1407 | 2026-09-18 16:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| d4f473ed-a778-3056-98d9-d003d071323c | -11.3442 | -43.9906 | 2026-09-18 16:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 274.5 |
| 29ff9f46-d55f-33b4-b1f4-1f2163edb53a | -11.3809 | -44.0788 | 2026-09-18 16:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 3c3a46c1-4b68-34a5-9d66-72d3ae250d7b | 1.2611 | -50.7679 | 2026-09-18 16:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.5 |
| fb5724d8-5cf9-31a6-94c5-933517312326 | -14.1932 | -45.1606 | 2026-09-18 16:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 74f5e5c8-4be3-3540-be6f-8e6cafbba850 | -0.803 | -48.6611 | 2026-09-18 16:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0449a892-03c2-35cf-b58f-07d5d6d61d05 | -0.803 | -48.6825 | 2026-09-18 16:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 2c4c1e0f-b179-3bd4-bacd-bdebd9502322 | 4.2971 | -60.9501 | 2026-09-18 16:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 50341e5f-2c14-3973-8d2f-d6d72f2d4011 | -10.7546 | -46.1667 | 2026-09-18 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |


