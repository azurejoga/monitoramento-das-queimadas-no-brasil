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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d14ebb74-95e7-3e18-938a-2c271502556b | -10.14371 | -45.76043 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ed8e072-68c9-3f09-8cea-3fdb867d8e25 | -11.16185 | -45.04648 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be0e74d6-e5bf-3f48-b361-5e8b30ac66de | -5.61118 | -44.0076 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c20bcd2-279e-3e2c-9c48-1239dd1a48b3 | -12.09647 | -45.04319 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8263e45-9dd8-321d-85c6-ca2f7bc16b8d | -7.20843 | -42.7401 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d461b1b-50e6-3716-ae9a-e9c841289f68 | -11.69276 | -47.60656 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7307cda9-1f37-316f-bdce-8fef474e0bff | -7.6939 | -39.34692 | 2026-08-31 04:14:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| baa05890-3e4b-3fa4-b444-7f792267c949 | -7.21725 | -42.77033 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a676ad7-4d84-302e-9646-de151fab461f | -11.23219 | -45.09422 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 63b4d4d3-cc61-39d1-9137-73a649ef1507 | -9.42989 | -45.68244 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cff2f0d8-c751-3bae-96ca-adf409b4404a | -12.08123 | -44.9861 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76acdd62-0420-315d-b244-ba435b170908 | -6.94876 | -55.70111 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 20fff8fc-ffed-35e1-aa2a-a317ee299e10 | -10.73864 | -54.04076 | 2026-08-31 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33d2e8ba-4535-3b41-a920-10bd359557a8 | -7.09376 | -42.8405 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bc1ab62-9c0b-3e38-994b-4d733ce079e0 | -11.20818 | -45.33309 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e6e674-0770-336b-a285-422e2403522c | -11.67696 | -47.60642 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a7abcea-21a5-37e8-8499-ffc7aa7e3770 | -7.91729 | -44.25153 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c150fd9-774a-39f8-b23f-7782e1e2a9dd | -7.73879 | -44.7385 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 98e74a9a-2158-3338-9329-d4e863045245 | -9.19156 | -51.55943 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b0b0aa6-7a04-3866-9580-7842fa955f30 | -11.21234 | -45.32975 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c287cb7-b737-3708-9f51-da3cf75f0d8d | -10.81453 | -45.34249 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c68a265-5cb6-3216-8d5c-91c4481d3f5e | -7.97982 | -44.28129 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5179ba50-89ca-3ea6-bd1a-ab1be0019adb | -11.33987 | -45.198 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ef90314-9f5c-3087-8f1f-621972db600d | -6.86835 | -41.6951 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63b8878d-7694-3a58-92b1-a9ab5ad1a487 | -8.0775 | -45.4728 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2446391e-9e58-3e0b-95cb-92798d80e389 | -11.21898 | -45.08799 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca183b79-394d-3b1f-bbdb-47983d4e5963 | -5.45144 | -42.65447 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b24fa65-f575-30ab-ab00-d78425f9eb09 | -7.06316 | -52.72097 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bb1ae5f-4bf0-3bcd-a71a-e152b2249798 | -11.04794 | -47.1237 | 2026-08-31 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39f1de42-2fa2-3ae9-867c-60cedce45351 | -7.05724 | -52.71986 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6958c684-4f77-32b7-89e6-973fc213c3c3 | -11.78742 | -47.66626 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cac0c71a-9d18-347b-8508-76d0f38717d3 | -12.13841 | -45.83951 | 2026-08-31 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 202e65da-0c75-3397-adab-9b4bec00765b | -11.36223 | -45.21375 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fc31fcd-e4b8-3c0e-a142-fe83db5fad7b | -6.85288 | -41.6643 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6306d33d-417e-374d-a482-fbef8adbcf8d | -8.6094 | -54.7838 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6aa0cc1d-98b0-382f-bdb8-b2dc2d5adc41 | -7.94155 | -44.29825 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 704e0a3e-32fd-3fbb-b7f4-9338344d90a4 | -6.91408 | -55.72929 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b9f797a1-0311-3f64-97d4-d44ca364ab07 | -10.81425 | -50.65919 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72866b07-751e-32c4-aae4-1f2cf760cf5f | -5.87511 | -52.15443 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26dc8927-5054-3cdb-a6f5-15b3a4afac18 | -11.88074 | -45.81737 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c3616c8-da0d-311d-8f0d-59f139d661a8 | -10.75991 | -50.8558 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcd2694c-5d8a-3590-a2ec-564f1d222498 | -11.79222 | -47.66182 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 476d042b-b125-3ba0-b9cc-b6d1cd8485b9 | -9.57846 | -47.61327 | 2026-08-31 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbf5e6ca-0e30-377b-87db-4c0c75916d61 | -8.21051 | -54.94548 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a289c88-60e7-31d2-bba3-a18407523202 | -11.07512 | -51.5174 | 2026-08-31 04:14:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea6cc9ff-d328-31e2-a383-4d4ed0f22afd | -11.9171 | -45.0639 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d68760-4997-38a7-8e31-5c6caecf4404 | -5.59783 | -44.0015 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 442910c0-bfa5-3fa3-8081-adaba1e2d6ac | -11.36312 | -45.22975 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee28ef72-0fba-3012-8c88-c87bdd3ae937 | -10.15734 | -45.72259 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e9c895-401a-36b8-839a-cd9720718fa6 | -6.8447 | -41.71612 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0f59bfc-cde2-3194-9aa3-dd09e35f6e86 | -6.919 | -55.7224 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c97deae9-a76a-3ee9-b911-31e34bee9aea | -8.3877 | -46.47419 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1442b3f-6700-3b94-8f77-62feb799ee75 | -7.69436 | -39.34637 | 2026-08-31 04:14:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 126cf62a-7f75-32b9-86cb-ce545aad1409 | -7.2949 | -46.18272 | 2026-08-31 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd86ba7d-3875-3ad5-9969-36dcbaffc297 | -11.20691 | -43.38116 | 2026-08-31 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 94cf7f54-c6c8-3329-9ed9-4b05e6f15087 | -9.41973 | -45.6545 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 857c965f-5470-3f0d-9a8c-bf34d039133f | -11.26091 | -45.06192 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7149f10e-f4f7-3820-9931-8dcb61b6e8d5 | -6.94746 | -55.70801 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6d77cd3b-f5a0-34b4-9ce0-0011436788f3 | -6.48661 | -43.71147 | 2026-08-31 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 921c1188-63d8-32ba-9eb4-bea56f95e37a | -11.22182 | -45.09239 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51af53e0-2dc2-37a8-a383-b539bc640438 | -7.6125 | -44.88761 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e140af8-9f0e-3893-b888-7def0b8f163b | -7.79036 | -43.9569 | 2026-08-31 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 474acf0c-d77f-34cf-8aba-1894a308d506 | -9.58251 | -47.61399 | 2026-08-31 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d5e5247-4517-3cc5-ab65-b11ea30157a8 | -10.73285 | -44.88135 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26b0e41b-d4bd-3a9f-b57e-daaf44dab8f6 | -7.52736 | -55.34528 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01d5fbb0-b19b-34c3-b5b7-168ae762c4ed | -8.20927 | -54.95192 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 529f0d1e-16ff-3654-83ca-ffc94673ef26 | -6.43858 | -41.53487 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39a1b587-93dd-3143-b635-cc95ae085c2d | -11.1625 | -45.04264 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8df2a521-d03d-3e82-be96-1b94fde76862 | -11.34117 | -45.19029 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5c720d0-4c52-3957-9889-c8c36deb0af7 | -11.32828 | -45.19252 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb66488c-2125-34f5-8b69-2f277773bd85 | -7.07662 | -42.22511 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c27e063a-5046-3c0f-ab09-570066765024 | -11.33081 | -45.17714 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 008f5a5c-83bd-31ed-8ccb-9e84f484860a | -8.14483 | -45.51803 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f4ebfbe-7f7b-3469-932c-f5bd88b51518 | -11.68023 | -47.60892 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ef0e3a5-8b19-31ed-b3e3-9b2f08228ab6 | -6.93645 | -55.63337 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 071dc556-18b2-30c8-9d50-db97b799165a | -7.03689 | -42.19743 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9686a5a-4d1d-327b-9e41-a8c04b60981e | -9.43565 | -45.67041 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3250bc5-c796-3240-8759-34f2e7e226ab | -5.58556 | -42.3296 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cd28d64-1c70-3f86-a053-c77764133cb9 | -11.36417 | -45.2021 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e574a0cf-82d3-38d1-970c-ae97e2a96d92 | -7.95404 | -44.26533 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8402d678-f18f-3449-a5f7-851ca7526d6b | -11.15428 | -45.04923 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4038d95-71f7-3a83-a1cb-1fd61851815c | -7.523 | -55.33076 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e73be94-3a2a-3011-93a7-bab483b61020 | -11.37615 | -45.21592 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 88914a3f-1d40-3d40-aa24-0fe0bf742ea9 | -6.94416 | -55.70643 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8d677ab2-fd65-32f6-b7e8-f93cd0b669f0 | -10.7963 | -50.51057 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2b46f98-15f2-3176-99ad-ef4d298485ac | -11.3477 | -45.21514 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 1d5df224-1641-37cb-b4a1-a8714e78a992 | -7.62284 | -55.29346 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b661ac3f-29cf-3f24-9ce9-7d8aa2587117 | -10.0109 | -46.39754 | 2026-08-31 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea6cb3e0-e8f4-310a-b2f6-e60db2e8d983 | -11.37087 | -45.18339 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0aeb6dd-9188-3b11-9f1a-b267767108c6 | -6.95252 | -55.70116 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ec655a9-f1d4-395d-b9e3-e63c17c83b3f | -11.20078 | -45.069 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db30bacb-211b-361d-9a07-2bdd12df171e | -8.08261 | -45.4646 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f142e0e-7648-357d-8fa6-79f794a3b899 | -7.93518 | -44.25058 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b8cb53e-5b9b-3bf4-8017-1f2bf0de0054 | -7.91515 | -44.28602 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc427092-da5f-3926-bf38-9b17a8a3204e | -11.20677 | -45.05424 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee0a09e4-a843-3dfc-9b91-45c21a004c77 | -11.33704 | -45.19358 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48116dd6-976b-302f-a09e-e2256c427509 | -8.12443 | -45.50554 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61d5723e-5c1d-3d20-883d-ff119779e35c | -11.83023 | -46.75978 | 2026-08-31 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2c9e173-39c9-3d60-a02d-961f34aa2096 | -11.91616 | -45.04838 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed2ceb18-7a76-319a-af50-0b8f04309bf5 | -11.34899 | -45.20747 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README29.md)
