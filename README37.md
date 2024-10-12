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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4731ece8-66da-36f0-9735-566099120537 | -10.96014 | -44.65274 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecd35a03-de1d-32a6-bd18-73da0dbb078b | -10.95957 | -44.65576 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcf7f8bc-3cef-3ef2-bde4-65be39d987c4 | -10.34237 | -44.36463 | 2024-10-12 03:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a96c1b7b-fae4-3ca2-bf84-93fa066b3a63 | -10.33734 | -44.3636 | 2024-10-12 03:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d10e1be-e1d3-3744-ab33-0ccf73de3535 | -10.73052 | -44.69774 | 2024-10-12 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d06b527-5576-3f1b-a2f8-986fc857206d | -8.7893 | -35.15026 | 2024-10-12 03:42:00 | NPP-375D | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30ba8ac3-e66f-3024-9a0c-c01b50cc95f5 | -8.38145 | -42.4534 | 2024-10-12 03:42:00 | NPP-375D | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cc0714c6-f053-3a79-8758-adf61e147e77 | -10.95563 | -44.64869 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2090a06c-3913-34ed-ad63-3314e4353cb3 | -8.31763 | -35.11899 | 2024-10-12 03:42:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a85ba553-3051-3ba1-bdf2-0e84ba357480 | -8.13442 | -35.46822 | 2024-10-12 03:42:00 | NPP-375D | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 963781ba-7378-3118-a71d-1839154d2ac4 | -8.07251 | -34.97619 | 2024-10-12 03:42:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5aa121ca-03bc-376a-9222-dfea54b4ed86 | -9.80217 | -36.49266 | 2024-10-12 03:42:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60dafa09-562c-36fe-be61-fc68f5a74a3b | -9.79695 | -35.99487 | 2024-10-12 03:42:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 790ed04d-969c-362f-8db7-9e13a735c821 | -9.7955 | -36.49157 | 2024-10-12 03:42:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb4974c6-51e9-39cc-a9a4-9aa0ed7f988a | -9.79363 | -35.99433 | 2024-10-12 03:42:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 11038e85-98c7-3ace-8f25-021c2fbb041f | -7.74653 | -36.96083 | 2024-10-12 03:42:00 | NPP-375D | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 67f09589-514f-3059-b6be-d84456e8f250 | -12.20576 | -38.24778 | 2024-10-12 03:42:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fda20057-ddc7-3f12-9d15-5201c5dfaa3c | -12.20233 | -38.24721 | 2024-10-12 03:42:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb38cb17-5562-31f4-9e30-829c2ce141d1 | -12.779 | -38.49813 | 2024-10-12 03:42:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f1a63c01-cbcd-3ea5-a3f5-68fedb3d48c9 | -10.06113 | -38.54999 | 2024-10-12 03:42:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8502e02-ee11-31de-baca-fbe014c5b0e6 | -10.06047 | -38.55407 | 2024-10-12 03:42:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f89e06b-2711-39b2-a811-a85e121a30dc | -12.84778 | -39.85545 | 2024-10-12 03:42:00 | NPP-375D | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99444d43-5f24-39e8-861a-72ef2519bb27 | -7.47041 | -40.21965 | 2024-10-12 03:42:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e6dbd3b-2e8d-330c-acb3-6fff200ec342 | -7.46982 | -40.22317 | 2024-10-12 03:42:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dbf74d73-84f2-3b0c-89ef-248d19665ce0 | -7.46581 | -40.22247 | 2024-10-12 03:42:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bb66d6e5-d1a8-3030-a4f4-ebd6dfbf9bc3 | -7.46179 | -40.22176 | 2024-10-12 03:42:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 040e8c4a-5d81-3fa3-89c4-a475e8037cab | -7.41938 | -40.44925 | 2024-10-12 03:42:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb4db434-6bf9-3374-a95a-2210b3a6bf62 | -8.77806 | -40.35573 | 2024-10-12 03:42:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4bc8b8c-23f1-3e80-ad14-449f71b2f8c4 | -8.77659 | -40.35295 | 2024-10-12 03:42:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bdb80c1-b69e-3ad8-ad0d-0d333224a83f | -8.42651 | -40.78738 | 2024-10-12 03:42:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d30147cc-b405-3bcb-9f3a-357b21828800 | -8.34833 | -40.68757 | 2024-10-12 03:42:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ff0683a-d671-35ad-81c6-2b1ae7932b49 | -8.14609 | -39.70396 | 2024-10-12 03:42:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f97f46a6-7455-3a79-bfff-37917fdbfd9c | -8.1117 | -40.80656 | 2024-10-12 03:42:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 72889102-8cdc-3b17-bef2-c4059bbd4ad2 | -9.29819 | -40.55286 | 2024-10-12 03:42:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d0598716-2e2e-30c4-8fcb-7dbdd28e6484 | -7.99257 | -40.97042 | 2024-10-12 03:42:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f48a66ba-ffc8-3388-808c-4ec45185e1ff | -8.23996 | -41.119 | 2024-10-12 03:42:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19b7ec78-4b38-33f1-a441-e8ac018a2c7c | -8.08226 | -41.08046 | 2024-10-12 03:42:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9a2f1d7-f61c-3c15-8f5a-92194266ef63 | -11.91374 | -41.67356 | 2024-10-12 03:42:00 | NPP-375D | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7a71a162-ce46-3971-862f-395ed9f22d7f | -11.91307 | -41.67732 | 2024-10-12 03:42:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c49e755a-0de2-349f-8e14-be4c5428f176 | -11.91176 | -41.67321 | 2024-10-12 03:42:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6feef857-fabb-349a-8142-e810e29ba1ab | -11.91111 | -41.67698 | 2024-10-12 03:42:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90d121cb-3003-3fdf-a1cc-04da0da725c9 | -11.21432 | -41.60735 | 2024-10-12 03:42:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1a9e2c1-f717-3386-8c2c-8be8fe7b007e | -10.83997 | -42.86445 | 2024-10-12 03:42:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2afa5017-0a32-35e9-8ce7-125fa1b188ce | -12.7767 | -43.30494 | 2024-10-12 03:42:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dfdb799-5704-3d3d-8001-3a0971bcdbf6 | -12.77586 | -43.30956 | 2024-10-12 03:42:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1046791c-1247-3564-bda8-657a4f054c3d | -9.26322 | -43.54242 | 2024-10-12 03:42:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 13d19d75-9ce0-391d-983f-4bfb90b8a45e | -9.26109 | -43.17056 | 2024-10-12 03:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cfde78df-4019-3582-be4b-f840f44212df | -9.26048 | -43.17323 | 2024-10-12 03:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7d46c05-3c09-3d72-8609-8df1fc99e092 | -9.6706 | -42.85969 | 2024-10-12 03:42:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6485e8f2-3652-3dec-9ef8-c1ae84befe65 | -12.28736 | -43.8368 | 2024-10-12 03:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05e57842-75d0-321b-a4f7-3e2eb9ab633a | -12.28658 | -43.83461 | 2024-10-12 03:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f8e2d0-a6b8-3410-bc84-7b7b0c32c245 | -12.24803 | -43.59616 | 2024-10-12 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65e2ace0-3bb6-3aa4-8c3d-7b63b724e2ba | -12.24712 | -43.60107 | 2024-10-12 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f3556ff-531a-3056-8204-295dfbd976e4 | -11.1071 | -43.33549 | 2024-10-12 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 805c26e2-1195-3bef-b0c3-4c7e35d66c32 | -10.84193 | -44.43774 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e640fd40-8995-39c1-878b-442bb102fae9 | -10.84138 | -44.44074 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63447d57-f365-3a89-9505-649d670af1e6 | -10.83692 | -44.43671 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb90af31-93c9-3f58-be58-6903a8f1da1d | -10.83637 | -44.43969 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8aaf9bfb-95c7-3dee-a238-59b6f3046c60 | -10.81376 | -44.30986 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1456d38-d828-379e-b30d-5297612ea3ba | -12.35838 | -44.05875 | 2024-10-12 03:42:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1158e054-48f1-3704-aa55-85eb8130d981 | -6.50115 | -44.14981 | 2024-10-12 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 105efa13-7662-3b66-9cad-a335c9f48eb5 | -6.5006 | -44.15286 | 2024-10-12 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8350a557-ed3a-3258-a035-ba1b3c8b3636 | -6.49832 | -44.14952 | 2024-10-12 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 738c44de-fb43-3f66-9392-12eac7043340 | -6.49778 | -44.15261 | 2024-10-12 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcb86f54-9a40-3988-b119-73635caf7e37 | -6.99848 | -45.2142 | 2024-10-12 03:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 305930e3-8a3a-33d2-89ea-bc7ee5aad8ca | -6.58324 | -44.1819 | 2024-10-12 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecc0cc4e-abb8-3550-9777-51641d53dbd8 | -6.57799 | -44.18056 | 2024-10-12 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa192c7c-3acf-367d-9626-b27ca1da1549 | -10.82436 | -44.94438 | 2024-10-12 03:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54203284-5ae6-3bff-8cb7-16db39452d13 | -10.82376 | -44.94756 | 2024-10-12 03:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 065aaf9d-bc60-388a-b0b7-abda503c43f3 | -10.73565 | -44.69869 | 2024-10-12 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7dde0f5-6a61-3211-9b0e-ed33102f20b2 | -10.95506 | -44.65171 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 13730ed3-6e57-3873-9c7d-d160ae439e6a | -10.95449 | -44.65474 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 210ef4b1-88ec-33f6-b656-42df7d31ab64 | -10.95391 | -44.65778 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 597c164f-7133-3f6b-8405-8baede491956 | -10.95112 | -44.64468 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 92e5d5ca-2538-388e-ac87-e171c63315bd | -10.95055 | -44.64769 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 809c6621-1fb3-3e16-a0d6-f5901a11440e | -10.94998 | -44.6507 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9d7465e-4231-32a9-acea-34d892819905 | -10.94941 | -44.65372 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbe132ba-659c-3f6e-91bc-b6ff1672827f | -10.94884 | -44.65675 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6082ec3-9394-3a9f-a4e1-0ea06eb75e43 | -10.94604 | -44.64367 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4803fe0a-12ec-3ad1-bc0b-580933a9b798 | -10.94547 | -44.64667 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65219583-d4d7-3338-8aa3-a10c7805657a | -10.9449 | -44.64969 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fb0bf84-6447-3f49-a5ee-f9d249adabd1 | -10.94433 | -44.6527 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31364eb0-4c02-3002-8ac7-b7bb885048bb | -10.94392 | -44.64291 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97a12725-8144-3b98-888e-2b2db7aec80f | -10.94337 | -44.64593 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b43e88d1-75f0-334d-916e-961677a378eb | -10.94282 | -44.64894 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb3c62f5-e4b0-3ca1-b6cf-b220d51e4a5d | -10.94227 | -44.65197 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41aec40f-3770-3ebe-b480-d9d313f3fa1a | -10.94097 | -44.64265 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71a13fe7-9ded-34dc-9d7c-07b7e9997616 | -10.94039 | -44.64566 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a83db106-78bb-3f4c-b06b-e8d557c7cbe7 | -10.93982 | -44.64868 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 829b7c58-6dde-3b6a-a84c-7ed64e172b2c | -10.93884 | -44.64189 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e60ee9e-5719-3e94-9a44-38bbd35f517e | -10.93829 | -44.6449 | 2024-10-12 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dce01b8b-eb4d-3c3b-aebd-8210a4b37cca | -12.34879 | -45.32168 | 2024-10-12 03:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc20fe26-274c-3be5-aa9f-0f7ba3db6d51 | -12.34236 | -45.32709 | 2024-10-12 03:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f14f474d-e678-383d-a89d-e4305cdd479e | -8.68103 | -46.58755 | 2024-10-12 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca20304c-d5b0-3aa1-837f-22f192e73fcc | -8.68017 | -46.59206 | 2024-10-12 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 640dafa5-7489-3c39-a5a4-6acb486d2715 | -9.31654 | -45.90744 | 2024-10-12 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 321299df-14c9-3fa2-9224-10126417402c | -9.31582 | -45.91119 | 2024-10-12 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a119b745-8b62-3b4e-9293-96b01bde36a7 | -9.31462 | -45.90823 | 2024-10-12 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bbd8a08-44a0-3653-a015-290c6f93d611 | -9.31393 | -45.91199 | 2024-10-12 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eabf9360-5078-38bd-8135-48855dc2c436 | -9.31011 | -45.91027 | 2024-10-12 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README38.md)
